---
name: ui-ux
description: 'Design, audit, or implement usable frontend experiences for applications, SaaS products, dashboards, marketing sites, and optional spatial-brand surfaces. Use when a task involves user flows, information architecture, components, interaction states, forms, navigation, responsive behavior, accessibility, UX writing, visual hierarchy, or interface verification. Load spatial references only when the active profile or request is explicitly interior, showroom, gallery, furniture, decor, staging, luxury-home, or architecture-adjacent. Do not use for backend-only, API-only, database-only, or infrastructure-only work.'
---

# UI/UX and Design Thinking

## Operating Contract

Design for the user's task before choosing visual treatment. Detect the interface register first:

- `product`: applications, SaaS, dashboards, tools, settings, and transactional flows.
- `brand`: marketing, editorial, campaign, and conversion surfaces.
- `spatial`: interior, showroom, gallery, furniture, decor, staging, luxury-home, and architecture-adjacent experiences.

The spatial register extends this general contract; it does not replace usability, accessibility, responsive behavior, or state coverage.

## Never Do

- Start from a component trend before identifying the user goal and information hierarchy.
- Design only the happy path; include empty, loading, error, success, disabled, permission, offline, and destructive states when relevant.
- Hide required actions behind spectacle, hover-only controls, ambiguous icons, or low-contrast text.
- Treat a desktop screenshot as a responsive specification.
- Add motion without purpose, reduced-motion behavior, and performance consideration.
- Assume a spatial or luxury visual register for a generic product interface.
- Change backend contracts, authorization, or business rules from a UI task without the corresponding authority and domain skill.

## Workflow

### 1. Ground the interface

- Identify the users, jobs, frequency, environment, constraints, and success signal.
- Read active project context, `PRODUCT.md`, and `DESIGN.md` when they exist.
- Name the register: product, brand, or spatial.

### 2. Map structure and flow

- Define entry points, navigation, information hierarchy, primary action, secondary actions, and exit/recovery paths.
- Trace the critical journey from intent through confirmation.
- Reduce steps only when clarity, safety, and reversibility remain intact.

### 3. Specify the state matrix

For every interactive component or screen, cover the observable states that can occur. Include validation timing, retry behavior, permissions, destructive confirmation, and recovery.

### 4. Establish interaction and visual rules

- Reuse the active design system before introducing new tokens or components.
- Make focus, hover, pressed, selected, disabled, busy, and error states distinguishable.
- Use typography, spacing, color, and motion to clarify hierarchy rather than decorate uncertainty.

### 5. Design responsively and accessibly

- Define reflow, content priority, touch targets, keyboard order, focus management, labels, landmarks, contrast, zoom behavior, and reduced motion.
- Verify that truncation, localization, long content, and narrow viewports do not hide meaning or actions.

### 6. Verify observable behavior

- Inspect the interface in a browser when implementation exists.
- Capture viewport evidence, keyboard traversal, reduced-motion behavior, console/network errors, and applicable accessibility results.
- Record anything that remains unverified.

## Conditional Reference Loading

- Load [product.md](reference/product.md) for applications, SaaS, dashboards, and product workflows.
- Load [brand.md](reference/brand.md) for brand, editorial, campaign, or conversion surfaces.
- Load [interaction-design.md](reference/interaction-design.md) for complex controls, feedback, or state transitions.
- Load [cognitive-load.md](reference/cognitive-load.md) when density, decisions, or progressive disclosure are difficult.
- Load [heuristics-scoring.md](reference/heuristics-scoring.md) and [personas.md](reference/personas.md) for structured audits.
- Load [responsive-design.md](reference/responsive-design.md) for layout adaptation and breakpoint behavior.
- Load [color-and-contrast.md](reference/color-and-contrast.md) when colour is selected, changed, tokenised, audited, or verified. It owns semantic roles, actual pairing/state checks, and rendered review. Load [color-evidence-and-context.md](reference/color-evidence-and-context.md) only when a brand, cultural, psychology, print, data, spatial, cinematic, or experiment claim materially affects the colour decision. Load [typography.md](reference/typography.md) and [ux-writing.md](reference/ux-writing.md) only for those concerns.
- Load [product-motion-contract.md](reference/product-motion-contract.md) when designing or implementing product or brand-interface motion. Use it to define purpose, trigger, interruption, reduced-motion behaviour, and input/device verification before choosing detailed motion techniques.
- Load [motion-design.md](reference/motion-design.md) when motion materially supports feedback, continuity, or hierarchy and the task needs timing, easing, material, or performance detail.
- Load [ui-implementation-handoff.md](reference/ui-implementation-handoff.md) when authorised work changes interface code. Use it to map interface state to its data/failure boundary, select project-native checks, and deliver changed artefacts with honest evidence.
- Load [operation-routing.md](reference/operation-routing.md) when a request uses a named UI operation such as audit, critique, polish, bolder, quieter, distill, adapt, layout, typeset, colorize, or clarify. Treat it as a direct task mode, not a workflow; load only the matching domain references.
- Load [interface-operation-playbook.md](reference/interface-operation-playbook.md) only when a named UI operation needs a detailed procedure beyond the routed domain reference. Use its checks proportionately; it is not a compulsory ceremony.
- For the spatial profile, load [spatial-ui-system.md](reference/spatial-ui-system.md), [spatial-design.md](reference/spatial-design.md), [spatial-ui-patterns.md](reference/spatial-ui-patterns.md), and [inquiry-and-gallery-states.md](reference/inquiry-and-gallery-states.md).
- Load [design-bans.md](reference/design-bans.md) during critique to detect generic AI-pattern output without turning its examples into rigid universal law.

## Output Contract

Provide:

1. Interface register and user goal.
2. Information architecture or flow.
3. Component and state inventory.
4. Interaction, accessibility, and responsive requirements.
5. Implementation or design changes within authorized scope.
6. Verification evidence and remaining risks.

## Completion Gate

- The primary user journey is understandable and recoverable.
- Important states and failure paths are specified or implemented.
- Keyboard, focus, labels, contrast, reduced motion, and responsive behavior are verified proportionately.
- Visual treatment matches the detected register and active profile.
- No unverified claim is presented as tested behavior.
