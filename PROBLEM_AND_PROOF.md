# Problem and proof scope

## Source target

The authoritative target is arXiv:2004.12497v11, row `k_607`. In paraphrase,
the row proposes that the quotient of the signed areas of the two focal
antipedal polygons equals `1` for elliptic-billiard periods divisible by four.
The displayed quotient has no stated nonzero-denominator condition.

The source prose uses the word “rays,” but the audited theorem and exact
witness use complete perpendicular supporting lines. No literal oriented
half-ray theorem is claimed.

## Corrected theorem

Let an exact even-period elliptic-billiard orbit have vertices
`P_0,...,P_(N-1)` and foci `F_1,F_2`. For each focus, take the complete line
through `P_i` perpendicular to `P_i-F_j`, and form the ordered antipedal
polygon from consecutive finite intersections.

The half-turn about the ellipse center sends `P_i` to `P_(i+N/2)`, sends
`F_1` to `F_2`, and sends each first-focus supporting line to the corresponding
second-focus supporting line. It therefore sends one ordered antipedal polygon
to the other by a cyclic shift. A planar half-turn preserves orientation and
signed area, so

```text
bar A_1^* = bar A_2^*.
```

Consequently, the quotient is defined exactly on the common nonzero-area
locus, and it equals `1` there.

## Exact domain counterexample

The audited certificate uses the unique root `u` in `(5/16,157/500)` of

```text
u^4 - 6u^3 - 2u^2 - 2u + 1 = 0
```

and the normalization

```text
a^2 = (1-u)^3(1+u)/(4u^3),  b=1.
```

It produces one noncircular, primitive one-winding `N=8` orbit tangent on open
segments to a nondegenerate confocal caustic. All sixteen supporting-line
intersections are finite, while both focal signed antipedal areas equal zero.
Thus the source quotient is `0/0` at that phase.

The exact coordinate certificate and its independent public replay are not yet
integrated in this staging repository. Until they are, this document is a
public-safe scope summary rather than a self-contained release proof.

## What is and is not answered

The package resolves the arXiv-v11/AMR target under complete supporting-line
semantics through a domain counterexample and corrected identity. It does not
prove a literal half-ray result, an unsigned-area result, a general zero-locus
classification, zeros at other periods or caustics, a neighboring invariant,
the differently formulated journal row, or another named open problem.

