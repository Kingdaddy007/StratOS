# Common Requests

Use plain language. These examples show the intent and safety mode Anti-Gravity should infer.

| Goal | Example request | Expected route |
| --- | --- | --- |
| Diagnose | “Diagnose the failing login test. Do not edit files.” | `diagnose` → debugging; read-only |
| Implement | “Implement the validated login fix and run the focused tests.” | `implement` → build/debug/test; local edit |
| New SaaS | “Help me start a general SaaS project. Ask for missing requirements before coding.” | general project inception |
| General UI | “Design the dashboard UX for a finance app.” | general UI design; no spatial profile |
| Spatial portfolio | “Plan a cinematic interior designer portfolio with a scroll narrative.” | Spatial project workflow for full coordination; direct Spatial skills for a focused concept, story, reference, UI, or motion task |
| Google video | “Draft a 10-second product reveal for Google Flow using the current Veo model in my account.” | video generation; inspect the current Flow model list |
| Seedance video | “Create a Seedance 2.0 multi-shot prompt with character continuity.” | video generation → Seedance references |
| Deploy | “Deploy the approved build to production.” | ship-to-production; just-in-time approval required |
| Security audit | “Audit this repository for auth and secret-handling risks; do not change code.” | security audit; read-only |

For video work, name the platform and model when you know them. Flow is the Google interface; Veo and Gemini Omni are model families available through Google surfaces. Seedance is a separate provider. If a model label is ambiguous, the workflow records the exact label shown in the active UI instead of guessing.
