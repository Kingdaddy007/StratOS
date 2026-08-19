---
name: coding
description: 'Use when writing or changing production code, configuration with runtime behaviour, components, services, endpoints, scripts, or integrations. Activate for “build”, “implement”, “write code”, “add a feature”, “make this work”, or “change this behaviour”. Do not use for a decision-only architecture discussion (use architecture), unexplained failure diagnosis (use debugging), behavior-preserving structural work as the primary task (use refactoring), or review-only work (use review-audit).'
---

# Coding

## WHEN TO USE THIS

- Implement a new or changed observable behaviour.
- Modify an existing module, integration, configuration, or runtime boundary.
- Make a small local repair after the mechanism is already understood.

## NEVER DO

- Treat a remembered API, a generic rule, or an example as a repository fact.
- Apply fixed parameter counts, abstraction counts, test counts, or Git commands as universal laws.
- Declare success from a green command that does not exercise the changed boundary.
- Let a locally correct change cross an authorization, sensitive-data, destructive, public-contract, production, or irreversible boundary without the required approval.
- Hide a behaviour change inside a claimed mechanical refactor.

## CLASSIFY THE CHANGE BEFORE EDITING

Start with the actual consequence, reversibility, exposure, uncertainty, and change surface. Do not create ceremony for a harmless local edit.

| Risk | Typical condition | Required action |
| --- | --- | --- |
| `R0` reversible local | Documentation, isolated formatting, or no-runtime artifact | Inspect the narrow surface. Use parse, render, lint, or diff evidence when applicable. |
| `R1` low-consequence repository | Clear local pattern; small reversible implementation or configuration change | Name the changed surface and highest-risk assumption. Use focused evidence. |
| `R2` ordinary feature | User-visible behaviour, module boundary, persistence, or external call | Write the compact change brief. Select evidence for local logic and each changed boundary. Run a fresh review pass before handoff or release. |
| `R3` high-consequence | Authorization, sensitive data, public contract, migration, billing, production access, or critical journey | State recovery limits. Add negative and boundary evidence. Route to the relevant specialist and obtain required human approval before external effect. |
| `R4` irreversible or uncontrolled | Destructive production action, irrecoverable migration, credential exposure, or safety-critical effect | Do not execute. Prepare evidence, a runbook, and a decision request for a human. |

For `R2` and above, record only what the next decision needs:

```text
Objective:
Non-goals:
Changed surface and boundaries:
Highest-risk assumption:
Evidence plan:
Recovery limit and approval boundary:
```

Update the record when discovery changes the actual surface. A plan that no longer matches the diff is stale evidence.

## ESTABLISH FACTS BEFORE IMPLEMENTING

1. Read nearby implementations, consumers, tests, configuration, and directory contracts.
2. State the behaviour that must change and the behaviour that must remain unchanged.
3. When a library, external API, generated output, or repository convention is unfamiliar, verify it from current local source and authoritative documentation. Do not infer signatures from memory.
4. Identify the source of truth for generated artifacts. Change the source and regenerate deterministically where the project supports it; do not silently hand-edit generated output.
5. Make the smallest coherent change that meets the objective. Prefer a clear local solution over speculative layers.

Introduce an abstraction when a stable domain concept, expected variation, ownership boundary, or real duplication cost makes it clearer than the alternatives. Treat repeated code as a prompt to inspect the reasons for change, not as a fixed numerical threshold. Use a named parameter object only when it makes the contract and call sites clearer.

## KEEP INTENT AND BEHAVIOUR INSPECTABLE

- Label behavioural edits separately from mechanical movement, renaming, formatting, and generated output.
- Separate them by default when doing so improves review or rollback.
- Combine them only when they are inseparable for a safe repair. State the dependency and provide distinct evidence for the structural and behavioural claims.
- Preserve explicit error handling. Handle malformed input, dependency failure, timeout, partial failure, and concurrency only where the changed boundary makes them plausible; do not manufacture generic branches.
- Check sibling functions or parallel consumers when the same failure pattern may recur.

## SELECT EVIDENCE FROM THE FAILURE SURFACE

Use `testing` to select and interpret evidence. Match the evidence to what could actually be wrong:

| Changed surface | Minimum evidence to consider |
| --- | --- |
| Local pure logic | Focused behaviour or invariant test; type/static check when available. |
| Runtime configuration or integration | Parse/build/type evidence plus a focused boundary check. |
| User-visible flow | Local tests plus targeted manual or browser evidence where the user journey changes. |
| Persistence, external service, or public contract | Integration or contract evidence, failure and compatibility cases. |
| Authorization, sensitive data, destructive migration, production path | Negative and boundary evidence, recovery proof where relevant, specialist route, and required approval. |
| Legacy code with weak tests | Characterize observable current behaviour where practical; state what remains unknown and escalate if the unobservable behaviour is high consequence. |

A check proves only the claim and environment it exercised. Record unrun, flaky, mocked, or non-representative evidence honestly.

## HAND OFF A NONTRIVIAL CHANGE

For `R2` and above, or whenever another agent reviews the work, provide:

```text
Objective and non-goals:
Meaningful change surface and review base:
Behavioural claim and unchanged behaviour:
Highest-risk assumptions:
Evidence actually run, with scope and results:
Recovery limit and residual uncertainty:
Questions for the reviewer:
Decision requested:
```

Ask `review-audit` for a fresh bounded reasoning pass when the risk, handoff, or release path warrants it. A distinct Assurance agent is useful when available; its absence must not turn a reversible local edit into a blocked task.

## OUTPUT SHAPE

```text
Risk and objective:
Change and why:
Evidence actually run and what it covers:
Residual uncertainty or approval gate:
```

## NON-NEGOTIABLE CHECKLIST

1. Classify the change before treating it as routine.
2. Verify unfamiliar repository and dependency facts from source.
3. Keep the meaningful behavioural claim inspectable.
4. Choose evidence for the plausible failure surface, not for a ritual.
5. State residual uncertainty and required approval honestly.
