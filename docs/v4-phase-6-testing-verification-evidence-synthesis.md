# V4 Phase 6 - Testing and verification evidence synthesis

**Status:** completed research-to-asset batch  
**Date:** 2026-08-18  
**Scope:** `testing`, `test-strategy`, and `verify-project` only. This batch does not alter security review, database migration, release execution, or project-specific test commands.

## Decision

Testing and verification are rebuilt around **risk-sized, interpretable evidence**. The OS must identify the claim, change surface, boundary, failure consequence, reversibility, and maintenance cost before choosing the smallest credible set of checks. A green command is execution evidence, not automatically a verification or release conclusion.

## Evidence assessment

The supplied **Manus** report is the primary source. It has the strongest discipline around evidence scope, uncertainty, durable versus project-specific guidance, security/release boundaries, and the distinction between test strategy and verification interpretation.

The supplied **Grok** report makes two useful supporting contributions:

1. its practical evidence matrix for API, migration, authorization, queue/cache/time, AI, UI, and high-impact release changes; and
2. adversarial fixtures that catch coverage worship, mock-only confidence, retry-until-green behavior, empty migration checks, and one-example AI evaluation.

The supplied **Gemini architecture** report is not a testing report and has a weak secondary-source bibliography. Its only adopted contribution is the compatible split between deterministic system guarantees, probabilistic AI behavior evaluation, and human/domain review. It does **not** justify fixed evaluation-set sizes, blanket CI release blockers, a dual-LLM pattern, or any architecture rewrite in this testing batch.

The limited durable external references were checked on 2026-08-18:

- [Google SRE canarying releases](https://sre.google/workbook/canarying-releases/) defines a canary as partial, time-limited evaluation against a control; V4 therefore treats it as additional, attributable release evidence rather than automatic proof.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) supports technical security-control verification; V4 keeps security conclusions in `security-audit`, not ordinary testing.
- [NIST SSDF](https://csrc.nist.gov/projects/ssdf) supports risk-, cost-, feasibility-, and applicability-sensitive secure development; V4 avoids one universal release checklist.
- [Microsoft consumer-driven contract testing guidance](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/cdc-testing/) supports contract testing as a complement to broader integration evidence, not a replacement for it.

## What changed

| Asset | Change | Reason |
| --- | --- | --- |
| `global/skills/testing/SKILL.md` | Replaced pyramid/trophy prescriptions and generic testing guidance with claim/risk/boundary selection, credible-oracle design, explicit status language, handoffs, and an evidence record. | Make the skill improve evidence selection rather than repeat generic test advice. |
| `global/skills/testing/references/` | Replaced one oversized mixed reference with four conditional references: evidence selection, oracles/stability, AI evaluation, and release evidence. | Preserve useful depth while avoiding needless load and stale stack-specific rules. |
| `global/skills/testing/evals/` | Added ten behavior scenarios, including authorization, cache, migration, flaky check, AI feature, high-impact release, and a low-risk control. | Evaluate false-confidence reduction and proportionality, not test-plan length. |
| `global/workflows/workflow-test-strategy.md` | Rebuilt as v2 planning/review/implementation coordination with project-adapter discovery and explicit authority. | Separate planning from release claims and prevent silent test edits in review/propose work. |
| `global/workflows/workflow-verify-project.md` | Rebuilt as v2 read-only evidence gathering/interpretation with four status outcomes and correct handoffs. | Replace the stale generic scanner checklist, fixed thresholds, and implicit release posture. |
| `global/skills/testing/agents/openai.yaml` | Updated Codex-facing skill metadata. | Keep host discovery aligned with the new capability. |

## Preserved, moved, and rejected rules

### Preserved and strengthened

- Test observable behavior and important invariants, not implementation accidents.
- Use lower-cost checks when they truly cover the risk; bring in realistic boundary evidence when they do not.
- Treat mocks as useful isolation tools with explicit limits.
- Keep regression defense, negative cases, repeatability, and actionable evidence important.
- Keep manual/exploratory, security, operational, product/UX, and accessibility evidence as distinct needs when they change the claim.

### Moved into selective references

- API/contract, persistence, queue/cache, concurrency, migration, authorization, UI, and high-impact evidence choices.
- Oracle quality, mocks, coverage interpretation, regression checks, fault sensitivity, and flakiness.
- AI-feature evaluation and progressive release/canary evidence.

### Explicitly rejected

- Fixed unit/integration/E2E ratios, a mandatory pyramid/trophy shape, or fixed counts of critical journeys.
- Universal coverage, mutation, timeout, retry, or canary thresholds.
- “Every bug must receive exactly one unit test,” “always mock,” “always use live services,” or “always test through the UI.”
- A green scanner, type check, coverage report, browser run, or CI pipeline as automatic security, release, or production-safety proof.
- Retrying an unstable check until it passes, hiding skipped/blocked work, or using an LLM judge as the sole high-impact oracle.
- Fixed evaluation task counts and blanket CI release blockers from the Gemini architecture report.

## Boundary with adjacent workflows

- `debug-issue` owns causal diagnosis; this package protects an already understood behavior and evaluates evidence, not root cause.
- `security-audit` owns security-specific verification and conclusions.
- `database-migration` owns migration execution/safety planning.
- `ship-to-production` owns external rollout and just-in-time approval. `verify-project` remains read-only and can only recommend a route/status.

## Verification plan and result

The batch is validated for portable skill metadata, conditional resource discovery, link integrity, no stale/unresolved tokens or personal paths, workflow schema/state/route compatibility, mode-specific mutation boundaries, and behavior scenarios that distinguish proportionate evidence from false confidence.

Repository validation and the complete unit suite are run after this batch. The standalone skill validator is still unavailable because its Python dependency on `PyYAML` is absent; no package is installed for a documentation validator.

## Phase-6 result

All four focused research-to-asset gates are now complete: Product Thinking, Project Inception, Debugging, and Testing/Verification. The next step is not more blind rewriting. It is a cross-asset integration review and real-task drill design to test whether the four updated packages route, cooperate, and stop at authority boundaries correctly in actual work.
