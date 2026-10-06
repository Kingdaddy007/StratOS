---
name: to-tickets
description: 'Use when the task requires to tickets guidance. Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (e.g. tickets.md or GitHub/Linear issues). Signal phrases: "break into tickets", "create issues", "vertical slices", "tracer bullets", "expand-contract migration", "generate tickets". Always seek user verification on ticket granularity and blocking dependencies.'
---

# TO TICKETS

## WHEN TO USE THIS

- Splitting a large spec or PRD into actionable chunks.
- Slicing work into vertical tracer bullets.
- Planning a wide refactor using the expand-contract strategy.
- Initializing a development sprint with clean issue definitions.

## NEVER DO

- Never create horizontal slices (e.g. "implement database", "implement UI") — every ticket must be a vertical tracer bullet.
- Never write tickets with vague or untestable acceptance criteria.
- Never hardcode file paths or line numbers in ticket descriptions (unless referring to prototype decisions).
- Never publish tickets without verify-gates or checking dependency edges.

---

## MINDSET

You are a master planner who slices complexity into independent, demoable steps.
- **Vertical Tracer Bullets:** Every ticket should cut through all layers (schema, API, UI, tests) so it is verifiable on its own.
- **Frontier Management:** Always identify which tickets block which, maintaining a clean "frontier" of tasks that can start immediately.
- **Expand-Contract:** For wide refactors that would otherwise break compilation across the app, add the new form alongside the old, migrate in batches, and then delete the old form. Keep CI green throughout.

---

## DECISION FRAMEWORK — 6 PRIORITIES (IN ORDER)

### Priority 1 — Slicing Direction
Ensure each ticket is a vertical slice. No single-layer tickets. A completed ticket must add observable value or behavior.

### Priority 2 — Dependency Hygiene
Ensure blocking links represent true gates. A ticket should only block another if it is physically impossible to start the second without the first.

### Priority 3 — Context Capacity
Scale each ticket so its implementation fits comfortably within a single, clean LLM context window.

### Priority 4 — Prefactoring
Always sequence "making the change easy" (prefactoring) before "making the easy change."

### Priority 5 — Verification Design
Every ticket must contain concrete, testable acceptance criteria that can be checked by an automated script or runner.

### Priority 6 — Tracker Integration
Publish in the format required by the repo (e.g. `tickets.md` locally or issues on a remote tracker).

---

## CORE PRINCIPLES

1. **Tracer Bullets, Not Layers.** Build thin vertical slices. Verify end-to-end behavior at every step.
2. **Make it Easy First.** Prefactor code in separate tickets before building new behavior.
3. **CI Must Stay Green.** Never commit a ticket that leaves the master branch broken.
4. **Clean Boundaries.** Clearly outline what is out of scope for each ticket to prevent gold-plating.

---

## TO TICKETS LENSES

| Lens | What to Inspect |
| --- | --- |
| **Slice Lens** | Does this ticket touch schema, API, UI, and tests? Is it demoable? |
| **Blast Radius** | Does this change break compilation? If yes, apply expand-contract sequence. |
| **Context Window** | Can this be implemented without exceeding ~50k-100k context tokens? |

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Understand & Gather Context
Gather the spec, PRD, or conversation context. Review the codebase to understand the current architecture and domain vocabulary.

### Phase 2 — Contextualize
Identify the target issue tracker configuration from the project contract or supplied ticket file; local Markdown is sufficient. Respect relevant ADRs. Follow `GLOSSARY-MAP.md` to the relevant `GLOSSARY.md` when present; use an existing authoritative legacy domain `CONTEXT.md` during migration. Keep broader project truth in `.agents/contexts/`. Do not rename documents or infer remote publication permission from tracker configuration.

### Phase 3 — Analyze
Draft the list of tickets. Group them by category: prefactoring, vertical slices, or expand-contract migration phases.
Identify blocking relationships: which tickets must be resolved before this one can start?

### Phase 4 — Plan
Structure the proposed list of tickets. For each ticket, define:
- Title
- Blocked by (dependencies)
- What it delivers (user-facing value)
- Acceptance criteria (verifiable checks)

### Phase 5 — Critique & Review (Quiz the User)
Present the list to the user. Ask:
1. Does the granularity feel right?
2. Are the blocking edges correct?
3. Should any tickets be merged or split further?
Iterate based on feedback.

### Phase 6 — Publish
Write to the configured tracker:
- **Local:** Generate a `tickets.md` file in the repo root following the template below.
- **Remote:** Use API commands to create issues in dependency order, linking them with blocking relationships.

Publish to a remote tracker only when that external effect is authorized. Otherwise return reviewable local ticket content. When the user requests implementation of the approved spec and tickets, use [implement-spec](../implement-spec/SKILL.md); ticket planning alone does not authorize implementation.

---

## KEY DIAGNOSTIC QUESTIONS

- Does this ticket deliver a verifiable end-to-end behavior?
- Is this a horizontal slice that will leave the build broken or undemoable?
- Are the blocking dependencies true gates?
- Can this work be completed in one session?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **Horizontal Layering** | Creating a "Database schema" ticket followed by a "REST API" ticket. | Undemoable steps; bugs are only caught late at integration. | Combine layers into a single vertical slice that does one thing end-to-end. |
| **The Blast-Radius Bomb** | Modifying a shared symbol across the codebase in a single massive ticket. | Leaves the project broken for days and causes merge hell. | Sequence as expand-contract: add new, migrate in batches, contract. |
| **Loose Criteria** | Acceptance criteria like "Make it work." | The developer/agent doesn't know when they are done. | Write testable, binary (yes/no) criteria. |

---

## OUTPUT SHAPE

### Local tickets.md Template

```markdown
# Tickets: [Short Name]

A one-line summary of what these tickets build.

## Ticket 1: [Title]
**What to build:** [Describe the user-facing behavior]
**Blocked by:** None

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

## Ticket 2: [Title]
**What to build:** [Describe the behavior]
**Blocked by:** Ticket 1: [Title]

- [ ] Acceptance criterion 1
```

---

## NON-NEGOTIABLE CHECKLIST

- [ ] Every ticket is a vertical slice (or a defined prefactoring/expand-contract step)
- [ ] Dependency links (Blocked by) are explicitly declared
- [ ] Every ticket has clear, binary acceptance criteria
- [ ] Out of scope items are clearly separated
- [ ] Tracker formatting matches the target environment

---

**Final Rule:** A ticket is a contract of done. If you cannot describe how to verify a ticket in three checkboxes, the ticket is not ready.
