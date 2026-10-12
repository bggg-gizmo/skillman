# Task: optimize stable deduplication without regressions

Improve `unique_stable` for large collections of hashable values, while preserving first-occurrence order, equality semantics, unhashable list/dict values, mixed input types, and the return type. Avoid silent changes to the public API. Avoid relying on timing-only claims; use actual measured comparisons and correctness tests.
