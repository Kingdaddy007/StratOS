---
name: api-design
description: 'Use when designing or changing an API, webhook, event, RPC boundary, or shared service contract; deciding compatibility, versioning, pagination, rate/cost limits, idempotency, or contract tests. Activate for “design an API”, “endpoint”, “API contract”, “OpenAPI”, “webhook”, “event schema”, “pagination”, “rate limit”, “breaking change”, “idempotency”, or “deprecation”. Do not use for an internal function with no independent consumer (use coding), data-model design without an interface decision (use database), or a full security threat model (use security).'
---

# API Contract Design

## WHEN TO USE THIS

- Create or change a request/response, webhook, event, RPC, or shared-service boundary.
- Assess independent consumers, compatibility, limits, retries, or contract evolution.
- Review an existing interface whose runtime behaviour, documentation, clients, or tests may disagree.

## NEVER DO

- Treat a database table, generated client, or prose document as the contract without checking its owner, consumers, and runtime behaviour.
- Add a version namespace, pagination scheme, rate limit, or compatibility layer merely because every API is assumed to need one.
- Change externally consumed semantics, authorization, ordering, error behaviour, or field meaning without a compatibility decision.
- Trust caller-supplied tenant, owner, role, or protected-property claims as authorization proof.
- Promise rollback when an observed contract, emitted event, data transform, or external side effect cannot be undone.

## CLASSIFY THE BOUNDARY FIRST

Identify the owner, intended consumers, independent deployment, data class, side effects, and recovery limit before selecting a contract shape.

| Boundary | Minimum contract work |
| --- | --- |
| Local and coordinated | Use a typed signature, examples, and targeted tests. Record why the caller set is bounded. |
| Internal but independently deployed | Record the consumer set, compatibility impact, ownership, errors, and a change window. |
| Public or partner-facing | Define an explicit machine-readable contract, consumer compatibility path, security/ownership checks, support and sunset terms. |
| Asynchronous event or webhook | Define identity, producer, consumer expectations, ordering, delivery/replay behaviour, duplicate handling, and schema-resolution policy. |

If ownership or the likely consumer set is unclear, do not silently widen a shared or external contract. Investigate the repository and deployment context. Proceed under a stated assumption only when the task is demonstrably local and reversible.

## WRITE THE CONTRACT DELTA

For a non-local boundary, state only the facts needed to make the next decision:

```text
Owner and known consumers:
Operation or event:
Request/input and response/output:
Errors, ordering, and limits:
Authorization subject, object, action, and protected properties:
Idempotency and concurrency behaviour:
Compatibility classification and recovery limit:
Evidence and approval boundary:
```

For an existing contract, compare the intended delta against current source, generated clients, tests, runtime behaviour, and deployed behaviour where evidence is available. Classify disagreement as stale artifact, implementation defect, intended contract change, or unresolved conflict. Escalate unresolved conflict to the contract owner; do not choose the most convenient artifact.

## PRESERVE COMPATIBILITY PROPORTIONALLY

Classify each change as additive, behaviourally narrowing, behaviourally widening, or breaking. Check semantic compatibility as well as field shape: defaults, units, ordering, authorization, error semantics, and unknown-field behaviour can affect existing consumers.

- Use a version, explicit compatibility window, capability negotiation, coordinated deployment, or another compatible path when independent consumers or a public commitment make coordination non-trivial.
- Keep a local, coordinated interface simple when its callers deploy together and a change is reversible.
- Treat a consumed asynchronous event as independently deployed unless evidence shows otherwise.
- Define an explicit sunset/retirement condition before carrying an old contract indefinitely.

## BOUND RESPONSES, COST, RETRIES, AND CONCURRENCY

Give every list a proven safe bound or an explicit limit. Add pagination, cursor/keyset, streaming, or another continuation contract only when collection growth, computation cost, serialization cost, or untrusted workload makes a bound unsafe. Define stable ordering and continuation behaviour whenever continuation exists.

Limit requests or cost at the identity or resource boundary when abuse, overload, paid effects, or automated sensitive business flows are plausible. Define reject, retry, and observability behaviour. Do not add arbitrary throttles to local, trusted, bounded calls.

When an uncertain outcome can duplicate a meaningful effect, make replay safe through natural idempotence or a scoped idempotency mechanism. Bind it to the request meaning, define retention and concurrent-use behaviour, and test the timeout/replay case. Choose optimistic concurrency, conditional updates, transactions, or another control from the invariant and expected contention; do not assume last-write-wins is harmless.

## ENFORCE OWNERSHIP AND ROUTE HIGHER RISK

Derive authorization server-side. For an external or multi-user boundary, check object, tenant, function, and protected-property access independently. Test both allowed and denied paths through the actual enforcement layer. Use `security` for threat modelling, identity design, sensitive data, or security ambiguity.

Use `database` when persistence invariants, model choice, concurrency, lifecycle, or migration shape affects the contract. Use `database-migration` when a live schema/data transition needs its approval-gated workflow. A contract decision does not authorize deployment, data mutation, messaging, or an external provider call.

## SELECT EVIDENCE AND STOP

- Local boundary: target the signature, examples, and changed behaviour.
- Shared or external boundary: add contract/consumer evidence, relevant failure cases, and compatibility checks.
- Identity, tenant, or property boundary: add positive and denial tests through the real path.
- Retry, queue, or event boundary: test duplicate, order, timeout, and replay behaviour that matters to the invariant.
- Destructive, public, paid, privacy-sensitive, or difficult-to-reverse change: state recovery limits, add the relevant specialist review, and obtain required human approval before the effect.

Stop when consumer scope, compatibility, invariants, and evidence are credible for the declared risk. Reopen the decision when a new consumer, inconsistent artifact, unbounded workload, or recovery gap appears.

## REFERENCE LOADING RULES

- Load [extended-guidance.md](references/extended-guidance.md) for public/partner APIs, independently deployed consumers, events/webhooks, pagination, rate/cost limits, idempotency, concurrency, generated clients, or contract disagreement.
- Load [resource-index.md](references/resource-index.md) when verifying current protocol, security, or implementation facts against primary sources.
- Use `testing` for evidence design and `review-audit` for an independent contract/change review. Do not use their output as release approval.

## OUTPUT SHAPE

```text
Boundary and consumer classification:
Contract delta and compatibility decision:
Ownership, invariants, limits, retry/concurrency behaviour:
Evidence actually available and recovery limit:
Required approval or next handoff:
```

## NON-NEGOTIABLE CHECKLIST

1. Identify the owner, consumers, side effects, and independent deployment before adding ceremony.
2. Resolve contract-artifact disagreement explicitly.
3. Match compatibility, limits, and evidence to actual consequence.
4. Test authorization denials where a trust boundary exists.
5. State unrecoverable effects and approval gates honestly.
