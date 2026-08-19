# UI Craft and UI Animate: Method-Parity Audit

**Status:** audit only — no source behaviour has been changed by this document
**Date:** 2026-08-19
**Scope:** compare the deleted general workflows in `HEAD` with the currently reachable direct skills and references.

## Decision being tested

The question is not “can these old workflow files be deleted?” It is:

> If an agent is asked to design or build a real product interface, can it still discover every useful part of the old method at the correct moment, without being forced through an oversized project process?

The appropriate outcome could be any of the following:

- the old workflow was genuinely duplicated and can remain deleted;
- its useful method should live in one or more selectively loaded references;
- it deserves a small direct skill; or
- it really needs a stateful workflow.

No conclusion is allowed until content and discoverability are both checked.

## Sources inspected

- Historical `global/workflows/workflow-ui-craft.md`
- Historical `global/workflows/workflow-ui-animate.md`
- Current `global/skills/ui-ux/SKILL.md`
- Current `global/skills/ui-ux/reference/operation-routing.md`
- Current `global/skills/ui-ux/reference/interface-operation-playbook.md`
- Current `global/skills/ui-ux/reference/motion-design.md`
- Current `global/skills/ui-ux/reference/product.md`
- Current `global/skills/ui-ux/reference/interaction-design.md`
- Current `global/skills/ui-ux/reference/responsive-design.md`
- Current `global/skills/cinematic-motion/SKILL.md`
- Current `global/skills/coding/SKILL.md`

Historical source remains recoverable from Git. It has not been treated as disposable evidence.

## `workflow-ui-craft` comparison

### What the former workflow was really for

It was a practical **general product-interface implementation method**. It was not a spatial-design workflow, and it was not just a visual checklist. Its value was that it connected product intent, state design, existing system primitives, implementation, browser inspection, and an honest handoff.

### Step-by-step preservation result

| Former instruction | Current destination | Result | What this means |
| --- | --- | --- | --- |
| Work only within approved UI scope; do not silently alter APIs, authorisation, data models, dependencies, or production systems. | `ui-ux/SKILL.md` “Never Do” boundary plus root authority policy. | **Preserved** | This boundary is now clearer and portable. |
| Read local contracts and active project context. | `ui-ux/SKILL.md`, Ground the interface. | **Preserved** | It now explicitly reads project context, `PRODUCT.md`, and `DESIGN.md` when present. |
| Confirm user goal, critical journey, information hierarchy, and design system. | `ui-ux/SKILL.md`, Ground + Map structure and flow. | **Preserved** | This is one of the strongest parts of the current skill. |
| Define loading, empty, error, success, disabled, permission, offline, destructive, and recovery states when applicable. | `ui-ux/SKILL.md`, Never Do + State matrix; `reference/product.md`; `reference/interaction-design.md`. | **Preserved** | The current route is stronger: it also names validation timing and retry behaviour. |
| Map components **and data boundaries**; reuse existing primitives before adding new ones. | `ui-ux/SKILL.md` says reuse the active design system; `coding/SKILL.md` says follow existing project patterns. | **Partially preserved** | Reuse is present. The explicit design question “what visible state owns which data and failure?” is no longer named clearly enough. |
| Implement semantic structure, labels, keyboard behaviour, focus management, responsive rules, and error handling. | `ui-ux/SKILL.md` and `reference/interaction-design.md`. | **Preserved** | The current material is more detailed for labels, focus, keyboard, and interactive states. |
| Run applicable project-native tests, types, lint, and build. | `coding/SKILL.md`, `testing`, and project-level verification routes. | **Partially preserved** | The checks exist elsewhere, but a direct `ui-ux` implementation route does not explicitly remind the agent to use the project’s own checks after changing code. |
| Inspect critical viewports and states in a browser; record screenshots/equivalent, console/network errors, keyboard traversal, and reduced-motion behaviour. | `ui-ux/SKILL.md`, Verify observable behaviour; `browser-test`. | **Preserved** | The current skill retains the correct evidence mindset. Browser-specific procedures remain separate, which is appropriate. |
| Deliver changed files, evidence, unknowns, and residual risks. | `ui-ux/SKILL.md`, Output Contract. | **Partially preserved** | Evidence and residual risk are present. A changed-artifact list is not explicit in the direct UI output. |
| Do not call the work complete until the critical journey works and failures are recoverable. | `ui-ux/SKILL.md`, Completion Gate. | **Preserved** | The present completion gate is at least as clear. |

### UI Craft verdict

**The core method is substantially preserved, but the deletion is not yet fully justified.**

Three useful implementation-facing details currently lack a single, discoverable home:

1. map the boundary between interface state and the data/failure it represents;
2. after authorised code changes, run the relevant project-native checks, not only browser inspection; and
3. return the changed-artifact list alongside evidence and known gaps.

These are not reasons to restore a stateful `ui-craft` workflow. They are small, stable, reusable instructions. The likely best home is a new conditional **UI implementation and handoff reference** under `ui-ux`, loaded only when an agent is changing interface code.

That would preserve the method without forcing every design task to create workflow state.

## `workflow-ui-animate` comparison

### What the former workflow was really for

It was a **general product-motion method**, not the cinematic/spatial motion system. It helped an agent decide whether an ordinary UI transition deserved to exist, define it completely, implement it with the lightest adequate technique, and verify it across real inputs and accessibility preferences.

This distinction matters. A product dashboard’s loading transition, a form’s error confirmation, and a spatial showroom’s scroll choreography should not be governed by the same amount of machinery.

### Step-by-step preservation result

| Former instruction | Current destination | Result | What this means |
| --- | --- | --- | --- |
| Name a user-facing purpose: feedback, continuity, hierarchy, progress, or orientation. | `ui-ux/SKILL.md` and `reference/product.md`; `cinematic-motion` for spatial work. | **Preserved** | Current guidance correctly rejects decorative motion. |
| Define trigger, affected property, duration, easing, interruption behaviour, and reduced-motion alternative. | `ui-ux/reference/motion-design.md` covers duration, easing, property cost, and reduced motion. | **Partially preserved** | A concrete product-motion contract does not yet explicitly bring together trigger, interruption, and a required alternative in one place. |
| Prefer transform/opacity where appropriate; do not delay required actions or animate inaccessible hidden state. | `motion-design.md`; `ui-ux/SKILL.md`. | **Mostly preserved** | The newer reference correctly allows carefully bounded non-transform effects when they serve the interface. The “do not delay required action” rule should be retained explicitly. |
| Reuse existing project motion primitives before adding a dependency. | `coding/SKILL.md` has an existing-pattern rule; `cinematic-motion` makes new heavy tools conditional. | **Partially preserved** | The direct product-motion route needs an explicit “use existing tokens/primitives first” instruction. |
| Verify pointer, keyboard, touch, interrupted transitions, narrow viewports, reduced motion, and layout stability. | `ui-ux` interaction/responsive references plus `motion-design.md`. | **Partially preserved** | The individual checks exist, but an agent asked to “animate this” is not clearly directed to load the full relevant set. Interrupted transitions and input parity are especially easy to miss. |
| Remove motion that does not improve the chosen purpose. | `ui-ux/SKILL.md`; `motion-design.md`; `cinematic-motion`. | **Preserved** | This is a strong current rule. |
| Deliver purpose-to-motion mapping, fallback, performance evidence, and residual risk. | General `ui-ux` Output Contract. | **Partially preserved** | General evidence exists, but the useful motion-specific deliverable is no longer explicit. |

### UI Animate verdict

**The design philosophy is preserved; the practical general-product motion method is only partly preserved.**

The correct action is **not** to push ordinary product motion into `cinematic-motion`, which is deliberately spatial and media-heavy. It is also not necessary to revive a stateful `ui-animate` workflow.

The likely best home is a concise conditional section or reference within `ui-ux` called something like **Product Motion Contract**. It should load only when an interface transition is being designed or implemented, and should contain:

```text
purpose -> trigger -> affected state/property -> duration/easing -> interruption rule
-> existing primitive or justified technique -> reduced-motion behaviour
-> input/device parity -> layout/performance check -> evidence
```

It should explicitly say: simple product motion stays with UI/UX; spatial, cinematic, scroll-driven, canvas, WebGL, or media choreography escalates to `cinematic-motion` only when that richer treatment is genuinely justified.

## Combined conclusion

| Old file | Is its stateful workflow wrapper still justified? | Is its useful method safely preserved today? | Next action |
| --- | --- | --- | --- |
| `workflow-ui-craft` | No, not for ordinary direct interface work. | Not completely. | Rehome the three missing implementation/handoff rules as an optional `ui-ux` reference, then run a route test. |
| `workflow-ui-animate` | No, not for ordinary direct product motion. | Not completely. | Rehome the product-motion contract under `ui-ux`; preserve `cinematic-motion` only for its intended spatial/media work. |

## What must be true before changing source

Before applying the proposed rehomes, test the intended routes against these scenarios:

1. **A simple product form:** build a validation/error state with no cinematic motion. The route must use `ui-ux` and not load the spatial pack.
2. **A dashboard interaction:** add a purposeful state transition that respects keyboard, touch, interruption, and reduced motion. The route must use the Product Motion Contract, not cinematic tools.
3. **An interior-studio gallery:** use approved non-trivial scroll motion. The route may load `cinematic-motion` and optionally `motion-library`, but must preserve usability and fallbacks.
4. **A small spacing correction:** use no workflow and no excessive checklist.

If these routes work, then the old wrapper deletions will be justified because the useful methods are both preserved and easier to invoke. Until then, the old files remain recoverable and their deletion is provisional.

## What this audit does not conclude

- It does not decide whether the spatial workflows are safe to consolidate; they require their own parity audit.
- It does not assess whether the existing motion library’s examples are current, safe, or all worth retaining.
- It does not change any production source, workflow count, skill count, or manifest entry.
- It does not require external research. The missing pieces are stable method/handoff instructions already evidenced by the historical source. Research is needed only if we later propose new current-practice claims.
