# Manuscript staging

The mathematically unchanged public editorial derivative of the frozen
Stage-4 Candidate-B source package is integrated here. Its nested
`MANIFEST.md`, `SHA256SUMS.txt`, and detached `SHA256SUMS.txt.sha256` preserve
the exact derivative identity independently of the repository-level manifest.

Source members:

- `manuscript.tex` and `references.bib`;
- `BUILD.md`;
- `CLAIM_SCOPE_AND_LIMITATIONS.md`;
- `SOURCE_TO_CANONICAL_COMPARISON.md`;
- `CHANGELOG_FROM_CANONICAL_PROOF.md`; and
- the nested manifest and checksum receipts.

The manuscript states the exact arXiv-v11 problem, corrected complete-line
theorem, exact primitive `N=8` certificate, computation/formalization boundary,
bounded prior-art language, and exclusions. It uses Candidate B unchanged as
its only proof base; no Candidate-A/C cross-patch was introduced. The article
itself is authorless; root citation and disclosure files carry the repository
identity and AI-production record.

The tracked `manuscript.pdf` is the accepted authorless artifact built from the
current exact source at private PR head
`941a1be9f05e8a92b0c1ab9c9523238ad85b1308`. It passed a clean
checksum-pinned build, source parity, blank-identity metadata and deep privacy
inspection, and visual inspection of all six 180-DPI rendered pages.
`PDF_PREFLIGHT.md` binds the source, workflow, artifact, log, PDF, extracted
text, and rendered-page hashes. No mathematical text changed during the
authorless-template or running-header repairs. The later commit integrating
this PDF passed all four workflows; its rebuild had byte-identical text and
pixel-identical renders on all six pages. The final receipt-only head must
repeat all four workflows before merge.
