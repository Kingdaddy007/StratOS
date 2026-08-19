# API Contract Source Index

Use these sources to verify current protocol or provider facts before relying on
an implementation detail. This index was checked on 2026-08-19; it does not
turn a source into a universal architecture rule.

| Source | Use when | Verification note |
| --- | --- | --- |
| [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) | Choosing HTTP methods, status, conditional requests, or representation semantics. | Standards-track protocol reference. |
| [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | Designing or validating an OpenAPI description, generated client, or contract artifact. | Description/tooling format; compare with actual runtime and consumers. |
| [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | Reviewing object/property/function authorization, resource consumption, or sensitive business flow risk. | Security-risk taxonomy; use `security` for a full threat model. |
| [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) | Studying one provider's idempotency implementation. | Provider example, not a universal header or retention policy. |

Load [extended-guidance.md](extended-guidance.md) for operating guidance; load an
external source only when its current behavior changes the decision.
