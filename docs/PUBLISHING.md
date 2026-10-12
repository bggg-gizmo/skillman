# Publishing this release to a public Git repository

This repository distribution is generated offline and can be reviewed before publication. Its authorship is not tied to an operator-specific account. No command below runs a GitHub Actions job or GitHub-hosted build.

1. Obtain a clean local checkout of the intended public repository, using the HTTPS or SSH remote **you** authorize. Confirm you are on the correct branch.
2. Review that repository's existing `.github/workflows` and any external push hooks or automation. Do **not** push if the operation might consume GitHub credits; use a verified non-metered publication path instead.
3. Copy the contents of the extracted `skillman/` directory into the repository checkout, preserving existing unrelated files. Review the planned diff, particularly the new README. Never copy personal `.codeman/config.json` files, secrets, or customer data.
4. Run `python tools/build_packages.py`, `python tools/audit_distribution.py`, and `python tools/verify_packages.py` locally.
5. Review the staged changes, confirm no original user content was included, and commit/push only once the remote's non-metered behavior is established.

A publication does not confer a software license. Select a license appropriate for public reuse before inviting third-party redistribution.
