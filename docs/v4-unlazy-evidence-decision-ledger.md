# V4 Unlazy Evidence Decision Ledger

**Date:** 2026-08-21

**Evidence:** [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy), supplied transcript, and supplied rolling-dispatch screenshot

**Authority:** Evidence only. No upstream instruction, installer, hook, or command is trusted as V4 policy or execution authority.

## Decision

V4 will adapt Unlazy's evidence-backed completion mechanism inside its existing workflow-state, task-dispatch, test-strategy, and verification contracts. V4 will not install or vendor the Unlazy skill, create a competing `PLAN.md` / `GATES.md` state system, execute gate text automatically, or use the Claude-only Stop hook.

## Current V4 baseline

Before this evidence, V4 already required bounded worker charters, exclusive ownership, parent inspection, proportionate integration verification, evidence records, blockers, residual-risk reporting, and just-in-time approval for destructive or external effects. The verified gap was not general orchestration discipline. It was the absence of a standard machine-readable link between a substantial task's completion claims, dependencies, evidence method, actual evidence, limitations, and resolution status.

## Keep / adapt / defer / reject

| Decision | Evidence element | V4 treatment |
| --- | --- | --- |
| KEEP | Outcome-based acceptance claims | Preserve as optional structured acceptance gates for substantial, resumable, or delegated work. |
| KEEP | Parent re-verification | Workers return candidate evidence; the accountable parent independently decides whether a gate is met. |
| KEEP | Leaf and integration evidence | Represent dependencies explicitly so integration gates follow the parts they verify. |
| KEEP | Final-number remeasurement and visible limitations | Record actual evidence and limitations; do not turn a green check into a broader claim. |
| ADAPT | Gate files | Store gates in the existing `.agents/workflows/<task-id>.json` record so V4 retains one task-state source. |
| ADAPT | Parallel leaves | Use a bounded ready queue: dependencies met, ownership disjoint, inputs available, and authority clear. Parallelism is optional and justified by wall-clock or evidence value. |
| ADAPT | `ABANDON` | Required gates become `blocked` and keep the task incomplete. Only optional gates may be `waived`, with a reason and named approver. |
| ADAPT | Runnable checks | Store a verification procedure and decisive success condition as inert plan data. Discover, inspect, authorize, and run project-native checks through normal host controls. |
| DEFER | Executable gate runner | Reconsider only after a command trust model, structured argument format, threat analysis, and cross-platform pilot exist. |
| DEFER | Completion/Stop hook | Claude Code-only behavior is not a Codex contract. Hooks require a separate host-capability and safety decision. |
| DEFER | Model router and automatic tiering | Requires measured route-quality and cost evidence in the actual target harness. |
| REJECT | Automatic `shell: true` execution of generated `CHECK:` text | Agent or external text cannot grant command authority. |
| REJECT | Substring-only success | Exit/result semantics, environment, artifact, scope, and limitations must be interpreted together. |
| REJECT | Fixed depth or default swarm size | Decompose at real ownership and integration boundaries; do not manufacture leaves or fill concurrency. |
| REJECT | Installing Unlazy as V4 policy | It would duplicate existing V4 governance and introduce a second state model plus unsafe execution assumptions. |

## Implemented canonical change

The additive `acceptance_gates` task-state field records:

- stable gate ID, observable claim, accountable owner, and required/optional status;
- acyclic dependencies used to identify ready work;
- verification kind, procedure, and success condition;
- evidence, limitations, blocker, or approved optional waiver; and
- `pending`, `met`, `blocked`, or `waived` state.

The writer rejects malformed gates, duplicate IDs, missing dependencies, dependency cycles, evidence-free `met` gates, blocked gates without blockers, required waivers, and a `complete` workflow containing unresolved gates. It never executes the recorded verification procedure.

## Routing integration

The Studio Director selects workflows privately from task shape; the user does not need to remember or invoke workflow names. `build-feature` makes the acceptance-gate, dispatch, evidence-strategy, and independent-verification decisions. `task-dispatch` is selected only for ready, disjoint, independently verifiable work. Generated Codex and Antigravity specialists receive an assigned workflow or gate as a narrowing charter, return candidate evidence, and cannot waive required gates or certify their own completion claim. `GLOBAL_MEMORY.md` names `AGENTS.md` as the Codex main policy and does not route Codex through `GEMINI.md`.

## Re-evaluation triggers

Reconsider the deferred tooling only when all of the following exist:

1. representative V4 tasks showing a recurring false-completion problem after the structured gate contract;
2. a safe execution design that does not run generated shell strings;
3. Codex and Antigravity host-capability evidence;
4. fixtures covering authority, injection, blocked work, integration gates, and resumability; and
5. measured benefit greater than the coordination and review cost.
