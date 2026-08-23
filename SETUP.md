# Anti-Gravity OS V4 Setup

Installation is a user-authorized operation. Reading this document does not authorize an AI assistant to modify global configuration.

## Supported hosts

| Installer choice | Host | Default location |
| --- | --- | --- |
| 1 | Google Antigravity 2.0 | Global `~/.gemini/` or one project workspace |
| 2 | Gemini compatibility | `~/.gemini/antigravity` |
| 3 | Codex | Global `~/.codex/` or one project workspace |
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

## Installation choices

For Antigravity and Codex, every interactive install first asks where V4 should operate:

- **Global:** available across projects. Active files go to the selected host's
  global discovery directories.
- **Workspace:** available only in one existing project. Active files go to that
  host's project discovery paths; global host configuration is unchanged.

It then asks which capability profile to install:

- **Option A — General Profile:** 6 canonical roles, 17 workflows, and the
  current General-profile skills. Spatial, Media, and Growth stay dormant.
- **Option B — Full System:** 6 canonical roles, 17 workflows, and all
  registered skills, including Spatial, Media, and Growth.

Antigravity exposes all six roles as host custom agents. Its built-in Main Agent
also becomes the Studio Director when the generated global `GEMINI.md` is
active. The Studio Director and five leads receive explicit Antigravity
collaboration tools; a lead may create bounded workers, while workers do not
receive recursive delegation capability. Codex keeps Studio Director as the
primary `AGENTS.md` role and exposes the other five as bounded custom-agent
TOMLs.

The counts come from `global/manifest.yaml`, so they stay current when the
registry changes. Use `--option general` or `--option full` for scripts and
CI. An omitted option keeps the existing non-interactive default: General.
Interactive Codex and Antigravity runs ask for Global or Workspace. Automated
runs should pass `--scope`/`-InstallScope`; when scope is omitted with
`--yes`/`-Yes` or redirected input, the safe compatibility default is Global.

The installer may replace only the dedicated `antigravity` namespace for compatibility hosts. Native Antigravity writes only its declared global files and directories. Codex writes only its declared native discovery files and keeps a rollback copy. It never clears a shared parent. Existing matching entries are staged and backed up under `.antigravity-backups/`; unrelated files remain untouched. When changing from Full to General, only entries listed in the installer's own previous record are moved to the backup. Failed activation restores the backup.

## Windows

### Google Antigravity 2.0

The installer asks whether you want Global or Workspace, then asks whether you
want General or Full. Use Global when you want V4 across new projects:

```powershell
.\install.ps1 -TargetHost antigravity -InstallOption general -DryRun
.\install.ps1 -TargetHost antigravity -InstallOption general -Yes
```

This installs the rule at `~/.gemini/GEMINI.md`, agents at
`~/.gemini/config/agents/`, skills at `~/.gemini/config/skills/`, and workflows
at `~/.gemini/config/workflows/`.

Use Workspace to test or activate V4 in one existing project only:

```powershell
.\install.ps1 -TargetHost antigravity -InstallScope workspace -WorkspacePath C:\path\to\project -InstallOption general -DryRun
.\install.ps1 -TargetHost antigravity -InstallScope workspace -WorkspacePath C:\path\to\project -InstallOption general -Yes
```

This installs the generated policy at `<project>/GEMINI.md` and discovers the
six agents, selected skills, and workflows from `<project>/.agents/`. It does
not change `~/.gemini/` and refuses to overwrite unmanaged project entries.

Start a fresh Antigravity conversation after installation so it reloads the
global configuration. For normal Anti-Gravity OS work, use `Main Agent`; the
generated global `GEMINI.md` makes it operate as Studio Director. You may select
`studio-director` when you want the explicit custom role. Both can invoke the
five leads. A directly selected lead can also create bounded workers and collect
their returns when the task justifies delegation.

### Gemini compatibility

Gemini compatibility uses a generated `GEMINI.md` payload in a namespaced
directory:

```powershell
.\install.ps1 -TargetHost gemini -InstallOption general -DryRun
.\install.ps1 -TargetHost gemini -InstallOption general -Yes
```

The canonical source remains in the repository; Gemini receives a generated copy under its `antigravity` namespace.

### Codex

The installer asks whether you want a Global or Workspace install, then asks
whether you want the General or Full profile. Preview the default global path:

```powershell
.\install.ps1 -TargetHost codex -InstallOption general -DryRun
.\install.ps1 -TargetHost codex -InstallOption general -Yes
```

For an explicit one-project install:

```powershell
.\install.ps1 -TargetHost codex -InstallScope workspace -WorkspacePath C:\path\to\project -InstallOption general -DryRun
.\install.ps1 -TargetHost codex -InstallScope workspace -WorkspacePath C:\path\to\project -InstallOption general -Yes
```

## macOS and Linux

```bash
chmod +x install.sh
./install.sh --host antigravity --option general --dry-run
./install.sh --host antigravity --option general --yes
./install.sh --host antigravity --scope workspace --workspace /path/to/project --option general --dry-run
./install.sh --host antigravity --scope workspace --workspace /path/to/project --option general --yes
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
python global/scripts/os.py install --host antigravity --target /path/to/project --option general --antigravity-workspace --dry-run
python global/scripts/os.py install --host antigravity --target /path/to/project --option general --antigravity-workspace --yes
```

### Codex global governance

Codex reads its global instructions from `AGENTS.md`, not from `GEMINI.md` and not from an arbitrary namespace. Build and review the direct Codex layout before installing it:

```bash
python global/scripts/os.py build --host codex
python global/scripts/os.py install --host codex --target ~/.codex --codex-global --dry-run
python global/scripts/os.py install --host codex --target ~/.codex --codex-global --yes
python global/scripts/os.py install --host codex --target /path/to/project --codex-workspace --dry-run
python global/scripts/os.py install --host codex --target /path/to/project --codex-workspace --yes
```

Global Codex installation keeps a complete generated copy at `~/.codex/antigravity/`, records the backup in `~/.codex/antigravity/installation.json`, and does not modify `config.toml`, `config.json`, permissions, plugins, or unrelated files. Workspace installation keeps its record under `.agents/antigravity/` and refuses to replace unmanaged project files. Start a new Codex task after a global installation so the global instructions reload.

Use `--profile spatial` only for interior, showroom, gallery, luxury-home, furniture, decor, staging, or architecture-adjacent work. General engineering is the default.

## Installed layout

The adapter's `content_root`, `instruction_target`, `skills_target`, and `workflows_target` determine the exact layout. For example:

- Native Antigravity installs `GEMINI.md` at `~/.gemini/` and discovers agents,
  skills, and workflows from `~/.gemini/config/`.
- Antigravity workspace installs `GEMINI.md` at the project root and discovers
  agents, skills, workflows, memory, and references from the project's
  `.agents/` tree. It does not modify the global `~/.gemini/` configuration.
- Gemini compatibility installs `GEMINI.md` with canonical content at its
  generated namespace root.
- Codex global installs `AGENTS.md` at `~/.codex/`, custom-agent TOMLs at
  `~/.codex/agents/`, and skills at `~/.codex/skills/`.
- Codex workspace installs `AGENTS.md` at the project root, TOMLs at
  `.codex/agents/`, skills at `.codex/skills/`, and V4 references under
  `.agents/`. Studio Director remains the primary `AGENTS.md` role; the five
  canonical specialist roles are real bounded custom agents.
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
