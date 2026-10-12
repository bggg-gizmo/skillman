---
name: codemaster
description: Coordinate the complete 40-module Codeman engineering and cybersecurity skill suite from one self-contained skill. Use for software engineering, coding, auditing, architecture, integration, security, testing, deployment preparation, research, and cross-specialty work.
---

# Codemaster — portable, self-contained master skill

## Activation and scope

Codemaster is the **single entry point** into the entire suite. It packages all 40 specialist skill instruction files and their complete references under `references/modules/`; **installing the 40 individual skills is optional** when Codemaster is installed. It does not create multiple autonomous agents, grant tools, or run 40 independent executions.

Read `references/operating-contract.md` and apply it on every task. Do not infer account, repository, machine, montage asset, access permission, or test results. Read `references/local-configuration.md` when per-project configuration is relevant. Do not initiate GitHub-credit-consuming operations, including indirectly triggering GitHub Actions or metered workflows.

## Mandatory coordination procedure

1. **Cheap complete inventory (mandatory):** Read `references/module-routing.json`. Assess **all 40** descriptions and signals for applicability without loading every full playbook. Use `references/module-index.md` to inspect detailed paths and coverage when needed. Apply `codeman-core` on every task; also select `codeman-guardian` and `codeman-tester` for every code-modification task, whether or not keywords match. Mark unrelated modules *not applicable*, not *executed*. Never skip any of the 40 relevance decisions.
2. **Load only applicable complete playbooks:** Read `references/modules/<skill-name>/module-guide.md` and its required references only for the specialties selected in step 1. Never load all 40 full guides merely because they are bundled. Reselect when new project facts implicate another specialty. Do not treat a one-line routing signal as a substitute for an applicable complete guide. Preserve every applicable specialist requirement.
3. **Establish facts and permissions:** Inspect the actual files, repository, application, existing changes, test environment, and available tools. Separate verified facts from assumptions. Request and use external access only within authorization and host constraints.
4. **Create a preservation baseline:** Inventory existing functions, interfaces, behavior, configuration, assets and integration paths. Guard pre-existing user work. Identify tests and evidence that can detect regression.
5. **Orchestrate the work:** Determine ordering and responsibility among relevant specialties. Architect/Mapper and Guardian precede invasive edits; Coder/Program/Domain skills implement; Integrator connects call paths; Tester/Auditor/Security verify; Release/Documentation finish requested deliverables. Do not replace requested complete files with summaries.
6. **Integrate and verify:** Validate imports, exports, packaging, routes, schemas, call sites, security boundaries, error paths and preserved features. Run only the tests actually available and record outcomes, failures, and skipped checks.
7. **Delivery gate:** Show a requirement-by-requirement result, complete requested source/artifacts, diff scope, actual executed checks, known limitations, and any unresolved risks. No automatic feature removal, unwarranted simplification, or unverified no-regression guarantee.

## Priority, incompatibility, and safety

Higher-priority system requirements and permitted access always take precedence. When specialist instructions conflict, enforce the common operating contract, user-approved scope, and measurable preservation criteria; identify unresolved conflicts instead of inventing a resolution. Read-only security analysis does not authorize mutation or deployment. Only claim a tool, scan, test, build, push, or release when it actually ran.

## Efficiency and coverage contract

Routing considers all 40 specialists, but **does not activate or preload all 40**. Apply the mandatory contract, preservation, integration and test requirements regardless of selection. Read full references when the specific task requires them. Log selected specialties, briefly note material exclusions, and re-evaluate on scope changes. This reduces unnecessary context use without dropping coverage. `module-routing.json` is the compact routing source; `module-index.md` remains the human-readable complete index.

## Module ownership

Specialist reference packages are **snapshots** of the 40 public Codeman modules. Update Codemaster's bundled snapshot together with the individual modules when revising the suite, then rebuild and verify archives. An install of Codemaster on its own works without other Codeman installations; installing individual modules remains useful for narrower tasks.
