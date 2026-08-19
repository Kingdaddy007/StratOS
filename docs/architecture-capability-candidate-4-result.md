# Architecture Capability Candidate 4 — Result

**Candidate:** `tenant-trust-boundaries`  
**Scope:** Multi-tenant and privileged cross-boundary access design  
**Status:** `demote-to-reference` — not approved, installed, or activated as a global skill  
**Verified:** 2026-08-18

## Plain-English verdict

The compact architecture kernel already produced strong tenant-isolation answers. Candidate 4 added useful wording, but it did not create a repeatable improvement over the kernel. It also made the model mention tenancy in two tasks where tenancy was irrelevant.

That is not a security failure, but it is the kind of prompt-weight leakage this evaluation is designed to catch. The material remains valuable as a tightly scoped reference for a security or architecture workflow after a project has established that it is multi-tenant. It should not become an always-available capability or a standalone global skill.

## What was tested

Each run used fresh, projectless `gpt-5.6-luna` tasks at maximum effort with no tools or network access. Every task received one of these conditions:

| Condition | Material supplied |
| --- | --- |
| A | Project request only |
| B | Request plus compact architecture kernel |
| C | Request plus kernel and Candidate 4 |

The answers were captured with thread ID, timestamps, SHA-256 response hash, and a no-tools telemetry note. Independent Luna-Max reviewers saw only a guide and shuffled answers for their own scenario; they did not receive candidate text, conditions, answer keys, or the other scenarios. The revision scorecard passed the runner's structural validation.

The four scenarios were:

1. a shared B2B notes product with two organisation memberships and customer-approved support access;
2. a single-company equipment register, included to catch invented tenancy;
3. an unjustified twelve-microservice request; and
4. a local landing-page visual restyle.

## First run: Candidate 4 v1.0

The first run showed that the candidate could generate a comprehensive tenant answer and correctly avoid tenant machinery for the single-company control. However, the blinded reviewer found an irrelevant conditional tenant/support discussion in the microservices control. The real tenant answer ranked behind the compact kernel.

**Decision after v1.0:** `revise-and-retest`.

The revision narrowed activation to systems with independently authorised customer, organisation, workspace, or tenant boundaries, or privileged access crossing such a boundary.

## Revised run: Candidate 4 v1.1

| Scenario | A | B | C | Decoded finding |
| --- | ---: | ---: | ---: | --- |
| Shared multi-tenant notes | 15/16 | **16/16** | 15/16 | All were safe; kernel was clearest on policy and verification. |
| Single-company access control | **16/16** | **16/16** | 15/16 | C avoided tenant machinery, but left SSO versus administrator role authority ambiguous. |
| Microservices trap | 15/16 | **16/16** | 15/16 | C still included an irrelevant tenancy aside; it did not cause a topology error. |
| Landing-page restyle | **16/16** | **16/16** | 14/16 | C added a tenant-isolation sentence to a local visual task. |

Scores are the four declared scenario-focus dimensions, each 0–4. They aid comparison; they are not a universal architecture-quality score.

## Survival-gate assessment

| Gate | Result | Evidence |
| --- | --- | --- |
| No new critical security, integrity, or external-effect failure | Pass | C did not trust browser tenancy or invent a dangerous persistence model. |
| C improves target behaviour over B across relevant runs | Fail | The kernel ranked above C in the true multi-tenant scenario in both runs. |
| Gain is a decision improvement, not longer terminology | Fail | No measured C gain exists to attribute. |
| No unjustified architecture in controls | Fail | Both C4 v1.0 and v1.1 added irrelevant tenancy language to the microservices control; v1.1 also did so in the landing-page control. |
| Overridable for simpler facts | Partial | The single-company answer stayed proportionate, but the candidate condition still altered answer behaviour. |
| Cost and provenance recorded | Pass | Twelve execution records, response hashes, and blinded files exist for each run. Host token and cost telemetry were unavailable. |
| Repeatable improvement mechanism identified | Fail | The candidate's useful details were already supplied by the kernel or the capable model without repeatable lift. |

## Decision and next gate

Candidate 4 is demoted to a **conditional reference**. Do not author or install a global `tenant-trust-boundaries` skill from it.

If a future multi-tenant product has real project facts, a security/architecture workflow may load a concise reference covering server-derived membership, shared-boundary propagation, support-grant lifecycle, authoritative storage enforcement, and cross-tenant negative tests. It must be loaded only after the project is known to require those controls.

No further Candidate 4 rerun is justified unless new evidence shows that the compact kernel consistently misses a tenant-specific failure mode. The next architecture work is therefore not Candidate 5; it is consolidation: retain only candidates that pass replication, and build no runtime skill until the required independent result sets exist.

## Evidence locations

The raw responses, execution records, answer keys, blinded review folders, and validated revised scorecard are intentionally local temporary evidence:

- `tmp/architecture-pilot-tenant-luna-max-20260818/`
- `tmp/architecture-pilot-tenant-luna-max-20260818-blind/`
- `tmp/architecture-pilot-tenant-revised-luna-max-20260818/`
- `tmp/architecture-pilot-tenant-revised-luna-max-20260818-blind/`

They contain no secrets and are not required for the OS runtime or distribution.
