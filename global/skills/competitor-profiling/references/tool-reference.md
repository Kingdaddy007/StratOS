# Capability-First Collection and Tool Routing

Load this reference when deciding how to collect or preserve competitor evidence. Tool names, access, and limits vary by host. Discover capabilities at runtime; never assume a provider, API, credential, or MCP server is installed.

## Capability Matrix

| Need | Adequate capability | Capture and limit |
| --- | --- | --- |
| Read public page text | Read-only page fetch or browser observation | URL, title, access date, visible scope, and blocked sections. |
| Observe visual/interactive experience | Browser screenshot, recording, or user-provided media | Viewport/device, timestamp, interaction path, and interpretation limits. |
| Discover relevant public pages | Search or public site navigation | Query, result date, source URL, and no claim that rank proves quality. |
| Extract structured fields | Schema-aware parser or manual evidence table | Preserve source span, field definition, missing value, and parser limitations. |
| Compare repeated snapshots | Local diff or structured comparison | Date each snapshot; do not overwrite prior evidence without authorization. |
| Collect public review/research evidence | Permitted public source or supplied document | Source identity, sample/method, date, permissions, and quote limits. |
| Preserve provenance | Workspace artifact or claim ledger | Write only when the task and workspace permit it; minimise personal data. |

## Safe Fallback Order

1. Use the supplied URL or artifact and the least intrusive available read-only capability.
2. Try an allowed public alternative such as a canonical page, public document, search result, screenshot, or user-provided capture.
3. Record the access failure and the claim as unknown when the evidence remains unavailable.

Never work around authentication, payment, CAPTCHA, technical blocks, contractual restrictions, or explicit automated-collection restrictions. Do not infer permission from visibility. If an external action, unusual-volume collection, paid source, or personal-data use is needed, stop for approval.

## Capture Record

For every non-trivial collection run, record:

- capability used and access condition;
- URL or artifact, source title/type, access date, publication/update date;
- scope, viewport/device, query or interaction path, extraction method;
- rate, volume, and personal-data limits;
- failed sources and fallbacks; and
- claim IDs produced from the capture.

## Do Not Promise Provider Metrics

Traffic estimates, domain authority, backlink counts, keyword counts, review scores, funding, team size, and founding dates are provider- or source-dependent. Use them only with source, date, definition, population, and limitations. When unavailable or non-comparable, report `unknown`.
