# Workflows

`global/workflows/` is the single canonical workflow source. Each active workflow declares portable metadata, task-scoped state, mutation authority, approval gates, outputs, evidence, failure behavior, and routing profiles. See `AGENTS.md` for the enforced contract.

The Studio Director selects these routes privately from task shape. Users may name a workflow, but they do not need to know or invoke workflow vocabulary for the correct route to activate. Small coherent work remains direct.

## Core Routing

| Intent | Workflow |
| --- | --- |
| Start a general product, service, tool, or application | `workflow-project-inception.md` |
| Start a complete high-end interior or spatial storytelling site | `workflow-spatial-project-inception.md` |
| Build a feature | `workflow-build-feature.md` |
| Diagnose or fix a defect | `workflow-debug-issue.md` |
| Respond to an active production incident | `workflow-incident-response.md` |
| Plan architecture | `workflow-plan-architecture.md` |
| Design a bounded API contract | Direct `api-design`; use `workflow-plan-architecture.md` for a material cross-system decision |
| Design general product UI | `workflow-design-ui.md` |
| Refine a bounded general UI concern | Direct `ui-ux` operation routing |
| Analyse references, develop a concept/story, design a bounded spatial surface, or plan approved motion | Direct Spatial skill work; use `spatial-experience-design/reference/project-phase-routing.md` |
| Review, refactor, or optimize | Direct `review-audit`, `refactoring`, or `performance` |
| Audit a material security boundary | `workflow-security-audit.md` |
| Plan tests or verify a project | `workflow-test-strategy.md`, `workflow-verify-project.md` |
| Migrate data or upgrade dependencies | `workflow-database-migration.md`, `workflow-dependency-upgrade.md` |
| Plan an AI-generated video | Direct `video-generation` skill |
| Prepare a material paid offer, proposal, scope, price, or claim decision | `workflow-commercial-decision-record.md` |
| Run an approved reversible live-learning intervention | `workflow-live-learning-loop.md` |
| Ship to production | `workflow-ship-to-production.md` |
| Maintain Anti-Gravity OS | `workflow-os-maintenance.md` |
| Dispatch independent work | `workflow-task-dispatch.md` |

## Spatial Profile

The one stateful Spatial coordination path is `workflow-spatial-project-inception.md`. Inside it, use the specialist skills directly for reference intelligence, territory generation, concept selection, story, UI/vertical-slice work, approved production slices, and approved motion. [Spatial Project Phase Routing](../skills/spatial-experience-design/reference/project-phase-routing.md) preserves the entry gates, escalation points, and return conditions for each phase.

General product UI begins with `workflow-design-ui.md` only when a coordinated design decision is needed. Approved implementation and purposeful motion use direct `ui-ux` work with the matching UI/UX references. Bounded UI operations never create workflow state.

Spatial implementation remains blocked until the five logical contracts or approved equivalents, applicable Director gates, and vertical-slice verdict pass. Video, motion, anchor objects, generated media, and scroll storyboards are conditional. General product and UI work must not be forced through this profile.

## Authority Rule

Diagnose and propose are read-only. Workspace implementation requires requested or confirmed implement authority. Production, database, deployment, traffic, publication, or other external mutation requires a just-in-time approval naming target, action, expected effect, rollback or containment, and evidence plan.
