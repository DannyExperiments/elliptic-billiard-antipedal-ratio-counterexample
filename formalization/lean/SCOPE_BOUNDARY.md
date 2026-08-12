# Scope boundary

## Maximum accurate claim

> Lean 4 kernel checking and a separate Python-standard-library exact replay
> independently verify the closed finite algebraic certificate for the
> canonical `N=8` supporting-line data: the quartic/semiaxis identities,
> rational root bracket, eight indexed conic vertices, eight dual-caustic
> tangencies, the cleared squared reflection identity, all sixteen finite
> focal supporting-line intersections, central-inversion focus exchange, both
> focal antipedal signed areas equal to zero, and failure of the nonzero
> quotient-domain predicate.

The formalization status is:

```text
FORMALIZATION_PARTIAL__FINITE_EXACT_SUPPORTING_LINE_CERTIFICATE_PASS
```

## What the Lean artifact checks

- a concrete 16-coordinate rational reduction algebra satisfying the exact
  quartic, semiaxis, focus, trigonometric, and caustic-parameter identities;
- exact rational values of the quartic at `5/16` and `157/500`, their opposite
  signs, and `157/500 < 1/3`;
- explicit units for the principal conic and parameter denominators;
- eight pairwise-distinct coefficient points, their central symmetry, eight
  outer-conic equations, and eight dual-caustic tangency equations;
- the squared-and-cleared reflection residual at the non-axis vertex type;
- sixteen displayed supporting-line incidences and direct nonzero plus unit
  checks for every adjacent-line determinant;
- focus exchange by central inversion;
- both exact signed double-areas equal to zero and failure of each quotient
  denominator's nonzero predicate.

## What the independent verifier adds

The standard-library verifier reconstructs the same exact field arithmetic by
Gaussian-elimination inverses rather than hard-coded inverse witnesses.  It
also performs clearly labeled floating-point diagnostics for the real root,
open-segment contact, and the source's ambiguous half-ray wording.  Those
floating-point diagnostics are useful checks, not formal proofs and not part
of the Lean theorem.

## Excluded claims

Neither artifact formalizes:

- existence, uniqueness, or isolation of the relevant real quartic root;
- an injective ordered-real embedding of the coefficient algebra;
- positivity of all geometric parameters;
- the unsquared directed reflection law;
- cyclic angular order, counterclockwise orientation, primitivity, or
  one-winding topology;
- a continuous Poncelet family;
- literal oriented half-rays.  The certified construction uses complete
  supporting lines;
- source interpretation, identifier chronology, novelty, historical priority,
  peer review, or publication readiness;
- the entire AMR-050-0035 / arXiv-v11 `k_607` theorem.

Forbidden descriptions include `Lean verified counterexample`, `Lean proof of
k_607`, `full theorem formalization`, and `formally verified primitive
one-winding orbit`.

## Ratio-domain rule

The supporting-line construction has both focal signed areas exactly zero at
the formal datum.  The package records that neither possible denominator is
nonzero.  It does not simplify `0/0`, assign a quotient value, or claim an
inequality between undefined expressions.
