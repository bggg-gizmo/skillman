# Codeman Tester — specialist playbooks

Use this reference when the request involves verification and failure prevention. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** unit testing, integration testing, regression testing, property-based testing.

## Unit testing

1. Derive cases from actual public contracts and internal branch logic without merely mirroring the implementation.
2. Cover ordinary, boundary, invalid, cancellation/error, and state-transition behavior with deterministic fixtures.
3. Use mocks/fakes only at relevant external boundaries; ensure tests still assert real behavior and preserve types/semantics.
4. Avoid altering production interfaces merely to make tests pass; add test seams only when architecture warrants them.
5. Execute the intended test runner and report counts, failures, skips, and the exact commands used.

## Integration testing

1. Identify components, service dependencies, schemas, event contracts, authentication, storage, and necessary environmental fixtures.
2. Cover full input/output across real module or service boundaries, including failure, retries, idempotence, and timeouts.
3. Isolate test state via dedicated databases/containers/temp directories and clean up without touching user data.
4. Distinguish local stand-ins from real external-service verification; do not claim production parity without evidence.
5. Capture migrations and version compatibility when interfaces cross component boundaries.

## Regression testing

1. Inventory each preserved function and feature, including UI routes, CLI options, API schemas, error behavior, and background tasks.
2. Build a traceability map from requested change and risk area to test cases; characterize ambiguous legacy behavior before editing.
3. Add focused reproduction tests for fixed bugs and tests for unchanged behavior impacted by the diff.
4. Compare baseline and post-change outputs and evaluate the complete existing test suite where feasible.
5. Report untested paths explicitly; never equate compilation or green unit tests alone with absence of regressions.

## Property-based testing

1. Define algebraic, round-trip, idempotence, order, boundary, security, and parser invariants derived from specifications.
2. Generate inputs across legitimate and malformed domains with intentional distributions and bounded sizes.
3. Keep random seeds reproducible and capture minimized failing examples for regression tests.
4. Check oracle validity, shrinking behavior, false assumptions, and interaction with nondeterminism or time.
5. Record property name, seed, generated case, shrink result, failing invariant, and implemented fix where applicable.

## Test evidence and coverage

1. Match tool selection to the repository: pytest/unittest, Jest/Vitest, Go test, cargo test, Pester, CTest, or existing supported runners.
2. Use coverage to find unexercised risk but do not treat percentage targets as proof of correctness.
3. Run targeted checks first and the relevant full suite when possible; keep failures visible and do not delete assertions to get green.
4. List exact command, environment, pass/fail/skip result, and whether results are from current edited state.

