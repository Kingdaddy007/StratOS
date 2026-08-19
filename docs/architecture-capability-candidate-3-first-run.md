# Architecture Capability Candidate 3 — First-Run Result

**Date:** 2026-08-18  
**Candidate:** Network failure, timeout, retry, and idempotency design  
**Decision:** `revise-and-retest` — do not install as canonical policy.

## Plain-language result

Candidate 3 made the payment answer materially safer. It explicitly treated a timeout as unknown, used stable effect identities and database-enforced uniqueness, bounded retries, and named the right failure tests.

It also stayed quiet on the simple landing-page restyle. But it did not stay fully quiet on the unrelated microservices trap: its answer rejected the twelve-service rewrite, then added a remote-effects section about idempotency, ambiguous timeouts, deadlines, and retries even though the scenario named no remote side effect. That is exactly the kind of negative transfer the suite is designed to catch.

This is a useful first-run finding, not a failed experiment: the candidate needs a sharper activation boundary before it can advance.

## Execution record

- **Conditions:** A (prompt only), B (compact architecture kernel), C (kernel plus Candidate 3).
- **Scenarios:** payment webhook timeout, unjustified microservices request, and landing-page restyle control.
- **Model:** `gpt-5.6-luna` at `max` effort in nine fresh, projectless tasks.
- **Tools:** the tasks were explicitly instructed to use no tools; the host did not expose per-turn token or cost telemetry.
- **Evidence:** each saved answer has a thread ID, start/end timestamps, execution note, and response hash under the ignored pilot bundle.
- **Review:** three fresh Luna Max scenario reviewers received only the judge guide and randomized response files for their assigned scenario. They did not receive the answer key, source prompt bundle, or original response paths. The parent decoded the answer key only after their reviews were complete.

The first attempt at one comprehensive all-dimensions scorecard was interrupted by a host retry loop and was discarded. It supplied no score and was not used. The bounded reviews below are therefore primary scoring-focus comparisons, not a complete survival-gate scorecard.

## Decoded blind review

| Scenario | A | B | C | Result |
| --- | --- | --- | --- | --- |
| Landing-page restyle control | Rank 3; verification slightly implicit | Rank 2; safe and lightweight | **Rank 1**; local scope, rendered-contrast checks, styling-only verification | Candidate caused no adjacent-task harm. |
| Unjustified microservices request | **Rank 1**; proportionate modular-monolith path | Rank 3; heavy cutover/operations ceremony | Rank 2; rejects twelve services but adds unrelated remote-effects material | Candidate fails the anti-bloat control for this run. |
| Payment webhook and ambiguous timeout | Rank 3; broad failure coverage but overbuilt and retry cap implicit | Rank 2; good safety but retry ownership/bounds less explicit | **Rank 1**; explicit unknown timeout, stable IDs, bounded single-owner retries, authoritative uniqueness, and tests | Candidate improves its target behaviour. |

The reviewers reported no critical security or data-integrity miss in the Candidate 3 payment response. Its concrete issue was **activation leakage**, not payment safety.

## Required revision

Candidate 3 now begins with this explicit stop rule:

> Before applying this capability, identify a concrete remote side effect or dependency failure in the request. If none is present, state that no network-effect contract is required and do not add retry, idempotency, deadline, or distributed-effects material.

This revision remains a candidate instruction in the evaluation fixture. It is not an installed skill and it has not changed a user's existing workflow.

## Next gate

Repeat this three-scenario A/B/C set with the revised candidate, then add it to the required independent result sets. Candidate 3 may be promoted only if it:

1. continues to improve the payment-safety response over the kernel;
2. stays out of the microservices trap once no remote effect is in scope;
3. remains quiet on the landing-page control; and
4. satisfies the broader three-independent-result-sets and full survival-gate requirements.

