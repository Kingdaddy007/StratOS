# V4 Phase 7 — Spatial Workflow Preservation Audit

**Status:** preservation map and public-route migration implemented and verified  
**Date:** 2026-08-19

## Scope

This audit reviews the seven proposed Spatial route migrations: `reference-intelligence`, `visual-brainstorm`, `spatial-concept`, `storytelling`, `spatial-design-ui`, `impeccable-craft`, and `impeccable-animate`.

It does not rewrite the protected Spatial skills, change Media provider material, discard legacy knowledge, or claim that an ordinary focused request needs a ten-phase project process.

## Finding

The route bodies carry three different kinds of information:

1. Specialist judgement already owned by `reference-intelligence`, `spatial-experience-design`, `storytelling`, `cinematic-motion`, `ui-ux`, and `master-design-director`.
2. Phase names, entry gates, escalation conditions, and return points that are useful when a project is large enough to coordinate.
3. Task-state wrappers that add little value to a focused request and create the false impression that every Spatial action must be a public workflow.

The first category stays in its owning specialist skill. The second is preserved in [Spatial Project Phase Routing](../global/skills/spatial-experience-design/reference/project-phase-routing.md). The third was the only category removed from the public registry.

## Preservation mapping

| Former public route | Owning direct capability | Preserved gate or decision | Future coordination location |
| --- | --- | --- | --- |
| `reference-intelligence` | `reference-intelligence` | source quality, observation/inference separation, translation approval | Spatial project reference phase |
| `visual-brainstorm` | `spatial-experience-design` | three structural territories, rough test, divergence challenge | Spatial project territory phase |
| `spatial-concept` | `spatial-experience-design`, `storytelling`, `master-design-director` | selection criteria, rejected-option rationale, reversal condition | Spatial project selection phase |
| `storytelling` | `storytelling` | controlling argument, alternative narrative forms, chapter/proof/inquiry jobs | Spatial project experience phase |
| `spatial-design-ui` | `ui-ux`, `spatial-experience-design`, `coding` | production contract, risk prototype, vertical-slice verdict | `build-feature` with Spatial skills, or the project production phase |
| `impeccable-craft` | `build-feature`, `ui-ux`, `spatial-experience-design` | coherent slices, real-enough assets, concept-continuity audit | approved project production phase |
| `impeccable-animate` | `cinematic-motion` | stillness comparison, separate motion ownership, performance/fallback evidence | approved project production phase |

## Migration evidence

- `tests/fixtures/routing.json` now distinguishes a direct skill route from a workflow route and covers focused Spatial reference, story, and motion requests.
- `workflow-spatial-project-inception.md` remains the single stateful coordination route and points to direct capabilities for its phases.
- `spatial-experience-design/reference/project-phase-routing.md` is included in Spatial host payloads.
- Canonical validation and the full test suite pass after the migration.

## What was deliberately not changed

- No specialist reference, motion method, storytelling method, or design-audit material has been compressed or deleted.
- No Spatial source is being made part of the General profile.
- No new Media workflow is being invented.

The seven public wrapper files were retired only after this map, direct-routing fixtures, and the skill-resource destination existed. Their former decisions remain available as direct specialist work or phases inside `spatial-project-inception`.

## Completed migration gate

1. Direct-routing fixtures prove focused requests select their owning skills without workflow state.
2. The existing full Spatial project fixture proves `spatial-project-inception` remains available only with the Spatial pack.
3. Every former next-workflow handoff has a named direct destination or explicit return point in the phase-routing reference.
4. Spatial payload generation was exercised through the host build suite, which checks the phase-routing reference.
5. Canonical validation, the full regression suite, and `git diff --check` pass.

## Decision

The migration is justified only as a **preservation-first routing change**. Seven old command-like routes became direct capabilities or phases inside the one genuine stateful Spatial project route. The work did not disappear.
