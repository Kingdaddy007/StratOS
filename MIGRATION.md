# Migrating to Anti-Gravity OS V4

Version 4 replaces duplicated, host-coupled configuration with canonical source,
generated adapters, profiles, and native Antigravity custom-agent discovery.

## Before migration

1. Commit or copy any personal changes from the existing installation.
2. Identify project-specific contexts, memory, project registrations, and permission grants. Keep them local; do not copy them into the OS source.
3. Run the new installer with `--dry-run` or `-DryRun`.
4. Review the selected host, target namespace, changes, and backup location.

## Path changes

| Previous path | Version 4 path |
| --- | --- |
| `global/contexts/` | `global/context_templates/` |
| `.agents/workflow-state.json` | `.agents/workflows/<task-id>.json` |
| `global/global_workflows/` | generated host workflow directory |
| spatial content as global default | optional `spatial` profile |
| compatibility `~/.gemini/antigravity` for native Antigravity | native `~/.gemini/GEMINI.md` plus `~/.gemini/config/agents`, `skills`, and `workflows` |

The old `global/contexts/` path contains a compatibility notice for one release. Duplicate workflow source is not retained.

## Skill and workflow IDs

Skill IDs are now portable, folder-matching, and hyphen-case. Workflow IDs omit the `workflow-` prefix in metadata, while filenames remain `workflow-<id>.md` for readability.

Host-specific fields belong in adapters or generated metadata, not canonical frontmatter.

## Installation behavior

The installer no longer clears a host configuration directory. Compatibility
hosts receive a namespaced payload. Native Antigravity receives only the
declared global rule, agents, skills, and workflows. It stages changes, backs
up matching entries under `.antigravity-backups/`, and activates atomically.
When a recorded Anti-Gravity profile is reduced, only its recorded entries are
moved to the backup; unrelated host files are preserved.

If migration fails after backup creation, the previous namespace is restored.

## Git history

Machine-specific project registrations have been removed from the current tree.
Version 4 does not rewrite Git history automatically. Repository owners who need
historical removal should perform a separately reviewed history-sanitization
operation and rotate any exposed credentials or permissions.

## Validation

After migration, run:

```bash
python global/scripts/os.py validate
python -m unittest discover -s tests -p "test_*.py"
```

Then build the selected host and inspect its generated payload before installation.
