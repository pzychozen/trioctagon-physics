"""Versioned, inert records and strict canonical binary64 serialization."""
from collections.abc import Mapping
from dataclasses import fields, is_dataclass
import hashlib
import json
import math
from pathlib import Path
import platform
import re
import subprocess
import sys
from types import MappingProxyType

import mpmath
import numpy as np
import sympy

from . import __version__, z_diagnostics as _diagnostics
from ._contract_types import (Parameters, Provenance, Clock, EMAState, StagedConfig,
                              EMAConfig, _provenance_data)

_VERSION = "1.0.0"
_READOUTS = ("z_chiral",)
_DIAGNOSTICS = ("chiral_area_accounting", "intensity_budget", "potential",
                "readout_accounting", "historical_alignment")
_OBSERVER_DIAGNOSTICS = ("readout_accounting", "historical_alignment")
_MODES = ("recomputed", "historical_constructor_zero")
_ROOT = Path(__file__).resolve().parent.parent
_MODULES = tuple(sorted("kernel_physics/" + name + ".py" for name in (
    "__init__", "api", "_contract_types", "_runner", "_records", "_geometry_records",
    "_presets", "dynamics", "readouts", "z_manifold", "z_diagnostics",
    "_response_numeric", "geometry", "reference_scaffold")))
_PAPERS = {
    "A": ("publication", "papers/PAPER_A/publication/paper_A_publication.md"),
    "B": ("0.1.2", "papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md"),
    "C": ("1.0.1", "papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md"),
    "D": ("0.1.1", "papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md"),
    "E": ("0.1.1", "papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md"),
    "F": ("0.2", "papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md"),
}
_LEDGER = {f"{prefix}{i:02}" for prefix, count in
           (("A", 9), ("N", 1), ("B", 6), ("C", 7), ("D", 8), ("E", 14),
            ("F", 7), ("X", 5), ("L", 6), ("R", 4), ("S", 5), ("O", 3))
           for i in range(1, count + 1)}


def _keys(value, required, optional=()):
    if not isinstance(value, dict):
        raise TypeError("expected a JSON object")
    required, optional = set(required), set(optional)
    if not required <= value.keys() or value.keys() - required - optional:
        raise ValueError(f"invalid fields: expected {sorted(required)}, optional {sorted(optional)}")


def _string(value):
    if not isinstance(value, str):
        raise TypeError("expected a string")
    if not value:
        raise ValueError("expected a nonempty string")
    return value


def _choice(value, choices):
    _string(value)
    if value not in choices:
        raise ValueError(f"unknown value {value!r}")
    return value


def _int(value, minimum=None):
    if not isinstance(value, str):
        raise TypeError("integer codec requires a decimal string")
    if re.fullmatch(r"0|-?[1-9][0-9]*", value) is None:
        raise ValueError("noncanonical integer")
    result = int(value)
    if minimum is not None and result < minimum:
        raise ValueError("integer out of range")
    return result


def _f64(value):
    _keys(value, ("f64",))
    _string(value["f64"])
    try:
        result = float.fromhex(value["f64"])
    except (ValueError, OverflowError) as exc:
        raise ValueError("invalid binary64 value") from exc
    if not math.isfinite(result) or result.hex() != value["f64"]:
        raise ValueError("nonfinite or noncanonical binary64 value")
    return result


def _complex(value):
    _keys(value, ("re", "im"))
    return complex(_f64(value["re"]), _f64(value["im"]))


def _array(value, size, decoder):
    if not isinstance(value, list):
        raise TypeError("array codec requires a list")
    if size is not None and len(value) != size:
        raise ValueError("invalid array shape")
    return [decoder(item) for item in value]


def _bool(value):
    if type(value) is not bool:
        raise TypeError("expected a JSON boolean")
    return value


def _sha(value):
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError("invalid SHA-256")
    return value


def _encode(value):
    """Encode numeric results without evaluating or normalizing them."""
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if isinstance(value, (int, np.integer)):
        return str(value)
    if isinstance(value, (float, np.floating)):
        result = float(value)
        if not math.isfinite(result):
            raise FloatingPointError("cannot record a nonfinite value")
        return {"f64": result.hex()}
    if isinstance(value, (complex, np.complexfloating)):
        return {"re": _encode(float(value.real)), "im": _encode(float(value.imag))}
    if is_dataclass(value):
        return {field.name: _encode(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return {key: _encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, np.ndarray)):
        return [_encode(item) for item in value]
    raise TypeError(f"unsupported record value: {type(value).__name__}")


def _canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def _digest(data):
    content = {key: value for key, value in data.items()
               if key not in ("deterministic_sha256", "execution_metadata")}
    return hashlib.sha256(_canonical(content).encode("utf-8")).hexdigest()


def _signed(data):
    data["deterministic_sha256"] = _digest(data)
    return data


def _parse(text):
    if not isinstance(text, str):
        raise TypeError("JSON input must be text")

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    def invalid(value):
        raise ValueError(f"nonfinite JSON constant: {value}")

    return json.loads(text, object_pairs_hook=pairs, parse_constant=invalid)


def _freeze(value):
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


class _Record:
    """Own canonical text; every view is detached and recursively immutable."""
    __slots__ = ("_json",)

    def __init__(self, data):
        detached = _parse(_canonical(data))
        self._validate(detached)
        object.__setattr__(self, "_json", _canonical(detached))

    def __setattr__(self, name, value):
        raise AttributeError("records are immutable")

    def __delattr__(self, name):
        raise AttributeError("records are immutable")

    @property
    def data(self):
        return _freeze(_parse(self._json))

    @property
    def deterministic_sha256(self):
        return _parse(self._json)["deterministic_sha256"]

    def to_json(self):
        return self._json

    @classmethod
    def from_json(cls, text):
        return cls(_parse(text))


def _provenance(data):
    _keys(data, ("kind", "source_id", "source_revision", "locator", "literal_values", "notes"))
    return Provenance(**data)


def _parameters(data):
    _keys(data, ("eps", "g", "phase_strength", "k"))
    return Parameters(eps=_f64(data["eps"]), g=_f64(data["g"]),
                      phase_strength=_f64(data["phase_strength"]), k=_array(data["k"], 3, _f64))


def _config(data, variant):
    cls = StagedConfig if variant == "staged" else EMAConfig
    _keys(data, (field.name for field in fields(cls)))
    return cls(**{key: _f64(value) for key, value in data.items()})


def _selection(values, allowed):
    result = _array(values, None, lambda value: _choice(value, allowed))
    if len(set(result)) != len(result):
        raise ValueError("duplicate selection")
    return result


def _provenance_git(*args):
    try:
        return subprocess.check_output(["git", "-C", str(_ROOT), *args],
                                       text=True, stderr=subprocess.PIPE).strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("record production requires an identifiable Git source checkout") from exc


def _source_checkout():
    """An unrelated enclosing repository never owns this package's provenance."""
    try:
        top = _provenance_git("rev-parse", "--show-toplevel")
    except ValueError:
        if (_ROOT / ".git").exists():
            raise  # Broken exact source checkout must not fall back.
        return False
    return Path(top).resolve() == _ROOT.resolve()


def _distribution_manifest():
    """Validate on every capture; cached assertions cannot detect later tampering.

    build_input_sha256 is canonical UTF-8 JSON (sorted keys, compact separators,
    no NaN/Infinity) excluding that field. It is consistency, not authorship.
    This software-only codec is separate from the unchanged record codecs.
    """
    data = _parse((_ROOT / "kernel_physics/_distribution_provenance.json").read_text(encoding="utf-8"))
    _keys(data, ("manifest_type", "manifest_version", "source", "software", "modules",
                 "papers", "build", "build_input_sha256"))
    if data["manifest_type"] != "TRIOCTAGON_DISTRIBUTION_PROVENANCE" or data["manifest_version"] != "1":
        raise ValueError("unsupported distribution provenance manifest")
    source = data["source"]
    _keys(source, ("repository", "commit", "tracked_dirty"))
    _string(source["repository"])
    if not isinstance(source["commit"], str) or re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", source["commit"]) is None:
        raise ValueError("manifest requires a full source commit ID")
    if source["tracked_dirty"] is not False:
        raise ValueError("distribution source must be attested clean")
    expected = {"package_version": __version__, "api_version": _VERSION,
                "run_record_schema_version": _VERSION, "geometry_record_schema_version": _VERSION,
                "ledger_version": "0.1"}
    _keys(data["software"], expected)
    if data["software"] != expected:
        raise ValueError("manifest software identity mismatch")
    modules = _array(data["modules"], len(_MODULES), lambda v: v)
    for entry, path in zip(modules, _MODULES):
        _keys(entry, ("path", "sha256"))
        _sha(entry["sha256"])
        if entry["path"] != path:
            raise ValueError("manifest module set/order mismatch")
        if hashlib.sha256((_ROOT / path).read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"installed module bytes differ from source: {path}")
    papers = _array(data["papers"], len(_PAPERS), lambda v: v)
    for entry, key in zip(papers, sorted(_PAPERS)):
        _keys(entry, ("source_id", "edition", "path", "sha256"))
        if (entry["source_id"], entry["edition"], entry["path"]) != ("P" + key, *_PAPERS[key]):
            raise ValueError("manifest paper identity/set/order mismatch")
        _sha(entry["sha256"])
    build = data["build"]
    _keys(build, ("backend", "setuptools", "wheel", "files"))
    if (build["backend"], build["setuptools"], build["wheel"]) != ("_build_backend", "81.0.0", "0.47.0"):
        raise ValueError("unsupported manifest build identity")
    # These software build-input hashes remain metadata in an installation.
    # Only the 14 frozen implementation paths are record identity members.
    inputs = tuple(sorted((*_MODULES, *("kernel_physics/" + n + ".py" for n in
        ("covering", "face_state", "boundary_response", "srg", "operating_region")),
        "pyproject.toml", "_build_backend.py", "LICENSE", "LICENSE_SCOPE.md", "kernel_physics/README.md")))
    entries = _array(build["files"], len(inputs), lambda v: v)
    for entry, path in zip(entries, inputs):
        _keys(entry, ("path", "sha256"))
        _sha(entry["sha256"])
        if entry["path"] != path:
            raise ValueError("manifest build-input set/order mismatch")
    hashes = {entry["path"]: entry["sha256"] for entry in entries}
    if any(hashes[e["path"]] != e["sha256"] for e in modules):
        raise ValueError("conflicting manifest module hashes")
    _sha(data["build_input_sha256"])
    payload = {k: v for k, v in data.items() if k != "build_input_sha256"}
    if hashlib.sha256(_canonical(payload).encode("utf-8")).hexdigest() != data["build_input_sha256"]:
        raise ValueError("distribution manifest digest mismatch")
    return data


def _live_source():
    """Exact source mode never substitutes a stale packaged manifest."""
    commit = _provenance_git("rev-parse", "HEAD")
    if re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit) is None:
        raise ValueError("source requires a full commit ID")
    repository = _string(_provenance_git("remote", "get-url", "origin"))
    tracked = set(_provenance_git("ls-files").splitlines())
    required = {*_MODULES, *(v[1] for v in _PAPERS.values())}
    if not required <= tracked or _provenance_git("status", "--porcelain", "--untracked-files=no"):
        raise ValueError("live source provenance requires clean, complete tracked evidence")
    if any(not (_ROOT / path).is_file() for path in required):
        raise ValueError("live source provenance evidence is missing")
    return repository, commit


def _implementation():
    if not _source_checkout():
        data = _distribution_manifest()
        return {**data["source"], "package_version": data["software"]["package_version"],
                "api_version": data["software"]["api_version"], "modules": data["modules"]}
    repository, commit = _live_source()
    return {"repository": repository, "commit": commit,
            "package_version": __version__, "api_version": _VERSION,
            "modules": [{"path": path, "sha256": hashlib.sha256((_ROOT / path).read_bytes()).hexdigest()}
                        for path in _MODULES],
            "tracked_dirty": False}


def _papers(ids):
    ids = sorted(set(ids))
    if any(key not in _PAPERS for key in ids):
        raise ValueError("unknown paper identity")
    if not _source_checkout():
        papers = {entry["source_id"]: entry for entry in _distribution_manifest()["papers"]}
        return [papers["P" + key] for key in ids]
    _live_source()
    return [{"source_id": "P" + key, "edition": _PAPERS[key][0], "path": _PAPERS[key][1],
             "sha256": hashlib.sha256((_ROOT / _PAPERS[key][1]).read_bytes()).hexdigest()}
            for key in ids]


def _producer_environment():
    return {"python": platform.python_version(), "numpy": np.__version__,
            "sympy": sympy.__version__, "mpmath": mpmath.__version__,
            "platform": platform.platform(), "architecture": platform.machine(),
            "byteorder": sys.byteorder}


def _environment(first, last):
    return {"first_update_index": str(first), "last_update_index": str(last), **_producer_environment()}


def _validate_environment(value, *, segment):
    required = ("python", "numpy", "sympy", "mpmath", "platform", "architecture", "byteorder")
    counters = ("first_update_index", "last_update_index") if segment else ()
    _keys(value, (*required, *counters), ("timestamp",))
    if segment and _int(value["last_update_index"], 0) < _int(value["first_update_index"], 0):
        raise ValueError("reversed execution segment")
    for key in set(value) - set(counters):
        _string(value[key])
    _choice(value["byteorder"], ("little", "big"))


def _metadata(data):
    for key, value in (("schema_version", _VERSION), ("api_version", _VERSION), ("ledger_version", "0.1")):
        if data[key] != value:
            raise ValueError(f"unsupported {key}")
    impl = data["implementation"]
    _keys(impl, ("repository", "commit", "package_version", "api_version", "modules", "tracked_dirty"))
    for key in ("repository", "package_version"):
        _string(impl[key])
    if not isinstance(impl["commit"], str) or re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", impl["commit"]) is None:
        raise ValueError("implementation requires a full commit ID")
    if impl["api_version"] != _VERSION:
        raise ValueError("unsupported implementation API")
    _bool(impl["tracked_dirty"])
    modules = _array(impl["modules"], len(_MODULES), lambda v: v)
    for module, path in zip(modules, _MODULES):
        _keys(module, ("path", "sha256"))
        if module["path"] != path:
            raise ValueError("unsupported or unsorted implementation modules")
        _sha(module["sha256"])
    papers = _array(data["paper_references"], None, lambda v: v)
    source_ids = []
    for paper in papers:
        _keys(paper, ("source_id", "edition", "path", "sha256"))
        key = _choice(paper["source_id"], tuple("P" + k for k in _PAPERS))[1:]
        if (paper["edition"], paper["path"]) != _PAPERS[key]:
            raise ValueError("unknown paper edition/path")
        _sha(paper["sha256"])
        source_ids.append(paper["source_id"])
    if source_ids != sorted(set(source_ids)):
        raise ValueError("paper references must be sorted and unique")
    if data["record_type"] == "KERNEL_RUN_RECORD":
        segments = _array(data["execution_metadata"], None, lambda v: v)
        if not segments:
            raise ValueError("execution metadata must contain a segment")
        for segment in segments:
            _validate_environment(segment, segment=True)
    else:
        _validate_environment(data["execution_metadata"], segment=False)
    _sha(data["deterministic_sha256"])
    if _digest(data) != data["deterministic_sha256"]:
        raise ValueError("deterministic digest mismatch")


def _definition_ids(data):
    ids = {"A01", "A02", "A03", "A04", "A05" if data["topology"] == "triad" else "A06",
           "N01", "S01", "S02", "S03", "S05"}
    if data["selection"]["readouts"] or data["observers"] or "chiral_area_accounting" in data["selection"]["diagnostics"]:
        ids.add("B01")
    if data["initialization"]["kind"] == "historical_seed":
        ids.add("L02")
    for observer in data["observers"]:
        ids.update(("E01", "E02", "E03"))
        if observer["variant"] == "ema":
            ids.update(("E04", "L04"))
        if observer["initialization"] == "historical_constructor_zero":
            ids.add("E05")
        if observer["provenance"]["kind"] == "historical_preset":
            ids.update(("L03", "L04"))
    diagnostics = {"readout_accounting": "E06", "chiral_area_accounting": "E07",
                   "intensity_budget": "E09", "potential": "E10", "historical_alignment": "E08"}
    ids.update(diagnostics[key] for key in data["selection"]["diagnostics"])
    if "historical_alignment" in data["selection"]["diagnostics"]:
        ids.add("L06")
    return sorted(ids)


def _result(data, variant, mode):
    _keys(data, ("z", "Z_macro", "Z_chiral", "Z_total", "variant", "initialization"))
    _f64(data["z"])
    for key in ("Z_macro", "Z_chiral", "Z_total"):
        _array(data[key], 3, _f64)
    if data["variant"] != variant or data["initialization"] != mode:
        raise ValueError("inconsistent observer result markers")


def _diagnostic(name, data):
    if name == "potential":
        _f64(data)
        return
    cls = {"readout_accounting": _diagnostics.ReadoutAccounting,
           "chiral_area_accounting": _diagnostics.ChiralAreaAccounting,
           "intensity_budget": _diagnostics.IntensityBudget,
           "historical_alignment": _diagnostics.HistoricalAlignment}[name]
    _keys(data, (f.name for f in fields(cls)))
    for key, value in data.items():
        if key in ("variant", "initialization"):
            _choice(value, ("staged", "ema") if key == "variant" else _MODES)
        elif key.endswith("_resolved"):
            _bool(value)
        elif key in ("increment", "diagnostic_pre_sync_prediction"):
            _array(value, 3, _complex)
        elif key in ("blend_residual", "chiral", "component_intensities"):
            _array(value, 3, _f64)
        else:
            _f64(value)


class RunRecord(_Record):
    """KERNEL_RUN_RECORD 1.0.0; loading validates structure, never equations."""
    __slots__ = ()

    @staticmethod
    def _validate(data):
        _keys(data, ("record_type", "schema_version", "api_version", "ledger_version", "topology",
                    "state_size", "parameters", "parameter_provenance", "initialization", "selection",
                    "observers", "samples", "definition_ids", "paper_references", "implementation",
                    "execution_metadata", "deterministic_sha256", "continuation"))
        if data["record_type"] != "KERNEL_RUN_RECORD":
            raise ValueError("wrong record type")
        _metadata(data)
        topology = _choice(data["topology"], ("triad", "ring"))
        size = _int(data["state_size"], 3)
        if size % 3 or (topology == "triad" and size != 3):
            raise ValueError("invalid topology size")
        _parameters(data["parameters"])
        _provenance(data["parameter_provenance"])
        init = data["initialization"]
        _keys(init, ("kind", "provenance", "update_index", "omega"), ("preset_id", "parent_digest"))
        kind = _choice(init["kind"], ("explicit", "historical_seed", "checkpoint"))
        provenance = _provenance(init["provenance"])
        initial_index = _int(init["update_index"], 0)
        _array(init["omega"], size, _complex)
        if ("preset_id" in init) != (kind == "historical_seed") or ("parent_digest" in init and kind != "checkpoint"):
            raise ValueError("incompatible initialization fields")
        if kind == "historical_seed":
            _choice(init["preset_id"], ("gate_torus_seed_v1",))
            if provenance.kind != "historical_preset" or provenance.source_id != init["preset_id"]:
                raise ValueError("inconsistent seed provenance")
            from ._presets import historical_seed
            if init["omega"] != _encode(historical_seed(init["preset_id"]).omega):
                raise ValueError("historical seed values do not match the named preset")
        elif provenance.kind == "historical_preset" or (kind == "checkpoint") != (provenance.kind == "checkpoint"):
            raise ValueError("initialization kind/provenance mismatch")
        if "parent_digest" in init:
            _sha(init["parent_digest"])
        selection = data["selection"]
        _keys(selection, ("readouts", "diagnostics", "observer_ids"))
        readouts = _selection(selection["readouts"], _READOUTS)
        diagnostics = _selection(selection["diagnostics"], _DIAGNOSTICS)
        observer_ids = _array(selection["observer_ids"], None, _string)
        if len(observer_ids) != len(set(observer_ids)):
            raise ValueError("duplicate observer IDs")
        if topology == "ring" and (readouts or diagnostics or observer_ids):
            raise ValueError("ring observations are not supported in v1")
        if not observer_ids and any(key in diagnostics for key in _OBSERVER_DIAGNOSTICS):
            raise ValueError("observer diagnostic requires an observer")
        observers = _array(data["observers"], len(observer_ids), lambda v: v)
        for observer, oid in zip(observers, observer_ids):
            _keys(observer, ("observer_id", "variant", "config", "q", "t", "m", "N", "q_step", "dt",
                             "initialization", "provenance"))
            if observer["observer_id"] != oid:
                raise ValueError("observer order/ID mismatch")
            variant = _choice(observer["variant"], ("staged", "ema"))
            _config(observer["config"], variant)
            Clock(q=_int(observer["q"]), N=_int(observer["N"], 1),
                  t=_f64(observer["t"]), q_step=_int(observer["q_step"]))
            _f64(observer["dt"])
            mode = _choice(observer["initialization"], _MODES)
            prov = _provenance(observer["provenance"])
            if prov.kind == "historical_preset":
                _choice(prov.source_id, ("paper_e_staged_v1", "paper_e_ema_v1"))
            if variant == "staged":
                if observer["m"] is not None:
                    raise ValueError("staged memory must be null")
            else:
                EMAState(m=_f64(observer["m"]))
            if mode == "historical_constructor_zero" and (initial_index != 0 or
                    (variant == "ema" and _f64(observer["m"]) != 0)):
                raise ValueError("invalid constructor-zero initialization")
        samples = _array(data["samples"], None, lambda v: v)
        if not samples:
            raise ValueError("samples cannot be empty")
        for ordinal, sample in enumerate(samples):
            _keys(sample, ("update_index", "omega", "observer_states", "raw_readouts", "observer_results", "diagnostics"))
            if _int(sample["update_index"], 0) != initial_index + ordinal:
                raise ValueError("noncontiguous sample indices")
            _array(sample["omega"], size, _complex)
            if ordinal == 0 and sample["omega"] != init["omega"]:
                raise ValueError("initialization differs from first sample")
            _keys(sample["observer_states"], observer_ids)
            _keys(sample["observer_results"], observer_ids)
            _keys(sample["raw_readouts"], readouts)
            _keys(sample["diagnostics"], diagnostics)
            for value in sample["raw_readouts"].values():
                _array(value, 3, _f64)
            for observer in observers:
                oid, variant = observer["observer_id"], observer["variant"]
                snapshot = sample["observer_states"][oid]
                _keys(snapshot, ("q", "t", "m", "observer_update_count"))
                q = _int(snapshot["q"])
                _f64(snapshot["t"])
                if ordinal and not 0 <= q < _int(observer["N"]):
                    raise ValueError("advanced q outside clock modulus")
                if _int(snapshot["observer_update_count"], 0) != ordinal:
                    raise ValueError("observer count mismatch")
                if variant == "staged":
                    if snapshot["m"] is not None:
                        raise ValueError("staged memory must be null")
                else:
                    EMAState(m=_f64(snapshot["m"]))
                if ordinal == 0 and any(snapshot[key] != observer[key] for key in ("q", "t", "m")):
                    raise ValueError("initial observer snapshot mismatch")
                mode = observer["initialization"] if ordinal == 0 else "recomputed"
                _result(sample["observer_results"][oid], variant, mode)
            for name, value in sample["diagnostics"].items():
                if name in _OBSERVER_DIAGNOSTICS:
                    _keys(value, observer_ids)
                    for item in value.values():
                        _diagnostic(name, item)
                else:
                    _diagnostic(name, value)
        ids = _array(data["definition_ids"], None, lambda v: _choice(v, _LEDGER))
        if ids != _definition_ids(data):
            raise ValueError("definition IDs do not match the selected operations")
        expected_papers = {"PA"}
        if "B01" in ids:
            expected_papers.update(("PB", "PE"))
        if observers or diagnostics:
            expected_papers.add("PE")
        if kind == "historical_seed":
            expected_papers.add("PF")
        if [paper["source_id"] for paper in data["paper_references"]] != sorted(expected_papers):
            raise ValueError("paper references do not match the selected operations")
        continuation = data["continuation"]
        if continuation is not None:
            _keys(continuation, ("parent_digest", "junction_index"))
            _sha(continuation["parent_digest"])
            if not initial_index <= _int(continuation["junction_index"], 0) <= _int(samples[-1]["update_index"]):
                raise ValueError("continuation junction outside samples")
        segments = data["execution_metadata"]
        if _int(segments[0]["first_update_index"]) != initial_index or segments[-1]["last_update_index"] != samples[-1]["update_index"]:
            raise ValueError("execution metadata does not cover the record")
        for previous, current in zip(segments, segments[1:]):
            if current["first_update_index"] != previous["last_update_index"]:
                raise ValueError("execution segments must meet at a junction")
        if continuation is None:
            if len(segments) != 1:
                raise ValueError("a fresh run has exactly one execution segment")
        elif len(segments) < 2 or segments[-1]["first_update_index"] != continuation["junction_index"]:
            raise ValueError("continuation must name the last execution junction")
