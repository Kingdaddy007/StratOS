# V4 Phase 6 — Core integration drills

**Status:** completed safe contract-drill checkpoint  
**Date:** 2026-08-18  
**Scope:** Integration of the four research-updated universal capabilities: Product Thinking, Project Inception, Debugging, and Testing/Verification.

## Purpose

The first four Phase 6 updates must cooperate as an operating system, rather than read well in isolation. These drills test the canonical routing and authority contracts against seven realistic request shapes.

They are deliberately **not** A/B model scores, a simulated agent swarm, a claim that a live user project was built, or a release exercise. They prove that the authored repository exposes the expected routes, resources, handoffs, and mutation stops. A real-project pilot is still needed to test host discovery, human interaction, and model judgement in use.

## Drills and expected behaviour

| Drill | Correct entry | Core result | Stop or handoff that matters |
| --- | --- | --- | --- |
| Uncertain AI product | `project-inception` + `product-thinking` | A bounded decision packet, non-AI comparison, and smallest credible next action. | Sensitive data, tool authority, and representative evaluation route conditionally to Security, Architecture, and Testing; no implementation or project-context write. |
| Known causal regression | `debug-issue` + `debugging` | Evidence-led causal assessment. | `diagnose` remains read-only; an insufficient theory cannot authorize a repair; regression evidence can route to `test-strategy`. |
| Flaky check | `debug-issue` + `debugging`/`testing` | Treat instability as an unexplained fault. | No retry-until-green claim; investigate first, then choose durable evidence. |
| Material API/cache change | `test-strategy` + `testing` | Claim, risk, boundary, oracle, negative case, fixture, and residual-risk plan. | Planning is read-only until explicit `implement`; broader evidence routes to `verify-project`. |
| AI feature evaluation | `test-strategy` + `product-thinking`/`testing` | Separate deterministic guarantees, probabilistic quality evidence, and human/domain review. | Tool permission, data, and authorization concerns route to `security-audit`; an LLM judge is not the sole high-impact oracle. |
| Release request | `verify-project` + `testing` | Scope-qualified verification status and visible uncertainty. | Release execution stops at `ship-to-production` and requires just-in-time approval. |
| Small reversible correction | Direct work | One acceptance check, proportionate to consequence. | No forced inception, test strategy, workflow state, or agent delegation. |

The machine-readable scenarios are in [`tests/fixtures/v4_phase_6_integration_drills.json`](../tests/fixtures/v4_phase_6_integration_drills.json). They intentionally name conditional capabilities, rather than loading every capability for every drill.

## What passed

The contract checks confirm that:

1. Every drill references a real canonical skill, conditional resource, and entry workflow.
2. Each expected handoff is declared by its entry workflow.
3. An uncertain AI product starts as a read-only decision, includes non-AI comparison, and does not silently write project truth.
4. Diagnosis and flaky evidence remain read-only until causal evidence and explicit implementation authority exist.
5. Test strategy can plan credible evidence without pretending that a plan or green result authorizes a release.
6. AI-evaluation security concerns route separately, and `verify-project` remains read-only before `ship-to-production`.
7. A clear, low-consequence local correction can remain direct work.

## First real low-risk pilot

**Task:** Correct the stale final “What happens next” statement in `docs/v4-roadmap.md`.

**Observed inconsistency:** The roadmap’s Phase 6 checkpoint records that its four research-to-asset gates and safe integration drills are complete, while its final summary still says that Phase 6 is the next work to begin. Those claims cannot both be current.

**Route selected:** Direct local documentation maintenance. The request is clear, reversible, low-consequence, and has a local acceptance check. Under the Studio Router, no workflow is mandatory for a small reversible task; Product Thinking, Project Inception, Debugging, Testing, optional packs, research, and delegation are intentionally not loaded.

**Action and acceptance check:** Replace only the stale final summary with the current state: the universal core has completed its first low-risk pilot and the next planned scope is the separately bounded Phase 7 optional-pack audit. Confirm that the final summary agrees with the current Phase 6 checkpoint, no unrelated roadmap section changes, canonical validation passes, and the full repository test suite remains green.

**Result:** The route stayed proportionate and no core-contract gap appeared. This validates the “small reversible change” drill in an actual repository task, but it does not claim that direct documentation maintenance exercises every specialist capability or proves host/model behaviour in every workspace.

## Second real low-risk pilot

**Task:** Reconcile current skill-count documentation with the canonical manifest.

**Observed inconsistency:** `global/manifest.yaml` contains 71 skills and 52 workflows. `docs/v4-roadmap.md` already reports that current count, but the README said “72 registered skills” and the Phase 1 inventory table said “72 active domain packages.” The historical sentence that the inventory **began** with 72 is accurate and remains unchanged.

**Route selected:** Direct local documentation maintenance. The manifest is the registry of canonical current state, the correction is two user-facing lines, and verification is deterministic. No research, specialist pack, product framing, architecture, debugging, test strategy, or worker is needed.

**Action and acceptance check:** Change only the two stale current-state counts to 71, preserve the historical 72 statement, confirm the manifest parses as 71 skills and 52 workflows, then run canonical validation and the repository suite.

**Result:** This is a second successful direct-work pilot. It reinforces that the OS should choose a small evidence-backed correction instead of inventing process around a reversible documentation defect.

## Limits and next gate

This checkpoint verifies the **written system contract**. It cannot establish that every model will follow it under every ambiguous prompt, that a host discovers the generated payload correctly, or that a real application meets its own acceptance conditions.

The next Phase 6 gate is one **small, real, low-risk project pilot**. Use a bounded request with a clear workspace, then trace: request → selected route → resources actually loaded → evidence produced → handoff or stop. Do not open another universal skill rewrite before that pilot exposes a concrete gap.
