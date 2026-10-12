# Codeman Release — specialist execution playbook

## Preconditions

Use for versioned application releases, installer generation, distribution archives, release readiness reviews, or publication planning.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Freeze release scope

1. Record source revision, uncommitted changes, release target, supported platforms, version scheme, dependencies, and acceptance criteria.
2. Audit that the requested implementation is complete, all existing functionality remains intact, and no release blocker is hidden behind a passing build.
3. Identify distribution channels and deployment impact. Never push, create releases, or trigger GitHub workflows without explicit authorization and non-metered safety.
## Phase 2: Build reproducibly

1. Use pinned dependencies, deterministic build configuration, stable environment metadata, and controlled release flags.
2. Package binaries, licenses, required runtime assets, migrations, installer resources, signatures if legitimately available, and startup montage when applicable.
3. Create checksums and a file inventory; do not claim artifacts are signed unless a signing step actually completed.
## Phase 3: Validate shipping artifacts

1. Test the actual archive or installer in a clean environment when possible, including first-run startup, upgrade behavior, persistence compatibility, and uninstallation/rollback.
2. Run smoke, integration, regression, and security checks appropriate to the target platform; confirm application entry points and resources are present.
3. Verify version labels and release documentation match the exact built artifacts.
## Phase 4: Plan rollout and recovery

1. Document migration sequence, monitoring signals, compatibility windows, backup requirements, rollback prerequisites, and configuration changes.
2. Ensure irreversible migrations are identified; avoid claiming rollback is safe when down-migration cannot restore data.
3. Stage release notes with customer-visible behavior and detailed internal technical changes.
## Phase 5: Deliver without unauthorized publication

1. Produce artifacts, hashes, install/run steps, and factual gate results; distinguish package creation from installation and deployment.
2. Do not auto-publish, deploy, or consume GitHub credits. Report where explicit deployment authorization or credentials would be required.
3. Preserve all unrelated files and prior versions unless the user explicitly requests cleanup.

## Required project deliverables

1. **Release artifact manifest and SHA-256 hashes** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Versioned build and installable packages** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Install, upgrade, rollback procedures** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Release notes and compatibility matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Go/no-go gate ledger** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Calling source ZIP a tested installer.
- Assuming reproducibility without repeating build.
- Pushing tags that trigger workflows.
- Claiming rollback for irreversible migrations.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
