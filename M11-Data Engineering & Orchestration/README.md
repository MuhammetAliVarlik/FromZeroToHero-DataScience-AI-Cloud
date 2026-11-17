# M11 · Data Engineering & Orchestration

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Data · **Lessons:** 10 existing + 0 planned (10 verified) · **GPU:** —

**Services:** postgres, airflow · start with `docker compose -f docker/compose.yml --profile db --profile orchestration up -d`

**Prerequisites:** [M07 SQL & Databases](../M07-SQL%20%26%20Databases/README.md), [M02 Software Engineering Practices](../M02-Software%20Engineering%20Practices/README.md)

**Part of paths:** [Data Engineer](../paths/data-engineer.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [The Modern Data Stack & ELT Physics](01-The%20Modern%20Data%20Stack%20&%20ELT%20Physics.ipynb) | 🟢 Beginner | ✅ | ETL vs ELT, warehouse layers (raw/staging/marts), a complete measured ELT pipeline into DuckDB, and the cost of moving vs. transforming data. |
| 02 | [Dimensional Data Modeling (Kimball)](02-Dimensional%20Data%20Modeling%20(Kimball).ipynb) | 🟡 Intermediate | ✅ | Bus matrix and conformed dimensions, transaction/snapshot/accumulating facts, SCD types 1-3 in SQL, degenerate and junk dimensions on Chinook. |
| 03 | [Transformations with dbt (Data Build Tool)](03-Transformations%20with%20dbt%20(Data%20Build%20Tool).ipynb) | 🟡 Intermediate | ✅ | A real dbt project on DuckDB: sources, seeds, staging and mart models, ref(), generic and singular tests, incremental models, docs and run results. |
| 04 | [Data Ingestion with dlt](04-Data%20Ingestion%20with%20dlt.ipynb) | 🟡 Intermediate | ✅ | REST API ingestion with dlt resources and pipelines: schema inference, nested-data normalisation, schema evolution, incremental cursors and merge loads. |
| 05 | [Apache Airflow Foundations](05-Apache%20Airflow%20Foundations.ipynb) | 🟡 Intermediate | ✅ | A real Airflow 3 instance in Docker: TaskFlow DAGs, scheduler and executors, XComs, triggering and monitoring runs through the REST API, catchup and retries. |
| 06 | [Advanced Airflow Orchestration](06-Advanced%20Airflow%20Orchestration.ipynb) | 🟠 Advanced | ✅ | Dynamic task mapping, branching and trigger rules, reschedule-mode sensors, retries and scheduler-managed backfills on Airflow 3. |
| 07 | [Airflow 3: What Changed](07-Airflow%203%20-%20What%20Changed.ipynb) | 🟡 Intermediate | ✅ | Task SDK, API-based task execution, asset-triggered DAGs, DAG versioning through REST API v2, and an Airflow 2 to 3 migration checklist. |
| 08 | [Asset-Based Orchestration with Dagster](08-Asset-Based%20Orchestration%20with%20Dagster.ipynb) | 🟠 Advanced | ✅ | Software-defined assets and dependencies, materialisation metadata, asset checks, daily partitions and backfills, asset- vs task-based orchestration. |
| 09 | [Incremental Data Loading Physics](09-Incremental%20Data%20Loading%20Physics.ipynb) | 🟠 Advanced | ✅ | High-water marks vs. full reloads (measured), idempotent MERGE and delete-insert loads, CDC inserts/updates/deletes, and lookback windows for late data. |
| 10 | [Data Quality via Great Expectations](10-Data%20Quality%20via%20Great%20Expectations.ipynb) | 🟠 Advanced | ✅ | GX data context, sources and batches, expectation suites for completeness, validity, uniqueness and distribution, checkpoints and failing a pipeline on bad data. |

## Assignments

| Assignment | Solution |
| :--- | :--- |
| [Taxi Analytics dbt Project](assignments/01-Taxi-Analytics-dbt-Project.ipynb) | [solution](assignments/01-Taxi-Analytics-dbt-Project-solution.ipynb) |
| [Weather-Aware Demand Pipeline](assignments/02-Weather-Aware-Demand-Pipeline.ipynb) | [solution](assignments/02-Weather-Aware-Demand-Pipeline-solution.ipynb) |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
