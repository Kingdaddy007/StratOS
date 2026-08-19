# V4 Phase 7 — Offer Architecture Evidence Synthesis

**Status:** accepted for narrow implementation  
**Date:** 2026-08-19

## Decision

The two independent reports agree that Offer Architecture is a distinct, reusable decision-preparation capability. It is not a sales playbook, pricing engine, legal document generator, or autonomous commercial agent.

It owns the commercial object: audience/context, desired change, deliverables, scope, exclusions, dependencies, proof limits, human-reviewed price hypothesis, and safest next step. It consumes product direction and positioning; it requests feasibility, design, quality, security, and specialist constraints rather than replacing those owners.

## Accepted implementation

- One optional Growth skill: `offer-architecture`.
- Two selective references: offer-family/scope mechanics and evidence/price/claim discipline.
- Reusable decision, claim, handoff, and learning templates.
- One material `commercial-decision-record` workflow and one conditional `live-learning-loop` workflow.
- Demotion of `marketing-copy` to a direct Growth selection procedure.

## Rejected or deferred

- AI-set pricing, mandatory value-pricing formulas, compulsory tiering, ROI guarantees, contract/legal sufficiency, autonomous contact/publication/spend/payment/CRM changes, sensitive-attribute inference, and generic growth automation.
- A standalone market-research, SEO, CRM, retention, distribution, partnership, analytics, or pricing-optimisation skill.

## Evidence assessment

Batch A supplies the decision object, scope mechanics, offer-family distinction, price-hypothesis limits, and capability boundary. Batch B supplies the claim ledger, explicit human/AI authority boundary, conditional state contracts, handoff packet, data-purpose constraints, and anti-automation-bias controls.

Primary-source sanity checks on 2026-08-19 confirmed the limited principles used: NIST describes AI RMF and Privacy Framework as voluntary risk-management tools; FTC substantiation guidance requires an appropriate reasonable basis for objective claims before dissemination in its U.S. context; OWASP identifies excessive functionality, permissions, and autonomy as LLM-agent risks and recommends least privilege and human approval for high-impact actions. These are portable design constraints, not global legal conclusions.

## Evaluation gate

The first real offer task must test decision quality and reversibility, not conversion alone: scope clarity, hidden dependencies caught before commitment, claim accuracy, price-assumption visibility, approval clarity, and fewer late scope changes. If the capability only repeats positioning or adds paperwork, merge or retire it.
