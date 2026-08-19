# Anti-Gravity OS v4 — Phase 1 Asset Inventory and Classification

**Status:** Complete — read-only inventory and provisional classification
**Date:** 2026-08-18
**Basis:** The approved v4 operating model, the current canonical repository, generated payloads, and the installed Codex payload. No external research was used and no existing OS asset was changed.

## 1. Executive Decision

The present Anti-Gravity OS is structurally healthy and fully installed for Codex, but it is a **v3 system with a v4 target model**, not a completed v4 operating system.

That is good news. The existing work is real, validated, and worth preserving. The correct path is not to delete it or begin rewriting the skill library blindly. The correct next phase is to define the v4 responsibility contracts that will decide which assets remain universal, which become departmental procedures, which move behind optional packs, and which are archived from active routing.

## 2. Evidence Snapshot

| Check | Result |
| :--- | :--- |
| Canonical skill files | 71 |
| Manifest skill records | 71; exact match with canonical files |
| Canonical workflow files | 52 |
| Manifest workflow records | 52; exact match with canonical files |
| Canonical skill metadata | Every skill has a valid hyphen-case name and description |
| Repository validator | os.py validate reported 0 issues |
| Automated test suite | 43 tests passed |
| Installed Codex skills | Legacy V3 installation must be regenerated before it can match the revised canonical source |
| Installed Codex workflows | All 52 canonical workflows match byte-for-byte |
| Oversized skill bodies | 13 exceed 250 lines |
| Oversized workflow bodies | 19 exceed 250 lines |

The inventory began with 72 canonical skills in a prior local host installation. The canonical source now has 71 after the scope correction, so existing host installations must be regenerated before they are treated as current. The earlier host installation also contained the prior 52-workflow snapshot.

There is one installed user skill outside the canonical repository: **scroll-scrubbed-hero-video**. It is a sound, narrow implementation skill, but it must enter the same audit process before it becomes part of v4 canonical source. Codex also supplies five protected system skills; those are host capabilities, not Anti-Gravity assets.

## 3. What Is Canonical Today

| Area | Current location | Current role | v4 inventory finding |
| :--- | :--- | :--- | :--- |
| Behavioural policy | global/GEMINI.md | Portable master policy | v3 policy, 285 lines; needs later conversion to the Studio Director and lead-contract model. |
| Global router | global/GLOBAL_MEMORY.md | Task routing and runtime assembly | v3 router, 370 lines; it currently contains too much always-loaded material for v4's lean-policy goal. |
| User preferences | global/USER_PROFILE.md | Optional preference layer | Keep as a bounded preference layer. |
| Registry | global/manifest.yaml | Canonical assets and host profile mapping | Healthy registry, but declares OS version 3.0.0 and only general / spatial profiles. |
| Skills | global/skills | 71 active canonical domain packages; inventory began with 72 before the scope correction | Preserve as source; do not edit until the functional contracts exist. |
| Workflows | global/workflows | 52 active routes and procedures | Too many are globally routable; classify by v4 workflow level. |
| Stable baselines | global/baselines | Authority, context, engineering, source verification | Keep as v4 safety inputs; later align wording with the approved operating model. |
| Project scaffolds | global/context_templates | 18 blank project-template records | Keep as scaffolds, not runtime truth. Several are large and need a later lean-template audit. |
| Supporting references | Skill-local references, global/reference, and global/design-audit | Specialist recipes and creative research | Preserve; several root collections are not individually registered in the manifest. |
| Host adapters | global/adapters | Gemini, Codex, Cursor, Windsurf, and OpenCode mappings | Keep. Five adapters exist and the validator accepts all five. |
| Generated payloads | dist | Build output | Not canonical source. Treat the empty dist/codex-spatial folder as stale generated output to reconcile later, not as editable source. |

## 4. Functional Skill Map and Provisional Disposition

This table classifies all 71 canonical skills at the bundle level. It is a decision queue, not an instruction to rewrite every item immediately.

| v4 functional home | Current skills | Proposed disposition | Reason |
| :--- | :--- | :--- | :--- |
| Systems Architect | architecture, api-design, database, devops-infra, performance | Keep; audit for compression and current evidence | These map directly to system boundaries, contracts, data safety, operational constraints, and measured reliability. |
| Staff Engineer | coding, debugging, refactoring, resolving-merge-conflicts, setup-pre-commit | Keep; separate implementation guidance from setup/tool recipes | They support implementation and local corrective work. setup-pre-commit may later become a procedure or template rather than a globally discoverable skill. |
| Assurance and Quality | browser-test, security, testing, review-audit, fallow, dox | Keep; clarify independent-assurance versus lead self-check | These are the strongest base for verification, testing, security, code review, and contract checks. fallow is partly a tool adapter and should be evaluated as such. |
| Product and Strategy / evidence | product-thinking, research-analysis, competitor-profiling, reference-intelligence | Keep; make reference-intelligence general rather than spatial-only | Product framing and evidence analysis are not spatial-only. The current spatial profile for reference-intelligence conflicts with its wider v4 role. |
| Studio operating support | deep-think, context-hygiene, learn, skill-creator, to-tickets, wizard, context-formatting | Consolidate or move behind Director / internal procedures | These govern how the Studio works rather than a customer-facing delivery discipline. context-formatting is unusually narrow and is a likely archive-or-maintenance candidate. |
| General design | ui-ux, color-system, scroll-storyboard, apply-transition | Keep design capability; demote narrow helpers where appropriate | These belong to the Design Director. apply-transition is likely a tool-backed helper rather than a primary global skill. |
| Growth, positioning, and outreach | copywriting, copy-editing, marketing-psychology, page-cro, expert-positioning, sales-enablement, prospect-research, brand-strategy | Move behind an optional Growth / Client-Strategy pack | Valuable capabilities, but not required for every software build. brand-strategy and prospect-research are currently intentionally spatial and should remain scoped. |
| Spatial Design optional pack | spatial-experience-design, storytelling, master-design-director, cinematic-motion, cinematic-showroom-strategy, motion-library | Keep as optional spatial pack | High-quality specialist capability. It must not be loaded for ordinary product work. |
| Generative media optional pack | prompt-engineering, video-generation, seedance plus its 23 specialist Seedance skills | Create an optional Media / Video pack | The current general profile includes all of these. That conflicts with v4's optional specialist-pack rule and creates excessive discovery surface. |

## 5. Workflow Inventory and Provisional Reclassification

The repository currently presents all 52 workflow files as equal active workflows. v4 requires three distinct levels instead: Studio Routes, Department Procedures, and Hard Gates.

| Proposed v4 level | Current workflow set | Proposed disposition |
| :--- | :--- | :--- |
| **Studio Routes** | task-dispatch, project-inception, build-feature, debug-issue, plan-architecture, design-api, database-migration, dependency-upgrade, incident-response, review-code, security-audit, verify-project, ship-to-production, os-maintenance, refactor-module, optimize-performance, test-strategy, context-hygiene | Retain as the candidate route layer, then rewrite their ownership and handoff language around the Studio Director and five functional leads. |
| **Design Department Procedures** | design-ui, ui-craft, ui-animate, plus the 23 impeccable workflows | Remove from universal routing and consolidate into the Design Director's procedure pack. design-ui currently says Impeccable owns all visual design, which conflicts with the approved v4 Design Director boundary. |
| **Spatial Optional-Pack Procedures** | spatial-concept, spatial-design-ui, spatial-project-inception, storytelling, visual-brainstorm | Preserve behind the spatial profile. Re-evaluate their sequencing so they are selectable procedures, not a forced waterfall. |
| **Evidence Procedure** | reference-intelligence | Move to a general evidence-analysis procedure owned jointly by Product/Strategy and Design when visual translation is required. It should not be spatial-only. |
| **Growth / Media Procedures** | marketing-copy, video-generation | Put behind optional Growth and Media packs; do not present them as universal Studio routes. |

## 6. Findings That Matter Before Asset Authoring

### High: v3 and v4 are different operating models

The repository validates its present v3 architecture, but it has no v4 Studio Director contract, no five v4 functional-lead contracts, and no v4 worker-charter implementation. The new v4 specification is therefore the target, not installed reality.

**Action later:** Phase 2 defines the functional contracts before any asset rewrite.

### High: profile model is too broad

The manifest has only two profiles: general and spatial. Every spatial-capable asset also participates in the general profile, except nine spatial-only skills. This means the general profile currently includes the whole Seedance package, video generation, and prompt engineering.

**Action later:** Add optional pack/profile routing for Media / Video and Growth.

### High: the UI workflow system has a competing authority

workflow-design-ui.md gives Impeccable ownership of all visual design, UI craft, and motion. The new operating model assigns that professional boundary to the Design Director. The 23 Impeccable workflows are useful source material, but they are not a sixth permanent organisation.

**Action later:** Reclassify them as Design Department procedures and retain only the smallest useful route surface.

### High: several workflow text references are not portable or resolvable

The Markdown-link validator passes, but several workflow prose references are not executable paths. For example, reference/live.md does not exist anywhere in canonical source, yet is cited by the Impeccable layout, colour, typeset, and live workflows. Other workflow prose assumes host-specific helpers or paths.

**Action later:** Any workflow retained after classification must use a manifest-resolved resource reference or a real relative link. No retained workflow may depend on an implied path.

### Medium: always-loaded policy is larger than the v4 target

global/GEMINI.md is 285 lines and global/GLOBAL_MEMORY.md is 370 lines. The present assembly expects both as Tier 1 material. That is 655 lines before task-specific skills, references, or project context.

**Action later:** Keep the safety invariants, but split operational detail into lead contracts, workflows, and references. Do not simply shorten text without preserving the protections.

### Medium: large assets and duplicated indexes need a purposeful audit

Thirteen skills and nineteen workflows exceed 250 lines. Fourteen skill packages contain the exact same resource-index file. Length and duplication alone are not proof an asset is bad, but they identify the highest-value review queue.

**Action later:** Start Phase 3 with the highest-use core assets, then extract examples, dated research, and repeated indexes only where doing so improves discoverability or reduces maintenance.

### Medium: unregistered reference collections need an owner

global/reference contains six spatial reference documents and global/design-audit contains thirty site-audit documents. They are preserved in builds but are not represented as individually auditable manifest assets.

**Action later:** Assign them to the Spatial pack's reference index or archive them from active routing after an evidence/freshness review.

## 7. Items Explicitly Preserved

Nothing was deleted, moved, rewritten, installed, pushed, or deployed during this phase.

The following remain protected source material until their later audit:

- all 71 canonical skills and their references;
- all 52 canonical workflows;
- the existing spatial design and Seedance resource packages;
- the current generated adapters and Codex installation;
- the installed-only scroll-scrubbed-hero-video skill, pending canonical intake.

## 8. Phase 2 Exit Target

The next phase is **not** “update all skills.” It is the v4 functional-contract phase.

It should produce, in this order:

1. a Studio Director contract: intake, risk sizing, lead selection, integration, and approval stops;
2. one contract each for Product and Strategy, Systems Architect, Design Director, Staff Engineer, and Assurance and Quality;
3. a standard worker charter and lead-to-lead escalation record;
4. a profile/pack routing decision for General, Spatial, Media, and Growth;
5. a precise mapping from the inventory above to the chosen lead, workflow level, and asset disposition.

Only after those contracts are accepted do we begin selective skill and workflow authoring.
