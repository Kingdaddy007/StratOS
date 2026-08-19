# V4 Product-Routing Pilot

**Date:** 2026-08-20  
**Mode:** read-only product framing  
**Scope:** simple notes feature; no project files or external systems

## Observed result

The first Antigravity product-framing response was useful. It produced:

- a clear user problem;
- a small first slice;
- explicit non-goals;
- important unknowns about authentication, persistence, limits, and editing;
- a safe next step before implementation.

The first run also selected too many technical routes too early: API design,
database, coding, UI/UX, and testing were listed before the project stack,
identity model, data boundary, or implementation authority were known. It also
called generic CRUD patterns “evidence” and used high confidence where the
project evidence was still absent.

The second run improved the route. It kept Product & Strategy as the lead and
removed coding, UI, and testing from the active skills. Two issues remained:

- it still named Systems Architecture and a transition to API design before
  context, tenancy, lifecycle, and stack were resolved;
- it still recommended an API contract as the safest next step and reported
  `95%` confidence from generic CRUD conventions.

## V4 correction

The main policy, router, Studio Director, and Product Strategy Lead now state a
technical loading gate:

1. product framing starts with Product Thinking and relevant evidence;
2. technical and design routes enter only for a named decision;
3. implementation routes enter only after implementation or a prototype is in
   scope;
4. missing stack, auth, persistence, design, and acceptance facts stay labelled
   as unknowns;
5. generic SaaS patterns are a starting inference, not project evidence;
6. unresolved context, tenancy, lifecycle, identity, and stack questions come
   before API design; confidence must match the evidence actually checked;
7. a simple framing task uses Product Thinking directly, while research and
   project-inception remain conditional;
8. route reports distinguish available, selected, loaded, and used capabilities.

## Expected next response

For the same notes request, the agent should keep the first response focused on
the product slice and ask for the missing project facts. It may recommend a
later API or schema decision, but it should first resolve the dominant product
unknown. It should not choose `POST /api/notes`, a database model, or an
implementation team before those facts and authority are available.

This is a routing improvement, not proof that the full product studio is better
at building software. A third read-only confirmation and then an authorised
small build pilot are still required.
