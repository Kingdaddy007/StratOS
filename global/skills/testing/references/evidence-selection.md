# Evidence selection by risk and boundary

Load this reference when selecting evidence for a non-trivial change, test plan, test review, or a claim that extends beyond local logic.

## Choose evidence from the risk, not a fixed hierarchy

Test levels trade speed, isolation, realism, and maintenance. Use the lightest credible combination, then add evidence when a material boundary is not exercised. A pyramid or trophy is a discussion aid, not a target shape.

| Change or risk | Minimum credible evidence | Escalate when | Common false confidence |
| --- | --- | --- | --- |
| Narrow deterministic local behavior | Behavior-focused unit/component evidence, meaningful boundary and negative cases, relevant static/type checks. | Hidden shared state, parsing/serialization, unclear oracle, broad callers, or prior boundary failure. | Testing the changed branch without asserting observable behavior. |
| Public API or data contract | Transformation tests, serialization/deserialization, contract/provider or consumer checks, representative integration. | Multiple consumers, versioning, async delivery, compatibility uncertainty, or production data diversity. | Client and server mocks agreeing with each other. |
| Persistence, queue, cache, configuration, time, or concurrency | Boundary integration with realistic state/serialization, failure/retry/order cases, repeatability and invariant checks. | Migration, data loss, race sensitivity, cross-process coordination, or shared infrastructure. | Clearing state, retrying, or mocking the boundary instead of proving the state transition. |
| Authentication, authorization, or sensitive data | Positive and negative identity/role/tenant/resource/action matrix through the real enforcement path; security handoff. | Privilege escalation, external identity, sensitive data, policy ambiguity, or production access. | Testing a policy helper while skipping middleware, routing, claims parsing, or data filtering. |
| Critical UI journey | Focused behavior checks plus a browser journey through the user boundary. | Consent, payment, account recovery, accessibility, cross-browser, or severe trust consequence. | One mocked component or one browser success treated as journey reliability. |
| High-impact or hard-to-reverse release | Relevant lower-level evidence, representative integration, security/operational evidence, rollback/containment plan, and explicit release route. | No representative environment, weak observability, migration, or irreversible effect. | Green CI treated as deployment authorization. |

For a database change, route to `database-migration` when the migration itself needs its dedicated safety process. Test prior states, invariants, compatibility windows, recovery/forward-fix options, and representative data behavior where the risk requires them. Do not infer production safety from an empty in-memory database.

## Boundary-specific questions

- **API/contract:** Are status/error semantics, null/missing/unknown values, ordering, idempotency, and known consumers covered where relevant?
- **Persistence/state:** Does the test observe the actual serialization, transaction, cache/invalidation, retry, and recovery behavior at risk?
- **Identity/security:** Are forbidden as well as allowed actions tested through the enforcement layer? Has Security been engaged when the scope requires it?
- **Time/concurrency:** Is the clock, schedule, shared state, retry, or ordering controlled or at least characterized? What distribution remains untested?
- **User journey:** Does the selected interaction include the real user-visible transition and critical failure state, not only a component implementation?

## Test assets and maintenance cost

Prefer evidence that is interpretable and maintainable. A test becomes expensive when it depends on brittle selectors, broad snapshots, live services, unstable timing, hidden shared state, enormous fixtures, or a private implementation structure likely to change. Do not replace necessary boundary realism with convenience; state the cost tradeoff instead.
