# V4 Canvas UI Candidate Audit

**Status:** Registered as a conditional Spatial decision capability; no upstream
component source is installed or distributed  
**Decision date:** 2026-08-19  
**Scope:** The host-local `canvas-ui` skill supplied for review and the
upstream Canvas UI project; no component source was copied and no package or
CLI command was run.

## Decision in one sentence

Canvas UI is an approved *optional decision capability* for a specific kind of
expressive web moment. It is not a universal design system, a default for every
website, or a reason to replace semantic HTML and ordinary interface motion.

## What it is

The current primary source is [DavidHDev/canvas-ui](https://github.com/DavidHDev/canvas-ui)
and [canvasui.dev](https://canvasui.dev/). It provides individual,
framework-specific creative components that place HTML-in-canvas or WebGL
effects over a live, interactive DOM. The source says that component source is
copied into the project through a shadcn-compatible registry, rather than used
as a conventional runtime package.

That makes it useful when a real visual idea needs one controlled effect — for
example, a material-led reveal, a quiet optical lens, or a distinctive 3D
object moment — and not when an ordinary page merely needs to look "more
premium."

## What the supplied local skill gets right

- Preserve semantic HTML, selectable text, and ordinary interaction.
- Select the smallest component that fulfils a named visual job.
- Keep the canvas responsive to its container.
- Dispose animation frames, WebGL resources, and listeners on unmount.
- Check mobile cost and provide a reduced-motion alternative.

Those are durable V4 rules. They should be retained if a future canonical
capability is created.

## Corrections and risks

| Finding | Why it matters | V4 treatment |
| --- | --- | --- |
| The local source calls `Kingdaddy007/canvas-ui` official, but the verifiable upstream source is `DavidHDev/canvas-ui`. | An agent could fetch the wrong fork or stale code. | Do not retain the Kingdaddy URL as an installation source. Record the official source and verification date instead. |
| The local catalogue lists 25 components; the current upstream documentation lists more. | A fixed full catalogue becomes stale quickly. | Keep a short selection index only; direct an implementation task to verify the needed component at that time. |
| Several effects depend on experimental HTML-in-canvas support. | The "full" effect is not a safe production assumption across browsers. | Require a browser-support decision and a working DOM/WebGL fallback before approval. |
| The upstream installation flow uses the shadcn CLI and may add source and dependencies to a project. | It is an environment/dependency mutation, not a harmless suggestion. | No automatic fetch, `npx`, registry MCP call, or installation. Explain the exact proposed change and obtain approval immediately before it. |
| The upstream license is described as MIT plus the Commons Clause. | It is not plain MIT; source provenance and redistribution constraints matter. | Check the current upstream licence before each source import and record the chosen component, source revision, and licence result in the project. |
| The supplied shader recipes have no primary-source provenance. | They cannot be represented as official Canvas UI recipes or blindly copied into a client project. | Keep them out of the canonical package until they are individually attributed, reviewed, and tested. |

## Correct role in the Product Studio

Canvas UI belongs, if adopted, in the **optional Spatial pack** as a narrow
implementation capability. It can be directly invoked as `$canvas-ui`, but it
must never activate merely because a task mentions a website, animation, or a
hero section.

It is eligible only when all of these are true:

1. The project has a named visual and communication job that a still, CSS, or
   conventional DOM implementation cannot meet as well.
2. The target component/effect is selected deliberately rather than by visual
   novelty.
3. Semantic content, keyboard use, navigation, and the core action remain
   usable without the effect.
4. A mobile and reduced-motion treatment is specified.
5. The page has a performance budget, and this is not a second heavy realtime
   canvas scene on the same page without explicit justification.
6. The project owner approves the dependency/source change before an external
   registry or CLI is used.

It is ineligible for generic cards, standard hover states, ordinary product
interfaces, unclear visual concepts, or a page that already carries heavy
video, frame sequences, and WebGL in its first viewport.

## How it should work with the V4 design model

The Design Director—not a rigid workflow—decides whether Canvas UI is worth
considering. `reference-intelligence` can translate reference material into a
specific visual job. `cinematic-motion` then compares stillness, CSS/DOM
motion, pre-rendered media, and realtime canvas before choosing one. Canvas UI
is one possible implementation route, never the default answer.

For a qualifying request, the order is:

```text
creative intent + evidence
  -> name the visual job
  -> compare still / DOM-CSS / media / Canvas UI
  -> define fallback and budget
  -> obtain approval for any source or dependency change
  -> build one isolated vertical slice
  -> test desktop, mobile, reduced-motion, interaction, and cleanup
  -> expand only if the slice earns its place
```

Beloved remains the decision owner for the creative direction. A temporary
worker can compare candidate effects, inspect a supplied reference, or verify
the resulting implementation, but it should not autonomously choose an effect
or import code.

## Component-import gate for a live project

The decision capability is registered in `global/manifest.yaml` so the Studio
and Design Directors can surface it intelligently. Before a live project imports
an upstream component, all of the following must be complete:

- A short primary-source refresh confirms the upstream URL, licence, browser
  support, installation method, and desired components at the time of use.
- A canonical skill is written as a lean activation and decision contract, not
  a frozen component dump. It has a reference index with conditional loading.
- The package does not contain copied upstream code unless the applicable
  licence and source record permit it.
- A local, disposable vertical-slice fixture proves semantic fallback,
  reduced-motion behaviour, responsive resize, cleanup, and budget evidence.
- The Spatial profile is updated only after that fixture passes and the user
  explicitly approves the promoted skill.

Until then, the correct statement is: **V4 can intelligently consider Canvas
UI, but it does not ship or automatically import any Canvas UI component.**

## Primary sources checked

- [Canvas UI upstream repository](https://github.com/DavidHDev/canvas-ui) —
  identity, component model, installation pattern, browser constraints, and
  licence statement; checked 2026-08-19.
- [Canvas UI site](https://canvasui.dev/) — component catalogue, framework
  targets, fallback claims, reduced-motion and lifecycle claims; checked
  2026-08-19.
