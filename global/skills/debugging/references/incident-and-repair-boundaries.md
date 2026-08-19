# Incident and repair boundaries

Load this reference for implementation decisions, a high-risk fault class, or any customer-impacting incident.

## Repair decision

Implementation is a decision, not the default final step of diagnosis. Confirm the requested mode, the established mechanism, smallest credible scope, a validation oracle, and a reversal path before editing. If a result contradicts the mechanism, the patch expands beyond its stated scope, or new high-risk behavior appears, stop and return to diagnosis or proposal.

| Action | Default | Requirement before action |
| --- | --- | --- |
| Inspect code, repository history, non-sensitive local state, existing outputs | Allowed in `diagnose` | Stay within the provided workspace and access boundary. |
| Run a local, isolated reproduction or existing test | Conditional | Declare material filesystem, network, cost, time, or state side effects; stop if unsafe or flaky. |
| Add a temporary diagnostic probe | Conditional | Scope it, make cleanup explicit, and obtain approval if it affects shared/runtime state. |
| Edit product code or tests | `implement` only | Explicit user authorization, established mechanism, minimal scope, validation, and reversal path. |
| Change data, queues, caches, credentials, deployment, traffic, or production configuration | Denied by default | Use the relevant workflow and just-in-time approval naming target, effect, containment/rollback, and evidence. |

## Incident-mitigate

For an active customer-impacting, availability, data-integrity, or serious security incident:

1. Route to `incident-response`; record observed impact, timeline, authority, and available evidence.
2. Preserve the evidence needed to understand the event before destructive cleanup.
3. Prefer the smallest reversible containment or restoration action, but do not execute an external action without its approval gate.
4. Label restoration as `mitigated`; do not call it a root-cause fix unless the diagnosis separately supports that claim.
5. Resume or schedule diagnosis after stabilization, including contributing conditions and prevention work where warranted.

## Verification after an authorized repair

Choose evidence that is proportional to risk and the defect mechanism:

- demonstrate the original failure-before/failure-after where a credible reproduction exists;
- check the relevant contract, invariant, or state transition;
- inspect genuinely similar sibling paths when the same pattern can recur;
- use an independent or differential check when a single test is a weak oracle;
- state any environment gap, unrun check, residual risk, and reversal plan.

Do not state that a repair is verified solely because a suite passed. Do not change tests merely to make a broken behavior green; a test change must protect the intended contract or correct an invalid oracle.
