# Adapters Context & Contract

## 1. Purpose

This directory maps the canonical OS into host-specific installation layouts without duplicating domain instructions.

## 2. Rules & Constraints

- An adapter may translate paths, filenames, discovery conventions, and capability names only.
- An adapter may not weaken authority, approval, or security policy.
- Adapter configuration must validate against `adapter.schema.json`.
- Generated payloads belong under `dist/<host>/`, never in this directory.

## 3. Exposed Interfaces

- `<host>/adapter.json`: host layout and capability mapping. The `antigravity`
  adapter additionally maps portable agent capabilities to Google Antigravity's
  generated Markdown agent format and declares both global and workspace-native
  discovery targets. The `zed` adapter maps the policy to native `AGENTS.md`
  and skills to Zed's `.agents/skills` catalog. The adapter-owned
  `antigravity-v4` support skill carries the globally readable routing and
  reference bundle because arbitrary files beside Zed's personal instruction
  file are not guaranteed to be readable by the Agent. Non-native router,
  workflow, role, metadata, and provenance copies live under the dedicated
  `antigravity/` namespace; only `AGENTS.md` and the skill catalog are direct
  runtime discovery surfaces. Its role contracts are labelled references
  because Zed's native Agent has no Markdown custom-agent registry; native
  `spawn_agent` and skill slash commands remain host/profile capabilities, not
  canonical role registration.

## 4. Internal Dependencies

- `../manifest.yaml`: declares supported adapters.
- `../schemas/adapter.schema.json`: defines the adapter contract.

## 5. Verification

- Run `python global/scripts/os.py validate`.
- Run adapter build smoke tests for every declared host.
