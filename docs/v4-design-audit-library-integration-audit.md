# V4 Design-Audit Library Integration Audit

**Status:** implemented and verified as a discoverability repair; no raw audit
report, Spatial skill, or workflow method was deleted or rewritten.  
**Date:** 2026-08-19

## Question

Beloved keeps a 30-report collection of cinematic and high-quality web
references. The question is how an AI Product Studio should use that collection
without loading it for every web task, copying reference sites, or treating an
AI-made transcript as direct visual fact.

## Findings

1. `global/design-audit/` was already correctly registered as the
   `spatial-design-audit-library` resource. It is included only in Spatial
   payloads, not General payloads.
2. `spatial-experience-design` already had an adaptation map and the
   full-project coordinator already routes reference work to
   `reference-intelligence`.
3. The adaptation map indexed only 20 of the 30 reports. Ten reports were
   preserved but difficult to retrieve by a meaningful question.
4. `reference-intelligence` covered recordings, screenshots, transcripts, and
   mediated reports in principle, but it did not explicitly tell an agent when
   the local Design-Audit library should be consulted.
5. The reports contain useful observed/reported design patterns, but their
   historical “Gap” and “Upgrade Specifications” sections are not accepted as
   automatic instructions to edit a skill or introduce a technique.

## Decision

Keep the collection as a Spatial-only **reference library**, not as 30 skills,
30 workflows, or a universal website-design checklist.

The correct route is:

```text
Named project/design question
  -> reference-intelligence
  -> inspect supplied recording/screenshots/transcript and/or selected local reports
  -> label source evidence and uncertainty
  -> spatial adaptation map, if the task qualifies for Spatial
  -> Keep / Adapt / Reject / Defer decision
  -> approved concept, storyboard, bounded prototype, or no action
```

## What Changed

- Added `global/design-audit/library-index.md`: a human-readable index, evidence
  discipline, and selection guide for all 30 reports.
- Completed the ten missing entries in the Spatial adaptation map.
- Added a conditional `local-design-audit-library` reference to
  `reference-intelligence`; it explicitly routes new recordings and AI-made
  transcripts with the appropriate evidence labels.
- Added a regression test so a later refactor cannot silently drop reports,
  the local library route, or the Spatial-only resource boundary.

## Recording and Transcript Rule

If an agent directly views a screen recording, it can document visible states,
timecodes, and demonstrated input as `OBSERVED`. If another AI produces a text
transcript/analysis of that recording, that text is `REPORTED`: it can help
search and compare, but it cannot establish an exact implementation or replace
the video/screenshot evidence for a visual decision.

## What This Does Not Do

- It does not make every website cinematic or activate the Spatial pack for
  ordinary product UI work.
- It does not approve copying a source site’s geometry, interactions, identity,
  model, dependency, or code.
- It does not add a new workflow; an ordinary reference question remains direct
  skill work. The existing `spatial-project-inception` route coordinates a
  substantial project only when its decisions must be managed together.
- It does not claim that every technique in the reports is current, necessary,
  performant, accessible, or feasible.
