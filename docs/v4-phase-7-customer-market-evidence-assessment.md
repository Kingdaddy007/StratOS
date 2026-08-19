# V4 Phase 7 — Customer, market, and demand evidence assessment

**Status:** accepted with one authority correction; implemented as a conditional shared reference  
**Assessed report:** `Customer, Market, and Demand Evidence for a One-Person AI Product Studio`, supplied 2026-08-19  
**Decision settled:** this job does not become a new Growth skill yet.

## Report score

| Criterion | Score (0–3) | Assessment |
| --- | ---: | --- |
| Source quality | 3 | It uses empirical/methodological work for interview, willingness-to-pay, and usability limits, plus official NIST, FTC, and European Commission guidance for AI/integrity boundaries. The health-intervention customer-discovery example is treated as context-limited rather than universal. |
| Claim discipline | 3 | It distinguishes sourced fact, inference, recommendation, and uncertainty; the evidence ladder states what each level cannot prove. |
| Context fit | 3 | It addresses a one-person studio, low traffic, professional services, product and website work, Nigeria/international variation, and reversibility. |
| Evidence limits | 3 | It rejects magic sample counts, hypothetical willingness-to-pay as payment, persona-as-proof, synthetic participants as customer evidence, and low-power A/B overclaims. |
| Ethical and authority fit | 2 | External effects and personal-data boundaries are strong. One phrase overreached by saying "no external research action" without clearly preserving read-only public desk research as allowed. The implementation corrects that ambiguity. |
| Operational usefulness | 3 | It gives an evidence ladder, decision/method boundaries, compact evidence fields, direct-work conditions, and positive/negative routing examples. |
| Reversibility | 3 | It compares four implementation forms and includes explicit conditions that would justify a future dedicated skill. |

**Total: 20/21 — strong primary implementation basis.**

## Source and inference check

The core limits used in the implementation are supported and deliberately narrow:

- qualitative interviews and reported preferences can inform context and hypotheses but do not establish payment, prevalence, or causal effects;
- stated willingness-to-pay needs calibration against real behaviour and context;
- fixed participant-count folklore is not a universal usability rule;
- model-generated personas and summaries are not human observations or demand evidence;
- fabricated reviews, testimonials, and AI performance claims are prohibited;
- data, consent, jurisdiction, and channel sensitivity remain project-specific.

No study in the report proves that a seven-step ladder, a particular interview method, or a new AI process improves every project. Those elements remain bounded Studio design choices, not universal laws.

## Decision

Adopt **Option B plus C** from the report:

- a **conditional shared reference** for decision-to-evidence selection, evidence status, provenance, AI safeguards, and stopping rules; and
- a **lightweight project record** only when the decision is material enough to require it.

Do **not** add a standalone Customer/Market/Demand Growth skill. Do **not** add a mandatory workflow, research agent, required context file, or universal approval gate.

The reference is a manifest `resource`, not a `baseline`: a baseline would be shipped as always-applicable policy, while this material must be discovered but loaded only when its activation condition is met.

## Authority correction

The report correctly stops recruitment, outreach, personal-data collection, public tests, advertising spend, CRM changes, payment handling, publication, and public customer/market claims. However, normal read-only desk research does not require a separate approval merely because it is external information.

The implemented rule is therefore:

> Read-only public desk research within task scope is allowed. Explicit approval is required only immediately before an external effect, sensitive/personal-data handling, or another action outside the original request.

The report's phrase "what action is now authorised" is also not adopted. Evidence can support a **proposed next action**; host policy and Beloved's approval remain the source of authorisation.

## Implemented asset

- [Customer, Market, and Demand Evidence reference](../global/reference/customer-market-demand-evidence.md) — conditional loading, proportionate route, decision-relative evidence labels, no magic sample count, light record, and approval limits.
- Manifest resource registration keeps it discoverable in General payloads without activating Growth or loading it automatically.
- The Product & Strategy router identifies it only for material customer/market/offer/willingness-to-pay/demand uncertainty.
- Regression tests cover payload delivery, non-compulsory routing, allowed read-only desk research, direct low-risk copy work, and the external-effect stop.

## Preserved boundaries

- Product Thinking still owns product framing, priority, and build decisions.
- Research Analysis still owns general source discovery and comparative synthesis.
- UI/UX still owns task success and interface quality.
- Page CRO still owns conversion/friction diagnosis; this reference prevents causal/demand overclaims when evidence is thin.
- Prospect Research remains a specialised active client-finding capability, not generic market validation.
- Sales Enablement remains buyer-facing preparation only; it cannot create commitments or send material.

## Next evidence gate

The next focused study is **Portable Brand, Positioning, Messaging, Proof, and Narrative**. It must decide the portable core that may be shared by `brand-strategy`, `expert-positioning`, `copywriting`, `copy-editing`, and `storytelling`, while preserving specialist spatial material and distinct draft/edit/narrative activation modes.

No standalone Growth Measurement, pricing/packaging, acquisition, social, SEO, advertising, or lifecycle skill is justified yet. Reconsider them only when a real recurring Studio decision shows that the shared reference and current capabilities cannot handle the work safely.
