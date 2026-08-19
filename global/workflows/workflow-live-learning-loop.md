---
id: live-learning-loop
version: 1
status: active
intent: Coordinate a meaningful, approved, reversible live intervention and interpret its evidence without claiming causal certainty that the method cannot support.
use_when: [a material commercial or product decision needs an approved reversible live intervention, credible observation plan, guardrails, interpretation, and archive]
do_not_use_when: [a local copy or design change can be reviewed directly, an observational signal is being overstated as proof, instrumentation is absent, the intervention is irreversible or unsafe, the task is routine analytics, or the user has not explicitly approved the external or production effect]
inputs: [decision owner, decision to inform, hypothesis, proposed intervention, audience or eligibility, available instrumentation, guardrails, rollback or containment path, requested mode, authority]
required_resources: [applicable AGENTS.md files, GLOBAL_MEMORY.md, owning product or Growth capability, live-learning-record template, testing or assurance capability when risk or evaluation design requires it]
mutation_class: external_or_production
approval_gates: [propose and review remain read-only, require explicit approval before creating local records, require explicit just-in-time approval immediately before instrumentation, data collection, a traffic or experience change, publication, messaging, spend, or any external or production intervention; approval must name target, action, affected audience, expected effect, guardrails, rollback or containment, observation window, owner, and evidence plan]
states: [proposed, instrumentation-checked, approval-pending, approved-to-run, running, stopped, interpreted, decided, archived]
outputs: [learning record, intervention and rollback boundary, evidence and limitations, alternative explanations, human decision, and archive or next route]
verification: [confirm a meaningful decision, feasible observation source, guardrails, reversibility, stop rule, approval record, actual intervention state, and interpretation limits; label observational or qualitative results rather than causal proof]
failure_paths: [do not run on missing approval, missing rollback or stop rule, inadequate instrumentation, privacy or security concern, unsafe exposure, unexpected harm, data-quality failure, or a decision that can be resolved more cheaply offline]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract
next_workflows: [verify-project, project-inception, commercial-decision-record, none]
profiles: [growth]
---

# Live Learning Loop

## PURPOSE AND BOUNDARY

Use this route only when live evidence can change a meaningful decision and the proposed intervention is both reversible and explicitly authorised. It is not an automatic optimisation loop, an analytics dashboard ritual, or authority to expose users to an experiment.

Prefer existing evidence, offline review, a prototype, or a bounded local test when they can answer the decision safely. Small traffic, weak data, or an observational signal can still be useful, but never call it causal proof.

## PREPARE THE SMALLEST CREDIBLE LEARNING PLAN

1. Name the human decision owner, decision, hypothesis, expected direction, and what result would change the next decision.
2. Define the intervention version, eligible audience, time window, primary metric, guardrails, data source, comparison type, stop rule, rollback or containment path, and material limitations.
3. Classify the evidence before running it: `randomised`, `observational`, or `qualitative signal`. Do not upgrade a lower-confidence class after the result arrives.
4. Check whether the intervention touches privacy, accessibility, security, pricing, a material claim, spend, traffic, publication, messaging, or a vulnerable audience. Add the owning specialist or stop when the boundary cannot be managed.
5. Create the local Live Learning Record only with local-edit authority. Present the plan and required external approval; do not run it.

## RUN ONLY AFTER JUST-IN-TIME APPROVAL

Immediately before the external or production action, obtain a just-in-time approval that names the target, precise intervention, affected audience, expected effect, guardrails, rollback or containment, observation window, owner, and evidence plan. Record the approval and actual start condition.

During the approved window, stop or contain when a guardrail, safety boundary, unexpected harm, or data-quality failure occurs. Do not broaden the audience, duration, spend, data collection, or intervention while it is running without a new approval.

## INTERPRET AND DECIDE

1. Record what actually happened, data gaps, anomalies, alternative explanations, and whether the stop rule was triggered.
2. Separate observed result from interpretation. Attribute causality only when the chosen evidence design supports it.
3. Ask the human owner to choose `keep`, `revert`, `iterate`, `gather evidence`, or `stop`. A positive metric alone does not select the action.
4. Archive the result, rollback state, decision, limitations, and revisit trigger. Route implementation, verification, or a material commercial revision to its own authorised workflow.

## OUTPUT AND COMPLETION

Return: decision and owner; intervention and approval state; evidence class; observed results and limits; guardrail and rollback result; alternate explanations; human decision; unperformed external actions; and next route.

Use task state only for a genuinely resumable run and only when local state tracking is authorised. Never use this workflow to silently start, extend, or repeat a live intervention.
