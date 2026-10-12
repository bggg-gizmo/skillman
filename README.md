# Skillman — Codeman Skills

**Background Gremlin Group — Creating Unique Tools for Unique Individuals**

[Skillmanual](SKILLMANUAL.md) · [Codemaster](skills/codemaster/) · [Complete Public Bundle](bundles/skillman-all-public-skills.zip)

**41 public, independently packaged skills: 40 Codeman specialties plus one self-contained Codemaster**, prepared for public use. This repository contains the complete editable `SKILL.md` source for each skill, plus individually packaged ZIP archives for import into compatible agent interfaces.

These are reusable **agent skills**, not preinstalled software or autonomous access grants. They guide an agent's workflow when activated and when the relevant files, tools, and permissions are available.

## Quick start

1. Read the [Skillmanual](SKILLMANUAL.md) and browse the [catalog](docs/CATALOG.md). Install [Codemaster](upload-zips/codemaster.zip) for one all-in-one skill, or choose any specialty.
2. Download an individual skill ZIP from [`upload-zips/`](upload-zips/) or [the entire public bundle](bundles/skillman-all-public-skills.zip). **Do not upload the entire bundle as a single skill.**
3. In a compatible ChatGPT Skills interface, use the available **Create / Upload** option to install one ZIP per skill. The exact UI and availability depend on the client and account.
4. For other compatible local agent environments, follow that agent's documented skill directory/import mechanism and use the unzipped directory under [`skills/`](skills/). A skill does not automatically install compilers, security tools, or connectors.
5. Invoke the skill by name or describe a task matching its activation description. For example: **"Use Codeman Guardian and Codeman Tester to inventory the existing behavior, implement this change completely, and verify no regressions."**

## What is covered

| Area | Skills |
| --- | --- |
| Core coding | Core, Program, Coder, Project, Guardian, Architect, Orchestrator, Integrator |
| Assurance and delivery | Tester, Auditor, Build Doctor, Release, Recovery, Contracts, Repository Mapper, Documentation |
| Security | Security, Red, Blue, Reverse, Fuzz Lab, Protocol Lab, Malware Lab, Detection Lab, Forensics, Supply Chain |
| Platforms and operations | Web, Ops, Desktop, Database, API, UI/UX, Performance, Dependencies, Observability, Migration, Automation |
| Repository and knowledge | GitHub, Knowledge, Research |

The [catalog](docs/CATALOG.md) lists the **40 standalone specialties**. **Codemaster** is a separate skill that embeds all 40 complete public specialty reference packages and can be installed on its own.

## Complete implementation and preservation requirements

Every skill contains `references/operating-contract.md`, which requires preservation of existing functions and features, complete implementations and integration, targeted regression checks, accurate reporting of tests actually run, and authorization for changes. No skill may silently remove or simplify existing behavior. These instructions guide work; they cannot guarantee an absence of bugs or bypass unavailable test environments.

The shared contract also forbids GitHub-credit-consuming actions, including workflows and other metered GitHub execution. A GitHub connector is used only if the current operator expressly requests it. Remote writes that may trigger metered automation must not be run without a confirmed non-metered path.

## Portable configuration — no creator-specific account or repo

**No public skill is preconfigured with an author's GitHub account, private or personal repositories, filesystem paths, or application intro montage.** The original author-specific montage reference was removed from the public edition.

If your own project needs repository pointers or a startup montage:

1. Copy [`config.example.json`](config.example.json) into your own project's `.codeman/config.json`.
2. Enter the repositories and existing assets relevant to **your** project; if no asset is required, leave the configuration unpopulated.
3. Keep the resulting `.codeman/config.json` private (the [`.gitignore`](.gitignore) ignores this file). Do not store credentials inside it.
4. The skill reads the configuration only if your agent has access to that project and your request authorizes the related operation.

See [configuration details](docs/CONFIGURATION.md). A project-specific configuration is optional; skills remain usable without it.

## Repository layout

- [`skills/codemaster/`](skills/codemaster/) — the complete master skill and its references to all 40 specialties
- [`upload-zips/codemaster.zip`](upload-zips/codemaster.zip) — one standalone installable master skill
- [`bundles/`](bundles/) — public all-skills bundle plus bundle README
- [`SKILLMANUAL.md`](SKILLMANUAL.md) — complete operator, configuration and maintenance guide
- Every specialist directory in [`skills/`](skills/) contains its own README.

Every skill includes complete instructions and all its references. The source and installable ZIP of each skill are available directly from this repository.

| Skill source directory | Individual ZIP |
| --- | --- |
| [`skills/codeman-api/`](skills/codeman-api/) | [`codeman-api.zip`](upload-zips/codeman-api.zip) |
| [`skills/codeman-architect/`](skills/codeman-architect/) | [`codeman-architect.zip`](upload-zips/codeman-architect.zip) |
| [`skills/codeman-auditor/`](skills/codeman-auditor/) | [`codeman-auditor.zip`](upload-zips/codeman-auditor.zip) |
| [`skills/codeman-automation/`](skills/codeman-automation/) | [`codeman-automation.zip`](upload-zips/codeman-automation.zip) |
| [`skills/codeman-blue/`](skills/codeman-blue/) | [`codeman-blue.zip`](upload-zips/codeman-blue.zip) |
| [`skills/codeman-build-doctor/`](skills/codeman-build-doctor/) | [`codeman-build-doctor.zip`](upload-zips/codeman-build-doctor.zip) |
| [`skills/codeman-coder/`](skills/codeman-coder/) | [`codeman-coder.zip`](upload-zips/codeman-coder.zip) |
| [`skills/codeman-contracts/`](skills/codeman-contracts/) | [`codeman-contracts.zip`](upload-zips/codeman-contracts.zip) |
| [`skills/codeman-core/`](skills/codeman-core/) | [`codeman-core.zip`](upload-zips/codeman-core.zip) |
| [`skills/codeman-database/`](skills/codeman-database/) | [`codeman-database.zip`](upload-zips/codeman-database.zip) |
| [`skills/codeman-dependencies/`](skills/codeman-dependencies/) | [`codeman-dependencies.zip`](upload-zips/codeman-dependencies.zip) |
| [`skills/codeman-desktop/`](skills/codeman-desktop/) | [`codeman-desktop.zip`](upload-zips/codeman-desktop.zip) |
| [`skills/codeman-detection-lab/`](skills/codeman-detection-lab/) | [`codeman-detection-lab.zip`](upload-zips/codeman-detection-lab.zip) |
| [`skills/codeman-documentation/`](skills/codeman-documentation/) | [`codeman-documentation.zip`](upload-zips/codeman-documentation.zip) |
| [`skills/codeman-forensics/`](skills/codeman-forensics/) | [`codeman-forensics.zip`](upload-zips/codeman-forensics.zip) |
| [`skills/codeman-fuzz-lab/`](skills/codeman-fuzz-lab/) | [`codeman-fuzz-lab.zip`](upload-zips/codeman-fuzz-lab.zip) |
| [`skills/codeman-github/`](skills/codeman-github/) | [`codeman-github.zip`](upload-zips/codeman-github.zip) |
| [`skills/codeman-guardian/`](skills/codeman-guardian/) | [`codeman-guardian.zip`](upload-zips/codeman-guardian.zip) |
| [`skills/codeman-integrator/`](skills/codeman-integrator/) | [`codeman-integrator.zip`](upload-zips/codeman-integrator.zip) |
| [`skills/codeman-knowledge/`](skills/codeman-knowledge/) | [`codeman-knowledge.zip`](upload-zips/codeman-knowledge.zip) |
| [`skills/codeman-malware-lab/`](skills/codeman-malware-lab/) | [`codeman-malware-lab.zip`](upload-zips/codeman-malware-lab.zip) |
| [`skills/codeman-migration/`](skills/codeman-migration/) | [`codeman-migration.zip`](upload-zips/codeman-migration.zip) |
| [`skills/codeman-observability/`](skills/codeman-observability/) | [`codeman-observability.zip`](upload-zips/codeman-observability.zip) |
| [`skills/codeman-ops/`](skills/codeman-ops/) | [`codeman-ops.zip`](upload-zips/codeman-ops.zip) |
| [`skills/codeman-orchestrator/`](skills/codeman-orchestrator/) | [`codeman-orchestrator.zip`](upload-zips/codeman-orchestrator.zip) |
| [`skills/codeman-performance/`](skills/codeman-performance/) | [`codeman-performance.zip`](upload-zips/codeman-performance.zip) |
| [`skills/codeman-program/`](skills/codeman-program/) | [`codeman-program.zip`](upload-zips/codeman-program.zip) |
| [`skills/codeman-project/`](skills/codeman-project/) | [`codeman-project.zip`](upload-zips/codeman-project.zip) |
| [`skills/codeman-protocol-lab/`](skills/codeman-protocol-lab/) | [`codeman-protocol-lab.zip`](upload-zips/codeman-protocol-lab.zip) |
| [`skills/codeman-recovery/`](skills/codeman-recovery/) | [`codeman-recovery.zip`](upload-zips/codeman-recovery.zip) |
| [`skills/codeman-red/`](skills/codeman-red/) | [`codeman-red.zip`](upload-zips/codeman-red.zip) |
| [`skills/codeman-release/`](skills/codeman-release/) | [`codeman-release.zip`](upload-zips/codeman-release.zip) |
| [`skills/codeman-repository-mapper/`](skills/codeman-repository-mapper/) | [`codeman-repository-mapper.zip`](upload-zips/codeman-repository-mapper.zip) |
| [`skills/codeman-research/`](skills/codeman-research/) | [`codeman-research.zip`](upload-zips/codeman-research.zip) |
| [`skills/codeman-reverse/`](skills/codeman-reverse/) | [`codeman-reverse.zip`](upload-zips/codeman-reverse.zip) |
| [`skills/codeman-security/`](skills/codeman-security/) | [`codeman-security.zip`](upload-zips/codeman-security.zip) |
| [`skills/codeman-supply-chain/`](skills/codeman-supply-chain/) | [`codeman-supply-chain.zip`](upload-zips/codeman-supply-chain.zip) |
| [`skills/codeman-tester/`](skills/codeman-tester/) | [`codeman-tester.zip`](upload-zips/codeman-tester.zip) |
| [`skills/codeman-ui-ux/`](skills/codeman-ui-ux/) | [`codeman-ui-ux.zip`](upload-zips/codeman-ui-ux.zip) |
| [`skills/codeman-web/`](skills/codeman-web/) | [`codeman-web.zip`](upload-zips/codeman-web.zip) |

Other repository files: [`config.example.json`](config.example.json), [`docs/CONFIGURATION.md`](docs/CONFIGURATION.md), [`docs/SECURITY.md`](docs/SECURITY.md), [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md), [`docs/CATALOG.md`](docs/CATALOG.md), [`tools/build_packages.py`](tools/build_packages.py), [`tools/audit_distribution.py`](tools/audit_distribution.py), [`tools/verify_packages.py`](tools/verify_packages.py), [`MANIFEST.json`](MANIFEST.json), and [`SHA256SUMS`](SHA256SUMS).

## Verify or rebuild locally

Use Python 3.10 or later. No third-party packages, network calls, remote workflows, or GitHub credits are required.

```bash
python tools/build_packages.py
python tools/audit_distribution.py
python tools/verify_packages.py
```

`build_packages.py` creates deterministic standalone archives and a complete public bundle from the source under `skills/` and regenerates the integrity manifest. The audit checks files and ZIP members for known personal/account identifiers and credentials. The verification checks names, references, ZIP integrity, deterministic source-to-archive equivalence, and SHA-256 digests. Do not interpret passing these checks as proof of security, runtime functionality, or flawless future application modifications.

## Maintenance and use

- Read [contribution instructions](docs/CONTRIBUTING.md) before submitting a change.
- Read [privacy and security guidance](docs/SECURITY.md) and [publication guidance](docs/PUBLISHING.md) before publishing a release.
- **No software license is assigned in this package.** The repository owner should explicitly select and add a suitable license before encouraging downstream redistribution, modification, and reuse.
- Original (private/personalized) archives are **not** included in this public distribution.
