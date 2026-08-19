# Design Bans — Absolute Prohibitions

## The Absolute Bans

Match-and-refuse. If you're about to write any of these, rewrite the element with different structure:

- **Side-stripe borders.** `border-left` or `border-right` > 1px as colored accent. Rewrite with full borders, background tints, icons, or nothing.
- **Gradient text.** `background-clip: text` with gradient. Use a single solid color. Emphasis via weight or size.
- **Glassmorphism as default.** Blurs and glass cards used decoratively. Rare and purposeful, or nothing.
- **The hero-metric template.** Big number, small label, supporting stats, gradient accent. SaaS cliche.
- **Identical card grids.** Same-sized cards with icon + heading + text, repeated endlessly.
- **Modal as first thought.** Exhaust inline and progressive alternatives first.
- **Em dashes in copy.** Use commas, colons, semicolons, periods, or parentheses.

## The AI Slop Test

If someone could look at this interface and say "AI made that" without doubt, it has failed. Check:

- Are you using Inter, DM Sans, or Outfit by reflex?
- Is the palette purple-to-blue or teal-to-green?
- Are there rounded-square icon tiles above every heading?
- Is every section a centered stack with identical card grids?
- Could someone guess the palette from the category name alone? ("fintech = navy + gold", "healthcare = white + teal")

If yes to any: rework until the answer is no.

## Context-Specific Bans

### Brand Register
- No bounce/elastic easing (except entertainment/gaming)
- No unconventional primary nav placement
- Zero images for imagery-dependent brands is a bug

### Product Register
- No page-load choreography
- No cinematic parallax
- Motion limited to 150-250ms state changes only

## Film Grain Overlay Note

Film grain via SVG `<feTurbulence>` is an intentional premium aesthetic treatment, NOT an AI slop tell. It should not be flagged by anti-pattern detection.

---

**Single source of truth.** All workflows and skills that check for anti-patterns should reference this file rather than duplicating the ban list.

**Cross-references:**
- `skills/ui-ux/SKILL.md` Layer 2 > Absolute Bans
- `skills/ui-ux/reference/operation-routing.md` > audit or critique
- `skills/cinematic-motion/SKILL.md` Section 1 > Diagnostic Step 3
