---
name: scroll-storyboard
description: 'Use this skill when an approved experience depends on authored scroll timing, pinning, transitions, persistent continuity, or media choreography, or when an existing site feels disconnected because sections were designed independently. Activated by "storyboard the scroll", "map scroll beats", "plan the pinned sequence", "how should the scroll feel", or a need to coordinate viewport-by-viewport narrative behavior. Do NOT use for ordinary page sequencing, copywriting, static editorial layouts, or as a universal precondition for design and implementation.'
---

# Scroll Storyboard

## WHEN TO USE THIS

- Load after a concept is selected and the experience architecture is approved.
- Load when scroll depth controls narrative timing, pinning, persistent objects, register changes, or media states.
- Load to audit an existing experience whose transitions or section continuity feel disconnected.

## NEVER DO

- Never require a scroll storyboard for a static, lightly animated, or conventionally scrolling page.
- Never invent scroll spectacle to justify using this skill.
- Never add a beat or animation without asking what communication job occurs at that depth.
- Never require an anchor object when composition, typography, color, image logic, or a deliberate hard cut already provides continuity.
- Never let pinned choreography hide proof, navigation, inquiry, or accessible alternatives.
- Never storyboard before the controlling argument and chapter jobs are approved.

## WHAT THIS IS

A **Scroll Storyboard Contract** is a conditional translation layer between:

- `storytelling` - controlling argument, chapter jobs, emotional arc;
- `spatial-experience-design` - approved composition, asset, and interaction system;
- `cinematic-motion` - motion jobs, tracks, timing, fallbacks;
- implementation - semantic sections, scroll ranges, timelines, and responsive behavior.

It normally lives in `scroll-storyboard.md`. Equivalent approved choreography inside `experience-blueprint.md` or `production-plan.md` is acceptable.

Before mapping depths, inherit the intended feeling curve from `storytelling`.
Name the primary remembered peak and ending impression. Treat one primary peak
as a pacing discipline, not a compulsory spectacle: if the approved story needs
another shape, record why. Avoid adjacent beats with indistinguishable feeling
and intensity unless the hold is deliberate.

## ACTIVATION TEST

Create the artifact only when at least one answer is yes:

1. Does meaning change at authored scroll depths rather than ordinary document flow?
2. Is content pinned, scrubbed, sequenced, or synchronized with media?
3. Must an object, image, word, register, or material persist across multiple beats?
4. Would independent section implementation create a continuity or timing failure?
5. Is a complex mobile or reduced-motion translation needed?

If all answers are no, record `scroll storyboard: not required` in `production-plan.md` and continue.

## STORYBOARD TABLE FORMAT

Produce one row per narrative beat: any moment where the visitor's emotional state, visual register, evidence, or argument changes because of scroll.

| Beat # | Label | Scroll Depth | Controlling Idea | What the User Sees | What the User Feels | Register | Continuity Device | Copy Mode | Transition Out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Column Definitions

- **Beat #:** Sequence; decimal inserts are allowed.
- **Label:** Short scene name, such as “The Dark Threshold” or “The Weight of Stone.”
- **Scroll Depth:** Relative depth, pin duration, or progress range.
- **Controlling Idea:** The claim this beat proves or prepares.
- **What the User Sees:** Concrete dominant visual, not “some animation.”
- **What the User Feels:** One or two target emotions.
- **Register:** `LIGHT`, `DARK`, `TRANSITION`, or a project-defined equivalent.
- **Continuity Device:** Optional persistent object, material, color, crop, type treatment, sound cue, or `NONE`.
- **Copy Mode:** `SILENT`, `ATMOSPHERIC`, `DECLARATIVE`, `EDITORIAL`, or `INVITATION`.
- **Transition Out:** `DISSOLVE`, `HARD CUT`, `PORTAL`, `DRIFT`, `ANCHOR HOLD`, or a named project-specific transition.

## BEAT TAXONOMY

Use only the beat types the selected narrative needs.

| Beat Type | Purpose | Typical Register | When to Use |
| --- | --- | --- | --- |
| **THRESHOLD** | Establishes the world and filters attention | Light or dark | When the opening needs an authored entrance |
| **ARGUMENT** | States the controlling idea | Either | When the claim needs explicit emphasis |
| **IMMERSION** | Pulls the visitor into the brand world without selling | Often dark | When atmosphere must precede proof |
| **PROOF** | Shows capability, work, transformation, or rigor | Either | Wherever trust must be earned |
| **PHILOSOPHY** | Explains the studio's way of seeing | Dark or transition | To connect work and method |
| **MATERIAL** | Shows sensory or craft intelligence | Often light | For material/process-led arguments |
| **INTERACTION** | Gives user agency to reveal or compare | Either | Sparingly, when agency improves understanding |
| **HARD CUT** | Intentionally resets attention or reframes the argument | Transition | Only when the narrative earns contrast |
| **ANCHOR HOLD** | Keeps one element while surrounding meaning changes | Often dark | When persistence clarifies continuity |
| **INVITATION** | Creates a calm, selective inquiry gate | Either | When readiness has been earned |

No beat type is universally required. A quiet page may use ordinary document flow and no storyboard at all.

## REGISTER SWITCHING

- Use one primary register with only justified excursions.
- A register change must express a narrative event, not supply arbitrary variety.
- Treat a hard cut or portal as a designed scene when the change is consequential.
- Do not impose a light/dark binary when the selected visual system uses another register model.

## CONTINUITY DEVICES

An anchor object is one possible continuity device, not a universal law. Continuity may instead come from crop logic, grid, typographic cadence, repeated material, color, sound, pacing, or a deliberate break.

When an anchor object is useful:

- Name its communication job before its path.
- Map position, scale, occlusion, collision-safe text zones, and responsive behavior.
- Keep it only while it improves orientation or argument.
- Mark `NONE` neutrally; it is not automatically a risk.

## PRODUCTION PROCESS

1. Read the selected territory, experience blueprint, and production constraints.
2. Confirm the activation test and record why a storyboard is required.
3. Name the controlling argument and the chapters affected by authored scroll.
4. Choose registers and continuity devices only where useful.
5. Write the beat table from narrative need, not existing effects.
6. Map desktop, mobile, reduced-motion, loading, and failure behavior.
7. Reconcile the table with media choreography and implementation ownership.
8. After implementation, perform a cold-scroll review: scroll once without
   reading code, record one felt word per beat, identify the perceived peak and
   ending, and compare them with the intended curve.
9. Obtain the applicable Director and user approval before complex implementation.

## INTEGRATION

| Downstream Consumer | What It Receives |
| --- | --- |
| Semantic page structure | Beat order and grouping, where scroll changes structure |
| Motion implementation | Progress ranges, pins, transitions, and timeline ownership |
| Visual system | Register scope and continuity rules |
| Media choreography | Cue timing, text-safe states, loading, and fallbacks |
| Accessibility | Reduced-motion and non-scroll equivalent |
| Responsive implementation | Mobile simplification and touch behavior |

The storyboard never supersedes the approved creative brief or selected concept. If they conflict, return to the Director gate.

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Fix |
| --- | --- | --- |
| Section Island | Adjacent beats have no argumentative relationship | Reconnect chapter jobs or use a deliberate cut |
| Motivation-Free Register Change | Visual mode changes only for variety | Require a narrative reason or remove it |
| Forced Anchor | An object travels because the template expects it | Replace it with the simplest useful continuity device |
| Copy Mode Collision | Copy posture fights the beat's job | Match copy mode to evidence and emotional state |
| Threshold Too Long | Opening delays access without earning attention | Shorten, simplify, or use ordinary flow |
| Orphan Section | A section does not continue or qualify the argument | Delete, move, or rewrite it |
| Desktop-Only Choreography | Mobile and reduced-motion become broken leftovers | Design equivalent experiences before implementation |

## OUTPUT SHAPE

**New storyboard:** Activation rationale -> controlling argument -> intended feeling curve and primary peak -> register/continuity map -> beat table -> mobile/reduced-motion translation -> cold-scroll comparison -> implementation notes.

**Audit:** Existing beat map -> disconnections -> timing and accessibility risks -> recommended repairs.

## NON-NEGOTIABLE CHECKLIST

1. The activation test justifies creating a storyboard.
2. The controlling argument and chapter jobs are already approved.
3. Every beat has a communication job.
4. Registers and continuity devices are optional and justified.
5. Every authored transition has desktop, mobile, and reduced-motion behavior.
6. Proof, navigation, and inquiry remain reachable.
7. The storyboard does not contradict the selected concept or creative brief.
8. The intended and felt curves, primary peak, and ending are compared after implementation when observable scroll exists.
