# V4 Architecture Evidence Map

**Status:** research-derived design map, not active runtime policy  
**Date:** 2026-08-18  
**Purpose:** define what a well-governed product architecture must be capable of before deciding which Anti-Gravity assets deserve to exist.

## Read this first

A **capability** is a result the studio must reliably achieve. It is not automatically a skill, a workflow, a permanent agent, or a document.

For example, "safe external effect" is a capability. Depending on the project, it may be handled by ordinary engineering judgement, a short security reference, a release workflow, or an explicit user approval. Creating a large generic skill just because a capability has a name would make the OS slower and less intelligent.

## The two layers

```text
Product opportunity
       |
       v
General product architecture capabilities ---------------------> normal product delivery
       |
       +-- product itself exposes AI? -- no --------------------> stop: no AI-native layer
                                      |
                                     yes
                                      v
                         AI-native product capabilities
                                      |
                                      v
                      project-specific evidence and controls
```

The first layer applies to all significant digital products. The second is activated only where a user-facing product actually contains an AI capability.

## Layer 1 - General product architecture capabilities

| Capability | What it protects | Trigger | Smallest useful output or control |
| --- | --- | --- | --- |
| 1. Product and risk framing | Building the wrong thing or treating a high-impact decision like a small UI edit | New product, major feature, external integration, material change | User job, users affected, desired outcome, risk level, key assumptions |
| 2. Quality attributes and trade-offs | A design that works only in the demo because reliability, privacy, cost, latency, accessibility, or recovery were never ranked | Architecture decision or meaningful non-functional constraint | Ranked quality attributes, one or two measurable scenarios, acknowledged sacrifice |
| 3. Boundaries, ownership, and data lifecycle | Hidden coupling, contradictory state, unclear responsibility, or accidental data retention | More than one component, service, store, actor, or sensitive data flow | Boundary and ownership map, source of truth, data creation-to-deletion story |
| 4. Contracts and failure behaviour | Consumers depending on undefined success/error semantics or a system that fails silently | API, async process, integration, job, import/export, or user-critical flow | Contract, invalid-input path, timeout/retry/idempotency decision, safe degradation |
| 5. Trust, privacy, and security | Unauthorized action, secrets exposure, abuse, unsafe data handling, or a false trust boundary | Authentication, authorization, sensitive data, uploads, third parties, external effects | Threat/boundary assessment and enforcement at the authoritative layer |
| 6. Change, migration, and release safety | A change that cannot be rolled back or verified without harming live users | Schema/data change, compatibility change, dependency/platform change, production release | Reversibility assessment, compatibility path, recovery/containment plan, approval when needed |
| 7. Operability and recovery | A product that cannot be understood, supported, or restored when something fails | Production service, critical integration, background work, user-impacting availability need | Meaningful signals, ownership, known failure response, fallback or recovery path |
| 8. Evidence and independent assurance | "It should work" being mistaken for proof | Before material release, after a risky change, when uncertainty is high | Proportionate tests, review from a distinct lens, recorded limitations and residual risk |

### Proportionality rule

The map is a **thinking aid**, not a waterfall.

- A simple landing-page restyle might need only product intent, accessibility/performance checks, and visual verification.
- A small internal CRUD feature may add explicit data ownership and authorization checks.
- A payment, health, financial, multi-tenant, production, or irreversible path needs deeper evidence and explicit approval before external action.

## Layer 2 - AI-native product capabilities

Activate these only when the product itself exposes AI. They extend Layer 1; they do not replace it.

| Capability | What it protects | Trigger | Smallest useful output or control |
| --- | --- | --- | --- |
| 1. AI suitability and operating mode | Adding AI where rules would be safer, or granting more autonomy than the job requires | Any proposed AI-facing feature | Value hypothesis, quality bar, failure tolerance, selected mode: feature, controlled workflow, tool-using agent, or autonomous system |
| 2. Model and instruction lifecycle | Invisible behaviour changes, untraceable provider/model shifts | Model/provider, system prompt, tool schema, or material configuration change | Named owner, versioned configuration, change record, regression check appropriate to impact |
| 3. Grounding, retrieval, and source access | Confident but unsupported answers, stale/poisoned context, cross-user data exposure | Product answers from a corpus or claims facts beyond known deterministic data | Source scope, retrieval-time access control, source display/citation where users rely on facts, refusal/fallback when unsupported |
| 4. Output validation and product enforcement | Model output becoming executable code, content, data, or action without validation | Structured output, generated query/code, browser rendering, downstream automation | Schema/semantic validation, safe rendering/escaping, policy enforcement outside the model |
| 5. Tool use and autonomy containment | Excessive functionality, permissions, iterations, cost, or blast radius | Model can call files, browser, API, database, payment, messaging, deploy, or other external tool | Narrow tool allowlist, least-privilege credential path, iteration/spend limit, stop/kill path, approval for high-impact effects |
| 6. Identity, tenancy, memory, and privacy | Cross-user leakage, unwanted persistence, poisoned memory, unclear deletion rights | Personalization, persistent memory, shared corpora, multi-tenant data, sensitive information | Explicit opt-in/need, tenant boundary, retention/deletion policy, safe logging/data-minimization decision |
| 7. Reliability, cost, latency, and graceful failure | Provider outage, runaway spend, long wait, or silent unsafe fallback | Live AI feature or external provider dependency | Budget and timeout, user-visible degraded state, fallback/non-AI path where practical, operational signal |
| 8. Evaluation, adversarial testing, monitoring, and change gate | Silent regression in quality, grounding, safety, or tool behaviour | New AI feature or material model/prompt/retrieval/tool change | Representative test set, deterministic checks where an oracle exists, human review of failures, adversarial untrusted-content tests, post-release observation |

## Authority boundary for AI products

```text
untrusted input / user prompt / retrieved document / tool output
                          |
                          v
               model proposes text or an action
                          |
                          v
         deterministic product controls validate and authorize
                          |
              +-----------+-----------+
              |                       |
          rejected                 allowed action
              |                       |
              v                       v
          safe response          durable audit/effect
```

The model does not own authorization, durable state, tool permissions, audit truth, or external side effects. This protects the product even when a model is wrong, manipulated, unavailable, or changed.

## Evidence classification for future implementation

| Use this when... | Encode it as... | Example |
| --- | --- | --- |
| An experienced builder can apply it case-by-case | Ordinary engineering judgement | Whether a simple feature needs a provider abstraction |
| A compact rule must be used consistently in many tasks | Stable baseline or short reference | Treat untrusted retrieved content as data, not instructions |
| A sequence must stop before an irreversible/external effect | Workflow and just-in-time approval gate | Deployment, purchase, deletion, live database mutation, outbound message |
| Quality can silently regress and needs repeatable evidence | Evaluation harness or project test fixture | Frozen AI task set after a prompt/model/retrieval change |
| A recurring specialist problem needs different reasoning, resources, and outputs | Dedicated skill, only after the case is proven | Future AI-product architecture skill, if products repeatedly need it |

## Sources and confidence

The general layer synthesizes the strongest Manus and Grok general product-architecture reports already reviewed. The AI-native layer primarily synthesizes the Manus and Grok AI-native reports, with official cross-checks from [NIST's Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), [OWASP LLM06](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), and the [NCSC/CISA secure development lifecycle guidance](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development).

This map intentionally contains no vendor choice, model choice, fixed stack, or universal agent pattern.
