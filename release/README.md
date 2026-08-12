# Release staging

A private repository and draft PR #1 exist. The accepted manuscript and PDF
passed source parity, blank-metadata and deep-privacy checks, and full visual
inspection. Exact PR head
`214a8c3001bbfe68b231b6158dd7904b5ac196ba` passed all four workflows (runs
`31577655770`, `31577655875`, `31577655948`, and `31577655760`). The human
owner has approved the final title, public evidence, disclosure, partial-Lean
scope, public visibility, immutable Version 1.0.0 release, and DOI deposit.
The approval-only successor head must pass the same four checks before merge.
No public repository, tag, immutable release, archive deposit, or DOI exists
yet; external notice remains separately unapproved.

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
