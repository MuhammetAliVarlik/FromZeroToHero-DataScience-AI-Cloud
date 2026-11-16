#!/usr/bin/env python3
"""Check which parts of the course this machine can run.

Run:  python tools/env_check.py

The script uses only the standard library. It reports Python, uv, R, Docker
(and GPU access inside Docker), the NVIDIA GPU and CUDA toolchain, Kubernetes
tools, RAM and disk. Then it lists the GPU features that the course uses and
whether this GPU supports them.
"""
from __future__ import annotations

import glob
import os
import platform
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OK, WARN, MISS = "✅", "⚠️ ", "❌"


def run(cmd: list[str], timeout: int = 60) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout + p.stderr).strip()
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return 127, str(e)


def row(status: str, name: str, detail: str) -> None:
    print(f"  {status} {name:<22} {detail}")


def version_of(cmd: list[str], pattern: str = r"(\d+\.\d+(\.\d+)?)") -> str | None:
    code, out = run(cmd)
    if code != 0:
        return None
    m = re.search(pattern, out)
    return m.group(1) if m else out.splitlines()[0]


def check_python() -> None:
    print("\nPython & tooling")
    v = sys.version_info
    row(OK if (3, 11) <= v[:2] <= (3, 12) else WARN, "python", f"{platform.python_version()} "
        "(course target: 3.11-3.12; `uv` downloads it for you)")
    uv = version_of(["uv", "--version"])
    row(OK if uv else MISS, "uv", uv or "missing -> pip install uv  (or see https://docs.astral.sh/uv/)")
    r = version_of(["R", "--version"], r"R version (\S+)")
    row(OK if r else WARN, "R", r or "missing (needed only for M05/M06)")
    code, out = run(["jupyter", "kernelspec", "list"])
    kernels = re.findall(r"^\s+(\S+)\s+/", out, re.M) if code == 0 else []
    row(OK if kernels else WARN, "jupyter kernels", ", ".join(kernels) or "none found")


def check_docker() -> None:
    print("\nDocker (databases, Kafka, Kubernetes, observability, Ollama)")
    v = version_of(["docker", "version", "--format", "{{.Server.Version}}"], r"(.+)")
    if not v:
        row(MISS, "docker", "daemon not reachable -> start Docker Desktop / dockerd")
        return
    row(OK, "docker", v)
    cv = version_of(["docker", "compose", "version", "--short"], r"(.+)")
    row(OK if cv else MISS, "docker compose", cv or "missing")
    code, out = run(["docker", "info", "--format", "{{json .Runtimes}}"])
    has_nvidia = "nvidia" in out
    row(OK if has_nvidia else WARN, "nvidia runtime", "available" if has_nvidia else
        "not configured -> install NVIDIA Container Toolkit (GPU containers such as Ollama run on CPU without it)")
    code, out = run(["docker", "info", "--format", "{{.NCPU}} CPUs, {{.MemTotal}} bytes RAM"])
    if code == 0:
        cpus, mem = out.split(" CPUs, ")
        row(OK, "docker resources", f"{cpus} CPUs, {int(mem.split()[0]) / 2**30:.1f} GiB RAM")


def gpu_features(cc: float) -> list[tuple[str, float, str]]:
    return [
        ("CUDA kernels, Triton", 7.0, "M20, M38"),
        ("FP16 Tensor Cores (not GTX 16xx)", 7.0, "M20, M35"),
        ("vLLM (small models)", 7.0, "M36"),
        ("bfloat16 training", 8.0, "M20, M27"),
        ("FlashAttention-2", 8.0, "M38"),
        ("FP8 (E4M3/E5M2)", 8.9, "M20, M35, M38"),
        ("TMA, wgmma, FlashAttention-3", 9.0, "M38"),
        ("FP4 / NVFP4", 10.0, "M35, M38"),
    ]


def check_gpu() -> None:
    print("\nNVIDIA GPU & CUDA")
    code, out = run(["nvidia-smi", "--query-gpu=name,memory.total,driver_version,compute_cap",
                     "--format=csv,noheader,nounits"])
    if code != 0:
        row(WARN, "GPU", "no NVIDIA GPU visible: GPU lessons will be slow or must use free Colab/Kaggle GPUs")
        return
    name, mem, driver, cc = [x.strip() for x in out.splitlines()[0].split(",")]
    cc_f = float(cc)
    row(OK, "GPU", f"{name}, {int(mem) / 1024:.0f} GiB VRAM, driver {driver}, compute capability {cc}")
    nvcc_path = shutil.which("nvcc")
    nvcc_v = version_of(["nvcc", "--version"], r"release (\d+\.\d+)") if nvcc_path else None
    toolkits = sorted(glob.glob("/usr/local/cuda-*/bin/nvcc"))
    newest = None
    if toolkits:
        newest = toolkits[-1]
        newest_v = version_of([newest, "--version"], r"release (\d+\.\d+)")
    if nvcc_v and newest and newest_v and nvcc_v != newest_v:
        row(WARN, "nvcc", f"{nvcc_v} on PATH ({nvcc_path}) but CUDA {newest_v} is installed. Put it first:\n"
            f"{'':28}export PATH={os.path.dirname(newest)}:$PATH")
    elif nvcc_v:
        row(OK, "nvcc", f"{nvcc_v} ({nvcc_path})")
    else:
        row(WARN, "nvcc", "missing (needed only for M38 custom CUDA kernels)")
    print(f"\n  GPU features used in the course (this GPU: compute capability {cc}, {int(mem) / 1024:.0f} GiB):")
    no_tensor_cores = "GTX 16" in name           # Turing GTX 16xx cards have no Tensor Cores
    for feat, need, mods in gpu_features(cc_f):
        status = OK if cc_f >= need and not (no_tensor_cores and "Tensor Cores" in feat) else MISS
        print(f"    {status} {feat:<30} needs >= {need:<4} used in {mods}")
    vram = int(mem) / 1024
    hint = ("<= 1B parameters in fp16, <= 3B with 4-bit quantisation" if vram < 6 else
            "<= 3B in fp16, <= 8B with 4-bit" if vram < 12 else "<= 7B in fp16, <= 30B with 4-bit")
    print(f"    ℹ️  LLM size that fits in {vram:.0f} GiB VRAM: {hint}")


def check_k8s() -> None:
    print("\nKubernetes tools (M32, M37)")
    for tool, args, hint in (("kubectl", ["kubectl", "version", "--client", "-o", "yaml"], "https://kubernetes.io/docs/tasks/tools/"),
                             ("kind", ["kind", "version"], "go install sigs.k8s.io/kind@latest  or  https://kind.sigs.k8s.io/"),
                             ("helm", ["helm", "version", "--short"], "https://helm.sh/docs/intro/install/")):
        v = version_of(args, r"(v?\d+\.\d+\.\d+)")
        row(OK if v else WARN, tool, v or f"missing -> {hint}")


def check_system() -> None:
    print("\nSystem")
    try:
        mem_kb = int(re.search(r"MemTotal:\s+(\d+)", open("/proc/meminfo").read()).group(1))
        mem = mem_kb / 2**20
        row(OK if mem >= 15 else WARN, "RAM", f"{mem:.1f} GiB" + ("" if mem >= 15 else
            " (start only the Docker profiles you need; Spark/Ray lessons use small data)"))
    except Exception:
        pass
    total, used, free = shutil.disk_usage(ROOT)
    row(OK if free > 50 * 2**30 else WARN, "disk free", f"{free / 2**30:.0f} GiB (models + images need ~30-60 GiB)")


def main() -> None:
    print(f"Environment check for {ROOT}")
    check_python()
    check_docker()
    check_gpu()
    check_k8s()
    check_system()
    print("\nLegend: ✅ ready · ⚠️  works with limits / optional · ❌ missing or unsupported")


if __name__ == "__main__":
    main()
