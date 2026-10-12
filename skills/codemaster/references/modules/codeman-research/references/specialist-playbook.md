# Codeman Research — specialist execution playbook

## Preconditions

Use before adopting libraries, implementing complex protocols, evaluating security reports, or making evidence-sensitive engineering decisions.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Frame an answerable technical question

1. State exact behavior to explain, codebase constraints, version/platform matrix, acceptable licensing, security requirements, and decision deadline.
2. Separate user requirements from hypotheses and determine which claims require fresh external verification.
3. Define what constitutes sufficient evidence: official docs, release notes, specifications, source/tests, maintainers, or reproducible experiments.
## Phase 2: Collect versioned evidence

1. Prefer vendor/maintainer documentation, RFCs, security advisories, released source, issue discussions, and authoritative test cases.
2. Check release and publication dates, affected versions, end-of-life status, and changes across relevant branches.
3. Use read-only GitHub access only when requested, and never start actions, hosted compute, or credit-consuming operations.
## Phase 3: Evaluate implementation options

1. Compare API compatibility, security posture, maintenance burden, platform support, performance evidence, transitive dependencies, and migration cost.
2. Identify conflicts or stale recommendations across sources; reproduce pivotal claims locally if an approved environment is available.
3. Distinguish design tradeoffs from hard constraints, and avoid inventing performance figures or vulnerabilities.
## Phase 4: Convert findings into actionable work

1. Recommend concrete implementation/verification approaches that retain all existing functions and features.
2. Tie each option to necessary configuration, code changes, tests, and rollback considerations.
3. For code requested directly, provide complete implementation artifacts rather than replacing delivery with a reading list.
## Phase 5: Publish cited, uncertainty-aware research

1. Provide source links/versions, evaluated alternatives, evidence-strength assessment, and explicit unknowns.
2. Note information that could not be verified due to missing browsing/connector access or tool constraints.
3. Do not represent prospective experiments, benchmarks, or integrations as performed.

## Required project deliverables

1. **Technical question and decision criteria** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Dated authoritative source ledger** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Options and compatibility comparison** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Reproducible validation plan/results** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Evidence-backed recommendation and residual unknowns** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Relying on out-of-date documentation for latest APIs.
- Confusing popularity with suitability.
- Quoting issue comments as confirmed vulnerabilities.
- Using an uncited guess as a design constraint.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
