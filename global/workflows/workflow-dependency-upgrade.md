---
id: dependency-upgrade
version: 2
status: active
intent: Evaluate and, only when approved, apply a minimal dependency change with source, compatibility, verification, and rollback evidence; never treat a package-manager command as harmless local work.
use_when: [an existing dependency must be upgraded, patched for a documented issue, or assessed for a compatibility/security change]
do_not_use_when: [the task is selecting a new dependency, a local code refactor without package changes, a package-manager command has not been approved, or the affected project/package manager is unknown]
inputs: [named dependency and current/target version or issue, affected project/package manager, lockfile and current baseline evidence, stated reason, relevant official release/security notes, requested authority]
required_resources: [applicable AGENTS.md files, current manifest/lockfile/project commands, Systems Staff Engineering Assurance contribution only when the dependency and risk require it, verified official source materials]
mutation_class: dependency_or_network
approval_gates: [inspection and plan remain read_only, require explicit approval before any package-manager/network command, manifest or lockfile mutation, dependency installation, registry access, or compatibility change; require a separate just-in-time approval before a production release or external follow-up]
states: [received, baseline-framed, source-checked, impact-mapped, approval-pending, executing, verifying, closed, stopped]
outputs: [version/change rationale, baseline and impact record, source/compatibility evidence, approved change scope, changed manifests/lockfile if executed, verification results, rollback/correction path, residual risks]
verification: [check only approved project-native install/build/type/test/audit/behaviour evidence, compare against the captured baseline, record tool/network/environment limitations, and validate affected contracts rather than relying on a version bump alone]
failure_paths: [stop on unknown source/version/target, missing approval, unsafe registry/network action, incompatible peer/runtime constraint, failed verification, transitive uncertainty, or scope expansion beyond the named dependency change]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract; record dependency, versions, source evidence, baseline, impact, approvals, executed commands/results, blockers, rollback/correction, owner, timestamps, and next action
next_workflows: [plan-architecture, build-feature, security-audit, test-strategy, verify-project, ship-to-production, none]
profiles: [general]
---

# Dependency Upgrade

## Purpose and boundary

Dependencies can change build output, runtime behaviour, licences, supply-chain risk, compatibility, and the lockfile. This workflow first makes the proposed change inspectable. It stops before any package manager, registry, download, install, manifest, or lockfile action unless Beloved has explicitly approved that exact scoped mutation.

The safe default is a read-only recommendation. A vulnerability report, release note, or stale dependency does not itself authorise a network call or version change.

## Prepare the smallest credible change

1. Identify the dependency, current resolved version, desired version/range, affected package/workspace, package manager, runtime/toolchain constraints, and reason for change.
2. Capture the available baseline: current lock/manifest state, existing project checks and their actual status, and known affected behaviours. Do not manufacture a “passing baseline” when the environment cannot run it.
3. Consult the relevant official release, migration, security, compatibility, licence, and peer/runtime information. Separate confirmed source facts from speculation and from advisories that have not been verified for the current project.
4. Map direct, transitive, build, runtime, configuration, API, generated-output, and deployment effects. Involve Systems, Product, or Assurance only where that effect is material.
5. Choose the smallest version/scope that addresses the stated need. Do not bundle unrelated upgrades, reformatting, or dependency substitutions into the same request.
6. Define the exact approved commands/mutations, expected lockfile changes, project-native verification, and rollback/correction path.

## Approval gate

Before executing, present:

```text
Dependency and current -> target version:
Project/package manager and exact commands:
Expected manifest/lockfile/configuration changes:
Official source evidence and compatibility risks:
Verification plan and environment/network limits:
Rollback or correction path:
Exact approval requested:
```

Only run the approved action. A registry change, extra package, install, target, or scope change needs a new approval.

## State and delivery

| State | Required result | Next state |
| --- | --- | --- |
| `received` | Named change, project, and reason are visible. | `baseline-framed` or `stopped` |
| `baseline-framed` | Current dependency/lock state and actual baseline evidence/limits are recorded. | `source-checked` or `stopped` |
| `source-checked` | Relevant official facts and unresolved compatibility questions are visible. | `impact-mapped` or `stopped` |
| `impact-mapped` | Smallest scope, risks, verification, and rollback/correction path are explicit. | `approval-pending` or `stopped` |
| `approval-pending` | Exact package/network mutation request is ready. | `executing` or `stopped` |
| `executing` | Only approved commands and files are changed. | `verifying`, rollback/correction, or `stopped` |
| `verifying` | Actual project-native evidence is interpreted against the stated change. | `closed`, owning repair route, or `stopped` |
| `closed` | Versions, changes, evidence, limits, residual risks, and next owner are recorded. | Reopen only for a changed upgrade. |
| `stopped` | No mutation occurred or the correction/rollback status is explicit. | Reopen only with changed authority/evidence. |

Do not report “upgraded safely” based on a lockfile diff alone. Report the exact version change, commands run, verification scope, environment limits, unresolved advisories, and the rollback/correction result.
