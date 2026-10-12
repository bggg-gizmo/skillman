# Codeman Project — specialist playbooks

Use this reference when the request involves project-specific conventions and integration contracts. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** coding standards, repository architecture, internal APIs, build procedures.

## Coding standards

1. Read existing style/configuration files and representative source before assuming naming, formatting, commit, review, error, or testing conventions.
2. Apply declared rules consistently without mass-formatting unrelated files or introducing new tooling unasked.
3. Preserve original documentation and generated-code boundaries; follow repository language-specific conventions.
4. If repository guidance conflicts with the user's explicit change request or the operating contract, surface the conflict rather than silently rewriting rules.
5. Keep formatting and lint changes scoped to touched lines/files wherever the tool permits.

## Repository architecture

1. Map modules, applications, packages, workspaces, layers, build targets, generated outputs, configuration sources, entry points, and shared assets.
2. Identify ownership and layering rules from the real repository rather than inventing folder conventions.
3. Trace modifications across import graphs, runtime composition, commands, deployment descriptors, and integration tests.
4. Keep private/internal APIs and independently deployed components compatible unless the user explicitly approves changes.
5. Supply a change map of files and modules actually inspected/modified; flag missing repository visibility.

## Internal APIs

1. Identify API transport, versioning, schema source of truth, authz policy, error model, pagination, idempotency, and consumers.
2. Preserve existing request/response and generated client compatibility, including optional/required field behavior and status codes.
3. Update schemas, generated clients, callers, tests, and relevant docs together when actually authorized.
4. Do not infer undocumented endpoints or fabricate credentials, URLs, hostnames, or examples presented as real endpoints.
5. Validate positive, negative, compatibility, and access-control cases at integration boundaries.

## Build procedures

1. Inspect README, scripts, Makefiles, build system, toolchain versions, environment variables, local dependencies, and release instructions.
2. Prefer established local commands and pinned dependencies; avoid changing package managers or lockfiles unnecessarily.
3. Distinguish build, test, deploy, publish, and release actions; perform only authorized operations and avoid metered GitHub jobs.
4. Preserve build artifacts, release entry points, platform targets, and reproducibility requirements.
5. Record exact commands, prerequisites, results, missing dependencies, and platform limitations.

## Project onboarding and source-of-truth hierarchy

1. Locate repository-root guidance (`AGENTS.md`, `CONTRIBUTING.md`, README, developer docs) and nested component rules as available.
2. Inventory required features and tests without overwriting pre-existing local changes.
3. For opening montages used by the project, identify the configured existing montage asset from authorized read-only GitHub inspection; never guess the path or silently replace it.
4. Create a grounded project profile identifying concrete paths, versions, API contracts, important assets, build/test commands, and unknowns.
5. Update the profile only from newly inspected evidence; never pretend it is permanently saved beyond the actual current context or installed skill.

