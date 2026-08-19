# V4 Phase 7 — Workflow Truth Audit

**Status:** classification accepted; General, Media, and Spatial direct-route migrations implemented  
**Date:** 2026-08-19  
**Scope:** the prior 52 canonical workflow registrations and their V4
successors; the current registry contains 17 routes.

## Decision being made

A workflow is a coordination contract. Keep one only when it makes a material state, handoff, independent evidence boundary, or approval gate visible. Do not call a useful sequence a workflow merely because it has numbered steps.

A skill supplies specialist judgement. A reference or recipe supplies a selectively loaded method. An agent chooses the smallest applicable combination. No one of those objects automatically requires the others.

This is a structural decision, not a claim that the instructions inside a retired workflow are useless. Before any source file is retired, every useful instruction needs a named destination and a behaviour check.

## Audit method and constraints

The audit parsed the canonical manifest and each workflow's active frontmatter, ownership, profile, mutation class, states, handoffs, and body shape. It then applied the operating-model test:

1. Does the job have meaningful observable state that another person or task must resume?
2. Does it coordinate a real cross-boundary handoff or independent evidence decision?
3. Does it impose an approval gate that cannot safely live as a short skill boundary?
4. Is the task materially safer or clearer as a route than as direct specialist work?

If the answer is no, the default destination is its owning skill or a conditional reference. This keeps ordinary work direct.

Constraints:

- Do not delete deep spatial, media, or engineering guidance for the sake of a smaller count.
- Do not rewrite domain knowledge without the relevant evidence gate.
- Do not let an old route's mandatory context, automatic state writing, or external-action assumptions survive a migration.
- Preserve every current external or production approval gate.

## Options considered

| Option | Benefit | Cost | Decision |
| --- | --- | --- | --- |
| Keep all 32 | No immediate migration work. | Preserves false workflow activation, legacy always-load bodies, and user confusion. | Reject. |
| Remove every route that is not external or destructive now | Fast count reduction. | Would discard or orphan valuable procedures and erase useful coordination. | Reject. |
| Preserve-first reclassification | Reduces public workflows only after each procedure has an owned destination and a regression check. | Requires small, careful migration batches. | **Accept.** |

## Proposed public workflow set: 17 routes

These routes earn public workflow status because they coordinate a material decision, state, evidence boundary, or approval gate. `Conditional` means a small task may still use the owning skill directly.

| Workflow | Profile | Recommendation | Reason and next treatment |
| --- | --- | --- | --- |
| `build-feature` | General | Keep; rewrite legacy body | Approved implementation needs a bounded scope, evidence, and handoff. Its large inherited body must be rebuilt around the current `coding`, design, and assurance boundaries. |
| `commercial-decision-record` | Growth | Keep | Material offer, price, scope, and claim decisions need versioned evidence and a named human approval state. |
| `database-migration` | General | Keep | Compatibility, rollback, production approval, and durable data evidence are real hard gates. |
| `debug-issue` | General | Keep | Separates diagnosis, authorised repair, containment, and root-cause confidence. |
| `dependency-upgrade` | General | Keep | A version change can affect supply chain, compatibility, rollback, and project verification. |
| `design-ui` | General | Keep, conditional | Use only for a material interface decision needing an explicit design handoff; bounded UI work stays direct through `ui-ux`. |
| `incident-response` | General | Keep | Production mitigation and recovery require observable state, authority, and post-incident evidence. |
| `live-learning-loop` | Growth | Keep | An approved, reversible live intervention needs guardrails, rollback, interpretation limits, and a human decision. |
| `os-maintenance` | General | Keep | Canonical OS changes affect host payloads, registry, validation, and compatibility at once. |
| `plan-architecture` | General | Keep; rewrite legacy body | A consequential boundary or data decision needs options, tradeoffs, and an inspectable record. Direct `architecture` work remains correct for smaller decisions. |
| `project-inception` | General | Keep | It turns an uncertain initiative into the smallest decision-ready next step. |
| `security-audit` | General | Keep; rewrite legacy body | Independent security evidence and escalation boundary remain distinct from ordinary code review. |
| `ship-to-production` | General | Keep; rewrite legacy body | Production mutation has a non-negotiable just-in-time approval and rollback/monitoring gate. |
| `spatial-project-inception` | Spatial | Keep | It is the one specialist project coordination route; its phases remain conditional rather than public workflows. |
| `task-dispatch` | General | Keep | It establishes bounded delegation, exclusive scope, return evidence, and integration. |
| `test-strategy` | General | Keep, conditional | A material test/evidence plan needs risk, claim, and specialist handoffs. A local test question stays direct through `testing`. |
| `verify-project` | General | Keep, conditional | It independently interprets evidence without granting release authority. A small local check stays direct. |

## Proposed direct capability and reference set: 15 migrations

Do not perform these moves as a bulk delete. Each row names the target that must absorb the useful content first.

| Current workflow | Profile | Reclassify as | Required destination and safety condition |
| --- | --- | --- | --- |
| `context-hygiene` | General | Direct capability | `context-hygiene` skill plus a small task-handoff reference. Remove its automatic memory-writing assumptions; durable memory/state writes remain authorised, scoped choices. |
| `design-api` | General | Direct architecture operation | `api-design` and `architecture` skills. Preserve only durable API-decision guidance; route material cross-system decisions to `plan-architecture`. |
| `optimize-performance` | General | Direct specialist operation | `performance` skill and a selectively loaded optimisation/check reference. Keep measurement and regression rules, not a generic state envelope. |
| `refactor-module` | General | Direct specialist operation | `refactoring` skill. Preserve behaviour locks, scope boundaries, and verification guidance. |
| `review-code` | General | Direct specialist operation | `review-audit` skill. Keep independent review as a role, not a resumable workflow. |
| `ui-craft` | General | Direct implementation procedure | `ui-ux` with `coding`; preserve state-matrix, accessibility, browser, and reduced-motion checks. A complex product change still begins with `design-ui` or `build-feature`. |
| `ui-animate` | General | Direct implementation procedure | `ui-ux` motion reference; preserve purpose, interruption, reduced-motion, and performance conditions. |
| `impeccable-animate` | Spatial | Conditional Spatial procedure | `cinematic-motion` and the Spatial Project reference set; keep it unavailable to ordinary product UI. |
| `impeccable-craft` | Spatial | Conditional Spatial procedure | `spatial-experience-design` and the Spatial Project reference set; preserve vertical-slice and concept-continuity gates. |
| `reference-intelligence` | Spatial | Direct specialist capability | Existing `reference-intelligence` skill. Preserve its keep/adapt/reject/defer method as a conditional reference route. |
| `spatial-concept` | Spatial | Spatial Project phase | The Spatial Project reference set and `spatial-experience-design`; retain concept comparison and selection record. |
| `spatial-design-ui` | Spatial | Spatial Project phase | `spatial-experience-design` plus relevant UI references; do not make spatial design rules universal. |
| `storytelling` | Spatial | Direct specialist capability | Existing `storytelling` skill; preserve its concept-to-narrative handoff. |
| `video-generation` | Media | Direct specialist capability | Existing `video-generation` skill. Normal provider-aware prompt planning does not need workflow state. A future multi-shot production route is justified only if current Media evidence shows a real asset, cost, rights, or delivery gate. |
| `visual-brainstorm` | Spatial | Spatial Project phase | Spatial Project reference set; preserve genuine divergence before concept selection. |

## Findings that change migration order

1. **Do not delete the large legacy routes yet.** `build-feature`, `plan-architecture`, `security-audit`, and `ship-to-production` still carry inherited always-load bodies. They are real routes, but their bodies need a separate preservation-first rewrite rather than a quick cut.
2. **Fix `context-hygiene` before demotion.** Its current procedure assumes automatic writes to workspace memory and state. That conflicts with V4's conditional authority model, so it cannot simply be copied into a direct skill.
3. **Do not reopen Media content during this audit.** The video route can become direct now because the `video-generation` skill exists; provider/model claims and the large Media pack stay behind their own current-source audit.
4. **Do not flatten Spatial.** Implemented with a dedicated [preservation audit](v4-phase-7-spatial-preservation-audit.md) and phase-routing reference. The seven migrations changed public routing, not whether the protected specialist content is available.

## Implemented first migration — 2026-08-19

The first General direct-route batch is complete. The six workflow wrappers for `design-api`, `optimize-performance`, `refactor-module`, `review-code`, `ui-craft`, and `ui-animate` were removed from the canonical registry only after their owning skills were compared and confirmed to contain the applicable judgement and verification method.

`context-hygiene` was handled separately because its old workflow assumed automatic workspace-memory writes. The direct skill was strengthened with explicit authority, state-isolation, output, and no-write rules before the duplicate route was retired.

The active registry is now **17 workflows**, the target selected by this audit. The seven Spatial wrappers were retired after their skill-owned methods, phase gates, direct-routing fixtures, and host payload destination were verified. The Media public wrapper was retired without changing any provider-specific source content.

## Recommended implementation order

1. **Low-risk General demotions:** reclassify `review-code`, `refactor-module`, `optimize-performance`, `design-api`, `ui-craft`, and `ui-animate` only after their owning skills receive the selected procedure material and direct-route tests.
2. **Context safety repair:** rewrite `context-hygiene` as an authority-safe skill/reference package, then remove its workflow registration.
3. **Spatial routing migration:** implemented. The seven named phases are preserved inside the [Spatial Project reference set](../global/skills/spatial-experience-design/reference/project-phase-routing.md); direct-routing fixtures prove focused work does not create workflow state.
4. **Media route demotion:** implemented. `workflow-video-generation` was retired only after the routing fixture and validator could prove provider-aware planning selects the `video-generation` skill directly; no provider-specific content changed.
5. **Retained-route rewrites:** separately revise the four oversized legacy coordination routes. Each rewrite requires its own source audit and regression checks.

## Verification contract for every migration batch

- The manifest, workflow files, router, catalogue, fixture, and host payload must agree.
- A direct request must not create workflow state merely because it contains a matching word.
- A material/external request must still stop at the appropriate approval gate.
- Every moved procedure must remain discoverable from its owning skill with conditional loading rules.
- Canonical validation, relevant regression fixtures, profile payload builds, and `git diff --check` must pass.

## Result

The target was never “fewest possible files.” The resulting registry has **17 honest coordination routes plus direct skills and references that retain the remaining useful methods**. This preserves expert depth while removing the false idea that every useful instruction is a workflow.
