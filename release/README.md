# Release staging

A private repository and draft PR #1 exist. The hardened source/workflow head
passed exact-head CI and its PDF passed independent audit. The accepted-PDF
integration head also passed all four workflows; its rebuilt PDF text and all
six rendered pages matched the accepted artifact.
The later authorless-template repair head
`941a1be9f05e8a92b0c1ab9c9523238ad85b1308` also passed all four workflows,
and its current six-page PDF passed clean-build, source-parity, blank-metadata,
deep-privacy, and full visual preflight. A final integration-head CI pass is
still required after committing those accepted PDF bytes and receipts.
No public repository, release tag, immutable release, archive deposit, or DOI
exists for this candidate.

The mature-repository release layout is staged in this directory:
`RELEASE_NOTES_v1.0.0.md`, `BADGE_ACTIVATION.md`,
`BRANCH_PROTECTION.md`, `DOI_DEPOSIT.md`, and the human checklist. The
deterministic public-evidence builder is
`scripts/build_evidence_bundle.py`. Its final ZIP, sidecar, release-asset
ledger, and any write-enabled publishing workflow must be frozen only after
the exact public-main bytes and citation metadata are approved.

`RELEASE_GATES.json` is machine-read by the repository verifier. Any false
gate keeps the default verification command blocked. Human approvals are
explicit fields and cannot be inferred from a successful build or audit.

Workflow and badge activation must occur only after the matching local gate
has passed and the proposed public action has been explicitly approved.
