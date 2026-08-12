# Release staging

PR #1's exact approval head
`320cd6a719b8b0a8307608217a91dd29acae7142` passed all four workflows and was
squash-merged to private `main` at
`614152f05d1b6e9005958d7566740b1205a14b25`. All four post-merge workflows
passed: repository integrity `31614190306`, exact replay `31614190363`, PDF
build `31614190281`, and partial Lean `31614190259`. The accepted manuscript
and PDF passed source parity, blank-metadata and deep-privacy checks, and full
visual inspection. The human owner approved the final title, public evidence,
disclosure, partial-Lean scope, public visibility, immutable Version 1.0.0
release, and DOI deposit. No tag, immutable release, archive deposit, or DOI
exists yet; external notice remains separately unapproved.

The mature-repository release layout is staged in this directory:
`RELEASE_NOTES_v1.0.0.md`, `BADGE_ACTIVATION.md`,
`BRANCH_PROTECTION.md`, `DOI_DEPOSIT.md`, and the human checklist. The
deterministic public-evidence builder is `scripts/build_evidence_bundle.py`.
Its final ZIP, sidecar, and release-asset ledger must rebuild byte-for-byte
before the Version 1.0.0 tag is created.

The five payloads named by `RELEASE_ASSET_SHA256SUMS.txt` are:

- `paper/manuscript.pdf`, staged as
  `elliptic-billiard-antipedal-ratio-counterexample-v1.0.0.pdf`;
- `paper/manuscript.tex`, staged as
  `elliptic-billiard-antipedal-ratio-counterexample-v1.0.0.tex`;
- `paper/references.bib`, staged as `references.bib`;
- `CITATION.cff`, staged as `CITATION.cff`; and
- `release/EVIDENCE_BUNDLE.zip`, staged as
  `elliptic-billiard-antipedal-ratio-counterexample-public-evidence-v1.0.0.zip`.

The ledger itself is the sixth immutable release asset.

`RELEASE_GATES.json` is machine-read by the repository verifier. Any false
gate keeps the default verification command blocked. Human approvals are
explicit fields and cannot be inferred from a successful build or audit.

Workflow and badge activation must occur only after the matching local gate
has passed and the proposed public action has been explicitly approved.
