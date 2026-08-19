---
name: color-system
description: 'Use this skill when selecting, auditing, or implementing color palettes for any brand, website, app, marketing asset, or design project. Activated by "choose a color palette", "color scheme", "brand colors", "color psychology", "what color should I use", "color harmony", "complementary colors", "color contrast", "accessible colors", "color roles", "functional color", "action color", "CTA color", "color for this brand", "color audit", "palette generation", "monochromatic", "analogous", "triadic", "tetradic", "split complementary", "color meaning", "what does this color convey", or any task where color decisions affect brand perception, usability, or emotional response.'
---

# Color System

## WHEN TO USE THIS

- Load when selecting or evaluating a color palette for a brand, website, app, or marketing asset.
- Load when implementing color tokens, CSS variables, or design system color scales.
- Load when auditing an existing design for color psychology alignment, accessibility, or cross-platform consistency.

## NEVER DO

- Never pick colors by personal taste alone. Start from audience, message, and brand positioning.
- Never assign colors without defining their functional role (action, support, neutral, anchor, communicator).
- Never evaluate a palette without testing lightness contrast for text readability.
- Never assume color meanings are universal — always check cultural and demographic context.
- Never use more than one attention-grabbing color per view without deliberate intent.
- Never skip cross-platform testing (RGB vs CMYK, mobile vs desktop, color blindness simulation).
- Never treat color as the only identity ingredient — if the brand's weight is on photography, typography, or product, color may play a supporting role.

## COLOR PSYCHOLOGY

Each color triggers both positive and negative emotional responses. Saturation and brightness modulate the effect more than hue alone.

| Color | Positive | Negative |
|---|---|---|
| Red | Passion, energy, power, urgency, love | Anger, danger, warning, aggression |
| Orange | Action, energy, playfulness, positive change | Cheapness, immaturity |
| Yellow | Optimism, warmth, energy, cheerfulness | Instability, anxiety, caution |
| Green | Nature, health, freshness, growth, healing | Envy, guilt, jealousy |
| Blue | Trust, security, intelligence, calm, loyalty | Coldness, fear, distance |
| Purple | Luxury, royalty, sophistication, novelty | Mystery, moodiness, excess |
| Pink | Femininity, warmth, care, modern energy (neon) | Immaturity, weakness |
| Brown | Ruggedness, earthiness, stability | Dullness, heaviness |
| Black | Luxury, power, elegance, modernity | Death, mourning, heaviness |
| White | Purity, cleanliness, simplicity | Emptiness, sterility, death (parts of Asia) |

**Scientific basis:** Red creates heightened physiological stimulation — elevated heart rate, muscle tension, memory formation (Jacobs 1974, Cooler 1981). HubSpot study: red CTA buttons outperformed green by 21% in click-through rate.

### Saturation × Brightness Rules

These matter MORE than hue for emotional tone:

| Combination | Feeling | Use Case |
|---|---|---|
| High brightness + low saturation | Soft, calm, open | Beauty, wellness, insurance, baby products, pastel brands |
| Low brightness + high saturation | Strong, hard, intense | Sports, gaming, urgency, nightlife |
| Weak contrast + weak saturation | Calm, trustworthy | Finance, healthcare, professional services |
| Strong contrast + strong saturation | Active, energetic, attention | Sales, fitness, action-oriented CTAs |

## CULTURE & DEMOGRAPHICS

- Research the target audience's cultural context before finalizing a palette.
- Red = love (West), wrath/anger (Japan). White = purity (West), death (parts of Asia).
- Women on average prefer softer, pastel palettes. Men on average prefer bolder, more saturated colors. These are statistical tendencies, not absolutes.
- Age affects color response: younger audiences tolerate higher saturation and contrast; older audiences prefer legibility and softer tones.
- Always verify: who is the CUSTOMER, not what the stakeholder personally likes. Re-align to audience perspective throughout the process.

## COLOR HARMONY

Use the color wheel to select combinations. Start with a base color derived from psychology/brand research, then apply a harmony formula.

| Harmony | How | Effect | Best For |
|---|---|---|---|
| Monochromatic | Tints, tones, shades of ONE hue | Cohesive, smooth, relaxing | Product-focused designs, editorial, luxury, digital art |
| Complementary | Two colors directly opposite on wheel | High contrast, striking, attention-grabbing | CTAs, posters, competitive differentiation |
| Analogous | 3-5 neighboring colors on wheel | Natural, harmonious, comfortable | Nature brands, organic products, editorial |
| Triadic | 3 colors equally spaced (triangle) | Varied, vibrant, balanced contrast | Charts, infographics, playful brands |
| Tetradic | 2 complementary pairs (rectangle) | Maximum variety, rich | Complex designs with many elements |
| Split Complementary | Base + 2 colors adjacent to its complement | Contrast with less tension than full complementary | Designs needing contrast without jarring effect |

**When stuck:** Use monochromatic. It always works. Extract colors from the product itself or from nature photography that matches the desired mood.

### HSL Properties

- **Hue:** The color itself (position on wheel). Change hue to shift identity.
- **Saturation:** Vividness. 100% = pure color. 0% = gray. Desaturation = calm. High saturation = energy.
- **Lightness:** Dark-to-light. Adding white = tint (softer). Adding black = shade (deeper). Adding both = tone (muted).
- **Lightness contrast is the primary driver of text readability.** Test readability by converting to grayscale — if text disappears, the lightness contrast is insufficient regardless of hue difference.

## BRAND COLOR STRATEGY

### Color Weight in Identity

Not every brand needs a signature color. Assess where color sits in the identity system:

| Identity Weight | Example Brands | Color Role |
|---|---|---|
| Color-dominant | Tiffany's, Coca-Cola, UPS, FedEx | Color IS the recognition signal |
| Color-supporting | Google, Microsoft, Snapchat | Color differentiates in a crowded field |
| Color-neutral | Apple, Nike | Other assets carry weight (product, photography, typography) |

### Competitive Landscape

- Audit competitors' palettes before choosing. In crowded fields (tech = blue, finance = blue/green), color overlap is inevitable.
- Overlap is not fatal — blue Twitter and blue Facebook are distinguished by other identity elements.
- Shift within a hue family to create distinction (purplish-blue vs greenish-blue).
- Consider being the outlier (Snapchat yellow in a sea of blue social apps) only if the brand can support that boldness.

### Client Bias Handling

- Stakeholders default to playing it safe or choosing personal favorites. Both are traps.
- Challenge: "You might not like green, but let's talk about your CUSTOMERS. What do they engage with?"
- Always reconnect color choices to the target audience, not internal preference.
- Question color equity: does the existing palette have real recognition value, or is staying close just comfort?

## FUNCTIONAL COLOR MAPPING

After selecting a palette, assign each color a JOB. Colors are a team with roles:

| Role | Purpose | Typical Use |
|---|---|---|
| Action | Drives user behavior | CTA buttons, primary links, interactive highlights |
| Communicator | Delivers key information with clarity | Headlines, key text, high-contrast labels |
| Support | Guides visual flow without stealing focus | Section transitions, secondary UI, dividers |
| Neutral | Provides breathing room | Backgrounds, whitespace areas, container fills |
| Anchor/Stabilizer | Ties sections together structurally | Borders, icons, subtle dividers, metadata text |

### Visual Rhythm

Build pacing through color: **tension → release → repeat.**
- Lead with action color at focal points (hero CTA)
- Transition through support color (feature sections)
- Reset with neutral (visual rest)
- End with action color again (closing CTA)

This creates a deliberate experience even on static layouts.

### Cross-Platform Testing (Color Map Matrix)

Test each color role across outputs before committing:

| | Digital (RGB) | Print (CMYK) | Social/Mobile |
|---|---|---|---|
| Action | ✓ Check vibrancy | ✓ Adjust for CMYK dulling | ✓ Check at small sizes |
| Communicator | ✓ Contrast ratio | ✓ Ink density | ✓ Readability on feeds |
| Support | ✓ Subtlety holds | ✓ Doesn't vanish | ✓ Doesn't blend on mobile |
| Neutral | ✓ Breathing room | ✓ Paper stock influence | ✓ Scales cleanly |
| Anchor | ✓ Subtle but visible | ✓ Holds in flat print | ✓ Not muddy in motion |

Accessibility checks: AAA contrast compliance, black-and-white preview, color blindness simulation (protanopia, deuteranopia, tritanopia). Verify on mobile at actual viewport sizes.

## TOOLS

- **Adobe Color** (color.adobe.com): Explore by keyword, generate harmonies, extract from images.
- **Sessions College Color Calculator**: Cycle through harmony schemes from a base color.
- **Paletton**: Advanced harmony explorer with real-world previews (web, animation).
- **Pigment**: Quick brightness/saturation control with Pantone codes and gradient/duotone generation.
- **Nature photography**: Extract palettes from images that evoke the desired mood. Nature is the ultimate source of proven color combinations.

## OUTPUT SHAPE

**Palette selection:** Audience context → emotional target → base color (with psychology rationale) → harmony formula applied → functional roles assigned → accessibility verified.

**Color audit:** Current palette assessment → psychology alignment check → harmony evaluation → functional role mapping → accessibility gaps → cross-platform issues → recommended fixes.

**Implementation handoff:** CSS custom properties / design tokens → role-to-token mapping → light/dark mode variants → contrast verification results.

## NON-NEGOTIABLE CHECKLIST

1. Every color in the palette has a named functional role (action, communicator, support, neutral, anchor).
2. Base color choice is justified by audience psychology, not personal taste.
3. Cultural and demographic context has been considered.
4. Lightness contrast is sufficient for all text elements (verify in grayscale).
5. Palette has been tested for color blindness accessibility.
6. Saturation and brightness are deliberately chosen to match emotional target.
7. Cross-platform behavior is accounted for (RGB, CMYK, mobile).
8. Color weight in the overall identity system is assessed — color may not be the primary carrier.
