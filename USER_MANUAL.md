# Anti-Gravity OS — Everyday User Manual

This is the practical guide. Read [`START_HERE.md`](START_HERE.md) first if the
words “agent”, “skill”, and “workflow” still feel confusing.

## 1. Start with Studio Director

In Google Antigravity, use **Main Agent** after installing V4 globally, or
select **studio-director** directly. Main Agent loads the Studio Director policy
from `GEMINI.md`; the custom entry provides the same role as an explicit choice.

Studio Director is the coordinator. It should understand your goal, decide how
much structure is useful, and either work directly or call a specialist. It is
not supposed to create a crowd of agents for a small job.

## 2. Give a useful brief

The best request is clear without being a giant prompt.

```text
Goal: Build a small client portal for an interior-design studio.
Context: This repository and these client references: [links/files].
Constraints: Keep the first version small. Use the existing stack. Do not add
new paid services.
Success: A client can review a room concept and approve or request changes.
Authority: First give me a plan. Do not edit files yet.
```

For a small task, one sentence can be enough:

```text
Fix the mobile navigation overlap and run the focused UI checks.
```

## 3. Let the system choose help

You can name a specialist when you know you need one, but normally you do not
have to.

| If your task is about | The likely lead |
| --- | --- |
| A product idea, customer, scope, offer, or business rule | Product & Strategy Lead |
| API, database, integration, migration, performance, or reliability | Systems Architect |
| Website direction, UX, states, accessibility, motion, or visual taste | Design Director |
| Code, tests, refactoring, an implementation, or a bug fix | Staff Engineer |
| Security, regression risk, independent review, or release evidence | Assurance & Quality Lead |

The result should come back as one answer from Studio Director. A specialist is
there to improve a decision, not to make the system feel busy.

### The delegation hierarchy

```text
Main Agent governed by GEMINI.md, or selected studio-director
        -> one or more functional leads
                -> bounded temporary workers
                <- worker evidence returns to its lead
        <- lead conclusions return to Studio Director
```

A lead may create several workers when the work is separable: for example, one
worker inspects an API contract while another runs a focused regression check.
Workers cannot create more workers. The lead checks their results before it
reports upward. A builder's own worker may self-check the build, but final
independent assurance should be a separate sibling assigned by Studio Director.

You can also select a lead directly. It may then create bounded workers and
return one integrated result to you. Do not ask for a fixed number of workers;
ask for the smallest useful team and the reason for each lane.

## 4. Skills, workflows, and references

| Item | What it is | What you need to do |
| --- | --- | --- |
| Skill | Focused instructions and resources for a type of work. | Usually nothing. Describe the job well. |
| Reference | A deeper file, template, script, design library, screenshot, recording, URL, or document. | Attach or point to it when it matters. |
| Workflow | A repeatable route for work that needs state, evidence, a handoff, rollback, or approval. | Ask in plain language; use a slash command only when you want the exact known route. |
| Context | Current facts about one client or project. | Keep the important current facts in the project, not global memory. |

For example, the Design Director can use Reference Intelligence to study a
website recording. You do not need to remember that name. Give it the recording
and ask what is worth learning from it.

## 5. The four levels of action

Be explicit about what you want the agent to do.

| Your instruction | Allowed work |
| --- | --- |
| “Review”, “audit”, “explain”, or “diagnose. Do not edit.” | Read-only work. |
| “Give options”, “recommend”, or “plan.” | Analysis and a proposal. No implementation. |
| “Implement”, “fix”, “build”, or “update these files.” | Scoped local edits and relevant tests. |
| “Deploy”, “publish”, “send”, “buy”, “push”, or “change production.” | It must stop immediately before the real external action and ask for approval. |

Never assume that a workflow, a skill, a tool, or a previous message is
permission for an external action.

## 6. How to use it for common work

### Build a product feature

```text
I want a simple notes feature in this app. Start with the user problem, the
smallest useful version, non-goals, key unknowns, and the safest next step.
Do not write code until the product shape is clear.
```

### Diagnose a bug

```text
The checkout page sometimes creates duplicate orders. Diagnose it without
editing. Trace the evidence, give confidence, show possible failure paths, and
recommend the smallest safe fix.
```

### Build a spatial website

```text
I want to design a luxury interior-design website. Here are the client site,
brand assets, and a screen recording of a reference site. First extract the
useful design ideas, then propose a distinct direction for this client. Do not
copy the reference.
```

### Use video or image planning

```text
Plan a ten-second product reveal for Google Flow using the model available in
my account. Give me the scene plan, prompt, reference needs, and risks. Do not
run generation or spend credits.
```

### Ask for an independent review

```text
The feature is implemented. Use independent assurance to review changed code,
tests, security, regression risk, and residual risk. Do not approve a release
for me.
```

### Ask for bounded parallel work

```text
This task has several independent parts. Use only the functional leads or
temporary workers that materially improve speed or confidence. Give every child
a clear scope and evidence requirement. Have them report back to their parent,
then return one integrated answer. Keep final assurance independent from the
implementation worker tree.
```

## 7. Help the AI when it cannot know something

AI is strong at analysing what it can see. It still needs you for:

- client facts that are not public;
- the actual brand or creative direction you prefer;
- product priorities when two good options conflict;
- access to private tools and accounts;
- final approval for messages, money, production, publishing, or deletion.

Give screenshots, recordings, URLs, project files, error messages, and exact
examples. A good reference is usually more useful than another page of rules.

## 8. Keep project truth separate

Global rules are for stable behaviour across every project. Client or project
facts belong in that project.

When a project becomes serious, keep active truth in:

```text
.agents/contexts/
```

Use the templates from `global/context_templates/` as a starting point. Mark
facts as verified, assumed, or unknown. Do not put client secrets into global
files.

For long work, the system can save resumable workflow state in:

```text
.agents/workflows/<task-id>.json
```

This prevents one task from overwriting another task's state.

## 9. How to tell whether it is working well

Good behaviour looks like this:

- It restates a complex goal accurately before building.
- It reads the relevant project and references before making claims.
- It says what it knows, assumes, and does not know.
- It chooses one useful specialist instead of pretending all six are needed.
- It runs focused checks after a change.
- It separates “tests passed” from “safe to release”.
- It stops before external, destructive, or costly actions.

Correct it when needed:

```text
You are assuming too much. Separate evidence, assumptions, unknowns, and the
next smallest action. Do not change files yet.
```

```text
This is a small task. Work directly unless a specialist has a clear reason to
be involved.
```

```text
Before you recommend a change, inspect these files and tell me what evidence
you used.
```

## 10. Install or update safely

Always preview installation first:

```powershell
.\install.ps1 -TargetHost antigravity -InstallOption general -DryRun
```

Then run the real install only after you have reviewed the plan:

```powershell
.\install.ps1 -TargetHost antigravity -InstallOption general -Yes
```

Choose `full` instead of `general` if you want all optional Spatial, Media,
and Growth material installed globally. See [`SETUP.md`](SETUP.md) before
changing hosts or upgrading an older installation.
