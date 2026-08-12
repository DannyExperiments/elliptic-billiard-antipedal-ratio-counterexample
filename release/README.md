# Release staging

A private repository and draft PR #1 exist. The hardened source/workflow head
passed exact-head CI and its PDF passed independent audit. The accepted-PDF
integration head also passed all four workflows; its rebuilt PDF text and all
six rendered pages matched the accepted artifact.
No public repository, release tag, immutable release, archive deposit, or DOI
exists for this candidate.

`RELEASE_GATES.json` is machine-read by the repository verifier. Any false
gate keeps the default verification command blocked. Human approvals are
explicit fields and cannot be inferred from a successful build or audit.

Workflow and badge activation must occur only after the matching local gate
has passed and the proposed public action has been explicitly approved.
