---
name: review-audit
description: 'Use when reviewing a pull request, branch, patch, module, implementation handoff, or legacy area for correctness, security, maintainability, and architecture. Activate for “review this”, “audit this code”, “check before merge”, “what is wrong here”, “review the PR”, or “inspect this diff”. Do not use to implement the change, diagnose an unexplained runtime fault, or authorize a deployment, external action, or destructive operation.'
---

# Review Audit

## WHEN TO USE THIS

- Review a meaningful implementation change, code branch, or generated output.
- Run a fresh self-review or Assurance-agent review before a handoff or release decision.
- Audit a legacy area where correctness, risk, or maintainability is uncertain.

## NEVER DO

- Assume `main`, a three-dot diff, a line-count threshold, or a branch naming convention is the right review scope.
- Reject a large change only because it is large, or accept a small change merely because it is small.
- Rewrite the work while claiming to review it.
- Treat a green test suite as proof that every affected boundary is safe.
- Approve, deploy, publish, or authorize external effects outside the authority granted by the user and host.

## ESTABLISH THE REVIEW QUESTION

Before line-level inspection, identify:

```text
Objective and non-goals:
Expected behavioural change and preserved behaviour:
Target/base and actual review comparison:
Changed modules, contracts, stores, generated outputs, and external effects:
Highest-risk assumptions and recovery limit:
Evidence already available and its limits:
Decision requested:
```

When the target, history, or review scope is unclear, inspect status, history, merge base, and repository tooling before choosing a comparison. Use the comparison that answers the actual question. Record excluded commits, generated outputs, and unrelated changes.

## REVIEW BY RISK, NOT RITUAL

| Condition | Review focus |
| --- | --- |
| Reversible local edit | Verify the narrow diff and applicable parse, render, lint, or static evidence. Do not invent a full review ceremony. |
| Local implementation or configuration | Reconstruct the claim, inspect sibling patterns and consumers, test the highest-risk assumption, and assess the evidence scope. |
| Ordinary feature or changed boundary | Trace the meaningful input, state, output, failure, and consumer path. Check local tests plus integration, contract, or UI evidence where the risk lives. |
| Legacy or weakly tested code | Separate observed behaviour from desired behaviour. Look for omitted consumers and state what remains unknown. |
| Auth, sensitive data, public contract, migration, billing, production, or irreversible path | Require negative and boundary evidence, recovery limits, appropriate specialist review, and the required human approval before any external effect. |

Review a generated or cross-cutting change by source of truth, determinism, semantic scope, and evidence. Decompose a diff when unrelated concepts hide one another; retain a coherent larger change when split commits would make the real behaviour less inspectable.

## RUN A FRESH REVIEW PASS

For a nontrivial, cross-boundary, or release-bound change, reconstruct the change surface independently before reading the builder’s conclusion. Inspect callers, consumers, error paths, state transitions, dependency facts, generated sources, and boundary assumptions that could invalidate the claim.

Use an Assurance agent or another distinct reviewer when configured and useful. Otherwise run a deliberately fresh review pass that challenges the implementation’s assumptions. Do not make an unavailable second agent a hard blocker for low-risk or reversible work.

## SEPARATE SPECIFICATION FROM STANDARDS

For a branch, pull request, or material implementation review, evaluate two
independent questions:

1. **Specification:** Does the change implement the requested behaviour, preserve
   stated non-goals, and avoid unapproved scope?
2. **Standards:** Does it satisfy applicable repository contracts, architecture,
   security, maintainability, and quality rules?

Keep findings under those separate headings so a standards-clean implementation
cannot hide a missed requirement, and a spec-correct implementation cannot hide
a repository violation. Run bounded parallel reviewers only when both axes are
substantial, their scopes are disjoint, and the host provides safe delegation;
otherwise review them sequentially. Never require an issue tracker, a fixed diff
shape, or a subagent when the actual review evidence is available another way.

## CLASSIFY FINDINGS AND STOP

Use the standard severity scale:

| Severity | Meaning | Decision |
| --- | --- | --- |
| `critical` | Credible security breach, data loss/corruption, uncontrolled external effect, or total failure of the claim | Block. Escalate immediately. |
| `high` | Material incorrectness, boundary failure, recovery gap, or architecture violation | Require correction or explicit authorized acceptance. |
| `medium` | Important maintainability, coverage, reliability, or clarity issue with bounded consequence | Require correction when it materially affects this decision; otherwise record as follow-up. |
| `low` | Useful non-blocking improvement or polish | Do not let it obscure material findings. |

Stop when the meaningful failure surface has credible evidence, material findings are resolved or explicitly accepted by the authorized person, and residual uncertainty is visible. Do not continue broad cleanup merely to appear thorough.

## REFERENCE LOADING RULES

- Load [change-scope-and-handoff.md](references/change-scope-and-handoff.md) for uncertain branch topology, builder-to-reviewer handoff, generated output, migration/recovery, or a mixed mechanical-and-behavioural diff.
- Use `testing` to interpret evidence adequacy; do not substitute review comments for tests.
- Use `security-audit`, `database-migration`, `dependency-upgrade`, or `ship-to-production` only for their actual triggers and approval gates.

## OUTPUT SHAPE

```text
Review scope and actual comparison:
Overall decision: approve | changes required | blocked | residual-risk handoff
Findings: severity, evidence, consequence, recommended action
Evidence reviewed and false-confidence limits:
Resolved, accepted, and unresolved risk:
```

## NON-NEGOTIABLE CHECKLIST

1. Review the intended outcome and actual comparison before judging the diff.
2. Trace the highest-risk boundary, not only the happy path.
3. Distinguish mechanical movement from behaviour change and generated output.
4. Classify findings by consequence and evidence.
5. Never imply release, deployment, or approval authority that the review does not have.
