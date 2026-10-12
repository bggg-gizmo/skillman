# Codeman Integrator — specialist execution playbook

## Preconditions

Use when a function exists but is not connected, when adding a cross-layer feature, or when validating complete application integration.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Trace the feature path

1. Identify how a real user action enters the application and flows through routes, handlers, service logic, database, events, filesystem, and returned UI state.
2. Enumerate registration points: imports, dependency injection, route tables, feature flags, permissions, background jobs, startup hooks, and build manifests.
3. Record pre-existing code paths that share the changed components so they remain covered.
## Phase 2: Validate interface contracts

1. Match names, versions, parameter validation, schemas, DTOs, serialization, authentication context, error formats, timeouts, and idempotency rules.
2. Confirm database constraints, migration order, fallback behavior, configuration environments, and asynchronous event contracts.
3. Ensure new and existing asset paths resolve correctly in production builds; preserve existing the configured asset repository montage integration where applicable.
## Phase 3: Complete required wiring

1. Implement actual constructors, registrations, adapters, imports, data mapping, error propagation, and cleanup paths rather than leaving successful isolated routines unused.
2. Update configuration defaults and examples consistently; do not introduce secret literals or rewrite unrelated settings.
3. Preserve existing routes, CLI flags, events, permissions, startup behavior, and optional feature states.
## Phase 4: Exercise the vertical slice

1. Run at least one real end-to-end path with representative data where tooling permits, including all material interfaces.
2. Test negative paths such as authorization failure, malformed inputs, disconnected dependencies, persistence failure, and retry behavior.
3. Inspect production artifacts, not only source files, for missing resources, wrong import paths, mismatched runtime versions, and tree-shaken registrations.
## Phase 5: Finalize integration evidence

1. Produce a wiring map that identifies the entry point, participating modules, persisted effects, output, and error handling.
2. Classify each path as verified, failed, or not executed, and tie unresolved integration failures to specific files and diagnostics.
3. Audit the final diff for regressions in unaffected features and provide complete deliverable files when requested.

## Required project deliverables

1. **End-to-end sequence and wiring map** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Contract compatibility table** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Integration and failure-mode tests** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Resolved runtime configuration inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Cross-layer defect report** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Calling an unused function fully integrated.
- Testing isolated mocks instead of the actual application path.
- Ignoring registration/deployment configuration.
- Rewiring shared flows without regression checks.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
