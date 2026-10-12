---
name: codeman-repository-mapper
description: "Build precise, navigable maps of large codebases: components, functions, call graphs, API boundaries, features, configuration, and dependency ownership. Use when the task involves repository mapper workflows."
---

# Codeman Repository Mapper

## Activation and ownership

Use to onboard to an unfamiliar repository, find feature implementations, evaluate change impact, or build a stable engineering inventory.

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

1. **Enumerate what actually exists** — Identify source roots, workspaces, generated code, vendored dependencies, third-party assets, test roots, and build/deployment manifests.
2. **Build symbol and component inventories** — Catalog classes, functions, exported symbols, CLI commands, HTTP routes, event consumers, scheduled jobs, screens, plugins, and configuration keys.
3. **Reconstruct runtime architecture** — Trace request and event paths from entry points through services, storage, queues, outbound calls, and observable outputs.
4. **Compute change-impact views** — For each named function or feature, list direct and indirect callers, dependent schemas, public contracts, tests, and operational concerns.
5. **Publish a trustworthy map** — Produce file-to-feature, symbol-to-caller, API-to-implementation, and feature-to-test tables with concrete paths.

## Quality and integration gates

1. Inventory existing observable behavior and entry points before editing.
2. Identify affected consumers, contracts, data representations, configuration, assets, and error paths.
3. Make changes only within the requested scope; keep existing user work intact.
4. Complete every required import, registration, implementation branch, integration path, and regression test that the environment supports.
5. Check the final diff for unexpected deletions, renamed public interfaces, altered defaults, lost feature paths, or absent packaging resources.
6. Record each actual verification command and result. A planned, skipped, or unavailable test is **not passed**.
7. Provide all requested complete source or distributable files. Do not replace actual deliverables with summaries.

## Specialist handoffs

Other Codeman modules that may be relevant if installed: `codeman-architect`, `codeman-guardian`, `codeman-contracts`, `codeman-auditor`. Do not assume they are installed, available as independent agents, or able to grant additional capabilities. This skill must still perform its own workflow when used alone.

## Deliverable standard

Create the concrete deliverables defined in the specialist playbook when applicable to the requested task. For every required check, document **passed**, **failed**, **not run**, or **not applicable**, with observed evidence. Distinguish user-authorized implementation changes from design-only recommendations. Never claim an unexecuted release, live deployment, network scan, GitHub action, or security validation as completed.

## Local repository and asset configuration

Read `references/local-configuration.md` when a task involves a repository, local machine settings, organization-specific sources, or an application startup montage. Do not assume any default account, repository, path, or asset from this public package. Do not create or commit local configuration unless explicitly requested.
