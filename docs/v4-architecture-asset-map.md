# V4 Architecture Asset Map

**Status:** current-state mapping and future design input; no skills or workflows changed  
**Date:** 2026-08-18  
**Purpose:** compare the evidence map to the Anti-Gravity source that already exists, so we preserve strong work instead of rebuilding blindly.

## Executive result

Anti-Gravity already contains most of the **general product architecture** capabilities. The main issue is not an absence of engineering thought. It is that parts of the source are too long, overlap, and do not yet have a clear V4 relationship to the Studio Director and five functional boundaries.

There is **no dedicated AI-native product architecture package**. That is a real gap only for products whose users interact with AI. It should be built as a small conditional extension, not imposed on normal engineering work.

The existing `prompt-engineering` skill is explicitly for image and video prompts. It is not a substitute for architecture of a user-facing LLM/AI product.

## General architecture coverage

| Evidence-map capability | Current source that already carries it | Current assessment | V4 action later |
| --- | --- | --- | --- |
| Product and risk framing | `product-thinking`; `workflow-project-inception` | Strong purpose/scope material exists | Clarify its handoff to the Product & Strategy boundary; reduce duplication where needed |
| Quality attributes and trade-offs | `architecture`; `workflow-plan-architecture`; architecture context template | Strong architectural lenses exist, including reversibility, failure, and operability | Make the quality-attribute output more explicit and proportional; do not create a separate skill yet |
| Boundaries, ownership, and data lifecycle | `architecture`, `database`, `api-design`; architecture/database/API context templates | Strong coverage, but the templates are much larger than active project truth should be | Split stable guidance from blank project fields; do not turn templates into assumed facts |
| Contracts and failure behaviour | `api-design`, `database`, `debugging`; API design and build-feature workflows | Strong coverage of contracts, auth, compatibility, error paths, and idempotency | Repair/normalise routes and cross-links during the skill/workflow reform, not now |
| Trust, privacy, and security | `security`; authority-and-trust baseline; security baseline/context; security-audit workflow | Strong policy foundation already exists | Keep it central. Add AI-specific threats only to the optional AI layer, not globally |
| Change, migration, and release safety | `database`, `refactoring`, `devops-infra`; database-migration, dependency-upgrade, ship-to-production workflows | Strong, explicit migration/recovery/approval controls | Keep. Ensure only the relevant projects pay the full release/migration cost |
| Operability and recovery | `devops-infra`, `performance`, `debugging`; incident-response and performance workflows; infra context | Strong coverage of observability, incident response, blast radius, and recovery | Consolidate duplicated instructions and keep project-specific operational truth outside global templates |
| Evidence and independent assurance | `testing`, `review-audit`, `security`; verify-project, review-code, security-audit workflows | Strong cross-checking foundation | Improve the distinction between baseline scans and actual project readiness; avoid score-chasing |

## AI-native coverage and gaps

| AI-native capability | Current source | Assessment | Recommended future treatment |
| --- | --- | --- | --- |
| AI suitability and operating mode | No dedicated asset | Missing | Add a compact decision reference first. It should stop unnecessary AI, RAG, tool, memory, and autonomy adoption. |
| Model/instruction lifecycle | No product-level asset; visual `prompt-engineering` is intentionally out of scope | Missing | Add only if an AI-product project needs it; likely a reference plus change/evaluation gate, not a broad standalone skill at first. |
| Grounding, retrieval, and source access | No dedicated asset | Missing, conditional | Add a focused reference when a RAG/corpus product is in scope. Do not build generic RAG machinery now. |
| Output validation and product enforcement | `security`, `api-design`, `testing` provide the general foundation | Partially covered | Extend the future AI layer with model-output-to-product boundary rules; keep enforcement in ordinary product code. |
| Tool use and autonomy containment | Authority baseline and external/production approval rules provide a strong foundation | Partially covered | Add AI-specific least-privilege, budget, iteration, and untrusted-tool-output guidance only for tool-using products. |
| Identity, tenancy, memory, and privacy | `security`, `database`, and their context templates | Partially covered | Add conditional AI memory/retention and retrieval-tenancy rules; do not create persistent memory by default. |
| Reliability, cost, latency, and graceful failure | `devops-infra`, `performance`, incident response | Partially covered | Add AI-provider fallback/budget/quality-degradation considerations to the future AI layer. |
| Evaluation, red-team, monitoring, and change gate | `testing`, `review-audit`, `security`, `verify-project` | Partially covered | Create an AI evaluation reference/harness pattern only when a product has an AI quality or safety claim that can regress silently. |

## What this means for the five functional boundaries

| Functional boundary | General responsibility | Conditional AI-native addition |
| --- | --- | --- |
| Product & Strategy | Decide the user problem, scope, success, risk, and whether to build at all | Decide whether AI is justified, what failure is tolerable, and which operating mode is proportionate |
| Systems Architecture | Set boundaries, ownership, data flow, contracts, trade-offs, recovery | Keep authority/enforcement/state outside the model; define provider/config/retrieval/tool boundaries when actually used |
| Design Direction | Shape usable, accessible, credible experience | Make AI uncertainty, sources, fallbacks, and user confirmation understandable rather than hidden |
| Engineering/Builder | Implement the chosen design and protect invariants | Implement deterministic validators, constrained executors, budgets, fallbacks, and telemetry |
| Assurance & Quality | Test/review against claims and risk | Run task evaluation, adversarial untrusted-content tests, and human review where deterministic proof is insufficient |

These are functional handoffs. They are not five permanent chat personas and do not mean a designer must wait for a separate auditor to notice every small issue.

## Confirmed strengths worth preserving

- The authority-and-trust baseline already classifies untrusted content and requires just-in-time approval for destructive or external effects.
- The database migration workflow already requires compatibility, rehearsal, evidence, recovery, and an approved target before production mutation.
- The incident-response workflow already distinguishes observation from authorized mitigation and prefers the smallest reversible action.
- The security, API, database, testing, review, performance, and DevOps materials already cover the core product engineering disciplines.

## Change boundaries for the next phase

The following should **not** happen yet:

- rewriting every skill;
- installing a generic agent framework;
- creating RAG, tool, memory, or multi-agent defaults;
- turning every architecture thought into a compulsory workflow;
- changing `global/GEMINI.md`, installed Codex skills, adapters, or host policy.

The next controlled phase is a **keep / strengthen / add / retire decision ledger**. For each relevant skill, workflow, reference, and template, it will answer:

1. What V4 capability does this asset serve?
2. Is it current, duplicated, too broad, too narrow, or wrongly routed?
3. Should it stay as judgement, become a short reference, become a workflow gate, or become a new conditional AI asset?
4. What evidence would make a proposed change worth implementing?

Only after that ledger is agreed should Phase 3 edit a source skill or workflow. This prevents the OS from becoming a pile of fashionable AI rules while still giving AI-native products the controls they genuinely need.
