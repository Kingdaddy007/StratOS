---
name: workflow-spatial-project-inception
description: Discover, select, prototype, and produce a brand-specific interior or spatial website experience
id: spatial-project-inception
version: 4
status: active
intent: Coordinate a material spatial website decision through conditional evidence, concept, and delivery lenses without imposing a fixed public sequence.
use_when: [starting or substantially redesigning an interior, spatial, decor, showroom, gallery, furniture, staging, luxury-home, or architecture-adjacent brand website]
do_not_use_when: [general product or SaaS UI, a small implementation task with approved context, backend-only work, or Project 003 before separate authorization]
inputs: [user objective, available brand evidence, workspace context, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, brand-strategy, reference-intelligence, storytelling, spatial-experience-design, master-design-director]
mutation_class: local_edit
approval_gates: [material creative direction, source or reference scope, project-context write, dependency or source import, implementation authority, final release or external effect]
states: [received, orient, evidence, diagnose, brief, reference, diverge, select, architect, prototype, produce, verify, deliver, stopped]
outputs: [decision-ready direction, only the logical contracts needed to support it, proportional reference-intelligence outputs, conditional artifacts when justified, implementation when separately authorized, verification evidence, residual risks]
verification: [trace evidence to decisions and downstream consumers, run spatial consistency checks, record raw evidence, label anything unverified]
failure_paths: [return to the earliest invalidated gate, stop on authority or contract conflict, preserve state, report blocker and safe next action]
resume_contract: task-scoped .agents/workflows/spatial-project-inception.json using the workflows directory contract
next_workflows: [build-feature, verify-project, none]
profiles: [spatial]
---

# WORKFLOW: SPATIAL PROJECT INCEPTION

## PURPOSE

Turn evidence about one interior or spatial brand into a distinct, testable
website direction and then, when authorised, controlled production. The Studio
Director brings in the Design Director when the request qualifies; Beloved does
not need to invoke this workflow or complete it as a public checklist.

This workflow is a set of **conditional decision lenses and resume support**.
It does not assume a cinematic hero, fixed story sequence, video, motion,
anchor object, effect-library choice, reference-derived architecture, or a
ten-step relay. Start at the lens that protects the next decision, skip a lens
whose risk is absent or already controlled, and return to any earlier lens when
new evidence invalidates the direction.

Reference questions follow a useful creative brief when references can change a
decision; their depth is proportional to that decision. The point is to make a
good design conversation and a buildable vertical slice, not to generate a
complete set of documents.

## ARTIFACT CONTRACT

Use one or more of these five logical contracts in `.agents/contexts/` or an
approved equivalent location **only when they make an active decision,
handoff, or resume state clearer**:

1. `evidence-dossier.md`
2. `creative-brief.md`
3. `concept-directions.md`
4. `experience-blueprint.md`
5. `production-plan.md`

They are contracts, not a file-count ritual. Existing approved documents may
satisfy them. Legacy spatial projects may retain fourteen-file context sets;
map their content, identify genuine gaps, and consolidate only with user
approval. Do not create every file before making a useful creative decision.

Conditional outputs:

- a reference question brief and translation ledger, embedded in an approved contract or stored separately;
- `reference-analysis-plan.md` and `reference-synthesis.md` for large, mixed-format, or implementation-oriented corpora;
- `scroll-storyboard.md` for authored scroll timing, pinning, continuity, or media choreography;
- `cinematic-prompt-pack.md` for approved generated imagery/video;
- `portfolio-proof-chapters.md` for detailed project decision narratives;
- `DESIGN.md` / `DESIGN.json` for implementation tokens and component rules.

## CONDITIONAL DECISION LENSES

The following lenses remain available because each prevents a real failure
mode. They are not mandatory phases or a public script. The Design Director
selects, combines, repeats, or omits them according to the client, evidence,
and next decision. A "Gate" below means a condition to meet *when that lens is
material*, not an automatic request for another Beloved approval.

## ROUTE VISIBILITY CONTRACT

Keep route selection private, but make material handoffs observable. At every
approval gate, resume point, or change of owning lens, report only the fields
that changed:

```text
Route and current lens:
Decision being protected:
Capabilities: selected | loaded | used
Evidence or artifact produced:
Unknown, conflict, or approval required:
Next route and activation reason:
Return condition:
```

Do not report an available capability as selected or used. Compress this to one
or two lines for a small conversational move. The user should never need to
remember a skill name, infer the current phase, or reconstruct what must happen
next.

The `design-director` is the functional lead that integrates design decisions.
`master-design-director` is a conditional critique and gate skill used by that
lead or the Studio Director; it is not a second owner or a competing agent.

### 1. Evidence Intake

Use `brand-strategy`. Catalog website, social, projects, assets, communications, proof, constraints, dates, and unknowns. Separate facts, reported claims, inferences, and unknowns. Write `evidence-dossier.md`.

**Decision check:** Surface coverage and unresolved gaps when they could change
the direction. Missing evidence may remain, but it must be visible.

### 2. Brand Diagnosis

Inside the dossier, diagnose perception gap, desired authority, audience, taste patterns, founder authority, proof burden, premium leaks, category conventions, wrong-fit audience, and inquiry posture. Do not prescribe visuals.

**Cognitive Engine checkpoint — Type 1.5 creative decision:** Load `core/system-thinking.md`, `core/expert-cognitive-patterns.md`, and `core/first-principles.md`. Decompose current perception, desired authority, evidence gap, real constraints, and unknowns. Reframe the diagnosis from the visitor's likely misunderstanding as well as the studio's self-description. Challenge any conclusion that relies on an attractive inference rather than observed proof, and record second-order implications for asset reality, proof burden, and inquiry posture.

**Decision check:** Bring the diagnosis to Beloved when it materially changes
the creative direction, client posture, or requested scope.

### 3. Creative Brief

Write `creative-brief.md`: what visitors should feel, understand, believe, and do; what must be known first; controlling problem; proof requirements; constraints; anti-goals; and territory-selection criteria.

**Decision check:** Use the Creative Brief Gate when a brief is the smallest
way to resolve a material creative conflict; otherwise capture its conclusion
in the active decision packet.

### 4. Reference Intelligence

Run the direct `reference-intelligence` skill after a brief establishes
selection criteria **when references can change a live choice**. Choose
proportional depth:

- **Lightweight:** record the questions and why no external corpus is required.
- **Focused:** analyze one or two references that answer bounded questions.
- **Corpus:** analyze three or more references, mixed formats, or an explicit comparison using per-source forensics, cross-corpus synthesis, and a translation ledger.

Use the pre-territory pass to expand vocabulary, identify candidate principles, expose costs, and preserve negative patterns. Do not select the concept or copy section architecture.

**Decision check:** Run the Reference Integrity Gate when external references
influence direction. Then make source scope, provenance,
observation/inference boundary, Keep/Adapt/Reject/Defer decisions, and
unresolved gaps explicit.

### 5. Concept Territories, Rough Externalization, and Reference Validation

Use the direct `spatial-experience-design` skill, with `reference-intelligence` when applicable, to generate three structurally different directions for the whole page, not hero, palette, or animation variations. Include one restrained or still-led option unless the evidence rules it out.

For every territory, produce a visible rough styleframe, sequence sketch, or prototype with realistic-enough assets. Run the second reference pass only for precise questions about continuity, hierarchy, proof, interaction, motion, responsive translation, assets, or feasibility. Record provenance, translation, rejection decisions, and pattern concentration in `concept-directions.md`.

**Decision check:** Before selecting a territory, verify genuine divergence,
brand-specific translation, and no reference collage. Use a visible rough test
when the choice cannot be judged from the available evidence alone.

### 6. Concept Selection

Use `spatial-experience-design`, `storytelling`, and `master-design-director` to compare territories on brand truth, first impression, proof, full-page potential, asset feasibility, motion necessity, accessibility, performance, responsiveness, and maintenance. Record the decision.

**Decision check:** Beloved selects a territory or an explicitly reasoned
hybrid before work is committed to a direction that would be costly to undo.

### 7. Experience Architecture

Use `storytelling` and `spatial-experience-design`. Decide controlling argument, narrative form, chapter jobs, hierarchy, proof timing, copy-visual relationship, inquiry, navigation, and responsive intent. Write `experience-blueprint.md`.

Load the Design Director's `ui-ux` baseline when navigation, inquiry forms,
interaction states, accessibility, responsive behaviour, or recovery paths
become concrete. Do not postpone these decisions until implementation merely
because the visual territory is spatial.

**Decision check:** Use the Experience Gate only for a material narrative,
hierarchy, proof, inquiry, or interaction decision.

### 8. Visual, Motion, and Asset Systems

Complete the blueprint and `production-plan.md`: type, color, composition, crop, material, density, stillness, motion grammar when justified, asset boundary, generated-media needs, performance, accessibility, fallbacks, and build slices.

Select conditional capabilities by the decision they own:

| Decision present | Select | Boundary |
| --- | --- | --- |
| Several scenes, room films, text-safe media states, portfolio proof, and prompts must operate as one media-heavy experience | `cinematic-showroom-strategy` | Own the whole-site media and scene choreography, not motion code or provider execution. |
| A named spatial job is served better by movement than stillness | `cinematic-motion` | Own motion grammar, tracks, implementation constraints, performance, and fallbacks. |
| Meaning changes at authored scroll depths, or pinning, scrubbing, persistent continuity, or synchronized media is required | `scroll-storyboard` | Translate the approved story and experience into beat-level scroll behavior. |
| An approved motion job needs an existing effect candidate | `motion-library` | Compare only relevant internal candidates; do not let the library choose the concept. |
| One contained realtime DOM/WebGL effect may outperform still, DOM/CSS, or pre-rendered media | `canvas-ui` | Compare alternatives first; own the component import, lifecycle, fallback, and isolated-slice gate. |
| A reference must validate continuity, hierarchy, motion, responsive translation, assets, or feasibility | `reference-intelligence` | Run the focused post-territory pass and preserve provenance and translation decisions. |
| An approved scene requires generated video | Media profile plus `video-generation`; add `prompt-engineering` only for a provider-ready prompt | Keep provider access, uploads, credits, generation, and external effects behind just-in-time approval. |

These routes may recur when a prototype changes the design question. Selecting
one never implies selecting the others, and a still-led production plan may
reject all of them.

**Decision check:** Obtain implementation authority before a production contract
causes local edits, source imports, dependency changes, or external effects.

### 9. Risk Prototype and Vertical Slice

Prototype the most dangerous assumption first. Then create one representative sequence using real-enough imagery, typography, mobile behavior, and signature motion only when applicable. Store evidence and findings in `production-plan.md`.

**Decision check:** A vertical-slice verdict is `expand`, `revise`,
`simplify`, or `return to concept`. A small, low-risk website may not need a
formal prototype if direct implementation is itself the cheapest credible test.

### 10. Full Production and Verification

After implementation authority, use `build-feature` with `ui-ux`, `spatial-experience-design`, and `coding`; add `cinematic-motion` only when motion is approved. Build coherent slices and critique each slice. Verify accessibility, performance, responsive composition, reduced-motion/fallback behavior, proof, inquiry, and concept continuity. See `spatial-experience-design/reference/project-phase-routing.md` for the preserved phase gates and direct-work boundaries.

**Decision check:** Verify the implemented scope and obtain any required
release or external-effect approval.

## STABLE NICHE JOBS, VARIABLE DESIGN

Interior brands commonly need atmosphere/point of view, curated work/taste, transformation or design intelligence, authority/proof, process/fit, and selective inquiry. These are reusable communication jobs, not required sections or a fixed order.

Every project independently decides what is known first, emotional register, controlling argument, narrative form, opening form, typography, color, crop, material, density, motion amount, proof strategy, and inquiry posture.

## QUALITY GATE

- [ ] Evidence and inference are visibly separated.
- [ ] Diagnosis precedes visual prescription.
- [ ] Reference questions are defined after the creative brief when references can change the direction.
- [ ] Reference depth is proportional, provenance is explicit, and translated principles remain subordinate to brand truth.
- [ ] Three whole-page territories diverge structurally and have visible rough tests.
- [ ] Pre-territory references expand vocabulary; post-territory references validate named design questions.
- [ ] Keep, Adapt, Reject, and Defer decisions prevent copied architecture and reference collage.
- [ ] Selection rationale traces to brief criteria.
- [ ] The decision, handoff, or resume state is supported by the necessary contracts or approved equivalents.
- [ ] Optional complexity is explicitly accepted or rejected.
- [ ] A risk prototype and vertical slice precede broad production.
- [ ] Material handoffs expose the current lens, used capabilities, evidence,
      next route, and return condition without turning the lenses into a public ritual.
- [ ] The general project/UI workflow remains untouched.
