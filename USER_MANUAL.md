# StratOS User Manual

## 1. Choose a profile

Use `general` for normal engineering, product, security, operations, testing, marketing, and general interface work. Use `spatial` only for interior, showroom, gallery, luxury-home, furniture, decor, staging, or architecture-adjacent experiences.

The spatial profile extends general behavior; it does not replace safety policy.

## 2. Activate project context

Global context templates are blank scaffolds. Copy only the needed files from `global/context_templates/` into `.agents/contexts/` in the active project.

An active context must declare:

```yaml
status: active
scope: project
project_id: your-project-id
updated_at: 2026-07-13T00:00:00Z
owner: your-name-or-team
confidence: verified
```

Do not treat unresolved placeholders, another project's context, or stale metadata as fact.

## 3. Understand workflow modes

- `diagnose`: read-only investigation and evidence
- `propose`: options, tradeoffs, and plans without implementation
- `implement`: authorized local changes with verification
- `incident-mitigate`: explicitly authorized containment or recovery work

A diagnosis request does not authorize a fix. Deployment, rollback, publishing, traffic changes, purchases, messages, and destructive operations require just-in-time approval.

## 4. Resume work safely

Each resumable task stores state in `.agents/workflows/<task-id>.json`. State identifies the workflow, mode, owner, thread, worktree, evidence, approvals, blockers, timestamps, lease, and archive status.

Parallel tasks require distinct task IDs. Do not restore the old shared `.agents/workflow-state.json` design.

## 5. Verify before completion

`workflow-verify-project` runs baseline scanners. A green baseline does not by itself mean a project is deployable.

Deployment readiness also requires the project's own applicable tests, type checks, build, integration checks, environment evidence, rollout plan, and explicit production approval.

## 6. Install and update

Run a dry-run first:

```bash
python global/scripts/os.py install --host gemini --target ~/.gemini --dry-run
```

The installer writes only to the dedicated `stratos` namespace. When replacing an existing namespace it creates a timestamped backup under `.stratos-backups/`. Files beside that namespace are outside its authority and remain untouched.

See `SETUP.md` for installation and `MIGRATION.md` for upgrades.
