# Release staging

A private repository and draft PR #1 exist for exact-head CI and PDF audit.
No public repository, release tag, immutable release, archive deposit, or DOI
exists for this candidate.

`RELEASE_GATES.json` is machine-read by the repository verifier. Any false
gate keeps the default verification command blocked. Human approvals are
explicit fields and cannot be inferred from a successful build or audit.

Workflow and badge activation must occur only after the matching local gate
has passed and the proposed public action has been explicitly approved.
