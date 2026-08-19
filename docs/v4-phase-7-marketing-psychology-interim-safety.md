# V4 Phase 7 — Marketing Psychology interim safety route

**Status:** implemented and verified as an interim safety route  
**Reason:** the pre-V4 skill contained a broad, unverified model catalogue and explicit tactics that can become deceptive or unsafe when applied as defaults.

## What changed now

- Replaced the active catalogue-as-instruction behaviour with a small Ethical Behavioural Insight route.
- Made product, UI/UX, Page CRO, Testing, Copywriting, Copy Editing, Expert Positioning, Prospect Research, and Sales Enablement ownership explicit.
- Reframed behavioural mechanisms as context-limited, falsifiable hypotheses rather than conversion levers.
- Added a clear stop for fake scarcity, deceptive comparison, hidden defaults, confirmshaming, obstructive cancellation, fabricated proof, coercive urgency, vulnerable-audience exploitation, and unapproved external effects.
- Preserved the former detailed catalogue as a candidate reference for explanation and evidence review, with a top-level rule preventing its use as a tactics manual.
- Replaced old evals that expected decoys, pre-selected choices, scarcity, and generic pricing psychology with direct-work, claim-limit, routing, safety, and high-risk-stop cases.

## What did not change yet

This is deliberately **not** the final evidence-led taxonomy. The supplied portable brand/positioning report shows that Behavioural Insight should be conditional and ethical, but it does not decide which individual models are robust enough to retain, move, demote, or reject.

The next evidence gate is the self-contained [behavioural insight research brief](v4-phase-7-behavioural-insight-research-brief.md). Its returned report must decide the final capability shape and the fate of each major model group before another substantive catalogue rewrite.

## Safety posture while research is pending

The current skill can still explain a named concept, flag ethical risk, or propose a small reversible hypothesis. It cannot claim that a bias will increase conversion, direct manipulative design, or authorise experiments, pricing changes, publication, contact, spend, or data collection.

## Verification completed 2026-08-19

- Canonical `os.py validate --json`: 0 issues.
- `python -m unittest tests.test_os_cli`: 25 passing tests.
- Marketing Psychology eval fixture: valid JSON.
- `git diff --check`: passed.
