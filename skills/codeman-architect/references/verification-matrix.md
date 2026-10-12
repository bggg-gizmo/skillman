# Codeman Architect — verification matrix

Use this matrix as an execution gate, not as a claim that testing has occurred. Each relevant row must have an outcome supported by direct evidence. A source-only review may support a static observation but does not replace live or integration testing.

| ID | Required check | Evidence required |
| --- | --- | --- |
| 1 | All runtime entry points and data stores are represented. | Inspect implementation and run a relevant local or authorized test; record exact file/command and observed result. |
| 2 | Interfaces have defined owners and compatibility semantics. | Inspect implementation and run a relevant local or authorized test; record exact file/command and observed result. |
| 3 | Critical failure and recovery paths have explicit behavior. | Inspect implementation and run a relevant local or authorized test; record exact file/command and observed result. |
| 4 | Design accounts for operational observability and security. | Inspect implementation and run a relevant local or authorized test; record exact file/command and observed result. |
| 5 | Migration phases are deployable in a realistic order. | Inspect implementation and run a relevant local or authorized test; record exact file/command and observed result. |
| 6 | No existing user-facing capability is silently dropped. | Inspect implementation and run a relevant local or authorized test; record exact file/command and observed result. |

## Universal cross-checks

1. **Preservation:** Compare original and changed functions, features, error paths, assets, and public interfaces; justify every observed difference with explicit request scope.
2. **Completeness:** Check that all requested features are implemented, registered, configured, integrated, built, and packaged; refuse stubs and partial handoffs.
3. **Functional proof:** Run applicable focused tests and existing regressions, or explicitly record why execution is unavailable.
4. **Working-tree safety:** Preserve pre-existing uncommitted changes, private files, credentials, and unrelated generated artifacts.
5. **GitHub credit compliance:** No read is attempted without request; no write, workflow, hosted job, or action with uncertain credit effect is launched.
6. **Montage provenance:** For relevant app openings, identify the actual authorized, operator-configured montage asset; report repository inaccessibility instead of substituting a guessed file.

## Outcome vocabulary

- **Passed:** Verification was executed and the recorded result satisfies the check.
- **Failed:** Executed verification showed an incorrect or incompatible result.
- **Not run:** The check applies but was not executed; give the reason.
- **Not applicable:** The check does not apply to the scoped work; explain why.

Do not claim all features are regression-free if applicable checks remain not run, failed, or outside the inspected scope.
