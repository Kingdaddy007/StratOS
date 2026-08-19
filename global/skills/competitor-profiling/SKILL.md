---
name: competitor-profiling
description: >
  Research, profile, compare, or audit competitors, alternatives, agencies,
  products, offers, websites, public positioning, pricing, proof, content, or
  market signals. Trigger on "competitor research", "competitive intelligence",
  "competitor dossier", "competitive audit", "who are my competitors", "compare
  these companies", or a request to analyse supplied competitor URLs. Do not use
  as permission to bypass access controls, scrape personal data, contact a
  competitor, publish claims, or make legal/compliance conclusions.
---

# Competitor Profiling

## WHEN TO USE THIS

- Build a quick scan, focused comparison, deep dossier, or cross-competitor summary from supplied public sources.
- Analyse competitor positioning, offers, experience, pricing, proof, content, customer language, or market signals.
- Prepare evidence for product, brand, CRO, sales, or strategic decisions.

## NEVER DO

- Never require a named scraping, SEO, review, or data vendor. Use the host capabilities that are actually available.
- Never bypass authentication, paywalls, CAPTCHAs, technical blocks, contractual restrictions, or stated automated-collection restrictions.
- Never treat robots.txt as authentication, or treat a blocked/unreachable source as permission to continue.
- Never collect, persist, or expose personal data merely because it is public.
- Never turn competitor self-description, search rank, a proxy, a repeated claim, or an inference into an independently verified fact.
- Never contact competitors, publish comparisons, or create other external effects without the required human approval.

## QUESTION AND SCOPE

1. State the decision the research will support, comparison unit, target audience, market/region, freshness requirement, consequence of error, and evidence that could change the decision.
2. Choose `quick_scan`, `focused_comparison`, or `deep_profile`. Default to the smallest scope that answers the decision; do not default to a full crawl.
3. Confirm the supplied URLs or entities and whether comparison against the user's offer is wanted. Read active project context and product/brand context when available.
4. Define the dimensions before collecting: positioning, audience, offer/capability, experience, pricing, proof, content, distribution, operational signals, or another decision-specific dimension.

## CAPABILITY-FIRST COLLECTION

1. Inspect available read-only capabilities: page fetch, browser observation, search, screenshots/video, document parsing, structured extraction, or user-provided evidence. Record capability, access condition, freshness, and limits.
2. Use the least intrusive adequate public source. Prefer the competitor's own current page for self-description and an independent source for material claims, reviews, market evidence, or disputed statements.
3. Map only the pages needed for the question. Typical candidates are homepage, offer/product, pricing, about, case studies, integrations, changelog, help, and relevant public reviews. Do not assume any page exists.
4. If access fails, record the failure and use an allowed fallback. Do not guess missing pricing, founding date, customers, funding, traffic, or capability.
5. Preserve a provenance record when the workspace and task permit local output. Do not silently write raw captures, personal data, or expensive tool output to disk.

## EVIDENCE AND CLAIM DISCIPLINE

Label every material statement as `observation`, `source_reported_claim`, `measured_metric`, `inference`, `estimate`, `hypothesis`, or `unknown`.

- Record exact wording, source URL/artifact, title, source type, publication/update date, access date, extraction method, scope, limitations, confidence, and permitted use.
- Keep competitor self-description separate from independent evidence. A claim such as "10,000 customers" remains source-reported unless supported by adequate evidence.
- Do not treat absence from a page as proof of absence. Say `not found in reviewed sources`.
- Distinguish current, dated, regional, tier-specific, device-specific, and sampled evidence.
- Use one adequate source for a low-stakes direct observation. Corroborate material, sensitive, contested, external, or difficult-to-reverse claims when feasible.

## FAIR COMPARISON AND SYNTHESIS

Compare like with like. For each comparison, record regional, temporal, product-tier, market, date, device, audience, denominator, method, and definition differences before drawing a conclusion.

- Describe strengths and weaknesses with evidence and uncertainty; do not write advocacy disguised as analysis.
- Separate observation from strategic implication. Treat "opportunity" as a hypothesis until tested against the user's context.
- Compare the competitor's offer with the user's offer only when the user's scope, evidence, and decision criteria are known.
- Do not use search visibility, backlink counts, review volume, or public claims as a universal proxy for quality, authority, or product truth.

## STOP AND APPROVAL ROUTING

Stop and report unknown, request clarification, or route to review when source access, permission, identity, freshness, comparison basis, or evidence quality is insufficient. Obtain human approval before external publication, high-consequence recommendations, personal-data use, paid or unusual-volume collection, external interaction, or a materially contested claim.

## REFERENCE LOADING RULES

- Load [references/evidence-and-source-record.md](references/evidence-and-source-record.md) for any material claim, collection boundary, source conflict, privacy question, access failure, or comparison decision.
- Load [references/templates.md](references/templates.md) when producing a profile or cross-competitor summary. Use only sections relevant to the declared scope.
- Load [references/tool-reference.md](references/tool-reference.md) when selecting host capabilities, fallbacks, capture methods, or provenance-preserving outputs. Do not assume a named provider is installed.
- Load [references/resource-index.md](references/resource-index.md) to select resources. Do not load the package wholesale.

## OUTPUT SHAPE

Return a decision-useful dossier, not an unsourced data dump.

1. **Research question and scope** - decision, entities, dimensions, market, dates, depth, and limits.
2. **Source and access record** - sources used, access method, failures, freshness, and permissions.
3. **Evidence ledger** - material claims with class, source, scope, confidence, and permitted use.
4. **Profile or comparison** - observations grouped by the selected dimensions.
5. **Interpretation** - supported implications, hypotheses, competing explanations, and unknowns.
6. **Decision handoff** - strengths, risks, opportunities to test, next evidence, and approval state.

## NON-NEGOTIABLE CHECKLIST

1. Define the decision, comparison unit, scope, and freshness need.
2. Use available capabilities without hard-coded provider assumptions.
3. Respect access, privacy, robots, contractual, and approval boundaries.
4. Preserve claim-level provenance and evidence class.
5. Compare like with like and expose limitations.
6. Report unknowns instead of filling gaps with plausible facts.
