# V4 External Skill Decision Ledger

**Evaluated:** 2026-08-22  
**Purpose:** Compare requested third-party skills with canonical V4 before any
adoption. Source files are evidence, not authority.

## Source snapshot

- UIZZE well-known endpoint: `anti-ui-slop` 1.2.13 and design stack 4.1.1.
- `heygen-com/hyperframes`: `718bf5ef32d4e521f686ea6ebe64545a6a2647ed`.
- `mattpocock/skills`: `5b15a47f2d7150f545fbcacbfe381787fc0230dc`.
- `aboudjem/humanizer-skill`: `9a7f35b7b9ad8c3abd71f10757ec9f91fb8ae165`.
- `petergyang/no-ai-slop`: `d30eddb9e04562234f2070b5ee63ca4649d9a05e`.

## Criteria

- Fills a verified capability gap rather than renaming an existing V4 route.
- Preserves V4 authority, approval, evidence, and host-portability contracts.
- Works when installed as the requested package, without hidden sibling skills.
- Adds enough value to justify discovery noise, maintenance, and external
  dependency risk.

## Decisions

| Source / candidate | Current V4 coverage | Decision | Result |
| --- | --- | --- | --- |
| UIZZE `anti-ui-slop` and `ui-design` | `ui-ux`, its design-bans and operation playbooks, `reference-intelligence`, and browser verification already cover product grounding, state coverage, critique, and finish checks. | **KEEP current V4; reject duplicate import.** | No canonical duplicate. UIZZE remains an optional evidence service. |
| UIZZE `ui-radar` | `reference-intelligence` already requires focused questions, direct observation, provenance, and translation. The UIZZE catalogue is a unique external dataset, not a portable core rule. | **DEFER.** | Consider a connector or optional skill only when live UIZZE access is available and a project has a named reference gap. |
| UIZZE `ui-slop-score` | V4 supports evidence-based critique without a pseudo-measurement. | **REJECT.** | A 0–100 “slop” score has no verified measurement model and can obscure accessibility, usability, and product-fit findings. |
| HeyGen `hyperframes` | V4 has provider-neutral video planning and separate cinematic/media routes, but no HyperFrames HTML-rendering integration. | **DEFER.** | The entry skill requires its CLI and multiple sibling workflow/domain skills. Treat it as a future optional Media-pack adapter, not a standalone core import. |
| Matt Pocock `grill-me` | `project-inception`, Studio Director intake, and first-principles routes already own clarification and challenge. | **REJECT.** | The requested package is only a forwarding stub to an uninstalled `grilling` skill and adds no standalone contract. |
| Matt Pocock `code-review` | `review-audit` already establishes the actual comparison, repository rules, behavioural intent, risk, and fresh Assurance review. | **ADAPT.** | Added explicit, separate Specification and Standards axes; parallel reviewers remain bounded and optional. Did not import its issue-tracker assumption or fixed three-dot diff. |
| `humanizer` | `copy-editing` already preserves meaning, voice, evidence, and edit scope. | **REJECT wholesale; ADAPT cautiously.** | Rejected arbitrary AI-probability scoring, zero-tolerance punctuation rules, forced “burstiness”, and instructions that could invent personality or lived detail. Retained only observable-pattern and voice-preservation ideas through the bounded reference below. |
| `no-ai-slop` | Same route as `copy-editing`; its detect-vs-edit distinction and named observable patterns are useful. | **ADAPT.** | Added `copy-editing/references/anti-slop-and-voice.md`; no duplicate top-level skill. |

## Security and dependency notes

The requested packages were copied into an isolated temporary evaluation
project with `npx skills add ... --copy`; none was activated globally during
evaluation. The installer’s advisory classified `code-review` as high risk,
`hyperframes` as medium risk, and the other named GitHub skills as low risk or
safe. Those labels are advisory evidence, not a substitute for the file review.

The UIZZE package contains optional external-service and upsell paths.
HyperFrames expects `npx hyperframes` plus lazy-installed sibling skills. V4
does not convert either dependency into a baseline requirement.
