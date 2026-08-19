# V4 Delivery and Assurance Asset Decision Ledger

**Status:** Batch B - decision design only; no source asset changed  
**Date:** 2026-08-18  
**Scope:** Design Direction, Staff Engineering, and Assurance & Quality.  
**Out of scope:** optional-pack classification, source rewrites, installation, adapters, or generated payloads.

## The operating rule

These three functions are collaborators, not a waterfall and not three permanent chat rooms.

```text
Product / Architecture handoff
             |
             +--> Design Direction: make the experience usable and intelligible
             |
             +--> Staff Engineering: build the approved, risk-sized slice
             |
             +--> Assurance: test/review claims independently when risk warrants it
```

The arrows can loop. Staff Engineering can ask Design for a missing state. Design can surface a technical constraint. Assurance can stop a risky claim, but it does not own product strategy or rewrite another lead's work.

Every function performs its own self-check. Independent Assurance is activated for material risk, high uncertainty, release readiness, security-sensitive change, recurring failure, or a claim that needs separate evidence.

## Decision vocabulary

| Decision | Meaning |
| --- | --- |
| **Keep and re-home** | Preserve the asset and give it a clear V4 functional owner or route level. |
| **Strengthen** | Preserve the core, then make a focused improvement in a later source-edit batch. |
| **Consolidate** | Reduce duplicate routes or instructions without losing specialist knowledge. |
| **Re-profile** | Keep the capability, but move it behind a narrower procedure or optional pack. |
| **Defer** | Leave untouched until a concrete project or later asset batch justifies a decision. |

## A. Design Direction

| Asset | V4 owner | Decision | Reason | Future source-edit objective |
| --- | --- | --- | --- | --- |
| `skills/ui-ux` | Design Direction | **Keep and re-home** | It is already a concise general design skill covering flows, state, interaction, responsiveness, accessibility, and verification | Make it the primary general-design contract and ensure spatial references remain conditional |
| `skills/color-system` | Design Direction procedure | **Keep; scope-check later** | It can improve visual hierarchy and accessibility, but it is not a mandatory step for every interface | Keep colour decisions attached to a real brand, system, or usability question rather than generic "colour psychology" |
| `skills/scroll-storyboard` | Design Direction procedure | **Keep and re-profile** | Its activation boundary is already narrow and sound | Keep it conditional on an approved authored scroll experience, never universal page design |
| `skills/apply-transition` | Tool-backed design helper | **Consolidate or re-profile** | It is a narrow integration recipe for one transition library, not a design authority | Move it out of core discovery or convert it to a small implementation reference; confirm tool/library freshness before any update |
| `workflow-design-ui` | Design Department procedure | **Strengthen and reduce** | It contains useful UI design work but gives the legacy Impeccable system a competing ownership claim | Recast it under the Design Director with a clear flow, state, accessibility, and implementation handoff; remove competing authority language |
| `workflow-ui-craft` | Shared Design/Staff procedure | **Keep and re-home** | It correctly begins after an approved flow and state contract | Keep it as a build procedure, not a substitute for design direction or architecture |
| `workflow-ui-animate` | Design Department procedure | **Keep and re-profile** | Its scope is general product motion with usability, accessibility, and performance constraints | Require a communication or interaction job; motion remains optional |
| `workflow-impeccable-*` (23 procedures) | Design Department source collection | **Preserve, consolidate, and remove from universal routing** | The material is valuable, but 23 equal top-level routes create false complexity and compete with the Design Director | Group them behind a smaller Design procedure surface; preserve specialised recipes and evidence as references rather than delete them |
| `workflow-impeccable-audit` and `workflow-impeccable-critique` | Design/Assurance collaboration | **Keep; re-home later** | They are useful design-quality inputs but must not become a rival operating system | Define when Design requests them and when Assurance independently verifies implementation evidence |
| Design and UI context templates | Project truth scaffolds | **Keep; audit for size later** | They contain valuable prompts but must not become an always-loaded fictional project context | Separate blank project fields, durable standards, and deep reference material |

### Design Direction acceptance test before editing

The future design route should produce an implementable handoff when the task merits one:

```text
User and task | information/flow | states and edge cases | interaction rules | visual system | accessibility/responsive constraints | evidence to verify
```

For a small UI change, this can be a short note or direct implementation. A full product or critical flow earns the full handoff. Spatial, cinematic, and video design remain optional packs, not a default visual style.

## B. Staff Engineering

| Asset | V4 owner | Decision | Reason | Future source-edit objective |
| --- | --- | --- | --- | --- |
| `skills/coding` | Staff Engineering | **Keep and re-home** | It covers implementation, boundaries, error handling, and verification without prescribing a stack | Connect it to explicit incoming contracts and a concise implementation/evidence handoff |
| `skills/debugging` | Staff Engineering, escalated to Systems Architecture for systemic/production issues | **Keep** | It is evidence-first and separates symptom, hypotheses, root cause, fix, and regression protection | Preserve diagnosis-only behaviour and ensure production incidents route to the hard incident gate |
| `skills/refactoring` | Staff Engineering | **Keep** | It correctly protects behaviour before structural improvement | Retain behaviour lock, bounded scope, reversibility, and regression proof |
| `skills/resolving-merge-conflicts` | Staff Engineering procedure | **Keep and re-profile** | It is a real specialist procedure, but not a general delivery capability | Keep it discoverable only during an actual merge/rebase conflict; retain its no-abort-without-consent boundary |
| `skills/setup-pre-commit` | Environment/setup procedure | **Re-profile** | It names a specific implementation and may install dependencies or alter repository configuration | Keep it as a conditional setup recipe with explicit environment-mutation approval; do not make it a default build step |
| `workflow-build-feature` | Studio Route, executed by Staff Engineering | **Strengthen and reduce** | It has valuable implementation/verification gates but is overlong for common work | Recast it as a risk-sized delivery route with clear intake from Product, Architecture, and Design; remove duplicated skill prose |
| `workflow-debug-issue` | Staff Engineering department procedure | **Keep and re-home** | Its diagnostic, propose, implement, and incident-mitigate modes already separate authority correctly | Preserve read-only diagnosis and route production containment to incident response |
| `workflow-refactor-module` | Staff Engineering department procedure | **Keep** | It has appropriate behaviour lock, scope control, and verification | Improve cross-route links only after the V4 routing model is installed |
| `workflow-dependency-upgrade` | Shared Systems Architecture/Staff procedure | **Keep** | It already treats compatibility, security, and rollback as evidence questions | Keep it conditional on an actual dependency decision; no universal upgrade churn |
| `workflow-context-hygiene`, `to-tickets`, and similar support assets | Studio operating support | **Defer to the Studio-support batch** | They serve coordination rather than product implementation itself | Decide later whether each becomes a Director capability, a short procedure, or an internal reference |

### Staff Engineering acceptance test before editing

For an authorized build, the staff engineer should be able to show:

```text
What changed | contract/invariant protected | validation and error path | tests/evidence run | known limitation | next owner, if any
```

The Staff Engineer is not required to await a ceremonial handoff for a one-line fix. It must activate the relevant boundary only when the missing decision changes correctness, risk, or user experience.

## C. Assurance and Quality

| Asset | V4 owner | Decision | Reason | Future source-edit objective |
| --- | --- | --- | --- | --- |
| `skills/testing` | Assurance & Quality, used by all functions | **Keep and strengthen** | It already prioritizes behavioural confidence, appropriate test level, integration value, and regression protection | Add a clearer distinction between test strategy, deterministic verification, human review, and incomplete evidence |
| `skills/review-audit` | Assurance & Quality | **Keep** | Its intent, correctness, security, failure, test, and architecture lenses support independent scrutiny | Retain severity and evidence focus; ensure the V4 process does not turn every small change into a full audit |
| `skills/security` | Shared safety discipline; Assurance owns independent security verification when triggered | **Keep and re-home** | Security informs architecture and implementation but benefits from independent review on risk-sensitive changes | Preserve threat modelling and authoritative enforcement; add AI-specific threats only in the optional AI-product layer |
| `skills/browser-test` | Assurance evidence helper, also available to Design/Staff | **Keep and re-profile** | It is a narrow browser-verification tool contract, not a quality theory | Make it a conditional evidence tool for observable UI behaviour, screenshots, and browser checks |
| `skills/fallow` | Assurance tool-backed analysis procedure | **Keep and re-profile** | It is useful JavaScript/TypeScript static/runtime intelligence with explicit prerequisites | Keep it conditional on supported repositories and distinguish its findings from proof of runtime correctness |
| `skills/dox` | Shared engineering-contract procedure | **Keep and re-home** | Directory contracts prevent hidden cascade effects but are not a complete assurance discipline | Keep the before-edit traversal rule; use it when directory interfaces/contracts are actually affected |
| `workflow-test-strategy` | Assurance & Quality procedure | **Keep** | It directly produces risk-based test evidence | Ensure it is selected when a material test strategy is needed, not for trivial edits |
| `workflow-review-code` | Assurance & Quality procedure | **Keep** | It gives code review a clear scope, risk assessment, and approval condition | Preserve independent review, but do not confuse it with a user approval gate |
| `workflow-security-audit` | Assurance & Quality procedure | **Keep** | It provides risk-scaled security audit behaviour | Retain its read-only default and its route to incident response for active compromise |
| `workflow-verify-project` | Assurance evidence route | **Strengthen and reduce** | Baseline scans are useful, but they are not a declaration that a project is production-ready | Preserve the "baseline checks passed" distinction; require project-native tests and explicit release approval separately |
| `workflow-impeccable-audit` / `workflow-impeccable-critique` | Design/Assurance collaboration | **Re-profile** | They add value for design-led work but are not universal code-quality routes | Keep their specialist checks behind the Design procedure surface and clarify their evidence limits |

### Assurance acceptance test before editing

Assurance should answer only what the evidence can support:

```text
Claim examined | evidence checked | result | limitation / residual risk | release or remediation condition
```

It does not promise "perfect" software, replace project-native tests with a generic scanner, or silently authorize deployment. It makes uncertainty visible early enough to act on it.

## The crucial self-check / independent-check boundary

| Situation | Required check |
| --- | --- |
| Small reversible local change | Builder or designer self-check plus proportionate verification |
| New user flow, material contract, or cross-boundary feature | Lead self-check plus test/architecture evidence; independent review when risk or uncertainty justifies it |
| Security-sensitive, data-sensitive, irreversible, external, or production action | Independent Assurance/Security evidence and the applicable explicit approval gate |
| Active production incident | Evidence-led containment through the incident hard gate; do not wait for a conventional review cycle |

## Accepted conditional strengthening rules

The following are useful additions identified during the cross-ledger review. They are **future source-edit criteria**, not new universal policy and not stack prescriptions.

| Area | Accepted strengthening rule | Boundary that prevents rigidity |
| --- | --- | --- |
| General UI | Use semantic design tokens when a shared UI system exists, and describe the user-visible states that matter for the component or flow | Do not require a fixed number of states: hover does not apply to touch-only controls; empty, busy, disabled, permission, and error states apply only where real |
| General UI taste | Check for generic visual defaults that weaken the intended brand or usability | Never ban a colour, glow, or aesthetic treatment as a universal rule; judge it against the product, brand, accessibility, and communication job |
| Implementation boundaries | Validate/parse untrusted input at real boundaries using the supported project/runtime mechanism | Do not make a library such as Zod or Pydantic a portable OS requirement |
| Implementation structure | Separate pure domain logic from I/O when it improves testability, correctness, or change safety | Do not force an abstraction on a small, simple feature with no meaningful separation need |
| Regression prevention | After a confirmed bug pattern, inspect sibling paths for the same defect and add proportionate regression protection | Do not expand a tiny isolated fix into an unrelated refactor without evidence |
| Test reliability | Prefer observable conditions, deterministic fixtures, and behaviour-level tests over arbitrary waits and brittle implementation assertions | Match the technique to the project's test runner and actual asynchronous behaviour |
| Security | Assume breach at trust boundaries: enforce authorization server-side for the specific actor, resource, and action; validate/parameterize data paths where applicable | Do not apply database, CSRF, CORS, or session-specific controls where that architecture is not present; retain the threat-model trigger |
| Tool helpers | Treat transition recipes, repository-hook setup, static analysis, and directory-contract tools as conditional helpers rather than universal reasoning disciplines | Preserve their useful instructions and activate them when their actual tool, stack, or change surface is present |

## What happens after Batch B

1. **Batch C:** classify Spatial, Media/Video, and Growth source into optional packs. This removes specialist discovery noise without deleting the strong specialist work.
2. **Integration decision:** compare the Core, Architecture, Delivery, and optional-pack ledgers. Only agreements become V4 source-change requirements.
3. **Selective rewrite plan:** choose the smallest first source slice. Likely candidates are the Director router, project-inception route, architecture route, and the design/assurance handoff rules.
4. **Targeted research:** only then refresh individual selected skills where their technical, legal, API, security, or provider claims are volatile or where research materially changes the design.

No skill becomes obsolete just because it is six months old. It must be shown to be mis-scoped, duplicated, unsupported, or less useful than a simpler replacement.
