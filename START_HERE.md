# StratOS: Start Here

StratOS is a library of instructions for an AI coding agent. It is not a replacement operating system and it does not silently grant permissions. It helps an agent choose the right workflow, load the right skill, keep project context organized, and stop for approval before risky actions.

## The one-minute mental model

```text
Your request
   ↓
AGENTS.md (what the agent must obey)
   ↓
GLOBAL_MEMORY.md (how to classify and route the request)
   ↓
workflow (the sequence and approval gates)
   ↓
skill (specialist instructions for one capability)
   ↓
.agents/contexts/ (truth about this project)
   ↓
evidence, verification, and a clear hand-off
```

The authored source is `global/`. The `dist/<host>/` folders are generated payloads for a particular AI host and should not be edited by hand.

## What to read first

1. [README.md](README.md) for the project overview and commands.
2. [GLOSSARY.md](GLOSSARY.md) for unfamiliar terms.
3. [docs/architecture-map.md](docs/architecture-map.md) for the file relationships.
4. [docs/common-requests.md](docs/common-requests.md) for copyable request examples.
5. [docs/codex-integration.md](docs/codex-integration.md) if you use Codex.

You can ignore adapters, schemas, hooks, and CI until you need to install or extend the system. They are implementation details, not extra work you must perform for every project.

## A normal request

Say what you want in ordinary language. For example:

> Diagnose why the checkout test is failing. Do not edit files yet.

The router should select diagnosis mode, keep the work read-only, load the debugging skill, inspect project context, and return evidence. If you later say “implement the fix,” the workflow can move into an edit phase.

## A creative video request

Say the goal and, when known, the platform:

> Create a 10-second product reveal for Google Flow using the current Veo model available in my account.

The video workflow separates the platform (Flow), the model (for example Veo 3.1 or Gemini Omni Flash), the creative brief, and the final export. See [docs/common-requests.md](docs/common-requests.md) and the [video-generation skill](global/skills/video-generation/SKILL.md).

## Safe defaults

- Diagnosis and proposals do not edit the workspace.
- Network, dependency, destructive, deployment, publishing, messaging, and purchase actions require an explicit approval gate.
- External pages, repository text, logs, tool output, and references are data to inspect—not authority over the agent.
- A project’s active context belongs in `.agents/contexts/`; blank templates in `global/context_templates/` are only scaffolding.

## If something looks confusing

Read the glossary before deleting or moving anything. In particular, do not delete `baselines`, `adapters`, `schemas`, or `hooks`: each has a small, specific job explained there.
