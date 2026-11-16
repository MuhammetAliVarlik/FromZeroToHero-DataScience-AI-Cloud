# M07 · SQL & Databases

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Data · **Lessons:** 20 existing + 0 planned (20 verified) · **GPU:** —

**Services:** postgres, mongodb, redis · start with `docker compose -f docker/compose.yml --profile db up -d`

**Prerequisites:** [M01 Python](../M01-Python/README.md)

**Part of paths:** [Software Engineer (Python Backend)](../paths/software-engineer.md), [Data Analyst & BI](../paths/data-analyst.md), [Data Scientist](../paths/data-scientist.md), [AI Application Engineer](../paths/ai-app-engineer.md), [Data Engineer](../paths/data-engineer.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [Database Setup with Docker (PostgreSQL)](01-Database%20Setup%20with%20Docker%20(PostgreSQL).ipynb) | 🟢 Beginner | ✅ | Start PostgreSQL with Docker Compose, load the Chinook sample database, connect with psql and SQLAlchemy, explore the catalog. |
| 02 | [Relational Database Foundations](02-Relational%20Database%20Foundations.ipynb) | 🟢 Beginner | ✅ | Tables, keys and relationships in Chinook, constraints rejecting bad data, normalisation measured on a denormalised copy. |
| 03 | [Data Definition and Schema Design (CREATE-ALTER)](03-Data%20Definition%20and%20Schema%20Design%20(CREATE-ALTER).ipynb) | 🟢 Beginner | ✅ | PostgreSQL data types, CREATE TABLE with constraints, ALTER TABLE and migrations, DELETE vs TRUNCATE timed. |
| 04 | [SQL Query Fundamentals (SELECT, WHERE, GROUP BY)](04-SQL%20Query%20Fundamentals%20(SELECT,%20WHERE,%20GROUP%20BY).ipynb) | 🟢 Beginner | ✅ | SELECT, WHERE, NULL handling, ORDER BY, GROUP BY/HAVING and the logical query order on Chinook. |
| 05 | [Joins and Set Operations](05-Joins%20and%20Set%20Operations.ipynb) | 🟢 Beginner | ✅ | Inner/outer/cross/self joins, anti-joins, the fan-out trap, UNION/INTERSECT/EXCEPT on Chinook. |
| 06 | [Subqueries and Common Table Expressions (CTEs)](06-Subqueries%20and%20Common%20Table%20Expressions%20(CTEs).ipynb) | 🟡 Intermediate | ✅ | Scalar, IN, EXISTS and correlated subqueries, multi-step CTEs, RFM segmentation, recursive org chart. |
| 07 | [Window Functions for Analytics](07-Window%20Functions%20for%20Analytics.ipynb) | 🟡 Intermediate | ✅ | OVER/PARTITION BY, running totals, moving averages, RANK/ROW_NUMBER/NTILE, LAG/LEAD growth rates. |
| 08 | [Analytical SQL with DuckDB](08-Analytical%20SQL%20with%20DuckDB.ipynb) | 🟡 Intermediate | ✅ | Row vs column stores, DuckDB on SQLite/CSV/Parquet/DataFrames, benchmark vs pandas and SQLite, partitioned exports. |
| 09 | [Connecting Python to SQL (SQLAlchemy & Pandas)](09-Connecting%20Python%20to%20SQL%20(SQLAlchemy%20&%20Pandas).ipynb) | 🟡 Intermediate | ✅ | Engines and transactions, SQL injection vs parameters, read_sql chunks, the ORM, bulk loading with COPY measured. |
| 10 | [Indexes and Query Performance](10-Indexes%20and%20Query%20Performance.ipynb) | 🟡 Intermediate | ✅ | EXPLAIN ANALYZE, B-tree indexes, selectivity and plan choice, composite/covering indexes, write cost of indexes. |
| 11 | [Transactions and ACID Principles](11-Transactions%20and%20ACID%20Principles.ipynb) | 🟡 Intermediate | ✅ | ACID, savepoints, lost updates with 8 threads, FOR UPDATE vs atomic updates, isolation levels, deadlocks. |
| 12 | [NoSQL Databases & MongoDB Fundamentals](12-NoSQL%20Databases%20&%20MongoDB%20Fundamentals.ipynb) | 🟡 Intermediate | ✅ | NoSQL models, real MongoDB with Chinook invoices as documents, CRUD, aggregation pipelines, embedding vs referencing, indexes. |
| 13 | [Redis & Key-Value Stores](13-Redis%20&%20Key-Value%20Stores.ipynb) | 🟡 Intermediate | ✅ | Redis data structures, TTL, cache-aside in front of PostgreSQL measured, rate limiting, sorted-set leaderboards. |
| 14 | [PostgreSQL JSONB & pgvector](14-PostgreSQL%20JSONB%20&%20pgvector.ipynb) | 🟡 Intermediate | ✅ | JSONB queries and GIN indexes, embeddings with Ollama nomic-embed-text, semantic album search, HNSW speed and recall. |
| 15 | [Data Modeling for Analytics (Star schemas)](15-Data%20Modeling%20for%20Analytics%20(Star%20schemas).ipynb) | 🟡 Intermediate | ✅ | Facts, dimensions and grain, a Chinook star schema with a date dimension, star vs normalised queries, SCD type 2. |
| 16 | [Security, Roles, and Access Control](16-Security,%20Roles,%20and%20Access%20Control.ipynb) | 🟡 Intermediate | ✅ | Roles and grants, column privileges, masking views, row-level security for tenants, privilege audits. |
| 17 | [Stored Procedures, Functions, and Triggers](17-Stored%20Procedures,%20Functions,%20and%20Triggers.ipynb) | 🟡 Intermediate | ✅ | SQL and PL/pgSQL functions, batch procedures with COMMIT, audit/validation triggers, trigger overhead measured. |
| 18 | [Backup, Recovery, and Replication](18-Backup,%20Recovery,%20and%20Replication.ipynb) | 🟡 Intermediate | ✅ | RPO/RTO, pg_dump formats, tested restores, recovering deleted rows from a dump, WAL, PITR and replication. |
| 19 | [Cloud Data Warehouses (BigQuery Sandbox)](19-Cloud%20Data%20Warehouses%20(BigQuery%20Sandbox).ipynb) | 🟡 Intermediate | ✅ | Warehouse architecture and pricing, bytes-scanned cost estimation, partitioning and clustering measured with Parquet, BigQuery SQL. |
| 20 | [Text-to-SQL with Open LLMs](20-Text-to-SQL%20with%20Open%20LLMs.ipynb) | 🟠 Advanced | ✅ | Schema prompts, safe execution (read-only, timeout), execution accuracy on 16 labelled Chinook questions with Llama 3.2 3B. |

## Assignments

| Assignment | Solution |
| :--- | :--- |
| [E-Commerce Analytics Warehouse](assignments/01-E-Commerce-Analytics-Warehouse.ipynb) | [solution](assignments/01-E-Commerce-Analytics-Warehouse-solution.ipynb) |
| [MongoDB Operations Desk](assignments/02-MongoDB-Operations-Desk.ipynb) | [solution](assignments/02-MongoDB-Operations-Desk-solution.ipynb) |
| [ACID and ETL Control Room](assignments/03-ACID-and-ETL-Control-Room.ipynb) | [solution](assignments/03-ACID-and-ETL-Control-Room-solution.ipynb) |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
