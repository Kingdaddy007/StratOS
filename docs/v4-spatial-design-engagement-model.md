# V4 Spatial Design Engagement Model

**Status:** proposed interaction model derived from Beloved's direction; no
agent or workflow implementation is changed by this document.  
**Date:** 2026-08-19

## The Correction

The old experience was effectively:

```text
Start Spatial Project Inception
  -> follow Brand Strategy
  -> follow Storytelling
  -> follow Design
  -> follow Motion
```

That is not the intended V4 experience. It makes an AI follow the names of
assets rather than exercise design judgement with Beloved.

V4 should instead operate as a **Director-led design engagement**. A workflow
is invisible coordination support for a complex project, not a public ritual
that dictates every conversation or every creative decision.

## What Beloved Should Be Able To Say

> “I want to create a website for this interior designer. Here is their website,
> project work, current assets, and the feeling I am trying to create.”

The Studio Director should recognise a qualifying Spatial task, activate the
Design Director with the Spatial pack, and begin an intelligent conversation.
Beloved does not need to name every skill, reference, or project phase.

## The Actual Design Conversation

```text
Beloved's goal and client material
  -> Studio Director sizes the task and selects Design Director
  -> Design Director establishes what is known, missing, and worth deciding now
  -> selective reference/design exploration
  -> Beloved chooses or reshapes a direction
  -> design system + one risk-reducing prototype
  -> scoped implementation and proportionate verification
```

### 1. Orient, do not interrogate

The Director first identifies the client, audience, desired change in
perception, available proof/assets, scope, budget/time constraint, and
Beloved's own creative intention. It asks only the questions that change the
next decision.

It does **not** demand a full dossier when the client already has enough clear
material, and it does not prescribe a visual treatment before understanding
what the site must communicate.

### 2. Choose the smallest useful design move

The Director may do any of the following, depending on uncertainty:

| Situation | Best next move |
| --- | --- |
| Clear client, approved direction, small change | Work directly; no full workflow or worker. |
| Clear client, but no convincing visual direction yet | Develop a few whole-page territories and rough tests with Beloved. |
| The brand, offer, or proof is unclear | Ask Product & Strategy for a bounded positioning/proof clarification. |
| A reference question could change the direction | Use `reference-intelligence` and selected local/external references. |
| A technical visual idea may be expensive or fragile | Ask Staff Engineering for a narrow feasibility check before committing the concept. |
| A material accessibility, responsive, or performance risk matters | Ask Assurance for an independent challenge of that risk. |

These moves can loop. They are not a waterfall.

### 3. Use references as material for judgement

The local Design-Audit library and Motion Library are available to the Director,
but they are not a cage.

- The Director checks them when a named question would benefit from precedent:
  “How could one material hold continuity through the site?” or “What would an
  editorial project archive look like here?”
- It may decide the libraries do not answer the question, ask Beloved for a
  recording or new reference, or propose a bounded external research step.
- A supplied screen recording is analysed directly when the active model can
  inspect it. A transcript made by another AI is a useful mediated aid, not
  direct visual fact.
- Every borrowed principle is translated to the client and may be rejected.
  The Director never copies a site's identity, layout, timing, or code.

### 4. Let Beloved own taste decisions

The Director proposes directions with their consequences: what the visitor will
understand/feel, the proof required, asset burden, motion cost, and what could
go wrong. Beloved can select, reject, combine, or introduce a new idea at any
point.

The system should make it easier for Beloved to think creatively, not turn
Beloved into someone who merely approves a preselected AI style.

### 5. Build only after the direction is real enough

Before broad production, the Design Director and Beloved agree on the
controlling argument, page/story logic, evidence/proof, design rules, asset
plan, and only the motion that has earned its place. A representative vertical
slice tests the riskiest idea before the whole website is built.

## Delegation: Helpful, Not The Main Event

The Design Director works directly for the majority of visual judgement. A
temporary worker is justified only for a separable result with a named payoff:

| Useful worker | Concrete bounded output |
| --- | --- |
| Reference scout | Compare a small, named corpus against a specific design question. |
| Evidence extractor | Turn approved public client material into a labelled evidence inventory. |
| Feasibility scout | Assess one proposed interaction, asset pipeline, or responsive fallback. |
| Implementation verifier | Check the finished vertical slice against named responsive/accessibility/performance criteria. |

Workers do not decide the concept, choose taste on Beloved's behalf, create a
permanent swarm, talk directly to Beloved, or spawn workers of their own. The
Design Director audits their evidence and integrates it into the conversation.

## What The Existing Assets Become

| Asset type | V4 role |
| --- | --- |
| Custom agent | A selectable professional owner: Studio Director, Design Director, Engineer, etc. |
| Skill | A capability the responsible agent chooses when it materially improves a decision or delivery. |
| Reference library | A selectively retrieved source of patterns, evidence, examples, or methods. |
| Workflow | Internal coordination and resume support only when linked decisions, approval gates, or multi-step delivery genuinely need it. |
| Temporary worker | A disposable, chartered evidence or execution lane. |

## Required Follow-Up Implementation

The current `spatial-project-inception` source still reads as a ten-phase
public workflow. It must be refactored in the later agent/routing implementation
batch so that:

1. it is not the normal way Beloved starts every Spatial project;
2. its ten phases remain available as conditional decision lenses and resume
   support for substantial work;
3. the Studio Director chooses the Design Director and relevant capabilities;
4. the Design Director's host contract explicitly binds the Spatial pack,
   reference-intelligence, storytelling, spatial experience, motion, and
   optional Media routes according to activation—not as an always-loaded list;
5. a real website drill proves that the conversation stays creative and useful
   rather than behaving like a form or a command checklist.

## Canvas UI Status

`Canvas UI` is registered as a **conditional Spatial decision capability**. It
is available for the Studio and Design Directors to surface when the visual job
qualifies; it is not an automatic effect, bundled third-party source package, or
permission to run an external installer. A host-local candidate source has been
audited against the verifiable upstream project.

The resulting decision is recorded in
[`v4-canvas-ui-candidate-audit.md`](v4-canvas-ui-candidate-audit.md): it is a
promising optional Spatial implementation capability, not a general default or
an automatic component installer. Each live import still requires a source
refresh, an isolated vertical-slice proof, and approval before any external CLI,
registry, dependency, or source mutation.
