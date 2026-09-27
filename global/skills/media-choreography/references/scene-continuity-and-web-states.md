# Scene Continuity and Web States

Load when a family of stills, clips, renders, composites, or generated frames must remain related, hand into the live page coherently, or survive crop, loading, and fallback states.

## Define stable anchors and intended change

For related assets, identify the few properties that must remain stable.

Possible anchors:

- project / room identity;
- architecture and openings;
- furniture / object placement;
- human identity / presence;
- camera side, height, lens character, horizon, perspective;
- light direction, exposure, colour temperature, shadow softness;
- material colour, pattern scale, texture, joinery, reflections;
- foreground / background relationships;
- real occlusions.

Identify intended change separately:

- camera travel;
- object movement;
- light shift;
- material change;
- transformation;
- time-of-day change;
- transition to another project.

Do not relabel continuity drift as intentional transformation after the fact.

## Map only useful states

For a media-led moment, define only what matters:

1. **Entry** — first meaningful usable state.
2. **Change** — significant intermediate state only when it matters to readability, proof, or transition.
3. **Resolution** — end state that hands into live content, another scene, or a deliberate hold.
4. **Poster / loading** — usable state before time-based media is ready.
5. **Fallback** — state on failure, reduced motion, low bandwidth, or another constrained mode.

The transition into and out of media may matter as much as the most impressive middle frame.

## Preserve project identity

A seamless match can falsely imply one continuous room or one client's work.

When project identity changes, consider:

- label;
- caption;
- project navigation;
- hard / editorial cut;
- colour / shape / camera-direction echo;
- another truthful signal.

Do not force seamless spatial continuity when editorial continuity is more honest.

## Source-image-to-video continuity

When one still becomes the source of a moving asset, preserve only what the experience requires:

- geometry;
- focal subject;
- camera logic;
- material identity;
- lighting;
- key objects;
- project identity.

Define separately:

- camera movement;
- subject / object movement;
- environmental movement;
- what must remain stable;
- useful end frame.

Do not ask the motion-generation stage to repair an unresolved source composition.

## Text and annotation regions

Check text / control regions against the actual changing and cropped media.

A clean area in frame 1 may become busy later.

Record only constraints the media must support:

- evidence that cannot be covered;
- acceptable low-detail region;
- contrast variability;
- safe crop range;
- mobile alternative.

Spatial Experience Design decides the final text placement and visual treatment.

## Check delivered quality

Inspect at actual rendered website size:

- pixel density after crop / zoom / overscan / device scaling;
- edge halos;
- missing contact shadows;
- geometry / light / material drift;
- compression blocking / banding / blur;
- frame instability;
- text contrast;
- focal subject;
- mobile / short-viewport crop;
- loading order.

A high-resolution source may still look poor after overscan or compression.

Record which final states were actually inspected.

## Useful fallback

Prefer a resolved still or poster that preserves the subject and message.

If a scrubbed / time-based source fails:

- keep chapter content reachable;
- preserve proof;
- avoid an empty frozen stage;
- preserve layout where possible;
- avoid a late-load jump that destroys reading.

Exact playback code belongs to engineering.
