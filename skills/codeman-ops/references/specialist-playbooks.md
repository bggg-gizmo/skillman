# Codeman Ops — specialist playbooks

Use this reference when the request involves infrastructure automation and operations. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** Docker, Kubernetes, Terraform, Linux, CI/CD.

## Docker

1. Inspect Dockerfile stages, base-image versions/digests, build context, ignore rules, entrypoint, environment variables, users, volumes, ports, and health checks.
2. Preserve runtime behavior, UID/GID assumptions, capabilities, signals, filesystem paths, dependency versions, and startup order.
3. Minimize attack surface without removing necessary packages or functions; handle build secrets and caches safely.
4. Build and test images locally when available and authorized; validate that application startup and health checks still work.
5. Provide exact image/tag behavior, changed layers, required variables, and rollback procedure.

## Kubernetes

1. Inspect workloads, namespaces, RBAC, services, ingress, ConfigMaps, Secrets references, PVCs, autoscaling, policies, selectors, and Helm/Kustomize sources.
2. Preserve existing service discovery, labels/selectors, probes, rollout behavior, persistent data, and workload identity.
3. Check resource limits, disruption budgets, network policies, readiness, and least privilege in context of service requirements.
4. Validate rendered manifests and schema locally where available; avoid `kubectl apply` or cluster mutations without explicit authorization.
5. Produce exact manifests/patches, deployment prerequisites, dry-run results where actually executed, and rollback guidance.

## Terraform

1. Inventory providers/versions, backends, workspaces, modules, variable contracts, data sources, drift, and state sensitivity.
2. Preserve resource identities, addresses, imports, and live-state expectations; mark any replacement or deletion risk explicitly.
3. Make changes in modules and variables consistently; avoid broad state refactors without explicit authorization.
4. Run `terraform fmt -check` and `terraform validate` when environment permits. Plan only with approved credentials and endpoints; never apply without explicit request.
5. Review any obtained plan for destroys, replacements, cost/security effects, and data loss; do not claim a plan was run when it was not.

## Linux

1. Identify distro/release, init system, shell, filesystem layout, permissions, packages, firewall, service manager, and logging paths.
2. Preserve service ownership, user/group IDs, startup ordering, sockets, cron/systemd timers, and OS-version compatibility.
3. Prefer inspect/read-only diagnostics before changing system config; validate syntax and permissions before writing.
4. For scripts and services, handle idempotence, signal termination, retries, logging, and rollback.
5. Do not restart or mutate live services without authorization; distinguish recommendations from executed operations.

## CI/CD

1. Inventory existing stages, runners, permissions, secrets, release artifacts, branch protection, required checks, environment approvals, and rollback process.
2. Preserve test and deployment gates while adding requested checks; avoid deleting security checks or bypassing protections.
3. For GitHub repositories, never trigger GitHub Actions, workflows, Codespaces, Copilot tasks, or changes that could consume GitHub credits. Do not push workflow edits that may trigger automation.
4. Validate pipeline configuration syntactically and with local/offline emulation where supported without metered hosted execution.
5. Document the difference between locally validated pipeline configuration and a pipeline run on a hosted runner.

## Operations changes

Before mutation, state target environments, affected resources, intended differences, privilege needs, maintenance impact, data backup/restore dependencies, and rollback sequence. Never conceal an operation that could destroy persistent data or incur metered resource use.

