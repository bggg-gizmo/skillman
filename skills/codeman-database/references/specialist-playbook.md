# Codeman Database — specialist execution playbook

## Preconditions

Use for PostgreSQL, SQLite, MySQL, data modeling, queries, migrations, consistency defects, or database-backed application features.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Inspect physical and logical model

1. Review actual DDL, ORM models, migrations, indexes, constraints, triggers, views, permissions, connection pooling, and data retention rules.
2. Map read/write code paths and consistency requirements, including isolation levels, concurrency, time zones, encoding, and null handling.
3. Identify pre-existing data formats and consumers before changing schema or queries.
## Phase 2: Design safe schema evolution

1. Specify primary/foreign keys, uniqueness, defaults, checks, on-delete behavior, nullability, migration ordering, and backward compatibility.
2. Prefer expand-and-contract patterns when old and new application versions coexist; plan data backfill with batching, retry safety, and integrity validation.
3. Explicitly identify irreversible operations, lock risks, table rewrites, and backup/recovery prerequisites.
## Phase 3: Implement data access correctly

1. Use parameterized queries, least-privilege credentials, bounded pagination, deterministic ordering, and transactions spanning coherent invariants.
2. Choose indexes and query forms from real access patterns and inspect query plans under representative data sizes.
3. Prevent N+1 queries, lost updates, transaction leaks, deadlocks, and surprising isolation-dependent behavior.
## Phase 4: Verify state and compatibility

1. Test schema constraints, transaction rollback, concurrent writes, older data decoding, migration upgrade, and backup restore where environment permits.
2. Check data types and precision, cross-time-zone handling, serialization differences, and default values in application layers.
3. Measure before/after query performance using comparable plans and data distributions rather than assumed gains.
## Phase 5: Deliver operationally safe changes

1. Provide complete migration scripts, application code, seed/fixture changes, backfill verification, and rollback caveats.
2. Do not run destructive operations on production or live user databases without explicit authorization.
3. Document operational resource requirements, estimated lock/scanning impact if measured, and unverified environments.

## Required project deliverables

1. **Schema and usage inventory** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Complete migration and data-access changes** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Compatibility and concurrency tests** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Query plan and benchmark evidence** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Backup and rollback limitations** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Changing column type without old-data analysis.
- Testing migrations only on empty databases.
- Using guessed performance metrics.
- Executing deletes on unbacked-up production data.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
