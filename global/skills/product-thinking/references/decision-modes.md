# Decision Modes

Use this reference when deciding how much product process is justified. It is a sizing aid, not a release process or authority grant.

## Direct change

Use when the requested outcome is clear, the change is low-consequence and reversible, and an acceptance check exists.

```markdown
Decision: [what will change]
Intent: [user or business outcome]
Material assumption: [only if one matters]
Check: [smallest acceptance or review check]
```

Example: update approved website copy with supplied text; preview the affected page and check links. Do not launch discovery or define analytics merely because the change appears on a product surface.

## Product decision

Use when the problem, value, scope, priority, or evidence is uncertain enough to change the work. Use the Product Decision Record in [extended-guidance.md](extended-guidance.md#product-decision-record). Keep it concise unless a real escalation trigger applies.

Common triggers include unclear problem framing, conflicting evidence, meaningful opportunity cost, repeated workflow impact, new operational burden, or a change that alters user behaviour rather than presentation alone.

## High-stakes decision

Use when a wrong choice could create material safety, privacy, security, financial, legal, reputational, access, third-party, lock-in, or public-commitment harm—or when rollback is difficult.

Expand the product decision record with the specific risks and relevant specialist review. Do not infer authority to expose, deploy, publish, collect data, or perform external actions. Record the gate and stop before the action that requires approval.
