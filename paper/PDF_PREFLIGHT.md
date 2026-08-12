# Accepted PDF preflight

Audit date: 2026-08-12.

Status: `SUPERSEDED_FOR_RELEASE__AUTHORLESS_TEMPLATE_PARITY_REBUILD_PENDING`.

This receipt remains the exact audit record for the tracked pre-template-parity
PDF. The current TeX differs only by removal of the article byline, date,
explicit PDF identity metadata, and manuscript-local AI production paragraph.
That editorial derivative requires a new exact clean build and complete PDF
preflight before release; none of the mathematical findings below is revoked.

The first authorless rebuild at private PR head
`5378131839880e54e3823cd2328c6105c72a9762`, run `31574483418`, compiled
successfully and had blank identity metadata, but visual preflight rejected it:
the `amsart` even-page running mark rendered as clipped fragments on pages 4
and 6. That PDF (SHA-256
`704d312e34a1b5fd044fde066c65a3a127d50c700204b44a06c55086ef89570d`)
is not integrated or accepted. The source now carries an explicit identical
short-title mark on both sides and requires another clean build plus complete
six-page inspection.

## Exact build identity

- private PR head: `1c29524a5eb5745cbf785c76e40018bbb979316d`;
- GitHub Actions run: `31570217856` (`PDF build`);
- job: `94030399023` (`Rebuild manuscript PDF`);
- artifact: `9131061650` (`manuscript-pdf`);
- artifact ZIP SHA-256:
  `bbc191d5af77fe520425555c776a7116021f17cbe490156501771a011133bbd5`;
- source TeX SHA-256:
  `dc82e016bb8fe7567f3283818d542d391b48a7a3aef9488677a657ef7c3089b0`;
- bibliography SHA-256:
  `6ab2dd7504ca52f188549c2cc255a0adb9859b2f6e658fdae3febe6a04c53d62`;
- accepted PDF SHA-256:
  `998ba5f77cb8d94a69e4dc7e089f5dd8a2b314aac7b8f77f677d95553064c7cd`;
- build-log SHA-256:
  `5adf949f7acd9e5122d82550da91dcaa3a7712b67aae429fdd4f00036360a3f5`.

The downloaded artifact ZIP digest exactly matched GitHub's server-reported
digest. Its CRC test passed, and it contained exactly `manuscript.pdf` and
`manuscript.log`.

## Build and content checks

- clean pinned-container build: `PASS`;
- unresolved citations or references: `NONE`;
- multiply defined labels: `NONE`;
- TeX errors: `NONE`;
- overfull or underfull boxes: `NONE`;
- page count and format: `6`, A4, PDF 1.7;
- source-to-rendered theorem and scope parity: `PASS`;
- exact problem, supporting-line convention, `0/0` conclusion, half-ray
  exclusion, journal-number exclusion, priority qualification, and partial
  Lean boundary: `PRESENT`;
- extracted-text audit: `337` lines and `2674` words; SHA-256
  `c02191b8cca6aa9795be4aab78a7c3da74976a22e127bd2db5449cc48f90d670`.

The metadata-only replacement changed the PDF subject from the TeX-sensitive
`k_607` spelling to `k607`. No visible theorem, proof, reference, formula, or
scope statement changed.

## Visual inspection

Every page was rendered independently at 160 DPI and inspected for clipping,
overlap, malformed glyphs, broken equations, bad page breaks, missing
citations, and bibliography overflow. Result: `PASS__6_OF_6_PAGES`.

Rendered-page SHA-256 values:

1. `db104eaec9f3d42bcc4dd5b6aef898bfde5fc53e530f3b2d725b14c5896149d3`
2. `7e9c03c0b831fb2c8c2496c5b59a3b8cecd84863a6de7608fc197f1d7ebc496d`
3. `1bbd2c14b832168eff494280e232a9ac12d1d3695d3a2a3bb07a02430ced23bd`
4. `4f150f38353035cfb75b6c205905b8955e9b9cd1badfcc91bfbf3c3540b2c03f`
5. `811dac95a9a0d0f36af1ed00feaedb82fa95fc7eaabe95a287c26b2b3e732512`
6. `abf65555e0806ea2a42c17c59a98dcf7ad74080d4915ba6bc041b05c5419afb6`

## Metadata and privacy

- title: `An Exact Zero of Focal Antipedal Areas`;
- subject: `An exact domain counterexample to arXiv:2004.12497v11, row k607`;
- author: `DannyExperiments`;
- affiliation: none;
- creator: `LaTeX with hyperref`;
- producer: `pdfTeX-1.40.28`;
- encrypted: no;
- forms or JavaScript: none;
- private paths, chat links, email addresses, account identifiers, credentials,
  secrets, screenshots, or raw research receipts: none detected in metadata,
  extracted text, binary strings, or the rendered pages.

## Disposition

```text
MANUSCRIPT_CLEAN_BUILD: PASS
SOURCE_TO_PDF_PARITY: PASS
VISUAL_PREFLIGHT: PASS__6_OF_6_PAGES
PDF_METADATA_PRIVACY: PASS
ACCEPTED_PDF_SHA256: 998ba5f77cb8d94a69e4dc7e089f5dd8a2b314aac7b8f77f677d95553064c7cd
RELEASE_PDF_APPROVED_FOR_CANDIDATE_TREE: YES
```

This receipt accepts the exact PDF as a candidate-tree artifact. It does not
claim peer review, absolute priority, a public release, or a DOI.

## Integration-head replay

The accepted PDF was then integrated at private PR head
`bfe5e31a9ed5ef315bfeb9ee016024e15a10a341`, exact Git tree
`e650e7acd82bcec95f8b0a6cdf561f9f35fb22eb`. All four workflows passed:

- repository integrity: run `31570981780`, job `94032731653`;
- exact Python replay: run `31570981838`, job `94032731648`;
- partial Lean certificate: run `31570981822`, job `94032731711`;
- PDF rebuild: run `31570981790`, job `94032731680`.

The integration-head PDF artifact `9131363607` had ZIP SHA-256
`69f98c86daed8c331d522aa1071a0cf4381182eff07bcf0cfe67f4edc600f9ad`.
Its rebuilt PDF SHA-256 was
`77fe9f661b21b97d067d4bab0258dc56573a8fb3a677399d03e32771c1c018e7`;
the byte difference from the accepted PDF is the expected build timestamp.
The extracted text was byte-identical at SHA-256
`c02191b8cca6aa9795be4aab78a7c3da74976a22e127bd2db5449cc48f90d670`,
and all six 160-DPI rendered pages were pixel-identical to the accepted-page
renders. The integration rebuild therefore confirms exact visible-content and
scope parity without replacing the accepted artifact.
