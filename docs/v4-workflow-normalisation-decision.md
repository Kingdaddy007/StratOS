# V4 workflow normalisation decision

## Decision

Keep a workflow only when it coordinates a meaningful stateful job: it must have a decision boundary, a real handoff or approval gate, and evidence that matters beyond one local operation. A workflow is not a synonym for a useful command.

A skill supplies judgement. A recipe supplies a bounded technique. An agent selects and combines both. A workflow coordinates work whose order, authority, state, or evidence must be visible across the task.

## Current inventory

The baseline registry had 52 workflows:

- 42 General
- 8 Spatial
- 1 Growth
- 1 Media

23 use the `impeccable-*` name. Twenty-one General entries share a generic state envelope despite representing distinct design operations. Their content may be useful; their workflow classification is not.

## Target public coordination routes

These are the workflows that remain public, stateful coordination routes after migration:

| Route | Why it remains a workflow |
| --- | --- |
| Project inception | Establishes project truth and the next reversible decision. |
| Architecture decision | Compares consequential structural choices and records the decision. |
| Build feature | Coordinates approved implementation, evidence, and handoff. |
| Debug issue | Separates diagnosis, authorised repair, and residual uncertainty. |
| Incident response | Coordinates mitigation, recovery, and learning under pressure. |
| Database migration | Requires compatibility, rollback, and execution approval. |
| Dependency upgrade | Requires impact assessment, verification, and rollback evidence. |
| Security audit | Maintains a distinct assurance boundary and escalation path. |
| Ship to production | Is an external hard gate, never a routine local command. |
| OS maintenance | Coordinates safe changes to the operating system itself. |
| Task dispatch | Exists only for genuinely independent delegated work. |
| Commercial decision record | Makes material offer, scope, claim, or price decisions inspectable before a human commitment. |
| Live learning loop | Gates an approved, reversible live intervention, its guardrails, and honest interpretation. |
| Spatial project | Coordinates the specialist spatial path and its explicit gates. |
| Media production plan | Replaces the current broad `video-generation` workflow only for multi-shot, provider-dependent work with asset, cost, rights, or delivery gates. |

`video-generation` remains a skill. A normal request for a video concept or prompt uses that skill directly; it does not start a workflow.

## Move out of the workflow registry

The following are direct capabilities, recipes, or phases selected by the owning agent. They will not remain public workflows after their content and links are migrated.

| Current entries | Destination |
| --- | --- |
| `context-hygiene`, `review-code`, `test-strategy`, `verify-project`, `refactor-module`, `optimize-performance` | Existing assurance, testing, debugging, refactoring, performance, and context capabilities. Use an agent's risk-sized procedure; do not create workflow state for ordinary use. |
| `design-api`, `design-ui`, `ui-craft`, `ui-animate` | Systems Architect and Design Director capabilities, using the relevant skills and approved project context. |
| `marketing-copy` | Growth-pack capability selection. Direct copy work stays direct; a consequential product or offer returns to Project Inception. |
| `reference-intelligence`, `visual-brainstorm`, `spatial-concept`, `storytelling`, `spatial-design-ui` | Conditional phases and recipes within the Spatial Project workflow. They remain available only when the task calls for them. |
| `impeccable-craft`, `impeccable-animate` | Spatial implementation and motion procedures within the Spatial Project workflow. |
| `impeccable-adapt`, `impeccable-audit`, `impeccable-bolder`, `impeccable-clarify`, `impeccable-colorize`, `impeccable-critique`, `impeccable-delight`, `impeccable-distill`, `impeccable-document`, `impeccable-extract`, `impeccable-harden`, `impeccable-layout`, `impeccable-live`, `impeccable-onboard`, `impeccable-optimize`, `impeccable-overdrive`, `impeccable-polish`, `impeccable-quieter`, `impeccable-shape`, `impeccable-teach`, `impeccable-typeset` | A selectively loaded UI operation library under the appropriate Design capability. Preserve useful technique; remove fake workflow state, command chains, automatic file writes, score theatre, and deployment implications. |

## Migration safeguards

1. Preserve useful content before removing any workflow entry.
2. Do not require a state file for a recipe or an ordinary review/design request.
3. Remove stale command chains, machine-local file assumptions, and automatic follow-on actions.
4. Rewrite references so a user can still ask for “make it bolder,” “improve the layout,” or “review the UI”; the Design or Assurance agent chooses the smallest relevant procedure.
5. Keep no duplicate editable source. The manifest, workflow catalogue, routing fixtures, and generated host payloads must agree.
6. Regression-test that routine prompt, review, UI, and copy requests do not route into workflow state; multi-stage projects and external/destructive actions still do.

## Migration order

1. Extract and index useful Impeccable material as Design/Spatial operation references.
2. Replace the 23 Impeccable workflow registrations and cross-links with the operation library.
3. Fold the direct capability entries into their owning agents and skills.
4. Narrow `video-generation` to direct skill usage and introduce `media-production-plan` only where the coordination criteria are met.
5. Rebuild the manifest, routing fixtures, host adapters, and documentation; then run full validation.

No workflow content is discarded by this decision. The implementation changes its loading location and authority model, not its value by name alone.

## Implemented structural step — 2026-08-19

The first migration removes only the 21 General `impeccable-*` wrappers. They shared a generic state envelope but represented direct operations such as audit, polish, layout, type, responsive adaptation, and clarity. At that structural step, the active registry was 31 workflows and its source-file count matched it.

- Their useful, portable judgement is retained as `skills/ui-ux/reference/operation-routing.md` and `interface-operation-playbook.md`; the former entries no longer create task state or automatic command chains.
- The exact former source remains recoverable in version control, in line with the repository policy against tracked backup copies.
- `workflow-design-ui.md` remains, rewritten as a proportionate Design UI coordination route. `workflow-ui-craft.md` and `workflow-ui-animate.md` were later reclassified as direct `ui-ux` operations after their owning skill and regression checks were confirmed; they no longer create task state.
- Spatial, Growth, Media, Assurance, and Engineering workflow classification remains pending the corresponding evidence and capability decisions. This migration does not claim that the 31-route interim registry is the final V4 target.

Subsequent Growth evidence added two narrow conditional routes: `commercial-decision-record` and `live-learning-loop`, bringing the interim count to 32. The first General direct-route migration then retired `design-api`, `optimize-performance`, `refactor-module`, `review-code`, `ui-craft`, `ui-animate`, and `context-hygiene` after preserving their active skills and repairing the context-hygiene authority boundary. This produced the historical 25-route snapshot. The later Phase-7 migration then reclassified seven Spatial direct/phase wrappers and the one Media `video-generation` wrapper, producing the live 17-route manifest. See `docs/v4-phase-7-workflow-truth-audit.md` for the exact destinations. Neither change reopens the retired `impeccable-*` wrappers or makes routine work stateful.
