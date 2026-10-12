# Security and privacy

This package is intended for public distribution. No skill requires a particular account, repository owner, local path, or montage asset. Account and project settings belong in a separate local `.codeman/config.json` and are not embedded in a skill ZIP.

The repository includes `tools/audit_distribution.py`, which scans every shipped file and packaged skill for known personal references, accidental URLs to account-specific repositories, credential patterns, email addresses, and local home directory paths. This scanner is a useful release gate but is not an exhaustive guarantee: maintainers must also review every newly contributed reference, fixture, image, archive, and metadata file manually.

Before publication or a release, run the audit and verify that no identity-bearing files, credentials, personally identifying metadata, or unlicensed internal content are included. Revoke any inadvertently exposed credentials, since deleting a Git commit does not undo public exposure.

Security skills document authorized, defensive, and verification workflows. Installing a skill does not grant access to systems or permission to conduct testing.
