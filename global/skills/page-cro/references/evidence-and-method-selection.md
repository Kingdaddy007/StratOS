# CRO Evidence and Method Selection

Load this reference before making a material CRO recommendation, interpreting behavioural data, or planning an experiment. Do not treat it as legal advice or a guarantee of conversion improvement.

## Decision Brief

Write one sentence that names the decision, user task, affected audience and context, desired outcome, and consequence of being wrong. "Increase conversion" is not a decision question.

| Weak brief | Decision-fit brief |
| --- | --- |
| Improve the landing page. | Determine whether first-time mobile visitors can identify service scope and the appropriate inquiry action without unnecessary abandonment. |
| Reduce form friction. | Determine whether removing a nonessential phone field increases completed valid submissions without increasing support contacts or consent errors. |
| Improve checkout conversion. | Determine whether a checkout change reduces payment abandonment without increasing refunds, chargebacks, accessibility failures, or privacy complaints. |

Use a known defect or conformance criterion directly for mechanical repairs. Do not force a CRO brief for a broken submission, an accessibility defect, or another correction with an objective acceptance criterion.

## Evidence and Claim Register

Label each material input and preserve its source, date, scope, confidence, and permitted wording.

| Class | Rule |
| --- | --- |
| Direct observation | Describe what was observed and its context; do not infer motive without support. |
| Measured project result | State metric, denominator, period, population, data-quality status, and uncertainty. |
| Validated analytics data | Confirm event validity and live firing before interpreting it. |
| Qualitative finding | State method, participants or artefact, and limits; do not generalise beyond the evidence. |
| Client or stakeholder assertion | Use as discovery input; do not present as independent proof. |
| Research-backed pattern or benchmark | State source and fit; never present as a project forecast. |
| Hypothesis | State the suspected mechanism, segment, proposed change, expected outcome, adverse effects, and disconfirming result. |
| Illustrative example or unknown | Label it; do not allow it to become a factual claim. |

## Safety, Accessibility, Privacy, and Autonomy Gate

Before discretionary optimisation, inspect relevant forms, navigation, interaction, hierarchy, pricing, consent, account creation, subscription, cancellation, urgency, and personal-data flows.

- Correct known accessibility, privacy, safety, or material-deception defects; do not withhold them as experiment variants.
- Keep labels, error paths, keyboard access, focus, escape routes, material terms, costs, and cancellation information available to users who need them.
- Never manufacture urgency, hide material information, obstruct cancellation, weaken privacy choices, or steer users toward more data sharing through deception.
- Escalate when legal basis, jurisdiction, sensitive data, children, profiling, material financial/health effect, or conformance target is unclear.

## Instrumentation Gate

For any analytics-driven conclusion or experiment, record the exposure unit, denominator, primary outcome, supporting outcomes, guardrails, event definitions, identity/deduplication rule, attribution window, traffic/device scope, and missing-data policy.

Validate event structure and live firing. Record the baseline or comparison window and known gaps. Do not invent quantitative confidence when analytics are absent or invalid.

## Select the Least Costly Valid Method

| Question or risk | Prefer | Do not assume |
| --- | --- | --- |
| Conformance or clear defect | Implement and verify against requirement and user task. | An A/B test is necessary. |
| Comprehension, findability, or task failure | Content review, accessibility audit, usability observation, or interview. | Dashboard data can explain why. |
| Funnel change or instrumentation doubt | Event audit, funnel/session analysis, and baseline comparison. | Association proves cause. |
| Safe, measurable causal decision with enough traffic | Controlled experiment or staged rollout with guardrails. | Any visible uplift is decisive. |
| Low-stakes reversible adjustment | Proportionate review or a staged change. | Research ceremony improves every small edit. |

Choose a method using the question, risk, traffic, observability, reversibility, and expected decision value. Explain why it can answer the question and why a cheaper or safer method is insufficient.

## Experiment Contract

When an experiment is justified, record before launch:

- control and treatment;
- eligible population, assignment unit, and exposure rule;
- primary outcome, guardrails, practical decision threshold, and intended duration or information threshold;
- exclusions, segmentation plan, data-quality checks, and stopping logic; and
- how repeated looks, multiple metrics, and post-hoc segments affect interpretation.

Never stop only because a dashboard looks favourable. Never extend or segment solely to find a preferred result. Report inconclusive when the evidence cannot support the decision.

## Result and Handoff Record

Report the estimate, uncertainty, population, time window, data-quality status, primary outcome, guardrails, relevant heterogeneity, external factors, and decision: ship, reject, iterate, observe, or inconclusive. State whether the evidence supports causation, association, or only a qualitative finding. Do not call a winning variant universally better.

## Source Snapshot

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): current W3C Recommendation; success criteria are testable, and WCAG does not address every user need. Verified 2026-08-19.
- [NIST/SEMATECH Process Improvement](https://www.itl.nist.gov/div898/handbook/pri/pri.htm): objectives, variables, design, measurement, analysis, interpretation, and confirmation for experimental work. Verified 2026-08-19.
- [FTC dark-pattern report](https://www.ftc.gov/news-events/news/press-releases/2022/09/ftc-report-shows-rise-sophisticated-dark-patterns-designed-trick-trap-consumers): deceptive practices such as obscured terms, difficult cancellation, false urgency, and privacy steering. Verified 2026-08-19.
- [Google Analytics event validation](https://developers.google.com/analytics/devguides/collection/protocol/ga4/validating-events): validate event payloads and verify implementation; platform-specific guidance. Verified 2026-08-19.
- [Mixpanel Experiments](https://docs.mixpanel.com/docs/experiments): planning, implementation, monitoring, and interpretation workflow; platform-specific guidance. Verified 2026-08-19.
