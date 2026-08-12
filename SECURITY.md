# Security policy

Report suspected credential exposure, private-path leakage, malicious files,
unsafe workflow behavior, checksum failure, or verifier tampering privately to
the repository owner before opening a public issue.

Do not attach browser exports, private model receipts, unpublished third-party
files, credentials, wallet material, or local-machine diagnostics to a public
report.

The exact staging verifier uses only Python's standard library and does not
install packages or execute imported private research artifacts. The Lean
project pins Lean 4.30.0, has zero external Lake packages, and is checked for
proof escapes and unsafe declarations. The Lean workflow downloads the
official 4.30.0 release archive and verifies its exact published SHA-256 before
extraction; it executes no remote installer script and uses no workflow cache.
The PDF workflow uses the same SHA-pinned LaTeX action audited in the
comparison repositories, binds its TeX Live container to an exact OCI digest,
and uploads only the manuscript PDF and build log. Staged workflows use pinned
action commits, checkout with credential persistence disabled, and read-only
content permissions. The offline repository verifier fails closed on recorded
release metadata and tree-integrity drift; it does not query GitHub, DOI.org,
Zenodo, or DataCite and does not substitute for the separate replay, PDF, and
Lean workflows. Live release, DOI-resolution, and workflow state are recorded
from independent external checks in the release receipts. External
problem-page notice remains a separate optional communication action.
