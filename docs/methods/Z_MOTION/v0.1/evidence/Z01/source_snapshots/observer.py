"""Detached motion correspondence for explicitly selected stored triad states.

This application observation does not import or step the kernel. It recomputes
the stated passive maps in binary64; it is not a Core RunRecord or an interval
certificate. The staged display clock is independent of recorded observers.
"""
from collections.abc import Mapping
from dataclasses import asdict, dataclass, field
import hashlib
import json
import math
from pathlib import Path
import re
from types import MappingProxyType


SOURCE_COMMIT = "7cc1fa03af589818bcdcfaaac51838cc36c84253"
COMPONENT = "natural_core_motion_correspondence/0.1"
MAX_SAMPLES = 4096
MAX_SOURCE_BYTES = 32_000_000
SQRT3 = math.sqrt(3.0)
ORIGIN = (0.0, SQRT3 / 6.0, 0.0)
FACE_CENTERS = ((-.25, SQRT3 / 4.0, 0.0), (0.0, 0.0, 0.0),
                (.25, SQRT3 / 4.0, 0.0))
NORMALS = ((-SQRT3 / 2.0, .5, 0.0), (0.0, -1.0, 0.0),
           (SQRT3 / 2.0, .5, 0.0))
TANGENTS = ((-.5, -SQRT3 / 2.0, 0.0), (1.0, 0.0, 0.0),
            (-.5, SQRT3 / 2.0, 0.0))
VERTICAL = (0.0, 0.0, 1.0)
SOURCES = {
    "decoder": "papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex",
    "placement": "papers/CENTRAL_GEOMETRY_Z_CHIRAL_RESPONSE/publication/v0.3/manuscript.tex",
    "turning": "papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex",
    "axial": "papers/PAPER_G/v0.1.1/source/paper_g.tex",
}


class MotionError(ValueError):
    """A bounded observation request cannot be represented faithfully."""


def _finite(value, name="value"):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise MotionError(name + " must be a finite real number")
    return float(value)


def _check_finite(value):
    if isinstance(value, Mapping):
        for item in value.values():
            _check_finite(item)
    elif isinstance(value, (tuple, list)):
        for item in value:
            _check_finite(item)
    elif isinstance(value, float) and not math.isfinite(value):
        raise MotionError("Nonfinite intermediate result; previous observation retained")


def _freeze(value):
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def plain(value):
    if isinstance(value, Mapping):
        return {key: plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(item) for item in value]
    return value


def _canonical(value):
    return json.dumps(plain(value), sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False)


def _seal(data):
    _check_finite(data)
    data = plain(data)
    data["content_sha256"] = hashlib.sha256(_canonical(data).encode("utf-8")).hexdigest()
    return _canonical(data)


@dataclass(frozen=True)
class MotionConfig:
    mu_place: float = 1.0
    psi: float = 0.0
    alpha: float = 1.0
    beta: float = .5
    lambda_vp: float = .618
    gamma: float = .577
    lock_angle: float = .244
    N: int = 12
    q0: int = 0
    q_step: int = 1
    time0: float = 0.0
    dt: float = .1

    def __post_init__(self):
        for key in ("mu_place", "psi", "alpha", "beta", "lambda_vp", "gamma",
                    "lock_angle", "time0", "dt"):
            object.__setattr__(self, key, _finite(getattr(self, key), key))
        if self.mu_place <= 0:
            raise MotionError("Placement scale must be positive")
        if min(self.gamma, self.time0, self.dt) < 0:
            raise MotionError("This staged display requires nonnegative decay and observer times")
        if type(self.N) is not int or not 1 <= self.N <= 1_000_000:
            raise MotionError("Clock sector count must be an integer from 1 to 1000000")
        if type(self.q0) is not int or type(self.q_step) is not int:
            raise MotionError("Clock start and increment must be integers")


@dataclass(frozen=True)
class MotionObservation:
    canonical_json: str
    data: object = field(init=False, repr=False)
    samples: tuple = field(init=False, repr=False)

    def __post_init__(self):
        data = _freeze(json.loads(self.canonical_json))
        object.__setattr__(self, "data", data)
        object.__setattr__(self, "samples", data["samples"])

    @property
    def parent_digest(self):
        return self.data["parent"]["deterministic_sha256"]


@dataclass(frozen=True)
class MotionProbe(MotionObservation):
    """A common-phase transform of a display copy, never a native trajectory."""


def dot(a, b):
    return math.fsum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def _add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def _sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def _scale(a, factor):
    return tuple(factor * x for x in a)


def decode(z, face):
    """The accepted D_i, without a display scale or a moving base point."""
    return (z.real * TANGENTS[face][0], z.real * TANGENTS[face][1], z.imag)


def transport(vector, source_face, target_face):
    return decode(complex(dot(TANGENTS[source_face], vector), vector[2]), target_face)


def signed_turn(first, second):
    """Signed increment area and angle; a zero increment has no turn angle."""
    area = (first.conjugate() * second).imag
    angle = None if first == 0 or second == 0 else math.atan2(
        area, (first.conjugate() * second).real)
    _check_finite((area, angle))
    return area, angle


def _linear_place(vector, config):
    c, s = math.cos(config.psi), math.sin(config.psi)
    return (config.mu_place * (c * vector[0] - s * vector[1]),
            config.mu_place * (s * vector[0] + c * vector[1]),
            config.mu_place * vector[2])


def _clock(index, config):
    sector = (config.q0 + index * config.q_step) % config.N
    time = config.time0 + index * config.dt
    theta = 2.0 * math.pi * sector / config.N
    _check_finite((time, theta))
    return {"sector": sector, "theta": theta, "time": time}


def _envelope_and_direction(clock, config):
    theta = clock["theta"]
    amplitude = math.cos(3.0 * (theta - config.lock_angle))
    H = (amplitude * math.cos(theta), amplitude * math.sin(theta), amplitude)
    return math.exp(-config.gamma * clock["time"]), H


def _placed(kappa, C, clock, config):
    K = config.lambda_vp * (kappa / (1.0 + kappa))
    E, H = _envelope_and_direction(clock, config)
    macro = _scale(H, K * E)
    Z = _add(_scale(macro, config.alpha), _scale(C, config.beta))
    return {"macro": macro, "Z": Z, "point": _add(ORIGIN, _linear_place(Z, config))}


def reference_geometry():
    """The fixed, declared PLUS tau=0 surface, in width-one Paper-C coordinates.

    No mechanical interpolation in tau or pose is defined here. Coordinates
    are numerical evaluations of the cited construction, not a new mesh fit.
    """
    from trioctagon_ui.shell_reference import load_reference, RESOURCE_SHA
    host = load_reference().data["geometry"]
    host_vertices = [_add(ORIGIN, vertex["centered"]) for vertex in host["vertices"]]
    host_edges = [(host_vertices[edge["vertices"][0]], host_vertices[edge["vertices"][1]])
                  for edge in host["edges"]]
    a = (1.0 - math.sqrt(2.0) / 2.0) / 2.0
    h, r = (math.sqrt(2.0) - 1.0) / 2.0, SQRT3 / 6.0
    directions = [(math.cos(-math.pi / 2.0 + i * math.pi / 3.0),
                   math.sin(-math.pi / 2.0 + i * math.pi / 3.0)) for i in range(6)]
    top = [_add(ORIGIN, (a * x, a * y, h)) for x, y in directions]
    bottom = [_add(ORIGIN, (a * x, a * y, -h)) for x, y in directions]
    upper = [_add(ORIGIN, (r * directions[2*k][0], r * directions[2*k][1], .5)) for k in range(3)]
    lower = [_add(ORIGIN, (r * directions[2*k][0], r * directions[2*k][1], -.5)) for k in range(3)]
    triangles = []
    for i in range(6):
        triangles += [(top[i], top[(i+1) % 6], bottom[(i+2) % 6]),
                      (top[i], bottom[(i+2) % 6], bottom[(i+1) % 6])]
    for tips, ring in ((upper, top), (lower, bottom)):
        for k in range(3):
            triangles += [(tips[k], ring[(2*k-1) % 6], ring[2*k]),
                          (tips[k], ring[2*k], ring[(2*k+1) % 6])]
    return {"origin": ORIGIN, "face_centers": FACE_CENTERS, "normals": NORMALS,
            "tangents": TANGENTS, "central_triangles": triangles,
            "host_edges": host_edges, "host_reference_sha256": RESOURCE_SHA,
            "surface": "declared refined PLUS tau=0; fixed reference",
            "width": 1.0, "source": SOURCES["placement"], "source_commit": SOURCE_COMMIT}


def _snapshot(omega, ordinal, index, clock, frozen_clock, config):
    real, imag = tuple(z.real for z in omega), tuple(z.imag for z in omega)
    C = cross(real, imag)
    W = tuple(math.fsum(TANGENTS[i][j] * C[i] for i in range(3)) for j in range(3))
    mean = complex(math.fsum(z.real / 3.0 for z in omega),
                   math.fsum(z.imag / 3.0 for z in omega))
    kappa = math.hypot(*(part for z in omega for part in (z.real, z.imag)))
    return {"sample_ordinal": ordinal, "update_index": index,
            "omega": [(z.real, z.imag) for z in omega],
            "omega_binary64_hex": [(z.real.hex(), z.imag.hex()) for z in omega],
            "mean": (mean.real, mean.imag), "kappa": kappa,
            "face_vectors": [decode(z, i) for i, z in enumerate(omega)],
            "collective_vectors": [decode(mean, i) for i in range(3)],
            "C": C, "W": W, "Gamma": math.fsum(C),
            "W_direction": None if W[0] == 0 and W[1] == 0 else math.atan2(W[1], W[0]),
            "clock": clock, "scheduled": _placed(kappa, C, clock, config),
            "frozen": _placed(kappa, C, frozen_clock, config),
            "mean_increment": None, "signed_turn": None, "turn_angle": None,
            "attribution": None}


def _attribute(old, new, config):
    Ko = config.lambda_vp * (old["kappa"] / (1.0 + old["kappa"]))
    Kn = config.lambda_vp * (new["kappa"] / (1.0 + new["kappa"]))
    Eo, Ho = _envelope_and_direction(old["clock"], config)
    En, Hn = _envelope_and_direction(new["clock"], config)
    native = _linear_place(_add(_scale(Ho, config.alpha * Eo * (Kn - Ko)),
                                _scale(_sub(new["C"], old["C"]), config.beta)), config)
    envelope = _linear_place(_scale(Ho, config.alpha * Kn * (En - Eo)), config)
    clock = _linear_place(_scale(_sub(Hn, Ho), config.alpha * Kn * En), config)
    total = _sub(new["scheduled"]["point"], old["scheduled"]["point"])
    residual = _sub(total, _add(native, _add(envelope, clock)))
    return {"from_index": old["update_index"], "to_index": new["update_index"],
            "update_span": new["update_index"] - old["update_index"],
            "native": native, "envelope": envelope, "clock": clock,
            "total": total, "residual": residual}


def _finish_rows(rows, config):
    for i, row in enumerate(rows):
        if i:
            delta = complex(*row["mean"]) - complex(*rows[i-1]["mean"])
            row["mean_increment"] = (delta.real, delta.imag)
            row["attribution"] = _attribute(rows[i-1], row, config)
        if i >= 2:
            row["signed_turn"], row["turn_angle"] = signed_turn(
                complex(*rows[i-1]["mean_increment"]), complex(*row["mean_increment"]))
    _check_finite(rows)
    return rows


def _strict_json(text):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise MotionError("Duplicate source JSON key: " + key)
            result[key] = value
        return result
    def invalid(value):
        raise MotionError("Nonfinite source JSON: " + value)
    return json.loads(text, object_pairs_hook=pairs, parse_constant=invalid)


def evaluate(record_json, config=None):
    """Analyze an application-selected, worker-validated triad RunRecord.

    Admission here protects this observation's numerical domain. It is not a
    replacement for the existing public record loader's validation or a replay.
    The schedule uses actual update indices, even for sparse stored histories.
    """
    config = MotionConfig() if config is None else config
    if not isinstance(config, MotionConfig):
        raise MotionError("An explicit MotionConfig is required")
    if not isinstance(record_json, str) or len(record_json.encode("utf-8")) > MAX_SOURCE_BYTES:
        raise MotionError("Select a stored record no larger than 32 MB")
    try:
        record = _strict_json(record_json)
        if record["record_type"] != "KERNEL_RUN_RECORD" or record["topology"] != "triad" or record["state_size"] not in ("3", 3):
            raise MotionError("Natural Core Motion requires a selected three-channel triad RunRecord")
        digest = record["deterministic_sha256"]
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise MotionError("The selected record has no valid parent digest")
        samples = record["samples"]
        if not isinstance(samples, list) or not 1 <= len(samples) <= MAX_SAMPLES:
            raise MotionError("Select a history with 1 to 4096 stored samples; no samples are silently dropped")
        states, indices = [], []
        for sample in samples:
            spelling = sample["update_index"]
            if not isinstance(spelling, str) or not re.fullmatch(r"0|[1-9][0-9]{0,18}", spelling):
                raise MotionError("Stored update indices must be nonnegative canonical integer strings")
            index = int(spelling)
            if indices and index <= indices[-1]:
                raise MotionError("Stored update indices must increase strictly")
            encoded = sample["omega"]
            if not isinstance(encoded, list) or len(encoded) != 3:
                raise MotionError("Every stored state must have three complex entries")
            state = []
            for z in encoded:
                parts = []
                for key in ("re", "im"):
                    if not isinstance(z[key], dict) or set(z[key]) != {"f64"}:
                        raise MotionError("Stored state entries require the existing f64 token format")
                    parts.append(_finite(float.fromhex(z[key]["f64"]), "stored state"))
                state.append(complex(*parts))
            states.append(tuple(state)); indices.append(index)
        frozen_clock = _clock(indices[0], config)
        rows = _finish_rows([_snapshot(state, i, index, _clock(index, config), frozen_clock, config)
                             for i, (state, index) in enumerate(zip(states, indices))], config)
        largest = max((abs(z) for state in states for z in state), default=0.0)
        data = {"schema": "TRIOCTAGON_NATURAL_MOTION_OBSERVATION_V1", "component": COMPONENT,
                "evidence_class": "detached application observation; binary64 evaluation",
                "source_commit": SOURCE_COMMIT, "sources": SOURCES,
                "component_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "parent": {"deterministic_sha256": digest,
                           "canonical_json_sha256": hashlib.sha256(record_json.encode("utf-8")).hexdigest(),
                           "implementation": record.get("implementation", {}),
                           "admission": "selected validated Core record; no scientific replay here"},
                "config": asdict(config), "geometry": reference_geometry(),
                "display_scale": .22 / largest if largest else .22,
                "frozen_clock": frozen_clock, "samples": rows,
                "conventions": {
                    "clock": "independent recomputed staged display observer, anchored at update index zero",
                    "initialization": "recomputed, including first stored sample; recorded observers are untouched",
                    "frozen": "angle and envelope time of first stored sample",
                    "attribution_order": ["native state", "envelope", "clock"],
                    "intervals": "endpoint differences between stored samples; update_span is explicit",
                    "connections": "visual sample connections; no interpolating trajectory or opening passage",
                    "numbers": "finite IEEE-754 binary64, round-trip JSON; no interval certification",
                    "geometry": "fixed reference; no native surface pose or shape update",
                    "feedback": "none"}}
        _check_finite(data)
        return MotionObservation(_seal(data))
    except MotionError:
        raise
    except (KeyError, TypeError, ValueError, ArithmeticError, RecursionError) as exc:
        raise MotionError("Cannot form the bounded motion observation: " + str(exc)) from exc


def phase_probe(observation, chi):
    """Transform a display copy of every cached state at fixed observer settings."""
    if type(observation) is not MotionObservation:
        raise MotionError("Apply the phase probe to the original completed observation")
    chi = _finite(chi, "probe angle")
    try:
        config = MotionConfig(**dict(observation.data["config"]))
        factor = complex(math.cos(chi), math.sin(chi))
        rows = []
        maxima = {key: 0.0 for key in ("kappa", "C", "W", "Gamma", "frozen_point", "scheduled_point")}
        max_gram_change = 0.0
        for old in observation.samples:
            state = tuple(complex(*z) * factor for z in old["omega"])
            row = _snapshot(state, old["sample_ordinal"], old["update_index"],
                            plain(old["clock"]), plain(observation.data["frozen_clock"]), config)
            residuals = {"kappa": abs(row["kappa"] - old["kappa"]),
                         "Gamma": abs(row["Gamma"] - old["Gamma"])}
            for key in ("C", "W"):
                residuals[key] = max(abs(x-y) for x,y in zip(row[key],old[key]))
            for key in ("frozen", "scheduled"):
                residuals[key+"_point"] = max(abs(x-y) for x,y in zip(row[key]["point"],old[key]["point"]))
            gram_change = max(abs(dot(row["face_vectors"][i],row["face_vectors"][j]) -
                                  dot(old["face_vectors"][i],old["face_vectors"][j]))
                              for i in range(3) for j in range(i+1,3))
            row["probe_residuals"] = residuals
            row["ambient_gram_change"] = gram_change
            max_gram_change = max(max_gram_change, gram_change)
            for key in maxima:
                maxima[key] = max(maxima[key], residuals[key])
            rows.append(row)
        data = {"schema": "TRIOCTAGON_NATURAL_MOTION_PHASE_PROBE_V1", "component": COMPONENT,
                "source_commit": SOURCE_COMMIT, "component_source_sha256": observation.data["component_source_sha256"],
                "parent": plain(observation.data["parent"]), "observation_sha256": observation.data["content_sha256"],
                "config": asdict(config), "geometry": plain(observation.data["geometry"]),
                "display_scale": observation.data["display_scale"], "frozen_clock": plain(observation.data["frozen_clock"]),
                "probe_angle": chi, "not_native_trajectory": True,
                "description": "common phase applied to display copies; no native map was executed",
                "samples": _finish_rows(rows, config), "invariance_residuals": maxima,
                "ambient_gram_change_max": max_gram_change}
        return MotionProbe(_seal(data))
    except MotionError:
        raise
    except (TypeError, ValueError, ArithmeticError) as exc:
        raise MotionError("Phase probe produced a nonfinite result: " + str(exc)) from exc


def export_json(path, observation, probe=None):
    """Publish a detached observation through the existing Windows export lane.

    Existing destinations are never overwritten. This deliberately keeps the
    application's supported filesystem semantics instead of adding a fallback.
    """
    from trioctagon_ui._export_publication import publication
    if type(observation) is not MotionObservation:
        raise MotionError("Export requires a completed original observation")
    if probe is not None and (type(probe) is not MotionProbe or
                             probe.data["observation_sha256"] != observation.data["content_sha256"]):
        raise MotionError("Probe and observation identities do not match")
    payload = {"schema": "TRIOCTAGON_NATURAL_MOTION_EXPORT_V1",
               "observation": plain(observation.data),
               "phase_probe": None if probe is None else plain(probe.data)}
    raw = (_seal(payload) + "\n").encode("utf-8")
    with publication(path) as files:
        files[0].stream.write(raw)
        files[0].publish()
    return {"path": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
            "parent_digest": observation.parent_digest}
