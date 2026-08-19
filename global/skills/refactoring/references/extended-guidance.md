# Refactoring Evidence and Migration Guidance

## Contents

- [Assess a structural problem](#assess-a-structural-problem)
- [Preserve behaviour under weak observability](#preserve-behaviour-under-weak-observability)
- [Keep repair and refactor distinct](#keep-repair-and-refactor-distinct)
- [Replace a legacy path safely](#replace-a-legacy-path-safely)
- [Decide on rewrite versus incremental change](#decide-on-rewrite-versus-incremental-change)
- [Review the result](#review-the-result)

## Assess a structural problem

Name a concrete cost before changing structure. Use evidence that exists: repeated incident classes, blocked feature work, fragile ownership, duplicated business decisions, change frequency, support burden, or a known inability to test a boundary. Do not convert aesthetic dislike into fabricated economics.

Inspect these lenses only when relevant:

| Lens | Decision it informs |
| --- | --- |
| Behaviour and consumers | What must remain unchanged, and who can observe a regression? |
| Ownership and seams | Can one bounded responsibility move without changing unrelated authority? |
| Duplication | Is the same concept changing for the same reason, or are similar lines about to diverge? |
| Lifecycle and state | Would extraction alter initialization, ordering, retries, disposal, or concurrency? |
| Source of truth | Is a file generated, mirrored, cached, or governed by a schema/migration? |
| Reversibility | Can a bad step be safely reversed, and does reversal recover data as well as code? |

Prefer the smallest change that removes the named cost. Avoid a generalized architecture until the concept, variation, and ownership boundary are stable enough to make the code clearer.

## Preserve behaviour under weak observability

First distinguish what is known from what is merely untested.

1. Inspect callers, outputs, stored state, telemetry, fixtures, and user-visible paths.
2. Capture current observable behaviour with a focused regression or characterization check where it can credibly observe the relevant mechanism.
3. Label a characterization check as **current behaviour**, not as a statement that the behaviour is correct or desirable.
4. Combine static/type evidence, narrow diff inspection, and focused manual observation when automation is incomplete.
5. Escalate rather than proceed autonomously when an unobservable path is security-sensitive, destructive, persistent, externally visible, or business-critical.

Do not demand a full harness for an isolated mechanical correction. Do not use the absence of a full harness as permission to alter an important unknown behaviour blindly.

## Keep repair and refactor distinct

Separate a behaviour-preserving structural change from a repair by default. This makes review, rollback, and diagnosis clearer.

Combine them only when the repair cannot be made safely without the structural change. In that case, record:

```text
Structural claim:
Behavioural repair claim:
Why separation is unsafe or misleading:
Evidence for each claim:
Recovery limit:
```

Do not conceal a repair as cleanup. Do not force an artificial separation that duplicates a dangerous path, misrepresents the safe change, or produces a temporary architecture that must immediately be discarded.

## Replace a legacy path safely

Use a staged replacement only when it reduces risk relative to in-place change. Define:

1. The old and new sources of truth.
2. The seam and the exact traffic, read, or write path being moved.
3. The observation that compares outcomes without exposing private data unnecessarily.
4. The rollback **and** data-recovery limit. A code rollback does not reconstruct lost or transformed data.
5. The owner, expiry, and consistency model of every temporary compatibility path.
6. The retirement condition that permits deletion of the old path.

Do not route live traffic, alter production data, or make an external cutover without the applicable workflow and explicit approval. A local simulation or proposal is not authorization.

For generated artifacts, verify generator, version, configuration, and source input. Change source first when possible. Regenerate deterministically and inspect the generated output for unexpected scope; do not treat a generated diff as automatically safe or automatically bad.

## Decide on rewrite versus incremental change

Prefer incremental refactor or bounded replacement when the current system contains valuable, partly undocumented business behaviour and a seam can be found.

Treat a rewrite proposal as a decision requiring evidence, not relief from frustration. Record:

- The current requirement the existing architecture cannot satisfy.
- Alternatives evaluated, including scoped refactor, adapter, seam extraction, and staged replacement.
- Known and unknown behaviour that could be lost.
- Migration, recovery, validation, and retirement plan.
- Who approves the irreversibility and external impact.

Do not use a generic duration multiplier, a fixed debt percentage, or the phrase “too messy” as proof.

## Review the result

Before handoff, confirm:

- The structural claim and the actual diff still match.
- Behavioural changes are separately labelled or explicitly justified as inseparable.
- Evidence covers the meaningful consumers and boundary risks, not only the moved implementation.
- Generated output, data migration, compatibility paths, and deletion conditions have named sources of truth.
- Unknowns and residual risks are visible.

Use `review-audit` for actual-base inspection and a fresh review pass where the change is nontrivial or crosses a meaningful boundary.
