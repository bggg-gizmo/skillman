<div align="center">

# SKILLMAN

### Modular engineering skills for AI coding agents

**Background Gremlin Group**  
*Creating Unique Tools for Unique Individuals*

**41 installable skills** · **40 focused specialists** · **1 unified Codemaster**

[Get started](#get-started) · [Skillmanual](SKILLMANUAL.md) · [Skill catalog](docs/CATALOG.md) · [Evaluations](evals/README.md) · [Contribute](docs/CONTRIBUTING.md)

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

1. Download `codemaster.zip` above or a specialty ZIP from [`upload-zips/`](upload-zips/).
2. In a compatible skill-enabled agent interface, select **Create / Upload** and choose that single ZIP. For local agent runtimes, install the corresponding directory under [`skills/`](skills/) using your host's documented process.
3. Provide project sources or authorized repository access. The skills do **not** include any individual's credentials, repositories, or local machine configuration.
4. Ask the agent to activate Codemaster or a specialist, then require an implementation, integration checks and evidence from tests it actually ran.

```text
Use Codemaster to inspect this application, preserve every existing feature,
implement the requested change completely, verify its integration paths,
and report all tests actually executed and any unverified requirements.
```

See the detailed [SKILLMANUAL](SKILLMANUAL.md) for individual installation, project settings, workflow selection, troubleshooting, and maintenance.

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
