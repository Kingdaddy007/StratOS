# Interface Operation Playbook

Use this reference only for a direct named UI operation that needs more than the normal UI/UX contract. Select the relevant section; do not run the whole document as a ceremony.

## Shape, Teach, Document, and Extract

- Start from observable product facts: audience, job, environment, constraints, content, primary journey, and failure/recovery path. Ask only the questions that materially change the design.
- Produce a brief that names the register, user goal, hierarchy, key states, anti-goals, constraints, and success evidence. A single task statement may be enough for a small change.
- Before documenting or extracting a system, discover what already governs: existing tokens, components, type scale, color roles, layout primitives, and stated product decisions.
- Record only evidence-backed reusable decisions. Label uncertainty and avoid creating a second source of truth beside the project’s existing design system.
- Extract a component or token only after it has at least two real uses and a stable responsibility. Preserve a local one-off when abstraction would obscure the intent.

## Audit and Critique

- Inspect the implemented critical journey where possible. Separate observed defects from inference, and name the viewport, state, device/input method, and evidence source.
- Check applicable accessibility, state visibility, content hierarchy, responsive behavior, error/recovery, theming, loading behavior, and generic-pattern risks. Do not replace evidence with a cosmetic score.
- Classify findings by `critical`, `high`, `medium`, `low`, or `info`; record urgency and confidence separately when they matter.
- Look for repeated causes before proposing individual fixes. A browser issue, a missing state, and a token mismatch may share one component boundary or design-system cause.
- Recommend the smallest safe correction first. A review does not authorize implementation, deployment, or a broad redesign.

## Clarify, Layout, Typeset, and Colorize

- Make the next action, current state, consequence, and recovery path understandable before adding visual treatment.
- For labels, instructions, errors, empty states, confirmations, loading states, and navigation, use the user’s language where it is available. Never invent user research or proof.
- Correct structure before decoration: reading order, grouping, alignment, visual weight, whitespace, responsive composition, and content priority.
- Use typography to establish hierarchy and legibility across realistic content length and viewports. Do not pick a font or scale by trend alone.
- Give colour a role: semantic state, hierarchy, grouping, or brand expression. Verify contrast in default, focus, selected, disabled, error, and busy states that apply.

## Adapt and Harden

- Test the actual constraints that can break the surface: narrow/wide layouts, zoom, keyboard order, touch targets, long text, localization, missing content, delayed data, errors, permissions, offline behavior, and destructive recovery when relevant.
- Preserve meaning and primary actions during reflow. Do not treat a desktop screenshot as a responsive design.
- Route authorization, data exposure, server-side validation, and input-boundary issues to the relevant security or engineering capability. Keep UI work focused on visible status and safe recovery.

## Distill, Quieten, Bolden, Delight, Polish, and Overdrive

- Name the observed problem before changing the register: weak hierarchy, excessive density, unclear emphasis, empty feedback, or a specific moment that needs recognition.
- Distill by removing or regrouping content, choices, decoration, or motion that does not help the critical journey. Preserve necessary information, accessible names, and recovery controls.
- Increase or reduce visual weight through hierarchy, spacing, composition, contrast, and restrained motion. Do not use spectacle to hide a missing product decision.
- Add delight only when it supports feedback, momentum, recognition, or brand fit. It must not block completion, exclude reduced-motion users, or undermine serious contexts.
- Treat convention-breaking as a proposed, reversible experiment. State the user benefit, constraints, fallback, and evidence needed before applying it.
- Finish with alignment, state completeness, content quality, responsive behavior, performance, and removal of temporary artefacts. “Polish” is not permission for unrelated redesign.

## Live and Optimize

- Use a browser or local preview only when available. Inspect a bounded change, identify the actual source, and make edits through the normal project path. Never assume an element-selection, hot-reload, or variant-generation service exists.
- Measure performance before optimisation. Distinguish network, rendering, image/media, animation, and interaction delay; route system-level causes to the performance capability.
- Retain UI responsibility for perceived responsiveness: visible progress, stable layout, understandable pending/error states, and interaction continuity.

## Completion Check

- The requested operation solved an observed problem, not a generic aesthetic rule.
- Relevant accessibility, responsive, state, and performance implications were checked proportionately.
- The result identifies evidence, assumptions, and unverified surfaces.
- No operation triggered unrelated implementation, external work, or a mandatory follow-on chain.
