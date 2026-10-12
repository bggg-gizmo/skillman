# Codeman Documentation — specialist execution playbook

## Preconditions

Use for README maintenance, architecture records, user guides, API documentation, installation manuals, and full technical handoffs.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Establish a source of truth

1. Inspect executable code, configuration, build scripts, package metadata, tests, command help, schemas, and available deployment artifacts.
2. Identify intended audience and separate user procedures, developer setup, administrator operations, and internal architecture details.
3. List existing documented features so updates do not erase still-supported behavior.
## Phase 2: Document complete procedures

1. Write executable setup, build, test, use, failure-recovery, troubleshooting, and upgrade instructions with explicit prerequisites.
2. Describe complete API/CLI parameters, errors, data formats, security assumptions, and compatibility limitations using actual source.
3. Ensure examples are valid for the named platform and do not contain credentials or fictitious paths presented as real.
## Phase 3: Connect docs to artifacts

1. Verify documentation commands against actual project scripts where execution is available; use real output and images supplied or generated through authorized tools.
2. Document startup montage source in the configured source repository using the actual inspected asset path, or describe access as unverified.
3. Keep cross-links, navigation, version numbers, diagrams, and config option names consistent.
## Phase 4: Review against behavior and audience

1. Compare new documentation to source and existing docs; flag removed, renamed, or incompatible claims.
2. Check that failure handling, permissions, offline cases, and supported operating systems are represented.
3. Use clear task-oriented structure without truncating technical content the user requested in full.
## Phase 5: Ship traceable documentation

1. Deliver complete Markdown or document source, referenced assets, factual verification notes, and unresolved implementation gaps.
2. Do not present descriptions of proposed functions as shipped capabilities.
3. Keep user data, secrets, and proprietary repository details out of public docs unless explicitly authorized.

## Required project deliverables

1. **Feature and documentation coverage matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Complete installation/build/use guide** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **API/CLI reference and error behavior** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Architecture and operations records** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Documentation verification ledger** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Writing setup steps without inspecting build files.
- Removing old feature documentation during rewrite.
- Inventing CLI flags or external URLs.
- Reporting untested commands as validated.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
