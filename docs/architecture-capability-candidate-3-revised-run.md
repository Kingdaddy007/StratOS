# Architecture Capability Candidate 3 — Revised First-Run Result

**Date:** 2026-08-18  
**Candidate:** Network failure, timeout, retry, and idempotency design, revised activation rule  
**Decision:** `advance-to-replication` — not approved or installed.

## What changed

The first Candidate 3 run found that the capability added a remote-effects section to a microservices-planning request that contained no remote side effect. The candidate gained an explicit non-activation rule: it must identify a concrete remote side effect or dependency failure before adding retry, idempotency, deadline, or distributed-effects material.

This run used fresh A/B/C responses; it did not reuse answers from the previous run.

## Execution record

- **Conditions:** A (prompt only), B (compact architecture kernel), C (kernel plus revised Candidate 3).
- **Scenarios:** payment webhook timeout, unjustified microservices request, and landing-page restyle control.
- **Model:** `gpt-5.6-luna` at `max` effort in nine fresh, projectless tasks.
- **Tools:** the tasks were instructed to use no tools; per-turn token and cost telemetry were unavailable.
- **Evidence:** all nine responses have thread IDs, timestamps, response hashes, and execution notes in the ignored pilot bundle.
- **Review:** three fresh Luna Max reviewers received only the guide and the three randomized response files for their assigned scenario. The answer key was decoded only after review.

The review used each scenario's declared scoring-focus dimensions. That is the current proportional scorecard design; it does not replace the full three-independent-result-sets promotion requirement.

## Decoded blind review

| Scenario | A | B | C | Result |
| --- | --- | --- | --- | --- |
| Landing-page restyle control | Rank 3; lacked explicit rendered-contrast verification | **Rank 1**; local with strong checks | Rank 2; stayed local, with one minor irrelevant reliability-boundary sentence | No structural or workflow harm from Candidate 3. |
| Unjustified microservices request | Rank 2; sound but broad operational foundation | Rank 3; defaults to event infrastructure | **Rank 1**; preserves the monolith, makes extraction evidence-gated, and limits distributed machinery | The activation leak found in the first run was removed. |
| Payment webhook and ambiguous timeout | Rank 3; retry bounds incomplete | Rank 2; sound but less explicit | **Rank 1**; explicit effect identity, ambiguity, bounded retry ownership, atomicity, and concurrency evidence | Candidate 3 improved its target behaviour over the kernel. |

No reviewer found a critical security or data-integrity miss in the Candidate 3 responses. The landing-page note is deliberately retained as residual risk: even a short statement about irrelevant network effects consumes attention, so future replications should keep Candidate 3 completely silent when its activation condition is absent.

## Decision

The revised candidate clears the **first-run** safety and usefulness screen:

- it outperformed the kernel on its target payment fixture;
- it avoided the prior unrelated network-effects detour in the microservices trap;
- it did not add architecture, dependencies, or workflow machinery to the visual control; and
- its improvement mechanism is observable rather than a change in preferred technology.

It does **not** clear the promotion gate. This is one fresh result set for a revised candidate, whereas the evaluation protocol requires three independent result sets before a candidate can be accepted, installed, or described as having passed all survival gates.

## Next gate

Run two additional independent A/B/C result sets for this exact candidate instruction, with the same target and control scenarios. If it remains stronger on payment safety and silent on unrelated tasks, then decide whether it belongs as a compact conditional architecture capability, a reference, or a deterministic tool-assisted check.

