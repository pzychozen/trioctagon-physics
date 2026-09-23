"""Opt-in tangent-vector view of the existing canonical complex triad.

D and E are exact inverse isometries between C^3 and the tangent-state space;
D E is only a projector on ambient arrays. Floating conversions are rounded.
FaceState steps its stored Omega, never an automatic E(D(Omega)) round trip.
No field, seam law, physical units, mesh motion or second recurrence is added.
"""
from dataclasses import dataclass, field
import hashlib
import math
import numbers
from pathlib import Path
import sys

import numpy as np
import sympy as sp

from . import dynamics, geometry, operating_region, readouts
from ._response_numeric import (checked_real, complex_vector, product,
                               real_scalar, total)

FRAME_ID = "face_center_tangent_ez_v1"
TRANSPORT_ID = "c3_matched_zero_phase_v1"
FACE_ORDER = ("A=P1", "B=P2", "C=P3")
TANGENCY_RTOL = 8 * sys.float_info.epsilon

# Derive once from the existing immutable exact shell; retain only immutable
# exact tuples, not a writable cached public frame or another shell generator.
_mesh = geometry.folded_module()
_CENTRES = tuple(tuple(sp.simplify(sum(_mesh.vertices[v][j] for v in face)/len(face))
                      for j in range(3)) for face in _mesh.faces)
_NORMALS = tuple(_mesh.face_normal(i) for i in range(3))
_EZ = (sp.Integer(0), sp.Integer(0), sp.Integer(1))
_TANGENTS = tuple(tuple(sp.ImmutableMatrix(_EZ).cross(sp.ImmutableMatrix(n)))
                  for n in _NORMALS)
if len(_CENTRES) != 3 or any(n[2] != 0 for n in _NORMALS):
    raise ValueError("face_center_tangent_ez_v1 requires the existing three vertical faces")
_GEOMETRY_SHA256 = hashlib.sha256(Path(geometry.__file__).read_bytes()).hexdigest()


def _readonly(values, dtype=float):
    result = np.array(values, dtype=dtype, copy=True)
    result.setflags(write=False)
    return result


@dataclass(frozen=True, slots=True)
class FaceFrames:
    """Rows are A=P1, B=P2, C=P3; free vectors are distinct from centre points."""
    tangents: np.ndarray
    ez: np.ndarray
    normals: np.ndarray
    centres: np.ndarray
    face_order: tuple[str, ...] = FACE_ORDER
    frame_id: str = FRAME_ID
    transport_id: str = TRANSPORT_ID
    geometry_sha256: str = _GEOMETRY_SHA256


def face_frames():
    """Fresh read-only frame arrays derived from geometry.folded_module()."""
    return FaceFrames(_readonly(_TANGENTS), _readonly(_EZ),
                      _readonly(_NORMALS), _readonly(_CENTRES))


def _decode(state):
    frames = face_frames()
    return np.array([[total((product(float(z.real), frames.tangents[i, j], "face decode"),
                             product(float(z.imag), frames.ez[j], "face decode")),
                            "face decode") for j in range(3)] for i, z in enumerate(state)])


def decode_to_faces(omega):
    """D: fresh real (3,3) vectors, retaining raw scale, never clipped to polygons.

    Checked nonzero subnormal/overflowing products raise ResponsePrecisionError;
    zeros remain zero. This view has its own conversion limits, not a new domain
    theorem for the existing recurrence. Caller data are never modified.
    """
    return _decode(complex_vector(omega, 3, "omega"))


def encode_from_faces(v):
    """E: accept finite real (3,3) tangent vectors; reject substantive normals.

    Tangency uses |sum(n_k v_k)| <= 8*eps_machine*sum(|n_k v_k|), k=x,y.
    Evaluate this homogeneous test after scaling the participating coordinates
    by their maximum magnitude. No absolute floor, no z-dependent slack, and
    no small-state zeroing. Normal residuals indistinguishable from frame
    roundoff within this bound can be lost in E; larger residuals are rejected.
    Checked products/results also retain the existing conservative precision
    policy. A zero normal coordinate on face B must be exactly zero.
    """
    raw = np.asarray(v, dtype=object)
    if raw.shape != (3, 3):
        raise ValueError("face vectors must have shape (3,3)")
    vector = np.array([[real_scalar(value, "face vector") for value in row] for row in raw])
    frames = face_frames()
    for row, normal in zip(vector, frames.normals):
        active = [k for k in range(2) if normal[k] != 0]
        scale = max(abs(float(row[k])) for k in active)
        if scale != 0:
            terms = [float(normal[k]) * (float(row[k])/scale) for k in active]
            if abs(math.fsum(terms)) > TANGENCY_RTOL * math.fsum(abs(t) for t in terms):
                raise ValueError("face vector has a substantive normal component")
    result = []
    for i, row in enumerate(vector):
        q = total((product(frames.tangents[i, k], row[k], "face encode")
                   for k in range(3)), "face encode")
        p = checked_real(float(row[2]), "face encode")
        result.append(complex(q, p))
    return np.array(result, dtype=np.complex128)


def _index(value):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, numbers.Integral):
        raise TypeError("face index must be an integer: 0=A=P1, 1=B=P2, 2=C=P3")
    if not 0 <= value < 3:
        raise IndexError("face index must be 0, 1 or 2")
    return int(value)


def transport(i, j):
    """Read-only T_ij, source j -> destination i, zero relative phase only.

    Rank two on ambient vectors, not a full rigid rotation. On tangent vectors
    it agrees with the matched C3 rotation's linear part; T_ij = Pi_i R_ij.
    Attached points instead use geometry.rotate_c3 about the centroid axis.
    """
    i, j = _index(i), _index(j)
    frames = face_frames()
    return _readonly(np.outer(frames.tangents[i], frames.tangents[j])
                     + np.outer(frames.ez, frames.ez))


def area_triple(omega):
    """(A_BC,A_CA,A_AB): delegate to the existing raw z_chiral, bit for bit."""
    return readouts.z_chiral(omega)


def state_area(i, j, omega):
    """Signed transported state area, not surface area or an ambient component.

    Evaluate the same complete readout (including for a diagonal request), so
    its input and conservative precision failures are retained.
    """
    i, j = _index(i), _index(j)
    values = area_triple(omega)
    if i == j:
        return 0.0
    pairs = {(1, 2): 0, (2, 0): 1, (0, 1): 2}
    if (i, j) in pairs:
        return float(values[pairs[i, j]])
    return -float(values[pairs[j, i]])


@dataclass(frozen=True, slots=True, eq=False)
class FaceState:
    """Raw canonical Omega with derived, read-only face vectors.

    Ordinary array mutation is disabled, not a security boundary. The metadata
    belongs to this view, never to the SRG initialization receipt. A caller
    wishing to initialize from face data explicitly uses from_faces once.
    """
    omega: np.ndarray
    vectors: np.ndarray = field(init=False)

    def __post_init__(self):
        state = complex_vector(self.omega, 3, "omega")
        vectors = _decode(state)
        state.setflags(write=False)
        vectors.setflags(write=False)
        object.__setattr__(self, "omega", state)
        object.__setattr__(self, "vectors", vectors)

    @classmethod
    def from_faces(cls, vectors):
        """Initialize once via rounded E; subsequent steps retain canonical Omega."""
        return cls(encode_from_faces(vectors))

    def step(self, config, *, profile=None):
        """One existing update, then decode; never re-encode a derived vector.

        profile=None selects plain step3. An explicitly supplied profile goes
        through step_bounded_triad, including its validation/failure policy.
        Decoding can fail conservatively even after the recurrence succeeds;
        the previous immutable view remains intact.
        """
        if not isinstance(config, dynamics.DynamicsConfig):
            raise TypeError("config must be an existing DynamicsConfig")
        if profile is None:
            updated = dynamics.step3(self.omega, config)
        else:
            updated = operating_region.step_bounded_triad(self.omega, config, profile=profile)
        return FaceState(updated)

    def metadata(self):
        """JSON-ready view conventions; caller records initialization/config/count."""
        return {"frame_id": FRAME_ID, "transport_id": TRANSPORT_ID,
                "face_order": list(FACE_ORDER), "canonical_state": "raw_omega",
                "geometry": {"source": "kernel_physics.geometry.folded_module",
                             "source_sha256": _GEOMETRY_SHA256,
                             "width": str(geometry.WIDTH),
                             "fold_angle": str(geometry.FOLD_ANGLE),
                             "centroid_axis_point": [str(x) for x in geometry.CENTROID]},
                "tangency_relative_tolerance": TANGENCY_RTOL,
                "normalization": "none"}
