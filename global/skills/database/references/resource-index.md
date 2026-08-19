# Data Modelling Source Index

Use these sources only when their current datastore or migration behaviour
changes the decision. This index was checked on 2026-08-19; it does not make a
PostgreSQL or GitLab practice universal.

| Source | Use when | Verification note |
| --- | --- | --- |
| [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) | Choosing constraints, keys, relationships, and deletion actions in PostgreSQL. | Engine-specific capabilities and limits. |
| [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | Evaluating isolation anomalies and concurrency choices in PostgreSQL. | Engine-specific behaviour; verify the deployed version. |
| [GitLab batched background migrations](https://docs.gitlab.com/development/database/batched_background_migrations/) | Studying operational patterns for long-running data movement. | Maintainer example, not a migration framework mandate. |
| [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | Checking tenant/object authorization or resource-consumption risk at a data boundary. | Route broader threat modelling to `security`. |

Load [extended-guidance.md](extended-guidance.md) for operational decision rules;
load an external source only when its current behavior changes the decision.
