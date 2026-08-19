# Anti-Gravity OS v4 - Master Asset Decision Ledger

**Status:** reconciled decision baseline; canonical source remains unchanged  
**Date:** 2026-08-18  
**Scope:** all 71 canonical skills, all 52 canonical workflows, shared baselines, templates, adapters, and generated output.  
**Authority:** this document plans future source edits. It does not itself grant installation, publication, external action, destructive change, or a release.

## 1. What this document settles

This is the single V4 planning ledger built from:

- the approved V4 operating model and functional contracts;
- the current-source inventory;
- the general-product and AI-native architecture evidence maps;
- the Core, Delivery/Assurance, and Optional-Pack decision ledgers; and
- useful ideas from the parallel ledgers, after removing unsupported rigid rules.

It settles **where each asset belongs and what kind of change it may need**. It does not rewrite the assets yet.

## 2. Non-negotiable interpretation rules

1. The current V3 source is still the installed, validated system. V4 is a controlled migration target.
2. A functional boundary is not a permanent persona or sequential department. The Director activates the smallest useful set of functions and integrates the result.
3. A skill is not automatically better because it is long or specific. It must provide distinct reusable judgement, resources, or output.
4. A workflow is a route, procedure, or hard gate - not a universal waterfall.
5. A reference/recipe or tool adapter is valuable, but it must not pose as a general reasoning authority.
6. Technical rules are portable principles unless project evidence selects a stack-specific implementation.
7. The AI-native product layer is conditional on a product exposing AI to its users. It is not an extra default pack for ordinary software work.

## 3. Target profile model - not implemented yet

```text
General product studio
    +-- Spatial: spatial/showroom work
    +-- Media: image and video generation
    +-- Growth: positioning, copy, conversion, prospecting
```

`general` is defined by functional necessity, not by an attractive fixed skill count. A project may combine packs only when justified by the request: for example, a showroom with a generated film is General + Spatial + Media.

## 4. Shared source and safety assets

| Asset group | V4 owner / role | Final decision | Future source-edit objective |
| --- | --- | --- | --- |
| `global/GEMINI.md` | Studio Director safety kernel | Keep and compress | Preserve authority, untrusted-content, approval, verification, and reasoning protections. Move role/process detail to routes, contracts, or references. |
| `global/GLOBAL_MEMORY.md` | Studio Director task router | Consolidate and rewrite | Route from task and risk to the smallest relevant functional boundary and optional pack. Do not carry large amounts of always-loaded detail. |
| `global/manifest.yaml` | Canonical asset registry | Keep and extend | Add V4 profile/pack membership, asset role, functional ownership, and compatibility validation without duplicating editable sources. |
| `global/baselines/*` | Shared stable policy | Keep and align | Preserve authority/trust, context integrity, engineering, and volatile-source rules. Add only cross-cutting durable principles. |
| `global/context_templates/*` | Blank project scaffolds | Keep; audit for leanness later | Separate stable guidance from fill-in project truth. A template is never a claim about the active project. |
| `global/adapters/*`, `dist/*` | Host translation and generated payloads | Keep untouched for now | Regenerate only after canonical source and manifest changes pass validation. |
| Installed-only `scroll-scrubbed-hero-video` | Candidate canonical intake | Defer | Audit it in the same way as every other asset before adding canonical source. |

## 5. General capability groups

| Asset group | V4 home / role | Final decision | Accepted future invariant |
| --- | --- | --- | --- |
| Product & Strategy skills: `product-thinking`, `research-analysis`, `competitor-profiling`, `reference-intelligence` | Product & Strategy; evidence skills | Keep; promote `reference-intelligence` to general evidence use | Product framing stays risk-sized. Research distinguishes observation, source, inference, and decision. Competitor evidence remains optional, not Growth-only. |
| Product routes: `task-dispatch`, `project-inception`, `workflow-reference-intelligence` | Studio route / Product procedure | Keep and reduce | The Director routes first; inception establishes a concise North Star and only activates needed disciplines. Reference work is optional and provenance-aware. |
| Architecture skills: `architecture`, `api-design`, `database`, `devops-infra`, `performance` | Systems Architecture | Keep and strengthen | Make boundaries, ownership, quality trade-offs, failure/recovery, security, and reversibility visible. Select protocols, storage, schemas, migrations, and performance techniques from project evidence - not global stack law. |
| Architecture routes: `plan-architecture`, `design-api`, `database-migration`, `dependency-upgrade`, `incident-response`, `ship-to-production`, `optimize-performance` | Studio route, procedure, or hard gate as appropriate | Keep; re-home/reduce where long | Use the smallest route that protects the risk. Production, destructive, and external paths keep their explicit just-in-time approval and recovery evidence. |
| General Design skills: `ui-ux`, `color-system`, `scroll-storyboard`, `apply-transition` | Design Direction | Keep; re-profile narrow helper | UI work includes the relevant user-visible states, accessibility, responsive behaviour, and observable verification. Semantic tokens help when a shared system exists. `apply-transition` becomes a conditional recipe, not a design authority. |
| General Design routes: `design-ui`, `ui-craft`, `ui-animate`, all `impeccable-*` procedures | Design route / procedure library | Keep; consolidate Impeccable | The Design Director owns general design direction. The 23 Impeccable procedures become selectable specialist procedures, never a rival organisation or forced sequence. Motion needs an interaction/communication job, reduced-motion consideration, and measured performance evidence. |
| Staff Engineering skills: `coding`, `debugging`, `refactoring`, `resolving-merge-conflicts`, `setup-pre-commit` | Staff Engineering | Keep; re-profile setup recipe | Coding protects contracts, boundaries, error paths, and verification; it is not a syntax tutorial. Validate untrusted boundaries with the supported runtime mechanism. Separate domain logic from I/O when it improves safety. Review sibling paths after a confirmed repeated bug pattern. |
| Staff routes: `build-feature`, `debug-issue`, `refactor-module`, `context-hygiene` | Studio route / Staff procedure / Studio support | Keep and reduce | Diagnose may remain read-only. Build and refactor work show behaviour/evidence. Context hygiene preserves resumable state only when authorized. |
| Assurance skills: `testing`, `security`, `browser-test`, `review-audit`, `fallow`, `dox` | Assurance & Quality; shared safety discipline | Keep; re-profile tool helpers | Testing is behavioural and proportionate. Security enforces actor/resource/action authorization at the authoritative boundary. Browser, static-analysis, and directory-contract helpers are conditional evidence tools, not proof on their own. |
| Assurance routes: `test-strategy`, `review-code`, `security-audit`, `verify-project` | Assurance procedure / hard gate | Keep; clarify evidence limit | Baseline scans passing are not release readiness. Material work needs relevant project-native tests and explicit release approval; independent assurance is triggered by risk, uncertainty, or consequential claims. |
| Studio-support skills: `deep-think`, `context-formatting`, `context-hygiene`, `learn`, `skill-creator`, `to-tickets`, `wizard` | Director/internal procedure support | Consolidate or re-profile | Keep useful thought, handoff, creation, and setup behaviour. Make narrow formatting/setup helpers on-demand; never expand authority or add unnecessary ceremony. |
| Studio-support route: `os-maintenance` | Studio maintenance procedure | Keep | Audit, propose, implement, and external publication remain distinct authority modes. |

## 6. Optional packs

| Pack | Assets and procedures | Final decision | Activation boundary |
| --- | --- | --- | --- |
| Spatial | `brand-strategy`, `reference-intelligence`, `cinematic-motion`, `cinematic-showroom-strategy`, `master-design-director`, `motion-library`, `spatial-experience-design`, `storytelling`; `spatial-project-inception` plus its phase-routing reference; Spatial reference collections | Keep as Spatial | Interior, showroom, architecture-adjacent, furniture/decor, staging, or explicitly spatial/cinematic work. It does not control ordinary app design. |
| Media | `prompt-engineering`, `video-generation`, and the 24-skill Seedance suite | Keep as Media | Image or video generation, provider-specific media direction, or a named Seedance request. Provider facts are reverified before active use. |
| Growth | `copywriting`, `copy-editing`, `marketing-psychology`, `page-cro`, `expert-positioning`, `prospect-research`, `sales-enablement`, `workflow-marketing-copy` | Keep as Growth | Positioning, copy, conversion, client acquisition, collateral, or outreach. It does not load for backend, debugging, database, or security work. |

## 7. Cross-cutting AI-native product capability

This is not a fifth optional pack. It is a conditional architecture extension when a product user interacts with AI.

| Capability | Minimal control when triggered |
| --- | --- |
| AI suitability and operating mode | Write the user job, quality bar, failure tolerance, and choose the smallest mode: feature, controlled workflow, tool-using agent, or autonomous system. |
| Model/instruction lifecycle | Owner, version/change record, and regression evidence proportionate to impact. |
| Grounding/retrieval | Use only for a real corpus-fact need; enforce source scope/access and clearly degrade/refuse when unsupported. |
| Output/tool boundary | Validate output and enforce authorization, durable state, budgets, audit, and external effects outside the model. |
| Memory/privacy/tenancy | Store only necessary information under explicit retention, tenant, and deletion rules. |
| Reliability/evaluation | Define timeout/cost/fallback behaviour; use deterministic checks where possible and human review where judgement is required. |

## 8. Principles accepted from the parallel ledgers

| Worth retaining | How V4 adopts it safely |
| --- | --- |
| Semantic tokens and component-state thinking | Cover the states that genuinely affect the component/flow. Do not impose a fixed state count or an aesthetic ban. |
| Boundary schema validation and domain/I-O separation | Require validation at real untrusted boundaries and separation where it materially helps correctness/testability. Do not mandate a named library or architecture style. |
| Sibling-function repair check | After confirming a recurring defect pattern, inspect related paths and add proportionate regression protection. |
| Assume-breach, server-side authorization, and resource-scoped access | Treat these as mandatory security principles whenever an authorization boundary exists. Apply database/session/web controls only where that architecture exists. |
| Recipe/tool-adapter demotions | Keep `apply-transition`, pre-commit setup, Fallow, and DOX useful but conditionally loaded and honestly described. |
| Three specialist packs | Adopt Spatial, Media, and Growth, but implement composition through manifest metadata before moving files. |

## 9. Principles explicitly rejected as universal OS policy

- Fixed colour or visual-style bans.
- A mandatory fixed number of component states.
- Fixed frame-rate, timeout, lock-timeout, pagination, error-schema, or database-index rules.
- Mandatory PostgreSQL, Zod, Pydantic, or any other library/framework.
- A mandatory independent audit for every small release or local edit.
- A universal RAG, memory, multi-agent, or autonomous-agent architecture.
- Claims that a generic scanner alone proves production readiness.

## 10. Coverage record

The group rows above cover every canonical asset. This explicit record prevents a group label from hiding an unclassified file.

### Canonical skill coverage (71)

- **Product/strategy:** `competitor-profiling`, `product-thinking`, `reference-intelligence`, `research-analysis`
- **Systems architecture:** `api-design`, `architecture`, `database`, `devops-infra`, `performance`
- **Design:** `apply-transition`, `color-system`, `scroll-storyboard`, `ui-ux`
- **Staff engineering:** `coding`, `debugging`, `refactoring`, `resolving-merge-conflicts`, `setup-pre-commit`
- **Assurance:** `browser-test`, `dox`, `fallow`, `review-audit`, `security`, `testing`
- **Studio support:** `context-formatting`, `context-hygiene`, `deep-think`, `learn`, `skill-creator`, `to-tickets`, `wizard`
- **Spatial:** `brand-strategy`, `cinematic-motion`, `cinematic-showroom-strategy`, `master-design-director`, `motion-library`, `spatial-experience-design`, `storytelling`
- **Media:** `prompt-engineering`, `video-generation`, `seedance`, `seedance-antislop`, `seedance-audio`, `seedance-camera`, `seedance-characters`, `seedance-copyright`, `seedance-examples-zh`, `seedance-filter`, `seedance-interview`, `seedance-interview-short`, `seedance-lighting`, `seedance-motion`, `seedance-pipeline`, `seedance-prompt`, `seedance-prompt-short`, `seedance-recipes`, `seedance-style`, `seedance-troubleshoot`, `seedance-vfx`, `seedance-vocab-es`, `seedance-vocab-ja`, `seedance-vocab-ko`, `seedance-vocab-ru`, `seedance-vocab-zh`
- **Growth:** `copy-editing`, `copywriting`, `expert-positioning`, `marketing-psychology`, `page-cro`, `prospect-research`, `sales-enablement`

### Workflow inventory at the original decision point (52)

- **Studio/Product:** `task-dispatch`, `project-inception`, `context-hygiene`, `os-maintenance`, `reference-intelligence`
- **Systems architecture:** `plan-architecture`, `design-api`, `database-migration`, `dependency-upgrade`, `incident-response`, `ship-to-production`, `optimize-performance`
- **Design:** `design-ui`, `ui-craft`, `ui-animate`, `impeccable-adapt`, `impeccable-animate`, `impeccable-audit`, `impeccable-bolder`, `impeccable-clarify`, `impeccable-colorize`, `impeccable-craft`, `impeccable-critique`, `impeccable-delight`, `impeccable-distill`, `impeccable-document`, `impeccable-extract`, `impeccable-harden`, `impeccable-layout`, `impeccable-live`, `impeccable-onboard`, `impeccable-optimize`, `impeccable-overdrive`, `impeccable-polish`, `impeccable-quieter`, `impeccable-shape`, `impeccable-teach`, `impeccable-typeset`
- **Staff engineering:** `build-feature`, `debug-issue`, `refactor-module`
- **Assurance:** `review-code`, `security-audit`, `test-strategy`, `verify-project`
- **Spatial:** `spatial-concept`, `spatial-design-ui`, `spatial-project-inception`, `storytelling`, `visual-brainstorm`
- **Media:** `video-generation`
- **Growth:** `marketing-copy`

## 11. Pre-source-edit acceptance tests

The master is ready for the first source-edit batch only when these checks pass:

| Check | Required result |
| --- | --- |
| Inventory coverage | 71 canonical skills and 52 canonical workflows are classified exactly once in the coverage record. |
| General request routing | Normal product/SaaS/API work does not discover Media, Spatial, or Growth assets unless activated by the request. |
| Cross-pack routing | A mixed request activates only justified packs and preserves general authority/safety gates. |
| Small-change proportionality | A safe local change does not require a forced full audit or a long workflow. |
| High-impact authority | Destructive, production, financial, publication, and other external effects stop at an explicit approval gate. |
| AI-native boundary | AI-product controls extend ordinary product authority rather than letting a model own authorization, state, audit, or side effects. |
| Manifest/adapters | A proposed profile change validates, generates compatible host output, and does not create duplicate editable sources. |

## 12. Next source-edit sequence

1. **Manifest and router design review:** define the profile/asset-role schema and routing fixtures. No source mutation until the schema and compatibility path are testable.
2. **Core routing batch:** update the manifest, then the lean Studio router and core policy wording together; build and validate all host adapters.
3. **Core-route batch:** update task dispatch, project inception, architecture, build, design, assurance, and hard-gate route ownership/handoffs.
4. **Selective skill batch:** revise the small high-leverage universal skills using the accepted portable invariants and targeted research only where it changes a decision.
5. **Pack and procedure batch:** re-profile optional assets, consolidate procedures, repair references, regenerate distributions, and run full routing fixtures.

No source edit is authorized merely because this ledger exists. Each batch must have an explicit scope, diff review, verification evidence, and the applicable approval gate.
