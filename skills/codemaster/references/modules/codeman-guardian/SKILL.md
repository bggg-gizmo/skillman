---
name: codeman-guardian
description: "Preserve all existing functions, application features, contracts, and runtime behavior through baseline inventory, change impact analysis, and rigorous regression gates. Use when the task involves guardian workflows."
---

# Codeman Guardian

## Activation and ownership

Use before and after modifying an existing codebase, especially when the user requires no feature loss, no regression, or complete implementation.

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

1. **Create an evidence-backed baseline** — Record repository status and tracked/untracked changes; exclude secrets from outputs and never overwrite pre-existing user work.
2. **Determine blast radius** — Trace changed symbols to callers, import sites, event subscribers, serializers, schemas, migrations, build outputs, and deployment/configuration paths.
3. **Enforce preservation during edits** — Perform minimal scoped changes, retain public interfaces and semantics, and block unauthorized deletion, renaming, rewriting, or removal of integrations.
4. **Verify behavior after changes** — Run the pre-change baseline test set and new focused tests on the edited tree where the environment permits.
5. **Issue preservation verdict** — Classify each monitored feature as preserved and verified, preserved but unverified, changed with authorization, failed, or unknown.

## Quality and integration gates

1. Inventory existing observable behavior and entry points before editing.
2. Identify affected consumers, contracts, data representations, configuration, assets, and error paths.
3. Make changes only within the requested scope; keep existing user work intact.
4. Complete every required import, registration, implementation branch, integration path, and regression test that the environment supports.
5. Check the final diff for unexpected deletions, renamed public interfaces, altered defaults, lost feature paths, or absent packaging resources.
6. Record each actual verification command and result. A planned, skipped, or unavailable test is **not passed**.
7. Provide all requested complete source or distributable files. Do not replace actual deliverables with summaries.

## Specialist handoffs

Other Codeman modules that may be relevant if installed: `codeman-repository-mapper`, `codeman-contracts`, `codeman-tester`, `codeman-recovery`. Do not assume they are installed, available as independent agents, or able to grant additional capabilities. This skill must still perform its own workflow when used alone.

## Deliverable standard

Create the concrete deliverables defined in the specialist playbook when applicable to the requested task. For every required check, document **passed**, **failed**, **not run**, or **not applicable**, with observed evidence. Distinguish user-authorized implementation changes from design-only recommendations. Never claim an unexecuted release, live deployment, network scan, GitHub action, or security validation as completed.

## Local repository and asset configuration

Read `references/local-configuration.md` when a task involves a repository, local machine settings, organization-specific sources, or an application startup montage. Do not assume any default account, repository, path, or asset from this public package. Do not create or commit local configuration unless explicitly requested.
