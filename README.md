<div align="center">

# SKILLMAN

### Modular engineering skills for AI coding agents

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Open_Standard-7C3AED?style=for-the-badge)](https://agentskills.io/specification)
[![Skill Count](https://img.shields.io/badge/Skills-41-0F766E?style=for-the-badge)](docs/CATALOG.md)
[![MIT License](https://img.shields.io/badge/License-MIT-2563EB?style=for-the-badge)](LICENSE)
[![Skillmanual](https://img.shields.io/badge/Docs-SKILLMANUAL-334155?style=for-the-badge)](SKILLMANUAL.md)

[![ChatGPT](https://img.shields.io/badge/ChatGPT-Skills-10A37F?logo=openai&logoColor=white)](docs/INSTALLATION.md#chatgpt)
[![Claude](https://img.shields.io/badge/Claude-Skills-D97757)](docs/INSTALLATION.md#claudeai-web)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Agent_Skills-8B5CF6)](docs/INSTALLATION.md#claude-code)
[![Codex](https://img.shields.io/badge/OpenAI_Codex-Agent_Skills-1E293B?logo=openai&logoColor=white)](docs/INSTALLATION.md#openai-codex-cli-and-ide)
[![Gemini CLI](https://img.shields.io/badge/Gemini_CLI-Agent_Skills-4285F4)](docs/INSTALLATION.md#google-gemini-cli)
[![Cursor](https://img.shields.io/badge/Cursor-Agent_Skills-111827)](docs/INSTALLATION.md#cursor)
[![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-Agent_Skills-181717?logo=github&logoColor=white)](docs/INSTALLATION.md#github-copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-Agent_Skills-475569)](docs/INSTALLATION.md#opencode)

**Background Gremlin Group**  
*Creating Unique Tools for Unique Individuals*

**41 installable skills** · **40 focused specialists** · **1 unified Codemaster**

[Get started](#get-started) · [Skillmanual](SKILLMANUAL.md) · [Install](docs/INSTALLATION.md) · [Skill catalog](docs/CATALOG.md) · [Evaluations](evals/README.md) · [Contribute](docs/CONTRIBUTING.md)

</div>

---

## Build complete systems. Keep their existing features.

Skillman is a public, portable suite of instruction-based agent skills for software development, security, testing, reverse engineering, infrastructure, and delivery. Each skill includes a reusable workflow and verification criteria. The **Codemaster** package combines all 40 specialties without requiring 40 separate installations.

Skills guide the agent; they do not grant tool permissions, install software, or guarantee successful execution. **No GitHub-credit-consuming operations** are authorized by these skills.

### Choose your setup

| Option | Best for | Install |
|---|---|---|
| **Codemaster** | Projects spanning multiple specialties | [Download Codemaster ZIP](upload-zips/codemaster.zip) |
| **Individual Codeman skills** | Narrow tasks and smaller skill footprints | [Browse all 40 ZIPs](upload-zips/) |
| **Offline collection** | Maintaining or distributing the entire set | [Download complete bundle](bundles/skillman-all-public-skills.zip) |

> **Important:** The complete collection ZIP is not one installable skill. Extract it and upload the individual skill ZIP you want, or install Codemaster alone.

## Get started

> **Coding agent skills, not artifact templates.** In ChatGPT, install them via **Plugins → Skills → Create → Upload from your computer**, **not `@Template Creator`**. The latter creates reusable document, presentation, and similar artifact templates.

1. Download the [Codemaster standalone ZIP](upload-zips/codemaster.zip) to get all 40 specialties inside one master skill, or select one from the [individual skill ZIPs](upload-zips/).
2. **ChatGPT or Claude web:** Upload one skill ZIP into the host's Skills manager.
3. **Local coding agent:** Install the **unpacked** `skills/codemaster/` directory into its skill discovery path. Do not install the complete collection ZIP as a single skill.
4. Activate Codemaster by name and ask for real integration and regression-test evidence.

| Host | Installation method | Full guide |
|---|---|---|
| **ChatGPT** | **Plugins → Skills → Create → Upload from your computer** (eligible accounts) | [ChatGPT](docs/INSTALLATION.md#chatgpt) |
| **Claude.ai** | **Customize → Skills → + → Create skill → Upload a skill** | [Claude web](docs/INSTALLATION.md#claudeai-web) |
| **Claude Code** | `.claude/skills/` or `~/.claude/skills/` | [Claude Code](docs/INSTALLATION.md#claude-code) |
| **OpenAI Codex** | `.agents/skills/` or `~/.agents/skills/` | [Codex](docs/INSTALLATION.md#openai-codex-cli-and-ide) |
| **Gemini CLI** | `.gemini/skills/` or `.agents/skills/` | [Gemini CLI](docs/INSTALLATION.md#google-gemini-cli) |
| **Cursor** | `.cursor/skills/` or `.agents/skills/` | [Cursor](docs/INSTALLATION.md#cursor) |
| **GitHub Copilot** | `.github/skills/` or `.agents/skills/` | [Copilot](docs/INSTALLATION.md#github-copilot) |
| **OpenCode** | `.opencode/skills/` or `.agents/skills/` | [OpenCode](docs/INSTALLATION.md#opencode) |

These badges and guides describe documented installation routes, **not vendor endorsements or proof of model-specific performance**. Refer to the [cross-agent installation guide](docs/INSTALLATION.md) for platform requirements, Windows PowerShell commands, official vendor sources, and troubleshooting.

```text
Use Codemaster to inspect this application, preserve every existing feature,
implement the requested change completely, verify its integration paths,
and report all tests actually executed and any unverified requirements.
```

Skills do **not** provide model tools, credentials, unrestricted execution, or free hosted compute. See the [Skillmanual](SKILLMANUAL.md) and [local configuration](docs/CONFIGURATION.md).

## Inside the collection

| Domain | Example specialties |
|---|---|
| Engineering | Core, Program, Coder, Guardian, Architect, Integrator, Auditor |
| Verification & delivery | Tester, Build Doctor, Recovery, Contracts, Release, Dependencies |
| Security | Security, Red, Blue, Fuzz Lab, Malware Lab, Detection Lab, Forensics, Reverse |
| Applications | Web, Desktop, API, Database, UI/UX, Performance |
| Operations & knowledge | Ops, GitHub, Repository Mapper, Research, Automation, Documentation |

The [complete catalog](docs/CATALOG.md) contains all 40 individual skill names and links. Every specialist has its own [`README.md`](skills/) and an installable ZIP. Codemaster scans a **compact 40-specialty routing index** and loads only the matching full playbooks, so all specialties are considered without automatically loading them all.

## Safeguards and quality

- **Feature preservation:** Existing functions, integrations, interfaces and behaviors are mandatory unless explicitly changed by the operator.
- **Complete implementation:** Avoid placeholders, pseudocode and silently omitted requested files; report inaccessible requirements rather than pretending they were implemented.
- **Project isolation:** Personal repos, startup assets and machine paths are not embedded; peers use optional [local configuration](docs/CONFIGURATION.md).
- **Transparent verification:** Packaging checks test archive integrity, while [agent evaluations](evals/README.md) must be run in a compatible agent environment to measure task performance. Results are not claimed where no agent run occurred.
- **No GitHub credits:** The skills prohibit metered GitHub execution and unapproved workflow-triggering writes.

### Development and verification

With Python 3.10+ at the repository root:

```bash
python tools/sync_shared.py --check
python tools/check_routing.py
python tools/build_packages.py
python tools/audit_distribution.py
python tools/verify_packages.py
python -m unittest discover -s evals -p 'test_*.py' -v
```

Shared requirements have a single canonical source: [`shared/operating-contract.md`](shared/operating-contract.md). The build ships identical copies in every standalone skill so each ZIP remains self-contained. [Evaluation instructions](evals/README.md) explain how to collect baseline-versus-skill results with an actual agent.

## Project map

| Location | Contents |
|---|---|
| [`skills/`](skills/) | 41 installable skill source directories; each with its own README |
| [`upload-zips/`](upload-zips/) | Individual installable skill archives |
| [`bundles/`](bundles/) | Complete offline distribution |
| [`SKILLMANUAL.md`](SKILLMANUAL.md) | Full user and maintainer manual |
| [`docs/INSTALLATION.md`](docs/INSTALLATION.md) | Cross-agent installation, invocation, and vendor documentation |
| [`evals/`](evals/) | Reproducible task fixtures, agent-result scorer, evaluation methodology |
| [`shared/`](shared/) | Single source of truth for the mandatory operating contract |
| [`tools/`](tools/) | Local rebuild, audit, ZIP validation and routing checks |
| [`docs/releases/`](docs/releases/) | Versioned release notes and GitHub release procedure |

## Community, policy and license

- Contributions: [Contributing](docs/CONTRIBUTING.md) · [Security reporting](docs/SECURITY.md)
- Pull-request creation is presently restricted to collaborators on the GitHub repository. See [contribution policy](docs/CONTRIBUTING.md); external contributors can open an issue when permitted.
- GitHub versioned Releases require a separate release-publishing step. The source archives here are published independently of a GitHub Release.
- **License:** [MIT](LICENSE). Copyright © 2026 Background Gremlin Group.

---

<div align="center">

**Background Gremlin Group**  
*Creating Unique Tools for Unique Individuals*

[Skillmanual](SKILLMANUAL.md) · [Catalog](docs/CATALOG.md) · [License](LICENSE)

</div>
