---
id: ship-to-production
version: 2
status: active
intent: Prepare, approve, execute, observe, and close a specific production release with target-specific evidence and a reversible response plan; never turn readiness checks into automatic deployment authority.
use_when: [a named release, production configuration change, traffic-affecting rollout, public publication, or live service change is explicitly requested]
do_not_use_when: [the task is local development, planning only, a test result is being interpreted, a production incident needs immediate containment, or no named target/action/owner exists]
inputs: [release candidate and target, owner and requested external authority, change scope and affected users, current environment/release evidence, rollback or containment path, observation plan and constraints]
required_resources: [applicable AGENTS.md files, current project release/runbook context when present, Systems Staff Engineering Assurance contributions only as risk requires, live host/tool availability verified before use]
mutation_class: external_or_production
approval_gates: [all preparation remains read_only, require explicit just-in-time approval immediately before execution naming target, exact action, expected effect, affected audience, rollback or containment path, observation window, owner, and evidence plan; require a separate approval for any changed target/action or irreversible follow-up]
states: [received, assessed, evidence-framed, ready-pending-approval, approved-to-execute, executing, observing, stabilized, closed, stopped]
outputs: [release scope and target record, risk/impact assessment, actual readiness evidence and limitations, just-in-time approval record, execution/observation record, rollback or containment status, residual risks, next owner]
verification: [confirm target and revision immediately before execution, check the stated critical behaviour and relevant health/observability signals, compare results with the approved expectation where a baseline exists, record actual evidence and unverified conditions, and confirm rollback/containment outcome if used]
failure_paths: [stop on missing target/revision/owner/approval/rollback path, unexpected scope, failed readiness evidence, unavailable safe observation, production anomaly, data-integrity concern, security concern, or a request to improvise an external action]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract; record target, release candidate, risk, evidence, approval, execution status, observation, rollback/containment, owner, timestamps, and next action
next_workflows: [incident-response, database-migration, security-audit, debug-issue, verify-project, none]
profiles: [general]
---

# Ship to Production

## Purpose and boundary

This is an external hard gate, not a deployment button. It prepares a specific release and stops until Beloved gives just-in-time approval for the exact external action. Passing tests, a green CI job, or a written plan are readiness evidence; none is authority to release.

Use the target's actual runbook, supported release mechanism, access controls, rollback/containment path, and observability. Do not invent a canary, feature flag, staging environment, alert threshold, rollback command, or cloud capability that the active project does not have.

## Assess the release

1. Identify the exact revision/artifact, target, environment, owner, affected behaviour, data/contract changes, external dependencies, and user/audience consequence.
2. Identify the material risk from the change itself: reversibility, data integrity, access/security, blast radius, availability, financial/public effect, and operational confidence. Do not classify risk from generic labels alone.
3. Gather only proportionate readiness evidence: project-native tests/build/type checks, targeted integration or browser checks where relevant, migration rehearsal/compatibility evidence when needed, security review when the boundary requires it, and environment/release facts that are actually observable.
4. Define the smallest credible observation plan: what must be observed, by whom, for how long, what counts as an unexpected result, and when the safe action is stop, rollback, or incident handoff.
5. State the correction/rollback/containment path in operational terms. If there is no credible reversal path, name the irreversible consequence and require a stronger decision before asking for approval.

## Readiness is not approval

Move to `ready-pending-approval` only when the record contains:

```text
Target and exact action:
Release candidate/revision:
Expected effect and affected audience:
Evidence and known limits:
Rollback or containment path:
Observation window and owner:
Exact just-in-time approval request:
```

Do not execute until the user approves that exact record. A changed revision, target, scope, or rollback path invalidates the approval and requires a new one.

## State and execution contract

| State | Required result | Next state |
| --- | --- | --- |
| `received` | Target, action, release candidate, and owner are identifiable. | `assessed` or `stopped` |
| `assessed` | Scope, affected parties, risks, dependencies, and reversibility are visible. | `evidence-framed` or `stopped` |
| `evidence-framed` | Readiness evidence, limitations, and observation/rollback plan are explicit. | `ready-pending-approval` or `stopped` |
| `ready-pending-approval` | Exact action and just-in-time approval request are visible. | `approved-to-execute` or `stopped` |
| `approved-to-execute` | Approval matches current target/action/revision and has not changed. | `executing` |
| `executing` | Execute only the approved action through the supported mechanism. | `observing`, `incident-response`, or `stopped` |
| `observing` | Critical behaviour and agreed signals are recorded for the observation window. | `stabilized`, rollback/containment, `incident-response`, or `stopped` |
| `stabilized` | Expected behaviour is supported by the stated evidence; limits remain visible. | `closed` |
| `closed` | Release result, evidence, residual risk, and owner are handed off. | Reopen only for a new release/change. |
| `stopped` | No external action occurred or containment/next owner is explicit. | Reopen only with changed authority/evidence. |

If an anomaly could harm users, data, security, or trust, stop improvisation. Preserve evidence, execute only a separately approved containment action if one exists, and route active impact to `incident-response`.

## Delivery record

Report the exact action taken or clearly state that no release occurred. Include target, revision, approval, checks/results, observation evidence, incidents/rollback/containment if any, known gaps, residual risks, and the next owner. Never call the release “safe” without defining the inspected scope and remaining uncertainty.
