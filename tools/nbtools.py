#!/usr/bin/env python3
"""Execute and audit lesson notebooks.

  python tools/nbtools.py run   --module M26              # execute in place (kernel from notebook metadata)
  python tools/nbtools.py run   PATH.ipynb [...]
  python tools/nbtools.py audit --module M26 [--sheet out.png]

`run` executes each notebook with nbconvert. R notebooks use the `ir` kernel; Python notebooks use
the kernel of the current environment (run it with `uv run python tools/nbtools.py ...`).
Messages are forced to English so outputs are the same on every machine.

`audit` reports, per notebook: unexecuted code cells, errors, stderr output, transparent images
(invisible on dark themes), and text that shows a simulation/fallback path ran instead of the real
tool. `--sheet` writes a contact sheet of all plots so you can inspect them at once (needs Pillow).
"""
from __future__ import annotations

import argparse
import base64
import glob
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FALLBACK = re.compile(r"(fallback|simulat(ed|ion) (path|mode|note)|\bsandbox\b|unavailable|not (installed|available)"
                      r"|mock(ed)? (response|client|llm)|\[Simulation Note\])", re.I)


def notebooks(args) -> list[str]:
    paths = list(args.notebooks)
    if args.module:
        paths += sorted(glob.glob(os.path.join(ROOT, f"{args.module}-*", "*.ipynb")))
    if not paths:
        sys.exit("give notebooks or --module")
    return paths


def kernel_of(path: str) -> str:
    meta = json.load(open(path, encoding="utf-8")).get("metadata", {})
    name = meta.get("kernelspec", {}).get("name", "python3")
    return "ir" if name == "ir" else "python3"


def run(args) -> int:
    env = dict(os.environ, LANGUAGE="en", LC_MESSAGES="C", PYTHONWARNINGS=os.environ.get("PYTHONWARNINGS", ""))
    # make `jupyter-*` subcommands and the python3 kernel come from the same environment as this interpreter
    env["PATH"] = os.path.dirname(sys.executable) + os.pathsep + env.get("PATH", "")
    env.setdefault("NO_COLOR", "1")          # no ANSI colour codes from CLI tools in stored outputs
    failed = 0
    for p in notebooks(args):
        k = kernel_of(p)
        cmd = [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace",
               f"--ExecutePreprocessor.timeout={args.timeout}", f"--ExecutePreprocessor.kernel_name={k}", os.path.abspath(p)]
        r = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(p)), env=env, capture_output=True, text=True)
        name = os.path.relpath(p, ROOT)
        if r.returncode == 0:
            print(f"OK   [{k}] {name}")
        else:
            failed += 1
            tail = "\n".join(l for l in r.stderr.splitlines() if not l.startswith("[NbConvertApp]"))[-2500:]
            print(f"FAIL [{k}] {name}\n{tail}\n")
    print(f"\n{failed} failed")
    return 1 if failed else 0


def audit(args) -> int:
    images, problems = [], 0
    for p in notebooks(args):
        nb = json.load(open(p, encoding="utf-8"))
        found = []
        n_code = n_out = 0
        for i, c in enumerate(nb["cells"]):
            if c["cell_type"] != "code" or not "".join(c["source"]).strip():
                continue
            n_code += 1
            if c.get("execution_count") is None:
                found.append(f"cell {i}: not executed")
            if c.get("outputs"):
                n_out += 1
            for o in c.get("outputs", []):
                text = "".join(o.get("text", "")) + "".join(o.get("data", {}).get("text/plain", ""))
                if o.get("output_type") == "error":
                    found.append(f"cell {i}: ERROR {o.get('ename')}: {o.get('evalue', '')[:120]}")
                if o.get("name") == "stderr" and text.strip():
                    found.append(f"cell {i}: stderr: {text.strip().splitlines()[0][:120]}")
                if FALLBACK.search(text):
                    found.append(f"cell {i}: fallback/simulation text: {FALLBACK.search(text).group(0)}")
                png = o.get("data", {}).get("image/png")
                if png:
                    try:
                        from PIL import Image
                        im = Image.open(io.BytesIO(base64.b64decode(png))).convert("RGBA")
                        if im.getpixel((2, 2))[3] == 0:
                            found.append(f"cell {i}: transparent plot background")
                        images.append(im.convert("RGB"))
                    except ImportError:
                        pass
        name = os.path.relpath(p, ROOT)
        print(f"{'OK  ' if not found else 'WARN'} {name}  (code cells: {n_code}, with output: {n_out})")
        for f in found:
            print(f"     - {f}")
        problems += bool(found)
    if args.sheet and images:
        from PIL import Image
        w, cols = 500, 4
        thumbs = [im.resize((w, int(im.height * w / im.width))) for im in images]
        rows = [thumbs[k:k + cols] for k in range(0, len(thumbs), cols)]
        sheet = Image.new("RGB", (w * cols, sum(max(t.height for t in r) for r in rows)), "grey")
        y = 0
        for r in rows:
            for k, t in enumerate(r):
                sheet.paste(t, (k * w, y))
            y += max(t.height for t in r)
        sheet.save(args.sheet)
        print(f"\ncontact sheet with {len(images)} plots -> {args.sheet}")
    print(f"\n{problems} notebook(s) with warnings")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("run", "audit"):
        s = sub.add_parser(name)
        s.add_argument("notebooks", nargs="*")
        s.add_argument("--module")
        if name == "run":
            s.add_argument("--timeout", type=int, default=900)
        else:
            s.add_argument("--sheet")
    a = ap.parse_args()
    sys.exit(run(a) if a.cmd == "run" else audit(a))


if __name__ == "__main__":
    main()
