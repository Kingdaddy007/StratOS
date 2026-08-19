---
id: commercial-decision-record
version: 1
status: active
intent: Coordinate a material commercial decision through versioned evidence, specialist challenge, human approval, and a durable record without executing an external commitment.
use_when: [a new paid offer, material repositioning, major proposal, material scope change, price hypothesis, or public claim needs an explicit owner, evidence ledger, specialist challenge, human approval, and archive]
do_not_use_when: [a bounded copy edit, direct offer draft, routine research, small local content change, technical estimate, contract acceptance, payment, outreach, publication, CRM change, or other external action is the real request]
inputs: [decision statement, owner, audience or buyer context when available, existing offer or project truth, source evidence, constraints, requested mode, mutation ceiling]
required_resources: [applicable AGENTS.md files, GLOBAL_MEMORY.md, offer-architecture when the commercial object is material, applicable specialist capability, offer-decision-record template, claim-and-decision-ledger template, commercial-handoff-packet template]
mutation_class: local_edit
approval_gates: [propose and review remain read-only, require explicit local-edit authority before creating or changing a local decision artifact, require a named human owner to approve any price, promise, scope commitment, data use, or public claim, require explicit just-in-time approval immediately before a proposal is sent, a price or claim is published, data is collected, a CRM is changed, a buyer is contacted, or any other external effect]
states: [received, triaged, evidence-framed, drafted, challenged, approval-pending, approved-record, superseded, archived, stopped]
outputs: [versioned decision record, claim-and-decision ledger when material, specialist handoff packet when needed, explicit approval state, unresolved risks, and next route]
verification: [check every material claim, scope boundary, price scenario, and specialist assertion against its available evidence or mark it unknown, verify an accountable owner and approval state, confirm no external effect was performed]
failure_paths: [stop or narrow on missing owner, material unknown, unsupported claim, unbounded scope, unconfirmed feasibility, privacy or security concern, absent local-edit authority, missing human approval, or attempted external effect]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract
next_workflows: [project-inception, verify-project, live-learning-loop, none]
profiles: [growth]
---

# Commercial Decision Record

## PURPOSE AND BOUNDARY

Use this route only when a commercial decision is consequential enough to need a small, inspectable record. It is a decision and handoff route, not a proposal generator, CRM workflow, pricing engine, legal review, or external-action mechanism.

For a clear, reversible draft or correction, work directly through the owning Growth capability. Do not create a state record because a task contains commercial language.

## COORDINATION LOOP

1. **Triage.** Name the decision, human owner, consequence of being wrong, requested mode, and mutation ceiling. Stop when an external action rather than decision preparation is requested.
2. **Frame evidence.** Create or update an Offer Decision Record only if local-edit authority exists. Separate facts, attributed statements, interpretations, hypotheses, recommendations, and unknowns. Keep evidence links, date/context, limitation, and source owner visible.
3. **Bound the commercial object.** Use `offer-architecture` only if offer, scope, proof, risk, or price hypothesis is actually changing. Keep deliverables, exclusions, assumptions, dependencies, buyer responsibilities, acceptance boundary, non-fit, and price status explicit.
4. **Challenge through the right owner.** Request Product, Design, Engineering, Quality, Security, or qualified legal/financial review only when its domain can change the decision. Record the finding, objection, source, and unresolved risk; do not convert it into approval.
5. **Prepare the human decision.** Make every commitment clear: draft, internal scenario, proposed, externally approved, or rejected. A human owner must approve a final scope commitment, price, material claim, data purpose, or buyer-facing representation.
6. **Archive or supersede.** Preserve the final state, evidence limits, approval, reversal path, and revisit trigger. An approved record remains internal decision evidence; it does not send, publish, negotiate, price, collect, or commit anything externally.

## STATE RULES

| State | Minimum condition | Leave state when |
| --- | --- | --- |
| `received` | A stated material decision and named owner exist. | It is triaged or stopped. |
| `triaged` | The smallest owner, mode, and risk boundary are selected. | Evidence is sufficient to frame or the task goes direct. |
| `evidence-framed` | Claims, assumptions, unknowns, and evidence limitations are visible. | A bounded draft can be challenged. |
| `drafted` | Scope, deliverability inputs, proof, and price scenario status are explicit. | Needed specialists return findings or a blocker stops it. |
| `challenged` | Relevant objections and cross-functional limits are recorded. | A human decision is ready or the record is narrowed. |
| `approval-pending` | The exact human decision and its external implications are stated. | Owner approves, rejects, or defers. |
| `approved-record` | Owner, date, scope, claim and price approval state are recorded. | A separate, just-in-time approved external action is requested, or the record is superseded. |
| `superseded` / `archived` | A newer decision or completed relevance period is linked. | Reopen only on material new evidence. |

## OUTPUT AND COMPLETION

Return: decision and owner; commercial object and boundaries; evidence checked and missing; claim and price status; specialist findings; approval state; external action explicitly not taken; residual risk; revisit trigger; and the next direct route, workflow, or approval.

Use task state only for a genuinely resumable record and only when local state tracking is authorised. Never reuse or overwrite another task's record.
