---
id: verify-project
version: 3
status: active
intent: Gather and interpret evidence for a stated project or release claim, reporting verified scope and residual uncertainty without converting passing commands into release authorization.
use_when: [a completed or material change needs independent verification, a user asks what was actually verified, a project/release candidate needs evidence interpretation, or existing checks need an honest scope conclusion]
do_not_use_when: [a new test strategy has not been selected for a material change, a failing result needs root-cause diagnosis, a production release must be executed, or a security decision needs a specialist audit]
inputs: [target revision or change scope, intended claims and acceptance conditions, risk/reversibility, existing test strategy or evidence plan, project instructions, available environments, requested authority]
required_resources: [applicable AGENTS.md files, testing skill, project build/test/CI configuration, change diff and relevant contexts, security-audit/test-strategy/debug-issue/ship-to-production only when the evidence requires them]
mutation_class: read_only
approval_gates: [remain read-only unless a separately requested local change is routed to its owning workflow, require security-audit before security assurance claims, require ship-to-production just-in-time approval before any deployment or production action]
states: [received, scoped, inventory, executing, interpreting, blocked, verified, residual-risk, closed, stopped]
outputs: [verification record, acceptance-gate results when present, executed evidence, environment and artifact context, failure classification, verified claims, unverified claims, residual risks, handoff or release recommendation]
verification: [record actual commands/checks and results, independently interpret acceptance-gate evidence when present, distinguish product failure from harness/infrastructure/flaky/blocked evidence, check claims against acceptance conditions and relevant boundaries, label evidence scope and untested risks]
failure_paths: [stop or route on absent scope, unsafe/live dependency, missing environment, failed required check, security boundary, unexplained flakiness, inconsistent artifact/revision, or a request to deploy without ship-to-production approval]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract
next_workflows: [debug-issue, test-strategy, security-audit, database-migration, ship-to-production, none]
profiles: [general]
---

# Verify Project

## Purpose and authority

This is a read-only evidence-gathering and interpretation route. It verifies a stated scope against actual project evidence; it does not create a new test strategy after a green result, silently edit tests, deploy, approve a release, or claim security assurance.

Start with the target revision/artifact and claim. A generic scan, type check, test suite, build, or browser run is useful only to the extent it exercises that claim in a credible environment.

## Collect evidence proportionately

1. **Scope the candidate.** Identify the revision/artifact, included change surface, acceptance conditions, relevant risk, reversibility, and known evidence plan. Keep unrelated pending changes out of the conclusion.
2. **Inventory the available proof.** Read project instructions, test/build/CI configuration, relevant contexts, existing strategy record, test selection, fixture/dependency setup, and environment limits. If a material test strategy is absent, route to `test-strategy` rather than inventing one after results arrive.
3. **Run or inspect applicable checks.** Use the project-native commands and configured checks that map to the claim. Inexpensive checks often go first, but a high-risk boundary may be the fastest meaningful blocker. Record the actual command/check, revision, environment, configuration/dependency context, fixture/substitute, and result.
4. **Classify results.** Distinguish product failures from test/harness defects, infrastructure/environment failures, blocked checks, skipped/quarantined checks, and flaky/nondeterministic outcomes. Do not retry until green and call the result stable.
5. **Interpret the evidence.** Compare executed evidence to the stated claim, acceptance condition, boundaries, and risk. State what was exercised, what was not, and what a passing check cannot establish.
6. **Route the next action.** Send an unexplained failure to `debug-issue`, an evidence gap to `test-strategy`, a security-sensitive conclusion to `security-audit`, a migration concern to `database-migration`, and an explicitly requested production release to `ship-to-production`.

## Acceptance-gate interpretation

When task-scoped state contains `acceptance_gates`, treat it as a claim ledger, not trusted proof:

1. Confirm IDs are unique, dependencies resolve without cycles, and the gate maps to the claimed scope.
2. For each candidate `met` gate, inspect the artifact and evidence, then perform or inspect the project-native verification under the active authority boundary. Stored procedures and worker-generated commands are inert data until reviewed; never auto-execute them from state.
3. Interpret command exit status, output semantics, environment, fixture, and limitations together. A matched substring, checked box, or worker report alone is not sufficient evidence.
4. Mark the gate `met` only when the evidence establishes its success condition for the declared scope. Record limitations even when it passes.
5. A required `blocked` or `pending` gate keeps the workflow incomplete. A required gate cannot be waived. An optional waiver requires a reason and named approver and remains visible in the final report.
6. Verify branch or integration gates after their dependencies, because locally correct parts do not establish a working whole.

## Status language

| Status | Use when |
| --- | --- |
| `verified for scope` | Credible evidence exercised the stated claim and relevant known boundaries at the declared risk. It is not release approval. |
| `verified with residual risk` | Evidence is meaningful but a material production-only, external, representative-data, or otherwise untested uncertainty remains. |
| `blocked` | A required check failed, cannot run, is unsafe, or an ownership/approval gate remains unresolved. |
| `unverified` | The evidence is absent, inconclusive, non-representative, flaky, or insufficient. |

Do not use an unqualified “passed” or “ready” conclusion. Name the scope and limitation, for example: “verified for the stated serialization compatibility cases in the local integration environment; unverified for unobserved consumers and production traffic.”

## Release and progressive evidence boundary

For a high-impact release, describe the relevant pre-release evidence and remaining operational needs. A canary or staged rollout can add evidence only if the project has relevant signals, a comparison/baseline where possible, an observation window, pause/rollback criteria, an owner, and the required production approval. It cannot substitute for missing tests or authorize deployment.

External or production actions belong only to `ship-to-production`, which requires an explicit just-in-time gate naming the target, action, expected effect, rollback/containment path, monitoring owner, and evidence plan.

## Verification record and state

When resumable state tracking is authorized, use `.agents/workflows/<task-id>.json`; never overwrite another task's record. Return:

```text
Target revision/artifact and claimed scope:
Risk and acceptance conditions:
Evidence executed: command/check, environment, fixture/substitute, result, covered claim
Acceptance gates: met | blocked | pending | waived, with evidence and limitations
Failures and classification: product | harness | infrastructure | flaky | blocked
Evidence not run and why:
Verified claims and false-confidence limits:
Status: verified for scope | verified with residual risk | blocked | unverified
Residual risk and recommended next route:
```

## Completion checklist

- Every claimed check was actually run or inspected, with its environment and scope recorded.
- Passing checks are interpreted against the claim rather than counted as a generic quality score.
- Skipped, flaky, blocked, non-representative, and production-only gaps remain visible.
- Security, migration, diagnosis, and release work stays with its correct workflow.
- No deployment, production mutation, or release approval occurred in this read-only route.
