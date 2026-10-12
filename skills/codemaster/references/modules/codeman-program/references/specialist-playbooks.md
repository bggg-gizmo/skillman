# Codeman Program — specialist playbooks

Use this reference when the request involves writing, porting, reviewing, or debugging code in the nine named languages. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** Python, C, C++, Rust, Go, JavaScript, TypeScript, PowerShell, Bash.

## Python

1. Inspect interpreter version, `pyproject.toml`, lockfiles, package layout, imports, typing policy, entry points, and the test runner.
2. Track behavior through imports and callers before changing signatures; preserve synchronous versus asynchronous behavior, generators, context managers, exceptions, and serialization contracts.
3. Use existing formatting and type conventions. When modifying async code, verify cancellation, task lifecycle, awaits, exception propagation, and resource cleanup.
4. For file/network/database operations, preserve encoding, timeouts, transactions, and error paths; avoid mutable defaults and accidental shared state.
5. Validate syntax with `python -m compileall` on the relevant package, then run the repository's actual unit/integration tests and configured type/lint tools when available.
6. Deliver complete updated modules and note Python-version compatibility and any unexecuted checks.

## C

1. Identify C standard, platform ABI, compiler flags, headers, linker scripts, allocation conventions, calling interfaces, and error codes.
2. Preserve struct layout, exported symbols, preprocessor branches, integer widths, pointer ownership, and thread-safety guarantees.
3. Audit bounds, signedness, integer overflow, null checks, lifetime, double-free, initialization, and resource cleanup on all failure paths.
4. Keep header declarations, translation units, build-system sources, and platform-specific branches synchronized.
5. Use the project compiler, strict warnings, sanitizers, and regression tests where available; do not pretend a sanitizer run has occurred if unavailable.

## C++

1. Inspect C++ standard, compiler/stdlib versions, CMake or other build descriptions, exported ABI, exception settings, and relevant templates.
2. Preserve overload resolution, interfaces, namespace and symbol compatibility, exception-safety guarantees, and data ownership.
3. Use project-consistent RAII and smart-pointer semantics; account for reference invalidation, move/copy behavior, polymorphism, and lifetime.
4. Check concurrency invariants, lock ordering, data races, atomics and memory order where applicable.
5. Build intended configurations and run unit/integration tests; apply ASan/UBSan/TSan only in suitable available environments.

## Rust

1. Inspect toolchain, edition, crate/workspace topology, features, `Cargo.lock`, `unsafe` blocks, public traits, and exposed FFI.
2. Preserve ownership and borrowing semantics, trait contracts, public type signatures, feature-gated behavior, Send/Sync guarantees, and error types.
3. Review `unsafe` invariants, lifetimes, pinning, aliasing, integer conversions, and panic boundaries; document assumptions near unsafe sites.
4. Prefer repository-consistent error handling and avoid introducing unnecessary crates or changing feature defaults.
5. Run available `cargo fmt --check`, `cargo check --all-targets`, `cargo test` and existing lint configurations as appropriate.

## Go

1. Inspect `go.mod`, `go.sum`, supported Go version, package boundaries, interfaces, build tags, and binary entry points.
2. Preserve context cancellation and deadlines, exported APIs, error wrapping semantics, HTTP/gRPC contracts, and goroutine lifetimes.
3. Avoid leaking goroutines and channels; check data races, synchronization, nil interfaces, and resource ownership.
4. Keep package dependency direction and generated files consistent with repository rules.
5. Run applicable `go test ./...`, `go vet ./...`, and race tests where practical and authorized.

## JavaScript

1. Identify runtime/browser matrix, module system, package manager, lockfile, bundler, transpilation, API contracts, and existing test setup.
2. Preserve observable async behavior, event listeners, exception handling, state transitions, exports, route behavior, and browser support.
3. Validate null/undefined cases, input coercion, promise lifecycle, unhandled rejections, and security-sensitive DOM/URL handling.
4. Reuse existing lint and formatting conventions; avoid new dependency and global state unless required.
5. Run the project test, lint, build, and relevant browser checks using existing scripts without enabling billable hosted CI.

## TypeScript

1. Inspect `tsconfig.json`, strictness, path aliases, declaration generation, API types, runtime validation, and monorepo workspaces.
2. Preserve exported types, discriminated unions, generic contracts, public declaration compatibility, and runtime semantics.
3. Do not use `any`, type assertions, `@ts-ignore`, or weakening of compiler settings to disguise type errors; justify exceptions with evidence.
4. Keep data schemas and runtime validation aligned with compile-time types, especially untrusted payloads.
5. Run the repository typecheck, tests, lint, and build, recording actual results.

## PowerShell

1. Identify Windows PowerShell versus PowerShell 7+, OS edition, profiles, required modules, execution policy assumptions, and invocation methods.
2. Preserve parameter sets, pipeline behavior, output object shapes, streams, exit codes, and side effects.
3. Use explicit `-WhatIf` and `-Confirm` behavior for mutating operations when the interface supports it; quote paths and handle encoding intentionally.
4. Distinguish terminating and nonterminating errors; do not swallow failures or leak credentials.
5. Validate with available PSScriptAnalyzer and Pester tests and check supported-platform behavior.

## Bash

1. Identify shell (`bash`, `sh`, or other), supported version, target OS, `set` flags, external command dependencies, and expected invocation.
2. Preserve exit codes, stdout/stderr protocols, quoting, globbing, traps, working-directory behavior, signals, and cleanup semantics.
3. Handle whitespace-safe argument arrays, untrusted filenames, pipeline failures, temporary files, and traps; avoid unsafe evaluation.
4. Do not substitute Bash-only syntax into POSIX `sh` scripts.
5. Run `bash -n` for Bash scripts and applicable ShellCheck and integration tests when available.

## Cross-language integrations

1. Identify ABI, serialization, protocol, and version boundaries across runtimes.
2. Keep schema, errors, character encodings, message framing, async behavior, and resource lifetimes consistent at both ends.
3. Validate at least one successful path and one representative error or boundary path using integration tests or reproducible local checks.

