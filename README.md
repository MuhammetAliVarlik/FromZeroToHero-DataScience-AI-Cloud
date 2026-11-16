# 📊🧠☁️ FromZeroToHero-DataScience-AI-Cloud

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Modules](https://img.shields.io/badge/modules-43-blue)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-about-this-project)

A free, self-authored, end-to-end curriculum covering **Data Science, AI, and Cloud** — from Python fundamentals and statistics through deep learning, LLM engineering, and GPU kernel programming. Every lesson is a runnable Jupyter notebook. Built as both a structured personal learning path and a public resource for anyone learning this stack from scratch.

## 📚 Table of Contents

- [About This Project](#-about-this-project)
- [Why This Course Exists](#-why-this-course-exists)
- [Choose Your Path](#-choose-your-path)
- [Getting Started](#-getting-started)
- [Module Catalogue](#️-module-catalogue)
- [Disclaimer](#disclaimer)

## 📌 About This Project

- **What this is:** a personal, non-commercial crash course — free for anyone to read, learn from, and reuse. There's no paywall, no sign-up, and no monetization plan; this is a charity/learning project, not a product.
- **How it was made:** lesson content was generated with AI assistance (Google Gemini and Claude Code) and then reviewed, curated, and structured by me. I'm disclosing this explicitly so nothing here is mistaken for hand-written-from-scratch prose or official vendor documentation — treat it as a curated, AI-assisted study guide, and always sanity-check anything safety- or production-critical against primary sources.
- **Why it exists:** I use these notebooks as my own study material (I also compile them into PDF for offline reading), and I'm sharing the repository publicly in case the same structured path is useful to someone else on the same journey.
- **Contributing:** the repository is MIT-licensed and I'm happy to receive issues or pull requests — typo fixes, corrections, or suggestions for topics worth covering are all welcome.

## 🎯 Why This Course Exists

Most Data Science/AI learning material is fragmented: one course covers pandas, another covers a single ML algorithm, a bootcamp covers "AI" but skips the SQL and infrastructure underneath it, and by the time GPUs or Kubernetes show up you're back to piecing together blog posts. Meanwhile the industry has splintered into a handful of distinct roles — Analyst, Data Scientist, Data Engineer, ML/AI Engineer, LLM/GenAI Engineer — that all draw on an overlapping but not identical slice of the same foundation.

This repository exists to be **one continuous, ordered pipeline** instead of a pile of disconnected tutorials:

- **Linear where it matters.** Modules declare their prerequisites — Python (M01) underpins everything, NumPy/Pandas (M08) underpins Feature Engineering (M10) and Machine Learning (M16), which underpin Deep Learning (M20), Computer Vision (M21) and LLMs (M26), and so on through to GPU kernels (M38).
- **Modular where it helps.** You rarely need every module for one job. [Choose Your Path](#-choose-your-path) maps the same modules to atomic skill paths and to real job roles (including new hybrid roles such as Forward Deployed Engineer), so a Data Analyst and an AI Engineer can start from the same Core and branch out.
- **Depth-tagged.** Every lesson in every module table carries a level and a status (🟢 Beginner → 🟡 Intermediate → 🟠 Advanced → 🔴 Expert), so you can gauge how far into a topic you're going before you open the notebook.
- **Honest about its own limits.** This is an AI-assisted, self-taught study guide, not vendor documentation — see [Disclaimer](#disclaimer).

<!-- BEGIN GENERATED:paths -->
## 🧭 Choose Your Path

The course is a catalogue of **modules**. A **path** is an ordered list of modules for one skill area. A **role** combines paths to match a real job. Every path starts with the Core modules (M01 Python, M03 Git, M04 Linux). Hybrid profiles are common, so you can combine roles. Each role page shows its closest roles and what extra modules you need.

### Roles (job market, 2025–26)

| Role | Combines | Modules | Lessons |
| :--- | :--- | :-: | :-: |
| [Forward Deployed Engineer (FDE)](roles/forward-deployed-engineer.md) | Software Engineer (Python Backend) + AI Application Engineer + M11, M43 | 14 | 176 |
| [AI Engineer](roles/ai-engineer.md) | Software Engineer (Python Backend) + AI Application Engineer | 12 | 159 |
| [Machine Learning Engineer](roles/ml-engineer.md) | Machine Learning Engineer | 14 | 202 |
| [Applied Scientist / Research Engineer](roles/applied-scientist.md) | Data Scientist + Deep Learning & Computer Vision + NLP & LLM Engineer | 24 | 330 |
| [Product Data Scientist](roles/product-data-scientist.md) | Data Analyst & BI + Data Scientist | 15 | 209 |
| [Analytics Engineer](roles/analytics-engineer.md) | Data Analyst & BI + M02, M11 | 11 | 141 |
| [Data Engineer](roles/data-engineer.md) | Data Engineer | 11 | 129 |
| [MLOps / AI Platform Engineer](roles/ai-platform-engineer.md) | MLOps & ML Platform Engineer + M26, M36 | 13 | 165 |
| [Inference & Performance Engineer](roles/inference-engineer.md) | AI Infrastructure & GPU Systems | 15 | 191 |
| [Computer Vision / Perception Engineer](roles/cv-engineer.md) | Deep Learning & Computer Vision + Edge AI & Reinforcement Learning | 14 | 195 |
| [AI Security Engineer / Red Teamer](roles/ai-security-engineer.md) | Responsible AI & AI Security + AI Application Engineer | 15 | 223 |
| [AI Solutions Architect](roles/ai-solutions-architect.md) | AI Application Engineer + MLOps & ML Platform Engineer + M43 | 18 | 239 |

### Atomic paths

| Path | Module order | Lessons |
| :--- | :--- | :-: |
| [Python Developer](paths/python-developer.md) | M01 → M03 → M04 → M02 | 39 |
| [Software Engineer (Python Backend)](paths/software-engineer.md) | M01 → M03 → M04 → M02 → M07 → M32 → M33 | 82 |
| [Data Analyst & BI](paths/data-analyst.md) | M01 → M03 → M04 → M05 → M06 → M07 → M08 → M09 → M14 | 121 |
| [Data Scientist](paths/data-scientist.md) | M01 → M03 → M04 → M05 → M06 → M07 → M08 → M09 → M10 → M14 → M15 → M16 → M17 → M18 → M19 | 209 |
| [Machine Learning Engineer](paths/ml-engineer.md) | M01 → M03 → M04 → M02 → M05 → M06 → M08 → M10 → M16 → M40 → M20 → M32 → M34 → M35 | 202 |
| [Deep Learning & Computer Vision](paths/deep-learning-cv.md) | M01 → M03 → M04 → M05 → M06 → M08 → M16 → M20 → M21 → M22 → M23 → M24 | 170 |
| [NLP & LLM Engineer](paths/nlp-llm.md) | M01 → M03 → M04 → M05 → M08 → M16 → M20 → M26 → M27 → M28 → M31 | 152 |
| [AI Application Engineer](paths/ai-app-engineer.md) | M01 → M03 → M04 → M02 → M07 → M26 → M28 → M29 → M30 → M31 | 136 |
| [Data Engineer](paths/data-engineer.md) | M01 → M03 → M04 → M02 → M07 → M08 → M11 → M12 → M13 → M32 → M33 | 129 |
| [MLOps & ML Platform Engineer](paths/mlops.md) | M01 → M03 → M04 → M02 → M05 → M08 → M16 → M40 → M32 → M33 → M34 | 135 |
| [AI Infrastructure & GPU Systems](paths/ai-infra-gpu.md) | M01 → M03 → M04 → M02 → M05 → M08 → M16 → M20 → M32 → M39 → M38 → M37 → M26 → M36 → M35 | 191 |
| [Responsible AI & AI Security](paths/responsible-ai.md) | M01 → M03 → M04 → M05 → M06 → M08 → M16 → M26 → M28 → M31 → M41 | 159 |
| [Edge AI & Reinforcement Learning](paths/edge-ai-rl.md) | M01 → M03 → M04 → M05 → M08 → M16 → M20 → M35 → M25 | 127 |

<!-- END GENERATED:paths -->

## 🚀 Getting Started

A first-time setup walkthrough. Module M01 also has its own [Python & Anaconda Installation](</M01-Python/01-Python%20&%20Anaconda%20Installation.ipynb>) notebook that covers the same ground interactively, if you'd rather learn it as a lesson.

### 1. Prerequisites

- **Git** and **[uv](https://docs.astral.sh/uv/)** (`pip install uv`). uv downloads the right Python (3.12) for you.
- *(Optional)* **R** — only for M05 and M06 (`IRkernel::installspec()` registers the Jupyter kernel).
- *(Optional)* **Docker** — for modules that list services (databases, Kafka, Kubernetes, observability).
- *(Optional)* **NVIDIA GPU + CUDA** — module READMEs mark GPU as *optional* or *required*. Foundations and data modules run on CPU.

Check what your machine can run:

```bash
python tools/env_check.py
```

It reports Python, uv, R, Docker (and GPU access inside Docker), the GPU, CUDA and Kubernetes tools. It also lists which GPU features the course uses and whether your GPU supports them. The reference machine for this course is a laptop with a 4 GiB GTX 1650 Ti (compute capability 7.5), so every lesson is designed to run on small hardware; lessons that need newer GPUs (bf16, FP8, FlashAttention-3) say so at the top.

### 2. Clone the repository

```bash
git clone https://github.com/MuhammetAliVarlik/FromZeroToHero-DataScience-AI-Cloud.git
cd FromZeroToHero-DataScience-AI-Cloud
```

### 3. Install the Python environment

Dependencies live in [`pyproject.toml`](pyproject.toml), split into groups that match the modules. Install the base and only the groups you need:

| Group | Modules |
| :--- | :--- |
| *(base)* | Jupyter, NumPy, pandas, SciPy, Matplotlib, Seaborn |
| `foundations` | M01–M04 (pytest, Ruff, mypy, Pydantic) |
| `data` | M07–M10, M14 (SQL drivers, DuckDB, Polars, Plotly, Streamlit, statsmodels, scikit-learn) |
| `data-eng` | M11–M13 (dbt, dlt, Dagster, Great Expectations, Kafka, Spark, Delta, Iceberg) |
| `ds` | M14–M19 (DoWhy, EconML, XGBoost/LightGBM/CatBoost, MAPIE, Nixtla, Prophet, graphs) |
| `dl` | M20–M25 (PyTorch, Lightning, Transformers, Diffusers, YOLO, CLIP, audio, PyMC/Pyro, RL) |
| `llm` | M26–M31 (Transformers, PEFT/TRL, LangChain/LangGraph, Ollama, FastAPI, MCP, vector stores) |
| `ops` | M32–M35, M37, M40 (MLflow, DVC, Prometheus, OpenTelemetry, ONNX, OpenVINO, Ray, Optuna) |
| `responsible` | M41 (SHAP, LIME, Fairlearn, Captum, Opacus, Presidio) |
| `gpu` | M38 (CuPy, Numba) |

```bash
uv sync                                  # base only
uv sync --group data --group ds          # add groups
uv sync --all-groups                     # everything
```

`uv.lock` pins every version, so everyone gets the same environment. A few heavy stacks that pin their own versions (vLLM, SGLang, TensorRT, DeepSpeed, Airflow, AutoGluon, NeMo Guardrails, TensorFlow/LiteRT) are installed in a separate environment; the lesson that needs one shows the command.

### 4. Start local services (only when a module needs them)

All services are free and run in Docker, defined in [`docker/compose.yml`](docker/compose.yml):

```bash
docker compose -f docker/compose.yml --profile db up -d     # PostgreSQL + pgvector, MongoDB, Redis
docker compose -f docker/compose.yml --profile db down      # stop when you are done
```

Profiles: `db`, `rag`, `vector`, `streaming`, `cloud` (LocalStack AWS emulator + MinIO), `observability` (Prometheus + Grafana), `graph` (Neo4j), `ollama`. For local LLMs you can also install [Ollama](https://ollama.com) natively; the lessons use `http://localhost:11434` either way.

### 5. Launch Jupyter and start learning

```bash
uv run jupyter lab
```

Open any `.ipynb` file directly — every lesson is self-contained. Pick a [role or path](#-choose-your-path), then work through its modules in order; each module folder has a README with its lesson list.

**Maintainer tools** (in `tools/`): `build_curriculum.py` (validate the structure and regenerate READMEs from `curriculum.yml`), `nbtools.py` (execute notebooks and audit their outputs), `style_check.py` (check prose against [STYLE.md](STYLE.md)), `env_check.py`.

### 6. (Optional) Configure environment variables

Only the agent lessons in M29 (LangChain/LangSmith tracing) read a `.env` file — every other module runs without one:

```bash
cp .env.example .env
# then fill in your own LangSmith key(s) in .env
```

<!-- BEGIN GENERATED:catalogue -->
## 🛣️ Module Catalogue

**43 modules · 553 lessons** (424 written, 129 planned, 126 fully verified). Each module folder has its own README with the lesson list. Status per lesson: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned.

### 🧱 Foundations

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M01 · Python](M01-Python/README.md) | 18 + 0 planned | 18 | — | — |
| [M02 · Software Engineering Practices](M02-Software%20Engineering%20Practices/README.md) | 10 + 0 planned | 10 | M01 | — |
| [M03 · Git & Collaboration](M03-Git%20%26%20Collaboration/README.md) | 4 + 0 planned | 4 | — | — |
| [M04 · Linux & Shell](M04-Linux%20%26%20Shell/README.md) | 7 + 0 planned | 7 | — | — |
| [M05 · Mathematics for Data Science (R)](M05-Mathematics%20for%20Data%20Science%20%28R%29/README.md) | 7 + 0 planned | 7 | — | — |
| [M06 · Statistics & Inference (R)](M06-Statistics%20%26%20Inference%20%28R%29/README.md) | 23 + 0 planned | 23 | M05 | — |

### 🗄️ Data

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M07 · SQL & Databases](M07-SQL%20%26%20Databases/README.md) | 20 + 0 planned | 20 | M01 | — |
| [M08 · NumPy, Pandas & Polars](M08-NumPy%2C%20Pandas%20%26%20Polars/README.md) | 18 + 0 planned | 18 | M01 | — |
| [M09 · Data Visualization & BI](M09-Data%20Visualization%20%26%20BI/README.md) | 18 + 0 planned | 18 | M08 | — |
| [M10 · Feature Engineering & Data Preprocessing](M10-Feature%20Engineering%20%26%20Data%20Preprocessing/README.md) | 14 + 2 planned | 0 | M08 | — |
| [M11 · Data Engineering & Orchestration](M11-Data%20Engineering%20%26%20Orchestration/README.md) | 7 + 3 planned | 0 | M07, M02 | — |
| [M12 · Streaming & Lakehouse](M12-Streaming%20%26%20Lakehouse/README.md) | 5 + 2 planned | 0 | M11 | — |
| [M13 · Spark & Distributed Data Processing](M13-Spark%20%26%20Distributed%20Data%20Processing/README.md) | 10 + 2 planned | 0 | M08, M11 | — |

### 🔬 Data Science

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M14 · Experimentation & A/B Testing](M14-Experimentation%20%26%20A/B%20Testing/README.md) | 0 + 6 planned | 0 | M06, M08 | — |
| [M15 · Causal Inference](M15-Causal%20Inference/README.md) | 0 + 6 planned | 0 | M14 | — |
| [M16 · Classical Machine Learning](M16-Classical%20Machine%20Learning/README.md) | 18 + 4 planned | 0 | M05, M08 | — |
| [M17 · Time Series & Forecasting](M17-Time%20Series%20%26%20Forecasting/README.md) | 22 + 3 planned | 0 | M16 | optional |
| [M18 · Recommender Systems](M18-Recommender%20Systems/README.md) | 0 + 6 planned | 0 | M16 | optional |
| [M19 · Graph Data Science](M19-Graph%20Data%20Science/README.md) | 12 + 1 planned | 0 | M16 | optional |

### 🧠 Deep Learning & Modalities

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M20 · Deep Learning Foundations](M20-Deep%20Learning%20Foundations/README.md) | 21 + 5 planned | 0 | M05, M01 | optional |
| [M21 · Computer Vision](M21-Computer%20Vision/README.md) | 11 + 5 planned | 0 | M20 | required |
| [M22 · Generative Models](M22-Generative%20Models/README.md) | 10 + 3 planned | 0 | M21 | required |
| [M23 · Speech & Audio](M23-Speech%20%26%20Audio/README.md) | 0 + 5 planned | 0 | M20 | optional |
| [M24 · Probabilistic & Bayesian Deep Learning](M24-Probabilistic%20%26%20Bayesian%20Deep%20Learning/README.md) | 9 + 2 planned | 0 | M20, M06 | optional |
| [M25 · Reinforcement Learning](M25-Reinforcement%20Learning/README.md) | 7 + 2 planned | 0 | M20 | optional |

### 🤖 LLM & AI Applications

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M26 · LLM Foundations](M26-LLM%20Foundations/README.md) | 9 + 6 planned | 1 | M01 | optional |
| [M27 · LLM Fine-Tuning & Alignment](M27-LLM%20Fine-Tuning%20%26%20Alignment/README.md) | 5 + 2 planned | 0 | M26 | required |
| [M28 · RAG & Retrieval Systems](M28-RAG%20%26%20Retrieval%20Systems/README.md) | 11 + 5 planned | 0 | M26 | optional |
| [M29 · AI Agents & MCP](M29-AI%20Agents%20%26%20MCP/README.md) | 13 + 6 planned | 0 | M28 | optional |
| [M30 · AI Application Engineering](M30-AI%20Application%20Engineering/README.md) | 12 + 3 planned | 0 | M02, M26 | optional |
| [M31 · Evaluation & Observability for ML and LLMs](M31-Evaluation%20%26%20Observability%20for%20ML%20and%20LLMs/README.md) | 9 + 3 planned | 0 | M28 | optional |

### ⚙️ Ops & Systems

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M32 · Containers & Kubernetes](M32-Containers%20%26%20Kubernetes/README.md) | 7 + 2 planned | 0 | M04, M02 | optional |
| [M33 · Cloud & Infrastructure as Code](M33-Cloud%20%26%20Infrastructure%20as%20Code/README.md) | 11 + 3 planned | 0 | M32 | — |
| [M34 · MLOps & LLMOps](M34-MLOps%20%26%20LLMOps/README.md) | 17 + 3 planned | 0 | M16, M32 | — |
| [M35 · Model Optimization & Edge AI](M35-Model%20Optimization%20%26%20Edge%20AI/README.md) | 13 + 3 planned | 0 | M20 | optional |
| [M36 · LLM Serving & Inference Systems](M36-LLM%20Serving%20%26%20Inference%20Systems/README.md) | 11 + 4 planned | 0 | M26, M32 | required |
| [M37 · Distributed Training](M37-Distributed%20Training/README.md) | 4 + 2 planned | 0 | M20, M32 | required |
| [M38 · GPU Programming & Kernels](M38-GPU%20Programming%20%26%20Kernels/README.md) | 11 + 4 planned | 0 | M20 | required |
| [M39 · Systems Languages for AI (C++ & Rust)](M39-Systems%20Languages%20for%20AI%20%28C%2B%2B%20%26%20Rust%29/README.md) | 2 + 1 planned | 0 | M01 | — |
| [M40 · AutoML & Hyperparameter Optimization](M40-AutoML%20%26%20Hyperparameter%20Optimization/README.md) | 6 + 0 planned | 0 | M16 | optional |

### 🛡️ Responsibility

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M41 · Responsible AI, AI Security & Governance](M41-Responsible%20AI%2C%20AI%20Security%20%26%20Governance/README.md) | 12 + 5 planned | 0 | M16, M26 | optional |

### 🏁 Capstones

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M42 · Capstone Projects](M42-Capstone%20Projects/README.md) | 0 + 13 planned | 0 | — | optional |

### 🤝 Delivery

| Module | Lessons | Verified | Prerequisites | GPU |
| :--- | :-: | :-: | :--- | :-: |
| [M43 · AI Solution Design & Delivery](M43-AI%20Solution%20Design%20%26%20Delivery/README.md) | 0 + 7 planned | 0 | M30, M33 | — |

<!-- END GENERATED:catalogue -->

### Notes on Supporting Material

- `files/` contains small sample inputs and outputs used in notebook examples.
- `images/` contains images referenced by the notes.

---

The structure is generated from [`curriculum.yml`](curriculum.yml) by `tools/build_curriculum.py`; edit the YAML, then run `python tools/build_curriculum.py --generate --check`. 🚀

---

## Disclaimer

* The content is created for **educational purposes only** and is not a substitute for official vendor documentation, especially for anything safety- or production-critical.
* All explanations are reviewed and structured based on my own understanding (see the "About This Project" section above for how the AI-assisted authoring process worked).
* Any referenced materials belong to their respective owners and are credited where applicable.
* If any unintentional copyright issue arises, please contact me and it will be promptly resolved.

If any unintentional copyright issue arises, please contact me and it will be promptly resolved.
