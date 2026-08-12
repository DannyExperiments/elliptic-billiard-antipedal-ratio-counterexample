# Repository-template and privacy audit

Audit date: 2026-08-12.

## Comparison set

The candidate was compared against fresh read-only clones of the live public
default branches of these established solve repositories:

- `DannyExperiments/a211420-fixed-divisor` at `2a83d67b13a8c61cf93e650e659fa57b0a477d19`;
- `DannyExperiments/imbalance-conjecture` at `5798b1e1eee926432d3b173f7b0aceef440373e8`;
- `DannyExperiments/finite-coset-union-complement` at `a4a022f49f3bbc382ca5fd96094244adf03be3a5`;
- `DannyExperiments/rubel-l-atoms` at `65b6668e63e7fa3aec7ff28e36396f0a59af2aa9`;
- `DannyExperiments/planar-strict-convex-hyperrigidity` at `1cabf87c796c0963c175e5313e66542c3161a254`;
- `DannyExperiments/generalized-brannan-counterexample` at `4f979fd163dde72e21d47c08ad20b4669b0c6f52`;
- `DannyExperiments/random-series-parallel-distance-exponent` at `a875da08e8bfbdb70fd8165c097ab036731b5f6f`;
- `DannyExperiments/dodecahedron-short-geodesic-counterexample` at `485db7db26b0be2528f0b8fa578de6085f770584`;
- `DannyExperiments/ottaviani-shapiro-sos-counterexample` at `41e3d18a8c536e5a859201afd5faefe2b0ecd315`; and
- `DannyExperiments/rectangular-lattice-landau-extremal` at `3563ab11800c2600a70764cacc9fa7bc1870a9e4`.

The last four repositories supply the controlling modern release template;
older repositories were used to detect stable conventions and historical
exceptions rather than to copy obsolete release mechanics.

## Template parity

The candidate contains the common theorem-release surfaces:

- theorem-first `README.md`, exact status, problem/proof statement, claims
  matrix, provenance, reproducibility, security, contributing, citation, AI
  disclosure, and all-rights-reserved files;
- `amsart`, A4, one-inch-margin TeX source, bibliography, tracked PDF, build
  instructions, source comparison, scope limitations, and PDF preflight;
- public-safe mathematical, literature/priority, and implications audits;
- deterministic exact evidence, a fail-closed standard-library verifier, an
  exact replay receipt, and a strict computation boundary;
- a partial Lean certificate with pinned toolchain, zero-package manifest,
  exact axiom output, kernel check, and explicit nonformalized bridges;
- separate integrity, exact-replay, PDF, and scoped-Lean workflows; and
- fail-closed human, protected-main, immutable-release, DOI, badge, and
  external-notice gates.

The article source was normalized to the recent solve convention: no
article byline, affiliation, date, or author identity in PDF metadata.
`DannyExperiments` remains only the established repository and
preferred-citation identity in `CITATION.cff`. AI assistance remains in the
separate disclosure/provenance surfaces. No DOI, badge, release version, or
publication claim is activated while the repository is private.

The previously tracked six-page PDF belongs to the pre-normalization source.
It remains a valid historical audit artifact but is superseded for release;
template parity is not complete until the authorless source is rebuilt and
the exact replacement PDF passes source, metadata, privacy, and complete
rendered-page inspection.

The first authorless rebuild compiled and passed its automated log gate, but
manual rendered-page inspection found clipped `amsart` running-mark fragments
on even pages 4 and 6. It was rejected. The source now uses the same explicit
short-title mark on both sides, following the established authorless
solve-paper pattern; that repaired PDF remains pending exact-head rebuild and
complete visual inspection.

Release-asset files and a write-enabled publishing workflow are deliberately
not treated as present-tense accomplishments. They are built only after the
final public-main bytes, citation metadata, branch protection, and explicit
human release approval are frozen.

## Privacy and rights checks

The exact allowlisted tree, private draft-PR body and comments, current PR
diff, known remote commit payloads, manuscript source, PDF metadata and raw
bytes, deterministic evidence ZIP, and every textual ZIP member were checked
for:

- personal names or private account domains outside the authorized public
  handle;
- email addresses, user-home paths, temporary paths, private chat or share
  URLs, attachment identifiers, internal search citations, UUID-like receipt
  identifiers, and local file URLs;
- tokens, private keys, generic API secrets, credentials, cookies, and wallet
  material;
- screenshots, source PDFs, third-party figures, symlinks, traversal paths,
  encrypted archive members, and generated caches; and
- raw prompts, responses, chain-of-thought, private audit receipts, and
  unrestricted logs.

No private-information or secret-bearing finding was detected. The current
GitHub surface exposes only the intentional public handle
`DannyExperiments`; commit metadata returned no email address, and the draft
PR has no comments. The repository remains private until a separate
visibility approval and a fresh exact-public-tree audit.

## Decision

`TEMPLATE_PARITY: PASS_AFTER_EDITORIAL_REBUILD`  
`CURRENT_TREE_PRIVACY: PASS`  
`PRIVATE_GITHUB_SURFACE_PRIVACY: PASS`  
`PUBLIC_VISIBILITY: NOT_AUTHORIZED`  
`RELEASE_AND_DOI: NOT_YET_PERFORMED`

The template comparison and privacy checks are release engineering. They do
not alter the mathematical, priority, implication, formalization, peer-review,
or publication classifications.
