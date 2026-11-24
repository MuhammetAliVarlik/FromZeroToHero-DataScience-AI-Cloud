# M13 · Spark & Distributed Data Processing

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Data · **Lessons:** 12 existing + 0 planned (12 verified) · **GPU:** —

**Prerequisites:** [M08 NumPy, Pandas & Polars](../M08-NumPy%2C%20Pandas%20%26%20Polars/README.md), [M11 Data Engineering & Orchestration](../M11-Data%20Engineering%20%26%20Orchestration/README.md)

**Part of paths:** [Data Engineer](../paths/data-engineer.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [Spark Architecture & Lazy Evaluation (PySpark)](01-Spark%20Architecture%20&%20Lazy%20Evaluation%20(PySpark).ipynb) | 🟢 Beginner | ✅ | Driver, executors, partitions and tasks; transformations vs. actions, lazy DAGs, jobs and stages, measured on taxi data. |
| 02 | [The Catalyst Optimizer & Execution Plans](02-The%20Catalyst%20Optimizer%20&%20Execution%20Plans.ipynb) | 🟡 Intermediate | ✅ | Reading logical and physical plans with explain(), predicate and projection pushdown, constant folding, and AQE plan changes at run time. |
| 03 | [Partitioning & the Shuffle](03-Partitioning%20&%20the%20Shuffle.ipynb) | 🟡 Intermediate | ✅ | Narrow vs. wide transformations, shuffle bytes measured per stage, repartition vs. coalesce, spark.sql.shuffle.partitions and partitioned Parquet layouts. |
| 04 | [Distributed Joins (Broadcast vs. Sort-Merge)](04-Distributed%20Joins%20(Broadcast%20vs.%20Sort-Merge).ipynb) | 🟠 Advanced | ✅ | Broadcast hash, sort-merge and shuffle hash joins, join hints and the broadcast threshold, with network bytes and run time compared. |
| 05 | [Vectorized UDFs (Apache Arrow & Pandas UDFs)](05-Vectorized%20UDFs%20(Apache%20Arrow%20&%20Pandas%20UDFs).ipynb) | 🟠 Advanced | ✅ | Row-at-a-time Python UDFs vs. Arrow-backed pandas UDFs and built-in functions, mapInPandas and applyInPandas, and the cost of crossing the JVM boundary. |
| 06 | [Window Functions (Spark SQL)](06-Window%20Functions%20(Spark%20SQL).ipynb) | 🟠 Advanced | ✅ | Ranking, lag/lead, running totals and moving averages over partitions and frames in Spark SQL, and the shuffle and sort each window needs. |
| 07 | [Data Skew, Salting & Adaptive Query Execution](07-Data%20Skew,%20Salting%20&%20Adaptive%20Query%20Execution.ipynb) | 🟠 Advanced | ✅ | Measuring key skew in taxi data, its effect on task times through the Spark REST API, and fixing it with salting and AQE skew-join handling. |
| 08 | [Structured Streaming & Watermarks (Spark)](08-Structured%20Streaming%20&%20Watermarks%20(Spark).ipynb) | 🟠 Advanced | ✅ | Micro-batches, event-time windows, watermarks for late data, output modes, and checkpoints that make a restart exactly-once. |
| 09 | [Delta Lake with Spark (delta-spark)](09-Delta%20Lake%20with%20Spark%20(delta-spark).ipynb) | 🔴 Expert | ✅ | MERGE INTO, time travel and RESTORE, OPTIMIZE with ZORDER, constraints and the Change Data Feed, then the same table read by other engines. |
| 10 | [Tuning & the Spark UI](10-Tuning%20&%20the%20Spark%20UI.ipynb) | 🔴 Expert | ✅ | Jobs, stages, executors and SQL tabs of the Spark UI; spill, caching, file formats and partition counts tuned one setting at a time with measurements. |
| 11 | [Spark 4 (Spark Connect, ANSI Mode, VARIANT)](11-Spark%204%20(Spark%20Connect,%20ANSI%20Mode,%20VARIANT).ipynb) | 🔴 Expert | ✅ | Spark Connect client/server, ANSI mode on by default, the VARIANT type for semi-structured data, and Python data sources, checked in pyspark 4.2. |
| 12 | [Beyond Spark (Polars, DuckDB, Ray Data & Daft)](12-Beyond%20Spark%20(Polars,%20DuckDB,%20Ray%20Data%20&%20Daft).ipynb) | 🟠 Advanced | ✅ | The same taxi queries in Spark, Polars, DuckDB, Daft and Ray Data, with time and memory measured, and when a single machine is enough. |

## Assignments

| Assignment | Solution |
| :--- | :--- |
| [A Taxi Batch Pipeline at Scale](assignments/01-Taxi-Batch-Pipeline-at-Scale.ipynb) | [solution](assignments/01-Taxi-Batch-Pipeline-at-Scale-solution.ipynb) |
| [Streaming Revenue into Delta Lake](assignments/02-Streaming-Revenue-into-Delta.ipynb) | [solution](assignments/02-Streaming-Revenue-into-Delta-solution.ipynb) |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
