# Codeman Core — change-execution protocol

This is a language-agnostic process for implementing requested code changes without losing existing behavior. It does not override environment capabilities, tool authorizations, or higher-priority instructions.

## 1. Read-only discovery

1. Confirm exactly which repository/files and requested changes are in scope; never infer missing access.
2. Inspect README, build/test commands, project-specific instructions, source entry points, configuration, tests, and relevant assets.
3. Build a preservation inventory: functions, features, external contracts, public APIs, user journeys, data formats, error cases, and jobs that might be affected.
4. Inspect repository status if available. Preserve pre-existing dirty changes and identify generated/secret files that must not be modified.
5. Check whether the project requires an opening montage; if yes, use the actual asset from the operator-configured source repository when requested and authorized; don't invent one.

## 2. Exact implementation

1. Convert every user requirement into a concrete change and integration/verification path.
2. Change the smallest set of files that satisfies the request. Keep all existing functions and features.
3. Implement all branches, error paths, imports, registrations, migrations/configuration, resources and call-site integration required for actual operation.
4. Do not return placeholders, stubs, summaries, shortened code, or pseudocode disguised as completion.
5. Never trigger metered GitHub compute or workflows. Use only approved, non-credit-consuming GitHub operations if requested.

## 3. Verification

1. Run syntax/type/build checks appropriate to the toolchain and actual environment.
2. Run focused new tests for the requested behavior; run existing tests that cover affected features.
3. Check failure paths, data integrity, backward compatibility, and the entire diff for unexpected deletions and regressions.
4. If a check is impossible, report it as unverified, not successful.

## 4. Delivery

Report delivered files, feature integration, affected interfaces, tests with pass/fail/skipped outcomes, known limitations, and unperformed work. When full output is too large for chat, deliver complete downloadable files rather than truncating the implementation.
