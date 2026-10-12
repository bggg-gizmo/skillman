# Codeman Security — specialist playbooks

Use this reference when the request involves security analysis of applications and services. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** secure code review, SAST, DAST, vulnerability analysis, threat modeling.

## Secure code review

1. Identify language/framework, trusted and untrusted entry points, assets, privilege boundaries, authentication, authorization, and data sensitivity.
2. Trace data from source through validation and sanitization to sensitive sinks, including SQL, shell, templates, file IO, deserialization, network and logs.
3. Review authentication/session lifecycle, object-level authorization, secret handling, cryptography, dependency boundaries, and error leakage.
4. For each claim, provide file/line anchors, affected path, trigger conditions, impact, exploitability assumptions, and proposed minimal mitigation.
5. Separate confirmed exploitable findings, plausible issues requiring validation, and defense-in-depth opportunities.

## SAST

1. Inspect configured static analyzers and versions; reuse existing rules and project-specific baselines.
2. Select scopes and rules appropriate to languages and frameworks. Avoid suppressing findings just to make the report clean.
3. Run available approved analyzers in non-mutating mode; capture versions, arguments, commit, results, and tool errors.
4. Triage each alert by reachability, taint path, preconditions, sanitizers, false-positive evidence, and duplicate root cause.
5. Offer narrow fixes and regression tests; preserve original alert metadata and confidence.

## DAST

1. Confirm the intended target is an authorized testing environment and identify target URLs, authentication, excluded paths, concurrency and rate constraints.
2. Inventory API routes and session flows to design non-destructive probes, choosing authenticated roles needed to validate access controls.
3. Keep testing bounded: do not modify production data, cause outages, or exceed the provided scope.
4. Capture reproducible request/response evidence with secrets and personal data redacted.
5. Retest suspected findings against controlled input variants to distinguish environment errors and false positives.

## Vulnerability analysis

1. Describe vulnerable component and affected versions, attacker position, preconditions, controllable input, trust boundary crossed, and reachable sink.
2. Identify root cause and inspect adjacent code for alternate paths, variants, and bypasses.
3. Classify with applicable CWE and optionally CVSS vector only when sufficient evidence exists; do not invent severity precision.
4. Propose minimal root-cause mitigation and tests for exploit path, boundary values, and failure behavior.
5. Explain evidence limitations, affected versions, workarounds, and verification status.

## Threat modeling

1. Capture assets, business functions, data classifications, actors, trust boundaries, entry points, deployment architecture, and assumptions.
2. Model key flows and enumerate plausible misuse cases, authentication/authorization failures, elevation, tampering, disclosure, and availability risks.
3. Prioritize by credible attack prerequisites and impact, not generic severity labels alone.
4. Map each threat to preventive, detective, and recovery controls with identified owners and validation criteria.
5. Maintain traceability as design changes; distinguish implemented controls from recommended controls.

## Finding record

Every finding must include: identifier; title; status (confirmed, probable, or unverified); severity and rationale; affected component/version/file/line; trust boundary; prerequisites; evidence; impact; minimal fix; regression test; and any uncertainty. Never call a scan clean merely because no tool returned alerts.

