# Production Classes and Fallbacks

Load when choosing how an approved motion should be produced or when a concept's visual requirement may be served by runtime motion, pre-rendered media, scrubbed media, or stillness.

This reference does not choose frameworks. It chooses **production class**.

## 1. Still / simple transition

Examples:
- still composition;
- CSS hover / focus;
- simple opacity / transform;
- direct image swap;
- restrained crossfade.

Use when:
- movement is low consequence;
- responsiveness matters more than cinematic complexity;
- the job is state clarity / hierarchy / small transition;
- heavy media adds little value.

Advantages:
- light;
- accessible;
- responsive;
- maintainable.

Risk:
- treating “simple” as generic rather than deliberately composed.

## 2. Live DOM / CSS / SVG

Examples:
- masks;
- type movement;
- layered composition;
- crop / transform;
- SVG path / reveal;
- DOM parallax;
- pinned panels.

Use when:
- states need to respond to viewport / content;
- source assets remain 2D;
- composition should stay editable;
- interactions need live control.

Requirements:
- semantic content remains available;
- lifecycle / resize behaviour;
- clear reduced-motion state;
- motion ownership between timelines.

Risk:
- attempting fake 3D / fake room geometry with 2D layers.

## 3. Live Canvas / WebGL / 3D

Examples:
- real camera path;
- 3D object;
- shader / material;
- particle field;
- depth-aware interactive scene.

Use when:
- real-time viewpoint / material / depth is integral;
- interaction meaningfully depends on live rendering;
- pre-rendered media would remove essential agency or responsiveness.

Requirements:
- performance budget;
- loading state;
- device fallback;
- lifecycle / disposal;
- accessible DOM alternative;
- input strategy.

Risk:
- WebGL vanity: complexity without a better experience.

## 4. Pre-rendered motion

Examples:
- Blender camera move;
- composited light / material sequence;
- AI-assisted room film;
- video transition;
- rendered object turn.

Use when:
- visual fidelity matters more than runtime interactivity;
- the scene is difficult or expensive to simulate live;
- camera / material continuity can be authored beforehand.

Requirements:
- useful start / end frames;
- responsive crop strategy;
- poster frame;
- compression / encoding plan;
- loading / autoplay behaviour;
- reduced-motion state.

Risk:
- video becomes wallpaper or cannot adapt to layout.

## 5. Scrubbed pre-rendered motion

Examples:
- frame sequence;
- video / canvas playhead mapped to scroll;
- rendered camera travel under user-controlled progress.

Use when:
- pre-rendered visual fidelity is needed;
- user progression should control time;
- discrete chapter states align with media progress.

Requirements:
- preload strategy;
- seeking / frame availability;
- reverse behaviour;
- mobile tier / simplification;
- poster / static fallback;
- dead-scroll testing.

Risk:
- high weight, frozen frames, progress mismatch, poor reverse.

## 6. Compare classes

Ask:

| Question | Why it matters |
| --- | --- |
| Does the effect need real-time agency? | If no, pre-rendering may be simpler |
| Does content change frequently? | Live DOM may be more maintainable |
| Does motion reveal real geometry? | Still / DOM may be insufficient |
| Is cinematic fidelity more important than interaction? | Pre-render may win |
| Must progress be user-controlled? | Scrubbed media may fit |
| Is the device / network budget tight? | Still / simpler live motion may be stronger |
| Does reduced motion preserve the same meaning? | If not, concept may depend too heavily on choreography |
| Can the team maintain the chosen class? | Long-term cost matters |

## 7. Fallback hierarchy

Design the fallback as an equivalent experience, not an apology.

Possible hierarchy:

1. full intended behaviour;
2. lighter runtime behaviour;
3. pre-rendered / compressed equivalent;
4. resolved still state;
5. direct semantic content.

Not every project needs all levels.

## 8. Mobile translation

Mobile may require:

- different crop;
- shorter travel;
- direct vertical sequence;
- touch control;
- fewer simultaneous layers;
- lower frame count;
- video instead of WebGL;
- still instead of scrubbed media.

Do not merely multiply desktop motion values by a smaller number.

## 9. Reduced motion

Preserve:

- order;
- hierarchy;
- state;
- proof;
- interaction meaning;
- navigation.

Possible substitutions:

- crossfade;
- direct resolved state;
- static pair;
- manual carousel / comparison;
- no parallax;
- poster frame;
- shorter distance;
- no autoplay.

## 10. Performance and maintenance questions

Before selecting a heavy class ask:

- What is loaded before first interaction?
- What can load later?
- How many heavy media systems coexist?
- Does one scene stay mounted across the page?
- What happens on resize / route change?
- Who can update the assets?
- Will a CMS edit break the choreography?
- What is the simplest production class that still achieves the required perception?

## 11. Handoff to engineering

Provide:

- selected production class;
- reason;
- interaction requirement;
- asset assumptions;
- start / end states;
- responsive / reduced-motion behaviour;
- performance risks;
- known implementation constraints.

Engineering chooses the exact framework unless the requirement already constrains it.


## Runtime handoff

When a production class is selected and implementation becomes a real task, load `runtime-contract-and-verification.md` for state ownership, lifecycle, loading, accessibility, and real-browser verification. Then load only the exact technical reference needed for the named implementation question.
