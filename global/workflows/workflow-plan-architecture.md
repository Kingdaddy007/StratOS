---
id: plan-architecture
version: 2
status: active
intent: Make a consequential system decision inspectable by recording the real quality attributes, options, evidence, accepted trade-offs, and re-evaluation conditions without treating analysis as permission to build.
use_when: [a durable boundary, state owner, API/data contract, integration, migration path, reliability posture, or hard-to-reverse technology decision needs an explicit decision record]
do_not_use_when: [a small local implementation follows an already accepted pattern, the product problem is still unclear, an observed fault needs diagnosis, an API/data choice is bounded and reversible, or a decision is being made only to satisfy a ritual]
inputs: [decision question, current system and project facts, affected users and owners, desired qualities and constraints, known options/evidence, reversibility and authority limits]
required_resources: [applicable AGENTS.md files, architecture skill, current project contexts and accepted decisions, Product Design Assurance or Staff Engineering contribution only when the decision creates their question]
mutation_class: read_only
approval_gates: [analysis and recommendation remain read_only, require explicit approval before a durable local architecture record is created or replaced, require a separate requested implementation route before code/configuration changes, require just-in-time approval before dependency/network, database, deployment, production, destructive, or external action]
states: [received, classified, evidence-framed, options-shaped, challenged, decision-pending, recorded, stopped]
outputs: [decision statement, quality attributes and constraints, current-state/evidence map, viable options and trade-offs, recommendation or no-decision outcome, accepted consequences, re-evaluation triggers, required next approval]
verification: [trace each recommendation to a stated constraint or evidence item, distinguish fact from inference and unknown, test the riskiest reversible assumption when practical, confirm ownership and failure/recovery implications, and record limitations]
failure_paths: [stop on missing decision owner, false precision, unresolved product meaning, incompatible authority, absent evidence for an irreversible commitment, or a decision that belongs to a smaller direct specialist operation]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract; record decision status, evidence, alternatives, approvals, blockers, next action, owner, and timestamps
next_workflows: [project-inception, build-feature, database-migration, security-audit, dependency-upgrade, test-strategy, none]
profiles: [general]
---

# Plan Architecture

## Purpose and boundary

Use this route for a decision that is expensive to reverse or affects more than one bounded concern. The `architecture` capability supplies the detailed reasoning method; this workflow makes the decision, authority, and consequences visible.

Do not run it for every folder, component, endpoint, or implementation detail. A small reversible decision should be made directly by the owner using existing project conventions. A request with unclear value or scope belongs in `project-inception` first.

## Classify before investing effort

| Decision shape | Default route |
| --- | --- |
| Local and easily corrected, with an existing accepted pattern | Direct Systems/Staff operation; record only the rationale needed for the project. |
| Material but reversible boundary, integration, data, reliability, or cost choice | Use this route proportionately. |
| Hard-to-reverse, sensitive, regulated, externally committed, or high-blast-radius choice | Use this route with Product and Assurance input; stop at the named human approval before any commitment. |

Classification does not turn an unknown into a metric. State what is known, what is estimated, and what must be learned before a commitment.

## Shape the decision

1. State the decision in one sentence: who/what is affected, what must be decided now, and what is deliberately out of scope.
2. Identify the quality attributes that actually matter: for example correctness, privacy, cost, latency, recovery, operability, change speed, accessibility, or data integrity. Rank conflicts rather than claiming everything is equally critical.
3. Map current boundaries, state/data ownership, interfaces, dependencies, failure behaviour, and real constraints. Mark evidence as fact, reported, inference, or unknown.
4. Generate the viable options that differ in a meaningful way. Include the existing/simple path when viable. Do not manufacture three tiers or a fashionable alternative merely to fill a table.
5. For each option, describe the useful boundary, responsibility/ownership, failure and recovery shape, operational burden, reversibility/migration path, and the quality attributes it sacrifices.
6. Invite only the leads whose decision is affected: Product for outcome/scope, Design for an experience consequence, Staff Engineering for delivery/operability, and Assurance for sensitive risk or an independent challenge.
7. Recommend an option only at the strength the evidence supports. If an assumption is decisive and cheaply testable, propose the smallest spike or measurement instead of pretending to know the answer.

## State and approval

| State | Required result | Next state |
| --- | --- | --- |
| `received` | A decision question and owner are identifiable. | `classified` or `stopped` |
| `classified` | Decision consequence, reversibility, affected concerns, and route are clear. | `evidence-framed`, direct operation, or `stopped` |
| `evidence-framed` | Current state, constraints, unknowns, and quality priorities are visible. | `options-shaped` or `stopped` |
| `options-shaped` | Viable options and their material trade-offs are explicit. | `challenged`, `decision-pending`, or `stopped` |
| `challenged` | Relevant cross-boundary objections or evidence gaps are resolved, bounded, or named. | `decision-pending` or `stopped` |
| `decision-pending` | Recommendation, consequences, and exact human approval or test are visible. | `recorded`, selected next workflow, or `stopped` |
| `recorded` | The approved decision and re-evaluation trigger are stored only when local-write authority exists. | Selected next workflow or `stopped` |
| `stopped` | No decision, insufficient evidence, or authority block is honest and actionable. | Reopen only with a changed fact, request, or approval. |

This workflow never authorises code, a database migration, package installation, deployment, or external communication. A decision record is not an implementation approval.

## Decision record and handoff

Deliver a concise record containing:

- decision and scope;
- current-state evidence, assumptions, and unknowns;
- ranked quality attributes and constraints;
- viable options, rejected option reasoning, and recommendation strength;
- ownership, failure/recovery, operational, migration, and security consequences;
- what is sacrificed and what would make the decision wrong later; and
- exact next owner, workflow, and approval boundary.

Use `build-feature` for authorised implementation, `database-migration` for data mutation, `security-audit` for material security evidence, and `test-strategy` for a risk-sized proof plan. Never describe a future review date as a substitute for a required present decision.
