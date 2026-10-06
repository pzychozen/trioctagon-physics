"""Opt-in exact Paper-D v0.1.1 reference geometry, equations (1)-(29).

Lengths accept Python int/Fraction and exact SymPy real finite expressions.
Floats (including nested SymPy Float), strings and booleans are rejected.
Positivity must be provable: use positive symbols for s and g_gap. Unknown
regularity and point membership return None, never a certified False/True.
No numerical tolerance, geometry registry, welding, state or dynamics is used.
"""

from dataclasses import dataclass
from fractions import Fraction

import sympy as sp

Point = tuple[sp.Expr, ...]
Segment = tuple[Point, Point]
_HALF = sp.Rational(1, 2)
_R3 = sp.sqrt(3)
RADIAL = ((sp.S.One, sp.S.Zero), (-_HALF, _R3/2), (-_HALF, -_R3/2))
TANGENT = tuple((-y, x) for x, y in RADIAL)
PAPER_C_SHRINK_FACTOR = (1 + sp.sqrt(2))/3


def _real(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction, sp.Expr)):
        raise TypeError(f"{name} requires an exact integer, Fraction or SymPy expression")
    value = sp.sympify(value)
    if value.has(sp.Float):
        raise TypeError(f"{name} must be exact; floats are not rationalized")
    if value.is_real is not True or value.is_finite is not True:
        raise ValueError(f"{name} must be provably real and finite")
    return sp.simplify(value)


def _positive(value, name):
    value = _real(value, name)
    if value.is_positive is not True:
        raise ValueError(f"{name} must be provably positive; undecidable domains are rejected")
    return value


def _point(*values):
    # Rationalizing symbolic denominators can introduce removable poles at
    # admitted inputs (e.g. 1/(1+sqrt(x)) at positive x=1). Keep those
    # denominators intact; numerical radical denominators remain exact.
    return tuple(sp.expand(sp.radsimp(sp.simplify(v), symbolic=False)) for v in values)


def _input_point(values, dimension):
    values = tuple(values)
    if len(values) != dimension:
        raise ValueError(f"point must have {dimension} coordinates")
    return tuple(_real(v, "coordinate") for v in values)


def _index(i):
    if isinstance(i, bool) or not isinstance(i, (int, sp.Integer)):
        raise TypeError("frame index must be an integer 0, 1 or 2")
    if not 0 <= i < 3:
        raise IndexError("frame index must be 0, 1 or 2")
    return int(i)


def _edges(vertices):
    return tuple(zip(vertices, vertices[1:] + vertices[:1]))


def _r60(v):
    x, y = v
    return _point(x/2 - _R3*y/2, _R3*x/2 + y/2)


@dataclass(frozen=True, slots=True)
class ConvexHull:
    """Closed convex hull of exact generators, including its boundary.

    This is a set prescription, not material, a welded face, or a Boolean
    polygon engine. Generated octagon/corner/triangle vertices are cyclic.
    """

    vertices: tuple[Point, ...]

    def __post_init__(self):
        vertices = tuple(tuple(p) for p in self.vertices)
        if len(vertices) < 3 or len(vertices[0]) not in (2, 3):
            raise ValueError("a reference hull needs at least three 2D or 3D generators")
        object.__setattr__(self, "vertices", tuple(
            _input_point(p, len(vertices[0])) for p in vertices))


@dataclass(frozen=True, slots=True)
class HalfPlane:
    """The closed planar set normal dot x <= offset; normals need not be unit."""

    normal: tuple[sp.Expr, sp.Expr]
    offset: sp.Expr

    def __post_init__(self):
        normal = _input_point(self.normal, 2)
        if sp.simplify(sum(x*x for x in normal)).is_positive is not True:
            raise ValueError("half-plane normal must be provably nonzero")
        object.__setattr__(self, "normal", normal)
        object.__setattr__(self, "offset", _real(self.offset, "offset"))

    def slack(self, point):
        """offset - normal dot point: nonnegative means retained, including zero."""
        point = _input_point(point, 2)
        return sp.simplify(self.offset - sum(x*y for x, y in zip(self.normal, point)))


@dataclass(frozen=True, slots=True)
class HalfPlaneIntersection:
    """Explicit closed region; contains returns True, False or undecidable None."""

    halfplanes: tuple[HalfPlane, ...]

    def __post_init__(self):
        planes = tuple(self.halfplanes)
        if not planes or not all(isinstance(h, HalfPlane) for h in planes):
            raise TypeError("a nonempty tuple of HalfPlane objects is required")
        object.__setattr__(self, "halfplanes", planes)

    def contains(self, point) -> bool | None:
        point = _input_point(point, 2)
        signs = tuple(h.slack(point).is_nonnegative for h in self.halfplanes)
        if False in signs:
            return False
        return True if all(v is True for v in signs) else None


@dataclass(frozen=True, slots=True)
class Octagon:
    """Exact local octagon: ordered vertices, closed outline, and filled hull."""

    s: sp.Expr

    def __post_init__(self):
        object.__setattr__(self, "s", _positive(self.s, "s"))

    @property
    def a(self):
        return sp.simplify((1 + sp.sqrt(2))*self.s/2)

    @property
    def w(self):
        return 2*self.a

    @property
    def R_oct(self):
        return self.s/(2*sp.sin(sp.pi/8))

    @property
    def b(self):
        return self.s/2

    @property
    def vertices(self):
        a, b = self.a, self.b
        return ((a, -b), (a, b), (b, a), (-b, a),
                (-a, b), (-a, -b), (-b, -a), (b, -a))

    @property
    def outline(self) -> tuple[Segment, ...]:
        return _edges(self.vertices)

    @property
    def filled(self):
        return ConvexHull(self.vertices)


@dataclass(frozen=True, slots=True)
class ReferenceScaffold:
    """Aligned positive family, canonically parameterized by s and g_gap.

    p is the selected-edge/vertical-centre radius; L=p+a is the planar-centre
    radius. g_gap is a reference length, never the recurrence coefficient g.
    E/G roles are retained even when regular. No individual label is fixed by
    the class-preserving symmetry claim (D3, or C3 with traversal preserved).
    """

    s: sp.Expr
    g_gap: sp.Expr

    def __post_init__(self):
        object.__setattr__(self, "s", _positive(self.s, "s"))
        object.__setattr__(self, "g_gap", _positive(self.g_gap, "g_gap"))

    @classmethod
    def from_radius(cls, s, p):
        """Require provably p > s/(2 sqrt(3)), not merely p > 0."""
        s, p = _positive(s, "s"), _positive(p, "p")
        return cls(s, sp.simplify(_R3*p - s/2))

    @classmethod
    def regular(cls, s):
        return cls(s, s)

    @property
    def octagon(self):
        return Octagon(self.s)

    @property
    def p(self):
        return sp.simplify((self.s + 2*self.g_gap)/(2*_R3))

    @property
    def L(self):
        return sp.simplify(self.p + self.octagon.a)

    @property
    def A(self):
        return tuple(_point(*(self.p*u - self.s*t/2 for u, t in zip(ui, ti)))
                     for ui, ti in zip(RADIAL, TANGENT))

    @property
    def B(self):
        return tuple(_point(*(self.p*u + self.s*t/2 for u, t in zip(ui, ti)))
                     for ui, ti in zip(RADIAL, TANGENT))

    @property
    def vertices(self):
        return tuple(v for pair in zip(self.A, self.B) for v in pair)

    @property
    def selected_edges(self):
        return tuple(zip(self.A, self.B))

    @property
    def connectors(self):
        a, b = self.A, self.B
        return tuple((b[i], a[(i+1) % 3]) for i in range(3))

    @property
    def outline(self):
        return _edges(self.vertices)

    @property
    def side_lengths(self):
        return (self.s, self.g_gap)*3

    @property
    def edge_roles(self):
        return ("E", "G")*3

    @property
    def circumradius_squared(self):
        s, g_gap = self.s, self.g_gap
        return (s*s + s*g_gap + g_gap*g_gap)/3

    @property
    def area(self):
        s, g_gap = self.s, self.g_gap
        return _R3*(s*s + 4*s*g_gap + g_gap*g_gap)/4

    @property
    def q_H(self):
        return (2*self.s + self.g_gap)/(2*_R3)

    @property
    def regularity_residual(self):
        return sp.simplify(self.g_gap - self.s)

    @property
    def is_regular(self) -> bool | None:
        return self.regularity_residual.is_zero

    @property
    def support_halfplanes(self):
        return tuple(HalfPlane(u, self.p) for u in RADIAL)

    @property
    def connector_halfplanes(self):
        return tuple(HalfPlane(_r60(u), self.q_H) for u in RADIAL)

    @property
    def filled_hexagon(self):
        """Equation (16a), not triangle minus ordinary open cell interiors."""
        return HalfPlaneIntersection(self.support_halfplanes + self.connector_halfplanes)

    @property
    def support_vertices(self):
        return tuple(_point(*(self.p*(u + _R3*t) for u, t in zip(ui, ti)))
                     for ui, ti in zip(RADIAL, TANGENT))

    @property
    def support_triangle(self):
        return ConvexHull(self.support_vertices)

    @property
    def W(self):
        return self.s + 2*self.g_gap

    @property
    def corner_cells(self):
        a, b, v = self.A, self.B, self.support_vertices
        return tuple(ConvexHull((b[i], v[i], a[(i+1) % 3])) for i in range(3))

    @property
    def planar_centres(self):
        return tuple(_point(*(self.L*x for x in u)) for u in RADIAL)

    def planar_point(self, i, x, y):
        """Affine map of (17); restrict its local domain to octagon.filled.

        In the CCW outline, indices 4 -> 5 give B_i -> A_i. The selected
        direction A_i -> B_i deliberately reverses that inward outline edge.
        """
        i = _index(i)
        x, y = _real(x, "x"), _real(y, "y")
        return _point(*((self.L + x)*u + y*t for u, t in zip(RADIAL[i], TANGENT[i])))

    @property
    def planar_frames(self):
        return tuple(ConvexHull(tuple(self.planar_point(i, x, y)
                                     for x, y in self.octagon.vertices)) for i in range(3))

    @property
    def vertical_centres(self):
        return tuple(_point(self.p*u[0], self.p*u[1], 0) for u in RADIAL)

    def vertical_point(self, i, xi, z):
        """Equation (19); finite face domain is (xi,z) in octagon.filled."""
        i = _index(i)
        xi, z = _real(xi, "xi"), _real(z, "z")
        return _point(self.p*RADIAL[i][0] + xi*TANGENT[i][0],
                      self.p*RADIAL[i][1] + xi*TANGENT[i][1], z)

    @property
    def vertical_frames(self):
        return tuple(ConvexHull(tuple(self.vertical_point(i, xi, z)
                                     for xi, z in self.octagon.vertices)) for i in range(3))

    @property
    def top_selected_edges(self):
        return tuple((self.vertical_point(i, -self.s/2, self.octagon.a),
                      self.vertical_point(i, self.s/2, self.octagon.a)) for i in range(3))


def paper_c_member(s):
    """Paper-C-family placement p0=a/sqrt(3); only width one matches geometry.py."""
    octagon = Octagon(s)
    return ReferenceScaffold.from_radius(octagon.s, octagon.a/_R3)


def paper_c_rigid_map(point, s):
    """M(x)=Rz(pi/6)x+(0,a/sqrt(3),0); frames 0,1,2 -> P3,P1,P2.

    Finite-face equivalence requires the starting member paper_c_member(s).
    This affine map itself accepts any exact real finite 3D point.
    """
    x, y, z = _input_point(point, 3)
    return _point(_R3*x/2 - y/2, x/2 + _R3*y/2 + Octagon(s).a/_R3, z)


def translate_paper_c_to_regular(s):
    """From p0 to p*=sqrt(3)s/2, preserving s, orientations and top height.

    Each centre translates by (2-sqrt(2))*s/(2*sqrt(3))*u_i.
    This is not a common rigid translation of the whole arrangement.
    """
    return ReferenceScaffold.regular(s)


def shrink_paper_c_at_fixed_centres(s):
    """Shrink ONLY the Paper-C starting member about its vertical face centres.

    Solving sqrt(3)*p0-lambda*s/2=lambda*s gives lambda=(1+sqrt(2))/3.
    Both xi and z scale. Neither the top height nor planar centres stay fixed.
    This factor is not a shrink prescription for arbitrary initial p.
    """
    original = paper_c_member(s)
    return ReferenceScaffold.from_radius(PAPER_C_SHRINK_FACTOR*original.s, original.p)
