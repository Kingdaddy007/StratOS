# UI Operation Routing

Treat the following names as direct UI/UX task modes. They are not separate workflows, do not create task state, and never trigger an automatic chain of work. Match the requested outcome, load only the relevant UI/UX references, and keep the scope and authority of the underlying task. Load `interface-operation-playbook.md` only when the named operation needs a detailed procedure.

| Requested operation | Route and evidence |
| --- | --- |
| adapt or harden | Load `responsive-design.md`; define or verify reflow, content priority, touch targets, narrow-view behavior, resilient content, and safe visible recovery. |
| audit or critique | Load `heuristics-scoring.md` and `design-bans.md`; inspect the actual interface when it exists. Report evidence, severity, and limits. Use independent review only when risk warrants it. |
| bolder, quieter, distill, polish, delight, or overdrive | Establish the user goal and active register first. Adjust hierarchy, density, visual emphasis, or purposeful feedback without weakening clarity, accessibility, or the existing brand. Do not manufacture spectacle or redesign unrelated work. |
| clarify | Load `ux-writing.md`; improve labels, instructions, error states, and confirmations using observed user and product context. |
| colorize | Load `color-and-contrast.md`; preserve existing tokens unless change is authorized and verify contrast in the relevant states. |
| layout | Load `product.md` or `brand.md` as applicable; correct information hierarchy, grouping, scanning order, and responsive composition. |
| typeset | Load `typography.md`; correct hierarchy, measure, legibility, and responsive behavior. Do not choose fonts by trend. |
| shape | Identify the user goal, critical journey, information hierarchy, and applicable state matrix. Produce a proportionate design brief or begin the approved design task. |
| document or extract | Capture only requested, evidence-backed design decisions, reusable patterns, or tokens in the project’s established location. Do not create competing design truth files. |
| live | Use the available browser or local preview to inspect a bounded change. Do not assume hot reload, element selection, or automatic file mutation exists. |
| onboard | Load `product.md` and `cognitive-load.md`; design the smallest clear path to activation, recovery, and continued use. |
| optimize | Route measured performance work to the performance capability; retain UI/UX work for perceived responsiveness, clarity, and recoverable loading states. |
| teach | Make assumptions, decisions, and trade-offs legible in the deliverable. Do not turn a design task into an unsolicited tutorial. |

## Boundaries

- Use `workflow-design-ui.md` for a coordinated design effort that needs a handoff or a durable design decision.
- Use direct `ui-ux` with `coding` when an approved interface needs local implementation.
- Load `motion-design.md` only when a product interaction needs purposeful motion and reduced-motion verification.
- Keep spatial cinematic direction in the spatial profile. Do not import it into a general product interface by default.
- A named operation never grants editing, dependency, external, or production authority.
