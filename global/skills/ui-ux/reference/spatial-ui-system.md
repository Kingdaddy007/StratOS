# Spatial UI System

## Contents

- When to use this reference
- Spatial prohibitions
- Primary UX model
- Spatial UI patterns
- Visual craft rules
- Accessibility and state coverage
- Responsive rules
- Anti-patterns
- Output and checklist

## WHEN TO USE THIS

- Load for spatial brand UI: decorator portfolios, project galleries, service/inquiry paths, material libraries, showrooms, and editorial interior pages.
- Load after `spatial-experience-design` when turning an approved experience blueprint into usable navigation, states, forms, and responsive behavior.
- Load when checking whether premium atmosphere still lets visitors understand proof, process, and inquiry.

## NEVER DO

- Never convert a spatial brand into a SaaS landing page.
- Never make buttons louder than the rooms, objects, materials, or transformation proof.
- Never start with generic cards, icon grids, or centered service blocks.
- Never hide essential inquiry, accessibility, or navigation under spectacle.
- Never use visual restraint as an excuse for unclear labels, invisible focus, or broken mobile flow.
- Never let project indexes, galleries, or forms feel like unstyled afterthoughts after a cinematic hero.

## REUSABLE UX JOBS

High-end interior and spatial sites commonly need the following UX jobs, but the approved experience blueprint decides their presence and order. `Atmosphere -> Taste -> Transformation -> Proof -> Method -> Inquiry` is one candidate journey, not a compulsory sequence.

Map UI responsibilities to whichever jobs the selected concept uses:

| Stage | Visitor Need | UI Behavior |
| --- | --- | --- |
| Atmosphere | Feel the world immediately | Quiet nav, full-bleed scene, minimal text |
| Taste | Understand the aesthetic standard | Curated projects, room captions, material cues |
| Transformation | See capability | Before/after, staging logic, design decisions |
| Proof | Trust the designer | Press, testimonials, project facts, client context |
| Method | Know how work happens | Process timeline, scope, fit, expectations |
| Inquiry | Take the next step | Calm form, concierge CTA, next-step clarity |

## SPATIAL UI PATTERNS

### Navigation

- Use quiet, persistent navigation with clear text labels.
- Keep nav at edges during cinematic sections; avoid floating center nav unless the visual thesis requires it.
- Use project index, studio, method, and inquiry as plain language labels.
- Keep inquiry reachable without shouting.

### CTAs

- Use concierge language: "Begin an inquiry", "Discuss a residence", "Request a consultation", "View private portfolio".
- Avoid SaaS urgency: "Get started", "Start free", "Try now", "Book instantly" unless the brand truly operates that way.
- Make one primary action visible per major view.

### Project Galleries

- Present projects as curated rooms or chapters before broad grids when the proof strategy depends on curation.
- Use gallery labels: location, room type, material focus, design move, year, role.
- Let one project breathe before showing many.
- Use indexes for scanning when the narrative has established enough context; a proof-first concept may legitimately expose structured evidence early.

### Material and Swatch UI

- Treat material swatches as tactile evidence, not color dots.
- Pair swatches with material names, source, finish, and room use when relevant.
- Use hover/tap previews carefully; every hover path needs a keyboard/touch equivalent.

### Inquiry Forms

- Keep forms calm and selective.
- Ask for project type, location, timeline, scope, budget posture if needed, and what the visitor wants changed.
- Explain what happens next.
- Preserve typed values on errors.
- Show success as a refined confirmation, not a generic toast.

## VISUAL CRAFT RULES

- Consult [hero-layout-blueprints.md](../../../reference/hero-layout-blueprints.md) for structural layouts, aesthetic palettes, and typography hierarchy models to inspire custom designs.
- Use typography as gallery hierarchy: large atmospheric display, tiny metadata, readable body.
- Use line length caps; interior captions should be short and precise.
- Use whitespace as architecture: walls, corridors, pauses, clearings.
- Use cards only when they are true artifacts: project plates, material samples, process notes, press clippings.
- Do not nest cards.
- Do not make every section the same width, rhythm, or grid.
- Use image crops deliberately; mobile crops must preserve room subject and lighting.
- Use OKLCH or a consistent token system for implementation, but choose colors from material/light behavior first.
- For a material colour decision, load `color-and-contrast.md`. Load
  `color-evidence-and-context.md` only when scene, material, light, culture,
  or a psychology claim affects the decision.

## ACCESSIBILITY AND STATE COVERAGE

Premium still needs complete UX:

- Keyboard access for navigation, galleries, accordions, sliders, forms, and project filters.
- Visible focus states that fit the visual system.
- Text alternatives for room images that describe information, not mood fluff.
- Reduced-motion alternatives for all travel, parallax, canvas, and reveal effects.
- Loading states for media-heavy pages.
- Empty states for filtered project indexes.
- Error and success states for inquiry forms.
- Mobile touch targets at least 44px.

## RESPONSIVE RULES

- Mobile must remain spatial, not collapse into raw content blocks.
- Replace pinned scenes with chaptered stills or reveal cascades on small screens.
- Preserve approved chapter logic, governing concept, and inquiry path.
- Use mobile-specific crops for room imagery and before/after comparisons.
- Keep captions near their images; do not force visitors to remember what a caption describes.

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Fix |
| --- | --- | --- |
| SaaS Skin | Hero headline, feature cards, bright CTA, logos, stats | Use the approved spatial argument and concierge inquiry |
| Grid Dump | Many projects shown without context or hierarchy | Use the selected proof strategy and intentional curation |
| Invisible Luxury | Pretty but unusable nav/forms/focus | Keep quiet UI, not hidden UI |
| Beige Template | Warm neutral, serif, stock room, fade-up | Require visual thesis and scene kit |
| Ghost CTA Failure | Low-contrast outline button | Use refined but legible action treatment |
| Captions as Decoration | Tiny labels with no useful information | Write project/material-specific metadata |


## REFERENCE LOADING RULES

Load `references/resource-index.md` when the task needs examples, specialist criteria, implementation details, or domain-specific diagnostics beyond this core workflow. Select only the references whose indexed purpose matches the task; do not load the package wholesale.
## OUTPUT SHAPE

**UX plan:** Journey stage -> primary action -> navigation/inquiry model -> key states -> responsive behavior.

**UI audit:** Generic-template risks -> clarity risks -> accessibility/state gaps -> spatial fixes.

**Implementation handoff:** Components/patterns -> states -> mobile/reduced-motion -> verification checklist.

## NON-NEGOTIABLE CHECKLIST

1. UI follows the approved brand-specific chapter logic.
2. Inquiry path is visible, calm, and specific.
3. Project/gallery UI supports curation before scanning.
4. Material and room captions provide real information.
5. Navigation, focus, forms, and state coverage are complete.
6. Mobile preserves the controlling argument and proof/inquiry responsibilities.
7. No default SaaS card grid or universal fade-up pattern remains.
