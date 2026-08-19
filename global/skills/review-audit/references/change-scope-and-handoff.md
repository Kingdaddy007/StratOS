# Change Scope and Review Handoff

## Contents

- [Choose the actual comparison](#choose-the-actual-comparison)
- [Read a builder handoff](#read-a-builder-handoff)
- [Inspect mixed and generated changes](#inspect-mixed-and-generated-changes)
- [Assess recovery and escalation](#assess-recovery-and-escalation)

## Choose the actual comparison

Do not select a Git command from habit. First establish the decision:

| Review question | Establish before comparison |
| --- | --- |
| What will this branch add to a named target? | Target branch, merge base, stacked-parent relationship, and excluded commits. |
| What changed since a release or incident? | Release/tag/commit boundary, hotfixes, generated outputs, and environment differences. |
| What is in an uncommitted local change? | Working tree, index, staged versus unstaged state, and unrelated local edits. |
| What did a migration or generator produce? | Source input, generator version/configuration, deterministic output, and semantic diff. |

Inspect repository status, relevant history, and merge-base semantics when the answer is not obvious. State the comparison used and why it fits. A three-dot comparison can be useful for a branch relative to its merge base, but it is not a universal review rule.

## Read a builder handoff

For a nontrivial change, request or reconstruct:

```text
Objective:
Non-goals:
Changed surface:
Behavioural claim and unchanged behaviour:
Highest-risk assumptions:
Evidence actually run and its coverage limits:
Recovery limit:
Questions the reviewer must decide:
Decision requested:
```

Test the handoff rather than echoing it. Search for omitted consumers, inconsistent sources of truth, dependency claims without local or authoritative support, and evidence that does not reach the claimed boundary.

## Inspect mixed and generated changes

Separate these concerns in the review:

- Mechanical movement, naming, formatting, and deletion.
- Intended behaviour change or defect repair.
- Generated outputs and their source inputs.
- Schema, migration, compatibility, or data transformation effects.

Ask whether the split is safe and meaningful. Require a distinct evidence statement for a combined refactor-plus-repair. Do not require artificial commit splitting when it hides the safe causal relationship or creates an unsafe intermediate state.

For generated output, verify the source of truth, generator/version/configuration, deterministic regeneration, and unexpected scope. For migration, distinguish code rollback from data recovery; a down migration does not recreate discarded or transformed data.

## Assess recovery and escalation

Escalate when the credible failure includes authorization bypass, data exposure, deletion or corruption, irreversible public contract change, billing effect, production traffic effect, or unrecoverable external action.

Require the relevant approval and recovery proof before the effect occurs. A reviewer can recommend an escalation or mark a change blocked; it cannot invent human authorization.

Record residual uncertainty in plain terms: what is unknown, why the current evidence cannot settle it, consequence if wrong, and the next safe action.
