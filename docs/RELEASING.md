# Versioned GitHub release procedure

The presence of ZIPs in `upload-zips/` and `bundles/` does not create a GitHub **Release**. Releases need an authenticated publishing operation outside basic Git object writing. Do not describe release notes, an archive, or a tag as a published Release unless the GitHub Releases API confirms it.

## Preconditions

- Repository maintainer has release/tag permissions and has reviewed [`LICENSE`](../LICENSE).
- No workflow or push automation will consume GitHub credits. Verify `.github/workflows/` and any externally configured hooks before creating a tag or release; stop if uncertain.
- A clean, reviewed main commit contains only public files and has passed all local checks.
- Use a local `gh` CLI installation **only when authenticated by the maintainer** and only if it will not trigger metered workflows.

## Prepare and publish v1.0.0

```bash
python tools/sync_shared.py --check
python tools/check_routing.py
python tools/build_packages.py
python tools/audit_distribution.py
python tools/verify_packages.py
python -m unittest discover -s evals -p 'test_*.py' -v

git fetch origin main
git checkout main
git pull --ff-only origin main

gh release create v1.0.0   upload-zips/*.zip   bundles/skillman-all-public-skills.zip   --target main   --title "Skillman v1.0.0 — Public Codeman and Codemaster"   --notes-file docs/releases/v1.0.0.md   --latest
```

**Do not run** the release command if the repository has a metered release/tag hook, or without publisher authorization. Confirm using `gh release view v1.0.0`. For releases in a repository with many per-skill ZIPs, GitHub release asset limits should be checked before running the command.

## Pull-request policy

The public repository currently reports `pull_request_creation_policy: collaborators_only` and `allow_forking: true`. Whether to retain that restriction is a maintainer decision. For open community PRs, set the policy to allow outside contributions using GitHub's repository settings (requires admin privileges); evaluate spam/moderation impact first. These instructions **do not** change repository policy automatically.
