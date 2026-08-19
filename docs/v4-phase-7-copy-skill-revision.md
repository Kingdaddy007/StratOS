# V4 Phase 7 — Copywriting and Copy Editing revision

**Status:** implemented and verified  
**Basis:** `v4-phase-7-portable-brand-positioning-messaging-assessment.md`

## Decision

Keep `copywriting` and `copy-editing` as separate capabilities:

- **Copywriting** creates new or materially rewritten communication from a known or explicitly qualified decision set.
- **Copy Editing** improves existing communication while preserving its intended meaning unless the user expressly authorises a strategic change.

They share the conditional Meaning and Evidence Foundation, but neither turns it into a mandatory workshop or a forced Growth workflow.

## Changes made

- Replaced legacy `contexts/` and `.claude/` assumptions with portable `.agents/contexts/` discovery and relevant supplied project truth.
- Added direct, deliberate, and evidence-gated levels so a small rewrite stays small.
- Replaced universal page, CTA, founder-story, proof, risk-reversal, and emotional-pressure prescriptions with candidate patterns that need a task-specific reason.
- Added claim/proof boundaries: no fabricated evidence, numbers, testimonials, scarcity, credentials, outcomes, comparative claims, guarantees, or invented customer language.
- Preserved the detailed `copy-frameworks`, transitions, copy sweeps, plain-English, and content-refresh references. They remain selectively loaded rather than discarded.
- Added regression assertions for distinct Draft/Edit jobs, supported CTA nuance, portable path removal, foundation routing, and evidence limits.

## Explicitly not changed

- No spatial Brand or Storytelling content was compressed, moved, or made universal.
- No Prospect Research, Sales Enablement, Page CRO, or Marketing Psychology rule was changed in this batch.
- No external action, publication, contact, campaign, or claim was performed.

## Verification target

Completed 2026-08-19:

- Canonical `os.py validate --json`: 0 issues.
- `python -m unittest tests.test_os_cli`: 23 passing tests.
- Copywriting and Copy Editing eval fixtures: valid JSON.
- `git diff --check`: passed.
