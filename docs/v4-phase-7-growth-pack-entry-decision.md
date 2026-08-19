# V4 Phase 7 — Growth pack entry decision

**Status:** selected; entry-state record. Subsequent evidence gates are recorded separately.  
**Date:** 2026-08-19  
**Scope:** Choose the first optional pack without rewriting its skills blindly.

## Decision

**Growth is the first Phase 7 pack.** It is the smallest contained specialist pack: seven capabilities and one workflow. Its work is valuable for Beloved’s positioning, prospecting, copy, conversion, and sales-material requests, while it remains irrelevant to ordinary engineering work.

This is a sequencing decision, not a claim that Growth is more important than Spatial or Media. Counts and workflow names below describe the entry-state snapshot; later records may change the active registry.

## Evidence

| Pack | Canonical skills | Canonical workflows | Immediate complication | Decision |
| --- | ---: | ---: | --- | --- |
| Growth | 7 | 1 | Older instruction bodies and one stale workflow profile/state contract. | Start here. It is small, non-provider-specific, and its routing boundary already exists. |
| Spatial | 9 | 8 | Large, valuable reference collections and specialist creative content that must be preserved carefully. | Audit after Growth; do not compress or rewrite protected depth blindly. |
| Media | 26 | 1 | Provider/model claims, limits, safety behaviour, and availability are volatile. | Audit after Growth; source verification must precede activation changes. |

At entry, the manifest registered seven Growth skills and `marketing-copy` under the optional `growth` profile. `global/profiles/growth/profile.json` correctly excluded ordinary engineering and unapproved external outreach.

## Safe source alignment and immediate safety correction completed

`workflow-marketing-copy.md` was internally inconsistent: the canonical manifest classified it as `growth`, while its own frontmatter declared `general` and pointed all runs to one shared `marketing-copy.json` state file. Its legacy body also forced all Growth skills and required context creation before copy work began.

At this entry-state step, the workflow was rewritten to version 3 with:

- `profiles: [growth]`; and
- task-scoped `.agents/workflows/<task-id>.json` resume state; and
- a short coordinator that selects one owning capability, keeps existing context optional, and separates drafts/research from external effects.

The local audit also found score-driven instructions in `prospect-research` that implied sending outreach. They now produce proposals or drafts for human review; its dossier template and local-only helper are preserved. The deeper Growth methods then remained behind the research gate below. Later accepted evidence demoted `marketing-copy` to the profile-scoped direct-selection procedure and introduced separate material-decision routes; see `v4-phase-7-offer-architecture-evidence-synthesis.md`.

## Asset groups and research gates

| Group | Assets | Research gate before substantive rewrite |
| --- | --- | --- |
| Positioning, messaging, and conversion | `copywriting`, `copy-editing`, `marketing-psychology`, `page-cro`, `expert-positioning` | Research how to improve decision quality, evidence use, ethical persuasion, experiment interpretation, and client-positioning judgement without forcing generic frameworks or manipulative tactics. |
| Prospecting and sales materials | `prospect-research`, `sales-enablement` | Research evidence-led account selection, truthful dossier construction, outreach/sales-material boundaries, buyer enablement, privacy/consent caveats, and external-effect approval controls. |
| Workflow coordination | `marketing-copy` | Rebuild only after the two groups establish which capability should own framing, drafting, editing, conversion diagnosis, collateral, and prospect evidence. The workflow must coordinate; it must not always load every skill or demand nonexistent project contexts. |

`prospect-research` already contains its dossier template and helper script; retain those assets and evaluate their routing, evidence, and safety fit rather than duplicating them.

## Non-negotiable boundaries

- Growth is opt-in. It never becomes a dependency of General engineering, debugging, security, or database work.
- A Growth request is not permission to send outreach, publish copy, contact prospects, purchase ads, or make a public claim. External effects retain their just-in-time approval gate.
- Preserve valuable specialist material. Move content into conditional references only when it changes a loading decision, not merely to reduce word count.
- Do not turn research findings, named copy frameworks, behavioural-science concepts, or a sales methodology into mandatory rituals.

## Exit criteria for the Growth pack

1. Two focused research reports are compared and their durable findings separated from volatile or unsupported claims.
2. Every Growth capability has a clear activation and exclusion boundary, portable metadata, and conditional reference routing.
3. `marketing-copy` becomes a short coordinator with correct mode, state, approval, and handoff semantics.
4. General payloads exclude all Growth assets; Growth payloads include only Growth plus the General base.
5. Routing fixtures cover copy drafting, copy editing, conversion diagnosis, sales collateral, prospect research, and an external-outreach approval stop.

The detailed evidence, preserved strengths, and remaining research-dependent work are in the [Growth baseline audit](v4-phase-7-growth-baseline-audit.md). The small official-source anchor set is in the [primary-source baseline](v4-phase-7-growth-primary-source-baseline.md). The two external research briefs are in [v4-phase-7-growth-research-briefs.md](v4-phase-7-growth-research-briefs.md), and their comparison will use the [research assessment template](v4-phase-7-growth-research-assessment-template.md).
