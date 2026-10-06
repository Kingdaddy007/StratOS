# Engineering skill adoption

Adopted source: [mattpocock/skills v1.3.1](https://github.com/mattpocock/skills/tree/v1.3.1), reviewed 2026-10-06. Canonical source remains `global/`; generated host payloads are built and installed through the supported OS CLI. Each adapted package carries the upstream MIT license and a source credit. The PR package also retains acknowledgment of Dex Horthy / Humanlayer's `show-me` contribution.

## Scope and dependencies

| Skill | Upstream source | Adaptation |
| --- | --- | --- |
| pr | skills/engineering/pr | Final-change narrative, optional visual, observed evidence, recovery limits, no publication authority |
| retro | skills/engineering/retro | Explicit invocation, session/worker coverage, sensitive-data boundaries, proportional prevention, recommendations before mutation |
| implement-spec | skills/engineering/implement-spec | Approved task graph, exclusive ownership, preserved dirty work, single integration owner, combined verification, sequential fallback |
| tdd | skills/engineering/tdd | Public-interface tests, independent oracles, intended red failure, proportional evidence, green refactoring, no redundant user confirmations |
| code-review | skills/engineering/code-review | Separate Specification/Standards axes, actual diff topology, uncommitted work, local requirements, risk-sized review |
| writing-for-agents | skills/productivity/writing-for-agents | Conditional pointers, checkable completion, single sources of truth, host loading, preserved authority |

Upstream `implement-spec` directly loads `tdd` and `code-review`; upstream `retro` directly loads `writing-for-agents`. All three dependencies are included as adapted skills. The upstream setup command is a configuration prerequisite, not an implementation dependency; existing project tracker/spec instructions replace it. `to-spec` and `to-tickets` name the upstream input-producing flow; supplied approved specs/tickets work without `to-spec`. Our existing `to-tickets` remains the planning route.

Upstream `tdd` conditionally loads `codebase-design` and upstream `writing-for-agents` links its own packaging mechanics. Existing `architecture`, `api-design`, `testing`, and `skill-creator` cover those decisions in this adaptation. No dangling upstream invocation remains. Skills load through actual host capability, not an assumed callable Skill tool.

Keep `retro` distinct from `learn`: the former diagnoses engineering-session friction, the latter evaluates broader learning and capability promotion. Keep `code-review` as a focused entry point that uses existing `review-audit` risk guidance. Keep implementation quality in both building and review. Accept legacy domain `CONTEXT.md` while following `GLOSSARY.md`/`GLOSSARY-MAP.md` when authoritative; never rename broader project context blindly.

## Boundaries and recovery

The user authorized skill integration, necessary compatibility changes, and bringing the skills into the existing local setup. No remote publication, PR creation, default-branch merge, deployment, package installation, or memory update is part of this change.

Use a separate local feature branch in the newer checkout; preserve the older checkout's unrelated dirty work. Validate source and host builds, inspect installation dry-runs, and use installer backups before native activation. Inspect unexpected replacements before installing; preserve unrelated active configuration.

`retro` and `implement-spec` declare explicit invocation in their descriptions and instructions, and set `allow_implicit_invocation: false` in Codex metadata. Other hosts may not enforce that metadata; portable invocation boundaries remain in the actual skill text.

## Evidence plan

Run canonical validation, host build/install tests with temporary targets, the repository suite, diff checks, and native installer dry-runs. Verify installed package bytes and recorded digests after activation. Use the [behavior scenarios](engineering-skills-scenarios.md) as representative routing and boundary evaluations. Record static contract evidence separately from live agent behavior; packaging tests and source checks do not prove successful implementation of a future application spec.

Installation results, evidence limits, and invocation examples are recorded in [the verification and usage guide](engineering-skills-verification.md).
