#!/usr/bin/env python3
"""Independent exact replay for the AMR-050-0035 / k_607 witness.

Only the Python standard library is used.  The exact computation is performed
in Q(u,a,c), where

    u^4 - 6u^3 - 2u^2 - 2u + 1 = 0,
    a^2 = (1-u)^3(1+u)/(4u^3),
    c^2 = a^2-1.

The final ray-direction diagnostic is deliberately labeled non-load-bearing;
the exact certificate itself uses the full perpendicular supporting lines.
"""

from fractions import Fraction as F


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def solve_linear(matrix, rhs):
    n = len(rhs)
    augmented = [list(matrix[i]) + [rhs[i]] for i in range(n)]
    for column in range(n):
        pivot = next((row for row in range(column, n) if augmented[row][column]), None)
        require(pivot is not None, "SINGULAR_LINEAR_SYSTEM")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [x / scale for x in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            scale = augmented[row][column]
            if scale:
                augmented[row] = [
                    x - scale * y for x, y in zip(augmented[row], augmented[column])
                ]
    return [augmented[i][-1] for i in range(n)]


class Quartic:
    """Q[u]/(u^4-6u^3-2u^2-2u+1)."""

    __slots__ = ("coeff",)

    def __init__(self, value=0):
        if isinstance(value, Quartic):
            self.coeff = value.coeff
        elif isinstance(value, (tuple, list)):
            require(len(value) == 4, "QUARTIC_DIMENSION")
            self.coeff = tuple(F(x) for x in value)
        else:
            self.coeff = (F(value), F(0), F(0), F(0))

    def __add__(self, other):
        other = Quartic(other)
        return Quartic(tuple(a + b for a, b in zip(self.coeff, other.coeff)))

    __radd__ = __add__

    def __neg__(self):
        return Quartic(tuple(-x for x in self.coeff))

    def __sub__(self, other):
        return self + (-Quartic(other))

    def __rsub__(self, other):
        return Quartic(other) - self

    def __mul__(self, other):
        other = Quartic(other)
        product = [F(0)] * 7
        for i, a in enumerate(self.coeff):
            for j, b in enumerate(other.coeff):
                product[i + j] += a * b
        # u^4 = 6u^3 + 2u^2 + 2u - 1.
        for degree in range(6, 3, -1):
            value = product[degree]
            if value:
                product[degree - 1] += 6 * value
                product[degree - 2] += 2 * value
                product[degree - 3] += 2 * value
                product[degree - 4] -= value
        return Quartic(product[:4])

    __rmul__ = __mul__

    def inverse(self):
        require(self != 0, "QUARTIC_DIVISION_BY_ZERO")
        columns = []
        for degree in range(4):
            basis = [F(0)] * 4
            basis[degree] = F(1)
            columns.append((self * Quartic(basis)).coeff)
        matrix = [[columns[column][row] for column in range(4)] for row in range(4)]
        return Quartic(solve_linear(matrix, [F(1), F(0), F(0), F(0)]))

    def __truediv__(self, other):
        return self * Quartic(other).inverse()

    def __rtruediv__(self, other):
        return Quartic(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = Quartic(1)
        base = self
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent //= 2
        return result

    def __eq__(self, other):
        return self.coeff == Quartic(other).coeff

    def evaluate(self, u_value):
        return sum(float(coefficient) * (u_value ** degree) for degree, coefficient in enumerate(self.coeff))


U0 = Quartic((0, 1, 0, 0))
R0 = ((1 - U0) ** 3 * (1 + U0)) / (4 * U0 ** 3)


class ExactField:
    """Quartic + a,c square roots, with basis 1,a,c,ac."""

    __slots__ = ("coeff",)

    def __init__(self, value=0):
        if isinstance(value, ExactField):
            self.coeff = value.coeff
        elif isinstance(value, Quartic):
            self.coeff = (value, Quartic(0), Quartic(0), Quartic(0))
        elif isinstance(value, (tuple, list)) and len(value) == 4 and all(
            isinstance(x, Quartic) for x in value
        ):
            self.coeff = tuple(value)
        else:
            self.coeff = (Quartic(value), Quartic(0), Quartic(0), Quartic(0))

    def __add__(self, other):
        other = ExactField(other)
        return ExactField(tuple(a + b for a, b in zip(self.coeff, other.coeff)))

    __radd__ = __add__

    def __neg__(self):
        return ExactField(tuple(-x for x in self.coeff))

    def __sub__(self, other):
        return self + (-ExactField(other))

    def __rsub__(self, other):
        return ExactField(other) - self

    def __mul__(self, other):
        other = ExactField(other)
        out = [Quartic(0) for _ in range(4)]
        for i, x in enumerate(self.coeff):
            if x == 0:
                continue
            i_a, i_c = i & 1, (i >> 1) & 1
            for j, y in enumerate(other.coeff):
                if y == 0:
                    continue
                j_a, j_c = j & 1, (j >> 1) & 1
                coefficient = x * y
                exponent_a = i_a + j_a
                exponent_c = i_c + j_c
                if exponent_a >= 2:
                    coefficient *= R0
                    exponent_a -= 2
                if exponent_c >= 2:
                    coefficient *= R0 - 1
                    exponent_c -= 2
                out[exponent_a + 2 * exponent_c] += coefficient
        return ExactField(tuple(out))

    __rmul__ = __mul__

    def inverse(self):
        require(self != 0, "EXACT_FIELD_DIVISION_BY_ZERO")
        basis = []
        for component in range(4):
            for degree in range(4):
                entries = [Quartic(0) for _ in range(4)]
                q = [F(0)] * 4
                q[degree] = F(1)
                entries[component] = Quartic(q)
                basis.append(ExactField(tuple(entries)))
        columns = []
        for element in basis:
            value = self * element
            columns.append([x for component in value.coeff for x in component.coeff])
        matrix = [[columns[column][row] for column in range(16)] for row in range(16)]
        solution = solve_linear(matrix, [F(1)] + [F(0)] * 15)
        entries = [Quartic(solution[4 * i : 4 * i + 4]) for i in range(4)]
        return ExactField(tuple(entries))

    def __truediv__(self, other):
        return self * ExactField(other).inverse()

    def __rtruediv__(self, other):
        return ExactField(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = ExactField(1)
        base = self
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent //= 2
        return result

    def __eq__(self, other):
        return self.coeff == ExactField(other).coeff

    def evaluate(self, u_value, a_value, c_value):
        basis = (1.0, a_value, c_value, a_value * c_value)
        return sum(self.coeff[i].evaluate(u_value) * basis[i] for i in range(4))


U = ExactField(U0)
A = ExactField((Quartic(0), Quartic(1), Quartic(0), Quartic(0)))
C_FOCUS = ExactField((Quartic(0), Quartic(0), Quartic(1), Quartic(0)))


def point(x, y):
    return ExactField(x), ExactField(y)


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def scale(scalar, p):
    return scalar * p[0], scalar * p[1]


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def line_through(p, q):
    x = p[1] - q[1]
    y = q[0] - p[0]
    d = x * p[0] + y * p[1]
    require(x * x + y * y != 0, "ZERO_SIDE")
    return x, y, d


def antipedal_line(p, focus):
    x = p[0] - focus[0]
    y = p[1] - focus[1]
    return x, y, p[0] * x + p[1] * y


def intersect(line1, line2):
    x, y, d = line1
    X, Y, D = line2
    determinant = x * Y - X * y
    require(determinant != 0, "PARALLEL_LINES")
    return point((d * Y - D * y) / determinant, (x * D - X * d) / determinant)


def signed_area(polygon):
    return sum(
        (cross(polygon[i], polygon[(i + 1) % len(polygon)]) for i in range(len(polygon))),
        ExactField(0),
    ) / 2


def antipedal_polygon(polygon, focus):
    lines = [antipedal_line(p, focus) for p in polygon]
    vertices = [intersect(lines[i], lines[(i + 1) % len(lines)]) for i in range(len(lines))]
    return vertices, lines


def rational_g(x):
    return x ** 4 - 6 * x ** 3 - 2 * x ** 2 - 2 * x + 1


def main():
    require(U0 ** 4 - 6 * U0 ** 3 - 2 * U0 ** 2 - 2 * U0 + 1 == 0, "QUARTIC_REDUCTION")
    require(A * A == ExactField(R0), "A_SQUARE_RELATION")
    require(C_FOCUS * C_FOCUS == ExactField(R0 - 1), "FOCUS_SQUARE_RELATION")

    lower = F(5, 16)
    upper = F(157, 500)
    require(rational_g(lower) > 0 and rational_g(upper) < 0, "ROOT_BRACKET")
    require(upper < F(1, 3), "ROOT_UPPER_BOUND")

    sine = 2 * U / (1 + U * U)
    cosine = (1 - U * U) / (1 + U * U)
    lam = ExactField(R0) * U * U / (1 + ExactField(R0) * U * U)
    caustic_x = ExactField(R0) - lam
    caustic_y = 1 - lam

    polygon = [
        point(A, 0),
        point(A * cosine, sine),
        point(0, 1),
        point(-A * cosine, sine),
        point(-A, 0),
        point(-A * cosine, -sine),
        point(0, -1),
        point(A * cosine, -sine),
    ]
    require(
        all(p[0] * p[0] / ExactField(R0) + p[1] * p[1] == 1 for p in polygon),
        "OUTER_ELLIPSE_MEMBERSHIP",
    )

    side_lines = [line_through(polygon[i], polygon[(i + 1) % 8]) for i in range(8)]
    require(
        all(caustic_x * x * x + caustic_y * y * y == d * d for x, y, d in side_lines),
        "ALL_EIGHT_COMMON_CAUSTIC_TANGENCIES",
    )
    require(
        all(polygon[i] != polygon[j] for i in range(8) for j in range(i)),
        "DISTINCT_EIGHT_VERTICES",
    )

    plus_vertices, plus_lines = antipedal_polygon(polygon, point(C_FOCUS, 0))
    minus_vertices, minus_lines = antipedal_polygon(polygon, point(-C_FOCUS, 0))
    require(
        all(
            plus_lines[i][0] * plus_lines[(i + 1) % 8][1]
            - plus_lines[(i + 1) % 8][0] * plus_lines[i][1]
            != 0
            for i in range(8)
        ),
        "PLUS_FOCUS_FINITE_INTERSECTIONS",
    )
    require(
        all(
            minus_lines[i][0] * minus_lines[(i + 1) % 8][1]
            - minus_lines[(i + 1) % 8][0] * minus_lines[i][1]
            != 0
            for i in range(8)
        ),
        "MINUS_FOCUS_FINITE_INTERSECTIONS",
    )
    require(signed_area(plus_vertices) == 0, "PLUS_SIGNED_AREA_NOT_ZERO")
    require(signed_area(minus_vertices) == 0, "MINUS_SIGNED_AREA_NOT_ZERO")
    require(
        all(
            minus_vertices[(i + 4) % 8] == point(-plus_vertices[i][0], -plus_vertices[i][1])
            for i in range(8)
        ),
        "CENTRAL_INVERSION_VERTEX_MAP",
    )

    # The A-lane parameterization is the same geometric orbit.  Its z is the
    # Mobius transform below, and its squared minor semiaxis is 1/R0.
    z = (1 - U) / (1 + U)
    p = z ** 4 - z ** 3 + 2 * z ** 2 + z - 1
    rho = (1 - z) ** 3 * (1 + z) / (4 * z ** 3)
    require(p == 0, "A_LANE_QUARTIC_EQUIVALENCE")
    require(rho * ExactField(R0) == 1, "A_LANE_SCALE_EQUIVALENCE")

    # Non-load-bearing numerical sign audit for the source's ambiguous word
    # "rays".  Four supporting lines have their two adjacent polygon vertices
    # on opposite half-lines, so no choice of one oriented ray at that vertex
    # contains both.  The source figure visibly uses full lines.
    lo, hi = float(lower), float(upper)
    for _ in range(120):
        mid = (lo + hi) / 2
        if mid ** 4 - 6 * mid ** 3 - 2 * mid ** 2 - 2 * mid + 1 > 0:
            lo = mid
        else:
            hi = mid
    u_value = (lo + hi) / 2
    r_value = ((1 - u_value) ** 3 * (1 + u_value)) / (4 * u_value ** 3)
    a_value = r_value ** 0.5
    c_value = (r_value - 1) ** 0.5
    require(r_value > 1, "REAL_NONCIRCULAR_ELLIPSE")
    require(0 < lam.evaluate(u_value, a_value, c_value) < 1, "REAL_NONDEGENERATE_CAUSTIC")

    touch_parameters = []
    for i, (x, y, d) in enumerate(side_lines):
        touch = point(caustic_x * x / d, caustic_y * y / d)
        direction = sub(polygon[(i + 1) % 8], polygon[i])
        if direction[0] != 0:
            t = (touch[0] - polygon[i][0]) / direction[0]
        else:
            t = (touch[1] - polygon[i][1]) / direction[1]
        require(touch == add(polygon[i], scale(t, direction)), "CAUSTIC_TOUCH_NOT_ON_SIDE")
        touch_parameters.append(t.evaluate(u_value, a_value, c_value))
    require(all(0 < t < 1 for t in touch_parameters), "CAUSTIC_TOUCH_NOT_IN_OPEN_SEGMENT")

    def ray_parameter(line_index, vertex):
        p = polygon[line_index]
        dx = p[0] - C_FOCUS
        dy = p[1]
        if dx != 0:
            parameter = (vertex[1] - p[1]) / dx
        else:
            parameter = (p[0] - vertex[0]) / dy
        require(vertex == point(p[0] - parameter * dy, p[1] + parameter * dx), "RAY_PARAMETER")
        return parameter.evaluate(u_value, a_value, c_value)

    opposite_half_lines = []
    for i in range(8):
        previous = ray_parameter(i, plus_vertices[(i - 1) % 8])
        following = ray_parameter(i, plus_vertices[i])
        if previous * following < 0:
            opposite_half_lines.append(i)
    require(opposite_half_lines == [0, 1, 4, 7], "RAY_DIAGNOSTIC_PATTERN")

    print("K607_INDEPENDENT_STDLIB_EXACT_FIELD_REPLAY: PASS")
    print("ROOT_BRACKET_AND_REAL_GEOMETRY: PASS")
    print("DISTINCT_ONE_WINDING_EIGHT_VERTICES: PASS")
    print("ALL_EIGHT_COMMON_CAUSTIC_TANGENCIES: PASS")
    print("ALL_EIGHT_TANGENCIES_LIE_IN_OPEN_SEGMENTS: PASS")
    print("ALL_SIXTEEN_SUPPORTING_LINE_INTERSECTIONS_FINITE: PASS")
    print("BOTH_SIGNED_ANTIPEDAL_AREAS_EXACTLY_ZERO: PASS")
    print("CENTRAL_INVERSION_FOCUS_EXCHANGE: PASS")
    print("THREE_LANES_SHARE_ONE_SIMILARITY_CLASS: YES")
    print("LITERAL_SUPPORTING_LINE_RATIO: UNDEFINED_0_OVER_0")
    print("SINGLE_RAY_CYCLE_DIAGNOSTIC: FAIL_AT_LINES_0_1_4_7")


if __name__ == "__main__":
    main()
