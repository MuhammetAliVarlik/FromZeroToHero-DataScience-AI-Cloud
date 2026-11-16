# M38 · GPU Programming & Kernels

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Ops & Systems · **Lessons:** 11 existing + 4 planned (0 verified) · **GPU:** required

**Prerequisites:** [M20 Deep Learning Foundations](../M20-Deep%20Learning%20Foundations/README.md) · **Recommended:** [M39 Systems Languages for AI (C++ & Rust)](../M39-Systems%20Languages%20for%20AI%20%28C%2B%2B%20%26%20Rust%29/README.md)

**Part of paths:** [AI Infrastructure & GPU Systems](../paths/ai-infra-gpu.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [CUDA Programming Basics (CUDA C++)](01-CUDA%20Programming%20Basics%20(CUDA%20C%2B%2B).ipynb) | 🟡 Intermediate | 🔍 | Kernels, threads, blocks, and execution model fundamentals. |
| 02 | [GPU Memory Hierarchy & Bandwidth Optimization (CUDA)](02-GPU%20Memory%20Hierarchy%20&%20Bandwidth%20Optimization%20(CUDA).ipynb) | 🟡 Intermediate | 🔍 | Global, shared, registers, and bandwidth-aware programming. |
| 03 | [Warp Divergence & Occupancy Tuning (Nsight Compute)](03-Warp%20Divergence%20&%20Occupancy%20Tuning%20(Nsight%20Compute).ipynb) | 🟠 Advanced | ⚙️ | SIMT behavior, occupancy tuning, and branch efficiency profiling. |
| 04 | Hopper & Blackwell Features (TMA, FP8, FP4) |  | 🆕 |  |
| 05 | [Writing GPU Kernels in Python (Triton)](05-Writing%20GPU%20Kernels%20in%20Python%20(Triton).ipynb) | 🟠 Advanced | 🔍 | Python-based custom kernels and performance-oriented implementation. |
| 06 | CUDA Python |  | 🆕 |  |
| 07 | [Custom CUDA Kernel Development (PyTorch C++-CUDA Extensions)](07-Custom%20CUDA%20Kernel%20Development%20(PyTorch%20C%2B%2B-CUDA%20Extensions).ipynb) | 🟠 Advanced | ⚙️ | Fused operations, tiling, and profiling-guided kernel optimization. |
| 08 | [Kernel Fusion Strategies (Triton & torch.compile)](08-Kernel%20Fusion%20Strategies%20(Triton%20&%20torch.compile).ipynb) | 🟠 Advanced | 🔍 | Combining operators to reduce memory traffic and latency overhead. |
| 09 | CUTLASS & CuTe DSL |  | 🆕 |  |
| 10 | [Flash Attention & Attention Optimization (FlashAttention)](10-Flash%20Attention%20&%20Attention%20Optimization%20(FlashAttention).ipynb) | 🔴 Expert | 🔍 | IO-aware attention, sparse attention, and sliding-window methods. |
| 11 | FlashAttention-3 |  | 🆕 |  |
| 12 | [Memory-Bound vs Compute-Bound Optimization (Nsight - CUDA Profiling)](12-Memory-Bound%20vs%20Compute-Bound%20Optimization%20(Nsight%20-%20CUDA%20Profiling).ipynb) | 🔴 Expert | 🔍 | Roofline analysis, coalesced access, and cache-aware kernel design. |
| 13 | [Distributed Attention for Long-Context Models (Ring Attention)](13-Distributed%20Attention%20for%20Long-Context%20Models%20(Ring%20Attention).ipynb) | 🔴 Expert | ⚙️ | Multi-GPU attention scaling and communication-efficient kernel pipelines. |
| 14 | [Pretraining Systems Engineering at Scale (Megatron-LM)](14-Pretraining%20Systems%20Engineering%20at%20Scale%20(Megatron-LM).ipynb) | 🔴 Expert | ⚙️ | Tokenizer design, data pipelines, scaling laws, and MoE basics at scale. |
| 15 | [Inference Runtime Engineering (CUDA Graphs - TensorRT)](15-Inference%20Runtime%20Engineering%20(CUDA%20Graphs%20-%20TensorRT).ipynb) | 🔴 Expert | 🔍 | Scheduler-aware serving optimization and runtime graph capture. |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
