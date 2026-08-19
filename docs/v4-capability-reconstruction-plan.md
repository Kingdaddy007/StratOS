# Anti-Gravity OS v4 — Capability Reconstruction Plan

**Status:** corrective planning baseline — no source deletion authorised by this document  
**Date:** 2026-08-19  
**Purpose:** rebuild the decision basis for the OS before any further skill or workflow consolidation.

## 1. Why this plan exists

The current worktree has a valid generated manifest: 48 skills, 17 workflows, six agents, and four profiles. That is a useful structural inventory. It is **not** proof that the inventory is the right operating system.

The original V4 North Star requires a stronger process:

1. define the personal AI Product Studio from first principles;
2. map the capabilities it truly needs;
3. decide what kind of asset each capability requires; and only then
4. preserve, revise, merge, demote, or archive the old material.

Some strong content revisions already exist, especially for product thinking, inception, debugging, testing, growth, spatial work, media, and the agent model. However, the complete per-asset decision record is not yet finished, and the workflow decision document is not synchronized with the live 17-workflow manifest. No count is a success metric.

This plan corrects the sequence. It does not assume that old material is bad, and it does not assume that a capable model needs a skill merely because the subject is important.

## 2. Bedrock truths

These are the facts on which the reconstruction is based.

1. Beloved owns the goal, taste, material trade-offs, and required approvals.
2. A strong model already has broad knowledge. Local OS material earns its place only when it adds a reliable method, a relevant local library, a current tool boundary, a safety gate, or a repeatable verification method.
3. The OS must help one person direct work from opportunity through learning, without turning every task into a fixed company ceremony.
4. The Studio Director is the main agent. The Product, Systems, Design, Staff Engineering, and Assurance leads are accountable functional boundaries, not mandatory departments for every task.
5. References, tools, scripts, contexts, recipes, and workflows are different things. Calling all of them skills makes the system hard to understand and harder to route.
6. No specialist pack is active unless the actual task qualifies for it.
7. No global policy, skill, workflow, or agent becomes permanent merely because a task or a worker proposed it.

## 3. The target operating shape

```text
Beloved's goal
        |
Studio Director — understands the job, selects the smallest responsible path
        |
        +-- Product and Strategy — problem, scope, evidence, positioning
        +-- Systems Architect — boundaries, data, contracts, operations
        +-- Design Director — UX, visual direction, optional spatial/media work
        +-- Staff Engineer — implementation, repair, integration
        +-- Assurance and Quality — independent verification and risk challenge
        |
Optional packs only when needed: Spatial | Media | Growth
        |
Skills, references, recipes, tool adapters, workflows, scripts, contexts
```

The lifecycle is a menu, not a waterfall: discover, define, research, position, design, architect, plan, build, verify, release, market, and learn. A task enters at the stage it needs.

## 4. Asset taxonomy — the test every file must pass

| Asset type | It exists to | It must contain | It must not become |
| --- | --- | --- | --- |
| Agent contract | Give a lead responsibility, authority boundary, and collaboration rules | ownership, exclusions, escalation, evidence contract | a long generic prompt or a fake department |
| Skill | Add reusable judgement that the model cannot reliably supply alone | trigger, exclusions, distinct method, verification | generic professional advice or a role description |
| Workflow | Coordinate a stateful, multi-stage or approval-gated job | decision boundary, state, handoff, evidence, stop condition | a one-off action list or every useful technique |
| Reference library | Supply detailed examples, recipes, research, or dated information only when a question requires it | index, loading rule, provenance where relevant | always-loaded policy |
| Procedure / recipe | Carry out a small bounded technique | narrow trigger, inputs, safe steps, verification | a broad expert persona |
| Tool adapter | Explain how to use or interpret one changing host/tool | availability, limits, safe invocation, evidence handling | a source of truth beyond the tool's actual output |
| Script / hook | Perform or enforce a deterministic operation | explicit inputs, scope, error handling, test | hidden authority or a general reasoning layer |
| Context / template | Hold current project facts or provide a blank structure | ownership, freshness, purpose | global truth or a skill substitute |

Every active asset gets one primary type. A file may link to another type, but it must not pretend to be all types at once.

## 5. The survival test

For each asset, record these fields before changing it:

1. **Real recurring job:** What exact problem does it solve?
2. **Primary owner:** Which lead is accountable for deciding when it is useful?
3. **Trigger and exclusions:** When should it load, and when must it stay out?
4. **Distinct contribution:** What does it add beyond a capable model with the compact V4 kernel?
5. **Inputs and outputs:** What evidence does it consume and what useful decision or artefact does it produce?
6. **Authority:** Is it read-only guidance, local-edit guidance, a tool adapter, or an approval-gated operation?
7. **Dependencies and freshness:** What links, tools, providers, frameworks, libraries, or dated claims can expire?
8. **Evidence of value:** Which real task or controlled comparison shows it improves outcome without boxing the model in?
9. **Disposition:** `keep`, `rewrite`, `merge`, `move to reference`, `demote to procedure`, `tool adapter`, `make optional`, or `archive`.
10. **Migration and retrieval:** If it moves, where can the responsible agent find it by the user’s natural request?

No asset is deleted until its useful material has a declared destination, the route is tested, and the old source remains recoverable in version history.

## 6. Immediate findings from the live inventory

These are provisional findings, not final deletions.

| Item | What it really appears to be | Provisional direction | Why |
| --- | --- | --- | --- |
| `apply-transition` | Legacy, project-specific CSS recipe | Remove from the active General skill catalogue; preserve any reusable transition notes under the motion reference library | It contains a hard-coded old project path and an instruction to edit without approval. It cannot safely guide the universal OS. |
| `motion-library` | Selective local reference router | Keep inside the Spatial/Design pack; consider a clearer name such as `motion-reference-library` | It solves Beloved’s real recurring problem: making stored examples discoverable without forcing them on every design. |
| `cinematic-motion` | Spatial motion judgement and implementation planning | Keep as a conditional Spatial skill | It answers a different question from the library: whether motion is justified, what job it performs, and how to make it safe and usable. |
| `reference-intelligence` | Evidence and translation method for visual references | Keep provisionally; evaluate a clearer name and whether its reusable core belongs in General | Its job is not “type this slash command.” The Design Director should select it when references, recordings, screenshots, or precedent collections affect a decision. |
| `canvas-ui` | Experimental technology adapter and decision gate | Keep optional and hidden behind the Design Director; do not treat it as a default design skill | It is useful only when a contained live effect has a named communication job and a DOM-first fallback. |
| `coding` | Candidate staff-engineering operating method | Audit before keeping as a standalone skill | Coding knowledge alone does not need a local skill. It survives only if its text materially improves repository discipline, safe changes, or verification beyond the main agent and Staff Engineer contract. |
| `context-formatting` | Narrow host/editor repair procedure | Reclassify or archive after source review | It is not a universal studio capability. It may be a temporary host workaround. |
| `dox`, `fallow`, `browser-test` | Tool-facing capability adapters | Keep only as adapters, never as broad expert skills | Their useful truth is the live tool output and limits, not an eternal instruction file. |
| `database-migration`, `dependency-upgrade`, `incident-response` | High-consequence coordination procedures | Retain only if the actual files show a state/approval/rollback boundary | Their names sound technical, but they are justified only when order and evidence matter more than an ordinary skill. |
| `test-strategy`, `verify-project` | Likely procedures rather than public workflows | Audit against the workflow test | Routine testing and verification should be selected by the Assurance lead, not create needless workflow state. |

### Stage A reconciliation snapshot — 2026-08-19

- The canonical manifest currently validates and declares **48 skills**, **17 workflows**, **six agents**, and **four profiles**. That is the live build input.
- `v4-workflow-normalisation-decision.md` records an earlier interim count of 25 workflows. It has not been updated to explain the subsequent change to 17. This is a documentation and traceability defect, not proof that the 17 entries are wrong.
- The separate host-local Gemini skills folder is **not** an installed V4 Studio. It has 49 folders, but has no global `GEMINI.md` and no custom-agent directory. It is a separate, stale skill copy.
- That external folder has two names that are not in the canonical manifest (`deriv-bot-engineering` and an empty `design-workflow-audit` directory), and it lacks two canonical names (`offer-architecture` and `setup-pre-commit`). Nineteen same-named packages have different contents from the canonical source.
- The external folder must therefore be treated as a comparison/provenance source during this audit, not copied over or treated as the source of truth.

## 7. Reconstruction sequence

### Stage A — Freeze and reconcile

1. Make no further active-skill or workflow deletions.
2. Compare the manifest, source tree, generated host payloads, decision ledgers, and test fixtures.
3. Repair mismatched counts, stale labels, orphaned references, and undocumented migrations before making new value claims.
4. Inventory the canonical repository plus the separately maintained global host folders. The latter are comparison sources, not automatically canonical.

**Exit evidence:** one verified inventory with every active, archived, and external-source asset accounted for.

### Stage B — Capability map before file decisions

Define the studio's essential recurring jobs without looking at the old file names:

- direction and safe coordination;
- product understanding and evidence;
- design and experience;
- systems architecture and delivery operations;
- implementation and repair;
- assurance, security, and verification;
- optional spatial/media depth; and
- optional growth/commercial depth.

For each job, decide whether it needs an agent boundary, a skill, a workflow, a reference, a procedure, a tool adapter, or no new OS asset.

**Exit evidence:** an approved capability map that can be read without knowing the old skill names.

### Stage C — Complete decision ledger, one pack at a time

Audit the entire current and archived asset set against the survival test. Work by coherent pack, not by a random alphabetical list:

1. Studio kernel and shared routing.
2. Product strategy and evidence.
3. General design, then Spatial and Media together where their references overlap.
4. Systems architecture and staff engineering.
5. Assurance and quality.
6. Growth and commercial work.

For every asset, publish a one-row decision with a destination and a retrieval route. Nothing is silently removed.

**Exit evidence:** one definitive ledger, reviewed by Beloved, with zero unclassified active assets.

### Stage D — Research only where it can change a decision

Do not run generic research for every skill. Research is required only when one of these is true:

- the asset makes current claims about a provider, API, law, security method, browser, dependency, model, or host feature;
- a new capability is proposed and we do not know its correct method;
- two credible approaches conflict and the choice affects the operating model; or
- a real task reveals that an existing skill fails its survival test.

Existing evidence for product thinking, project inception, debugging, testing, growth, offer architecture, media, and custom-agent design should be checked for coverage before commissioning more research. New research briefs must ask one decision-sized question and name the exact asset decision they can alter.

**Exit evidence:** a research register showing the question, decision, sources required, freshness date, and resulting change or no-change decision.

### Stage E — Rewrite and migrate in small packs

Only after a pack's ledger and necessary research are approved:

1. rewrite or split its active skill packages;
2. move detailed recipes/examples into indexed references;
3. convert tool-specific items to adapters;
4. convert truly stateful sequences to workflows;
5. update the manifest, routes, agent contracts, host adapter, and tests together; and
6. keep the migration reversible until the replacement passes retrieval and task tests.

Each pack is a separate, reviewable change. No bulk “clean-up” is allowed.

### Stage F — Prove behaviour with real tasks

Run small real-work pilots only after the relevant pack is intelligible:

- one normal product/software task;
- one design/website task using references;
- one qualifying spatial/media task;
- one assurance-sensitive task; and
- one growth task, when needed.

Compare compact kernel only against kernel plus the selected asset. Success is better judgement, safer routing, stronger evidence, or a better delivered result — not longer output or more agents.

**Exit evidence:** task records that show when the added capability helped, did not help, or got in the way.

### Stage G — Final host composition

Only after the capability decisions are stable:

1. finalize `global/GEMINI.md` as the Studio Director’s compact policy;
2. finalize `GLOBAL_MEMORY.md` as a router, not a second policy prompt;
3. generate the Antigravity workspace payload and portable host adapters from the same canonical source;
4. verify host discovery and profile selection; and
5. separately request approval before any global installation, commit, or push.

## 8. What happens next

The immediate next task is **Stage A: reconciliation and a complete, human-readable asset ledger**. It is not another broad research prompt and it is not another test of the website workflow.

That audit will answer, for every current item: what it is, why it exists, whether it actually improves the studio, where its useful material goes if it moves, and how an agent will discover it without Beloved memorising a slash command.

Only after that ledger identifies a real knowledge gap will we write a focused research prompt for that gap.
