# Manuscript staging

The exact frozen Stage-4 Candidate-B source package is integrated here
byte-for-byte. Its nested `MANIFEST.md`, `SHA256SUMS.txt`, and detached
`SHA256SUMS.txt.sha256` preserve the source-freeze identity independently of
the repository-level manifest.

Source members:

- `manuscript.tex` and `references.bib`;
- `BUILD.md`;
- `CLAIM_SCOPE_AND_LIMITATIONS.md`;
- `SOURCE_TO_CANONICAL_COMPARISON.md`; and
- the nested manifest and checksum receipts.

The manuscript states the exact arXiv-v11 problem, corrected complete-line
theorem, exact primitive `N=8` certificate, computation/formalization boundary,
bounded prior-art language, exclusions, authorship, and AI disclosure. It uses
Candidate B unchanged as its only proof base; no Candidate-A/C cross-patch was
introduced.

No accepted PDF is present in the repository. The first external CI artifact
passed clean-build, text-parity, metadata/privacy, and all-page rendered
inspection. A metadata-only PDF-subject repair now requires one replacement
build and focused delta audit before repository integration or release-PDF
approval. See `BUILD_STATUS.md` and `BUILD.md`.
