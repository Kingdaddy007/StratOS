# Data Modelling, Migration, and Recovery Guidance

## Contents

- [Choose a datastore and model shape](#choose-a-datastore-and-model-shape)
- [Map invariants and ownership](#map-invariants-and-ownership)
- [Design query and index evidence](#design-query-and-index-evidence)
- [Control concurrent updates](#control-concurrent-updates)
- [Evolve schema and data safely](#evolve-schema-and-data-safely)
- [Handle lifecycle, retention, and deletion](#handle-lifecycle-retention-and-deletion)
- [Select evidence and stopping conditions](#select-evidence-and-stopping-conditions)

## Choose a datastore and model shape

Start with the existing datastore when it meets the required integrity, query, lifecycle, recovery, operational, and team constraints. Change technology only for a concrete benefit that outweighs migration and operational risk.

Compare candidate shapes using the decisions that matter:

| Question | Evidence to inspect |
| --- | --- |
| What is authoritative truth? | Owner, writer set, external source, replication and reconciliation needs. |
| Which invariants must never break? | Uniqueness, relationship, state, balance, ordering, tenant, or retention rules. |
| How is data read and written? | Representative queries, aggregates, traversal, write frequency, payload size, and access locality. |
| What must be atomic? | Multi-record transition, external effect, partial failure, retry, and concurrency consequence. |
| What will evolve? | Independent consumers, schema changes, migration volume, copy/backfill, and recovery needs. |

Normalize where it protects a real update invariant or ownership boundary. Denormalize or use document-shaped aggregates where locality and lifecycle make it safer, but name the duplicated facts, their owner, and reconciliation rule. Do not require a fixed normal form, join count, row count, or storage technology.

## Map invariants and ownership

Write each material invariant as a falsifiable statement, then map it to enforcement and evidence.

| Invariant | Strong candidate enforcement | Evidence |
| --- | --- | --- |
| A value is present or within a local range | Type, not-null, check, or datastore validation. | Attempt an invalid write. |
| A value or tuple is unique | Unique/exclusion constraint or authoritative conditional write. | Concurrent/duplicate write attempt. |
| A relationship must exist | Foreign key, document ownership check, or authoritative relation validation. | Invalid reference attempt. |
| A state transition is legal | Transactional conditional update, state machine, or serialized owner. | Valid, invalid, and concurrent transition tests. |
| A tenant may access only its objects | Server-side authorization plus tenant/object relationship. | Allowed and cross-tenant denied requests. |

Avoid an impossible constraint. Some cross-row/cross-table or external invariants need a transaction, trigger, authoritative service, or reconciliation instead of a row-level check. State the residual failure mode rather than pretending a simple field constraint protects it.

## Design query and index evidence

Inspect actual query shape before adding indexes, caching, partitions, or a new store. Ask:

1. Which operation is slow, costly, or unreliable, and for whom?
2. Which filters, joins, ordering, aggregation, volume, and write costs form the real workload?
3. Is the cause query shape, missing/incorrect index, N+1 behavior, over-fetching, lock contention, or an environmental limit?
4. Can the selected datastore show a plan or equivalent observation?
5. What workload or volume is represented by the evidence, and what remains unrepresented?

Use the narrowest fix that addresses the measured bottleneck. Do not create speculative indexes, partitions, caches, or distributed storage merely because future scale is imaginable. For a financial value, choose exact representation only when the domain requires it; document precision, rounding, currency/unit, and arithmetic ownership rather than applying a generic database type slogan.

## Control concurrent updates

Define the accepted anomaly before choosing the mechanism.

| Situation | Possible control |
| --- | --- |
| Competing edits to one aggregate | Version/ETag/conditional update and explicit conflict response. |
| Cross-row or multi-write invariant | Transaction isolation, constraint, serialized owner, or carefully designed lock. |
| Duplicate command or retry | Natural idempotence, operation identity, deduplication record, or compensation. |
| Asynchronous replicated copy | Owner, ordering assumption, idempotent consumer, reconciliation, and repair route. |

Run an interleaving or conflict scenario that could violate the invariant. Do not equate a single sequential test with concurrency safety. Do not promise exactly-once delivery without platform-specific end-to-end evidence.

## Evolve schema and data safely

Choose the smallest safe sequence from the actual engine, consumers, table/data size, traffic, deployment order, and recovery limit.

For a change that requires coexistence, use an explicit staged plan:

```text
Current and desired shape:
Old/new readers and writers:
Compatibility phase and expiration:
Data movement/backfill unit, idempotency, progress, and throttle:
Reconciliation and stopping threshold:
Switch/cutover condition:
Contraction/retirement condition:
Restore point, forward recovery, and irreversibilities:
```

Separate fast schema compatibility from long-running data movement when the latter has its own locks, retries, volume, or failure modes. A batch needs a stable unit of work, resume behaviour, progress observation, reconciliation, and a limit that stops further harm. Use dual writes only when the owner, consistency strategy, failure handling, and retirement condition are clear.

Do not assume every project needs expand/migrate/contract. A bounded local transition may be safely atomic. A destructive live change, high-traffic backfill, or independent reader/writer path requires the dedicated `database-migration` workflow and just-in-time human approval before execution.

## Handle lifecycle, retention, and deletion

Classify the purpose before choosing a deletion pattern:

| Purpose | Possible state or mechanism |
| --- | --- |
| Product inactivity | Active/inactive state. |
| Temporary recovery | Reversible deletion with defined retention and restore authority. |
| Audit evidence | Immutable or access-controlled audit record with retention purpose. |
| Historical storage | Archive with retrieval and deletion policy. |
| Privacy erasure | Erasure/anonymization and propagation across copies/backups as required. |
| Distributed reference | Tombstone or replacement rule that prevents resurrection. |

Map primary store, indexes, replicas, exports, caches, analytics, queues, and backups when the decision involves deletion, retention, or recovery. Do not claim legal compliance from a generic soft-delete flag. Escalate jurisdiction, retention, or privacy ambiguity.

## Select evidence and stopping conditions

| Claim | Minimum credible evidence |
| --- | --- |
| Schema invariant | Schema inspection and violating-write result. |
| Query/index improvement | Actual plan/observation and representative workload comparison. |
| Compatibility change | Old/new reader-writer matrix and contract/serialization evidence. |
| Backfill | Dry run or rehearsal, batch/retry/resume proof, progress/reconciliation signal. |
| Recovery | Restore or forward-repair rehearsal, or an explicit untested limitation. |
| Deletion/lifecycle | Data map, propagation evidence, authority/retention decision. |

Stop and escalate if the owner, consumer set, invariant, target, lock risk, recovery path, or authority for a consequential data operation is unknown. A passing command is only evidence that that command completed in that environment.
