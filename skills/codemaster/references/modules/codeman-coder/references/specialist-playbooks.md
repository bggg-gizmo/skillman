# Codeman Coder — specialist playbooks

Use this reference when the request involves software architecture and behavioral-preserving changes. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** architecture, refactoring, debugging, dependency management, performance optimization.

## Architecture

1. Map modules, dependencies, deployed services, interfaces, runtime responsibilities, state ownership, data flows, and nonfunctional requirements.
2. Separate observed architecture from assumptions; document current coupling, change constraints, failure domains, and compatibility surfaces.
3. Propose a concrete incremental design with modified files, contracts, data migrations, feature switches, testing plan, and rollback strategy.
4. Do not reorganize an unrelated subsystem or silently change deployment topology; secure explicit authorization for breaking changes.
5. Validate dependency direction, initialization order, fault propagation, observability, and operational constraints.

## Refactoring

1. Define the smallest behavior-preserving transformation, then inventory all callers, imports, side effects, and externally visible surfaces.
2. Capture golden outputs or characterization tests before altering ambiguous behavior.
3. Refactor in small coherent steps while keeping compile/build/test feedback available.
4. Prove equivalence for expected behavior, error cases, concurrency, resource handling, and public APIs; inspect entire diff for unintended changes.
5. Reject opportunistic cleanup unrelated to the explicit task unless separately authorized.

## Debugging

1. Reproduce the failure with exact inputs, environment, versions, observed output, and expected behavior.
2. Trace the actual execution path across layers rather than inferring from error text alone.
3. Build competing hypotheses and eliminate them with targeted logging, tracing, breakpoints, reduced test cases, or static reasoning.
4. Identify root cause, triggering conditions, affected call sites, and why existing tests failed to catch it.
5. Implement the minimal fix and add a regression test that fails before and passes after the fix when possible.

## Dependency management

1. Inventory direct and transitive packages, lockfiles, licenses, pinned versions, platform/runtime constraints, and build reproducibility.
2. Map why each proposed dependency is necessary and identify security advisories and compatibility risks from trustworthy evidence.
3. Keep existing pin and package-manager strategy; avoid blind major upgrades and uncontrolled install-script execution.
4. Update manifests and lockfiles together using authorized tools, preserving vendored/generated metadata when required.
5. Run installation/build/test checks locally when supported without consuming GitHub credits; report transitive changes accurately.

## Performance optimization

1. Define performance metric, workload, correctness invariants, baseline, hardware/runtime details, and acceptable variance.
2. Profile real hotspots including allocations, IO, locking, network waits, and data access before choosing an optimization.
3. Change only the proven bottleneck; verify algorithmic complexity, memory trade-offs, concurrency behavior, and cache validity.
4. Benchmark comparable scenarios with warmed/cold states as appropriate and preserve result correctness under edge cases.
5. Provide before/after measurements with measurement limitations; never claim a speedup based only on intuition.

## Change-control checklist

1. List existing features and functions at risk, including UI/CLI/API behavior and configuration.
2. Link each changed file to an explicit requirement and at least one validation check.
3. Inspect additions, deletions, and renames in the final diff; reconcile all unexpected differences.
4. Provide concise final traceability: requirement → implementation → evidence → remaining limitation.

