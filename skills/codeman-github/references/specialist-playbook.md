# Codeman GitHub — specialist execution playbook

## Preconditions

Use only when the user explicitly requests GitHub-based repository analysis or interaction; never activate GitHub access merely because a GitHub remote exists.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Confirm access and billing boundary

1. Identify the specific repository, organization, ref, and authorized operation. Use only a connected or approved GitHub interface with appropriate permissions.
2. Assume any write that might fire Actions, checks, deployment hooks, hosted runners, Codespaces, or Copilot jobs is disallowed under the no-credit rule; do not trigger it.
3. If the consumption status of an operation cannot be proven non-metered, stop that operation and report the constraint without attempting an alternative billable route.
## Phase 2: Read source and repository metadata

1. Use read-only fetch/search/list functions when requested to inspect current files, commit history, branches, issues, and PR metadata.
2. Confirm default branch and exact commit SHA for every cited code location; use named refs only with their resolved revision context.
3. Avoid revealing credentials, tokens, private repository content, or security findings to unauthorized destinations.
## Phase 3: Analyze repository changes

1. Compare files and patch hunks by path and exact revision; map modified symbols to runtime features and tests.
2. Inspect CI configuration read-only to identify triggers, but never dispatch a workflow or push code that might trigger a metered job.
3. Detect incompatible merges, deleted feature paths, lockfile drift, and submodule/LFS issues from available evidence.
## Phase 4: Prepare safe local changes

1. Where local source is available and authorized, implement complete changes on the local copy and verify using local non-metered tools.
2. Do not create commits, PRs, reviews, tags, releases, branches, workflow runs, or pushes unless the user expressly asks and the specific operation is known to consume no credits.
3. For the opening montage, locate its actual path within the configured source repository using requested read-only access; do not assume a URL or download from guessed paths.
## Phase 5: Report exactly what occurred

1. Give precise repository and commit identity, inspected paths, findings, diffs, and test results.
2. Clearly separate locally prepared work from changes committed or published on GitHub. Never claim a push, review, merge, or CI run not executed.
3. Describe unavailable access or billing ambiguity as a blocker rather than silently performing a credit-consuming operation.

## Required project deliverables

1. **GitHub operation/authorization record** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Repository and commit provenance** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Revision comparison and compatibility review** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Local change patch when requested** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Credit-consumption and execution audit** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Assuming API requests are always unbilled.
- Pushing a branch that automatically launches Actions.
- Fabricating montage asset paths.
- Treating repository read permission as approval to write.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
