---
name: testing
description: 'Use when choosing, creating, reviewing, running, or interpreting test and verification evidence for a software or AI-feature change. Selects risk-sized behavior, boundary, and release evidence without mistaking green checks for proof. Do NOT use to diagnose an unexplained failure before its mechanism is understood (use debugging), or to authorize a release, deployment, or security decision.'
---

# Testing and verification

## Purpose and boundary

Testing is evidence selection under risk, not the production of a green pipeline. Start from the claim that matters, the failure that would matter, the boundaries exposed by the change, and the cheapest evidence that could credibly disprove a plausible but wrong implementation.

A passing check proves only the observation it exercised in its stated environment. Coverage is a scope signal, not a quality certificate. Static checks and type checks cheaply detect some defects; they do not prove runtime behavior, release readiness, security assurance, product acceptance, or production equivalence.

This skill chooses and interprets evidence. It does not authorize a release, conduct a threat model, deploy, or turn an unexercised environment into a successful result.

## Start with claim, risk, and boundary

For each material change, name:

1. **Claim:** the observable behavior, invariant, or outcome that must hold.
2. **Failure cost:** user, data, security, operational, financial, legal, or trust consequence if it is wrong.
3. **Change surface:** code, API, schema, configuration, dependency, prompt/model, retrieval, tool policy, or deployment path affected.
4. **Boundary exposure:** persistence, network, serialization, authorization, queue/cache, time, concurrency, browser, external provider, or production environment.
5. **Reversibility and maintenance cost:** how safely failure can be undone, and what it costs to keep proposed evidence trustworthy.

Select the smallest evidence set that is credible for that combination. A test pyramid or testing trophy can help compare cost and realism, but neither is a universal target or ratio.

## Core evidence loop

1. **Frame the claim and risk.** Separate a local behavior claim from broader compatibility, safety, operational, or release claims.
2. **Map behavior and boundaries.** Include success, meaningful negative, failure, and state-transition cases that could violate the claim.
3. **Choose evidence deliberately.** Use focused behavior tests for local logic; add integration, contract, browser, property, exploratory, operational, or AI evaluation evidence only when the risk lives at those boundaries.
4. **Design a credible oracle.** Assert observable behavior or invariants, not private implementation accidents. State what a mock, snapshot, heuristic, or model judge cannot establish.
5. **Execute and classify honestly.** Record actual commands/checks, environment, inputs/fixtures, results, skipped or blocked work, and flaky/nondeterministic behavior. Do not claim work that was not run.
6. **Interpret, do not merely count.** State which claim is supported, which boundaries remain untested, and whether more evidence, a specialist handoff, or a release route is needed.

For a bug already understood through `debugging`, a regression test should protect the observable mechanism or invariant and, when feasible, fail against the original fault. It should remain meaningful after a sensible refactor; it is not a ritual requiring one unit test for every bug.

## Choose a status that matches the evidence

| Status | Meaning |
| --- | --- |
| `verified for scope` | Credible evidence exercised the stated claim and relevant known boundary for the declared risk. It does not imply untested environments or release approval. |
| `verified with residual risk` | Meaningful evidence exists, but an important production-only, external, representative-data, or otherwise untested uncertainty remains visible. |
| `blocked` | A required check failed, cannot safely run, or an approval/risk gate remains unresolved. |
| `unverified` | Evidence is absent, inconclusive, non-representative, flaky, or insufficient for the claim. This is not a synonym for failure and must never be upgraded silently to success. |

## Required handoffs

- Use `debugging` for a failing or flaky result whose cause is not established; do not retry until green and call that verification.
- Use `security-audit` for authorization, identity, tenant/object isolation, secrets, sensitive data, injection, command/file execution, dependency provenance, cryptography, or model/tool permission changes. Ordinary test success is not a security decision.
- Use `verify-project` to gather and interpret project/release evidence. Its conclusion is not deployment approval.
- Use `ship-to-production` only for a requested release; production rollout and external effects require its just-in-time approval gate.
- Use Product, UX, accessibility, performance, or domain review when the meaningful claim is not purely a technical contract.

## Load detail only when it changes the decision

- For risk sizing, test-level selection, contracts, migrations, queues/caches, authorization, or UI journeys, read [evidence-selection.md](references/evidence-selection.md).
- For behavior/invariant design, mocks, coverage, mutation/property checks, regression evidence, or flakiness, read [oracles-and-stability.md](references/oracles-and-stability.md).
- For model, prompt, retrieval, tool-use, or agent changes, read [ai-feature-evaluation.md](references/ai-feature-evaluation.md).
- For project verification, release interpretation, monitoring, canary evidence, or status language, read [release-evidence.md](references/release-evidence.md).
- For routing and source verification dates, read [resource-index.md](references/resource-index.md).
- For behavioral evaluation of this package, read [testing-scenarios.md](evals/testing-scenarios.md).

## Return a traceable verification record

```text
Claim and risk:
Changed surface and boundaries:
Evidence selected: check, reason, environment/fixture, actual result, scope covered
Oracle and false-confidence limits: what a green result does not establish
Flaky, skipped, blocked, or unrun checks:
Status: verified for scope | verified with residual risk | blocked | unverified
Residual uncertainty and recommended handoff:
```

## Non-negotiable checks

- Do not claim release readiness from coverage, a scanner, a single green command, or one successful browser run.
- Do not test a mock and claim the real boundary is verified.
- Do not use an LLM judge as the sole oracle for high-impact behavior.
- Do not hide skipped, quarantined, environment-blocked, or flaky checks.
- Do not use production services, credentials, personal data, or destructive operations for routine tests without explicit authorization and isolation.
