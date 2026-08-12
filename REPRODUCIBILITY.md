# Reproducibility

The staging integrity check uses only the existing shell and Python standard
library and performs no network access or dependency installation:

```bash
bash scripts/verify.sh --integrity-only
```

It verifies the explicit allowlist, exact manifest, per-file SHA-256 ledger,
absence of symlinks and generated caches, public-safe file types, privacy and
secret patterns, authorship/license boundaries, release-gate metadata, the
exact Stage-4 manuscript source hashes, the certificate archive/sidecar, the
frozen verifier replay, and the formalization source/toolchain/axiom receipts.

The manuscript subpackage also carries an independent nested ledger and
detached checksum. Verify both from the repository root with:

```bash
(cd paper && shasum -a 256 -c SHA256SUMS.txt && \
  shasum -a 256 -c SHA256SUMS.txt.sha256)
```

This nested ledger verifies source identity only. The accepted PDF is covered
by the repository-level ledger and `paper/PDF_PREFLIGHT.md`. The pinned
`pdf.yml` workflow performs clean rebuilds; a workflow success alone never
replaces the independent artifact, rendered-page, metadata, privacy, and
source-parity inspection recorded in that receipt.

Replay the exact standard-library verifier in both assertion modes:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B verification/verify_k607_stdlib.py > /tmp/replay.txt
diff -u verification/EXPECTED_K607_STDLIB.txt /tmp/replay.txt
PYTHONDONTWRITEBYTECODE=1 python3 -O -B verification/verify_k607_stdlib.py > /tmp/replay-O.txt
diff -u verification/EXPECTED_K607_STDLIB.txt /tmp/replay-O.txt
```

Build and kernel-check the partial finite Lean certificate:

```bash
(cd formalization/lean && lake build && \
  lake env leanchecker K607FiniteCertificate && \
  lake env lean AxiomAudit.lean > /tmp/axioms.txt && \
  diff -u AXIOM_REPORT.txt /tmp/axioms.txt)
```

This pins Lean 4.30.0 and uses no external Lake packages.

The default command evaluates the completed release-and-DOI gate:

```bash
bash scripts/verify.sh
```

On the post-DOI closure tree it must exit zero with
`PUBLIC_RELEASE_GATE: RELEASE_AND_DOI_CLOSED`. External problem-page notice is
a separate optional communication gate and remains false without blocking this
release closure.

GitHub CI deliberately runs the narrower `--integrity-only` mode. That green
check establishes the tree's exact inventory and frozen bytes; the default
local command separately checks the recorded release-and-DOI closure state.

Version 1.0.0 is immutable. Post-release DOI metadata in current `README.md`,
`STATUS.md`, and `CITATION.cff` intentionally differs from the copies inside
the released evidence ZIP. `scripts/build_evidence_bundle.py --check` therefore
pins the published evidence bundle, sidecar, and release-asset ledger by their
frozen hashes instead of silently rebuilding them from current-main metadata.

To regenerate the deterministic manifest and checksum ledger after an
allowlisted edit:

```bash
python3 -B scripts/freeze_manifest.py
```

Repository integrity is not a mathematical proof, literature result, formal
verification, peer review, or release authorization.
