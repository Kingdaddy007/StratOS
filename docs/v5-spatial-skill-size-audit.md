# V5 Spatial Skill Size Audit

The Skills directory uses 15 KB as a default `SKILL.md` guardrail.
These accepted V5 packages intentionally exceed 15,360 bytes:

| Skill | UTF-8 bytes | Retained in the entrypoint |
| --- | ---: | --- |
| `cinematic-motion` | 17,015 | Motion jobs, tracks, grammar, production choices, runtime boundary, and fallbacks must stay visible together when the skill activates. |
| `master-design-director` | 16,955 | Critique ownership, judgement checks, intervention priorities, and the teaching response must stay visible together. |

Both packages keep detailed examples and deeper technique guidance in their
`references/` files. Their active entrypoints remain about 1–2 KB above the
default guardrail; splitting those decision rules further would make the core
contract easier to miss.

Verification: `python global/scripts/os.py validate`, the Spatial workflow
contract tests, the V5 host payload tests, and inspection of each generated
`SKILL.md` plus its conditional reference links. Revisit these exceptions only
if a real loading or comprehension problem appears.
