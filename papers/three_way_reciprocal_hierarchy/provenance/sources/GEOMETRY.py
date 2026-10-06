"""Exact width-one local shell from Paper C §§2–7,9 and Appendix B.

Points are immutable tuples of SymPy expressions; no floating-point welding.
Panel numbers in panel_point are 1,2,3. Mesh face indices are 0,1,2.
"""

from collections import Counter
from dataclasses import dataclass

import sympy as sp

Point = tuple[sp.Expr, sp.Expr, sp.Expr]
Edge = tuple[int, int]
Face = tuple[int, ...]

WIDTH = sp.Integer(1)
EDGE_LENGTH = sp.sqrt(2) - 1
FOLD_ANGLE = sp.pi / 3
HALF = sp.Rational(1, 2)
CENTROID = (sp.Integer(0), sp.sqrt(3) / 6, sp.Integer(0))
LOCAL_OCTAGON = (
    (-HALF, -EDGE_LENGTH / 2), (-EDGE_LENGTH / 2, -HALF),
    (EDGE_LENGTH / 2, -HALF), (HALF, -EDGE_LENGTH / 2),
    (HALF, EDGE_LENGTH / 2), (EDGE_LENGTH / 2, HALF),
    (-EDGE_LENGTH / 2, HALF), (-HALF, EDGE_LENGTH / 2),
)


def _point(x, y, z) -> Point:
    # Expanded, denested radicals make exact vertex keys and normals consistent.
    return tuple(sp.expand(sp.radsimp(sp.sqrtdenest(sp.simplify(v))))
                 for v in (x, y, z))


def panel_point(panel: int, u, z, beta=FOLD_ANGLE) -> Point:
    """Paper C Theorem 2: general-angle maps from the reversed stacked start.

    The expressions extend to real beta; the canonical shell uses pi/3.
    Intermediate configurations are not asserted to avoid intersections.
    """
    u, z, beta = map(sp.sympify, (u, z, beta))
    if panel == 1:
        return _point(-HALF + (HALF - u) * sp.cos(beta),
                      (HALF - u) * sp.sin(beta), z)
    if panel == 2:
        return _point(u, 0, z)
    if panel == 3:
        return _point(HALF - (HALF + u) * sp.cos(beta),
                      (HALF + u) * sp.sin(beta), z)
    raise ValueError("panel must be 1, 2 or 3")


def _face_edges(face: Face):
    return zip(face, face[1:] + face[:1])


@dataclass(frozen=True, slots=True)
class FoldedModule:
    """Immutable exact vertices and outward-oriented face cycles."""

    vertices: tuple[Point, ...]
    faces: tuple[Face, ...]

    def _incidence(self) -> Counter:
        return Counter(tuple(sorted(edge))
                       for face in self.faces for edge in _face_edges(face))

    @property
    def edges(self) -> tuple[Edge, ...]:
        return tuple(sorted(self._incidence()))

    @property
    def seam_edges(self) -> tuple[Edge, ...]:
        return tuple(sorted(e for e, n in self._incidence().items() if n == 2))

    @property
    def boundary_edges(self) -> tuple[Edge, ...]:
        return tuple(sorted(e for e, n in self._incidence().items() if n == 1))

    @property
    def euler_characteristic(self) -> int:
        return len(self.vertices) - len(self.edges) + len(self.faces)

    @property
    def boundary_loops(self) -> tuple[Face, ...]:
        """Trace degree-two boundary graphs; omit the repeated closing vertex.

        Each loop starts at its lowest index and first takes its lower neighbor.
        The canonical result orders the bottom rim before the top rim.
        """
        neighbors: dict[int, list[int]] = {}
        for a, b in self.boundary_edges:
            neighbors.setdefault(a, []).append(b)
            neighbors.setdefault(b, []).append(a)
        if any(len(adj) != 2 for adj in neighbors.values()):
            raise ValueError("boundary is not a union of degree-two cycles")
        unvisited = set(neighbors)
        loops = []
        while unvisited:
            start = min(unvisited)
            loop = [start]
            previous, current = start, min(neighbors[start])
            while current != start:
                if current in loop:
                    raise ValueError("boundary cycle revisits a vertex")
                loop.append(current)
                following = next(v for v in neighbors[current] if v != previous)
                previous, current = current, following
            unvisited.difference_update(loop)
            loops.append(tuple(loop))
        return tuple(loops)

    def face_normal(self, index: int) -> Point:
        """Outward unit normal from the oriented coordinates, not an angle label."""
        if not 0 <= index < len(self.faces):
            raise IndexError("face index out of range")
        a, b, c = (sp.ImmutableMatrix(self.vertices[i])
                   for i in self.faces[index][:3])
        normal = (b - a).cross(c - a)
        length = sp.sqrt(sp.simplify(normal.dot(normal)))
        return _point(*(normal / length))

    def normal_separation(self, first: int, second: int) -> sp.Expr:
        """Outward-normal angle for two distinct adjacent faces, in radians."""
        if first == second:
            raise ValueError("choose two distinct adjacent faces")
        n1 = sp.ImmutableMatrix(self.face_normal(first))
        n2 = sp.ImmutableMatrix(self.face_normal(second))
        return sp.acos(sp.simplify(n1.dot(n2)))

    def interior_dihedral(self, first: int, second: int) -> sp.Expr:
        """Interior wedge angle, the supplement of outward-normal separation."""
        return sp.simplify(sp.pi - self.normal_separation(first, second))


def folded_module() -> FoldedModule:
    """Weld exact panel images in material order, matching Paper C §4 indices."""
    vertices = []
    index = {}
    faces = []
    for panel in (1, 2, 3):
        face = []
        for u, z in LOCAL_OCTAGON:
            point = panel_point(panel, u, z)
            if point not in index:
                index[point] = len(vertices)
                vertices.append(point)
            face.append(index[point])
        faces.append(tuple(face))
    return FoldedModule(tuple(vertices), tuple(faces))


def central_section(height=0) -> tuple[tuple[Point, Point], ...]:
    """Three unit segments of the section curve, not a filled region or cap.

    Height must be provably real and within the closed central band.
    """
    height = sp.sympify(height)
    if height.is_real is not True or (sp.Abs(height) <= EDGE_LENGTH / 2) != sp.true:
        raise ValueError("height must lie in [-s/2, s/2]")
    corners = (_point(-HALF, 0, height), _point(HALF, 0, height),
               _point(0, sp.sqrt(3) / 2, height))
    return tuple((corners[i], corners[(i + 1) % 3]) for i in range(3))


def rotate_c3(point: Point) -> Point:
    """120-degree rotation about the vertical centroid axis (Paper C §9)."""
    x, y, z = map(sp.sympify, point)
    y0 = y - CENTROID[1]
    return _point(-x / 2 - sp.sqrt(3) * y0 / 2,
                  CENTROID[1] + sp.sqrt(3) * x / 2 - y0 / 2, z)


def reflect_vertical(point: Point) -> Point:
    """sigma_v: reflection through x=0."""
    x, y, z = map(sp.sympify, point)
    return _point(-x, y, z)


def reflect_horizontal(point: Point) -> Point:
    """sigma_h: reflection through z=0."""
    x, y, z = map(sp.sympify, point)
    return _point(x, y, -z)
