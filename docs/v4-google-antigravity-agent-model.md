# Google Antigravity Native Agent Model - V4 Evidence Note

**Status:** Current primary-source capability evidence for Phase 4  
**Verified:** 2026-08-18  
**Decision supported:** Google Antigravity is Anti-Gravity OS V4's primary custom-agent target. Gemini compatibility and Codex support follow through generated adapters.

## The question answered

Does Google Antigravity actually provide a model suitable for Anti-Gravity's Studio Director, functional leads, temporary workers, skills, project boundaries, and approval model - or were those ideas imported mainly from other coding tools?

**Answer:** It does. The native Google surface directly supports reusable custom agents, dynamic subagents, project-scoped settings/resources/permissions, skills, plugins, hooks, worktree isolation, artifacts, and approval handling. That is sufficient to make Antigravity the V4 reference host.

## Verified native capabilities

| Capability | Primary-source evidence | V4 consequence |
| --- | --- | --- |
| Reusable custom agent files | Antigravity discovers `.agents/agents/<name>.md` or `<name>/agent.md` in a workspace and `~/.gemini/config/agents/...` globally. | Keep a canonical V4 agent registry that generates these files. |
| Per-agent configuration | YAML frontmatter supports a name, description, tools, main-agent/subagent role, model, command execution policy, MCP servers, and skills/plugins. | An agent role can have a real capability ceiling rather than being only a prompt persona. |
| Dynamic and reusable subagents | A parent invokes a separate session; the user can also create transient subagents. | Use temporary workers for a narrow result, not broad permanent helper swarms. |
| Context and execution isolation | A subagent begins with a clean context and can inherit, share, or use an isolated Git worktree. | Parent must send a compact charter and only needed project truth. |
| Project authority | A project sets agent behaviour, available resources, and permissions; child agents inherit the parent scope. | Project permissions and canonical policy are the safety ceiling. An agent definition cannot grant more. |
| Human visibility and control | The agent manager shows active/completed work; protected operations can surface approval. | Preserve evidence artifacts and require just-in-time approval for consequential action. |
| Skills and packaged extension | Plugins can package skills, rules, MCP configuration, and hooks. | Build General and optional packs as generated Antigravity packages rather than copy-pasted instruction sets. |
| AGENTS.md/SKILL.md-based managed agents | Google Gemini API can register a custom managed Antigravity agent using these versionable files. | Confirms the canonical policy/skill architecture is directionally compatible with Google, not merely with Codex. |

## Non-assumptions

This evidence does **not** prove that every V4 agent should be deployed immediately or that host features are safe by default.

- A custom agent definition is not evidence that delegation improves a small task.
- An installed hook executes local code and needs explicit threat, failure, and approval testing.
- A child agent's inherited permissions are not permission for external, destructive, production, credential, or cost-bearing actions; V4 retains its explicit human approval gates.
- The exact versions, plan availability, and tool names must be probed in Beloved's installed Antigravity environment before installation.
- Codex, Gemini compatibility, Cursor, Windsurf, and OpenCode are adapters, not authorities that can weaken the native V4 contract.

## Evidence links

1. [Google Blog: Introducing Managed Agents in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/) - custom managed agents based on the Antigravity agent; AGENTS.md and SKILL.md are versionable inputs.
2. [Google Antigravity custom-subagents documentation](https://antigravity.google/docs/subagents) - discovery locations, frontmatter, isolated sessions/worktrees, lifecycle, messages, and inherited permission scopes.
3. [Google Antigravity product blog](https://antigravity.google/blog/google-io-2026-feature-deep-dive) - subagents, projects, hooks, native worktrees, and approval-centred agent management.
4. [Google Antigravity plugin documentation](https://antigravity.google/docs/plugins) - package structure and workspace/global discovery of skills, rules, MCP configuration, and hooks.

## V4 decision

Phase 5 must introduce a separate `antigravity` host adapter and a canonical agent registry. It must preserve the existing `gemini` adapter as a compatibility target until migration testing proves a safe replacement path.
