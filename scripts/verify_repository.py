#!/usr/bin/env python3
"""Verify public staging integrity and fail closed on release readiness."""

from __future__ import annotations

import argparse
import io
import json
import re
import stat
import sys
import zipfile
from pathlib import Path

from freeze_manifest import (
    GENERATED,
    ROOT,
    build_manifest,
    build_sums,
    listed_paths,
    public_files,
)


ALLOWED_SUFFIXES = {
    "",
    ".bib",
    ".cff",
    ".json",
    ".lean",
    ".md",
    ".pdf",
    ".py",
    ".sha256",
    ".sh",
    ".tex",
    ".toml",
    ".txt",
    ".yml",
    ".zip",
}

ALLOWED_BINARY_PATHS = {
    "evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip",
    "paper/manuscript.pdf",
}

REQUIRED_RELEASE_FILES = {
    "evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip",
    "evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip.sha256",
    "formalization/lean/AXIOM_REPORT.txt",
    "formalization/lean/AxiomAudit.lean",
    "formalization/lean/K607FiniteCertificate.lean",
    "formalization/lean/SCOPE_BOUNDARY.md",
    "formalization/lean/lake-manifest.json",
    "formalization/lean/lakefile.toml",
    "formalization/lean/lean-toolchain",
    "paper/manuscript.pdf",
    "paper/manuscript.tex",
    "paper/references.bib",
    "verification/EXPECTED_K607_STDLIB.txt",
    "verification/REPLAY_ACTUAL.txt",
    "verification/REPLAY_RECEIPT.md",
    "verification/verify_k607_stdlib.py",
}

REQUIRED_GATE_NAMES = {
    "mathematical_audit_pass",
    "implications_scope_pass",
    "priority_three_lanes_adjudicated",
    "canonical_proof_selected",
    "canonical_proof_public_integration",
    "public_evidence_integrated",
    "verifier_replay_pass",
    "manuscript_integrated",
    "manuscript_clean_build",
    "manuscript_visual_preflight",
    "formalization_status_finalized",
    "privacy_and_rights_final_pass",
    "human_authorship_approved",
    "human_license_approved",
    "human_ai_disclosure_approved",
    "human_visibility_approved",
    "human_doi_metadata_approved",
    "human_external_notice_approved",
    "remote_created",
    "immutable_release_created",
    "doi_deposited_and_resolving",
}

FROZEN_MANUSCRIPT_HASHES = {
    "paper/manuscript.tex": "032ece89a0158b9eb7537ae085b0e1f2159607aaf6817f2a1bf57bf305e06ba0",
    "paper/references.bib": "6ab2dd7504ca52f188549c2cc255a0adb9859b2f6e658fdae3febe6a04c53d62",
    "paper/BUILD.md": "a9d8fc2d794353c9b49bb5a1c9c1bf3d2b6d226399bb371e85c62943120d9c5c",
    "paper/CLAIM_SCOPE_AND_LIMITATIONS.md": "67320296fb0ebb196c6925c0cfcd3d1afcec9d8cec1ee5982f8df5a7411f79a8",
    "paper/SOURCE_TO_CANONICAL_COMPARISON.md": "34f185ec5bc229947ea117d5f51310b9d56ccae62e9f81ef43f0e379a19cde4c",
    "paper/CHANGELOG_FROM_CANONICAL_PROOF.md": "8d46e5b12b6d1803952da351c5aa57ec11c26671f2fb8a8a5465ed7fbba8ae14",
    "paper/MANIFEST.md": "518620a33d10f247f0a6d3a673243ffed41ef746e03c091743c49f0121dc2649",
    "paper/SHA256SUMS.txt": "05a8833ff023fb2af94655723db44e0728497991d5560672cbc052ca05a974f1",
    "paper/SHA256SUMS.txt.sha256": "808ea01dfbd8438fef74608467297e212f0e12bb92f9f7186891cde1804b5d35",
    "paper/PDF_PREFLIGHT.md": "2b32ca4421fa7a392a06bc4ce423208ec2081495f89b9bb0fce25d7349ba9167",
    "paper/manuscript.pdf": "998ba5f77cb8d94a69e4dc7e089f5dd8a2b314aac7b8f77f677d95553064c7cd",
}

FROZEN_PUBLIC_CERTIFICATE_HASHES = {
    "evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip": "b054bf76bd5d70e4b4e43b00c0bfd3f349cbfff9739b629aadac74f74ca30b07",
    "verification/EXPECTED_K607_STDLIB.txt": "8db0d193ef6820c9ae10dcd4ecb4004d3091522f67ee716ad4da3f7b17c9c64a",
    "verification/REPLAY_ACTUAL.txt": "8db0d193ef6820c9ae10dcd4ecb4004d3091522f67ee716ad4da3f7b17c9c64a",
    "verification/verify_k607_stdlib.py": "23a83b0637a20609179fc9e6418fd860a34b11984b12754add8b3eed36c4ed3d",
    "formalization/lean/AXIOM_REPORT.txt": "de0e34c2b69249bd703069c74c91b37477f2c12f45d58bba0c8fc59458fa90a7",
    "formalization/lean/AxiomAudit.lean": "3a4e1e6436d05734415d4f7fc2077e771e553c4e31d1c1e0a16f430bcf91d190",
    "formalization/lean/K607FiniteCertificate.lean": "93981c7537d99fa0db6b2389c03bffb17dda2c7cf26fc0437bdf191c883945f8",
    "formalization/lean/lake-manifest.json": "67850569f23850f50bc5bcece763d7a5e429364df46eade38b81a5f84e0202b4",
    "formalization/lean/lakefile.toml": "4f7ba5ff9bdeaad36f6c6046d23eb83deab5a144bfdcebbd9805818cb87dead2",
    "formalization/lean/lean-toolchain": "54727eec5cba149c18842e6deb5c41b369d66455c93ce135d7d5347c782b2325",
}


TEXT_SUFFIXES = {
    ".bib",
    ".cff",
    ".json",
    ".lean",
    ".md",
    ".py",
    ".sha256",
    ".sh",
    ".tex",
    ".toml",
    ".txt",
    ".yml",
}


def privacy_findings(label: str, body: str) -> list[str]:
    failures: list[str] = []
    fragments = {
        "/" + "Users" + "/": "absolute macOS user path",
        "/private/var/" + "folders/": "private temporary-item path",
        "/var/" + "folders/": "temporary-item path",
        "/home/" + "runner/work/": "CI workspace path",
        "\\" + "Users" + "\\": "absolute Windows user path",
        "." + "codex": "internal application path",
        "chatgpt" + ".com": "private conversation URL",
        "chat" + ".openai.com": "private conversation URL",
        "sandbox" + ":": "internal download URL",
        "file" + "://": "local file URL",
        "codex" + "-clipboard": "clipboard artifact name",
        "pasted" + "-text": "attachment artifact name",
        "daniel" + "cabezas": "private local identifier",
        "imaginary" + "ones.com": "private account domain",
        "danny" + ".social": "private profile identifier",
        "oai" + "-mem-citation": "internal memory citation",
        chr(0xE200) + "cite": "internal tool citation",
    }
    lowered = body.lower()
    for fragment, description in fragments.items():
        if fragment.lower() in lowered:
            failures.append(f"{description} in {label}")

    patterns = {
        "internal search reference": re.compile(r"\bturn\d+(?:search|view|fetch|open)\d+\b"),
        "email address": re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
        "UUID-like receipt identifier": re.compile(
            r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b"
        ),
        "private key block": re.compile("BEGIN " + "(?:RSA |EC |OPENSSH )?PRIVATE KEY"),
        "GitHub token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b"),
        "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
        "generic API secret": re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    }
    for description, pattern in patterns.items():
        if pattern.search(body):
            failures.append(f"{description} in {label}")
    return failures


def scan_zip_bytes(label: str, payload: bytes, depth: int = 0) -> list[str]:
    failures: list[str] = []
    if depth > 2:
        return [f"nested ZIP depth exceeds policy in {label}"]
    try:
        archive = zipfile.ZipFile(io.BytesIO(payload))
    except zipfile.BadZipFile:
        return [f"invalid ZIP archive: {label}"]

    infos = archive.infolist()
    if len(infos) > 1000:
        failures.append(f"ZIP member count exceeds policy in {label}")
    if sum(info.file_size for info in infos) > 100 * 1024 * 1024:
        failures.append(f"ZIP expanded size exceeds policy in {label}")
    seen: set[str] = set()
    for info in infos:
        name = info.filename
        member_label = f"{label}!{name}"
        path = Path(name)
        if not name or name in seen:
            failures.append(f"empty or duplicate ZIP member path in {member_label}")
            continue
        seen.add(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name:
            failures.append(f"unsafe ZIP member path in {member_label}")
        mode = (info.external_attr >> 16) & 0xFFFF
        if mode and stat.S_ISLNK(mode):
            failures.append(f"ZIP symlink member in {member_label}")
        if info.flag_bits & 0x1:
            failures.append(f"encrypted ZIP member in {member_label}")
        if info.is_dir():
            continue
        data = archive.read(info)
        suffix = path.suffix.lower()
        if suffix in TEXT_SUFFIXES:
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                failures.append(f"non-UTF-8 public text member: {member_label}")
            else:
                failures.extend(privacy_findings(member_label, text))
        elif suffix == ".zip":
            failures.extend(scan_zip_bytes(member_label, data, depth + 1))
        elif suffix == ".pdf":
            failures.extend(privacy_findings(member_label, data.decode("latin-1", errors="ignore")))
    archive.close()
    return failures


def scan_public_text(paths: set[str]) -> list[str]:
    failures: list[str] = []
    for rel in sorted(paths):
        candidate = ROOT / rel
        suffix = candidate.suffix.lower()
        if suffix in TEXT_SUFFIXES:
            try:
                body = candidate.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                failures.append(f"non-UTF-8 public text file: {rel}")
            else:
                failures.extend(privacy_findings(rel, body))
        elif suffix == ".zip":
            failures.extend(scan_zip_bytes(rel, candidate.read_bytes()))
        elif suffix == ".pdf":
            failures.extend(
                privacy_findings(rel, candidate.read_bytes().decode("latin-1", errors="ignore"))
            )
    return failures


def check_inventory(paths: list[str]) -> list[str]:
    failures: list[str] = []
    actual = set(public_files())
    expected = set(paths) | GENERATED
    if actual != expected:
        for rel in sorted(actual - expected):
            failures.append(f"unallowlisted file: {rel}")
        for rel in sorted(expected - actual):
            failures.append(f"missing public file: {rel}")

    for rel in sorted(actual):
        suffix = Path(rel).suffix.lower()
        if suffix not in ALLOWED_SUFFIXES:
            failures.append(f"prohibited public file type: {rel}")
        if suffix in {".pdf", ".zip"} and rel not in ALLOWED_BINARY_PATHS:
            failures.append(f"unapproved binary artifact: {rel}")
        parts = Path(rel).parts
        if any(part in {"__pycache__", ".lake", "node_modules"} for part in parts):
            failures.append(f"generated cache in public tree: {rel}")
    return failures


def check_frozen_ledgers(paths: list[str]) -> list[str]:
    failures: list[str] = []
    manifest = ROOT / "MANIFEST.md"
    sums = ROOT / "SHA256SUMS.txt"
    if not manifest.is_file() or manifest.read_text(encoding="utf-8") != build_manifest(paths):
        failures.append("MANIFEST.md is missing or stale")
    if not sums.is_file() or sums.read_text(encoding="utf-8") != build_sums(paths):
        failures.append("SHA256SUMS.txt is missing or stale")
    return failures


def check_frozen_manuscript() -> list[str]:
    """Require the Stage-4 source package to remain byte-identical."""

    from freeze_manifest import digest

    failures: list[str] = []
    for rel, expected in FROZEN_MANUSCRIPT_HASHES.items():
        candidate = ROOT / rel
        if not candidate.is_file():
            failures.append(f"frozen manuscript member absent: {rel}")
        elif digest(candidate) != expected:
            failures.append(f"frozen manuscript hash mismatch: {rel}")
    return failures


def check_frozen_public_certificate() -> list[str]:
    """Require the public certificate, replay, and Lean core to stay frozen."""

    from freeze_manifest import digest

    failures: list[str] = []
    for rel, expected in FROZEN_PUBLIC_CERTIFICATE_HASHES.items():
        candidate = ROOT / rel
        if not candidate.is_file():
            failures.append(f"frozen public certificate member absent: {rel}")
        elif digest(candidate) != expected:
            failures.append(f"frozen public certificate hash mismatch: {rel}")

    sidecar = ROOT / "evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip.sha256"
    expected_sidecar = (
        FROZEN_PUBLIC_CERTIFICATE_HASHES["evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip"]
        + "  N8_SUPPORTING_LINE_CERTIFICATE.zip\n"
    )
    if not sidecar.is_file() or sidecar.read_text(encoding="utf-8") != expected_sidecar:
        failures.append("certificate archive sidecar is absent or mismatched")

    expected = ROOT / "verification/EXPECTED_K607_STDLIB.txt"
    actual = ROOT / "verification/REPLAY_ACTUAL.txt"
    if expected.is_file() and actual.is_file() and expected.read_bytes() != actual.read_bytes():
        failures.append("frozen verifier replay does not byte-match expected output")
    return failures


def check_rights_and_metadata() -> list[str]:
    failures: list[str] = []
    root_license_names = {"LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"}
    for name in root_license_names:
        if (ROOT / name).exists():
            failures.append(f"repository-wide license file prohibited: {name}")

    rights = (ROOT / "LICENSE_STATUS.md").read_text(encoding="utf-8")
    if "No repository-wide reuse license is granted" not in rights:
        failures.append("all-rights-reserved statement is absent")

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    if citation.count('name: "DannyExperiments"') != 2:
        failures.append("CITATION.cff authorship does not match the approved convention")
    if "affiliation:" in citation:
        failures.append("CITATION.cff must not list an affiliation")
    citation_lines = {line.strip() for line in citation.splitlines()}
    for premature in ("repository-code:", "date-released:", "doi:", "version:"):
        if any(line.startswith(premature) for line in citation_lines):
            failures.append(f"premature citation metadata: {premature}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "badge.svg" in readme or "[![" in readme:
        failures.append("README contains an unapproved badge")

    manuscript = (ROOT / "paper/manuscript.tex").read_text(encoding="utf-8")
    article_identity_markers = {
        "\\author{": "article author byline",
        "\\affiliation{": "article affiliation",
        "pdfauthor=": "explicit PDF author metadata",
        "pdftitle=": "explicit PDF title metadata",
        "pdfsubject=": "explicit PDF subject metadata",
        "DannyExperiments": "repository identity in mathematical article",
        "OpenAI": "AI vendor name in mathematical article",
        "ChatGPT": "AI product name in mathematical article",
        "Codex": "AI product name in mathematical article",
    }
    for marker, description in article_identity_markers.items():
        if marker in manuscript:
            failures.append(f"{description} must remain on repository metadata/disclosure surfaces")
    if "\\date{}" not in manuscript:
        failures.append("article date must remain empty under the established paper template")
    expected_running_mark = (
        "\\markboth{FOCAL ANTIPEDAL AREAS}{FOCAL ANTIPEDAL AREAS}"
    )
    if manuscript.count(expected_running_mark) != 1:
        failures.append("authorless article running-title mark is absent or ambiguous")
    return failures


def load_release_gates() -> tuple[dict[str, bool], list[str]]:
    failures: list[str] = []
    path = ROOT / "release/RELEASE_GATES.json"
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return {}, [f"release gate JSON invalid: {error}"]

    if document.get("schema_version") != 1:
        failures.append("unsupported release-gate schema")
    gates = document.get("gates")
    if not isinstance(gates, dict):
        return {}, failures + ["release gates must be an object"]
    if set(gates) != REQUIRED_GATE_NAMES:
        failures.append("release-gate names do not match the required schema")
    if any(type(value) is not bool for value in gates.values()):
        failures.append("every release gate must be a boolean")

    all_pass = set(gates) == REQUIRED_GATE_NAMES and all(gates.values())
    expected_status = "RELEASE_AND_DOI_CLOSED" if all_pass else "BLOCKED_FAIL_CLOSED"
    if document.get("status") != expected_status:
        failures.append(f"release status must be {expected_status}")
    return gates, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--integrity-only",
        action="store_true",
        help="check the staging tree without requiring every release gate",
    )
    args = parser.parse_args()

    failures: list[str] = []
    try:
        paths = listed_paths()
        failures.extend(check_inventory(paths))
        failures.extend(check_frozen_ledgers(paths))
    except Exception as error:
        print(f"STAGING_INTEGRITY: FAIL\n- {error}")
        return 1

    public = set(public_files())
    failures.extend(check_frozen_manuscript())
    failures.extend(check_frozen_public_certificate())
    failures.extend(scan_public_text(public))
    failures.extend(check_rights_and_metadata())
    gates, gate_schema_failures = load_release_gates()
    failures.extend(gate_schema_failures)

    if failures:
        print("STAGING_INTEGRITY: FAIL")
        for failure in sorted(set(failures)):
            print(f"- {failure}")
        return 1

    print("STAGING_INTEGRITY: PASS")
    if args.integrity_only:
        print("PUBLIC_RELEASE_GATE: NOT_EVALUATED")
        return 0

    blockers = [f"gate false: {name}" for name, value in sorted(gates.items()) if not value]
    actual = set(public_files())
    blockers.extend(
        f"required release file absent: {rel}"
        for rel in sorted(REQUIRED_RELEASE_FILES - actual)
    )
    if blockers:
        print("PUBLIC_RELEASE_GATE: BLOCKED")
        for blocker in blockers:
            print(f"- {blocker}")
        return 2

    print("PUBLIC_RELEASE_GATE: RELEASE_AND_DOI_CLOSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
