# 📊🧠☁️ FromZeroToHero-DataScience-AI-Cloud

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Sections](https://img.shields.io/badge/sections-27-blue)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-about-this-project)

A free, self-authored, end-to-end curriculum covering **Data Science, AI, and Cloud** — from Python fundamentals and statistics through deep learning, LLM engineering, and GPU kernel programming. Every lesson is a runnable Jupyter notebook. Built as both a structured personal learning path and a public resource for anyone learning this stack from scratch.

## 📚 Table of Contents

- [About This Project](#-about-this-project)
- [Why This Course Exists](#-why-this-course-exists)
- [Choose Your Path](#-choose-your-path)
- [Getting Started](#-getting-started)
- [Roadmap Plan](#-roadmap-plan)
- [Full Curriculum (Section by Section)](#-programming--data-manipulation)
- [Disclaimer](#disclaimer)

## 📌 About This Project

- **What this is:** a personal, non-commercial crash course — free for anyone to read, learn from, and reuse. There's no paywall, no sign-up, and no monetization plan; this is a charity/learning project, not a product.
- **How it was made:** lesson content was generated with AI assistance (Google Gemini and Claude Code) and then reviewed, curated, and structured by me. I'm disclosing this explicitly so nothing here is mistaken for hand-written-from-scratch prose or official vendor documentation — treat it as a curated, AI-assisted study guide, and always sanity-check anything safety- or production-critical against primary sources.
- **Why it exists:** I use these notebooks as my own study material (I also compile them into PDF for offline reading), and I'm sharing the repository publicly in case the same structured path is useful to someone else on the same journey.
- **Contributing:** the repository is MIT-licensed and I'm happy to receive issues or pull requests — typo fixes, corrections, or suggestions for topics worth covering are all welcome.

## 🎯 Why This Course Exists

Most Data Science/AI learning material is fragmented: one course covers pandas, another covers a single ML algorithm, a bootcamp covers "AI" but skips the SQL and infrastructure underneath it, and by the time GPUs or Kubernetes show up you're back to piecing together blog posts. Meanwhile the industry has splintered into a handful of distinct roles — Analyst, Data Scientist, Data Engineer, ML/AI Engineer, LLM/GenAI Engineer — that all draw on an overlapping but not identical slice of the same foundation.

This repository exists to be **one continuous, ordered pipeline** instead of a pile of disconnected tutorials:

- **Linear where it matters.** Sections build on each other — Python (01) underpins everything, NumPy/Pandas (04) underpins Feature Engineering (05), which underpins Machine Learning (07), which underpins Deep Learning (09), which underpins Computer Vision (10) and NLP/LLMs (11), and so on through to GPU kernels (27).
- **Modular where it helps.** You rarely need all 27 sections for one job. The [Choose Your Path](#-choose-your-path) section below maps this same content to role-specific orderings, so a Data Analyst and an LLM Engineer can both start here and stop at different points.
- **Depth-tagged.** Every lesson in every section table carries a level (🟢 Beginner → 🟡 Intermediate → 🟠 Advanced → 🔴 Expert), so you can gauge how far into a topic you're going before you open the notebook.
- **Honest about its own limits.** This is an AI-assisted, self-taught study guide, not vendor documentation — see [Disclaimer](#disclaimer).

## 🧭 Choose Your Path

Same 27 sections, different routes through them depending on the role you're aiming for. Numbers refer to the **Section** column in the [Roadmap Plan](#-roadmap-plan) table below — click through to a section's row there, then scroll down to its lesson table for the individual notebooks.

| Path | Recommended Order | Focus |
| :--- | :--- | :--- |
| 📈 **Data Analyst** | 01 → 03 → 04 → 02 → 06 → 05 | Query, clean, and visualize data; turn it into decisions and dashboards. |
| 🔬 **Data Scientist** | 01 → 02 → 04 → 03 → 05 → 06 → 07 → 08 → 09 → 19 → 21 | The full statistical + ML modeling lifecycle, from EDA to responsible evaluation. |
| 🏗️ **Data Engineer** | 01 → 03 → 04 → 15 → 16 → 17 → 18 → 22 | Build and operate the pipelines, warehouses, and cloud infra data teams depend on. |
| 🤖 **AI / ML Engineer** | 01 → 04 → 05 → 07 → 09 → 19 → 20 → 12 → 17 → 23 | Train, evaluate, optimize, and ship ML models into production systems. |
| 🧠 **LLM / GenAI Engineer** | 01 → 04 → 11 → 12 → 13 → 14 → 19 → 21 → 26 → 27 | Build, retrieve, orchestrate, evaluate, and serve LLM-powered applications. |
| ☁️ **MLOps / Platform Engineer** | 01 → 18 → 17 → 23 → 19 → 20 → 26 → 27 | Own the infrastructure, observability, and scaling behind every model in production. |

None of these are exclusive — most real careers end up borrowing from two or three of them. When in doubt, start with **01 → 03 → 04**; almost every path needs that base.

## 🚀 Getting Started

A first-time setup walkthrough. Section 01 also has its own [00-Python & Anaconda Installation](</Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/00-Python%20&%20Anaconda%20Installation.ipynb>) notebook that covers the same ground interactively, if you'd rather learn it as a lesson.

### 1. Prerequisites

- **Python 3.10 or 3.11**
- **Git**
- *(Optional)* R + RStudio, or the R extension for VS Code — for Section 02
- *(Optional)* Docker — for Section 18 onward, where containers show up
- *(Optional)* An NVIDIA GPU + CUDA toolkit — for Sections 09, 20, 23, and 25–27; every notebook up through Section 08 runs fine on CPU

### 2. Clone the repository

```bash
git clone https://github.com/MuhammetAliVarlik/FromZeroToHero-DataScience-AI-Cloud.git
cd FromZeroToHero-DataScience-AI-Cloud
```

### 3. Create an isolated environment

Pick one — conda/mamba or plain venv both work.

```bash
# conda / mamba
conda create -n ds python=3.11 -y
conda activate ds
```

```bash
# venv
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` is grouped by the section that first introduces each package. A handful of packages in Sections 09, 20, and 22–27 (`torch`, `deepspeed`, `dgl`, `torch-geometric`, `tensorrt`, `vllm`, `openvino`, GPU builds of `onnxruntime`) need a vendor-specific install matched to your OS/GPU — check each one's own docs before running notebooks in those sections. You don't need them to work through Sections 01–08.

### 5. Launch Jupyter and start learning

```bash
jupyter lab
```

Open any `.ipynb` file directly — every lesson is self-contained. Follow the [Roadmap Plan](#-roadmap-plan) top to bottom, or jump to your [path](#-choose-your-path) above.

### 6. (Optional) Configure environment variables

Only Section 14 (LangChain/LangSmith tracing) reads a `.env` file — every other section runs without one:

```bash
cp .env.example .env
# then fill in your own LangSmith key(s) in .env
```

## 🛣️ Roadmap Plan

The roadmap below shows the full learning path. All 27 sections now have authored lesson content in this repository (see each section's table further down for the full lesson list).

| Section | Title | Number of Notes | Status | Common Tools & Technologies | Description |
| :-----: | :--- | :-------------: | :---: | :--- | :--- |
| 01 | 🐍 Python Programming, Git & Environment Management | 21 | 🟡 Done,Not Published | Python, Git, GitHub, venv, Poetry | Variables, core programming, OOP, source control workflows, and environment/dependency management. |
| 02 | 📏 Mathematics & Statistics with R | 25 | 🟡 Done,Not Published | R, RStudio | Linear algebra, probability, hypothesis testing, and statistical reasoning for data science. |
| 03 | 🗄️ SQL & NoSQL Databases | 14 | 🟡 Done,Not Published | MySQL, MongoDB | Relational querying, MongoDB fundamentals, CRUD workflows, and practical data modeling. |
| 04 | 📊 NumPy & Pandas | 14 | 🟡 Done,Not Published | NumPy, Pandas | Vectorized computation, tabular manipulation, and efficient exploratory data workflows. |
| 05 | 🔍 Feature Engineering & Data Preprocessing | 14 | 🟡 Done,Not Published | Python, Pandas, scikit-learn | Missing-value handling, scaling, transformations, and dimensionality reduction including PCA. |
| 06 | 📊 Data Visualization & Business Intelligence | 14 | 🟡 Done,Not Published | Matplotlib, Seaborn, Tableau | Exploratory and executive-focused visualization, dashboarding, and data storytelling. |
| 07 | 🤖 Machine Learning Fundamentals | 22 | 🟡 Done,Not Published | scikit-learn, Python | Regression, classification, model selection, and end-to-end baseline ML workflows. |
| 08 | ⏳ Time Series Analysis & Forecasting | 22 | 🟡 Done,Not Published | statsmodels, Prophet | Trend/seasonality analysis, ARIMA-family methods, and forecasting evaluation patterns. |
| 09 | 🧠 Deep Learning & Neural Networks | 22 | 🟡 Done,Not Published | PyTorch, TensorFlow | MLPs, backpropagation, optimization, and neural network training fundamentals. |
| 10 | 👀 Computer Vision & Generative Models | 20 | 🟡 Done,Not Published | OpenCV, PyTorch, TensorFlow | CNNs, image processing pipelines, generative modeling, and GAN-based workflows. |
| 11 | 🗣️ NLP, Transformers & LLMs | 15 | 🟡 Done,Not Published | Hugging Face, spaCy, NLTK | Text preprocessing, transformer attention mechanics, and modern LLM application patterns. |
| 12 | 🌐 REST APIs, FastAPI & AI Prototyping | 12 | 🟡 Done,Not Published | FastAPI, Streamlit, Gradio | API endpoint design, AI app prototyping, validation, and rapid model-facing interfaces. |
| 13 | 🔎 RAG, Vector Databases & Retrieval Systems | 12 | 🟡 Done,Not Published | Pinecone, Qdrant, FAISS | Embeddings, indexing, retrieval pipelines, and grounded generation system design. |
| 14 | 🧩 LangChain, LangGraph & Multi-Agent Orchestration | 13 | 🟡 Done,Not Published | LangChain, LangGraph, AutoGen, CrewAI | Autonomous agent orchestration, memory/state management, and multi-agent interaction design. |
| 15 | 🏗️ Data Engineering & ETL Pipelines | 12 | 🟡 Done,Not Published | Apache Airflow, SQL | Pipeline orchestration, warehouse-oriented ETL/ELT, and reliable data movement patterns. |
| 16 | ⚡ PySpark & Big Data Processing | 10 | 🟡 Done,Not Published | Apache Spark, Spark SQL | Distributed data processing, partition-aware transformations, and scalable analytics workloads. |
| 17 | ☁️ Cloud Computing & AI Services | 10 | 🟡 Done,Not Published | AWS, Azure, GCP | Cloud architecture, managed AI/ML services, and deployment-ready infrastructure foundations. |
| 18 | 🐧 Linux, Bash Foundations & MLOps | 15 | 🟡 Done,Not Published | Linux, Bash, Docker, MLflow, CI/CD | Terminal-first engineering workflows, automation, packaging, and reproducible ML operations. |
| 19 | 📏 Model Evaluation & Monitoring | 13 | 🟡 Done,Not Published | Prometheus, Grafana, MLflow | Online/offline evaluation, observability, alerting, and production model quality tracking. |
| 20 | ⚙️ AutoML & Model Optimization | 10 | 🟡 Done,Not Published | Auto-sklearn, Optuna, H2O.ai | Hyperparameter optimization, automated model search, and inference/training efficiency tuning. |
| 21 | 🔦 Explainable AI, Ethics & Responsible AI | 12 | 🟡 Done,Not Published | SHAP, LIME | Transparency, fairness, interpretability, and governance-oriented responsible AI practices. |
| 22 | 🕸️ Graph Data Science & Network Analysis | 12 | 🟡 Done,Not Published | Neo4j, NetworkX | Graph modeling, network metrics, traversal, and graph-based analytical applications. |
| 23 | ☸️ Kubernetes & Distributed Training | 12 | 🟡 Done,Not Published | Kubernetes, DeepSpeed, PyTorch Distributed | Container orchestration, distributed training, and data/model parallel scaling strategies. |
| 24 | 📐 Statistical Deep Learning | 12 | 🟡 Done,Not Published | PyTorch, Bayesian methods, VAE, diffusion | Bayesian deep learning, uncertainty modeling, VAEs, and diffusion-based generative methods. |
| 25 | 📱 Edge AI, TinyML & Reinforcement Learning | 13 | 🟡 Done,Not Published | TensorFlow Lite, Edge Impulse, OpenAI Gym | Embedded inference, constrained-device deployment, and agent training workflows. |
| 26 | 🖥️ System Programming & LLM Serving | 12 | 🟡 Done,Not Published | Modern C++, Rust, vLLM, TensorRT-LLM | Systems-level memory/performance engineering and high-throughput LLM inference serving. |
| 27 | ⚙️ GPU Systems, CUDA & Attention Optimization | 11 | 🟡 Done,Not Published | CUDA, Triton, C++, Rust, Flash Attention | Kernel programming, low-level acceleration, and attention/runtime optimization for scale. |
### 🔹 Programming & Data Manipulation

#### 🐍 Section 1 - Python Programming, Git & Environment Management

| Context                                                                                                                | Description                                                                         | Medium Page | Level                                              |
| :--------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :---------- | :---------------------------------------------------- |
| [00-Python & Anaconda Installation](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/00-Python%20&%20Anaconda%20Installation.ipynb) | Installing Python and Anaconda, and setting up the basic development environment.   |             | <span style="color:green;">Beginner 🟢</span>      |
| [01-Python Data Structures Overview](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/01-Python%20Data%20Structures%20Overview.ipynb) | Overview of Python built-in data structures (list, tuple, dict, set).              |             | <span style="color:green;">Beginner 🟢</span>      |
| [02-Comprehensions in Python](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/02-Comprehensions%20in%20Python.ipynb) | Writing concise and readable code using list, dictionary, and set comprehensions.   |             | <span style="color:green;">Beginner 🟢</span>      |
| [03-Loops in Python](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/03-Loops%20in%20Python.ipynb) | Iterating over data using for and while loops.                                       |             | <span style="color:green;">Beginner 🟢</span>      |
| [04-Conditions in Python](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/04-Conditions%20in%20Python.ipynb) | Creating conditional logic with if, elif, and else statements.                      |             | <span style="color:green;">Beginner 🟢</span>      |
| [05-Functions in Python](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/05-Functions%20in%20Python.ipynb) | Defining functions, using parameters, and making code modular.                      |             | <span style="color:green;">Beginner 🟢</span>      |
| [06-Modules & Packages](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/06-Modules%20&%20Packages.ipynb) | Importing modules, creating packages, and improving code reusability.               |             | <span style="color:green;">Beginner 🟢</span>      |
| [07-Basic Input-Output (I-O) in Python](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/07-Basic%20Input-Output%20%28I-O%29%20in%20Python.ipynb) | Getting user input and displaying output effectively.                                |             | <span style="color:green;">Beginner 🟢</span>      |
| [08-Exception Handling](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/08-Exception%20Handling.ipynb) | Catching and managing errors using try, except, and finally.                        |             | <span style="color:green;">Beginner 🟢</span>      |
| [09-Lambda & Higher-Order Functions](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/09-Lambda%20&%20Higher-Order%20Functions.ipynb) | Using lambda expressions, map, filter, and reduce for functional workflows.         |             | <span style="color:yellow;">Intermediate 🟡</span> |
| [10-Iterators & Generators](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/10-Iterators%20&%20Generators.ipynb) | Using iter and next, and creating generators with yield.                            |             | <span style="color:yellow;">Intermediate 🟡</span> |
| [11-Object Oriented Programming in Python](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/11-Object%20Oriented%20Programming%20in%20Python.ipynb) | Classes, objects, inheritance, and encapsulation in OOP.                            |             | <span style="color:yellow;">Intermediate 🟡</span> |
| [12-Decorators](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/12-Decorators.ipynb) | Wrapping functions and modifying behavior using decorators.                          |             | <span style="color:yellow;">Intermediate 🟡</span> |
| [13-Type Hinting & Static Typing](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/13-Type%20Hinting%20&%20Static%20Typing.ipynb) | Adding type hints to improve readability, IDE support, and reliability.             |             | <span style="color:yellow;">Intermediate 🟡</span> |
| [14-Best Practices](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/14-Best%20Practices%20%28PEP8,%20docstring,%20clean%20code%29.ipynb) | Following PEP8, writing docstrings, and applying clean code principles.             |             | <span style="color:yellow;">Intermediate 🟡</span> |
| [15-Performance Optimization](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/15-Performance%20Optimization.ipynb) | Techniques to optimize Python code for speed and memory usage.                      |             | <span style="color:orange;">Advanced 🟠</span>     |
| [16-SOLID Principles](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/16-SOLID%20Principles.ipynb) | Applying SOLID design principles in object-oriented programming.                     |             | <span style="color:orange;">Advanced 🟠</span>     |
| [17-Virtual Environments (venv)](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/17-Virtual%20Environments%20%28venv%29.ipynb) | Creating isolated Python environments and managing dependencies with requirements.txt. |             | <span style="color:green;">Beginner 🟢</span>      |
| [18-Dependency Management with Poetry](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/18-Dependency%20Management%20with%20Poetry.ipynb) | Modern package management, working with pyproject.toml, and lock files.              |             | <span style="color:yellow;">Intermediate 🟡</span> |
| [19-Git Fundamentals](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/19-Git%20Fundamentals.ipynb) | Version control basics: init, add, commit, status, branching, and merging.           |             | <span style="color:green;">Beginner 🟢</span>      |
| [20-Github & Collaboration](/Section%2001-Python%20Programming,%20Git%20&%20Environment%20Management/20-Github%20&%20Collaboration.ipynb) | Remote repositories, push, pull, cloning, .gitignore, and Pull Request workflows.    |             | <span style="color:yellow;">Intermediate 🟡</span> |

#### 📏 Section 2 - Mathematics & Statistics with R

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [00-R & Visual Studio Code Installation](/Section%2002-Mathematics%20&%20Statistics%20with%20R/00-R%20&%20Visual%20Studio%20Code%20Installation.ipynb) | Installing R, VS Code, and preparing a statistical computing environment. | | <span style="color:green;">Beginner 🟢</span> |
| [01-Getting Started with R](/Section%2002-Mathematics%20&%20Statistics%20with%20R/01-Getting%20Started%20with%20R.ipynb) | Syntax, vectors, lists, factors, and working with the R console. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Mathematical Notation in R](/Section%2002-Mathematics%20&%20Statistics%20with%20R/02-Mathematical%20Notation%20in%20R.ipynb) | Expression writing, operator usage, and mathematical conventions. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Basic Arithmetic and Algebra](/Section%2002-Mathematics%20&%20Statistics%20with%20R/03-Basic%20Arithmetic%20and%20Algebra.ipynb) | Arithmetic review, algebraic identities, and statistical notation. | | <span style="color:green;">Beginner 🟢</span> |
| [04-Functions, Graphs, and Transformations](/Section%2002-Mathematics%20&%20Statistics%20with%20R/04-Functions,%20Graphs,%20and%20Transformations.ipynb) | Function behavior, graphical interpretation, and transformation rules. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Basics of Linear Algebra](/Section%2002-Mathematics%20&%20Statistics%20with%20R/05-Basics%20of%20Linear%20Algebra.ipynb) | Vectors, matrices, matrix multiplication, and linear systems. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Calculus and Optimization](/Section%2002-Mathematics%20&%20Statistics%20with%20R/06-Calculus%20and%20Optimization.ipynb) | Derivatives, integrals, gradient intuition, and optimization methods. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Introduction to Probability Theory](/Section%2002-Mathematics%20&%20Statistics%20with%20R/07-Introduction%20to%20Probability%20Theory.ipynb) | Probability axioms, conditional probability, and Bayes reasoning. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [08-Descriptive Statistics and Data Summary](/Section%2002-Mathematics%20&%20Statistics%20with%20R/08-Descriptive%20Statistics%20and%20Data%20Summary.ipynb) | Center, spread, quantiles, distribution summaries, and charts. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [09-Basics of Data Visualization](/Section%2002-Mathematics%20&%20Statistics%20with%20R/09-Basics%20of%20Data%20Visualization.ipynb) | Core plotting principles and visual data communication in R. | | <span style="color:green;">Beginner 🟢</span> |
| [10-Basic Probability Distributions](/Section%2002-Mathematics%20&%20Statistics%20with%20R/10-Basic%20Probability%20Distributions.ipynb) | Normal, binomial, Poisson, uniform, and related distributions. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [11-Central Limit Theorem and Sampling](/Section%2002-Mathematics%20&%20Statistics%20with%20R/11-Central%20Limit%20Theorem%20and%20Sampling.ipynb) | Sampling distributions, standard error, and CLT-based inference. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Introduction to Hypothesis Testing](/Section%2002-Mathematics%20&%20Statistics%20with%20R/12-Introduction%20to%20Hypothesis%20Testing.ipynb) | Null hypothesis setup, p-values, Type I/II errors, and decision rules. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [13-Test Selection Flowchart](/Section%2002-Mathematics%20&%20Statistics%20with%20R/13-Test%20Selection%20Flowchart.ipynb) | Structured statistical test selection by data type and assumptions. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [14-Two-Group Comparisons](/Section%2002-Mathematics%20&%20Statistics%20with%20R/14-Two-Group%20Comparisons.ipynb) | t-test families, non-parametric alternatives, and effect size basics. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [15-Comparisons for Three or More Groups](/Section%2002-Mathematics%20&%20Statistics%20with%20R/15-Comparisons%20for%20Three%20or%20More%20Groups.ipynb) | ANOVA families, non-parametric alternatives, and group-wise interpretation. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [16-Assumption Checks](/Section%2002-Mathematics%20&%20Statistics%20with%20R/16-Assumption%20Checks.ipynb) | Normality, homogeneity, independence, and diagnostic checks before testing. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [17-Post-hoc Analyses and Effect Size](/Section%2002-Mathematics%20&%20Statistics%20with%20R/17-Post-hoc%20Analyses%20and%20Effect%20Size.ipynb) | Multiple-comparison procedures and practical significance interpretation. | | <span style="color:orange;">Advanced 🟠</span> |
| [18-Correlation and Causality](/Section%2002-Mathematics%20&%20Statistics%20with%20R/18-Correlation%20and%20Causality.ipynb) | Correlation metrics, confounding, and causal interpretation limits. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [19-Introduction to Regression Analysis](/Section%2002-Mathematics%20&%20Statistics%20with%20R/19-Introduction%20to%20Regression%20Analysis.ipynb) | Simple linear regression concepts, fitting, and interpretation basics. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [20-Multiple Linear Regression](/Section%2002-Mathematics%20&%20Statistics%20with%20R/20-Multiple%20Linear%20Regression.ipynb) | Multivariable modeling, coefficients, assumptions, and diagnostics. | | <span style="color:orange;">Advanced 🟠</span> |
| [21-Logistic Regression](/Section%2002-Mathematics%20&%20Statistics%20with%20R/21-Logistic%20Regression.ipynb) | Binary outcome modeling, odds interpretation, and model evaluation. | | <span style="color:orange;">Advanced 🟠</span> |
| [22-Introduction to Time Series Analysis](/Section%2002-Mathematics%20&%20Statistics%20with%20R/22-Introduction%20to%20Time%20Series%20Analysis.ipynb) | Time-indexed data foundations, trend/seasonality, and temporal structure. | | <span style="color:orange;">Advanced 🟠</span> |
| [23-Generalized Linear Models (GLM) and Advanced Techniques](/Section%2002-Mathematics%20&%20Statistics%20with%20R/23-Generalized%20Linear%20Models%20%28GLM%29%20and%20Advanced%20Techniques.ipynb) | GLM families, link functions, and advanced statistical modeling techniques. | | <span style="color:orange;">Advanced 🟠</span> |
| [24-Model Evaluation and Comparison](/Section%2002-Mathematics%20&%20Statistics%20with%20R/24-Model%20Evaluation%20and%20Comparison.ipynb) | Comparing statistical models with fit metrics and validation criteria. | | <span style="color:orange;">Advanced 🟠</span> |

#### 🗄️ Section 3 - SQL & NoSQL Databases

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Relational Database Foundations](/Section%2003-SQL%20&%20NoSQL%20Databases/01-Relational%20Database%20Foundations.ipynb) | Tables, keys, relationships, constraints, and normalization basics. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Data Definition and Schema Design (CREATE-ALTER)](/Section%2003-SQL%20&%20NoSQL%20Databases/02-Data%20Definition%20and%20Schema%20Design%20%28CREATE-ALTER%29.ipynb) | CREATE/ALTER/DROP, schema modeling, and database evolution. | | <span style="color:green;">Beginner 🟢</span> |
| [03-SQL Query Fundamentals (SELECT, WHERE, GROUP BY)](/Section%2003-SQL%20&%20NoSQL%20Databases/03-SQL%20Query%20Fundamentals%20%28SELECT,%20WHERE,%20GROUP%20BY%29.ipynb) | SELECT, WHERE, ORDER BY, GROUP BY, HAVING, and expressions. | | <span style="color:green;">Beginner 🟢</span> |
| [04-Joins and Set Operations](/Section%2003-SQL%20&%20NoSQL%20Databases/04-Joins%20and%20Set%20Operations.ipynb) | INNER/LEFT/RIGHT/FULL joins, UNION, INTERSECT, and EXCEPT. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Subqueries and Common Table Expressions (CTEs)](/Section%2003-SQL%20&%20NoSQL%20Databases/05-Subqueries%20and%20Common%20Table%20Expressions%20%28CTEs%29.ipynb) | Nested queries, CTEs, recursive patterns, and readability. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Window Functions for Analytics](/Section%2003-SQL%20&%20NoSQL%20Databases/06-Window%20Functions%20for%20Analytics.ipynb) | Running totals, ranking, lag/lead, and analytic calculations. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [07-Connecting Python to SQL (SQLAlchemy & Pandas)](/Section%2003-SQL%20&%20NoSQL%20Databases/07-Connecting%20Python%20to%20SQL%20%28SQLAlchemy%20&%20Pandas%29.ipynb) | SQLAlchemy integration, Python connectivity, and pandas-driven SQL workflows. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [08-Indexes and Query Performance](/Section%2003-SQL%20&%20NoSQL%20Databases/08-Indexes%20and%20Query%20Performance.ipynb) | Index design, query plans, selectivity, and performance tuning. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [09-Transactions and ACID Principles](/Section%2003-SQL%20&%20NoSQL%20Databases/09-Transactions%20and%20ACID%20Principles.ipynb) | Isolation levels, consistency, rollback, and concurrency control. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [10-NoSQL Databases & MongoDB Fundamentals](/Section%2003-SQL%20&%20NoSQL%20Databases/10-NoSQL%20Databases%20&%20MongoDB%20Fundamentals.ipynb) | Documents, collections, aggregation pipelines, and flexible schema. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [11-Data Modeling for Analytics (Star schemas)](/Section%2003-SQL%20&%20NoSQL%20Databases/11-Data%20Modeling%20for%20Analytics%20%28Star%20schemas%29.ipynb) | Star schemas, dimensions, facts, and analytical query design. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Security, Roles, and Access Control](/Section%2003-SQL%20&%20NoSQL%20Databases/12-Security,%20Roles,%20and%20Access%20Control.ipynb) | Roles, permissions, injection prevention, and least privilege. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-Stored Procedures, Functions, and Triggers](/Section%2003-SQL%20&%20NoSQL%20Databases/13-Stored%20Procedures,%20Functions,%20and%20Triggers.ipynb) | Encapsulating business logic inside the database layer. | | <span style="color:orange;">Advanced 🟠</span> |
| [14-Backup, Recovery, and Replication](/Section%2003-SQL%20&%20NoSQL%20Databases/14-Backup,%20Recovery,%20and%20Replication.ipynb) | High availability, disaster recovery, and data durability patterns. | | <span style="color:red;">Expert 🔴</span> |

#### 📊 Section 4 - NumPy & Pandas

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Introduction to NumPy and Arrays](/Section%2004-Numpy%20&%20Pandas/01-Introduction%20to%20NumPy%20and%20Arrays.ipynb) | Array creation, shape, dtype, dimensionality, and array metadata. | | <span style="color:green;">Beginner 🟢</span> |
| [02-NumPy Indexing, Slicing, and Fancy Indexing](/Section%2004-Numpy%20&%20Pandas/02-NumPy%20Indexing,%20Slicing,%20and%20Fancy%20Indexing.ipynb) | Scalar access, slicing, boolean masks, and advanced selection patterns. | | <span style="color:green;">Beginner 🟢</span> |
| [03-NumPy Data Manipulation](/Section%2004-Numpy%20&%20Pandas/03-NumPy%20Data%20Manipulation.ipynb) | Reshaping, stacking, concatenation, flattening, and transposition. | | <span style="color:green;">Beginner 🟢</span> |
| [04-NumPy Mathematical and Statistical Functions](/Section%2004-Numpy%20&%20Pandas/04-NumPy%20Mathematical%20and%20Statistical%20Functions.ipynb) | Ufuncs, aggregates, linear algebra, and element-wise transformations. | | <span style="color:green;">Beginner 🟢</span> |
| [05-NumPy Performance Techniques and Broadcasting](/Section%2004-Numpy%20&%20Pandas/05-NumPy%20Performance%20Techniques%20and%20Broadcasting.ipynb) | Vectorization, broadcasting, memory behavior, and speed-aware design. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Introduction to Pandas Series and DataFrames](/Section%2004-Numpy%20&%20Pandas/06-Introduction%20to%20Pandas%20Series%20and%20DataFrames.ipynb) | Series, DataFrame structure, indexes, and data inspection. | | <span style="color:green;">Beginner 🟢</span> |
| [07-Selecting, Filtering, and Indexing Data in Pandas](/Section%2004-Numpy%20&%20Pandas/07-Selecting,%20Filtering,%20and%20Indexing%20Data%20in%20Pandas.ipynb) | loc, iloc, boolean filters, column selection, and slicing. | | <span style="color:green;">Beginner 🟢</span> |
| [08-Data Cleaning and Handling Missing Data with Pandas](/Section%2004-Numpy%20&%20Pandas/08-Data%20Cleaning%20and%20Handling%20Missing%20Data%20with%20Pandas.ipynb) | Missing values, replacement strategies, imputation, and data validation. | | <span style="color:green;">Beginner 🟢</span> |
| [09-Data Transformation and Manipulation in Pandas](/Section%2004-Numpy%20&%20Pandas/09-Data%20Transformation%20and%20Manipulation%20in%20Pandas.ipynb) | Renaming, derived columns, type casting, apply, map, and sorting. | | <span style="color:green;">Beginner 🟢</span> |
| [10-Grouping and Aggregation in Pandas (groupby)](/Section%2004-Numpy%20&%20Pandas/10-Grouping%20and%20Aggregation%20in%20Pandas%20%28groupby%29.ipynb) | Group-wise summaries, aggregations, transformations, and filtering. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [11-Merging and Joining DataFrames in Pandas](/Section%2004-Numpy%20&%20Pandas/11-Merging%20and%20Joining%20DataFrames%20in%20Pandas.ipynb) | Merge strategies, join types, concatenation, and relational matching. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [12-Time Series and Date Handling in Pandas](/Section%2004-Numpy%20&%20Pandas/12-Time%20Series%20and%20Date%20Handling%20in%20Pandas.ipynb) | Datetime indexes, resampling, offsets, periods, and calendar handling. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [13-MultiIndex and Advanced Data Structures in Pandas](/Section%2004-Numpy%20&%20Pandas/13-MultiIndex%20and%20Advanced%20Data%20Structures%20in%20Pandas.ipynb) | Hierarchical indexing, reshaping, and advanced tabular organization. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [14-Performance Optimization with NumPy and Pandas](/Section%2004-Numpy%20&%20Pandas/14-Performance%20Optimization%20with%20NumPy%20and%20Pandas.ipynb) | Categorical data, chunking, vectorization, and efficient workflows. | | <span style="color:yellow;">Intermediate 🟡</span> |

#### 🔍 Section 5 - Feature Engineering & Data Preprocessing

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Data Profiling and Quality Checks](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/01-Data%20Profiling%20and%20Quality%20Checks.ipynb) | Data types, uniqueness, duplicates, nulls, and summary statistics. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Missing Value Treatment](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/02-Missing%20Value%20Treatment.ipynb) | Deletion, imputation, and model-specific strategies for nulls. | | <span style="color:green;">Beginner 🟢</span> |
| [03-Outlier Detection and Robust Handling](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/03-Outlier%20Detection%20and%20Robust%20Handling.ipynb) | IQR, z-score, winsorization, and anomaly-aware preprocessing. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Scaling and Normalization](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/04-Scaling%20and%20Normalization.ipynb) | Standardization, min-max scaling, robust scaling, and their tradeoffs. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Categorical Encoding](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/05-Categorical%20Encoding.ipynb) | One-hot, ordinal, target, hashing, and embedding-style encoding. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Binning and Discretization](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/06-Binning%20and%20Discretization.ipynb) | Turning continuous variables into informative buckets. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Feature Construction](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/07-Feature%20Construction.ipynb) | Polynomial terms, interactions, ratios, and domain-driven features. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Feature Selection & PCA](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/08-Feature%20Selection%20&%20PCA.ipynb) | Filter, wrapper, and embedded methods for reducing dimensionality. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Target Leakage Prevention](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/09-Target%20Leakage%20Prevention.ipynb) | Leakage patterns, time-aware splits, and safer pipeline design. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-Pipeline Engineering (scikit-learn)](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/10-Pipeline%20Engineering%20%28scikit-learn%29.ipynb) | Reusable transformations, train/test consistency, and reproducibility. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-Handling Imbalanced Data](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/11-Handling%20Imbalanced%20Data.ipynb) | Resampling, class weights, and preprocessing for skewed targets. | | <span style="color:red;">Expert 🔴</span> |
| [12-Temporal Feature Engineering](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/12-Temporal%20Feature%20Engineering.ipynb) | Lag features, rolling statistics, and date-derived signals. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-Text and Categorical Cleaning (Advanced)](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/13-Text%20and%20Categorical%20Cleaning%20%28Advanced%29.ipynb) | Standardizing labels, handling rare categories, and normalization. | | <span style="color:red;">Expert 🔴</span> |
| [14-Feature Stores and Reuse](/Section%2005-Feature%20Engineering%20&%20Data%20Preprocessing/14-Feature%20Stores%20and%20Reuse.ipynb) | Persisting engineered features for repeatable model training. | | <span style="color:red;">Expert 🔴</span> |

#### 📊 Section 6 - Data Visualization & Business Intelligence

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Visualization Principles](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/01-Visualization%20Principles.ipynb) | Chart selection, visual hierarchy, and reducing noise. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Exploratory Visual Analysis](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/02-Exploratory%20Visual%20Analysis.ipynb) | Distribution, relationship, and comparison plots for EDA. | | <span style="color:green;">Beginner 🟢</span> |
| [03-Color, Layout, and Accessibility](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/03-Color%2C%20Layout%2C%20and%20Accessibility.ipynb) | Palette choice, contrast, annotations, and readability. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Advanced Chart Types](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/04-Advanced%20Chart%20Types.ipynb) | Heatmaps, small multiples, network visuals, and layered plots. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Geospatial Visualization](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/05-Geospatial%20Visualization.ipynb) | Maps, coordinates, and location-aware storytelling. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Exploratory Storyboarding](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/06-Exploratory%20Storyboarding.ipynb) | Structuring plots into a coherent analytical flow. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Storytelling with Dashboards](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/07-Storytelling%20with%20Dashboards.ipynb) | Sequencing insights and building stakeholder-ready narratives. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [08-Tableau Calculated Fields](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/08-Tableau%20Calculated%20Fields.ipynb) | Table calculations, parameters, and reusable logic in Tableau. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [09-Interactive Dashboards](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/09-Interactive%20Dashboards.ipynb) | Filters, actions, drill-downs, and interactive exploration. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [10-Advanced Tableau Modeling](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/10-Advanced%20Tableau%20Modeling.ipynb) | Data blending, extracts, and performance-aware dashboard design. | | <span style="color:red;">Expert 🔴</span> |
| [11-Operational Reporting](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/11-Operational%20Reporting.ipynb) | KPI design, refresh cadence, and executive reporting patterns. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Publishing and Sharing](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/12-Publishing%20and%20Sharing.ipynb) | Deployment, permissions, and governance for visual assets. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-Visualization QA and UX](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/13-Visualization%20QA%20and%20UX.ipynb) | Validation, labeling, and dashboard usability checks. | | <span style="color:red;">Expert 🔴</span> |
| [14-Visual Analytics Governance](/Section%2006-Data%20Visualization%20&%20Business%20Intelligence/14-Visual%20Analytics%20Governance.ipynb) | Definition of KPIs, source-of-truth control, and dashboard maintenance. | | <span style="color:red;">Expert 🔴</span> |

#### 🤖 Section 7 - Machine Learning Fundamentals

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-ML Problem Framing](/Section%2007-Machine%20Learning%20Fundamentals/01-ML%20Problem%20Framing.ipynb) | Problem definition, success metrics, and business alignment. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Gradient Descent & Optimization](/Section%2007-Machine%20Learning%20Fundamentals/02-Gradient%20Descent%20&%20Optimization.ipynb) | Optimization algorithms, learning rates, and convergence. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Linear Regression](/Section%2007-Machine%20Learning%20Fundamentals/03-Linear%20Regression.ipynb) | Regression basics, least squares, and interpretation. | | <span style="color:green;">Beginner 🟢</span> |
| [04-Logistic Regression](/Section%2007-Machine%20Learning%20Fundamentals/04-Logistic%20Regression.ipynb) | Binary classification, odds, and probability calibration. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Distance Models (KNN)](/Section%2007-Machine%20Learning%20Fundamentals/05-Distance%20Models%20%28KNN%29.ipynb) | Instance-based learning, distance metrics, and KNN. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Support Vector Machines](/Section%2007-Machine%20Learning%20Fundamentals/06-Support%20Vector%20Machines.ipynb) | Margin maximization, kernels, and SVM workflows. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Naive Bayes](/Section%2007-Machine%20Learning%20Fundamentals/07-Naive%20Bayes.ipynb) | Probabilistic classification and conditional independence. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [08-Decision Trees](/Section%2007-Machine%20Learning%20Fundamentals/08-Decision%20Trees.ipynb) | Tree construction, splitting criteria, and interpretability. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [09-Bias-Variance & Regularization](/Section%2007-Machine%20Learning%20Fundamentals/09-Bias-Variance%20&%20Regularization.ipynb) | Underfitting, overfitting, and generalization control. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [10-Ensemble: Bagging](/Section%2007-Machine%20Learning%20Fundamentals/10-Ensemble%3A%20Bagging.ipynb) | Bootstrap aggregating and parallel ensemble methods. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-Ensemble: Boosting](/Section%2007-Machine%20Learning%20Fundamentals/11-Ensemble%3A%20Boosting.ipynb) | Sequential ensemble building and gradient boosting. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Unsupervised: Clustering](/Section%2007-Machine%20Learning%20Fundamentals/12-Unsupervised%3A%20Clustering.ipynb) | K-means, hierarchical clustering, and cluster evaluation. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-Unsupervised: Dimensionality](/Section%2007-Machine%20Learning%20Fundamentals/13-Unsupervised%3A%20Dimensionality.ipynb) | PCA, manifold learning, and dimensionality reduction. | | <span style="color:orange;">Advanced 🟠</span> |
| [14-Model Evaluation & Validation](/Section%2007-Machine%20Learning%20Fundamentals/14-Model%20Evaluation%20&%20Validation.ipynb) | Cross-validation, metrics, and model selection. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [15-Classification Metrics](/Section%2007-Machine%20Learning%20Fundamentals/15-Classification%20Metrics.ipynb) | Precision, recall, F1, ROC-AUC, and threshold selection. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [16-Hyperparameter Tuning](/Section%2007-Machine%20Learning%20Fundamentals/16-Hyperparameter%20Tuning.ipynb) | Grid search, random search, and Bayesian optimization. | | <span style="color:orange;">Advanced 🟠</span> |
| [17-Multiclass and Multilabel](/Section%2007-Machine%20Learning%20Fundamentals/17-Multiclass%20and%20Multilabel.ipynb) | Multi-class classification and multilabel strategies. | | <span style="color:orange;">Advanced 🟠</span> |
| [18-Probability Calibration](/Section%2007-Machine%20Learning%20Fundamentals/18-Probability%20Calibration.ipynb) | Calibration methods and reliability diagrams. | | <span style="color:orange;">Advanced 🟠</span> |
| [19-Building ML Pipelines](/Section%2007-Machine%20Learning%20Fundamentals/19-Building%20ML%20Pipelines.ipynb) | End-to-end pipeline design and reproducibility. | | <span style="color:orange;">Advanced 🟠</span> |
| [20-Model Interpretability](/Section%2007-Machine%20Learning%20Fundamentals/20-Model%20Interpretability.ipynb) | Feature importance, SHAP, LIME, and explainability. | | <span style="color:red;">Expert 🔴</span> |
| [21-MLOps: Serialization](/Section%2007-Machine%20Learning%20Fundamentals/21-MLOps%3A%20Serialization.ipynb) | Model saving, loading, and deployment packaging. | | <span style="color:orange;">Advanced 🟠</span> |
| [22-MLOps: Experiment Tracking](/Section%2007-Machine%20Learning%20Fundamentals/22-MLOps%3A%20Experiment%20Tracking.ipynb) | MLflow, experiment logging, and model versioning. | | <span style="color:orange;">Advanced 🟠</span> |

#### ⏳ Section 8 - Time Series Analysis & Forecasting

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Time Series Problem Framing](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/01-Time%20Series%20Problem%20Framing.ipynb) | Problem definition, horizons, and baseline strategies. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Components & Decomposition](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/02-Components%20%26%20Decomposition.ipynb) | Trend/seasonality decomposition and component analysis. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Exploratory Time Series Analysis](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/03-Exploratory%20Time%20Series%20Analysis.ipynb) | Decomposition, ACF/PACF inspection, and diagnostics. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Autocorrelation (ACF-PACF)](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/04-Autocorrelation%20%28ACF-PACF%29.ipynb) | ACF/PACF interpretation and lag selection. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Stationarity & Differencing](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/05-Stationarity%20%26%20Differencing.ipynb) | Unit roots, tests, and differencing strategies. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Temporal Feature Engineering](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/06-Temporal%20Feature%20Engineering.ipynb) | Lag/window features, calendar effects, and encodings. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Lag & Window Features](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/07-Lag%20%26%20Window%20Features.ipynb) | Rolling statistics, expanding windows, and feature lags. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Classic: Exponential Smoothing](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/08-Classic%3A%20Exponential%20Smoothing.ipynb) | Simple/seasonal exponential smoothing and Holt-Winters. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Classic: ARIMA Models](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/09-Classic%3A%20ARIMA%20Models.ipynb) | ARIMA identification, estimation, and forecasting. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-Classic: SARIMAX](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/10-Classic%3A%20SARIMAX.ipynb) | Seasonal ARIMA with exogenous regressors. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-Time Series Validation Strategies](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/11-Time%20Series%20Validation%20Strategies.ipynb) | Walk-forward validation, backtesting, and horizons. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Forecasting Metrics](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/12-Forecasting%20Metrics.ipynb) | MAPE, RMSE, MAE, and probabilistic metrics. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-ML Forecasting (Tabularization)](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/13-ML%20Forecasting%20%28Tabularization%29.ipynb) | Converting series to supervised tabular format for ML. | | <span style="color:orange;">Advanced 🟠</span> |
| [14-Global vs. Local Models](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/14-Global%20vs.%20Local%20Models.ipynb) | Model per-series vs pooled/global approaches. | | <span style="color:orange;">Advanced 🟠</span> |
| [15-Multivariate Forecasting (VAR)](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/15-Multivariate%20Forecasting%20%28VAR%29.ipynb) | VAR models and multivariate temporal dependencies. | | <span style="color:orange;">Advanced 🟠</span> |
| [16-Deep Learning: LSTMs](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/16-Deep%20Learning%3A%20LSTMs.ipynb) | Sequence models, LSTM architectures, and training tips. | | <span style="color:orange;">Advanced 🟠</span> |
| [17-Deep Learning: Transformers](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/17-Deep%20Learning%3A%20Transformers.ipynb) | Transformer-based time series models and attention. | | <span style="color:orange;">Advanced 🟠</span> |
| [18-Hierarchical Forecasting](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/18-Hierarchical%20Forecasting.ipynb) | Reconciliation, aggregation, and bottom-up/top-down methods. | | <span style="color:red;">Expert 🔴</span> |
| [19-Uncertainty Quantification](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/19-Uncertainty%20Quantification.ipynb) | Prediction intervals, quantiles, and probabilistic forecasts. | | <span style="color:red;">Expert 🔴</span> |
| [20-Anomaly Detection in Time](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/20-Anomaly%20Detection%20in%20Time.ipynb) | Detecting temporal anomalies and change points. | | <span style="color:red;">Expert 🔴</span> |
| [21-MLOps: Continuous Backtesting](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/21-MLOps%3A%20Continuous%20Backtesting.ipynb) | Automated backtests, scheduling, and monitoring. | | <span style="color:red;">Expert 🔴</span> |
| [22-MLOps: Operationalization](/Section%2008-Time%20Series%20Analysis%20%26%20Forecasting/22-MLOps%3A%20Operationalization.ipynb) | Serving, retraining, and production considerations. | | <span style="color:red;">Expert 🔴</span> |

#### 🧠 Section 9 - Deep Learning & Neural Networks

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Tensor Mathematics](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/01-Tensor%20Mathematics.ipynb) | Tensor operations and linear algebra foundations for DL. | | <span style="color:green;">Beginner 🟢</span> |
| [02-The Artificial Neuron](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/02-The%20Artificial%20Neuron.ipynb) | Neuron model, weights, bias, and activation intuition. | | <span style="color:green;">Beginner 🟢</span> |
| [03-Activation Functions](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/03-Activation%20Functions.ipynb) | Common activations and their properties. | | <span style="color:green;">Beginner 🟢</span> |
| [04-Multi-Layer Perceptrons](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/04-Multi-Layer%20Perceptrons.ipynb) | MLP architectures and feedforward networks. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Loss Functions](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/05-Loss%20Functions.ipynb) | Loss choices and their effects on training. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Gradient Descent](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/06-Gradient%20Descent.ipynb) | Optimization basics and learning dynamics. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [07-Backpropagation](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/07-Backpropagation.ipynb) | Backprop algorithm and computational graph derivatives. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [08-Auto-Differentiation](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/08-Auto-Differentiation.ipynb) | Autograd mechanics and practical tips. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [09-Batches & DataLoaders](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/09-Batches%20%26%20DataLoaders.ipynb) | Mini-batching, loaders, and efficient data pipelines. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [10-Advanced Optimizers](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/10-Advanced%20Optimizers.ipynb) | Adam, RMSProp, and optimizer variants. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-The Training Loop](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/11-The%20Training%20Loop.ipynb) | Epochs, steps, evaluation, and debugging loops. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Gradient Instability](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/12-Gradient%20Instability.ipynb) | Vanishing/exploding gradients and remedies. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-Weight Initialization](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/13-Weight%20Initialization.ipynb) | Initialization schemes and their impact. | | <span style="color:orange;">Advanced 🟠</span> |
| [14-Regularization: Dropout](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/14-Regularization%3A%20Dropout.ipynb) | Dropout and other regularization techniques. | | <span style="color:orange;">Advanced 🟠</span> |
| [15-Normalization Layers](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/15-Normalization%20Layers.ipynb) | BatchNorm, LayerNorm and training stability. | | <span style="color:orange;">Advanced 🟠</span> |
| [16-Learning Rate Scheduling](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/16-Learning%20Rate%20Scheduling.ipynb) | Schedulers, warmup, and cyclic strategies. | | <span style="color:orange;">Advanced 🟠</span> |
| [17-Handling Imbalanced Data](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/17-Handling%20Imbalanced%20Data.ipynb) | Techniques for class imbalance in DL. | | <span style="color:orange;">Advanced 🟠</span> |
| [18-Deep Learning Diagnostics](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/18-Deep%20Learning%20Diagnostics.ipynb) | Training diagnostics, visualizations, and fixes. | | <span style="color:orange;">Advanced 🟠</span> |
| [19-Hardware Acceleration](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/19-Hardware%20Acceleration.ipynb) | GPUs, mixed precision, and performance tips. | | <span style="color:red;">Expert 🔴</span> |
| [20-Callbacks & Checkpointing](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/20-Callbacks%20%26%20Checkpointing.ipynb) | Checkpoints, callbacks, and training utilities. | | <span style="color:orange;">Advanced 🟠</span> |
| [21-Model Serialization](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/21-Model%20Serialization.ipynb) | Saving/loading models and portable formats. | | <span style="color:orange;">Advanced 🟠</span> |
| [22-Multi-Task Architectures](/Section%2009-Deep%20Learning%20%26%20Neural%20Networks/22-Multi-Task%20Architectures.ipynb) | Multi-head and multi-task model designs. | | <span style="color:orange;">Advanced 🟠</span> |

#### 👀 Section 10 - Computer Vision & Generative Models

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Pixels, Tensors & Color Spaces](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/01-Pixels,%20Tensors%20%26%20Color%20Spaces.ipynb) | Image representation, color spaces, and pixel operations. | | <span style="color:green;">Beginner 🟢</span> |
| [02-The Math of Convolutions](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/02-The%20Math%20of%20Convolutions.ipynb) | Convolution math and filter interpretation. | | <span style="color:green;">Beginner 🟢</span> |
| [03-Pooling & Receptive Fields](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/03-Pooling%20%26%20Receptive%20Fields.ipynb) | Pooling operations and receptive field concepts. | | <span style="color:green;">Beginner 🟢</span> |
| [04-Architecting CNNs in PyTorch](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/04-Architecting%20CNNs%20in%20PyTorch.ipynb) | Building CNNs and best practices in PyTorch. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Enterprise Backbones](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/05-Enterprise%20Backbones.ipynb) | Backbone architectures and pretrained models. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Transfer Learning & Fine-Tuning](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/06-Transfer%20Learning%20%26%20Fine-Tuning.ipynb) | Fine-tuning strategies and transfer learning workflows. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Vision Data Pipelines](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/07-Vision%20Data%20Pipelines.ipynb) | Augmentation, dataset versioning, and loaders. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Object Detection I: Metrics](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/08-Object%20Detection%20I%3A%20Metrics.ipynb) | Detection metrics, IoU, and evaluation. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Object Detection II: Architectures](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/09-Object%20Detection%20II%3A%20Architectures.ipynb) | One-stage vs two-stage detectors and modern models. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-Semantic Segmentation](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/10-Semantic%20Segmentation.ipynb) | Pixel-wise labeling and segmentation architectures. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-Vision Transformers (ViT).](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/11-Vision%20Transformers%20%28ViT%29.ipynb) | Transformer models for vision tasks. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Autoencoders & Latent Space](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/12-Autoencoders%20%26%20Latent%20Space.ipynb) | Representation learning with autoencoders. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-Variational Autoencoders (VAEs).](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/13-Variational%20Autoencoders%20%28VAEs%29.ipynb) | Probabilistic autoencoders and latent sampling. | | <span style="color:orange;">Advanced 🟠</span> |
| [14-Generative Adversarial Networks](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/14-Generative%20Adversarial%20Networks.ipynb) | GAN training, loss dynamics, and stability. | | <span style="color:orange;">Advanced 🟠</span> |
| [15-Advanced GANs & Pitfalls](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/15-Advanced%20GANs%20%26%20Pitfalls.ipynb) | Improved architectures and common failure modes. | | <span style="color:red;">Expert 🔴</span> |
| [16-Diffusion Models I: The Math](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/16-Diffusion%20Models%20I%3A%20The%20Math.ipynb) | Theory of diffusion-based generative models. | | <span style="color:red;">Expert 🔴</span> |
| [17-Diffusion Models II: Latent Diffusion](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/17-Diffusion%20Models%20II%3A%20Latent%20Diffusion.ipynb) | Practical latent diffusion pipelines and training. | | <span style="color:red;">Expert 🔴</span> |
| [18-Image-to-Image & ControlNet](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/18-Image-to-Image%20%26%20ControlNet.ipynb) | Conditional generation and control mechanisms. | | <span style="color:red;">Expert 🔴</span> |
| [19-Generative Evaluation](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/19-Generative%20Evaluation.ipynb) | Metrics for generative model quality and diversity. | | <span style="color:red;">Expert 🔴</span> |
| [20-Edge Vision & Quantization](/Section%2010-Computer%20Vision%20%26%20Generative%20Models/20-Edge%20Vision%20%26%20Quantization.ipynb) | Compression, quantization, and on-device inference. | | <span style="color:red;">Expert 🔴</span> |

#### 🗣️ Section 11 - NLP, Transformers & LLMs

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Tokenization & Text Math](/Section%2011-NLP,%20Transformers%20%26%20LLMs/01-Tokenization%20%26%20Text%20Math.ipynb) | Tokenization, vocab, and text-to-token math. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Vector Semantics](/Section%2011-NLP,%20Transformers%20%26%20LLMs/02-Vector%20Semantics.ipynb) | Embedding spaces, similarity, and semantic search basics. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-RNNs & Vanishing Gradients](/Section%2011-NLP,%20Transformers%20%26%20LLMs/03-RNNs%20%26%20Vanishing%20Gradients.ipynb) | Sequence models and gradient stability issues. | | <span style="color:orange;">Advanced 🟠</span> |
| [04-Seq2Seq & Early Attention](/Section%2011-NLP,%20Transformers%20%26%20LLMs/04-Seq2Seq%20%26%20Early%20Attention.ipynb) | Encoder-decoder workflows and attention intro. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Transformers I: Self-Attention](/Section%2011-NLP,%20Transformers%20%26%20LLMs/05-Transformers%20I%3A%20Self-Attention.ipynb) | Self-attention mechanisms and scaled dot-product math. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Transformers II: Architecture](/Section%2011-NLP,%20Transformers%20%26%20LLMs/06-Transformers%20II%3A%20Architecture.ipynb) | Full transformer stacks, positional encodings, and blocks. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Encoder Models (BERT).](/Section%2011-NLP,%20Transformers%20%26%20LLMs/07-Encoder%20Models%20%28BERT%29.ipynb) | Encoder-only models and masked-language pretraining. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Decoder Models (GPT).](/Section%2011-NLP,%20Transformers%20%26%20LLMs/08-Decoder%20Models%20%28GPT%29.ipynb) | Causal decoding, autoregression, and next-token modelling. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Decoding Strategies](/Section%2011-NLP,%20Transformers%20%26%20LLMs/09-Decoding%20Strategies.ipynb) | Greedy, beam, sampling, temperature and practical tradeoffs. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-Task Fine-Tuning](/Section%2011-NLP,%20Transformers%20%26%20LLMs/10-Task%20Fine-Tuning.ipynb) | Supervised fine-tuning patterns for downstream tasks. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-PEFT & LoRA Mathematics](/Section%2011-NLP,%20Transformers%20%26%20LLMs/11-PEFT%20%26%20LoRA%20Mathematics.ipynb) | Parameter-efficient fine-tuning techniques and math. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Quantized LLMs (QLoRA).](/Section%2011-NLP,%20Transformers%20%26%20LLMs/12-Quantized%20LLMs%20%28QLoRA%29.ipynb) | Quantization strategies for LLM inference. | | <span style="color:red;">Expert 🔴</span> |
| [13-Instruction Tuning (SFT).](/Section%2011-NLP,%20Transformers%20%26%20LLMs/13-Instruction%20Tuning%20%28SFT%29.ipynb) | Supervised instruction datasets and tuning workflows. | | <span style="color:red;">Expert 🔴</span> |
| [14-LLM Alignment (RLHF & DPO).](/Section%2011-NLP,%20Transformers%20%26%20LLMs/14-LLM%20Alignment%20%28RLHF%20%26%20DPO%29.ipynb) | Alignment strategies using RLHF and direct policy optimization. | | <span style="color:red;">Expert 🔴</span> |
| [15-NLP Evaluation Metrics](/Section%2011-NLP,%20Transformers%20%26%20LLMs/15-NLP%20Evaluation%20Metrics.ipynb) | BLEU, ROUGE, BERTScore and human-eval practices. | | <span style="color:orange;">Advanced 🟠</span> |

#### 🌐 Section 12 - REST APIs, FastAPI & AI Prototyping

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Rapid Prototyping (Gradio).](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/01-Rapid%20Prototyping%20%28Gradio%29.ipynb) | Quick demo UIs and interactive prototyping with Gradio. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Stateful AI UIs (Streamlit).](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/02-Stateful%20AI%20UIs%20%28Streamlit%29.ipynb) | Building stateful interfaces for model interaction. | | <span style="color:green;">Beginner 🟢</span> |
| [03-FastAPI & REST Physics](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/03-FastAPI%20%26%20REST%20Physics.ipynb) | FastAPI design patterns, routers, and endpoint best practices. | | <span style="color:green;">Beginner 🟢</span> |
| [04-Pydantic for Machine Learning](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/04-Pydantic%20for%20Machine%20Learning.ipynb) | Validation models, schemas, and serialization for ML payloads. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Model Memory & Lifespans](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/05-Model%20Memory%20%26%20Lifespans.ipynb) | Managing model lifecycle, in-memory caches and warmup strategies. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Concurrency & Blocking Inference](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/06-Concurrency%20%26%20Blocking%20Inference.ipynb) | Async endpoints, thread pools, and safe inference patterns. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Token Streaming (Server-Sent Events).](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/07-Token%20Streaming%20%28Server-Sent%20Events%29.ipynb) | Streaming tokens, SSE, and chunked responses. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Vision Endpoints (File I-O)](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/08-Vision%20Endpoints%20%28File%20I-O%29.ipynb) | File uploads, preprocessing, and image model endpoints. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Decoupled Systems](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/09-Decoupled%20Systems.ipynb) | Producer-consumer patterns and traffic shaping for ML services. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-Securing GPU Endpoints](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/10-Securing%20GPU%20Endpoints.ipynb) | Auth, isolation, and secure service exposure for GPU-backed endpoints. | | <span style="color:red;">Expert 🔴</span> |
| [11-Background Batch Processing](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/11-Background%20Batch%20Processing.ipynb) | Offloading heavy jobs and background task orchestration. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Mocking & Testing ML APIs](/Section%2012-REST%20APIs,%20FastAPI%20%26%20AI%20Prototyping/12-Mocking%20%26%20Testing%20ML%20APIs.ipynb) | Test patterns, mocking model responses and CI integration. | | <span style="color:orange;">Advanced 🟠</span> |

#### 🔎 Section 13 - RAG, Vector Databases & Retrieval Systems

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-The Physics of RAG](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/01-The%20Physics%20of%20RAG.ipynb) | RAG conceptual workflow and system building blocks. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Document Parsing & Chunking Math](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/02-Document%20Parsing%20%26%20Chunking%20Math.ipynb) | Chunking strategies, overlap, and semantic segmentation. | | <span style="color:green;">Beginner 🟢</span> |
| [03-Bi-Encoders & Dense Retrieval](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/03-Bi-Encoders%20%26%20Dense%20Retrieval.ipynb) | Bi-encoder training and dense retrieval pipelines. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Vector Databases & Metadata](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/04-Vector%20Databases%20%26%20Metadata.ipynb) | DB choices, schema, and metadata-driven filtering. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-The Mathematics of ANN (HNSW & IVF).](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/05-The%20Mathematics%20of%20ANN%20%28HNSW%20%26%20IVF%29.ipynb) | ANN algorithms and tradeoffs for recall/latency. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Sparse Search & BM25](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/06-Sparse%20Search%20%26%20BM25.ipynb) | BM25 and sparse retrieval techniques. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [07-Hybrid Search & RRF](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/07-Hybrid%20Search%20%26%20RRF.ipynb) | Combining dense and sparse signals for robust retrieval. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Reranking (Cross-Encoders).](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/08-Reranking%20%28Cross-Encoders%29.ipynb) | Cross-encoder reranking and relevance calibration. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Query Transformation (HyDE).](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/09-Query%20Transformation%20%28HyDE%29.ipynb) | Query augmentation and hallucinated document expansion. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-Advanced Context Topologies](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/10-Advanced%20Context%20Topologies.ipynb) | Context assembly strategies and slot-filling topologies. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-GraphRAG Foundations](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/11-GraphRAG%20Foundations.ipynb) | Graph-based retrieval and knowledge augmentation. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Evaluating RAG (RAGAS-TruLens).](/Section%2013-RAG,%20Vector%20Databases%20%26%20Retrieval%20Systems/12-Evaluating%20RAG%20%28RAGAS-TruLens%29.ipynb) | Evaluation frameworks and reliability assessments for RAG. | | <span style="color:orange;">Advanced 🟠</span> |

#### 🧩 Section 14 - LangChain, LangGraph & Multi-Agent Orchestration

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-The Physics of Agentic Workflows](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/01-The%20Physics%20of%20Agentic%20Workflows.ipynb) | Agent lifecycle, planning loops, and orchestration basics. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Function Calling & Tool Execution](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/02-Function%20Calling%20%26%20Tool%20Execution.ipynb) | Safe function calling, tool contracts, and validations. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Structured Output & Pydantic Coercion](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/03-Structured%20Output%20%26%20Pydantic%20Coercion.ipynb) | Reliable schema outputs and coercion strategies. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-LangGraph Foundations (State & Nodes)](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/04-LangGraph%20Foundations%20%28State%20%26%20Nodes%29.ipynb) | Graph-based workflows and node-state modeling. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Cyclic Routing & Conditional Edges](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/05-Cyclic%20Routing%20%26%20Conditional%20Edges.ipynb) | Routing patterns, cycles, and guard conditions. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Cognitive Memory Architectures](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/06-Cognitive%20Memory%20Architectures.ipynb) | Short/long-term memory patterns for agents. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Human-in-the-Loop (HITL) Physics](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/07-Human-in-the-Loop%20%28HITL%29%20Physics.ipynb) | HITL patterns, gating, and feedback loops. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Agentic RAG (CRAG & Self-RAG).](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/08-Agentic%20RAG%20%28CRAG%20%26%20Self-RAG%29.ipynb) | Combining RAG with agent orchestration patterns. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Multi-Agent Network Topologies](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/09-Multi-Agent%20Network%20Topologies.ipynb) | Topologies for agent collaboration and routing. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-The Supervisor Architecture](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/10-The%20Supervisor%20Architecture.ipynb) | Supervisor patterns for orchestration and fault tolerance. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-Resilient Error Handling (LLM Try-Except).](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/11-Resilient%20Error%20Handling%20%28LLM%20Try-Except%29.ipynb) | Robust error handling and retry strategies for agents. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-LangSmith Observability & Tracing](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/12-LangSmith%20Observability%20%26%20Tracing.ipynb) | Observability patterns and tracing agent runs. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-Evaluating Agentic Trajectories](/Section%2014-LangChain,%20LangGraph%20%26%20Multi-Agent%20Orchestration/13-Evaluating%20Agentic%20Trajectories.ipynb) | Metrics and evaluation for multi-agent runs. | | <span style="color:orange;">Advanced 🟠</span> |

#### 🏗️ Section 15 - Data Engineering & ETL Pipelines

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-The Modern Data Stack & ELT Physics](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/01-The%20Modern%20Data%20Stack%20%26%20ELT%20Physics.ipynb) | Modern ELT stacks and data flow architectures. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Dimensional Data Modeling (Kimball).](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/02-Dimensional%20Data%20Modeling%20%28Kimball%29.ipynb) | Star schemas, facts, dimensions, and modeling tradeoffs. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Transformations with dbt (Data Build Tool).](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/03-Transformations%20with%20dbt%20%28Data%20Build%20Tool%29.ipynb) | dbt patterns, models, testing and CI. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Apache Airflow Foundations](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/04-Apache%20Airflow%20Foundations.ipynb) | DAG design, scheduling, and orchestration basics. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Advanced Airflow Orchestration](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/05-Advanced%20Airflow%20Orchestration.ipynb) | Complex DAG patterns, sensors, and backfills. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Incremental Data Loading Physics](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/06-Incremental%20Data%20Loading%20Physics.ipynb) | CDC, idempotency, and incremental ingestion techniques. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Data Quality via Great Expectations](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/07-Data%20Quality%20via%20Great%20Expectations.ipynb) | Data validation, expectations, and test-driven QA. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Change Data Capture (CDC) with Debezium](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/08-Change%20Data%20Capture%20%28CDC%29%20with%20Debezium.ipynb) | CDC patterns and Debezium integration. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Event Streaming with Apache Kafka](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/09-Event%20Streaming%20with%20Apache%20Kafka.ipynb) | Kafka topics, partitions, and stream processing basics. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-The Lakehouse Architecture (Iceberg - Delta).](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/10-The%20Lakehouse%20Architecture%20%28Iceberg%20-%20Delta%29.ipynb) | Lakehouse design, ACID tables and formats. | | <span style="color:red;">Expert 🔴</span> |
| [11-Data Contracts & Schema Registries](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/11-Data%20Contracts%20%26%20Schema%20Registries.ipynb) | Contracts, schema evolution, and governance patterns. | | <span style="color:red;">Expert 🔴</span> |
| [12-Data Observability & Lineage](/Section%2015-Data%20Engineering%20%26%20ETL%20Pipelines/12-Data%20Observability%20%26%20Lineage.ipynb) | Lineage, observability tooling and alerting for data. | | <span style="color:red;">Expert 🔴</span> |

#### ⚡ Section 16 - PySpark & Big Data Processing

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-The Physics of Distributed Compute](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/01-The%20Physics%20of%20Distributed%20Compute.ipynb) | Cluster compute fundamentals and execution models. | | <span style="color:green;">Beginner 🟢</span> |
| [02-The Catalyst Optimizer & Execution Plans](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/02-The%20Catalyst%20Optimizer%20%26%20Execution%20Plans.ipynb) | Query planning, logical/physical plans and optimization. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Partitioning & The Shuffle Penalty](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/03-Partitioning%20%26%20The%20Shuffle%20Penalty.ipynb) | Partitioning strategies and the cost of shuffles. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Distributed Joins & Broadcast Physics](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/04-Distributed%20Joins%20%26%20Broadcast%20Physics.ipynb) | Join strategies and broadcast join tradeoffs. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Vectorized Computation (Apache Arrow).](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/05-Vectorized%20Computation%20%28Apache%20Arrow%29.ipynb) | Arrow-based vectorized execution and IO performance. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Window Functions & Stateful Bounding](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/06-Window%20Functions%20%26%20Stateful%20Bounding.ipynb) | Windowed analytics and stateful computation patterns. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Data Skew & Cryptographic Salting](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/07-Data%20Skew%20%26%20Cryptographic%20Salting.ipynb) | Skew detection and salting strategies for joins. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Structured Streaming & Watermarks](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/08-Structured%20Streaming%20%26%20Watermarks.ipynb) | Streaming processing, watermarks, and time handling. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Delta Lake Integration (Lakehouse Scaling).](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/09-Delta%20Lake%20Integration%20%28Lakehouse%20Scaling%29.ipynb) | Delta Lake usage patterns and ACID table integration. | | <span style="color:red;">Expert 🔴</span> |
| [10-Cluster Optimization & The Spark UI](/Section%2016-PySpark%20%26%20Big%20Data%20Processing/10-Cluster%20Optimization%20%26%20The%20Spark%20UI.ipynb) | Tuning clusters, executors, and using the Spark UI effectively. | | <span style="color:red;">Expert 🔴</span> |

#### ☁️ Section 17 - Cloud Computing & AI Services

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Infrastructure as Code (IaC) & Python SDKs](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/01-Infrastructure%20as%20Code%20%28IaC%29%20%26%20Python%20SDKs.ipynb) | IaC patterns, SDK usage, and provisioning workflows. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Identity & Access Management (IAM) Cryptography](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/02-Identity%20%26%20Access%20Management%20%28IAM%29%20Cryptography.ipynb) | IAM design, keys, and secure identity patterns. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-The Physics of Cloud Storage (AWS S3 & EventBridge).](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/03-The%20Physics%20of%20Cloud%20Storage%20%28AWS%20S3%20%26%20EventBridge%29.ipynb) | Storage semantics, eventing, and durable object patterns. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Virtual Private Clouds (VPC) & Network Topologies](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/04-Virtual%20Private%20Clouds%20%28VPC%29%20%26%20Network%20Topologies.ipynb) | VPC design, subnets, routing and secure network patterns. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Event-Driven Compute (AWS Lambda & SQS).](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/05-Event-Driven%20Compute%20%28AWS%20Lambda%20%26%20SQS%29.ipynb) | Serverless compute, queues, and event-driven patterns. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Serverless Containers (ECR & AWS Fargate).](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/06-Serverless%20Containers%20%28ECR%20%26%20AWS%20Fargate%29.ipynb) | Container-based serverless patterns and orchestration. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Ephemeral ML Training (Amazon SageMaker).](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/07-Ephemeral%20ML%20Training%20%28Amazon%20SageMaker%29.ipynb) | Short-lived training jobs, managed services, and cost control. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-High-Throughput Inference Endpoints](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/08-High-Throughput%20Inference%20Endpoints.ipynb) | Serving at scale, autoscaling, batching and latency tradeoffs. | | <span style="color:red;">Expert 🔴</span> |
| [09-Enterprise Generative AI (Amazon Bedrock).](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/09-Enterprise%20Generative%20AI%20%28Amazon%20Bedrock%29.ipynb) | Managed generative AI services and enterprise patterns. | | <span style="color:red;">Expert 🔴</span> |
| [10-Cloud FinOps & Spot Instance Physics](/Section%2017-Cloud%20Computing%20%26%20AI%20Services/10-Cloud%20FinOps%20%26%20Spot%20Instance%20Physics.ipynb) | Cost optimization, spot instances and budgeting practices. | | <span style="color:red;">Expert 🔴</span> |

#### 🐧 Section 18 - Linux, Bash Foundations & MLOps

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-POSIX Storage Physics & Directory Topologies](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/01-POSIX%20Storage%20Physics%20%26%20Directory%20Topologies.ipynb) | Filesystem hierarchy, permission bits, and inode-level storage mechanics. | | <span style="color:green;">Beginner 🟢</span> |
| [02-The Linux Stream Matrix (I-O Redirection & Pipes)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/02-The%20Linux%20Stream%20Matrix%20%28I-O%20Redirection%20%26%20Pipes%29.ipynb) | stdin/stdout/stderr redirection, pipes, and composing shell commands. | | <span style="color:green;">Beginner 🟢</span> |
| [03-Hardware Telemetry & Kernel Resource Management](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/03-Hardware%20Telemetry%20%26%20Kernel%20Resource%20Management.ipynb) | CPU, memory, and process introspection via /proc and kernel resource accounting. | | <span style="color:green;">Beginner 🟢</span> |
| [04-Text Processing Mechanics (grep, sed, awk)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/04-Text%20Processing%20Mechanics%20%28grep,%20sed,%20awk%29.ipynb) | Pattern matching, stream editing, and field-based text processing at the command line. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Structured Log Extraction & Telemetry Parsing (jq)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/05-Structured%20Log%20Extraction%20%26%20Telemetry%20Parsing%20%28jq%29.ipynb) | Querying and reshaping JSON log streams directly from the shell. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Automated Batch Scripts & Network Cron Daemon](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/06-Automated%20Batch%20Scripts%20%26%20Network%20Cron%20Daemon.ipynb) | Scheduling recurring jobs and building resilient batch automation scripts. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [07-Network Socket Physics, SSH & Remote Automation](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/07-Network%20Socket%20Physics,%20SSH%20%26%20Remote%20Automation.ipynb) | TCP/socket fundamentals, SSH key-based access, and remote command execution. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [08-Immutable Layer Engineering (Dockerfiles & Layer Caching)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/08-Immutable%20Layer%20Engineering%20%28Dockerfiles%20%26%20Layer%20Caching%29.ipynb) | Writing efficient Dockerfiles and understanding image layer caching. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Multi-Container Grid Topologies (Docker Compose)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/09-Multi-Container%20Grid%20Topologies%20%28Docker%20Compose%29.ipynb) | Orchestrating multi-service local stacks with Docker Compose. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-Experiment Tracking & Artifact Lineage (MLflow Engine)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/10-Experiment%20Tracking%20%26%20Artifact%20Lineage%20%28MLflow%20Engine%29.ipynb) | Logging runs, parameters, and artifacts for reproducible experimentation. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-Local Continuous Integration (GitHub Actions Core Workflows)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/11-Local%20Continuous%20Integration%20%28GitHub%20Actions%20Core%20Workflows%29.ipynb) | Writing CI workflows that lint, test, and validate ML code on every push. | | <span style="color:orange;">Advanced 🟠</span> |
| [12-Production Model Serving Topologies (FastAPI & Docker)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/12-Production%20Model%20Serving%20Topologies%20%28FastAPI%20%26%20Docker%29.ipynb) | Packaging and serving a trained model behind a containerized API. | | <span style="color:orange;">Advanced 🟠</span> |
| [13-High-Throughput Serving & Engine Optimization (vLLM - Triton)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/13-High-Throughput%20Serving%20%26%20Engine%20Optimization%20%28vLLM%20-%20Triton%29.ipynb) | Comparing serving engines for high-throughput inference workloads. | | <span style="color:red;">Expert 🔴</span> |
| [14-Telemetry Scraping & Observability Metrology (Prometheus)](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/14-Telemetry%20Scraping%20%26%20Observability%20Metrology%20%28Prometheus%29.ipynb) | Instrumenting services with Prometheus metrics for production observability. | | <span style="color:red;">Expert 🔴</span> |
| [15-Enterprise Secrets Security & Hardening Boundarie](/Section%2018-Linux,%20Bash%20Foundations%20%26%20MLOps/15-Enterprise%20Secrets%20Security%20%26%20Hardening%20Boundarie.ipynb) | Secrets management, least-privilege boundaries, and system hardening practices. | | <span style="color:red;">Expert 🔴</span> |

#### 📏 Section 19 - Model Evaluation & Monitoring

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Lexical & Statistical NLP Metrics](/Section%2019-Model%20Evaluation%20%26%20Monitoring/01-Lexical%20%26%20Statistical%20NLP%20Metrics.ipynb) | BLEU, ROUGE, and other n-gram-overlap text evaluation metrics. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Semantic Similarity & Cross-Encoders](/Section%2019-Model%20Evaluation%20%26%20Monitoring/02-Semantic%20Similarity%20%26%20Cross-Encoders.ipynb) | Embedding-based similarity and cross-encoder scoring for text evaluation. | | <span style="color:green;">Beginner 🟢</span> |
| [03-The RAG Triad & LLM-as-a-Judge](/Section%2019-Model%20Evaluation%20%26%20Monitoring/03-The%20RAG%20Triad%20%26%20LLM-as-a-Judge.ipynb) | Context relevance, groundedness, and answer relevance scored via an LLM judge. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Hallucination Detection & Factuality](/Section%2019-Model%20Evaluation%20%26%20Monitoring/04-Hallucination%20Detection%20%26%20Factuality.ipynb) | Detecting unsupported claims and factuality gaps in generated text. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Data Drift & Concept Drift (Evidently AI)](/Section%2019-Model%20Evaluation%20%26%20Monitoring/05-Data%20Drift%20%26%20Concept%20Drift%20%28Evidently%20AI%29.ipynb) | Detecting distributional shift in features and model inputs over time. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [06-Unlabeled Performance Estimation (NannyML)](/Section%2019-Model%20Evaluation%20%26%20Monitoring/06-Unlabeled%20Performance%20Estimation%20%28NannyML%29.ipynb) | Estimating model performance in production without ground-truth labels. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [07-Distributed Tracing & Latency (OpenTelemetry + Jaeger)](/Section%2019-Model%20Evaluation%20%26%20Monitoring/07-Distributed%20Tracing%20%26%20Latency%20%28OpenTelemetry%20+%20Jaeger%29.ipynb) | Tracing requests across services to localize latency bottlenecks. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Custom ML Metric Scraping (Prometheus)](/Section%2019-Model%20Evaluation%20%26%20Monitoring/08-Custom%20ML%20Metric%20Scraping%20%28Prometheus%29.ipynb) | Exposing custom model-quality metrics for Prometheus scraping. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-High-Definition Observability (Grafana)](/Section%2019-Model%20Evaluation%20%26%20Monitoring/09-High-Definition%20Observability%20%28Grafana%29.ipynb) | Building dashboards that surface model health at a glance. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-High-Volume Log Aggregation (Grafana Loki)](/Section%2019-Model%20Evaluation%20%26%20Monitoring/10-High-Volume%20Log%20Aggregation%20%28Grafana%20Loki%29.ipynb) | Centralizing and querying logs at scale with Loki. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-SLOs, Error Budgets & Alerting (Alertmanager)](/Section%2019-Model%20Evaluation%20%26%20Monitoring/11-SLOs,%20Error%20Budgets%20%26%20Alerting%20%28Alertmanager%29.ipynb) | Defining service-level objectives and routing alerts on error-budget burn. | | <span style="color:red;">Expert 🔴</span> |
| [12-Shadow Deployments & Traffic Mirroring](/Section%2019-Model%20Evaluation%20%26%20Monitoring/12-Shadow%20Deployments%20%26%20Traffic%20Mirroring.ipynb) | Testing new models against production traffic without serving live responses. | | <span style="color:red;">Expert 🔴</span> |
| [13-Statistical Canary Testing & Rollbacks](/Section%2019-Model%20Evaluation%20%26%20Monitoring/13-Statistical%20Canary%20Testing%20%26%20Rollbacks.ipynb) | Statistically validating canary releases before a full rollout. | | <span style="color:red;">Expert 🔴</span> |

#### ⚙️ Section 20 - AutoML & Model Optimization

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Advanced HPO & Bayesian Search (Optuna)](/Section%2020-AutoML%20%26%20Model%20Optimization/01-Advanced%20HPO%20%26%20Bayesian%20Search%20%28Optuna%29.ipynb) | Bayesian hyperparameter search beyond grid and random search. | | <span style="color:green;">Beginner 🟢</span> |
| [02-High-Speed Tabular AutoML (FLAML)](/Section%2020-AutoML%20%26%20Model%20Optimization/02-High-Speed%20Tabular%20AutoML%20%28FLAML%29.ipynb) | Fast, resource-aware automated model selection for tabular data. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-State-of-the-Art Ensembling (AutoGluon)](/Section%2020-AutoML%20%26%20Model%20Optimization/03-State-of-the-Art%20Ensembling%20%28AutoGluon%29.ipynb) | Automated stacked ensembling for maximal predictive performance. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Neural Architecture Search & Hyperband](/Section%2020-AutoML%20%26%20Model%20Optimization/04-Neural%20Architecture%20Search%20%26%20Hyperband.ipynb) | Automated architecture search with early-stopping-based budget allocation. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Graph Compilation & Execution (ONNX Runtime)](/Section%2020-AutoML%20%26%20Model%20Optimization/05-Graph%20Compilation%20%26%20Execution%20%28ONNX%20Runtime%29.ipynb) | Compiling models to a portable graph format for optimized inference. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Post-Training Quantization (PTQ & INT8)](/Section%2020-AutoML%20%26%20Model%20Optimization/06-Post-Training%20Quantization%20%28PTQ%20%26%20INT8%29.ipynb) | Reducing model precision after training for faster, smaller inference. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Network Pruning & Sparsity Mechanics](/Section%2020-AutoML%20%26%20Model%20Optimization/07-Network%20Pruning%20%26%20Sparsity%20Mechanics.ipynb) | Removing redundant weights and connections to shrink and speed up models. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Knowledge Distillation (Teacher-Student)](/Section%2020-AutoML%20%26%20Model%20Optimization/08-Knowledge%20Distillation%20%28Teacher-Student%29.ipynb) | Training a compact student model to mimic a larger teacher model. | | <span style="color:red;">Expert 🔴</span> |
| [09-Massive Model Compression (bitsandbytes & GGUF)](/Section%2020-AutoML%20%26%20Model%20Optimization/09-Massive%20Model%20Compression%20%28bitsandbytes%20%26%20GGUF%29.ipynb) | Extreme quantization and compact serialization formats for large models. | | <span style="color:red;">Expert 🔴</span> |
| [10-Bare-Metal Hardware Acceleration (OpenVINO)](/Section%2020-AutoML%20%26%20Model%20Optimization/10-Bare-Metal%20Hardware%20Acceleration%20%28OpenVINO%29.ipynb) | Compiling models for optimized inference on specific hardware targets. | | <span style="color:red;">Expert 🔴</span> |

#### 🔦 Section 21 - Explainable AI, Ethics & Responsible AI

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Interpretable Glassbox Models (InterpretML)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/01-Interpretable%20Glassbox%20Models%20%28InterpretML%29.ipynb) | Inherently interpretable model families and their transparency tradeoffs. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Game Theory XAI (SHAP)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/02-Game%20Theory%20XAI%20%28SHAP%29.ipynb) | Shapley-value-based feature attribution grounded in cooperative game theory. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Local Surrogate Perturbation (LIME)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/03-Local%20Surrogate%20Perturbation%20%28LIME%29.ipynb) | Explaining individual predictions via local surrogate models. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Deep Learning Attribution (Captum)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/04-Deep%20Learning%20Attribution%20%28Captum%29.ipynb) | Gradient- and attribution-based explainability for neural networks. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Counterfactual Reasoning (Alibi Explain)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/05-Counterfactual%20Reasoning%20%28Alibi%20Explain%29.ipynb) | Generating counterfactual examples to explain decision boundaries. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Statistical Fairness Auditing (Fairlearn)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/06-Statistical%20Fairness%20Auditing%20%28Fairlearn%29.ipynb) | Measuring and auditing fairness metrics across protected groups. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Algorithmic Bias Mitigation (AIF360)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/07-Algorithmic%20Bias%20Mitigation%20%28AIF360%29.ipynb) | Bias mitigation techniques applied pre-, in-, and post-processing. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Differential Privacy in DL (Opacus)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/08-Differential%20Privacy%20in%20DL%20%28Opacus%29.ipynb) | Training neural networks with differential privacy guarantees. | | <span style="color:red;">Expert 🔴</span> |
| [09-Real-Time PII Sanitization (Presidio)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/09-Real-Time%20PII%20Sanitization%20%28Presidio%29.ipynb) | Detecting and anonymizing personally identifiable information in text. | | <span style="color:red;">Expert 🔴</span> |
| [10-LLM Guardrails & Jailbreak Defense (NeMo)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/10-LLM%20Guardrails%20%26%20Jailbreak%20Defense%20%28NeMo%29.ipynb) | Guardrail policies and jailbreak-resistant LLM application design. | | <span style="color:red;">Expert 🔴</span> |
| [11-RAG Hallucination Detection (TruLens)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/11-RAG%20Hallucination%20Detection%20%28TruLens%29.ipynb) | Detecting and quantifying hallucinations in retrieval-augmented LLM outputs. | | <span style="color:red;">Expert 🔴</span> |
| [12-Automated Model Governance (Model Cards)](/Section%2021-Explainable%20AI,%20Ethics%20%26%20Responsible%20AI/12-Automated%20Model%20Governance%20%28Model%20Cards%29.ipynb) | Automated documentation, compliance tracking, and model card generation for governance. | | <span style="color:red;">Expert 🔴</span> |

#### 🕸️ Section 22 - Graph Data Science & Network Analysis

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Graph Fundamentals & Network Construction (NetworkX)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/01-Graph%20Fundamentals%20%26%20Network%20Construction%20%28NetworkX%29.ipynb) | Nodes, edges, adjacency representations, and graph construction in Python. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [02-Centrality & Network Metrics (NetworkX)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/02-Centrality%20%26%20Network%20Metrics%20%28NetworkX%29.ipynb) | Degree, betweenness, closeness, and eigenvector centrality measures. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Path Finding & Traversal Algorithms (NetworkX / igraph)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/03-Path%20Finding%20%26%20Traversal%20Algorithms%20%28NetworkX%20／%20igraph%29.ipynb) | BFS, DFS, shortest paths, and traversal logic across graph libraries. | | <span style="color:orange;">Advanced 🟠</span> |
| [04-Community Detection (Louvain & Leiden — python-igraph)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/04-Community%20Detection%20%28Louvain%20%26%20Leiden%20—%20python-igraph%29.ipynb) | Modularity optimization, clustering, and network segmentation algorithms. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Graph Databases & Cypher Queries (Neo4j)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/05-Graph%20Databases%20%26%20Cypher%20Queries%20%28Neo4j%29.ipynb) | Native graph storage, Cypher query language, and relationship-first modeling. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Graph Data Modeling at Scale (Neo4j Graph Data Science Library)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/06-Graph%20Data%20Modeling%20at%20Scale%20%28Neo4j%20Graph%20Data%20Science%20Library%29.ipynb) | Schema design, projection, and scalable graph algorithms in production. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Graph Embeddings (Node2Vec)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/07-Graph%20Embeddings%20%28Node2Vec%29.ipynb) | Random-walk-based structural embeddings and similarity learning. | | <span style="color:red;">Expert 🔴</span> |
| [08-Graph Neural Network Foundations (PyTorch Geometric)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/08-Graph%20Neural%20Network%20Foundations%20%28PyTorch%20Geometric%29.ipynb) | Message passing, node classification, and link prediction with GNNs. | | <span style="color:red;">Expert 🔴</span> |
| [09-Graph Machine Learning at Scale (DGL — Deep Graph Library)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/09-Graph%20Machine%20Learning%20at%20Scale%20%28DGL%20—%20Deep%20Graph%20Library%29.ipynb) | Distributed graph learning and large-scale GNN training pipelines. | | <span style="color:red;">Expert 🔴</span> |
| [10-Temporal & Dynamic Graphs (PyTorch Geometric Temporal)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/10-Temporal%20%26%20Dynamic%20Graphs%20%28PyTorch%20Geometric%20Temporal%29.ipynb) | Evolving networks, event streams, and time-aware graph representation learning. | | <span style="color:red;">Expert 🔴</span> |
| [11-Graph Visualization (Gephi / PyVis)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/11-Graph%20Visualization%20%28Gephi%20／%20PyVis%29.ipynb) | Layouts, readability, and interactive storytelling with network graphs. | | <span style="color:red;">Expert 🔴</span> |
| [12-Enterprise Graph Applications & Governance (Neo4j)](/Section%2022-Graph%20Data%20Science%20%26%20Network%20Analysis/12-Enterprise%20Graph%20Applications%20%26%20Governance%20%28Neo4j%29.ipynb) | Knowledge graphs, fraud rings, recommendation systems, and data governance. | | <span style="color:red;">Expert 🔴</span> |

#### ☸️ Section 23 - Kubernetes & Distributed Training

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Container Orchestration Fundamentals (kubectl & Pods)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/01-Container%20Orchestration%20Fundamentals%20%28kubectl%20%26%20Pods%29.ipynb) | Pods, deployments, services, and namespaces via the Kubernetes CLI. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Resource Management & Autoscaling (Kubernetes HPA-VPA)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/02-Resource%20Management%20%26%20Autoscaling%20%28Kubernetes%20HPA-VPA%29.ipynb) | CPU/memory limits, requests, and horizontal/vertical autoscaling behavior. | | <span style="color:green;">Beginner 🟢</span> |
| [03-Rolling Deployments & Scaling Strategies (Kubernetes Deployments)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/03-Rolling%20Deployments%20%26%20Scaling%20Strategies%20%28Kubernetes%20Deployments%29.ipynb) | Rollout strategies, service stability, and zero-downtime scaling. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-Templated Infrastructure (Helm Charts)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/04-Templated%20Infrastructure%20%28Helm%20Charts%29.ipynb) | Packaging, templating, and repeatable deployment definitions. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [05-Data-Parallel Training (PyTorch DDP)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/05-Data-Parallel%20Training%20%28PyTorch%20DDP%29.ipynb) | Synchronous gradient training across multiple devices with DistributedDataParallel. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Model Parallelism & Sharding (DeepSpeed ZeRO)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/06-Model%20Parallelism%20%26%20Sharding%20%28DeepSpeed%20ZeRO%29.ipynb) | Splitting model computation and memory across devices with ZeRO stages. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Distributed Checkpointing & Fault Recovery (Torch Distributed Checkpoint)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/07-Distributed%20Checkpointing%20%26%20Fault%20Recovery%20%28Torch%20Distributed%20Checkpoint%29.ipynb) | Saving, restoring, and syncing distributed training state reliably. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-GPU Scheduling & Allocation (NVIDIA GPU Operator)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/08-GPU%20Scheduling%20%26%20Allocation%20%28NVIDIA%20GPU%20Operator%29.ipynb) | Node selectors, taints, and topology-aware GPU resource planning. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-ML Workflow Orchestration on Kubernetes (Kubeflow)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/09-ML%20Workflow%20Orchestration%20on%20Kubernetes%20%28Kubeflow%29.ipynb) | Pipeline orchestration and experiment tracking for ML on Kubernetes. | | <span style="color:red;">Expert 🔴</span> |
| [10-Distributed Training at Scale (Ray Train)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/10-Distributed%20Training%20at%20Scale%20%28Ray%20Train%29.ipynb) | Cluster-wide distributed training orchestration and scale strategy selection. | | <span style="color:red;">Expert 🔴</span> |
| [11-Cluster Debugging & Observability (Prometheus & Grafana)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/11-Cluster%20Debugging%20%26%20Observability%20%28Prometheus%20%26%20Grafana%29.ipynb) | Scheduling issues, networking, logs, and runtime failure diagnosis. | | <span style="color:red;">Expert 🔴</span> |
| [12-Operational Cost & Efficiency (Spot/Preemptible GPU Nodes)](/Section%2023-Kubernetes%20%26%20Distributed%20Training/12-Operational%20Cost%20%26%20Efficiency%20%28Spot／Preemptible%20GPU%20Nodes%29.ipynb) | Throughput-cost tradeoffs and cluster utilization optimization. | | <span style="color:red;">Expert 🔴</span> |

#### 📐 Section 24 - Statistical Deep Learning

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Bayesian Foundations & Probabilistic Programming (PyMC)](/Section%2024-Statistical%20Deep%20Learning/01-Bayesian%20Foundations%20%26%20Probabilistic%20Programming%20%28PyMC%29.ipynb) | Priors, posteriors, and probabilistic reasoning with a modern PPL. | | <span style="color:green;">Beginner 🟢</span> |
| [02-Uncertainty Estimation (TensorFlow Probability)](/Section%2024-Statistical%20Deep%20Learning/02-Uncertainty%20Estimation%20%28TensorFlow%20Probability%29.ipynb) | Aleatoric vs epistemic uncertainty and practical estimation techniques. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Variational Inference (Pyro)](/Section%2024-Statistical%20Deep%20Learning/03-Variational%20Inference%20%28Pyro%29.ipynb) | Approximate posterior learning and ELBO optimization. | | <span style="color:orange;">Advanced 🟠</span> |
| [04-Variational Autoencoders (PyTorch)](/Section%2024-Statistical%20Deep%20Learning/04-Variational%20Autoencoders%20%28PyTorch%29.ipynb) | Latent variables, reconstruction, and generative representation learning. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Diffusion Model Fundamentals (Hugging Face Diffusers)](/Section%2024-Statistical%20Deep%20Learning/05-Diffusion%20Model%20Fundamentals%20%28Hugging%20Face%20Diffusers%29.ipynb) | Noise schedules, denoising, and generative diffusion steps. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Probabilistic Losses & Calibration (TorchUncertainty)](/Section%2024-Statistical%20Deep%20Learning/06-Probabilistic%20Losses%20%26%20Calibration%20%28TorchUncertainty%29.ipynb) | Gaussian, categorical, and uncertainty-aware objectives with calibration checks. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Bayesian Neural Networks (Pyro - BLiTZ)](/Section%2024-Statistical%20Deep%20Learning/07-Bayesian%20Neural%20Networks%20%28Pyro%20-%20BLiTZ%29.ipynb) | Parameter uncertainty and Monte Carlo approximation in neural nets. | | <span style="color:red;">Expert 🔴</span> |
| [08-Stochastic Training Dynamics (Monte Carlo Dropout — PyTorch)](/Section%2024-Statistical%20Deep%20Learning/08-Stochastic%20Training%20Dynamics%20%28Monte%20Carlo%20Dropout%20—%20PyTorch%29.ipynb) | Noise, regularization, and probabilistic interpretation of gradients. | | <span style="color:red;">Expert 🔴</span> |
| [09-Deep Ensembles for Uncertainty Quantification (PyTorch)](/Section%2024-Statistical%20Deep%20Learning/09-Deep%20Ensembles%20for%20Uncertainty%20Quantification%20%28PyTorch%29.ipynb) | Ensemble-based uncertainty quantification and robustness behavior. | | <span style="color:red;">Expert 🔴</span> |
| [10-Bayesian Optimization for Training (Optuna / BoTorch)](/Section%2024-Statistical%20Deep%20Learning/10-Bayesian%20Optimization%20for%20Training%20%28Optuna%20／%20BoTorch%29.ipynb) | Hyperparameter search guided by probabilistic surrogate models. | | <span style="color:red;">Expert 🔴</span> |
| [11-Posterior Predictive & Risk-Aware Prediction (ArviZ)](/Section%2024-Statistical%20Deep%20Learning/11-Posterior%20Predictive%20%26%20Risk-Aware%20Prediction%20%28ArviZ%29.ipynb) | Estimating uncertainty bands and decision confidence under shift. | | <span style="color:red;">Expert 🔴</span> |
| [12-Decision-Theoretic Inference & Risk Communication](/Section%2024-Statistical%20Deep%20Learning/12-Decision-Theoretic%20Inference%20%26%20Risk%20Communication.ipynb) | Utility-aware prediction and uncertainty-informed action selection. | | <span style="color:red;">Expert 🔴</span> |

#### 📱 Section 25 - Edge AI, TinyML & Reinforcement Learning

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Edge AI Fundamentals & Model Conversion (ONNX)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/01-Edge%20AI%20Fundamentals%20%26%20Model%20Conversion%20%28ONNX%29.ipynb) | Latency constraints, offline inference, and cross-framework model conversion. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [02-Model Compression Pruning & Quantization (TensorFlow Lite)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/02-Model%20Compression%20Pruning%20%26%20Quantization%20%28TensorFlow%20Lite%29.ipynb) | Quantization, pruning, distillation, and sparse deployment. | | <span style="color:orange;">Advanced 🟠</span> |
| [03-TinyML Toolchains for Microcontrollers (Edge Impulse)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/03-TinyML%20Toolchains%20for%20Microcontrollers%20%28Edge%20Impulse%29.ipynb) | Embedded workflows, interpreters, and runtime toolchains for MCUs. | | <span style="color:orange;">Advanced 🟠</span> |
| [04-Sensor Data Processing & Signal Pipelines (TinyML)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/04-Sensor%20Data%20Processing%20%26%20Signal%20Pipelines%20%28TinyML%29.ipynb) | Signal collection, filtering, preprocessing, and feature extraction. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Low-Power Inference Optimization (TensorFlow Lite Micro)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/05-Low-Power%20Inference%20Optimization%20%28TensorFlow%20Lite%20Micro%29.ipynb) | Memory footprint, energy efficiency, and device-level tuning. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Edge Deployment Patterns (NVIDIA Jetson & ONNX Runtime)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/06-Edge%20Deployment%20Patterns%20%28NVIDIA%20Jetson%20%26%20ONNX%20Runtime%29.ipynb) | OTA updates, model versioning, and fleet management for edge devices. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Reinforcement Learning Fundamentals & MDPs (Gymnasium)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/07-Reinforcement%20Learning%20Fundamentals%20%26%20MDPs%20%28Gymnasium%29.ipynb) | Agent, environment, reward, states, actions, and Markov decision processes. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [08-Value-Based Methods (Deep Q-Networks — Stable-Baselines3)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/08-Value-Based%20Methods%20%28Deep%20Q-Networks%20—%20Stable-Baselines3%29.ipynb) | Q-learning, SARSA, and value approximation with deep Q-networks. | | <span style="color:orange;">Advanced 🟠</span> |
| [09-Policy Gradient Methods (PPO — Stable-Baselines3)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/09-Policy%20Gradient%20Methods%20%28PPO%20—%20Stable-Baselines3%29.ipynb) | REINFORCE, actor-critic, and proximal policy optimization. | | <span style="color:orange;">Advanced 🟠</span> |
| [10-Exploration Strategies & Multi-Armed Bandits](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/10-Exploration%20Strategies%20%26%20Multi-Armed%20Bandits.ipynb) | Epsilon-greedy, entropy, and exploration/exploitation balance. | | <span style="color:orange;">Advanced 🟠</span> |
| [11-Deep RL at Scale (Ray RLlib)](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/11-Deep%20RL%20at%20Scale%20%28Ray%20RLlib%29.ipynb) | Distributed deep reinforcement learning training and scaling strategies. | | <span style="color:red;">Expert 🔴</span> |
| [12-Safe & Constrained RL](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/12-Safe%20%26%20Constrained%20RL.ipynb) | Constraints, risk-aware policies, and deployment safeguards. | | <span style="color:red;">Expert 🔴</span> |
| [13-Sim-to-Real & Embedded RL Deployment](/Section%2025-Edge%20AI,%20TinyML%20%26%20Reinforcement%20Learning/13-Sim-to-Real%20%26%20Embedded%20RL%20Deployment.ipynb) | Transferring trained policies from simulation to constrained edge hardware. | | <span style="color:red;">Expert 🔴</span> |

#### 🖥️ Section 26 - System Programming & LLM Serving

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-Modern C++ Foundations for AI Systems](/Section%2026-System%20Programming%20%26%20LLM%20Serving/01-Modern%20C++%20Foundations%20for%20AI%20Systems.ipynb) | Memory management, RAII, templates, and performance-oriented design. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [02-Rust Foundations for Safe Systems](/Section%2026-System%20Programming%20%26%20LLM%20Serving/02-Rust%20Foundations%20for%20Safe%20Systems.ipynb) | Ownership, borrowing, and concurrency-safe service development. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-LLM Serving Fundamentals (Hugging Face Text Generation Inference)](/Section%2026-System%20Programming%20%26%20LLM%20Serving/03-LLM%20Serving%20Fundamentals%20%28Hugging%20Face%20Text%20Generation%20Inference%29.ipynb) | Throughput, latency, batching, and token streaming behavior. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [04-High-Throughput Serving Architecture (vLLM)](/Section%2026-System%20Programming%20%26%20LLM%20Serving/04-High-Throughput%20Serving%20Architecture%20%28vLLM%29.ipynb) | Paged attention, continuous batching, and high-throughput inference internals. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Kernel-Level Inference Optimization (TensorRT-LLM)](/Section%2026-System%20Programming%20%26%20LLM%20Serving/05-Kernel-Level%20Inference%20Optimization%20%28TensorRT-LLM%29.ipynb) | Engine building, kernel fusion, and precision-aware optimization. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Tokenizer & Runtime Integration (Hugging Face Tokenizers & ONNX Runtime)](/Section%2026-System%20Programming%20%26%20LLM%20Serving/06-Tokenizer%20%26%20Runtime%20Integration%20%28Hugging%20Face%20Tokenizers%20%26%20ONNX%20Runtime%29.ipynb) | Efficient tokenization pipelines and cross-runtime interoperability. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Concurrent Inference Scheduling (vLLM PagedAttention & Continuous Batching)](/Section%2026-System%20Programming%20%26%20LLM%20Serving/07-Concurrent%20Inference%20Scheduling%20%28vLLM%20PagedAttention%20%26%20Continuous%20Batching%29.ipynb) | Queueing models, prioritization, and fairness in serving workloads. | | <span style="color:orange;">Advanced 🟠</span> |
| [08-Quantization for Production Serving (GPTQ / AWQ)](/Section%2026-System%20Programming%20%26%20LLM%20Serving/08-Quantization%20for%20Production%20Serving%20%28GPTQ%20／%20AWQ%29.ipynb) | INT8/FP8 tradeoffs and deployment-time calibration strategies. | | <span style="color:red;">Expert 🔴</span> |
| [09-Multi-Model Serving Infrastructure (NVIDIA Triton Inference Server)](/Section%2026-System%20Programming%20%26%20LLM%20Serving/09-Multi-Model%20Serving%20Infrastructure%20%28NVIDIA%20Triton%20Inference%20Server%29.ipynb) | Routing, model isolation, and shared GPU resource management. | | <span style="color:red;">Expert 🔴</span> |
| [10-Observability in LLM Serving (Prometheus & OpenTelemetry)](/Section%2026-System%20Programming%20%26%20LLM%20Serving/10-Observability%20in%20LLM%20Serving%20%28Prometheus%20%26%20OpenTelemetry%29.ipynb) | Metrics, tracing, tail-latency analysis, and SLA tracking. | | <span style="color:red;">Expert 🔴</span> |
| [11-Fault Tolerance & Recovery for Inference Endpoints](/Section%2026-System%20Programming%20%26%20LLM%20Serving/11-Fault%20Tolerance%20%26%20Recovery%20for%20Inference%20Endpoints.ipynb) | Graceful degradation, retries, and resilient inference operations. | | <span style="color:red;">Expert 🔴</span> |
| [12-Production Cost-Performance Engineering](/Section%2026-System%20Programming%20%26%20LLM%20Serving/12-Production%20Cost-Performance%20Engineering.ipynb) | Throughput-per-dollar optimization and capacity planning for scale. | | <span style="color:red;">Expert 🔴</span> |

#### ⚙️ Section 27 - GPU Systems, CUDA & Attention Optimization

| Context | Description | Medium Page | Level |
| :--- | :--- | :--- | :--- |
| [01-CUDA Programming Basics (CUDA C++)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/01-CUDA%20Programming%20Basics%20%28CUDA%20C++%29.ipynb) | Kernels, threads, blocks, and execution model fundamentals. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [02-GPU Memory Hierarchy & Bandwidth Optimization (CUDA)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/02-GPU%20Memory%20Hierarchy%20%26%20Bandwidth%20Optimization%20%28CUDA%29.ipynb) | Global, shared, registers, and bandwidth-aware programming. | | <span style="color:yellow;">Intermediate 🟡</span> |
| [03-Warp Divergence & Occupancy Tuning (Nsight Compute)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/03-Warp%20Divergence%20%26%20Occupancy%20Tuning%20%28Nsight%20Compute%29.ipynb) | SIMT behavior, occupancy tuning, and branch efficiency profiling. | | <span style="color:orange;">Advanced 🟠</span> |
| [04-Writing GPU Kernels in Python (Triton)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/04-Writing%20GPU%20Kernels%20in%20Python%20%28Triton%29.ipynb) | Python-based custom kernels and performance-oriented implementation. | | <span style="color:orange;">Advanced 🟠</span> |
| [05-Custom CUDA Kernel Development (PyTorch C++/CUDA Extensions)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/05-Custom%20CUDA%20Kernel%20Development%20%28PyTorch%20C++／CUDA%20Extensions%29.ipynb) | Fused operations, tiling, and profiling-guided kernel optimization. | | <span style="color:orange;">Advanced 🟠</span> |
| [06-Kernel Fusion Strategies (Triton & torch.compile)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/06-Kernel%20Fusion%20Strategies%20%28Triton%20%26%20torch.compile%29.ipynb) | Combining operators to reduce memory traffic and latency overhead. | | <span style="color:orange;">Advanced 🟠</span> |
| [07-Flash Attention & Attention Optimization (FlashAttention)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/07-Flash%20Attention%20%26%20Attention%20Optimization%20%28FlashAttention%29.ipynb) | IO-aware attention, sparse attention, and sliding-window methods. | | <span style="color:red;">Expert 🔴</span> |
| [08-Memory-Bound vs Compute-Bound Optimization (Nsight ／ CUDA Profiling)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/08-Memory-Bound%20vs%20Compute-Bound%20Optimization%20%28Nsight%20／%20CUDA%20Profiling%29.ipynb) | Roofline analysis, coalesced access, and cache-aware kernel design. | | <span style="color:red;">Expert 🔴</span> |
| [09-Distributed Attention for Long-Context Models (Ring Attention)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/09-Distributed%20Attention%20for%20Long-Context%20Models%20%28Ring%20Attention%29.ipynb) | Multi-GPU attention scaling and communication-efficient kernel pipelines. | | <span style="color:red;">Expert 🔴</span> |
| [10-Pretraining Systems Engineering at Scale (Megatron-LM)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/10-Pretraining%20Systems%20Engineering%20at%20Scale%20%28Megatron-LM%29.ipynb) | Tokenizer design, data pipelines, scaling laws, and MoE basics at scale. | | <span style="color:red;">Expert 🔴</span> |
| [11-Inference Runtime Engineering (CUDA Graphs ／ TensorRT)](/Section%2027-GPU%20Systems,%20CUDA%20%26%20Attention%20Optimization/11-Inference%20Runtime%20Engineering%20%28CUDA%20Graphs%20／%20TensorRT%29.ipynb) | Scheduler-aware serving optimization and runtime graph capture. | | <span style="color:red;">Expert 🔴</span> |

### Notes on Supporting Material

- `medium/` is kept for supplementary content and reference material.
- `files/` contains small sample inputs and outputs used in notebook examples.
- `images/` contains images referenced by the notes.

---

This roadmap will continue to be updated as I explore more topics in Data Science. 🚀

---

## Disclaimer

* The content is created for **educational purposes only** and is not a substitute for official vendor documentation, especially for anything safety- or production-critical.
* All explanations are reviewed and structured based on my own understanding (see the "About This Project" section above for how the AI-assisted authoring process worked).
* Any referenced materials belong to their respective owners and are credited where applicable.
* If any unintentional copyright issue arises, please contact me and it will be promptly resolved.

If any unintentional copyright issue arises, please contact me and it will be promptly resolved.
