# Contract Evolution and Boundary Evidence

## Contents

- [Resolve contract disagreement](#resolve-contract-disagreement)
- [Choose a compatibility path](#choose-a-compatibility-path)
- [Bound lists and resource cost](#bound-lists-and-resource-cost)
- [Make retries and concurrent writes safe](#make-retries-and-concurrent-writes-safe)
- [Secure identity and object access](#secure-identity-and-object-access)
- [Evolve events and webhooks](#evolve-events-and-webhooks)
- [Select evidence](#select-evidence)

## Resolve contract disagreement

Inspect the explicitly owned contract artifact, current implementation, tests, generated clients, and observed runtime/deployed behaviour when available. Do not rank them by filename or readability.

When they disagree, create a compact discrepancy record:

```text
Claimed contract:
Observed implementation/client/test behaviour:
Known consumers and consequence:
Likely classification: stale artifact | defect | intended change | unresolved conflict
Owner and decision required:
Evidence needed to reconcile it:
```

Do not silently update a specification to match a defect, or change runtime behaviour to match stale prose. Resolve the owner decision before expanding the change.

## Choose a compatibility path

Classify the change before deciding its mechanism.

| Change | Check before proceeding |
| --- | --- |
| Additive field or operation | Unknown-field behaviour, defaults, response strictness, generated-client behavior, and semantic expectations. |
| Narrowing validation, authorization, or limits | Which existing callers become rejected, throttled, or unable to observe data? |
| Rename, removal, type/meaning/unit/order change | Consumer migration, compatibility window, fallback, and sunset condition. |
| Local coordinated interface | Whether callers truly deploy together and no durable external consumer exists. |
| Event/webhook change | Old/new producer and consumer combinations, replay, duplicate delivery, ordering, and retention. |

Versioning is one possible compatibility mechanism. Choose a version identity, coordinated deployment, adapter, dual-read period, capability negotiation, or other approach only after identifying independent consumers and the transition need. Do not keep a compatibility path without an owner and retirement condition.

## Bound lists and resource cost

For any collection, establish one of these facts:

1. It has a documented small bound and cheap response cost.
2. It has a maximum response size or item limit.
3. It has a continuation contract with stable ordering, filtering semantics, defaults, maximums, and invalid/expired-token behaviour.
4. It is intentionally streamed, with backpressure, cancellation, cost, and failure semantics defined.

Use an identity/resource/cost boundary for request limits when untrusted callers, independently scaled consumers, scarce compute, paid providers, or abuse-sensitive flows are present. Define what rejection looks like, whether a caller may retry, and what signal permits the owner to adjust the limit. Do not use rate limiting to conceal an undefined workload or authorization problem.

## Make retries and concurrent writes safe

For each meaningful side effect, ask:

- Can the caller lose the response after the effect commits?
- Can a queue redeliver the message?
- Can two callers update the same invariant concurrently?
- What identity makes two attempts the same business operation?

Use natural idempotence where the desired final state is inherently repeatable. Otherwise define a scoped key or equivalent identity, bind it to the request meaning, specify retention, handle concurrent reuse, and return a defined replay result. Test timeout/retry and duplicate-delivery behaviour.

Choose concurrency control from the invariant: conditional update/version/ETag for competing edits, datastore constraint for cross-writer uniqueness, transaction isolation for a multi-write invariant, or an explicit conflict response where human resolution is accepted. Do not claim exactly-once delivery without an end-to-end mechanism and evidence.

## Secure identity and object access

For a trust boundary, map:

| Check | Question |
| --- | --- |
| Subject | Who is authenticated, and how is that identity established? |
| Object/tenant | May this subject access this specific resource in this specific tenant? |
| Function | May this role invoke this operation, including administrative variants? |
| Property | May this subject read or write each protected field? |
| Cost/abuse | Can this action exhaust a scarce resource or a sensitive business flow? |

Derive authority from server-side identity and authoritative ownership data. Do not trust a path, body field, UI state, or client claim as proof. Test unauthenticated, wrong-tenant, wrong-role, protected-property, and permitted cases through the actual enforcement path. Route policy ambiguity and threat-model work to `security`.

## Evolve events and webhooks

Record event identity, schema owner, producer, consumer set, ordering expectation, delivery guarantee, retry/duplicate behaviour, replay source, retention, and dead-letter/repair plan.

Treat a consumed event as a compatibility boundary. An additive change can still break strict consumers; a field rename is breaking unless readers understand both forms. Prefer a bounded additive period, adapter, or replacement event when independent consumers must coexist. Verify old-reader/new-event and new-reader/old-event cases where those combinations are supported.

Validate webhook signatures and incoming payload shape at the receiving boundary. Handle duplicate delivery and retry explicitly. Do not make the sender's documentation your sole evidence of actual delivery semantics.

## Select evidence

| Claim | Credible evidence |
| --- | --- |
| Local contract | Type/signature, focused behavior test, direct consumer inspection. |
| External compatibility | Contract diff, consumer matrix, old/new combination test, explicit transition and sunset. |
| Object/tenant/property authorization | Allowed and denied path through real middleware/routing/data filtering. |
| List/limit contract | Cardinality or workload bound, ordering/continuation test, limit/rejection behavior. |
| Retry/idempotency | Timeout/replay/duplicate test proving the intended business effect count. |
| Event evolution | Producer/consumer compatibility and replay/duplicate evidence. |

State which environment, consumer, or failure path remains untested. Green local checks do not prove deployed compatibility.
