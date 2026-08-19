# Current Skill Capability Audit

**Status:** historical inventory snapshot. The count and package locations remain useful, but its provisional keep/demote decisions are superseded by `docs/v4-stage-a-asset-reconciliation.md` as of 2026-08-19.
**Date:** 2026-08-19
**Evidence source:** `global/manifest.yaml` parsed from the current local worktree

> **Read this first:** this document was written before the complete source-level audit. It is not permission to treat the current 48 skills and 17 workflows as the final V4 design. Use the Stage-A reconciliation ledger for current decisions, and `docs/v4-canonical-capability-map.md` for the target model that does not start from old filenames.

## The count, explained plainly

The current manifest contains **48 skills** and **17 workflows**.

That does not mean an ordinary task loads 72 instruction files. The current profile split is:

| Profile | Registered skills | Meaning |
| --- | ---: | --- |
| `general` | 29 | Default product-studio capabilities. |
| `spatial` | 10 | Interior, showroom, architecture-adjacent, furniture/decor, and cinematic-spatial work only. |
| `media` | 2 | Generic visual prompting plus one provider-aware video-generation package, only when media work is requested. |
| `growth` | 8 | Positioning, copy, conversion, prospecting, offers, and sales support only when commercial work is requested. |

The apparent disagreement with some earlier V4 documents is historical: they describe an earlier 71/72-skill snapshot. The 24 former Seedance entries were consolidated into one active package on 2026-08-19. The controlled `canvas-ui` decision capability was then added to the Spatial pack, changing the current local manifest to 49. This is a local-worktree fact, not a claim about a committed or pushed GitHub revision.

## The rule for judging a skill

Every skill will be judged by this question:

> Does it give the agent distinct reusable judgement, a selective library, a safe tool boundary, or a decision-changing verification method that would otherwise be unreliable?

If yes, it stays as a capability. If it is a narrow setup command, transition lookup, formatting recipe, or tool adapter, it can still stay in the OS but should be labelled and discovered as that—not presented as a general expert brain.

No item is removed merely because a foundation model might know some of its subject. The bar is whether the local method, reference collection, safety boundary, or project-specific route improves the outcome.

## Current capability map

### Product strategy and evidence — 12 skills

| Skills | Current role | Provisional decision | Research / revision gate |
| --- | --- | --- | --- |
| `product-thinking`, `research-analysis` | Product framing, evidence, decision sizing, and option comparison. | Keep as core general capabilities. | Product Thinking already has a research-backed revision. Improve only when a real pilot exposes a decision gap. |
| `competitor-profiling` | External market/competitor evidence when it changes a product or positioning decision. | Keep, conditional. | Audit its claims, source discipline, and output quality before broadening it. |
| `reference-intelligence` | Reference provenance and translation rather than visual copying. | Keep. Presently Spatial-only; assess promotion to general evidence capability after direct-route testing proves it adds value outside spatial work. | No broad research needed for the profile question; test it on a non-spatial website/product reference task. |
| `copy-editing`, `copywriting`, `expert-positioning`, `marketing-psychology`, `page-cro`, `prospect-research`, `sales-enablement`, `offer-architecture` | Optional Growth pack: message, proof, conversion, client acquisition, offers, and sales support. | Keep as an isolated Growth pack. | Existing Growth research informs current revisions. Do not add a new skill until a concrete commercial job has no credible owner. |

### Systems architecture — 5 skills

| Skills | Current role | Provisional decision | Research / revision gate |
| --- | --- | --- | --- |
| `architecture` | Boundaries, quality trade-offs, ownership, data flow, failure, and reversibility. | Keep as a core capability. | Architecture candidate evaluations exist; next evidence should be a real product decision, not more synthetic tests. |
| `api-design`, `database`, `devops-infra`, `performance` | Contract design, persistence, operations, and measured performance. | Keep as specialised general capabilities. | Audit each against current primary sources only when changing a technology-specific claim or introducing a new platform practice. |

### Staff engineering — 5 skills

| Skills | Current role | Provisional decision | Research / revision gate |
| --- | --- | --- | --- |
| `coding`, `debugging`, `refactoring` | Implementation, diagnosis, and behaviour-preserving structure change. | Keep as core capabilities. | Their recent research-backed revisions should be tested against real work before further rewriting. |
| `resolving-merge-conflicts` | A narrow, high-risk recovery procedure. | Keep, but label mentally as an on-demand procedure rather than general reasoning authority. | No research required to re-profile its discovery language. |
| `setup-pre-commit` | A narrow development-tool setup procedure. | Keep as an on-demand procedure/recipe. | Never run it automatically; platform/tooling details require current verification when invoked. |

### Assurance and quality — 6 skills

| Skills | Current role | Provisional decision | Research / revision gate |
| --- | --- | --- | --- |
| `testing`, `security`, `review-audit` | Behavioural evidence, trust boundaries, and meaningful review. | Keep as core assurance capabilities. | Testing and security evolve; update specific claims only with targeted primary-source research or a real failure. |
| `browser-test` | Browser inspection and evidence collection. | Keep as a conditional tool-facing capability. | Verify host/tool instructions whenever the browser tool changes. |
| `dox`, `fallow` | Directory-contract and static-analysis helpers. | Keep as tool adapters, not independent expert domains. | Their availability/output must be verified at use time. |

### Studio support — 7 skills

| Skills | Current role | Provisional decision | Research / revision gate |
| --- | --- | --- | --- |
| `deep-think`, `learn`, `context-hygiene` | Deliberate reasoning, after-action learning, and safe resumable context. | Keep; they govern how work is handled, not a client-facing department. | Assess through real task quality and authority safety, not a broad internet study. |
| `skill-creator` | Constructs/refactors an Anti-Gravity skill package. | Keep as internal OS maintenance support. | Use only after a capability decision has been evidenced. |
| `context-formatting`, `to-tickets`, `wizard` | Narrow formatting, planning, and guided setup procedures. | Keep as on-demand procedures. | No new research required unless their host/tool assumptions change. |

### General design — current snapshot updated 2026-08-19

| Skills | Current role | Provisional decision | Research / revision gate |
| --- | --- | --- | --- |
| `ui-ux` plus conditional colour references | Interface structure, states, accessibility, visual hierarchy, and semantic colour. | Keep UI/UX as the general capability; retire the former standalone `color-system` from active routing. | Colour evidence review completed. Next evidence is a real interface task, not generic design research. |
| `apply-transition` | A narrow pre-built transition lookup/application helper. | Keep as a procedure/reference, never as a design authority. | Verify the upstream library only when used. |
| `scroll-storyboard` | Authored scroll timing and continuity. | Keep inside the Spatial pack, conditional on an approved experience needing it. | Audit current browser/animation implementation details only when a project selects it. |

### Spatial pack — 10 skills

| Skills | Current role | Provisional decision | Research / revision gate |
| --- | --- | --- | --- |
| `brand-strategy`, `spatial-experience-design`, `storytelling`, `master-design-director` | Evidence-backed positioning, concept, story, and high-stakes creative judgement for spatial work. | Keep. | The website-system and spatial-parity audits establish the structural map. Use a real client brief before revising creative judgement. |
| `reference-intelligence` | Reference analysis and translation. | Keep; see the general-evidence promotion question above. | Test first outside spatial work. |
| `cinematic-motion`, `motion-library`, `cinematic-showroom-strategy`, `scroll-storyboard` | Conditional spatial media, motion, and choreography. | Keep, deliberately optional. | Do not consolidate based on file count. Reverify platform/tool details before changing implementation recipes. |
| `canvas-ui` | Controlled decision and implementation-readiness support for one contained live DOM/WebGL effect. | Keep as a conditional Spatial capability. | Reverify the exact upstream component, licence, browser support, and import method; prove one vertical slice before source enters a client project. |

### Media pack — 2 skills

| Skills | Current role | Provisional decision | Research / revision gate |
| --- | --- | --- | --- |
| `video-generation`, `prompt-engineering` | Provider-neutral entry point for media direction and generic visual prompt work. `video-generation` holds selective provider and craft references. | Keep as the media front door. | Reverify Google Flow, Veo, Gemini/Omni, Seedance, and other provider behaviour from official sources whenever a concrete provider claim is added or changed. |

The Media count is small because the provider-specific specialist suite is no longer installed as 24 separate skills. Its useful method has been rehomed into selective references, while the prior source package remains archived for provenance and future curation.

## What is a skill, a reference, a procedure, or a tool adapter?

| Category | Present examples | Correct behaviour |
| --- | --- | --- |
| Core capability | `product-thinking`, `architecture`, `ui-ux`, `coding`, `testing`, `brand-strategy` | Carry reusable judgement and decision checks. Load only when the task matches. |
| Optional specialist capability | `cinematic-motion`, `storytelling`, `offer-architecture`, `video-generation` | Activate only with the relevant pack and task. |
| Procedure / recipe | `apply-transition`, `setup-pre-commit`, `to-tickets`, `wizard`, `resolving-merge-conflicts` | Stay discoverable, but do not behave like universal operating policy. |
| Tool adapter | `browser-test`, `dox`, `fallow` | Use a host/tool only when it is available; record tool limits rather than treating its output as truth. |
| Reference library inside a skill | motion library, UI references, storytelling library, cinematic-motion examples | Load by a named question or job; never dump the whole library into a task. |

## What this audit says about the skill count

The current number is not the thing to optimise. The real targets are:

1. ordinary general work must not load Spatial, Media, or Growth material by accident;
2. a valuable specialist method must be discoverable when it is requested;
3. a recipe or tool must not masquerade as a general capability;
4. a reference must be selectively retrievable rather than bloating every task; and
5. no skill should remain merely because it is old or be deleted merely because it overlaps another file.

The existing manifest already begins to express this through profiles and delivery roles. The next audits should improve the **quality and routing of packages**, not chase a smaller number.

## Research gates from here

Research is justified only before a substantive content change that needs fresh evidence.

| Priority | Focused study | Why |
| --- | --- | --- |
| 1 | Provider recheck at use time: Google Flow, Veo, Gemini/Omni, Seedance | The 2026-08-19 Media audit is complete; provider facts remain volatile. |
| 2 | Real website outcome pilot | Tests whether the spatial, UI, story, and motion routes improve a real client result rather than merely preserving text. |
| 3 | General evidence capability pilot | Tests whether `reference-intelligence` should move from Spatial to General without causing context pollution. |
| 4 | A targeted audit of one architecture/API/database claim only when a real product needs it | Avoids researching technology in the abstract. |

Product thinking, project inception, debugging, testing/verification, growth, and offer architecture already have recent evidence records in this worktree. Their next step is real-project validation, not another broad research report.

## The next build order

1. Complete the current website route checks and, when an actual client brief is available, run one outcome pilot.
2. Curate archived media examples or language vocabulary only when a real job needs them, with a retrieval test and current surface verification.
3. Audit the Systems Architecture group one capability at a time against actual product work, starting with an API or data decision only when one exists.
4. Continue the Growth pack through actual prospecting/website work, adding a skill only when the documented capabilities cannot own a necessary job.
5. After each group, update the master ledger and routing fixtures before making source consolidation decisions.

## What has not been decided

- No additional active skill is approved for removal from this inventory alone; the previous Seedance package was archived only after its preservation audit and replacement references passed.
- No new skill is approved merely because a domain sounds important.
- No provider-specific Seedance syntax or limit has been declared current for Google Flow, Veo, Gemini/Omni, or any other video model.
- No claim is made that the current local worktree is committed, pushed, or installed into a host.
