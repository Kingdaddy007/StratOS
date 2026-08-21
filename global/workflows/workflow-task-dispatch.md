---
id: task-dispatch
version: 3
status: active
intent: Coordinate only bounded independent work without turning every task into a multi-agent exercise.
use_when: [a task has independently verifiable parts with exclusive ownership and a clear benefit from delegation]
do_not_use_when: [one agent can safely complete the work, tasks overlap in ownership, the return contract is unclear, or delegation would add ceremony without evidence]
inputs: [parent objective, mode, mutation ceiling, task boundaries, relevant project truth, acceptance gates and dependencies when the work is substantial, available host capabilities]
required_resources: [applicable AGENTS.md files, relevant skill contracts, task-scoped workflow state when local writes are authorised]
mutation_class: read_only
approval_gates: [inherit the parent task ceiling; require just-in-time approval before any destructive or external worker effect]
states: [assess, charter, dispatch-if-justified, integrate, verify, deliver]
outputs: [dispatch decision, bounded worker charters when used, acceptance-gate ownership and evidence ledger when justified, integration result, residual risks]
verification: [confirm exclusive ownership and dependency readiness, review each return against its charter and assigned gate, run proportionate integration checks, label unverified evidence]
failure_paths: [do not dispatch on ambiguous ownership, stop a worker that exceeds its charter, preserve evidence, release ownership, and return work to the coordinator]
resume_contract: task-scoped .agents/workflows/task-id.json following the workflows directory contract
next_workflows: [none]
profiles: [general]
---

# Task Dispatch

## WHEN TO USE

- Split a task only when at least two parts are independent, have exclusive file or decision ownership, and can return useful evidence separately.
- Use a host-visible functional lead or temporary worker only when its distinct judgement, isolation, or speed benefit is material.
- Keep work in the current task when direct execution is clearer, safer, or faster.

## NEVER DO

- Never create workers to simulate activity, use up concurrency, or avoid integrating the work yourself.
- Never give two workers write ownership of the same file or unresolved interface.
- Never let a worker raise its mutation ceiling, install software, publish, deploy, message, purchase, alter credentials, or act on production without the parent's explicit just-in-time approval.
- Never treat a worker's summary as proof; inspect its evidence and affected boundaries.
- Never make a custom agent a permanent department or require all work to pass through it.

## DISPATCH DECISION

Dispatch only if all answers are yes:

1. Is the parent objective already clear enough to state a testable sub-outcome?
2. Does the subtask have exclusive file/decision ownership?
3. Can the worker receive a minimum, non-sensitive context bundle?
4. Is the allowed mode and mutation ceiling explicit?
5. Can the parent verify the result without trusting the worker's self-assessment?
6. Does delegation improve time, independence of review, or evidence quality enough to justify the coordination cost?

If any answer is no, do not dispatch. Narrow the task, resolve the dependency, or work directly.

## ACCEPTANCE GATES AND READY WORK

Use the optional `acceptance_gates` field in task-scoped workflow state only for substantial, resumable, or delegated work whose outcomes can be judged credibly. Do not create gates for conversational replies, trivial edits, or work where a normal local acceptance check is sufficient.

Each gate states one observable claim, its accountable owner, whether it is required, its dependencies, the planned verification procedure and success condition, collected evidence, limitations, and any blocker or approved optional waiver. Gate procedures are inert plan data. Never execute a stored or worker-generated command merely because it appears in state; inspect it, discover the project-native check, and apply the normal authority and tool-safety boundary first.

A gate is ready only when:

1. every gate in `depends_on` is `met`;
2. its owner has exclusive file or decision ownership;
3. required inputs and environment are available; and
4. no approval or authority boundary blocks the work.

Dispatch multiple ready gates concurrently only when their ownership is disjoint, the host supports it, and the wall-clock benefit justifies coordination. Verify each returned gate as it arrives, then dispatch newly ready gates. This is a bounded dependency-aware queue, not a fixed-depth tree or a reason to fill every worker slot.

Workers return candidate evidence; they do not certify their own gate as met. The parent inspects the artifact and evidence, performs the planned check, records limitations, and decides the gate status. A required gate that becomes impossible is `blocked` and keeps the task incomplete. Only an optional gate may be `waived`, with a reason and named approver.

## WORKER CHARTER

Create one concise charter per worker:

| Field | Required content |
| --- | --- |
| Goal | Testable outcome, not a vague activity |
| Mode and ceiling | `diagnose`, `propose`, `implement`, or `incident-mitigate`; maximum permitted mutation class |
| Owned scope | Exact files, decision boundary, and forbidden overlap |
| Inputs | Minimum applicable context, interfaces, and constraints |
| Required output | Artifact, decision, or finding the parent needs |
| Verification | Assigned acceptance gate or commands, inspections, fixtures, and evidence expected |
| Stop conditions | Ambiguity, authority conflict, blocked dependency, or approval gate |
| Return contract | Touched files, raw evidence, assumptions, blockers, residual risks |

Use a functional lead when its role owns the decision. Use a temporary worker for a narrow bounded job. Both remain subordinate to the Studio Director's integration and the user's authority.

## INTEGRATE

1. Confirm the worker stayed inside its charter and ownership boundary.
2. Read the changed files or decision artifact; do not rely only on the summary.
3. Check interfaces, adjacent dependent paths, and any shared project truth affected by the result.
4. Run the planned proportionate verification.
5. Update an assigned acceptance gate only from inspected evidence; record the procedure actually used, result, limitations, unresolved risks, and next action in task-scoped state only when state writes are authorised.
6. Reject, revise, or re-scope work that lacks evidence, exceeds authority, or conflicts with the parent objective.

## OUTPUT SHAPE

Return:

```text
Dispatch decision: direct work | delegated
Why: <material reason>
Workers: <none or compact charter list>
Ownership: <exclusive boundaries>
Evidence required: <acceptance gates and integration checks>
Approval boundary: <none or exact later action>
Result: <integrated outcome or blocker>
Residual risks: <none or explicit list>
```

## NON-NEGOTIABLE CHECKLIST

1. Dispatch only independently verifiable work.
2. Keep authority and scope explicit.
3. Preserve exclusive ownership.
4. Integrate and verify every worker result.
5. Stop at the parent task's approval gate.
