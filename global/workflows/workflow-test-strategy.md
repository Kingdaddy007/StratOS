---
id: test-strategy
version: 2
status: active
intent: Turn a specific change or claim into the smallest credible, maintainable evidence plan without confusing a planned test suite with a release conclusion.
use_when: [a change needs test or verification planning, an agent must add or review tests, a regression needs durable protection, a test suite is weak or flaky, or a material boundary needs evidence selection]
do_not_use_when: [an unexplained failure needs root-cause diagnosis first, the request is only style formatting, a production release is being executed, or a security decision requires security-audit]
inputs: [change or claim, intended behavior and acceptance conditions, changed surfaces, risk and reversibility, known boundaries, existing tests and project conventions, available environments, requested mode and authority]
required_resources: [applicable AGENTS.md files, testing skill, project test/build/CI configuration, relevant contracts/schema/runbooks, debugging/security-audit/database-migration/design-ui only when the change requires them]
mutation_class: local_edit
approval_gates: [propose and review remain read-only, require explicit implement authority before adding or changing tests, require security-audit before treating sensitive security behavior as verified, require ship-to-production just-in-time approval for any production release or external effect]
states: [received, scoped, risk-mapped, planned, approval-gated, implementing, executed, evaluated, closed, stopped]
outputs: [claim and risk statement, behavior/boundary inventory, selected evidence and oracle plan, fixture/dependency plan, test changes when authorized, executed evidence, unverified claims, handoffs]
verification: [assert observable behavior or invariants, record environment and actual execution, include appropriate negative/failure cases, classify flaky or blocked results honestly, check the claim rather than a coverage target]
failure_paths: [stop on unclear claim, absent authority, unsafe/live dependency, invalid oracle, non-representative environment, security boundary, unresolvable flakiness, or evidence plan whose maintenance cost exceeds its credible value]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract
next_workflows: [debug-issue, security-audit, database-migration, build-feature, verify-project, none]
profiles: [general]
---

# Test Strategy

## Purpose and boundary

This route selects evidence before or during implementation. It is not a required ceremony for a small reversible change, a test-count exercise, a release approval, or a substitute for diagnosing an unexplained failure.

Use `testing` for the portable evidence method. This workflow turns that method into a project-specific plan using actual repository conventions and constraints. It may produce a plan in `propose` or `review`; it edits tests only in explicitly requested `implement` mode.

## Modes and authority

| Mode | Allowed work | Required result |
| --- | --- | --- |
| `propose` | Inspect project evidence and design a test/verification plan. | Risk, claim, boundaries, chosen evidence, oracle, residual uncertainty, and required approval. |
| `review` | Assess existing tests or an evidence claim without edits. | Adequacy findings, false-confidence risks, gaps, and next evidence. |
| `implement` | Add or change the smallest authorized tests/fixtures and run proportionate checks. | Test diff, actual results, environment, scope verified, residual risk. |

Neither this workflow nor a passing test suite authorizes a release, production test, deployment, credential access, data mutation, external effect, or security sign-off.

## Build the strategy

1. **Scope the claim.** State the behavior/invariant, acceptance condition, and the limit of the claim. Separate a local behavior claim from API compatibility, security assurance, operational readiness, and production-release claims.
2. **Map risk and boundaries.** Consider consequence, change surface, reversibility, persistence, serialization, identity, external provider, time, concurrency, UI, AI behavior, and operational exposure. Involve only the relevant perspective.
3. **Inventory actual evidence.** Discover project instructions, existing tests, test/build/CI definitions, fixtures, known flaky checks, contracts, schemas, and runnable environments. Do not invent commands, test infrastructure, or production access.
4. **Select the smallest credible evidence.** Choose test levels and checks by risk. Prefer direct behavior/invariant evidence; use boundary-realistic integration, contract, browser, migration, security, or AI evaluation where the risk exists. State substitutes and their limitations.
5. **Define the oracle and failure cases.** Describe the positive behavior, meaningful negative/failure cases, expected state transition or invariant, fixture/dependency choice, determinism controls, and what would disprove the claim.
6. **Plan execution and interpretation.** State commands/environments only after discovery, the expected evidence artifact, classification of product/harness/infrastructure/flaky results, and the conclusion that each outcome permits.
7. **Implement only behind the gate.** In `implement` mode, make the smallest test change that protects the relevant contract. For a diagnosed bug, demonstrate failure-before/failure-after when feasible; otherwise record the limit.

## Risk-sensitive handoffs

- Send an unexplained failing or flaky result to `debug-issue`; retry success is not diagnosis.
- Send auth, authorization, secrets, sensitive data, tenant/object isolation, injection, command/file execution, provenance, or AI tool-permission changes to `security-audit`.
- Send migration safety and execution planning to `database-migration`; do not write migration runbooks here.
- Send a project-wide/release evidence collection request to `verify-project`.
- Send the build work itself to `build-feature`; do not turn a test plan into unrelated implementation.

## State and deliverable

When resumable state tracking is authorized, use `.agents/workflows/<task-id>.json`; never overwrite another task's record. The strategy record should contain:

```text
Claim and acceptance condition:
Risk and reversibility:
Behavior and boundary inventory:
Evidence selected: purpose, level, environment/fixture, oracle, limitations
Negative/failure and adversarial cases:
Flakiness or nondeterminism controls:
Security, product/UX, performance, migration, or AI-evaluation handoffs:
Implementation authority and actual execution evidence:
Unverified claims, residual risk, and recommended next route:
```

## Completion checklist

- The selected evidence can change the decision; it is not present merely for coverage or convention.
- The oracle observes intended behavior/invariants rather than a private implementation accident.
- Important boundary and negative cases are covered when their risk justifies it.
- Mocks, fakes, live dependencies, and environment differences are explicit.
- A security or production conclusion has been routed to the correct owner.
- Any unrun, flaky, non-representative, or blocked evidence remains visible.
