---
id: incident-response
version: 2
status: active
intent: Coordinate an active production/security/data incident through evidence preservation, impact containment, just-in-time approved mitigation, recovery observation, and follow-up without confusing restored service with root-cause confirmation.
use_when: [an active production outage, security event, data-integrity threat, material availability degradation, or credible live incident requires coordinated containment or recovery]
do_not_use_when: [the issue is local/non-production, there is no active impact requiring incident coordination, the task is a planned release, or the primary need is ordinary root-cause diagnosis]
inputs: [observed impact and affected target, reporter/source/time, available telemetry and changes, affected users/data/services, responders/owner, requested authority and known containment options]
required_resources: [applicable AGENTS.md files, active project runbooks/contexts when present, incident evidence, relevant Systems Security Debugging and Assurance capabilities, live host/tool availability verified before use]
mutation_class: external_or_production
approval_gates: [observation and planning remain read_only, require explicit just-in-time approval immediately before any mitigation naming target, exact action, expected effect, affected audience/data, rollback or containment path, evidence/observation owner, and stop condition; a new mitigation requires a new approval]
states: [declared, triaged, stabilizing, mitigation-pending, mitigating, recovery-checking, observing, stabilized, follow-up-owned, closed, stopped]
outputs: [incident record and timeline, impact/urgency assessment, evidence register, approved mitigation record, recovery/observation evidence, root-cause status, residual risk, follow-up owner]
verification: [verify the stated affected critical path and impact signals where observable, distinguish recovery evidence from causal proof, preserve pre/post-mitigation evidence, record the observation window and limits, and validate data/security consequences as far as safe access allows]
failure_paths: [stop or escalate on absent authority, missing safe target/action, failed or harmful mitigation, data/security risk, contradictory impact evidence, lost observability, or need for destructive/irreversible action without a separate approval]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract; record incident source/time, target, impact, urgency, evidence, approvals, mitigation, recovery state, blockers, owner, timestamps, and next action
next_workflows: [debug-issue, security-audit, database-migration, ship-to-production, verify-project, none]
profiles: [general]
---

# Incident Response

## Purpose and boundary

The first job in an incident is to understand and reduce live harm safely. It is not to prove a root cause quickly, change everything at once, or turn urgency into automatic authority.

Use severity `critical`, `high`, `medium`, `low`, or `info` for finding impact where warranted. Use operational urgency `SEV-1` through `SEV-4` only to order response and communication; it is not a permission level.

## Establish an evidence-led response

1. Record reported versus observed impact, affected target/environment, first-known time, source, users/data/services affected, current status, and what is not known.
2. Name the incident owner and any available communications, technical, and operations owners. If one person holds several roles, state it; do not invent a team.
3. Preserve relevant timestamps, changes, telemetry, and hypotheses before a mitigation when practical and safe. Do not access credentials, sensitive data, or production tools beyond existing authority.
4. Select the smallest credible containment/mitigation option. Compare its expected benefit, possible harm, reversibility, data/security consequence, and observation signal. A rollback, feature disable, traffic action, configuration change, or communication is an external effect and needs its own approval.
5. Keep mitigation and root cause separate. A system can recover without knowing the cause; a theory can be strong without authorising a production change.

## Just-in-time mitigation gate

Before any external or production action, provide this record and wait for approval:

```text
Incident target and current impact:
Exact mitigation action:
Expected effect and affected users/data:
Known risks and alternatives rejected:
Rollback or containment path:
Observation/evidence owner and stop condition:
Exact just-in-time approval requested:
```

Execute one approved action at a time. If the target, action, evidence, rollback path, or effect changes, stop and request fresh approval.

## State and handoff

| State | Required result | Next state |
| --- | --- | --- |
| `declared` | Report, target, impact, and owner are identifiable. | `triaged` or `stopped` |
| `triaged` | Urgency, affected surface, authority, available evidence, and safe response options are clear enough to act or stop. | `stabilizing`, `mitigation-pending`, or `stopped` |
| `stabilizing` | Evidence preservation and immediate non-mutating containment planning are underway. | `mitigation-pending`, `recovery-checking`, or `stopped` |
| `mitigation-pending` | Exact approved-action request is visible. | `mitigating` or `stopped` |
| `mitigating` | Only the approved action is executed and evidence is captured. | `recovery-checking`, new approval, or `stopped` |
| `recovery-checking` | Critical impact/behaviour and data/security consequences are checked to the available scope. | `observing`, `stabilized`, `debug-issue`, or `stopped` |
| `observing` | Agreed impact/health signals are watched for the stated window. | `stabilized`, new mitigation, or `stopped` |
| `stabilized` | Material impact is controlled; causal status and residual risk remain explicit. | `follow-up-owned` or `closed` |
| `follow-up-owned` | Root-cause, security, migration, or release follow-up has a named owner/route. | `closed` |
| `closed` | Timeline, actual effect, evidence, residual risk, and owners are delivered. | Reopen only on new impact/evidence. |
| `stopped` | No unsafe action occurs; safe escalation/next owner is clear. | Reopen only with changed authority/evidence. |

Route root-cause work to `debug-issue`, security investigation to `security-audit`, data remediation to `database-migration`, and a later release to `ship-to-production`. A post-incident learning review is only useful after impact is controlled and must not silently rewrite global OS policy.
