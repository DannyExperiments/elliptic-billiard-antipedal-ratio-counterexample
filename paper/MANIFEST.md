# Stage-4 manuscript source-package manifest

Date: 2026-08-12  
Lane: `MANUSCRIPT_STAGE4/LANE2_CANDIDATE_B_SOURCE_PACKAGE`  
Canonical version: `AMR-050-0035_CANONICAL_B_v1_2026-08-12`

## Package disposition

```text
MANUSCRIPT_SOURCE_FROZEN: YES
CANONICAL_BASE: B_CENTRAL_SYMMETRY__UNCHANGED
CROSS_PATCH_USED: NO
SOURCE_COMPARISON_COMPLETE: YES
STATIC_SOURCE_CHECKS: PASS
HOSTILE_SOURCE_AUDIT_REPAIRS: APPLIED__C14_N6_CARVEOUT__VERSION_OF_RECORD_BIBLIOGRAPHY
POST_REPAIR_INDEPENDENT_REAUDIT: PENDING
TEX_ENGINE_AVAILABLE: NO
PDF_COMPILED: NO
PDF_VISUALLY_INSPECTED: NO
MANUSCRIPT_PASS: NOT_YET__COMPILE_AND_PDF_AUDIT_PENDING
REPOSITORY_OR_PUBLIC_ACTION: NONE
```

## Members

| File | Purpose |
|---|---|
| `manuscript.tex` | Publication-quality `amsart` source with exact problem, corrected theorem, exact witness proof, priority, verification, and limits |
| `references.bib` | Bibliography for the authoritative target and credited prior components, including the explicit 2020 focal `N=6` precursor and corrected 2022 version-of-record metadata |
| `BUILD.md` | Build instructions and mandatory post-build audit |
| `CLAIM_SCOPE_AND_LIMITATIONS.md` | Exact permissible public scope and forbidden extrapolations |
| `SOURCE_TO_CANONICAL_COMPARISON.md` | Formula/claim mapping to Candidate B and frozen adjudications |
| `MANIFEST.md` | This inventory and disposition receipt |
| `SHA256SUMS.txt` | SHA-256 ledger for the six preceding files; self-excluded |
| `SHA256SUMS.txt.sha256` | Detached checksum for the ledger |

## Presentation and identity

- Document class: `amsart`, `a4paper`, 11 point.
- Margins: one inch via `geometry`.
- Abstract: six sentences.
- First page: exact arXiv-v11 problem and direct answer.
- Sole author identity: `DannyExperiments`.
- Affiliation: none.
- AI systems: disclosed as tools, not authors.

The 2026-08-12 hostile source audit's two editorial findings were applied
without changing any theorem, witness parameter, calculation, or proof step:
the focal `N=6`, `a/b=2` one-focus experimental precursor is now named and
directly cited, and the Garcia--Reznik 2022 entry now distinguishes its
version-of-record title and metadata from the older arXiv preprint title.

## Privacy and rights surface

The package is intended to be public-safe. It includes only original
manuscript text, bibliographic metadata, public URLs, public mathematical
claims, and cryptographic identifiers. It contains no source PDFs, images,
raw prompts, chat URLs, browser data, personal paths, email addresses,
credentials, cookies, tokens, or private keys.

Third-party works are referenced rather than redistributed. No license or
public repository action is part of this lane.

## Integrity policy

`SHA256SUMS.txt` hashes every substantive member exactly once and excludes
itself to avoid recursive self-reference. `SHA256SUMS.txt.sha256` hashes the
ledger. Any source edit invalidates both layers and requires a new freeze.
