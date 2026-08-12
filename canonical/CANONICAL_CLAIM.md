# Canonical claim

## Convention

Use complete affine lines through each billiard vertex, perpendicular to the
segment joining that vertex to the selected focus. Consecutive finite line
intersections form the ordered focal antipedal polygon. Area means cyclic
signed shoelace area.

## Corrected all-even theorem

Let an exact even-period elliptic-billiard orbit have vertices
`P_0,...,P_(N-1)`, opposite foci `F_1,F_2`, and finite consecutive
supporting-line intersections. The half-turn about the ellipse center sends

```text
P_i       to P_(i+N/2),
F_1       to F_2,
L_(1,i)   to L_(2,i+N/2),
Q_(1,i)   to Q_(2,i+N/2).
```

Thus the ordered focal antipedal polygons are congruent by an
orientation-preserving half-turn and a cyclic shift. Their cyclic signed
areas satisfy

```text
bar A_1^* = bar A_2^*.
```

The real quotient is defined precisely where this common signed area is
nonzero, and it equals `1` there.

## Exact `N=8` domain certificate

Let `u` be the unique root in `(313/1000,157/500)` of

```text
u^4 - 6u^3 - 2u^2 - 2u + 1 = 0,
```

and define

```text
r = (1-u)^3(1+u)/(4u^3),
a = sqrt(r),  b = 1,
c = sqrt(r-1),
C = (1-u^2)/(1+u^2),
S = 2u/(1+u^2),
lambda = r*u^2/(1+r*u^2).
```

The certified ordered vertices are

```text
(a,0), (aC,S), (0,1), (-aC,S),
(-a,0), (-aC,-S), (0,-1), (aC,-S).
```

The audited exact construction is noncircular, nondegenerate, primitive,
one-winding, tangent on each open side segment to a single interior confocal
caustic, and satisfies the billiard reflection law. All sixteen consecutive
supporting-line intersections are finite. Its two focal signed antipedal
areas are both zero.

Consequently, the unqualified quotient in arXiv:2004.12497v11 source-table
row `k_607` evaluates to the undefined expression `0/0` at an admissible
`N=8` phase. This is a domain counterexample. It is not a defined nonunit
ratio and not a counterexample to signed-area equality.

The exact coordinate proof, certificate, and independent replay are not yet
present in this repository. Public release remains blocked until those
artifacts are integrated and independently verified.

