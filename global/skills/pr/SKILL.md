---
name: pr
license: MIT
description: >
  Write or improve a pull request description with a clear change summary, concrete evidence, and merge risk. Activate on `/pr`, "write the PR body", "prepare a pull request", or a requested implementation handoff that includes a PR. Do not use for code review, feature implementation, or permission to create, publish, merge, or deploy a PR.
---

# Pull Request Description

## WHEN TO USE THIS

- Draft or update the body of a requested pull request.
- Explain a finished change to a reviewer using verified artifacts and execution evidence.

## NEVER DO

- Invent a before result, test run, screenshot, rollout result, or rollback guarantee.
- Treat writing the body as authorization to publish, mark ready, merge, or deploy.
- Force diagrams or lengthy risk sections into a trivial change.
- Treat a screenshot or passing build as proof of an interaction or live service.

## WRITE FOR THE REVIEW DECISION

1. Inspect the actual final diff, requested behavior, repository PR template, and available checks. Lead with the concrete problem and resulting behavior. Rewrite stale descriptions when scope changes.
2. Follow the repository's required template. Otherwise use Summary, Evidence, and Merge Risk; combine them into a short paragraph for a small change.
3. Use the smallest view that clarifies the change: prose, a before/after example, pseudocode, a shallow call/file/component tree, a diff sketch, or Mermaid. Place a visual next to its explanation. Label sketches so they cannot be mistaken for executed code or exact diffs.
4. Use the project's actual terminology. Read a relevant `GLOSSARY.md`, or follow `GLOSSARY-MAP.md` to the correct domain. Use an existing legacy domain `CONTEXT.md` when it is still authoritative; do not rename project documents during PR writing.
5. Report the exact checks run, observed outcome, and relevant environment limits. Include before/after evidence when available. State "before evidence unavailable" when it was not captured; do not manufacture a failing test after the fact.
6. Match evidence to the claim. Use screenshots for appearance, interaction checks for behavior, and integration evidence for changed service or persistence boundaries. Identify mocks and local-only evidence. Use [testing](../testing/SKILL.md) if evidence adequacy is uncertain.
7. Describe reversibility and the affected users, modules, data, contracts, or operational paths. Treat destructive migrations and incompatible writes as potentially hard to undo. Explain the recovery limits; a Git revert alone may not restore data.
8. Name material unresolved risk and required follow-up. Keep routine check output out of the prose. Save or publish only within the user's authorized scope; use [code-review](../code-review/SKILL.md) when the change needs review rather than better wording.

## OUTPUT SHAPE

```markdown
## Summary
<problem and resulting behavior; optional compact visual>

## Evidence
<checks and observed results; before/after when available; limitations>

## Merge Risk
<affected surface; reversibility and recovery limits; unresolved concerns>
```

## NON-NEGOTIABLE CHECKLIST

1. Describe the final implementation and match the repository template.
2. Separate observed evidence from sketches and expectations.
3. State material impact and recovery limits.
4. Keep publication and release authorization separate from writing.
