---
name: architecture
description: 'Use when making a structural software decision: system boundaries, state/data ownership, component interfaces, service topology, migration/recovery shape, major framework choice, or scaling failure. Trigger phrases include "design the architecture", "should this be a microservice?", "how should data flow?", "service boundaries", "how should I structure this?", or "this system does not scale". Do NOT use for a small local implementation with an existing contract; use coding. Do NOT use for a narrow bug diagnosis before its scope is understood; use debugging.'
---

# SOFTWARE ARCHITECTURE & SYSTEM DESIGN

## WHEN TO USE THIS

- Initializing a new project, service, or major feature
- Designing data flow between multiple components
- Breaking apart a legacy monolith or splitting services
- Defining folder structures and project organization
- Evaluating core technology or framework choices
- When current systems fail to scale under anticipated load

## NEVER DO

- Commit to a material structural change before the relevant data ownership, interfaces, and boundaries are understood
- Create circular dependencies
- Build abstractions for imagined future use cases without explicit scaling requirements
- Let the database schema be dictated by the UI rather than the domain
- Choose a technology simply because it is trendy, without a performance or maintenance justification
- Let a single failure take down the entire application by design
- Choose a topology because it is fashionable, or because it is "enterprise", rather than because real requirements and failure costs justify it
- Make the final architecture decision without surfacing options and tradeoffs to the user first

---

## MINDSET

**Architecture must match the Ambition.** While simplicity is a virtue, great systems often require sophisticated structures to handle scale, reliability, and client expectations.

Expert software architecture is about establishing rigid boundaries, defining clean seams, and managing continuous tradeoffs. There is no perfect architecture — only optimal compromises based on the project's real scale, budget, and context.

Focus on John Ousterhout's concept of "deep modules" — interfaces that are exceptionally simple but hide massive internal complexity. Evaluate every design against the **2 AM test**: how will the system fail, and can a mid-level engineer diagnose it without the original creator?

**Right-sizing principle:** The correct architecture is the simplest one that genuinely meets the real requirements — not the simplest one by default. Simple is the starting point for evaluation, not the ceiling. Artificially capping complexity to stay "safe" is just as bad as adding complexity without reason.

**Client context:** the user builds platforms and products for clients, not just for himself. Client requirements may include high availability, data isolation, multi-tenancy, regulatory compliance, and scale that a personal project would never need. Always assess who this is for, what it needs to survive, and what failure costs the client.

**Decision authority:** Anti-Gravity's role is to present the full architecture landscape — options, tradeoffs, risks, and a clear recommendation. the user makes the final call. Never silently narrow the options or present only one path as if no choice exists.

---

## DECISION FRAMEWORK

| Architectural Axis | Evaluation Focus | Resolution Strategy |
| :--- | :--- | :--- |
| **Performance vs. Scalability** | CPU/memory efficiency vs. ability to handle massive concurrent loads | Optimize vertically for latency; scale horizontally for traffic spikes |
| **Simplicity vs. Ambition** | Ease of understanding versus capability needed for real scale, reliability, or compliance | Compare only viable options. Recommend the smallest option that meets the requirements and name the triggers that would justify more complexity. |
| **Consistency vs. Availability** | Consistency/availability trade-offs when data is replicated or a network partition is plausible | Define the required correctness model and failure behaviour. Discuss eventual consistency only where asynchronous or distributed writes are real. |
| **Build vs. Buy** | Custom control vs. speed of integration and maintenance offloading | Build core differentiators. Buy commodity capabilities (auth, email, generic search). |

---

## ARCHITECTURAL LENSES

Apply the relevant lenses before and during design. Use all ten for a consequential or irreversible architecture decision; do not pretend every local change needs a full-system review.

### 1. Purpose and Quality Attributes

- What is the system trying to achieve?
- What matters most: speed of delivery, reliability, scale, compliance, simplicity, flexibility?
- Which non-functional requirements truly matter here?

### 2. Responsibilities and Boundaries

- What are the major responsibilities? How should they be separated?
- Where should one module or service end and another begin?

### 3. Ownership

- Who owns what data, behavior, and operational responsibility?
- Is ownership explicit or implied? Are multiple components mutating the same truth unsafely?

### 4. Data Flow

- How does information move through the system?
- Where are the write paths, read paths, async flows, and control points?
- Are the flows visible and understandable?

### 5. Coupling and Cohesion

- Are related behaviors kept together? Are unrelated concerns entangled?
- Will common changes land cleanly within one boundary or spray across many?
- **The Deletion Test:** If you delete a module and all its complexity vanishes, the module was a pass-through. If its complexity scatters into N caller sites, the module was earning its keep.

### 6. Failure Behavior

- How does the design degrade when a dependency fails?
- Can the system isolate failure, retry safely, or fall back gracefully?

### 7. Reversibility and Migration Cost

- How expensive is it to change this later? Are we locking into a hard-to-reverse structure too early?
- Can this be staged incrementally?

### 8. Observability and Operability

- Can we see what the system is doing?
- Are logs, metrics, traces, health checks, and ownership paths obvious enough for operation and debugging?

### 9. Change Surface

- Which parts will change most often?
- Does the design localize those changes or spread them widely?

### 10. Appropriate Complexity

- Is the architecture matching the client's ambition and the project's real-world scale?
- Are we under-engineering a system that needs high-availability, or over-engineering a simple CRUD app?
- Present options that allow for Greatness — not just "good enough."

---

## BEHAVIORAL WORKFLOW

### Step 1 — Define the Reality

- Define exact business requirements and domain metrics.
- Define expected scale (throughput, latency, payload size, data volume) when it could change the architecture.
- Apply the "What would have to be true?" test to force objective evaluation of prerequisites.

### Step 2 — Map the Data Flow

- Data is the center of gravity. Map how it enters, transforms, persists, and exits the system.
- Determine which component "owns" which piece of state.
- Define how state changes are communicated (synchronous calls vs asynchronous events).

### Step 3 — Draw the Boundaries

- Draft module/service boundaries based on domain concepts, not technical layers.
- Ensure high cohesion (things that change together, live together).
- Ensure low coupling (modules interact through stable, minimal interfaces).
- Explicitly reject cyclical dependencies.

### Step 4 — Design the Interfaces (Deep Modules)

- Minimize the surface area of the API/interface.
- Maximize the internal functionality hidden behind that API.
- Ensure the interface speaks the language of the domain, not the language of the underlying implementation.

### Step 4.5 — Design It Twice (Interface Evaluation)

- Your first architectural draft is rarely your best. Force parallel explorations before finalizing code boundaries.
- Sketch a Minimalist interface (1-3 entry points), a Flexible interface (high configuration), and a Default-focused interface.
- Compare them on depth, locality, and seam placement. Pick the one that provides the most leverage.

### Step 5 — Map Failure Domains

- Define the "Blast Radius": if Component A fails, does Component B fail?
- Define the exact degradation paths for when dependencies become unavailable.
- Ensure the system degrades gracefully rather than failing catastrophically.

### Step 6 — Select Technology Stack

Compare only the options that are credible for the actual project. For each, explain operational cost, maintenance burden, failure behaviour, reversibility, and the requirement it satisfies. Recommend the smallest sufficient option and name the concrete trigger that would justify a more complex one.

Explain why a complex choice such as a distributed database or event stream is justified only when evidence requires it. Make a clear recommendation and surface material trade-offs to the user before an irreversible commitment.

### Step 7 — Document Tradeoffs

- Write down what was sacrificed to achieve this design.
- Document rejected alternatives and exactly why they were rejected.

### Step 8 — Before Finalizing, Re-check

- Is the chosen boundary the right one?
- Is ownership and contract clarity verified?
- What does the system optimize for?
- How does this fail?
- What is the reversibility and cost of change?
- Is the design more or less complex than the real requirements justify?
- What should trigger architectural re-evaluation later?

---

## KEY DIAGNOSTIC QUESTIONS

- **2 AM Test:** Can a developer who did not build this debug it during an outage without calling the original creator?
- **Fit Test:** What is the simplest architecture that *genuinely* meets the real requirements? Is there a case where a more capable architecture is actually the correct fit?
- **Client Reality Test:** Who is this being built for? What does failure cost them? What are their actual scale, availability, and compliance requirements?
- **Options Test:** Have we presented the viable alternatives and their material trade-offs, without inventing a complex option for show?
- **Replacement Test:** If we need to rewrite this specific component in two years, how many other components will we have to change?
- **Degradation Test:** If the primary database (or third-party API) fails, how exactly does the application behave, and what is the user experience?
- **State Test:** Is there a single source of truth for this data, or is it scattered and requiring complex synchronization?
- **Longevity Test:** What would force us to revisit this design in 6–12 months, and are we designing with that pressure in mind?
- **Decision Test:** Have all viable options been presented with honest tradeoffs? Has the user been given the final choice?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| :--- | :--- | :--- | :--- |
| **Resume-Driven Development** | Using complex tech for the sake of it, without scale justification | Massive operational overhead without performance gain | Present the simple path as baseline; use complex tech only when requirements justify the cost |
| **Complexity Aversion** | Defaulting to the simplest architecture even when real client scale or compliance demands more | Under-engineered systems fail at the wrong moment; retrofitting is expensive | Assess real requirements first. If complexity is justified, recommend it — don't suppress it |
| **Silent Narrowing** | Presenting only one architecture option as if no other viable path exists | Removes the user's ability to make an informed decision | Always present Simple, Balanced, and Enterprise paths; make a recommendation; let the user choose |
| **Shallow Modules** | An interface that requires 15 configuration parameters to initialize, or a class that simply delegates all its calls to a repository without adding logic | No cognitive relief; complexity scales linearly with codebase size; fails the deletion test | Push complexity downward. The interface should offer a simple abstraction that hides the difficult mechanics. |
| **Distributed Monolith** | Microservices that share a single database, or services that must be deployed simultaneously | All the operational complexity of microservices with none of the independence or fault isolation benefits | Redraw boundaries based on domain contexts. Use async communication between boundaries |
| **Premature Generalization** | Building an "Entity Management Engine" instead of the specific User and Order tables needed today | Future requirements are usually guessed wrong; the generalized system handles the actual present clumsily | YAGNI. Build exactly what is needed today. Refactor when the third concrete use case arrives |

---

## OUTPUT SHAPE

```markdown
## Objective & Scale

What are we building, for whom, and at what anticipated volume/throughput?

## System Boundaries & Components

Definition of the major modules, what they own, and what they do not own.

## Data Flow & State Ownership

How data enters, moves, and rests. Which component is the Source of Truth.

## Interface Design (Deep Modules)

How the components communicate (APIs, events, contracts).

## Options & Tradeoffs

| Option    | Pros | Cons | Recommendation |
| :-------- | :--- | :--- | :------------- |
| Simple    | ...  | ...  | ...            |
| Balanced  | ...  | ...  | ...            |
| Enterprise| ...  | ...  | ...            |

## Failure Modes & Degradation

What happens when dependencies fail, and how the system degrades safely.

## Decisions Log

Explicit recording of technology choices and accepted technical debt.
```

---

## NON-NEGOTIABLE CHECKLIST

- [ ] Known business requirements and expected scale are stated where they change the decision
- [ ] Client context established — who this is for and what failure costs them
- [ ] Relevant viable alternatives and trade-offs are presented for a consequential decision
- [ ] Module boundaries strictly defined with zero cyclical dependencies
- [ ] Data flow and state ownership explicitly mapped
- [ ] Interface (API) is simpler than the implementation (Deep Module)
- [ ] Failure modes and degradation paths defined
- [ ] Distributed consistency, availability, and recovery trade-offs are documented when the architecture actually has replicated or partition-prone state
- [ ] Rejected alternatives documented with reasons for rejection
- [ ] the user has been given the final decision
