# Debugging resource index

| Resource | Read when | Decision it changes |
| --- | --- | --- |
| [Evidence and hypotheses](evidence-and-hypotheses.md) | Several theories, incomplete reproduction, or a comparison/bisection decision. | What evidence can safely change the causal ranking. |
| [Fault-class map](fault-class-map.md) | A likely fault class has emerged. | Which first checks distinguish the class without anchoring. |
| [Incident and repair boundaries](incident-and-repair-boundaries.md) | Proposing/applying a repair, handling data/security risk, or mitigating impact. | Whether the work must remain read-only, escalate, or use an approval gate. |
| [Behavior scenarios](../evals/debugging-scenarios.md) | Revising or evaluating the skill. | Whether the skill improves action quality rather than only sounding detailed. |

## Source snapshot

This package was revised on 2026-08-18 from the supplied Manus and Grok research reports. Manus is the primary synthesis because it distinguishes empirical support, practitioner guidance, limitations, uncertainty, and authority boundaries. Grok contributes the useful known-good/failing differential slice and adversarial evaluation ideas, but its unsupported statistics and noisy bibliography are not encoded as operating rules.

Durable external references verified on 2026-08-18:

- [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) for the complementary role of traces, metrics, and logs.
- [Google SRE incident management](https://sre.google/sre-book/managing-incidents/) for separating stabilization from later causal analysis.
- [Git bisect documentation](https://git-scm.com/docs/git-bisect) for the mechanics and oracle dependence of good/bad change-point search.

These links inform the method; they do not grant production access, prescribe a particular toolchain, or replace project-specific incident procedures.
