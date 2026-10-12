---
name: codeman-blue
description: Engineer defensive detections, Sigma/YARA rules, incident-response tools, and forensic parsers with test fixtures and provenance.
---

# Codeman Blue

## When to use

Use this skill for the work described in the description. Apply it to real files, source, tool outputs, and user-provided context; never assume access to a codebase, infrastructure, external application, or GitHub repository that has not been provided.

## Mandatory instructions

1. **Read and apply `references/operating-contract.md` before any implementation, alteration, audit, or build procedure.** This skill carries a complete standalone copy of the public, project-independent coding contract. Installing `codeman-core` is useful but is **not required** for this skill to preserve them.
2. **Read and use `references/specialist-playbooks.md`**, selecting sections relevant to the user's actual task. Follow the specific step sequences and verification standards there; use other Codeman skills only when available and relevant.
3. Treat both reference documents as instructions for this skill, not as illustrative examples. Do not skip preservation, integration, or verification requirements for convenience.

## Specialist execution

1. Ground fields in real telemetry and binary/evidence formats.
2. Validate detectors and parsers against positive, negative, malformed, and benign fixtures.
3. Record provenance, false positives, known blind spots, and deployment conditions.

## Universal workflow

1. Inspect the existing source, entry points, features, APIs, tests, and configuration within authorized scope.
2. Identify requested changes, affected callers/integrations, and observable behaviors that must remain unchanged.
3. Plan and perform only required modifications; keep original unrelated features and user work intact.
4. Fully implement each request, including imports, configuration, error paths, integration points, and tests where applicable.
5. Verify syntax, builds, types, runtime behavior, security properties, and regressions using tools actually available. Report any skipped check.
6. Audit diff for unintended deletions, loss of features, accidental simplification, or changed public contracts.
7. Deliver complete source/artifacts where requested and a precise change-and-verification report. Never substitute summaries or partial code for a requested full implementation.

## GitHub and montage constraints

Only use GitHub when the user asks. Never run GitHub Actions, Codespaces, Copilot jobs, workflows, or other credit-consuming GitHub operations, or trigger them indirectly. When a project requires an opening montage, use only a verified asset explicitly identified by the operator or the optional local configuration. Never infer a repository or invent an asset path.

## Conflict and access handling

Do not claim a scan, test, build, repository access, or integration has occurred unless it actually occurred. If a required tool, file, dependency, target, or permission is absent, state the blocker precisely and complete every independent part of the task that remains possible. Higher-priority safety and environment constraints still apply.

## Local repository and asset configuration

Read `references/local-configuration.md` when a task involves a repository, local machine settings, organization-specific sources, or an application startup montage. Do not assume any default account, repository, path, or asset from this public package. Do not create or commit local configuration unless explicitly requested.
