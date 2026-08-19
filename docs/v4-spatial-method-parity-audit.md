# Spatial Website Method-Parity Audit

**Status:** audit only — no skill, reference, workflow, manifest, or generated adapter was changed by this document
**Date:** 2026-08-19
**Scope:** compare the deleted spatial phase workflows in `HEAD` with the current spatial coordinator, skills, and selective references.

## The key finding

The important spatial website method was **not simply deleted**. The current `workflow-spatial-project-inception.md` retains the ten-phase project process and calls the specialist skills at the relevant points.

The design is now:

```text
One full spatial project needs coordination over time
    -> workflow-spatial-project-inception

A bounded design question needs specialist judgement
    -> direct skill(s), with only the reference needed for that question
```

That is the right high-level shape. It prevents seven separate project workflows from turning one website into a rigid relay race.

However, there is one genuine problem: some former phases can now be requested directly (“help me choose a concept”, “make this gallery motion work”), and the short direct-routing table does not always make the full detailed method as discoverable as the original phase workflow did. The method is largely present; the direct entry points need a more rigorous parity/discoverability check before their old wrappers are considered permanently retired.

## What the full spatial project workflow currently preserves

`workflow-spatial-project-inception.md` still contains these coordinated phases:

1. evidence intake;
2. brand diagnosis;
3. creative brief;
4. reference intelligence;
5. concept territories, rough externalisation, and reference validation;
6. concept selection;
7. experience architecture;
8. visual, motion, and asset systems;
9. risk prototype and vertical slice; and
10. full production and verification.

Its five project contracts are evidence dossier, creative brief, concept directions, experience blueprint, and production plan. They are explicitly described as **logical contracts, not a file-count ritual**. Existing approved project material may satisfy them.

This matters because it answers the fear that spatial work is now merely “open UI/UX and start designing.” It is not. A complete interior or showroom project still has a coherent path from business evidence to tested production.

## Former workflow comparison

| Former workflow | Valuable method it contained | Current home | Preservation result | Provisional decision |
| --- | --- | --- | --- | --- |
| `workflow-reference-intelligence` | questions before sources; source provenance; observed vs inferred evidence; corpus synthesis; Keep/Adapt/Reject/Defer; brand translation; approval before implementation | `reference-intelligence/SKILL.md` plus its forensics, synthesis, and translation references; Phase 4 of the spatial coordinator | **Strongly preserved** | Its wrapper is likely unnecessary. Prove route fixtures, then it can remain retired. |
| `workflow-visual-brainstorm` | three structurally different whole-page territories; a restrained option; named reference questions; visible rough tests; divergence gate; no early winner | `spatial-experience-design/SKILL.md`; `master-design-director` Territory Divergence Gate; Phase 5 of the spatial coordinator | **Strongly preserved in the full project route; mostly preserved for direct work** | Do not restore its old stateful wrapper. Improve the direct route only if the parity test shows agents miss the rough-test or divergence requirement. |
| `workflow-spatial-concept` | full-page comparison; source removability; pattern-concentration test; stillness vs motion; user selection; hybrid trade-offs; reversal conditions | `spatial-experience-design/SKILL.md`; `master-design-director` Concept Selection and Reference Integrity gates; Phase 6 of the coordinator | **Strongly preserved in the full project route; mostly preserved for direct work** | Keep it as a project phase, not a standalone workflow. The direct selection route needs to clearly name when user approval and decision recording are required. |
| `workflow-storytelling` | controlling argument; at least two narrative forms; chapter jobs; proof and inquiry timing; copy/visual/motion responsibilities; Director gate | `storytelling/SKILL.md`, its library, `master-design-director`, and Phase 7 of the coordinator | **Strongly preserved** | The original wrapper is likely unnecessary. The skill is the correct direct entry point; the coordinator owns the project-level approval. |
| `workflow-spatial-design-ui` | map UI responsibilities; visual/asset systems; identify the riskiest assumption; representative vertical slice; `expand/revise/simplify/return` verdict | Phase 8–9 of the coordinator; `spatial-experience-design`; `ui-ux`; `master-design-director` Risk Prototype and Vertical-Slice Gate | **Strongly preserved in the full project route; partial direct discoverability** | Do not restore a separate workflow yet. Audit whether direct spatial UI requests load the vertical-slice method before broad production. |
| `workflow-impeccable-craft` | build coherent visitor-responsibility slices; asset boundaries; still composition before motion; concept-continuity audit; per-slice evidence | Phase 10 of the coordinator; `project-phase-routing.md`; `spatial-experience-design` asset references; `ui-ux`; `build-feature` | **Preserved for coordinated projects; partial direct discoverability** | Keep the method. Its likely home is the spatial production reference layer used with `build-feature`, not a separate workflow. |
| `workflow-impeccable-animate` | motion activation gate; stillness comparison; track ownership; risk prototype; proportionate technique; mobile/reduced-motion/failure checks | `cinematic-motion/SKILL.md`, its resource index, `motion-library`, and Phase 8/10 of the coordinator | **Strongly preserved** | The separate wrapper is likely unnecessary. The cinematic skill contains the important method and should stay conditional. |

## Why this arrangement is better than restoring every old workflow unchanged

The former files had useful content, but they were mostly **phases inside one larger project decision**, not independent processes. If an agent had to invoke all of them separately, it could create pointless state files and follow steps mechanically even when a decision was already made.

The better separation is:

| Need | Correct home |
| --- | --- |
| A full spatial website from uncertain evidence to build-ready production | `spatial-project-inception` coordinates the linked decisions and approvals. |
| Analyse design references | `reference-intelligence` directly. |
| Explore directions or choose a concept | `spatial-experience-design`, `storytelling`, and `master-design-director` directly; escalate if the decision affects the full project. |
| Create the page story | `storytelling` directly. |
| Build an approved section or vertical slice | `ui-ux`, `spatial-experience-design`, and `coding`; use the full coordinator if the selected concept or production contract may change. |
| Find a useful animation pattern | `motion-library` directly. |
| Plan or build non-trivial spatial/cinematic motion | `cinematic-motion` directly. |

The `motion-library` exists for the exact reason Beloved described: it gives an agent a named, deliberate way to check the library rather than relying on the agent to remember that a library exists. It should remain a discoverable direct capability.

## What is genuinely worth preserving in the spatial system

These are not decorative rituals. Each stops a particular common AI failure.

| Method | The failure it prevents |
| --- | --- |
| Evidence and brand diagnosis before a visual prescription | a beautiful site that does not actually position the client or earn its claims |
| Three full-page territories and visible rough tests | three different hero treatments that all become the same generic site |
| Reference provenance, removability, and pattern-concentration tests | copying award-site effects or producing a collage of borrowed tricks |
| A controlling argument and chapter jobs | rooms/photos that look expensive but say nothing or fail to build trust |
| Proof and inquiry choreography | a site that produces mood but does not establish capability or generate the right enquiry |
| Risk prototype and a representative vertical slice | discovering too late that the signature idea fails on mobile, with real assets, or in performance |
| Stillness before motion, plus fallbacks | using animation to cover weak composition or make the site unusable |
| Coherent visitor-responsibility build slices | technically complete sections that no longer form one persuasive experience |

## What must remain conditional

The spatial system becomes harmful if it turns these optional methods into automatic rules:

- a large external reference corpus;
- a cinematic hero or video;
- scroll pinning, WebGL, canvas, or a new motion dependency;
- an anchor object, a room metaphor, or a fixed page sequence;
- a new generated-media prompt pack;
- a full set of context files when the client already has approved evidence;
- an exhaustive Director gate for a small reversible edit.

The current spatial coordinator and skills generally express this conditionality correctly. That is a strength to preserve.

## The direct-route gap to test next

`reference/project-phase-routing.md` contains useful summary routes, but it is only 59 lines. A summary cannot automatically replace every detailed instruction from the old phase workflows.

The next test is not “does the text mention the old phase?” It is whether an agent receiving a direct request will load enough of the actual method.

| Direct request | Minimum capability set it must find | Failure that would prove a gap |
| --- | --- | --- |
| “Give me three directions for this interior studio.” | `spatial-experience-design`; brief context; reference intelligence only if references are involved; visible rough-test requirement | returns three palettes/heroes with no whole-page logic, asset burden, failure condition, or still option |
| “Help me choose between these concepts.” | `spatial-experience-design`, `storytelling`, `master-design-director`; user approval boundary | picks the prettiest mock-up with no proof, mobile, asset, reference, or reversal analysis |
| “Develop the story for this site.” | `storytelling`; selected concept or explicit uncertainty; proof and inquiry jobs | produces a fixed template of sections or generic luxury copy |
| “Build the approved gallery section.” | `ui-ux`, `spatial-experience-design`, `coding`; relevant asset and responsive constraints | broad production begins before a representative slice or loses concept continuity |
| “Add motion to this gallery.” | `cinematic-motion`; `motion-library` only for a named job; performance and fallback scope | adds an effect because it looks impressive, or hides content/fails reduced motion |

If the direct route fails any of these, the repair should be the smallest discoverability improvement: a conditional link, a reference index entry, or an explicit handoff rule. It should not automatically recreate seven stateful workflows.

## Precise conclusion

The spatial workflow consolidation should **not** be reversed wholesale. The core project method is present and, for a complete spatial website, better organised around one coordinator plus specialists.

But we should also **not** declare the work finished. The next source changes, if the direct-route tests expose a gap, must preserve detailed method in the most discoverable conditional location. Nothing should be deleted simply because the words “workflow” and “skill” overlap.

## What this audit did not do

- It did not alter the current spatial workflow or any skill.
- It did not restore deleted files merely to improve a count.
- It did not claim the old workflow count or the new workflow count is a measure of quality.
- It did not assess each motion-library example for current technology accuracy; that is a separate, focused reference audit.
- It did not use external research. This was a structural/content-preservation assessment based on the current repository and its recoverable historical source.
