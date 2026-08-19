---
id: os-maintenance
version: 1
status: active
intent: Safely add or reform Anti-Gravity rules, skills, workflows, references, and harness contracts.
use_when: [maintaining Anti-Gravity OS, adding a skill or workflow, changing rule or dispatch behavior]
do_not_use_when: [ordinary project feature work, application debugging]
inputs: [requested OS change, affected surfaces, compatibility constraints]
required_resources: [applicable AGENTS.md files, current rule files, referenced skills and workflows]
mutation_class: local_edit
approval_gates: [confirm scope before changing multiple OS surfaces, approve any external publication separately]
states: [inventory, impact-map, propose, approve, implement, validate, handoff]
outputs: [change set, compatibility notes, validation evidence, migration notes]
verification: [schema checks, reference checks, unresolved-token scan, targeted behavior trace, git diff check]
failure_paths: [stop on contract conflict, preserve existing files on incomplete migration, report unresolved references]
resume_contract: task-scoped .agents/workflows/os-maintenance.json using the workflows directory contract
next_workflows: [test-strategy, none]
profiles: [general]
---

# WORKFLOW: OS MAINTENANCE

## Modes

- **Audit:** read-only inventory and findings.
- **Propose:** produce an impact map and patch plan without editing.
- **Implement:** edit only the approved OS surfaces.

## Sequence

1. Traverse applicable `AGENTS.md` contracts and inventory every affected rule, skill, workflow, template, script, and installer.
2. Map consumers and compatibility risks before changing a canonical contract.
3. State the intended behavior, non-goals, migration path, and verification plan.
4. Obtain approval if the requested scope materially expands or affects publication/install state.
5. Make the smallest coherent change; never maintain duplicate canonical sources.
6. Validate schema, references, dispatch behavior, state transitions, and representative dry-run requests.
7. Deliver files changed, evidence, residual risks, and any required downstream work.
