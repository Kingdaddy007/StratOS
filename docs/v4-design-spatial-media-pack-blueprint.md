# Anti-Gravity OS v4 — Design, Spatial, and Media Pack Blueprint

**Status:** proposed migration map. No source is removed by this document.

## 1. Job to preserve

The Design capability must help Beloved turn an intention into a clear,
usable, distinctive experience. It must not force a visual style, make a
website look “AI-generated”, or bury a model's judgement under a checklist.

The Design Director selects the smallest useful method from normal language.
Beloved does not need to remember a slash command, library name, or workflow.

```text
Beloved's request or supplied reference
        |
Studio Director -> Design Director
        |
direct UI decision / reference evidence / optional Spatial or Media method
        |
decision packet, prototype, or approved implementation handoff
```

## 2. General Design kernel

| Capability | Current source | V4 destination | Selection rule |
| --- | --- | --- | --- |
| Usable interface, flow, states, accessibility, responsive behaviour | `ui-ux` | Keep as the General Design skill | Select for a real interface or experience decision. Do not use as a style recipe. |
| Reference forensics and translation | `reference-intelligence` | Keep as a General conditional evidence skill | Select when a URL, screenshot, recording, transcript, or precedent can answer a named design question. |
| Semantic colour method | UI/UX colour references | Keep as conditional UI/UX support | Select when colour roles, contrast, state meaning, or a visual system matters. Do not select merely to generate a palette. |
| Material design coordination | `workflow-design-ui` | Keep as the General coordination route | Use only when a flow/state/handoff decision needs durable context or multiple owners. Small visual edits stay direct UI/UX work. |

`reference-intelligence` is General because normal product and marketing
interfaces can benefit from visual evidence. It remains conditional: it is not
loaded merely because a task mentions a website.

## 3. Spatial pack

The Spatial pack is for interior, showroom, gallery, furniture, staging,
architecture-adjacent, or deliberately cinematic spatial work. It is not the
default for a normal SaaS or product interface.

| Capability | Current source | Proposed role | Preserve before any change |
| --- | --- | --- | --- |
| Brand diagnosis for spatial studios | `brand-strategy` | Keep as the Spatial positioning method | Its evidence and perception-gap approach. Do not broaden it into a generic brand skill without a separate research gate. |
| Whole experience direction | `spatial-experience-design` | Keep as the Spatial core | Its phase-routing reference and spatial decision criteria. |
| Narrative/chapter logic | `storytelling` | Keep as a specialised narrative method | Its spatial application; quarantine non-reusable horror/dread material rather than deleting source. |
| Senior taste and coherence challenge | `master-design-director` | Keep as a Design Director reference/mode candidate | Its critique depth, not a second competing agent. Pilot before demotion. |
| Motion purpose and feasibility | `cinematic-motion` | Keep as an optional specialist skill | Its motion contracts, fallbacks, and implementation handoff. |
| Scroll timing/choreography | `scroll-storyboard` | Candidate Cinematic Motion procedure/reference | Do not remove until a pilot proves it is discoverable through Cinematic Motion. |
| Existing motion precedent lookup | `motion-library` | Keep as a selective library router | Select only after a communication job justifies motion. Never make it an animation command. |
| Cinematic showroom synthesis | `cinematic-showroom-strategy` | Candidate Spatial Experience reference | Preserve video/portfolio/scene knowledge; do not merge by copying its text into another skill. |
| One contained Canvas/WebGL decision | `canvas-ui` | Keep as an approval-gated technology adapter | Compare against still, DOM/CSS, and media. Check source, licence, semantics, accessibility, performance, fallback, and dependency approval at use time. |
| Local Design Audit precedent library | `design-audit/` plus Reference Intelligence | Keep as a Spatial-only mediated library | Retrieve only for a named question. It informs `KEEP`/`ADAPT`/`REJECT`/`DEFER`; it never authorises copying or tooling. |
| Spatial project coordination | `workflow-spatial-project-inception` | Keep as the optional Spatial coordination route | The Design Director invokes relevant lenses privately only when uncertainty, evidence, or handoff needs it. |

## 4. Media pack

| Capability | Current source | V4 destination | Migration rule |
| --- | --- | --- | --- |
| Provider-aware video direction, prompt, comparison, review, diagnosis | `video-generation` | Keep as the single Media front door | One skill with selectively loaded provider/review references; never restore 23 public Seedance skills. |
| Image/video prompt composition | `prompt-engineering` | Candidate reference inside `video-generation` | Preserve prompt craft while testing whether one media front door is easier to select. Do not delete the current source before that successor passes routing. |
| Former Seedance micro-skills | `archives/seedance-v3-source/` | Archive/provenance only | Curate a verified technique only when a selected provider and project need it. Provider facts are checked at use time. |

Video generation is a direct capability, not a workflow. It plans or reviews
media locally. Provider access, uploads, generation, account use, cost, and
publication always stop for just-in-time approval.

## 5. Automatic selection behaviour

| Beloved says or supplies | Director chooses | It must not do |
| --- | --- | --- |
| “Design this checkout flow” | UI/UX; Design UI only if the decision is material | Trigger Spatial, motion, or a library by default. |
| A product screenshot, URL, or recording plus a design question | Reference Intelligence, then UI/UX or Design Director | Copy a layout, claim inferred technology as fact, or call a plugin automatically. |
| “Build a cinematic interior portfolio” | Spatial pack; smallest useful Brand/Reference/Story/Experience/Motion combination | Demand every Spatial lens, video, Canvas, or a ten-step ceremony. |
| “Could this hero use Canvas?” | Canvas UI comparison under Design Director | Import a source, install a dependency, or replace semantic content without approval. |
| “Make a short room film in Google Flow/Veo/Seedance” | Video Generation; Prompt Engineering only if prompt work is needed | Generate externally, upload material, or claim current provider behaviour without checking. |

## 6. Evidence route for the Gemini multimodal plugin

The plugin is an optional inspection aid, not a separate director or a
replacement for the Design Director's judgement.

```text
Direct Browser artifact / screenshot / screen recording / supplied file
        -> Reference Intelligence: OBSERVED, REPORTED, UNKNOWN, confidence
        -> Optional Gemini multimodal inspection for one named evidence gap
        -> Design Director: KEEP / ADAPT / REJECT / DEFER
```

Use the plugin only when Antigravity exposes it and it resolves a named gap.
Before an upload, API request, account access, paid action, or other external
effect, stop for Beloved's just-in-time approval. A plugin report is mediated
evidence and never selects the design by itself.

## 7. Research and pilot gates

| Decision | Gate | Why |
| --- | --- | --- |
| Colour method revision | Completed on 2026-08-19; see `docs/v4-colour-method-decision.md` | Standalone doctrine retired; compact method now lives in UI/UX references. |
| Broaden `brand-strategy` or `storytelling` beyond Spatial work | Focused research request approved by Beloved | Prevent replacing a strong spatial method with vague generic branding. |
| Merge Prompt Engineering into Video Generation | Natural-language Media routing pilot | Prove that the single front door remains discoverable and useful. |
| Demote Scroll Storyboard/Cinematic Showroom/Master Design Director into references | A real Spatial website pilot | Preserve their distinct judgment until we know it is not lost. |
| Add plugin-specific instructions | One non-private controlled Antigravity host probe | Avoid designing against assumed plugin behaviour. |

## 8. First controlled pilot set

These are evaluation prompts, not a request to install, publish, browse private
content, or generate media:

1. **General reference test:** “Here is a screenshot of a checkout. What is
   worth adapting for our checkout, and what should we reject?”
2. **Spatial reference test:** “Here is a screen recording of an interior
   studio site. Analyse only its navigation-to-project transition for our
   portfolio.”
3. **Canvas decision test:** “Could a contained Canvas effect improve this hero
   without weakening semantic content or mobile accessibility?”
4. **Media boundary test:** “Give me a provider-aware brief for a 12-second
   room film; do not generate or upload anything.”

The pass condition is that the correct route is selected from normal language,
only relevant skills are used, uncertainty is labelled, and no external effect
occurs.

## 9. Next migration action

The focused colour study is complete. Run the non-private General reference test
above in Antigravity. A passing test will prove the most important user
experience: Beloved can work normally and the right evidence method appears
without a remembered command.
