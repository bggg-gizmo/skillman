---
name: codeman-protocol-lab
description: "Analyze and validate network or binary protocols, parsers, framing, state machines, serializers, and safe interoperability tests. Use when the task involves protocol lab workflows."
---

# Codeman Protocol Lab

## Activation and ownership

Use for protocol implementation, packet decoding, compatibility testing, troubleshooting, or scoped local protocol resilience assessment.

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

1. **Establish protocol authority** — Identify published RFC/specification, local captures, implementation source, negotiated versions, transport, and authorized endpoints.
2. **Model framing and state** — Specify byte order, length fields, delimiters, checksums, encoding, compression, escaping, retransmission, and fragmentation/reassembly rules.
3. **Implement robust codecs** — Validate all sizes and offsets before allocation or access, reject malformed length prefixes, and enforce resource/time limits.
4. **Validate interoperability and resilience** — Run byte-level round-trip tests, known-answer vectors, malformed/truncated packet cases, replay-resistant behavior where relevant, and cross-version tests.
5. **Deliver protocol evidence** — Publish frame layouts, state transitions, decoder edge cases, compatibility behavior, and exact test evidence.

## Quality and integration gates

1. Inventory existing observable behavior and entry points before editing.
2. Identify affected consumers, contracts, data representations, configuration, assets, and error paths.
3. Make changes only within the requested scope; keep existing user work intact.
4. Complete every required import, registration, implementation branch, integration path, and regression test that the environment supports.
5. Check the final diff for unexpected deletions, renamed public interfaces, altered defaults, lost feature paths, or absent packaging resources.
6. Record each actual verification command and result. A planned, skipped, or unavailable test is **not passed**.
7. Provide all requested complete source or distributable files. Do not replace actual deliverables with summaries.

## Specialist handoffs

Other Codeman modules that may be relevant if installed: `codeman-program`, `codeman-fuzz-lab`, `codeman-contracts`, `codeman-red`. Do not assume they are installed, available as independent agents, or able to grant additional capabilities. This skill must still perform its own workflow when used alone.

## Deliverable standard

Create the concrete deliverables defined in the specialist playbook when applicable to the requested task. For every required check, document **passed**, **failed**, **not run**, or **not applicable**, with observed evidence. Distinguish user-authorized implementation changes from design-only recommendations. Never claim an unexecuted release, live deployment, network scan, GitHub action, or security validation as completed.

## Local repository and asset configuration

Read `references/local-configuration.md` when a task involves a repository, local machine settings, organization-specific sources, or an application startup montage. Do not assume any default account, repository, path, or asset from this public package. Do not create or commit local configuration unless explicitly requested.
