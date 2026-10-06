# OS source and installation comparison

Snapshot date: 2026-10-06. Comparison base: freshly fetched GitHub `main` at `d9e1d01`. Current authored source includes engineering adoption commit `28984ff`, the existing main history, and the documentation/regression changes recorded below.

## Inventory difference

| Surface | GitHub main before publication | Current authored and installed OS |
| --- | --- | --- |
| Registered skills | 51 | 57 |
| Registered workflows | 17 | 17 |
| Registered agents | 6 | 6 |
| Profiles | General, Spatial, Media, Growth | Same four profiles |
| Spatial creative system | V5, router V5.2.1, inception workflow version 6 | Same current system |
| Engineering helpers | Existing coding/testing/review/learning capabilities | Adds pr, retro, implement-spec, tdd, code-review, writing-for-agents |

The portable manifest's OS release metadata remains `4.0.0`. V5 labels the spatial creative system and router evolution; this update does not invent a new whole-OS release number.

## What is being published

- Six adapted engineering skill packages, including Codex metadata, MIT notices, and source attribution.
- Engineering routes in `GLOBAL_MEMORY.md`, the existing `learn` link to requested retrospectives, and `to-tickets` glossary/local-tracker compatibility.
- Six static routing fixtures, four build/native-installer packaging tests, and adoption/usage evidence.
- README inventory correction from 51 to 57 and a link to the engineering usage guide.
- Two public host-build regression tests restored from the useful profile-scoping intent of the older spatial-sprint test: General excludes the spatial sprint; Spatial includes the complete package on Codex and Anti-Gravity.
- A portable temporary-directory fixture for native-installer tests: macOS's `/var` alias is resolved before constructing the controlled test home, preserving the installer's symlink protection.

No existing workflow source or functional-agent contract needs replacement. GitHub already contains the V5 Creative Constitution, current spatial skills and private outreach lane, media choreography, design-audit resources, installer improvements, and router-linked shared-reference fix. The pre-existing `review-audit` remains intact; `code-review` is a new focused entry point using its risk guidance.

## Older checkout findings

The older checkout is still based on `9903900` and contains uncommitted work. Its outdated local base does not mean GitHub is still at that version. An independent read-only comparison found no missing runtime improvement in the inspected older changes: current V5 preserves their useful intent and updates their contract/reference names.

The repeat-install assertions already match current source. The dedicated older sprint test file was not present in the newer source; its observable profile/build coverage is restored without copying obsolete workflow headings, fixture IDs, or wording assertions. The old V4 decision note remains a historical artifact in the preserved older checkout. Older files are not used to overwrite current V5.

## Installation evidence

Both existing native Full-profile installations were compared with generated payloads and version-controlled canonical skill/workflow resources. All 388 compared authored files matched on each host, as did all 82 Codex and 93 Anti-Gravity managed payload targets. Generated Python caches are excluded from authored-source comparison, matching the builder's packaging rules.

The installed OS therefore already has the intended current source. Publication synchronizes GitHub with it; these documentation/test changes require no new global installation. User-authorized publication targets `main` after verification, using a normal pull-request merge without resetting the older dirty checkout or rewriting remote history.

## Verification limits

Canonical validation, local regression tests, installer syntax checks, whitespace checks, and GitHub CI are recorded during publication. Source/build/install checks establish the snapshot and packaging; they do not prove a future agent-run implementation, retrospective, live client project, or production deployment.
