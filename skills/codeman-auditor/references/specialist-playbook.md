# Codeman Auditor — specialist execution playbook

## Preconditions

Use for full codebase audits, pre-release inspections, implementation completeness reviews, and investigation of incomplete or disconnected features.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Set audit scope and evidence rules

1. Confirm authorized repositories, branches, environments, standards, and threat model; keep existing working-tree changes intact.
2. Enumerate entry points, source modules, exported APIs, dependencies, generated artifacts, test suites, and release pathways.
3. Separate demonstrably defective code from speculative risk, style preference, and requests for new functionality.
## Phase 2: Inspect feature completeness

1. Trace each feature from entry point through validation, execution, data persistence, response, and error handling.
2. Find unregistered routes, orphaned UI actions, missing handlers, empty implementations, swallowed exceptions, unreachable code, ignored feature flags, and nonfunctional packaging.
3. Compare design documentation and configuration against code; verify which assertions are executable and which are prose only.
## Phase 3: Inspect quality and security

1. Review authz/authn boundaries, input validation, secrets, dangerous deserialization, unsafe filesystem access, injections, concurrency and resource lifetimes.
2. Assess dependency and build integrity, observability, portability, performance hot spots, and exception transparency.
3. Check test assertions for behavior coverage, flakiness, false positives, and missing negative paths.
## Phase 4: Validate and classify findings

1. Produce minimal reproducible evidence using read-only or non-destructive techniques where available, and label unexecuted hypotheses accurately.
2. Assign severity and confidence based on technical impact, exploitability or reliability impact, reachability, and tested conditions.
3. Deduplicate root causes; record affected files and symbols and the smallest safe correction compatible with all existing behavior.
## Phase 5: Report without unauthorized modification

1. Deliver a prioritized findings register, traceability to affected features, and remediation tests; do not change source unless explicitly asked.
2. State scan/tool limitations, files excluded from scope, and why each finding was or was not validated.
3. If asked to fix findings, obtain a pre-change baseline and send fixes through guardian, integrator, and tester checks.

## Required project deliverables

1. **Scoped repository inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Prioritized finding register with file and symbol references** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Reachability and reproduction evidence** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Test coverage and integration-gap matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Remediation and verification plan** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Conflating grep matches with vulnerabilities.
- Calling partial scanning comprehensive.
- Reporting missing code from an inaccessible file.
- Refactoring under the guise of auditing.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
