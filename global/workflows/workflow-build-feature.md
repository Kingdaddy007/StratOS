---
id: build-feature
version: 2
status: active
intent: Coordinate an approved material product change through only the roles, decisions, implementation, and evidence that its actual risk requires.
use_when: [an approved feature or material change needs implementation across more than one concern, a visible handoff, a scoped delivery record, or risk-sized verification]
do_not_use_when: [the request is still an unclear initiative or product decision, an observed fault needs diagnosis, a bounded one-surface implementation is already fully specified, a purely visual/design decision is unresolved, or Anti-Gravity itself is being changed]
inputs: [approved user outcome and authority, current workspace facts and applicable contracts, affected surface and non-goals, acceptance evidence or an explicit evidence gap, constraints and known risks]
required_resources: [applicable AGENTS.md files, active project contexts when present, Studio Director route selection, only the relevant Product Design Systems Staff Engineering and Assurance capabilities]
mutation_class: local_edit
approval_gates: [propose and planning remain read_only, require explicit implementation authority before local edits, require just-in-time approval before dependency or network work, destructive action, data repair, credentials, deployment, traffic changes, messaging, publication, purchases, or another external effect]
states: [received, scoped, shaped, ready, approval-gated, implementing, checking, handoff, closed, stopped]
outputs: [delivery scope and non-goals, selected role contributions, approved change set or proposal, verification evidence, residual risks, rollback or correction path, next owner]
verification: [check the stated acceptance condition, affected contracts and failure paths, proportionate automated or observable evidence, relevant sibling paths when the mechanism can recur, and explicitly record unrun checks or environment limits]
failure_paths: [stop or return to the owning decision route on missing authority, unclear product meaning, unresolved design or architectural boundary, unsafe dependency/external action, contradictory evidence, scope expansion, or failed verification]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract; record only material state, evidence, approvals, blockers, next action, owner, and timestamps
next_workflows: [project-inception, design-ui, plan-architecture, debug-issue, test-strategy, verify-project, security-audit, database-migration, dependency-upgrade, none]
profiles: [general]
---

# Build Feature

## Purpose and boundary

Use this route only when an approved change benefits from explicit coordination. It does not impose a waterfall or create permission to make a product, technical, design, dependency, or external decision that has not been authorised.

A small, fully specified local change may go directly to the Staff Engineer. A material change uses this route when the Director needs a visible scope, selected contribution from more than one role, or a delivery/evidence handoff.

## Select the smallest collaboration loop

Start with the approved outcome, existing project truth, affected behaviour, and acceptance condition. Involve a lead only when its question is real:

| Need | Select | Expected contribution |
| --- | --- | --- |
| User, value, scope, priority, or acceptance is unclear | Product & Strategy | Bounded outcome, non-goals, assumption/evidence gap, or a stop decision |
| Flow, state, accessibility, content, or interaction changes the outcome | Design Director | Representative flow/state contract and acceptance criteria |
| Boundary, data, contract, dependency, security, cost, performance, or reversibility is materially changing | Systems Architect | Options, constraints, smallest safe commitment, and escalation condition |
| A feature is authorised and its implementation shape is understood | Staff Engineer | Thin vertical slice, implementation, local evidence, and handoff |
| Risk, sensitive data, AI variability, security, reliability, or a completion claim requires independent challenge | Assurance & Quality | Evidence plan, findings, residual risk, or stop/escalation condition |

Do not load every skill or summon every lead by default. The selected roles may loop: a Staff Engineer can request a missing state from Design; Design can expose a product ambiguity; Assurance can return a change to any owner. The Studio Director integrates the result.

## State and authority

| State | Required result | Next state |
| --- | --- | --- |
| `received` | Request, claimed outcome, authority, and source are visible. | `scoped` or `stopped` |
| `scoped` | Affected surface, non-goals, risk, constraints, and acceptance evidence are clear enough to choose the route. | `shaped`, `ready`, `approval-gated`, or `stopped` |
| `shaped` | Only the necessary product, design, system, or assurance questions have a decision, bounded assumption, or named owner. | `ready`, owning workflow, or `stopped` |
| `ready` | Smallest implementation slice, relevant interfaces, verification approach, and correction path are visible. | `approval-gated` or `implementing` |
| `approval-gated` | Exact missing approval and its consequence are recorded. | `implementing`, another route, or `stopped` |
| `implementing` | Authorised work stays within the stated scope. | `checking`, `shaped`, `approval-gated`, or `stopped` |
| `checking` | Actual evidence is interpreted against the stated acceptance condition. | `handoff`, `shaped`, `debug-issue`, or `stopped` |
| `handoff` | Change, evidence, unverified limits, residual risks, and next owner are clear. | `closed` |
| `closed` | The scoped result is delivered honestly. | Reopen only on a changed request or material new evidence. |
| `stopped` | A safe no-change, authority, evidence, or scope stop is explicit. | Reopen only when the blocker changes. |

`local_edit` applies only in `implementing` after the user has authorised local implementation. It never includes package installation, credentials, database mutation, deployment, publishing, contact, purchase, traffic change, or production action.

## Build and check

1. Prefer one coherent vertical slice over layer-by-layer activity that leaves the project broken between steps.
2. Reuse existing conventions, supported dependencies, contracts, and tests before introducing a new abstraction or package.
3. Keep product, design, systems, and assurance decisions visible where they affect the change. Do not hide them in implementation detail.
4. When an observed failure appears, pause feature work and route to `debug-issue`; do not label a guessed cause as a feature adjustment.
5. Treat passing commands as evidence for their stated scope, not release approval. Route production work to `ship-to-production` only after a separate just-in-time approval.

## Completion record

Deliver:

- outcome and scope actually addressed;
- changed files/interfaces or the no-change/proposal result;
- selected role contributions and decisions;
- checks run, actual results, environment, and checks not run;
- residual risks and the simplest correction/rollback path; and
- the next owner or workflow if work remains.

Do not report “complete” merely because code exists. Report `verified for scope`, `verified with residual risk`, `proposed`, `blocked`, or `unverified` as the evidence supports.
