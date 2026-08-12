#!/usr/bin/env python3
"""Build or check the deterministic sanitized public evidence bundle."""

from __future__ import annotations

import argparse
import hashlib
import io
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release/EVIDENCE_BUNDLE.zip"
SIDECAR = ROOT / "release/EVIDENCE_BUNDLE.sha256"
ASSET_LEDGER = ROOT / "release/RELEASE_ASSET_SHA256SUMS.txt"
PREFIX = "AMR-050-0035_PUBLIC_EVIDENCE_V1/"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
FROZEN_BUNDLE_SHA256 = "507c6b33d60a1bf2cff00e80c36b008a637bd390fe37f6c8aed18e593545af3b"
FROZEN_ASSET_LEDGER_SHA256 = "a91a779d8513c022f03aef1e2aee08562570978bd4fe33b708315f2ffa2b5c48"

ALLOWLIST = (
    "README.md",
    "STATUS.md",
    "PROBLEM_AND_PROOF.md",
    "CITATION.cff",
    "AI_DISCLOSURE.md",
    "PROVENANCE.md",
    "CLAIMS_EVIDENCE_MATRIX.md",
    "REPRODUCIBILITY.md",
    "LICENSE_STATUS.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "canonical/CANONICAL_CLAIM.md",
    "canonical/DEPENDENCY_MAP.md",
    "canonical/SCOPE_LIMITATIONS.md",
    "audits/README.md",
    "audits/public_safe_reports/MATHEMATICAL_AUDIT_SUMMARY.md",
    "audits/public_safe_reports/LITERATURE_STATUS_SUMMARY.md",
    "audits/public_safe_reports/IMPLICATIONS_SCOPE_SUMMARY.md",
    "audits/public_safe_reports/REPOSITORY_TEMPLATE_AND_PRIVACY_AUDIT_2026-08-12.md",
    "paper/manuscript.tex",
    "paper/manuscript.pdf",
    "paper/references.bib",
    "paper/README.md",
    "paper/BUILD.md",
    "paper/BUILD_STATUS.md",
    "paper/PDF_PREFLIGHT.md",
    "paper/CLAIM_SCOPE_AND_LIMITATIONS.md",
    "paper/SOURCE_TO_CANONICAL_COMPARISON.md",
    "paper/CHANGELOG_FROM_CANONICAL_PROOF.md",
    "evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip",
    "evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip.sha256",
    "evidence/README.md",
    "verification/README.md",
    "verification/verify_k607_stdlib.py",
    "verification/EXPECTED_K607_STDLIB.txt",
    "verification/REPLAY_ACTUAL.txt",
    "verification/REPLAY_RECEIPT.md",
    "formalization/README.md",
    "formalization/THEOREM_SCOPE.md",
    "formalization/lean/README.md",
    "formalization/lean/SCOPE_BOUNDARY.md",
    "formalization/lean/K607FiniteCertificate.lean",
    "formalization/lean/AxiomAudit.lean",
    "formalization/lean/AXIOM_REPORT.txt",
    "formalization/lean/lake-manifest.json",
    "formalization/lean/lakefile.toml",
    "formalization/lean/lean-toolchain",
    "formalization/aristotle/README.md",
    "release/README.md",
    "release/HUMAN_RELEASE_CHECKLIST.md",
    "release/BADGE_ACTIVATION.md",
    "release/BRANCH_PROTECTION.md",
    "release/DOI_DEPOSIT.md",
    "release/RELEASE_NOTES_v1.0.0.md",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replay_readme() -> bytes:
    return b"""# Replay the public evidence bundle

This deterministic archive is an allowlisted public-safe evidence subset. It
contains no raw conversation, private receipt, local path, credential,
personal identifier, screenshot, or third-party source PDF. After extraction,
enter the AMR-050-0035_PUBLIC_EVIDENCE_V1 directory and run:

```bash
sha256sum -c BUNDLE_SHA256SUMS.txt
python3 -B verification/verify_k607_stdlib.py
```

These checks establish the archived bytes and finite exact certificate. They
do not replace the analytic proof, mathematical review, peer review, source
interpretation, priority search, or the explicitly partial Lean boundary.
"""


def manifest(names: list[str]) -> bytes:
    lines = [
        "# Public evidence bundle manifest",
        "",
        "Bundle ID: `AMR-050-0035_PUBLIC_EVIDENCE_V1`.",
        "",
        "Every member is a regular file with fixed timestamp and mode.",
        "`BUNDLE_SHA256SUMS.txt` hashes every member except itself.",
        "",
        "## Members",
        "",
    ]
    lines.extend(f"- `{name}`" for name in sorted(names))
    return ("\n".join(lines) + "\n").encode("utf-8")


def build_bytes() -> bytes:
    missing = [name for name in ALLOWLIST if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit("missing bundle members: " + ", ".join(missing))
    payloads = {name: (ROOT / name).read_bytes() for name in ALLOWLIST}
    payloads["REPLAY_README.md"] = replay_readme()
    names = sorted([*payloads, "BUNDLE_MANIFEST.md", "BUNDLE_SHA256SUMS.txt"])
    payloads["BUNDLE_MANIFEST.md"] = manifest(names)
    payloads["BUNDLE_SHA256SUMS.txt"] = "".join(
        f"{sha256(payloads[name])}  {name}\n" for name in sorted(payloads)
    ).encode("utf-8")

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(payloads):
            info = zipfile.ZipInfo(PREFIX + name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, payloads[name])
    return buffer.getvalue()


def sidecar_text(bundle: bytes) -> str:
    return f"{sha256(bundle)}  EVIDENCE_BUNDLE.zip\n"


def asset_ledger_text(bundle: bytes) -> str:
    assets = {
        "elliptic-billiard-antipedal-ratio-counterexample-v1.0.0.pdf":
            (ROOT / "paper/manuscript.pdf").read_bytes(),
        "elliptic-billiard-antipedal-ratio-counterexample-v1.0.0.tex":
            (ROOT / "paper/manuscript.tex").read_bytes(),
        "references.bib": (ROOT / "paper/references.bib").read_bytes(),
        "CITATION.cff": (ROOT / "CITATION.cff").read_bytes(),
        "elliptic-billiard-antipedal-ratio-counterexample-public-evidence-v1.0.0.zip": bundle,
    }
    return "".join(
        f"{sha256(assets[name])}  {name}\n" for name in sorted(assets)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if args.check:
        if not OUTPUT.is_file() or sha256(OUTPUT.read_bytes()) != FROZEN_BUNDLE_SHA256:
            raise SystemExit("IMMUTABLE_EVIDENCE_BUNDLE_HASH_MISMATCH")
        expected_sidecar = f"{FROZEN_BUNDLE_SHA256}  EVIDENCE_BUNDLE.zip\n"
        if not SIDECAR.is_file() or SIDECAR.read_text(encoding="utf-8") != expected_sidecar:
            raise SystemExit("EVIDENCE_BUNDLE_SIDECAR_OUT_OF_DATE")
        if not ASSET_LEDGER.is_file() or sha256(ASSET_LEDGER.read_bytes()) != FROZEN_ASSET_LEDGER_SHA256:
            raise SystemExit("IMMUTABLE_RELEASE_ASSET_LEDGER_HASH_MISMATCH")
        print("IMMUTABLE_RELEASE_EVIDENCE_BUNDLE: PASS")
        return 0

    bundle = build_bytes()
    sidecar = sidecar_text(bundle)
    asset_ledger = asset_ledger_text(bundle)
    OUTPUT.write_bytes(bundle)
    SIDECAR.write_text(sidecar, encoding="utf-8")
    ASSET_LEDGER.write_text(asset_ledger, encoding="utf-8")
    print(f"WROTE {OUTPUT.relative_to(ROOT)}")
    print(f"SHA256 {sha256(bundle)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
