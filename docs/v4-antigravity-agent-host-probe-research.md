# V4 Antigravity Agent Host-Probe Research

**Status:** General workspace probe passed; collaboration payload fixed; live
nested-delegation pilot remains
**Verified:** 2026-08-23
**Scope:** Google Antigravity 2.0 custom agents, skills, projects, subagents,
hooks, and the V4 adapter. No live installation, hook, permission change, or
external account action was performed.

## Decision

Run the **Antigravity-native host probe before the first real website pilot**.
The six canonical V4 agent contracts are the right starting structure, but the
next proof must be in Antigravity itself: discovery, skill visibility, tool
mapping, project scope, delegation, approval stops, and worktree isolation.

Do not create more permanent roles, hooks, MCP servers, or autonomous loops
until that small probe establishes the actual host behaviour.

## Host finding: Manager-surface skill binding

The disposable probe proved that Antigravity discovers all six generated
agents and lets a user select them directly. It also exposed a host limitation
in the tested Manager-surface Project: the host logged an `AgentBasePath is not
set` error for every relative entry in a custom agent's `skills:` frontmatter,
then discarded the whole skill section.

The skill folders themselves are valid workspace skills. The failure is the
host's relative-path binding in this surface, not a missing `video-generation`
skill. The adapter therefore does not emit that fragile frontmatter field for
generated main agents. Instead it writes the selected capability routes into
the loaded agent instruction body. Antigravity still performs normal workspace
skill discovery; the explicit route list keeps the role aware of the intended
profile-specific skills.

This preserves an important distinction: `video-generation` is available for
planning, provider-aware briefing, prompt drafting, comparison, and diagnosis.
It does not mean the agent has a logged-in video provider or permission to
spend credits and generate media.

The canonical main policy is `global/GEMINI.md`. The first disposable pilot
showed that this host session still selected the machine-level `user_global`
policy when the generated copy lived only at `.agents/rules/`. The adapter now
generates the policy as the workspace-root `GEMINI.md`, which is the clearest
project rule location for Antigravity. The `.agents/` directory continues to
hold skills, workflows, agents, references, and schemas. A global installation
would instead write the same policy to `~/.gemini/GEMINI.md`; that remains a
separate, explicitly approved action.

## What current Google documentation establishes

| Capability | Confirmed host behaviour | V4 consequence |
| --- | --- | --- |
| Custom agents | Antigravity discovers Markdown agents at workspace, global, and plugin locations. Agent frontmatter controls description, tools, main-agent/subagent availability, model tier, command policy, and skills/plugins. | Keep the six reusable canonical agents; generate host Markdown rather than hand-maintaining host copies. |
| Skills | The agent receives skill names/descriptions first and loads a full `SKILL.md` only when relevant. Skills may be workspace-scoped or global. | Keep skills focused and route by description. Canvas UI can surface intelligently without being always loaded. |
| Projects | A project can scope one or more folders, settings, and permissions. New worktree mode isolates concurrent work. | Put real project truth and access boundaries in the Project; do not place client facts in global agents or skills. |
| Subagents | A parent can invoke a reusable or temporary child that starts with an isolated context. The child can use inherited/selected scope, shared storage, or an isolated worktree. | Use bounded worker charters and artifacts. Do not rely on a worker having the parent conversation or build a permanent swarm. |
| Hooks | Hooks can observe or intercept lifecycle/tool events and can run commands. | Do not enable hooks in the first probe. Add one only after a separate safety, failure, timeout, and approval test. |
| Agent-to-agent communication | The host exposes subagent invocation and messaging. It does not make a worker report self-validating. | Treat messages as coordination; accept work only after the Director or Assurance lead inspects evidence and runs the relevant check. |

## Important correction found

The canonical adapter previously mapped its portable `list_files` capability to
Antigravity's `view_file` tool. Current first-party documentation names
`list_dir` for directory listing, while `view_file` is for file contents.

The adapter now maps `list_files` to `list_dir` and the generated-payload test
asserts that exact tool. This avoids a documented tool-name mismatch that could
make agent behaviour incomplete or fragile.

## Delegation capability correction

The canonical roles declared `can_delegate: true`, but the generated
Antigravity tool lists originally contained only file, search, edit, and command
tools. That prose-level declaration could not create a child session.

The canonical capability ceiling now requires four collaboration capabilities
for every delegating role, and the Antigravity adapter maps them to the host's
documented `invoke_subagent`, `define_subagent`, `send_message`, and
`manage_subagents` tools. Validation fails when a role claims delegation without
the full tool set. Generated-payload tests confirm all six roles receive the
mapping.

This establishes payload correctness, not a live-host result. A fresh
Antigravity conversation must still prove both paths: selected Studio Director
to functional lead, and invoked functional lead to a temporary worker. Workers
must be defined without subagent tools so they cannot extend the hierarchy.

## What agents can and cannot guarantee

Agents can divide work, inspect evidence, compare options, run tests, and
return structured artifacts. They cannot guarantee that a product has no bugs
simply by talking to each other.

V4 therefore uses this reliability chain:

```text
clear task and authority
  -> smallest responsible lead or worker
  -> bounded implementation or analysis
  -> independent evidence / tests / review
  -> Director integrates findings
  -> Beloved approves material or external decisions
```

The Assurance & Quality Lead challenges material claims; it does not silently
certify a builder's work. Automated tests, browser checks, and project-native
verification remain the evidence layer. Agent-to-agent messaging is not a
substitute for either.

## Phase 8A: disposable host-probe acceptance checks

Use a new, harmless Antigravity Project or a disposable local worktree. Build
the Antigravity General payload and a General + Spatial payload from canonical
source. Do not install globally until the generated files pass this probe.

1. **Discovery:** Antigravity shows all six generated agents with clear names
   and descriptions. **Passed in the disposable probe.**
2. **Role-aware General isolation:** A normal software task sees General
   resources only. The Design Director has its General methods but not Canvas
   UI/video direction, and the Product Lead has its General methods but not
   Growth copy/sales methods. **Passed in the 2026-08-20 read-only check:**
   Spatial, Media, and Growth skills were absent from the workspace-local
   General profile and were not used.
3. **Spatial route:** A spatial website request makes the Design Director and
   relevant Spatial skills available; Canvas UI is considered only for a named
   visual job.
4. **Direct-lead use:** Select one lead directly, confirm the four collaboration
   tools are available, and confirm it stays inside its role and tool ceiling.
5. **Director-to-lead:** Select `studio-director`, invoke one installed lead,
   and confirm the lead returns evidence to Studio Director.
6. **Lead-to-worker nesting:** From the invoked lead, define and invoke one
   read-only worker with subagent tools disabled. Confirm it receives a compact
   charter, returns evidence to the lead, and stops.
7. **Sibling assurance:** Let Staff Engineering own a harmless implementation
   lane and Assurance own a separate review lane. Confirm Assurance is not a
   child controlled by the implementer.
8. **Permission stop:** Attempt a dependency, source-import, or external-style
   request. Confirm the host asks rather than silently proceeding.
9. **Worktree isolation:** Use a small concurrent task only in a disposable
   worktree and confirm it does not overwrite the primary project folder.
10. **Tool surface:** Confirm every generated tool name is accepted by the
   installed host version. Stop on an unknown tool rather than guessing.
11. **Capability-route wording:** In a fresh project from the fallback payload,
   select Design Director and confirm it reports `canvas-ui` and
   `video-generation` as available *guidance* under Spatial + Media, while
   correctly saying direct provider generation is unavailable without a visible
   provider surface and approval.

The probe can expose a host-version difference. If that happens, update only
the Antigravity adapter or its canonical capability mapping; do not distort the
portable OS policy around a temporary host quirk.

## What follows the first probe

Run a real read-only product or website pilot through the proven host model.
The first product-framing run completed on 2026-08-20. It produced a useful
problem frame, smallest slice, non-goals, and unknowns. It also exposed one
targeted routing gap: the response listed API, database, coding, UI, and testing
routes before the project supplied stack, identity, persistence, or design
facts. It called generic SaaS patterns evidence and used more confidence than
the available project evidence supported.

The correction is now in the main policy, router, Studio Director, and Product
Strategy Lead contracts. A second read-only run must confirm that the technical
loading gate works. After that, an explicitly authorised small build pilot can
test whether the revised route improves implementation evidence, defect
detection, and human review effort. The first pilot does not prove those
outcomes.

The second run confirmed the broad loading gate: coding, UI, and testing were
not selected. It still moved toward API design before context, tenancy,
lifecycle, and stack were known and reported 95% confidence from generic CRUD
conventions. The policy now requires the dominant product unknown to be
resolved before API design and requires confidence to match the evidence scope.

## Primary sources

- [Google Antigravity: Custom subagents](https://antigravity.google/docs/subagents)
  — discovery locations, frontmatter, tools, skills, lifecycle, and isolation;
  checked 2026-08-19.
- [Google Antigravity: Projects](https://www.antigravity.google/docs/projects)
  — project folder, permission, and worktree boundaries; checked 2026-08-19.
- [Google Antigravity: Skills](https://antigravity.google/docs/skills)
  — progressive disclosure, scope, and description-based activation; checked
  2026-08-19.
- [Google Antigravity: Hooks](https://antigravity.google/docs/hooks) — lifecycle
  points and available tool names; checked 2026-08-19.
- [Google Blog: Managed Agents in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/)
  — versionable `AGENTS.md`/`SKILL.md` customisation model; checked 2026-08-19.
