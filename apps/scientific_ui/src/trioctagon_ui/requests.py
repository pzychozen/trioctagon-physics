"""Application request v2 and v1 draft migration; representation, never science."""
from copy import deepcopy
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from importlib import resources
import json
import math
import re
import uuid

OPERATIONS = frozenset(("run", "resume", "new_checkpoint_run", "geometry", "load_record", "passive_analysis"))
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
    if len(draft["omega"]) != 3:
        raise ValueError("Historical triad seed cannot fill a larger ring")
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
    if draft["topology"] not in ("triad", "ring"):
        raise ValueError("Topology must be triad or ring")
    if not isinstance(draft["omega"], list) or len(draft["omega"]) < 3 or len(draft["omega"]) % 3 or any(not isinstance(p, list) or len(p) != 2 for p in draft["omega"]):
        raise ValueError("Omega requires 3q explicit real/imaginary pairs, q >= 1")
    if draft["topology"] == "triad" and len(draft["omega"]) != 3:
        raise ValueError("Triad requires exactly three components; explicitly resize the draft")
    if draft["topology"] == "ring" and any(draft[k] for k in ("observers", "readouts", "diagnostics")):
        raise ValueError("Ring requires empty observers/readouts/diagnostics. Clear incompatible passive selections explicitly.")
    if not isinstance(draft["k"], list) or len(draft["k"]) != 3:
        raise ValueError("k requires three explicit values")
    resolved = {k: number(draft[k], k).hex() for k in ("eps", "g", "phase_strength")}
    resolved["k"] = [number(v, f"k{i}").hex() for i, v in enumerate(draft["k"])]
    resolved["omega"] = [[number(v, f"Omega{i}.{part}").hex() for part, v in zip(("re", "im"), pair)] for i, pair in enumerate(draft["omega"])]
    resolved["update_index"] = str(integer(draft["update_index"], "update_index"))
    resolved["updates"] = str(integer(draft["updates"], "updates"))
    if not isinstance(draft["observers"], list):
        raise ValueError("observers must be an explicit list")
    resolved["observers"] = [resolve_observer(v) for v in draft["observers"]]
    ids = [v["observer_id"] for v in resolved["observers"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Observer IDs must be unique")
    if any(v.get("initialization") == "historical_constructor_zero" for v in resolved["observers"]) and int(resolved["update_index"]) != 0:
        raise ValueError("constructor-zero requires update index zero")
    for field, allowed in (("readouts", ("z_chiral",)), ("diagnostics", DIAGNOSTICS)):
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
    resolved["topology"] = draft["topology"]
    return resolved


def request(operation, payload):
    if operation not in OPERATIONS:
        raise ValueError("Unsupported UI operation")
    return {"ui_request_version": 2, "request_id": str(uuid.uuid4()), "operation": operation, "payload": deepcopy(payload)}


def run_request(draft, updates=None):
    snapshot = deepcopy(draft)
    if updates is not None:
        snapshot["updates"] = str(updates)
    return request("run", {"draft": snapshot, "resolved": resolve_draft(snapshot)})


def validate_envelope(value):
    if not isinstance(value, dict) or set(value) != {"ui_request_version", "request_id", "operation", "payload"}:
        raise ValueError("Invalid UI request envelope")
    if type(value["ui_request_version"]) is not int or value["ui_request_version"] != 2:
        raise ValueError("Unsupported ui_request_version")
    if not isinstance(value["request_id"], str) or not value["request_id"] or value["operation"] not in OPERATIONS or not isinstance(value["payload"], dict):
        raise ValueError("Invalid request ID, operation or payload")
    return value


def draft_json(draft):
    try:
        resolved = resolve_draft(draft)
    except ValueError:
        resolved = None
    return json.dumps({"ui_request_version": 2, "data_class": "APPLICATION_DATA_NOT_KERNEL_RECORD",
                       "app_version": "0.1.0", "draft": draft, "resolved": resolved}, ensure_ascii=False, indent=2, allow_nan=False)


def load_draft(text):
    data = json.loads(text)
    if not isinstance(data, dict) or set(data) != {"ui_request_version", "data_class", "app_version", "draft", "resolved"} or type(data["ui_request_version"]) is not int or data["ui_request_version"] not in (1, 2) or data["app_version"] != "0.1.0" or data["data_class"] != "APPLICATION_DATA_NOT_KERNEL_RECORD":
        raise ValueError("Not a supported UI draft document")
    draft = data["draft"]
    if not isinstance(draft, dict) or set(draft) != set(blank_draft()):
        raise ValueError("Malformed draft")
    if data["ui_request_version"] == 1:
        if draft["topology"] != "triad" or len(draft["omega"]) != 3 or any(v not in OBSERVER_NAMES for v in draft["observers"]):
            raise ValueError("Malformed v1 triad/preset draft")
        draft = deepcopy(draft)
        draft["observers"] = [{"mode": "preset", "name": v} for v in draft["observers"]]
        if data["resolved"] is not None:
            claimed = deepcopy(data["resolved"])
            if claimed.get("observers") != data["draft"]["observers"]:
                raise ValueError("v1 observer spellings and resolved values disagree")
            claimed["observers"] = [resolve_observer(v) for v in draft["observers"]]
            data["resolved"] = claimed
    # Check widget structure even when scientific values remain unset/invalid.
    probe = deepcopy(draft)
    for field in ("eps", "g", "phase_strength", "updates", "update_index"):
        if not isinstance(probe[field], str):
            raise ValueError(f"{field}: draft entries must be text")
        probe[field] = "0"
    if not isinstance(probe["k"], list) or len(probe["k"]) != 3 or not isinstance(probe["omega"], list) or len(probe["omega"]) < 3 or len(probe["omega"]) % 3:
        raise ValueError("Malformed draft arrays")
    if len(probe["omega"]) > 3000: raise ValueError("Draft editor row-count resource guard: at most 1000 triads")
    if any(not isinstance(p, list) or len(p) != 2 or any(not isinstance(v, str) for v in p) for p in probe["omega"]) or any(not isinstance(v, str) for v in probe["k"]):
        raise ValueError("Draft Omega/k entries must be text")
    # Validate descriptor shapes while preserving incomplete visible field text.
    for observer in probe["observers"]:
        observer_shape(observer)
    for field, allowed in (("readouts", ("z_chiral",)), ("diagnostics", DIAGNOSTICS)):
        if not isinstance(probe[field], list) or any(not isinstance(v, str) or v not in allowed for v in probe[field]) or len(set(probe[field])) != len(probe[field]):
            raise ValueError(f"Unsupported or duplicate draft {field}")
    probe["omega"] = [["0", "0"] for _ in probe["omega"]]; probe["k"] = ["0"] * 3
    probe["topology"] = "ring" if len(probe["omega"]) > 3 else "triad"
    if draft["topology"] not in ("triad", "ring"):
        raise ValueError("Unknown topology")
    probe["observers"] = []; probe["readouts"] = []; probe["diagnostics"] = []
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


def resize_ring(draft, q, *, discard_confirmed=False):
    if type(q) is not int or not 1 <= q <= 1000:
        raise ValueError("UI row-count guard: q must be 1..1000 (not a kernel limit)")
    size = 3 * q; result = deepcopy(draft)
    if size < len(result["omega"]) and any(v.strip() for p in result["omega"][size:] for v in p) and not discard_confirmed:
        raise ValueError("Confirm discarding nonblank Omega rows")
    result["omega"] = result["omega"][:size] + [["", ""] for _ in range(max(0, size - len(result["omega"])))]
    if size != len(draft["omega"]) and result["origin"]["seed"]:
        result["origin"]["changes"].append("Resized explicit state originally filled from " + result["origin"]["seed"] + "; no seed repetition")
        result["origin"]["seed"] = None
    return result


def signed_integer(text, field):
    if not isinstance(text, str) or not re.fullmatch(r"[+-]?[0-9]+", text.strip()):
        raise ValueError(f"{field}: enter an explicit signed integer")
    return int(text)


CONFIG_FIELDS = {"staged": ("lambda_vp", "gamma", "theta_lock", "alpha", "beta"),
                 "ema": ("lambda_vp", "theta_lock", "alpha", "beta")}


def blank_observer(variant):
    if variant not in CONFIG_FIELDS: raise ValueError("Unknown observer variant")
    return {"mode": "custom", "observer_id": "", "variant": variant,
        "clock": {k: "" for k in ("q", "N", "t", "q_step")}, "dt": "", "initialization": "",
        "config": {k: "" for k in CONFIG_FIELDS[variant]}, "memory": {"m": ""} if variant == "ema" else None,
        "provenance": {"source_id": "trioctagon-scientific-ui", "source_revision": None, "locator": "custom-observer", "notes": ""}, "origin": None}


def observer_shape(value):
    if not isinstance(value, dict): raise ValueError("Observer descriptor must be an object")
    if value.get("mode") == "preset":
        if set(value) != {"mode", "name"} or value["name"] not in OBSERVER_NAMES: raise ValueError("Unknown historical observer")
        return
    if value.get("variant") not in CONFIG_FIELDS or set(value) != set(blank_observer(value["variant"])) or value["mode"] != "custom":
        raise ValueError("Malformed custom observer")
    for field, expected in (("clock", ("q", "N", "t", "q_step")), ("config", CONFIG_FIELDS[value["variant"]]), ("provenance", ("source_id", "source_revision", "locator", "notes"))):
        if not isinstance(value[field], dict) or set(value[field]) != set(expected): raise ValueError(f"Observer {field}: missing/extra fields")
        if any(not isinstance(v, str) for k, v in value[field].items() if k != "source_revision"): raise ValueError(f"Observer {field}: entries must be text")
    if any(not isinstance(value[k], str) for k in ("observer_id", "dt", "initialization")): raise ValueError("Observer entries must be text")
    if value["origin"] is not None and not isinstance(value["origin"], str): raise ValueError("Invalid observer origin")
    if value["variant"] == "ema":
        if not isinstance(value["memory"], dict) or set(value["memory"]) != {"m"} or not isinstance(value["memory"]["m"], str): raise ValueError("EMA requires explicit memory m text")
    elif value["memory"] is not None: raise ValueError("Staged observer memory must be null")


def resolve_observer(value):
    observer_shape(value)
    if value["mode"] == "preset": return {**value, "observer_id": value["name"]}
    if not value["observer_id"].strip(): raise ValueError("Observer ID must be explicit and nonempty")
    if value["initialization"] not in ("recomputed", "historical_constructor_zero"): raise ValueError("Choose observer initialization explicitly")
    clock = value["clock"]
    resolved = deepcopy(value)
    resolved["clock"] = {k: str(signed_integer(clock[k], k)) for k in ("q", "N", "q_step")}
    if int(resolved["clock"]["N"]) < 1: raise ValueError("Clock N must be >= 1")
    resolved["clock"]["t"] = number(clock["t"], "Clock.t").hex()
    resolved["dt"] = number(value["dt"], "Clock dt").hex()
    resolved["config"] = {k: number(v, k).hex() for k, v in value["config"].items()}
    if value["memory"] is not None:
        m = number(value["memory"]["m"], "EMA memory m")
        if abs(m) > 1: raise ValueError("Public EMA memory requires |m| <= 1")
        if value["initialization"] == "historical_constructor_zero" and m != 0: raise ValueError("constructor-zero requires zero initial memory")
        resolved["memory"] = {"m": m.hex()}
    p = value["provenance"]
    if not p["source_id"] or not p["locator"] or (p["source_revision"] is not None and (not isinstance(p["source_revision"], str) or not p["source_revision"])):
        raise ValueError("Observer provenance source/locator/revision invalid")
    return resolved


def preset_to_custom(value):
    observer_shape(value)
    if value["mode"] != "preset": raise ValueError("Select a historical preset to convert")
    result = deepcopy(help_data()["observer_presets"][value["name"]])
    result["mode"] = "custom"; result["origin"] = value["name"]
    result["provenance"]["notes"] += "\nExplicitly converted historical preset to CUSTOM / USER-SUPPLIED; subsequent edits are user values."
    return result


EXACT_LIMITS = {"length": 2048, "tokens": 256, "depth": 32, "integer_digits": 64, "power_bound": 64, "growth_budget": 4096}
D03_FIELDS = {"aligned": ("s", "g_gap"), "from_radius": ("s", "p"), "regular": ("s",),
    "paper_c_member": ("s",), "translate_paper_c_to_regular": ("s",), "shrink_paper_c_at_fixed_centres": ("s",)}


def exact_expression(text):
    """Bounded arithmetic grammar to tagged nodes; no Python expression engine."""
    if not isinstance(text, str) or not text.strip() or len(text) > EXACT_LIMITS["length"]:
        raise ValueError("Exact input length guard: enter 1..2048 characters")
    tokens = []; pos = 0
    while pos < len(text):
        if text[pos].isspace(): pos += 1; continue
        match = re.match(r"[0-9]+|pi|sin|cos|\*\*|[()+*/^\-]", text[pos:])
        if not match: raise ValueError(f"Unsupported exact token at character {pos}; floats/symbols/functions are forbidden")
        tokens.append(match[0]); pos += len(match[0])
        if len(tokens) > EXACT_LIMITS["tokens"]: raise ValueError("Exact token-count guard: maximum 256")
    index = 0
    def peek(): return tokens[index] if index < len(tokens) else None
    def take():
        nonlocal index
        value = peek(); index += 1; return value
    def constant(node):
        if "integer" in node: return Fraction(int(node["integer"]))
        if "rational" in node: return Fraction(int(node["rational"]["numerator"]), int(node["rational"]["denominator"]))
        if "mul" in node:
            result = Fraction(1)
            for v in node["mul"]: result *= constant(v)
            return result
        if "add" in node: return sum((constant(v) for v in node["add"]), Fraction(0))
        if "pow" in node and node["pow"]["exponent"] == {"integer": "-1"}: return 1 / constant(node["pow"]["base"])
        raise ValueError("Power exponent must be an explicit rational")
    def expression(depth=0, minimum=0):
        if depth > EXACT_LIMITS["depth"]: raise ValueError("Exact parse-depth guard: maximum 32")
        token = take()
        if token in ("+", "-"):
            node = expression(depth + 1, 3)
            if token == "-": node = {"mul": [{"integer": "-1"}, node]}
        elif token == "(":
            node = expression(depth + 1)
            if take() != ")": raise ValueError("Missing exact closing parenthesis")
        elif token in ("sin", "cos"):
            if take() != "(": raise ValueError("Exact trigonometric call requires parentheses")
            node = {token: expression(depth + 1)}
            if take() != ")": raise ValueError("Missing exact function closing parenthesis")
        elif token == "pi": node = {"pi": True}
        elif token and token.isdigit():
            if len(token) > EXACT_LIMITS["integer_digits"]: raise ValueError("Exact integer-digit guard: maximum 64")
            node = {"integer": str(int(token))}
        else: raise ValueError("Expected exact integer, pi, sin/cos or parenthesis")
        while peek() in ("+", "-", "*", "/", "^", "**"):
            op = peek(); precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 4, "**": 4}[op]
            if precedence < minimum: break
            take(); right = expression(depth + 1, precedence if precedence == 4 else precedence + 1)
            if op in ("^", "**"):
                try: exponent = constant(right)
                except ZeroDivisionError as exc: raise ValueError("Zero rational exponent denominator") from exc
                if abs(exponent.numerator) > 64 or exponent.denominator > 64: raise ValueError("Exact power resource guard: reduced numerator/denominator bounded by 64")
                right = {"rational": {"numerator": str(exponent.numerator), "denominator": str(exponent.denominator)}}
                node = {"pow": {"base": node, "exponent": right}}
            elif op == "/": node = {"mul": [node, {"pow": {"base": right, "exponent": {"integer": "-1"}}}]}
            elif op == "*": node = {"mul": [node, right]}
            else: node = {"add": [node, right if op == "+" else {"mul": [{"integer": "-1"}, right]}]}
        return node
    result = expression()
    if index != len(tokens): raise ValueError("Trailing exact input tokens")
    def resource_cost(node, depth=0):
        if depth > 32: raise ValueError("Exact expression-tree depth guard: maximum 32")
        kind, value = next(iter(node.items()))
        if kind == "integer": cost = len(value.lstrip("-"))
        elif kind == "rational": cost = max(len(v.lstrip("-")) for v in value.values())
        elif kind == "pi": cost = 1
        elif kind in ("sin", "cos"): cost = resource_cost(value, depth + 1)
        elif kind in ("add", "mul"): cost = sum(resource_cost(v, depth + 1) for v in value) + 1
        else:
            exponent = constant(value["exponent"])
            cost = resource_cost(value["base"], depth + 1) * max(1, abs(exponent.numerator))
        if cost > EXACT_LIMITS["growth_budget"]: raise ValueError("Exact representation-growth resource guard: budget 4096")
        return cost
    resource_cost(result)
    return result


def geometry_request(definition, fields):
    if definition == "C01":
        if set(fields) != {"section_heights"} or not isinstance(fields["section_heights"], list): raise ValueError("C01 requires an explicit height list")
        nodes = {"section_heights": [exact_expression(v) for v in fields["section_heights"]]}
    elif definition == "D03":
        construction = fields.get("construction")
        if construction not in D03_FIELDS or set(fields) != {"construction", *D03_FIELDS[construction]}: raise ValueError("D03 option matrix mismatch")
        nodes = {"construction": construction, **{k: exact_expression(fields[k]) for k in D03_FIELDS[construction]}}
    else: raise ValueError("Choose C01 or D03 explicitly")
    return request("geometry", {"definition_id": definition, "fields": fields, "exact_nodes": nodes})


ANALYSIS_TYPES = ("step_preview", "advance_clock", "advance_ema", "observe_staged", "observe_ema", "quadratic_form",
    "readout_accounting", "chiral_area_accounting", "intensity_budget", "potential", "historical_alignment",
    "direct_history_coordinates", "cylinder_point", "cylinder_history_coordinates", "history_torus_coordinates")
HISTORY_TYPES = ("direct_history_coordinates", "cylinder_history_coordinates", "history_torus_coordinates")
KAPPA_SOURCES = ("chiral_area_accounting.intensity", "intensity_budget.intensity_before")


def analysis_template(kind):
    if kind not in ANALYSIS_TYPES: raise ValueError("Unsupported detached analysis")
    omega = [["", ""] for _ in range(3)]; vector = ["", "", ""]
    parameters = {"eps": "", "g": "", "phase_strength": "", "k": ["", "", ""]}
    clock = {k: "" for k in ("q", "N", "t", "q_step")}
    if kind == "step_preview": return {"state": {"omega": omega, "update_index": ""}, "parameters": parameters, "topology": ""}
    if kind == "advance_clock": return {"clock": clock, "dt": ""}
    if kind == "advance_ema": return {"omega": omega, "memory": {"m": ""}}
    if kind.startswith("observe_"):
        variant = kind[8:]; result = {"omega": omega, "clock": clock, "config": {k: "" for k in CONFIG_FIELDS[variant]}}
        if variant == "ema": result["memory"] = {"m": ""}
        return result
    if kind == "quadratic_form": return {"vector": vector}
    if kind == "readout_accounting": return {"readout": {"z": "", "Z_macro": vector[:], "Z_chiral": vector[:], "Z_total": vector[:], "variant": "", "initialization": ""}, "alpha": "", "beta": ""}
    if kind == "chiral_area_accounting": return {"omega": omega}
    if kind in ("intensity_budget", "potential"): return {"omega": omega, "parameters": parameters}
    if kind == "historical_alignment": return {k: vector[:] for k in ("macro", "chiral", "total_vector")}
    if kind == "cylinder_point": return {k: "" for k in ("kappa", "q", "z", "N")}
    return {"observer_id": "", **({"key": ""} if kind == "direct_history_coordinates" else {"kappa_source": "", "N": "", **({"R": "", "r_max": ""} if kind == "history_torus_coordinates" else {})})}


def analysis_request(kind, inputs, *, source=None):
    if kind not in ANALYSIS_TYPES or not isinstance(inputs, dict) or set(inputs) != set(analysis_template(kind)):
        raise ValueError("Detached analysis input fields do not match the selected public operation")
    if source is None: source = {"mode": "explicit"}
    if source.get("mode") == "explicit":
        if set(source) != {"mode"} or kind in HISTORY_TYPES: raise ValueError("History analysis requires an explicit selected record")
    elif source.get("mode") == "record":
        if set(source) != {"mode", "record_json", "sample_index"} or not isinstance(source["record_json"], str): raise ValueError("Explicit record source is incomplete")
        integer(source["sample_index"], "sample ordinal")
    else: raise ValueError("Choose explicit scratchpad or explicit stored record source")
    return request("passive_analysis", {"analysis_type": kind, "inputs": inputs, "source": source})
