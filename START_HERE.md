# Start Here — Anti-Gravity OS V4

## What this is

Anti-Gravity is a **personal AI Product Studio**. It helps one person direct
capable AI to understand, design, build, check, and improve a product without
forcing every task through a giant prompt or a fake company roleplay.

It does not replace your judgement. You set the goal and approve important
effects. The system helps choose the right depth of thinking and checking.

## The simple picture

```text
You set the goal
        ↓
Studio Director understands the job
        ↓
It works directly or calls the right lead
        ↓
Skills give focused help; workflows add useful gates
        ↓
Evidence is checked; you approve consequential actions
```

## The main pieces

| Name | Plain meaning |
| --- | --- |
| `global/GEMINI.md` | The main agent. It tells the Studio Director how to behave, stay safe, and decide when to involve help. |
| `global/GLOBAL_MEMORY.md` | The router. It tells the main agent which lead, skill, workflow, or pack fits the task. |
| `global/manifest.yaml` | The exact inventory. It is the source of truth for what exists and which pack it belongs to. |
| `global/agents/` | The five on-demand specialist leads plus the Studio Director. |
| `global/skills/` | Focused expert playbooks. A skill is used only when it helps. |
| `global/workflows/` | Useful routes and gates. They are not mandatory checklists. |
| `global/reference/` and skill references | Deeper information loaded only when needed. |
| `.agents/contexts/` in a real project | Current facts about that one client or product. It is not global memory. |

## The six agents

| Agent | Use it when you need |
| --- | --- |
| Studio Director | The best default. It sizes the task and chooses the smallest useful route. |
| Product & Strategy Lead | Product ideas, client understanding, scope, market, positioning, growth decisions. |
| Systems Architect | Data, APIs, boundaries, reliability, migrations, technical trade-offs. |
| Design Director | UX, interface states, accessible design, visual direction, spatial/media decisions. |
| Staff Engineer | Building, fixing, integrating, refactoring, and local tests. |
| Assurance & Quality Lead | Independent checking, security, regression risk, and proof. |

They are not all used for every task. A small change can be handled directly.

## Packs

`general` is always active. The other packs add specialist material only when
the job needs it:

| Pack | For |
| --- | --- |
| `spatial` | Cinematic/showroom/interior/architecture-adjacent website work. |
| `media` | AI image or video planning and provider-aware generation guidance. |
| `growth` | Positioning, offers, copy, conversion, prospecting, and sales material. |

## What exists now

The canonical manifest currently contains **48 skills**, **17 workflows**, and
**6 reusable agents**.

- General: 29 skills and 14 workflows.
- Spatial: 10 skills and 1 workflow.
- Media: 2 skills and no standalone workflow; video work routes through the
  `video-generation` skill.
- Growth: 8 skills and 2 guarded commercial workflows.

For the exact current list, read `global/manifest.yaml`. Do not rely on old
folders, generated copies, or a previous installation.

## Before using it in a real project

1. Start with the **Studio Director**.
2. Give the project name, goal, constraints, links/files, and what success
   looks like.
3. Let it choose direct work or the smallest relevant lead/skill/route.
4. Approve only actions with real outside consequences: spend, publish, send,
   deploy, change production data, or delete important data.

## Important distinction

A skill can give planning or prompt guidance without giving the agent a real
external account or button. For example, `video-generation` can plan a film or
write a provider-aware prompt. It cannot spend credits or generate a video
until you have provider access and approve that action.

## Where this is today

The canonical V4 source is being completed and tested in this repository.
Generated host payloads are disposable test output until Beloved explicitly
approves a global installation or repository release.
