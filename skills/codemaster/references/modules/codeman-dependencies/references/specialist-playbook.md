# Codeman Dependencies — specialist execution playbook

## Preconditions

Use for dependency upgrades, lockfile conflicts, runtime version mismatches, deprecations, package provenance, and library replacement planning.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Inventory resolution sources

1. Read manifests, lockfiles, workspace constraints, toolchain versions, registries, container base images, transitive edges, peer/optional dependencies, and private package sources.
2. Distinguish declared version ranges from actually resolved versions and identify hash/integrity metadata.
3. Record supported operating systems, language runtime and ABI constraints, and existing integration APIs.
## Phase 2: Characterize the change

1. Determine whether the task is vulnerability remediation, build repair, lifecycle maintenance, license issue, performance concern, or explicit modernization.
2. Inspect upstream release notes, API migrations, deprecations, advisories, and license changes from trusted sources if access is allowed.
3. Build a compatibility matrix for direct and indirect users of any changed library.
## Phase 3: Plan minimal version movement

1. Prefer targeted, compatible upgrades with deterministic lockfile regeneration and reproducible resolution.
2. Avoid unbounded range widening, dependency removal, or wholesale framework rewrites without explicit scope and tests.
3. Account for native extensions, build scripts, platform packages, runtime assets, and major-version behavior changes.
## Phase 4: Integrate and verify

1. Compile/typecheck/build, exercise affected interfaces, run existing unit/integration/security tests, and verify installer/runtime packaging.
2. Check dependency trees for duplicate incompatible versions, vulnerability exposure, license issues, and integrity failures.
3. Do not trigger hosted GitHub CI or metered tools; execute local checks when permitted.
## Phase 5: Deliver exact resolution evidence

1. Supply complete updated manifests/lockfiles, rationale, version deltas, impacted API paths, and test outcomes.
2. Report repositories or package sources not contacted and vulnerability databases not refreshed.
3. Never claim an upgrade is safe merely because a lockfile generated successfully.

## Required project deliverables

1. **Manifest and resolved dependency inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Version/ABI compatibility matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Minimal updated lockfiles** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Functional and supply-chain test evidence** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Remaining advisory and license risk report** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Deleting locked dependencies to make install pass.
- Ignoring peer and optional dependency behavior.
- Trusting package version numbers without provenance.
- Running broad update-all commands reflexively.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
