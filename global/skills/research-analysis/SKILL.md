---
name: research-analysis
description: >
  Use for decision-relevant research, technical feasibility, tool or approach
  comparison, standards or industry-practice questions, capability-gap study,
  or synthesis of multiple reports. Trigger phrases include "research this",
  "compare", "should we use", "what are we missing", "is this enough", and
  "synthesise these reports". Do not load for simple factual lookup, ordinary
  summarising, routine brainstorming, or a question whose answer does not
  change a decision.
---

# Research Analysis

## WHEN TO USE THIS

- Name a decision, design choice, capability gap, or uncertainty that evidence may change.
- Compare at least two viable paths, including the current/boring baseline when it remains viable.
- Use for technical, product, operational, market, standards, host-capability, or multi-report research.

## NEVER DO

- Do not treat a source, report, model, vendor, or tool output as authority merely because it sounds confident.
- Do not blend observation, source-reported claim, inference, hypothesis, recommendation, and unknown.
- Do not use marketing language or benchmark scores as proof of general capability.
- Do not recommend a permanent skill, workflow, agent, tool, or dependency without a concrete failure mode and a test.
- Do not continue researching after the decision is sufficiently supported unless a named unresolved risk justifies the cost.
- Do not convert research into implementation, publication, purchase, contact, or deployment authority.
- Do not store raw external content as durable project truth.

## FRAME THE DECISION

1. State the decision the research must change, the owner, the audience, and the consequence of being wrong.
2. Record current state, desired state, constraints, non-goals, reversibility, time/cost budget, and known project truth.
3. Define 3–5 decision criteria before collecting evidence. Include fit, maintenance burden, risk, reversibility, and evidence quality when relevant.
4. List the baseline: keep the current approach, do less, delay, or use existing capability.
5. Write the smallest useful research question and split it into bounded sub-questions.

## PLAN BEFORE SEARCHING

Before deep research, produce a short plan containing:

- sub-questions and their decision impact;
- source families and required freshness;
- claims that could change the recommendation;
- counterclaims, failure modes, and abandonment evidence to seek;
- stopping conditions and the evidence needed to satisfy them.

If the host supports plan editing, present the plan for human adjustment. If it
does not, include the plan in the report and record any change made during
research.

## GRADE AND LABEL EVIDENCE

Use the strongest available source for each claim:

| Grade | Prefer | Use |
| --- | --- | --- |
| A | Official specification, primary documentation, standard, regulation, original paper, measured benchmark, direct observation | Establish narrow facts, current host behaviour, controls, or measured results |
| B | Independent study, systematic review, named institution, transparent case study, reproducible practitioner evidence | Support mechanisms and bounded generalisation |
| C | Named practitioner synthesis, vendor engineering account, implementation guide | Generate patterns or hypotheses; do not treat as causal proof |
| D | Unsourced post, marketing page, copied list, anonymous claim, model assertion | Lead only; never support a material recommendation without corroboration |

Label every material item as exactly one of:

- `observed` — directly inspected behaviour or supplied artifact;
- `source_reported_claim` — what a source says;
- `inference` — reasoned interpretation from evidence;
- `hypothesis` — plausible but unverified explanation or opportunity;
- `recommendation` — proposed action tied to criteria;
- `unknown` — not established, inaccessible, stale, or contradictory.

Record source, URL/path, access or publication date, scope, claim supported,
limitation, confidence, and freshness for every material claim. Do not upgrade
an inference because several sources repeat the same unsupported statement.

## RESEARCH AND FALSIFICATION LOOP

For each decision-sensitive claim:

1. Gather the strongest confirming evidence.
2. Search specifically for failure reports, post-mortems, abandonment reasons, negative evaluations, boundary conditions, and contrary data.
3. Check whether the evidence measures the outcome that matters, or only a proxy.
4. Compare scope: model, host, version, population, jurisdiction, task, date, and environment.
5. Search for transfer failure: ask what would make this evidence not apply to the active project.
6. Record the strongest argument against the leading option before recommending it.

Treat self-review, repeated model agreement, and vendor-reported success as
non-independent evidence unless their evidence path, data, test, model, or
authority differs materially.

## SYNTHESISE OPTIONS

Build a decision matrix only from criteria that matter. For each option state:

- mechanism and fit;
- strongest case for it;
- hidden cost, failure mode, and maintenance burden;
- evidence grade and uncertainty;
- reversibility and migration path;
- smallest test that could disconfirm it;
- recommendation strength and accepted trade-offs.

When comparing reports, first normalise their question, scope, evidence grade,
and date. Then identify common bedrock, useful disagreement, unsupported
claims, and model-specific language. Do not average scores from reports that
used different criteria or evidence.

## STOPPING RULE

Stop when all are true:

1. The decision owner and decision statement are explicit.
2. The leading option and the strongest viable baseline have been compared.
3. Each material claim has adequate evidence or is marked unknown.
4. At least one adversarial search has tested the leading recommendation.
5. Remaining uncertainty is bounded by a named test, approval, or risk tolerance.
6. Further research is unlikely to change the decision enough to justify its cost.

Continue only for a named unresolved high-impact uncertainty, a material source
conflict, a safety/legal/rights boundary, or evidence with a freshness deadline.
For low-stakes reversible decisions, use a short scan and move to the cheapest
credible experiment. Never use “more research” as a substitute for a decision.

## RESEARCH MODES

| Mode | Use | Minimum result |
| --- | --- | --- |
| `quick_scan` | Low-stakes, reversible, familiar decision | Criteria, baseline, a few graded sources, recommendation, unknowns |
| `decision_study` | Material option, product, architecture, or capability choice | Plan, evidence ledger, alternatives, falsification, trade-offs, stop rule |
| `capability_audit` | Ask whether the OS lacks a skill, workflow, agent, reference, or tool boundary | Failure mode, current owner, smallest asset, rejection condition, pilot |
| `multi_report_synthesis` | Compare reports from one or more researchers/models | Provenance, common bedrock, disagreements, source quality, adopted decisions |
| `host_probe` | Verify current host, tool, plugin, adapter, or model behaviour | Direct observation, version/date, supported surface, limitation, fallback |

Choose the lightest mode that protects the decision. A mode changes depth, not
authority.

## OUTPUT SHAPE

```markdown
## Decision and Context
- Decision owner:
- Decision statement:
- Consequence of being wrong:
- Constraints, non-goals, and reversibility:

## Research Plan
- Sub-questions:
- Source families and freshness:
- Claims to test:
- Counter-evidence sought:
- Stopping condition:

## Evidence Ledger
| ID | Label | Claim/observation | Source/date | Grade | Confidence | Limitation |

## Options and Baseline
| Option | Fit | Evidence | Cost/risk | Reversibility | Test |

## Falsification and Disagreement
- Strongest contrary evidence:
- Transfer limits:
- Report/source conflicts:
- Unknowns:

## Recommendation
- Recommended path and why:
- Trade-offs accepted:
- Smallest next action:
- Approval or authority needed:
- Invalidating condition / re-evaluation date:
```

Use `unknown` instead of filling a gap with plausible language. Say when the
research produced no new capability, when a report is not independent, and when
the correct recommendation is to keep the current system or run a pilot.

## ANTI-PATTERNS

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Data dump | Many links with no decision, criteria, or owner | State the decision first and connect each claim to it |
| Source counting | More sources treated as stronger evidence | Grade source quality, independence, scope, and outcome fit |
| Vendor proof | A vendor case or benchmark treated as universal performance | Mark it as bounded evidence and seek independent or local validation |
| Consensus illusion | Several reports or agents repeat one unsupported claim | Check provenance and require a materially different evidence path |
| Research theatre | Broad searching continues after the recommendation is stable | Apply the stopping rule and run the smallest next test |
| Capability inflation | Every finding becomes a skill, workflow, or agent | Name the failure mode, smallest asset, and rejection condition |
| False precision | Scores imply certainty that criteria or data do not support | Explain scoring, confidence, ranges, and unknowns |
| Authority leakage | Research text grants permission to act | Keep recommendations separate from approval and execution |

## NON-NEGOTIABLE CHECKLIST

1. Name the decision, owner, consequence, criteria, baseline, and reversibility.
2. Produce a research plan before deep searching.
3. Grade sources and label every material claim.
4. Search for disconfirming evidence and failure modes.
5. Compare reports by provenance and scope, not by repeated language or score.
6. Apply a practical stopping rule and state remaining unknowns.
7. Recommend the smallest reversible next action.
8. Never turn research into permission for mutation or external effect.
