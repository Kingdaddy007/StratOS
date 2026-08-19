# Local Design-Audit Library

## Purpose

The local Design-Audit Reference Library is a curated Spatial precedent
collection. It gives a Spatial project a way to retrieve a specific design or
motion question without pretending that every premium site needs cinematic
motion, WebGL, or an award-site visual language.

Use it only after the project has a named question, such as:

- How could one project object carry continuity across a portfolio?
- What would make this room-by-room sequence feel editorial rather than like a
  template?
- Is a sequence-scrub renovation story worth its asset and performance cost?
- Which existing pattern should we reject because it would bury proof or
  usability?

## Evidence Rules

The 30 local reports are **mediated reference notes**, not automatic current
technical specifications. Their design observations can suggest a candidate;
their proposed "upgrade" sections do not authorize a skill rewrite, a
dependency, or an implementation choice.

For a new source supplied by Beloved:

| Source | Evidence label | Handling |
| --- | --- | --- |
| A recording or page directly inspected by a vision-capable agent | `OBSERVED` for what is visibly demonstrated | Preserve timecodes/positions and mark trigger ambiguity. |
| A transcript or analysis produced by another AI | `REPORTED` | Keep the original recording or screenshots where possible; do not turn its implementation guesses into facts. |
| A written recollection, moodboard caption, or link that cannot be viewed | `REPORTED` or `UNKNOWN` | Use only to form questions or request the missing source. |

Always load [source-forensics.md](source-forensics.md) for recordings,
screenshots, transcripts, or AI observation reports. A transcript helps the
agent search, compare, and remember a source; it is not a substitute for visual
evidence when visual decisions are important.

## Retrieval and Translation

1. Confirm that the Spatial pack is active. This reference is not a General
   product/UI library.
2. State the project decision and the named reference question.
3. Start at the active host payload's Design Audit library index, then use the
   Spatial adaptation map supplied with the Spatial Experience Design package.
   In an Antigravity payload these are normally
   `.agents/reference/design-audit/library-index.md` and
   `.agents/skills/spatial-experience-design/reference/audit-mechanics-map.md`.
   In another host, use the generated payload's equivalent locations rather
   than guessing a repository-relative path.
4. Load only the raw report(s) that answer the question. Compare no more than
   necessary; a single strong source may be enough.
5. Separate the observed/reported pattern from any inferred technology or
   historic gap claim.
6. Translate the candidate through the current brand, proof burden, asset
   reality, mobile, reduced-motion, accessibility, performance, maintenance,
   and budget constraints.
7. Record `KEEP`, `ADAPT`, `REJECT`, or `DEFER`, including what is explicitly
   not copied.

The result is a design decision or a bounded experiment—not permission to copy
another site, add heavy tooling, generate media, or begin implementation.
