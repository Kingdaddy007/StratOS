# Extended Guidance

## Contents

- [Choose the right mode](#choose-the-right-mode)
- [Frame a decision and problem](#frame-a-decision-and-problem)
- [Review a requirement without becoming a gatekeeper](#review-a-requirement-without-becoming-a-gatekeeper)
- [Compare opportunities and scope](#compare-opportunities-and-scope)
- [Choose a credible test](#choose-a-credible-test)
- [Choose outcome checks and measurement](#choose-outcome-checks-and-measurement)
- [Run a proportional pre-mortem](#run-a-proportional-pre-mortem)
- [Product decision record](#product-decision-record)
- [Failure patterns](#failure-patterns)

## Choose the right mode

Use a direct change when the requested result, acceptance condition, and reversal path are clear. State the intended outcome and implement; do not manufacture research.

Use a product decision when a choice about problem, value, scope, priority, evidence, or experiment can materially change the work. The purpose is to make a better next decision, not to produce a product ceremony.

Use high-stakes treatment when a wrong decision could cause material harm, difficult rollback, lock-in, exposure of sensitive information, or a public commitment. The amount of work follows consequence and uncertainty, not job title, project size, or the length of a specification.

## Frame a decision and problem

Start with a sentence that can be proved wrong: **Decide whether/how to [action] for [actor/context] before [commitment].** Then identify:

- **Actor and stakeholders:** who uses, pays, approves, supports, is affected by, or can block the outcome?
- **Situation and progress:** what is happening now, what are they trying to accomplish, and why does it matter?
- **Alternative:** what do they do today—another tool, manual work, workaround, avoidance, or nothing?
- **Constraints:** time, trust, access, policy, integration, budget, skill, safety, or adoption constraints.
- **Value hypothesis:** if this change works, whose situation improves and in what observable way?

A Jobs-to-be-Done sentence can clarify thinking, but it is optional. Use plain language when that is clearer.

## Review a requirement without becoming a gatekeeper

For each consequential requirement, ask what outcome it serves, what would make the requirement unnecessary, and whether a lower-cost alternative exists. Classify it as core to the present decision, a plausible later addition, a constraint, or an unresolved assumption.

Do not refuse a small authorised change merely because it has no research package. Record the acceptance condition and any material ambiguity. Ask one focused question only if choosing the wrong interpretation would disappoint the requester or create meaningful cost.

Surface contradictions instead of silently selecting a winner. A requirement may be a workaround for confusing design, policy, process, or a missing default—not proof that new code is needed.

## Compare opportunities and scope

Compare only the factors that could change the choice:

| Factor | Question |
| --- | --- |
| Expected value | If this works, whose meaningful outcome changes? |
| Evidence confidence | What supports the claim, and what does it not prove? |
| Effort and burden | What build, maintenance, support, and coordination cost follows? |
| Opportunity cost | What meaningful work is displaced? |
| Risk and reversibility | What happens if it is wrong, and can it be undone? |
| Time sensitivity | Is there a real deadline, dependency, or cost of delay? |

Named scores are optional shorthand. Do not produce precision that the inputs cannot support. If the choice hinges on weak assumptions, prefer a cheap, discriminating learning step over arithmetic certainty.

For scope, compare a direct improvement, a narrow value slice, and a learning-focused test where those options are genuinely viable. State what is intentionally excluded and what evidence or trigger could justify revisiting it.

## Choose a credible test

Define the learning question before selecting a test. Separate at least these risks when relevant:

- **Problem/value risk:** does the actor have the problem, and does solving it matter?
- **Solution/usability risk:** can they understand and use the proposed experience?
- **Delivery/operational risk:** can it work reliably with real data, permissions, workflow, and support conditions?

| Need to learn | Suitable approach | What it cannot establish alone |
| --- | --- | --- |
| Whether people understand or see potential value | Sketch, clickable prototype, walkthrough, or task observation | Sustained real-world use or operational reliability |
| Whether a service/outcome is valuable before automation | Manual-backed or Wizard-of-Oz pilot | Long-term cost or full-scale feasibility |
| Whether integration, repeated use, latency, permissions, or reliability work | Narrow code pilot or staged delivery | Broad demand beyond the tested setting |
| Whether a clear, low-risk request works | Direct implementation with an acceptance check | General product-market claims |

Write a learning rule before the test: the actor/context, signal, time window, what would support or weaken the hypothesis, invalid test conditions, and the next decision. A useful test may be inconclusive; do not retrofit the conclusion after seeing the result.

## Choose outcome checks and measurement

Start with the desired change, then choose the lightest signal that can inform the next decision. A metric is a proxy, not the outcome itself.

Use production instrumentation when repeated use, material uncertainty, scale, safety, or delayed feedback justifies the cost. For a private tool, client site, early prototype, or low-frequency service, task observation, consented screen recordings, artefact review, short debriefs, support messages, a manual log, or a scheduled review may be more informative and less invasive.

Avoid metrics that can be easily gamed, confuse correlation with cause, or reward activity while hiding harm. Define a response before measuring: if the signal is below/above the agreed threshold, what will change?

## Run a proportional pre-mortem

For a consequential decision, imagine a failed outcome and list the few plausible causes that would materially change today's plan. For each, identify the earliest visible signal and a mitigation or safe stop.

Do not impose a fixed count of scenarios. A small reversible decision may need one check; a public, AI-enabled, or hard-to-reverse decision may need distinct failure, harm, oversight, and rollback analysis.

## Product decision record

```markdown
## Decision
[Build, test, defer, narrow, reframe, or escalate—and why now.]

## Problem frame
[Actor, situation, intended progress, alternative, constraints.]

## Value hypothesis and consequence
[Who benefits, expected change, and cost if wrong.]

## Evidence and limits
[Observed, reported, domain, technical, or behavioural evidence; what it cannot establish.]

## Dominant uncertainty
[The uncertainty most likely to change the decision.]

## Smallest credible next action
[Direct change, prototype, manual pilot, code pilot, staged delivery, or targeted research.]

## Learning or acceptance rule
[What would support, weaken, invalidate, or confirm the next step.]

## Scope boundary and opportunity cost
[Included, deliberately excluded, and what work is displaced.]

## Outcome check and next decision
[One or two signals, owner/timeframe where material, and the decision after evidence arrives.]
```

Add high-stakes fields only when needed: affected parties, harm boundaries, data/privacy/security constraints, representative evaluation, human oversight/correction/appeal, fallback, staged exposure, rollback, owner, and approval gate.

## Failure patterns

| Pattern | Correction |
| --- | --- |
| Feature-first delivery | Reframe the requested feature as a proposed solution; identify the problem and alternative. |
| Discovery theatre | Name the decision-changing uncertainty. If none exists, act proportionately. |
| “Users always lie” | Match reports and observed behaviour to the claims they can answer; investigate important disagreement. |
| Score worship | Expose the estimates, uncertainty, opportunity cost, and reversibility behind the score. |
| Analytics by default | Explain the decision the signal will inform; prefer a lighter signal when it is sufficient. |
| Cheap-but-invalid MVP | Preserve usability, trust, and safety needed for the test to mean anything. |
| AI by default | Compare a rule, existing tool, process, human service, or no-change baseline before adding probabilistic behaviour. |
