# Shared Codeman operating contract

[`operating-contract.md`](operating-contract.md) is the canonical, public operating contract. Every one of the 41 standalone skills must retain a complete byte-identical copy at `references/operating-contract.md` so installing one ZIP never requires other skills or network access.

**Maintainers:** Edit this file only, then run `python tools/sync_shared.py`, `python tools/build_packages.py`, `python tools/audit_distribution.py` and `python tools/verify_packages.py`. The sync script updates the necessary copies, including Codemaster's 40 embedded module snapshots. This reduces maintenance duplication without deleting any mandatory rule.
