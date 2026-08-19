# Operations, Delivery, and Recovery Guide

## Contents

- [Choose proportional controls](#choose-proportional-controls)
- [Select operational signals](#select-operational-signals)
- [Design actionable alerts](#design-actionable-alerts)
- [Assess delivery and recovery](#assess-delivery-and-recovery)
- [Run an incident safely](#run-an-incident-safely)
- [Anti-patterns](#anti-patterns)
- [Operational record](#operational-record)

## Choose proportional controls

Choose controls from the failure mode, not an infrastructure maturity checklist.

| Situation | Add when needed | Do not assume |
| --- | --- | --- |
| Repeated/shared environments or manual drift | Declarative/reproducible environment definition and reviewable change records | Every prototype needs a complete IaC stack |
| Cross-process request path cannot be attributed | Correlation and tracing suited to the request path | All services need distributed traces from day one |
| Logs need machine aggregation or multi-service diagnosis | Structured fields and a searchable format | JSON itself makes logs useful or safe |
| Multiple environments, rotation, access audit, or high-consequence credentials | A dedicated secret-management service and audited access | A dedicated manager alone prevents secret exposure |
| Frequent, risky, or repeated releases | Versioned artifacts, automation, limited exposure, and verified recovery | Automation makes a bad state model safe |
| Material user/business impact | Actionable paging plus diagnostic and early-warning signals | Only user symptoms or only infrastructure causes matter |

## Select operational signals

Start with the question:

- **Did users or the business succeed?** Use a black-box or user-facing signal.
- **Where did the request, job, or dependency fail or slow?** Add diagnostic evidence at the relevant boundary.
- **Is failure imminent but not yet visible to users?** Add an internal early-warning signal only if it leads to a defined action.
- **Can an operator attribute the failure across components?** Add correlation or tracing if logs and metrics are insufficient.

Choose the minimum. An internal tool may need a smoke check, outcome count, and relevant logs. A production API usually needs user-facing success/error, latency or duration, request volume, deploy marker, resource/dependency evidence, and enough correlation to distinguish the failure mode. A batch job needs work-unit and deadline signals, not only HTTP-style metrics.

## Design actionable alerts

For each alert, record:

```text
Signal and user/business consequence:
Threshold or anomaly rule and rationale:
Owner and expected response:
Immediate containment or diagnosis action:
Known blind spots and noise risk:
Escalation and review cadence:
```

Page for current or imminent impact with a clear action. Use lower-urgency views for diagnosis, trends, or capacity planning. A CPU or queue signal can be useful when it gives time to avert impact; it must not be treated as an automatic pager merely because a percentage was crossed.

## Assess delivery and recovery

Before exposure, determine the change profile:

| Change | Delivery evidence | Containment or recovery |
| --- | --- | --- |
| Local, reversible, no external effect | Reproduction and focused check | Revert or recreate the local environment |
| Shared internal | Recorded artifact/configuration, smoke check, key path, logs/health | Re-deploy prior version or restore configuration |
| External, moderate blast radius | Baseline, focused regression, deploy marker, key signals, release window/flag/cohort where useful | Disable flag, revert compatible artifact, restore configuration |
| Stateful job or migration | Work-unit/output evidence, checkpoint/replay analysis, partial/duplicate-work check | Pause, quarantine, compensate, forward-fix, or restore only when proved safe |
| High consequence | Representative/domain-specific evidence, independent review, formal human authorization | Domain-specific containment; generic rollback may be inadequate |

Treat a rollback plan as a hypothesis. Check the artifact, configuration, durable data, external side effects, and dependency compatibility. A migration, message, transaction, user-visible mutation, or credential effect may require containment or a forward fix instead of rollback.

## Run an incident safely

1. State current impact, affected users/systems, severity, and time boundary.
2. Inspect recent changes, dependencies, telemetry, and safe containment options.
3. Separate facts, hypotheses, and unknowns. Preserve evidence needed for recovery and diagnosis.
4. Propose the narrowest mitigation. Obtain human approval before an external, production, destructive, or financially consequential effect.
5. Verify mitigation at the harm boundary. Record residual risk and recovery limits.
6. After stability, identify the smallest prevention candidate. Do not claim root cause or complete prevention without evidence.

## Anti-patterns

| Anti-pattern | What it is | Fix |
| --- | --- | --- |
| Maturity checklist import | IaC, traces, JSON logs, canaries, and automation are imposed on a small local task | Select controls from failure mode, consequence, and operating need |
| Alert without action | A page fires but no one can do anything useful | Add an owner/action or demote it to a lower-urgency signal |
| Recovery fiction | Binary rollback is assumed to undo stateful or external effects | Check state and compatibility; choose forward fix, disablement, compensation, pause, or quarantine |
| Secret-tool substitution | A secret manager is installed but secrets leak into logs or prompts | Enforce non-exposure and least privilege regardless of mechanism |
| Telemetry hoarding | Every signal is collected without a diagnosis use | Specify the question, retention/cost, and sensitive-data boundary |
| Unsafe incident reflex | An agent executes an external action before evidence and approval | Propose, gate, then act only with just-in-time approval |

## Operational record

```markdown
## Operational record

- Service/environment and consequence:
- Change or incident scope:
- Existing controls and evidence:
- Selected signals and alert actions:
- Release/containment plan:
- Recovery assumptions and limits:
- Approval boundary:
- Harm-boundary verification and decision:
```
