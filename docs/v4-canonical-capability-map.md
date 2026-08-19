# Anti-Gravity OS v4 — Canonical Capability Map

**Status:** Canonical capability model, reconciled 2026-08-19. This is
deliberately independent of raw file count; the live registry remains the
machine-readable authority.

## 0. Live registry checkpoint

At this checkpoint, `global/manifest.yaml` records **48 skills, 17 workflows,
6 agents, and 4 profiles**. The [research synthesis decision ledger](v4-research-synthesis-decision-ledger.md)
records why these are a working inventory rather than a reason to invent a
larger library. Historical counts are provenance only. Trading is not an
active V4 capability.

## 1. The job of the OS

Anti-Gravity turns Beloved's intent into a credible product, service, website, or improvement by making the right decisions visible, building only what is authorised, and proving the result to the extent the available evidence allows.

It is not a library of commands. It is a small studio:

```text
Beloved's intent
       |
Studio Director: clarify, choose the smallest useful route, coordinate
       |
Product <-> Design <-> Systems <-> Delivery <-> Assurance
       |
evidence, decisions, implementation, verification, honest handoff
```

The arrows are deliberately two-way. A builder may discover that a design state is missing; a design decision may expose an API or performance constraint; Assurance may return work to any owner. This is collaboration, not a relay race.

## 2. The six fixed roles

The role model is already approved in `V4_OPERATING_MODEL_SPECIFICATION.md`. This map does not introduce new “departments.”

| Role | Accountable for | Does not own |
| --- | --- | --- |
| Studio Director | Task framing, routing, authority ceiling, coordination, integrated outcome | Overriding Beloved's decisions or approving external effects |
| Product & Strategy Lead | Value, users, scope, evidence, priorities, commercial meaning | Technical topology, visual production, deployment |
| Systems Architect | Boundaries, data/contracts, reliability, reversibility, technical trade-offs | Product scope, routine implementation, release approval |
| Design Director | Usability, interface meaning, visual direction, accessibility, specialist design packs | Backend ownership, unsupported technical claims, release approval |
| Staff Engineer | Bounded implementation, debugging, integration, maintainable delivery | Unapproved scope/contract changes, environment/external actions |
| Assurance & Quality Lead | Independent evidence, security and reliability challenge, residual-risk report | Implementing the feature it audits or approving release |

## 3. Capability families

These are jobs the studio must be able to perform. A family can later become one skill, a small package, a director procedure, a reference, or a host adapter. It does **not** automatically become a standalone slash command.

### A. Product and decision evidence

| Capability | Owner | Needed when | Minimum useful result |
| --- | --- | --- |
| Problem framing and smallest credible slice | Product | A request, product, client brief, or priority is unclear | Actor, problem, value, non-goals, first decision |
| Decision research and option comparison | Product | Options, cost, adoption, or reversibility matter | Evidence, alternatives, trade-offs, recommendation, invalidating condition |
| Market and competitor evidence | Product, with Growth when commercial | External market claims could change positioning or scope | Dated source card; fact/inference split; comparable implications |
| Commercial position and offer boundaries | Product/Growth | A service, product, price hypothesis, claim, or proposal is material | Credible posture, proof burden, scope, exclusions, human decision needed |

### B. Design and evidence translation

| Capability | Owner | Needed when | Minimum useful result |
| --- | --- | --- |
| Interface and experience design | Design | Flow, hierarchy, states, accessibility, or interaction changes an outcome | Flow/state decision, constraints, representative design evidence |
| Reference intelligence | Design | A screenshot, recording, URL, precedent, or visual corpus could inform a decision | Source register; observations separate from inference; Keep/Adapt/Reject/Defer decision |
| Semantic visual system | Design | Type, colour, spacing, visual hierarchy, or component semantics need coherence | Tokens/roles and accessible state use—not a generic palette recipe |
| Motion and visual enhancement | Design | Motion, scroll, Canvas/WebGL, or media may carry a real communication job | Stillness comparison, job, fallback, accessibility/performance/source limits |
| Spatial experience direction *(optional)* | Design | Interior, showroom, gallery, furniture, architecture-adjacent, or cinematic spatial work qualifies | Evidence-informed experience brief, concept choices, proof and production constraints |
| Directed generated media *(optional)* | Design | A project needs AI-generated still/video direction or provider-aware evaluation | Creative brief, reference/rights boundary, provider check, review criteria |

### C. Systems and technical decisions

| Capability | Owner | Needed when | Minimum useful result |
| --- | --- | --- |
| Architecture and quality trade-offs | Systems | A durable boundary, ownership, topology, integration, or reversal path changes | Options, quality attributes, decision, consequences, re-evaluation trigger |
| Interface/data contract design | Systems | API, data model, migration, or integration contract is material | Consumer/owner, invariants, compatibility, failure shape, testable contract |
| Operational and performance reasoning | Systems | A measured bottleneck, deployment/recovery shape, or operational constraint matters | Baseline, hypothesis, smallest intervention, evidence, operational trade-off |

### D. Delivery and repair

| Capability | Owner | Needed when | Minimum useful result |
| --- | --- | --- |
| Repository-aware implementation | Staff Engineer | A scoped change is approved | Smallest coherent patch, failure handling, conventions, tests/handoff |
| Evidence-led debugging | Staff Engineer | A defect, regression, crash, flaky check, or unexpected behaviour exists | Symptom/evidence, hypotheses, discriminating check, bounded repair or proposal |
| Behaviour-preserving structural improvement | Staff Engineer | Design debt or change friction matters without a new observable behaviour | Characterisation evidence, contained refactor, unchanged contract proof |

### E. Assurance

| Capability | Owner | Needed when | Minimum useful result |
| --- | --- | --- |
| Risk-sized verification | Assurance | A change or claim needs credible evidence | Claim/risk/boundary map, chosen checks/oracles, actual result, residual uncertainty |
| Independent review | Assurance | A non-trivial change, decision, or disagreement needs challenge | Findings with severity, confidence, evidence, owner, and next action |
| Security and trust-boundary review | Assurance | Sensitive data, access control, payment, external API, or material harm is involved | Boundary/asset/abuse path review; no false guarantee of security |

### F. Studio operating safeguards

| Capability | Owner | Needed when | Minimum useful result |
| --- | --- | --- |
| Deliberate deep decision mode | Studio Director | A decision is Type 1, consequential, novel, or cross-boundary | Assumptions, competing frames, trade-offs, pre-mortem where needed, verification plan |
| Safe handoff and resume | Studio Director | Work is genuinely long, resumable, or context quality is degrading | Minimal state, owner, next safe action, no unapproved memory write |
| After-action learning | Studio Director | A substantial result reveals a reusable lesson | Audit, no-change option, proposed destination, evidence/regression need |
| Bounded worker delegation | Director or owning lead | Independent work materially improves speed or confidence | Charter, exact scope, effect ceiling, return evidence, stop conditions |

## 4. What a future skill must prove

A skill earns an active package only when it provides at least one of these things:

1. A local decision method that changes a difficult judgement.
2. A selective library that a model cannot reliably recreate from general knowledge.
3. A verified safety/tool boundary that prevents a common harmful action.
4. A repeatable evidence/verification method that prevents false confidence.
5. A specialised method with a clear owner, trigger, exclusions, input, output, and freshness path.

Otherwise it becomes one of the following:

| Correct destination | Examples |
| --- | --- |
| Director or lead contract | delegation rules, deep reasoning, normal implementation discipline |
| Reference/procedure inside an owning package | scroll choreography, API migration pattern, merge recovery |
| Host/tool adapter | browser control, static analyser, Canvas import surface |
| Project context | client facts, chosen stack, actual design tokens, active constraints |
| Archive/provenance | obsolete tools, unvalidated creative libraries, historical provider syntax |

## 5. Workflows are coordination routes, not checklists

A workflow survives only when it needs state, handoff, evidence, rollback, or an approval boundary. Future routing has three levels:

| Level | Examples | User experience |
| --- | --- | --- |
| Direct lead operation | Compare a component state, write a small patch, inspect a page | Beloved asks normally; the Director/lead chooses the method silently. |
| Coordination route | Project inception, spatial inception, debugging, material design, commercial decision record | Use when more than one owner, a decision record, or a visible handoff is useful. |
| High-risk route | Migration, incident, release, live external learning | Stops at a named human approval gate before destructive, production, costly, or public effects. |

The future workflow menu is therefore expected to be smaller than the current 17. The audit has already shown that dispatch, test planning, and final verification are usually lead procedures; they should not be separate rituals for Beloved.

## 6. The evidence and multimodal route

Reference Intelligence is an evidence capability, not a command Beloved must remember. The Design Director should choose it whenever visual evidence would materially improve a design decision.

```text
URL, screenshot, browser recording, or user-provided video
        |
Antigravity Browser artifact when available / supplied file
        |
Reference Intelligence: source, observation, inference, unknown, confidence
        |
Optional Gemini multimodal analysis when direct inspection is insufficient
        |
Design Director: Keep / Adapt / Reject / Defer
```

Rules:

- A browser recording is direct evidence; a third-party/Gemini report is mediated evidence and must be labelled as such.
- Do not claim a video was watched when only a transcript or report was available.
- Do not upload private media, invoke paid/API processing, or generate media without just-in-time approval.
- A plugin report never selects the design by itself. It informs a human-guided creative decision.
- One controlled, non-private Antigravity host probe must succeed before this becomes plugin-specific active routing.

## 7. Optional packs

The general studio remains the default. A pack is activated only by the request or project truth.

| Pack | Enables | Does not do |
| --- | --- | --- |
| Spatial | spatial brand, concept, story, motion, showroom direction | Apply cinematic ceremony to normal product/UI work |
| Media | directed image/video work and provider-aware evaluation | Load 23 provider micro-skills or perform external generation automatically |
| Growth | positioning, offers, writing, prospect evidence, client collateral | Use manipulation, invent proof/ROI, contact leads, or make price commitments |

There is intentionally no Trading pack in V4.

## 8. Migration sequence from the current inventory

1. **Finish Stage A:** reconcile manifest versus historical documents and classify every source. This is now substantially complete in `docs/v4-stage-a-asset-reconciliation.md`.
2. **Resolve research gates:** the colour-system study completed on 2026-08-19. Do not run broad research just to make the folder count look complete.
3. **Create pack blueprints:** translate each capability family into the smallest skill/reference/agent/tool/procedure shape.
4. **Migrate one pack at a time:** preserve source, write the successor, update manifest/routes, test ordinary and specialist prompts, then retire only the proven duplicate.
5. **Write final host instructions:** generate the concise main `GEMINI.md`/Antigravity payload from the finished map and agents. Do not make it a second competing source of truth.
6. **Run real pilots:** a normal product task, a spatial website task, a defect, and a high-risk stop-at-approval case.
7. **Install and publish only after approval:** host-global installation and GitHub publication are separate external actions.

## 9. Current research request

No open research study is required before the next substantive content rewrite.
The semantic-colour study has been implemented as a conditional UI/UX method;
see `docs/v4-colour-method-decision.md`. The next research studies will be
triggered by an actual gap revealed during a pack blueprint or a real pilot.
They will not be used to create random new skills.

## 10. Completion criteria for this stage

This stage is complete when:

- every active asset has a named destination and preservation rule;
- no “recipe” or “tool adapter” is presented as a general expert brain;
- each director knows the capability families it can select;
- General work remains general; Spatial, Media, and Growth activate only when justified;
- Reference Intelligence has one safe host probe and a verified retrieval route;
- each migrated pack passes natural-language routing, safety, and evidence tests; and
- final main-agent/host files are generated from the canonical map rather than hand-maintained in parallel.
