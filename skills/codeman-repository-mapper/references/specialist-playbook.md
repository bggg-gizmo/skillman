# Codeman Repository Mapper — specialist execution playbook

## Preconditions

Use to onboard to an unfamiliar repository, find feature implementations, evaluate change impact, or build a stable engineering inventory.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Enumerate what actually exists

1. Identify source roots, workspaces, generated code, vendored dependencies, third-party assets, test roots, and build/deployment manifests.
2. Inspect language-specific project metadata and entry points; record gitignored paths without reading secrets or uncontrolled binary blobs.
3. Record repository revision and branch so the resulting map can be regenerated against a known tree.
## Phase 2: Build symbol and component inventories

1. Catalog classes, functions, exported symbols, CLI commands, HTTP routes, event consumers, scheduled jobs, screens, plugins, and configuration keys.
2. Capture definitions and call sites using language-aware parsers when available; label text-search-derived edges as potentially incomplete.
3. Disambiguate duplicate symbol names by module/file, signature, visibility, and runtime binding.
## Phase 3: Reconstruct runtime architecture

1. Trace request and event paths from entry points through services, storage, queues, outbound calls, and observable outputs.
2. Link feature flags, environment variables, startup actions, migrations, and installer assets to the features that use them.
3. Account for conditional imports, reflection, dynamic dispatch, dependency injection, generated code, and platform-specific builds.
## Phase 4: Compute change-impact views

1. For each named function or feature, list direct and indirect callers, dependent schemas, public contracts, tests, and operational concerns.
2. Identify cyclic dependencies, orphaned registrations, unreachable functionality candidates, and duplicated implementations without deleting them.
3. Locate the existing intro montage only through authorized repository inspection and record its actual integration path.
## Phase 5: Publish a trustworthy map

1. Produce file-to-feature, symbol-to-caller, API-to-implementation, and feature-to-test tables with concrete paths.
2. Mark partial or unparsed directories, dynamic calls, generated entry points, and stale assumptions as coverage limitations.
3. Do not mutate source during discovery; recommend updates only in response to a separate modification request.

## Required project deliverables

1. **Repository tree and entry-point index** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Symbol and call-site graph** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Feature-to-file and feature-to-test matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Dependency and runtime path diagrams** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Mapping coverage and uncertainty register** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Treating import graph as full runtime call graph.
- Ignoring generated or dynamically registered handlers.
- Inventing paths from naming conventions.
- Dumping secrets during recursive indexing.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
