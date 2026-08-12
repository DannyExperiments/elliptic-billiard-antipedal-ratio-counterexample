# Stage-4 manuscript build instructions

The nested checksum package freezes the manuscript source and comparison
records. The repository also tracks `manuscript.pdf` and its independent
`PDF_PREFLIGHT.md`; those two files are intentionally outside the nested
source ledger and are covered by the root ledger.

The current authorless editorial derivative compiled successfully in
checksum-pinned private CI at exact head
`941a1be9f05e8a92b0c1ab9c9523238ad85b1308`. Its six-page PDF passed source
parity, clean-log review, blank-identity metadata and deep privacy inspection,
and complete visual inspection at 180 DPI. The exact receipt is
`PDF_PREFLIGHT.md`; the later PDF-integration head must repeat all four
workflows before merge.

## Expected toolchain

- a current TeX Live distribution;
- `latexmk`, or `pdflatex` plus `bibtex`;
- standard packages `amsmath`, `amssymb`, `mathtools`, `geometry`,
  `microtype`, and `hyperref`.

The repository workflow uses a commit-pinned LaTeX action and an exact
TeX Live container digest. No package manager, installer, or dependency fetch
is run on the local staging host.

## Rebuild

From this directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
```

The equivalent explicit sequence is:

```sh
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

## Required post-build gate

A later production lane must, before accepting any PDF:

1. build in a clean directory from only the files in this package;
2. reject undefined citations/references, multiply defined labels, TeX errors,
   and material box warnings;
3. inspect every rendered page for clipping, overlap, bad breaks, malformed
   symbols, and bibliography defects;
4. extract text and compare the theorem, root interval, witness coordinates,
   supporting-line qualification, `0/0` conclusion, journal-numbering
   exclusion, and novelty statement against the frozen source;
5. inspect PDF metadata and scan for private paths or personal information;
6. record source, bibliography, log, and PDF SHA-256 values.

No source-package checksum should be treated as a PDF-build or visual-review
receipt.
