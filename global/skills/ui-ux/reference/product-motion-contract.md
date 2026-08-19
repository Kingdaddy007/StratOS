# Product Motion Contract

Load this reference only when a product or brand interface needs purposeful motion. Use `cinematic-motion` only when approved spatial, media-led, scroll-driven, canvas, WebGL, or other cinematic treatment is genuinely required.

## Define The Contract Before The Effect

Write the motion decision as:

```text
purpose -> trigger -> affected state/property -> duration/easing -> interruption behaviour
-> existing primitive or justified technique -> reduced-motion behaviour
-> input/device verification -> layout/performance evidence
```

1. Name one user-facing purpose: feedback, continuity, hierarchy, progress, orientation, or meaningful state change.
2. Name the trigger and the state transition. Explain what the user should understand before, during, and after the motion.
3. Define what happens if the user acts again, navigates away, data changes, or the transition is interrupted. Required actions must remain available; motion must not conceal, delay, or replace the result.
4. Use existing project motion primitives, tokens, and component patterns before adding a dependency. Prefer the simplest technique that preserves meaning and layout stability.
5. Define a reduced-motion behaviour that preserves the information or feedback without unnecessary travel, flashing, or continuous motion.

## Choose A Proportionate Technique

- Use a simple CSS transition or the existing component primitive for state feedback, disclosure, focus, hover, and ordinary layout changes.
- Use a richer implementation only when the communication job cannot be met with the existing primitive and its maintenance, loading, and fallback costs are explicit.
- Avoid casual animation of layout-driving properties. Keep expensive visual effects bounded, verify them in the target interface, and remove them when they reduce clarity or responsiveness.
- Keep product motion distinct from spatial spectacle. A strong product interface may appropriately use no motion at all.

## Verify Interaction, Not Just Appearance

Check the normal, repeated, interrupted, and failure paths. Verify pointer, keyboard, and touch behaviour; narrow and wide layouts; focus order; reduced-motion behaviour; stable layout; and relevant loading or error states.

Record whether the motion was retained, simplified, or removed, the reason, and the evidence. Escalate to `cinematic-motion` only after the product-motion contract shows that a spatial or media-led treatment is necessary.
