# Anti-Gravity OS v4 - Phase 5 Manifest and Agent Foundation

**Status:** implemented and verified  
**Date:** 2026-08-18  
**Scope:** canonical registry, profile composition, native Google Antigravity payload, and routing-fixture contract. No global installation, hook, MCP server, skill-prose rewrite, publication, or deployment was performed.

## What changed

| Area | Implemented result |
| --- | --- |
| Manifest | `global/manifest.yaml` is schema V2 and OS version `4.0.0`. It now records profile definitions, ownership, delivery role, resources, and six agent contracts. |
| Profiles | `general` remains implicit base. `spatial`, `media`, and `growth` are optional packs with their own profile descriptions. |
| Pack boundaries | Seedance, video-generation, and image/video prompt direction are Media. Copy, conversion, positioning, prospecting, and sales assets are Growth. Spatial references and design-audit material are Spatial. |
| Resources | Resources now use the manifest rather than being copied into every build. The broadly applicable hero-layout reference remains General; the spatial reference library and design-audit library are Spatial. |
| Agent registry | Six portable contracts exist under `global/agents/`: Director, Product, Architecture, Design, Staff Engineering, and Assurance. |
| Antigravity adapter | A distinct `antigravity` host adapter renders Google-compatible `.agents/agents/<id>/agent.md` files from the portable contracts. The legacy `gemini` adapter remains unchanged as a compatibility lane. |
| Composition | `build` and `install` preserve `--profile` as a single-pack shorthand and add repeatable/comma-separated `--packs`. Generated output is collision-safe: `dist/<host>/general`, `dist/<host>/spatial+media`, and so on. |
| Routing fixtures | Fixtures now declare `base_profile`, `active_packs`, and `functional_leads`, rather than pretending one profile represents an entire task. |

## What the agent files do and do not do

The six canonical files state role, activation, exclusions, mutation ceiling,
tool capabilities, delegation boundary, and default skills. They are not a
second system prompt and they do not run by themselves.

Only the Antigravity adapter renders them today. The other hosts retain their
current policy/skills/workflow payloads until a later adapter capability probe
proves an honest native translation.

## Commands now supported

```text
build --host antigravity --profile general
build --host antigravity --profile spatial
build --host antigravity --packs spatial,media
install --host antigravity --packs spatial,media --target <path> --dry-run
```

`general` is always present and must not be supplied through `--packs`.

## Verification evidence

- Canonical validation: zero issues.
- Unit and integration suite: 45 tests passed.
- All declared hosts build a General payload.
- Antigravity General and Antigravity Spatial + Media payloads build into distinct output directories.
- General excludes Seedance and the spatial-only reference library.
- Growth is opt-in; its copywriting asset is absent from General and present in a Growth composition.
- Generated Antigravity payload contains six discovered agent files; Assurance has no edit tool in its generated frontmatter.

## Deferred intentionally

- Live installation into `~/.gemini/config/agents` or any global host directory.
- Host probes on Beloved's specific installed Antigravity build.
- Hooks, MCP servers, and direct Codex/Cursor/Windsurf/OpenCode agent generation.
- Source-prose improvements to core skills, workflows, references, and the lean router.

Those belong to the next controlled work, Phase 6: selective revision of the
highest-leverage General routes and skills.
