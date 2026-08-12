# Stage-4 manuscript build instructions

This directory is a source freeze. No PDF is part of this package and no
successful TeX compilation is claimed.

## Expected toolchain

- a current TeX Live distribution;
- `latexmk`, or `pdflatex` plus `bibtex`;
- standard packages `amsmath`, `amssymb`, `mathtools`, `geometry`,
  `microtype`, and `hyperref`.

No TeX engine was available on the source-freeze host. In accordance with the
release gate, no package manager, installer, or dependency fetch was run.

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
