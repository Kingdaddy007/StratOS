---
id: debug-issue
version: 2
status: active
intent: Coordinate evidence-led diagnosis, bounded repair proposals, authorized local fixes, and incident handoffs without confusing containment with root-cause confirmation.
use_when: [a failure, regression, crash, failing test, unexpected behavior, flaky result, integration fault, state inconsistency, or suspected incident needs diagnosis]
do_not_use_when: [a request is clear new implementation with no observed failure, an intentional code-structure improvement, a performance question without an observed degradation, or a production incident that needs immediate incident command]
inputs: [observed and expected behavior, affected scope and environment, available evidence, impact and urgency, known changes, requested mode and authority]
required_resources: [applicable AGENTS.md files, debugging skill, relevant project contexts and runbooks, incident-response/security-audit/test-strategy only when the evidence or risk requires them]
mutation_class: local_edit
approval_gates: [diagnose and propose remain read-only, require explicit implement authority before any local repair, require incident-response just-in-time approval before production or external containment, require explicit human approval before data repair, security-sensitive mutation, credentials, deployment, traffic, or irreversible action]
states: [received, triaged, stabilized, diagnosing, proposed, approval-gated, implementing, verified, mitigated, closed, stopped]
outputs: [symptom record, evidence ledger, hypothesis status, proposed or applied change, verification evidence, residual risks, incident handoff or next owner]
verification: [make executed versus unexecuted checks explicit, validate the original symptom and relevant contract or invariant, inspect sibling paths when the mechanism can recur, record environment gaps and residual uncertainty]
failure_paths: [stop on absent authority, unsafe experiment, contradictory evidence, invalid oracle, scope expansion, data/security boundary, or unresolved production impact; preserve evidence and name the next safe action]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract
next_workflows: [incident-response, security-audit, test-strategy, verify-project, plan-architecture, none]
profiles: [general]
---

# Debug Issue

## Purpose and boundary

This route coordinates the work around a failure; the `debugging` skill owns the detailed investigation method. It is not a universal linear checklist, a license to rewrite a module, or a promise that every report has one code-level root cause.

Default to `diagnose`. A task can stop with a confirmed cause, a strongly supported or likely explanation, an insufficient-evidence report, a no-code conclusion, a repair proposal, or an incident handoff. Those are different outcomes and must not be blurred together.

## Mode and authority contract

| Mode | Allowed work | Required exit |
| --- | --- | --- |
| `diagnose` | Read workspace evidence, inspect existing logs/test output/history, perform only safe observation or isolated checks. | Diagnosis record with evidence labels, unknowns, and next safe action. No source/test edit. |
| `propose` | Do `diagnose` work and prepare a minimal repair, non-code action, or escalation plan. | Scope, mechanism, validation, reversal path, owner, and exact approval needed. No applied edit. |
| `implement` | Apply the approved smallest local repair and proportionate checks. | Evidence that the original issue and relevant contract were checked; residual risk/reversal. |
| `incident-mitigate` | Hand off to `incident-response` for impact restoration and evidence preservation. | Mitigation status distinct from root-cause status; later `diagnose` work if still needed. |

`mutation_class: local_edit` permits only the authorized `implement` path. It never permits data repair, credential changes, deployment, traffic shifts, external communication, or production mutation. Urgency is a routing signal, not an approval.

## Triage

1. Record observed versus expected behavior, scope, environment, first-seen time, frequency, impact, and the evidence provided.
2. Identify whether the risk is local, intermittent, data/security-sensitive, or customer-impacting. Use canonical severity (`critical`, `high`, `medium`, `low`, or `info`) only when the project has evidence to classify it; incident urgency belongs to `incident-response`.
3. If active impact requires coordinated restoration, preserve evidence and route to `incident-response`. Do not delay safe containment for exhaustive diagnosis, and do not call containment a root-cause fix.
4. If the request lacks a clear symptom, tighten the observable statement before searching for causes. A user-supplied theory is a hypothesis, not a fact.

## Diagnose

Use the `debugging` skill's core loop: frame, observe, model, hypothesize, test, update, decide, repair or stop, verify, and record.

- Start from existing evidence and the relevant boundary, not the first file named in an error.
- Attempt a minimal or repeatable reproduction when safe and decision-useful. For non-reproducible, data/security, or incident cases, state why it is absent and choose the safest available evidence instead.
- Maintain only distinguishable hypotheses. Each must identify a mechanism, support and contradiction, a predicted observation, and a safe discriminating check.
- Use known-good/failing comparisons or bisection only when there is an ordered comparison and reliable oracle. A change point is evidence, not proof of mechanism.
- Record negative evidence and unperformed checks. Do not invent tool results, logs, state, or successful test runs.

The diagnosis exit is one of: `confirmed`, `strongly supported`, `likely`, `unverified`, `ruled out`, `no justified code change`, `mitigated without root cause`, or `insufficient evidence`. Read [the debugging skill's references](../skills/debugging/references/resource-index.md) only when their loading conditions apply.

## Propose and implement gate

Move to `propose` when a repair or non-code action is credible but editing is not authorized. The proposal names the mechanism, alternatives rejected, smallest scope, affected sibling paths, validation, reversal, residual risk, and required owner/approval.

Enter `implement` only when:

1. the user has explicitly requested or approved a local repair;
2. evidence supports the mechanism to the level the risk requires;
3. the scope is the smallest credible repair rather than an unrelated cleanup or redesign; and
4. a credible validation and reversal path exist.

Stop implementation and return to diagnosis/proposal if the result contradicts the theory, testing exposes a new material failure, the patch grows beyond scope, the oracle is unreliable, or an authority boundary is encountered. Do not delete/skip tests, swallow the error, weaken authorization, or hard-code a result merely to remove the symptom.

## Verify and close

After an authorized local repair:

1. Check the original symptom where a credible reproduction or equivalent observation exists.
2. Check the contract, invariant, state transition, or boundary that the repair claims to protect.
3. Check genuinely similar sibling paths if the same defect pattern could recur.
4. Run proportionate project checks and state those not run, the reason, environment limits, and residual risk.
5. Close only with a factual change list, evidence, status label, and next owner/action if uncertainty remains.

Passing tests are evidence, not standalone proof. A complete result distinguishes `verified repair`, `mitigated`, `proposed`, `no justified code change`, and `unverified` rather than reporting all outcomes as fixed.

## State and resume contract

Use one record at `.agents/workflows/<task-id>.json`. It records the workflow ID, requested mode, current state, completed states, artifacts, evidence, approvals, blockers, next action, owner, timestamps, and archive state. Never overwrite another task's record.

| State | Required result | Next result |
| --- | --- | --- |
| `received` | Request and source are normalized. | `triaged` or `stopped`. |
| `triaged` | Symptom, impact, risk, mode, authority, and evidence availability are clear enough to select a path. | `stabilized`, `diagnosing`, or `stopped`. |
| `stabilized` | Incident route has recorded containment status and preserved evidence. | `mitigated` or `diagnosing`. |
| `diagnosing` | Evidence ledger, causal model, and hypothesis labels are current. | `proposed`, `approval-gated`, `mitigated`, `stopped`, or `closed`. |
| `proposed` | A minimal change/non-code action and validation plan exist. | `approval-gated` or `closed`. |
| `approval-gated` | Exact local or external approval required is visible. | `implementing`, incident handoff, or `stopped`. |
| `implementing` | Authorized patch remains within scope. | `verified` or return to `diagnosing`. |
| `verified` | Original symptom and claimed protection evidence are recorded. | `closed`. |
| `mitigated` | Impact is controlled but causal status is explicit. | `diagnosing` or `closed` with follow-up owner. |
| `closed` | Result, evidence, residual risks, and next owner are clear. | Reopen only on new evidence or a changed request. |
| `stopped` | Safe stop, evidence gap, authority block, or no-change conclusion is explicit. | Reopen only when the blocker changes. |

## Handoffs

- Route active external/customer-impacting work to `incident-response`.
- Route authorization, exposure, or sensitive-data concerns to `security-audit` before any mutation.
- Route regression or coverage design to `test-strategy`; do not redesign the test system inside this workflow.
- Route a structural boundary decision exposed by the fault to `plan-architecture`; use direct `refactoring` for behavior-preserving cleanup only after the current diagnosis is clear.
- Route a finished material change to `verify-project` when broader independent checks are appropriate.

## Completion checklist

- The symptom is stated separately from its explanation.
- Executed evidence, negative evidence, and unperformed checks are visible.
- The authority and mode match the action taken.
- A mitigation is not described as root-cause confirmation.
- Any repair is narrow, reversible, and verified against the claimed mechanism.
- Data, security, production, and external-effect boundaries are preserved.
