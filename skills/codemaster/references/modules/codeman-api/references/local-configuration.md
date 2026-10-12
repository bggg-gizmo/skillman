# Local configuration for Codeman skills

Codeman skills are independent, reusable instructions. No distributed skill binds to a particular personal repository, GitHub account, filesystem path, or application asset.

## Configuration precedence

1. The current operator's explicit request and authorized scope.
2. The current project's `.codeman/config.json`, if present and readable.
3. The current project's existing settings and documentation, when reliably established.
4. Otherwise leave the field **unconfigured**; request the necessary source or explain the blocker. Never fabricate values.

A machine- or project-specific configuration is **optional**. An operator can copy the repository's `config.example.json` to the local project's `.codeman/config.json` and edit it with their own data. The example intentionally contains no repository URLs, usernames, accounts, or asset paths. The project should ignore `.codeman/config.json` in version control unless all fields have been intentionally reviewed for public release.

Supported fields:

- `schema_version`: configuration format revision, currently `1`.
- `repositories`: list of repository definitions with `id`, `provider`, `url`, and `default_branch`, used only when the current request authorizes working with those repositories. The list may be empty.
- `intro_montage.enabled`: whether a specific project uses an existing opening montage; default `false`.
- `intro_montage.repository_url`: optional remote repository with the existing montage asset.
- `intro_montage.asset_path`: optional path within that repository.
- `intro_montage.local_file`: optional path to an existing local asset.
- `github.only_when_requested`: must remain `true` to respect the operating contract.
- `github.allow_metered_operations`: must remain `false`; a project configuration cannot override the published prohibition.

The `config.example.json` is an editable **data configuration**, not missing implementation code. An empty repository list and null montage paths intentionally mean no account-specific source is configured. A skill can still perform its full general workflows without them.

Do not place tokens, passwords, API keys, private keys, credential material, or customer data in this configuration. Use the host tool's supported authentication mechanism instead.

## Operating rules

- Never discover or choose a user's GitHub repositories without their request or a specific authorized input.
- Never infer an original author's repository or machine settings.
- Never use a configured montage unless relevant to the project and verifiably available.
- Do not claim automatic code access or execution simply because this document exists.
- Keep local configuration separate from the public skill distribution.
