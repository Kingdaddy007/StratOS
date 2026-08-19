---
id: database-migration
version: 2
status: active
intent: Plan and execute a named database/schema/data transition only with compatibility, recovery, target-specific evidence, and just-in-time human approval for the exact mutation.
use_when: [a schema change, data transformation/backfill, storage transition, constraint/index change, retention/deletion operation, or migration of a live data boundary is requested]
do_not_use_when: [the task is query-only analysis, a data model discussion without a planned mutation, an ordinary local fixture change, or the target/authority/recovery consequence is unknown]
inputs: [current and desired data shape, affected producers/consumers, target database/environment and owner, data characteristics and compatibility constraints, migration/recovery tools actually available, requested authority]
required_resources: [applicable AGENTS.md files, database and architecture capabilities, current schema/migration/project contexts when present, backup/restore and release evidence only where the active project can provide them]
mutation_class: external_or_production
approval_gates: [assessment and plan remain read_only, require explicit approval before writing durable migration artifacts when not already requested, require just-in-time approval immediately before any database/data mutation naming target, exact migration/version, expected effect, affected data/consumers, recovery or containment path, observation window, owner, and evidence plan]
states: [received, assessed, designed, rehearsed, approval-pending, executing, validating, observing, contracted, closed, stopped]
outputs: [migration decision and compatibility record, target-specific execution plan, rehearsal or evidence limits, approval record, checkpoint/result log, validation and recovery/containment outcome, deferred cleanup and next owner]
verification: [check stated data invariants and affected consumer behaviour, record executed versus unexecuted checks and data scope, verify current target/version before mutation, compare relevant performance/availability signals where observable, and preserve evidence of recovery/containment if used]
failure_paths: [stop on missing target/owner/approval/recovery path, incompatible consumer, unsafe lock or data-loss risk, failed checkpoint, integrity anomaly, inability to observe, or a change that exceeds the approved migration]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract; record target, migration version, compatibility state, checkpoints, evidence, approvals, blockers, recovery/containment, owner, timestamps, and next action
next_workflows: [plan-architecture, build-feature, security-audit, incident-response, ship-to-production, verify-project, none]
profiles: [general]
---

# Database Migration

## Purpose and boundary

Data changes are high-consequence because a mistake can affect durable truth, customers, consumers, and recovery. This route does not run a migration merely because a file exists. It turns the exact data transition into an observable, approval-gated plan.

No database or data mutation is permitted during assessment, design, rehearsal, or approval preparation. A local migration file is not approval to run it against any target.

## Assess the actual transition

1. Name the target database/environment, intended migration/version, owner, affected data, producer/consumer paths, and business consequence.
2. Map the current and desired shape, invariants, access/availability constraints, data size/shape where known, and every consumer that must remain compatible.
3. Determine whether an additive/compatibility phase, backfill, dual-read/write period, staged consumer change, later contraction, or a simpler local transition is justified by the actual engine and constraints. Do not make any pattern universal.
4. Define checkpoints, idempotency/retry requirements, ordering, expected side effects, lock/load/budget concern, safe abort criteria, and recovery/containment path.
5. Rehearse only when a safe, representative environment and authorised data exist. If they do not, state the limitation and increase the required approval/observation confidence rather than claiming rehearsal passed.

## Approval record

Before mutation, prepare this exact record:

```text
Target and owner:
Migration/version and action:
Affected data and consumer compatibility:
Expected effect and known risks:
Preconditions/checkpoints:
Recovery or containment path:
Evidence and observation plan:
Exact just-in-time approval requested:
```

The user must approve this current record immediately before execution. A new target, changed migration, changed data scope, or changed recovery path requires a new approval.

## State and execution contract

| State | Required result | Next state |
| --- | --- | --- |
| `received` | Target, requested transition, and owner are identifiable. | `assessed` or `stopped` |
| `assessed` | Current/desired shape, consumers, constraints, and risk are visible. | `designed` or `stopped` |
| `designed` | Compatibility, execution order, checkpoints, recovery, and validation are explicit. | `rehearsed`, `approval-pending`, or `stopped` |
| `rehearsed` | Safe rehearsal evidence or its honest limitation is recorded. | `approval-pending` or `stopped` |
| `approval-pending` | Exact mutation and just-in-time approval request are ready. | `executing` or `stopped` |
| `executing` | Only the approved target/action is performed; checkpoint evidence is preserved. | `validating`, recovery/containment, `incident-response`, or `stopped` |
| `validating` | Stated invariants and affected consumer behaviour are checked to the declared scope. | `observing`, `contracted`, or `stopped` |
| `observing` | Agreed data/application signals are observed for the agreed window. | `contracted`, `closed`, `incident-response`, or `stopped` |
| `contracted` | Old compatibility structures are removed only after a separately approved, evidence-backed decision. | `closed` |
| `closed` | Actual result, evidence, limits, recovery status, and deferred cleanup owner are visible. | Reopen only for a new/changed migration. |
| `stopped` | No unapproved mutation occurs; safe next action or containment owner is explicit. | Reopen only with changed evidence/authority. |

If data integrity, customer impact, or security is threatened, stop improvised changes. Preserve evidence and route active impact to `incident-response` under its separate external-approval contract.

## Delivery record

Report the exact target and mutation performed—or explicitly state that none occurred—alongside compatibility state, checkpoints, validation, observation, recovery/containment outcome, residual risk, deferred contraction, and next owner. Do not call a migration complete merely because its command exited successfully.
