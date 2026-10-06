# Engineering skills: verification and use

Verified 2026-10-06 from the newer StratOS checkout, on local branch `codex/engineering-skills-adoption-20261006`. The older checkout's unrelated changes were preserved. No remote publication, default-branch merge, deployment, dependency installation, or memory update occurred.

## Installed result

Installed all six adapted packages into existing Full-profile Codex and native Anti-Gravity global installations:

- Codex discovery: `~/.codex/skills/`.
- Anti-Gravity discovery: `~/.gemini/config/skills/`.
- Added `pr`, `retro`, `implement-spec`, `tdd`, `code-review`, and `writing-for-agents`.
- Updated only the existing router, `learn`, and `to-tickets` in each host's active discovery surface.
- Retained upstream MIT notices and PR visual attribution.

Dry-runs showed six additions, three expected replacements, and no removals. Native installation succeeded on both hosts with recoverable backups. Backup identifiers: Codex `20261006T060242.076322Z`; Anti-Gravity `20261006T060333.981115Z`, under each host's `.antigravity-backups/` directory. Ownership records remain in the standard managed namespace.

## Checks and actual evidence

| Check | Observed result | What it establishes |
| --- | --- | --- |
| Canonical validation | Zero issues | Frontmatter, registry, links, and portable source consistency |
| Focused packaging tests | 4 passed | General-profile packages include all files; Codex invocation metadata survives build; temporary native installs preserve unrelated skills/settings |
| Full repository suite | 203 tests passed | Repository build, validation, routing-fixture, and installer regressions covered by that suite |
| PowerShell installer parse | Passed | Existing Windows installer remains syntactically valid |
| Git diff whitespace check | Passed | No diff whitespace errors |
| Independent source assurance | No blocking finding; omitted review prompts restored | Source-level challenge of dependencies, invocation, authority, isolation, and integration rules |
| Native package comparison | 24 files per host matched source byte-for-byte | Both actual discovery locations contain all six complete source packages |
| Native payload comparison | All 82 Codex and 93 Anti-Gravity managed targets matched payload digests | Installed managed content matches generated output |
| Anti-Gravity recorded digests | All 93 matched | Active ownership record agrees with actual installed content |

The Codex ownership record lists managed targets but does not store per-target digests; its 82 digest comparisons were computed against the generated payload. Both hosts' updated router and compatibility skill entrypoints matched canonical source exactly.

The [20 behavior scenarios](engineering-skills-scenarios.md) specify positive triggers, negative routes, and failure/approval cases for source-level review. They are not a recorded run of a real application spec. No live end-to-end multi-ticket implementation or retrospective has been exercised through these newly installed skills. Source assurance, static routing fixtures, and packaging tests do not prove universal instruction compliance or application release readiness.

## Use the skills

Start a new Codex chat so global routing and skill discovery reload. In Codex, mention the skill with `$skill-name` or use the natural-language request; do not depend on another host's slash-command syntax.

```text
Use $retro to review this coding session and suggest what would prevent its failures.

Use $implement-spec to implement the approved spec at [path] and tickets at [path].

Use $pr to draft the PR body from this final diff and the checks we ran.

Use $tdd to build this approved behavior through its established public interface.

Use $code-review to review this branch and its uncommitted changes against [spec path].

Use $writing-for-agents to improve these authorized agent-facing instructions.
```

`retro` and `implement-spec` are explicitly user-invoked. `retro` recommends improvements before mutation; `implement-spec` accepts supplied local specs/tickets and falls back to sequential execution when appropriate. Existing project tracker configuration replaces the upstream setup command. Remote ticket changes, PR publication/readiness, default-branch merge, and deployment retain their separate authorization boundaries.

Use `learn` for broader after-action learning and cross-project capability promotion. Use the existing architecture and testing routes for technical boundary or evidence decisions instead of importing the upstream library wholesale.
