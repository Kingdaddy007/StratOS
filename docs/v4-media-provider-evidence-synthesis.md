# V4 Media Provider Evidence Synthesis

Decision date: 2026-08-19  
Inputs reviewed: Google Flow study, Seedance ecosystem study, and the supplied change-decision document.

## Decision

Adopt a provider-neutral `video-generation` entry point. Treat Google Flow as a Google creative surface and Seedance as a ByteDance model family available through distinct creator and API surfaces. Select a route in this order:

```text
job -> active surface -> exact model/API identifier -> verified capability -> provider-specific adaptation
```

Do not make either Google Flow or Seedance the universal default. Do not create a Google-only top-level skill. Preserve the inherited Seedance package in the archive rather than distributing it as separate skills.

## What the Evidence Establishes

| Finding | Decision | Confidence |
| --- | --- | --- |
| Flow is an interface, not a model. Its active matrix currently names Veo 3.1 - Lite, Fast, Quality, and Gemini Omni Flash. | Adopt exact-label, active-UI routing. | High; primary Google help verified 2026-08-19. |
| Google documentation conflicts about Fast/Quality extension. | Keep extension live-checked; do not encode a standing Fast/Quality rule. | High. |
| Seedance 2.0 and 2.5 publish materially different versioned counts and durations. Creator UI and ModelArk can differ again. | Scope every Seedance fact by version, surface, source date, and checked date. | High; primary ByteDance material verified 2026-08-19. |
| Existing creative methods remain potentially useful, but many inherited files contain 2.0-specific tags, limits, and community claims. | Preserve them for review; do not use their stale provider facts as defaults. | High; verified against the current package. |
| Rights, likeness, confidentiality, moderation, and provenance can invalidate an otherwise good video route. | Make them visible production gates. | High. |

## Comparison of the Three Inputs

The Google Flow study is strongest on model/surface terminology, the capability matrix, and the extension contradiction. The Seedance study is strongest on the distinction between announcement pages, creator surfaces, and ModelArk/API behavior. The change-decision document correctly combines the two into a minimal architecture, but it described a future direct-specialist structure that the repository has not yet implemented.

The decision document is therefore accepted as the **target structure**, not as proof that the prior 24 registered Seedance entries were correctly classified.

## Actual Repository Gap

The prior package had one Seedance parent plus 23 separately registered child skills, all marked `capability` in the manifest. Several inherited references stated fixed 2.0 durations, tags, file limits, API behavior, or prompt rules. The count was an inventory fact, not a quality target.

The active catalogue now has one `video-generation` skill. The prior package is preserved outside the active skill tree as source provenance; it is not copied into host builds or used for routing.

## Implementation Slice Completed

- Rewrote `video-generation` around job, surface, exact model, verified capability, and provider-specific adaptation.
- Added a missing `video-generation` resource index and replaced its two provider references with dated, source-scoped routing notes.
- Reworked `video-generation` into the sole active entry, with conditional Google, Seedance, brief/prompt, reference, look/motion, audio, diagnosis, rights, and handoff references.
- Archived the prior Seedance source package intact outside `global/skills`, removed its 24 active manifest entries, and removed its former special build rule.
- Updated the shared volatile-source baseline with the current Google Flow, Seedance 2.0, and Seedance 2.5 evidence boundary.

## Deferred Preservation Work

1. Curate useful examples, recipes, and language vocabulary from the archive into active references only after each claim is separated from stale platform behavior.
2. Add retrieval fixtures when a curated reference is promoted, proving that it loads for the intended job but not for unrelated media work.
3. Recheck provider evidence when it is older than 90 days or when the active UI/API differs.

## Evidence and Re-evaluation

Use [Google Flow models and features](https://support.google.com/flow/answer/16352836?hl=en), [Google Flow credits](https://support.google.com/flow/answer/16526234?hl=en), [Seedance 2.0 launch](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0), and [Seedance 2.5 launch](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) as primary-source snapshots. Recheck a provider-specific fact at production time, on a different surface/region, or after 90 days.
