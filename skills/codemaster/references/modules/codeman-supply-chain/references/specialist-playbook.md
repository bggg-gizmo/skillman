# Codeman Supply Chain — specialist execution playbook

## Preconditions

Use for software supply-chain audits, release hardening, dependency provenance, CI integrity reviews, and incident response to compromised packages.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Define trust chain

1. Inventory first-party source, registries, dependencies, build tooling, base images, signing identities, secrets, CI configuration, and distribution endpoints.
2. Identify authoritative manifests and lockfiles; distinguish runtime, build-time, development, optional, and transitive dependencies.
3. Record repository revision, target platforms, and packaging targets before interpreting vulnerability or integrity results.
## Phase 2: Inspect component provenance

1. Generate or review SBOMs with accurate versions, hashes, package URLs, licenses, and dependency relationships when tools are available.
2. Check integrity metadata, source references, registry origins, dependency confusions, typosquatting indications, and suspicious maintainer or publish changes.
3. Classify CVEs by reachable affected functionality and existing mitigations instead of assuming every matched advisory is exploitable.
## Phase 3: Review reproducibility and build control

1. Inspect pinned resolution, hermetic inputs where supported, deterministic archives, build flags, container digest pinning, and isolation of build credentials.
2. Audit CI workflow files read-only when GitHub access was requested, but never dispatch workflows, hosted runners, Codespaces, or any credit-consuming service.
3. Separate attestation verification from attestation creation; never claim artifacts are signed or provenance-attested unless evidence exists.
## Phase 4: Plan and test safe remediation

1. Upgrade or replace dependencies only with authorization, preserving APIs, behavior, supported platforms, and lockfile consistency.
2. Test affected code paths, dependency license constraints, and artifact hashes after changes; avoid mass upgrades without risk/compatibility analysis.
3. Plan key rotation or package yanking only as an explicitly authorized operational change.
## Phase 5: Publish traceable results

1. Deliver SBOMs, provenance chain, verified hashes, advisory findings, remediation tests, and unresolved trust gaps.
2. Identify which verification depended on external registry access and which was performed offline.
3. Keep secret values out of reports and preserve user assets and packaging contracts.

## Required project deliverables

1. **Dependency/SBOM inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Artifact provenance and hash ledger** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Reachability-based advisory findings** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Build trust and credential flow review** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Remediation compatibility results** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Treating a vulnerability count as risk score.
- Claiming reproducible build without matching artifacts.
- Verifying only first-party dependencies.
- Triggering GitHub CI while auditing credit safety.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
