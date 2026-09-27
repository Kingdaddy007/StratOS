# Runtime Contract and Verification

Load only when motion implementation is authorized, an implemented motion system is being diagnosed, or a named runtime question must be handed to engineering.

This reference does **not** choose the creative motion direction. It translates an approved motion behaviour into runtime responsibilities and observable checks.

## 1. Name the owner of every changing state

Before implementation, identify what drives each changing property or playhead.

Separate, when relevant:

- scroll progress;
- time-based ambience;
- pointer / drag intent;
- hover / focus state;
- route or page transition;
- responsive layout state;
- media playhead;
- poster / fallback state;
- loading / failure state.

Avoid two systems writing the same transform, opacity, camera, or media time without an explicit coordination rule.

## 2. Define lifecycle

For every substantial motion system, define only what applies:

- initialize;
- start;
- update;
- pause;
- resume;
- settle;
- interrupt;
- reverse;
- cancel;
- re-enter;
- resize / recalculate;
- dispose / cleanup.

A motion prototype is not production-ready merely because its ideal forward path works once.

## 3. Schedule work from actual change

Prefer updates caused by real invalidation or active movement.

Watch for:

- idle requestAnimationFrame loops;
- repeated layout read/write cycles;
- timelines continuing offscreen without purpose;
- permanent compositor promotion / `will-change`;
- unnecessary large GPU layers;
- media decoding when no longer visible;
- event listeners / resources surviving route changes.

Engineering chooses the exact implementation pattern.

## 4. Scroll-driven runtime

For authored scroll behaviour:

- calculate ranges from the real rendered layout;
- recalculate after meaningful resize or late-loading media;
- test forward and reverse;
- test quick scrub;
- stop mid-state;
- re-entry;
- deep-link / non-zero entry when relevant.

A deliberate hold is valid.

A frozen playhead, dead scroll span, or trapped focus is a defect.

Scroll progress existing in code does not prove that the intended media or visual state is advancing.

## 5. Source and image quality

Inspect motion using the real output size.

Check:

- native source resolution;
- overscan required by travel;
- device-pixel ratio;
- crop;
- compression;
- scaling;
- exposed seams;
- cutout edges;
- material detail;
- text contrast against actual composited frames.

Do not approve an effect from the source asset alone when runtime scaling changes its quality.

## 6. Preserve access and meaning

Essential content, proof, navigation, and inquiry should remain reachable without precision scrolling, hover, or full-motion playback.

Check:

- keyboard focus remains visible and reachable;
- touch has an alternative to hover-only behaviour;
- controls remain operable during pinned / animated states;
- motion does not reorder semantic content incorrectly;
- reduced-motion mode preserves sequence and meaning;
- disabling animation does not remove a project, caption, or action.

If motion preferences can change during a session, the implementation should respond coherently rather than only reading the setting at initial load.

## 7. Loading and failure

Heavy media or live rendering needs a useful state before and during failure.

Define:

- poster / resolved still;
- loading state;
- timeout / failure behaviour where relevant;
- what content remains usable;
- what happens when media arrives late;
- what happens if a frame / video / model never arrives.

Pause low-value ambience when offscreen or backgrounded when practical.

Release heavy resources when the scene no longer needs them.

## 8. Responsive runtime

Do not assume desktop timelines can simply be scaled down.

Check whether mobile / short viewports require:

- different travel;
- different pin duration;
- ordinary document flow;
- manual control;
- poster image;
- fewer simultaneous states;
- simplified media class.

Runtime breakpoints should follow the approved mobile motion intent.

## 9. Real-browser verification

Review the real implementation at the relevant scope.

Sample as applicable:

- entry;
- midpoint;
- exit;
- reverse;
- quick scroll;
- resize;
- orientation change;
- touch;
- keyboard;
- reduced motion;
- late-loading media;
- media failure;
- short viewport;
- representative mobile device.

For scrubbed media, observe actual frame / playhead advancement rather than assuming the listener or timeline proves movement.

Record what was tested and what remains untested.

## 10. Handoff from motion direction

Engineering should receive:

- approved motion job;
- state A / state B;
- driver;
- perceptual character;
- moving / stable elements;
- property / playhead ownership;
- interruption / reverse intent;
- mobile intent;
- reduced-motion equivalent;
- production class;
- asset assumptions;
- loading / failure state;
- observable acceptance checks.

Load an older implementation reference only when a **named technical question** requires it.

Do not let a stored GSAP, WebGL, Canvas, or scrolling preset silently redefine the approved movement.
