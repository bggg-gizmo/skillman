# Codeman Blue — specialist playbooks

Use this reference when the request involves defensive detections and incident investigation tooling. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** detection engineering, Sigma/YARA rules, incident-response tooling, forensic parsers.

## Detection engineering

1. Define the behavior to detect, threat hypothesis, coverage objective, relevant ATT&CK techniques if supportable, and required log sources.
2. Enumerate event IDs, field names, normalization, collection prerequisites, ingestion delays, and expected data loss.
3. Write detection logic that encodes behavior rather than unstable superficial indicators when possible.
4. Build positive and benign-negative fixtures, test against representative telemetry, and tune false positives without suppressing meaningful coverage.
5. Provide rule version, environment assumptions, deployment requirements, triage instructions, and known blind spots.

## Sigma rules

1. Inspect logsource category/product/service and the target SIEM backend field mappings.
2. Write valid Sigma YAML with stable detection identifiers, selectors, condition, descriptive metadata, and field names grounded in the actual log schema.
3. Validate parser/schema with the available supported Sigma tooling; test conversion to the intended backend and review semantic fidelity.
4. Test known-good detections and known-benign events; document required ingestion filters and alert thresholds.
5. Do not assume Sigma conversion is universal: document unsupported modifiers or mapping differences.

## YARA rules

1. Define file/memory scope and feature provenance; select robust strings, hex sequences, metadata, and boolean constraints.
2. Use distinctive identifiers and contextual conditions to avoid matching generic libraries or legitimate software.
3. Keep file-size/PE/ELF/module assumptions compatible with the YARA version and extensions available.
4. Run compilation and scan tests against representative malicious samples and clean corpora when they are available; note false-positive exposure.
5. Provide sample hashes and expected match behavior without embedding sensitive samples in deliverables.

## Incident-response tooling

1. Identify the collection objective, endpoints, permissions, evidence handling, retention, output formats, and live-response side effects.
2. Favor read-only collection, record acquisition time in UTC, capture source host identity and tool version, and preserve metadata.
3. Make scripts robust to missing permissions, locked files, partial results, retries, locale differences, and interrupted runs.
4. Log exactly what was collected and what failed without storing plaintext credentials or unneeded personal content.
5. Test on fixtures or approved endpoints and document operational permissions and impact.

## Forensic parsers

1. Define the evidence format, magic/header versions, byte order, alignment, timestamp encoding, character encoding, and corruption cases.
2. Preserve original bytes, offsets, checksums, and provenance; do not silently normalize away potentially probative data.
3. Parse incrementally and bounds-check lengths and offsets; represent malformed records as evidence rather than guessing missing values.
4. Normalize timestamps explicitly with timezone/source semantics and keep original raw values alongside parsed fields.
5. Test valid, truncated, malformed, adversarial, and cross-version fixtures and round-trip invariants where meaningful.

## Defensive handoff

Provide rule/parser version, input and output schema, test fixtures used, source coverage, expected alerts or records, known false positives/negatives, operational deployment notes, and clear distinction between evaluated and unevaluated datasets.

