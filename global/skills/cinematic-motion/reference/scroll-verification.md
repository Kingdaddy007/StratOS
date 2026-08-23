# Scroll Verification

Use this reference after implementing authored scroll, pinned scenes, scrubbed
media, persistent objects, or scroll-controlled Canvas/WebGL. It supplements
project-native tests and browser inspection; it does not certify release.

## Define the claim before testing

Record:

- target revision and route;
- storyboard beats or choreography ranges under test;
- desktop, mobile, and reduced-motion expectations;
- media sources, posters, loading behavior, and fallbacks;
- observable success and failure conditions;
- browsers and devices actually available.

Sample within every authored beat, including entry, middle, exit, and boundary
transitions. Uniform document sampling can miss short cues and pinned failures.

## Mechanical checks

### Dead scroll

Flag a sampled range when scroll position changes but no intended narrative
state, cue, media time, mask, rail, camera, or stage transition changes. A
deliberate hold is valid only when the storyboard names its job and duration.

For bespoke fixed stages, expose a testable semantic state such as a current
beat, scene, or progress label. Do not add fake motion merely to satisfy the
check.

### Frozen media

Flag a visible scrubbed clip or frame-controlled stage when its intended
playhead or frame state does not advance across sampled progress. Check entry,
middle, and exit after allowing the implementation to settle. Distinguish a
frozen poster, decode failure, unloaded frame, and intentionally held frame.

### Composited contrast

Inspect text against the rendered underlying frame, not only the declared CSS
background. Sample the worst plausible frames for each line and state. Account
for crops, overlays, gradients, scrims, and fixed chrome. Treat automated pixel
analysis as bounded evidence; manually inspect representative and failure-prone
frames.

### Focus and reachability

Keyboard-traverse navigation, proof, gallery controls, and inquiry actions.
Ensure focus is not moved offscreen or trapped by a pinned stage. Verify that
the primary action remains reachable without completing a precision scroll.

### Mobile and reduced motion

Verify the authored mobile translation rather than a shrunken desktop timeline.
Verify reduced motion without disabling content, proof, navigation, or inquiry.
Check manual controls when autoplay or scrubbing is replaced.

### Loading and failure

Throttle or simulate delayed media where the project permits. Verify posters,
progress, error/fallback behavior, late asset arrival, and navigation during
loading. Record unavailable network/device conditions as unverified.

## Scrubbed-video encoding evidence

For direct video playhead scrubbing, record codec, container, frame rate,
resolution, keyframe interval/GOP, mobile source, poster, and measured seek
behavior. Dense keyframes can improve seeking but increase file size; do not
copy a fixed GOP value without testing the actual clip, delivery path, target
browser, and bandwidth budget.

For extracted canvas frames, record source probe data, extraction rate, frame
count, dimensions, preload tiers, and missing-frame behavior. GOP density of the
source is an ingestion concern; runtime quality depends on the extracted frame
set and loader.

## Evidence artifacts

Collect only what changes the decision:

- per-beat results with sampled progress values;
- screenshots or a contact sheet across the journey;
- media time/frame observations for scrubbed sections;
- console and network failures;
- keyboard/focus evidence;
- mobile and reduced-motion evidence;
- residual untested browsers, devices, and network conditions.

After mechanical checks, perform one uninterrupted cold scroll without reading
the implementation. Record one felt word per beat, the perceived primary peak,
the ending impression, and any section that feels dead, repetitive, or louder
than its communication job. Compare that observation with the intended feeling
curve; treat disagreement as design evidence, not an automatic failure.

## Status

Use one of:

- `verified for sampled scroll scope`;
- `verified with residual scroll risk`;
- `blocked by scroll failure or environment`;
- `unverified`.

Report what the sampling proves and what it cannot prove. A contact sheet,
green script, or one browser run is not release approval.
