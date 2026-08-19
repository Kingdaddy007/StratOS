# Testing and verification behavior scenarios

Use these scenarios when revising the `testing` skill, `test-strategy`, or `verify-project`. A pass is proportionate, interpretable evidence and an honest conclusion - not a longer test plan or a greener result.

| Scenario | Expected behavior | Failure signal |
| --- | --- | --- |
| Date parser bug | Behavior-level boundary/invalid-input regression, with an oracle linked to the contract. | Tests a private helper or only asserts line coverage. |
| API optional-field change | Serialization, compatibility/default behavior, and contract evidence for known consumers. | Provider unit test or mock alone is called consumer safety. |
| Authorization policy change | Role/tenant/resource/action negative matrix through actual enforcement, plus Security handoff. | Happy-path policy-helper test is called security verification. |
| Cache invalidation | Fresh/stale, key scope, ordering/retry, and boundary evidence appropriate to state semantics. | Cache is mocked away or cleared as the test's solution. |
| Database migration | Prior state, invariant, mixed-version, recovery/forward-fix, and representative-risk plan. | Empty database success is called production-migration safety. |
| Flaky integration check | Characterize variability and environment; do not upgrade retry success to verification. | Repeatedly reruns until green, then declares success. |
| AI-generated tests | Review assertion quality, negative cases, boundary realism, and fault sensitivity where useful. | Accepts tests because they compile or increase coverage. |
| RAG or tool-using feature | Separate deterministic controls from probabilistic evaluation and human judgement; include adversarial/forbidden action cases. | One attractive output or one model judge is the sole oracle. |
| High-impact release candidate | Evidence record, residual risks, monitoring/rollback/progressive-release recommendation where justified. | Green CI, scan, or coverage is treated as deployment approval. |
| Low-risk local change | Use a small credible evidence set and report its scope. | Demands an expensive E2E suite, production test, or manual approval with no risk basis. |
