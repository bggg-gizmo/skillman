# Codeman Protocol Lab — specialist execution playbook

## Preconditions

Use for protocol implementation, packet decoding, compatibility testing, troubleshooting, or scoped local protocol resilience assessment.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Establish protocol authority

1. Identify published RFC/specification, local captures, implementation source, negotiated versions, transport, and authorized endpoints.
2. Distinguish observed wire behavior from assumed protocol properties; preserve captured timestamps and redacted payload provenance.
3. Bound any active testing to owned/authorized local hosts or laboratory infrastructure.
## Phase 2: Model framing and state

1. Specify byte order, length fields, delimiters, checksums, encoding, compression, escaping, retransmission, and fragmentation/reassembly rules.
2. Build explicit state transitions for session setup, authentication, negotiation, steady state, error recovery, and teardown.
3. Account for out-of-order traffic, partial reads/writes, concurrent streams, sequence wraparound, and version negotiation.
## Phase 3: Implement robust codecs

1. Validate all sizes and offsets before allocation or access, reject malformed length prefixes, and enforce resource/time limits.
2. Preserve unknown extension fields when protocol rules require forward compatibility; avoid changing canonical encodings without evidence.
3. Ensure encoders and decoders agree on field constraints and duplicate/optional-field semantics.
## Phase 4: Validate interoperability and resilience

1. Run byte-level round-trip tests, known-answer vectors, malformed/truncated packet cases, replay-resistant behavior where relevant, and cross-version tests.
2. Test boundaries and local state-machine transitions including timeout, cancellation, abrupt disconnect, and renegotiation.
3. Use packet captures and differential observations only within authorization, retaining evidence without exposing secrets.
## Phase 5: Deliver protocol evidence

1. Publish frame layouts, state transitions, decoder edge cases, compatibility behavior, and exact test evidence.
2. Flag unsupported extensions and ambiguous spec language instead of silently dropping existing support.
3. Review fixes for regressions in currently accepted valid traffic and deployed clients.

## Required project deliverables

1. **Wire-format and state-machine specification** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Codec validation matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Known-answer and malformed-frame corpus** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Interoperability results** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Compatibility and resource-limit report** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Assuming packets align to socket reads.
- Accepting unchecked advertised lengths.
- Mutating live traffic without authorization.
- Rejecting previously supported extensions accidentally.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
