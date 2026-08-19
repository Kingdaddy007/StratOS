# Anti-Gravity OS v4 — Stage A Asset Reconciliation

**Status:** inventory and classification baseline — not a final keep/remove decision  
**Date:** 2026-08-19  
**Scope:** canonical repository, archive, generated structure, and the separate local Gemini skill folder.

## 1. What this document proves

This is the first complete account of the assets that are currently in scope. It answers what each active item claims to do and what must be checked before it can remain active.

It does **not** claim that 48 skills or 17 workflows are the final V4 inventory. It prevents another blind deletion or addition.

## 2. Reconciled sources

| Source | State | Meaning |
| --- | --- | --- |
| `global/manifest.yaml` | Validated; 48 skills, 17 workflows, 6 agents, 4 profiles | Current canonical build registry. |
| `global/skills/` and `global/workflows/` | Matches manifest entry count | Active canonical source files. |
| `global/archives/seedance-v3-source/` | Archived; excluded from builds | Preserved historical Seedance source, not active policy. |
| Separate host-local Gemini skills folder | Separate local copy, not V4-composed | Comparison source only. It has no global `GEMINI.md` or custom-agent folder. |
| `docs/v4-workflow-normalisation-decision.md` | Historically useful but stale | Its stated interim count of 25 does not explain the live 17-workflow manifest. |

## 3. How to read the tables

- **Claimed job** comes from the live asset's name, manifest owner, and frontmatter—not from a final judgement.
- **Stage-A classification** is the asset type it appears to be today.
- **Decision needed** tells us what must be proved before the asset can remain active.
- `Keep conditionally` is not a final keep decision. It means the job is plausible but must pass the survival test in the reconstruction plan.

## 4. Agent and pack inventory

| Asset | Claimed job | Status |
| --- | --- | --- |
| Studio Director | Main agent: intake, routing, integration, approvals, and final handoff | Active canonical agent contract. |
| Product Strategy Lead | Product problem, evidence, scope, and positioning | Active canonical agent contract. |
| Systems Architect | Boundaries, data, contracts, quality attributes, and operations | Active canonical agent contract. |
| Design Director | UX, visual direction, Spatial/Media pack routing, and design handoff | Active canonical agent contract. |
| Staff Engineer | Implementation, repair, integration, and local delivery evidence | Active canonical agent contract. |
| Assurance Quality Lead | Independent risk, security, accessibility, and completion challenge | Active canonical agent contract. |
| General profile | Normal product/software work | Base profile. |
| Spatial profile | Cinematic, interior, spatial, luxury-editorial work | Optional pack; never default. |
| Media profile | Image/video prompting and directed media work | Optional pack; never default. |
| Growth profile | Positioning, offer, sales, conversion, and outreach work | Optional pack; never default. |

**Stage-A conclusion:** The agent model is a coherent starting point. It still needs a later routing test proving that each lead discovers the correct capability without Beloved memorising slash commands.

## 5. Active skills — Product Strategy and Evidence

| Asset | Claimed job | Stage-A classification | Decision needed |
| --- | --- | --- | --- |
| `product-thinking` | Frame a problem, scope a bet, define outcomes | Core judgement skill | Recent research-backed revision exists. Confirm it adds a distinct operating method beyond the Director and Product Lead contracts. |
| `research-analysis` | Compare options and make an evidence-backed recommendation | Core judgement skill | Audit source discipline, uncertainty handling, and overlap with general research routes. |
| `competitor-profiling` | Gather and interpret competitor evidence | Conditional evidence skill | Check claim discipline, privacy, source quality, and distinction from market research. |
| `brand-strategy` | Position a brand and diagnose perception/market fit | Conditional Spatial/Growth judgement skill | Decide portable brand core versus spatial-only material; do not reduce website-specific references without a destination. |
| `copy-editing` | Improve existing persuasive text without inventing claims | Optional Growth judgement skill | Existing revision evidence must be checked against real client copy work. |
| `copywriting` | Draft evidence-led marketing or product copy | Optional Growth judgement skill | Prove it produces honest, context-specific copy rather than generic model prose. |
| `expert-positioning` | Build credible expert/service positioning | Optional Growth judgement skill | Retain only the distinct positioning method; move generic website craft material to Design or references. |
| `marketing-psychology` | Use ethical behavioural insight | Optional Growth judgement skill | Keep strict evidence and ethics boundary; do not allow manipulation recipes to masquerade as strategy. |
| `page-cro` | Diagnose and improve conversion paths | Optional Growth/Design judgement skill | Clarify overlap with product UX, copy, and analytics. |
| `prospect-research` | Research, score, and document qualified prospects | Optional Growth workflow-support skill | Preserve its dossier template/script if its evidence discipline remains distinct. |
| `sales-enablement` | Create truthful sales collateral and objection support | Optional Growth judgement skill | Audit its breadth, proof rules, and distinction from copywriting/offer architecture. |
| `offer-architecture` | Define service/product offers, scope, proof, and boundaries | Optional Growth judgement skill | Recent research gate exists; validate on one real offer decision before expansion. |

## 6. Active skills — Systems Architecture and Operations

| Asset | Claimed job | Stage-A classification | Decision needed |
| --- | --- | --- | --- |
| `architecture` | Boundaries, quality trade-offs, data, failure, evolution | Core judgement skill | Candidate evaluations exist. Test on a real decision rather than continue synthetic testing. |
| `api-design` | Durable API/service contracts | Conditional specialised judgement skill | Audit current claim freshness and distinct contribution from Architecture. |
| `database` | Data models, queries, persistence, and migrations | Conditional specialised judgement skill | Audit current database guidance and boundary with the migration workflow. |
| `devops-infra` | Operations, deployment infrastructure, monitoring | Conditional specialised judgement skill | Audit whether it contains a useful current method or generic platform advice. |
| `performance` | Measure and improve bottlenecks | Conditional specialised judgement skill | Keep only if it prevents unmeasured optimisation and overlaps cleanly with Assurance. |

## 7. Active skills — Staff Engineering

| Asset | Claimed job | Stage-A classification | Decision needed |
| --- | --- | --- | --- |
| `coding` | Repository-aware implementation discipline | Candidate core judgement skill | Must prove it adds more than model coding ability plus the Staff Engineer contract. |
| `debugging` | Reproduce, isolate, repair, verify, and communicate defects | Core judgement skill | Recent evidence-backed revision exists; prove it on a live defect. |
| `refactoring` | Improve structure while preserving behaviour | Conditional judgement skill | Check safe overlap with Coding, Architecture, and testing. |
| `resolving-merge-conflicts` | Safely recover from a Git conflict | Narrow recovery procedure | Keep only as an on-demand procedure, never as general coding policy. |
| `setup-pre-commit` | Configure local checks before commits | Narrow setup procedure | Keep only if it is current and explicitly approved at use time; never auto-run. |

## 8. Active skills — Assurance and Quality

| Asset | Claimed job | Stage-A classification | Decision needed |
| --- | --- | --- | --- |
| `testing` | Plan and implement useful verification | Core judgement skill | Recent evidence-backed revision exists; test its selection of test types on real work. |
| `security` | Protect trust boundaries and sensitive data | Core assurance judgement skill | Audit current claims against primary sources where needed; never treat generic advice as a security guarantee. |
| `review-audit` | Independently inspect code or decisions | Core assurance judgement skill | Clarify boundary with Debugging and Testing: review finds risks; debugging establishes a fault and repair. |
| `browser-test` | Browser inspection, screenshots, and observable checks | Tool adapter | Keep only as a live-host-aware adapter. |
| `dox` | Directory-contract analysis | Tool adapter | Keep only when that local tool is available. |
| `fallow` | Static JS/TS code intelligence | Tool adapter | Keep only when that local tool is available and report its limits. |

## 9. Active skills — Studio Support

| Asset | Claimed job | Stage-A classification | Decision needed |
| --- | --- | --- | --- |
| `deep-think` | Deliberate reasoning for consequential decisions | Candidate kernel method | Audit duplication with `GEMINI.md` and core reasoning files. It should be an escalation method, not a huge prompt load. |
| `context-hygiene` | Protect a long/resumable task's state and context | Core support method | Preserve authority limits and decide whether it needs a standalone discovery route. |
| `learn` | Propose evidence-backed post-task improvements | Core support method | Prove that it cannot silently alter global policy or memory. |
| `skill-creator` | Create/refactor a skill package after approval | Internal OS-maintenance capability | Keep only as an internal support route, never a client-facing skill. |
| `context-formatting` | Fix narrow Markdown/editor context issues | Narrow legacy procedure | Audit host dependence; likely archive or move to a host-specific reference. |
| `to-tickets` | Convert an approved plan into bounded work items | Narrow planning procedure | Decide whether this is an internal Director operation rather than a public capability. |
| `wizard` | Guide a person through a manual external setup | Narrow procedure | Keep only if it has a real repeatable setup job and does not hide external effects. |

## 10. Active skills — Design, Spatial, and Media

| Asset | Claimed job | Stage-A classification | Decision needed |
| --- | --- | --- | --- |
| `ui-ux` | General usable interface, flow, states, accessibility, and handoff | Core Design judgement skill | Preserve its operation references; audit whether it needs current UI implementation evidence. |
| `color-system` | Former standalone colour selection skill | Archived provenance | Retired from active routing after the 2026-08-19 evidence review. Its compact semantic-role and verification method now lives in UI/UX references; the original is preserved under `global/archives/color-system-v3-source/`. |
| `apply-transition` | Use an old transition.css library effect | Unsafe legacy project recipe | Quarantine from active General routing. Preserve only genuinely reusable notes under a motion reference destination. |
| `reference-intelligence` | Analyse recordings, screenshots, URLs, and precedent sets; translate rather than copy | Conditional Design evidence skill | Promoted to the General profile on 2026-08-19 because reference analysis is useful for ordinary product/UI work as well as Spatial work. It remains conditional, not a default design ritual. Test the plain-English discovery route on a controlled host probe. |
| `motion-library` | Find local motion/effect references by communication job | Selective reference router | Keep provisionally inside Design/Spatial. Decide clear naming and make retrieval automatic through the Design Director. |
| `cinematic-motion` | Decide and plan meaningful spatial motion | Conditional Spatial judgement skill | Keep provisionally; preserve reference index and verify implementation claims at project time. |
| `scroll-storyboard` | Plan intentional scroll choreography | Conditional Spatial procedure/skill | Check whether its method belongs inside Cinematic Motion or remains a separate reusable planning method. |
| `spatial-experience-design` | Spatial website concept, experience, and quality direction | Optional Spatial judgement skill | Preserve its references and project-phase routing while testing one real brief. |
| `storytelling` | Narrative/emotional sequence for spatial experience | Optional Spatial judgement skill | Decide portable storytelling core versus specialist spatial application. |
| `master-design-director` | Senior creative review and taste calibration | Optional Spatial judgement skill | Preserve deliberate creative depth; test its distinct role against the Design Director agent contract. |
| `cinematic-showroom-strategy` | Strategy for a cinematic showroom/portfolio experience | Optional Spatial judgement skill | Audit overlap with spatial experience, storytelling, and brand strategy. |
| `canvas-ui` | Decide/prepare a contained DOM/WebGL visual effect | Experimental technology adapter | Keep optional behind Design Director. Require a source, licence, accessibility, performance, fallback, and approval check each time. |
| `prompt-engineering` | Create image/video generation prompts | Optional Media judgement skill | Clarify its boundary with provider-aware Video Generation. |
| `video-generation` | Plan, prompt, and review directed video across providers | Optional Media judgement skill with reference library | Keep as one front door, not 23 skills. Reverify provider facts only when a project selects them. |

## 11. Active workflows

A workflow survives only when state, handoff, evidence, rollback, or approval matters beyond a local operation.

| Workflow | Plain-English job | Stage-A classification | Decision needed |
| --- | --- | --- | --- |
| `project-inception` | Turn a raw idea/client brief into agreed project truth and the next decision | Genuine coordination route | Keep provisionally; its research-backed revision needs a real pilot. |
| `plan-architecture` | Record a consequential structural decision | Genuine coordination route | Keep provisionally; use only when a decision crosses durable boundaries. |
| `build-feature` | Coordinate approved implementation and handoff | Genuine coordination route | Keep provisionally; prevent it becoming a mandatory waterfall. |
| `debug-issue` | Separate diagnosis, authorised repair, and verification | Genuine coordination route | Keep provisionally; allow narrow bugs to remain lightweight. |
| `database-migration` | Change data safely with compatibility, rollback, and approval | High-consequence workflow | Keep only when a real database migration is in scope. |
| `dependency-upgrade` | Upgrade a dependency with impact and rollback evidence | High-consequence procedure/workflow candidate | Decide from source whether it really needs durable state or should be a Staff/System procedure. |
| `incident-response` | Contain and recover from a live failure | High-consequence workflow | Keep only for real incidents, never as routine debugging. |
| `security-audit` | Independently inspect a security-sensitive boundary | Assurance hard gate | Keep provisionally; distinguish audit from a generic security review. |
| `ship-to-production` | Prepare and approve a production release | External hard gate | Keep. It is an approval boundary, not an automatic deployment command. |
| `os-maintenance` | Make a controlled change to Anti-Gravity itself | Internal coordination route | Keep provisionally; should not run for ordinary project work. |
| `task-dispatch` | Delegate genuinely independent, bounded work | Agent-operation procedure/workflow candidate | Decide whether this belongs in the Studio Director contract rather than the public workflow list. |
| `design-ui` | Coordinate a material UI design phase | Design route/workflow candidate | Decide whether it has enough state/handoff to remain distinct from Design Director skill selection. |
| `test-strategy` | Choose proportionate tests before implementation/release | Assurance procedure | Likely demote from public workflow to Assurance procedure. |
| `verify-project` | Gather final project evidence | Assurance procedure | Likely demote from public workflow to Assurance procedure. |
| `spatial-project-inception` | Coordinate a qualifying spatial/cinematic project | Genuine optional coordination route | Keep provisionally; must not force every website through spatial ceremony. |
| `commercial-decision-record` | Record a material offer, scope, price, or claim decision before commitment | Growth hard gate | Keep only for consequential commercial decisions. |
| `live-learning-loop` | Safely run an approved, bounded commercial/market learning intervention | Growth hard gate | Keep only if its real-world safeguards are operationally usable. |

## 12. Archives and external comparison sources

### Archived Seedance source

The former multi-skill Seedance suite is preserved under `global/archives/seedance-v3-source/`. It includes the former parent package, 23 specialist skills, references, assets, and metadata. It is not installed or loaded by the current manifest.

**Stage-A decision:** keep as provenance only. A useful technique may be selectively curated into the active `video-generation` reference library after current-provider verification. Do not reactivate its 23 standalone skills.

### Separate global Gemini skill folder

The separate host-local Gemini skills folder has 49 top-level folders but is not the V4 system:

- it contains `deriv-bot-engineering`, which has been explicitly removed from the V4 scope;
- it contains an empty `design-workflow-audit` folder;
- it lacks current canonical `offer-architecture` and `setup-pre-commit`;
- 19 same-named packages differ in content from the canonical repository; and
- it has neither the V4 main `GEMINI.md` rule nor V4 custom agents.

**Stage-A decision:** do not delete or overwrite this folder. Compare it skill by skill only when it contains material missing from canonical source. Global installation is a later, separately approved action.

## 13. Gemini multimodal evidence integration candidate

The local Antigravity configuration contains a `gemini-api` plugin, version `1.1.0`. Its manifest describes Gemini Interactions/Live API development and multimodal capability. It is not currently an active Anti-Gravity OS route and it has no `mcp_config.json` in the installed package.

The correct V4 design is:

```text
Website / screen recording / screenshot / user-provided media
        |
Antigravity Browser artifact when available, or user-supplied file
        |
Reference Intelligence — source register, observation vs inference, questions
        |
Optional Gemini multimodal provider — only when built-in analysis is insufficient
        |
Evidence ledger -> Design Director -> keep/adapt/reject/defer decision
```

Rules for this route:

1. The Design Director selects it when visual evidence changes a design decision; Beloved does not need to remember a slash command.
2. Browser screenshots and recordings are direct artifacts. A Gemini/API report is mediated evidence and must be labelled as such.
3. Uploading a private recording, sending a URL/media to an external API, generating media, or incurring provider cost is `dependency_or_network` and needs explicit approval at the time.
4. The agent must record source, date, limitations, observations, inferences, and confidence. It must not claim to have watched something it only received as a transcript/report.
5. No plugin or media provider can change design direction by itself. Its output informs Reference Intelligence; it does not replace creative judgement.

**Decision needed:** run one controlled, non-private reference-analysis probe before adding any plugin-specific instruction to an active skill or agent.

## 14. Stage-A exit gap

The inventory is now complete, but the following reconciliation work remains before Stage A can close:

1. Reconcile the historical 25-workflow snapshot with the live 17-workflow manifest and link the exact migration record. This is resolved in Section 21; the older normalisation document still needs its status line updated.
2. Inspect every active asset's full content against the survival test, beginning with legacy or ambiguous items (`apply-transition`, `coding`, `context-formatting`, `task-dispatch`, `test-strategy`, and `verify-project`).
3. Compare the 19 differing external Gemini packages against canonical only where the external version may contain missing useful material.
4. Run the single safe Gemini multimodal evidence probe after Beloved approves a non-private test input.

Only then do we begin Stage B: the capability map written independently of the old asset names.

## 15. Stage-A source findings — Batch A: ambiguous core routes

This batch inspected the complete live source of the items below. These are stronger than name-based classifications, but their source moves are still deferred until the owning pack is migrated together.

| Asset | Finding from source | Confirmed migration direction | Useful material to preserve |
| --- | --- | --- | --- |
| `apply-transition` | Hard-codes an old Bevamped CSS location and aesthetic, assumes a library is installed, and instructs the agent not to ask permission before edits. | Remove from active General routing; archive as legacy provenance and selectively extract generic CSS transition notes into the motion reference library only if a project needs them. | The distinction between hover, loop, and scroll triggers—after current stack verification. |
| `coding` | Repeats broad model knowledge and existing V4 policy. It also imposes context-free constraints such as three-or-fewer parameters and reading architecture before all implementation. | Demote most content into the Staff Engineer contract and Engineering baseline; retain only concrete repository-aware checks that survive a later proof test. Do not keep an all-code slash skill by default. | Structural verification trace, sibling-pattern check, existing-convention check, and explicit failure-path review. |
| `context-formatting` | Targets three old Markdown-lint codes in Gold Context files. Its examples are malformed/no-op and its instructions are host-specific. | Archive or move to a narrow host-specific repair reference; remove from normal discovery. | A verified, current lint-fix recipe only if a real host still needs it. |
| `task-dispatch` | Has a strong worker charter, exclusive-ownership test, authority ceiling, and evidence integration process. The job is agent coordination, not a user-facing project workflow. | Move its decision checklist and charter into the Studio Director/lead delegation reference. Retire the public workflow after routing tests prove leads can invoke it naturally. | Dispatch decision test, worker charter, integration checklist, and stop conditions. |
| `test-strategy` | Contains a strong risk-to-evidence method, but makes ordinary planning appear stateful and workflow-heavy. | Move the method into `testing` references and the Assurance Lead contract. Keep a resumable record only for material/high-risk work when task state is authorised. | Claim scope, oracle selection, negative cases, evidence limits, and risk-sensitive handoffs. |
| `verify-project` | Contains an honest evidence-interpretation method, but it is a read-only Assurance operation rather than a public stateful workflow for normal work. | Move the method into `testing` references and the Assurance Lead contract. Retain `ship-to-production` as the actual external approval workflow. | Verified-for-scope language, environment recording, result classification, residual-risk reporting. |
| `dependency-upgrade` | The job is real and consequential, but the source currently permits dependency/network work without an immediate approval gate and uses an inconsistent fixed resume path. | Rewrite as an approval-gated Systems/Staff procedure or retain as a workflow only after its state, rollback, and approval contracts match V4. It must not run package-manager mutations by default. | Baseline capture, official migration-note review, impact map, smallest upgrade, verification, and rollback evidence. |

**Batch-A conclusion:** Four current workflow entries are better represented as selected lead procedures (`task-dispatch`, `test-strategy`, `verify-project`, and possibly `dependency-upgrade`). Three current skills are not valid active universal skills in their current form (`apply-transition`, `coding`, and `context-formatting`). No source has been removed by this finding.

## 16. Stage-A source findings — Batch B: Design, Spatial, and Media

| Asset | Finding from source | Confirmed migration direction | Useful material to preserve |
| --- | --- | --- | --- |
| `ui-ux` | Has a clear cross-product interface contract, state coverage, accessibility, responsive design, and selective reference loading. | Keep as the General Design skill. Later remove only reference duplication after a retrieval test. | Register detection, state matrix, interface verification, direct UI-operation routing, and implementation handoff. |
| `color-system` | Contained deterministic colour-psychology, gender, culture, and CTA-conversion claims without usable source context. It also mixed web, print, and generic branding claims. | The focused study completed on 2026-08-19. Retire it from active routing; preserve its source in the archive and move the compact semantic colour/accessibility method into UI/UX references. | Functional colour roles, semantic tokens, contrast checks, and the principle that colour is not the only identity carrier. |
| `storytelling` core | Its core narrative/proof/inquiry method is valuable and specific to spatial work. | Keep the core as a conditional Spatial narrative method. | Controlling argument, chapter jobs, proof choreography, copy constraints, stillness/motion posture. |
| `storytelling` library | The indexed 24-mechanic library promotes horror, disorientation, status threat, dread, and generic brand-archetype recipes. It is not evidence-based, conflicts with the V4 anti-manipulation and anti-template goals, and is not a suitable default source for client work. | Quarantine the library from active routing. Preserve it as unvalidated creative provenance; selectively curate only an evidence-defensible pattern after a specific project needs it. | At most: the non-prescriptive idea that pacing, density, and emotional register need deliberate choice. |
| `spatial-experience-design` | It is the strongest main Spatial package: evidence -> brief -> concept -> blueprint -> production plan, with clear conditional use of motion and generated media. | Keep as the Spatial front door. Audit stale project names and over-prescriptive content later without shrinking its real reasoning depth. | The five logical contracts, three-territory comparison, asset boundary, reference gate, and risk-prototype gate. |
| `master-design-director` | Contains serious senior-critique/taste-calibration material, but duplicates the Design Director agent's role and includes stale Bevamped-specific language. | Keep its depth, but migrate it into a high-stakes `Design Director` critique reference/mode rather than a separate public persona/skill. | Visual-thesis challenge, ranked critique, subtraction before addition, and reference-integrity gate. |
| `cinematic-motion` | Distinctly answers whether spatial motion has a real communication job and how to implement it safely. | Keep as a conditional Spatial skill. | Stillness comparison, motion tracks, asset/performance/fallback gates. |
| `motion-library` | Solves the real retrieval problem: finding a local effect by communication job and comparing it with stillness. | Keep as a selective Design/Spatial reference router; consider the clearer name `motion-reference-library` later. | Semantic-index route and exact-reference-before-implementation rule. |
| `scroll-storyboard` | A strong conditional choreography contract, not a universal design skill. | Move into Cinematic Motion/Spatial references as a selected procedure; preserve its activation test and beat table. | Activation test, beat table, mobile/reduced-motion translation, continuity rules. |
| `cinematic-showroom-strategy` | Useful only for media-heavy spatial work. Its content overlaps Spatial Experience, Cinematic Motion, and Video Generation but has a distinct media-choreography job. | Demote from standalone public skill to a selective Spatial media-choreography reference/procedure. | Brand-to-scene translation, production choreography map, prompt inheritance, and proof chapters. |
| `canvas-ui` | Correctly treats Canvas/WebGL as a contained, approval-gated enhancement with fallbacks. | Keep as an optional technology adapter under the Design Director. | Alternatives comparison, DOM-first fallback, lifecycle/performance and source/licence gates. |
| `prompt-engineering` | Uses an unverified, provider-agnostic fixed prompt formula and does not match modern provider-specific multimodal work. | Retire as a standalone active skill after its useful physical-direction cues move into a smaller Visual Asset Direction reference. | Subject, setting, composition, light, temporal movement, and a clear asset goal. |
| `video-generation` | Has a clean provider-neutral front door, separates provider facts from creative direction, and loads precise references on demand. | Keep as the single Media front door. | Production brief, provider/surface verification, rights/confidentiality, diagnosis, and approval boundary. |

**Batch-B conclusion:** Preserve the substantial Spatial method, but reduce false skill boundaries. The likely end-state is one General UI/UX skill, one main Spatial Experience skill, one Cinematic Motion skill, one optional Canvas adapter, one Video Generation skill, and selective references/procedures below them—not many separate commands Beloved must remember.

## 17. Stage-A source findings — Batch C: Systems, Engineering, and Assurance

| Asset | Finding from source | Confirmed migration direction | Useful material to preserve |
| --- | --- | --- | --- |
| `architecture` | Has a distinct quality-attribute, boundary, ownership, failure, reversibility, and trade-off method. Prior candidate evidence exists. | Keep as a conditional Systems Architect capability; do not repeat synthetic evaluation before a real decision needs it. | Quality attributes, state ownership, failure behaviour, options/trade-offs, and re-evaluation triggers. |
| `api-design` | The job is distinct, but the source uses unsafe universal rules such as versioning every API on day one and treating all collection/API protections identically. | Keep only as a conditional contract-design reference/capability under Systems Architect; rewrite when a real API decision needs current standards. | Consumer-facing contract, additive evolution, error shape, idempotency, compatibility, and documentation discipline. |
| `database` | The job is distinct but contains universal prescriptions such as designing for a billion rows, soft deletes for all recoverable data, and schema/code separation as a single fixed sequence. | Keep only as a conditional data-design/migration reference under Systems Architect; rewrite from current, database-specific evidence when real data work requires it. | Access-pattern-first modelling, integrity/invariants, migration safety, ownership, and measured indexing. |
| `devops-infra` | Mostly broad, provider-free operations slogans and absolute rules; it does not yet provide a right-sized solo-studio method. | Demote into Systems Architect operations/release references, plus `ship-to-production` and Incident workflows. Do not keep as an everyday standalone skill. | Observability, deployment/rollback, secret handling, blast-radius, and operational simplicity questions. |
| `performance` | Provides a useful measurement-first diagnostic method, but includes context-free mandates such as universal p95/p99 and production-scale tests. | Keep as a conditional Systems capability or reference. Rewrite its standards only when the target system, browser, or platform is known. | Baseline -> hypothesis -> single change -> re-measure loop; before/after evidence and operational trade-offs. |
| `debugging` | A strong, current evidence-led diagnosis/repair contract with modes, hypothesis discipline, and explicit authority. | Keep as a core Staff Engineer capability. | Observation/inference separation, discriminating tests, repair gate, and honest outcomes. |
| `refactoring` | A useful behaviour-preservation method, but it is a Staff Engineer operation rather than a public studio role. | Move to a selected Staff Engineer reference/procedure after tests protect its retrieval route. | Characterisation evidence, scope containment, cost of debt, incremental versus rewrite decision. |
| `resolving-merge-conflicts` | The conflict method is useful, but it tells the agent to stage/continue a merge and uses hard-coded commands without an immediate approval check. | Keep only as an approval-gated, on-demand recovery procedure. | Intent comparison, no silent discard, conflict-marker check, and repository-native verification. |
| `setup-pre-commit` | Assumes Husky/Prettier, permits dependency installation, creates configuration, stages all files, and commits. That is not safe universal OS behaviour. | Remove from active discovery; retain only a rewritten, project-specific setup recipe when explicitly requested and approved. | Existing-tool detection and fast-hook principle. |
| `testing` | A strong evidence-selection and interpretation method, including AI-feature evaluation and honest result language. | Keep as a core Assurance capability; absorb test planning/verification procedure material from the two public workflow candidates. | Claim/risk/boundary mapping, oracle selection, test-level choice, and residual-risk language. |
| `security` | Contains a useful trust-boundary and object-level authorization method, but has generic prescriptions and lacks source/provenance routing for changing standards. | Keep as a conditional Assurance capability. Reverify detailed standards only for actual high-risk work; do not claim an audit guarantees security. | Trust boundary, assets, abuse path, object-level authorization, secret handling, and fail-safe review. |
| `review-audit` | Its independent-review job overlaps the Assurance Lead and Testing but remains useful as a structured adversarial review mode. | Move into Assurance Lead reference/mode rather than a separately advertised skill. | Scope-first review, severity/confidence, evidence traceability, and actionable findings. |
| `browser-test` | Hard-codes a Windows Playwright MCP protocol that may not exist on the active host. | Replace with a live host-browser adapter that detects available browser capability. It must integrate with Reference Intelligence but not assume a tool name. | Observable browser evidence and a clearly stated verification scope. |
| `dox` | Repeats the repository `AGENTS.md` traversal rule. It is a baseline policy, not a user-facing specialist skill. | Move into the Engineering baseline/Director contract; retain a small reference only for creating directory contracts. | Root-to-target contract traversal and local contract update conditions. |
| `fallow` | Vendor/tool-specific static-analysis instructions, not independent engineering judgement. | Keep only as an optional tool adapter, with live version/availability verification at use time. | Machine-readable output, dry run before fixes, false-positive limits, and no telemetry activation. |

**Batch-C conclusion:** The durable engineering kernel is smaller than the current file list suggests: Architecture, Debugging, Testing, and conditional Security clearly earn focused methods. API, database, performance, and operational work remain conditional specialist routes. The remaining material belongs in lead contracts, references, or tool adapters—not in a list Beloved must manually choose from.

## 18. Stage-A source findings — Batch D: Product, Growth, Research, and Studio Support

| Asset | Finding from source | Confirmed migration direction | Useful material to preserve |
| --- | --- | --- | --- |
| `research-analysis` | Has a useful option-comparison and uncertainty method. It does not need to be a public command Beloved remembers for every search. | Keep as the Product Strategy Lead's evidence-and-decision method. Invoke it only when an option, cost, adoption, or reversibility decision is genuinely open. | Decision criteria, strongest-case comparison, invalidating conditions, calibrated recommendation, and re-evaluation trigger. |
| `brand-strategy` | Provides a real evidence-to-perception-gap-to-creative-brief method, but its current signals and enemies are intentionally specific to premium spatial studios. | Preserve as a conditional Spatial/Growth method. Do not falsely broaden it into universal brand doctrine. Commission focused research before a general-brand version is created. | Fact/reported/inference/unknown discipline; perception gap; proof burden; category rejection; creative constraints rather than premature visual prescription. |
| `competitor-profiling` | Has a sound source/snapshot principle, but it hard-codes Firecrawl and DataForSEO, assumes paid/tool access, and tells the agent to persist raw external data as a default. | Replace with a tool-optional Market and Competitor Evidence reference under Product/Growth. Any browser/API use, cost, or persistent data collection must be selected from the live host and approved at the point of use. | Comparable evidence cards, snapshot date, fact/inference separation, honest strengths and weaknesses, and a cross-competitor synthesis. |
| `expert-positioning` | Is the strongest commercial method in the current Growth pack: it distinguishes honest service posture, proof, mutual fit, scope, and commercial boundaries. | Keep as a conditional Growth judgement method. It should inform the Growth Lead; it must not manufacture exclusivity, proof, or prices. | Commercial-posture selection, proof architecture, fit questions, diagnosis/prescription boundary, and truthful case-study posture. |
| `offer-architecture` | Is narrowly scoped to a material service/product offer and already separates human approval from external commitment. | Keep as a conditional Growth decision method. Validate it on the next real offer before adding more content. | Scope object, inclusions/exclusions, handoffs, proof limits, and approved decision record. |
| `copywriting` and `copy-editing` | The split is useful: one creates or materially rewrites a claim; the other preserves intent while improving an existing asset. Neither establishes product truth or a commercial promise. | Keep both as small Growth output methods, selected by the Growth Lead rather than memorised commands. Require source/evidence context when a claim is material. | Claim boundaries, audience/context checks, and the distinction between a fresh draft and bounded editing. |
| `marketing-psychology` | The present version correctly rejects manipulation and routes ownership to Product, UX, Testing, or Growth. Its contribution is a hypothesis/dignity check, not a persuasion machine. | Demote to a selected Ethical Behavioural Insight reference under Growth/Product. Do not keep a separate default public skill. | Decision-friction hypothesis, ethics boundary, evidence limits, and correct owner routing. |
| `page-cro` | Has a practical conversion-diagnosis outline, but it currently reads as generic best-practice advice and can be misused without traffic/qualitative evidence. | Move into a joint Growth/Design conversion-diagnosis reference. Invoke only for a stated page, funnel, or measurable decision—not as a blanket website makeover recipe. | Value/clarity/friction/proof diagnosis, test ideas as hypotheses, and separation of observed data from recommendation. |
| `prospect-research` | Preserves a genuinely useful local dossier workflow and validation script. Its narrow luxury-interior ICP, fixed scores, `/last30days` route, and team-size rule are campaign assumptions—not universal truth. | Keep as a conditional Growth capability for the current Cinematic Digital Showroom campaign; later generalise the evidence model, not the old score thresholds. | Dossier template and helper script; evidence-before-score; specific website/portfolio gap; human-reviewed next action; no autonomous outreach. |
| `sales-enablement` | Is a large generic B2B SaaS playbook with invented ROI framing, fixed deck lengths, and tool/role assumptions unrelated to a one-person studio. | Remove from active discovery after its truthful, reusable pieces are extracted into Offer Architecture, Copywriting, and a future client-specific collateral reference. Preserve its source as provenance; do not silently delete it. | Asset-to-buyer-stage matching, objection/proof structure, and customisation requirement—only when actual evidence exists. |
| `deep-think` | Duplicates the V4 core reasoning protocol and is valuable as an escalation signal, not as a separate domain capability. | Move to the Studio Director baseline as an explicit Type-1/complex-decision mode. Keep the current files as the full on-demand protocol. | Assumption audit, competing frames, second-order effects, pre-mortem, and verification plan. |
| `context-hygiene` | Provides sound rules for safe handoff and authorised task state. This is an operating safeguard, not an end-user specialist service. | Move to the Studio Director baseline and resumable-work contract. Keep it discoverable only for an explicit handoff or long-task recovery. | Smallest effective state, no automatic memory writes, safe resume record, and no unnecessary thread split. |
| `learn` | Has a good audit-before-apply model and an explicit no-new-skill reflex. It is already aligned with the needed “get better without uncontrolled mutation” behaviour. | Keep as an internal post-task improvement method for the Studio Director/OS Maintenance route, not a generic public skill. | No-change option, promotion standard, approved destinations, and regression/evaluation choice. |
| `skill-creator`, `to-tickets`, and `wizard` | These are maintenance/procedure helpers, not capabilities a client project should discover. `wizard` is additionally Bash-specific and cannot be assumed on Antigravity/Windows. | Move them to internal OS-maintenance or lead procedures. Keep them available only when the requested job explicitly matches; do not load them into ordinary tasks. | Package/reference-routing discipline; vertical slicing/acceptance criteria; explicit manual-step confirmation and secrets safety. |

**Batch-D conclusion:** Growth is not a bag of persuasion tricks. Its durable jobs are evidence, positioning, offer boundaries, honest writing, and a narrowly governed prospect process. Most “growth” material should be selected by the Growth Lead, not exposed as commands Beloved must remember. The Studio-support material belongs in the Director’s operating contract unless a specific maintenance or handoff request activates it.

## 19. Stage-A source findings — Batch E: workflow truth audit

The 17 active files are not equally modern. The workflow name alone is not proof that its body follows V4 authority, current skill names, host availability, or the non-waterfall collaboration model.

| Workflow | Finding from source | Confirmed migration direction |
| --- | --- | --- |
| `project-inception` | Current V3 source is proportionate, routes from uncertainty rather than a fixed sequence, and invokes Product/Design/Architecture/Engineering/Assurance as needed. | Keep as the primary intake-and-framing coordination route. Test it on a real project before treating it as final. |
| `spatial-project-inception` | Current V4 source has conditional lenses and preserves creative divergence, evidence, reference intelligence, and prototypes. | Keep as the optional spatial route. It must never replace general `project-inception` for ordinary websites or apps. |
| `debug-issue` | Current V2 source clearly separates diagnosis, proposal, implementation, and incident mitigation. | Keep as the defect coordination route. |
| `design-ui` | Current V2 source is proportionate and requires a durable decision/handoff only when design work warrants one. | Keep provisionally as the Design Director's material-design route; validate with a real interface task. |
| `task-dispatch` | Its worker charter is strong, but it describes lead-agent operation rather than a task a user chooses. | Its decision test, charter, and integration test are now in the Studio Director contract. Retain its source as a compatibility reference until the controlled host-routing pilot proves natural director delegation; then retire it from the public workflow menu. |
| `test-strategy` and `verify-project` | Their V2 methods are good, but most runs are selected Assurance operations rather than durable public workflows. | Migrate their methods into Testing/Assurance Lead. Retain resumable workflow state only when risk, evidence, or handoff makes it necessary. |
| `commercial-decision-record` and `live-learning-loop` | Both are current, evidence/approval-gated growth routes. | Keep only for consequential claims, pricing, scope, data collection, messaging, traffic, or live experimentation—not everyday copy. |
| `os-maintenance` | It scopes Anti-Gravity changes and has a validation step. | Keep as the internal reform route, not a project-facing workflow. |
| `database-migration`, `incident-response`, and `ship-to-production` | Their high-consequence jobs are real, but their bodies need a source-by-source V4 rewrite before they can be trusted as active routes. The current release workflow contains generic platform assumptions and operational thresholds that cannot be universal. | Preserve as approval-gated high-risk templates. Do not invoke to mutate production until a project-specific plan, target, rollback path, and just-in-time approval exist. |
| `dependency-upgrade` | Current source permits package/network work too easily and has an unsafe fixed resume path. | Rebuild as an approval-gated Systems/Staff procedure or retain only if state/rollback contracts prove it needs a workflow. |
| `build-feature`, `plan-architecture`, and `security-audit` | Their body text is old “full source” material: forced phases, obsolete `skill-*` names, assumed context files, and universal step lists. They conflict with V4’s conditional-agent design. | Freeze from new use and replace with short, current coordination routes built on V4 director/skill names and live workspace facts. Preserve their legacy source until a successor passes routing and behaviour tests. |

**Batch-E conclusion:** The true future public workflow menu will be smaller than 17. Task dispatch, test strategy, and verification are likely director procedures. High-risk operations remain explicit templates and approval gates, never autonomous commands.

### Batch-E implementation update — 2026-08-19

The four inherited legacy coordination bodies have now been replaced with V4 contracts:

| Workflow | Completed repair |
| --- | --- |
| `build-feature` | Replaced the forced legacy sequence and obsolete `skill-*` references with a selected-lead collaboration loop, scoped implementation gate, state contract, and evidence handoff. |
| `plan-architecture` | Replaced mandatory tier theatre and assumed contexts with a proportional, evidence-labelled decision record and clear implementation boundary. |
| `security-audit` | Replaced generic checklist/certification posture with a read-only independent audit, evidence/confidence/severity record, and owning-workflow remediation handoff. |
| `ship-to-production` | Replaced generic release mechanics with target-specific readiness, explicit just-in-time external approval, observation, and rollback/containment contract. |

`python global/scripts/os.py validate --json` and `git diff --check` passed after the four replacements. Database migration, incident response, and dependency upgrade remain the next high-consequence source reviews; no production or external action was performed.

## 20. What Stage A has now proven

1. The live manifest's 48 skills and 17 workflows are a **working inventory**, not the finished public design.
2. There is no basis for deleting more files now. Every proposed demotion preserves a destination and requires a retrieval/routing test before the source is retired.
3. The next productive work is a **capability map independent of old filenames**, followed by a one-pack-at-a-time migration. It is not another synthetic architecture test.
4. The colour-system study closed on 2026-08-19: its active successor is the conditional UI/UX colour method and its prior source is archived. A general-brand study becomes necessary only if we decide to broaden `brand-strategy` beyond its spatial domain; it is not needed to preserve the current spatial method.
5. Gemini multimodal/browser use will enter through Reference Intelligence and Design Director routing after one non-private, controlled host probe—not by asking Beloved to remember a plugin or slash command.

## 21. Historical workflow-count reconciliation

The earlier `25` was an **interim count**, not a competing target. The exact trace is now documented by `docs/v4-phase-7-workflow-truth-audit.md`:

```text
52 original workflow registrations
  - 21 General Impeccable wrapper migrations
= 31 interim routes
  + 2 Growth hard-gate routes
= 33 routes at that historical point
  - 7 General direct-operation migrations
= 26 historical snapshot
  - 7 Spatial direct/phase migrations
  - 1 Media direct-route migration
= 17 live manifest routes
```

The seven General direct operations were `context-hygiene`, `design-api`, `optimize-performance`, `refactor-module`, `review-code`, `ui-craft`, and `ui-animate`. The seven Spatial migrations were `impeccable-animate`, `impeccable-craft`, `reference-intelligence`, `spatial-concept`, `spatial-design-ui`, `storytelling`, and `visual-brainstorm`. The one Media migration was `video-generation`.

Each migration had a named destination in a skill or selective Spatial/Media reference. This explains the number change; it does **not** settle the separate source-quality question in Batch E. In particular, the 17 retained routes still need the legacy-body rewrites identified there before V4 can be called finished.

## 22. Separate Gemini skill-folder comparison — Canvas UI first

Beloved identified a separate host-local Gemini skills folder as a possible newer source. It is a separate, unmanaged copy—not the canonical V4 source—so its content must be compared rather than copied over wholesale.

| Package | Comparison result | Decision |
| --- | --- | --- |
| `canvas-ui` | The external copy contains a larger component list and generic GLSL snippets, but it hard-codes the old `Kingdaddy007/canvas-ui` repository and unverified `npx` commands. It has no Codex/portable agent metadata. The canonical package has the safer decision/fallback method and explicitly records that the old host-local URL is not an upstream source. | Do **not** merge the external catalog or shader recipes as authoritative material. Preserve the external copy untouched as provenance. Recheck an exact upstream component, source, licence, command, and framework only when a real project selects Canvas UI. |
| `reference-intelligence`, `ui-ux`, `spatial-experience-design`, `video-generation`, `debugging` | Canonical V4 contains additional routing, evidence, adapter, or reference material that the external copy lacks. | Keep canonical V4 as the source of truth; external copies remain comparison evidence only. |
| `product-thinking` and `testing` | The external copies are larger in parts but differ materially from the recently research-backed canonical packages. Larger size is not proof of better guidance. | Do not merge by size. Compare a named missing behaviour only if a real task exposes it. |
| `motion-library` | File counts and size match. | No action needed. |

**Rule:** the separate Gemini folder is neither deleted nor installed over. Any valuable external fragment is admitted only with source, current relevance, licence/provenance where code is involved, a named destination, and a retrieval test.
