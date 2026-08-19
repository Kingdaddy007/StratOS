# Project and release evidence

Load this reference when interpreting a project verification run, preparing a release recommendation, or deciding whether operational/progressive evidence is needed.

## Verification is not release approval

`verify-project` gathers and interprets local/project evidence. `ship-to-production` owns a requested production release and its just-in-time approval. A green command, build artifact, or pre-production run cannot authorize deployment or prove an untested production distribution.

Use one of the four status labels from `SKILL.md` and name the exact claim. A good result says, for example, “verified for the stated API compatibility cases in the local integration environment,” not “fully verified.”

## Verification record

Record the revision/artifact, scope, relevant instructions, commands/checks actually executed, test selection, environment and dependency/configuration context, fixtures or substitutes, results, skipped/blocked/flaky checks, evidence artifacts, known limitations, residual risk, and handoff recommendation.

Run inexpensive applicable checks early when they reduce uncertainty quickly, but let risk reorder the sequence. A security-sensitive boundary, failed migration rehearsal, or missing authorization check may be the fastest relevant blocker rather than a formatter or generic scan.

## Progressive release evidence

For high-impact changes where pre-release environments cannot represent production, a canary or staged rollout can provide additional evidence only when the project has an attributable comparison/baseline, relevant signals, an observation window, pause/rollback criteria, an owner, and the necessary external approval. It does not substitute for pre-release evidence or hide weak observability.

Canary design is project-specific: traffic, duration, signals, and thresholds must be justified by risk and system behavior. If a signal cannot distinguish the release from unrelated noise, state that limitation rather than treating a quiet canary as proof.
