# M34 · MLOps & LLMOps

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Ops & Systems · **Lessons:** 17 existing + 3 planned (0 verified) · **GPU:** — · **Services:** docker, prometheus, grafana

**Prerequisites:** [M16 Classical Machine Learning](../M16-Classical%20Machine%20Learning/README.md), [M32 Containers & Kubernetes](../M32-Containers%20%26%20Kubernetes/README.md)

**Part of paths:** [Machine Learning Engineer](../paths/ml-engineer.md), [MLOps & ML Platform Engineer](../paths/mlops.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [MLOps: Serialization](01-MLOps%20-%20Serialization.ipynb) | 🟠 Advanced | 🔍 | Model saving, loading, and deployment packaging. |
| 02 | [Model Serialization](02-Model%20Serialization.ipynb) | 🟠 Advanced | 🔀 | Saving/loading models and portable formats. *(merge into S07-21: one serialisation lesson in M34)* |
| 03 | [MLOps: Experiment Tracking](03-MLOps%20-%20Experiment%20Tracking.ipynb) | 🟠 Advanced | 🔀 | MLflow, experiment logging, and model versioning. *(merge into S18-10: real MLflow lesson is canonical)* |
| 04 | [Experiment Tracking & Artifact Lineage (MLflow Engine)](04-Experiment%20Tracking%20&%20Artifact%20Lineage%20(MLflow%20Engine).ipynb) | 🟠 Advanced | 🔍 | Logging runs, parameters, and artifacts for reproducible experimentation. |
| 05 | Data & Model Versioning (DVC) |  | 🆕 |  |
| 06 | Model Registry & Promotion |  | 🆕 |  |
| 07 | [Local Continuous Integration (GitHub Actions Core Workflows)](07-Local%20Continuous%20Integration%20(GitHub%20Actions%20Core%20Workflows).ipynb) | 🟠 Advanced | 🔍 | Writing CI workflows that lint, test, and validate ML code on every push. |
| 08 | [Production Model Serving Topologies (FastAPI & Docker)](08-Production%20Model%20Serving%20Topologies%20(FastAPI%20&%20Docker).ipynb) | 🟠 Advanced | ⚙️ | Packaging and serving a trained model behind a containerized API. |
| 09 | [ML Workflow Orchestration on Kubernetes (Kubeflow)](09-ML%20Workflow%20Orchestration%20on%20Kubernetes%20(Kubeflow).ipynb) | 🔴 Expert | ⚙️ | Pipeline orchestration and experiment tracking for ML on Kubernetes. |
| 10 | [Telemetry Scraping & Observability Metrology (Prometheus)](10-Telemetry%20Scraping%20&%20Observability%20Metrology%20(Prometheus).ipynb) | 🔴 Expert | 🔍 | Instrumenting services with Prometheus metrics for production observability. |
| 11 | [Custom ML Metric Scraping (Prometheus)](11-Custom%20ML%20Metric%20Scraping%20(Prometheus).ipynb) | 🟠 Advanced | 🔀 | Exposing custom model-quality metrics for Prometheus scraping. *(merge into S18-14: one Prometheus lesson)* |
| 12 | [Distributed Tracing & Latency (OpenTelemetry + Jaeger)](12-Distributed%20Tracing%20&%20Latency%20(OpenTelemetry%20%2B%20Jaeger).ipynb) | 🟠 Advanced | 🔍 | Tracing requests across services to localize latency bottlenecks. |
| 13 | [High-Definition Observability (Grafana)](13-High-Definition%20Observability%20(Grafana).ipynb) | 🟠 Advanced | ⚙️ | Building dashboards that surface model health at a glance. |
| 14 | [High-Volume Log Aggregation (Grafana Loki)](14-High-Volume%20Log%20Aggregation%20(Grafana%20Loki).ipynb) | 🟠 Advanced | ⚙️ | Centralizing and querying logs at scale with Loki. |
| 15 | [SLOs, Error Budgets & Alerting (Alertmanager)](15-SLOs,%20Error%20Budgets%20&%20Alerting%20(Alertmanager).ipynb) | 🔴 Expert | ⚙️ | Defining service-level objectives and routing alerts on error-budget burn. |
| 16 | [Cluster Debugging & Observability (Prometheus & Grafana)](16-Cluster%20Debugging%20&%20Observability%20(Prometheus%20&%20Grafana).ipynb) | 🔴 Expert | 🔀 | Scheduling issues, networking, logs, and runtime failure diagnosis. *(merge into S19-11: one SLO / alerting lesson)* |
| 17 | [Shadow Deployments & Traffic Mirroring](17-Shadow%20Deployments%20&%20Traffic%20Mirroring.ipynb) | 🔴 Expert | ⚙️ | Testing new models against production traffic without serving live responses. |
| 18 | [Statistical Canary Testing & Rollbacks](18-Statistical%20Canary%20Testing%20&%20Rollbacks.ipynb) | 🔴 Expert | 🔍 | Statistically validating canary releases before a full rollout. |
| 19 | [Enterprise Secrets Security & Hardening Boundarie](19-Enterprise%20Secrets%20Security%20&%20Hardening%20Boundarie.ipynb) | 🔴 Expert | 🔍 | Secrets management, least-privilege boundaries, and system hardening practices. |
| 20 | LLMOps: Prompt Versioning & Release Management |  | 🆕 |  |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
