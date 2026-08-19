---
name: database
description: 'Use when designing or changing persistent data models, schemas, queries, indexes, transactions, data lifecycle, datastore choice, or migration shape. Activate for “schema”, “database”, “table”, “SQL”, “migration”, “backfill”, “index”, “query”, “normalize”, “denormalize”, “foreign key”, “data integrity”, “transaction”, “concurrency”, “retention”, or “soft delete”. Do not use for an API contract without a persistence decision (use api-design), a live migration execution (use database-migration), or a full security threat model (use security).'
---

# Data Modelling and Evolution

## WHEN TO USE THIS

- Design or change persistent data, relationships, constraints, query paths, or ownership.
- Choose a persistence model or analyze a concurrency, lifecycle, integrity, or access-pattern decision.
- Prepare a migration approach before an approval-gated live transition.

## NEVER DO

- Apply third normal form, a relational datastore, billion-row architecture, soft deletion, or separate schema deployment as a universal default.
- Treat code rollback as proof that transformed, deleted, emitted, or externally observed data can be recovered.
- Let multiple writers mutate shared truth without explicit ownership, invariant enforcement, and reconciliation rules.
- Run a live migration, backfill, deletion, or retention change merely because a plan or migration file exists.
- Present an application-only check as protection for a cross-writer invariant when the datastore can enforce that invariant.

## CLASSIFY DATA, OWNERSHIP, AND CONSEQUENCE

Before modelling, record the data owner, writers, readers, lifecycle, trust/tenant boundaries, required invariants, dominant operations, expected growth, and recovery consequence. Start from actual requirements, not from entity nouns or a preferred technology.

| Condition | Minimum decision record |
| --- | --- |
| Local, disposable, bounded data | State the local owner, shape, and why simple storage is sufficient. |
| Shared product data | State writers/readers, lifecycle, invariants, access patterns, and failure/recovery consequence. |
| Independently consumed or migrated data | Add compatibility window, consumer matrix, data-movement/resume path, and retirement condition. |
| Personal, regulated, financial, security-sensitive, or destructive data | Add classification, authority, retention/deletion meaning, backup/copy impact, recovery limit, and required specialist/approval route. |

When the current datastore satisfies the real invariants and access patterns, prefer keeping it. Evaluate another model only when it materially improves integrity, access, lifecycle, or recovery with acceptable operational cost.

## MODEL INVARIANTS, ACCESS, AND LIFECYCLE

List each invariant in plain language and place enforcement at the strongest practical boundary:

| Invariant type | Typical enforcement |
| --- | --- |
| Row-local validity or required value | Schema type, check, not-null, or equivalent datastore constraint. |
| Cross-writer uniqueness or relationship | Unique, foreign-key, exclusion, transaction, or equivalent authoritative constraint. |
| Multi-step state transition | Transaction, conditional update/version, or a deliberately handled conflict. |
| User-facing shape or external policy | Application validation plus an authoritative data/authorization check where needed. |
| Cross-system copy | Named owner, event/reconciliation rule, and a way to detect divergence. |

Choose normalization, denormalization, document shape, relationship model, and indexes from ownership, update anomalies, aggregate locality, dominant reads/writes, and operational cost. Record duplication and reconciliation when data is intentionally copied. Use specific data types, constraints, and query plans where the selected datastore supports them; do not invent datastore-specific rules for a project that does not use that engine.

Treat identity separately from lifecycle. `active`, `inactive`, `archived`, `tombstoned`, `audited`, `anonymized`, and `erased` have different legal, recovery, and access meanings. Choose the state by data class and requirement; do not call soft deletion a complete privacy, audit, or recovery solution.

## HANDLE CONCURRENCY AND EVOLUTION PROPORTIONALLY

Choose concurrency control from the invariant and expected contention. Use a conditional update/version/ETag, transaction isolation, serialization, lock, or explicit conflict response only when it protects a real shared-state risk. State accepted anomalies or conflict behaviour; do not silently accept lost updates.

For a schema or data change, distinguish these cases:

- A small local, coordinated, reversible change may use an atomic transition if the actual platform guarantees the required ordering and recovery.
- A change with rolling deployment, independent readers/writers, high volume, long-running backfill, or coexistence requirements may need additive compatibility, staged data movement, reconciliation, and later contraction.
- A destructive or lossy change needs an explicit restore point or forward-recovery path; a down migration alone is not enough.

Use `database-migration` for a live or consequential execution path. This skill may design and assess; it does not grant approval to mutate data or a production target.

## SELECT EVIDENCE FROM THE REAL FAILURE SURFACE

- Model/invariant change: inspect schema and attempt violating writes through the authoritative boundary.
- Query/index change: inspect actual query shape/plan where available and compare the relevant workload, not an invented scale target.
- Concurrent write: exercise an interleaving or conflict case that could violate the invariant.
- Compatibility/backfill change: verify old/new reader-writer combinations, batch/resume/retry behaviour, reconciliation, and stopping thresholds where applicable.
- Data lifecycle/deletion change: trace affected copies/backups, retention/erasure meaning, and recovery/audit consequence. Escalate legal ambiguity.

Record what was not tested: representative data, production locking, restore, external reader, or a possible data anomaly. Never turn a green migration command into a claim of safety.

## REFERENCE LOADING RULES

- Load [extended-guidance.md](references/extended-guidance.md) for datastore selection, schema modelling, transactions, query/index analysis, staged migration/backfill, lifecycle/deletion, or recovery decisions.
- Load [resource-index.md](references/resource-index.md) when a current datastore or migration-platform fact affects the decision.
- Use `api-design` for a changed external contract, `security` for tenant/access/sensitive-data ambiguity, and `testing` for evidence design.

## OUTPUT SHAPE

```text
Data owner, writers/readers, lifecycle, and invariant map:
Chosen model and access-pattern rationale:
Compatibility/migration or recovery decision:
Evidence actually available and known limits:
Required approval or next handoff:
```

## NON-NEGOTIABLE CHECKLIST

1. Name the data owner, writers, consumers, and invariants.
2. Enforce cross-writer invariants at an authoritative boundary where practical.
3. Choose model shape and scale work from evidence, not doctrine.
4. Separate code rollback from data recovery.
5. Route live, destructive, privacy-sensitive, or consequential changes through the required approval path.
