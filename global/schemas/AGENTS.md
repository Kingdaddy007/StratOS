# Schemas Context & Contract

## 1. Purpose

This directory defines machine-readable contracts for canonical skills, workflows, manifests, adapters, and task-scoped workflow state.

## 2. Rules & Constraints

- Schemas are versioned public interfaces.
- Additive optional fields are preferred; breaking changes require a schema-version increment and migration notes.
- Keep runtime validation implementable with Python's standard library.
- Do not embed host-specific behavior in canonical schemas.

## 3. Exposed Interfaces

- `manifest.schema.json`: canonical OS registry, profiles, resources, and agent registry.
- `agent.schema.json`: portable canonical agent contract rendered by host adapters.
- `workflow.schema.json`: active workflow metadata.
- `workflow-state.schema.json`: resumable task state, including optional dependency-aware acceptance gates for substantial work.
- `workflow-index.schema.json`: task ID to state-file registry.
- `adapter.schema.json`: host mapping contract.

## 4. Internal Dependencies

- `../manifest.yaml`: conforms to the manifest schema.
- `../workflows/`: workflow files conform to the workflow schema.
- `../adapters/`: adapter records conform to the adapter schema.

## 5. Verification

- Run `python global/scripts/os.py validate`.
