"""Application request v1: explicit text, loss-aware representation, no science."""
from copy import deepcopy
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from importlib import resources
import json
import math
import re
import uuid

OPERATIONS = frozenset(("run", "resume", "new_checkpoint_run", "geometry", "load_record"))
DIAGNOSTICS = ("chiral_area_accounting", "intensity_budget", "potential",
               "readout_accounting", "historical_alignment")
OBSERVER_NAMES = ("paper_e_staged_v1", "paper_e_ema_v1")
SOFT_RANGES = {"eps": ("-0.1", "0.1", "0.001"), "g": ("-0.5", "0.5", "0.005"),
               "phase_strength": ("-0.05", "0.05", "0.001"),
               **{f"k{i}": ("-2", "2", "0.01") for i in range(3)},
               "updates": ("0", "1000", "1")}


def help_data():
    return json.loads(resources.files("trioctagon_ui").joinpath("help.json").read_text(encoding="utf-8"))


def number(text, field="value"):
    if not isinstance(text, str) or not text.strip():
        raise ValueError(f"{field}: enter an explicit number")
    try:
        exact = Decimal(text.strip())
    except InvalidOperation as exc:
        raise ValueError(f"{field}: malformed number") from exc
    if not exact.is_finite():
        raise ValueError(f"{field}: NaN and Infinity are not accepted")
    value = float(exact)
    if not math.isfinite(value):
        raise ValueError(f"{field}: not representable as finite binary64")
    if exact != 0 and value == 0:
        raise ValueError(f"{field}: nonzero decimal underflows to binary64 zero")
    return value


def integer(text, field="value"):
    if not isinstance(text, str) or not re.fullmatch(r"[+]?[0-9]+", text.strip()):
        raise ValueError(f"{field}: enter an integer >= 0")
    return int(text.strip())


def rational(text):
    if not isinstance(text, str) or len(text) > 512 or not re.fullmatch(r"[+-]?[0-9]+(?:/[+-]?[0-9]+)?", text.strip()):
        raise ValueError("s: enter an exact integer or integer/integer rational (at most 512 characters)")
    parts = text.strip().split("/")
    try:
        value = Fraction(int(parts[0]), int(parts[1]) if len(parts) == 2 else 1)
    except ZeroDivisionError as exc:
        raise ValueError("s: denominator must not be zero") from exc
    if value <= 0:
        raise ValueError("s: must be positive")
    return value


def blank_draft():
    return {"topology": "triad", "omega": [["", ""] for _ in range(3)],
            "update_index": "", "eps": "", "g": "", "phase_strength": "",
            "k": ["", "", ""], "updates": "", "observers": [], "readouts": [],
            "diagnostics": [], "provenance": {"source_id": "trioctagon-scientific-ui",
            "source_revision": None, "locator": "manual-entry", "notes": ""},
            "origin": {"seed": None, "parameters": None, "changes": []}}


def apply_seed(draft):
    result = deepcopy(draft)
    result["omega"] = deepcopy(help_data()["presets"]["gate_torus_seed_v1"]["omega"])
    result["origin"]["seed"] = "gate_torus_seed_v1"
    return result


def apply_reference(draft, phase):
    if phase not in ("0", "0.001"):
        raise ValueError("Choose phase_strength=0 or 0.001 explicitly")
    result = deepcopy(draft)
    result.update(deepcopy(help_data()["presets"]["L01"]["parameters"]))
    result["phase_strength"] = phase
    result["origin"]["parameters"] = "L01"
    return result


def mark_edited(draft, field):
    result = deepcopy(draft)
    group = "seed" if field.startswith("omega") else "parameters" if field in ("eps", "g", "phase_strength", "k") else None
    if group and result["origin"].get(group):
        result["origin"]["changes"].append(f"Edited {field} from {result['origin'][group]}")
        result["origin"][group] = None
    return result


def equal_k(draft, text):
    number(text, "equal k")
    result = mark_edited(draft, "k")
    result["k"] = [text, text, text]
    return result


def resolve_draft(draft):
    if not isinstance(draft, dict) or set(draft) != set(blank_draft()):
        raise ValueError("draft: missing or unsupported fields")
    if draft["topology"] != "triad":
        raise ValueError("K4b topology is triad; ring editing is deferred")
    if not isinstance(draft["omega"], list) or len(draft["omega"]) != 3 or any(not isinstance(p, list) or len(p) != 2 for p in draft["omega"]):
        raise ValueError("Omega requires three real/imaginary pairs")
    if not isinstance(draft["k"], list) or len(draft["k"]) != 3:
        raise ValueError("k requires three explicit values")
    resolved = {k: number(draft[k], k).hex() for k in ("eps", "g", "phase_strength")}
    resolved["k"] = [number(v, f"k{i}").hex() for i, v in enumerate(draft["k"])]
    resolved["omega"] = [[number(v, f"Omega{i}.{part}").hex() for part, v in zip(("re", "im"), pair)] for i, pair in enumerate(draft["omega"])]
    resolved["update_index"] = str(integer(draft["update_index"], "update_index"))
    resolved["updates"] = str(integer(draft["updates"], "updates"))
    for field, allowed in (("observers", OBSERVER_NAMES), ("readouts", ("z_chiral",)), ("diagnostics", DIAGNOSTICS)):
        chosen = draft[field]
        if not isinstance(chosen, list) or any(not isinstance(v, str) or v not in allowed for v in chosen) or len(set(chosen)) != len(chosen):
            raise ValueError(f"{field}: unsupported or duplicate selection")
        resolved[field] = list(chosen)
    if not draft["observers"] and any(v in draft["diagnostics"] for v in ("readout_accounting", "historical_alignment")):
        raise ValueError("readout_accounting and historical_alignment require an explicitly selected observer")
    prov = draft["provenance"]
    if not isinstance(prov, dict) or set(prov) != {"source_id", "source_revision", "locator", "notes"}:
        raise ValueError("provenance: explicit descriptor required")
    if any(not isinstance(prov[k], str) or not prov[k] for k in ("source_id", "locator")):
        raise ValueError("provenance source_id and locator must be nonempty")
    if not isinstance(prov["notes"], str) or (prov["source_revision"] is not None and (not isinstance(prov["source_revision"], str) or not prov["source_revision"])):
        raise ValueError("provenance: invalid notes/revision")
    origin = draft["origin"]
    if not isinstance(origin, dict) or set(origin) != {"seed", "parameters", "changes"} or origin["seed"] not in (None, "gate_torus_seed_v1") or origin["parameters"] not in (None, "L01") or not isinstance(origin["changes"], list) or any(not isinstance(v, str) for v in origin["changes"]):
        raise ValueError("draft origin: invalid preset/change description")
    resolved["topology"] = "triad"
    return resolved


def request(operation, payload):
    if operation not in OPERATIONS:
        raise ValueError("Unsupported UI operation")
    return {"ui_request_version": 1, "request_id": str(uuid.uuid4()), "operation": operation, "payload": deepcopy(payload)}


def run_request(draft, updates=None):
    snapshot = deepcopy(draft)
    if updates is not None:
        snapshot["updates"] = str(updates)
    return request("run", {"draft": snapshot, "resolved": resolve_draft(snapshot)})


def validate_envelope(value):
    if not isinstance(value, dict) or set(value) != {"ui_request_version", "request_id", "operation", "payload"}:
        raise ValueError("Invalid UI request envelope")
    if type(value["ui_request_version"]) is not int or value["ui_request_version"] != 1:
        raise ValueError("Unsupported ui_request_version")
    if not isinstance(value["request_id"], str) or not value["request_id"] or value["operation"] not in OPERATIONS or not isinstance(value["payload"], dict):
        raise ValueError("Invalid request ID, operation or payload")
    return value


def draft_json(draft):
    try:
        resolved = resolve_draft(draft)
    except ValueError:
        resolved = None
    return json.dumps({"ui_request_version": 1, "data_class": "APPLICATION_DATA_NOT_KERNEL_RECORD",
                       "app_version": "0.1.0", "draft": draft, "resolved": resolved}, ensure_ascii=False, indent=2, allow_nan=False)


def load_draft(text):
    data = json.loads(text)
    if not isinstance(data, dict) or set(data) != {"ui_request_version", "data_class", "app_version", "draft", "resolved"} or type(data["ui_request_version"]) is not int or data["ui_request_version"] != 1 or data["app_version"] != "0.1.0" or data["data_class"] != "APPLICATION_DATA_NOT_KERNEL_RECORD":
        raise ValueError("Not a UI draft v1 document")
    draft = data["draft"]
    if not isinstance(draft, dict) or set(draft) != set(blank_draft()):
        raise ValueError("Malformed draft")
    # Check widget structure even when scientific values remain unset/invalid.
    probe = deepcopy(draft)
    for field in ("eps", "g", "phase_strength", "updates", "update_index"):
        if not isinstance(probe[field], str):
            raise ValueError(f"{field}: draft entries must be text")
        probe[field] = "0"
    for field in ("k", "omega"):
        if not isinstance(probe[field], list) or len(probe[field]) != 3:
            raise ValueError(f"{field}: malformed draft array")
    if any(not isinstance(p, list) or len(p) != 2 or any(not isinstance(v, str) for v in p) for p in probe["omega"]) or any(not isinstance(v, str) for v in probe["k"]):
        raise ValueError("Draft Omega/k entries must be text")
    probe["omega"] = [["0", "0"] for _ in range(3)]; probe["k"] = ["0"] * 3
    # An incomplete observer-dependent choice remains visibly invalid after load.
    if isinstance(probe["observers"], list) and not probe["observers"]:
        probe["observers"] = [OBSERVER_NAMES[0]]
    resolve_draft(probe)
    # A blank/incomplete draft can be saved. Its resolved claim must be absent.
    try:
        resolved = resolve_draft(draft)
    except ValueError:
        if data["resolved"] is not None:
            raise ValueError("Invalid draft claims resolved values")
    else:
        if data["resolved"] != resolved:
            raise ValueError("Draft spellings and resolved values disagree")
    return deepcopy(draft)
