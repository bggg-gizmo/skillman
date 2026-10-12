# Codeman Detection Lab — specialist execution playbook

## Preconditions

Use for building detections, hunting hypotheses, log mapping, rule regression tests, and false-positive tuning.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Define detection intent and telemetry

1. State attacker technique or policy violation, observable behavior, source field names, expected event IDs, retention, and known collection gaps.
2. Map native logs into the selected rule schema; verify timestamp semantics, process identity, network tuples, command-line normalization, and tenant context.
3. Keep environment-specific constants separate from behavioral invariants when the detection language supports them.
## Phase 2: Implement concrete detections

1. Write valid complete rule syntax with names, logsource/metadata, conditions, filters, and severity appropriate to the platform.
2. Avoid relying solely on brittle IOCs when behavior-based signals are available; avoid wide wildcards that explode noise.
3. Ensure every indicator maps to real collected fields and that rule syntax survives the intended backend conversion.
## Phase 3: Construct test fixtures

1. Prepare positive samples representing the target behavior, adversarially varied encodings, expected normal activity, and known confusing benign events.
2. Test Sigma query conversion or YARA compilation, Suricata rule parsing, and event matching with versioned fixture corpora where tooling exists.
3. Validate both true-positive and false-positive behavior; mark absent datasets as unverified rather than reporting accuracy metrics.
## Phase 4: Tune operational quality

1. Estimate event volume, signal specificity, alert latency, coverage, schema drift, and triage context using actual available data.
2. Add justified filters only after examining the affected normal behavior and risk of suppressing true positives.
3. Define alert enrichment, response ownership, documentation, and maintenance triggers.
## Phase 5: Deliver detections with proof

1. Supply complete deployable rule files, test input files, parse/compile results, and implementation notes.
2. Document the collection prerequisites, known bypasses, false-positive conditions, and testing environment.
3. Do not deploy to production detection infrastructure without explicit authorization.

## Required project deliverables

1. **Fully formed rule files** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Telemetry and field mapping** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Positive/negative detection fixture corpus** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Rule compilation and precision evidence** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Tuning and deployment prerequisites** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Inferring data collection from SIEM vendor names.
- Calling untested rules production-ready.
- Using a hash-only IOC without context.
- Introducing broad suppression filters to hide alert volume.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
