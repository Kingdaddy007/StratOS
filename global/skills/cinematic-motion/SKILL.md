---
name: cinematic-motion
description: 'Use this skill when planning or implementing cinematic motion for high-end interior decorator, spatial design, architecture, gallery, showroom, furniture, decor, or luxury home websites. Activated by "add GSAP", "scroll animation", "make this cinematic", "room walkthrough", "parallax interior scene", "before/after reveal", "object spine", "curtain reveal", "image sequence", "WebGL", "canvas", "gallery procession", or any spatial storytelling motion task. Do NOT use for generic product dashboards, backend/API/security/database work, or decorative motion that is not tied to a room, material, threshold, object, proof, or inquiry moment.'
---

# Cinematic Motion

## WHEN TO USE THIS

- Load after a territory is selected and `experience-blueprint.md` plus `production-plan.md` (or approved equivalents) define the communication job, assets, constraints, and fallbacks.
- Consult the motion library only after naming the motion job. Library effects are candidates to adapt, not a compulsory source or a substitute for concept reasoning.
- Load when motion must express interior atmosphere, spatial transformation, material behavior, gallery pacing, or object-led scrollytelling.
- Load before writing GSAP, ScrollTrigger, canvas, R3F, image sequence, parallax, mask, or before/after reveal code.
- Load `reference/lenis-gsap-scroll-foundation.md` when Lenis is used as scroll infrastructure.
- Load `reference/scroll-driven-3d-cube.md` when the concept is a room box, rotating wall set, material plinth, CSS 3D cube, or scroll-driven cube gallery.
- Load `canvas-ui` when a contained live DOM/WebGL effect may serve a named
  spatial communication job. Let `canvas-ui` compare it against still, DOM/CSS,
  and media alternatives, verify the current upstream source, and own its
  import/fallback gate.

## NEVER DO

- Never animate before naming the physical law of the space.
- Never use the same fade-up preset across consecutive sections.
- Never add motion that could be pasted onto any other industry.
- Never let scroll-jacking hide proof, navigation, or inquiry.
- Never run canvas/WebGL/image-sequence work without a performance and fallback plan.
- Never use video as wallpaper behind ordinary sections without a section-specific spatial job.
- Never mix ambient loops, arrival timelines, and scroll-bound timelines in one uncontrolled animation chain.
- Never build a spatial site with placeholder animation when the concept depends on real imagery, rendered frames, or 3D assets.

## MOTION CONTRACT

Stillness is an explicit valid decision. Add motion only when it answers one of these spatial jobs better than a still composition:

1. Open a threshold.
2. Reveal a room.
3. Move light across material.
4. Transform before into after.
5. Guide the eye with a signature object.
6. Let a material behave physically.
7. Shift from atmosphere to proof.
8. Slow the visitor into inquiry.

If the motion does none of these, remove it.

For every proposed motion, record: communication job, triggering evidence, why stillness is insufficient, affected content, interaction model, reduced-motion equivalent, mobile simplification, performance cost, and maintenance burden.

## FOUR MOTION TRACKS

When motion exists, classify applicable behavior into four separate tracks. A project does not need motion in every track:

| Track | Purpose | Examples | Guardrail |
| --- | --- | --- | --- |
| Arrival | First physical event | curtain split, door open, light wash, mural reveal | Run once; do not block content too long |
| Ambient | Low-attention life | dust motes, textile drift, light shimmer, plant shadow | Pause offscreen; respect reduced motion |
| Scroll-bound | Playhead-controlled narrative | stacked panels, room walk, object guide, before/after reveal | Must scrub or hold, not autoplay after scroll stops |
| Interaction | User feedback | material swatch hover, project index preview, concierge form focus | Subtle, direct, accessible |

## SPATIAL MOTION ARCHETYPES

These are candidate grammars. Select only what the approved concept and constraints justify; selecting no cinematic archetype is acceptable.

### Gallery Procession

Use for portfolio and editorial interiors. Pin or hold one focal image/room at a time. Reveal captions like museum labels. Use slow scale from `1.04` to `1`, opacity, and light shifts. Avoid scatter, bouncy easing, and excessive overlays.

### Layered Diorama

Use for immersive hero scenes. Build a depth sandwich: atmosphere, display type, room/object plane, proof/UI plane, foreground blur. Animate layers with different amplitudes. Keep text static when an object is carrying attention.

### Signature Object Spine

Use when one chair, lamp, vase, door, mural, textile roll, or material sample can own the journey. Create an object blocking map with position, scale, rotation, section role, and collision-safe text zones at 0/25/50/75/100%.

### Transformation Reveal

Use for before/after, redesign, staging, renovation, or styling proof. Make the reveal a cinematic argument: slider, curtain, light sweep, plan-to-room morph, or photograph-to-material transition. Caption the decision, not just the result.

### Stacked Media Panels

Use for full-bleed room films or project chapters. Pin the viewport, stack panels vertically, move the entering panel from `yPercent: 100` to `0`, and add restrained shadow or darkening to sell physical overlap.

### Material Wipe

Use scene-native matter as the transition: fabric pull, plaster scrape, glass fog, shadow pass, sunlight spill, brush stroke, stone edge, or curtain veil. Avoid generic CSS diagonals unless the brand has a geometric reason.

### Architectural Room Box

Use for a scroll-driven CSS 3D cube that rotates through four curated room walls or six sides of a material sample. Load `reference/scroll-driven-3d-cube.md`. Every face must have a context-inherited prompt, strategic source, proof job, text-safe zone, and mobile/reduced-motion fallback.

### Cinematic Layout Formation

Use when portfolios, material archives, or process galleries assemble, swing, slide, or sweep dynamically during scroll. Load `reference/on-scroll-layout-formations.md`. Covers:
- **Spatial Convergence** (exploded 3D items assembling into a clean mosaic).
- **Cinematic Window** (dual-axis container/image sliding reveals).
- **Swinging Cabinet** (Y-axis panel rotations).
- **Arc Procession** (sweeping items around remote centers).

### Canvas-First Walkthrough

Use only when a camera path through a room/world is the concept. DOM becomes edge instrumentation: labels, progress, inquiry, captions. Require camera-path brief, frame/scene map, preload strategy, and mobile still/video fallback.

### Living Proof System

Use for method/process credibility. Animate project index states, press/proof ribbons, material selection, availability notes, or inquiry progress. Keep motion trust-preserving and quiet.

## VIDEO-LED WEBSITE CHOREOGRAPHY

Load `reference/video-to-website-choreography.md` when video, canvas, frame sequence, or scroll-led media is involved.

For a media-heavy experience, create or require a choreography section in `production-plan.md` or an approved equivalent before implementation. A legacy `showroom-choreography.md` remains valid.

For each media-led section define:

- Journey stage.
- Belief/proof job.
- Media type.
- Scroll behavior.
- Enter and leave range.
- Text zone.
- Reveal rhythm.
- Motion track.
- Fallback.
- Prompt requirement.

Video must perform one of these jobs:

1. Establish atmosphere.
2. Open a threshold.
3. Reveal taste.
4. Prove transformation.
5. Show material intelligence.
6. Carry portfolio proof.
7. Slow the visitor into inquiry.

If it does none of these, use a still or remove it.

## IMPLEMENTATION RULES

- Use GSAP + ScrollTrigger when approved scroll choreography needs timeline control, pinning, or scrubbed sequencing; do not add it for simple transitions.
- Use Lenis only as scroll infrastructure; it must serve the showroom choreography.
- Use `motion`/Framer only for product-like microstates and small UI transitions.
- Use CSS transitions for simple hover/focus states.
- Use canvas image sequences for pre-rendered room/object/camera films that must scrub frame-accurately; load `reference/canvas-frame-scroll-implementation.md`.
- Use R3F/WebGL only when depth, camera path, object inspection, or material behavior cannot be achieved with DOM/image layers; load `reference/codrops-canvas-cylinder-gallery.md` or `reference/scroll-mapped-3d-camera-scenes.md` when relevant.
- Use CSS 3D + GSAP when a scroll-controlled cube can tell the spatial story without WebGL; load `reference/scroll-driven-3d-cube.md`.
- Use dynamic grid assembly, dual-axis window reveals, or Y-axis swing cabinets when scroll layouts must transition dynamically; load `reference/on-scroll-layout-formations.md`.
- Use IntersectionObserver or ScrollTrigger lifecycle hooks to pause ambient loops offscreen.
- Use `prefers-reduced-motion` to replace travel with crossfades, static chapter images, or manual navigation.
- Keep primary navigation and inquiry reachable even during pinned sequences.

## ASSET AND PERFORMANCE GATES

Before implementation, classify the motion:

| Motion Type | Required Production Evidence | Fallback |
| --- | --- | --- |
| Image sequence | frame map, preload plan, mobile frame tier | poster image or compressed video |
| R3F object | 3D spec sheet, material budget, collision zones | transparent PNG or short video loop |
| Canvas-first walkthrough | camera-path brief, chapter cues, DOM overlay map | still chapter stack |
| Diorama parallax | depth-map, scene-kit brief, asset-lighting brief | static layered hero |
| Before/after reveal | paired assets, crop parity, caption logic | static paired gallery |

Performance rules:

- Use no more than one heavy real-time WebGL scene per page unless explicitly justified.
- Do not combine heavy WebGL, image sequence, and multiple autoplay videos in the first viewport.
- Preload only the frames/assets required for the first interaction; lazy-load later chapters.
- Use poster frames and mobile-specific crops for all room films.
- Dispose WebGL geometries/materials when changing worlds or unmounting scenes.

## ENGINEERING PATTERNS

- Canvas sequence: preload frames in chunks, draw closest loaded frame during fast scroll, resize canvas for DPR, and clear between draws.
- 3D annotation: project named 3D points to CSS pixels, hide labels when occluded, and provide mobile stacked labels.
- Horizontal scroll transfer: pin the section and map vertical progress to `x` translation; never rely on native horizontal overflow for narrative sections.
- SVG material masks: animate `clipPath`, `mask-size`, path progress, or transform scale; keep semantic text outside raster masks.
- Layer sandwich: place background, type, object, UI, and foreground blur in named wrappers; define pointer-events intentionally.
- Stacked panels: pin a parent, absolutely stack panels, translate active panels, and use z-index based on chapter order.

## EASING AND TIMING

- Interior luxury: `power2.out`, `power3.out`, or cubic `0.16, 1, 0.3, 1`; 700-1400ms for arrivals.
- Gallery: long, smooth ease-outs; no bounce.
- Industrial/spatial systems: linear or near-linear scrub with dampening.
- Textile/organic: slow in/out, subtle sine loops, low amplitude.
- Playful decor object: limited `back.out` only when the brand is visibly playful.

## ANTI-PATTERNS

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Universal Fade-Up Syndrome | Same opacity/y reveal everywhere | Use scroll scrub, static holds, material wipes, or distinct chapter timings |
| Decorative Parallax | Layers move but mean nothing | Tie every layer to depth, light, object, or room transition |
| WebGL Vanity | 3D asset does not guide, reveal, prove, or transition | Use image/DOM instead |
| Timeline Collision | Ambient loops are overwritten by scroll timelines | Separate tracks and refs |
| Hidden Inquiry | Pinned sequence traps access to contact/action | Keep edge CTA or final clear inquiry section |
| Impossible Reverse | Scrubbed liquid/gravity looks absurd backwards | Use event-triggered clips or non-reversible transitions |
| Background Video Wallpaper | Video loops behind normal sections without narrative responsibility | Define section job, text zone, scroll behavior, and fallback or remove video |


## REFERENCE LOADING RULES

Load `references/resource-index.md` when the task needs examples, specialist criteria, implementation details, or domain-specific diagnostics beyond this core workflow. Select only the references whose indexed purpose matches the task; do not load the package wholesale.
## OUTPUT SHAPE

**Motion plan:** Communication job -> stillness comparison -> applicable tracks -> candidate grammar -> production evidence -> fallback -> implementation notes.

**Implementation guidance:** DOM/canvas/WebGL structure -> timeline responsibilities -> asset loading -> reduced-motion -> verification.

**Audit:** Motion purpose -> track separation -> template risks -> performance risks -> required fixes.

## NON-NEGOTIABLE CHECKLIST

1. The communication job and stillness alternative are evaluated.
2. Applicable motion tracks are separated; unused tracks are explicitly omitted.
3. Any selected archetype is justified by the approved concept.
4. Production evidence exists before code.
5. Video/canvas scenes have choreography maps, not only motion descriptions.
6. Scene-native transitions replace generic wipes when transitions are needed.
7. Scroll-bound motion stops when scroll stops unless intentionally ambient.
8. Reduced-motion and mobile fallbacks exist.
9. Inquiry and navigation remain reachable.
10. No repeated fade-up preset across consecutive chapters.
