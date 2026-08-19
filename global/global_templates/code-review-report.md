# TEMPLATE: CODE REVIEW REPORT

**Version:** Gold v1.1 (Master Merge)
**Layer:** 9 — Output Contract
**Tier:** 3 — Loaded on demand
**File:** templates/code-review-report.md
**Purpose:** Standardized format for delivering code review findings with consistent severity classification, explicit approval conditions, and actionable feedback. Ensures intent, risk, severity, and approval status are communicated consistently.
**Loaded When:** Delivering the output of a code review. Referenced by the `review-audit` skill.

***

## WHEN TO USE THIS TEMPLATE

Use this template when:

- Delivering a formal code review
- Reviewing a pull request or patch
- Auditing a module or codebase section
- Summarizing a review for handoff to authors or approvers
- Self-reviewing before delivery — use the abbreviated version

For quick review feedback with one or two findings, use inline comments instead of this full template.

***

## THE TEMPLATE

```markdown

# Code Review: [PR Title / Module Name / Change Description]

***

## Overview

| Field | Value |
| :--- | :--- |
| Author | [Who wrote the code] |
| Reviewer | [Who reviewed it] |
| Date | [YYYY-MM-DD] |
| Scope | [Files, modules, or PR reviewed] |
| Lines Changed | [Approximate] |
| Risk Level | [Low / Medium / High] |

***

## Intent of Change

<!-- What is this code trying to accomplish?
     Understanding intent before judging implementation. -->

[What the change is supposed to do and why]

## Affected Surface

- Files or modules: [list]
- Intended change: [summary]
- Critical paths touched: [list — auth, payments, data, etc.]
- Blast radius if wrong: [narrow / moderate / broad]

***

## Summary Assessment

<!-- One paragraph: what this code does, overall quality assessment,
     and whether it is ready to merge.

     Template:
     The change generally [meets / partially meets / does not yet meet]
     the expected quality bar. The main strengths are [x].
     The main concerns are [y]. -->

[Summary]

***

## Verdict

<!-- One of:
     ✅ Approve
     ✅ Approve with comments
     🔄 Request changes
     🚫 Block — critical issues must be resolved first -->

[Verdict]

***

## Findings

### 🔴 Critical — Must Fix Before Merge

<!-- Logic errors, security vulnerabilities, data corruption risks,
     broken functionality. Blocks merge without exception. -->

#### [Finding Title]

- **Location:** [file:line]
- **Issue:** [What is wrong]
- **Why it matters:** [Impact if not fixed]
- **Suggested fix:** [How to fix it]
- **Risk if ignored:** [What could go wrong in production]

***

### 🟠 High — Should Fix Before Merge

<!-- Missing error handling, architectural violations, significant
     unhandled edge cases. Blocks merge unless explicitly accepted. -->

#### [Finding Title]

- **Location:** [file:line]
- **Issue:** [What is wrong]
- **Why it matters:** [Impact if not fixed]
- **Suggested fix:** [How to fix it]
- **Risk if ignored:** [What could go wrong]

***

### 🟡 Medium — Recommended

<!-- Readability improvements, naming issues, missing test cases,
     minor convention violations. Does not block merge. -->

#### [Finding Title]

- **Location:** [file:line]
- **Suggestion:** [What could be improved]
- **Rationale:** [Why this would be better]

***

### 🟢 Low / 💬 Notes

<!-- Style suggestions, alternative approaches, questions,
     teaching moments. Does not block merge. -->

- [Observation or suggestion]
- [Observation or suggestion]

***

## Review Dimensions

### Correctness

[Does the code do what it claims? Key logic concerns or confidence notes.]

### Maintainability

[Naming, responsibilities, readability, long-term changeability.]

### Architecture Fit

[Boundary placement, layering, module ownership, consistency with existing patterns.]

### Security

[Input validation, auth, authz, data exposure, secret handling.]

### Performance

[N+1 queries, unnecessary re-renders, expensive operations in hot paths.]

### Testing

[Test coverage quality, behavior versus implementation testing, edge case coverage.]

### Readability and Clarity

[Variable names, function length, comment quality, domain vocabulary usage.]

***

## Security Checklist

- [ ] Input validation present where needed
- [ ] Authentication checked on all protected paths
- [ ] Authorization checked — role and resource ownership
- [ ] No sensitive data exposed in responses or logs
- [ ] No hardcoded secrets or credentials
- [ ] Error messages do not leak internal details

***

## Test Assessment

- [ ] Tests included for new or changed behavior
- [ ] Tests verify behavior, not implementation details
- [ ] Edge cases covered
- [ ] Tests pass in CI
- [ ] No flaky tests introduced

### Well Covered

- [Item 1]
- [Item 2]

### Coverage Gaps

- [Item 1 — what is missing and why it matters]

***

## Strengths

<!-- Acknowledge what was done well. This section is not optional.
     A review that only identifies problems misses important signal. -->

- [Strength 1]
- [Strength 2]
- [Strength 3]

***

## Approval Status and Conditions

**Status:** [Approve / Approve with caveats / Revise / Block]

### Approval conditions (must resolve before merge)

- [Condition 1]
- [Condition 2]

### Advisory items (can be merged with these noted)

- [Advisory 1]
- [Advisory 2]

***

## What Should Change Before Merge

1. [Required change 1]
2. [Required change 2]

## Optional Improvements

- [Optional improvement 1 — not blocking]
- [Optional improvement 2 — not blocking]

***

## Overall Notes

<!-- Any broader observations, patterns noticed, architectural
     considerations, or suggestions for follow-up work beyond
     the immediate findings. -->

[Notes]

***

## Follow-Up Items

- [Deferred improvement 1 — owner if known]
- [Deferred improvement 2 — owner if known]

***

## Related Files

- `skills/review-audit/SKILL.md`
- [contexts/...]
- [skills/...]

## Reviewer

[Name / team / system owner]
```

***

## SEVERITY QUICK REFERENCE

| Severity | Blocks Merge? | Examples |
| :--- | :--- | :--- |
| 🔴 Critical | YES | Auth bypass, SQL injection, data loss, logic error causing wrong results |
| 🟠 High | YES unless explicitly accepted | Missing error handling on external call, N+1 query in hot path, missing auth check |
| 🟡 Medium | NO | Unclear naming, missing test for edge case, inconsistent pattern usage |
| 🟢 Low | NO | Style preference, alternative approach suggestion, minor improvement |
| 💬 Note | NO | Question, observation, teaching moment |

***

## TONE GUIDANCE

Phrase feedback as suggestions, not commands:

- ✅ "What do you think about extracting this into a separate function for clarity?"
- ❌ "Extract this into a function."

Explain WHY, not just WHAT:

- ✅ "This catch block swallows the error silently — if the save fails, the user will not know. Consider showing an error state."
- ❌ "Add error handling."

Assume good intent:

- ✅ "I might be missing context — is there a reason this skips validation here?"
- ❌ "You forgot to validate the input."

Acknowledge strengths alongside problems:

- ✅ "The error handling pattern here is really clean and consistent with our conventions."

***

## FIELD GUIDANCE

- Severity must reflect real risk, not personal preference or emotional annoyance
- Make blocking versus advisory findings explicit — never leave the author guessing whether a finding blocks merge
- If context is missing, say how that limits confidence rather than pretending full certainty
- Strengths section is not optional — a review that only finds problems misses important signal and erodes trust
- Approval conditions should state exactly what must change, not vaguely reference "the issues above"
