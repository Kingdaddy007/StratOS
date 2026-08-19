# Anti-Gravity OS v4 Architecture Capability Decision Packet

**Status:** Research synthesis and evaluation specification  
**Version:** 0.1  
**Verified:** 2026-08-18  
**Scope:** Software and systems architecture capability only  
**Authority:** This document proposes what should be evaluated. It does not install an agent, activate a skill, grant permission, or approve an external action.

## Plain-English conclusion

Anti-Gravity needs an architecture capability, but it does not yet need a large architecture department or a library of architecture lectures.

The smallest promising design is:

1. detect whether a request is architecturally significant;
2. give one responsible reasoning role a compact set of architecture obligations;
3. ground that reasoning in current project architecture context;
4. record expensive-to-reverse decisions;
5. use deterministic checks for properties that tools can prove;
6. use independent review for residual architectural risk; and
7. keep specialised knowledge conditional.

Four custom capability candidates deserve controlled testing. None is approved as a skill yet:

- quality-attribute scenario and trade-off analysis;
- safe API and database evolution;
- network failure, timeout, retry, and idempotency design; and
- multi-tenant and trust-boundary design.

The machine-readable evaluation suite is [`tests/fixtures/architecture_capability_evals.json`](../tests/fixtures/architecture_capability_evals.json).

## Decision classification

This is a **Type 1.5 decision**. Choosing the architecture kernel is reversible, but a bad choice can spread through every future skill, workflow, project, and host adapter.

The safe sequence is therefore:

```text
discover capabilities
        -> define the smallest candidate kernel
        -> run A/B/C evaluations
        -> accept, revise, demote, or reject each component
        -> only then author runtime agents, skills, workflows, and tools
```

## Research synthesis

Three independent reports were compared against the original assignment.

| Report | What it contributed | Main limitation | How it is used here |
| --- | --- | --- | --- |
| Grok | Best anti-bloat judgment, responsibility boundaries, adversarial fixtures, and explicit non-decisions | Mixed source quality and an untested conclusion that only four skills survive | Primary decision logic and evaluation shape |
| Gemini | Broadest technical inventory and strongest capability-to-component mapping | Overconfident language, premature implementation, and several rigid universal rules | Technical coverage and candidate mechanisms |
| ChatGPT | Accessible lifecycle overview and useful test categories | No verifiable source ledger, incomplete required structure, generic prompt-first solutions, and unsupported thresholds | Secondary checklist only |

Agreement between the reports is treated as a hypothesis, not proof. The accepted direction below also had to survive first-principles review, source cleanup, and an anti-boxing check.

## Bedrock truths

The architecture capability is rebuilt from the following truths rather than from the current v3 skill inventory:

1. Some software decisions are substantially more expensive to reverse than others.
2. A product's required qualities can conflict; improving one can worsen another.
3. Boundaries, ownership, and contracts determine how failures and changes propagate.
4. Distributed communication can fail partially, repeat, arrive late, or arrive more than once.
5. Security depends on explicit trust boundaries and server-side enforcement, not descriptive intent.
6. Architecture documentation can drift away from implementation.
7. Deterministic tools are stronger than model self-assessment for mechanically checkable properties.
8. A strong frontier model already knows much common architecture vocabulary.
9. Additional instructions can improve judgment, add ceremony, or anchor the model toward an inferior solution.
10. Therefore, every custom architecture component must prove that its benefit exceeds its cost and constraint.

## Complete architecture capability map

The domain contains ten capability groups. A group is not automatically a skill or agent.

### 1. Problem and quality foundations

- clarify the product outcome, users, constraints, non-goals, and ambition;
- identify architecturally significant requirements;
- turn important qualities into measurable scenarios;
- rank competing qualities and expose trade-offs;
- evaluate build, buy, and compose options; and
- distinguish verified constraints from inherited assumptions.

### 2. Structure, boundaries, and ownership

- choose the smallest topology that satisfies the actual requirements;
- separate domains by ownership and axes of change;
- make data and behaviour ownership explicit;
- design deep interfaces that hide internal complexity;
- prevent unjustified distribution and circular dependencies; and
- state what each boundary does not own.

### 3. Interfaces and contracts

- define internal, public, synchronous, and asynchronous contracts;
- define error, timeout, retry, and idempotency semantics;
- manage compatibility, versioning, deprecation, and semantic change;
- isolate third-party dependencies behind replaceable seams; and
- verify published contracts mechanically where practical.

### 4. Data architecture

- establish the source of truth and mutation authority;
- select storage from access patterns, consistency needs, and operational constraints;
- define transaction and concurrency boundaries;
- design indexes and caches from measured access patterns;
- cover retention, deletion, privacy, backup, and recovery; and
- evolve stored data without corrupting old or new consumers.

### 5. Distributed reliability

- model partial failure and dependency unavailability;
- bound timeouts, retries, backoff, jitter, and retry budgets;
- design idempotent effects and duplicate handling;
- define ordering, delivery, and consistency expectations;
- contain failure with bulkheads, load shedding, and degradation paths; and
- design disaster recovery proportional to actual impact.

### 6. Security and privacy architecture

- map actors, assets, data flows, and trust boundaries;
- define authentication, authorisation, and privileged operations;
- enforce tenant and client isolation;
- manage secrets, sensitive data, and supply-chain trust;
- identify abuse cases and threat paths; and
- assign final control sufficiency to independent security review.

### 7. Performance, scale, and cost

- define latency, throughput, capacity, and resource budgets;
- measure before optimisation;
- model contention and saturation rather than relying on average load;
- choose horizontal or vertical scaling from evidence;
- treat cost as a quality attribute; and
- detect both over-engineering and under-engineering.

### 8. Operability

- define logs, metrics, traces, health signals, and diagnostic ownership;
- ensure failures are diagnosable by someone other than the original author;
- define environment and configuration boundaries;
- make deployment and rollback structurally possible;
- establish alerting and incident evidence; and
- prevent telemetry cost and cardinality explosions.

### 9. Evolution

- preserve consequential decisions and their assumptions;
- design reversible change and component replacement;
- use incremental migration where a one-step change is unsafe;
- track architecture debt and expiry conditions;
- retire deprecated paths using observed usage; and
- revisit decisions when their assumptions stop holding.

### 10. Verification and conformance

- validate dependency direction and cycles;
- validate schemas and public contracts;
- test migrations, load, resilience, and failure behaviour where relevant;
- compare implementation with declared architecture;
- disclose coverage limits and residual risk; and
- keep deterministic evidence separate from agentic opinion.

## Responsibility boundaries

Accountability is assigned by outcome, not by impressive role names.

| Outcome | Final accountability | Important collaborators | Boundary |
| --- | --- | --- | --- |
| Problem, desired outcome, non-goals, and ambition | Product | Architecture, Design | Architecture cannot invent the product's purpose |
| Quality-attribute priority and architecture scenarios | Architecture | Product, Engineering, Quality | Product sets business priority; Architecture makes technical implications explicit |
| System, module, interface, and data ownership | Architecture | Engineering | Engineering can challenge the boundary but must not drift across it silently |
| Component implementation and local tests | Engineering | Architecture, Quality | Architecture does not own syntax or routine implementation choices |
| UX states, interaction, accessibility, and visual system | Design | Product, Engineering | Architecture constrains feasibility and performance, not creative direction |
| Threat-model completeness and control sufficiency | Quality and Security | Architecture, Engineering | Architecture draws trust boundaries; Security can block unsafe release |
| Independent verification and residual-risk report | Quality and Security | Architecture, Engineering, Operations | The designer must not be the only evaluator |
| Deployment, rollback, environments, and operational readiness | Release and Operations | Architecture, Quality | Architecture must make operation possible; Operations owns execution |
| ADR hygiene, evidence provenance, and lesson freshness | Knowledge and Learning | Architecture, all functions | Knowledge preserves reviewed conclusions, not raw model output |

### Arbitration rules

- Product may reduce scope, but it cannot silently waive security or data-integrity requirements.
- Architecture may reject an infeasible design, but it must show the constraint and viable alternatives.
- Engineering may choose local implementation details inside an approved boundary.
- Security may block release for an unresolved critical control failure.
- Operations owns production execution; architecture documentation is not deployment approval.
- Human approval remains mandatory for production, destructive data changes, money, identity, publishing, and other external effects.

## Architecture significance gate

Architecture reasoning should activate when at least one trigger is present:

- a new product, service, major subsystem, or bounded context;
- a public or cross-component interface is created or changed;
- data ownership, schema, retention, or migration changes;
- authentication, authorisation, tenant isolation, money, identity, or sensitive data is involved;
- a remote dependency can create partial failure or duplicate effects;
- availability, latency, scale, compliance, or material cost has an explicit target;
- deployment topology, rollback, or infrastructure boundaries change;
- a decision is expensive to reverse; or
- implementation appears to violate an accepted architectural decision.

Architecture should normally remain quiet for:

- copy changes;
- isolated visual styling;
- a single-function correction with no boundary effect;
- formatting, naming, or internal mechanical cleanup;
- a small script without persistent data or external effects; and
- requests whose only architectural content is fashionable terminology.

If significance is uncertain, the system should ask one or two targeted questions or perform a lightweight architecture check. It should not launch the full process by default.

## Capability-to-component decisions

| Capability | Smallest proposed form | Decision state | Reason |
| --- | --- | --- | --- |
| Architecture significance detection | Compact kernel routing rule | Evaluate | Prevents both missed architecture and unnecessary ceremony |
| Quality-attribute ranking | Architect responsibility | Evaluate | Core judgment, not a standalone lecture |
| Measurable quality scenarios | Candidate skill or workflow | Test candidate | Procedural method may outperform generic NFR lists |
| Boundary and ownership design | Architect responsibility plus project context | Evaluate | Central accountability that depends on live project truth |
| Monolith, services, events, or serverless choice | Architect responsibility | Evaluate | Must remain conditional; never a style-specific skill |
| Common design principles and pattern definitions | No custom component | Reject | Strong models already know them |
| Project architecture map and budgets | Project context | Accept in principle | Facts vary by project and must not live in global policy |
| Public API description | Project artifact plus standard tool | Conditional | Useful when consumers or compatibility exist |
| Contract and schema compatibility checking | Tool or script | Evaluate per stack | Mechanical checks should be deterministic |
| Safe API and schema evolution | Candidate skill plus workflow and tools | Test candidate | Sequence and compatibility failures can be expensive |
| Basic SQL, normalisation, and index tutorials | No custom component | Reject | Model-common knowledge |
| Data ownership and consistency class | Architect responsibility | Evaluate | Missing ownership can create silent corruption |
| Event sourcing, CQRS, consensus, and multi-region | Optional specialist reference or pack | Defer | High-value only when qualifying conditions exist |
| Network failure and idempotency design | Candidate skill plus tests | Test candidate | Models often miss duplicate effects and retry amplification |
| Threat modelling | Security workflow with architecture input | Coordinate later | Security owns final assurance |
| Multi-tenant and trust-boundary design | Candidate skill plus verifier | Test candidate | Cross-tenant failure is catastrophic and context-dependent |
| Performance and cost budgets | Project context plus measurement tools | Accept in principle | Numeric targets are project facts, not global defaults |
| Provider pricing and console instructions | Dated reference | Conditional | Volatile and provider-specific |
| Observability vocabulary | Reference | Conditional | Useful on demand; must follow specification stability |
| ADR capture | Lightweight workflow and template | Evaluate | Procedure and state matter more than prose |
| Dependency boundaries | Stack-specific tool | Evaluate | Deterministic but not language-neutral |
| Architecture conformance review | Independent verifier | Evaluate | Reduces self-certification bias |
| Destructive and production protection | Host approval semantics and validated hooks where supported | Preserve | Safety policy, not an architecture skill |

## Minimal candidate kernel

The kernel is **universally available but selectively activated**. It is not an always-running architecture ceremony.

### K1. Significance detection

Decide whether architecture reasoning is required and identify the minimum depth.

### K2. Architect obligations

For significant work, require the responsible role to identify:

- objective and current reality;
- architecturally significant requirements;
- assumptions and real constraints;
- boundaries and ownership;
- important data and control flows;
- at least two genuinely viable options for consequential decisions;
- trade-offs and failure behaviour;
- security and privacy implications;
- reversibility and migration path;
- verification evidence; and
- residual risk.

This is an obligation contract, not a requirement to generate a long report.

### K3. Project architecture context

Load current architecture facts only when relevant:

- system context and major containers;
- module and data ownership;
- external dependencies;
- public contracts;
- quality and cost budgets;
- accepted ADRs;
- forbidden couplings;
- current migrations and known debt; and
- open questions and stale assumptions.

Observed implementation outranks stale documentation. A mismatch must be reported.

### K4. Consequential decision record

Record decisions that are expensive to reverse. A minimal record contains:

- decision and status;
- context and drivers;
- options considered;
- trade-offs accepted;
- assumptions;
- consequences;
- reversibility;
- confirmation evidence; and
- review trigger.

Routine Type 2 choices should not produce full ADRs.

### K5. Deterministic conformance

Use a tool only when the repository and stack make the check meaningful. Examples include:

- dependency-direction and cycle rules;
- OpenAPI, AsyncAPI, Protobuf, or JSON Schema validation;
- breaking-contract detection;
- migration ordering and compatibility tests;
- permission and tenant-isolation tests; and
- load or fault tests for explicit reliability targets.

Tools can prove configured properties, not architectural correctness as a whole.

### K6. Independent review and approval

An independent evaluator reviews high-impact architecture for hidden failure modes, unjustified complexity, security gaps, and unsupported completion claims. Independence may be a separate agent, separate context, deterministic tool, or human review; the exact mechanism remains open.

The kernel never converts review into permission. External and destructive actions still require their own approval.

## Candidate capability specifications

### C1. Quality-attribute scenario and trade-off analysis

**Problem:** Models commonly list qualities such as performance and security without making them measurable or resolving conflicts.

**Activate when:** Starting a non-trivial product or subsystem, or changing availability, security, privacy, data integrity, latency, cost, or other important quality requirements.

**Exclude when:** Copy, styling, isolated fixes, and small internal changes have no material quality-attribute effect.

**Unique procedure:** Convert the highest-priority qualities into scenario elements such as source, stimulus, environment, affected artifact, response, and measurable response. Identify sensitivity and trade-off points.

**Invariants:**

- qualities must be ranked rather than declared universally maximal;
- top qualities need observable success criteria;
- conflicts and accepted compromises must be explicit; and
- the method must scale down for a one-operator project.

**Overridable heuristics:** Use three to five scenarios by default, but permit fewer for small work and more for safety-critical systems.

**Boxing risk:** Turning a lightweight decision aid into mandatory ATAM ceremony.

**Evaluation focus:** Whether C discovers measurable and conflicting requirements that A and B miss without producing unnecessary process.

### C2. Safe API and database evolution

**Problem:** A syntactically valid change can break existing consumers, stored data, rollback, or mixed-version deployment.

**Activate when:** Existing production data, published interfaces, multiple consumers, mixed application versions, or non-trivial rollback requirements exist.

**Exclude when:** The system is unreleased, has no persistent data, and all consumers can change atomically.

**Unique procedure:** Identify compatibility direction and use staged change when necessary: expand, migrate or dual-read/write, verify adoption, and contract only after old dependencies are gone.

**Invariants:**

- old code must not lose a field or structure it still requires;
- destructive contraction must follow evidence that old readers and writers are gone;
- rollback behaviour must be described; and
- data backfill must be restartable and observable.

**Overridable heuristics:** A one-step change remains valid for empty, disposable, or atomically upgraded systems.

**Boxing risk:** Forcing expensive dual-write migrations onto greenfield or disposable environments.

**Evaluation focus:** Whether C prevents breaking changes and unsafe rollback without blocking justified simple changes.

### C3. Network failure, timeout, retry, and idempotency design

**Problem:** Remote calls can time out after succeeding, be retried, duplicate effects, overload dependencies, or fail at one layer while succeeding at another.

**Activate when:** A remote call performs a user-visible write, moves money, changes identity or permission, triggers a job, or participates in a critical request path.

**Exclude when:** The operation is a pure in-process function or a disposable read with no relevant side effect.

**Unique procedure:** Classify the effect, define timeout and deadline behaviour, decide whether retry is safe, bound retries, use backoff and jitter where appropriate, and prove idempotency or explicitly prohibit automatic retry.

**Invariants:**

- every external write must state its idempotency strategy;
- retries must be bounded and must not multiply across layers;
- permanent errors must not be retried; and
- a timeout must not be treated as proof that the remote effect did not occur.

**Overridable heuristics:** Numeric timeout and retry defaults remain project- and dependency-specific.

**Boxing risk:** Introducing circuit-breaker libraries and distributed coordination where a bounded call and clear error are sufficient.

**Evaluation focus:** Whether C prevents duplicate effects and retry amplification while preserving simple designs.

### C4. Multi-tenant and trust-boundary design

**Problem:** A valid query or privileged integration can expose one customer's data to another or allow a confused deputy to act with the wrong authority.

**Activate when:** A shared system has multiple independently authorised customer, organisation, workspace, or tenant boundaries, or privileged access crosses one.

**Exclude when:** The task is ordinary single-company role authorisation, general untrusted-client validation, third-party integration design, or otherwise lacks independently authorised tenant boundaries.

**Unique procedure:** Map actors, assets, trust transitions, tenant identity propagation, server-side authorisation, storage isolation, administrative escalation, audit, and adversarial fixtures.

**Invariants:**

- tenant identity cannot be enforced only by a UI filter;
- authorisation must be checked at the trusted boundary;
- privileged and break-glass access must be explicit and auditable; and
- cross-tenant negative tests must exist for shared storage paths.

**Overridable heuristics:** Pool, bridge, and silo isolation remain design choices driven by risk, cost, and compliance.

**Boxing risk:** Imposing multi-tenant SaaS structure on single-tenant deployments.

**Evaluation focus:** Whether C prevents cross-tenant access and confused-deputy behaviour without inventing unnecessary tenancy.

## Model-common knowledge to exclude

Do not create custom skills whose main content is:

- definitions of SOLID, DRY, cohesion, coupling, or common design patterns;
- REST versus GraphQL versus gRPC comparison essays;
- CAP theorem recitation;
- UML or C4 drawing instructions without a specific decision need;
- generic descriptions of PostgreSQL, Redis, Kafka, Docker, or Kubernetes;
- cloud-console walkthroughs in global policy;
- slogans such as "design for scale" or "think like a principal architect";
- a universal preference for microservices, event sourcing, serverless, or a particular cloud; or
- a mandatory enterprise checklist for small applications.

These may be project context, dated references, or tools when relevant. They do not justify permanent prompt weight.

## A/B/C evaluation protocol

### Conditions

- **A — Baseline:** The same capable model receives the task and project evidence, with no Anti-Gravity architecture customisation.
- **B — Kernel:** The model receives the same material plus only the compact candidate kernel.
- **C — Candidate:** The model receives the same material, the kernel, and exactly one candidate capability.

Do not show one condition's answer to another. Keep model version, tool access, temperature or reasoning setting, context, and time budget as comparable as the host permits.

### Repetition

For a pilot, collect at least three independent result sets spanning at least two model families or fresh runs. This is a minimum for detecting obvious effects, not a statistical proof.

A single scored A/B/C set has only one permitted status: `advance-to-replication`. It may identify a promising candidate, but it must not be described as accepted, approved, installed, or as having passed all survival gates. The three required result sets must each record the model, effort setting, active host baseline, tool access, execution context, execution time, and any unavailable telemetry.

### Blinding

Remove condition and candidate labels from the reviewer material and randomise review order. A judge must score observable behavior against the fixture rather than reward terminology copied from the candidate. The answer key remains withheld until a complete scorecard records the judge identity, reviewing model, timestamp, independence statement, every dimension score, and every rationale.

### Scoring scale

Each dimension is scored from 0 to 4:

| Score | Meaning |
| --- | --- |
| 0 | Missing, dangerous, or materially wrong |
| 1 | Major omissions or unjustified claims |
| 2 | Partially correct but unreliable or incomplete |
| 3 | Correct and useful with minor gaps |
| 4 | Strong, evidence-aware, proportionate, and operationally usable |

### Weighted dimensions

| Dimension | Weight | What the judge examines |
| --- | ---: | --- |
| Correctness and requirement fit | 18 | Does the proposal solve the real problem and respect stated constraints? |
| Failure-mode detection | 15 | Does it find the costly partial, duplicate, stale, overload, or rollback failures? |
| Security and data integrity | 12 | Are trust, authority, isolation, and corruption risks handled? |
| Maintainability and ownership | 10 | Are boundaries, ownership, and change surfaces clear? |
| Adaptability and reversibility | 10 | Can the decision be changed or rolled back safely? |
| Verification evidence | 10 | Are claims connected to executable or observable checks? |
| Unnecessary complexity | 10 | Does it avoid unjustified services, stores, patterns, and ceremony? |
| Instruction rigidity | 5 | Can it override the heuristic when project facts justify a different choice? |
| Context consumption | 4 | Is the improvement worth the additional instruction weight? |
| Tool cost and latency | 2 | Is extra execution proportionate to risk? |
| Adjacent-task harm | 4 | Does architecture guidance stay quiet when irrelevant? |
| **Total** | **100** | |

Scores support comparison; they are not universal measurements of architectural quality.

### Survival gates

A candidate survives the pilot only when all gates pass:

1. C introduces no new critical security, data-integrity, or external-effect failure.
2. C outperforms B on its target behavior in a majority of relevant fixtures and independent runs.
3. The gain is caused by correct decisions, not merely longer answers or copied terminology.
4. C does not create unjustified architecture in the microservices trap or adjacent UI control.
5. C remains overridable when fixture facts justify a simpler path.
6. Added context, tools, latency, and maintenance cost are recorded.
7. A reviewer can identify a repeatable reason for the improvement.

Possible decisions are `accept`, `revise-and-retest`, `demote-to-reference`, `replace-with-tool`, and `reject`.

## Evaluation fixtures

The nine fixtures deliberately include positive, adversarial, anti-boxing, and negative-control work:

| Fixture | Primary target | Failure the test exposes |
| --- | --- | --- |
| Greenfield booking product | C1 | Vague qualities, premature stack selection, unnecessary distribution |
| Live contract and column rename | C2 | Breaking old clients, mixed-version failure, unsafe contraction |
| Conflicting live dual-write | C2 | Divergent fields, ambiguous writer authority, unsafe concurrent backfill |
| Unreleased atomic rename control | C2 | Compatibility ceremony imposed where no compatibility boundary exists |
| Payment webhook and timeout | C3 | Duplicate charge, retry amplification, ambiguous completion |
| Shared multi-tenant notes | C4 | Cross-tenant read/write and confused-deputy administration |
| Single-company internal access control | C4 anti-boxing | Tenant machinery imposed where server-side role checks are sufficient |
| Unjustified microservices request | Kernel and anti-boxing | Compliance with fashionable over-engineering |
| Landing-page visual restyle | Adjacent control | Architecture ceremony contaminating unrelated work |

Full prompts, hidden evaluator risks, prohibited overreach, and scoring focus live in the JSON fixture.
Positive fixtures test their named candidate. The adversarial and adjacent-control fixtures test every candidate separately under Condition C so that irrelevant activation and negative transfer remain visible.

### Pilot runner

The standard-library runner creates isolated prompt and response files without calling a model or spending credits:

```powershell
python tests/architecture_eval_runner.py prepare `
  --candidate quality-attribute-scenarios `
  --run-label pilot-1 `
  --model gpt-5.6-luna `
  --effort max `
  --tool-access "read-only filesystem; no network" `
  --environment "fresh projectless Codex task" `
  --baseline-description "Describe all active host instructions and installed skills" `
  --run-family luna-max-replication-1 `
  --output tmp/architecture-pilot-quality
```

Run every generated prompt in a fresh model task, then paste each answer into its matching file under `responses/`. Immediately bind it to actual execution facts; the runner hashes the response and refuses to blind it without matching evidence. Keep the model, effort setting, tools, and project evidence as comparable as possible.

```powershell
python tests/architecture_eval_runner.py record `
  --bundle tmp/architecture-pilot-quality `
  --scenario booking-greenfield `
  --condition A `
  --thread-id <fresh-task-id> `
  --started-at 2026-08-18T12:00:00+00:00 `
  --completed-at 2026-08-18T12:03:00+00:00 `
  --measurement-note "The host did not expose token or cost telemetry."
```

After all generated responses exist, generate reviewer-safe randomized files:

```powershell
python tests/architecture_eval_runner.py blind `
  --bundle tmp/architecture-pilot-quality `
  --output tmp/architecture-pilot-quality-blind `
  --seed 17
```

Give the reviewer `judge-guide.md`, `scorecard-template.json`, and the `review/` directory. Do not give the reviewer `answer-key.json` until scoring is complete. The scorecard asks for each scenario's declared scoring-focus dimensions, rather than irrelevant dimensions that would make a small control task look like a full architecture review. The runner refuses to overwrite an existing output directory or blind an incomplete response/evidence set. After the independent reviewer fills the template, validate it before decoding the answer key:

```powershell
python tests/architecture_eval_runner.py validate-scorecard `
  --blind tmp/architecture-pilot-quality-blind `
  --scorecard tmp/architecture-pilot-quality-blind/scorecard-template.json
```

## Evidence envelope for each run

Every recorded result should include:

```text
run_id
fixture_id
condition
model and version
reasoning or effort setting
tool access
candidate version or hash
input hash
raw output
dimension scores with rationale
critical misses
unnecessary complexity introduced
judge identity or model
timestamp
cost, latency, and token usage where available
decision notes
```

Outputs containing secrets, personal data, or client-confidential material must not be committed.

## Proposed North Star corrections

These are recommendations, not automatic edits.

### Preserve

- personal AI product studio as the system category;
- universal kernel plus optional specialist packs;
- selective activation and conditional delegation;
- evidence-based completion and disclosed residual risk;
- A/B/C survival testing;
- controlled, human-reviewed learning;
- provider independence; and
- explicit external-effect approval.

### Revise after the pilot

- describe the 12 lifecycle stages as a routable graph, not a process that must be traversed;
- change "enterprise-grade assurance" from a present claim to a measurable aspiration;
- make architecture universally available but selectively activated;
- add data ownership, deletion, reversibility, operability, independent review, and residual risk;
- treat named specialist packs as current examples rather than permanent topology;
- separate deterministic conformance from agentic evaluation; and
- state that host hooks enforce only what the host actually exposes and what tests verify.

### Keep open

- whether Architect is a separate agent, a mode, or a responsibility of another engineering lead;
- the final number of agents or departments;
- whether C4 is required or merely one available notation;
- which language-specific dependency tools are supported;
- whether agentic semantic fitness functions become gates; and
- the final runtime state and evidence schema.

### Explicitly reject

- guaranteed zero defects or vulnerabilities;
- mandatory microservices, event sourcing, TDD, zero-downtime, or cloud architecture for every project;
- silent self-editing of global policy;
- removing human approval merely to increase throughput; and
- writing the four candidate skills before the evaluation justifies them.

## Source ledger

The ledger favours official standards, primary research, official project specifications, and first-party engineering material. Practitioner guidance is labelled as such.

| Claim supported | Source | Institution or author | Date | Category | Status | Verified |
| --- | --- | --- | --- | --- | --- | --- |
| Architecture must be distinguished from its description; descriptions address stakeholder concerns through viewpoints and models | [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) | ISO, IEC, IEEE | 2022-11 | Official standard | Established | 2026-08-18 |
| Product quality can be examined through nine characteristics across the lifecycle | [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | ISO, IEC | 2023-11 | Official standard | Established vocabulary; application remains contextual | 2026-08-18 |
| ATAM evaluates architecture against competing quality attributes and exposes risks, sensitivity points, and trade-off points | [The Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) | Carnegie Mellon Software Engineering Institute | 1998-07 | Authoritative technical report | Established method | 2026-08-18 |
| QAW elicits prioritised and refined quality-attribute scenarios early | [Quality Attribute Workshops, Third Edition](https://sei.cmu.edu/library/quality-attribute-workshops-qaws-third-edition/) | Carnegie Mellon Software Engineering Institute | 2003-10 | Authoritative technical report | Established method; full workshop may be too heavy here | 2026-08-18 |
| OpenAPI is a language-neutral interface description for HTTP APIs | [OpenAPI Specification](https://spec.openapis.org/oas/) | OpenAPI Initiative | Living specification | Official specification | Established; use version supported by project tooling | 2026-08-18 |
| Problem Details defines a standard machine-readable HTTP error representation but does not require it for every API | [RFC 9457](https://datatracker.ietf.org/doc/rfc9457/) | IETF | 2023-07 | Internet standard | Established and conditional | 2026-08-18 |
| Microservices require explicit authentication, service discovery, secure communication, monitoring, resilience, load management, and session handling | [NIST SP 800-204](https://csrc.nist.gov/pubs/sp/800/204/final) | NIST | 2019-08 | Official government publication | Established for microservices, not a reason to adopt them | 2026-08-18 |
| Trust boundaries identify changes in trust level along data flows | [OWASP Threat Modeling Process](https://owasp.org/www-community/Threat_Modeling_Process) | OWASP Foundation | Living page | First-party project guidance | Established technique; page is marked historical | 2026-08-18 |
| Unbounded or multi-layer retries can amplify overload; retries and deadlines require explicit budgets and propagation | [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) | Google SRE | 2016 | First-party engineering book | Established practitioner evidence; numeric defaults are contextual | 2026-08-18 |
| OpenTelemetry semantic conventions have explicit stability levels and mixed-stability areas | [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) | Cloud Native Computing Foundation project | Living specification | Official project specification | Established; individual conventions require freshness checks | 2026-08-18 |
| MADR 4.0.0 provides maintained minimal and full ADR templates | [MADR releases](https://github.com/adr/madr/releases) | MADR maintainers | Living project | Official project release | Established template option, not mandatory process | 2026-08-18 |
| Dependency rules can detect configured cycles and forbidden imports but only within the tool's language and configuration scope | [dependency-cruiser rules reference](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md) | dependency-cruiser maintainers | Living project | Official project documentation | Established for supported JavaScript-family projects | 2026-08-18 |
| A simple constrained software-engineering approach can outperform more complex agent systems on a specific benchmark | [Agentless](https://arxiv.org/abs/2407.01489) | Xia, Deng, Dunn, Zhang | 2024-07 | Primary research preprint | Established for reported benchmark; not universal proof against multi-agent systems | 2026-08-18 |

## Pre-mortem

Assume this architecture reform fails six months from now. The most plausible causes are:

| Failure | Early signal | Prevention in this packet |
| --- | --- | --- |
| The kernel becomes another giant prompt | Token growth without measurable fixture gain | Context-cost score and survival gate |
| Architecture activates for everything | UI and copy tasks receive long architecture reports | Adjacent-task control fixture |
| Candidate skills repeat model-common knowledge | C sounds longer but makes the same decisions as B | Blinded behavior scoring |
| The OS over-engineers simple products | Microservices, queues, or multiple stores appear without a requirement | Unjustified-microservices trap |
| Deterministic tools are treated as omniscient | Passing configured lint is called architecture correctness | Evidence wording that limits tool claims |
| A designer self-certifies unsafe work | No independent failure-mode review | Independent review obligation |
| Source claims become stale | Provider or specification details change silently | Dated source ledger and freshness classification |
| Evaluation favours the component that wrote the rubric | Judge rewards terminology rather than behavior | Blinding, raw outputs, and multiple independent runs |

## Decision and next gate

### Decided now

- Architecture is a complete capability domain, not the existing five skill names.
- The kernel must be compact and selectively activated.
- Project facts belong in project architecture context.
- Deterministic properties should be checked with appropriate tools.
- High-impact architecture cannot rely on self-certification alone.
- The four candidates enter evaluation; they are not yet skills.

### Not decided now

- final agent count;
- final Architect prompt;
- skill text;
- universal toolchain;
- mandatory notation;
- provider-specific architecture defaults; or
- promotion of any candidate into the v4 runtime.

### Next gate

Run all fixtures relevant to the candidate under A, B, and C. Review blinded outputs. The first runtime artifact may be authored only after three independent result sets demonstrate repeatable improvement and pass every survival gate.

### Pilot 1 status

The first three-scenario A/B/C run for quality-attribute scenarios is complete. The candidate condition won all three blinded comparisons with a 97.00 mean versus 94.00 for the compact kernel. This is preliminary `advance-to-replication` evidence only: its baseline had an active architecture skill, and it does not satisfy the three-independent-result-sets gate.

See [Architecture Capability Pilot 1 — Result](architecture-capability-pilot-1-result.md) for the decoded scores, limitations, and next action. New confirmation tasks use gpt-5.6-luna at max effort.

### Candidate 3 first-run status

The original Candidate 3 first run found a real payment-safety improvement but also activation leakage into the microservices trap. It was revised and retested with fresh A/B/C responses. The revised candidate is `advance-to-replication`: promising, but not approved or installed. See [Candidate 3 — First-Run Result](architecture-capability-candidate-3-first-run.md) and [Candidate 3 — Revised First-Run Result](architecture-capability-candidate-3-revised-run.md) for the evidence, residual risk, and next gate.

### Candidate 4 status

Candidate 4 completed an initial and revised fresh Luna-Max A/B/C run, each with a direct single-company anti-boxing control and blinded review. The candidate remained technically safe but did not beat the compact kernel on the true tenant scenario and still produced irrelevant tenant commentary in unrelated controls. It is `demote-to-reference`, not approved or installed. See [Candidate 4 — Result](architecture-capability-candidate-4-result.md).
