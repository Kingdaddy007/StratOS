# Oracles, regression protection, and stable evidence

Load this reference when designing or reviewing assertions, deciding what to mock, interpreting coverage, choosing property/mutation checks, or handling a flaky result.

## Credible oracle

An oracle says how a test distinguishes correct from wrong behavior. Prefer observable behavior, a contract, or an invariant:

```text
Given [state/input], when [action], then [observable result/invariant], because [risk or contract].
```

For negative cases, also name the forbidden result: unauthorized access, duplicate side effect, corrupted data, stale read, silent fallback, unsupported claim, or unsafe tool action.

Avoid asserting call order, private fields, or a particular algorithm unless it is itself a public contract. A snapshot needs a stated semantic purpose; otherwise it is a change detector, not a correctness oracle.

## Mocks and boundary realism

Mocks and fakes are useful to isolate local control flow, inject failures, or make a test deterministic. They prove the modeled collaborator behavior, not the real collaborator. Pair them with a real, contract-verified, or production-compatible boundary check when the material risk is serialization, persistence, authorization, provider behavior, queuing, or cache semantics.

Do not adopt either extreme as a rule: not every external service must be mocked, and not every test should call a real one. State which substitute is used, why it is credible for the claimed behavior, and what it cannot prove.

## Regression and fault sensitivity

For a diagnosed defect, add the narrowest durable regression defense that exercises the intended mechanism or contract. When feasible, demonstrate that it fails against the original behavior and passes against the repair. A lack of such a demonstration is a limit to record, not a reason to invent evidence.

Use property, metamorphic, mutation, or fault-seeding checks selectively when the risk is subtle, the behavior is invariant-rich, or ordinary assertions may be tautological. These methods reveal a different kind of weakness; they are not universal score gates and cannot replace domain judgement.

## Flakiness and nondeterminism

A check that both passes and fails without a relevant code change is degraded evidence. Do not retry until it happens to pass and report success. Instead record:

- observed variability, attempted seed/rerun/isolation conditions, and frequency if known;
- potential uncontrolled time, randomness, network, load, order, shared state, or environment differences;
- whether the result is a product failure, harness/infrastructure failure, or presently unclassified;
- the safe next action, owner, and whether a release claim must remain `unverified` or `blocked`.

Some AI systems and distributed systems are inherently variable. Characterize the variability with the appropriate evaluation or operational evidence rather than promising determinism the system cannot supply.

## Coverage interpretation

Coverage can expose unexecuted areas and trends, but it cannot establish assertion strength, boundary reach, failure-mode coverage, or product correctness. Report it only alongside the claim exercised, test quality, and material blind spots. Never convert a coverage percentage into a standalone release gate.
