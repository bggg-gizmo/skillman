# Codeman Desktop — specialist execution playbook

## Preconditions

Use for Windows, macOS, and Linux desktop application features, native integrations, packaging, installer fixes, or graphical runtime troubleshooting.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Map desktop runtime

1. Identify GUI toolkit, runtime versions, process boundaries, event loop, windows, menus, tray behavior, notifications, background processes, and updater.
2. Inspect platform adapters, signing/permissions, install paths, auto-start rules, persistence, and graphics/resource bundling.
3. Locate existing splash/intro montage integration and trace its actual the configured asset repository origin where access permits.
## Phase 2: Specify platform behavior

1. Document UI state transitions, focus/input behavior, accessibility semantics, native dialogs, filesystem/clipboard integrations, high-DPI scaling, and shutdown.
2. Distinguish operating-system policies and packaging constraints on Windows, macOS, Linux, sandboxed and portable distributions.
3. Map app data, user settings, migration needs, update behavior, and background task lifecycle before modifying architecture.
## Phase 3: Implement complete native wiring

1. Connect UI handlers to actual services, IPC bridge, backend commands, persistent storage, and responsive state management.
2. Validate IPC authorization and input handling; do not expose broad filesystem or command execution privileges from renderer code.
3. Preserve existing menus, shortcuts, assets, installer options, protocol handlers, and resource cleanup.
## Phase 4: Package for real target platforms

1. Verify bundled DLLs/shared libraries/frameworks, icon and localization assets, platform manifests, code signing capabilities, and auto-update channels.
2. Perform build and launch verification per supported platform where tools permit; distinguish build-host verification from target-platform proof.
3. Check cold start, offline launch, upgrade, uninstall, window lifecycle, resource loading, and error reporting.
## Phase 5: Deliver verified desktop behavior

1. Provide source changes, installer artifacts, runtime compatibility notes, platform test evidence, and known missing verification.
2. Preserve existing opening animation/montage and do not fabricate fallback artwork without approval.
3. Do not claim notarization, signing, or installer execution unless successfully performed.

## Required project deliverables

1. **Desktop entry-point and IPC map** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **UI lifecycle and platform contract inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Complete feature implementation files** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Platform build/install validation** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Installer asset and compatibility report** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Confusing web dev preview with packaged desktop behavior.
- Dropping platform-specific feature branches.
- Breaking updater signing metadata.
- Replacing intro montage with an unverified asset.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
