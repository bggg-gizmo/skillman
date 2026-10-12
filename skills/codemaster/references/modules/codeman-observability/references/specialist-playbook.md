# Codeman Observability — specialist execution playbook

## Preconditions

Use for production troubleshooting, tracing distributed requests, defining SLOs, instrumenting services, and improving diagnostic coverage.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Map operational questions

1. Identify critical user journeys, service dependencies, failure modes, performance requirements, and incident-response questions.
2. Inventory current structured logs, event IDs, metrics, traces, dashboards, alerts, and correlation context.
3. Document telemetry access and privacy restrictions, retention, sampling, and cardinality budgets.
## Phase 2: Define telemetry contracts

1. Choose stable event names, severity levels, timestamps, correlation IDs, trace/span attributes, dimensional labels, error codes, and ownership metadata.
2. Preserve causal context across asynchronous queues, background tasks, incoming/outgoing requests, and retries.
3. Design metrics with sane label cardinality and meaningful histograms rather than per-user/per-request metric dimensions.
## Phase 3: Instrument end-to-end paths

1. Add log/metric/span emission at meaningful boundaries without double counting, exposing credentials, or logging personal data unnecessarily.
2. Ensure failures are observable even when requests abort, dependencies time out, or processes shut down.
3. Retain existing logging contracts and application behavior while avoiding excessive synchronous I/O.
## Phase 4: Validate signal quality

1. Exercise successful calls and controlled failures; verify timestamps, propagation, redaction, metric counts, sampling behavior, and export configuration.
2. Validate alerts against known failures and plausible benign load, including alert fatigue and missing-data states.
3. Use real measured output for latency/error metrics instead of invented SLA figures.
## Phase 5: Deliver operable monitoring

1. Provide instrumentation code, telemetry schema, query/dashboard definitions when requested, and alert routing/runbook requirements.
2. Document retention/privacy risks, overhead measurements where available, and telemetry backends not actually connected.
3. Do not enable outbound telemetry or external monitoring services without authorization.

## Required project deliverables

1. **Telemetry schema and correlation map** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Instrumentation files and configuration** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Redaction and cardinality review** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Failure-path signal test results** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Monitoring/alert runbook and gaps** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Logging secrets to improve debugging.
- Unbounded labels on metrics.
- Generating dashboards without any data source.
- Confusing emitted logs with delivered telemetry.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
