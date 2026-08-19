---
name: seedance-filter
description: Diagnose a blocked or refused Seedance request while preserving platform, safety, likeness, and intellectual-property boundaries. Use only when the user needs a policy-compliant alternative or an evidence-based explanation of an observed refusal; do not use to bypass a provider safeguard.
license: MIT
---

# Seedance Refusal and Policy Diagnosis

## WHEN TO USE THIS

- The user reports that Seedance rejected, blocked, or materially altered a prompt and needs a safe next step.
- A prompt may involve a real person, protected material, sensitive content, or an unclear provider-policy boundary.
- The task is to make a lawful, truthful creative brief clearer without concealing what it asks the provider to generate.

## NEVER DO

- Never devise a workaround, translation, euphemism, image-selection tactic, or repeated retry plan intended to evade a safeguard.
- Never advise disguising a person, age, weapon, protected work, sexual content, violence, or other material to change how a platform classifies it.
- Never claim to know a provider's hidden filter logic, rejection rate, or current policy without a dated primary source.
- Never upload an asset, submit a generation, spend credits, or publish a result without the required approval.

## DIAGNOSE THE OBSERVED OUTCOME

1. Record the visible refusal text, selected provider/model, active surface, region if known, and the intended creative outcome. Do not infer a hidden reason from one refusal.
2. Separate a technical error from a safety, rights, likeness, or policy concern. Route technical failures to `seedance-troubleshoot`; route rights and likeness review to `seedance-copyright`.
3. If the requested outcome is prohibited or would require concealment, stop. Say that this skill cannot help bypass the restriction.
4. If a legitimate alternative exists, express it plainly: use original or licensed assets, fictional/non-identifiable subjects where appropriate, an age-appropriate scenario, or a different non-sensitive creative treatment. Do not preserve the restricted intent under different wording.
5. If the cause is unclear, request the current provider guidance or record the cause as unverified. Do not turn guesswork into a retry strategy.

## REFERENCE LOADING RULES

- Do not load `references/extended-guidance.md` as runtime filter guidance. It is quarantined historical material awaiting a later Media Pack review.
- Load the current official provider policy only when the user asks for a policy-dependent decision; record its URL and verification date.

## OUTPUT SHAPE

Return: observed evidence; what is known versus unverified; the relevant owner or route; a plainly stated compliant alternative if one exists; and the approval needed before any external generation.

## NON-NEGOTIABLE CHECKLIST

1. Preserve the actual request rather than disguising it.
2. Do not infer hidden platform behavior from a single result.
3. Stop rather than bypass when a safety, rights, or likeness boundary applies.
4. Mark volatile provider claims unverified without a current primary source.
