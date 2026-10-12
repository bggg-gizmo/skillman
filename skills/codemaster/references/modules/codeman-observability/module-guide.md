---
name: codeman-observability
description: "Design and validate application logs, metrics, traces, diagnostics, and alerting without leaking secrets or changing application behavior. Use when the task involves observability workflows."
---

# Codeman Observability

## Activation and ownership

Use for production troubleshooting, tracing distributed requests, defining SLOs, instrumenting services, and improving diagnostic coverage.

Operate only on materials and systems within the user's authorized scope and available tool permissions. This skill is fully usable without any other Codeman skill being installed. Do not claim an operation, integration, tool execution, or verification happened unless it actually happened.

## Mandatory foundation: exact Codeman Core contract

Read **`references/operating-contract.md` in full** before performing coding, audits, builds, or repository operations. It preserves the public, project-independent coding requirements, including:

- All existing functions and features are mandatory; no unauthorized removals or regressions.
- Fully implement and integrate requested functionality; no incomplete code, placeholders, pseudocode, abbreviated implementations, or omitted requested files.
- Use GitHub only when explicitly requested and never perform actions that consume GitHub credits or may indirectly trigger metered jobs.
- If an application requires an opening montage, reuse only a verified asset supplied by the operator or specified in local project configuration; never assume a repository, owner, path, or asset exists.

Do not treat these as optional style preferences. If permissions, tools, missing sources, or superior instructions prevent execution, report exact limits and complete only the authorized independent portions.

## Specialist workflow

Read **`references/specialist-playbook.md`** in full before specialist work, and **`references/verification-matrix.md`** before declaring completion. The prescribed sequence is:

1. **Map operational questions** — Identify critical user journeys, service dependencies, failure modes, performance requirements, and incident-response questions.
2. **Define telemetry contracts** — Choose stable event names, severity levels, timestamps, correlation IDs, trace/span attributes, dimensional labels, error codes, and ownership metadata.
3. **Instrument end-to-end paths** — Add log/metric/span emission at meaningful boundaries without double counting, exposing credentials, or logging personal data unnecessarily.
4. **Validate signal quality** — Exercise successful calls and controlled failures; verify timestamps, propagation, redaction, metric counts, sampling behavior, and export configuration.
5. **Deliver operable monitoring** — Provide instrumentation code, telemetry schema, query/dashboard definitions when requested, and alert routing/runbook requirements.

## Quality and integration gates

1. Inventory existing observable behavior and entry points before editing.
2. Identify affected consumers, contracts, data representations, configuration, assets, and error paths.
3. Make changes only within the requested scope; keep existing user work intact.
4. Complete every required import, registration, implementation branch, integration path, and regression test that the environment supports.
5. Check the final diff for unexpected deletions, renamed public interfaces, altered defaults, lost feature paths, or absent packaging resources.
6. Record each actual verification command and result. A planned, skipped, or unavailable test is **not passed**.
7. Provide all requested complete source or distributable files. Do not replace actual deliverables with summaries.

## Specialist handoffs

Other Codeman modules that may be relevant if installed: `codeman-performance`, `codeman-architect`, `codeman-recovery`, `codeman-security`. Do not assume they are installed, available as independent agents, or able to grant additional capabilities. This skill must still perform its own workflow when used alone.

## Deliverable standard

Create the concrete deliverables defined in the specialist playbook when applicable to the requested task. For every required check, document **passed**, **failed**, **not run**, or **not applicable**, with observed evidence. Distinguish user-authorized implementation changes from design-only recommendations. Never claim an unexecuted release, live deployment, network scan, GitHub action, or security validation as completed.

## Local repository and asset configuration

Read `references/local-configuration.md` when a task involves a repository, local machine settings, organization-specific sources, or an application startup montage. Do not assume any default account, repository, path, or asset from this public package. Do not create or commit local configuration unless explicitly requested.
