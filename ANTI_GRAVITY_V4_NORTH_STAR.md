# Anti-Gravity OS v4 — North Star

**Status:** Draft for research and architectural review  
**Version:** 0.1  
**Purpose:** Define what Anti-Gravity OS v4 is meant to become before deciding which agents, skills, workflows, tools, hooks, references, and existing v3 materials belong in it.

---

## 1. The Plain-English Definition

Anti-Gravity OS v4 is a **personal AI product studio operating system**.

It is designed to help one capable human direct AI like a disciplined, multidisciplinary company: understanding an opportunity, researching it, defining the right product, designing the experience, engineering the system, verifying the result, preparing it for release, positioning it in the market, and learning from the work.

Anti-Gravity is not another AI model. It is the operating structure around capable models.

Its job is to make the difference between:

- having access to powerful AI; and
- knowing how to organise that AI, give it the right context, activate the right expertise, use the right tools, demand the right evidence, and stop weak or unsafe work from being treated as complete.

### One-sentence North Star

> Anti-Gravity OS enables one AI operator to direct a living, evidence-driven product studio that can research, design, engineer, verify, release, and grow exceptional digital products while activating specialist depth only when the work requires it.

---

## 2. Why It Exists

Frontier AI models are increasingly capable out of the box. Access to a strong model alone, however, does not guarantee strong outcomes.

Results still depend on whether the person and system using the model can:

- understand the real problem rather than immediately build the first idea;
- provide current and relevant context;
- distinguish facts from assumptions;
- route work to the right specialisation;
- choose tools and models intelligently;
- preserve product, brand, and architectural coherence;
- verify functionality instead of trusting confident claims;
- control permissions and external effects;
- retain useful lessons without accumulating stale instructions; and
- adapt as models, providers, projects, and best practices change.

Anti-Gravity exists to provide that operating discipline.

---

## 3. Who It Is For

The primary user is an **AI-native product operator**: one person using AI to perform work that would traditionally require a coordinated product, research, design, engineering, quality, release, and growth team.

The initial system is optimised for a single principal operator, not a large organisation.

It must be especially effective for:

- software products and applications;
- websites and digital experiences;
- frontend and backend engineering;
- product discovery and product strategy;
- brand research, positioning, and storytelling;
- high-end cinematic and spatial web experiences;
- AI-assisted image and video production;
- marketing, sales, and prospect intelligence; and
- specialised domain packs added when evidence justifies them.

The architecture may later support teams, but it must not adopt enterprise complexity before a real multi-user requirement exists.

---

## 4. The Outcome Anti-Gravity Seeks

Anti-Gravity should help its user produce work closer to what a disciplined, well-funded, multidisciplinary product company could produce.

It does this by assembling the appropriate process around each task—not by pretending an AI can never make mistakes.

The desired outcome is work that is:

- grounded in the correct problem and user need;
- informed by credible evidence;
- coherent across product, brand, design, and engineering;
- functional across important states and failure paths;
- maintainable and appropriate to the project’s real ambition;
- accessible, secure, reliable, and performant to the required standard;
- verified through observable evidence;
- honest about uncertainty and remaining risk; and
- ready for its intended next step, whether that is prototyping, client review, release, or market activation.

### What “excellent” means

Excellent does not mean adding the most agents, documentation, animation, technology, or ceremony.

Excellent means applying the smallest sufficient combination of expertise, process, tooling, and verification needed to produce a strong result for the actual project.

---

## 5. The Complete Product Lifecycle

Anti-Gravity must be capable of supporting the full journey from raw opportunity to validated learning:

1. **Discover** — Understand the opportunity, user, client, problem, constraints, and available evidence.
2. **Define** — Establish the product thesis, desired outcome, scope, success criteria, and non-goals.
3. **Research** — Investigate the market, users, competitors, technology, brand, domain, references, and risks.
4. **Position** — Determine the product or brand’s distinctive value, story, audience, and proof.
5. **Design** — Shape the information architecture, flows, interaction states, interface, visual system, and optional cinematic experience.
6. **Architect** — Define system boundaries, data ownership, interfaces, failure behaviour, security, operability, and evolution strategy.
7. **Plan** — Break the work into bounded, verifiable milestones with dependencies, ownership, and acceptance criteria.
8. **Build** — Implement the smallest correct slices while preserving project conventions and authorised scope.
9. **Verify** — Test behaviour, states, integrations, accessibility, security, performance, and conformity to the product intent.
10. **Release** — Prepare deployment, rollback, monitoring, documentation, and explicit external approval.
11. **Market** — Create truthful positioning, content, sales material, campaigns, and outreach appropriate to the product and audience.
12. **Learn** — Examine evidence from the project and propose controlled improvements to project context or the OS.

This lifecycle is a capability map, not a mandatory waterfall.

A task may enter at any stage. Anti-Gravity must select only the stages required for that task. A small bug fix must not trigger company-wide ceremony. A high-risk product or architectural decision must not be treated like a small edit.

---

## 6. The Operating Shape

Anti-Gravity should behave as a **small universal studio kernel with optional specialist packs**.

### Universal studio kernel

The kernel supplies capabilities that matter across most serious product work:

- intake and objective clarification;
- product and requirements reasoning;
- research and evidence handling;
- system architecture;
- implementation and debugging;
- product design and usability;
- quality, security, and verification;
- release discipline;
- context and knowledge management; and
- controlled learning.

### Optional specialist packs

Specialist packs are activated only when the project qualifies for them. Initial candidates include:

- spatial and cinematic web experiences;
- interior, architecture, furniture, showroom, and luxury-brand experiences;
- expert positioning, brand strategy, and storytelling;
- image and video generation, including provider-specific capabilities;
- sales, prospect intelligence, and controlled outreach;
- other specialised product domains; and
- provider/tool integrations whose value depends on current availability.

Provider-specific knowledge must remain separable from durable domain knowledge so that a provider can be replaced without rewriting the OS.

---

## 7. Generalist and Specialist Principle

Anti-Gravity is not a shallow generalist and not a permanently overloaded specialist.

It should:

1. begin with a compact understanding of the request;
2. determine the task’s domain, stakes, uncertainty, and effect level;
3. activate the smallest capable role or team;
4. load only the knowledge and tools required;
5. delegate only when specialisation, independence, context isolation, or parallelism creates real value; and
6. return one coherent result with evidence.

The OS must never activate a specialist merely because the specialist exists.

---

## 8. Agents, Skills, Workflows, Tools, and Hooks

These components serve different purposes and must not be confused.

| Component | Responsibility |
| --- | --- |
| **Agent** | Owns a role, responsibility, effect ceiling, allowed tools, and delegation boundary |
| **Skill** | Supplies focused specialist knowledge or a proven decision procedure when relevant |
| **Workflow** | Defines a repeatable ordered process where sequence, state, or approval matters |
| **Tool or script** | Performs or validates a concrete operation |
| **Hook** | Deterministically intercepts lifecycle or tool events to enforce a rule or collect evidence |
| **Reference** | Supplies detailed, dated, or specialised information on demand |
| **Context** | Describes current project truth, constraints, decisions, and unknowns |
| **Memory** | Preserves sanitised, durable lessons that remain useful beyond one project |

### Agent principle

An agent is valuable only when the role creates a meaningful boundary in responsibility, tools, context, authority, or independent judgement.

A named persona without a real boundary is not architecture.

### Delegation principle

Delegation is conditional, not mandatory.

An agent should delegate when one or more of the following is true:

- the task benefits from independent verification;
- specialist knowledge or tools are required;
- parallel work materially improves delivery;
- the work needs an isolated context or worktree; or
- separating ownership reduces risk.

For small or tightly coupled work, the responsible agent may execute directly.

---

## 9. Provisional Capability Departments

These are capability areas to research, not a final commitment to a specific number of custom agents.

1. **Direction and Delivery** — intake, routing, scoping, coordination, and final synthesis.
2. **Product and Research** — opportunity understanding, user needs, market evidence, requirements, and success criteria.
3. **Systems Architecture** — boundaries, interfaces, data, reliability, security architecture, operability, and evolution.
4. **Engineering** — implementation, debugging, refactoring, integration, and local verification.
5. **Product Design** — general UI/UX, information architecture, accessibility, interaction states, and visual systems.
6. **Quality and Security** — independent behavioural, security, accessibility, performance, and evidence-based assurance.
7. **Release and Operations** — dependencies, infrastructure, deployment preparation, rollback, and monitoring.
8. **Brand and Growth** — positioning, storytelling, copy, marketing, sales, prospect intelligence, and campaigns.
9. **Knowledge and Learning** — context hygiene, documentation, source provenance, memory, and controlled improvement proposals.
10. **Optional Creative Studios** — spatial, cinematic, motion, image, and video specialisations.

Research and evaluation must determine whether each area becomes an agent, a responsibility shared by another agent, an optional pack, or no custom component at all.

---

## 10. Quality and Completion

Anti-Gravity must never equate confidence, documentation volume, or agent agreement with correctness.

A meaningful completion claim should identify:

- what objective was pursued;
- what changed;
- what evidence was inspected;
- what tests or checks were run;
- what passed and failed;
- what was not tested;
- what assumptions remain;
- what residual risks remain; and
- whether any external action still requires approval.

### Professional-quality principle

Anti-Gravity cannot promise zero defects. It must instead maximise defensible release confidence and make uncertainty visible.

When time or budget is constrained, reduce scope before sacrificing essential correctness, safety, or verification.

---

## 11. Evidence and Research

Research exists to improve a decision, not to produce impressive reports.

Anti-Gravity must:

- distinguish primary evidence, credible secondary analysis, practitioner opinion, and inference;
- prefer current primary sources for platform, API, legal, security, and provider-specific claims;
- record source URLs and verification dates for unstable knowledge;
- state conflicts between credible sources;
- report when evidence is weak or missing;
- avoid converting popularity into authority; and
- test important recommendations where research alone cannot resolve the question.

Independent research from multiple models should be compared claim by claim. Agreement between models is not proof if the models rely on the same weak source or repeat the same assumption.

---

## 12. The Skill Survival Standard

A custom skill must earn its place.

It should survive only when it contributes one or more of the following:

- specialist knowledge a capable model cannot reliably reproduce;
- a deterministic script, validator, template, or tool;
- a project-specific or domain-specific contract;
- a proven procedure that prevents an expensive recurring failure;
- an important security, legal, financial, or safety boundary;
- a distinctive creative method that demonstrably improves outcomes; or
- a current provider-specific capability that cannot be safely discovered at execution time.

A skill should be rejected, merged, or demoted when it merely:

- tells the model to think carefully;
- repeats common professional advice;
- describes a role better represented by an agent;
- duplicates another capability under different branding;
- forces one technique without regard to project context;
- contains stale provider claims; or
- adds more context than value.

### Anti-boxing evaluation

Important capabilities must be compared under at least three conditions:

1. capable model without Anti-Gravity customisation;
2. capable model with only the compact Anti-Gravity kernel; and
3. capable model with the kernel plus the candidate capability.

The custom capability survives only when it produces meaningful improvement without introducing unacceptable rigidity, cost, confusion, or regressions.

---

## 13. Learning Without Self-Corruption

Anti-Gravity should become better through use, but it must not silently rewrite its governing system.

The learning loop is:

1. observe a possible lesson during a project;
2. preserve the evidence and context;
3. classify the lesson;
4. determine whether it is project-specific, temporary, provider-specific, or globally durable;
5. sanitise private and untrusted material;
6. propose a change;
7. run relevant regression evaluations;
8. request human review when the change affects global behaviour; and
9. release the accepted change as a versioned, reversible update.

### Learning destinations

| Lesson type | Destination |
| --- | --- |
| Current project fact | Project context |
| Project-specific decision | Project decision record or memory |
| Temporary workaround | Dated project note |
| Provider-specific discovery | Dated provider reference |
| Durable cross-project lesson | Proposed global OS change after evaluation |
| Unverified observation | Evidence backlog; not active memory |

No agent, workflow, website, tool output, or reference may grant itself authority by writing into memory or policy.

---

## 14. Context, Memory, and Client Separation

Anti-Gravity must preserve clear boundaries between:

- global OS policy;
- the operator’s preferences;
- reusable cross-project learning;
- the current workspace;
- the current client or brand;
- task-specific evidence; and
- untrusted external material.

Client research, strategy, private information, credentials, and creative direction must not leak into another project or global memory.

Active project truth belongs with the project. Global memory must contain only sanitised lessons that are genuinely reusable.

---

## 15. Authority and External Effects

Anti-Gravity remains subordinate to platform, developer, organisation, user, and workspace authority.

It must distinguish:

- read-only investigation;
- proposals;
- scoped local edits;
- dependency or network effects;
- destructive actions; and
- external or production actions.

Research, drafting, analysis, and local verification may be highly autonomous inside the user’s authorised scope.

The following require explicit, just-in-time authorisation unless a higher-authority host mechanism already governs them:

- destructive deletion;
- history rewriting;
- pushing or publishing;
- deployment and rollback;
- production data or traffic changes;
- sending messages or outreach;
- posting marketing content;
- purchases or paid model actions;
- credential changes; and
- other material effects on external people or systems.

Delegation never expands permission. A child agent inherits or narrows its parent’s authority.

---

## 16. Model, Tool, and Provider Independence

Anti-Gravity should benefit from improving models rather than fighting them.

The canonical OS should describe capabilities, responsibilities, evidence, and effects in provider-neutral language. Host adapters should translate those contracts into the supported forms for Antigravity, Codex, and future hosts.

Provider-specific packs may define current details for tools such as image generators, video generators, browser systems, infrastructure providers, and commercial platforms. These packs must be removable and replaceable without changing the OS kernel.

The OS should use the strongest appropriate available capability, but it must also account for cost, latency, quota, privacy, and the task’s actual stakes.

---

## 17. What Anti-Gravity Must Never Become

Anti-Gravity must not become:

- a giant always-loaded prompt;
- a collection of fashionable skills without measured value;
- a role-playing company where agents exist only to give work impressive titles;
- an autonomous system that can expand its own authority;
- a self-editing instruction base that accumulates unreviewed lessons;
- a spatial or cinematic design system forced onto every project;
- a provider-specific system that breaks when one vendor changes;
- a waterfall that sends every small task through every department;
- a documentation factory that confuses volume with quality;
- a claim of guaranteed perfection;
- an enterprise orchestration platform without an enterprise requirement; or
- a replacement for the user’s judgement, intent, and final authority.

---

## 18. Success Measures

Anti-Gravity v4 is successful when evidence shows that it:

- improves correctness and completeness over a capable model used without the OS;
- catches important mistakes before delivery;
- preserves product and brand coherence across long projects;
- activates relevant specialist depth without polluting unrelated work;
- reduces unsupported completion claims;
- makes assumptions, tests, and residual risks visible;
- routes tasks correctly with minimal unnecessary ceremony;
- prevents unauthorised destructive or external actions;
- enables safe parallel work without conflicting edits or lost state;
- remains understandable and maintainable by its operator;
- adapts to model and provider changes without complete reconstruction; and
- retires components that no longer provide measurable value.

Metrics may include task success, defect discovery, verification coverage, routing accuracy, context cost, tool-call cost, latency, unnecessary-agent activation, user intervention, regression rate, and capability usage.

---

## 19. Research and Build Order

Anti-Gravity v4 should be developed in this order:

1. Approve this North Star and its non-goals.
2. Correct the existing v4 architecture blueprint against the approved North Star and official host documentation.
3. Define the capability-discovery and evaluation method.
4. Research each major capability domain from first principles using independent sources and models.
5. Build a canonical capability map before deciding the final skill or agent inventory.
6. Compare the clean capability map with existing v3 material.
7. Classify existing material as retain, consolidate, rewrite, optional, archive, delete, or replace.
8. Create a small vertical slice with a compact kernel and the minimum useful agent roster.
9. Add deterministic hooks and adversarial tests for important effect boundaries.
10. Compare model-only, kernel-only, and kernel-plus-capability performance.
11. Expand agents and specialist packs only when evidence justifies them.
12. Generate and validate native Antigravity and portable Codex payloads from one canonical source.
13. Shadow-test v4 against v3 before installation or cutover.
14. Preserve a reversible rollback path for at least one compatibility release.

---

## 20. Decisions Still Open

This North Star deliberately does not decide:

- the final product name or whether `StratOS` replaces `Anti-Gravity`;
- the final number of agents;
- the final skill inventory;
- the final workflow inventory;
- which provider integrations belong in the initial release;
- whether commercial capabilities ship as one pack or several;
- exact model-routing policy;
- whether v4 remains personal-only or later supports teams; or
- the public licensing and distribution model.

Those decisions require research, evaluation, or explicit user approval.

---

## 21. The Final Test

Every proposed v4 component must answer four questions:

1. What important problem does this solve?
2. Why can a capable model not handle it reliably without this component?
3. What evidence will prove that the component improves the outcome?
4. What cost, constraint, or failure mode does the component introduce?

If those questions cannot be answered, the component does not yet deserve a place in Anti-Gravity OS v4.

---

## North-Star Commitment

> Build an operating system that amplifies capable models through context, specialisation, evidence, tools, verification, and controlled learning—without reducing their intelligence to rigid instructions or replacing the human who owns the goal.
