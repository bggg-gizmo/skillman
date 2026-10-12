# Codeman Reverse — specialist playbooks

Use this reference when the request involves static and controlled dynamic reverse engineering. Select the applicable subsection(s) based on the actual repository and request; do not execute every workflow reflexively. Record evidence from actual files, output, and tool results. Keep all operations within the Codeman operating contract.

**Routing clues:** binary analysis, Ghidra workflows, assembly analysis, malware triage.

## Binary analysis

1. Preserve sample identity: cryptographic hashes, file size, format, architecture, endianness, sections, imports/exports, compiler clues, and symbols when available.
2. Inspect metadata, strings, resources, dependency imports, exception metadata, and code/signature consistency without assuming labels are trustworthy.
3. Map entry points and reachable call graph; trace security-sensitive paths, file/network IO, parsers, cryptography, and persistence or privilege behaviors.
4. Distinguish static evidence, dynamic observations, and inferences; supply address or offset for each concrete claim.
5. Record packing/obfuscation limitations, missing code coverage, and architectural uncertainties.

## Ghidra workflows

1. Import the sample using verified language/compiler selection and retain analysis settings and sample identity.
2. Run baseline analysis where tooling permits; review function boundaries, references, calling conventions, stack variables, and decompiler artifacts.
3. Rename symbols and annotate only where justified by instructions and xrefs; keep inferred names recognizable as analyst-assigned.
4. Use the listing and cross-references to validate decompiler output before asserting high-level semantics.
5. Preserve project metadata, annotations, and an address-indexed findings log. Do not assume access to a running Ghidra instance.

## Assembly analysis

1. Identify ISA, bitness, ABI, register roles, stack discipline, instruction semantics, and control-flow transfers.
2. Trace dataflow through registers, stack, global memory, indirection, and calling convention boundaries.
3. Check signed versus unsigned comparisons, integer widths, truncation, aliasing, and branch conditions.
4. Reconstruct higher-level logic faithfully, preserving side effects and unusual error paths rather than normalizing behavior.
5. Attach offsets/addresses and note uncertain symbol resolution, self-modification, or unmodeled indirect calls.

## Malware triage

1. Keep unknown binaries inert by default; hash and classify the sample, then perform metadata, strings, section, import, resource, and configuration analysis.
2. Extract candidate indicators and classify them by direct observation, decoding, or heuristic inference; avoid asserting infrastructure ownership without evidence.
3. Assess likely execution, persistence, privilege, anti-analysis, credential access, and network behavior using static evidence first.
4. If dynamic analysis is authorized and tools exist, use isolated disposable environments with controlled networking and capture process/file/registry/network telemetry; do not execute on the host.
5. Produce behavior summary, IOCs with provenance, detection opportunities, confidence, and artifacts/telemetry limitations.

## Reverse-engineering evidence

Each finding should identify the sample hash; architecture and tool/version when known; function/address/offset; observed bytes, strings, instructions, or traces; interpretation; alternative explanations; confidence; and whether behavior was actually executed. Do not treat a decompiler guess as verified source.

