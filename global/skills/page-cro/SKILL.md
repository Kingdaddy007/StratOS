---
name: page-cro
description: >
  Diagnose or improve a website or product journey when the request concerns
  conversion, abandonment, findability, form completion, signup, checkout,
  onboarding, pricing, CTA placement, page friction, funnel analysis, or an
  experiment. Trigger on "CRO", "conversion rate", "not converting", "drop-off",
  "reduce friction", "A/B test", "shorten the form", or "move the CTA". Do not
  use for a fresh copy draft without diagnosis, a purely mechanical defect fix,
  or as authority to deploy, change pricing/consent, collect personal data, or
  make a conversion promise.
---

# Page CRO

## WHEN TO USE THIS

- Diagnose a marketing page, signup, form, onboarding step, pricing journey, modal, popup, or checkout where a user task or business outcome may be failing.
- Review proposed conversion changes for evidence quality, accessibility, privacy, autonomy, instrumentation, or experiment readiness.
- Plan proportionate validation for a material behavioural hypothesis.

## NEVER DO

- Never promise that a design, copy, CTA, form, or experiment will improve conversion.
- Never treat five seconds, above the fold, one CTA, no navigation, proof near a CTA, fewer fields, or any page pattern as a universal rule.
- Never hide material costs, manufacture urgency, obstruct cancellation or exit, weaken privacy choices, or degrade accessibility to improve a metric.
- Never turn an analytics correlation, benchmark, stakeholder assertion, persona, or hypothesis into a measured project result.
- Never launch an experiment, deploy a change, alter pricing or consent, publish a result, or create another external effect without required human approval.

## DECISION AND EVIDENCE TRIAGE

1. Define the decision, user task, audience/context, desired outcome, and consequence of being wrong. "Increase conversion" alone is insufficient.
2. Classify the work: mechanical correction, required accessibility/privacy/safety remediation, qualitative diagnosis, analytics diagnosis, staged change, controlled experiment, or no additional research.
3. Create a compact evidence register for material claims. Label direct observation, measured project result, validated analytics data, qualitative finding, stakeholder assertion, research pattern, benchmark, hypothesis, illustration, or unknown.
4. State known inputs, unknowns, and the strongest claim the evidence supports. Keep causal, associative, and qualitative findings distinct.
5. Use an objective acceptance criterion directly for a mechanical defect or required conformance correction. Do not slow required remediation with conversion experimentation.

## ACCESSIBILITY, AUTONOMY, AND PRIVACY GATE

Before discretionary optimisation, inspect the affected user task for relevant accessibility defects, unclear labels or errors, keyboard/focus problems, inaccessible escape routes, material hidden information, deceptive urgency, obstructed cancellation, consent issues, and unnecessary personal-data requests.

- Correct and verify known defect, conformance, privacy, or safety issues. Do not randomise them as CRO variants.
- Treat proof, urgency, scarcity, defaults, badges, navigation, and field count as conditional design choices. Use them only when they are truthful, relevant, accessible, and support the user task.
- Stop and escalate when jurisdiction, consent basis, sensitive data, children, profiling, price/contract terms, or material harm is unclear.

## MEASUREMENT AND METHOD SELECTION

For an analytics-based claim, verify event structure and live firing before interpretation. Record exposure unit, denominator, primary outcome, supporting outcomes, guardrails, event definition, identity/deduplication rule, attribution window, scope, and missing-data policy.

Choose the least costly valid method for the question:

| Need | Prefer | Not sufficient by itself |
| --- | --- | --- |
| Fix a defect or accessibility failure | Implement and verify against the requirement and task. | A/B testing. |
| Understand comprehension or task failure | Content review, accessibility audit, interview, or usability observation. | Funnel numbers alone. |
| Find a behavioural drop or measurement issue | Event audit, session/funnel analysis, and a baseline. | A plausible explanation. |
| Estimate a safe causal effect | Controlled experiment or staged rollout with guardrails. | A dashboard uplift without valid exposure/outcome data. |
| Evaluate a small reversible improvement | Proportionate review or staged change. | A large research process by default. |

Record why the selected method can answer the decision and why a less costly method cannot.

## HYPOTHESIS, EXPERIMENT, AND RESULT DISCIPLINE

- State a falsifiable hypothesis: mechanism, affected segment/context, proposed change, primary outcome, plausible adverse effects, and result that would weaken the hypothesis.
- Before a controlled experiment, record control/treatment, population, assignment/exposure, primary outcome, guardrails, practical decision threshold, duration/information threshold, exclusions, segmentation plan, data checks, and stopping logic.
- Do not stop or extend a test merely to find a preferred result. Distinguish uncertainty from practical importance. Report inconclusive when data cannot support the decision.
- Interpret results within their population, time window, implementation state, evidence quality, and guardrails. A "winner" is not a universal truth.

## REFERENCE LOADING RULES

- Load [references/evidence-and-method-selection.md](references/evidence-and-method-selection.md) for material CRO diagnosis, analytics interpretation, accessibility/privacy/autonomy review, method selection, experiment design, or result handoff.
- Load [references/experiments.md](references/experiments.md) only after a decision brief and hypothesis exist; select task-relevant candidates rather than treating the list as a backlog.
- Load [references/resource-index.md](references/resource-index.md) to select a resource and verify source scope. Do not load the package wholesale.
- Use `copywriting` when the primary task is writing or revising copy after CRO diagnosis. Use `testing` for implementation-level test strategy. Use `ui-ux` for interface design and accessibility detail. Use `security` when data/identity/authorisation boundaries become material.

## OUTPUT SHAPE

Return a decision document, not a generic list of conversion tips.

1. **Decision and user task** - audience, context, desired outcome, and consequence.
2. **Evidence status** - facts, assertions, hypotheses, missing data, and measurement quality.
3. **Accessibility, autonomy, and privacy gate** - remediation, guardrails, or escalation.
4. **Diagnosis or hypothesis** - mechanism, scope, alternatives, and confidence.
5. **Recommended method** - why it is valid and proportionate.
6. **Change or experiment plan** - only when justified; include primary outcome and guardrails.
7. **Decision gate** - implement/verify, research, experiment, ship, reject, or inconclusive; state required approval.

## NON-NEGOTIABLE CHECKLIST

1. Name the actual decision and user task.
2. Keep evidence class, scope, and uncertainty visible.
3. Fix required accessibility, privacy, safety, and defect issues instead of testing whether to fix them.
4. Validate measurement before making quantitative claims.
5. Choose the least costly valid method.
6. Keep material or external changes behind human approval.
