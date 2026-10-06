---
name: implement-spec
license: MIT
description: >
  Implement an approved specification and its dependency-linked tickets on one integration branch. Activate only on an explicit request such as `/implement-spec`, "implement this spec and its tickets", or "build all tickets in this specification". Do not use for product framing, speculative implementation, a single trivial fix, or authorization to publish, close remote tickets, merge to the default branch, or deploy.
---

# Implement Specification

## WHEN TO USE THIS

- Execute an approved spec with acceptance criteria and dependency-linked tickets.
- Coordinate a substantial build whose independently verifiable units benefit from isolation.

## NEVER DO

- Infer approval to implement from a planning, review, or retrospective question.
- Reset, discard, stash, overwrite, or remove another task's work to make a worktree match a branch.
- Treat a configured tracker, a closing keyword, or a skill as permission for external effects.
- Declare a ticket complete solely from a worker summary or a passing command unrelated to its acceptance criteria.
- Dispatch overlapping write ownership or force workers merely to fill concurrency slots.
- Require an unavailable Skill tool, named provider, remote tracker, or subagent to finish safe local work.

## ESTABLISH THE EXECUTION CONTRACT

1. Read applicable contracts, the approved spec, non-goals, tickets, acceptance criteria, project context, and relevant ADRs. Follow the project glossary or glossary map; accept an existing authoritative legacy domain document without renaming it.
2. Resolve the tracker from existing project instructions or a supplied path. A supplied local ticket file is sufficient. Separate local progress reporting from remote ticket mutation. Ask only for missing information that blocks implementation; do not force an upstream setup command or invent remote issues.
3. Inspect Git status, branch, history, and available worktree tools. Record the source revision and existing unrelated changes. Select a new integration branch from the approved base; reuse an explicitly designated integration branch when appropriate. Preserve the default branch.
4. Validate the task graph: unique IDs, real dependency edges, no missing blockers or cycles, and testable completion criteria. Treat genuinely unresolved product/architecture choices as blockers instead of manufacturing implementation details.
5. Record a compact execution ledger for resumable work: ticket IDs, dependencies, ownership, base revisions, status, artifact pointers, evidence, limitations, and integration commits. Use the project's established state location; never overwrite another task's state. Use `planned`, `ready`, `running`, `review`, `integrated`, or `blocked` explicitly.

## DISPATCH ONLY READY, OWNED WORK

A ticket is ready when its dependencies are integrated and verified, required inputs are available, its scope is approved, and its write ownership does not overlap active work.

Load [coding](../coding/SKILL.md) for implementation and [testing](../testing/SKILL.md) for evidence selection. Load [tdd](../tdd/SKILL.md) for nontrivial behavior at an established testable boundary; choose parse, render, or other proportionate evidence for reversible no-runtime edits.

Use the installed `task-dispatch` workflow when at least two ready units have exclusive ownership and coordination will improve speed or evidence. Load its contract from the router's workflow location. Use only host-supported delegation; fall back to sequential execution when delegation or worktree isolation is unavailable or not useful. Do not claim that review in the same agent is independent assurance.

For each worker, provide objective, parent owner, exact owned files/modules, forbidden overlap, mutation ceiling, spec/ticket pointers, integration base revision, required checks, return contract, and end condition. State that others are working in the codebase and their edits must be preserved. Keep temporary workers non-delegating. Prefer shared artifact pointers to copied transcripts.

Create each implementation worktree from a recorded integration revision. If its base is wrong, preserve the checkout and create a correctly based worktree; do not reset dirty or unrelated work. Give each worker its own branch. Keep shared interface edits under one owner or sequence them.

## INTEGRATE THROUGH ONE OWNER

1. Require the worker to return its exact revision, diff summary, acceptance evidence, unresolved concerns, and test environment limits. Independently inspect the returned artifacts against the ticket contract.
2. Serialize integration: one owner updates the integration branch; workers and merger agents never modify it concurrently. Refresh a candidate against the current integration tip using the project's supported non-destructive merge strategy. Resolve conflicts inside the assigned scope and recheck affected behavior.
3. Verify the integration tip again immediately before integrating. If it changed, refresh and recheck. A worker's earlier sync does not guarantee a fast-forward or conflict-free merge. Use fast-forward only when the topology permits it; otherwise follow the repository's approved merge policy.
4. Run the ticket's acceptance checks on the combined result. Use focused cross-ticket checks when shared contracts change. Keep a ticket in `review` or `blocked` when evidence is absent or fails; open the next frontier only after its dependencies are `integrated` with inspected evidence.
5. Preserve candidate branches and evidence when integration fails. Stop dependent tickets, report the exact blocker, and continue independent ready work within scope.

## REVIEW AND CLOSE OUT

Run [code-review](../code-review/SKILL.md) over the complete integration change against the recorded base and originating spec. Assign independent Assurance separately when the risk merits it and delegation is available. Fix actionable issues inside the approved scope, rerun affected checks, and review the final diff.

Run the appropriate combined build, tests, and boundary checks. Report every required ticket as integrated with evidence or blocked; do not call the whole spec complete while a required ticket remains unresolved. Keep new discoveries as proposed scope until they are authorized.

Use [pr](../pr/SKILL.md) to prepare a requested PR body. Create/publish a draft, mark it ready, close remote tickets, merge to the default branch, or deploy only when that specific effect is already authorized. Until then, return the integration branch and reviewable evidence. Do not auto-run `retro`; use it only when requested.

Before removing task-created worktrees, verify their exact paths and that commits, non-ignored artifacts, and needed ignored files are recoverable. Prefer the host's recoverable archive mechanism. Apply the host's destructive-action approval rules; retain worktrees when cleanup is not authorized or recovery is uncertain.

## OUTPUT SHAPE

```text
Spec, integration branch, and base revision:
Ticket ledger: status, dependencies, owner, integrated revision, evidence
Review findings and final combined checks:
Blocked requirements and environment limitations:
External effects authorized/performed, or pending:
Worktrees retained/archived and recovery pointers:
```

## NON-NEGOTIABLE CHECKLIST

1. Confirm approved scope, graph validity, and preserved existing work.
2. Dispatch only ready tickets with exclusive ownership.
3. Serialize integration and verify the combined result.
4. Require inspected acceptance evidence for completion.
5. Review the complete change and disclose remaining blockers.
6. Respect external-action and recoverable-cleanup boundaries.
