# V4 Phase 6 - Debugging evidence synthesis

**Status:** completed research-to-asset batch  
**Date:** 2026-08-18  
**Scope:** `debugging` skill and `debug-issue` workflow only. Testing/verification is deliberately deferred to Prompt 4.

## Decision

Rebuild debugging around a bounded, evidence-led investigation loop rather than a fixed number of attempts, a universal reproduction gate, or “make the tests pass.” The result keeps the reusable judgement in `SKILL.md`, moves fault-specific procedures to conditional references, and makes authority explicit across diagnosis, proposal, local implementation, and incident containment.

## Evidence assessment

The supplied **Manus** report is the primary source. It is materially stronger because it separates empirical claims from practitioner guidance, states limitations, distinguishes root-cause confidence labels, and treats non-reproduction, mitigation, escalation, and no-code action as valid outcomes.

The supplied **Grok** report adds two useful practical contributions:

1. a known-good versus failing *differential slice* across code, configuration, dependencies, state, traffic, or time; and
2. adversarial behavioral fixtures that reject stack-trace anchoring, weak-test overfitting, and deceptive “success.”

It is not used as the primary authority. Its bibliography includes noisy secondary/social sources and its quantitative AI-agent claims are not independently adopted as OS rules. Its “reproduce before changing product code” guidance is preserved only as a strong preference when safe and feasible, never as a universal blocker for incidents, security, data integrity, or unavailable environments.

The limited durable external principles were checked on 2026-08-18:

- [OpenTelemetry's observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) describes distinct telemetry signals; V4 therefore treats logs, metrics, and traces as complementary evidence rather than a single proof source.
- [Google SRE's incident-management guidance](https://sre.google/sre-book/managing-incidents/) supports separating restoration/containment from later causal learning; V4 therefore separates `incident-mitigate` from root-cause confirmation.
- [Git's bisect documentation](https://git-scm.com/docs/git-bisect) supports ordered good/bad comparisons; V4 records that bisection finds a change point, not a causal mechanism by itself.

## What changed

| Asset | Change | Reason |
| --- | --- | --- |
| `global/skills/debugging/SKILL.md` | Replaced rigid repro/attempt/5-Whys rules with the evidence-led core loop, labels, repair gate, mode selection, output contract, and conditional resource routing. | Improve causal discipline without forcing the same ritual on every fault. |
| `global/skills/debugging/references/` | Added evidence/hypothesis, fault-class, incident/repair, and source-routing references. | Preserve useful depth while loading it only when it changes the investigation. |
| `global/skills/debugging/evals/` | Added eight safety and action-quality scenarios. | Test for correct action class, truthful evidence, and safe stopping—not patch plausibility alone. |
| `global/workflows/workflow-debug-issue.md` | Rebuilt as a v2 coordination contract using task-scoped state, mode-specific authority, explicit handoffs, and no duplicated debugging manual. | Remove stale paths, fixed state filename, universal flow, and hidden mutation risk. |
| `global/skills/debugging/agents/openai.yaml` | Updated UI-facing description and invocation prompt. | Keep Codex metadata consistent with the revised capability. |

## Preserved, moved, and rejected rules

### Preserved and strengthened

- State the observable symptom before treating a proposed cause as fact.
- Use evidence, boundaries, falsifiable hypotheses, targeted checks, targeted repair, and recurrence prevention.
- Prefer a minimal/reversible repair and make verification evidence visible.
- Keep incidents, data, authorization, secrets, and production actions behind their relevant authority gates.

### Moved into selective references

- Detailed fault-class first checks and false-positive risks.
- Causal evidence cards, hypothesis records, reproduction nuance, differential comparison, and bisection.
- Incident containment and high-risk repair boundaries.

### Explicitly rejected

- A deterministic reproduction command as the required entry ticket to every repair.
- A fixed number of hypotheses, failed attempts, or “five whys.” These are tools, not laws.
- Treating the deepest stack frame, an issue description, a green suite, or the first bad commit as causal proof.
- Treating a mitigation as root-cause confirmation.
- Editing/deleting tests, catching-and-ignoring errors, or hard-coding outputs to make a symptom disappear.
- Claims that the skill guarantees fault detection, absence of regressions, or debugging superiority from benchmark statistics.

## Verification plan and result

The package is checked for portable hyphen-case metadata, resource discovery, link integrity, absence of unresolved tokens/personal paths, workflow schema/state/route compatibility, mode-specific authority language, and behavior scenarios for stack-trace, configuration, cache, timing, third-party, no-change, data/security, and incident cases.

Repository validation and the full existing unit suite are run after this batch. The standalone skill validator remains unavailable because both available Python runtimes lack its `PyYAML` import; no dependency is installed for a documentation validator.

## Boundary with Prompt 4

Prompt 3 changes only debugging and its coordination workflow. It does not rewrite the `testing` skill, `test-strategy`, `verify-project`, or release verification policy. Those decisions wait for the dedicated Testing/Verification research so the OS does not manufacture its own evidence or blur debugging with assurance.
