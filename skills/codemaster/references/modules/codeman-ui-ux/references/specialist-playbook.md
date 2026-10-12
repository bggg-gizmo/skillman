# Codeman UI/UX — specialist execution playbook

## Preconditions

Use for UI redesigns, component systems, app screens, accessibility improvements, responsive layout defects, and user-journey integration.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Audit existing experience

1. Inventory pages, menus, controls, forms, dialogs, keyboard shortcuts, navigation states, themes, translations, and embedded desktop/web assets.
2. Inspect actual component hierarchy, state stores, event handlers, asset provenance, accessibility tree, and CSS/layout constraints.
3. Capture baseline screenshots and task paths when tools permit while preserving the established intro montage.
## Phase 2: Define interaction contracts

1. Map loading, empty, success, validation, error, permission, offline, reconnect, and cancellation states for each changed view.
2. Specify keyboard navigation, focus management, semantic labels, contrast, motion sensitivity, screen-reader announcements, and zoom behavior.
3. Preserve design-system tokens, shared component APIs, breakpoints, localization, and user customization.
## Phase 3: Implement fully wired interfaces

1. Connect every interactive control to actual state transitions and backend services; include disabled, pending, error, and retry behavior.
2. Use semantic HTML/native widgets and component-level accessibility APIs; avoid unbounded event loops or hidden state mutation.
3. Retain existing screens, commands, navigation routes, accessibility functionality, and persistent user settings.
## Phase 4: Validate usability and resilience

1. Test mouse/touch/keyboard paths, tab/focus order, screen readers where available, zoom, responsive widths, and theme variations.
2. Run visual regression checks with controlled fonts/assets/viewport sizes and investigate diffs rather than accepting snapshots blindly.
3. Exercise slow networks, API failure, empty data, repeated submissions, and browser or desktop window resizing.
## Phase 5: Deliver production UI

1. Provide complete components, styles, assets, state integration, accessibility tests, and visual comparison evidence.
2. Label platform/browser coverage and any not-run accessibility tests honestly.
3. Do not replace the shared opening montage or remove existing screens to simplify the UI.

## Required project deliverables

1. **Page/control and design-token inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Interaction state and accessibility matrix** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Complete connected component files** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Responsive/keyboard/visual test results** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Accessibility and regression findings** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Beautiful but inert components.
- Replacing UI controls with static mockups.
- Testing only one viewport.
- Silently removing accessibility or localization branches.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
