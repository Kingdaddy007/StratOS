---
id: security-audit
version: 2
status: active
intent: Independently examine a stated security-sensitive boundary, report evidence-backed risks and residual uncertainty, and preserve human authority over remediation and release decisions.
use_when: [a material authentication, authorization, sensitive-data, external-integration, file-input, payment, trust-boundary, security-incident, or security-assurance claim needs an independent review]
do_not_use_when: [the request is a routine code-style review, a narrow non-security bug diagnosis, a vague request for a guarantee that a system is secure, or no identifiable boundary/asset/claim exists]
inputs: [audit question and scope, affected assets and parties, architecture/current implementation evidence, data and authority boundaries, known controls and incidents, allowed access and requested mode]
required_resources: [applicable AGENTS.md files, security capability, relevant project contexts and architecture decisions, assurance review method, current primary sources only when a changing standard/provider claim is material]
mutation_class: read_only
approval_gates: [audit remains read_only, require explicit implement authority before a local remediation is applied through its owning workflow, require just-in-time approval before credentials, data repair, traffic, deployment, publication, communication, production containment, destructive action, or other external effect]
states: [received, scoped, mapped, examined, challenged, reported, remediation-pending, stopped]
outputs: [audit scope and evidence limits, asset/trust-boundary map, findings with severity and confidence, abuse/failure paths, remediation options, verification needs, residual risk, next owner]
verification: [trace each finding to observed code/configuration/behaviour or label it as a hypothesis, validate the finding against the actual boundary and authorization path where safely possible, separate exploitability from hardening advice, and record evidence that was unavailable]
failure_paths: [stop on missing scope/authority, unsafe access attempt, need for credentials or production probing, unsupported compliance claim, contradictory evidence, or discovery that remediation would cross a protected boundary]
resume_contract: task-scoped .agents/workflows/<task-id>.json following the workflows directory contract; record scope, evidence, findings, confidence, approvals, blockers, next action, owner, and timestamps
next_workflows: [debug-issue, plan-architecture, build-feature, database-migration, incident-response, verify-project, ship-to-production, none]
profiles: [general]
---

# Security Audit

## Purpose and boundary

This is an independent Assurance route. It finds and explains credible risks; it does not modify the system, execute an attack, access credentials, promise compliance, or certify that the system is secure.

Choose it when a named boundary or claim matters. For example: “Can one tenant read another tenant's data?”, “Does this upload flow have an unsafe trust boundary?”, or “What security evidence is needed before this release?” A normal code review or an unexplained failure uses its owning route instead.

## Scope before scanning

1. State the audit question, business consequence, affected users/parties, systems, data, and explicit exclusions.
2. Record what access and evidence are actually available. A missing environment, repository, configuration, production log, or credential is a limitation, not permission to infer the result.
3. Map asset ownership and trust boundaries: callers, identity changes, authorization points, data stores, third parties, administrative paths, and observability/control surfaces.
4. Select only relevant threat and failure lenses. Use a structured model such as STRIDE as a prompt for questions, not a checklist that manufactures vulnerabilities.
5. Ask the Systems Architect when the boundary/ownership model is unclear; ask Product when harm or user consequence is unclear. The Assurance Lead remains independent of implementation ownership.

## Examine the stated claim

For each plausible finding, record:

| Field | Required content |
| --- | --- |
| Claim | What might fail or be abused; do not present a guess as a confirmed vulnerability. |
| Evidence | Exact observed code/configuration/behaviour, source, date, and relevant boundary. |
| Preconditions | Identity, input, access, timing, configuration, or other conditions required. |
| Impact | Confidentiality, integrity, availability, safety, financial, privacy, or operational consequence. |
| Severity | `critical`, `high`, `medium`, `low`, or `info`, justified by realistic impact and exploit conditions. |
| Confidence | What is confirmed, what is inferred, and what would change the conclusion. |
| Next action | Bounded remediation proposal, further safe evidence, owner, and verification required. |

Focus on real control questions: who can invoke an action, how the authoritative boundary validates it, whether an object/tenant/resource path is checked, how untrusted input is handled at its use site, what secrets/data can be exposed, what a failed dependency permits, and how abuse would be detected. Do not replace project-specific evidence with slogans such as “always encrypt everything” or a generic list of headers.

## State and authority

| State | Required result | Next state |
| --- | --- | --- |
| `received` | Audit question, owner, and claimed boundary are identifiable. | `scoped` or `stopped` |
| `scoped` | Scope, permitted access, material assets, evidence limits, and exit are visible. | `mapped` or `stopped` |
| `mapped` | Trust boundaries, ownership, control points, and relevant failure/abuse paths are visible. | `examined` |
| `examined` | Findings, non-findings, and unverified questions are evidence-labelled. | `challenged`, `reported`, or `stopped` |
| `challenged` | Material findings receive independent challenge or architecture/product clarification. | `reported` or `stopped` |
| `reported` | Findings, limits, severity, confidence, remediation options, and owners are delivered. | `remediation-pending`, named next workflow, or `stopped` |
| `remediation-pending` | Exact implementation/production approval and verification path are stated. | Owning workflow or `stopped` |
| `stopped` | A safe stop and the evidence/authority gap are explicit. | Reopen only when the gap changes. |

No finding authorises a fix. Local repairs go to `build-feature` or `debug-issue` with explicit implementation authority. A live/customer-impacting security event goes to `incident-response`, which must obtain a separate just-in-time production approval before containment effects.

## Report and handoff

Deliver an assurance report with:

- scope, available evidence, and important exclusions;
- asset/trust-boundary map;
- confirmed findings, hypotheses, and meaningful non-findings separately;
- severity, confidence, impact, affected ownership, and minimal safe next action for each finding;
- verification required after a repair; and
- residual risk, including the exact reason an assurance claim cannot yet be made.

Use careful language: `confirmed for inspected scope`, `likely`, `needs verification`, or `not assessed`. Never say “secure,” “compliant,” or “safe for production” as a blanket conclusion.
