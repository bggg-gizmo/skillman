# Codeman Contracts — specialist execution playbook

## Preconditions

Use for backwards-compatibility reviews, API/schema changes, versioning, migrations, or integration failures caused by mismatched interfaces.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Identify contract consumers

1. Enumerate API paths, methods, headers, request/response schemas, errors, public functions, CLI options, events, database formats, plug-in entry points, and documented guarantees.
2. Locate producers and consumers including external clients and older application versions; do not assume an unobserved consumer does not exist.
3. Determine contractual semantics for authentication, timeouts, retries, ordering, defaults, optional fields, and failure responses.
## Phase 2: Baseline compatibility

1. Capture OpenAPI/JSON Schema/Protobuf/GraphQL declarations or equivalent source definitions and implementation-level behavior.
2. Store representative samples and contract tests that exercise valid, invalid, boundary, and version-skewed data.
3. Classify changes as additive, behaviorally compatible, conditionally compatible, or breaking with stated consumer impact.
## Phase 3: Design compatible evolution

1. Prefer additive versioned fields and tolerant readers where safe; retain stable field names, return types, status/error semantics, and serialization rules.
2. For breaking changes explicitly requested by the user, specify version negotiation, deprecation windows, dual support, migration, and consumer updates.
3. Preserve stored data semantics and feature behavior across schema transitions; document constraints and reversible steps.
## Phase 4: Implement and verify contract tests

1. Test producer serialization and consumer parsing against canonical fixtures and actual runtime endpoints where possible.
2. Validate old-client/new-server and new-client/old-server combinations, malformed fields, auth failures, idempotency, and case/encoding behavior.
3. Run type/schema/static compatibility checks, but do not equate schema agreement alone with behavioral compatibility.
## Phase 5: Maintain contract evidence

1. Deliver a versioned contract inventory, compatibility decision per change, executable test results, and migration notes.
2. Escalate undocumented breaking behavior instead of silently changing clients, databases, or endpoints.
3. Tie contract exceptions to explicit user authorization and review changes for feature loss.

## Required project deliverables

1. **Contract surface inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Producer/consumer dependency matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Backward-compatibility classification** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Contract test fixtures and results** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Versioning and migration specification** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Relying on successful compilation for wire compatibility.
- Changing error codes without assessing clients.
- Treating undocumented consumers as nonexistent.
- Dropping old fields to simplify parsers.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
