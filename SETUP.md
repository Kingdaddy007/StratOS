# StratOS 3 Setup

Installation is a user-authorized operation. Reading this document does not authorize an AI assistant to modify global configuration.

## Supported hosts

| Installer choice | Host | Default namespace |
| --- | --- | --- |
| 1 | Gemini | `~/.gemini/stratos` |
| 2 | Codex | `~/.codex/stratos` |
| 3 | Cursor | `~/.cursor/rules/stratos` |
| 4 | Windsurf | `~/.codeium/windsurf/memories/stratos` |
| 5 | OpenCode | `~/.config/opencode/stratos` |

Each host receives a generated adapter payload. Canonical `global/` source is never installed directly.

## Safe setup sequence

1. Inspect the selected installer or use the development CLI.
2. Run a dry-run.
3. Review the host, payload, exact target, changes, and backup path.
4. Approve the real installation explicitly.
5. Verify the adapter-declared instruction file exists after activation.

The installer may replace only the dedicated `stratos` namespace. It never clears its shared parent. An existing namespace is staged and backed up under `.stratos-backups/`; unrelated files in the parent remain untouched. Failed activation restores the backup.

## Windows

### Gemini

Gemini uses the generated `GEMINI.md` adapter payload. Preview and approve the normal namespaced install:

```powershell
.\install.ps1 -IDE 1 -DryRun
.\install.ps1 -IDE 1 -Yes
```

The canonical source remains in the repository; Gemini receives a generated copy under its `stratos` namespace.

```powershell
# Preview; no target files are written
.\install.ps1 -IDE 2 -DryRun

# Install Codex after reviewing the preview
.\install.ps1 -IDE 2 -Yes
```

For a custom parent, identify the host explicitly:

```powershell
.\install.ps1 -GlobalConfig C:\path\to\host-config -TargetHost codex -DryRun
.\install.ps1 -GlobalConfig C:\path\to\host-config -TargetHost codex -Yes
```

## macOS and Linux

```bash
chmod +x install.sh
./install.sh --ide 1 --dry-run
./install.sh --ide 1 --yes
```

For a custom parent:

```bash
./install.sh --global-config /path/to/host-config --host gemini --dry-run
./install.sh --global-config /path/to/host-config --host gemini --yes
```

## Payload availability

Release packages contain prebuilt `dist/<host>/` payloads and do not require Python. A source checkout without a payload requires Python 3.10 or newer so the installer can run:

```bash
python global/scripts/os.py build --host <host>
```

If neither a prebuilt payload nor Python is available, installation stops without changing the target.

## Development CLI

```bash
python global/scripts/os.py validate
python global/scripts/os.py build --host gemini
python global/scripts/os.py install --host gemini --target ~/.gemini --dry-run
python global/scripts/os.py install --host gemini --target ~/.gemini --yes
```

### Codex global governance

Codex reads its global instructions from `AGENTS.md`, not from `GEMINI.md` and not from an arbitrary namespace. Build and review the direct Codex layout before installing it:

```bash
python global/scripts/os.py build --host codex
python global/scripts/os.py install --host codex --target ~/.codex --codex-global --dry-run
python global/scripts/os.py install --host codex --target ~/.codex --codex-global --yes
```

The installer keeps a complete generated copy at `~/.codex/stratos/`, records the backup in `~/.codex/stratos/installation.json`, and does not modify `config.toml`, `config.json`, permissions, plugins, or unrelated files. Start a new Codex task after installation so the global instructions reload.

Use `--profile spatial` only for interior, showroom, gallery, luxury-home, furniture, decor, staging, or architecture-adjacent work. General engineering is the default.

## Installed layout

The adapter's `content_root`, `instruction_target`, `skills_target`, and `workflows_target` determine the exact layout. For example:

- Gemini installs `GEMINI.md` with canonical content at the namespace root.
- Codex installs `AGENTS.md` at the namespace root and canonical content under `.agents/`.
- Cursor, Windsurf, and OpenCode use their adapter-declared instruction and discovery paths.

Every payload also includes `adapter.json`, `profile.json`, the manifest snapshot, baselines, schemas, context templates, skills, workflows, and their required references.

## Activate project context

Do not edit global templates with project facts. Copy only the needed templates into the project:

```text
.agents/contexts/
```

Set `status: active`, the project ID, update time, owner, and confidence. Until then, the files remain scaffolds rather than project truth.

## Upgrade

Read [`MIGRATION.md`](MIGRATION.md) before upgrading a version 2 installation. Do not manually merge the removed duplicate workflow tree or restore machine-local project registration files.
