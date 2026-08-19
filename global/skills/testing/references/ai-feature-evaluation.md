# AI-feature evaluation

Load this reference only when a change affects model behavior, prompts, retrieval, model/tool routing, evaluators, safety boundaries, cost, latency, or an agent's actions.

## Separate the claim types

AI-enabled products normally need three complementary evidence classes:

| Claim type | Examples | Suitable evidence |
| --- | --- | --- |
| Deterministic system guarantee | schema validation, authorization, tool argument validation, durable state, token/cost limit, no secret exposure | code-level invariants, contract/integration tests, negative permission cases, logs/traces. |
| Probabilistic product behavior | groundedness, relevance, refusal quality, tool selection, task completion, prompt sensitivity | versioned representative evaluation set, adversarial/negative/out-of-scope cases, repeated runs, trace/result review. |
| Human or domain judgement | high-consequence semantics, safety, usefulness, fairness, ambiguous quality tradeoff | named human/domain review with a clear decision rubric and escalation boundary. |

Do not let a model grade its own high-impact behavior as the sole oracle. Automated judges can be one signal; use independent checks, execution-grounded evidence, and human review when consequence or uncertainty warrants it.

## Evaluation record

For an AI feature, record model/prompt/retrieval/tool/evaluator versions, representative task source, positive and negative cases, expected behavior or rubric, run conditions, repeated-run variability, cost/latency observation, tool/action traces, and what the data does not represent.

Include failure cases appropriate to the product: unsupported or missing-context answers, unsafe refusal, prompt injection, data leakage, bad tool arguments, unauthorized actions, timeout/cost growth, and unsafe side effects. Evaluation is not a fixed leaderboard, prompt count, judge score, or success threshold.

## Release boundary

Changes involving production model behavior, autonomous tool effects, sensitive data, or hard-to-reverse outcomes may need project-specific progressive release evidence and a human owner. This reference does not authorize access to real users, production prompts, external tools, or paid model calls.
