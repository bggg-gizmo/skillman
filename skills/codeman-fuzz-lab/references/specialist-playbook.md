# Codeman Fuzz Lab — specialist execution playbook

## Preconditions

Use for local fuzz testing, parser hardening, seed corpus construction, crash minimization, and reliability testing within authorized boundaries.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Define safe target and objective

1. Identify target binary or library, accepted inputs, security boundaries, authorized environment, memory/time budgets, and prohibited destructive side effects.
2. Prefer local test builds and isolated targets; avoid scanning networks or third-party services absent explicit scope and permission.
3. Select correctness or memory-safety invariants, available sanitizers, and baseline regression tests.
## Phase 2: Build a production-relevant harness

1. Call real input-processing entry points with bounded input sizes and deterministic setup/teardown; avoid mocking away the parser under test.
2. Reset global state between iterations, constrain filesystem/network effects, and prevent persistent shared-resource corruption.
3. Treat expected parse rejection as normal; preserve crashes, assertion failures, memory errors, and contract violations as actionable outcomes.
## Phase 3: Seed and instrument

1. Use valid, malformed, boundary, historical-bug, and structurally distinct seed inputs, retaining provenance and licensing.
2. Choose coverage-guided instrumentation or grammar/mutation fuzzing appropriate to format complexity and toolchain.
3. Track unique edges/paths, executions, timeouts, OOM events, sanitizer findings, and nondeterminism without inventing rates.
## Phase 4: Triage and minimize

1. Reproduce each candidate crash in a clean local run; distinguish harness defects, resource exhaustion, false positives, and real target faults.
2. Minimize failing inputs while preserving the fault and record exact build flags, sanitizer output, stack trace, and source revision.
3. Group defects by root cause and assess exploitability only with evidence; avoid publishing sensitive proof material without authorization.
## Phase 5: Fix and regression-test

1. Apply narrowly scoped fixes that preserve valid inputs and all existing features; add each minimized input to the regression corpus.
2. Rebuild with appropriate sanitizers and compare coverage and behavior across corrected and original edge cases.
3. Report fuzzing time/budget, environment, reproduction results, test outcomes, and limits to conclusions.

## Required project deliverables

1. **Authorized target and harness interface specification** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Deterministic seed corpus inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Crash reproduction and minimization records** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Coverage and sanitizer result ledger** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Regression inputs and root-cause remediation** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Fuzzing remote systems without authorization.
- Reporting a crash without independent reproduction.
- Losing minimized cases after fixes.
- Making harness bypass security-relevant parsing.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
