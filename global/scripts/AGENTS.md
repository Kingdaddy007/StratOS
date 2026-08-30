# Scripts Context & Contract

## 1. Purpose

This directory contains deterministic development, validation, build, and verification tooling for Anti-Gravity OS.

## 2. Rules & Constraints

- Keep core tooling dependency-free and compatible with the supported Python version.
- Treat `global/` as authored source and `dist/` as generated output.
- Never delete or overwrite files outside a caller-provided, validated target.
- Validation commands must be read-only unless the command explicitly documents generated output.
- Tool output must be UTF-8 safe and useful in non-interactive CI.

## 3. Exposed Interfaces

- `os.py`: `validate`, `build`, and `install` development CLI. `--profile` is the
  compatible single-pack shorthand; `--packs` safely composes Media, Growth,
  and Spatial with the implicit General base. Interactive installs ask for the
  General or Full option; automation can use `--option general|full`.
  `--antigravity-global` installs an Antigravity payload into the host's native
  global rule, agent, skill, and workflow discovery paths while preserving a
  namespaced rollback copy. `--antigravity-workspace` activates the same
  generated policy and resources in one existing project without changing
  GEMINI_HOME. `--codex-global` activates global Codex policy,
  skills, and custom-agent TOMLs; `--codex-workspace` activates them in one
  existing project without changing CODEX_HOME. `--zed-global` activates Zed's
  native AGENTS.md and global skill catalog (including the `antigravity-v4`
  routing support skill); `--zed-workspace` activates them in one existing
  project without changing Zed's global configuration. Zed installs require
  one of these explicit modes; the generic compatibility namespace is not a
  native Zed install.
- `verify.py`: project baseline verification runner; it does not declare deployment readiness.
- `checks/`: focused baseline scanners used by `verify.py`.

## 4. Internal Dependencies

- `../manifest.yaml`: canonical registry and build configuration.
- `../schemas/`: structural contracts validated by the CLI.
- `../adapters/`: host-specific build mappings.

## 5. Verification

- Run `python -m unittest discover -s tests -p "test_*.py"`.
- Run `python global/scripts/os.py validate`.
