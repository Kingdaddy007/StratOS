# UI Implementation And Handoff

Load this reference only when authorised work changes interface code. Do not load it for a design proposal, a copy-only task, or an unimplemented visual critique.

## Ground The Change

1. Read the nearest project contract, active context, user goal, critical journey, and existing design system.
2. State the approved interface scope and non-goals. Route API, authorisation, data-model, dependency, and production changes to their proper capability and approval boundary.
3. Map each changed component's responsibility and its **data and failure boundary**:
   - what data or action it represents;
   - which loading, empty, success, error, permission, offline, destructive, or recovery state can reach it;
   - how the user sees the state, retries safely, or recovers; and
   - what must remain true if the network, data, or action fails.

Do not let an interface imply success, permission, completion, or saved data before the responsible project layer can support that claim.

## Implement Deliberately

- Reuse existing components, tokens, interaction patterns, and project primitives before creating a new abstraction.
- Keep semantic structure, visible labels, keyboard behaviour, focus management, responsive rules, and error/recovery states alongside the changed interaction.
- Build in small verifiable increments. Preserve unrelated behaviour and existing design-system contracts.
- Escalate a changed interface contract, authorisation rule, or data boundary instead of silently compensating for it in presentation code.

## Verify The Actual Change

- Run the applicable project-native checks: tests, type checks, lint, build, or the configured equivalent. Select checks that exercise the changed claim; do not report a generic green result as proof of every surface.
- Inspect the critical journey in a browser when a runnable interface exists. Check the changed state at relevant viewports, keyboard traversal, focus, touch behaviour, reduced motion, console/network errors, and realistic loading or failure behaviour.
- Record checks that could not run, the environment limitation, and the residual risk. A design review does not become implementation verification without executed evidence.

## Deliver A Useful Handoff

Return:

```text
Changed artefacts:
User journey and states covered:
Project-native checks executed and result:
Browser evidence and environments inspected:
Unverified surfaces and why:
Residual risks, dependencies, and next smallest action:
```

Do not claim completion until the primary journey works within the authorised scope and important applicable failure states remain understandable and recoverable.
