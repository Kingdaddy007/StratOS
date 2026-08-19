---
name: debugging
description: 'Use when diagnosing a failure, regression, crash, unexpected behavior, flaky test, integration fault, or incident. Separates evidence-led diagnosis from repair and supports diagnose, propose, implement, and incident-mitigate modes. Do NOT use for approved new implementation with no observed failure (use coding), or to choose a system structure (use architecture).'
---

# Debugging

## Purpose and boundary

Debugging is a controlled investigation, not a patch-generation loop. Turn an observed symptom into evidence, test competing explanations safely, then either repair the established mechanism or stop with an honest uncertainty, mitigation, escalation, or no-code conclusion.

Do not treat a stack-trace endpoint, a reporter's suspected file, a green test suite, or a plausible-looking patch as causal proof. Never claim to have inspected evidence or run a check that did not occur.

## Select the mode before acting

| Mode | Default authority | Outcome |
| --- | --- | --- |
| `diagnose` | Read-only | Evidence-led explanation, ranked hypotheses, and next safe observation. |
| `propose` | Read-only | Diagnosis plus the smallest repair or non-code action plan; no edit is applied. |
| `implement` | Scoped local edit only after explicit authorization | A narrowly justified repair with validation and reversal path. |
| `incident-mitigate` | Escalate to `incident-response` | Restore or contain impact through its just-in-time production approval gate; root-cause work remains separate. |

Default to `diagnose` when the user asks why something happens. Urgency does not grant implementation or production authority. Data integrity, authorization, privacy, secrets, irreversible state, or customer-impacting incidents require a narrower safety boundary and may need a human owner before mutation.

## Core loop

**Frame -> Observe -> Model -> Hypothesize -> Test -> Update -> Decide -> Repair or stop -> Verify -> Record.**

1. **Frame the symptom.** Separate observed from expected behavior, reporter interpretation, affected scope, time window, frequency, environment, and impact. Name known facts and missing facts.
2. **Observe available evidence.** Inspect the relevant error, test output, state, logs, traces, metrics, recent code/config/dependency changes, and boundary inputs/outputs that actually exist. A minimal or repeatable reproduction is valuable when safe and feasible; it is not a universal gate.
3. **Model the causal path.** Trace the relevant boundary: input, transformation, authorization, serialization, persistence, cache, configuration, timing, dependency, or client state. The visible crash may be downstream of the first invalid state.
4. **Maintain distinguishable hypotheses.** For each meaningful theory record its mechanism, evidence for and against, assumption, predicted observation, and smallest safe discriminator. Do not preserve a disproven theory because its patch seems attractive.
5. **Test for information, not activity.** Prefer the least invasive observation, replay, controlled fixture, comparison, or targeted experiment that can split the hypotheses. Use a known-good versus failing comparison or bisection only when the comparison order and oracle are reliable.
6. **Decide honestly.** Mark a cause as `confirmed`, `strongly supported`, `likely`, `unverified`, or `ruled out`. `No justified code change`, `mitigation without root cause`, and `insufficient evidence` are valid outcomes.
7. **Repair only behind the gate.** In `implement` mode, apply the smallest reversible change that addresses the established mechanism. Do not hide the symptom by deleting/skipping a test, swallowing an error, weakening a guard, or hard-coding an expected value.
8. **Verify the claimed mechanism.** Check the original symptom, the affected contract or invariant, genuinely similar sibling paths where applicable, and relevant side effects. Passing tests are evidence, not proof by themselves.

## Evidence and repair gate

A `confirmed` cause explains the observed behavior and survives a targeted causal check or controlled counterfactual in the inspected context. A `likely` cause has coherent supporting evidence but retains an important untested alternative. An `unverified` theory cannot authorize a repair.

Begin a local repair only when all four are true:

- the user has requested or explicitly approved `implement` mode;
- the mechanism is established to the level the risk requires;
- the patch is the smallest credible way to address that mechanism; and
- a failure-before/failure-after, invariant, differential, or other credible validation plus a reversal path is available.

Stop and report the safe next action when evidence remains contradictory, the oracle is invalid, the required experiment is unsafe, the patch expands beyond the mechanism, or a data/security/production action needs an approval that is absent.

## Load detail only when it changes the investigation

- For evidence cards, causal mapping, hypothesis records, comparison, or bisection, read [evidence-and-hypotheses.md](references/evidence-and-hypotheses.md).
- For a selected fault class—configuration, cache, integration, timing, UI, performance, or data/security—read [fault-class-map.md](references/fault-class-map.md).
- For repair authority, incident containment, high-risk data, or an incident handoff, read [incident-and-repair-boundaries.md](references/incident-and-repair-boundaries.md).
- For the complete routing guide and source snapshot, read [resource-index.md](references/resource-index.md).
- For behavioral regression checks on this skill, read [debugging-scenarios.md](evals/debugging-scenarios.md).

## Return a traceable result

For a small issue, state the symptom, evidence checked and missing, leading explanation with its label, and next safe action. For a substantive issue, also state:

```text
Symptom and impact:
Reproduction: confirmed | intermittent | not reproduced | unavailable with current access
Evidence: inspected facts, negative evidence, and unperformed checks
Hypotheses: label, mechanism, support/contradiction, next discriminator
Decision: stay read-only | propose | implement | mitigate | escalate | no justified code change
If repairing: scope, reason, rollback/reversal, validation, residual risk
```

## Non-negotiable checks

- Keep observation separate from explanation and mitigation separate from root cause.
- Preserve evidence and approval boundaries; do not create new production or data side effects during diagnosis.
- Make uncertainty and unperformed checks visible.
- Do not let an appealing patch outrun its causal evidence.
