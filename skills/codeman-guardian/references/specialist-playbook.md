# Codeman Guardian — specialist execution playbook

## Preconditions

Use before and after modifying an existing codebase, especially when the user requires no feature loss, no regression, or complete implementation.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Create an evidence-backed baseline

1. Record repository status and tracked/untracked changes; exclude secrets from outputs and never overwrite pre-existing user work.
2. Inventory exported functions, CLI options, screens, routes, jobs, configuration, feature flags, assets, integrations, error paths, and persistence behaviors.
3. Map key user journeys and map tests to features. Note undocumented functions rather than considering them expendable.
## Phase 2: Determine blast radius

1. Trace changed symbols to callers, import sites, event subscribers, serializers, schemas, migrations, build outputs, and deployment/configuration paths.
2. Classify each expected effect as preserved behavior, authorized change, newly required behavior, or unresolved ambiguity; do not reclassify changes to make diffs appear harmless.
3. Snapshot pre-change observable behavior where available using tests, golden files, contract schemas, and deterministic sample inputs.
## Phase 3: Enforce preservation during edits

1. Perform minimal scoped changes, retain public interfaces and semantics, and block unauthorized deletion, renaming, rewriting, or removal of integrations.
2. Review diff hunks for missing branches, dead routes, dropped dependencies, changed defaults, simplified exceptions, and partially implemented feature paths.
3. Protect the original intro montage and its integration when a project uses the configured montage asset.
## Phase 4: Verify behavior after changes

1. Run the pre-change baseline test set and new focused tests on the edited tree where the environment permits.
2. Compare API outputs, CLI flags, persisted data formats, state transitions, accessibility paths, and negative/error cases against recorded expectations.
3. Document genuine product changes as user-authorized exceptions only; unresolved differences remain potential regressions.
## Phase 5: Issue preservation verdict

1. Classify each monitored feature as preserved and verified, preserved but unverified, changed with authorization, failed, or unknown.
2. Flag missing test coverage, incomplete integration, and environmental blockers; never issue a universal no-regression guarantee from partial evidence.
3. Provide diff review evidence and focused repair guidance without discarding unrelated changes.

## Required project deliverables

1. **Pre-change feature and API inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Caller and dependency impact graph** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Baseline and after-change test outcomes** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Feature-by-feature preservation matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Unresolved compatibility-risk register** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Equating typecheck success with behavior preservation.
- Considering undocumented behavior disposable.
- Reporting no regression without baseline evidence.
- Overwriting an already dirty workspace.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
