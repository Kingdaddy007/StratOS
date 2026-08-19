# Website System Understanding Map

**Status:** audit only — no skill, reference, or workflow decision is final from this document
**Created:** 2026-08-19
**Purpose:** make the existing website-design system understandable before any further consolidation, deletion, restoration, or rewrite.

## The simple answer

Anti-Gravity should not make every website through a long fixed ritual. It should help the model make **better decisions at the moments where generic AI work usually fails**:

1. understand the real business and visitor problem;
2. form a distinctive, evidence-based design direction;
3. turn that direction into a usable website rather than a beautiful screenshot;
4. build only the interaction and motion that earn their place; and
5. check the finished result in a real browser.

The system should be quiet when a task is small and direct when a task is large. A useful instruction gives the model a better question, a necessary constraint, or a repeatable check. An instruction is harmful when it forces ceremony, a visual style, or a technology that the task does not need.

This is the rule that will govern the audit:

> Preserve or improve a method only when it helps the model make a better decision or verify a real outcome. Do not preserve a file merely because it exists, and do not delete a method merely because its wrapper is inconvenient.

## What the three kinds of files are for

| Thing | Plain-English job | When it should be used |
| --- | --- | --- |
| **Skill** | The specialist's method for solving one type of problem. | “Help me create a website story”, “analyse these references”, “design the interface”, “choose a motion treatment”. |
| **Reference** | The optional deeper library behind a skill: examples, tests, recipes, patterns, and detailed checklists. | Only when the current decision needs that detail. It keeps the main skill intelligent without making it huge. |
| **Workflow** | Coordination for a substantial task that needs state, handoffs, an approval point, or evidence across time. | “Take this full client website from discovery through a build-ready plan.” It should not be required for a one-section change. |

The fact that something is *not* a workflow does **not** mean it is unimportant. For example, `motion-library` is valuable as a direct skill because it lets you say “check the motion library for a useful pattern.” It should be discoverable on purpose, not silently loaded for every website.

## The website journey we are actually trying to support

```text
Client / product reality
        |
        v
Understand the business, visitor and proof needed
  brand-strategy, product-thinking, research-analysis
        |
        +---- supplied references? ----> reference-intelligence
        |
        v
Create and test a distinctive direction
  spatial-experience-design (only for spatial / editorial work)
  storytelling, master-design-director
        |
        v
Make it usable as an interface
  ui-ux (including conditional colour references), copywriting, expert-positioning
        |
        +---- approved motion has a real communication job? ----> cinematic-motion
        |                                                       motion-library (lookup only)
        |
        v
Build the real site
  coding, build-feature
        |
        v
Check what a visitor can actually use
  browser-test, testing, verify-project
```

This is a **decision map**, not a compulsory sequence. A client may already have an approved brand strategy; then we start further down. A small copy correction may use only `copy-editing`. A conventional business website may never use the spatial, cinematic, or motion capabilities. A complex interior-studio website needs more of the map, but still does not need every box by default.

## Two routes, not one rigid website process

### 1. Focused direct work

Use a named skill or a small set of skills when the request is bounded.

Examples:

- “Analyse these three reference websites.” → `reference-intelligence`
- “Give me three directions for this interior-studio site.” → `spatial-experience-design` and `storytelling`
- “Develop the story for the homepage.” → `storytelling`
- “Design this booking form so it works on mobile.” → `ui-ux`
- “Check the motion library for a transition that serves this gallery.” → `motion-library`, then `cinematic-motion` if a candidate is chosen
- “Build this approved section.” → `coding`, `ui-ux`, and the relevant design skill

No durable project state is needed merely because one of these tasks is substantial. The model still applies the relevant skill and records what it actually verified.

### 2. Coordinated spatial project

Use `workflow-spatial-project-inception` when you are starting or rescuing a full spatial client project and need the connected decisions to remain coherent: evidence, concept, story, production plan, approvals, and a build handoff.

The workflow is the **project coordinator**. It is not the sole holder of design intelligence, and it does not replace the individual skills. It calls on them when a phase genuinely needs them. It is therefore acceptable for this one route to contain state and approval gates while the individual design jobs remain direct.

## What the current website capabilities contribute

The table below records the current intended role, not a promise that every item is already perfect.

| Capability | Helps the model avoid | Use it when | Do not force it when | Audit status |
| --- | --- | --- | --- | --- |
| `brand-strategy` | generic “premium” language and design with no business point of view | an interior/spatial brand's audience, authority, price signal, or proof is unclear | a client already has a well-supported, current brand brief | keep; needs a later portability review beyond spatial brands |
| `reference-intelligence` | copying fashionable references without understanding why they work | references, recordings, screenshots, or precedent collections are supplied | no reference is informing a decision | keep; former dedicated workflow appears largely represented in the skill, but parity must still be proved |
| `spatial-experience-design` | a generic “hero / services / portfolio / testimonial” page and empty visual spectacle | interior, showroom, architecture, decor, furniture, gallery, or other spatial work | ordinary SaaS, dashboard, or conventional business site | keep; this is an optional spatial capability, not the default design method |
| `storytelling` | section order copied from a template rather than a persuasive visitor journey | a brand site needs an argument, chapter sequence, proof timing, or inquiry posture | final copy is the only requested task | keep; strong value, but its relationship to the former storytelling workflow needs a parity review |
| `master-design-director` | accepting the first attractive concept without a serious creative challenge | high-stakes creative direction, a contested concept, or an important review | a small reversible UI adjustment | keep as a proportionate review layer, never a mandatory gate for every task |
| `ui-ux` | pretty-but-unusable screens, missing states, desktop-only work, inaccessible controls | any interface, form, navigation, responsive behaviour, or interaction design | backend-only work | keep; it holds important general UI craft, but it is not yet proven to preserve every former UI Craft and UI Animate method |
| UI/UX colour references | decoration without contrast, hierarchy, or semantic meaning | a material colour, token, contrast, state, or palette decision | colours are already settled and not part of the task | keep; conditional UI/UX method, with evidence reference only for specialist claims |
| `copywriting` and `expert-positioning` | vague claims, weak proof, and generic calls to action | site messaging, case study, offer, CTA, or positioning needs work | early concept work has not established the argument yet | keep; use after or alongside story, not instead of it |
| `cinematic-motion` | motion added only because it looks impressive | motion, scroll, media, or cinematic continuity has a named communication job | stillness, a simple CSS state change, or a conventional interaction is sufficient | keep; it contains a substantial library and must remain conditional |
| `motion-library` | inventing an effect from scratch or repeatedly forgetting useful existing patterns | you explicitly want to look up a motion pattern by communication job | no motion decision exists | keep as a direct discovery skill; do not automatically load the entire library |
| `scroll-storyboard` | unplanned scroll choreography and effects that destroy reading order | an approved experience needs authored scroll timing, pinning, persistence, or synchronized media | normal document-like scrolling is right for the page | keep, conditional |
| `coding` and `build-feature` | producing a design plan without a maintainable, working website | authorised implementation is required | the task is research, concept selection, or critique only | keep; build work must not silently replace a creative decision |
| `browser-test`, `testing`, and `verify-project` | declaring a website “good” from source code or a static screenshot | an implementation exists and the claim needs evidence | there is nothing runnable yet | keep; checks must match the actual claim, not become a meaningless checklist |

## What the prior workflow consolidation got right

It correctly identified a structural problem: many files were named as workflows even though they did not own state, authority, or cross-time coordination. Making every named operation a workflow would create a bloated command menu and encourage mechanical sequence-following.

It also correctly moved some common UI operation routes—such as “critique”, “polish”, “bolder”, “quieter”, and “clarify”—toward direct UI task modes. Those are ways of working, not independent project processes.

The intent behind one stateful `spatial-project-inception` workflow plus direct specialist skills is sound.

## What is not yet proven, and therefore cannot be treated as finished

The earlier consolidation made an invalid leap in several places: it treated a routing note or a related skill as proof that all of the old method had been preserved. That proof has not been made.

The following table is the important correction.

| Former workflow | What it contributed | Current preservation finding | Safe provisional decision |
| --- | --- | --- | --- |
| `workflow-ui-craft` | nearest project contract, journey and hierarchy, full relevant state matrix, use of existing primitives, browser checks, and delivery evidence | **Partial.** `ui-ux` clearly preserves user goal, hierarchy, state coverage, responsive/accessibility requirements, and browser verification. It does not yet visibly preserve every implementation-facing instruction as a dedicated optional reference. | Do not call its deletion final. Perform a line-by-line value/parity review. The likely end state is a direct UI implementation reference, not a workflow. |
| `workflow-ui-animate` | motion purpose, trigger/property/duration/easing/interruption, reduced motion, simple techniques first, and interaction testing | **Partial.** `ui-ux` covers purposeful motion at a high level; `cinematic-motion` covers rich motion. The generic UI-motion method sits between them and should not disappear into a spatial-only capability. | Do not call its deletion final. Decide whether its generic method belongs in `ui-ux/reference/motion-design.md` or a small dedicated direct reference after parity review. |
| `workflow-design-api` | consumer-first contract design, errors, compatibility, security, and verification | **Not part of this website audit.** Its removal cannot be justified by a website workflow decision. | Freeze its deletion decision and audit it separately against the `api-design` skill. |
| `workflow-reference-intelligence` | questions before sources, provenance, observed vs inferred evidence, synthesis, translation, and handoff | **Likely strong preservation.** The current `reference-intelligence` skill carries the same purpose and has forensics, synthesis, and translation resources. | Prove parity before final removal; no restoration merely because of its old wrapper. |
| `workflow-visual-brainstorm` | three genuinely different whole-page territories, named reference questions, visible rough tests, and a no-winner-yet gate | **Partial.** Current spatial skills and phase-routing reference mention these ideas, but a short routing table is not the full method. | Preserve the method pending a parity review. It may become a focused `spatial-experience-design` reference rather than a workflow. |
| `workflow-spatial-concept` | comparison criteria, removability and pattern-concentration tests, stillness comparison, risk/pre-mortem, user selection, and reversal condition | **Partial.** A number of the tests are named in current skills and routing, but no full preservation proof exists. | Preserve pending parity review. Likely a decision reference plus explicit user approval point; it does not automatically need its own stateful workflow. |
| `workflow-storytelling` | controlling argument, alternative narrative forms, chapter jobs, proof choreography, and experience gate | **Likely strong preservation.** The current `storytelling` skill covers these jobs and has a deep library. | Verify parity, then decide whether any missing decision-record format should be a reference rather than restoring the wrapper. |
| `workflow-spatial-design-ui` | UI responsibilities, visual/asset systems, risk prototype, representative vertical slice, and Director verdict | **Partial.** `ui-ux`, `spatial-experience-design`, and `master-design-director` cover parts of it. The full vertical-slice method is not yet proven to be preserved in one coherent optional resource. | Preserve pending parity review; decide whether its method belongs in the spatial production reference set. |
| `workflow-impeccable-craft` | coherent visitor-responsibility slices, real-enough assets, concept-continuity audit, and per-slice verification | **Partial.** Current production routing names the intent but does not itself prove the full detail is available at build time. | Preserve pending parity review. The most likely destination is a spatial production reference used alongside `build-feature`. |
| `workflow-impeccable-animate` | motion activation gate, stillness comparison, track ownership, risk prototype, simple technique choice, and fallback checks | **Likely partial-to-strong.** `cinematic-motion` has extensive motion resources, but an exact comparison is still required. | Preserve pending parity review. It may become an explicit activation/reference layer in `cinematic-motion`, not a separate workflow. |

### Important consequence

No additional workflow or skill should be deleted until its row has a documented answer to both questions:

1. **Where exactly does each useful instruction live now?**
2. **Can the model discover and load it at the point where it is useful?**

“It is broadly related to another skill” is not an acceptable answer.

## How we will judge every existing skill, reference, and workflow

This is the proposed audit test. It applies to old and new material alike.

### Keep or upgrade a capability when it does at least one of these

- supplies project-specific evidence that a general model does not have;
- prevents a known high-cost failure, such as generic visual imitation, inaccessible interaction, weak proof, or a broken mobile journey;
- improves a decision through a concrete comparison, question, or verification method;
- provides a reusable lookup library that the model can deliberately choose from;
- captures durable judgement that is hard to reliably recreate from a one-line prompt.

### Move it from a workflow into a skill or reference when

- it is a method or check that can be invoked directly;
- it does not own cross-time state, an approval, a handoff, or a mutation boundary;
- its detailed instructions should load only in particular cases;
- it is principally a search/lookup capability, like the motion library.

### Remove it only when all of these are true

- its useful content has been preserved with traceable destination links;
- the destination is discoverable at the actual point of use;
- it does not add a different decision, constraint, or verification method;
- a realistic task test shows no loss of outcome quality; and
- it does not contain user-specific knowledge that needs a deliberate new home.

### Research before changing a capability when

- the proposed update depends on current platform/model/tool behaviour;
- the practice has materially changed since the old skill was authored;
- we cannot tell whether the instruction improves results or merely sounds clever;
- it makes a broad claim about design, product, accessibility, growth, security, or engineering that needs current evidence.

Research is **not** needed merely to decide that a repeated checklist belongs in a reference rather than a workflow. We already have the file and can inspect its value. Research is needed before we claim a new practice is better.

## The next controlled phase

This document is phase A: **understand before changing**. The next phases are deliberately narrow.

1. **Website method parity audit.** Compare each provisional deletion above against its proposed destination line by line. Record `preserved`, `partially preserved`, `missing`, or `should not preserve`, with the reason. No silent rewriting.
2. **Website outcome pilot.** Use one realistic client website brief and compare a raw approach with the mapped Anti-Gravity route. Judge business fit, originality, proof, usability, mobile/accessibility, buildability, and unnecessary complexity. A longer answer is not a better result.
3. **Focused research gates.** Only for gaps that the parity audit or pilot exposes, prepare one narrow research brief at a time—e.g. current brand/positioning practice, interaction motion, design-system implementation, or visual-quality evaluation. Do not research all website design indiscriminately.
4. **One capability cluster at a time.** Rehome, revise, restore, merge, or retire only the content for one proven cluster, then validate routing and the pilot scenario again.
5. **Only then continue the wider OS roadmap.** The final number of skills or workflows is an outcome of evidence, not a target to optimise.

## What has deliberately not happened in this audit

- No existing skill, reference, or workflow was deleted, restored, compressed, or rewritten by this document.
- No claim is made that the current 17-workflow figure is final or correct.
- No claim is made that the current 71/72-skill counts are an indicator of quality.
- No external research was used to turn current fashion into permanent rules.
- No commit, push, install, or external action occurred.

## The immediate next action

Start with the **UI Craft and UI Animate parity audit**. They are the clearest case where a useful general website method may have been diluted during workflow consolidation. That audit should answer, in plain English, whether their best instructions belong in the current `ui-ux` skill, its optional references, `cinematic-motion`, or nowhere.

Only after that answer exists should we decide whether to keep the old files deleted, revive them in a better form, or restore them temporarily while a better home is built.
