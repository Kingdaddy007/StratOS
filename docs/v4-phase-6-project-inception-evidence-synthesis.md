# V4 Phase 6 — Project Inception Evidence Synthesis

**Status:** implemented research-to-workflow batch  
**Scope:** `global/workflows/workflow-project-inception.md` only  
**Research input:** Prompt 2—Project Inception and AI-Assisted Delivery Shaping  
**Decision date:** 2026-08-18

## Decision

Upgrade `project-inception` from a useful proportional brief into a **read-only, decision-ready first-direction workflow**. It must classify the starting condition and risk, create only the project truth needed to choose a next move, and hand off to a separate workflow before any implementation or external effect.

It must not become a universal lifecycle, a permanent multi-agent process, or a substitute for delivery, diagnosis, architecture, testing, security, or human approval.

## Comparison of the supplied reports

| Dimension | Manus | Grok | Decision |
| --- | --- | --- | --- |
| Evidence discipline | Separates source-backed findings, transferable implications, and Studio proposals; states research gaps. | Contains useful ideas, but mixes primary sources with newsletters, blogs, vendor material, social posts, and raw link lists. | Use Manus as the primary synthesis. |
| Operating model | Clear Project Decision Packet, three paths, gate/skip logic, starting overlays, and bounded state model. | Strong concise artifacts, path table, and anti-ceremony examples. | Keep Manus's structure; borrow only compatible practical details from Grok. |
| Custom-agent routing | Conditional leads and bounded workers, with the human as goal owner. | Strong supervisor-not-swarm warning and worker contract. | Retain the existing Director/task-dispatch model; clarify the handoff boundary in Project Inception. |
| Risk handling | Contextual AI, authority, data, evaluation, control, and containment principles. | Good concrete illustrations, but several domain claims and sources need specialist treatment. | Keep proportional high-impact framing; do not import medical, regulatory, or model-specific rules. |

## Findings adopted

| Finding | Workflow decision |
| --- | --- |
| A first direction needs only enough durable truth to choose the next safe move. | Define a compact Project Decision Packet rather than a PRD or full plan. |
| Starting conditions differ: narrow change, greenfield idea, existing product, client brief, rescue, and high-impact work. | Add a starting-condition triage table before product framing. |
| Decision effort should scale with consequence, uncertainty, sensitivity, reversibility, and coordination cost. | Use Paths A/B/C: bounded change, normal initiative, high-impact initiative. |
| Gates are decision checkpoints, not mandatory meetings or phases. | Define Frame, Bound, Evidence, Shape, Feasibility, and Assurance with skip conditions. |
| Product, Design, Architecture, Engineering, and Assurance should collaborate only when their evidence changes the next choice. | Retain a loop model with conditional lenses, not a fixed pipeline. |
| Small batches and explicit decisions improve feedback and reduce sunk-cost exposure. | Require a first valuable slice, acceptance signal, stop condition, and selected next workflow for normal work. |
| High-impact AI needs authority, data, human control, evaluation, and containment consideration. | Add high-impact packet fields and an explicit no-build/narrow/approval-gated-pilot outcome. |
| Task workers require bounded scope, minimum context, no unapproved effects, and a return path. | Reference `task-dispatch`; do not duplicate or expand worker authority here. |

## Findings deliberately not encoded as universal rules

- A week-long Lean Inception, full PRD, fixed stack, story points, journey atlas, design system, deployment plan, or named product framework.
- A universal `in-delivery` lifecycle state inside this read-only workflow. Delivery belongs to `build-feature`, diagnosis to `debug-issue`, and verification to their own routes.
- Permanent agents, peer-to-peer swarm handoffs, or parallel workers by default.
- Fixed interview counts, fixed time-boxes, or a mandatory “appetite” measured in hours/days. The workflow uses a contextual decision budget instead.
- Medical-device, hiring, clinical, financial, or other domain-specific risk classification outside the relevant domain authority.
- Persisting transcripts, secrets, raw personal data, or speculative stacks as project truth.

## Source grounding

The sources below were independently checked on 2026-08-18 and used only for their stated, limited principles:

- [DORA—Working in small batches](https://dora.dev/capabilities/working-in-small-batches/) supports small, independently testable work as a way to shorten feedback cycles and counter AI-assisted delivery instability. It does not require all initiatives to be released immediately or use a fixed implementation cadence.
- [Agile Manifesto principles](https://agilemanifesto.org/principles.html) support early valuable delivery, responsiveness to change, simplicity, and technical excellence; they do not prescribe this Studio's workflow states.
- [NIST Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design) supports understanding users, tasks, and environments and iterative evaluation. The page itself notes it is no longer updated, so this workflow uses the stable ISO-derived principle rather than treating the page as current policy.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) treats AI risk management as voluntary and contextual across design, development, use, and evaluation. AI RMF 1.0 is currently under revision, so the workflow keeps only a small risk-sizing frame rather than a frozen checklist.
- [Nygard's ADR guidance](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) supports short records for architecturally significant decisions and preserving rationale/consequences. It is not used to require an ADR for ordinary work.

## Concrete implementation

- Updated `workflow-project-inception.md` from version 2 to version 3.
- Added starting-condition triage, proportional paths, project-packet fields, decision gates, loop-based collaboration, and explicit read-only state semantics.
- Preserved the current approval ceiling and task-scoped state contract.
- Added route regression checks for the v3 contract.
- Did not change the global router, task dispatch, custom agent registry, or any delivery workflow in this batch.

## Remaining research boundaries

Prompt 3 still governs a future Debugging revision. Prompt 4 still governs future Testing/Verification revisions. This batch does not treat either topic as settled by Project Inception research.
