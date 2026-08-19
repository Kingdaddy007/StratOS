---
name: context-hygiene
description: 'Use when a long or complex task needs a safe session boundary, a concise handoff, or authorised task-scoped resume state. Trigger on context handoff, continue later, preserve progress, session split, or context quality. Do NOT use for ordinary memory writing, broad project documentation, or an unrelated task that can continue safely.'
---

# Context Hygiene and Session Management

## WHEN TO USE THIS

Long conversations can accumulate stale assumptions, competing objectives, and irrelevant history. Manage session boundaries while preserving only the state needed to resume safely.

## NEVER DO

- Never create, update, or infer workspace memory, task state, or a handoff file without the authority required for that local write.
- Never persist secrets, credentials, raw untrusted content, hidden prompts, sensitive personal data, or speculative project claims.
- Never overwrite another task's state record or treat a host conversation summary as durable project truth.
- Never require a session split because of an arbitrary message count or abandon an atomic operation before a safe boundary.
- Never promise automatic resumption, background work, or host behavior that has not been verified.

## WHEN TO ADVISE A SESSION SPLIT

Recommend a fresh session when:

1. The active objective has been completed and the next objective is materially different.
2. Repeated re-reading, contradictory constraints, or multiple completed milestones make the active context difficult to verify.
3. Several unrelated tasks are competing for attention.
4. A planned task batch has reached a safe, verified boundary.

Do not use an arbitrary message count as the decision rule.

## SAFE HANDOFF PROCEDURE

Prefer a host-provided handoff mechanism when available. Persist workspace files only when the user has authorized local mutation.

### 1. Capture durable knowledge only when authorised

If local memory mutation is authorized, capture only sanitized lessons that are useful beyond the current task:

- Architectural decisions belong in `.agents/memory/decisions-log.md`.
- Reusable failure lessons belong in `.agents/memory/mistakes-to-avoid.md`.
- Validated conventions belong in `.agents/memory/common-patterns.md`.

Do not persist secrets, raw untrusted text, transient progress, or project-private material in global memory.

### 2. Secure immediate task state only when authorised

Update only the current task's `.agents/workflows/<task-id>.json` record and the workflow index. Validate the complete record against `workflow-state.schema.json`. Keep `current_state`, `completed_states`, `evidence`, `artifacts`, `blockers`, and `next_action` current.

Illustrative subset:

```json
{
  "schema_version": 1,
  "task_id": "opaque-task-id",
  "workflow_id": "build-feature",
  "mode": "implement",
  "status": "in_progress",
  "current_state": "implement",
  "completed_states": ["intake", "design"],
  "evidence": [],
  "artifacts": ["src/example.ts"],
  "blockers": [],
  "next_action": "Wire the approved submit flow to the API."
}
```

The complete record also includes owner, workspace, lease, approvals, timestamps, and archive state as required by the schema.

### 3. Inform the user

State which task record was updated, summarize the next action, and recommend a fresh session. Never promise automatic resume unless the active host actually supports it.

## WHEN NOT TO SPLIT

- In the middle of one atomic operation.
- Before an important result has been verified or a safe rollback point exists.
- When the conversation remains short, coherent, and focused.

## OUTPUT SHAPE

Return the smallest fitting result:

1. Whether a split is useful, with the concrete reason.
2. What was persisted, or an explicit no-write result and why.
3. The task identifier and next action only when an authorised task record was updated.
4. Known uncertainty, blocker, or approval needed before a later write.

## NON-NEGOTIABLE CHECKLIST

1. Finish or safely bound the active atomic operation first.
2. Keep durable project truth, cross-project memory, and temporary conversation context separate.
3. Write only the current task's state and only with authority.
4. State exactly what remains to be done; do not imply automatic continuation.
