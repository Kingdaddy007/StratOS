---
name: seedance-interview-short
description: 'Use when the task requires seedance interview short guidance. A guided creative journey to craft a production-ready prompt under the hard 2000-character limit. Follow the "Director\\''s Journey" workflow: Vision → Narrative → Visuals → Technical → Final Compressed Brief.'
license: MIT
---
## STATUS VERIFICATION GATE

Treat platform availability, model limits, filter behavior, enforcement actions, and API status dated February-March 2026 as historical snapshots. Before relying on them, verify current official ByteDance/Seedance documentation. If verification is unavailable, label the claim unverified and avoid presenting it as current fact.

# seedance-interview-short (v5.0)

This skill transforms a simple idea into a professional, **sub-2000-character** Seedance 2.0 production brief, with a target of **30-100 words**.

## The Workflow

1.  **The Vision & Genre**: Ask for a 1-sentence concept and a genre from [ref:genre-guides].
2.  **Reference Media**: Ask if the user has any `@Image`, `@Video`, or `@Audio` references.
3.  **"Quick Mode" Exit**: If the user has strong references, offer to switch to the [skill:seedance-prompt] skill to build a prompt directly.
4.  **Narrative Core**: If needed, ask 1-2 questions to find the emotional anchor.
5.  **Build & Compress**: Construct the prompt using the Director's Formula, keeping a live character count.

## The Interviewer's Craft

-   Prioritize action verbs and physics over descriptive adjectives.
-   Explain that shorter, denser prompts perform better.
-   Use the character budget as a creative constraint, not just a technical one.

### Final Output Format

```
**Final Prompt (185/2000 chars):**

[PROMPT TEXT]

---

**Director's Notes:**
- **Genre:** [User's chosen genre]
- **Core Intent:** [Summary of emotional goal]
- **References:** [@Image1, @Video1]
```
