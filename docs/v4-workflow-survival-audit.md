# Anti-Gravity OS v4 Workflow Survival Audit

**Date:** 2026-08-19  
**Status:** audited; source migration is deliberately deferred until parity
proof exists.

## Decision rule

A workflow earns a live route only when the task benefits from at least one of:

- visible resumable state;
- a specialist handoff;
- an evidence record that must survive the conversation;
- a rollback, recovery, or observation gate;
- a just-in-time approval before a consequential mutation.

If a route is mainly a method for one lead, it is a candidate for demotion to a
skill, reference, or agent procedure. Demotion is not deletion. Its useful
content must first have a named destination and a parity test.

## Live inventory and disposition

The live manifest contains **17 active workflows**. Historical counts do not
override this inventory. Trading is not an active V4 profile or workflow.

| Workflow | Survival reason | Disposition | Destination or parity owner |
|---|---|---|---|
| `build-feature` | Cross-concern handoff, implementation authority, verification, rollback | Keep | Staff Engineer + Studio Director; retain delivery state |
| `commercial-decision-record` | Durable evidence, claim challenge, human approval, supersession | Keep | Product Strategy; retain decision record |
| `database-migration` | Durable data risk, rehearsal, recovery, target-specific approval | Keep | Systems Architect + Staff Engineer; retain migration state |
| `debug-issue` | Evidence-led diagnosis, bounded repair, incident handoff | Keep | Staff Engineer; retain symptom and hypothesis evidence |
| `dependency-upgrade` | Network/package mutation, compatibility, supply-chain and rollback gate | Keep | Systems Architect + Assurance; retain approval and baseline |
| `design-ui` | Usually a single lead method; no durable state unless a material design contract is created | Demote candidate | Design Director procedure; preserve parity for material design records |
| `incident-response` | Live harm, containment approval, observation window, recovery evidence | Keep | Assurance + Systems Architect; retain incident timeline |
| `live-learning-loop` | Durable experiment, stopping rule, learning owner, supersession | Keep | Product Strategy; retain learning record |
| `os-maintenance` | Changes the governing OS, requires validation, rollback, and scope control | Keep | Studio Director + Assurance; retain maintenance state |
| `plan-architecture` | Durable boundary decision, alternatives, failure paths, reversibility | Keep | Systems Architect; retain architecture decision record |
| `project-inception` | Uncertain initiative needs shared truth, first slice, authority, and next route | Keep | Product Strategy + Studio Director; retain project packet |
| `security-audit` | Independent review, trust-boundary evidence, severity, remediation handoff | Keep | Assurance; retain read-only audit record |
| `ship-to-production` | External hard gate, exact target, approval, observation, rollback | Keep | Assurance + Staff Engineer; retain release record |
| `spatial-project-inception` | Optional spatial evidence/reference gates and profile-specific direction | Keep | Design Director; retain spatial project state |
| `task-dispatch` | Bounded delegation decision can remain with Studio Director and agent contracts | Demote candidate | Studio Director procedure + agent return contract; parity test required |
| `test-strategy` | Often a testing method; durable workflow is needed only for material evidence plans | Demote candidate | Testing skill + Assurance procedure; retain a record when the claim is material |
| `verify-project` | Usually a read-only assurance procedure; release and audit routes already provide hard gates | Demote candidate | Assurance procedure; parity test must preserve evidence-scope reporting |

## Findings

1. There is no safe basis for deleting a workflow in this audit. The four
   demotion candidates still contain useful content and remain live until their
   destination and parity tests are implemented.
2. `dependency-upgrade` remains a workflow because package-manager and network
   actions have a distinct approval and rollback boundary. It should not be
   collapsed merely because its happy path is familiar.
3. `design-ui`, `task-dispatch`, `test-strategy`, and `verify-project` are the
   strongest demotion candidates because their ordinary path is a lead method,
   not a durable multi-state operation. They still become workflows when a
   material handoff, evidence record, or gate makes state valuable.
4. `spatial-project-inception` remains profile-gated. General work must not
   load its spatial references or routes.

## Next gate before source migration

For each demotion candidate, add a destination procedure and a positive/negative
routing fixture. Only then may the workflow be marked `archived` or removed
from the manifest. Until that happens, this document is the decision record and
the current source files remain protected.
