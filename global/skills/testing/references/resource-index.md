# Testing and verification resource index

| Resource | Read when | Decision it changes |
| --- | --- | --- |
| [Evidence selection](evidence-selection.md) | Planning non-trivial test/verification evidence or selecting a test level. | What evidence is credible for the actual risk and boundary. |
| [Oracles and stability](oracles-and-stability.md) | Designing assertions, reviewing mocks/coverage, adding a regression, or classifying flakiness. | Whether the evidence could actually distinguish correct from plausible-wrong behavior. |
| [AI-feature evaluation](ai-feature-evaluation.md) | A model, prompt, retrieval, tool, evaluator, cost, latency, or agent behavior changes. | Which deterministic, probabilistic, and human evidence is needed. |
| [Release evidence](release-evidence.md) | Interpreting a verification run or preparing a release recommendation. | The exact status, residual uncertainty, and progressive-release handoff. |
| [Behavior scenarios](../evals/testing-scenarios.md) | Revising or evaluating this package. | Whether the guidance reduces false confidence without mandating excessive tests. |

## Source snapshot

This package was revised on 2026-08-18 from the supplied Manus, Grok, and Gemini reports. Manus is the primary synthesis: it distinguishes evidence strength, durable method, project-specific adapter detail, authority, and uncertainty. Grok contributes useful change-class and adversarial fixtures. Gemini contributes the compatible distinction between deterministic checks, probabilistic AI evaluation, and human review, but is architecture context only; its fixed evaluation counts, blanket CI blockers, and secondary-source claims are not encoded.

Durable external references verified on 2026-08-18:

- [Google SRE canarying releases](https://sre.google/workbook/canarying-releases/) for partial, time-limited rollout evaluation and the need for attributable signals.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) for security-control verification as a specialist concern.
- [NIST SSDF](https://csrc.nist.gov/projects/ssdf) for risk-, cost-, feasibility-, and applicability-sensitive secure development.
- [Microsoft's consumer-driven contract testing guidance](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/cdc-testing/) for contract tests as one complement to integration evidence.

These sources inform evidence selection; they do not prescribe a test framework, thresholds, commands, release approval, or access to production systems.
