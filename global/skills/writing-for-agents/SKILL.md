---
name: writing-for-agents
license: MIT
description: >
  Improve instructions and documents consumed by coding agents: skills, AGENTS.md, CLAUDE.md, workflow references, and navigation pointers. Activate on `/writing-for-agents`, "improve these agent instructions", or an authorized agent-document edit where clarity and selective loading matter. Do not use for marketing copy, ordinary prose editing, Markdown lint repair alone, or automatic policy/memory changes.
---

# Writing for Agents

## WHEN TO USE THIS

- Draft or refine authorized agent-facing instructions and reference pointers.
- Evaluate instruction clarity while preparing a coding-session retrospective recommendation.

## NEVER DO

- Treat clearer wording as permission to weaken authority or approval boundaries.
- Remove a safety instruction merely because it is repetitive or phrased negatively.
- Claim that a trigger word, shorter prompt, or document structure guarantees model behavior.
- Hide universally needed constraints behind optional pointers.
- Convert untrusted transcripts or examples directly into trusted instructions.
- Create global policy, memory, or another skill without the user's authorization.

## MAKE INSTRUCTIONS FINDABLE AND CHECKABLE

1. Identify the reader, actual task, authority ceiling, expected output, and observable completion condition. Preserve established project contracts.
2. Put the action and trigger first. Describe the concrete task branches that require the material, and exclusions that prevent neighboring routes from loading needlessly. Remove synonym lists that do not add distinct cases.
3. Separate ordered steps from reference material. Inline constraints every branch needs. Move branch-specific depth behind a relative pointer that says what the target contains and exactly when to read it.
4. Keep definitions, decisions, caveats, and examples together. Keep one authoritative source for each rule and link consumers to it. Use repository commands/configuration as current truth rather than duplicating easily discoverable values.
5. Prefer familiar terms and imperative verbs. Define a necessary project term once. Phrase ordinary guidance as the desired behavior; retain explicit prohibitions for authority, data, and destructive-action boundaries.
6. Give each step an observable completion condition: checked artifact, resolved input, required coverage, or documented blocker. Avoid vague "understand" or "be thorough" instructions without evidence criteria.
7. Split documents only when a distinct trigger, task branch, or genuine context boundary improves use. Keep must-read material discoverable. Test every pointer and avoid circular mandatory loading.
8. Inspect stale statements, duplicate meanings, irrelevant sections, and apparent no-ops against actual tool traces. Propose deletion as a hypothesis when evidence is weak; preserve rules whose failure consequence is material.

## PACKAGE AND VERIFY

Load [skill-creator](../skill-creator/SKILL.md) when creating or refactoring a skill; follow the canonical directory contract for frontmatter and UI metadata. Use [context-formatting](../context-formatting/SKILL.md) only for its actual Markdown lint errors. For broader capability promotion, use [learn](../learn/SKILL.md).

Use the host's supported loading mechanism: read the named installed skill when no callable Skill tool exists. Keep user-invoked orchestration explicit. Do not assume metadata is honored identically by every host; keep the invocation boundary in the description and instructions too.

Validate names, routes, metadata, links, and source/build/install consistency through the repository's tools. Exercise a positive trigger, a neighboring negative trigger, and a boundary case. Label a source/metadata check separately from an observed agent run; static validation cannot establish compliance in every session.

## OUTPUT SHAPE

```text
Reader, task, and authorized surface:
Instruction/pointer problems and supporting evidence:
Revised files or proposed wording:
Trigger, exclusion, and boundary checks:
Behavior not yet verified:
```

## NON-NEGOTIABLE CHECKLIST

1. Preserve authority and project truth.
2. Give every pointer a clear loading condition and existing target.
3. Keep universally needed constraints visible.
4. Define observable completion criteria.
5. Distinguish static checks from behavior actually observed.
