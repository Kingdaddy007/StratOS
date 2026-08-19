---
id: project-inception
version: 3
status: active
intent: Turn a new, uncertain, or consequential initiative into the smallest inspectable basis for the next reversible decision, without imposing a universal project process.
use_when: [a user is starting a product, service, app, client website, internal tool, AI-enabled capability, rescue initiative, or needs an aligned first direction before material implementation]
do_not_use_when: [the request is a clear low-consequence local change, a narrow bug diagnosis with an established problem, a provider-specific media task, or a specialist spatial/growth task with a more precise route]
inputs: [goal, starting condition, target user or operating context, available evidence, constraints, desired outcome, risk, reversibility, authority and data boundaries, deadline or decision budget, existing project truth]
required_resources: [applicable AGENTS.md files, product-thinking, relevant project contexts, architecture/design/assurance capabilities only when a named uncertainty requires them]
mutation_class: read_only
approval_gates: [obtain explicit approval before writing project contexts, making a material architecture or stack commitment, beginning implementation, accessing non-provided sensitive data, or initiating any external action]
states: [received, triaged, bounded, framed, evidence, shaped, feasibility, assurance-framed, ready-to-build, stopped]
outputs: [project decision packet, path classification, first valuable slice, non-goals, assumptions and unknowns, acceptance signal, authority boundaries, selected next route, optional decision record]
verification: [test whether the packet changes a real next decision, distinguish evidence from inference, keep the path proportionate, confirm the first slice is bounded and inspectable, preserve authority and approval boundaries]
failure_paths: [stop or reframe on no accountable goal owner, conflicting outcome, untestable or unacceptable high-impact risk, missing data/authority basis, infeasible first slice, or an attempt to convert a proposal into implementation without approval]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract
next_workflows: [plan-architecture, design-ui, build-feature, debug-issue, test-strategy, security-audit, verify-project, none]
profiles: [general]
---

# Project Inception

## PURPOSE AND BOUNDARY

Project Inception is a **decision-ready first-direction workflow**, not a waterfall and not a project-management ceremony. Its outcome is enough shared truth to choose the next safe move: proceed directly, run a bounded spike or test, involve a functional capability, defer, narrow, or stop.

This workflow is read-only. It may produce a proposed packet and route, but it does not create project contexts, select a production stack, write code, access sensitive data, deploy, or grant authority. Those actions remain subject to the requested mode and explicit approval.

## WHEN TO USE

- Starting a genuinely new product, service, app, client website, internal tool, or AI-enabled capability.
- Reframing work whose outcome, user, scope, evidence, risk, or first slice remains unclear.
- Turning a vague brief, rescue request, or opportunity into a bounded next decision.
- Deciding whether the work needs deeper evidence, a design exploration, a technical spike, assurance framing, or direct implementation.

## NEVER DO

- Force every request through research, personas, competitor analysis, full UI design, an architecture review, a fixed stack, or deployment planning.
- Treat an early concept, polished prototype, model confidence score, or roadmap item as proof of demand, feasibility, safety, quality, or user value.
- Invent project facts, user research, constraints, market claims, or authority to complete a packet.
- Create a permanent agent swarm or call every functional lead. Use direct work by default; add a functional perspective only for a named uncertainty.
- Persist secrets, credentials, raw client personal data, full chat transcripts, or speculative material as project truth.
- Turn a proposal into a local or external action without the required approval.

## TRIAGE THE STARTING CONDITION

First name the starting condition. The same first-direction workflow should not pretend that every request is a greenfield product:

| Starting condition | Start from | Avoid |
| --- | --- | --- |
| Narrow request or local correction | Current behaviour, desired behaviour, affected surface, and acceptance check. | A product brief or formal discovery. |
| Greenfield idea | Actor, problem context, alternatives, value hypothesis, and decision budget. | Premature stack, roadmap, or agent architecture. |
| Existing-product improvement | Current journey, defect/support signals, observed friction, and known constraints. | Repeating discovery that existing evidence already answers. |
| Client website or service brief | Audience, commercial outcome, decision-maker constraints, first conversion or trust journey. | Inventing a startup strategy, market claim, or unnecessary platform scope. |
| Technical rescue | Symptoms, affected surface, recent changes, containment, and available evidence. | Rebranding a narrow defect as a product rewrite; route to `debug-issue` when diagnosis is the real first action. |
| High-impact or regulated initiative | Affected parties, authority, harm, data, and reversibility. | Treating a small UI or prototype as low-risk when the consequence is not. |

## CHOOSE A PROPORTIONAL PATH

Choose the lightest path that protects the riskiest decision. Path selection is about consequence, uncertainty, sensitivity, reversibility, and coordination cost—not project status or document length.

| Path | Use when | Minimum durable truth | Default outcome |
| --- | --- | --- | --- |
| A — bounded change | The intent is clear, reversal is cheap, consequence is low, and a local check is available. | Current and desired behaviour, affected surface, acceptance check, rollback or correction path. | Propose direct implementation or a narrow diagnosis. |
| B — normal initiative | A product, client, internal-tool, or existing-product decision is material but contained. | Project Decision Packet, first valuable slice, non-goals, material assumptions, acceptance signal, next owner. | Bounded discovery, design/feasibility work, or approved first slice. |
| C — high-impact initiative | Harm, privacy, security, financial, legal, reputational, access, external-action, public-commitment, or hard-to-reverse risk is material. | Expanded packet: parties, authority, data, failure tolerance, evaluation, human control, containment, and required approval. | Do not proceed, narrow to decision support, or prepare a tightly bounded pilot for human approval. |

Path A may collapse to a task statement. Path B should remain short enough to read in one sitting. Path C must be inspectable enough for an accountable human to judge whether risk, authority, and evidence are acceptable; paperwork never makes an unacceptable use case safe.

## FORM THE PROJECT DECISION PACKET

Create only the fields that change the next decision. A normal initiative usually needs the following:

| Field | Required question |
| --- | --- |
| Outcome | What user, client, or operating outcome should improve? |
| Context | Who is affected, in what situation, with what alternative and constraints? |
| First valuable slice | What smallest behaviour can provide value or useful learning? |
| Non-goals | What will not be solved or committed to now? |
| Assumptions and unknowns | Which beliefs could change direction, and what evidence would matter? |
| Acceptance signal | What would count as useful, correct, safe, or worth continuing? |
| Decision budget | What time, cost, coordination, or exposure is justified before the next review? |
| Next step and owner | What is the next reversible action, who owns the decision, and what ends it? |

For an AI-enabled or high-impact initiative, add only the risk-bearing fields: AI suitability versus non-AI baseline; data classification and access; error and misuse consequences; representative evaluation; user correction, override, or appeal; fallback/containment; monitoring if live; and the approval gate before exposure or external effect.

Mark facts, inferences, assumptions, and aspirations differently. Link to project-local source artefacts rather than duplicating sensitive data. Keep accepted structural decisions as short records that can be superseded with their rationale; do not create decision records for trivial or temporary choices.

## APPLY DECISION GATES, NOT PHASES

A gate is a checkpoint that prevents a specific failure. It may collapse into one sentence, be met by existing evidence, or be skipped only when its risk is absent, already controlled, or irrelevant.

| Gate | Risk prevented | Minimum evidence | May collapse when | Must not collapse when |
| --- | --- | --- | --- | --- |
| Frame | Building for an unclear or invented outcome. | Outcome, affected context, current behaviour or explicit hypothesis. | A clear local correction. | Objectives conflict, beneficiary is unclear, or impact is high. |
| Bound | Scope expansion and accidental commitments. | First slice, non-goals, known dependencies, stop condition. | The task itself is already narrow. | Multiple stakeholders, broad platform promises, or external systems are involved. |
| Choose evidence | Polished but uninformative work. | Decision-changing uncertainty and cheapest credible check. | Direct work is reversible and is itself the credible test. | Wrong assumptions could cause harm, lock-in, or invalidate the direction. |
| Shape | An unusable, uncontrolled, or context-blind interaction. | Relevant flow, example, prototype, or alternative. | No meaningful interaction exists and behaviour is directly testable. | User flow, accessibility, uncertainty display, or human control changes the outcome. |
| Feasibility | An impossible, insecure, unaffordable, or hard-to-maintain commitment. | Constraint check, spike, decision note, or cost boundary. | Local known-pattern work. | New external contract, sensitive data, broad permissions, material performance/cost, or hard-to-reverse commitment. |
| Assurance | Harmful, insecure, privacy-invasive, unreliable, or non-compliant use. | Failure cases, evaluation/acceptance basis, access boundary, and control plan as relevant. | Low-risk deterministic local work with a sufficient local check. | AI variability, sensitive data, external effect, high-impact decisions, or regulatory/domain consequence. |

## USE COLLABORATION AS A LOOP

Functional perspectives are lenses, not a relay race. The normal loop is **frame → shape or test → learn → revise or commit**. Architecture and Assurance may enter early if they change the decision; Engineering may run a small spike before framing is complete if that is the cheapest evidence.

| Need | Involve | Expected contribution | Do not involve when |
| --- | --- | --- | --- |
| Unclear value, actor, scope, or competing priorities | Product Thinking | Problem frame, first slice, non-goals, uncertainty or evidence proposal. | The requested change and acceptance condition are clear. |
| Interaction, trust, accessibility, information flow, or brand meaning changes the outcome | Design/UI | Representative flow, prototype, content, or control decision. | The work is non-interactive or uses an established pattern without material UX consequence. |
| Boundary, data, dependency, security, cost, performance, or reversibility decision | Architecture | Viable options, tradeoffs, smallest safe commitment, spike/ADR recommendation. | The change is local and within an existing, understood shape. |
| Build path, integration, reliability, or slicing uncertainty | Engineering | Thin slice, feasibility evidence, testable increment, or bounded diagnostic. | No implementation decision is pending. |
| Sensitive data, AI variability, security, external effects, material harm, or domain consequence | Assurance | Failure cases, evaluation/control needs, authority boundary, and stop criteria. | Low-risk deterministic work with a sufficient local check. |

Use `task-dispatch` only when a bounded worker has an independent, finite, inspectable task with minimum context and no unapproved side effect. A worker cannot redefine the product, access broad workspace data for convenience, contact external parties, spend money, deploy, or approve its own result.

## STATE CONTRACT AND ROUTING

The states describe observable conditions. They are not a fixed sequence, and new evidence may return work to an earlier state. This workflow ends once it has a decision-ready handoff or a deliberate stop; delivery is owned by the selected next workflow.

| State | Required result | Stop or next route |
| --- | --- | --- |
| `received` | A normalized request with its source, starting condition, and claimed urgency. | Stop on no identifiable request or unauthorized source; otherwise triage. |
| `triaged` | Path classification and the first relevant uncertainty/risk scan. | Bounded change → `bounded`; normal initiative → `framed`; high-impact → `assurance-framed`; technical rescue → `debug-issue`. |
| `bounded` | Current/desired behaviour, acceptance check, affected surface, and correction path. | Propose `build-feature` or a narrow specialist route; escalate if a hidden dependency appears. |
| `framed` | Outcome, context, first slice, non-goals, assumptions, and decision budget. | Evidence gap → `evidence`; interaction gap → `shaped`; feasibility gap → `feasibility`; sufficient clarity → `ready-to-build`; invalid premise → `stopped`. |
| `evidence` | A decision-relevant result, explicitly unresolved uncertainty, or a conclusion that learning is not worth its cost. | Revise `framed`, move to `feasibility`, or stop. |
| `shaped` | A representative flow, interaction decision, or explicitly irrelevant design finding. | Return to `framed`, move to `feasibility`, or proceed when the first slice is clear. |
| `feasibility` | A viable thin slice, spike result, or decision note for a material commitment. | Revise scope, call Assurance, select `plan-architecture`, or proceed to `ready-to-build`. |
| `assurance-framed` | Affected parties, authority/data boundary, failure/evaluation outline, human-control and containment proposal. | Stop or redesign if authority, evidence, or safety basis is inadequate; otherwise form a bounded, approval-gated proposal. |
| `ready-to-build` | A buildable first slice, acceptance signal, owner, selected route, and exact approval needed for mutation. | Handoff to the selected workflow. |
| `stopped` | A clear stop/defer rationale and retained learning that may matter later. | Reopen only when the request or material evidence changes. |

## PACKAGE AND HAND OFF

Return the smallest fitting packet.

```text
Path and decision: direct, frame, test, narrow, defer, stop, or prepare for approval
Outcome and context: affected actor, situation, alternative, constraints
First valuable slice: one bounded behaviour or learning objective
Non-goals: excluded promises and deferred decisions
Evidence and unknowns: facts, inferences, assumptions, and the dominant uncertainty
Acceptance or evaluation signal: what will make the next decision credible
Decision budget and risk: material exposure, reversibility, and cost of delay
Authority boundary: permitted data/actions and the approval needed before mutation or exposure
Recommended next route: direct build, debug, design, architecture, assurance, test, or none
```

When the user authorises a project-context write, create only factual context required by the selected route. Use a context template as scaffolding and retain a task-scoped workflow state record separately. Do not turn a working brief into global memory.

## REFERENCE LOADING RULES

- Load `product-thinking` for framing, value, scope, evidence, or AI-suitability decisions.
- Load `research-analysis` or `competitor-profiling` only when external evidence can change a real choice.
- Load Architecture, UI/UX, Security, Testing, or a specialist pack only when a gate actually triggers that perspective.
- Load `task-dispatch` only after a bounded-worker case is established.
- Load detailed references under the selected skill's own loading rules. Do not load a library to make the packet look complete.

## NON-NEGOTIABLE CHECKLIST

1. State the next decision and the consequence of being wrong.
2. Start from the actual request type; do not force a greenfield-product framing.
3. Keep only facts and questions that can change the next move.
4. Make the first slice, non-goals, acceptance signal, and stop condition visible when they matter.
5. Keep functional collaboration conditional, bounded, and loop-based.
6. Preserve data, authority, external-action, and approval boundaries.
7. Hand off to a distinct delivery, diagnosis, architecture, design, assurance, or test workflow; do not begin that work inside this read-only route.
