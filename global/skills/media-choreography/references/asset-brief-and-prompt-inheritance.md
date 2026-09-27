# Asset Brief and Prompt Inheritance

Load when a photographer, filmmaker, renderer, compositor, or media model needs enough context to produce a coherent asset or asset family.

Use a few lines for a small job. Expand only where a decision would otherwise be lost.

## Inherit real authority, not a fixed file stack

Pull from whichever current sources actually govern the project:

- verified project facts and roles;
- selected / provisional concept and visual subject;
- narrative / proof job;
- approved or exploratory motion behaviour;
- available source images, plans, models, footage, and rights;
- responsive, text, poster, and fallback requirements.

Label:

- observation;
- client report;
- creative hypothesis;
- unknown.

Do not require a fixed dossier / brief / blueprint / production-plan stack when the decisions already exist elsewhere.

## Write a producer-ready brief

Use only relevant fields:

| Field | Decision it protects |
| --- | --- |
| **Media role** | Proof, atmosphere, exploration, transition, interaction, context |
| **Truth status** | What the result may legitimately imply |
| **Subject identity** | What must remain recognizable and whose work it represents |
| **Source material** | What exists, provenance, rights, permitted alteration |
| **Composition requirement** | Focal point, crop, overlay region, camera side / viewpoint when material |
| **State sequence** | Entry, significant change, resolution, poster / fallback |
| **Continuity anchors** | Geometry, materials, light, people, project identity |
| **Motion requirement** | Camera and subject movement stated separately, inherited from motion direction |
| **Output use** | Page / section, aspect intent, rendered-size quality, mobile translation |
| **Proof / rights limit** | What the asset may and may not claim |
| **Acceptance check** | Visible failure that makes the asset unusable |

## Generated media roles

Before prompting, state what generation is doing:

- private study;
- concept exploration;
- mood / atmosphere;
- speculative art direction;
- source-state development;
- non-factual transition media;
- approved illustrative client-facing media;
- extension / cleanup;
- another explicit role.

State whether the output is:

- factual representation;
- illustrative;
- speculative;
- synthetic extension;
- unknown.

Do not let provider output decide this after generation.

## Build prompts from the brief

Provider-ready prompts are downstream production instructions, not brand or concept authority.

Include only the source references, constraints, state changes, exclusions, and output requirements the provider needs.

Preserve approved project facts. Do not fill missing details with plausible invention.

A compact prompt-source block may include:

```text
Media role:
Truth status:
Subject:
Source / reference:
Viewpoint / framing:
Light / material constraints:
Continuity anchors:
Camera movement:
Subject movement:
Entry state:
Resolved state:
Text / crop constraint:
Mobile / fallback:
Must preserve:
Must avoid:
```

Use only relevant fields.

## Source-image-to-video

When continuity matters:

1. approve / inspect the still source state;
2. confirm subject, geometry, camera, light, material, crop;
3. define camera movement separately from subject movement;
4. state what must remain stable;
5. define the useful resolved / end state;
6. identify warping / morphing failures to avoid;
7. define how the result will hand into the webpage.

Do not ask video generation to solve unresolved composition.

## Asset families

For a family, establish shared context and controlled difference.

Possible shared anchors:

- room / project identity;
- camera family;
- lighting family;
- material fidelity;
- person / object identity;
- framing rhythm;
- text / crop behaviour.

Variation may be intentional.

The goal is controlled continuity, not identical outputs.

## Provider-specific handoff

Only after a provider is selected, add provider-specific details such as:

- syntax;
- reference-image controls;
- duration;
- aspect;
- seed / consistency control;
- motion controls;
- quality mode.

Do not confuse prompt length with art-direction quality.

## Review the result independently of the prompt

Inspect at website size.

Check:

- factual role;
- subject integrity;
- geometry;
- light;
- material;
- continuity;
- crop;
- text collision;
- motion plausibility;
- compression;
- entry / resolved state;
- mobile viability.

A prompt-compliant output can still be false, ugly, or unusable.

When repeated generation cannot meet the requirement, revise the source method or the creative assumption rather than endlessly rewriting the prompt.
