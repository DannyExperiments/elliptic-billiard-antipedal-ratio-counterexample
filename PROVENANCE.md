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

## Stage-4 proof import and public editorial derivative

The Stage-4 Candidate-B source first received two citation-only repairs
required by hostile source audit. The current public derivative additionally
removes only the article byline, date, explicit PDF identity metadata, and
manuscript-local AI production paragraph to match the established
solve-repository template. The central-symmetry proof architecture,
mathematics, references, and scope were not changed, and no Candidate-A/C
proof material was cross-patched.

| Imported member | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `762610722c4d138b3ac3915f9d15f0ad660896c327a26ace7007a8b3bf4ed71b` |
| `paper/references.bib` | `6ab2dd7504ca52f188549c2cc255a0adb9859b2f6e658fdae3febe6a04c53d62` |
| `paper/BUILD.md` | `a9d8fc2d794353c9b49bb5a1c9c1bf3d2b6d226399bb371e85c62943120d9c5c` |
| `paper/CLAIM_SCOPE_AND_LIMITATIONS.md` | `67320296fb0ebb196c6925c0cfcd3d1afcec9d8cec1ee5982f8df5a7411f79a8` |
| `paper/SOURCE_TO_CANONICAL_COMPARISON.md` | `c1dcc78a7568594456eca93ab6352ec67d7291ffae26f6f533c9db5830fedbab` |
| `paper/CHANGELOG_FROM_CANONICAL_PROOF.md` | `d69b317918c42cd4fc7bfefbfb2c51c03e0785d3c1de6d5995fee0fac73014c9` |
| `paper/MANIFEST.md` | `4eb0cf3f6ee89386cdc28880b56c9754af7249f9bf24d777e8546a514fbd3e8a` |
| `paper/SHA256SUMS.txt` | `d035653daf0c46300daea167104d36cf07ac32f0ed43faab343902956bb2093e` |
| `paper/SHA256SUMS.txt.sha256` | `2038db066fb8cb3181ccb39de151b17f6a25df9158c1c47ed8273f196afc7722` |

These receipts establish exact source identity only. The earlier tracked PDF
passed its own complete audit against the pre-template-parity source; the
current derivative still requires a fresh TeX build, PDF parity, metadata
scan, and visual preflight before it becomes the release PDF.

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
