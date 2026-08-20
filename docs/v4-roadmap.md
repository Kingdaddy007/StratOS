# Anti-Gravity OS v4 - Delivery Roadmap

**Status:** active delivery roadmap  
**Date:** 2026-08-18  
**Scope:** Personal AI Product Studio for Beloved. Financial-market strategy and broker-specific automation are outside this OS.

## The destination

Anti-Gravity V4 is a personal AI Product Studio: one human directs capable AI through clear decision ownership, bounded specialist help, shared project truth, optional domain packs, and proportionate verification.

It is not a giant always-loaded prompt, a rigid workflow factory, a permanent roleplay swarm, or a collection of skills that merely repeats what a capable model already knows.

## The roadmap at a glance

```text
Foundation and scope
        ↓
Functional operating model
        ↓
Asset and pack decisions
        ↓
Custom-agent delivery design + targeted host research
        ↓
Manifest and router implementation
        ↓
Core routes, skills, and references - selective revision
        ↓
Optional-pack implementation
        ↓
Host payloads, real task drills, documentation, and release
```

## Phase 0 - Scope and safety baseline

**Status: complete**

- Canonical source, generated output, host adapters, authority boundaries, and validation tooling were identified.
- The OS remains portable across Gemini, Codex, Cursor, Windsurf, and OpenCode.
- The former broker-specific capability has been removed from the canonical OS scope.
- The system remains General by default, with Spatial, Media, and Growth as the only proposed specialist packs.

**Evidence:** the historical Phase 0 baseline contained 71 skills and 52 workflows. The current live manifest is the authority and contains 48 skills, 17 workflows, 6 agents, and 4 profiles.

## Phase 1 - Foundation evidence and asset inventory

**Status: complete**

- Compared the broad Product Studio research and AI-native product research.
- Distinguished durable principles from framework, provider, and marketing noise.
- Inventoried the canonical assets rather than rewriting them blindly.
- Created decision ledgers for core, delivery/assurance, and optional-pack assets.

**What this phase does not do:** It does not prove that every existing skill needs replacement. It creates the basis for deciding which asset is kept, reduced, merged, moved behind a pack, turned into a reference/tool procedure, or retired.

## Phase 2 - Operating model and functional contracts

**Status: complete as design**

The studio has five functional boundaries:

1. Product & Strategy
2. Systems Architecture
3. Design Direction
4. Staff Engineering
5. Assurance & Quality

Beloved remains the goal owner. A Studio Director sizes each task, activates only the relevant boundaries, and integrates the result. A functional boundary is not automatically a permanent host agent.

**Important result:** a designer can ask engineering for a feasibility clarification, and engineering can ask design for a missing state, without forcing every task through a slow departmental relay.

## Phase 3 - Pack, manifest, and router design

**Status: complete as design**

- Spatial, Media, and Growth are defined as optional packs.
- General remains the mandatory base.
- The manifest/router design separates task routing from host-payload composition.
- The required future migration is clear: a registry version that can express functional ownership, honest asset roles, resource membership, and safe multi-pack composition.

**Current authoritative planning documents:**

- [Master asset decision ledger](v4-master-asset-decision-ledger.md)
- [Manifest and router design](v4-manifest-router-design.md)
- [Functional contracts](../V4_FUNCTIONAL_CONTRACTS.md)

## Phase 4 - Google Antigravity-first custom-agent delivery design

**Status: complete as design and primary-host capability baseline**

This phase decides what “custom agents” mean in practice. Google Antigravity is the primary native target; Gemini compatibility, Codex, Cursor, Windsurf, and OpenCode are generated adapter targets.

### Questions this phase must answer

- Which roles produce enough distinct value to deserve a host-visible custom agent, rather than remaining a route, skill, or temporary worker charter?
- What context can each agent read, write, or delegate without leaking project truth or authority?
- Which tasks should be executed directly by the Studio Director, versus passed to a functional lead, versus given to a bounded temporary worker?
- How will an agent prove its result, communicate uncertainty, escalate cross-boundary conflicts, and stop at an approval gate?
- What are the actual current capabilities and limitations of Google Antigravity, Gemini compatibility, Codex, and the other target hosts for instructions, skills, delegation, tools, state, and approvals?

### Research rule

This phase needs **targeted, current, primary-source research** about host capabilities. It does not need another broad “what is an AI agent?” report.

For each proposed custom agent, the output must be a one-page contract:

| Field | Required decision |
| --- | --- |
| Job | The unique decision/outcome it owns |
| Activation | The clear trigger and exclusions |
| Context | Minimum project truth and references it can read |
| Authority | Read-only, scoped local edit, or escalation-only |
| Tools | What it may use and what it may not use |
| Delegation | When a bounded worker is justified; worker limits |
| Handoffs | What it gives to another functional boundary |
| Evidence | What proof it must return |
| Stop conditions | External/destructive/production and ambiguity gates |
| Host mapping | How its contract is represented in each supported host |

The Google Antigravity research answered a key design question: reusable custom-agent definitions are native and materially useful for V4's distinct functional boundaries. V4 will therefore define a Studio Director plus five reusable functional leads. They are on-demand configurations, not an always-running swarm. Dynamic workers remain temporary and chartered.

**Phase 4 records:**

- [Google Antigravity native-agent evidence](v4-google-antigravity-agent-model.md)
- [Google Antigravity-first agent delivery design](v4-custom-agent-delivery-design.md)

## Phase 5 - Manifest, agent registry, routing, and composition implementation

**Status: complete**

After Phase 4 settled the real agent surface, the registry and build mechanics were implemented together:

1. Add Media and Growth profile definitions; keep General and Spatial.
2. Add a canonical agent registry for the Studio Director and five functional leads; register functional owner, delivery role, and profile membership without a duplicate editable catalog.
3. Classify resources so Spatial references do not leak into General payloads.
4. Preserve old single-pack commands while adding safe explicit multi-pack composition.
5. Updated routing fixtures to test pack selection, functional boundaries, modes, and approval ceilings.
6. Added a native `antigravity` adapter while retaining the present `gemini` compatibility adapter; built and smoke-tested each declared host payload.

**Implementation record:** [Phase 5 manifest and agent foundation](v4-phase-5-manifest-agent-implementation.md)

This is an implementation batch, not a skill-prose rewrite.

## Phase 6 - Core studio routes and high-leverage skills

**Status: in progress; batches 1, 2, and the Product Thinking/Project Inception/Debugging/Testing-and-Verification research-to-asset batches complete; no blind rewrite**

Revise the smallest, highest-leverage universal layer first:

- Studio Director router and task dispatch;
- project inception and product framing;
- architecture decision support;
- implementation, debugging, and verification routes;
- Design/Engineering/Assurance collaboration handoffs.

Each asset gets an audit card before edits:

1. What decision or result does it improve beyond ordinary model capability?
2. What triggers and exclusions should activate it?
3. Which instructions are durable, and which claims are volatile or stack-specific?
4. Should it remain a skill, become a route, move into a reference, become a tool adapter, merge, or retire?
5. What behaviour test would prove the revision helped rather than merely made the document longer?

### Batch 1 — complete

- Created the [core asset audit](v4-phase-6-core-asset-audit.md), which classifies all 71 skills and 52 workflows by the role they should play rather than their raw count.
- Protected intentionally deep packages from mechanical size reduction; compression, merge, or removal now requires a named destination and preservation proof.
- Rewrote the Studio Director router, `task-dispatch`, and `project-inception` around proportionality, optional packs, bounded delegation, and approval-first project framing.
- Added route regression checks so future edits cannot silently restore forced delegation or a universal product-development waterfall.

### Research gates and integration checkpoint

The four focused research gates are complete. Product Thinking, Project Inception, Debugging, and Testing/Verification are applied in their [evidence syntheses](v4-phase-6-product-thinking-evidence-synthesis.md), [workflow synthesis](v4-phase-6-project-inception-evidence-synthesis.md), [debugging synthesis](v4-phase-6-debugging-evidence-synthesis.md), and [testing/verification synthesis](v4-phase-6-testing-verification-evidence-synthesis.md). The cross-asset [integration drills](v4-phase-6-integration-drills.md) now confirm their canonical routes, conditional resources, handoffs, and authority stops. The next gate is one small real, low-risk project pilot—not a new blind rewrite. Preserve depth that changes a decision or verification outcome; move only genuinely selective material to a reference or procedure, with a named destination and behaviour test.

### Batch 2 — complete

- Audited `product-thinking`, `architecture`, `coding`, and `testing` individually.
- Kept `coding` unchanged because it already has a clear activation boundary and proportionate implementation guidance.
- Preserved the detailed content and references in the other three skills while correcting rigid universal rules, stale paths, ungrounded cost claims, and poor exclusions.
- Added regression checks for proportionate product evidence, risk-sized architecture alternatives, portable testing routes, and explicit skill exclusions.

### Product Thinking research-to-skill batch — complete

- Re-opened and compared the supplied Manus and Grok Product Thinking reports; Manus was the primary evidence synthesis and Grok contributed only compatible secondary prompts.
- Independently verified the limited principles used from Google HEART, Google PAIR, NIST AI RMF, NN/g, and value-of-information research.
- Rebuilt `product-thinking` as a selective, multi-file capability with direct/product/high-stakes modes, evidence-to-claim matching, proportional measurement, smallest-credible-test guidance, and an explicit AI-versus-non-AI decision.
- Added decision, evidence, AI-fit, and behaviour-scenario references. It does not rewrite Project Inception, Debugging, or Testing/Verification ahead of their dedicated research prompts.

### Project Inception research-to-workflow batch — complete

- Compared the supplied Manus and Grok Prompt 2 reports; Manus supplied the primary, evidence-disciplined model, while Grok contributed limited practical refinements.
- Independently checked the limited principles used from DORA, the Agile Manifesto, NIST Human-Centered Design, NIST AI RMF, and ADR guidance.
- Rebuilt `project-inception` as a read-only, decision-ready route with starting-condition triage, risk-scaled paths, decision gates, a compact Project Decision Packet, and conditional functional collaboration.
- Kept delivery, diagnosis, implementation, testing, and security in separate routes; Prompt 3 and Prompt 4 remained the gates for their dedicated revisions.

### Debugging research-to-skill/workflow batch — complete

- Compared the supplied Manus and Grok Prompt 3 reports; Manus provided the primary evidence-disciplined model, and Grok contributed the compatible differential-slice and adversarial-fixture ideas.
- Independently checked the limited durable principles used from OpenTelemetry, Google SRE incident management, and Git bisection documentation.
- Rebuilt `debugging` as a selective package with evidence labels, a non-universal reproduction rule, risk-sensitive repair gates, explicit `diagnose`/`propose`/`implement`/`incident-mitigate` modes, fault-class references, and behavior scenarios.
- Rebuilt `debug-issue` as workflow v2: coordination and authority only, with task-scoped state and handoffs. It no longer embeds a giant stale debugging manual or silently treats diagnosis as permission to edit.
- Prompt 4 was retained as the dedicated gate before changing Testing/Verification assets; that subsequent batch is now complete below.

### Testing and Verification research-to-skill/workflow batch — complete

- Compared the supplied Manus, Grok, and Gemini reports; Manus supplied the primary evidence model, Grok contributed change-class/fixture detail, and Gemini supplied only a compatible AI-evaluation taxonomy.
- Independently checked the limited durable principles used from Google SRE canarying, OWASP ASVS, NIST SSDF, and Microsoft consumer-driven contract guidance.
- Rebuilt `testing` as a selective evidence-selection package with claim/risk/boundary framing, credible-oracle design, explicit uncertainty statuses, specialist handoffs, four conditional references, and behavior scenarios.
- Rebuilt `test-strategy` as workflow v2 for planning/review/authorized local test implementation, and `verify-project` as a separate read-only v2 evidence-interpretation route. Neither route authorizes release or production action.
- The first four Phase-6 research gates are complete; the safe integration drills now pass. Before opening a new universal asset batch, run one small real, low-risk project pilot and capture only concrete gaps.

## Phase 7 - Specialist packs, references, and scripts

**Status: in progress; Growth is the first bounded pack. Its initial workflow/profile conflict was corrected, Customer/Market Evidence was added as a conditional shared reference rather than a new skill, and the completed Offer Architecture research gate justified one narrow optional skill plus two conditional hard-gate workflows. A workflow truth audit plus General, Media, and Spatial direct-route migrations have reduced the active registry to 17 without discarding the owning skills, protected specialist methods, or provider-specific Media content. Portable Brand/Positioning/Messaging/Narrative evidence remains the next gate before another substantive Growth-skill rewrite.**

Implement and audit Spatial, Media, and Growth separately. Each pack keeps only assets with a clear activation boundary. Growth establishes the smallest valid product-studio capability map, then changes positioning/copy/CRO and prospecting/sales only behind separate evidence gates. The accepted Offer Architecture package is deliberately narrow: it prepares a decision; it does not automate price, claims, outreach, publication, payment, CRM, or legal commitments. Media waits for fresh provider verification, and Spatial waits for a preservation-first specialist audit.

Provider-specific Media material receives current-source verification before use. References and scripts remain when they have a defined loading rule and a measurable purpose; they are not preserved merely because they already exist.

External repositories, including any repository Beloved brings from another creator, enter here as **candidate evidence**. They are reviewed against the same audit card and are never copied wholesale into Anti-Gravity.

## Research synthesis checkpoint — 2026-08-19

The [research synthesis decision ledger](v4-research-synthesis-decision-ledger.md)
reconciles the three supplied AI-native product-studio reports with the live
manifest. They support selective implementation, not a blind rewrite or a new
agent swarm. The research-analysis upgrade, general decision/evidence record,
shared agent return contract, workflow survival audit, and pilot fixture are
now implemented and structurally verified.

Historical ledgers that mention 71 skills or 52 workflows remain provenance;
they do not override the live manifest. Trading remains outside V4.

## Phase 8 - Host integration and real-task drills

**Status: generated-payload gate passed for General, Spatial, Media, and Growth.
The native Antigravity global installer is implemented and has been verified
locally with a Full-profile install. Hooks and extra permissions remain off.**

- Generate a native Google Antigravity payload first, then compatible Gemini, Codex, Cursor, Windsurf, and OpenCode payloads.
- Verify the native global discovery paths in a fresh Antigravity project after restarting the host.
- Test General-only, Spatial, Media, Growth, and justified mixed-pack tasks.
- Run a small safe task, a multi-boundary product task, a diagnosis-only task, and a high-impact approval-gated task.
- Confirm that a pack does not leak into unrelated work and that a custom agent/worker cannot exceed its authority.

**Immediate order inside this phase:** run the ten-case private routing fixture,
then run one real low-risk website or product pilot through the verified host
model. See [Antigravity agent host-probe research](v4-antigravity-agent-host-probe-research.md).

## Phase 9 - Documentation, migration, and release

**Status: planned**

- Produce the non-technical “start here,” glossary, task-flow diagram, and common-request guide.
- Explain host installation and safe migration from the V3 layout.
- Regenerate distributable payloads only after canonical validation and host smoke tests pass.
- Commit/push only with Beloved's explicit approval at that time.

## What happens next

The next user-visible scope is the representative pilot: first run the private
fixture, then send one safe real task through the installed Antigravity General
payload and one qualified Spatial or Media task if needed. Record what helped,
what added ceremony, and what failed before changing more skills. Do not
reactivate Trading, reopen all skills blindly, or let an optional pack become a
General dependency.

If Beloved provides the exact external repository URL, treat it as candidate evidence for the applicable pack audit or a future evidence-driven core review—not as new authority or content to copy blindly.
