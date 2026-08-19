# Performance Evidence and Intervention Guide

## Contents

- [Choose the measurement](#choose-the-measurement)
- [Diagnose by boundary](#diagnose-by-boundary)
- [Design a credible comparison](#design-a-credible-comparison)
- [Cache, retry, and degradation decisions](#cache-retry-and-degradation-decisions)
- [Capacity and load evidence](#capacity-and-load-evidence)
- [Anti-patterns](#anti-patterns)
- [Evidence record](#evidence-record)

## Choose the measurement

| Claim | Prefer | Avoid |
| --- | --- | --- |
| A page or interaction feels slow | Interaction, render, network, and device evidence at the client boundary | Declaring success from server time alone |
| An API regressed | Success/error behaviour plus central and, when relevant, tail latency under a named workload | A percentile without the observation count or workload |
| A batch job is late | Completion time, deadline success, queue age, failed/duplicate work, and throughput | Forcing request-percentile language onto a job |
| CPU, memory, lock, or render cost is suspected | A suitable profile or runtime trace after a focused hypothesis | High-overhead instrumentation that materially changes the behaviour being diagnosed |
| A dependency is slow or failing | Dependency duration/outcome, timeout/retry count, queueing and saturation evidence | Adding retries before deciding whether the operation is safe to repeat |

Use mean or median to describe typical behaviour. Add a tail measure when slow outcomes themselves change the decision. State why the chosen statistic answers the question. A small or changing sample does not establish a stable population percentile.

## Diagnose by boundary

Inspect the path where harm appears before choosing the mechanism:

- **Browser/UI:** capture the representative interaction, device/network conditions, runtime work, rendering, assets, and dependent requests. Use field evidence only when it exists and state when laboratory evidence is substituted.
- **Request/service:** inspect entry, application work, data access, external calls, serialization, timeouts/retries, queues, and saturation. Add traces only when correlation through the path cannot be reconstructed from simpler evidence.
- **Data access:** inspect query shape, query count, plans where available, cardinality, lock/transaction scope, cache effects, and connection use. Do not assume an index is the answer before observing the access pattern.
- **Job/queue:** inspect work-unit semantics, arrival and drain rate, queue age/depth, retry/duplicate handling, deadlines, checkpoints, and downstream failure.
- **Resource leak:** compare resource use across a repeatable scenario and time window. Separate a temporary allocation peak from retained growth.

## Design a credible comparison

Keep treatment and baseline comparable. Record the input or request mix, arrival/concurrency model, data state, cache state, warmup, device/network conditions, dependency behaviour, build/version, measurement overhead, sample count, and time window.

Use an unchanged path, prior release, treatment/control, or explicit target. If the baseline changed, say so and narrow the conclusion. Label synthetic results as synthetic; state which user, traffic, data, and dependency conditions they omit. Escalate from local or synthetic evidence only when the decision needs capacity, tail, concurrency, or production-exposure confidence.

## Cache, retry, and degradation decisions

### Cache

Before adding a cache, write:

```text
Value and owner:
Key and variation inputs:
Freshness and invalidation:
Consistency tolerance:
Authorization and privacy boundary:
Miss, stale, eviction, and origin-failure behaviour:
Storage/cost limit:
Evidence of repeated work or transfer:
```

Treat personalized or authenticated responses as a privacy boundary. Follow the applicable HTTP cache semantics; do not infer safe sharing from a URL alone.

### Retry and timeout

Before retrying, decide:

```text
Operation and side effect:
Idempotency or idempotency key:
Deadline:
Retry budget, backoff, and jitter:
Dependency-unavailable behaviour:
User-visible result and recovery path:
```

Avoid automatic retry where repeat execution can duplicate an external or durable effect and the safety mechanism is uncertain. Observe queue growth and dependency pressure; retry amplification is a failure mode, not a cure.

### Degradation

Name the degraded behaviour: stale public content, optional feature disabled, low-priority work deferred, bounded failure, or queued recovery. Reject a degradation plan that can disclose data, create an irreversible duplicate effect, violate a business invariant, or conceal a safety hazard.

## Capacity and load evidence

Use the smallest representative evidence that can change the decision. A local microbenchmark may answer an algorithm comparison. A service capacity claim may require a workload that represents arrival pattern, concurrency, cache effects, dependencies, and the relevant failure behaviour. Closed-loop generators can hide queueing by reducing demand when a system slows; state the load model and its limits.

Stop when the stated target is met with evidence suited to the risk, when further improvement has no demonstrated user or business value, or when additional complexity and blast radius exceed expected benefit. Stop and escalate if the workload is unrepresentative, measurements conflict, the baseline moved, instrumentation perturbs the result, or recovery cannot be demonstrated.

## Anti-patterns

| Anti-pattern | What it is | Fix |
| --- | --- | --- |
| Metric substitution | Server time is used to prove a browser experience improved | Measure at the client/interaction boundary or state the missing bridge |
| Percentile ritual | p99 is required for a small local tool without a tail-risk decision | Choose a statistic matched to the consequence and sample |
| Benchmark overclaim | Laptop or synthetic results are presented as production capacity | Label evidence, name omissions, and escalate only when necessary |
| Cache-by-URL | Personalized data is shared because keying/privacy was not designed | Define variation, authorization, freshness, and cross-user tests |
| Retry amplification | Timed-out work is blindly repeated during dependency failure | Define idempotency, budget, deadline, and unavailable-state behaviour |
| Multi-change causality loss | Cache, query, library, and infrastructure changes land together | Narrow the change or separate evidence and behaviour changes |
| Tuning without a decision | Work continues after target/value is already clear | Set a decision threshold and stopping condition |

## Evidence record

```markdown
## Evidence record

- Claim and harm boundary:
- Environment and version:
- Workload, concurrency, cache/warmup state:
- Method and measurement overhead:
- Baseline/control:
- Results and observation count:
- Limitations and excluded conditions:
- Decision threshold, result, and next action:
```
