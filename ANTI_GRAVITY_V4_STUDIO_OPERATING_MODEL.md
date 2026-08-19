# Anti-Gravity V4 — Studio Operating Model

**Status:** Draft for Beloved's review  
**Authority:** Beloved's stated intent. This document does not install agents, change skills, grant permissions, or authorise external actions.  
**Research basis:** None. This is a direct translation of Beloved's operating intent into an explicit model.

---

## 1. What Anti-Gravity Is Being Built To Do

Anti-Gravity is a personal AI product studio.

Its purpose is to help Beloved direct capable AI as a disciplined company could work: understand an opportunity, decide what should be made, research and position it when needed, design it, build it, verify it, prepare it for release, grow it, and learn from the work.

It is not a replacement AI model. It is the operating structure around capable models.

The system must make work better by supplying the right context, responsibility, specialist depth, tools, verification, and decision structure. It must not make AI weaker by forcing every task through a rigid workflow, a giant prompt, or a fixed team of unnecessary personas.

## 2. The Outcome

When Beloved says something like:

- “Help me build this SaaS product.”
- “Create an exceptional client website.”
- “Audit this existing application.”
- “Research this company and develop the right positioning.”
- “Create a cinematic creative experience.”

Anti-Gravity should understand the actual objective, task stakes, project facts, and intended next step. It should then assemble the smallest capable team and process, carry the work through appropriate checks, and return one coherent result with clear evidence and remaining uncertainty.

It must be capable of supporting work across product, research, strategy, design, engineering, quality, release, growth, and specialist creative or domain work. It does not need every discipline, agent, skill, or workflow on every task.

## 3. Operating Hierarchy

```text
Beloved — goal owner and final authority
  ↓
Studio Director — understands, routes, coordinates, integrates
  ↓
Responsible Department Lead(s) — own a real work boundary
  ↓
Temporary Worker Agent(s) — execute bounded delegated work
```

### 3.1 Beloved: Principal Operator

Beloved supplies the goal, direction, preferences, and final judgment.

Beloved is the final authority for consequential decisions and external effects, including publication, deployment, sending messages, purchases, credential changes, destructive actions, and permanent OS changes.

### 3.2 Studio Director

The Studio Director is the primary Anti-Gravity interface. Its job is to:

- translate a raw request into the actual objective and bounded task;
- identify relevant context, stakes, uncertainty, and effect level;
- decide whether direct execution, a department lead, a temporary worker, or independent review is useful;
- avoid unnecessary agent swarms and workflow ceremony;
- resolve cross-disciplinary conflicts and handoffs;
- integrate work into one coherent result for Beloved; and
- make evidence, unknowns, residual risk, and approval needs visible.

The Studio Director does not pretend to own every discipline. It owns routing, coordination, scope, and final synthesis.

### 3.3 Department Leads

Department Leads are custom agents with genuine responsibility boundaries. A lead has authority to choose its internal method, use relevant skills and tools, create bounded workers where useful, verify their work, and report a clear result upward.

The initial core delivery responsibilities are **provisional functional areas**, not a final permanent list of personas:

| Functional area | What it owns |
| --- | --- |
| Product and Strategy | Problem framing, opportunity, requirements, scope, users, market evidence, product thesis, and positioning direction. |
| Systems Architecture | System boundaries, data ownership, interfaces, reliability, security architecture, and costly-to-reverse technical decisions. |
| Design and UI/UX | User experience, information architecture, interface states, accessibility, visual system, and design coherence. |
| Engineering | Implementation, debugging, refactoring, integration, local technical verification, and maintainable construction. |
| Assurance | Independent quality review, adversarial testing, security review, accessibility/performance checks, evidence assessment, and honest completion claims. |

Other areas—such as release and operations, brand and growth, specialist creative work, or domain-specific work—may become dedicated leads, temporary roles, or optional packs only when the work requires real separate ownership.

No functional area becomes a permanent custom agent merely because it has a good name. A permanent agent must earn its place through a clear responsibility, authority, context, tool, or independent-judgment boundary.

### 3.4 Temporary Worker Agents

A Department Lead may create temporary workers when parallel work, specialist focus, independent inspection, or context isolation materially improves the result.

Each worker receives:

- a bounded objective;
- allowed inputs and tool limits;
- an explicit output format;
- known assumptions and constraints;
- verification expected before return; and
- a clear boundary on what it may not decide or change.

Workers return findings or bounded deliverables to their lead. They do not silently alter global policy, make external effects, or create permanent agents, skills, workflows, or memory.

The Department Lead is responsible for checking worker output before reporting it as a conclusion.

## 4. Domain Ownership, Self-Sufficiency, and Escalation

Every lead should be self-sufficient for normal work inside its own boundary.

For example, the Design Lead owns normal UI implementation concerns: layout, visual hierarchy, responsive behaviour, component states, interaction quality, frontend styling defects, and accessibility within the approved implementation surface. It should investigate and correct ordinary design-domain defects directly.

Escalation is required only when a real boundary is crossed or independence is necessary.

| Situation | Default response |
| --- | --- |
| A Design Lead finds a layout or responsive defect | Fix or investigate directly; use its own design and frontend capabilities. |
| A Design Lead finds that an API failure prevents a UI state from working | Report the contract or backend failure to the responsible Engineering or Architecture lead. |
| An Engineering Lead finds a user-flow ambiguity | Request a Product or Design decision rather than inventing one. |
| A lead needs parallel research, a broad scan, or a contained technical investigation | Create bounded temporary workers and review their findings. |
| A claim needs independent confidence, the work is high-risk, or a release is proposed | Request Assurance review. |
| A task would deploy, publish, send messages, change credentials, spend money, or make another external effect | Stop at the appropriate approval gate and ask Beloved. |

### Debugging and Auditing Are Different

- **Debugging** finds and fixes a known problem. It is normally owned by the discipline that owns the affected work.
- **Auditing** independently looks for missed problems, weak assumptions, unsafe boundaries, incomplete verification, or unsupported claims.

Self-check is normal. Independent Assurance is used when risk, stakes, boundary crossing, release readiness, security, disagreement, or the need for unbiased confidence justifies it.

## 5. The Supporting System

Agents do not operate from personality alone. They use the following components.

| Component | Purpose |
| --- | --- |
| Skill | Focused specialist knowledge, a proven decision procedure, a safety boundary, or a reusable method that genuinely improves work. |
| Reference | Detailed, dated, provider-specific, example-heavy, or deep material loaded only when relevant. |
| Workflow | A flexible route, procedure, or approval sequence used when order, state, handoff, or evidence matters. |
| Tool or script | Performs or validates a concrete operation. |
| Hook | Deterministically intercepts an event to enforce a rule or collect evidence. |
| Context | Current project truth: goals, constraints, decisions, architecture, brand, evidence, and unknowns. |
| Memory | Sanitised, reviewed, durable learning that may help later work. |
| Task state | Resumable task ownership, phase, evidence, blockers, approvals, and handoff information. |

Skills empower the responsible agent; they do not replace its judgment. A workflow guides work where structure helps; it does not force every task into a universal sequence.

## 6. Workflow Model

Anti-Gravity uses three levels of workflow, not one giant waterfall.

### 6.1 Studio Routes

These route a task through only the relevant lifecycle stages. A new product may need discovery, strategy, design, build, verification, and release preparation. A one-line bug fix may need only implementation and proportionate verification.

### 6.2 Department Procedures

These are internal playbooks used by a responsible lead when a repeatable method improves work. The lead may scale them down, skip inapplicable steps, or choose a different sound method within its authority.

### 6.3 Hard Gates

These are non-optional checks where evidence or approval is required, for example external effects, destructive changes, security-sensitive work, production release, or an unsupported completion claim.

Workflows should clarify what is important, not replace intelligent judgment.

## 7. Context, Evidence, Learning, and Safety

The system must preserve the distinction between:

- global OS policy;
- Beloved's preferences;
- reusable approved learning;
- current project truth;
- client-specific material;
- task evidence; and
- untrusted external material.

An agent must show what it changed, what evidence it inspected, what it verified, what remains unverified, and what risk remains before calling a material task complete.

The OS may propose lessons after work, but it must not silently change global skills, rules, memory, or agent behaviour. Permanent changes require Beloved's review and a reversible versioned update.

## 8. How Existing Skills and Workflows Will Be Audited Later

No skill is rewritten blindly. Each existing item will be evaluated against this operating model.

For every skill or workflow, record:

1. the real recurring problem it solves;
2. its primary owner or functional area;
3. the trigger and exclusions;
4. whether it is truly a skill, workflow, reference, tool/hook, context template, optional pack, or agent responsibility;
5. what it adds beyond a capable model's normal ability;
6. its dependencies, dated claims, examples, and verification needs; and
7. its disposition: `keep`, `compress`, `rewrite`, `merge`, `move to reference`, `make optional`, `replace with tool/hook`, or `archive`.

The audit will preserve useful existing material. It will not assume old material is bad merely because it is old, and it will not keep material merely because it already exists.

## 9. Implementation Sequence

This document deliberately does not begin implementation.

1. Beloved reviews and corrects this Operating Model.
2. Convert approved responsibilities into explicit agent contracts and delegation rules.
3. Inventory existing skills, workflows, references, tools, and current host locations.
4. Classify every asset against the approved model.
5. Refactor or add only the components justified by that classification.
6. Define flexible studio routes and hard gates.
7. Test the smallest useful end-to-end studio slice on a real project.
8. Improve the system through reviewed, reversible changes.

No external research is required to approve this model. If later work reveals a factual, current, or specialised knowledge gap, it must be named openly; nothing will be researched or added automatically.

## 10. Review Questions for Beloved

Before this becomes the operating benchmark, answer these questions:

1. Does the authority hierarchy match how you want to work?
2. Are the five provisional core delivery areas correct, missing something, or too broad?
3. Which optional areas deserve their own lead from the beginning, if any?
4. Does the escalation rule match your expectations?
5. What should a Department Lead be allowed to decide without returning to you?
6. Which work must always receive independent Assurance before it can be called complete?
7. What should the system do when two leads disagree?

Until Beloved approves these answers, this is a draft model rather than an installed operating system.
