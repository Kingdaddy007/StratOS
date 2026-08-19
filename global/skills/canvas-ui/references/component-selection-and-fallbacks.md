# Canvas UI Component Selection and Fallbacks

**Primary-source snapshot:** 2026-08-19  
**Sources:** [Canvas UI repository](https://github.com/DavidHDev/canvas-ui) and
[Canvas UI documentation](https://canvasui.dev/).

## Source boundary

Canvas UI is a third-party component source, not an Anti-Gravity dependency or
an automatically installed tool. The upstream project documents framework
wrappers and a shadcn-compatible source-copy workflow. Its feature set, browser
support, component names, licence, and commands can change. Recheck the exact
upstream component and licence before source enters a client project.

Do not use the old host-local `Kingdaddy007` URL as an upstream source. Do not
present generic local shader snippets as official Canvas UI code unless their
origin and licence are independently established.

## Choose by visual job

| Visual job | Candidate family | Prefer a simpler route when | Required fallback |
| --- | --- | --- | --- |
| Let a material or image respond to deliberate pointer interaction | Fluid, ripple, cloth, or displacement effect | The effect is merely decorative or a CSS state carries the meaning | Static image/material treatment or restrained DOM response |
| Create one optical transition or focus moment | Glass, frost, magnify, peel, or related optical effect | Readability, focus, or task completion is reduced | Unfiltered DOM content with ordinary focus/hover state |
| Make a bounded reveal communicate transformation | Particle, laser, shatter, or structured reveal | A fade, crop, or staged media sequence says the same thing | Still or DOM reveal that preserves the source order |
| Inspect a real object, model, or material | 3D-object treatment | A GLB/SVG/image lacks rights, quality, mobile budget, or a real inspection job | Image, turntable video, or labelled gallery |
| Carry a whole spatial journey | Usually reject Canvas UI as the first answer | A canvas sequence, real film, or ordinary document flow is clearer | Narrative DOM/media layout with reachable navigation |

## Browser and performance reality

The upstream documentation distinguishes richer HTML-in-canvas treatments from
WebGL-overlay fallbacks. Treat the full HTML-in-canvas result as experimental:
never rely on a browser flag, trial, or account configuration without a
current, project-specific check. Keep core content and controls as working DOM
in all supported browsers.

Before accepting a vertical slice, demonstrate:

1. DOM content, links, focus, keyboard operation, and core CTA work with the
   effect disabled or unavailable.
2. The enhanced effect has a defined desktop and mobile quality tier.
3. Reduced motion removes continuous travel while retaining meaning.
4. Resize, unmount, route change, and offscreen states cancel work and release
   listeners, animation frames, and graphics resources.
5. The page does not combine unbudgeted heavy video, image sequences, and
   realtime scenes in the first viewport.

## Import decision record

Request approval with this minimum record before any upstream import:

```text
Component/effect: <exact current upstream identifier>
Visual job: <what it communicates>
Why simpler routes lose: <still / DOM-CSS / media comparison>
Contained surface: <one component or section>
Source and licence checked: <URL, revision/date, result>
Expected mutation: <CLI, copied source, dependency, configuration>
Fallback: <ordinary DOM/mobile/reduced-motion treatment>
Verification: <desktop, mobile, keyboard, reduced-motion, cleanup, budget>
Rollback: <remove isolated component and retain fallback>
```
