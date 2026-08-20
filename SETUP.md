# Anti-Gravity OS V4 Setup

Installation is a user-authorized operation. Reading this document does not authorize an AI assistant to modify global configuration.

## Supported hosts

| Installer choice | Host | Default location |
| --- | --- | --- |
| 1 | Google Antigravity 2.0 | `~/.gemini/GEMINI.md`, `~/.gemini/config/` |
| 2 | Gemini compatibility | `~/.gemini/antigravity` |
| 3 | Codex | `~/.codex/antigravity` and Codex global files |
| 4 | Cursor | `~/.cursor/rules/antigravity` |
| 5 | Windsurf | `~/.codeium/windsurf/memories/antigravity` |
| 6 | OpenCode | `~/.config/opencode/antigravity` |

Each host receives a generated adapter payload. Canonical `global/` source is never installed directly. Antigravity's native global path is different from the Gemini compatibility namespace.

## Safe setup sequence

1. Inspect the selected installer or use the development CLI.
2. Run a dry-run.
3. Review the host, payload, exact target, changes, and backup path.
4. Approve the real installation explicitly.
5. Verify the adapter-declared instruction file exists after activation.

## Installation options

Every interactive install asks which system to install:

- **Option A — General Profile:** 6 custom agents, 17 workflows, and the
  current General-profile skills. Spatial, Media, and Growth stay dormant.
- **Option B — Full System:** 6 custom agents, 17 workflows, and all
  registered skills, including Spatial, Media, and Growth.

The counts come from `global/manifest.yaml`, so they stay current when the
registry changes. Use `--option general` or `--option full` for scripts and
CI. An omitted option keeps the existing non-interactive default: General.

The installer may replace only the dedicated `antigravity` namespace for compatibility hosts. Native Antigravity writes only its declared global files and directories. It never clears a shared parent. Existing matching entries are staged and backed up under `.antigravity-backups/`; unrelated files remain untouched. When changing from Full to General, only entries listed in the installer's own previous record are moved to the backup. Failed activation restores the backup.

## Windows

### Google Antigravity 2.0

Use the native global path when you want the custom-agent drop-down in new
projects:

```powershell
.\install.ps1 -TargetHost antigravity -InstallOption general -DryRun
.\install.ps1 -TargetHost antigravity -InstallOption general -Yes
```

This installs the rule at `~/.gemini/GEMINI.md`, agents at
`~/.gemini/config/agents/`, skills at `~/.gemini/config/skills/`, and workflows
at `~/.gemini/config/workflows/`.

Start a fresh Antigravity conversation after installation so it reloads the
global configuration. For normal Anti-Gravity OS work, select
`studio-director` from the agent menu. `Main Agent` is Antigravity's built-in
default, while `studio-director` is the custom Anti-Gravity OS coordinator.

### Gemini compatibility

Gemini compatibility uses a generated `GEMINI.md` payload in a namespaced
directory:

```powershell
.\install.ps1 -TargetHost gemini -InstallOption general -DryRun
.\install.ps1 -TargetHost gemini -InstallOption general -Yes
```

The canonical source remains in the repository; Gemini receives a generated copy under its `antigravity` namespace.

### Codex compatibility namespace

Preview and approve the namespaced Codex payload:

```powershell
.\install.ps1 -TargetHost codex -InstallOption general -DryRun
.\install.ps1 -TargetHost codex -InstallOption general -Yes
```

For a custom parent, identify the host explicitly:

```powershell
.\install.ps1 -GlobalConfig C:\path\to\host-config -TargetHost codex -DryRun
.\install.ps1 -GlobalConfig C:\path\to\host-config -TargetHost codex -Yes
```

## macOS and Linux

```bash
chmod +x install.sh
./install.sh --host antigravity --option general --dry-run
./install.sh --host antigravity --option general --yes
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
python global/scripts/os.py build --host antigravity
python global/scripts/os.py install --host antigravity --target ~/.gemini --option general --antigravity-global --dry-run
python global/scripts/os.py install --host antigravity --target ~/.gemini --option general --antigravity-global --yes
```

### Codex global governance

Codex reads its global instructions from `AGENTS.md`, not from `GEMINI.md` and not from an arbitrary namespace. Build and review the direct Codex layout before installing it:

```bash
python global/scripts/os.py build --host codex
python global/scripts/os.py install --host codex --target ~/.codex --codex-global --dry-run
python global/scripts/os.py install --host codex --target ~/.codex --codex-global --yes
```

The installer keeps a complete generated copy at `~/.codex/antigravity/`, records the backup in `~/.codex/antigravity/installation.json`, and does not modify `config.toml`, `config.json`, permissions, plugins, or unrelated files. Start a new Codex task after installation so the global instructions reload.

Use `--profile spatial` only for interior, showroom, gallery, luxury-home, furniture, decor, staging, or architecture-adjacent work. General engineering is the default.

## Installed layout

The adapter's `content_root`, `instruction_target`, `skills_target`, and `workflows_target` determine the exact layout. For example:

- Native Antigravity installs `GEMINI.md` at `~/.gemini/` and discovers agents,
  skills, and workflows from `~/.gemini/config/`.
- Gemini compatibility installs `GEMINI.md` with canonical content at its
  generated namespace root.
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
