# V4 Round 2 — Active Skill Audit

**Status:** source audit complete; no skill is rewritten by this audit.  
**Date:** 2026-08-19

## Decision standard

Keep a skill when its local method, reference material, safety boundary, or
routing rule improves a capable model's work. Do not keep a rigid or dated rule
just because it is old. Do not rewrite a skill until its evidence gate is met.

## Engineering and Assurance

| Skill | Audit finding | Decision |
| --- | --- | --- |
| `coding` | Good readability and failure handling base. Rigid parameter, abstraction, and universal-trace rules; no references or evals. | Revised 19 August 2026 from Prompt 1 evidence: risk-triggered change record, repository/dependency facts, inspectable behavioural claims, and failure-surface evidence. |
| `refactoring` | Good behavior-preservation and scope discipline. Overstates universal test, time-box, and replacement rules. | Revised 19 August 2026 from Prompt 1 evidence: risk-and-observability evidence selection, explicit combined-repair exception, and conditional legacy/migration guidance. |
| `review-audit` | Strong lenses. Incorrectly assumes `main...HEAD` and lacks risk-sized direct review routing. | Revised 19 August 2026 from Prompt 1 evidence: actual-base review, bounded fresh review, risk-sized findings, and explicit escalation limits. |
| `api-design` | Useful contract-first method. Versioning, pagination, rate limiting, and specification authority are overgeneralized. | Revised 19 August 2026 from Prompt 2 evidence: boundary/consumer classification, contract discrepancy handling, proportional compatibility/limits, retry/concurrency, and object/tenant/property authorization. |
| `database` | Useful integrity and migration thinking. Billion-row, 3NF, deployment, and soft-delete rules are overgeneralized. | Revised 19 August 2026 from Prompt 2 evidence: owner/invariant placement, evidence-led model choice, lifecycle distinction, proportional staged evolution, and explicit data recovery limits. |
| `performance` | Correctly starts with measurement. Universal p95/p99 and production-load requirements do not fit all work. | Revised 19 August 2026 from Prompt 3 evidence: harm-boundary measurement, labelled risk-scaled evidence, comparable baselines, cache/retry correctness, and explicit stopping/escalation. |
| `devops-infra` | Good reliability intent. IaC, secret manager, JSON logging, tracing, and automation are presented as universal baselines. | Revised 19 August 2026 from Prompt 3 evidence: proportional observability, actionable alerts, delivery/containment decisions, recovery reality, and approval before external effects. |
| `security` | Correct trust-boundary direction. Needs current primary-source grounding, risk sizing, and evaluations. | Revised 19 August 2026 from Prompt 4 evidence: Boundary-to-Evidence method, actor/resource/action security controls, untrusted AI-content handling, separate severity/confidence/impact evidence, and explicit residual-risk/approval boundaries. |

Tool adapters (`browser-test`, `dox`, `fallow`) remain conditional on host
availability. Procedures (`resolving-merge-conflicts`, `setup-pre-commit`) are
reviewed after the core Engineering set.

## Product, Growth, and Research

| Skill | Audit finding | Decision |
| --- | --- | --- |
| `research-analysis` | Sound decision framework. Missing V4 provenance, claim labels, project-context use, and evaluations. | Small V4-policy revision; no broad research required. |
| `sales-enablement` | Useful format knowledge, but had stale `.claude` paths, a fixed deck shape, unverified ROI language, and no external-claim boundary. | Revised 19 August 2026 from Prompt 5 evidence: claim classification and provenance, buyer-interpretation checks, scenario-only value modelling, evidence-gated proof, and just-in-time approval for external effects. |
| `page-cro` | Useful friction and experiment framing, but had five-second, above-fold, one-CTA, navigation-removal, and fewer-fields folklore. | Revised 19 August 2026 from the CRO evidence study: decision-first diagnosis, evidence and instrumentation gates, accessibility/privacy/autonomy protection, proportional method selection, and scoped experiment interpretation. |
| `competitor-profiling` | Valuable dossier concept, but hard-coded Firecrawl/DataForSEO, raw-data writes, and old paths. | Revised 19 August 2026 from Prompt 7 evidence: capability-first collection, access/privacy boundaries, claim-level provenance, fair comparison, proportionate corroboration, and explicit unknown/approval routing. |

Do not reopen the already revised Growth skills without a real contradiction or
pilot result: `copywriting`, `copy-editing`, `expert-positioning`,
`marketing-psychology`, `prospect-research`, and `offer-architecture`.

## Studio Support

| Skill | Audit finding | Decision |
| --- | --- | --- |
| `deep-think` | Core reasoning files remain useful. Persistent full-depth mode, forced visible traces, and mandatory three options conflict with risk-sized thinking. | Revise from the V4 operating model; no external research required. |
| `learn` | Has a sound audit/apply boundary and explicit approval for capability mutation. | Keep; validate through a real completed-project learning pilot. |
| `context-formatting` | Narrow, broken Markdown-lint recipe with stale Gold-Context framing. | Demote to host-specific procedure or archive. |
| `to-tickets` | Useful ticket structure, but vertical-only slicing, fixed token limits, and publication handling are too rigid. | Revise from V4 policy and a local fixture. |
| `wizard` | Bash-only, secret-handling, auto-opening, and GitHub-secret behaviour conflicts with Windows-first portability and approval rules. | Replace or archive before host installation. |
| `skill-creator` | Current package/refactoring guidance is sound. | Keep; verify as each successor skill is rewritten. |

## Outcome

No skill was deleted. The next revision batch is driven by the focused prompts
in the next delivery, then by routing and behavior tests. New skills are not
assumed necessary.
