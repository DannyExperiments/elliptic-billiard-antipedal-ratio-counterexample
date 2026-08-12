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

`manuscript.pdf` is the exact accepted replacement artifact from private PR
head `1c29524a5eb5745cbf785c76e40018bbb979316d`. It passed a clean
checksum-pinned build, source parity, metadata/privacy inspection, and visual
inspection of all six rendered pages. `PDF_PREFLIGHT.md` binds the source,
workflow, artifact, log, PDF, extracted text, and rendered-page hashes. The
accepted-PDF integration head passed all four workflows; its PDF rebuild had
byte-identical extracted text and pixel-identical renders on all six pages.
