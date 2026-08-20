# Anti-Gravity OS v4 - Google Antigravity-First Agent Delivery Design

**Status:** Historical Phase 4 design baseline, implemented in canonical source
through `global/agents/` and the generated Antigravity payload. No live
installation, hook, or host permission change has been applied. Current host
findings and the next probe are recorded in
[v4-antigravity-agent-host-probe-research.md](v4-antigravity-agent-host-probe-research.md).  
**Updated:** 2026-08-19  
**Depends on:** [V4 operating model](../V4_OPERATING_MODEL_SPECIFICATION.md), [functional contracts](../V4_FUNCTIONAL_CONTRACTS.md), [native-agent evidence](v4-google-antigravity-agent-model.md), and [V4 roadmap](v4-roadmap.md)

## 1. Correction and decision

The first version treated the five functional leads primarily as Director "modes" and proposed only two later persistent host agents. That was too cautious for Beloved's intended operating model and insufficiently grounded in Google Antigravity's actual custom-agent capability.

Google Antigravity natively discovers reusable Markdown custom agents, lets the user select them directly or invoke them as subagents, and gives each definition its own tool, model, skills/plugin, command-policy, and context-boundary settings. V4 will use that capability as its **primary host model**.

V4 will therefore define six reusable agent configurations:

1. `studio-director` - the default integrated task owner.
2. `product-strategy-lead` - product framing, customer value, scope, and decision evidence.
3. `systems-architect` - durable boundaries, contracts, state ownership, and quality trade-offs.
4. `design-director` - usable experience, accessibility, interface states, and applicable visual direction.
5. `staff-engineer` - implementation inside approved boundaries, local debugging, and delivery evidence.
6. `assurance-quality-lead` - independent challenge of material claims, security, regression, and release evidence.

This does **not** create a permanent swarm. A definition is reusable configuration; an agent session exists only when Beloved selects it or the Director delegates a justified, bounded task. A simple task still goes directly to the Director. The Director does not call all five leads by default.

```text
Beloved
  |
  +-- Antigravity Project
  |     resources, workspace scope, permissions, task artifacts
  |
  +-- Studio Director (default primary agent)
        |
        +-- one or more selected functional agents, only when useful
        |     Product | Architecture | Design | Engineering | Assurance
        |
        +-- temporary worker, only for a named, bounded payoff
              separate context, evidence lane, or isolated worktree
```

## 2. What is native to Google Antigravity

The V4 design should work *with* Antigravity rather than pretend it is a generic chat model:

| Google Antigravity capability | V4 use |
| --- | --- |
| Markdown custom agents with YAML frontmatter | Each of the six reusable roles has a versioned `agent.md` definition rather than a vague persona inside one enormous prompt. |
| Selectable main agents and invocable subagents | Beloved can open a focused agent directly; the Director can invoke a lead when delegated expertise genuinely improves the result. |
| Per-agent tools, skills/plugins, model tier, and command policy | Every agent receives the minimum capability set for its job. It never receives authority merely because another agent has it. |
| Projects with scoped resources and permissions | Project truth stays with the project. A global role definition does not carry Beloved's private information into unrelated workspaces. |
| Temporary subagents, background execution, and isolated worktrees | Use for independently useful research, verification, tests, or separable delivery slices - not for routine busywork. |
| Artifacts and agent monitoring | Plans, decision records, test evidence, walkthroughs, and review results are the human-readable handoff; the user can inspect or stop work. |
| Approval bubbling and inherited safety configuration | A child cannot enlarge the parent project's permissions. Protected actions return to the human approval surface. |
| Plugins containing skills, rules, MCP configuration, and hooks | The General core and optional packs can become installable Antigravity packages without duplicating canonical skill prose. |

The Google Gemini API also supports extending the Antigravity agent with `AGENTS.md` and `SKILL.md` sources. That confirms the existing canonical policy-and-skill architecture is compatible with the underlying Google direction; the missing V4 layer is the native custom-agent registry and adapter.

## 3. Agent roster and authority

| Agent | Default activation | Normal authority | Distinct result | Must stop or escalate for |
| --- | --- | --- | --- | --- |
| Studio Director | Every task unless Beloved deliberately selects a focused lead | Read-only or scoped local edit matching the task; may delegate with a charter | One integrated task record and outcome | External/destructive effects, product trade-offs requiring Beloved, or an unresolved cross-boundary conflict. |
| Product & Strategy Lead | New product, unclear request, business rule, client strategy, positioning, or market evidence | Read-only by default; scoped document edits only when chartered | Testable problem/scope/acceptance brief | Implementation, architecture, release, or unsupported market claims. |
| Systems Architect | New durable boundary, API/data contract, migration, reliability, integration, or consequential technical choice | Read-only analysis by default; scoped architecture docs or prototypes when chartered | Boundary and decision record, including rejected alternatives | Product scope change, irreversible choice without approval, or implementation/release ownership. |
| Design Director | User flow, IA, interaction states, accessibility, visual direction, or qualifying specialist pack | Read-only/design-artifact work by default; scoped local edits when chartered | Design decision packet and acceptance criteria | Unsupported performance/technical claims, product-positioning changes, or release approval. |
| Staff Engineer | Approved implementation, targeted debug, refactor, or test work | Scoped local edit inside stated files/interfaces | Delivery record: changes, tests, limits, and handoffs | Scope/contract ambiguity, dependency or environment mutation, or external/destructive action. |
| Assurance & Quality Lead | Security/privacy/auth changes, migrations, release claims, cross-boundary risk, audit request, or disagreement | Read-only by default | Independent assurance report: evidence, severity, confidence, owner, and residual risk | Fixing the feature it is judging, accepting a release, or executing external/destructive actions. |

All six roles use the functional contracts as their behavioural source. The agent file only adds host-specific selection, discoverability, tool ceiling, skill/plugin bindings, and model policy. It must not become a second, conflicting body of rules.

### Capability-aware skill routing

Each canonical role has two resource layers:

1. a small baseline skill list for its normal professional method; and
2. profile-conditioned skills that are generated only when an optional pack is
   selected.

Every role reads the installed `GLOBAL_MEMORY.md` routing index before choosing
a skill, reference, workflow, or another Custom Agent. That makes the full
system discoverable without pretending every role should load every skill.
For example, the Design Director receives `ui-ux` and `reference-intelligence`
in a General build. UI/UX loads its compact colour references only when colour
is material. A Spatial build adds storytelling, motion, Canvas UI, and spatial
methods; a Media build adds video direction. The Studio Director coordinates
through the router and delegates specialist method work rather than loading
every optional skill itself.

Tools remain a capability ceiling. A listed tool makes an operation technically
available; it does not approve the operation or override a workflow, project
boundary, or human gate.

## 4. Lead autonomy versus Studio authority

Each functional lead has real professional autonomy **inside its charter**. It may choose its methods, request a factual clarification from another lead, and decide whether its own work needs a bounded temporary worker. It does not need a workflow for every thought.

The Studio Director remains responsible for the task as a whole:

- chooses whether direct work, a selected lead, multiple leads, or a worker is worth the cost;
- supplies the minimum relevant project truth and explicit acceptance evidence;
- resolves conflict between leads or asks Beloved where the trade-off is genuinely Beloved's;
- integrates results into one task record rather than leaving six competing conclusions;
- ensures an agent cannot convert a skill, workflow, or source it reads into permission.

Leads may cooperate in a loop. For example, a Staff Engineer can ask Design for a missing error state, and Design can ask Architecture whether an interaction is feasible. This is a clarification loop, not a slow waterfall. Material scope, ownership, quality, or risk trade-offs return to the Director.

## 5. Temporary workers: dynamic, constrained, and disposable

Do not define a large permanent army of generic helpers. Google Antigravity permits transient subagents, so V4 will use a temporary worker when a named objective benefits from separate context, independent evidence, background execution, or an isolated worktree.

The parent must provide this charter:

| Field | Required content |
| --- | --- |
| Objective | One question or named deliverable. |
| Parent | Studio Director or one named functional lead. |
| Scope | Named repository areas, sources, interfaces, and exclusions. |
| Authority | `read_only` or the exact scoped-local-edit boundary. |
| Inputs | Minimum project truth, accepted decisions, and untrusted material to inspect. |
| Deliverable | Findings or files, evidence, commands, assumptions, and blockers. |
| Verification | Exact checks or observations expected before return. |
| Stop conditions | Missing critical context; cross-boundary conflict; credentials; cost; dependency/environment change; destructive/external/production action; or approval requirement. |
| Expiry | The completion or stop condition that ends the worker. |

Workers do not create or modify global policy, global memory, agent definitions, workflows, or skills. They do not make external effects. A worker report is evidence, not an automatically accepted decision.

## 6. Project truth, global definitions, and privacy

The separation is deliberate:

| Location/type | Contents | Must not contain |
| --- | --- | --- |
| Global agent definition | Role, activation, tool ceiling, safety limits, and references to canonical skills. | Beloved's private facts, credentials, or project-specific assumptions. |
| Global General/optional-pack skills | Reusable methods and resources. | A live project's secrets, client data, or unverified discoveries. |
| Antigravity Project / workspace context | Current goal, approved decisions, local architecture, files, and task evidence. | Authority that overrides host/developer/user policy. |
| Temporary-worker charter | Only the slice necessary to do its assignment. | Full private history or unrelated project context. |

This is why a global `agent.md` can be reused across projects without pretending it remembers every project. A new task supplies current truth; persistent definitions supply capability and conduct.

## 7. Future Antigravity payload shape

No payload is created in this phase. The future Antigravity adapter must generate, rather than hand-maintain, this shape:

```text
generated Antigravity payload
  .agents/
    AGENTS.md                         # generated policy entry point
    agents/
      studio-director/agent.md
      product-strategy-lead/agent.md
      systems-architect/agent.md
      design-director/agent.md
      staff-engineer/agent.md
      assurance-quality-lead/agent.md
    skills/                            # selected canonical skills and resources
    plugins/
      anti-gravity-core/               # optional package form for core resources
      anti-gravity-spatial/            # only when selected
      anti-gravity-media/              # only when selected
      anti-gravity-growth/             # only when selected
```

The live Antigravity installation may be workspace-scoped (`.agents/agents/...`) or global (`~/.gemini/config/agents/...`), as selected by the installer. The native global installer also places the rule at `~/.gemini/GEMINI.md`, skills at `~/.gemini/config/skills/`, and workflows at `~/.gemini/config/workflows/`. It keeps a shallow provenance record under `~/.gemini/config/antigravity-os/`; it does not duplicate the deep reference tree there. Direct targets are backed up before replacement, and the canonical source remains in this repository; `dist/antigravity/` is generated output.

The existing `gemini` adapter is a compatibility lane for Gemini-style policy/skills. It is **not** an adequate substitute for the new native `antigravity` adapter, because it does not represent custom agents, project scoping, or Antigravity's native subagent model. The Phase 5 manifest migration must add `antigravity` without deleting the existing Gemini compatibility target.

## 8. Hooks, MCP, and plugins are capability layers, not authority

Google Antigravity hooks can run local scripts before and after tool/model/loop events. MCP can attach additional tools and data sources. Plugins can package skills, rules, MCP configuration, and hooks. These are useful extensions, but none is the OS constitution.

- Policy, host sandboxing, and just-in-time human approval remain the safety boundary.
- A hook may be added only after its allow, deny, timeout, unavailable-script, malformed-output, and host-downgrade behaviour are tested.
- MCP servers are added only with explicit scope, least privilege, and their own approval/security review.
- Optional packs package domain resources; they do not give a lead broader authority or make specialist content a General default.

## 9. Host order and portable translation

| Order | Host | V4 status |
| --- | --- | --- |
| 1 | **Google Antigravity** | Primary native target. Defines the first concrete agent-file, project, worker, artifact, and approval mapping. |
| 2 | Gemini compatibility | Keep policy/skill compatibility. Do not claim it has the complete Antigravity custom-agent surface until a host probe confirms the exact installed version. |
| 3 | Codex | Translate the canonical roles, skills, and worker charters into only the current Codex capabilities that are actually supported. It must not invent an equivalent file format. |
| 4 | Cursor, Windsurf, OpenCode | Secondary generated adapters. Use host-native features only where verified; preserve canonical authority ceilings. |

This corrects the earlier implication that Cursor/OpenCode should shape the model. They are comparison and compatibility targets, not V4's design authority.

## 10. Required acceptance probes before implementation is accepted

Before a generated Antigravity payload is declared usable, test it in a disposable workspace:

1. Each of the six custom-agent files is discovered and its description makes selection/delegation unambiguous.
2. The Director and every lead load only intended skills/resources; Media, Growth, and Spatial do not leak into a General-only task.
3. A lead can be selected directly and can return a result to the Director without receiving unrelated conversation or project context.
4. A read-only Assurance agent is refused a harmless edit attempt.
5. A scoped Staff Engineer edit is contained to its chartered files/worktree.
6. A temporary worker receives only its charter, returns evidence, and stops; it cannot create nested unbounded work.
7. A protected/dependency/destructive/external request reaches a visible approval gate and is not silently executed.
8. A hook, if enabled, is tested for deny, timeout, malformed output, unavailable script, and no-secret logging.
9. Removing the payload removes only Anti-Gravity namespaced files, never unrelated configuration.

## 11. What Phase 4 completes and what it does not

Phase 4 now completes the *design decision*: reusable custom agents are a first-class Antigravity layer, but always-running departmental bots are not.

Phase 5 created the canonical `global/agents/` source, migrated the manifest,
and added a generated Antigravity payload. The native global installer is now
implemented and has been verified locally; hooks are still not enabled and a
fresh-host UI smoke test remains before publication.

## Sources verified on 2026-08-18

- [Google Blog: Introducing Managed Agents in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/)
- [Google Antigravity: Custom subagents](https://antigravity.google/docs/subagents)
- [Google Antigravity: Agent Manager](https://antigravity.google/docs/cli/commands/agents)
- [Google Antigravity Blog: Subagents, hooks, projects, and worktrees](https://antigravity.google/blog/google-io-2026-feature-deep-dive)
- [Google Antigravity: Plugins](https://antigravity.google/docs/plugins)
