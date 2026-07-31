# StratOS Glossary

| Term | Plain-language meaning | Where it lives |
| --- | --- | --- |
| Adapter | A small translation layer that changes filenames, metadata, and capability names for one host. It does not duplicate the canonical instructions. | `global/adapters/` |
| Baseline | A stable rule or safety reference shared across projects, such as authority, engineering, context integrity, or source verification. It is policy, not project facts. | `global/baselines/` |
| CI | Continuous integration: an automated clean-machine check that validates, builds, and tests the repository on supported operating systems. | `.github/workflows/` |
| Context template | A blank form for recording project facts. Copy and fill it into `.agents/contexts/`; the template itself is not truth. | `global/context_templates/` |
| Design audit | A structured review of interface or spatial experience quality. It produces findings and recommendations; it does not grant implementation authority. | `global/design-audit/` |
| Distribution / payload | Generated files for one host, ready to install. Regenerate them from `global/` instead of editing them directly. | `dist/<host>/` |
| Hook | An optional host lifecycle callback used for checks or notifications. This repository does not currently install a background hook; any future hook must obey the same authority and approval rules. | host adapter/runtime configuration |
| Manifest | The registry that tells the compiler which skills, workflows, profiles, templates, and baselines exist. Think of it as the table of contents for the OS. | `global/manifest.yaml` |
| Mutation class | A risk label: `read_only`, `local_edit`, `dependency_or_network`, `destructive`, or `external_or_production`. The label determines the approval gate. | workflow metadata and schemas |
| Profile | A filter for a domain. `general` is the default; `spatial` enables interior, showroom, gallery, and architecture-adjacent guidance. | `global/profiles/` |
| Reference | Detailed or dated material loaded only when a skill’s rules say it is relevant. | `global/skills/*/references/` |
| Schema | A machine-checkable shape for manifests, skills, workflows, and state records. It catches missing fields before installation. | `global/schemas/` |
| Skill | A specialist instruction package invoked for a capability, with activation rules, boundaries, output shape, and optional references. | `global/skills/` |
| Workflow | A repeatable sequence for a type of task, including states, evidence, failure paths, and approvals. | `global/workflows/` |
| Workflow state | A task-specific JSON record used to resume work without one task overwriting another. | `.agents/workflows/<task-id>.json` |
| WSPI | “Workflow state and process integrity”: the repository’s term for validating that workflow states, approvals, and resume records remain coherent. It is a check, not a separate AI service. | workflow schemas and validators |

## How the pieces connect

The manifest points to canonical skills and workflows. The compiler reads that registry, validates the contracts, and emits a host payload. The host reads its generated instruction file (`AGENTS.md` for Codex), then the router selects a workflow and skill at runtime. Project context is loaded only from the active project’s `.agents/contexts/` files.
