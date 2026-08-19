# Volatile Source Verification Baseline

Verification date: 2026-08-19

## Rule

Volatile platform, legal, API, pricing, product-limit, and tool-version claims require a primary source and a verification date. If no current primary source supports a claim, mark it unverified, quarantine it as historical research, and do not make production decisions from it.

## Current Records

| Area | Verified claims | Primary source | Result |
| --- | --- | --- | --- |
| Google Flow | Flow is a Google interface/workflow surface. Its dated support matrix lists Veo 3.1 - Lite, Fast, Quality, and Gemini Omni Flash with model-dependent controls. Credits, plans, region, feature exposure, and active cost remain account/UI-dependent. | [Flow model matrix](https://support.google.com/flow/answer/16352836?hl=en), [Flow credits](https://support.google.com/flow/answer/16526234?hl=en) | Rechecked 2026-08-19; inspect the active UI before production use. |
| Seedance 2.0 | The dated 2026-02-12 launch announcement describes four input modalities, 9/3/3 reference counts, editing/extension, 15-second multi-shot audio-video output, dual-channel audio, and real-person authorization. | [Seedance 2.0 official launch](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0) | Historical version-specific evidence; not a universal creator/API limit. |
| Seedance 2.5 | The dated 2026-07-31 launch announcement describes up to 30-second clips, multiple extensions, timestamped editing, and 30/10/10 reference counts. | [Seedance 2.5 launch](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) | Historical version-specific evidence; confirm active surface access and controls. |
| Seedance creator/API behavior | Surface labels, limits, roles, pricing, access, region, moderation, export, and terms vary across Dreamina/Jimeng/Doubao/CapCut/ModelArk. | [ModelArk documentation](https://docs.byteplus.com/en/docs/ModelArk/2607689) | Active-surface check required. |
| Legal/API/filter narratives | Universal prompt limits, filter-pass techniques, named-party enforcement causes, fixed endpoint behavior, universal availability, or blanket legal clearance. | No matching current primary evidence established | Unverified; historical only. |

## Reverification Trigger

Reverify before production use, when the active surface differs by region, when a dated record is older than 90 days, or when observed behavior conflicts with this baseline.
