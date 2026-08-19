---
name: performance
description: 'Use this skill to diagnose, measure, or improve runtime performance, capacity, responsiveness, resource use, caching, retries, or degradation. Trigger on slow pages, interactions, APIs, jobs, high CPU or memory, timeouts, throughput, latency, Core Web Vitals, load, scaling, cache design, or a performance regression. Do not use for a deployment, outage, or infrastructure task that has no performance question; use devops-infra or incident-response instead.'
---

# Performance

## WHEN TO USE THIS

- Diagnose a slow user interaction, request, query, job, render, or resource leak.
- Test a capacity, responsiveness, throughput, or reliability claim.
- Decide whether caching, batching, retry limits, backpressure, or degradation is justified.

## NEVER DO

- Claim an improvement without a comparable baseline and a result at the boundary where harm appears.
- Treat a local or synthetic benchmark as proof of production capacity.
- Require p95, p99, production load, profiling, or caching for every task.
- Add a cache without defining its key, freshness, invalidation, privacy, failure, and cost behaviour.
- Add retries without an idempotency, deadline, retry-budget, and unavailable-dependency decision.
- Execute a production release or external change. Hand it to the approved delivery path.

## FRAME THE DECISION

1. State the affected user or system behaviour, the harm boundary, the consequence, and the decision the evidence must support.
2. Inspect the relevant interaction, request, job, dependency, resource, cache, and existing evidence before changing anything.
3. Write at least two plausible explanations when the cause is not already demonstrated. Select the least intrusive signal that can distinguish them.
4. Classify the work before acting:

| Context | Minimum evidence |
| --- | --- |
| Local or disposable prototype | Reproduction, simple baseline, focused check, and reversal path. |
| Browser or UI experience | Representative interaction, device/network conditions, and client-boundary evidence. |
| API or service | Success/error behaviour, latency or duration measure suited to traffic, dependency/resource evidence, and a comparable workload. |
| Background or batch job | Work-unit success/failure, completion or deadline time, queue age/depth where relevant, retry and partial-work behaviour. |
| External, production, or high-consequence path | A risk-scaled baseline, harm-boundary verification, containment plan, and the required human approval before effect. |

## SELECT EVIDENCE THAT ANSWERS THE QUESTION

- Match the measure to the claim. Measure a browser experience at the client or interaction boundary where practical; do not substitute server time for user experience.
- Name the environment, workload or input mix, concurrency or arrival model, cache and warmup state, dependency behaviour, sample count, measurement window, baseline, and material limitations.
- Label evidence as local, synthetic, staging, field, or production. State the bridge before generalising from one label to another.
- Use central measures, tail measures, completion time, throughput, error rate, queue delay, resource saturation, or qualitative reproduction according to the decision. Use a tail measure when worst-case user harm, fan-out, queueing, burstiness, overload, or an explicit objective makes it decision-relevant.
- Use representative load or real-traffic observation when capacity, concurrency, tail behaviour, costly dependencies, or high-consequence exposure is the decision. Do not create enterprise load infrastructure for a harmless local edit.

## DIAGNOSE, CHANGE, AND VERIFY

1. Establish a comparable baseline, control, unchanged path, prior release, or explicit target.
2. Identify the leading constraint from evidence. Eliminate needless work before making necessary work faster.
3. Make the smallest reversible change that tests the supported hypothesis. Separate instrumentation from behaviour changes when combining them hides causality.
4. Treat caching as an option, not a last-resort ritual. Define the cached value, key, freshness and invalidation rule, consistency tolerance, authorization/privacy boundary, stale/miss/origin-failure behaviour, storage cost, and the evidence of repeated work.
5. Treat degradation as a correctness decision. Name exactly what remains available, what is delayed, dropped, stale, or failed, and the invariant it must not violate.
6. Re-run the appropriate harm-boundary check. Check for errors, data loss, duplicate work, unacceptable delay, or a shifted bottleneck as applicable.
7. State one of: ship through the approved delivery path, hold, revert or disable locally, investigate, or escalate. Stop when evidence meets the stated decision threshold or cannot support a safe conclusion.

## REFERENCE LOADING RULES

- Load [references/extended-guidance.md](references/extended-guidance.md) for browser measurement, load-test design, caching, retry/degradation, queues, or detailed diagnosis and evidence limits.
- Load [references/resource-index.md](references/resource-index.md) when using a dated browser, HTTP, telemetry, or release-engineering claim; verify the linked primary source before applying volatile platform syntax or tool behaviour.
- Route a deployment, production incident, infrastructure provision, alerting design, or recovery procedure to `$devops-infra` or the matching workflow. Keep this skill focused on the performance decision and its evidence.

## OUTPUT SHAPE

```markdown
## Performance decision

- Question and harm boundary:
- Context and risk:
- Baseline and evidence limits:
- Leading hypothesis and evidence:
- Change or recommendation:
- Verification at the harm boundary:
- Tradeoffs, containment, and approval boundary:
- Decision and stopping condition:
```

## NON-NEGOTIABLE CHECKLIST

1. Tie every conclusion to an observable question and comparable evidence.
2. Label workload, environment, and evidence limits.
3. Preserve correctness, privacy, and data integrity when optimising.
4. Escalate before an external, irreversible, or high-consequence effect.
