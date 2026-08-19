---
name: product-thinking
description: 'Use when deciding what, whether, when, or how much to build: clarifying a product problem, comparing opportunities, shaping a smallest credible test, choosing evidence, defining outcome checks, or assessing whether AI adds value. Do NOT use for a clear, low-risk approved implementation with an acceptance condition; use coding. Do NOT use to choose system boundaries or implementation architecture; use architecture.'
---

# PRODUCT THINKING

## WHEN TO USE THIS

- A request is feature-shaped but its user, outcome, or value is uncertain.
- The decision is whether to build, defer, narrow, test, buy, simplify, or stop.
- Several opportunities, scopes, or experiments compete for limited effort.
- A product, service, website, internal tool, or AI feature needs a credible outcome and learning path.
- A proposed change is consequential, difficult to reverse, or likely to create material operational burden.

## NEVER DO

- Turn a clear, reversible, low-consequence change into compulsory discovery work.
- Treat a request, roadmap item, score, interview, analytics event, or stakeholder opinion as proof on its own.
- Require named frameworks, customer interviews, analytics, A/B tests, MVPs, or personas when they cannot change the decision.
- Equate an MVP with poor quality. The test must be credible for the question it is meant to answer.
- Add AI because it is available. Compare the simplest non-AI, rule-based, or human-supported alternative first.
- Use this skill to approve a release, production change, or external action. Preserve the host's approval and safety gates.

## CORE OPERATING MODEL

Product Thinking is a decision-quality reflex, not a mandatory discovery phase. Start by naming the decision, the consequence of being wrong, and what information could actually change the next action.

| Mode | Use when | Minimum useful response |
| --- | --- | --- |
| Direct change | Intent and acceptance are clear; reversal is cheap; consequence is low. | State the intended outcome and acceptance check, then implement. |
| Product decision | The problem, scope, priority, value, or evidence is meaningfully uncertain. | Frame the problem, expose the dominant uncertainty, choose the smallest credible next action. |
| High-stakes decision | Harm, privacy, safety, security, financial, legal, reputational, access, public-commitment, or lock-in risk is material. | Expand the record for affected parties, failure boundaries, evidence gaps, safeguards, ownership, and reversal path. |

Escalate because consequence or uncertainty is high—not because a project is large or sounds important. A small change in a sensitive workflow can be high-stakes; a private, reversible prototype can stay lightweight.

## DECISION RULES

1. **Name the decision.** Is the next action to frame, choose, build, test, measure, defer, or escalate? Do not collect research without a decision it could change.
2. **Check consequence and reversibility.** Ask what happens if the choice is wrong, who absorbs the cost, and how easily it can be undone.
3. **Frame the problem before defending a solution.** Identify the actor, situation, intended progress, current alternative or workaround, constraints, and value hypothesis. A requester, user, approver, payer, supporter, and blocker may be different people.
4. **Match evidence to the claim.** Reports help with meaning, motivation, context, and constraints; observed behaviour helps with enacted behaviour in a defined context; domain expertise helps with feasibility and risk. Record important disagreement instead of declaring one type universally superior.
5. **Resolve the dominant uncertainty.** Seek only evidence that could change the decision. Choose the cheapest credible source or test, considering the cost of delay and of learning too late.
6. **Treat scores as assumptions.** RICE, ICE, impact-effort, and similar methods may expose assumptions, but they do not create truth. Show confidence, opportunity cost, dependencies, time sensitivity, and reversibility beside any score.
7. **Use the smallest credible test.** A prototype, manual-backed pilot, code pilot, staged delivery, or direct implementation should fit the learning goal. Minimum scope never means untrustworthy, unusable, or unsafe quality.
8. **Define the desired outcome before a metric.** Instrument only when the resulting signal is decision-relevant and worth its privacy, engineering, and interpretation cost. Observation, artefact review, short debriefs, support signals, manual logs, or an acceptance check can be stronger for small or low-frequency work.
9. **Start from the available context.** Existing products have traces such as workflow evidence, support history, and known failure points. Greenfield ideas need evidence about the problem, alternatives, adoption conditions, and the smallest credible test.
10. **Calibrate confidence to evidence.** Generic conventions and remembered patterns can support a starting hypothesis, not a high-confidence project conclusion. Use `low`, `medium`, or `high` confidence only when the evidence scope justifies it; state what would raise or lower confidence.
11. **Resolve product unknowns before technical commitment.** If context, tenancy, lifecycle, stack, identity, persistence, or acceptance conditions are unknown, resolve the dominant product question first. Keep endpoint, schema, library, and migration examples explicitly provisional until the relevant technical decision is in scope.

## AI PRODUCT FIT

Before proposing AI, answer these questions:

1. What user outcome needs improvement, and can a deterministic rule, existing tool, process change, or human service serve it better?
2. What unique value would AI add, and is augmentation preferable to full automation?
3. What is the cost of a wrong, uncertain, delayed, or unexplainable result?
4. What data is necessary, prohibited, or sensitive? Who can inspect, correct, override, or appeal the result?
5. How will representative cases be evaluated, and what is the fallback if the feature underperforms or fails?

For material risk, route the applicable implementation questions to Security, Architecture, Testing, and the relevant domain expertise. This skill identifies the product decision; it does not replace those disciplines.

## REFERENCE LOADING RULES

- Read [decision-modes.md](references/decision-modes.md) when producing a decision record, scoping an experiment, or deciding whether the task should stay direct, product-sized, or high-stakes.
- Read [evidence-and-experiments.md](references/evidence-and-experiments.md) when evidence conflicts, discovery is warranted, a test is being designed, or measurement choices could distort the decision.
- Read [ai-product-fit.md](references/ai-product-fit.md) when an AI capability, automation, agent, recommendation, or probabilistic model is proposed.
- Read [extended-guidance.md](references/extended-guidance.md) only for detailed facilitation, requirement review, opportunity comparison, or a substantive product brief. Inspect its Contents first and load only the relevant section.
- Use [resource-index.md](references/resource-index.md) to select a reference; do not load the full package by default.

## OUTPUT SHAPE

Use the smallest record that makes the next decision auditable.

**Direct change:** decision; intended outcome; one material assumption (if any); acceptance check.

**Product decision:** decision; problem frame; value hypothesis; dominant uncertainty; evidence and limits; smallest credible next action; learning or acceptance rule; scope boundary; one or two outcome checks; next decision.

**High-stakes decision:** expand the product-decision record with affected parties, harms and constraints, ownership, privacy/security/data boundaries, representative evaluation, human correction or appeal, staged exposure, rollback/fallback, and any required approval gate.

## NON-NEGOTIABLE CHECKLIST

- [ ] The decision and consequence of being wrong are explicit.
- [ ] The response is proportionate to uncertainty and reversibility.
- [ ] The problem is distinguished from the requested solution when that distinction matters.
- [ ] Evidence is labelled by what it can and cannot establish.
- [ ] The next action can change the decision or verify the requested outcome.
- [ ] Scope, quality, safety, and authority are not traded away to move faster.
