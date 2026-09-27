"""Detached presentation of worker-validated public record JSON; no kernel imports."""
from dataclasses import dataclass, field
from importlib import metadata
import json
import os
from pathlib import Path
import tempfile
from types import MappingProxyType


def freeze(value):
    if isinstance(value, dict):
        return MappingProxyType({k: freeze(v) for k, v in value.items()})
    if isinstance(value, list):
        return tuple(freeze(v) for v in value)
    return value


def f64(value):
    return float.fromhex(value["f64"])


def flatten(value, prefix="", precision=None):
    """Rows preserve stored spelling and present decoded numbers alongside it."""
    if isinstance(value, (dict, MappingProxyType)):
        if set(value) == {"f64"}:
            decoded = f64(value)
            yield prefix, repr(decoded) if precision is None else format(decoded, f".{precision}g"), value["f64"]
        else:
            for key, item in value.items():
                yield from flatten(item, f"{prefix}.{key}" if prefix else str(key), precision)
    elif isinstance(value, (list, tuple)):
        for i, item in enumerate(value):
            yield from flatten(item, f"{prefix}[{i}]", precision)
    else:
        yield prefix, str(value), str(value)


@dataclass(frozen=True)
class RecordView:
    canonical_json: str
    data: object = field(init=False, repr=False)
    samples: tuple = field(init=False, repr=False)
    series: object = field(init=False, repr=False)

    def __post_init__(self):
        data = freeze(json.loads(self.canonical_json))
        object.__setattr__(self, "data", data)
        samples = data.get("samples", ())
        object.__setattr__(self, "samples", samples)
        series = {"indices": tuple(int(s["update_index"]) for s in samples)}
        if samples:
            for i in range(int(data["state_size"])):
                for part in ("re", "im"):
                    series[f"omega{i}.{part}"] = tuple(f64(s["omega"][i][part]) for s in samples)
            if all("z_chiral" in s["raw_readouts"] for s in samples):
                for i in range(3):
                    series[f"chirality{i}"] = tuple(f64(s["raw_readouts"]["z_chiral"][i]) for s in samples)
        object.__setattr__(self, "series", MappingProxyType(series))

    @property
    def digest(self):
        return self.data["deterministic_sha256"]

    @property
    def kind(self):
        return self.data["record_type"]

    def sample_rows(self, index, precision=None):
        return tuple(flatten(self.samples[index], precision=precision))

    def missing_series(self, name):
        return "recorded" if name in self.series else "not recorded"

    def save(self, path):
        atomic_text(path, self.canonical_json)


@dataclass(frozen=True)
class AnalysisView:
    """Detached application cache, never placed in public record history."""
    result: object
    _coordinates: object = field(init=False, repr=False)

    def __post_init__(self):
        copied = json.loads(json.dumps(self.result, allow_nan=False))
        if copied.get("result_kind") != "analysis": raise ValueError("AnalysisView requires detached analysis")
        object.__setattr__(self, "result", freeze(copied))
        data = self.result["data"]; coordinates = None
        if isinstance(data, MappingProxyType) and all(k in data for k in ("x", "y", "z")):
            coordinates = tuple(tuple(f64(v) for v in data[k]) for k in ("x", "y", "z"))
        elif self.result["analysis_type"] == "cylinder_point":
            coordinates = tuple((f64(v),) for v in data)
        object.__setattr__(self, "_coordinates", coordinates)

    def rows(self, precision=None):
        return tuple(flatten(self.result, precision=precision))

    @property
    def coordinates(self):
        return self._coordinates


def atomic_text(path, text):
    path = Path(path)
    fd, staging = tempfile.mkstemp(prefix=".trioctagon-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as out:
            out.write(text)
            out.flush()
            os.fsync(out.fileno())
        os.replace(staging, path)
    finally:
        if os.path.exists(staging):
            os.unlink(staging)


def kernel_lock():
    dist = metadata.distribution("trioctagon-scientific-ui")
    files = [p for p in dist.files or () if str(p).replace("\\", "/").endswith("share/trioctagon-scientific-ui/kernel-artifact.lock.json")]
    if len(files) != 1:
        raise RuntimeError("Installed kernel artifact lock is missing or ambiguous; reinstall the companion wheel")
    return json.loads(Path(dist.locate_file(files[0])).read_text(encoding="utf-8"))
