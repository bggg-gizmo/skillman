# Codeman Build Doctor — specialist execution playbook

## Preconditions

Use when builds fail, installers break, tools disagree across machines, or a program starts incorrectly after compilation.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Reproduce the exact failure

1. Capture the original command, toolchain versions, platform/architecture, environment differences, logs, exit status, and first actionable diagnostic.
2. Inspect manifests, lockfiles, CMake/Cargo/npm/Python/Go build configuration and caches without deleting or rewriting them reflexively.
3. Preserve source-tree status and distinguish clean baseline failures from errors introduced by requested work.
## Phase 2: Isolate the responsible layer

1. Differentiate syntax/type errors, ABI/architecture mismatch, missing imports, conflicting dependency versions, linker symbols, build scripts, missing assets, and runtime configuration.
2. Trace compiler or runtime messages to originating imports, modules, flags, environment variables, and exact dependency edges.
3. Use targeted diagnostics and reproducible tool invocations before broad upgrades or toolchain replacement.
## Phase 3: Implement minimal complete repair

1. Modify only responsible code/configuration while retaining exports, feature flags, asset paths, and application behavior.
2. Prefer supported, compatible dependency changes with lockfile consistency; never silently unpin entire dependency graphs.
3. Repair platform-specific paths, dynamic loader requirements, packaging manifests, startup hooks, and installer metadata when involved.
## Phase 4: Verify across lifecycle

1. Rerun the originally failing command and relevant clean build, static checks, tests, smoke start, packaging, and installation steps where available.
2. Confirm debug/release and target platform differences; treat a locally successful compile as insufficient if the reported issue was packaging or runtime.
3. Inspect required application resources including the existing opening montage if it is part of startup.
## Phase 5: Deliver diagnostics and repair evidence

1. Record root cause, exact modifications, commands and exit codes, validated build artifacts, and residual environment dependencies.
2. Flag each untested environment as unverified; do not infer success across unsupported platforms.
3. Provide complete changed files and a safe recovery path without wiping untracked user data.

## Required project deliverables

1. **Reproduction log and environment fingerprint** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Root-cause analysis** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Minimal repair diff** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Build and runtime verification report** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Platform compatibility matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Fixing errors by deleting features.
- Mass dependency upgrades without compatibility analysis.
- Assuming compile success proves installer success.
- Clearing entire caches or user files without approval.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
