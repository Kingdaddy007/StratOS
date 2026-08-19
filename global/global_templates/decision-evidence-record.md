# Decision and Evidence Record

Use this record when a product, design, architecture, engineering, assurance,
research, or growth decision is material enough to need traceable reasoning.
Do not use it for ordinary drafting, a tiny reversible edit, or to grant
permission for an external effect.

## Decision

- **Record ID:** [unique task or decision ID]
- **Status:** `draft` | `proposed` | `accepted` | `rejected` | `superseded`
- **Decision owner:** [person or accountable agent]
- **Decision statement:** [one sentence]
- **Consequence of being wrong:** [impact and affected parties]
- **Current state:** [verified starting facts]
- **Desired state:** [what should change]
- **Constraints and non-goals:** [limits and exclusions]
- **Reversibility:** [easy / bounded / hard / irreversible, with reason]
- **Decision criteria:** [three to five criteria]
- **Baseline:** [keep current approach, do less, delay, or existing capability]

## Evidence ledger

Label each entry exactly as `observed`, `source_reported_claim`, `inference`,
`hypothesis`, `recommendation`, or `unknown`.

| ID | Label | Statement or observation | Source/path and date | Grade | Confidence | Limitation or conflict |
| --- | --- | --- | --- | --- | --- | --- |
| E-01 | observed | [fill] | [fill] | A/B/C/D | high/medium/low | [fill] |

Source grades:

- **A:** official or primary evidence, standard, original study, measured result, or direct observation;
- **B:** independent study, review, named institution, or transparent case evidence;
- **C:** named practitioner or vendor synthesis used for patterns and hypotheses;
- **D:** unsourced or marketing material used only as a lead.

## Options and trade-offs

| Option | Fit to criteria | Strongest case | Cost or failure mode | Reversibility | Smallest disconfirming test |
| --- | --- | --- | --- | --- | --- |
| Baseline | [fill] | [fill] | [fill] | [fill] | [fill] |
| Option A | [fill] | [fill] | [fill] | [fill] | [fill] |

## Falsification and uncertainty

- **Strongest contrary evidence:** [what argues against the leading path]
- **Transfer limits:** [why supplied evidence may not apply here]
- **Unresolved conflicts:** [sources, agents, requirements, or observations]
- **Unknowns:** [facts not established]
- **Stopping condition:** [what is enough evidence to decide]
- **Invalidating condition:** [what would reopen or reverse the decision]

## Decision and handoff

- **Recommendation:** [smallest next action]
- **Trade-offs accepted:** [what this choice gives up]
- **Evidence still required:** [tests, pilot, review, or source check]
- **Approval required:** [none / exact human approval and timing]
- **Next owner:** [person, lead, or workflow]
- **Review date or trigger:** [when to revisit]

## Integrity rules

- Keep project facts separate from global policy.
- Preserve source paths, dates, and limitations; do not paste raw external content as truth.
- Record a superseding record instead of silently rewriting an accepted decision.
- A recommendation does not authorise implementation, deletion, publication, deployment, messaging, spending, or another external effect.
