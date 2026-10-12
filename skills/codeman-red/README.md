# Codeman Red

Conduct authorized, scoped exploit validation, attack-surface analysis, fuzzing, and protocol testing with reproducible evidence and safeguards.

## Install and use

Install the standalone [`codeman-red.zip`](../../upload-zips/codeman-red.zip) in a compatible skill-capable agent, or copy this entire folder into that agent's supported skills directory. Invoke **codeman-red** for work in this specialty. Follow the host agent's documented installation rules.

This skill is standalone. Its operating contract and reference material are packaged with it, so it does not require the other Codeman skills. It does not automatically install or grant access to compilers, GitHub, repositories, scanners, or external systems.

## Files

- [`SKILL.md`](SKILL.md): activation and instructions.
- [`references/local-configuration.md`](references/local-configuration.md): bundled reference.
- [`references/operating-contract.md`](references/operating-contract.md): bundled reference.
- [`references/specialist-playbooks.md`](references/specialist-playbooks.md): bundled reference.

## Local configuration

When your own project requires repository pointers or startup assets, use the [configuration guide](../../docs/CONFIGURATION.md) and [blank example](../../config.example.json). Do not add credentials or personal configuration to a public skill.

## Publication checks

Run `python tools/audit_distribution.py` and `python tools/verify_packages.py` from the repository root after rebuilding packages. See [Skillmanual](../../SKILLMANUAL.md) for workflows and guarantees.
