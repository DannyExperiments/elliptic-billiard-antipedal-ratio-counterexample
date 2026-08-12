# Stage-4 manuscript source-package manifest

Date: 2026-08-12  
Lane: `MANUSCRIPT_STAGE4/LANE2_CANDIDATE_B_SOURCE_PACKAGE`  
Canonical version: `AMR-050-0035_CANONICAL_B_v1_2026-08-12`  
Public derivative: `AUTHORLESS_TEMPLATE_PARITY_EDIT_1`

## Package disposition

```text
MANUSCRIPT_SOURCE_FROZEN: YES__EDITORIAL_DERIVATIVE
CANONICAL_BASE: B_CENTRAL_SYMMETRY__UNCHANGED
CROSS_PATCH_USED: NO
SOURCE_COMPARISON_COMPLETE: YES
STATIC_SOURCE_CHECKS: PASS
HOSTILE_SOURCE_AUDIT_REPAIRS: APPLIED__C14_N6_CARVEOUT__VERSION_OF_RECORD_BIBLIOGRAPHY
POST_REPAIR_INDEPENDENT_REAUDIT: PASS__REPORT_SHA256_CA8AC13832EB37C486DF0740BF938ECC620C34640C99B5B499F53FF155C9A0FD
FIRST_REMOTE_CLEAN_BUILD: PASS__COMMIT_33EEEF1268954056B0616394F07549D0DC5B086F
FIRST_PDF_VISUAL_AND_PRIVACY_AUDIT: PASS__6_OF_6_PAGES__PDF_SHA256_89B57F280EC8A18F18627E9CFC594C4FD6EE28F37E672816DD30614492FE599A
METADATA_ONLY_PDF_SUBJECT_REPAIR: APPLIED__VISIBLE_MATHEMATICS_UNCHANGED
CURRENT_SOURCE_REPLACEMENT_BUILD: PASS__COMMIT_1C29524A5EB5745CBF785C76E40018BBB979316D__RUN_31570217856
REPLACEMENT_PDF_VISUAL_AND_PRIVACY_AUDIT: PASS__6_OF_6_PAGES__PRE_TEMPLATE_PARITY_SOURCE
AUTHORLESS_TEMPLATE_PARITY_EDIT: APPLIED__NO_MATHEMATICAL_CHANGE
CURRENT_SOURCE_CLEAN_BUILD: PENDING_EXACT_HEAD_CI
CURRENT_SOURCE_VISUAL_AND_PRIVACY_AUDIT: PENDING
MANUSCRIPT_PASS: PENDING__CURRENT_SOURCE_REBUILD_AND_PREFLIGHT
REPOSITORY_ACTION: PRIVATE_DRAFT_PR_1__EDITORIAL_PARITY_REBUILD_PENDING
```

## Members

| File | Purpose |
|---|---|
| `manuscript.tex` | Publication-quality `amsart` source with exact problem, corrected theorem, exact witness proof, priority, verification, and limits |
| `references.bib` | Bibliography for the authoritative target and credited prior components, including the explicit 2020 focal `N=6` precursor and corrected 2022 version-of-record metadata |
| `BUILD.md` | Build instructions and mandatory post-build audit |
| `CLAIM_SCOPE_AND_LIMITATIONS.md` | Exact permissible public scope and forbidden extrapolations |
| `SOURCE_TO_CANONICAL_COMPARISON.md` | Formula/claim mapping to Candidate B and frozen adjudications |
| `CHANGELOG_FROM_CANONICAL_PROOF.md` | Source-audit and authorless-template editorial delta record |
| `MANIFEST.md` | This inventory and disposition receipt |
| `SHA256SUMS.txt` | SHA-256 ledger for the seven preceding files; self-excluded |
| `SHA256SUMS.txt.sha256` | Detached checksum for the ledger |

## Presentation and identity

- Document class: `amsart`, `a4paper`, 11 point.
- Margins: one inch via `geometry`.
- Abstract: six sentences.
- First page: exact arXiv-v11 problem and direct answer.
- Article byline, affiliation, and date: empty, matching the established recent
  solve-repository paper convention.
- PDF identity metadata: source leaves title, subject, keywords, and author
  fields blank.
- Repository and preferred-citation identity: `DannyExperiments` in the root
  `CITATION.cff`, with no affiliation.
- AI systems: documented in the root disclosure and provenance files, never
  listed as authors or human peer reviewers.

The 2026-08-12 hostile source audit's two editorial findings were applied
without changing any theorem, witness parameter, calculation, or proof step:
the focal `N=6`, `a/b=2` one-focus experimental precursor is now named and
directly cited, and the Garcia--Reznik 2022 entry now distinguishes its
version-of-record title and metadata from the older arXiv preprint title. A
separate independent re-audit passed on exact report SHA-256
`ca8ac13832eb37c486df0740bf938ecc620c34640c99b5b499f53ff155c9a0fd`.

The first clean remote build on commit `33eeef1268954056b0616394f07549d0dc5b086f`
produced a six-page PDF that passed complete rendered-page, content, metadata,
and privacy inspection. That build exposed one harmless Hyperref bookmark
warning caused solely by the underscore in the PDF subject string. The
subject metadata was changed from `k_607` to `k607`; no visible manuscript,
theorem, proof, reference, or mathematical dependency changed. The replacement
clean build on private PR head `1c29524a5eb5745cbf785c76e40018bbb979316d`
passed the focused content, metadata, privacy, and complete six-page visual
audit. The accepted PDF is recorded separately in the repository-level ledger
and `PDF_PREFLIGHT.md`; the nested ledger remains a source-package identity.
The accepted-PDF integration head
`bfe5e31a9ed5ef315bfeb9ee016024e15a10a341` subsequently passed all four
workflows, and its rebuild had byte-identical extracted text and pixel-identical
renders on all six pages.

The later repository-template comparison found that the recent mature solve
papers are authorless and keep repository/preferred-citation authorship on the
root metadata surface. The public derivative therefore removes only the
article byline, date, explicit PDF identity metadata, and manuscript-local AI
production paragraph. The theorem, abstract, proof, formulas, bibliography,
priority boundary, computation/formalization description, and exclusions are
unchanged. The previously accepted PDF remains a historical audit artifact
but is superseded for release until the current exact source is rebuilt and
passes a new complete visual, metadata, privacy, and source-parity audit.

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
