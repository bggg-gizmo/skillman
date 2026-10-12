# Codeman Automation — specialist execution playbook

## Preconditions

Use for build scripts, maintenance jobs, data-processing utilities, task orchestration, and CLI automation outside unauthorized metered services.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Define job and permissions

1. Document inputs, outputs, side effects, scheduling expectations, operating system, credentials, ownership, and failure recovery.
2. Identify idempotency requirements, concurrency limits, file locking, retries, timeouts, exit codes, and audit logging.
3. Explicitly distinguish local non-metered execution from GitHub-hosted Actions, Codespaces, Copilot jobs, or other credit-consuming services.
## Phase 2: Design the execution lifecycle

1. Separate parsing/validation, planning, dry-run when appropriate, mutation, verification, and structured reporting.
2. Use stable paths, safe quoting, bounded resource usage, least privileges, and secret-safe configuration.
3. Determine interruption behavior, atomic writes, rollback/compensation, checkpointing, and restart semantics.
## Phase 3: Implement full automation

1. Write complete executable commands/scripts including help, validation, error handling, logging, cleanup, and reliable nonzero failure exit status.
2. Handle malformed inputs, missing tools, network failures, repeated runs, partial outputs, and concurrent invocations.
3. Preserve existing tasks, flags, hooks, and expected file formats unless changes are explicitly authorized.
## Phase 4: Test failure and concurrency cases

1. Run deterministic unit and integration tests using isolated temporary files, controlled environment variables, and non-production endpoints.
2. Simulate partial failures, timeouts, interrupted writes, duplicate jobs, and retry exhaustion without destroying real data.
3. Verify exact created/modified files, scheduler setup assumptions, and actual exit statuses.
## Phase 5: Document deployable use

1. Provide complete scripts, dependencies, installation instructions, usage, permission model, and recovery steps.
2. Do not configure recurring tasks or execute external systems without user authorization.
3. Report scheduled configuration separately from jobs actually run and tested.

## Required project deliverables

1. **Runnable automation source and CLI help** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Execution/side-effect contract** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Idempotency and failure-mode tests** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Privilege and secret-handling review** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Operation/recovery documentation** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Automating destructive operations without dry-run safeguards.
- Assuming retries are always safe.
- Silently installing scheduled jobs.
- Using cloud-hosted GitHub automation despite credit rule.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
