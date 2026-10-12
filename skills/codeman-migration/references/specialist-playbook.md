# Codeman Migration — specialist execution playbook

## Preconditions

Use for framework/version upgrades, database migrations, service decomposition, API deprecations, and platform moves.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Discover current and target states

1. Inventory current versions, public interfaces, dependencies, data formats, storage, assets, workflows, and operating environments.
2. Define target-state requirements without removing features, and list explicit user-authorized breaking differences.
3. Capture a working baseline, representative datasets, consumer versions, and recovery constraints.
## Phase 2: Perform gap and risk analysis

1. Compare runtime/toolchain behavior, deprecated APIs, serialization, permissions, transaction semantics, file formats, and dependency compatibility.
2. Assess migration duration, lock impact, downtime requirements, resource constraints, and failure/replay handling.
3. Differentiate reversible configuration and code changes from irreversible data transformations.
## Phase 3: Design staged transition

1. Specify preparation, dual-support/compatibility, data backfill, traffic cutover, monitoring, and retirement steps as independently testable phases.
2. Plan feature flags, version negotiation, backfill verification, incremental deploy order, and strict data/contract invariants.
3. Define abort criteria and recovery procedures based on real backup/restore capability, not assumed reversibility.
## Phase 4: Execute within user-authorized scope

1. Implement complete adapters, migrations, dependent code updates, package changes, CLI revisions, and test fixtures.
2. Preserve legacy consumers and stored data until the explicit cutover step is approved; do not delete deprecated code solely for tidiness.
3. Run dry-run or staging tests before touching live environments where such environments exist.
## Phase 5: Verify and report

1. Test old and new functionality, migration repeatability, partial failure, re-entry, data consistency, concurrent operation, and performance.
2. Validate the actual upgrade and downgrade/recovery paths supported, including persistence integrity and externally observable behavior.
3. Report executed migrations versus prepared scripts, incomplete phases, and non-reversible effects.

## Required project deliverables

1. **Current/target compatibility inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Risk-ranked phased migration plan** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Complete scripts/adapters and tests** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Cutover and data-integrity verification** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Rollback/abort constraints and status** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Big-bang rewrite without intermediate compatibility.
- Blind migration against production.
- Dropping columns before old clients retire.
- Promising rollback after irreversible transformations.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
