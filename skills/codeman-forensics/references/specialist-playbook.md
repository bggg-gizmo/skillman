# Codeman Forensics — specialist execution playbook

## Preconditions

Use for authorized disk, memory, event-log, browser, endpoint, and network forensic investigation.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Establish evidence custody

1. Record source identity, collection scope, case context, acquisition time, hash algorithm, custody changes, and original media handling.
2. Prefer read-only copies and write-protection; do not modify original evidence or run repair utilities on it.
3. Document time zones, clock drift, encryption state, and limits of the available acquisition method.
## Phase 2: Validate and normalize artifacts

1. Hash acquisitions and calculate integrity checks before/after transformations; retain the original bytes separately.
2. Parse logs, filesystem metadata, registries, browser histories, memory structures, packet captures, and process artifacts according to their format versions.
3. Distinguish absent events from uncollected, expired, encrypted, or malformed evidence.
## Phase 3: Correlate multi-source timelines

1. Normalize timestamps to a declared time scale with conversion provenance, daylight-saving assumptions, and explicit clock uncertainty.
2. Cross-reference process lineage, network activity, file changes, authentication, persistence artifacts, and user actions with attributable source records.
3. Build hypotheses with competing explanations rather than declaring intent from a single artifact.
## Phase 4: Validate conclusions

1. Use independent sources where possible, demonstrate parser correctness with known fixtures, and track every derived event back to bytes or log records.
2. Separate observation, inference, and attribution; assign confidence based on artifact integrity and corroboration.
3. Identify evidence gaps, anti-forensic possibilities, and acquisition limitations without overstating causality.
## Phase 5: Deliver defensible outputs

1. Provide chain-of-custody records, checksums, timestamped timelines, evidence tables, and repeatable parsing procedures.
2. Redact unrelated personal information as authorized and keep sensitive artifacts within approved destinations.
3. Ensure scripts and reports do not alter source evidence or discard uncertainty.

## Required project deliverables

1. **Chain-of-custody and integrity record** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Acquisition/source inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Normalized event timeline** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Artifact-to-conclusion evidence map** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Investigation findings and uncertainty report** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Editing artifacts during analysis.
- Losing time-zone and clock-drift context.
- Assuming no log means no event.
- Reporting attribution without corroboration.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
