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

The tracked `manuscript.pdf` is the last accepted pre-template-parity artifact
from private PR head `1c29524a5eb5745cbf785c76e40018bbb979316d`. It passed a clean
checksum-pinned build, source parity, metadata/privacy inspection, and visual
inspection of all six rendered pages. `PDF_PREFLIGHT.md` binds the source,
workflow, artifact, log, PDF, extracted text, and rendered-page hashes. The
accepted-PDF integration head passed all four workflows; its PDF rebuild had
byte-identical extracted text and pixel-identical renders on all six pages.
It is superseded for release because the current source removes only the
article byline, explicit identity metadata, date, and manuscript-local AI
production paragraph to match the mature solve-paper template. A replacement
clean build and complete six-page audit are pending; no mathematical text was
changed.
