# Playback, Poster, and Fallback

Load when prepared media must support autoplay, looping, scrubbing, poster frames, delayed media, responsive variants, reduced motion, or playback failure.

This reference defines **source-state and acceptance requirements**. Runtime implementation belongs downstream.

## Define playback intent

Possible requirements:

- still only;
- autoplay once;
- autoplay loop;
- manual play / pause;
- scroll-scrubbed source;
- drag / interaction-controlled source;
- state-based segment;
- poster until activation.

Ask whether playback materially improves the experience.

## First usable state

The first usable state should work before the motion has played.

Check:

- subject is identifiable;
- composition is intentional;
- essential proof is present;
- overlaid text / controls can remain legible when relevant;
- loading does not expose an ugly transitional frame.

Do not require several seconds of playback before the page becomes understandable.

## Resolved / end state

Define where the media leaves the visitor.

The end state may need to:

- become the live hero;
- hand into the next section;
- hold for reading;
- align with another source;
- become a resolved poster-like state;
- loop;
- stop without feeling broken.

A strong middle sequence with a useless end state is an integration failure.

## Poster

Choose the poster intentionally.

It should:

- represent the subject honestly;
- work compositionally;
- survive intended crop;
- support necessary overlays;
- avoid transition blur / half states;
- match playback closely enough to avoid a jarring jump.

The poster is part of the designed experience, not a browser accident.

## Looping

When a loop is required, inspect:

- visual seam;
- camera position;
- object position;
- light continuity;
- temporal jump;
- audio seam if relevant.

Perfect invisibility is not always necessary; perceptual disruption is the real test.

## Scrubbed source

When progress controls prepared media, define:

- usable start / end states;
- meaningful intermediate states;
- whether reverse is required;
- whether frames must settle cleanly;
- expected quality during rapid seeking;
- unloaded / poster state;
- mobile alternative;
- reduced-motion source state.

Cinematic Motion owns perceptual behaviour.

Scroll Storyboard owns beat mapping.

Engineering owns seek / frame / playback implementation.

Media Choreography owns whether the source can support the required states.

## Text-safe media over time

Inspect the actual sequence.

A safe zone can disappear as:

- brightness changes;
- objects move;
- camera shifts;
- crop changes;
- overlays collide.

Record the constraint. Let Spatial Experience Design choose the visual solution.

Do not automatically darken or blur the work until the asset loses its value.

## Reduced motion

Preserve:

- subject;
- proof;
- order;
- information;
- action.

Possible source equivalents:

- poster;
- resolved end frame;
- static pair;
- manual comparison;
- still chapter image.

Do not require video playback for essential content.

## Mobile

Mobile may require:

- dedicated crop;
- alternate poster;
- alternate clip;
- shorter source;
- no scrub;
- lower file weight;
- ordinary document-flow equivalent.

Do not assume a desktop center-crop will work.

## Loading and failure

Define what source state is available:

- before load;
- during delay;
- when autoplay is blocked;
- on media failure;
- on poor bandwidth;
- when the heavy rendering path is unavailable.

The page should retain a credible, useful state without successful playback.

## Downstream handoff

Provide:

- playback intent;
- entry / end / poster states;
- source variants;
- crop constraints;
- loop requirement;
- scrub / reverse requirement;
- reduced-motion source;
- mobile alternative;
- loading / failure state;
- acceptance checks.

Engineering / media implementation chooses encoding, player, preload, canvas, and runtime architecture.
