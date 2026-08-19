# Colour Roles and Verification

Use this reference when colour is selected, changed, audited, tokenised, or
verified for a product UI, website, component, theme, form, status, chart, or
brand surface. It is a decision method, not a palette generator.

## Inputs

Establish the smallest relevant context before proposing a value:

- medium and user task;
- existing brand assets, tokens, and constraints;
- affected states, content, themes, viewports, images, overlays, motion, or
  material/light conditions;
- functional or expressive job; and
- accessibility target and any market/site constraint that materially matters.

State when an input is missing. Do not infer an audience's response from a
mood word, a demographic label, or a hue name.

## Decision Method

1. **Purpose.** Name what colour must accomplish: separation, hierarchy,
   interaction, focus, status, data distinction, atmosphere, brand expression,
   or another concrete job.
2. **Role.** Reuse an existing semantic role when it already fits. Propose the
   smallest new role only when it does not. Name roles by purpose, not raw hue
   or component location.
3. **Constraint.** Separate functional uses from expressive uses. Treat text,
   controls, focus, status, warnings, links, selection, and data as
   constraint-first. Treat atmosphere, imagery, material, and brand accent as
   exploratory only while they preserve functional clarity.
4. **Context.** Check the actual pairing and rendered conditions: theme,
   state, background, viewport, content length, display, image, overlay,
   motion, material, or light.
5. **Verification.** Measure the applicable accessibility constraints and
   inspect a representative rendered result. Label any remaining judgement as
   a hypothesis, convention, or unresolved question.

## Semantic Roles

Keep the set small. Typical roles include:

| Family | Example roles | Check |
| --- | --- | --- |
| Foundation | `surface`, `surface-subtle`, `surface-inverse` | Layer separation and theme behaviour |
| Content | `text-primary`, `text-secondary`, `text-inverse`, `border-subtle` | Actual foreground/background pairings |
| Action | `action-primary`, hover, pressed, disabled variants | Discoverability and all relevant states |
| Focus | `focus-ring`, `focus-offset` | Keyboard-visible focus across backgrounds |
| Status | error, warning, success, info plus paired content | A non-colour cue for consequential meaning |
| Data | minimum required series plus labels/patterns/shapes | Distinguishability without hue alone |
| Expression | brand or display accents | Hierarchy, context, and whole-composition review |

Use raw colour scales only as implementation inputs. Components should consume
semantic roles so a theme or brand change does not require scattered manual
replacement.

## Required Web Checks

For web UI, use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) as the current
baseline where it applies.

- Do not use colour as the only cue for information, action, response, or
  distinction. Pair consequential meaning with text, iconography, shape,
  pattern, position, or another perceivable signal.
- Check real text/background pairings. WCAG 2.2 minimum contrast is 4.5:1 for
  normal text and 3:1 for large text, subject to its stated exceptions.
- Check meaningful UI component boundaries, state indicators, focus treatment,
  and graphical objects at 3:1 where the non-text contrast criterion applies.
- Check hover, focus, pressed, selected, disabled, busy, error, empty, and
  success states that exist in the product. A token can pass in one state and
  fail over an image, gradient, overlay, or different theme.
- Inspect the rendered result at relevant viewport sizes, content lengths,
  light/dark themes, keyboard focus, and reduced-colour/CVD conditions when
  useful. A calculated ratio is evidence, not a complete visual review.

Do not claim WCAG conformance unless the requested scope, applicable criteria,
and actual tested result support that claim.

## Context-Specific Judgement

For brand and marketing work, use colour as one layer alongside typography,
imagery, spacing, copy, category codes, and proof. Treat statements such as
“blue creates trust,” “purple creates luxury,” or “red converts better” as
context-dependent hypotheses, never causal rules.

For spatial, cinematic, editorial, print, projection, or material-led work,
inspect actual scene/display conditions: luminance, salience, light, texture,
reflectance, glare, viewing distance, motion, and site/cultural context. A web
contrast ratio does not settle whether a scene works.

Load [color-evidence-and-context.md](color-evidence-and-context.md) when a
claim about psychology, culture, audience, print, data visualisation, spatial
conditions, or an experiment affects the decision.

## Output

Return only what the task needs:

| Field | Content |
| --- | --- |
| Context | Medium, task, existing system, theme/display constraints |
| Role decision | Reuse, extend, or remove a semantic role and why |
| Value mapping | Relevant values and `on-*`/state pairings |
| Redundant cue | Non-colour communication where meaning is consequential |
| Verification | Ratios/checks performed, rendered review, and limits |
| Evidence label | Required, supported, context-dependent, conventional, or unresolved |
| Next action | Smallest project validation still needed |

## Anti-Patterns

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Palette first | Choosing hues before naming the user or communication job | Start with purpose and semantic role |
| Hue determinism | Treating a colour/emotion association as universal | State it as a hypothesis and validate in context |
| Ratio-only approval | Passing a calculator result without inspecting states or rendering | Check actual pairings, states, themes, and the rendered result |
| Colour-only status | Meaning exists only in red, green, or another hue | Add text, icon, shape, pattern, or placement |
| Raw-value sprawl | Components consume scattered hex values | Use semantic roles and paired values |
| Formula as proof | Treating harmony rules as evidence of quality | Use relationships only for exploration, then review the composition |
