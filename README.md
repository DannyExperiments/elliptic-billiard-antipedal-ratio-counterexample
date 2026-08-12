# A domain counterexample for a focal-antipedal area ratio

[![Verify public evidence](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/actions/workflows/verify.yml)
[![Exact verifier replay](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/actions/workflows/replay-exact-verifier.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/actions/workflows/replay-exact-verifier.yml)
[![PDF build](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/actions/workflows/pdf.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/actions/workflows/pdf.yml)
[![Partial finite exact certificate (Lean)](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/actions/workflows/lean-finite-certificate.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/actions/workflows/lean-finite-certificate.yml)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21907169-blue.svg)](https://doi.org/10.5281/zenodo.21907169)

An exact primitive one-winding `N=8` elliptic-billiard orbit makes both focal
signed antipedal areas zero under the complete supporting-line construction.
Consequently, the unqualified quotient in arXiv-v11 row `k_607` is `0/0` at
that phase. The corrected theorem is stronger in period scope: for every exact
even orbit with finite supporting-line intersections, the two focal antipedal
polygons are half-turn images, their signed areas agree, and their quotient is
`1` wherever the common area is nonzero.

## Original problem

Row `k_607` of Dan Reznik, Ronaldo Garcia, and Jair Koiller,
“Eighty New Invariants of N-Periodics in the Elliptic Billiard,” asserts that
the quotient of the two focal signed antipedal areas is `1` when the period is
divisible by four. The arXiv-v11 row supplies no nonzero-denominator clause and
marks the proof status `?`.

Authoritative source:
[arXiv:2004.12497v11](https://arxiv.org/abs/2004.12497v11).
Problem-page cross-reference:
[UnsolvedMath AMR-050-0035](https://www.unsolvedmath.com/problems/AMR-050-0035).

## Exact result

Let `N=2m`, let the billiard orbit be centrally symmetric, and use complete
lines through each orbit vertex perpendicular to the vertex-to-focus segment.
When all consecutive intersections are finite, the half-turn about the ellipse
center maps one ordered focal antipedal polygon to the other with an index
shift of `m`. Hence their cyclic signed areas are equal.

The audited exact `N=8` certificate locates one noncircular, nondegenerate,
primitive one-winding configuration where both signed areas vanish. This is a
domain counterexample to the unqualified quotient, not a nonunit quotient and
not a counterexample to the signed-area identity.

[Problem and proof scope](PROBLEM_AND_PROOF.md) ·
[Canonical claim](canonical/CANONICAL_CLAIM.md) ·
[Status](STATUS.md) ·
[Claims/evidence matrix](CLAIMS_EVIDENCE_MATRIX.md) ·
[Reproducibility](REPRODUCIBILITY.md) ·
[Citation status](CITATION_STATUS.md)

## Read the result

- [Manuscript PDF](paper/manuscript.pdf)
- [TeX source](paper/manuscript.tex)
- [Problem and proof scope](PROBLEM_AND_PROOF.md)
- [Claim scope and limitations](paper/CLAIM_SCOPE_AND_LIMITATIONS.md)
- [Canonical dependency map](canonical/DEPENDENCY_MAP.md)
- [Claims/evidence matrix](CLAIMS_EVIDENCE_MATRIX.md)

The PDF follows the established solve-repository convention: the article is
authorless, while repository and preferred-citation authorship are recorded
as `DannyExperiments` in `CITATION.cff`. AI assistance is documented only on
the repository disclosure surface, not presented as article authorship or
peer review.

## Reproduce the public-safe evidence

```bash
bash scripts/verify.sh --integrity-only
python3 -B verification/verify_k607_stdlib.py
```

The repository check verifies the exact allowlist, hashes, public-safe
evidence, manuscript identity, privacy rules, and release gates. The exact
verifier checks the finite `N=8` certificate. Neither command substitutes for
the analytic proof, mathematical audit, human peer review, or the explicitly
scoped Lean artifact.

## Verification status

| Gate | Current status |
|---|---|
| Mathematical audit | Passed for the complete supporting-line theorem and exact `N=8` certificate |
| Literal single half-rays | Not proved; the witness does not form the required cyclic polygon |
| Priority | Passed with bounded language: exact `N=8` certificate apparently new after a three-lane search through 2026-08-12 |
| Public verifier | Fail-closed standard-library exact replay passes in ordinary and optimized modes; integrity-only mode also verifies its frozen output |
| Exact evidence | Deterministic public-safe certificate archive and detached SHA-256 sidecar integrated |
| Manuscript | Authorless source matches the mature solve template; the current six-page PDF passed its clean build, source-parity check, blank-metadata/privacy audit, and complete 6/6 visual inspection |
| Formalization | Integrated partial finite exact Lean certificate builds and kernel-checks; the real/topological bridge and full theorem are not formalized |
| Peer review | No human specialist or journal peer review is claimed |
| Repository | Public protected `main`; all four release-commit workflows passed at `d577ee6b199f5954dc74893834820df2656d56cb` |
| Release | Immutable GitHub Version 1.0.0 published; all six public assets anonymously re-downloaded and hash-verified |
| DOI | Version DOI `10.5281/zenodo.21907170` and concept DOI `10.5281/zenodo.21907169` resolve; all six Zenodo files match the GitHub release bytes |

## Strict scope

This project does not claim:

- unequal focal signed areas or a defined quotient different from `1`;
- zero-area phases for any period other than the certified `N=8` case;
- a classification, uniqueness theorem, or stability theorem for the zero
  locus;
- an unsigned-area theorem;
- a literal half-ray theorem;
- a result for another caustic, odd period, neighboring invariant row, or the
  differently numbered journal formula; or
- a second named open problem.

## Repository map

- `canonical/`: exact public-safe theorem, dependency map, and limitations.
- `audits/public_safe_reports/`: sanitized audit summaries only.
- `evidence/`: deterministic public-safe certificate archive and sidecar; no
  private evidence.
- `verification/`: independent exact standard-library verifier, expected
  output, and replay receipt.
- `paper/`: frozen manuscript source package, accepted PDF, bibliography,
  source-to-canonical comparison, and exact PDF-preflight receipt.
- `.github/workflows/pdf.yml`: pinned clean manuscript build that uploads the
  PDF and build log for independent inspection; it does not itself accept the
  manuscript.
- `formalization/`: integrated partial Lean certificate, strict scope
  boundary, and reserved Aristotle slot.
- `release/`: human approvals, workflow activation, and immutable-release gates.
- `scripts/`: standard-library allowlist, checksum, privacy, and release-gate
  checks.

## Authorship, disclosure, and rights

Repository and preferred-citation authorship use the established public
convention `DannyExperiments`, with no affiliation listed; the mathematical
article itself is authorless. AI assistance is disclosed in
[AI_DISCLOSURE.md](AI_DISCLOSURE.md). No repository-wide reuse license is
granted; all rights are reserved as described in
[LICENSE_STATUS.md](LICENSE_STATUS.md).

## Release status

The exact result is archived in the
[immutable GitHub Version 1.0.0 release](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/releases/tag/v1.0.0)
and at the [version DOI](https://doi.org/10.5281/zenodo.21907170). The
[concept DOI](https://doi.org/10.5281/zenodo.21907169) represents all Zenodo
versions. The release tag remains fixed at protected-main commit
`d577ee6b199f5954dc74893834820df2656d56cb`; current-main DOI metadata does not
alter the immutable assets. Any external problem-site notice remains separately
unapproved. See [STATUS.md](STATUS.md) and
[release/README.md](release/README.md).
