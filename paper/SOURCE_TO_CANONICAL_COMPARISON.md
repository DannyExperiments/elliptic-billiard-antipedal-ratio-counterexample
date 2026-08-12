# Source-to-canonical manuscript comparison

## Controlling artifacts

| Object | SHA-256 | Function |
|---|---|---|
| Candidate B ZIP | `d3be5f3af03954877e0634e0959dcba72261ded8cbdcfedce2c1baafaf66c5d0` | Single unchanged canonical proof container |
| Candidate B `REPORT.md` | `ea03a396bc65fe1b935d73ea323a1eeba7078d4f2f0b1e1eaa8ecc2b3c0ff8bc` | Sole proof base |
| Stage-3 canonical theorem and scope | `f42372031f9c810bb3ed06530b28ee3d083b38747fdb30a4e25d92c4dbe1666f` | Frozen theorem, source, numbering, and priority boundary |
| Stage-3 dependency map | `09dd2bc8e5247188403a3f5a20de98e7a3891542ee83b25accc33be184a93faf` | Proof and evidence dependencies |
| Stage-3 claims/evidence matrix | `d521228f0ffefd28412a36bd14ae5630fc943ba8367a02981beffa6e4558d20c` | Claim-level release boundary |
| Mathematical adjudication | `b2f005e91801ecc2d4d32fa9b580414b8ccd02448c408e56980cdb48f09427d6` | Mathematical pass and required qualifications |
| Literature/priority adjudication | `026ee68b058b75ba7d1a373c760efc3a35ec830aa51dacd2623a9cb03c78be7c` | Bounded novelty and prior-component carveouts |
| Implications scope audit | `5ddaa1c362398b2c74d7cf25e7a492f22a9882fdeca2387e904c5a7e48fa2109` | Prohibited extrapolations and one-problem boundary |

Candidate A and Candidate C were not used to write or repair the manuscript.
The source is an expository restatement of frozen Candidate B, subject only to
the already-frozen audit, priority, and implications qualifications.

## Claim mapping

| Manuscript content | Canonical source | Relation |
|---|---|---|
| Exact arXiv-v11 `k_607` problem and direct `0/0` answer on page 1 | Candidate B result; source receipt; canonical `C00`, `C09` | Faithful, with mandatory version/formula qualification |
| Complete supporting-line definition and signed shoelace area | Candidate B §§2–4,7; canonical `C16` | Faithful; makes the controlling convention explicit |
| Corrected central-inversion theorem | Candidate B §§1–4; canonical `C10`–`C12` | Same proof, stated first for its exact polygonal hypotheses |
| Nonparallel/finiteness lemma | Candidate B §3 | Faithful and self-contained |
| Root interval, quartic, semiaxis, and octagon coordinates | Candidate B §5.1 | Byte-level formulas preserved |
| Cyclic order, primitivity, and one winding | Candidate B §5.1 | Expository expansion only; no scope change |
| Caustic parameter and two-side tangency reduction | Candidate B §5.2 | Formula-preserving restatement |
| Open-segment contact | Candidate B §5.2 | Same strict-interior/convexity argument |
| Direct reflection equation and positivity guard | Candidate B §5.2 | Same unsquared equality and squared residual |
| Four determinant factorizations and sixteen finite intersections | Candidate B §5.3 | Same exact expressions and symmetry propagation |
| Line-intersection formula and area factorization | Candidate B §5.4 | Same exact formula and positive-denominator guard |
| Second focal zero | Candidate B §§2,4,5.4 | Same cyclic-shift central-inversion proof |
| Half-ray exclusion | Candidate B §7 plus frozen math audit qualification | Narrows Candidate B's ray-transport sentence to the audited result; no new theorem |
| Bounded novelty and prior-component credit | Stage-2 priority adjudication | Mandatory qualification, not a proof patch |
| Computational/formalization status | Independent verifier and partial Lean receipts | Corroboration only, explicitly separated from proof |

## Intentional omissions

- Candidate B's separate `N=6` construction is omitted because other-period
  zeros are outside the headline and already have material prior disclosure.
- No Candidate A normalization or Candidate C coordinate display is included.
- No whole zero-locus question is pursued.
- No broad hyperbola-caustic or arbitrary-turning-class theorem is stated.
- No literal half-ray polygon is defined.
- No journal `k607`, neighboring-row, or second-problem solve is claimed.

## Editorial changes that do not alter mathematics

- The source problem and answer are placed on the first page.
- Candidate B's result is split into a corrected structural theorem and the
  exact witness theorem.
- Notation is normalized to `F_+`, `F_-`, and zero-based cyclic indices.
- Prior-component citations and bounded novelty wording are added from the
  frozen priority adjudication.
- Computation and partial Lean status are moved to a separate verification
  section so no software output is mistaken for the geometric proof.
- Repository identity `DannyExperiments` is supplied as the sole author, with
  no affiliation; AI systems appear only in the disclosure.

Any later mathematical alteration to the quartic, root interval, orbit,
caustic, reflection bridge, line construction, signed-area formula, theorem
quantifiers, or novelty boundary creates a new manuscript version requiring
comparison and re-audit.
