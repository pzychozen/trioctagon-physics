"""Descriptive comparisons of immutable stored values; no scientific execution."""
from collections.abc import Mapping
from dataclasses import dataclass, field
import math
import re
from trioctagon_ui.record_views import freeze


def plain(value):
    if isinstance(value, Mapping): return {k: plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [plain(v) for v in value]
    return value


def leaves(value, prefix=""):
    if isinstance(value, Mapping):
        if set(value) == {"f64"}: yield prefix, plain(value)
        else:
            for key, item in value.items(): yield from leaves(item, f"{prefix}.{key}" if prefix else key)
    elif isinstance(value, (tuple, list)):
        for i, item in enumerate(value): yield from leaves(item, f"{prefix}[{i}]")
    else: yield prefix, value


def scalar(value):
    if isinstance(value, Mapping) and set(value) == {"f64"}: return float.fromhex(value["f64"])
    if type(value) in (int, float): return value
    if isinstance(value, str) and re.fullmatch(r"[+-]?\d+", value): return int(value)
    return None


def display(value, precision=17):
    if value is None: return "not recorded"
    if isinstance(value, Mapping) and set(value) == {"f64"}: return format(float.fromhex(value["f64"]), f".{precision}g") + " [" + value["f64"] + "]"
    return str(value)


@dataclass(frozen=True)
class ComparisonView:
    a: object
    b: object
    channels: tuple = ()
    result: object = field(init=False)

    def __post_init__(self):
        a, b = self.a, self.b
        if a.kind != b.kind or a.kind not in ("KERNEL_RUN_RECORD", "GEOMETRY_RECORD"):
            raise ValueError("Choose two RunRecords or two GeometryRecords; cross-kind comparison is unavailable")
        result = {"kind": a.kind, "parents": [{"digest": v.digest, "source_commit": v.data["implementation"]["commit"]} for v in (a, b)],
            "qualification": "Descriptive stored values. B - A is DISPLAY_DERIVATION_ONLY; no interpolation, resampling or scientific criterion."}
        if a.kind == "GEOMETRY_RECORD":
            fields = ("geometry_definition_id", "options", "resolved_parameters", "objects", "coordinates", "symmetry", "construction_provenance")
            result["metadata"] = {label: {k: plain(v.data[k]) for k in fields} for label, v in (("A", a), ("B", b))}
            result["presentation"] = "Separate panels, frames and cameras; no automatic alignment, deformation or overlay"
        else:
            sizes = [int(v.data["state_size"]) for v in (a, b)]
            if len(set(self.channels)) != len(self.channels) or any(type(i) is not int or not 0 <= i < min(sizes) for i in self.channels):
                raise ValueError("Explicit shared Omega channel indices must exist in both records")
            fields = ("parameters", "parameter_provenance", "initialization", "topology", "state_size", "observers", "selection", "execution_metadata")
            result["metadata"] = {label: {**{k: plain(v.data[k]) for k in fields}, "sample_count": len(v.samples),
                "source_commit": v.data["implementation"]["commit"], "digest": v.digest} for label, v in (("A", a), ("B", b))}
            result["state_size_mismatch"] = sizes[0] != sizes[1]
            result["explicit_shared_channels"] = list(self.channels)
            samples = [{int(s["update_index"]): s for s in v.samples} for v in (a, b)]
            if any(len(mapped) != len(v.samples) for mapped, v in zip(samples, (a, b))): raise ValueError("Duplicate stored update indices")
            left, right = map(set, samples)
            result.update(indices_only_A=sorted(left - right), indices_common=sorted(left & right), indices_only_B=sorted(right - left))
            rows = []
            for index in result["indices_common"]:
                values = [dict(leaves(mapped[index])) for mapped in samples]
                for path in sorted(set(values[0]) | set(values[1])):
                    if path == "update_index": continue
                    if path.startswith("omega[") and int(path.split("[", 1)[1].split("]", 1)[0]) not in self.channels: continue
                    x, y = values[0].get(path), values[1].get(path)
                    nx, ny = scalar(x), scalar(y)
                    delta = None
                    if nx is not None and ny is not None:
                        delta = ny - nx
                        if isinstance(delta, float) and not math.isfinite(delta): delta = "not representable at binary64 display precision"
                    rows.append({"update_index": index, "path": path, "A": x, "B": y, "delta": delta})
            result["rows"] = rows
        object.__setattr__(self, "result", freeze(result))

    def rows(self, precision=17):
        return tuple((str(row["update_index"]), row["path"], display(row["A"], precision), display(row["B"], precision),
            "not recorded / not numeric" if row["delta"] is None else str(row["delta"])) for row in self.result.get("rows", ()))

    def series(self):
        paths = {}
        for row in self.result.get("rows", ()):
            x, y = scalar(row["A"]), scalar(row["B"])
            if x is not None and y is not None: paths.setdefault(row["path"], []).append((row["update_index"], x, y))
        return paths
