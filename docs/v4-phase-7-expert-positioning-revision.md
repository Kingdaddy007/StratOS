# V4 Phase 7 — Expert Positioning revision

**Status:** implemented and verified  
**Basis:** portable brand/positioning assessment and the existing `expert-positioning` skill.

## Decision

Keep Expert Positioning as the dedicated professional-services, offer-fit, qualification, proof, portfolio, and inquiry capability. Preserve its useful diagnostic insight—an interchangeable service needs a clearer credible reason to choose it—but remove the claim that one commercial doctrine is always the right way to sell expertise.

## Changes made

- Retained the audit’s core focus, proof, diagnosis, commercial-boundary, offer, portfolio, and inquiry layers.
- Reframed paid diagnostics, no-free-work, minimum engagements, deposits, fixed pricing, exclusivity, application gates, and proposals as contextual business choices.
- Added four posture options: selective expert, collaborative service, productised service, and early credibility.
- Replaced a fixed 75-point authority score with qualitative or user-approved evaluation.
- Removed old `contexts/positioning-audit.md` output assumptions and added portable active-context loading.
- Added claim/proof discipline and explicit authority boundaries.
- Kept detailed commercial guidance in a selectively loaded reference and added positive, boundary, and negative-routing eval fixtures.

## Preserved limits

- No false premium/exclusive claim, invented result, fabricated case-study outcome, manipulative gate, or unsupported price/minimum is permitted.
- The skill still does not own general copy polishing, product scope, UI styling, contracts, pricing commitment, publication, outreach, or external action.
- Spatial Brand and Storytelling content remain untouched.

## Verification target

Completed 2026-08-19:

- Canonical `os.py validate --json`: 0 issues.
- Relevant host metadata and core-skill tests: passed.
- Expert Positioning eval fixture: valid JSON.
- `git diff --check`: passed.
