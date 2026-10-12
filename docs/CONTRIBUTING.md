# Contributing

Contributions are welcome as patches to standalone skills. Each skill must retain a working SKILL.md frontmatter block, complete specialist guidance, public operating contract, and local configuration instructions. Do not remove previously documented behavior without an explicit, justified change and the appropriate compatibility updates.

Do not commit personal repositories, local configuration, credentials, tokens, private assets, specific customer data, sensitive crash dumps, or embedded host usernames. Run `python tools/audit_distribution.py` and `python tools/verify_packages.py` before submitting changes. Add or update tests for changes to distribution or configuration semantics.

Never run GitHub Actions, Codespaces, or other metered GitHub operations as part of preparing a change with a no-credit-use requirement. Use local validation. The presence of a skill's GitHub-related instructions does not authorize GitHub access without the current operator's request.
