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
  generated Markdown agent format.

## 4. Internal Dependencies

- `../manifest.yaml`: declares supported adapters.
- `../schemas/adapter.schema.json`: defines the adapter contract.

## 5. Verification

- Run `python global/scripts/os.py validate`.
- Run adapter build smoke tests for every declared host.
