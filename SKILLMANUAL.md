# SKILLMANUAL — Skillman User, Configuration, and Maintainer Manual

**Published by Background Gremlin Group — Creating Unique Tools for Unique Individuals**

This manual documents the public Codeman skill collection: 40 standalone specialties plus **Codemaster**, a single self-contained master skill that bundles all 40. The original personalized operator edition is not distributed here.

## 1. Understand the format

An agent skill consists of a directory containing `SKILL.md`, optional supporting references, and optional scripts/assets. The frontmatter declares `name` and `description`; the Markdown body gives instructions and applicability. Installing a skill does **not** automatically install a compiler, create permissions, grant GitHub access, run a security scanner, or bypass safety checks.

The source of truth is under `skills/<skill-name>/`. Each ZIP in `upload-zips/` reproduces the matching skill directory and its references under a single top-level folder. `bundles/skillman-all-public-skills.zip` is the **entire collection**, not an individual skill to upload directly.

## 2. Decide which installation style you want

**Codemaster only**: Install `upload-zips/codemaster.zip`. Codemaster bundles all 40 specialist instruction and reference trees internally. This is best for broad, multi-language, cross-domain projects. It evaluates all 40 modules for relevance; it does not claim to launch 40 agents or run every test.

**Individual specialties**: Install any subset of the other 40 ZIPs. Every specialist retains the public operating contract and works independently, even when Codemaster and Core are absent. This is best when you want narrow triggering or to minimize skill footprint.

**Source directory**: In an agent runtime that supports local skills, copy one or more complete folders from `skills/` to the runtime's documented skill installation directory. Never flatten a folder or separate `SKILL.md` from its references.

## 3. Install in ChatGPT or another compatible host

1. Download the selected standalone ZIP under `upload-zips/`. Do not select `bundles/` for single-skill upload.
2. Open the host's Skills manager and choose Create/Upload (wording and availability vary by client and account).
3. Select the ZIP. Confirm the skill name, description, and visibility. If updating an existing skill, follow the host's update workflow.
4. Ask the assistant to use the skill by name and provide the relevant project files or authorized connector links.
5. Confirm the result from the actual tests and artifacts, not just a claim that a skill was activated.

Examples: `Use Codeman Guardian and Codeman Tester to implement a change with regression checks.` Or `Use Codemaster to inspect, implement, integrate and verify this application update without removing any existing function.`

## 4. How Codemaster coordinates all modules

1. Reads its mandatory `references/operating-contract.md` (preservation rules, complete implementation, no surprise feature removals, GitHub-credit restrictions).
2. Evaluates the entire list in `references/module-index.md` for relevance to the actual task.
3. Reads the full bundled `SKILL.md` and all required references for every applicable specialist.
4. Inventories existing code and interfaces before edits; identifies cross-module dependencies.
5. Performs authorized implementation only with tools actually available; verifies integration points.
6. Records test evidence and unresolved risks; does not promise zero regressions without proof.

Examples of multi-domain routing: a desktop application upgrade may need Architect, Desktop, Database, Contracts, Integrator, Tester, Guardian, Build Doctor, and Release; a security event may need Forensics, Detection Lab, Blue, Protocol Lab, and Documentation. Non-applicable specialties are assessed but not blindly executed.

## 5. Configure your own repositories and assets

The public skills intentionally contain **no original creator-specific repository, montage, username, machine path, or account**. `config.example.json` is the blank, optional schema. In your own **project** (not in this public repository), create `.codeman/config.json` from it and populate only authorized data.

Repository definitions may contain an `id`, `provider`, `url`, and `default_branch` when your own project needs them. The optional `intro_montage` object is disabled by default; it can specify your actual asset location if your application uses one. If no montage exists, leave it disabled. A skill must not invent one.

Never save tokens, API keys, passwords, SSH keys, or customer data in the config file. `.codeman/config.json` is ignored by this distribution. Use agent-supported authentication tools and only supply sources you intend the assistant to access. See [docs/CONFIGURATION.md](docs/CONFIGURATION.md).

## 6. GitHub and no-credit policy

GitHub access is opt-in per request. No module should start GitHub Actions, Codespaces, Copilot sessions, hosted runners, or metered services, or push content that would indirectly trigger paid automation. Before requesting a GitHub push, check whether target workflows or automation could run. Standard repository reads and basic git object writes are different from hosted compute; do not assume a repo is non-metered without inspecting its current behavior.

Security skills operate only with appropriate authorization, tools, and isolated analysis conditions. They do not confer permission to scan third-party targets or execute unknown malware on a personal workstation.

## 7. Workflow: inspect, implement, verify

For modifications, provide scope, desired behavior, input files, expected output, constraints, and anything that must remain unchanged. The skill should: (a) record the existing feature baseline, (b) map callers/interfaces/configs, (c) make complete in-scope changes, (d) run available type/build/test/security checks, (e) audit the diff, and (f) supply requested deliverables and an explicit status for any test that could not run.

A skill is an instruction layer, not an automatic guarantee: unavailable tools, incomplete access, and nondeterministic software behavior must be disclosed rather than described as successful.

## 8. Public repository layout

- `README.md` — overview, credit and quick start
- `SKILLMANUAL.md` — this complete operator/maintainer manual
- `skills/codemaster/` — self-contained master skill, all 40 bundled specialty references
- `skills/codeman-*/` — 40 separate fully referenced specialty folders, each containing an individual README
- `upload-zips/` — 41 standalone ZIPs
- `bundles/README.md` — collection-bundle instructions
- `bundles/skillman-all-public-skills.zip` — one offline bundle containing all public skill sources and individual archives
- `docs/CATALOG.md` — complete directory of skills and their responsibilities
- `docs/CONFIGURATION.md` — optional peer-local settings
- `docs/PUBLISHING.md` — publication workflow and credit safeguards
- `docs/CONTRIBUTING.md` — public contribution standards
- `docs/SECURITY.md` — safety and personal-information handling
- `tools/build_packages.py` — deterministic ZIP and manifest builder
- `tools/audit_distribution.py` — personal-reference/secret-pattern scanner
- `tools/verify_packages.py` — source, archive, and checksum verification
- `MANIFEST.json`, `SHA256SUMS` — file-integrity metadata

## 9. Rebuild, inspect, and validate before sharing

From the repository root, with Python 3.10 or newer:

```bash
python tools/build_packages.py
python tools/audit_distribution.py
python tools/verify_packages.py
```

The builder assembles **41 ZIPs and one combined bundle** deterministically from public sources; the scanner checks text files plus every ZIP member; verification checks every packaged file against its source and every manifest checksum. Review the actual source and diff manually too: an automated scan cannot guarantee every possible personal reference was detected. Do not mix `codemaster-personal.zip` or any personal archive into the public tree.

## 10. Editing and contributing

1. Work on the source in `skills/<skill-name>/`, not only inside `upload-zips/`.
2. Update the skill's README when behavior or prerequisites change.
3. If a specialist changes, update Codemaster's bundled copy at `skills/codemaster/references/modules/<skill-name>/` so standalone and master instructions stay aligned.
4. Run the three validation commands and examine changes for accidentally committed secrets, personal repo pointers, generated credentials, and unexpected deletions.
5. Verify user-facing links, archive names, and filenames. Follow contribution/security documents before opening a PR or publishing.

## 11. Troubleshooting

**Skill says a reference is missing:** You likely copied only `SKILL.md`, rather than the full skill directory. Install the matching complete ZIP.

**Codemaster cannot find a specialist:** Ensure the master archive includes `references/modules/` and all 40 subfolders; use the included verification script.

**GitHub or build tools unavailable:** Grant appropriate non-metered access through the host, provide files directly, or run the operations locally. Do not interpret skill text as tool access.

**Intro montage not found:** Set an explicit project-specific source if the project requires one, otherwise leave the optional montage disabled. Never use another person's repository by default.

**Test cannot run:** Mark it as not run, identify the missing environment, and provide a reproducible local test procedure.

**Unexpected new feature loss:** Use Codeman Guardian and Codeman Recovery, inventory the change against the baseline, and revert only the scoped regression without discarding unrelated work.

## 12. Attribution and legal

**Background Gremlin Group — Creating Unique Tools for Unique Individuals.**

Attribution is required in the root README and this manual for this distribution. An explicit software license is not included here; the repository owner should choose the appropriate license before setting terms for downstream redistribution. This manual does not grant additional rights by itself.
