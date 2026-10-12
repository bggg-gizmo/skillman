# Codeman Orchestrator — specialist execution playbook

## Preconditions

Use for multi-module development, cross-disciplinary changes, complex audits, or requests requiring sequencing between Codeman skills.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Intake and scope control

1. Translate the exact request into independently testable acceptance criteria; distinguish requested modifications from context and identify protected behavior.
2. Determine repository, execution environment, authorization, deliverable format, and whether read-only GitHub access was explicitly requested. No unstated external access is presumed.
3. Create a traceability matrix connecting each requirement to owners, files, upstream dependencies, integration points, and verification evidence.
## Phase 2: Delegate by specialty, not by guesswork

1. Choose the smallest capable specialty set: architect for topology, guardian for preservation, coder/program for implementation, integrator for wiring, tester for verification, security for risk, release for packaging.
2. Assign one owner for each mutable file or shared interface; resolve overlapping edits before execution rather than allowing competing modifications.
3. Route contradictory recommendations through the operating contract and explicit user requirements. Do not silently simplify requirements to resolve a conflict.
## Phase 3: Establish dependency order

1. Sequence discovery, baselining, implementation, integration, verification, and delivery. Enforce prerequisites for migrations, public APIs, generated artifacts, and backward compatibility.
2. Hold a change until its contract, source-of-truth file, expected side effects, and validation method are understood.
3. When a dependent capability or tool is unavailable, continue independent authorized work and mark the blocked acceptance criterion unverified.
## Phase 4: Control implementation and handoffs

1. Require each work unit to report files touched, interfaces preserved, new behavior, unresolved risks, and tests executed.
2. Compare cross-component assumptions: payload shapes, database migrations, event ordering, auth boundaries, filenames, packaging locations, and version constraints.
3. Refuse silent feature removal and ensure the optional opening montage is sourced from the configured source repository when applicable and authorized.
## Phase 5: Integrate, gate, deliver

1. Combine work only after the integrator validates all registrations, call paths, packaging hooks, configs, and runtime entry points.
2. Check preservation against the baseline; verify requirement coverage and record executed evidence instead of treating planned tests as passed.
3. Deliver every requested complete artifact and a factual status matrix: implemented, verified, blocked, or failed, without concealing incomplete requirements.

## Required project deliverables

1. **Acceptance and preservation matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Module ownership and dependency map** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Integrated change set** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Test execution and risk ledger** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Final delivered artifact inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Claiming autonomous background agents or tool access not present.
- Treating a proposed workflow as an executed one.
- Combining inconsistent API assumptions across modules.
- Accepting a green unit test while the user-visible feature remains disconnected.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
