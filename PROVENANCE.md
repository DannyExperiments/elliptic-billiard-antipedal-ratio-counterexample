# Public-safe provenance

This local staging tree was assembled by explicit allowlist from sanitized
mathematical summaries. It is not a copy of the private evidence case.

## Controlling public-safe inputs

| Input | Role | SHA-256 |
|---|---|---|
| Canonical theorem packet | Exact source target, corrected theorem, and witness locator | `3d35e3ebdd91ec558410c96c1c8c2fd0f9cf3e8b8d1d38742f3b7e474fb83bc3` |
| Mathematical-audit adjudication | Qualified mathematical pass and prohibited inflation | `b2f005e91801ecc2d4d32fa9b580414b8ccd02448c408e56980cdb48f09427d6` |
| Official-status literature lane | Version chronology, public status, and partial-precedent boundary | `f66c037dfbc896fa468f2e24490fc6aa2c968f2c6a2920dbb8f8e84d4e1b7b41` |
| Stage 3 implication audit | Exact consequence matrix and strongest supported extension | `5ddaa1c362398b2c74d7cf25e7a492f22a9882fdeca2387e904c5a7e48fa2109` |
| Candidate B archive | Single unchanged canonical proof container; not redistributed here | `d3be5f3af03954877e0634e0959dcba72261ded8cbdcfedce2c1baafaf66c5d0` |
| Candidate B report | Sole proof base for the manuscript; not redistributed separately | `ea03a396bc65fe1b935d73ea323a1eeba7078d4f2f0b1e1eaa8ecc2b3c0ff8bc` |
| Stage-3 canonical theorem and scope | Frozen theorem, numbering, semantics, and priority boundary | `f42372031f9c810bb3ed06530b28ee3d083b38747fdb30a4e25d92c4dbe1666f` |
| Stage-3 dependency map | Frozen proof and evidence dependencies | `09dd2bc8e5247188403a3f5a20de98e7a3891542ee83b25accc33be184a93faf` |
| Stage-3 claims/evidence matrix | Frozen claim-level release boundary | `d521228f0ffefd28412a36bd14ae5630fc943ba8367a02981beffa6e4558d20c` |

Except for the public-safe manuscript source package described below, these
hashes identify controlling artifacts that are summarized rather than copied
wholesale into this staging tree.

## Frozen Stage-4 manuscript import after source audit

The following Stage-4 Candidate-B source members are frozen under `paper/`
after two citation-only repairs required by the hostile source audit. The
central-symmetry proof architecture and mathematics were not changed, and no
Candidate-A/C proof material was cross-patched.

| Imported member | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `972dcf53662ce94efcf56b7f6ccee0a8db30e7a0dcf7e74f6033e22aab40584e` |
| `paper/references.bib` | `6ab2dd7504ca52f188549c2cc255a0adb9859b2f6e658fdae3febe6a04c53d62` |
| `paper/BUILD.md` | `3162d9383364c86dd2483b6c573bcf4966e3a900a85b358936827ca022964f3b` |
| `paper/CLAIM_SCOPE_AND_LIMITATIONS.md` | `870d4ab842470ebc757cd5ac78c9932304520669771a7527ecfedfb84a700312` |
| `paper/SOURCE_TO_CANONICAL_COMPARISON.md` | `56f876c9a9d35b2c51b7605b9af6de8fbec84aa78dfe270baad5bb5e5e2031e5` |
| `paper/MANIFEST.md` | `b56fc4d13530b6b9fe3d3b10561c38ac4fc16d59e9a07324c256b66c811b424e` |
| `paper/SHA256SUMS.txt` | `b13a369a74f49e386841547252f6b80dabd987e2db45c801492d67e441347a54` |
| `paper/SHA256SUMS.txt.sha256` | `93db4b5b18697acd179382b5c220165670e16b9c2cfa0f833f2d6f7626eaadbc` |

These receipts establish source identity only. No TeX build, PDF parity,
metadata scan, or visual preflight is inferred.

## Public exact-certificate and formalization import

The following sanitized, author-controlled artifacts are integrated for
reproducibility. They contain no private candidate return or source archive.

| Imported member | SHA-256 |
|---|---|
| `evidence/N8_SUPPORTING_LINE_CERTIFICATE.zip` | `b054bf76bd5d70e4b4e43b00c0bfd3f349cbfff9739b629aadac74f74ca30b07` |
| `verification/verify_k607_stdlib.py` | `23a83b0637a20609179fc9e6418fd860a34b11984b12754add8b3eed36c4ed3d` |
| `verification/EXPECTED_K607_STDLIB.txt` | `8db0d193ef6820c9ae10dcd4ecb4004d3091522f67ee716ad4da3f7b17c9c64a` |
| `verification/REPLAY_ACTUAL.txt` | `8db0d193ef6820c9ae10dcd4ecb4004d3091522f67ee716ad4da3f7b17c9c64a` |
| `formalization/lean/K607FiniteCertificate.lean` | `93981c7537d99fa0db6b2389c03bffb17dda2c7cf26fc0437bdf191c883945f8` |
| `formalization/lean/AxiomAudit.lean` | `3a4e1e6436d05734415d4f7fc2077e771e553c4e31d1c1e0a16f430bcf91d190` |
| `formalization/lean/AXIOM_REPORT.txt` | `de0e34c2b69249bd703069c74c91b37477f2c12f45d58bba0c8fc59458fa90a7` |
| `formalization/lean/lean-toolchain` | `54727eec5cba149c18842e6deb5c41b369d66455c93ce135d7d5347c782b2325` |

The evidence ZIP was assembled twice with normalized timestamps, sorted member
paths, and stripped ZIP extras; both archives were byte-identical. Its CRC,
internal SHA ledger, privacy scan, ordinary/optimized standard-library replay,
Lean build, `leanchecker`, axiom-output comparison, and proof-escape scan all
passed before integration.

## Deliberately excluded

- raw model prompts, responses, and thread or request receipts;
- private audit packets and preliminary adjudications;
- local paths, browser artifacts, screenshots, and internal tool metadata;
- third-party source archives, article PDFs, figures, images, and videos;
- unpublished correspondence and unrestricted literature-search logs;
- uninspected formalization or evidence archives beyond the explicitly
  integrated public-safe files above; and
- any credential, cookie, token, or personal contact field.

Future imports must be individually sanitized, allowlisted, hashed, and
classified by role before inclusion.
