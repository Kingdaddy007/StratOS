# Evidence, hypotheses, and differential checks

Load this reference when the issue is not immediately bounded, when two explanations remain plausible, or when a comparison or bisection could reduce uncertainty.

## Evidence card

Keep evidence factual and traceable. A compact card is enough:

| Field | Record |
| --- | --- |
| Observation | Expected and actual behavior, actor/input class, time window, environment, affected scope. |
| Artifact | Exact test output, log, trace, metric, request/response, state snapshot, diff, or configuration observation actually inspected. |
| Boundary | Where input, state, control, authorization, serialization, dependency, or output crosses a responsibility boundary. |
| Strength and limit | What the artifact supports and what it cannot establish. |
| Negative evidence | An expected observation that did not occur, or an explanation disproved by a result. |
| Missing evidence | The most decision-changing observation not yet available. |

Use traces, metrics, and logs as complementary signals rather than substitutes: a trace can show a path and timing, but it does not automatically explain the causal mechanism. Preserve timestamps, correlation identifiers, and environment details where available; do not expose secrets or sensitive payloads in a diagnosis record.

## Hypothesis record

Keep the set small enough to reason about. A good hypothesis is falsifiable:

```text
Label: unverified | likely | strongly supported | confirmed | ruled out
Mechanism: the causal explanation, not merely a file or symptom
Support: inspected observations that fit it
Contradiction: observations that weaken it
Assumption: what must be true for it to hold
Prediction: what should be observed if it is true
Discriminator: smallest safe observation or experiment that would distinguish it
Risk: side effect, cost, privacy, data, or production implication of that check
```

Do not use a numerical confidence score as a substitute for the support and contradiction. A `ruled out` label needs a failed prediction or incompatible evidence, not a hunch.

## Reproduction and controlled experiments

A minimal or repeatable reproduction is useful because it creates an oracle for experiments and later regression protection. It may be a targeted test, replay, controlled fixture, recorded request, state snapshot, or production-like observation. It is not required before every action:

- In a production incident, contain impact first through the incident route when authorized.
- In data integrity, security, privacy, or third-party cases, preserve evidence and respect access limits before attempting reproduction.
- When exact reproduction is unavailable, state that limitation and triangulate from independent evidence instead of fabricating certainty.

Choose the smallest safe experiment that can change the hypothesis ranking. Change one relevant variable where that yields a meaningful causal comparison; do not turn this into a ritual when the only safe action is inspection or escalation.

## Differential slice and bisection

Compare an ordered known-good and failing state when a stable oracle exists. A slice can compare:

- commits or generated artifacts;
- effective configuration, flags, runtime, dependency, or platform;
- request shape, authorization context, data snapshot, cache state, or feature path;
- traffic, load, time, clock, or schedule conditions.

Treat “what changed last” as a starting probe, not a diagnosis. A bisection identifies a change point; it does not, by itself, establish why the change caused the defect. Stop bisection if labels are flaky, the oracle is unstable, or the comparison alters risk-bearing state.

## Decision labels

| Label | Meaning | Minimum basis |
| --- | --- | --- |
| `confirmed` | Mechanism causally explains the observed failure in the inspected context. | Targeted causal evidence or counterfactual plus contract/invariant check. |
| `strongly supported` | One mechanism fits several independent signals and alternatives are materially weaker. | Coherent evidence with stated residual uncertainty. |
| `likely` | A plausible leading explanation remains meaningfully untested. | Supporting evidence and a named next discriminator. |
| `unverified` | A theory without enough evidence to guide a repair. | State it as a question, not a conclusion. |
| `ruled out` | A theory conflicts with an observation or failed its prediction. | Record the disconfirming evidence. |
| `no justified code change` | Code is not the responsible mechanism, the contract/oracle is wrong, or evidence does not support a safe edit. | Evidence and an owner/next observation or non-code action. |
