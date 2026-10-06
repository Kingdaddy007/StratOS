---
name: tdd
license: MIT
description: >
  Implement behavior through a focused red-green-refactor cycle at public interfaces. Activate on `/tdd`, "test first", "red green refactor", a requested regression test, or a nontrivial approved implement-spec ticket with a stable testable boundary. Do not use for review-only work, trivial reversible documentation/formatting, speculative tests, or permission to install a test framework.
---

# Test-Driven Development

## WHEN TO USE THIS

- Build approved behavior test-first through an observable public interface.
- Fix an established bug with a regression test that demonstrates the failure.

## NEVER DO

- Write a test that merely reproduces the implementation or passes by construction.
- Mock away the very boundary whose behavior is under test.
- Add a new framework or dependency without the required authorization.
- Treat a setup/import error as the intended failing behavior.
- Force a user confirmation for a boundary already settled by the approved spec and existing tests.
- Replace changed service, persistence, device, or UI evidence with a mocked unit-test claim.

## CHOOSE THE BOUNDARY AND ORACLE

Use [testing](../testing/SKILL.md) to select the evidence level and interpret its limits. Inspect nearby tests and native check commands. Identify the public input, output, meaningful failure case, and expected result from the spec, a known-good literal, a worked example, or a domain invariant.

Use the approved acceptance criteria and established interfaces to select the seam. State it briefly; ask only when an unresolved choice materially changes scope or architecture. Use [architecture](../architecture/SKILL.md) when boundary ownership is genuinely unresolved; use [api-design](../api-design/SKILL.md) only for an actual API contract decision. Do not add an upstream vocabulary dependency solely to define "public interface".

For legacy bugs, distinguish observed current behavior from the requested correction. Load [debugging](../debugging/SKILL.md) when the mechanism is still unknown. Match terminology to relevant project context, glossary, and ADRs.

## WORK ONE VERTICAL SLICE

1. **Red:** Write one behavioral test at the chosen public boundary. Run it and verify it fails for the intended missing or wrong behavior. Record the command and observed failure; fix broken test setup before interpreting the result.
2. **Green:** Implement the smallest coherent behavior that passes the test. Handle relevant failure paths; avoid speculative features or abstractions.
3. **Refactor:** Improve structure within the approved scope while the behavior tests stay green. Separate a material structural change when it improves review or rollback; do not defer obviously necessary clarity until a separate review ceremony.
4. Repeat from the next acceptance criterion or plausible failure case. Let each result inform the next slice instead of writing a speculative bulk suite.
5. Run relevant neighboring tests, type/static checks, and changed-boundary evidence. Confirm the test rejects a representative wrong result when its sensitivity is uncertain. Report unavailable integration checks separately.

Mock only boundaries outside the claim. Use realistic contract fixtures and explicit limitations. Avoid private-method assertions, internal call choreography, self-generated snapshots, arbitrary sleeps, and coverage targets without a failure rationale. Do not query an implementation side channel when the public interface can establish the result; inspect storage directly only when storage integrity is itself the requirement.

## OUTPUT SHAPE

```text
Acceptance criterion, public boundary, and independent oracle:
Red: command and intended observed failure
Green/refactor: change and passing result
Neighboring/boundary checks and limitations:
```

## NON-NEGOTIABLE CHECKLIST

1. Trace each test to observable requested behavior.
2. Observe the intended red result before claiming a test-first cycle.
3. Derive expectations independently of the implementation.
4. Keep refactoring green and within scope.
5. State mock and integration limits.
