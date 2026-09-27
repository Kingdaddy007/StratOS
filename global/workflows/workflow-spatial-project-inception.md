---
name: workflow-spatial-project-inception
description: Coordinate V5.2 spatial website discovery, concept testing, and production through conditional decision loops
id: spatial-project-inception
version: 6
status: active
intent: Help a designer understand a spatial brand, test a fitting website idea, and carry an earned direction into a coherent experience.
use_when: [starting or substantially redesigning an interior, spatial, decor, showroom, gallery, furniture, staging, luxury-home, or architecture-adjacent brand website; building an authorized private prospect-specific spatial website concept]
do_not_use_when: [general product or SaaS UI, bounded reference study or screen critique, a small implementation task with approved context, backend-only work]
inputs: [user objective, available brand evidence, accepted decisions, workspace context, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, reference/v5-creative-constitution-v1.0.0.md, brand-strategy, storytelling, spatial-experience-design, master-design-director]
mutation_class: local_edit
approval_gates: [material creative commitment, source or reference scope, project-context write, dependency or source import, implementation authority, final release or external effect]
states: [received, orient, evidence, diagnose, brief, reference, diverge, select, architect, prototype, produce, verify, deliver, stopped]
outputs: [decision-ready direction, proportional working records, risk prototype when needed, authorized implementation, verification evidence, residual risks]
verification: [trace evidence to decisions, inspect the risky assumption, check implemented scope in its real environment, label anything unverified]
failure_paths: [return to the earliest invalidated decision, stop on authority or contract conflict, preserve state, report blocker and safe next action]
resume_contract: task-scoped .agents/workflows/spatial-project-inception.json using the workflows directory contract
next_workflows: [build-feature, verify-project, none]
profiles: [spatial]
---

# Spatial Project Inception — V5.2

## What this workflow does

Help the designer understand a spatial brand, discover a fitting website idea, test its most uncertain parts, and carry the selected idea into a coherent site.

The AI brings professional knowledge, useful proposals, critique, and production ability. The designer can interrupt, redirect, reject, or choose a direction in ordinary conversation. Internal routing should rarely be visible. Consequential choices and their reasons should be.

Use this workflow for a new spatial website or a substantial change in its creative direction. A request to discuss a reference, critique one screen, repair an animation, or change a known section can be handled directly. Do not restart inception merely because the subject is an interior designer.

The [**V5 Creative Constitution v1.0.0**](../reference/v5-creative-constitution-v1.0.0.md) governs creative judgement. This workflow describes how to move work forward. It does not impose a house aesthetic, cinematic hero, opening animation, fixed number of concepts, fixed set of files, or required skill chain.

## Start with the decision at hand

At entry, establish four things in the smallest useful form:

1. **The job** — Is the user learning, exploring, choosing, prototyping, building, or reviewing? What decision would make this conversation useful?
2. **The authority** — What local work has the user authorized? What source, asset, generation, dependency, publication, or external action remains outside that scope?
3. **The project truth** — What is observed, what the client reports, what is inferred, what is proposed, and what is still unknown? Which existing decisions should be respected?
4. **The cost of being wrong** — Which assumption would waste the most design or production effort if it fails?

Do useful work with the available evidence. Ask for missing information only when it would change the next consequential choice. The user should not have to complete a questionnaire before the AI can sketch an idea, explain a reference, or identify an obvious risk.

## Decision states

Creative work may be:

- **Study** — learn, inspect, recreate, or understand a reference, technique, or mechanism without requiring immediate project fit.
- **Explore** — reversible research, sketches, recreations, comparisons, prototypes, and experiments. Not project truth.
- **Provisional** — a low-risk working choice used to keep moving while uncertainty remains. Record what could change it.
- **Committed** — a consequential direction with enough evidence, fit, or prototype support to justify downstream dependency.

Do not ask for approval on every reversible move. Make consequential commitments visible. Full production follows commitment; experiments may precede it.

# Three working loops

The loops are areas of responsibility, not stages that must be completed in order. A reference or visual experiment may open the work. New evidence or a failed prototype may send the project back to an earlier question.

## 1. Understand the brand and its constraints

Investigate the studio's work, clients, audience, aims, capacity, current presentation, available assets, and the claims it can support. Look for what visitors should notice, understand, believe, and be able to do. Distinguish the client's desired perception from what its evidence currently earns.

Build a **Constraint Box** when it will sharpen the work:

- truth and claims the site must respect;
- real project images, film, people, writing, and proof available;
- visitor needs, including orientation, trust, access, and inquiry;
- production limits such as time, asset rights, loading, mobile, accessibility, maintenance, and budget;
- subject integrity: what must remain visually or spatially coherent;
- useful creative freedoms and specific clichés this brand should avoid.

The Constraint Box is provisional. It protects truth and resources without deciding the visual solution.

If commercial posture, price, exclusivity, qualification, or offer structure is unresolved, treat it as a business question. Do not infer a concierge or selective model from luxurious imagery.

**Useful result:** a concise Creative Brief or equivalent conversation record containing the perception task, strongest proof, key constraints, live unknowns, and criteria by which concepts will be judged.

Do not create a document when a few lines in an existing project record are enough.

## 2. Discover and select a concept

Ideas may enter through brand meaning, content relationships, a visual asset, an unusual reference, motion, typography, a stored layout, a technical experiment, or the designer's intuition.

An idea is not disqualified because of where it began. A stored pattern also does not earn adoption merely because it is available.

The AI should explore promising leads and offer alternatives when comparison would improve judgement. Stored archetypes, audits, layouts, and motion libraries expand vocabulary; they never define all possible answers.

### References

For an interesting reference without a client brief, run **source forensics**:

- what is actually visible;
- how the experience unfolds;
- what subject supports it;
- what produces the perceived effect;
- what assets and technology it requires;
- where it may fail.

Keep the result as learning.

When a project is present, translate the underlying principle through that project's subject, assets, visitors, and purpose before recommending adoption. Record source and uncertainty when reference evidence affects a decision.

A private recreation may teach mechanics. A client-facing concept needs its own reason to exist.

### Find generative structure

Look for what can generate form:

- relationship;
- hierarchy;
- contrast;
- sequence;
- repetition;
- scale;
- geometry;
- rhythm;
- material;
- transformation;
- personality;
- environment;
- spatial behaviour.

Also permit visual form to lead and test its meaning later. No section owes the system a literal metaphor.

### Diverge only as much as the decision requires

Create as many directions as the decision warrants.

One strong direction may need a challenge rather than two invented competitors. When the choice is genuinely open, compare materially different possibilities, including stillness where relevant.

A direction is meaningfully different because its subject, visitor journey, proof logic, composition, or spatial behaviour changes—not because the palette changes.

### Make a small concept packet

For each serious candidate, show enough to judge:

| Question | Show enough to judge |
| --- | --- |
| **Why this brand?** | The observed fact, meaningful inference, or explicit creative hypothesis behind it. |
| **What does the visitor experience?** | The first visible state, hero subject, first meaningful transition, and the feeling or understanding gained. An opening animation is optional. |
| **Can it continue?** | One later section and a seed of the site's image, type, transition, interaction, and continuity rules. |
| **What must exist?** | Asset, media, content, accessibility, mobile, and production requirements. |
| **Why might it fail?** | The weakest claim, illusion, crop, source, visitor assumption, or technical cost. |

Externalize promising directions at the cheapest credible fidelity: sketch, styleframe, motion study, rough layout, asset test, AI media test, or small coded prototype.

Do not spend equal effort on every candidate.

### Test the risk that could change the decision

The usual front-door test—opening/initial state -> hero -> first handoff plus one later chapter—is useful because it exposes whether the concept has a transferable grammar.

But it is not mandatory.

If the deciding risk is elsewhere, test that instead: an impossible mobile crop, inconsistent generated imagery, cross-project transition, long scroll, asset-generation continuity, performance burden, accessibility issue, or proof gap.

Prototype the assumption most likely to overturn the concept.

### Critique and commitment

Use critique to ask whether the result:

- respects the subject;
- reveals something specific;
- helps visitors;
- produces a language the rest of the site can carry;
- earns its complexity.

The AI should give its own recommendation and explain the tradeoff.

The designer chooses a costly creative commitment unless that authority has explicitly been delegated. Reversible implementation choices may remain delegated.

Record the selection, strongest rejected alternative when relevant, major assumptions, sacrifices, and the condition that would reopen the decision.

**Useful result:** a selected concept and decision record. Its shape may be a short conversation summary, an existing project brief, or a dedicated file when handoff/resume requires one.

## 3. Shape, produce, and inspect the experience

Translate the selected concept into a site-wide experience.

Define only the rules this project needs.

### Experience Grammar

As relevant, define:

- the first visible state and how visitors reach the resolved hero;
- hero subject and subject integrity;
- what each chapter helps visitors understand;
- proof timing;
- camera or viewpoint language;
- typography behaviour;
- image behaviour;
- recurring transition and continuity language;
- navigation and interaction character;
- motion physics and intensity;
- where the experience intentionally pauses or changes register;
- inquiry behaviour;
- asset states and text-safe areas;
- responsive compositions;
- loading and failure behaviour;
- reduced-motion and bandwidth fallbacks.

Intentional repetition may create identity. Variation should create hierarchy.

Treat a full interior as a coherent volume. Separate or move visual planes only when the source supports the illusion. Preserve architectural perspective, materials, light, project identity, and truthful proof.

If an effect is impressive but competes with the work, alter or remove it.

### Specialist ownership

Let a specialist answer a named question:

| Question | Primary owner |
| --- | --- |
| Claims and brand diagnosis | `brand-strategy` |
| Offer, qualification, commercial posture | `expert-positioning` when needed |
| Narrative argument and chapter logic | `storytelling` |
| Reference forensics and translation | `reference-intelligence` |
| Visual-spatial concept and experience grammar | `spatial-experience-design` |
| Focused critique at a consequential or costly decision | `master-design-director` |
| Approved motion behaviour | `cinematic-motion` |
| Beat-level authored scroll progression | `scroll-storyboard` |
| Media source, state, continuity, prompt inheritance, poster, and fallback requirements | `media-choreography` |
| Known implementation candidates | `motion-library` |
| Navigation, inquiry, responsive interaction, and accessible states | `ui-ux` with the Design Director |
| One contained live effect after still, DOM/CSS, and pre-rendered options are compared | `canvas-ui` |
| Approved provider generation | Media pack plus `video-generation`; add `prompt-engineering` only for a provider-ready prompt |
| Engineering implementation | build/coding workflow |

**One owner per question.**

The **Studio Director integrates the project decision**. When involved, the `design-director` functional lead integrates visual and interaction work. The selected concept and Experience Blueprint (or equivalent record) preserve those integrated decisions. `master-design-director` provides focused critique at consequential moments and does not become a second concept owner.

A specialist's example, archetype, or library entry cannot become an unexamined project decision. Not every specialist is needed on every project.

### Choose the production method

For each demanding moment, choose the lightest production class that can deliver the required experience:

- **Live Motion** — DOM, CSS, SVG, GSAP, Canvas, or WebGL generated at runtime.
- **Pre-Rendered Motion** — Blender, AI video, compositor, or conventional video rendered beforehand.
- **Scrubbed Pre-Rendered Motion** — pre-rendered media whose playhead is controlled by scroll or interaction.
- **Still / Simple** — static imagery or minimal runtime behaviour when additional motion adds no value.

Choose by visual requirement, responsiveness, composability, file weight, interaction needs, production cost, accessibility, and maintenance.

### Produce proportionally

Before broad production, test a representative slice when the risk justifies it.

When implementation is authorized, build coherent slices. Judge mechanics and feeling in the real browser:

- first view;
- scroll progression;
- image quality;
- typography over media;
- navigation;
- focus and keyboard;
- inquiry;
- loading/failure states;
- mobile;
- reduced motion;
- performance;
- real media quality.

A passing build or polished still does not establish that the experience works.

Record what was observed and what remains untested.

**Useful result:** an Experience Blueprint and Production Plan only as detailed as the build or handoff requires, followed by a working site and proportionate verification evidence when production is in scope.

# Working records, kept light

There are four questions worth preserving when another person, agent, or later session must continue the work:

1. **What do we know?** Sources, claims, inferences, constraints, and important unknowns.
2. **What have we chosen?** The concept, why it fits, what it sacrifices, and what could reverse it.
3. **How should it behave?** Site-wide visual and interaction rules, with meaningful fallbacks.
4. **What must be made and proven?** Assets, build slices, risky assumptions, and checks.

These answers may live in existing project documents, one concise project brief, or a few task notes.

Do not create files to satisfy a file count.

Make consequential changes visible in the conversation; keep routine routing and exploratory scraps out of the user's way.

A principle learned from one project may be explained to the designer, but it does not silently become a global rule.

# Private speculative concepts

If the user authorizes a private, local concept for a prospective client, the AI may compress the loops into one execution pass.

Use supplied or authorized public evidence, label inference and unverified claims, and make reversible creative choices within scope.

Build a bounded proof slice or fuller local prototype according to the request and available resources.

Show why the direction belongs to that prospect and what it would take to develop it responsibly.

The concept is independent and uncommissioned unless the client has actually commissioned it. Local prototype authority does not imply permission to send outreach, upload private assets, purchase media, publish, deploy, or make public claims on the client's behalf.

When the private concept is a complete build-first prospect website, select
`spatial-outreach-site-sprint` for the local production loop and
`speculative-outreach` when its evidence, claim, or privacy boundary matters.
The sprint's three whole-page territories and three continuity candidates are
specific to that delegated route; they are not a rule for every V5 project.
Preserve its prospect-specific proof spine, honest limit, source rights, risk
prototype, whole-sequence browser review, mobile and reduced-motion equivalents,
and verification handoff. Record a reversible self-selection only when the user
delegated that choice. Do not present it as client approval.

# Legacy compatibility bridge

For retained V4 callers and references:

- “Exactly three territories” means **enough genuinely different directions to expose the real choice**.
- Stored hero layouts, narrative forms, aesthetic archetypes, and motion archetypes are **vocabularies, not mandatory starting menus**.
- A stored layout may spark an idea, but it cannot win merely because it is available.
- `spatial-experience-design` must not select a known hero formula before the project-specific reasoning exists.
- `master-design-director` critiques; it does not become a second concept owner.
- Legacy `cinematic-showroom-strategy` routes delegate media-only work to `media-choreography`; media choreography must not redefine brand, narrative, visual concept, or commercial posture.
- Do not infer “selective,” “concierge,” “quiet,” “museum-like,” or similar luxury postures without evidence.
- Reject meaningless repetition, not intentional motion identity.
- Reject unreasoned conventional structures, not convention itself.

This section is temporary. Remove bridge rules as the relevant V4 skills are replaced.

# Return conditions

Return to **understanding** if a claim, audience assumption, project scope, commercial posture, asset reality, or usage right changes.

Return to **concept exploration** if the selected visual mechanism cannot carry the real subject, the visitor journey is weak, or the concept has no downstream language.

Return to **experience shaping** if the concept stands but a crop, interaction, fallback, media, or production choice fails.

Explain the smallest change that follows from the evidence instead of restarting the whole process.

# Completion standard

For a direction-only request, completion means the designer can see the proposed concept, its basis, tradeoffs, and next useful test.

For an authorized build, completion means the requested local experience works at the tested scope, consequential defects are addressed, and unresolved limits are reported plainly.

External release remains a separate decision.

## Recurring question

**Does this reveal something specific about the brand, reward the visitor's attention, respect the work, serve the people using the site, and give the experience somewhere to go?**

If the answer is unclear, identify the missing evidence and run the smallest useful test. When the risk is low, make a provisional choice and continue.
