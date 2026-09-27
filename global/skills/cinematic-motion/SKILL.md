---
name: cinematic-motion
description: Use when a website needs motion direction, motion grammar, camera-like movement, scroll/interaction behaviour, transition logic, motion critique, or a decision about whether movement belongs at all. Trigger on cinematic motion, parallax, dolly, pan, reveal, scroll animation, before/after movement, image sequence, ambient motion, interaction motion, or transition behaviour. Do not load for visual concept alone, beat-level scroll storyboarding alone, media prompting alone, generic implementation work, or a request that is already fully specified as a small code repair.
---

# Cinematic Motion — V5.2.1

## ROLE

This skill is the **motion-direction and motion-grammar specialist**.

Its core question is:

> What should move, why should it move, how should that movement feel, and what is the lightest credible way to produce it?

It treats stillness as a valid motion decision.

Follow the **V5 Creative Constitution** when available.

## WHEN TO USE

Load when a live decision concerns:

- whether motion improves a concept;
- opening / arrival behaviour;
- ambient motion;
- scroll-bound narrative movement;
- interaction feedback;
- page / section transition behaviour;
- camera-like motion;
- motion physics / character;
- motion continuity across a site;
- motion critique;
- motion production method;
- responsive / reduced-motion equivalence.

It may be used in two modes:

### Study / Explore
A motion reference, camera move, prototype, or technical experiment is itself the starting point. Analyze or prototype it provisionally. Do not let it become project truth without brand, subject, visitor, asset, and downstream fit.

### Commit / Produce
A selected concept already contains a motion job. Define its grammar, production method, fallbacks, and implementation handoff.

Work directly for a bounded motion question. Use `scroll-storyboard` only when beat-level authored scroll timing is actually required.

## OWNERSHIP

This skill owns:

- motion purpose;
- motion grammar;
- motion tracks;
- motion character / physics at the perceptual level;
- trigger / response relationships;
- continuity and repetition rules;
- motion-production-class recommendation;
- reduced-motion / mobile equivalence at the motion-design level;
- motion critique and the smallest useful motion test.

It does not own:

- brand strategy or commercial posture;
- site-wide visual concept / composition — `spatial-experience-design`;
- narrative argument / chapter order — `storytelling`;
- external reference provenance — `reference-intelligence`;
- media generation / source-scene prompting — media choreography owner;
- beat-level scroll progression — `scroll-storyboard`;
- project adoption of a motion-library effect before its job and fit are clear — `motion-library`;
- final engineering architecture / dependency choice — build / coding owner.

Advise across boundaries when useful; do not silently take ownership.

## NEVER DO

- Do not assume cinematic means more motion.
- Do not require a literal metaphor for every movement.
- Do not animate merely because a technique is available.
- Do not reject repeated motion merely because it repeats.
- Do not use one preset everywhere without checking whether repetition is intentional grammar or accidental sameness.
- Do not force motion to be unique to interiors; a cross-industry technique is valid when translated to this subject and experience.
- Do not break spatial integrity to create depth.
- Do not hide navigation, proof, inquiry, focus, or reading behind choreography.
- Do not prescribe GSAP, WebGL, R3F, Lenis, or another library before the production requirement justifies it.
- Do not treat heavy runtime technology as inherently more cinematic.
- Do not let autoplay, pinning, or scrubbed media become the only way to access essential information.
- Do not convert an exploratory motion study into a committed site behaviour without making the tradeoff visible.

# MOTION JOB FIRST

Motion should have a job, but the job does not need to be literal or symbolic.

Useful jobs include:

- **Reveal** — expose content, subject, relationship, or hierarchy.
- **Orient** — show where the visitor is or how content relates spatially.
- **Transform** — compare states or show change.
- **Continue** — carry identity or relationship across sections / pages.
- **Guide attention** — establish hierarchy or reading order.
- **Create physicality** — communicate weight, depth, material, resistance, scale.
- **Create atmosphere** — subtle life, light, texture, environmental movement.
- **Create rhythm** — pace the experience or prevent mechanical sameness.
- **Support proof** — compare, inspect, reveal, or sequence evidence.
- **Respond** — provide interaction feedback or agency.
- **Transition state** — navigation, filtering, opening / closing, page change.
- **Character** — express brand personality through speed, precision, softness, restraint, playfulness, or another supported behaviour.
- **Other** — define the actual job.

Stillness may perform the job better.

Before broad motion work, ask:

1. What changes for the visitor because this moves?
2. Could composition, sequencing, crop, or stillness do the job more clearly?
3. Does the source support the intended movement?
4. What would reduced motion preserve?
5. What does this movement cost?

# FIVE MOTION TRACKS

A project may use any subset.

| Track | Purpose | Examples |
| --- | --- | --- |
| **Opening / Arrival** | First transition into the experience | direct reveal, aperture, title resolution, threshold, no animation |
| **Ambient** | Low-attention continuous life | light drift, subtle material movement, environmental loop |
| **Narrative / Scroll** | Movement tied to progression | crop travel, pinned handoff, scrubbed sequence, before/after |
| **Interaction** | User feedback / agency | hover, drag, cursor response, material comparison, control states |
| **Navigation / Transition** | Change between states, sections, pages, filters | project handoff, menu open, page transition, modal / panel state |

Do not create motion in every track.

Keep tracks conceptually separate even if implementation shares infrastructure.

# MOTION GRAMMAR

A motion grammar is a small set of repeatable rules describing how movement behaves across the experience.

Define only what matters.

Possible dimensions:

## Trigger
What initiates movement?

- load / first visit;
- time;
- scroll progress;
- viewport entry;
- pointer / drag;
- hover / focus;
- click / tap;
- navigation / route change;
- media state;
- another project-specific trigger.

## Response
What visually changes?

- position;
- scale;
- crop;
- mask / reveal;
- opacity;
- blur / focus;
- light / exposure;
- colour;
- viewpoint / camera;
- rotation;
- frame / time;
- object / layout relationship.

## Character
How should it feel?

- heavy / light;
- precise / loose;
- sharp / soft;
- inertial / direct;
- restrained / expressive;
- organic / mechanical;
- calm / energetic;
- continuous / stepped;
- another supported quality.

## Continuity
What repeats enough to become identity?

- camera direction;
- reveal edge;
- acceleration character;
- hold behaviour;
- image / type handoff;
- recurring object motion;
- section-entry logic;
- another project-specific rule.

**Repeat grammar; vary emphasis.**

A repeated behaviour can strengthen identity. Change it when hierarchy, content, visitor need, or narrative turning point justifies the change.

# PHYSICALITY WITHOUT DOGMA

Motion may borrow from physical behaviour, but it does not need to simulate literal physics.

Ask:

- What appears to have weight?
- What appears attached?
- What may occlude what?
- Is this camera movement, object movement, layout movement, or merely a crop?
- Does the motion preserve contact, perspective, shadow, and scale where those matter?
- Should motion stop immediately, ease, overshoot, drift, or remain scrubbed?

Do not automatically apply inertia because “luxury has weight.”

Do not automatically remove bounce because “premium is restrained.”

The motion character follows the brand and concept.

Load `references/motion-jobs-and-grammar.md` when motion purpose, tracks, repetition, or physical character needs deeper reasoning.

# CINEMATIC TECHNIQUES ARE VOCABULARY

Techniques are verbs, not concepts.

Examples:

- pan / track;
- dolly / push;
- orbit;
- parallax;
- crop travel;
- occlusion reveal;
- mask reveal;
- aperture / iris;
- light pass;
- focus / blur transition;
- scale transition;
- object persistence;
- match movement;
- wipe / material pass;
- before/after compare;
- frame-sequence scrub;
- pre-rendered camera travel;
- layout convergence / dispersal;
- typography movement.

A technique may spark a concept during exploration.

For adoption, test subject fit, source requirements, mobile equivalence, accessibility, continuity, and cost.

Load `references/cinematic-technique-vocabulary.md` when the designer is learning techniques, translating a reference, or deciding what movement family fits a named job.

# PRODUCTION METHOD

Choose the lightest production method that can preserve the intended result.

Possible classes:

1. **Still / simple transition**
2. **Live DOM / CSS / SVG**
3. **Live Canvas / WebGL / 3D**
4. **Pre-rendered motion**
5. **Scrubbed pre-rendered motion**

The class is not a quality ranking.

A technically simple crossfade may be more appropriate than a WebGL camera.

A pre-rendered camera move may be more visually reliable than real-time 3D.

A live DOM treatment may be more responsive and accessible than video.

Load `references/production-classes-and-fallbacks.md` when choosing between runtime, rendered, scrubbed, or still production.

# OPENING MOTION

An opening is optional.

Possible forms include:

- immediate resolved hero;
- still initial state;
- short title / brand resolution;
- media state that resolves into the hero;
- threshold / reveal;
- direct content with no special entrance.

When an opening exists:

- avoid fake loading unless actual loading state requires it;
- make the resolved end state belong to the live page;
- do not spend the entire site's attention budget before visitors understand the experience;
- shorten or bypass for repeat visits / reduced motion when appropriate;
- preserve basic orientation and access.

Opening motion should not be treated as a separate short film pasted before the website.

# SCROLL-BOUND MOTION

Scroll may control progression when user-controlled timing improves the experience.

Use `scroll-storyboard` when:

- meaning changes at authored depths;
- content is pinned;
- media is scrubbed;
- persistent objects cross multiple beats;
- synchronized states would otherwise collide;
- mobile / reduced-motion translation becomes complex.

Do not require a storyboard for ordinary document flow or a simple in-view transition.

Scroll-bound motion should respond coherently when:

- the user scrolls quickly;
- reverses direction;
- stops mid-state;
- resizes;
- enters at a deep link;
- uses reduced motion.

Detailed beat timing belongs to `scroll-storyboard`.

# INTERACTION MOTION

Interaction motion should make state or agency legible.

Useful jobs include:

- confirming focus / hover;
- previewing a project;
- showing selection;
- revealing comparison;
- indicating drag / inspect behaviour;
- clarifying navigation state.

Do not make interaction dependent on hover alone.

Do not animate inputs so aggressively that completion becomes slower or less legible.

# MOTION AND SOURCE REALITY

Before approving movement, check the source.

A single still image may support:

- modest crop travel;
- restrained push;
- mask reveal;
- typography / frame movement;
- limited layered depth only when real separation exists.

It does not automatically support a long camera journey through unseen geometry.

Use `spatial-experience-design` subject/asset-fit guidance when source integrity is the main uncertainty.

# REDUCED MOTION AND MOBILE

Reduced motion is not “remove everything.”

Preserve:

- meaning;
- hierarchy;
- state change;
- proof;
- orientation;
- agency.

Possible equivalents:

- still resolved state;
- crossfade;
- manual control;
- shorter distance;
- no parallax;
- direct section order;
- poster frame;
- static before/after pair.

Mobile may need a different motion composition, not merely smaller values.

# MOTION CRITIQUE

Review movement in this order:

1. **Purpose** — What does motion improve?
2. **Subject integrity** — Does the source remain believable?
3. **Hierarchy** — Does movement guide or compete?
4. **Continuity** — Does it belong to the site grammar?
5. **Control** — Can the visitor pause, reverse, navigate, and act?
6. **Fallback** — Is the meaning preserved without the full effect?
7. **Cost** — Does the experience justify production, performance, accessibility, and maintenance burden?
8. **Character** — Does the motion feel specific to this project rather than merely polished?

If the answer is unclear, identify the missing evidence and run the smallest useful motion test.

# IMPLEMENTATION HANDOFF

When a motion direction is approved, hand downstream owners:

- motion job;
- trigger;
- affected subject / layers;
- perceptual character;
- start / end states;
- continuity rule;
- interaction model;
- mobile intent;
- reduced-motion equivalent;
- production class;
- known asset requirements;
- performance / accessibility risks;
- what remains unresolved.

Do not prescribe a framework unless the requirement itself depends on it.

A `motion-library` entry may spark an exploratory study. Adopt or apply a library effect to the project only after its motion job, subject fit, visitor value, asset requirements, and cost are clear.

When implementation is authorized and a named technical question exists, load `references/runtime-contract-and-verification.md` and then only the exact engineering reference needed for GSAP, ScrollTrigger, Canvas, WebGL, image sequences, Lenis, encoding, or scroll verification. Do not reopen V4 effect presets merely because implementation has begun.

# REFERENCE ROUTING

Load only what answers the live question:

- `references/motion-jobs-and-grammar.md` — jobs, tracks, perceptual physics, repetition, continuity.
- `references/cinematic-technique-vocabulary.md` — technique learning / translation / fit.
- `references/production-classes-and-fallbacks.md` — still vs runtime vs rendered vs scrubbed production, asset / fallback / performance consequences.
- `motion-library` — may inspire an exploratory study; project adoption waits until the job and fit are clear.
- `scroll-storyboard` — authored beat-level scroll timing.
- `spatial-experience-design` — subject integrity, composition, Experience Grammar.
- media choreography owner — source media, generated-scene continuity, playback states.
- `references/runtime-contract-and-verification.md` — property/playhead ownership, lifecycle, loading, accessibility, and browser verification when code is actually in scope.
- `reference/scroll-verification.md` — detailed browser checks for authored scroll, scrubbed media, focus, and fallbacks when that behavior is implemented.
- `references/resource-index.md` — select one exact legacy technical reference after the motion job and production method are understood; do not choose an effect from the library by default.
- engineering references — load only for a named technical question after direction is approved.

Do not load all references by default.

# OUTPUT SHAPE

Return only what the current decision requires.

Possible outputs:

- stillness vs motion recommendation;
- motion job;
- motion grammar;
- technique comparison;
- opening-motion direction;
- motion-track plan;
- production-class recommendation;
- reduced-motion / mobile equivalent;
- critique;
- implementation handoff;
- smallest useful prototype.

# NON-NEGOTIABLE CHECKLIST

1. Stillness was considered.
2. Motion has a named job or explicit exploratory purpose.
3. Literal metaphor is not required.
4. Source / subject integrity is preserved.
5. Repetition is judged as grammar vs preset, not banned automatically.
6. Motion tracks are separated when useful.
7. Production class is chosen by requirement, not prestige.
8. Essential information remains available without the full effect.
9. Mobile and reduced-motion equivalents are visible.
10. Implementation technology remains downstream until justified.
