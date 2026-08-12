import Std
import Lean.Elab.Tactic.Decide

/-!
# AMR-050-0035 / arXiv-v11 k_607: finite exact certificate only

This file kernel-checks the closed finite algebraic data of the canonical
eight-vertex supporting-line witness.  Its coefficient algebra is a concrete
reduced model with basis

  1, u, u^2, u^3;  a times that basis;  c times that basis;  ac times it,

and relations

  u^4 - 6u^3 - 2u^2 - 2u + 1 = 0,
  a^2 = R(u),
  c^2 = R(u) - 1.

The certificate deliberately does not construct a real embedding, prove root
existence or uniqueness, establish positivity/cyclic order/one winding, prove
the unsquared directed reflection law, interpret the source's word `rays`, or
formalize source semantics, priority, or novelty.  All exported proofs use
kernel-mode `decide` over exact rational coefficients.
-/

namespace K607FiniteCertificate

def rq (n d : Int) : Rat := n / d

structure K4 where
  c0 : Rat
  c1 : Rat
  c2 : Rat
  c3 : Rat
deriving DecidableEq, Repr

namespace K4

def mk4 (a b c d : Rat) : K4 := ⟨a, b, c, d⟩
def zero : K4 := mk4 0 0 0 0
def one : K4 := mk4 1 0 0 0
def u : K4 := mk4 0 1 0 0

def add (x y : K4) : K4 :=
  mk4 (x.c0 + y.c0) (x.c1 + y.c1) (x.c2 + y.c2) (x.c3 + y.c3)

def neg (x : K4) : K4 := mk4 (-x.c0) (-x.c1) (-x.c2) (-x.c3)

/- Multiplication followed by descending reduction with
   u^4 = 6u^3 + 2u^2 + 2u - 1. -/
def mul (x y : K4) : K4 :=
  let p0 := x.c0 * y.c0
  let p1 := x.c0 * y.c1 + x.c1 * y.c0
  let p2 := x.c0 * y.c2 + x.c1 * y.c1 + x.c2 * y.c0
  let p3 := x.c0 * y.c3 + x.c1 * y.c2 + x.c2 * y.c1 + x.c3 * y.c0
  let p4 := x.c1 * y.c3 + x.c2 * y.c2 + x.c3 * y.c1
  let p5 := x.c2 * y.c3 + x.c3 * y.c2
  let p6 := x.c3 * y.c3
  let v5 := p5 + 6 * p6
  let v4 := p4 + 2 * p6 + 6 * v5
  mk4
    (p0 - v4)
    (p1 - v5 + 2 * v4)
    (p2 - p6 + 2 * v5 + 2 * v4)
    (p3 + 2 * p6 + 2 * v5 + 6 * v4)

instance : Zero K4 := ⟨zero⟩
instance : One K4 := ⟨one⟩
instance : Add K4 := ⟨add⟩
instance : Neg K4 := ⟨neg⟩
instance : Sub K4 := ⟨fun x y => add x (neg y)⟩
instance : Mul K4 := ⟨mul⟩

def ofRat (q : Rat) : K4 := mk4 q 0 0 0

end K4

open K4

def rK : K4 := mk4 3 (rq 1 2) 3 (rq (-1) 2)

structure E where
  k0 : K4
  kA : K4
  kC : K4
  kAC : K4
deriving DecidableEq, Repr

namespace E

def mkE (x0 xA xC xAC : K4) : E := ⟨x0, xA, xC, xAC⟩
def zero : E := mkE 0 0 0 0
def one : E := mkE 1 0 0 0
def embedK (x : K4) : E := mkE x 0 0 0
def ofRat (q : Rat) : E := embedK (K4.ofRat q)

def add (x y : E) : E :=
  mkE (x.k0 + y.k0) (x.kA + y.kA) (x.kC + y.kC) (x.kAC + y.kAC)

def neg (x : E) : E := mkE (-x.k0) (-x.kA) (-x.kC) (-x.kAC)

/- Multiplication in the basis 1,a,c,ac using a^2=R and c^2=R-1. -/
def mul (x y : E) : E :=
  let rm1 := rK - 1
  mkE
    (x.k0 * y.k0 + rK * (x.kA * y.kA) + rm1 * (x.kC * y.kC) +
      (rK * rm1) * (x.kAC * y.kAC))
    (x.k0 * y.kA + x.kA * y.k0 + rm1 * (x.kC * y.kAC + x.kAC * y.kC))
    (x.k0 * y.kC + x.kC * y.k0 + rK * (x.kA * y.kAC + x.kAC * y.kA))
    (x.k0 * y.kAC + x.kAC * y.k0 + x.kA * y.kC + x.kC * y.kA)

instance : Zero E := ⟨zero⟩
instance : One E := ⟨one⟩
instance : Add E := ⟨add⟩
instance : Neg E := ⟨neg⟩
instance : Sub E := ⟨fun x y => add x (neg y)⟩
instance : Mul E := ⟨mul⟩

end E

open E

def Q (n : Int) : E := E.ofRat n
def Qf (n d : Int) : E := E.ofRat (rq n d)
def U : E := embedK K4.u
def R : E := embedK rK
def A : E := mkE 0 1 0 0
def C : E := mkE 0 0 1 0

def S : E := embedK (mk4 (rq (-1) 4) (rq 9 4) (rq 5 4) (rq (-1) 4))
def Co : E := embedK (mk4 (rq 3 4) (rq 3 4) (rq (-7) 4) (rq 1 4))
def Lam : E := embedK (mk4 (rq 5 8) (rq (-7) 4) (rq 15 8) (rq (-1) 4))
def CX : E := embedK (mk4 (rq 19 8) (rq 9 4) (rq 9 8) (rq (-1) 4))
def CY : E := embedK (mk4 (rq 3 8) (rq 7 4) (rq (-15) 8) (rq 1 4))

def invR : E := embedK (mk4 (rq 5 16) (rq 1 16) (rq (-7) 16) (rq 1 16))
def invLam : E := embedK (mk4 (rq 41 16) (rq 53 16) (rq 61 16) (rq (-11) 16))
def invCX : E := embedK (mk4 (rq 7 16) (rq (-15) 32) (rq 1 4) (rq (-1) 32))
def invCY : E := embedK (mk4 1 (rq 1 2) 2 (rq (-1) 2))
def invOnePlusUSq : E := embedK (mk4 (rq 7 8) (rq 3 8) (rq (-7) 8) (rq 1 8))
def invOnePlusRUSq : E := embedK (mk4 (rq 3 8) (rq 7 4) (rq (-15) 8) (rq 1 4))

structure Point where
  x : E
  y : E
deriving DecidableEq, Repr

structure Line where
  a : E
  b : E
  d : E
deriving DecidableEq, Repr

def point (x y : E) : Point := ⟨x, y⟩
def pneg (p : Point) : Point := point (-p.x) (-p.y)
def psub (p q : Point) : Point := point (p.x - q.x) (p.y - q.y)
def cross (p q : Point) : E := p.x * q.y - p.y * q.x

def lineThrough (p q : Point) : Line :=
  let x := p.y - q.y
  let y := q.x - p.x
  ⟨x, y, x * p.x + y * p.y⟩

def antipedalLine (p focus : Point) : Line :=
  let x := p.x - focus.x
  let y := p.y - focus.y
  ⟨x, y, p.x * x + p.y * y⟩

def lineEval (l : Line) (p : Point) : E := l.a * p.x + l.b * p.y - l.d
def lineDet (l m : Line) : E := l.a * m.b - m.a * l.b
def dualCausticResidual (l : Line) : E := CX * l.a * l.a + CY * l.b * l.b - l.d * l.d
def outerClearedResidual (p : Point) : E := p.x * p.x + R * p.y * p.y - R

def P0 : Point := point A 0
def P1 : Point := point (A * Co) S
def P2 : Point := point 0 (Q 1)
def P3 : Point := point (-A * Co) S
def P4 : Point := point (-A) 0
def P5 : Point := point (-A * Co) (-S)
def P6 : Point := point 0 (Q (-1))
def P7 : Point := point (A * Co) (-S)
def polygon : List Point := [P0, P1, P2, P3, P4, P5, P6, P7]

def L0 : Line := lineThrough P0 P1
def L1 : Line := lineThrough P1 P2
def L2 : Line := lineThrough P2 P3
def L3 : Line := lineThrough P3 P4
def L4 : Line := lineThrough P4 P5
def L5 : Line := lineThrough P5 P6
def L6 : Line := lineThrough P6 P7
def L7 : Line := lineThrough P7 P0
def sideLines : List Line := [L0, L1, L2, L3, L4, L5, L6, L7]

def Fplus : Point := point C 0
def Fminus : Point := point (-C) 0

def PL0 : Line := antipedalLine P0 Fplus
def PL1 : Line := antipedalLine P1 Fplus
def PL2 : Line := antipedalLine P2 Fplus
def PL3 : Line := antipedalLine P3 Fplus
def PL4 : Line := antipedalLine P4 Fplus
def PL5 : Line := antipedalLine P5 Fplus
def PL6 : Line := antipedalLine P6 Fplus
def PL7 : Line := antipedalLine P7 Fplus

def ML0 : Line := antipedalLine P0 Fminus
def ML1 : Line := antipedalLine P1 Fminus
def ML2 : Line := antipedalLine P2 Fminus
def ML3 : Line := antipedalLine P3 Fminus
def ML4 : Line := antipedalLine P4 Fminus
def ML5 : Line := antipedalLine P5 Fminus
def ML6 : Line := antipedalLine P6 Fminus
def ML7 : Line := antipedalLine P7 Fminus

def h : K4 := mk4 (rq 1 2) 0 (rq (-1) 2) 0
def mh : K4 := -h
def m : K4 := mk4 (rq (-1) 2) (-1) (rq 1 2) 0
def mm : K4 := -m
def n : K4 := mk4 (rq (-1) 2) (-1) (rq (-1) 2) 0
def nn : K4 := -n
def ku : K4 := K4.u

def QP0 : Point := point A (mkE (-ku) 0 0 ku)
def QP1 : Point := point (mkE 0 h m 0) (mkE n 0 0 h)
def QP2 : Point := point (mkE 0 mh m 0) (mkE n 0 0 mh)
def QP3 : Point := point (-A) (mkE (-ku) 0 0 (-ku))
def QP4 : Point := point (-A) (mkE ku 0 0 ku)
def QP5 : Point := point (mkE 0 mh m 0) (mkE nn 0 0 h)
def QP6 : Point := point (mkE 0 h m 0) (mkE nn 0 0 mh)
def QP7 : Point := point A (mkE ku 0 0 (-ku))
def plusVertices : List Point := [QP0, QP1, QP2, QP3, QP4, QP5, QP6, QP7]

def QM0 : Point := point A (mkE (-ku) 0 0 (-ku))
def QM1 : Point := point (mkE 0 h mm 0) (mkE n 0 0 mh)
def QM2 : Point := point (mkE 0 mh mm 0) (mkE n 0 0 h)
def QM3 : Point := point (-A) (mkE (-ku) 0 0 ku)
def QM4 : Point := point (-A) (mkE ku 0 0 (-ku))
def QM5 : Point := point (mkE 0 mh mm 0) (mkE nn 0 0 mh)
def QM6 : Point := point (mkE 0 h mm 0) (mkE nn 0 0 h)
def QM7 : Point := point A (mkE ku 0 0 ku)
def minusVertices : List Point := [QM0, QM1, QM2, QM3, QM4, QM5, QM6, QM7]

def signedDoubleArea8 (p0 p1 p2 p3 p4 p5 p6 p7 : Point) : E :=
  cross p0 p1 + cross p1 p2 + cross p2 p3 + cross p3 p4 +
  cross p4 p5 + cross p5 p6 + cross p6 p7 + cross p7 p0

def plusArea2 : E := signedDoubleArea8 QP0 QP1 QP2 QP3 QP4 QP5 QP6 QP7
def minusArea2 : E := signedDoubleArea8 QM0 QM1 QM2 QM3 QM4 QM5 QM6 QM7

def i0 : K4 := mk4 1 (rq 3 2) 3 (rq (-1) 2)
def i1a : K4 := mk4 (rq 3 8) (rq 1 8) (rq 3 8) (rq (-3) 8)
def i1c : K4 := mk4 (rq 1 8) (rq 1 8) (rq 5 8) (rq 1 8)

def invD0 : E := mkE 0 i0 i0 0
def invD1 : E := mkE 0 i1a i1c 0
def invD2 : E := mkE 0 i1a (-i1c) 0
def invD3 : E := mkE 0 i0 (-i0) 0

def plusDeterminants : List E :=
  [lineDet PL0 PL1, lineDet PL1 PL2, lineDet PL2 PL3, lineDet PL3 PL4,
   lineDet PL4 PL5, lineDet PL5 PL6, lineDet PL6 PL7, lineDet PL7 PL0]

def minusDeterminants : List E :=
  [lineDet ML0 ML1, lineDet ML1 ML2, lineDet ML2 ML3, lineDet ML3 ML4,
   lineDet ML4 ML5, lineDet ML5 ML6, lineDet ML6 ML7, lineDet ML7 ML0]

def plusDetInverses : List E := [invD0, invD1, invD2, invD3, invD3, invD2, invD1, invD0]
def minusDetInverses : List E := [invD3, invD2, invD1, invD0, invD0, invD1, invD2, invD3]

def products (xs ys : List E) : List E := List.zipWith (fun x y => x * y) xs ys

def allNonzero (xs : List E) : Bool := xs.all (fun x => decide (x ≠ 0))

def plusIncidenceResiduals : List E :=
  [lineEval PL0 QP0, lineEval PL1 QP0,
   lineEval PL1 QP1, lineEval PL2 QP1,
   lineEval PL2 QP2, lineEval PL3 QP2,
   lineEval PL3 QP3, lineEval PL4 QP3,
   lineEval PL4 QP4, lineEval PL5 QP4,
   lineEval PL5 QP5, lineEval PL6 QP5,
   lineEval PL6 QP6, lineEval PL7 QP6,
   lineEval PL7 QP7, lineEval PL0 QP7]

def minusIncidenceResiduals : List E :=
  [lineEval ML0 QM0, lineEval ML1 QM0,
   lineEval ML1 QM1, lineEval ML2 QM1,
   lineEval ML2 QM2, lineEval ML3 QM2,
   lineEval ML3 QM3, lineEval ML4 QM3,
   lineEval ML4 QM4, lineEval ML5 QM4,
   lineEval ML5 QM5, lineEval ML6 QM5,
   lineEval ML6 QM6, lineEval ML7 QM6,
   lineEval ML7 QM7, lineEval ML0 QM7]

def outerResiduals : List E := polygon.map outerClearedResidual
def tangencyResiduals : List E := sideLines.map dualCausticResidual

def zero8 : List E := List.replicate 8 0
def zero16 : List E := List.replicate 16 0
def one8 : List E := List.replicate 8 (Q 1)

def gU : E := U * U * U * U - Q 6 * U * U * U - Q 2 * U * U - Q 2 * U + Q 1

def rootParameterResidual : E :=
  Q 4 * R * U * U * U - (Q 1 - U) * (Q 1 - U) * (Q 1 - U) * (Q 1 + U)

def closurePoly : E :=
  U * U * U * U + (Q 4 * R - Q 2) * U * U * U + Q 2 * U - Q 1

def squaredReflectionResidual : E :=
  let leftNum := Q 2 * R * U * U + Q 1 - U * U
  let leftDenSq := R * U * U + Q 1
  let rightNum := (Q 1 + U) * (Q 2 * R * U + (Q 1 - U) * (Q 1 - U))
  let rightDenSq := R * (Q 1 + U) * (Q 1 + U) + (Q 1 - U) * (Q 1 - U)
  leftNum * leftNum * rightDenSq - rightNum * rightNum * leftDenSq

def gRat (x : Rat) : Rat := x*x*x*x - 6*x*x*x - 2*x*x - 2*x + 1
def lower : Rat := rq 5 16
def upper : Rat := rq 157 500

def algebraProp : Prop :=
  gU = 0 ∧ A * A = R ∧ C * C = R - Q 1 ∧
  rootParameterResidual = 0 ∧
  (Q 1 + U * U) * S = Q 2 * U ∧
  (Q 1 + U * U) * Co = Q 1 - U * U ∧
  Co * Co + S * S = Q 1 ∧
  (Q 1 + R * U * U) * Lam = R * U * U ∧
  CX = R - Lam ∧ CY = Q 1 - Lam

def rootBracketProp : Prop :=
  gRat lower = rq 401 65536 ∧
  gRat upper = rq (-76605799) 62500000000 ∧
  gRat lower > 0 ∧ gRat upper < 0 ∧ upper < rq 1 3

def conicDenominatorUnitsProp : Prop :=
  R * invR = Q 1 ∧ Lam * invLam = Q 1 ∧
  CX * invCX = Q 1 ∧ CY * invCY = Q 1 ∧
  (Q 1 + U * U) * invOnePlusUSq = Q 1 ∧
  (Q 1 + R * U * U) * invOnePlusRUSq = Q 1

def orbitConicProp : Prop :=
  polygon.Nodup ∧ outerResiduals = zero8 ∧ tangencyResiduals = zero8 ∧
  P4 = pneg P0 ∧ P5 = pneg P1 ∧ P6 = pneg P2 ∧ P7 = pneg P3 ∧
  (8 % 4 = 0)

def reflectionSquaredProp : Prop :=
  closurePoly = 0 ∧
  squaredReflectionResidual = -(R * (Q 1 + U * U) * (Q 1 + U * U) * closurePoly) ∧
  squaredReflectionResidual = 0

def finiteIntersectionProp : Prop :=
  plusIncidenceResiduals = zero16 ∧ minusIncidenceResiduals = zero16 ∧
  products plusDeterminants plusDetInverses = one8 ∧
  products minusDeterminants minusDetInverses = one8 ∧
  allNonzero plusDeterminants = true ∧ allNonzero minusDeterminants = true ∧
  Q 1 ≠ 0

def centralInversionProp : Prop :=
  QM4 = pneg QP0 ∧ QM5 = pneg QP1 ∧ QM6 = pneg QP2 ∧ QM7 = pneg QP3 ∧
  QM0 = pneg QP4 ∧ QM1 = pneg QP5 ∧ QM2 = pneg QP6 ∧ QM3 = pneg QP7

def areaDomainProp : Prop :=
  plusArea2 = 0 ∧ minusArea2 = 0 ∧
  ¬ (plusArea2 ≠ 0) ∧ ¬ (minusArea2 ≠ 0) ∧
  ¬ (plusArea2 ≠ 0 ∧ minusArea2 ≠ 0)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 5000000 in
theorem algebraCertificate : algebraProp := by
  unfold algebraProp
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 5000000 in
theorem rootBracketCertificate : rootBracketProp := by
  unfold rootBracketProp
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 5000000 in
theorem conicDenominatorUnitsCertificate : conicDenominatorUnitsProp := by
  unfold conicDenominatorUnitsProp
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 5000000 in
theorem orbitConicCertificate : orbitConicProp := by
  unfold orbitConicProp
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 5000000 in
theorem reflectionSquaredCertificate : reflectionSquaredProp := by
  unfold reflectionSquaredProp
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 5000000 in
theorem finiteIntersectionCertificate : finiteIntersectionProp := by
  unfold finiteIntersectionProp
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 5000000 in
theorem centralInversionCertificate : centralInversionProp := by
  unfold centralInversionProp
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 5000000 in
theorem areaDomainCertificate : areaDomainProp := by
  unfold areaDomainProp
  decide +kernel

theorem finiteExactCertificate :
    algebraProp ∧ rootBracketProp ∧ conicDenominatorUnitsProp ∧
    orbitConicProp ∧ reflectionSquaredProp ∧ finiteIntersectionProp ∧
    centralInversionProp ∧ areaDomainProp := by
  exact ⟨algebraCertificate, rootBracketCertificate, conicDenominatorUnitsCertificate,
    orbitConicCertificate, reflectionSquaredCertificate, finiteIntersectionCertificate,
    centralInversionCertificate, areaDomainCertificate⟩

end K607FiniteCertificate
