# M28 · RAG & Retrieval Systems

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** LLM & AI Applications · **Lessons:** 11 existing + 5 planned (0 verified) · **GPU:** optional

**Services:** ollama, postgres · start with `docker compose -f docker/compose.yml --profile db --profile ollama up -d` (ollama: or native Ollama on http://localhost:11434)

**Prerequisites:** [M26 LLM Foundations](../M26-LLM%20Foundations/README.md) · **Recommended:** [M07 SQL & Databases](../M07-SQL%20%26%20Databases/README.md)

**Part of paths:** [NLP & LLM Engineer](../paths/nlp-llm.md), [AI Application Engineer](../paths/ai-app-engineer.md), [Responsible AI & AI Security](../paths/responsible-ai.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [The Physics of RAG](01-The%20Physics%20of%20RAG.ipynb) | 🟢 Beginner | ⚙️ | RAG conceptual workflow and system building blocks. |
| 02 | [Document Parsing & Chunking Math](02-Document%20Parsing%20&%20Chunking%20Math.ipynb) | 🟢 Beginner | 🔍 | Chunking strategies, overlap, and semantic segmentation. |
| 03 | Document Parsing with Docling |  | 🆕 |  |
| 04 | [Bi-Encoders & Dense Retrieval](04-Bi-Encoders%20&%20Dense%20Retrieval.ipynb) | 🟡 Intermediate | 🔍 | Bi-encoder training and dense retrieval pipelines. |
| 05 | Choosing Embedding Models (MTEB & Matryoshka) |  | 🆕 |  |
| 06 | [Vector Databases & Metadata](06-Vector%20Databases%20&%20Metadata.ipynb) | 🟡 Intermediate | 🔍 | DB choices, schema, and metadata-driven filtering. |
| 07 | pgvector in Production |  | 🆕 |  |
| 08 | [The Mathematics of ANN (HNSW & IVF)](08-The%20Mathematics%20of%20ANN%20(HNSW%20&%20IVF).ipynb) | 🟡 Intermediate | 🔍 | ANN algorithms and tradeoffs for recall/latency. |
| 09 | [Sparse Search & BM25](09-Sparse%20Search%20&%20BM25.ipynb) | 🟡 Intermediate | 🔍 | BM25 and sparse retrieval techniques. |
| 10 | [Hybrid Search & RRF](10-Hybrid%20Search%20&%20RRF.ipynb) | 🟠 Advanced | 🔍 | Combining dense and sparse signals for robust retrieval. |
| 11 | [Reranking (Cross-Encoders)](11-Reranking%20(Cross-Encoders).ipynb) | 🟠 Advanced | ⚙️ | Cross-encoder reranking and relevance calibration. |
| 12 | [Query Transformation (HyDE)](12-Query%20Transformation%20(HyDE).ipynb) | 🟠 Advanced | ⚙️ | Query augmentation and hallucinated document expansion. |
| 13 | Contextual Retrieval & Late Chunking |  | 🆕 |  |
| 14 | Multi-Vector Retrieval (ColBERT & ColPali) |  | 🆕 |  |
| 15 | [Advanced Context Topologies](15-Advanced%20Context%20Topologies.ipynb) | 🟠 Advanced | 🔍 | Context assembly strategies and slot-filling topologies. |
| 16 | [GraphRAG Foundations](16-GraphRAG%20Foundations.ipynb) | 🟠 Advanced | 🔍 | Graph-based retrieval and knowledge augmentation. |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
