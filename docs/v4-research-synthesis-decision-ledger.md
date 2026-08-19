# Anti-Gravity OS v4 — Research Synthesis Decision Ledger

**Status:** active implementation baseline  
**Date:** 2026-08-19  
**Scope:** the three supplied AI-native product-studio research reports and the live V4 canonical source

## 1. Decision

The three reports are sufficient to guide selective V4 implementation. They do
not justify rewriting the whole skill library, adding a permanent agent swarm,
or creating a new general AI-engineering mega-skill.

The durable direction is:

- one accountable Studio Director;
- a small number of bounded functional agents;
- human authority for taste, truth, rights, money, publication, release, and
  other consequential effects;
- skills loaded only when their judgement, reference, safety boundary, or
  evidence method is useful;
- workflows reserved for state, handoff, evidence, rollback, or approval;
- risk-scaled verification and explicit residual uncertainty; and
- General as the default, with Spatial, Media, and Growth as optional packs.

Most remaining work is contract, evidence, routing, and pilot work. It is not
the creation of more standalone skills.

## 2. Source provenance and confidence

| Report | Provenance | Strongest contribution | Confidence for V4 |
| --- | --- | --- | --- |
| Wide Research Report — AI-Native Product Studio Benchmark | Manus AI; 19 August 2026 | Creative direction, reference abstraction, media, growth, ethical claims, and optional profiles | High for boundaries; medium for creative/commercial outcome claims |
| Independent Capability Map for an AI-Native Product Studio Harness | Manus AI; current through 19 August 2026 | Main-agent control, project truth, delegation, evidence, stopping, and bounded specialists | High for operating principles; medium for exact local thresholds |
| High-Reliability AI-Assisted Software and Product Delivery | Manus AI; 19 August 2026 | Repository reconnaissance, intended-behaviour verification, causal debugging, security, release, and incident controls | High for delivery principles; medium for studio-specific causal lift |

These are three domain reports, not three independent model opinions. Their
shared author and related evidence base increase coherence but reduce
independence. Real Anti-Gravity pilots remain the decision gate for claims
about quality lift, speed, creativity, or specialist value.

## 3. Cross-report conclusions

| Accepted conclusion | Canonical home | Decision |
| --- | --- | --- |
| Accountable main agent with selective specialist help | `global/GEMINI.md`, `global/GLOBAL_MEMORY.md`, `global/agents/` | Keep |
| Explicit authority and untrusted-content boundaries | `global/baselines/`, main policy, agent contracts | Keep |
| Layered project truth with provenance and freshness | `global/context_templates/`, task state schemas, project context | Strengthen the general decision/evidence record |
| Evidence-gated completion | Workflow metadata, testing, review, release routes | Keep; prove with fixtures and pilots |
| Risk-scaled assurance | Router, workflow gates, testing, security, incident, release | Keep; calibrate on real work |
| Causal debugging and intended-behaviour oracles | `debugging`, `testing`, `debug-issue`, `test-strategy` | Keep; validate on a real defect and feature |
| Reference abstraction instead of imitation | `reference-intelligence`, Design Audit library | Keep; preserve human originality decision |
| Optional Spatial, Media, and Growth packs | Manifest, agents, router, references | Keep; prevent profile leakage |
| One provider-neutral video front door | `video-generation` plus references | Keep; do not restore 23 provider skills |
| No permanent agency-style swarm | Agent contracts and task dispatch | Keep as a hard boundary |

## 4. Confirmed gaps and smallest durable response

| Gap | Smallest response | New standalone skill? |
| --- | --- | --- |
| Research lacks source tiers, falsification, stopping, and cross-report synthesis | Upgrade `research-analysis` and add a focused eval set | No |
| General decision/evidence fields are split across templates | Add one general `decision-evidence-record` template; keep commercial ledgers specialised | No |
| Specialist return fields are mostly prose | Add a shared return contract to agent documentation/schema and routing fixtures | No |
| Workflow count and dispositions have historical drift | Run a survival audit against the 17 live workflows before any retirement | No |
| Local quality lift is unproven | Add a small private capability pilot and real-task drills | No |
| Native Antigravity distribution is not present in current `dist/` | Generate and smoke-test `dist/antigravity/` after source validation | No |
| Trading directory remains as a dangling unregistered folder | Quarantine/remove only the exact empty/non-canonical directory after preservation check | No |

## 5. Current live source truth

The live manifest is the inventory authority:

- 48 registered skills;
- 17 registered workflows;
- 6 registered agents;
- 4 profiles: `general`, `spatial`, `media`, and `growth`;
- no active Trading profile or manifest entry.

The 17 workflow files match the manifest. The `global/skills/` directory still
contains a dangling `deriv-bot-engineering` directory without `SKILL.md`; it is
not an active capability and must not be treated as canonical source.

Historical ledgers that describe 71 skills or 52 workflows remain useful as
provenance. They do not override the current manifest or this ledger.

## 6. Rejected additions

Do not add any of the following from the reports:

- a giant always-loaded prompt;
- a universal RAG, memory, or vector-database layer;
- one specialist agent for every task;
- a universal story, luxury, or conversion formula;
- autonomous outreach, publication, spending, or production release;
- a provider-specific permanent doctrine from dated documentation;
- a standalone skill for ordinary summarising, brainstorming, drafting, or
  comparison;
- a permanent workflow for a local reversible operation; or
- claims of zero bugs, perfect security, or universal model superiority.

## 7. Implementation gates

1. Upgrade the research method and add the general evidence record.
2. Normalize agent return contracts and test authority boundaries.
3. Audit every live workflow and record keep/demote/archive decisions.
4. Audit skills by capability and trigger; do not optimise the count.
5. Run representative private and real-task pilots.
6. Generate the native Antigravity payload and verify all profile routes.
7. Update the roadmap, manifest-derived documentation, and release notes only
   after the preceding evidence exists.

## 8. Implementation checkpoint — 2026-08-19

Gates 1–3 are implemented. `research-analysis` now has source grading,
claim labels, falsification, cross-report synthesis, and a practical stopping
rule. The general `decision-evidence-record` is registered in the manifest.
Every canonical agent now declares a machine-checked return and delegation
contract, and the generated Antigravity agents expose those contracts.

The 17-workflow survival audit is recorded in
[`v4-workflow-survival-audit.md`](v4-workflow-survival-audit.md). No workflow
was deleted. A ten-case private pilot fixture is ready in
[`tests/fixtures/v4_private_pilot.json`](../tests/fixtures/v4_private_pilot.json),
but no real project outcome claim is made until Beloved runs the pilot on
representative work.

Antigravity General, Spatial, Media, and Growth payloads build successfully
under `dist/antigravity/`. The empty Trading directory could not be removed by
the restricted shell in this run; it contains no active `SKILL.md`, is outside
the manifest, and remains a release-hygiene cleanup item.

## 9. Acceptance rule

An asset changes status only when its proposed destination, preserved content,
trigger, exclusions, evidence requirement, and verification test are recorded.
No deletion, host installation, commit, push, or publication is authorised by
this ledger alone.
