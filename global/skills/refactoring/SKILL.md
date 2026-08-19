---
name: refactoring
description: 'Use when changing code structure while intending to preserve observable behaviour, reducing technical debt, extracting a seam, removing dead paths, or deciding between incremental refactor, replacement, and rewrite. Activate for “refactor”, “clean up”, “technical debt”, “make this maintainable”, “dead code”, “modernize”, or “rewrite versus refactor”. Do not use for a known defect or feature change as the primary task (use coding), unexplained failure diagnosis (use debugging), or review-only work (use review-audit).'
---

# Refactoring

## WHEN TO USE THIS

- Improve structure without intending to change an observable contract.
- Reduce a named source of maintenance, reliability, delivery, or comprehension cost.
- Plan an incremental modernization, replacement seam, or rare rewrite decision.

## NEVER DO

- Call a behaviour change a refactor.
- Require a perfect test harness before every low-risk mechanical change.
- Treat a characterization test as proof that current behaviour is desired behaviour.
- Combine refactor and repair without exposing the dependency and distinct evidence.
- Replace a working system merely because its domain is unfamiliar or its code looks old.
- Leave dual-write or dual-authoritative paths without an explicit, verified retirement plan.

## DEFINE THE STRUCTURAL CLAIM

State the structural problem, its practical cost, the intended unchanged behaviour, and the smallest scope that reduces the cost. A precise measure is useful when available; do not invent defect rates, time savings, or business impact merely to make the case sound stronger.

Decide which task is actually present:

| Task | Required treatment |
| --- | --- |
| Mechanical refactor | Preserve behaviour. Select the cheapest credible structural and behaviour evidence. |
| Refactor plus repair | Separate by default. Combine only when the repair depends on the structural change; label both claims and test both. |
| Preparatory refactor for a feature | State the feature as a non-goal until its own behavioural change begins. |
| Replacement or migration | Identify the source of truth, cutover, recovery limit, observability, and retirement condition. |
| Rewrite proposal | Prove why incremental change or a seam cannot meet the current need; identify undocumented behaviour at risk. |

## CHOOSE EVIDENCE BY RISK AND OBSERVABILITY

Use `testing` to select evidence. Do not use a single blanket gate.

- For a reversible rename, move, formatting correction, or dead local branch: inspect references, compile/type-check or parse when applicable, and review the narrow diff.
- For a behaviour-sensitive or cross-boundary refactor: establish focused regression or characterization evidence where practical, then verify the affected consumers and boundaries.
- For legacy code with incomplete tests: observe and characterize relevant current behaviour, stage the smallest change, state unknowns, and escalate when critical behaviour cannot be observed credibly.
- For persistence, authorization, migration, generated code, or externally visible paths: load the applicable conditional guidance and treat recovery as a separate claim from code rollback.

## MAKE THE CHANGE REVIEWABLE

1. Inspect callers, consumers, contracts, generated sources, and deletion candidates before moving code.
2. Make changes in coherent slices. A slice may be large when deterministic generation or one cross-cutting semantic change makes it inspectable; line count alone is not a verdict.
3. Keep mechanical movement, behaviour changes, generated output, and migration effects distinguishable in the diff or handoff.
4. Remove retired paths only after the replacement is verified against the actual retirement condition. Keep a temporary compatibility path only when its owner, expiry, and data-consistency risk are explicit.
5. Stop and reassess when the changed surface, recovery limit, or known behaviour differs materially from the initial claim.

## REFERENCE LOADING RULES

- Load [extended-guidance.md](references/extended-guidance.md) for legacy code, characterization strategy, migrations, generated output, strangler-style replacement, or a rewrite decision.
- Use `review-audit` when a structural change needs a fresh independent reasoning pass or review base inspection.
- Use `security-audit`, `database-migration`, `dependency-upgrade`, or `ship-to-production` only when their actual trigger is present; refactoring does not grant authority for external effects.

## OUTPUT SHAPE

```text
Structural problem and intended unchanged behaviour:
Scope, non-goals, and chosen strategy:
Evidence selected and actual result:
Recovery/retirement limit:
Residual uncertainty and required handoff:
```

## NON-NEGOTIABLE CHECKLIST

1. Separate structural and behavioural claims.
2. Match evidence to the changed failure surface and current observability.
3. Keep the meaningful diff and retirement condition inspectable.
4. State unknown legacy behaviour rather than pretending it is covered.
5. Escalate irreversible, data-sensitive, security-sensitive, or production effects.
