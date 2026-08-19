---
name: devops-infra
description: 'Use this skill to design, inspect, or change infrastructure, environments, CI/CD, operational telemetry, alerts, secret handling, delivery, recovery, or incident readiness. Trigger on deploy, production, CI/CD, infrastructure, cloud, environment, monitoring, logs, metrics, traces, alerts, secrets, backup, rollback, disaster recovery, outage, or operational readiness. Do not use for a code-only performance diagnosis; use performance unless delivery or operations are materially involved.'
---

# DevOps and Infrastructure

## WHEN TO USE THIS

- Design or inspect an environment, deployment path, CI/CD process, recovery path, backup, or operational readiness.
- Choose logs, metrics, traces, profiles, health checks, dashboards, or alerts for a live failure mode.
- Handle infrastructure, secret, configuration, incident, or delivery-risk decisions.

## NEVER DO

- Treat IaC, JSON logs, distributed tracing, a dedicated secret manager, automated deployment, canaries, or automated rollback as universal baselines.
- Expose live secrets in source, logs, screenshots, prompts, generated artifacts, or untrusted tool input.
- Page a human without a concrete action, owner, and response path.
- Call rollback real without checking the artifact, configuration, data state, external effects, and dependency compatibility.
- Execute a deploy, publish, traffic change, credential change, or other external effect without the required just-in-time human approval.
- Claim generic checks establish safety, compliance, security, or production readiness.

## CLASSIFY THE OPERATIONAL DECISION

1. State the service or user boundary, affected environment, failure consequence, operational decision, and recovery limit.
2. Inspect current delivery, configuration, dependencies, stateful effects, existing telemetry, ownership, and documented/manual steps.
3. Use the smallest operational package that can expose the current failure mode:

| Context | Minimum useful package |
| --- | --- |
| Local or disposable prototype | Reproduction, focused check, relevant logs, simple timing where needed, and a reversible local change. |
| Shared internal tool | Success/failure evidence, relevant duration, correlation without sensitive data, health or smoke check, recorded version, and recovery note. |
| Early product | User-facing success/error signal, relevant latency or job duration, dependency/resource signal, deploy version, and reproducible build/deploy path. |
| Production service | User-facing check, success/error and latency or duration signal, dependency/resource evidence, deploy marker, correlation sufficient for diagnosis, and containment path. |
| Stateful job or high-consequence system | Work-unit outcomes, partial/duplicate output controls, recovery or quarantine path, independent/domain review, and human authorization before effect. |

4. Escalate to stronger controls only when repeated environments, manual drift, multiple operators, cross-service attribution, credential rotation/audit, traffic, blast radius, recovery cost, or consequence make them necessary.

## DESIGN OBSERVABILITY AND ALERTS

- Select signals by question. Use logs for events, metrics for measured behaviour, traces for request paths, and profiles for resource attribution. Do not require the full set by default.
- Capture only the fields needed for diagnosis. Protect secrets and sensitive data. Add correlation where a failure crosses components or cannot be reconstructed safely from simpler evidence.
- Page on actionable current or imminent user/business harm. Use internal signals for diagnosis and carefully chosen early warning. Demote a signal with no defined action to a dashboard, ticket, or scheduled review.
- Tie every alert to its threshold rationale, owner, response action, and known blind spots. Review noise and remove or repair ignored alerts.

## PLAN DELIVERY, CONTAINMENT, AND RECOVERY

1. Record the artifact or configuration version, affected state, blast radius, pre-exposure evidence, continue/hold decision, and containment path.
2. Use a direct controlled release for local reversible work. Use a recorded version and repeatable steps for shared internal work. Use limited exposure, a feature flag, a scheduled window, or a staged rollout when external impact or blast radius makes it worthwhile.
3. Treat rollout as a decision point, not proof. Monitor the relevant harm boundary and stop, hold, or contain when the criterion is crossed.
4. Distinguish rollback from containment. If data, schema, messages, payment, access, or another one-way effect changed, prefer a tested forward fix, feature disablement, compensating action, pause, or quarantine when binary rollback cannot safely restore state.
5. Use IaC or equivalent recorded automation when reproducibility, drift control, repeated environments, or recovery makes it valuable. Capture a simple manual path when that is the safer proportional choice.
6. Use a secret-handling mechanism proportionate to the environment. Strengthen it for multiple environments, rotation, audit, multiple operators, or high-consequence credentials; never weaken the exposure prohibition.
7. Stop before external or consequential effect until the required human approval is present. A second agent does not count as independent merely because it is a different agent.

## HANDLE INCIDENTS WITHOUT OVERCLAIMING

- First establish scope, user impact, affected boundaries, recent changes, and immediate containment options.
- Preserve the evidence needed to diagnose; avoid irreversible actions that obscure recovery or root cause.
- Mitigate the active harm with the narrowest safe action. Route production actions to the approval gate.
- Record what is known, inferred, unknown, and the recovery limit. After restoration, identify a structural prevention candidate; do not force a large observability programme onto a small incident.

## REFERENCE LOADING RULES

- Load [references/extended-guidance.md](references/extended-guidance.md) for delivery profiles, signal selection, alert design, recovery analysis, incident handling, or concrete evidence records.
- Load [references/resource-index.md](references/resource-index.md) when applying a dated telemetry, HTTP, release, or host-specific operational claim. Verify the linked source before using provider syntax or tool behaviour.
- Route a code-level latency/capacity diagnosis to `$performance`. Route a security vulnerability or authorization decision to `$security`. Use the matching workflow for `incident-response`, `ship-to-production`, `dependency-upgrade`, or `database-migration` execution sequence.

## OUTPUT SHAPE

```markdown
## Operational decision

- Boundary, environment, and consequence:
- Current evidence and known limits:
- Minimum operational package:
- Delivery or containment approach:
- Recovery reality and approval boundary:
- Verification at the harm boundary:
- Decision, owner, and next action:
```

## NON-NEGOTIABLE CHECKLIST

1. Match controls and evidence to the actual consequence and failure mode.
2. Keep secrets and sensitive data out of observable artifacts.
3. Make recovery limits explicit; do not promise rollback without proof.
4. Obtain approval before an external, irreversible, or high-consequence effect.
