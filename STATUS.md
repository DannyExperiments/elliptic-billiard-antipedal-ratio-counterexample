# Status

Status date: 2026-08-12.

Current repository state: `RELEASE_AND_DOI_CLOSED`.

Public release gate: `RELEASE_AND_DOI_CLOSED`.

| Dimension | State | Exact meaning |
|---|---|---|
| Source target | `VERIFIED` | The target is arXiv:2004.12497v11 row `k_607`, not the differently formulated 2021 journal row. |
| Mathematical audit | `MATH_AUDIT_PASS_QUALIFIED` | Complete supporting lines, finite intersections, all-even signed identity, and the exact admissible `N=8` common-zero certificate passed independent audit. |
| Named-problem scope | `ONE_TARGET` | AMR-050-0035 and arXiv-v11 `k_607` are the same target. No second problem is claimed. |
| Implications | `PASS_WITH_STRICT_SCOPE` | The half-turn congruence and its signed-area/domain corollaries are supported; broader zero-locus, period, caustic, ray, and unsigned-area claims are excluded. |
| Priority | `PRIORITY_PASS_QUALIFIED` | The three-lane adjudication found no exact collision; “apparently new after a documented three-lane search through 2026-08-12” is the strongest authorized language. |
| Exact evidence | `INTEGRATED_REPLAY_PASS` | Deterministic public-safe archive, detached hash, inspected fail-closed verifier, expected output, and frozen replay receipt are integrated. Ordinary and optimized replays byte-match. |
| Manuscript source | `AUTHORLESS_EDITORIAL_DERIVATIVE_STATIC_PASS` | The Candidate-B proof is mathematically unchanged. The public derivative removes only article identity/date metadata and manuscript-local AI-production prose to match the established solve-paper template. |
| Manuscript PDF | `CURRENT_AUTHORLESS_PDF_AUDIT_PASS` | The exact current source built cleanly; the accepted six-page PDF passed source parity, blank-identity metadata and deep privacy scans, and complete 6/6 rendered-page inspection. |
| Formalization | `PARTIAL_LEAN_INTEGRATED_PASS` | The dependency-free Lean 4.30.0 finite certificate builds, passes `leanchecker`, exact axiom comparison, and no-escape scanning. It does not formalize the full real-geometric theorem. No Aristotle artifact is claimed. |
| Peer review | `NOT_OBTAINED` | AI mathematical audits are not human peer review. |
| Authorship | `DANNYEXPERIMENTS_APPROVED` | Repository and preferred-citation authorship use the established public convention, with no affiliation. |
| License | `ALL_RIGHTS_RESERVED` | No repository-wide reuse license is granted. |
| Public main | `PASS_EXACT_RELEASE_COMMIT` | Release-candidate PR #2 was squash-merged through protection to `d577ee6b199f5954dc74893834820df2656d56cb`. Fresh public-main runs all passed: repository integrity `31617801307`, exact replay `31617800526`, PDF build `31617800543`, and partial Lean `31617801245`. |
| Protected main | `PASS` | Pull requests, all four exact required checks, up-to-date branches, conversation resolution, linear history, and administrator non-bypass are enforced; force pushes and deletions are disabled. |
| Public release | `V1_RELEASE_PUBLISHED` | Immutable GitHub Version 1.0.0 (release ID `369384507`) was published from `d577ee6b199f5954dc74893834820df2656d56cb` on 2026-08-12. The tag and all six uploaded assets were anonymously re-read and hash-verified; the evidence ZIP passed integrity testing. |
| DOI | `DOI_DEPOSITED` | Version DOI `10.5281/zenodo.21907170` and concept DOI `10.5281/zenodo.21907169` resolve; DataCite reports both findable, and all six Zenodo files byte-match the immutable GitHub assets. |

## Release state

`DOI_DEPOSITED`, `PUBLIC_TIMESTAMPED`, `MANUSCRIPT_PASS`,
`FORMALIZATION_PARTIAL`, and `PRIORITY_PASS_QUALIFIED`.

The immutable
[`v1.0.0` release](https://github.com/DannyExperiments/elliptic-billiard-antipedal-ratio-counterexample/releases/tag/v1.0.0)
and [Zenodo deposit](https://zenodo.org/records/21907170) are complete.
Repository release immutability and protected `main` remain enabled. External
problem-page notice is the only release-adjacent gate still unapproved; it is
not required for release-and-DOI closure.
