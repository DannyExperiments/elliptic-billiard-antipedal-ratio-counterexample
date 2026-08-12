# Accepted authorless PDF preflight

Audit date: 2026-08-12.

Status: `PASS__CURRENT_AUTHORLESS_SOURCE__6_OF_6_PAGES`.

This receipt accepts the exact authorless PDF built from the frozen current
manuscript source. It supersedes the earlier pre-template-parity PDF and the
rejected first authorless build. The mathematical theorem, proof, formulas,
bibliography, priority boundary, and formalization scope are unchanged.

## Exact accepted build identity

- private draft-PR head:
  `941a1be9f05e8a92b0c1ab9c9523238ad85b1308`;
- exact source tree:
  `c3756e05c55313b7b1935d79d7cbf893df9f41b8`;
- GitHub Actions run: `31575265707` (`PDF build`);
- job: `94045853460` (`Rebuild manuscript PDF`);
- artifact: `9132969036` (`manuscript-pdf`);
- artifact ZIP SHA-256:
  `66277970b15456ae7062ffe24ac5c1d588d71be47fe55c16064d22d680f0a532`;
- source TeX SHA-256:
  `032ece89a0158b9eb7537ae085b0e1f2159607aaf6817f2a1bf57bf305e06ba0`;
- bibliography SHA-256:
  `6ab2dd7504ca52f188549c2cc255a0adb9859b2f6e658fdae3febe6a04c53d62`;
- accepted PDF SHA-256:
  `02c377df84aa9f1d94bbd1d1eee4ce56fc3fe9f9330bf5b31005a20601678a47`;
- build-log SHA-256:
  `f2e92f898fdc65ca616e360c91610471c64ca4eb52b4f3fccc3e050c8abb85d9`;
- extracted-text SHA-256:
  `631cb2520e8b7a84cab913cf83bcee7ed1f85f9e87bdcf1379a87f38e1cf84ce`.

The downloaded artifact ZIP digest exactly matched GitHub's reported digest.
Its CRC test passed, and it contained exactly `manuscript.pdf` and
`manuscript.log`.

All four workflows passed on the exact accepted-source head:

- repository integrity: run `31575265658`;
- exact Python replay: run `31575265736`;
- partial Lean certificate: run `31575265659`;
- PDF rebuild: run `31575265707`.

## Build and content checks

- clean checksum-pinned build: `PASS`;
- unresolved citations or references: `NONE`;
- multiply defined labels: `NONE`;
- TeX errors: `NONE`;
- overfull or underfull boxes: `NONE`;
- page count and format: `6`, A4, PDF 1.7;
- source-to-rendered theorem and scope parity: `PASS`;
- exact problem, supporting-line convention, `0/0` conclusion, half-ray
  exclusion, journal-number exclusion, priority qualification, and partial
  Lean boundary: `PRESENT`;
- extracted text: `328` lines, `2593` words, `16569` bytes.

The extracted body text agrees with the first authorless build. The only
rendered-text change is the intended running header `FOCAL ANTIPEDAL AREAS`.

## Visual inspection

Every page was rendered independently at 180 DPI and inspected for clipping,
overlap, malformed glyphs, broken equations, bad page breaks, missing
citations, and bibliography overflow. Result: `PASS__6_OF_6_PAGES`.

Rendered-page SHA-256 values:

1. `d14a78b43b933e8dfd44574258a2b81df4d1d4eb455c6c95f32be983bcbcf8e5`
2. `d18250cd37b2636c6f202e9f3e50dd781bd97a965c27c8e1b791dbaf43a4681a`
3. `4c6b6796bf8f1a8888b56fe7a71486abd607d5063a562fa528cdfad9b8715133`
4. `931e079923af0713899abb61409048d19027458d6456a53c98766599eb005a3e`
5. `151857ec686f8c66b239bb961c2e00fd7ced56b49d7ed9a2724a6ba8f15b673a`
6. `9502c140a4cd3e2c34b5df64e21d1f8ce092e6abfa835587df0a17ec68a77fec`

The explicit identical running-title marks render cleanly on pages 2--6.
No page has clipping, overlap, missing glyphs, broken references, or privacy
material.

## Metadata and privacy

- title: blank;
- subject: blank;
- keywords: blank;
- author: blank;
- creator: `LaTeX with hyperref`;
- producer: `pdfTeX-1.40.28`;
- encrypted: no;
- forms, JavaScript, embedded files, or images: none;
- private paths, chat links, email addresses, private account identifiers,
  credentials, secrets, screenshots, raw prompts, or raw research receipts:
  none detected in metadata, extracted text, binary strings, or rendered
  pages.

## Rejected historical build

The first authorless build at private PR head
`5378131839880e54e3823cd2328c6105c72a9762` compiled and had blank identity
metadata, but manual inspection rejected it because the default empty `amsart`
author mark produced clipped fragments on even pages 4 and 6. Its PDF SHA-256
was `704d312e34a1b5fd044fde066c65a3a127d50c700204b44a06c55086ef89570d`.
It is not integrated or accepted.

## Disposition

```text
MANUSCRIPT_CLEAN_BUILD: PASS
SOURCE_TO_PDF_PARITY: PASS
VISUAL_PREFLIGHT: PASS__6_OF_6_PAGES
PDF_METADATA_PRIVACY: PASS
ACCEPTED_PDF_SHA256: 02c377df84aa9f1d94bbd1d1eee4ce56fc3fe9f9330bf5b31005a20601678a47
RELEASE_PDF_APPROVED_FOR_CURRENT_SOURCE: YES
PDF_INTEGRATION_HEAD_CI: PENDING
```

This receipt accepts the exact PDF as the candidate-tree artifact. The next
commit integrates these bytes and this receipt; all four workflows must pass
again on that exact integration head. This receipt does not claim human peer
review, absolute priority, public visibility, an immutable release, or a DOI.
