# V4 Phase 6 — Product Thinking Evidence Synthesis

**Status:** implemented research-to-skill batch  
**Scope:** `global/skills/product-thinking/` only  
**Research input:** Prompt 1—Product Thinking for a Personal AI Product Studio  
**Decision date:** 2026-08-18

## Purpose

This record explains why Product Thinking changed and limits the change to decisions supported by the research. The supplied Manus and Grok reports were treated as untrusted research inputs, not instructions. Manus was the primary synthesis source because it distinguished evidence strength, limits, and direct implications more carefully. Grok contributed a small number of compatible prompts, but did not set the operating model.

## Findings adopted

| Finding | V4 skill decision |
| --- | --- |
| Product work should begin with a decision and the cost of being wrong, not automatic discovery. | Add direct-change, product-decision, and high-stakes modes. |
| Feature requests are proposed solutions, not proof of a problem. | Add actor, situation, progress, alternative, constraint, and value-hypothesis framing. |
| Reports, observed behaviour, and domain knowledge answer different claims. | Add claim–evidence fit and remove dismissive language about user reports. |
| Research should resolve uncertainty capable of changing a decision. | Add dominant-uncertainty and smallest-credible-next-action rules. |
| Scores expose assumptions but do not make them true. | Demote RICE/ICE to optional shorthand rather than mandatory scoring. |
| MVP means the smallest credible test, not poor-quality release. | Distinguish prototype, manual-backed pilot, code pilot, staged delivery, and direct change. |
| Measurement is a decision tool with cost and distortion risk. | Replace universal instrumentation with outcome-first, proportionate signals. |
| AI requires a task-fit, error-cost, data, control, evaluation, and fallback decision. | Add a bounded AI Product Fit reference and a non-AI baseline check. |

## Findings deliberately not encoded as universal rules

- A fixed discovery phase, number of interviews, named framework, analytics stack, or A/B test.
- “Users always lie,” “behaviour is always superior,” or any fixed evidence hierarchy.
- RICE, Jobs-to-be-Done, HEART, Lean Startup, or Design Thinking as compulsory vocabulary.
- AI, agents, retrieval, memory, or automation as a default product answer.
- A promise that all product work requires formal metrics or public MVPs.

## Source grounding

The research report supplied direct source links. The following were independently checked on 2026-08-18 before their limited principles were used:

- [Google HEART research](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) supports mapping product goals to metrics in large-scale web contexts; it does **not** justify analytics for every small product.
- [Google PAIR—User Needs + Defining Success](https://pair.withgoogle.com/chapter/user-needs/) supports testing whether AI adds unique value, considering deterministic alternatives, and choosing automation versus augmentation.
- [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) supports a socio-technical risk frame; it remains a voluntary, general framework rather than a compact checklist.
- [NN/g’s MVP definition](https://www.nngroup.com/articles/mvp-definition/) supports treating an MVP as a means of testing meaningful value, not as permission to deliver a confusing experience.
- [Oostenbrink et al. on value of information](https://pubmed.ncbi.nlm.nih.gov/19602213/) supports the decision-theory principle that additional research is valuable when it reduces decision-changing uncertainty; its health-economics setting is not treated as a product-team formula.

The supplied Manus study also cites its full evidence set and limits; it is retained outside the repository as source material, not copied into the runtime skill.

## Concrete package changes

- Rewrote `SKILL.md` around proportional modes, decision rules, output records, and explicit boundaries.
- Rewrote the extended guidance to preserve strategic depth without mandatory rituals.
- Added selective references for modes, evidence/experiments, and AI product fit.
- Added behaviour scenarios that test escalation and restraint.
- Updated Codex-facing metadata to describe the actual capability.

## Boundary with the remaining research prompts

This batch does **not** rewrite Project Inception, Debugging, or Testing/Verification. Prompt 2 must inform Project Inception; Prompt 3 must inform Debugging; Prompt 4 must inform Testing/Verification. Product Thinking now provides only the product decision inputs those routes may later use.

## Verification plan

1. Validate the repository schema and links.
2. Run the repository unit suite, including core skill contracts.
3. Run the Product Thinking behaviour scenarios manually against a future clean task or independent evaluator; assess decisions and restraint, not framework wording.
4. Confirm this batch did not alter the Project Inception workflow or unrelated skills.
