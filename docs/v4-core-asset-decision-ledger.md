# V4 Core Asset Decision Ledger

**Status:** Batch A - decision design only; no source asset changed  
**Date:** 2026-08-18  
**Scope:** Studio core, Product & Strategy, and Systems Architecture.  
**Out of scope:** rewrites, installation, generated adapters, the Design/Engineering/Assurance batches, and all optional packs.

## Why this is the next step

Research told us what the studio must be capable of. The asset map showed that much of that capability already exists. This ledger decides the future role of the core assets before anyone edits them.

It prevents two bad outcomes:

- deleting valuable six-month-old work because it is not written in V4 language; and
- adding fashionable AI rules to every task when most products do not need them.

## Decision vocabulary

| Decision | Meaning | It does not mean |
| --- | --- | --- |
| **Keep and re-home** | Preserve the source, but give it a clearer V4 owner and route | Rewrite it now |
| **Strengthen** | Preserve the core, then make one targeted improvement in a later source-edit batch | Add more length by default |
| **Consolidate** | Move repeated operating instructions into the smallest correct shared layer | Delete the underlying knowledge |
| **Re-profile** | Keep a capability but remove it from universal discovery when it is specialist | Discard the asset |
| **Defer** | Preserve unchanged until a real project or later batch supplies a concrete reason to decide | Forget about it |

## A. Studio core

| Asset | V4 home | Decision | Reason | Future source-edit objective | Prerequisite |
| --- | --- | --- | --- | --- | --- |
| `global/GEMINI.md` | Studio Director safety kernel | **Strengthen and compress** | Its authority, trust, approval, and reasoning protections are valuable; 285 always-loaded lines are too broad for the V4 lean kernel | Keep non-negotiable safety and authority rules; move role/process detail into functional contracts and routes | Director route and contract wording agreed |
| `global/GLOBAL_MEMORY.md` | Studio Director routing map | **Consolidate and rewrite later** | It is a v3 router with too much policy, mode, context, and state detail mixed together | Turn it into a compact task router that activates the Director and the appropriate functional boundary | Director intake/routing design |
| `global/manifest.yaml` | Canonical registry | **Keep and strengthen** | It already correctly registers canonical assets and host compatibility | Add V4 functional ownership, route level, optional-pack membership, and AI-native conditionality only after these decisions are stable | Pack/profile model agreed |
| `global/baselines/authority-and-trust.md` | Shared safety baseline | **Keep and align** | It already correctly defines authority order, untrusted content, mutation classes, and external approval | Align terminology with the Studio Director and the worker charter without weakening any safety control | Director/worker authority vocabulary agreed |
| `global/baselines/context-integrity.md` | Shared context baseline | **Keep** | Stable rule: templates are not active project truth | Verify it remains short and is linked from the future project-context creation route | Context-template batch |
| `global/baselines/engineering.md` | Shared engineering baseline | **Strengthen later** | It is intentionally concise but must point to evidence/verification expectations without duplicating every skill | Add only durable cross-cutting engineering invariants after the Assurance batch | Assurance and engineering handoff |
| `global/baselines/source-verification.md` | Volatile-claim baseline | **Keep and extend selectively** | It already holds the correct primary-source and freshness rule | Add records only for time-sensitive claims actually used by an active optional pack or AI-product reference | A claim is selected for adoption |
| `global/context_templates/*` | Project scaffolding | **Keep; defer lean-template audit** | They are scaffolds, not runtime truth, but several are too large to be copied blindly | Split stable policy from blank project fields; do not make a template a mandatory reading burden | Functional batch that owns the template |
| `global/adapters/*` and `dist/*` | Host translation and generated output | **Keep untouched** | No canonical behavioural decision has changed yet | Regenerate only after canonical source changes and manifest validation pass | Source-edit batches complete |

### Core acceptance test before editing

The future core rewrite succeeds only if a new task can answer these questions quickly:

1. Who has authority to decide and to act?
2. Which functional boundary owns the next decision?
3. What is untrusted data?
4. Is the requested operation read-only, local, environmental, destructive, or external?
5. What evidence and approval are required before an irreversible or external effect?

If a proposed rewrite cannot improve those answers while reducing loading burden, it should not be made.

## B. Product & Strategy

| Asset | V4 owner | Decision | Reason | Future source-edit objective |
| --- | --- | --- | --- | --- |
| `skills/product-thinking` | Product & Strategy | **Keep and re-home** | It already frames whether, why, and how much to build | Tie its output directly to a concise product/risk brief handed to Systems Architecture and Design |
| `skills/research-analysis` | Product & Strategy | **Keep and strengthen** | It gives a useful comparison method | Add a clear source-evidence distinction and a rule that research informs judgement rather than replacing it |
| `skills/competitor-profiling` | Product & Strategy, optional when market evidence is needed | **Keep; scope-check later** | It can provide decision evidence but not every product needs it | Verify its current activation is honest and does not claim unobserved facts |
| `skills/reference-intelligence` | Product & Strategy and Design Direction | **Keep; move to general evidence capability** | Reference analysis can serve product and UX decisions, not only spatial work | Remove spatial-only routing while preserving specialist visual references behind the spatial pack |
| `workflow-project-inception` | Studio Route, led by Product & Strategy | **Strengthen and reduce** | It contains valuable discovery/inception material but is too large and too sequential for the V4 model | Recast as risk-sized route: discover, choose only needed boundaries, establish a North Star, then hand off; no forced waterfall |
| `workflow-reference-intelligence` | Department procedure shared by Product & Strategy / Design | **Keep and re-home** | It has useful provenance and translation gates | Make it selectable evidence work, not a default route for every project |
| `global/context_templates/business-priorities.md` and product-related templates | Project truth scaffold | **Keep; audit with Product batch** | Product context must remain a project-owned record, not global assumptions | Reduce blanks and ensure a short current-brief output exists |

### Product & Strategy acceptance test before editing

For a new idea, a solo builder should be able to produce a short, honest handoff:

```text
User/problem | desired outcome | scope boundary | evidence/assumptions | risk | success signal | open decisions
```

The route should activate research, competitive evidence, design, or architecture only when they change a real decision.

## C. Systems Architecture

| Asset | V4 owner | Decision | Reason | Future source-edit objective |
| --- | --- | --- | --- | --- |
| `skills/architecture` | Systems Architecture | **Keep and strengthen** | It already covers purpose, quality attributes, boundaries, data flow, failure, reversibility, observability, and complexity | Make its output explicitly risk-sized: quality scenarios and a decision record for material/Type 1 decisions; simple outline for reversible work |
| `skills/api-design` | Systems Architecture | **Keep** | Strong contract, consumer, boundary, security, evolvability, and operational priorities | Verify resource links and make consumer/error/failure contracts the central output rather than a generic protocol recommendation |
| `skills/database` | Systems Architecture | **Keep** | Strong ownership, migration, access, integrity, and recovery material | Preserve expand-and-contract safety; ensure database advice remains conditional on actual persistence needs |
| `skills/devops-infra` | Systems Architecture, with Assurance involvement | **Keep and re-home** | Operations, deployment, observability, secret handling, and blast radius are architectural concerns with assurance evidence | Clarify shared handoff to Assurance rather than making infrastructure a separate permanent organisation |
| `skills/performance` | Systems Architecture, with Assurance involvement | **Keep** | It correctly requires measurement before optimisation | Keep it project-triggered; connect performance targets to explicit quality attributes when architecture work is material |
| `workflow-plan-architecture` | Studio Route, led by Systems Architecture | **Strengthen and reduce** | It has sound options, trade-offs, ADR, and implementation-path steps but is long | Rebuild as a decision-sized route with clear handoffs and conditions for loading deep references |
| `workflow-design-api` | Systems Architecture department procedure | **Keep and re-home** | It has a strong authority mode and contract-first approach | Remove unrelated boilerplate and ensure a route starts only where an API boundary is real |
| `workflow-database-migration` | Hard Gate, led by Systems Architecture | **Keep** | It is already compact, production-aware, and approval-gated | Keep its explicit target, rehearsal, compatibility, recovery, and evidence requirements |
| `workflow-dependency-upgrade` | Department procedure, led by Systems Architecture / Staff Engineer | **Keep** | Dependencies can affect compatibility, security, and rollback | Retain the proportional migration/rollback path and improve only broken links/routes |
| `workflow-incident-response` | Hard Gate, operationally led by Systems Architecture with Assurance | **Keep** | It correctly separates observation, proposal, approved mitigation, recovery, and learning | Preserve external approval and smallest-reversible-mitigation rules; make V4 lead handoffs explicit |
| `workflow-ship-to-production` | Hard Gate, integrated by Studio Director | **Keep and reduce** | Release safety is necessary but current source is overlong | Preserve risk classification, rollback, monitoring, and approval; remove duplicate skill prose |
| `workflow-optimize-performance` | Department procedure, led by Systems Architecture | **Keep** | It is explicitly evidence/measurement first | Ensure it is only selected by a performance signal or capacity decision |
| Architecture/API/database/infra context templates | Project truth scaffolds | **Keep; lean-template audit later** | They contain valuable questions but are too long for unconditional loading | Separate fill-in project facts from on-demand reference material; never treat scaffold text as a project fact |

### Systems Architecture acceptance test before editing

For any material product decision, the architect should leave a handoff that makes the following visible:

```text
Boundaries and ownership | top quality trade-offs | data/contract path | failure and recovery | security boundary | reversibility | evidence needed
```

For small reversible tasks, this can be a few lines. For a high-impact decision, it becomes an ADR or project record. The form changes; the underlying thinking does not.

## D. AI-native conditional extension

No current core asset is being marked "replace with an AI agent." The future extension is intentionally small:

| Need | First asset type to consider | Do not build unless |
| --- | --- | --- |
| Decide whether AI belongs in a product | Short decision reference under Product & Strategy | A product has a real AI-facing user job |
| Choose feature/workflow/tool-using-agent/autonomous mode | Architecture reference plus an approval condition | The product needs more than generation inside a normal deterministic flow |
| Version a model/prompt/retrieval/tool behaviour change | Reference plus evaluation/change gate | The change can silently alter product quality, safety, cost, or data exposure |
| Evaluate an AI feature | Project evaluation harness pattern | The product makes an AI quality or safety claim worth regression-testing |

This is deliberately not a new swarm, a global "AI engineer" persona, or an agent framework.

## What happens after Batch A

1. **Batch B:** Design Direction, Staff Engineering, and Assurance & Quality assets receive the same decision ledger.
2. **Batch C:** classify the Spatial, Media/Video, and Growth packs so optional capability no longer pollutes general discovery.
3. **Integration decision:** update the V4 operating model, functional contracts, and manifest design only where the three ledgers agree.
4. **Selective source edit:** revise the first small, high-leverage source set. The likely order is core routing, project inception, architecture route, then the affected references—not all skills at once.

No source asset should be rewritten merely because it is old. A change must identify the served capability, actual gap, affected route, evidence, and verification path first.
