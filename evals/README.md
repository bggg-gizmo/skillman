# Skillman agent evaluations

The tests here are **reproducible evaluation tasks**, not fabricated demonstrations of better agent performance. To measure improvements, run real coding agents on the exact same tasks with and without Codeman/Codemaster, capture their finished working directories, and score them with `run.py`. Do not conflate ZIP/package checks, fixture smoke tests, or hand-written reference repairs with executed agent evaluations.

## Protocol

1. Use the **same** model/version, runtime, repository snapshot, timeout, allowed tools and task prompt for each pair of runs. Use fresh separate workspaces for each arm; randomize order to reduce temporal bias.
2. **Baseline arm:** Provide only the task prompt, the checked-out fixture, and standard tools. Do not provide these skills.
3. **Skill arm:** Install either the chosen public Codeman skill or public Codemaster, confirm its activation, and give the identical task prompt and tools.
4. Independently apply `prepare` and `score` to each arm. Keep full diffs, prompts, resulting files and test stdout/stderr in private result storage for audit. Never publish secrets from actual projects.
5. Repeat with at least 5 paired runs per task, with more replications when variance is high. Aggregate pass rates, per-test assertion outcomes, and incomplete tasks. If a run cannot execute, label it **not run**, not passed.
6. Report model/version, temperature where applicable, skill hash, date, execution duration, and number of runs. Compare per-task pass/fail, not only headline averages. Explain that tests do not cover all possible regressions.

## Commands

```bash
python evals/run.py list
python evals/run.py prepare --task feature-preservation --output /tmp/skillman-feature-baseline
# Ask a real agent to apply the task stated in /tmp/skillman-feature-baseline/TASK.md,
# using only the prepared workspace. Repeat in a separate directory with Codemaster enabled.
python evals/run.py score --task feature-preservation --workspace /tmp/skillman-feature-baseline --arm baseline --run-id baseline-01 --record /tmp/baseline-01.json
python evals/run.py score --task feature-preservation --workspace /tmp/skillman-feature-codemaster --arm codemaster --run-id codemaster-01 --record /tmp/codemaster-01.json
python evals/run.py compare /tmp/baseline-01.json /tmp/codemaster-01.json
```

The scorer only inspects files and executes tests in the selected **local evaluation workspace**. Treat solutions as untrusted software; run inside an isolated disposable container or VM without sensitive credentials or network access. `score` starts subprocesses running the tested code.

## Evaluation cases

| Task | Primary skills exercised | What the tests check |
|---|---|---|
| `feature-preservation` | Guardian, Program, Tester, Integrator | Add division without deleting or changing addition, subtraction, multiplication, history or unknown-operation errors |
| `api-integration` | API, Architect, Integrator, Tester | Wire a new health endpoint into the router and service, preserving existing API behavior |
| `untrusted-input` | Security, Auditor, Tester | Remove an `eval` injection path while preserving supported literal structures and correct exception behavior |
| `performance-preservation` | Performance, Coder, Guardian | Reduce comparisons for hashable inputs while retaining order, duplicates semantics and unhashable support |

### Current evidence status

**Agent comparison outcomes: not yet run.** This repository includes a complete fixture/scorer and self-tests; it does not currently contain verified baseline-versus-skill outcomes from independent agent executions. The self-tests validate that the harness detects known failing/passing solutions, not that skills improve model capabilities. The finding "No demonstrated end-to-end skill evaluations" remains **open** until real paired runs are published with evidence.
