# Contributing

Contributions are welcome as patches to standalone skills. Each skill must retain a working SKILL.md frontmatter block, complete specialist guidance, public operating contract, and local configuration instructions. Do not remove previously documented behavior without an explicit, justified change and the appropriate compatibility updates.

Do not commit personal repositories, local configuration, credentials, tokens, private assets, specific customer data, sensitive crash dumps, or embedded host usernames. Run `python tools/audit_distribution.py` and `python tools/verify_packages.py` before submitting changes. Add or update tests for changes to distribution or configuration semantics.

Never run GitHub Actions, Codespaces, or other metered GitHub operations as part of preparing a change with a no-credit-use requirement. Use local validation. The presence of a skill's GitHub-related instructions does not authorize GitHub access without the current operator's request.

## Contribution policy and shared instructions

The repository currently reports `pull_request_creation_policy: collaborators_only`, so external PR creation may require maintainer access. Report proposals through repository issues if issue creation is available. This is a documented governance decision to review, not an invitation to work around access controls.

Edit `shared/operating-contract.md` and run `python tools/sync_shared.py` rather than editing 81 contract copies. Specialist changes must also be synchronized to Codemaster snapshots and followed by `python tools/build_packages.py` and the full verification suite.

License: MIT; retain the copyright and permission notices.
