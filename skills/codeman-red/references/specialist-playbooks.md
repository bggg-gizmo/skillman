# Codeman Red — specialist playbooks

Use this reference when the request involves authorized adversarial security testing. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** authorized exploit validation, attack-surface analysis, fuzzing, protocol testing.

## Engagement setup

1. Extract the user-approved target set, environment, credentials/roles, rules of engagement, exclusions, maintenance windows, and allowed testing intensity.
2. Select non-destructive methods and test data where possible; establish stop conditions and rollback for actions that could alter state.
3. Identify whether the task is analysis, local reproduction, external testing, or exploit validation, and only use tools actually available.
4. Do not expand testing to connected assets or production targets merely because they are discoverable.

## Authorized exploit validation

1. Confirm the suspected weakness, component/version, privilege context, prerequisites, and explicit validation objective.
2. Choose the least intrusive proof that distinguishes a vulnerability from an incorrect hypothesis.
3. Use scoped controlled payloads or benign markers, preserve expected service behavior, and avoid unnecessary exfiltration or persistence.
4. Capture request/response, crash traces, logs, or state changes sufficient for reproducibility; sanitize secrets and avoid publishing sensitive access material.
5. Provide root cause, exact observed result, cleanup status, remediation and post-fix regression validation.

## Attack-surface analysis

1. Inventory only approved domains, repositories, IP ranges, application routes, APIs, packages, and service identities.
2. Correlate assets and exposure to ownership and reachable entry points; distinguish observed from inferred endpoints.
3. Classify authenticated/unauthenticated trust boundaries, permissions, third-party dependencies, data access, and risky default configurations.
4. Prioritize realistic paths and validation plans, including exposure window, preconditions, and potential blast radius.
5. Provide source/timestamp for discoveries; do not infer that untested hosts are exploitable.

## Fuzzing

1. Identify parser or API grammar, input corpus, harness, invocation mode, mutation strategy, instrumentation, and crash-detection mechanism.
2. Define a bounded budget and isolation strategy; preserve reproducible seeds, target build, and sanitizer configurations.
3. Exercise valid and malformed inputs with deterministic reproduction paths and meaningful coverage signals.
4. Deduplicate and minimize failures without discarding the original artifact; separate target bugs from harness failures and out-of-memory artifacts.
5. Convert confirmed failures into regression tests and report exact conditions and coverage limitations.

## Protocol testing

1. Document transport, framing, states, version negotiation, authentication, cryptographic expectations, and timeout/retry semantics.
2. Construct permitted valid, malformed, boundary, ordering, replay, and downgrade tests against an approved service or local harness.
3. Preserve traffic captures and correlate client/server state while avoiding credential disclosure.
4. Validate error recovery, resource handling, authorization boundaries, and state-machine invariants.
5. Provide reproducible traces, protocol field details, observed divergence, and safe remediation.

## Engagement output

Report approved scope, tests actually executed, observations and timestamps, affected assets, reproducible evidence, severity with rationale, cleanup actions, unknowns, and retest steps. Do not claim exploitation where only source review or simulation occurred.

