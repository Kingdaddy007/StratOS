# Skills

This directory is the canonical source for Anti-Gravity task behavior. Every skill has portable frontmatter, folder-matching identity, conditional reference routing, and host UI metadata under `agents/openai.yaml`.

## General profile

General engineering is the default. It includes architecture, coding, testing, debugging, security, database, API, DevOps, performance, product, research, review, refactoring, marketing, sales, general UI/UX, and other non-spatial capabilities.

Engineering delivery adds `pr`, `retro`, `implement-spec`, `tdd`, `code-review`, and `writing-for-agents`. `retro` and `implement-spec` require an explicit user request; their Codex UI metadata disables implicit invocation. Use `learn` for broader capability promotion, `testing` for evidence selection, and `review-audit` for risk interpretation. Existing local specs and tracker configuration are sufficient; no upstream setup command is required. Source attribution and adaptation decisions are recorded in [the adoption record](../../docs/engineering-skills-adoption.md).

`ui-ux/SKILL.md` detects product, brand, or spatial register. Product and application work uses its general workflow; spatial references load only when the spatial profile or request is explicit.

## Spatial profile

The optional spatial profile adds:

- `spatial-experience-design`
- `brand-strategy`
- `storytelling`
- `cinematic-motion`
- `media-choreography`
- `master-design-director`
- `motion-library`
- `scroll-storyboard`
- `spatial-outreach-site-sprint`

Use it for interior, showroom, gallery, furniture, decor, staging, luxury-home, or architecture-adjacent work. Do not activate it merely because a task has a frontend.

Within the spatial profile, `media-choreography`, `cinematic-motion`, and `scroll-storyboard` are conditional specialists. `cinematic-showroom-strategy` remains a temporary compatibility route for legacy callers. A still-image experience can complete the workflow without media or motion specialists.

`spatial-outreach-site-sprint` is the private local build route for a prospect-specific spatial concept. It keeps evidence, claim, rights, verification, and external-sending boundaries explicit.

## Resource contract

- Keep runtime behavior in `SKILL.md` concise.
- Put detailed procedures, examples, recipes, and volatile facts in `reference/` or `references/`.
- Link every resource from the parent skill and state when it should be loaded.
- Add a contents section to long references.
- Treat dated platform, legal, API, and enforcement claims as historical until reverified against a primary source.

## Validation

Run:

```bash
python global/scripts/os.py validate
```

The validator rejects mismatched names, unsupported canonical metadata, missing UI metadata, broken routes, personal paths, and non-portable links.
