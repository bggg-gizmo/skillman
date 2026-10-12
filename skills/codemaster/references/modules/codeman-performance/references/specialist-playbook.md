# Codeman Performance — specialist execution playbook

## Preconditions

Use for performance regressions, memory leaks, slow APIs, desktop startup delays, capacity analysis, or benchmarking.

This workflow does not imply repository, browser, laboratory, cloud, sandbox, CI, package registry, or live system access. Read `operating-contract.md` before doing any work. A preservation baseline is mandatory for changes to existing applications. Do not modify source merely to complete an analysis request.


## Phase 1: Define measurable target

1. Capture performance goal and user-visible workload; specify input sizes, concurrent clients, hardware, runtime, cold/warm state, and percentile/statistical metrics.
2. Reproduce current behavior and verify correctness before performance edits; keep baseline throughput/latency and resource consumption.
3. Separate environmental variability and background load from application bottlenecks.
## Phase 2: Profile to establish causality

1. Use CPU profiles, allocation traces, heap snapshots, flame graphs, database EXPLAIN plans, I/O counters, and distributed traces as applicable.
2. Follow high-cost stacks to specific code paths and characterize contention, lock time, N+1 queries, memory retention, and serialization cost.
3. Identify the cost of the existing feature set, including startup montage if it is truly part of the reported path.
## Phase 3: Choose bounded optimization

1. Prioritize algorithmic complexity, needless allocations, repeated work, inefficient queries, unbounded queues, and inappropriate blocking.
2. Preserve outputs, ordering semantics, side effects, thread-safety, permissions, and behavior under concurrency.
3. Avoid broad rewrites, silent cache staleness, and relaxed validation that would make benchmarks appear faster.
## Phase 4: Verify performance and correctness

1. Benchmark before/after under comparable workload, environment, warmup, concurrency, and repeated trials.
2. Run existing functional/regression tests plus concurrency, resource-pressure, and malformed-input tests where applicable.
3. Watch for latency tail growth, memory spikes, contention shifts, and worst-case regressions despite mean improvements.
## Phase 5: Report quantified outcomes

1. Provide workload definition, profile evidence, code changes, before/after measurements, and limitations.
2. Distinguish measured improvements from estimates and make no cross-platform claims without measurement.
3. Preserve related feature and contract invariants even when they limit achievable speedups.

## Required project deliverables

1. **Baseline workload and profiling capture** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
2. **Bottleneck hypothesis and measured evidence** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
3. **Minimal optimization diff** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
4. **Repeated benchmark and correctness results** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.
5. **Latency/memory tradeoff assessment** — Provide evidence from inspected files or executed tools; if not applicable, state the project-specific reason.

## Known failure patterns to reject

- Benchmarks using different data sets.
- Claiming fast from code inspection alone.
- Caching authorization decisions unsafely.
- Ignoring worse latency tails.

## Completion and escalation

Before completion, inspect the exact requested scope against the deliverable inventory and `verification-matrix.md`. Name every implementation file and external integration that was actually created or modified; link the evidence available. If a test failed, repair within the permitted scope or state the unresolved failure. If a verification tool or source is unavailable, record the missing prerequisite and do not convert an assumption into a passed result. Never discard an original function, feature, integration, user configuration, test, or data asset without the user's explicit permission. GitHub-credit and operator-configured montage rules apply even when the specialty has no GitHub-specific purpose.
