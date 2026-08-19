# Anti-Gravity OS v4 - Manifest and Router Design

**Status:** design review only; no canonical source, installed payload, or generated distribution has changed  
**Date:** 2026-08-18  
**Depends on:** [V4 master asset decision ledger](v4-master-asset-decision-ledger.md), [V4 operating model](../V4_OPERATING_MODEL_SPECIFICATION.md), and [V4 functional contracts](../V4_FUNCTIONAL_CONTRACTS.md)

## 1. Decision this phase makes

This phase defines how V4 will answer two different questions without confusing them:

1. **Task routing:** Which functional boundaries, optional packs, workflow mode, and approval gate are relevant to this request?
2. **Host payload composition:** Which canonical assets are installed or generated for a particular host and selected set of packs?

They are related, but they are not the same thing. A route is a reasoned decision for one task; a payload is a portable collection of files. Neither one grants authority. Host policy, explicit user approval, and applicable repository contracts still control mutations and external effects.

## 2. What the current source already does well

The present V3 builder has a sound, small composition rule:

```text
selected assets = assets tagged "general" + assets tagged with one requested profile
```

`global/scripts/os.py` already enforces that rule with `selected_profiles = {"general", profile}`. It keeps general engineering available when `spatial` is selected and allows the general payload to exclude current spatial skills and workflows.

The existing JSON-compatible `global/manifest.yaml` is also the single registry for the current 71 skills and 52 workflows. This is worth preserving. V4 must not create a second editable inventory merely to describe routing.

## 3. Gaps V4 must resolve

| Current fact | Why it is a V4 gap | Required design response |
| --- | --- | --- |
| Only `general` and `spatial` profiles exist. | Media and Growth still leak into general discovery. | Add the two packs and retag assets from the master ledger. |
| Build and install accept one `--profile`. | A real request can need General + Spatial + Media, but the current command cannot generate that combination. | Preserve the one-pack shorthand, then add explicit multi-pack composition. |
| `manifest.yaml` is schema version 1 and has only `id`, `path`, and `profiles` per asset. | V4 needs ownership and delivery-role metadata for routing and auditing. | Make one coordinated, versioned manifest/schema/validator migration; do not bolt on a duplicate catalog. |
| `global/reference/` is copied into every payload unconditionally. | Its current file names include spatial material such as interior archetypes, materials, scene-kit requirements, and motion patterns. A General-only installation therefore still receives specialist content. | Register references as profile-scoped assets instead of copying their directory globally. |
| `global/design-audit/` is special-cased for only `spatial`. | This pattern does not scale cleanly to Media or Growth resources. | Treat every profile-specific resource through the same manifest-driven registry mechanism. |
| The current router fixture records exactly one profile. | It cannot prove that a mixed request selects only the necessary packs. | Evolve fixtures to declare an ordered set of packs plus a primary workflow, lead set, mode, and authority limit. |

## 4. Target profile model

`general` remains a base capability, not an optional pack. The three packs are intentionally narrow.

| ID | Kind | Activated when | Does not activate for |
| --- | --- | --- | --- |
| `general` | mandatory base | Every task | N/A |
| `spatial` | pack | Interior, spatial, showroom, architecture-adjacent, furniture/decor, staging, or an expressly cinematic spatial experience | Ordinary SaaS, backend, dashboard, and general UI work |
| `media` | pack | Image/video generation, media direction, provider-specific video work, or a named Seedance request | A normal product feature that merely contains an image or video field |
| `growth` | pack | Positioning, copy, conversion, prospecting, outreach, sales collateral, or client-acquisition work | Routine product requirements, backend, security, debugging, or engineering |

The normal result is therefore a set, not a hierarchy:

```text
ordinary SaaS feature       -> { general }
interior showroom concept   -> { general, spatial }
showroom + generated film   -> { general, spatial, media }
sales page for that studio  -> { general, spatial, growth }
```

No pack changes the authority hierarchy, enables autonomous external action, or makes its specialist workflows mandatory.

## 5. Functional boundaries and packs are orthogonal

Functional boundaries answer **who is responsible for what kind of decision**. Packs answer **which specialist resources are discoverable for this particular domain**.

| Routing output | Meaning | Examples |
| --- | --- | --- |
| `functional_leads` | Professional decision boundaries the Studio Director activates | Product & Strategy, Systems Architecture, Design Direction, Staff Engineering, Assurance & Quality |
| `active_packs` | Narrow domain resources that may be loaded | `spatial`, `media`, `growth` |
| `workflow` | A route or hard gate, selected only if it protects the task | `project-inception`, `build-feature`, `security-audit`, `video-generation` |
| `mode` | The permitted kind of work | `diagnose`, `propose`, `implement`, `incident-mitigate` |
| `maximum_mutation_class` | The ceiling, not permission to perform an action | `read_only` through `external_or_production` |

For example, a Staff Engineer can implement a spatial website without “becoming” a permanent Spatial agent. The Design Director may ask the Staff Engineer to resolve a technically infeasible motion treatment. Assurance is independent when the risk justifies it; it is not a compulsory relay stage for every edit.

## 6. Manifest contract: recommended V4 shape

### 6.1 Keep one manifest; move it to schema version 2

The manifest should remain the single authored registry. Because V1 explicitly rejects additional fields and the Python validator currently requires `schema_version: 1`, ownership metadata cannot be added safely as an undocumented extra field.

The recommended first source batch is a coordinated **V1 to V2** migration of:

- `global/manifest.yaml` (which is currently JSON syntax despite its `.yaml` extension);
- `global/schemas/manifest.schema.json`;
- the standard-library validation in `global/scripts/os.py`; and
- manifest/build/fixture tests.

The file can remain JSON-compatible under its current filename. Renaming it or introducing a YAML parser is unnecessary churn and would add a dependency or a more complex parser without helping V4.

### 6.2 Profile definitions

V2 should make the existing profile files and the manifest agree. The manifest carries machine-readable composition metadata; `global/profiles/<id>/profile.json` carries the human-readable activation and exclusion explanation installed with that profile.

Illustrative shape only:

```json
{
  "schema_version": 2,
  "profiles": ["general", "spatial", "media", "growth"],
  "profile_definitions": {
    "general": { "kind": "base", "extends": [] },
    "spatial": { "kind": "pack", "extends": ["general"] },
    "media": { "kind": "pack", "extends": ["general"] },
    "growth": { "kind": "pack", "extends": ["general"] }
  }
}
```

`general` is the only base profile. Every other profile must extend it. A cycle, an unknown parent, or a second base profile is invalid.

### 6.3 Asset metadata

Every registry item keeps its stable `id`, portable `path`, and `profiles` membership. V2 adds only metadata necessary to audit and route it:

| Field | Purpose | Example values |
| --- | --- | --- |
| `functional_owner` | Primary accountable functional boundary | `product_strategy`, `systems_architecture`, `design_direction`, `staff_engineering`, `assurance_quality`, `studio_support` |
| `delivery_role` | What the asset contributes | `capability`, `route`, `procedure`, `tool_adapter`, `reference`, `template`, `baseline` |
| `profiles` | Base or optional pack membership used for build selection | `['general']`, `['media']`, `['spatial', 'growth']` |

The current registry name already tells the builder whether an item is a skill, workflow, template, or baseline. `delivery_role` is deliberately about how it should be treated, not a second type system. Thus `apply-transition`, `fallow`, and `dox` can remain useful while being honestly routed as a conditional `procedure` or `tool_adapter`, rather than being mistaken for general reasoning authorities.

Asset membership rule:

```text
Core asset              -> tag only general
Specialist-only asset   -> tag only its relevant pack(s)
Cross-domain asset      -> tag general only, unless it truly cannot be useful without a pack
```

Because `general` is automatically included, a core asset must not also be tagged to every pack merely to keep it available. Removing those redundant tags is what prevents profile drift.

### 6.4 Resources must become registered assets

Add a `resources` registry rather than keeping special global copies for `reference/` and `design-audit/`. Each resource entry follows the same `id`, `path`, `profiles`, `functional_owner`, and `delivery_role` contract.

This is essential for content boundaries. The V4 source batch should classify each reference before it is moved or retagged; no source file is discarded merely because it is currently copied globally.

## 7. Builder and installer composition

### 7.1 Compatibility and target interface

The existing commands remain meaningful:

```text
build --host codex --profile general
build --host codex --profile spatial
install --host codex --profile spatial --target <path> --dry-run
```

In V4, `--profile <pack>` remains a backward-compatible shorthand for `general + <pack>`. The target interface adds an explicit repeatable or comma-separated pack option:

```text
build --host codex --packs spatial,media
install --host codex --packs spatial,media --target <path> --dry-run
```

Rules:

1. `general` is always included and cannot be passed as an optional pack.
2. Zero packs means a General-only payload.
3. Pack IDs are de-duplicated and validated against the manifest.
4. A payload's generated `profile.json` records `base_profile: general` and the exact ordered `active_packs`.
5. A request to install a different pack set remains namespaced, backed up, dry-runnable, and explicitly confirmed just as the current installer is.

### 7.2 Output collision must be designed before implementation

Today every build writes to `dist/<host>`. That is safe only while a caller builds one profile at a time. Mixed pack builds need a distinct final directory so they cannot silently replace another payload.

Recommended target:

```text
dist/<host>/<profile-key>/

general
spatial
media
growth
spatial+media
spatial+growth
```

`profile-key` is generated from the canonical pack order, never copied from arbitrary user text. The original one-profile command may retain a compatibility output path for one release only, but the build result must always print the exact directory it produced. The source batch must choose and test the migration rather than writing over `dist/<host>` by accident.

### 7.3 Registry-driven copying

The builder must stop unconditional copying of `global/reference/` and stop special-casing `design-audit` as the only specialist resource. It should copy every registry class using the same selected-profile intersection rule. That gives all future packs the same safe pathway and makes payload validation meaningful.

## 8. Router contract

The router is a compact decision policy, not a hidden prompt that attempts to run the whole studio. For each substantial request it returns a small record:

```json
{
  "functional_leads": ["staff_engineering", "assurance_quality"],
  "active_packs": [],
  "workflow": "debug-issue",
  "mode": "diagnose",
  "maximum_mutation_class": "read_only",
  "approval_required_before_effect": false,
  "reason": "The user requested diagnosis only."
}
```

Routing procedure:

1. Read the request, applicable project truth, and explicit restrictions.
2. Classify the requested mode and mutation ceiling first. `diagnose` is always read-only.
3. Activate the smallest functional boundary set that can own the decision.
4. Activate a pack only from an explicit domain signal or a necessary task requirement. Absence of a signal means no pack.
5. Select a workflow only if it gives a useful route, procedure, or hard gate. Direct execution remains valid for a small reversible task.
6. Record required evidence and approval gates. An external, destructive, financial, production, publication, messaging, or purchase effect stops for just-in-time explicit approval.
7. When a user-facing AI feature is in scope, add the conditional AI-native product controls; do not activate a generic “agent” architecture by default.

## 9. Required routing fixtures

The next test-fixture revision should use a `base_profile` and `active_packs` list instead of a single `profile`, plus `functional_leads`. The fixtures test routing expectations; they do not pretend to prove natural-language understanding by a model.

| Scenario | Expected packs | Primary route/mode | Non-negotiable assertion |
| --- | --- | --- | --- |
| Diagnose a failing service, no edits | none | `debug-issue` / `diagnose` | Mutation ceiling is `read_only`. |
| Implement an approved ordinary product feature | none | `build-feature` / `implement` | No specialist pack is selected by default. |
| Plan a multi-tenant SaaS | none | `project-inception` / `propose` | General Product + Architecture can be selected without Spatial/Media/Growth. |
| Audit authentication without edits | none | `security-audit` / `diagnose` | Authorization boundary receives Assurance; no source mutation. |
| Deploy a release | none | `ship-to-production` / `implement` | External/production approval is recorded immediately before the effect. |
| Create a luxury interior portfolio concept | spatial | `spatial-project-inception` / `propose` | Spatial is selected; Media and Growth are absent unless requested. |
| Direct a generated product/showroom film | media, possibly spatial | `video-generation` / `propose` | Provider-specific media resources are selected only for a media request. |
| Write prospecting material or improve a conversion page | growth | `marketing-copy` / `propose` | No Media asset enters discovery. |
| Build an AI-assisted product feature | none; conditional AI-native controls | product/architecture route | No automatic RAG, memory, tool-using agent, or vector database. |
| Spatial website with an AI-generated film | spatial, media | Director-selected route | Exactly those two packs are composed with General. |
| Split bounded independent tasks | none unless task content qualifies | `task-dispatch` / relevant mode | Every worker has a bounded charter; no worker self-authorises external effects. |

## 10. Source-edit sequence after this review

This is the recommended order, deliberately small enough to verify.

1. **Manifest foundation batch:** migrate schema/validator to V2, add the three profile definitions and human-readable profile files, register resources, and retag assets exactly from the master ledger. Do not rewrite skill prose in this batch.
2. **Build composition batch:** implement selected-pack resolution, collision-safe output paths, registry-driven resources, dry-run reporting, and profile-composition smoke tests across all five hosts.
3. **Router batch:** rewrite the lean `GLOBAL_MEMORY.md` router to the contract above; update routing fixtures and mode/approval validation. Keep core policy in `GEMINI.md`, not duplicated into the router.
4. **Core route batch:** update only the highest-leverage general workflows and handoffs selected by the master ledger.
5. **Selective skill and pack batches:** revise assets in small, evidence-backed groups. Use targeted research only for a real dated, provider-specific, legal, API, or disputed claim.

Each batch requires its own diff review, baseline validation, relevant new regression tests, and generated-host smoke tests. A passing OS baseline check remains different from project-native release readiness.

## 11. Design verdict

V4 does **not** need a new swarm of permanent personas, a duplicate “routing catalog,” a YAML dependency, a universal multi-agent architecture, or a blind rewrite of every skill.

It needs one versioned registry capable of expressing five functional owners, three optional packs, honest delivery roles, resource boundaries, and safe composition. That gives Beloved a system that stays general by default, grows into specialist work only when the task calls for it, and remains explainable and auditable across Codex, Gemini, Cursor, Windsurf, and OpenCode.
