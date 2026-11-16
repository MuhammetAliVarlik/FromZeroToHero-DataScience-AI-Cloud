# M31 · Evaluation & Observability for ML and LLMs

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** LLM & AI Applications · **Lessons:** 9 existing + 3 planned (0 verified) · **GPU:** optional

**Services:** ollama · start with `docker compose -f docker/compose.yml --profile ollama up -d` (ollama: or native Ollama on http://localhost:11434)

**Prerequisites:** [M28 RAG & Retrieval Systems](../M28-RAG%20%26%20Retrieval%20Systems/README.md)

**Part of paths:** [NLP & LLM Engineer](../paths/nlp-llm.md), [AI Application Engineer](../paths/ai-app-engineer.md), [Responsible AI & AI Security](../paths/responsible-ai.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [NLP Evaluation Metrics](01-NLP%20Evaluation%20Metrics.ipynb) | 🟠 Advanced | 🔍 | BLEU, ROUGE, BERTScore and human-eval practices. |
| 02 | [Lexical & Statistical NLP Metrics](02-Lexical%20&%20Statistical%20NLP%20Metrics.ipynb) | 🟢 Beginner | ⚙️ | BLEU, ROUGE, and other n-gram-overlap text evaluation metrics. |
| 03 | [Semantic Similarity & Cross-Encoders](03-Semantic%20Similarity%20&%20Cross-Encoders.ipynb) | 🟢 Beginner | 🔍 | Embedding-based similarity and cross-encoder scoring for text evaluation. |
| 04 | [Evaluating RAG (RAGAS-TruLens)](04-Evaluating%20RAG%20(RAGAS-TruLens).ipynb) | 🟠 Advanced | ⚙️ | Evaluation frameworks and reliability assessments for RAG. |
| 05 | [The RAG Triad & LLM-as-a-Judge](05-The%20RAG%20Triad%20&%20LLM-as-a-Judge.ipynb) | 🟡 Intermediate | 🔀 | Context relevance, groundedness, and answer relevance scored via an LLM judge. *(merge into S13-12: one RAG-triad / LLM-judge lesson)* |
| 06 | [Hallucination Detection & Factuality](06-Hallucination%20Detection%20&%20Factuality.ipynb) | 🟡 Intermediate | 🔍 | Detecting unsupported claims and factuality gaps in generated text. |
| 07 | [RAG Hallucination Detection (TruLens)](07-RAG%20Hallucination%20Detection%20(TruLens).ipynb) | 🔴 Expert | 🔀 | Detecting and quantifying hallucinations in retrieval-augmented LLM outputs. *(merge into S19-04: one hallucination-detection lesson)* |
| 08 | LLM Evaluation Frameworks (DeepEval, promptfoo, Inspect) |  | 🆕 |  |
| 09 | Benchmarks & Data Contamination |  | 🆕 |  |
| 10 | [Data Drift & Concept Drift (Evidently AI)](10-Data%20Drift%20&%20Concept%20Drift%20(Evidently%20AI).ipynb) | 🟡 Intermediate | 🔍 | Detecting distributional shift in features and model inputs over time. |
| 11 | [Unlabeled Performance Estimation (NannyML)](11-Unlabeled%20Performance%20Estimation%20(NannyML).ipynb) | 🟡 Intermediate | 🔍 | Estimating model performance in production without ground-truth labels. |
| 12 | LLM Observability (Langfuse, Phoenix, OpenTelemetry GenAI) |  | 🆕 |  |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
