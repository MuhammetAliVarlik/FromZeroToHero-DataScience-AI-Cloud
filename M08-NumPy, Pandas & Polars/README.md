# M08 · NumPy, Pandas & Polars

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Data · **Lessons:** 18 existing + 0 planned (18 verified) · **GPU:** —

**Prerequisites:** [M01 Python](../M01-Python/README.md)

**Part of paths:** [Data Analyst & BI](../paths/data-analyst.md), [Data Scientist](../paths/data-scientist.md), [Machine Learning Engineer](../paths/ml-engineer.md), [Deep Learning & Computer Vision](../paths/deep-learning-cv.md), [NLP & LLM Engineer](../paths/nlp-llm.md), [Data Engineer](../paths/data-engineer.md), [MLOps & ML Platform Engineer](../paths/mlops.md), [AI Infrastructure & GPU Systems](../paths/ai-infra-gpu.md), [Responsible AI & AI Security](../paths/responsible-ai.md), [Edge AI & Reinforcement Learning](../paths/edge-ai-rl.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [Introduction to NumPy and Arrays](01-Introduction%20to%20NumPy%20and%20Arrays.ipynb) | 🟢 Beginner | ✅ | Why arrays are fast (measured), creating arrays, shape/dtype/nbytes, dtype limits: overflow and precision. |
| 02 | [NumPy Indexing, Slicing, and Fancy Indexing](02-NumPy%20Indexing,%20Slicing,%20and%20Fancy%20Indexing.ipynb) | 🟢 Beginner | ✅ | Indexing and slicing a years x days weather matrix, views vs copies, boolean masks, fancy indexing, top-k. |
| 03 | [NumPy Data Manipulation](03-NumPy%20Data%20Manipulation.ipynb) | 🟢 Beginner | ✅ | reshape and -1, axes and transpose, stack/concatenate/split, newaxis, sort and unique on weather data. |
| 04 | [NumPy Mathematical and Statistical Functions](04-NumPy%20Mathematical%20and%20Statistical%20Functions.ipynb) | 🟢 Beginner | ✅ | ufuncs, axis aggregations, nan-functions, percentiles, cumsum/diff, correlation, least-squares regression on penguins. |
| 05 | [NumPy Performance Techniques and Broadcasting](05-NumPy%20Performance%20Techniques%20and%20Broadcasting.ipynb) | 🟡 Intermediate | ✅ | Broadcasting rules, standardisation, pairwise distances (loops vs broadcasting vs matmul), memory, strides, einsum. |
| 06 | [Introduction to Pandas Series and DataFrames](06-Introduction%20to%20Pandas%20Series%20and%20DataFrames.ipynb) | 🟢 Beginner | ✅ | Series alignment, DataFrames and the index, reading CSV/JSON/Parquet, inspection, first plots, Copy-on-Write basics. |
| 07 | [Selecting, Filtering, and Indexing Data in Pandas](07-Selecting,%20Filtering,%20and%20Indexing%20Data%20in%20Pandas.ipynb) | 🟢 Beginner | ✅ | Columns, loc/iloc, boolean filters, isin/between/query, sorted datetime index lookups on 3 million taxi trips. |
| 08 | [Data Cleaning and Handling Missing Data with Pandas](08-Data%20Cleaning%20and%20Handling%20Missing%20Data%20with%20Pandas.ipynb) | 🟡 Intermediate | ✅ | Missingness, domain rules, duplicates and fare reversals, IQR outliers, code mapping, a reusable cleaning function with a report. |
| 09 | [Data Transformation and Manipulation in Pandas](09-Data%20Transformation%20and%20Manipulation%20in%20Pandas.ipynb) | 🟡 Intermediate | ✅ | Derived columns, dates and types, np.select, cut/qcut, mapping, .str methods, vectorised vs apply measured, pipe chains. |
| 10 | [Grouping and Aggregation in Pandas (groupby)](10-Grouping%20and%20Aggregation%20in%20Pandas%20(groupby).ipynb) | 🟡 Intermediate | ✅ | Named aggregations, multi-key and time groups, transform, filter, pivot_table and crosstab on NYC taxi trips. |
| 11 | [Merging and Joining DataFrames in Pandas](11-Merging%20and%20Joining%20DataFrames%20in%20Pandas.ipynb) | 🟡 Intermediate | ✅ | Merges with validate and indicator, the many-to-many trap, concat with keys, merge_asof without leakage. |
| 12 | [Time Series and Date Handling in Pandas](12-Time%20Series%20and%20Date%20Handling%20in%20Pandas.ipynb) | 🟡 Intermediate | ✅ | DatetimeIndex, resampling, rolling/expanding windows, seasonal decomposition, time zones and DST, calendar offsets. |
| 13 | [MultiIndex and Advanced Data Structures in Pandas](13-MultiIndex%20and%20Advanced%20Data%20Structures%20in%20Pandas.ipynb) | 🟡 Intermediate | ✅ | MultiIndex selection with xs and IndexSlice, long vs wide with stack/unstack/pivot/melt, weighted group means on Gapminder. |
| 14 | [Performance Optimization with NumPy and Pandas](14-Performance%20Optimization%20with%20NumPy%20and%20Pandas.ipynb) | 🟡 Intermediate | ✅ | Memory profiling, downcasting, category and Arrow strings, Parquet column/row filters, chunked aggregation. |
| 15 | [pandas 2.x & 3.0 (Copy-on-Write, Arrow Types)](15-pandas%202.x%20&%203.0%20(Copy-on-Write,%20Arrow%20Types).ipynb) | 🟡 Intermediate | ✅ | Copy-on-Write and chained assignment, the str dtype, nullable and Arrow dtypes, zero-copy exchange, migration checklist. |
| 16 | [Polars Fundamentals](16-Polars%20Fundamentals.ipynb) | 🟡 Intermediate | ✅ | Expressions and contexts, selectors, group_by/join/over, pandas vs Polars on the same pipeline, translation table. |
| 17 | [Polars Lazy API & Performance](17-Polars%20Lazy%20API%20&%20Performance.ipynb) | 🟡 Intermediate | ✅ | scan_parquet, query plans with projection/predicate pushdown, eager vs lazy vs streaming time and memory, sink_parquet. |
| 18 | [Querying DataFrames with DuckDB](18-Querying%20DataFrames%20with%20DuckDB.ipynb) | 🟡 Intermediate | ✅ | SQL on pandas/Polars frames and Parquet files, QUALIFY, the relational API, pandas vs Polars vs DuckDB benchmark. |

## Assignments

| Assignment | Solution |
| :--- | :--- |
| [Customer Purchase Data Clinic](assignments/01-Customer-Purchase-Data-Clinic.ipynb) | [solution](assignments/01-Customer-Purchase-Data-Clinic-solution.ipynb) |
| [Multi-Source Data Integration Hub](assignments/02-Multi-Source-Data-Integration-Hub.ipynb) | [solution](assignments/02-Multi-Source-Data-Integration-Hub-solution.ipynb) |
| [Fleet Demand Time Series Command](assignments/03-Fleet-Demand-Time-Series-Command.ipynb) | [solution](assignments/03-Fleet-Demand-Time-Series-Command-solution.ipynb) |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
