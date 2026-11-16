# M36 · LLM Serving & Inference Systems

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Ops & Systems · **Lessons:** 11 existing + 4 planned (0 verified) · **GPU:** required

**Services:** docker (docker: Docker Engine)

**Prerequisites:** [M26 LLM Foundations](../M26-LLM%20Foundations/README.md), [M32 Containers & Kubernetes](../M32-Containers%20%26%20Kubernetes/README.md)

**Part of paths:** [AI Infrastructure & GPU Systems](../paths/ai-infra-gpu.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [LLM Serving Fundamentals (Hugging Face Text Generation Inference)](01-LLM%20Serving%20Fundamentals%20(Hugging%20Face%20Text%20Generation%20Inference).ipynb) | 🟡 Intermediate | 🔍 | Throughput, latency, batching, and token streaming behavior. |
| 02 | [High-Throughput Serving Architecture (vLLM)](02-High-Throughput%20Serving%20Architecture%20(vLLM).ipynb) | 🟠 Advanced | ⚙️ | Paged attention, continuous batching, and high-throughput inference internals. |
| 03 | [Concurrent Inference Scheduling (vLLM PagedAttention & Continuous Batching)](03-Concurrent%20Inference%20Scheduling%20(vLLM%20PagedAttention%20&%20Continuous%20Batching).ipynb) | 🟠 Advanced | 🔀 | Queueing models, prioritization, and fairness in serving workloads. *(merge into S26-04: one vLLM internals lesson)* |
| 04 | [High-Throughput Serving & Engine Optimization (vLLM - Triton)](04-High-Throughput%20Serving%20&%20Engine%20Optimization%20(vLLM%20-%20Triton).ipynb) | 🔴 Expert | 🔀 | Comparing serving engines for high-throughput inference workloads. *(merge into S26-04: serving engines live in M36)* |
| 05 | [Kernel-Level Inference Optimization (TensorRT-LLM)](05-Kernel-Level%20Inference%20Optimization%20(TensorRT-LLM).ipynb) | 🟠 Advanced | ⚙️ | Engine building, kernel fusion, and precision-aware optimization. |
| 06 | [Tokenizer & Runtime Integration (Hugging Face Tokenizers & ONNX Runtime)](06-Tokenizer%20&%20Runtime%20Integration%20(Hugging%20Face%20Tokenizers%20&%20ONNX%20Runtime).ipynb) | 🟠 Advanced | ⚙️ | Efficient tokenization pipelines and cross-runtime interoperability. |
| 07 | [Quantization for Production Serving (GPTQ - AWQ)](07-Quantization%20for%20Production%20Serving%20(GPTQ%20-%20AWQ).ipynb) | 🔴 Expert | ⚙️ | INT8/FP8 tradeoffs and deployment-time calibration strategies. |
| 08 | [Multi-Model Serving Infrastructure (NVIDIA Triton Inference Server)](08-Multi-Model%20Serving%20Infrastructure%20(NVIDIA%20Triton%20Inference%20Server).ipynb) | 🔴 Expert | ⚙️ | Routing, model isolation, and shared GPU resource management. |
| 09 | [Observability in LLM Serving (Prometheus & OpenTelemetry)](09-Observability%20in%20LLM%20Serving%20(Prometheus%20&%20OpenTelemetry).ipynb) | 🔴 Expert | ⚙️ | Metrics, tracing, tail-latency analysis, and SLA tracking. |
| 10 | [Fault Tolerance & Recovery for Inference Endpoints](10-Fault%20Tolerance%20&%20Recovery%20for%20Inference%20Endpoints.ipynb) | 🔴 Expert | ⚙️ | Graceful degradation, retries, and resilient inference operations. |
| 11 | [Production Cost-Performance Engineering](11-Production%20Cost-Performance%20Engineering.ipynb) | 🔴 Expert | ⚙️ | Throughput-per-dollar optimization and capacity planning for scale. |
| 12 | SGLang & Structured Generation |  | 🆕 |  |
| 13 | Speculative Decoding |  | 🆕 |  |
| 14 | Prefix Caching & Disaggregated Prefill-Decode |  | 🆕 |  |
| 15 | Local Serving with llama.cpp & Ollama |  | 🆕 |  |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
