# V4 Round 2 — Focused Research Prompts

Run each prompt in a separate deep-research task. These reports decide whether
we change existing skills; they do not authorize creating new skills.

## Shared instruction

\`\`\`text
You are informing an AI-agent operating system, not writing a tutorial.

Use current primary sources first: official standards, maintainers' technical
documentation, authoritative framework documentation, and original research
where it directly supports a claim. Label each material conclusion as
required, supported, context-dependent, conventional, or unresolved. Include a
direct source link and publication or verification date for volatile claims.

Do not invent citations, product facts, or “best practice.” Separate public
production systems from prototypes, local tools, batch jobs, internal systems,
and low-consequence work. Reject a universal rule when it only fits one
context.

Return a decision report: keep/revise/remove matrix for the current rules;
smallest durable AI-agent method; lean skill versus conditional-reference
boundary; approval boundaries; evaluation cases; and explicit limits.
\`\`\`

## 1. Implementation, Refactoring, and Code Review

\`\`\`text
Conduct a source-backed decision study for a one-person AI Product Studio that
uses a main agent plus bounded specialist agents to build websites, apps,
services, and internal tools. It needs safer changes without turning every edit
into a ceremony.

Study implementation planning, safe local change, behavior-preserving
refactoring, code review, test/evidence selection, and a builder-to-reviewer
handoff. Critically assess these inherited rules: three cases before an
abstraction; at most three function parameters; the same full data trace for
every change; a test harness before every refactor; never combine a refactor and
bug fix; every review must use \`git diff main...HEAD\`; and large diffs are
automatically bad.

Cover low-risk docs/config, ordinary features, critical data/auth changes, and
legacy code with incomplete tests. Decide how discovery, diff inspection,
sibling-pattern checks, verification, independent review, and stopping
conditions scale by risk.

[Paste Shared instruction.]
\`\`\`

## 2. API Contracts, Data Modelling, and Safe Evolution

\`\`\`text
Conduct a source-backed decision study for a personal AI Product Studio that
builds small products and growing multi-user systems. We need durable agent
guidance for API contracts, data integrity, schema evolution, and migrations
without premature enterprise design.

Critically assess: version every API from day one; paginate every collection;
rate-limit every endpoint; the written specification is always authoritative;
start every schema at 3NF; design for a billion rows; always deploy schema and
code separately; soft-delete every recoverable/audit-relevant record; and use a
relational database by default.

Separate public, internal, local-only, and event/async contracts; bounded and
unbounded lists; relational and document data; small and live large datasets.
Cover compatibility, idempotency, ownership, validation, authorization,
audit/recovery, rollback limits, and observability.

[Paste Shared instruction.]
\`\`\`

## 3. Performance, Operations, and Delivery Reliability

\`\`\`text
Conduct a source-backed decision study for a personal AI Product Studio. It
needs agents that diagnose slow or unreliable systems and prepare delivery
safely without forcing production-SRE machinery onto a prototype or a small
website.

Critically assess: always use p95/p99 rather than averages; every performance
claim needs production-scale load; caching is always last; all infrastructure
must be infrastructure-as-code; all logs must be JSON; distributed tracing is a
baseline; every secret needs a dedicated manager; deployments/rollbacks must be
automated; and alerts must only follow user-facing symptoms.

Separate browser/UI, API, background/batch, local development, early product,
production service, and safety-critical operations. Cover measurement,
baselines, profiling, capacity, graceful degradation, observability, incident
readiness, deployment/rollback, and external approval boundaries.

[Paste Shared instruction.]
\`\`\`

## 4. Application Security for AI-Assisted Product Work

\`\`\`text
Conduct a source-backed decision study for a personal AI Product Studio that
uses agents for code, review, and technical planning. Build a durable security
method for ordinary web products that makes no guarantee and does not turn each
task into a penetration test.

Use current primary sources such as OWASP, NIST, language/framework guidance,
and protocol standards where relevant. Cover trust boundaries, authentication
versus authorization, tenant/object access, input/output handling, secrets,
dependencies/supply chain, logs, uploads, webhooks, external APIs, abuse
controls, and incident escalation.

Decide when a builder self-check is enough and when independent security audit
is needed. Define evidence, severity/confidence, remediation handoff, limits,
and approval before external or production effects.

[Paste Shared instruction.]
\`\`\`

## 5. Ethical Sales Enablement

\`\`\`text
Conduct a source-backed decision study for a one-person AI Product Studio that
creates websites, software, and product services. It needs truthful proposals,
one-pagers, decks, demos, discovery summaries, objection handling, and buyer
materials. It must never invent outcomes, ROI, quotes, urgency, authority, or
social proof.

Critically assess: every deck has 10–12 slides; every sale uses a fixed
discovery/demo/close sequence; every claim must connect to revenue, efficiency,
or risk; buyer personas determine motives; and ROI calculators may state annual
ROI, payback, or three-year value from assumed inputs.

Separate local service, bespoke website, SaaS, enterprise, discovery call, and
internal sales aid. Specify supplied evidence versus client assertions,
hypotheses, examples, and unsupported claims. Cover consent, privacy,
competitive claims, pricing/scope authority, and approval before sending.

[Paste Shared instruction.]
\`\`\`

## 6. CRO Evidence and Experimentation

\`\`\`text
Conduct a source-backed decision study for a personal AI Product Studio that
designs websites, product flows, signup/onboarding paths, and marketing pages.
We need AI guidance that improves clarity and test quality without turning CRO
folklore into rules.

Critically assess: users must understand a page in five seconds; the primary
CTA must be above the fold; landing pages need one CTA and no navigation;
testimonials/security badges belong near CTAs; fewer form fields always reduces
friction; and every proposed change needs an A/B test.

Separate information pages, service sites, ecommerce, lead generation,
onboarding, high-traffic experiments, and low-traffic/no-test contexts. Cover
accessibility, qualitative evidence, analytics limits, experiment uncertainty,
guardrails, ethics, and when a proposal is only a design hypothesis.

[Paste Shared instruction.]
\`\`\`

## 7. Tool-Agnostic Competitor Intelligence

\`\`\`text
Conduct a source-backed decision study for a personal AI Product Studio that
needs competitor and market intelligence for product decisions, positioning,
and client work. The OS must work whether browser/search tools, Firecrawl,
DataForSEO, or no paid tool is available.

Define how an agent should set a decision question, choose proportionate public
sources, separate observed claims from inference, record source/date/access
limits, compare competitors fairly, and avoid unsupported traffic, funding,
pricing, review, technology, or market claims.

Cover tool capability checks, legal/terms-aware collection, rate/cost/consent
limits, private-data boundaries, raw-evidence preservation, confidence labels,
and the difference between a quick public scan and a decision-grade dossier.
Do not require a named provider or automatic local writes.

[Paste Shared instruction.]
\`\`\`

