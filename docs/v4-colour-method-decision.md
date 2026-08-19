# V4 Colour Method Decision

**Status:** implemented in the canonical source on 2026-08-19.

## Decision

Retire the standalone `color-system` skill from active routing. Keep one
conditional colour method inside `ui-ux`:

- `global/skills/ui-ux/reference/color-and-contrast.md` for semantic roles,
  actual rendered pairings/states, accessible communication, and review.
- `global/skills/ui-ux/reference/color-evidence-and-context.md` only for
  psychology, culture, brand expression, print, data, spatial/cinematic, or
  experimental claims.

The old source remains in `global/archives/color-system-v3-source/`. It is not
deleted and is not built into host payloads.

## What changed

| Previous pattern | V4 replacement |
| --- | --- |
| Palette generation as a standalone authority | A UI/UX decision method: purpose -> semantic role -> constraint -> context -> verification |
| “Blue means trust”, “purple means luxury”, or a hue-emotion table | A context-dependent hypothesis that needs audience, category, and composition evidence |
| Gender/age/culture preferences as a prescription | No demographic inference; use actual audience or local context where material |
| “Red CTA beats green” | Define the action and outcome, preserve accessibility, and run a valid experiment only when warranted |
| Harmony formulas as a decision engine | Optional exploration only; verify hierarchy, legibility, and the rendered composition |
| Palette-level accessibility | Actual text, component, focus, state, theme, overlay, and non-colour-cue checks |

## Evidence basis

The decision report from 2026-08-19 was checked against the current canonical
source and current W3C WCAG 2.2 documentation. The durable web baseline is:

- colour is not the sole communication cue where it carries meaning;
- text and non-text contrast are checks on actual rendered pairings, not a hue;
- semantic roles help components reuse intended meaning across themes and
  states; and
- standards answer perceptibility requirements, not whether a colour creates
  trust, luxury, emotion, or conversion.

See [WCAG 2.2](https://www.w3.org/TR/WCAG22/),
[contrast minimum guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html),
and [non-text contrast guidance](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html).

## Verification needed later

The refactor passes source validation and routing tests. It still needs one real
interface task that selects colour from normal language, reuses or extends
tokens, checks a real rendered state, and reports the remaining uncertainty.
