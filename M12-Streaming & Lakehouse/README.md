# M12 · Streaming & Lakehouse

> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.

**Group:** Data · **Lessons:** 7 existing + 0 planned (7 verified) · **GPU:** —

**Services:** postgres, kafka, connect, flink, schema-registry, rustfs, iceberg-rest, marquez · start with `docker compose -f docker/compose.yml --profile cdc --profile db --profile flink --profile lakehouse --profile lineage --profile streaming up -d`

**Prerequisites:** [M11 Data Engineering & Orchestration](../M11-Data%20Engineering%20%26%20Orchestration/README.md)

**Part of paths:** [Data Engineer](../paths/data-engineer.md)

| # | Lesson | Level | Status | Description |
| :-: | :--- | :--- | :-: | :--- |
| 01 | [Change Data Capture (CDC) with Debezium](01-Change%20Data%20Capture%20(CDC)%20with%20Debezium.ipynb) | 🟠 Advanced | ✅ | Log-based CDC from PostgreSQL through Debezium and Kafka Connect, an idempotent replica, capture latency, why polling misses deletes, and replication slot (WAL) monitoring. |
| 02 | [Event Streaming with Apache Kafka](02-Event%20Streaming%20with%20Apache%20Kafka.ipynb) | 🟠 Advanced | ✅ | Topics, partitions and keys, consumer groups and rebalancing, delivery guarantees, idempotent and transactional producers, retention and log compaction, measured throughput and lag. |
| 03 | [Stream Processing with Apache Flink](03-Stream%20Processing%20with%20Apache%20Flink.ipynb) | 🟠 Advanced | ✅ | Flink SQL through the SQL Gateway, event time and watermarks, late events and the latency/completeness trade-off, window Top-N, state and checkpoints. |
| 04 | [The Lakehouse Architecture (Iceberg - Delta)](04-The%20Lakehouse%20Architecture%20(Iceberg%20-%20Delta).ipynb) | 🔴 Expert | ✅ | Delta Lake on S3 (transaction log, merge, time travel, schema enforcement, compaction, vacuum) and Apache Iceberg (hidden partitioning, snapshots, schema evolution). |
| 05 | [Open Table Catalogs (Iceberg REST)](05-Open%20Table%20Catalogs%20(Iceberg%20REST).ipynb) | 🔴 Expert | ✅ | The Iceberg REST catalog protocol, PyIceberg and DuckDB on one table, optimistic concurrency, branches and tags for write-audit-publish, partition evolution. |
| 06 | [Data Contracts & Schema Registries](06-Data%20Contracts%20&%20Schema%20Registries.ipynb) | 🔴 Expert | ✅ | Avro with the Schema Registry wire format, compatibility modes measured on six schema changes, blocked producers, and a data contract checked as code. |
| 07 | [Data Observability & Lineage](07-Data%20Observability%20&%20Lineage.ipynb) | 🔴 Expert | ✅ | OpenLineage events into Marquez, upstream/downstream impact from the lineage graph, and freshness, volume and schema monitors that find three built-in incidents. |

## Assignments

| Assignment | Solution |
| :--- | :--- |
| [CDC into the Lakehouse](assignments/01-CDC-into-the-Lakehouse.ipynb) | [solution](assignments/01-CDC-into-the-Lakehouse-solution.ipynb) |
| [A Governed Taxi Feed](assignments/02-Governed-Taxi-Feed.ipynb) | [solution](assignments/02-Governed-Taxi-Feed-solution.ipynb) |

Status legend: ✅ done · 🔍 review · 📈 deepen · ⚙️ realise · 🔀 merge · ✏️ rewrite · 🆕 planned
