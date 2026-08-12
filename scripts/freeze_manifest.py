#!/usr/bin/env python3
"""Regenerate the deterministic public manifest and SHA-256 ledger."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "PUBLIC_ALLOWLIST.txt"
GENERATED = {"MANIFEST.md", "SHA256SUMS.txt"}


class FreezeError(RuntimeError):
    pass


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def listed_paths() -> list[str]:
    if not ALLOWLIST.is_file():
        raise FreezeError("PUBLIC_ALLOWLIST.txt is missing")
    paths = [
        line.strip()
        for line in ALLOWLIST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if paths != sorted(paths):
        raise FreezeError("allowlist is not sorted")
    if len(paths) != len(set(paths)):
        raise FreezeError("allowlist contains duplicates")
    for rel in paths:
        item = Path(rel)
        if item.is_absolute() or ".." in item.parts:
            raise FreezeError(f"unsafe allowlist path: {rel}")
        candidate = ROOT / item
        if candidate.is_symlink() or not candidate.is_file():
            raise FreezeError(f"allowlisted regular file is absent: {rel}")
    return paths


def public_files() -> list[str]:
    paths: list[str] = []
    for candidate in ROOT.rglob("*"):
        rel = candidate.relative_to(ROOT)
        if rel.parts and rel.parts[0] == ".git":
            continue
        if candidate.is_symlink():
            raise FreezeError(f"symlink prohibited: {rel.as_posix()}")
        if candidate.is_file():
            paths.append(rel.as_posix())
    return sorted(paths)


def build_manifest(paths: list[str]) -> str:
    rows = [
        "# Public manifest",
        "",
        "Generated deterministically from `PUBLIC_ALLOWLIST.txt`.",
        "`SHA256SUMS.txt` additionally covers this manifest.",
        "",
        "| Path | Bytes | SHA-256 |",
        "|---|---:|---|",
    ]
    for rel in paths:
        candidate = ROOT / rel
        rows.append(f"| `{rel}` | {candidate.stat().st_size} | `{digest(candidate)}` |")
    rows.append("")
    return "\n".join(rows)


def build_sums(paths: list[str]) -> str:
    entries = sorted(paths + ["MANIFEST.md"])
    return "".join(f"{digest(ROOT / rel)}  {rel}\n" for rel in entries)


def main() -> int:
    paths = listed_paths()
    actual = set(public_files())
    expected_before = set(paths) | (actual & GENERATED)
    if actual != expected_before:
        extra = sorted(actual - expected_before)
        missing = sorted(expected_before - actual)
        raise FreezeError(f"inventory mismatch: extra={extra}; missing={missing}")

    (ROOT / "MANIFEST.md").write_text(build_manifest(paths), encoding="utf-8")
    (ROOT / "SHA256SUMS.txt").write_text(build_sums(paths), encoding="utf-8")

    final_actual = set(public_files())
    final_expected = set(paths) | GENERATED
    if final_actual != final_expected:
        raise FreezeError("generated inventory does not match the public tree")

    print(f"ALLOWLIST_ENTRIES: {len(paths)}")
    print(f"PUBLIC_REGULAR_FILES: {len(final_actual)}")
    print("MANIFEST_FREEZE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

