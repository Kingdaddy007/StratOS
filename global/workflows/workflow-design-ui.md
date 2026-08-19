---
id: design-ui
version: 2
status: active
intent: Coordinate a proportionate general-interface design effort, record the design decision, and hand off only the work that is actually needed.
use_when: [a product, application, dashboard, service, or brand surface needs a new or materially revised interface flow, hierarchy, state model, or design decision]
do_not_use_when: [the request is a bounded visual adjustment, a backend-only change, spatial-profile direction, or local interface implementation with an already-approved design contract]
inputs: [user objective, active workspace facts, existing design system or product requirements, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, skills/ui-ux/SKILL.md, active project contexts when they exist]
mutation_class: local_edit
approval_gates: [diagnose and propose remain read_only; confirm before creating or replacing durable project design artifacts, widening scope, installing dependencies, or taking an external action]
states: [intake, ground, map-flow, specify, review, handoff, deliver]
outputs: [interface decision, flow and state contract, component boundary notes, implementation handoff when requested, evidence, residual risks]
verification: [check the critical journey, applicable states, accessibility and responsive requirements, and existing implementation evidence when available]
failure_paths: [stop and request the missing product decision when it materially changes the interface; preserve existing behavior; report unverified surfaces and a safe next action]
resume_contract: task-scoped .agents/workflows/<task-id>.json using the workflows directory contract
next_workflows: [verify-project, none]
profiles: [general]
---

# Workflow: Design UI

## Authority

Use this for a coordinated design decision, not every visual request. Diagnosis and proposal are read-only. Create or replace a durable project artifact only with the requested local-edit authority. This workflow never grants implementation, dependency, security, or production authority.

## Procedure

1. Ground the task in the user goal, existing product facts, technical constraints, and detected interface register: `product` or `brand`. Route spatial work to the spatial profile.
2. Map the critical journey: entry point, information hierarchy, primary and secondary actions, confirmation, recovery, and exit paths.
3. Specify only the states that can occur: loading, empty, error, success, disabled, permission, offline, destructive, and recovery states when applicable.
4. Reuse the active design system. Define component responsibilities, content hierarchy, responsive behavior, accessibility requirements, and any evidence needed to judge the result.
5. Review the proposal against the critical journey and applicable UI/UX references. Inspect an existing implementation where that is possible; identify evidence that remains unavailable.
6. Hand off to direct `ui-ux` work with `coding` only when the interface is approved and local implementation is requested. Load the UI/UX motion reference only when motion has a named user-facing job and reduced-motion verification is part of the scope.

## Boundaries

- A small layout, wording, color, typography, responsiveness, or refinement request is a direct UI/UX operation. Load `skills/ui-ux/reference/operation-routing.md`; do not create workflow state.
- Do not require a mockup, a full design system, a new context file, or a visual exploration phase for a small reversible change.
- Do not make browser inspection, animation, or a separate audit mandatory when no implementation or proportionate risk exists.
- Do not force a framework, font, motion library, or visual style.

## Completion Gate

Deliver the user goal, register, flow or hierarchy, applicable state requirements, handoff boundary, evidence, and remaining uncertainty. Do not claim an implementation was verified when only a proposal exists.
