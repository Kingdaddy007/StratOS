# V4 Optional Packs Decision Ledger

**Status:** Batch C - decision design only; no source asset, manifest, router, or adapter changed  
**Date:** 2026-08-18  
**Purpose:** remove specialist discovery noise from ordinary product work while preserving and selectively combining the specialist capabilities Beloved already values.

## The decision

Anti-Gravity will have one lean **general** capability base and three optional packs:

```text
general product studio
    +-- spatial       -> high-end spatial/showroom work
    +-- media         -> image/video generation and Seedance work
    +-- growth        -> positioning, copy, conversion, prospecting
```

A pack is a discovery and routing boundary. It is not a separate operating system, a permanent agent, or a physical folder move. The Director activates it only when the request and project evidence justify it.

## Pack-composition rule

Projects may activate more than one pack, but only deliberately.

| Project situation | Active capability |
| --- | --- |
| Standard app, SaaS, API, or internal tool | General only |
| Luxury interior/showroom website | General + Spatial |
| Showroom with an AI-generated room film | General + Spatial + Media |
| Marketing/copy/conversion work for a normal product | General + Growth |
| Client acquisition for a spatial studio | General + Spatial + Growth |

Spatial work does not automatically need Media. Growth work does not automatically need Spatial. No pack is activated merely because an asset happens to be installed.

## A. Spatial pack

| Asset group | Disposition | Why |
| --- | --- | --- |
| `spatial-experience-design`, `storytelling`, `master-design-director` | Keep in Spatial | These are specialised judgement assets for spatial experience, narrative, and high-end creative direction |
| `cinematic-motion`, `cinematic-showroom-strategy`, `motion-library` | Keep in Spatial | They are specialised web-motion/showroom assets; they must not dictate general product UI |
| `brand-strategy` | Keep in Spatial | Its present scope is luxury/interior/spatial positioning; do not misrepresent it as universal B2B brand strategy |
| Spatial coordination: `spatial-project-inception` plus `spatial-experience-design/reference/project-phase-routing.md` | Keep one stateful project route; make focused phases direct specialist work | The Spatial pack preserves entry gates and return conditions without making a focused reference, concept, story, UI, or motion task a mandatory waterfall. |
| `global/reference/*`, `global/design-audit/*` spatial collections | Preserve; give them an explicit Spatial reference index later | They are valuable specialist source material but currently lack a clear manifest-level ownership/index |

## B. Media pack

| Asset group | Disposition | Why |
| --- | --- | --- |
| `prompt-engineering` | Re-profile to Media | It is explicitly for image/video prompting, not product LLM prompt architecture |
| `video-generation` | Keep as a direct Media skill | It plans AI video work, including provider-specific tooling that changes frequently; a routine plan does not create workflow state. |
| `seedance` plus its 23 named subskills (24 Seedance-named skills in total) | Keep as one Media suite | These are deep provider-specialist capabilities. They should load only for a Seedance request, not every ordinary product task |
| Seedance references and provider claims | Preserve; reverify before active use | Model labels, limits, pricing, API availability, safety filters, and platform behaviour are volatile and already belong under source-verification rules |

The Media pack remains provider-neutral at its entry point. Google Flow, Veo, Gemini Omni, Seedance, and any later provider are routed by the active request and verified current capability, not by a permanent preference hard-coded into general policy.

## C. Growth pack

| Asset group | Disposition | Why |
| --- | --- | --- |
| `copywriting`, `copy-editing`, `marketing-psychology`, `page-cro`, `sales-enablement` | Re-profile to Growth | Valuable work, but it should not clutter a backend, debugging, or database task |
| `expert-positioning`, `prospect-research` | Re-profile to Growth; retain spatial compatibility later where justified | They support client strategy and acquisition. Their current specialist context must remain visible rather than silently becoming universal advice |
| `workflow-marketing-copy` | Re-profile to Growth | It is a focused procedure for a marketing objective |
| `competitor-profiling` | Keep under Product & Strategy, optionally activated for Growth | Competitor evidence can inform product decisions as well as marketing; it should not be captured exclusively by Growth |
| `brand-strategy` | Remains Spatial in the first V4 transition | Its existing activation is spatial-specific. A future general brand strategy capability would need its own evidence and scope, not a misleading rename |

## Shared assets that do not belong in a pack

| Asset | Decision |
| --- | --- |
| `reference-intelligence` | General evidence capability shared by Product & Strategy and Design Direction; it may load Spatial references only when the Spatial pack is active |
| `ui-ux` | General Design Direction capability; it conditionally adapts to Spatial work rather than becoming a Spatial-only skill |
| `security`, `testing`, `review-audit`, `browser-test` | General assurance capabilities; specialist packs add risks but do not replace the shared safety/evidence foundation |
| `architecture`, `api-design`, `database`, `devops-infra`, `performance` | General product architecture capabilities; a pack may add specialised considerations but cannot bypass them |

## Later manifest design - not implemented now

The eventual manifest must express the following without duplicating files:

1. `general`, `spatial`, `media`, and `growth` as supported profiles or pack memberships.
2. A profile/pack array per skill and workflow, allowing intentional composition where needed.
3. An asset role: general skill, studio route, department procedure, hard gate, reference, or tool adapter.
4. Pack activation conditions and resource-index ownership.
5. Backward-compatible adapter output for each supported host.

It must not claim a magic fixed number of "core" skills. The general base must be determined by functional ownership and tested routing, not an attractive count.

## Pack acceptance tests before implementation

| Test | Expected result |
| --- | --- |
| General SaaS/API request | Does not surface Seedance, spatial showroom, or sales-outreach procedures unless explicitly requested |
| Spatial portfolio request | Selects Spatial assets without automatically loading Media or Growth |
| Video-generation request | Selects Media assets and current provider verification without forcing Spatial |
| Client-acquisition request | Selects Growth assets; may combine with Spatial only when the client/studio domain requires it |
| Cross-pack request | Activates only the named/justified packs and preserves general safety gates |

## What comes next

The three decision batches are now represented without changing live source:

1. Core, Product & Systems Architecture.
2. Design Direction, Staff Engineering, and Assurance & Quality.
3. Optional packs.

The next phase is to reconcile those ledgers into one master source-change backlog. Only then do we change the manifest and the Studio router together as a small verified batch.
