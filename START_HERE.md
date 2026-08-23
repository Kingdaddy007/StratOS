# Start Here — Anti-Gravity OS V4

Anti-Gravity OS helps you direct AI like a small, careful product studio.

You bring the goal, client context, taste, and approval for real-world actions.
The system helps the agent choose the right depth of work, specialist help,
skills, evidence, and safety checks.

## The five-minute mental model

```text
You explain the outcome you want.
          ↓
Studio Director understands the task.
          ↓
It works directly or calls one useful specialist.
          ↓
Skills and references add focused help.
          ↓
The result is checked. You approve real-world effects.
```

This is not a permanent swarm. A small question should get a small answer. A
large or risky job gets more structure only where it helps.

## The first important choice

For normal Anti-Gravity OS work, use **Main Agent** after the global OS is
installed, or choose **studio-director** directly. Both follow the Studio
Director operating model. Main Agent is the most reliable default coordinator;
the custom entry is useful when you want the role selected explicitly.

| Name you see | What it means |
| --- | --- |
| `Main Agent` | Antigravity's built-in coordinator. When V4's global `GEMINI.md` is active, it operates as the Studio Director and can call the five leads. This is the recommended default. |
| `studio-director` | The selectable custom form of the same Studio Director role. It has explicit collaboration tools for leads and bounded workers. |
| `product-strategy-lead`, `systems-architect`, `design-director`, `staff-engineer`, `assurance-quality-lead` | Specialist agents. They can be called by Studio Director, selected directly, and—when justified—create bounded workers that report back to them. |
| `GEMINI.md` | The policy that gives Main Agent the Studio Director behaviour. The file itself is not a running agent. |
| `GLOBAL_MEMORY.md` | The routing index. It is not an agent and it does not contain client facts. |

## What to say when you start

Give the agent five things when you know them:

1. **Goal** — what you want to achieve.
2. **Context** — client, product, existing project, links, screenshots, or files.
3. **Constraints** — deadline, stack, budget, things to avoid, or non-negotiables.
4. **Success** — what a good result must prove or feel like.
5. **Authority** — whether you want explanation only, a plan, local edits, or a prepared release.

Example:

```text
I am building a website for an interior-design studio.
Here are the client site, logo, and reference video: [links/files].
The site should feel calm, editorial, and high-end. Do not build yet.
First explain what you understand, what you need to learn, and the best first
step. Use the Spatial material only if it really helps.
```

## What you do manually

The AI cannot replace these decisions:

- whether a client story, brand direction, or visual idea feels right;
- what private information is safe to give it;
- product priorities, real deadlines, and budget;
- approval to deploy, publish, send, spend, delete, or change production;
- access to accounts, files, and client information that it cannot see.

You do **not** need to remember every skill name. Give good context and say
what result you want. Studio Director should select the smallest useful skill,
reference, workflow, or specialist.

## The profiles

| Profile | Use it for |
| --- | --- |
| General | Software, SaaS, product thinking, UX, testing, debugging, security, and ordinary work. This is the default. |
| Spatial | Luxury interior, showroom, furniture, decor, staging, gallery, and cinematic website work. |
| Media | Image or video planning, reference direction, provider-aware prompts, and film treatment work. |
| Growth | Positioning, offers, copy, research, conversion, prospecting, and sales material. |

The agent should not load every profile for every task.

## Four request modes

| Say this | What it means |
| --- | --- |
| “Diagnose this. Do not edit files.” | Read-only investigation. |
| “Give me options and recommend one. Do not implement yet.” | A proposal, not a change. |
| “Implement the approved plan and run the focused tests.” | Local work is authorized. |
| “Prepare this for release. Stop before deployment.” | It may prepare evidence but must stop for approval. |

## Signs something needs attention

| What you notice | What to do |
| --- | --- |
| You cannot see `studio-director` after a fresh Antigravity start. | Check the global install with `SETUP.md`, then restart Antigravity. |
| The input says `Main Agent`. | This is expected after a global install: `GEMINI.md` makes Main Agent the Studio Director. You may still select `studio-director` directly. |
| A selected custom agent says it cannot invoke a child. | Confirm its generated tool list contains `invoke_subagent`, `define_subagent`, `send_message`, and `manage_subagents`, then reinstall the current payload and start a fresh conversation. |
| The agent gives a generic answer without reading the project. | Say: “Inspect the relevant files and references first. State the evidence you used.” |
| The agent assumes client facts or hides uncertainty. | Say: “Separate facts, assumptions, unknowns, and your recommendation.” |
| The agent suggests deployment, publishing, or spending without pausing. | Stop it. Those actions require your explicit approval. |
| A visual or website reference matters. | Attach screenshots, a recording, URL, or transcript and ask it to analyse the reference before copying it. |

## The next document

Read [`USER_MANUAL.md`](USER_MANUAL.md) for everyday prompts, project context,
how specialists work, and how to tell whether the system is helping.
