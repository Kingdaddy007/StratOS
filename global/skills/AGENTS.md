# Skills Directory Contract

## Purpose

This directory contains portable, model-invoked skills and their selectively loaded resources.

## Rules

- Keep each skill in a hyphen-case folder with a matching hyphen-case `name` in `SKILL.md`.
- Keep frontmatter portable: use `name`, `description`, and only supported optional fields.
- Put UI metadata in `agents/openai.yaml`; ensure its default prompt explicitly names the skill as `$skill-name`.
- Treat 15 KB as a default guardrail, not a quality target. Keep `SKILL.md` activation-first; move detailed examples, taxonomies, history, and edge cases into `references/` when that improves selective loading. Never remove behaviourally useful judgement merely to meet a size number. A deliberate exception needs an audit record that names the retained value and its verification path.
- Add conditional loading rules for every bundled resource. Link resources with relative paths; never use personal absolute paths or product-specific file tools.
- Treat dated platform behavior as a snapshot. Record the verification date and source, or require verification before use.
- Do not route to a sibling skill unless that skill exists in this directory and its folder name matches the route.
- Preserve domain behavior when refactoring. Move guidance; do not silently discard it.

## Resource Layout

- `SKILL.md`: activation, boundaries, core workflow, output contract, and verification gates.
- `agents/openai.yaml`: display name, short description, and default invocation prompt.
- `references/`: detailed operational guidance and a resource index when the package has multiple resources.
- `assets/`: output assets only; do not use it for explanatory documentation.
- `evals/`: positive, negative-routing, boundary, and regression cases.

## Verification

- Validate every `SKILL.md` frontmatter block and folder/name match.
- Validate every `agents/openai.yaml` interface field and `$skill-name` default prompt.
- Check all relative Markdown links and sibling-skill routes.
- Confirm no runtime `SKILL.md` exceeds 15 KB without an explicit exception.
- Run relevant evals after behavior changes.
