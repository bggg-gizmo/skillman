# Codeman Recovery — specialist execution playbook

## Preconditions

Use when code or a release previously worked and now fails, while preserving unrelated work and user data.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Contain and preserve evidence

1. Record error symptoms, timeline, last known-good behavior, environment, logs, affected customers/systems, and current repository status.
2. Make safe backups of user data and existing configuration before stateful recovery when authorized and practical; never overwrite backups.
3. Avoid destructive resets, hard cleans, broad rollbacks, or unreviewed migration reversal.
## Phase 2: Identify the regression boundary

1. Compare working and failing versions by config, schemas, public contracts, dependency resolution, external service behavior, and deployment assets.
2. Use deterministic reproduction and targeted git diff/log/bisect only when repository access exists and worktree safety is established.
3. Separate coincidental environmental changes from true code regression using evidence.
## Phase 3: Plan smallest restorative change

1. Identify the minimal component needed to restore previous behavior while retaining authorized new features.
2. For data failures, design reversible repair with transaction boundaries, audit trails, idempotency, and integrity checks.
3. Check migrations and backward compatibility so a repair does not leave application and persisted state out of sync.
## Phase 4: Execute and verify cautiously

1. Apply repair only inside user-authorized scope, preserving the working tree, audit logs, unrelated code, and prior generated assets.
2. Verify the originally failing path plus surrounding unaffected user journeys and failure modes.
3. Test the repair against both old and new expected behavior where feasible, including startup montage behavior when related.
## Phase 5: Report recovery state

1. Provide root cause evidence, restoration actions, data integrity checks, tests and remaining gaps.
2. Distinguish full restoration, degraded but usable operation, unresolved corruption, and unverified state.
3. Propose follow-up preventive tests without adding unrelated functionality absent authorization.

## Required project deliverables

1. **Incident/reproduction timeline** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Last-known-good versus failing diff** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Data-preserving recovery plan** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Regression test evidence** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Repair and residual-risk report** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Using git reset --hard as a default fix.
- Deleting failing tests to go green.
- Rolling back schema without data compatibility.
- Claiming restored functionality from a build alone.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
