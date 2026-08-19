---
name: seedance-pipeline
description: Plan or review a verified Seedance production pipeline that may include a provider-supported integration and local finishing. Use for a deliberate automation decision or post-production handoff; do not use to invent API contracts, run unverified integrations, or publish media.
license: MIT
---

# Seedance Pipeline

## WHEN TO USE THIS

- The user needs to choose between manual generation, a documented provider integration, and local finishing for a real production task.
- The work depends on current model, regional surface, asset, metadata, export, or handoff constraints.
- The user supplies current provider documentation or asks for a source-backed feasibility assessment.

## NEVER DO

- Never present an old endpoint, model identifier, quota, file limit, node graph, or response lifecycle as a usable current contract without current official evidence.
- Never place credentials in a prompt, source file, generated configuration, or command example.
- Never assume a ComfyUI node, post-production tool, codec, resolution, or metadata-cleanup requirement is available or appropriate.
- Never execute an integration, upload assets, spend credits, or distribute media without explicit approval for that external effect.

## PLAN A VERIFIED PIPELINE

1. Record the target provider, model label, region/surface, input assets, desired output, ownership rights, budget, and delivery target.
2. Select the smallest viable route: prompt-only planning; user-operated manual generation; documented provider integration; or local-only finishing of an already-held file.
3. For any automation, verify the official model/API documentation, authentication method, supported inputs, asynchronous lifecycle, quotas, error handling, and current cost. Mark every missing item unverified.
4. Keep credentials in the user's approved secret mechanism. Design idempotency, bounded retries, artifact naming, and failure reporting before any execution.
5. For local finishing, propose a reversible export/grade/audio/metadata review plan that matches the delivery target; do not prescribe a tool or format until project constraints are known.
6. Stop for approval immediately before provider calls, uploads, paid generation, destructive metadata changes, publication, or delivery.

## OUTPUT SHAPE

Return: verified capability record; chosen route and rejected alternatives; local versus external boundary; required approvals; failure/retry plan; and delivery checks. Include executable commands only when they are derived from current verified documentation and the user authorized implementation.

## NON-NEGOTIABLE CHECKLIST

1. Separate a production plan from an executed integration.
2. Treat provider contracts and costs as volatile.
3. Keep secrets out of artifacts and prompts.
4. Record evidence before proposing external execution.
