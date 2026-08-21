# Codex Integration

Codex reads global instructions from `CODEX_HOME/AGENTS.md` (`~/.codex/AGENTS.md` by default). It reads project instructions from `AGENTS.md` files from the repository root downward. Codex custom agents are TOML files in `CODEX_HOME/agents/` globally or `.codex/agents/` in one project. Project skills are discovered from `.codex/skills/`.

Anti-Gravity V4 translates canonical policy into one primary role and five bounded specialist agents:

| Canonical role | Codex form | Why |
| --- | --- | --- |
| Studio Director | `AGENTS.md` policy plus `.agents/agents/studio-director/agent.md` reference | Its canonical contract sets `subagent: false`; it owns the main task rather than spawning recursively. |
| Staff Engineer | `staff-engineer.toml` | The only role with `workspace-write`; bounded by the parent charter. |
| Product Strategy, Systems Architecture, Design, Assurance | Four read-only TOMLs | Research, architecture, design, and review specialists. |

This deliberate 1+5 split preserves the canonical role contract. Turning Studio Director into a sixth spawnable agent is a role-policy change, not an adapter change.

Users do not need to invoke workflow names. The main Codex task applies the Studio Director routing rules from `AGENTS.md` and `GLOBAL_MEMORY.md`, chooses direct work or the smallest fitting workflow from task shape, and assigns a bounded workflow or acceptance gate to a specialist only when needed. Specialist TOMLs return candidate evidence and limitations; the main task integrates the result and decides final gate status.

`GLOBAL_MEMORY.md` resolves selected portable workflow contracts from its sibling `workflows/` directory. In a global install those are `CODEX_HOME/workflows/`; in a workspace install they are `.agents/workflows/`. They are internal contracts, not Codex slash commands.

## Scope and profile choices

The Windows and macOS/Linux installers ask Codex users for both:

1. **Scope:** **Global** for all Codex projects, or **Workspace** for one existing project.
2. **Profile:** **General** for the core V4 bundle, or **Full** to add Spatial, Media, and Growth capability packs.

Global installation writes active policy to `~/.codex/AGENTS.md`, active custom agents to `~/.codex/agents/`, and active skills to `~/.codex/skills/`. It keeps a complete generated rollback copy and record in `~/.codex/antigravity/`.

Workspace installation writes `AGENTS.md` in the selected project, agents to `.codex/agents/`, skills to `.codex/skills/`, and portable V4 references, workflows, memory, and the installation record under `.agents/`. It never touches `CODEX_HOME`. It refuses to replace unmanaged or locally changed files, including an existing project `AGENTS.md`.

Neither scope uses `GEMINI.md` for Codex.

## Review and install

```bash
python global/scripts/os.py build --host codex
python global/scripts/os.py install --host codex --target ~/.codex --option general --codex-global --dry-run
python global/scripts/os.py install --host codex --target /path/to/project --option general --codex-workspace --dry-run
```

After reviewing the exact changes, repeat the selected command with `--yes`. Start a new Codex task after a global installation so global instructions reload. Verify that `AGENTS.md`, all five TOMLs, and the selected skills exist at their native discovery paths.

The installer never changes `config.toml`, `config.json`, permissions, trusted-project registrations, plugins, or unrelated skills. It takes a timestamped backup before replacing managed global entries; workspace installs retain their own file-level backup under `.agents/.antigravity-backups/`.

Source-of-truth workflow: edit `global/` → `validate` → `build --host codex` → review dry-run → install with backup → start a new task.

Official references: [AGENTS.md configuration](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), and [Codex skills](https://developers.openai.com/api/docs/guides/tools-skills).
