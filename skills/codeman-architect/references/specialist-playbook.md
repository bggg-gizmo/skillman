# Codeman Architect — specialist execution playbook

## Preconditions

Use for system design, component decomposition, complex refactors, cross-service changes, or architecture decisions that must preserve backward compatibility.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Discover the deployed reality

1. Inspect actual entry points, processes, packages, data stores, schemas, external APIs, infrastructure definitions, and tests instead of inferring architecture from directory names.
2. Diagram runtime calls, asynchronous events, authentication trust boundaries, persistence and cache paths, and failure propagation.
3. Record existing SLA/SLO assumptions, traffic shape, consistency requirements, compatibility contracts, and security controls when present.
## Phase 2: Express constraints and decision drivers

1. Separate functional requirements from latency, throughput, availability, operability, security, deployment, and maintainability constraints.
2. Identify invariants and forbidden changes including all pre-existing functions and user journeys.
3. Explicitly document the risks, migration effort, and operational overhead of plausible alternatives.
## Phase 3: Design interfaces and responsibility boundaries

1. Define component ownership, public interfaces, version negotiation, error semantics, retry/idempotency behavior, transactional boundaries, and observability hooks.
2. Plan schema transitions, feature rollout sequencing, backward compatibility, and failure containment before implementation.
3. Integrate existing shared assets such as the the configured asset repository opening montage instead of replacing them with new visuals.
## Phase 4: Translate design into buildable work

1. Map each interface to its implementing module, consumer, configuration, tests, and deployment artifact.
2. Produce a phased implementation order that leaves the application runnable between phases; include dual-read/write strategies for compatible migrations where needed.
3. Record architecture decisions with rejected alternatives and their measurable tradeoffs, not subjective preferences alone.
## Phase 5: Validate architectural fit

1. Review the proposed design against current source code and contracts; identify incompatible assumptions and cyclic dependencies.
2. Require load, failure-mode, contract, and security verification for critical paths and explicit rollbacks where the actual system supports them.
3. Classify conclusions as implemented evidence, design proposal, or unresolved risk to avoid confusing a diagram with functioning software.

## Required project deliverables

1. **Component and data-flow diagrams** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Architecture decision records** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Interface and failure-mode specification** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Incremental migration plan** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Architectural verification matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Inventing uninspected infrastructure.
- Specifying a rewrite without a migration path.
- Ignoring retry/idempotency semantics.
- Treating diagrams as proof of integration.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
