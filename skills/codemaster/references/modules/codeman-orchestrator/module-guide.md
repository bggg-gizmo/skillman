---
name: codeman-orchestrator
description: "Coordinate multiple Codeman specialties to deliver complete, integrated changes while protecting every existing function, feature, and interface. Use when the task involves orchestrator workflows."
---

# Codeman Orchestrator

## Activation and ownership

Use for multi-module development, cross-disciplinary changes, complex audits, or requests requiring sequencing between Codeman skills.

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

1. **Intake and scope control** — Translate the exact request into independently testable acceptance criteria; distinguish requested modifications from context and identify protected behavior.
2. **Delegate by specialty, not by guesswork** — Choose the smallest capable specialty set: architect for topology, guardian for preservation, coder/program for implementation, integrator for wiring, tester for verification, security for risk, release for packaging.
3. **Establish dependency order** — Sequence discovery, baselining, implementation, integration, verification, and delivery. Enforce prerequisites for migrations, public APIs, generated artifacts, and backward compatibility.
4. **Control implementation and handoffs** — Require each work unit to report files touched, interfaces preserved, new behavior, unresolved risks, and tests executed.
5. **Integrate, gate, deliver** — Combine work only after the integrator validates all registrations, call paths, packaging hooks, configs, and runtime entry points.

## Quality and integration gates

1. Inventory existing observable behavior and entry points before editing.
2. Identify affected consumers, contracts, data representations, configuration, assets, and error paths.
3. Make changes only within the requested scope; keep existing user work intact.
4. Complete every required import, registration, implementation branch, integration path, and regression test that the environment supports.
5. Check the final diff for unexpected deletions, renamed public interfaces, altered defaults, lost feature paths, or absent packaging resources.
6. Record each actual verification command and result. A planned, skipped, or unavailable test is **not passed**.
7. Provide all requested complete source or distributable files. Do not replace actual deliverables with summaries.

## Specialist handoffs

Other Codeman modules that may be relevant if installed: `codeman-architect`, `codeman-guardian`, `codeman-integrator`, `codeman-tester`, `codeman-release`. Do not assume they are installed, available as independent agents, or able to grant additional capabilities. This skill must still perform its own workflow when used alone.

## Deliverable standard

Create the concrete deliverables defined in the specialist playbook when applicable to the requested task. For every required check, document **passed**, **failed**, **not run**, or **not applicable**, with observed evidence. Distinguish user-authorized implementation changes from design-only recommendations. Never claim an unexecuted release, live deployment, network scan, GitHub action, or security validation as completed.

## Local repository and asset configuration

Read `references/local-configuration.md` when a task involves a repository, local machine settings, organization-specific sources, or an application startup montage. Do not assume any default account, repository, path, or asset from this public package. Do not create or commit local configuration unless explicitly requested.
