# Codeman operating contract — public edition

This public, standalone contract is included with each Codeman skill. Apply it before specialized guidance. These universal requirements are not tied to any developer, account, repository owner, organization, or machine. If the environment or higher-priority instructions prevent completion, report the specific limitation rather than claiming compliance.

## Mandatory implementation directives

```text
all functions and features are mandatory. No regression. Do not remove functions or features. Make sure all code for all functions and features are fully fleshed out and completely implemented and fully integrated; without any placeholders or omissions or sumerizations or minimizations or simplifications or ellipses or pseudo code or brevity or anything like that. 

Use GitHub if asked, but never consume any GitHub credits.

For any application or programming startup montage, use only the asset explicitly specified for the current project or configured by its operator; do not assume a repository, owner, path, or asset exists.
```

## Enforceable interpretation

1. Inventory the existing system before proposing or making edits: source files, exported interfaces, commands, APIs, routes, build targets, tests, configurations, assets, feature flags, integrations, and side effects.
2. Treat every discovered function and feature as a preservation requirement. Changes must remain backward-compatible unless the operator explicitly authorizes a named breaking change. Preserve inputs, outputs, state semantics, error handling, security properties, and expected behavior.
3. Implement every requested feature end-to-end: call sites, wiring, configuration, UI and API contracts where applicable, test coverage, documentation required for correct operation, and required assets. Do not return placeholders, TODO bodies, unimplemented branches, ellipses, pseudocode, illustrative-only fragments, or silently omitted files as completed work.
4. Do not autonomously broaden scope by deleting, renaming, simplifying, consolidating, or replacing functions, modules, features, screens, flags, assets, or external interfaces. Do not claim equivalence without proof through tests or direct comparison.
5. Before editing, take a read-only baseline and, if a repository is available, inspect its working tree so pre-existing changes remain untouched. Make a narrow change set and audit the final diff against the baseline.
6. Run relevant existing tests and new focused tests where execution is available. Report each command and its outcome accurately. If tests cannot run, state that they were not run and why; do not promise zero regression without evidence.
7. Use GitHub only when explicitly requested. Avoid consuming GitHub credits: never start GitHub Actions workflows or checks, Codespaces, Copilot tasks, metered GitHub-hosted computing, or other credit-consuming operations; never make a push or write action that might trigger metered automation. Reading repository files and metadata is permitted when requested and supported by available tools, provided the operation itself is not credit-consuming. If the billing impact is uncertain, do not perform the operation; ask for an alternative or a confirmed non-metered workflow. The instruction is about preventing consumption, not merely avoiding direct billing.
8. For application/program opening montages, determine whether the project requires an existing montage. When required, consult the operator's explicit request and optional local configuration in `references/local-configuration.md`. Use only a verified, authorized existing asset, whether local or in a configured remote repository; do not fabricate filenames, paths, or content. If the asset source is absent or inaccessible, report what is missing rather than silently substituting something else.
9. Use full source files or downloadable complete artifacts when the requested solution is too large for inline output. Never replace missing implementation with a summary or a statement that other files are unchanged when complete contents were explicitly requested. Preserve original files outside the requested scope.
10. Do not access, alter, deploy, or share private systems or data without appropriate operator authorization and tool access. Never represent a proposed command as one that has actually run.
11. Treat project-specific sources, internal services, GitHub owner names, paths, and montage assets as opt-in local settings; do not assume these public skills confer access or authorize an action. Do not commit machine-specific configurations or secrets to a public repository.

## Required completion checks

- Explicitly identify requested changes and preserved behavior.
- Check integration paths, call sites, imports, schemas, configs, and existing features impacted by the diff.
- Provide implementation artifacts or exact changed source where requested.
- List tests actually executed, tests not executed, their results, and any known unresolved risk.
- State any incomplete requirement rather than treating it as completed.
