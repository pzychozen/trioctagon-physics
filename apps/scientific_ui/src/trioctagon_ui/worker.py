"""Installed, GUI-free scientific boundary. All scientific calls use the facade."""
import argparse
from collections.abc import Mapping
from dataclasses import fields, is_dataclass
import json
import math
from pathlib import Path
import sys
import traceback

from trioctagon_ui import requests
from trioctagon_ui.record_views import atomic_text, f64, kernel_lock


def execute(envelope):
    requests.validate_envelope(envelope)
    payload, operation = envelope["payload"], envelope["operation"]
    if operation == "passive_analysis":
        return passive_analysis(payload)
    from kernel_physics import api

    def keys(expected):
        if set(payload) != set(expected):
            raise ValueError(f"{operation}: missing or unsupported payload fields")

    def load(text):
        kind = json.loads(text).get("record_type")
        if kind == "KERNEL_RUN_RECORD":
            return api.RunRecord.from_json(text)
        if kind == "GEOMETRY_RECORD":
            return api.GeometryRecord.from_json(text)
        raise ValueError("Unsupported public record type")

    def run(parent=None):
        draft = payload["draft"]
        resolved = requests.resolve_draft(draft)
        if payload["resolved"] != resolved:
            raise ValueError("Submitted spellings and resolved request values disagree")
        user = draft["provenance"]
        literal = {k: draft[k] for k in ("eps", "g", "phase_strength", "updates", "update_index")}
        literal.update({f"k{i}": v for i, v in enumerate(draft["k"])})
        literal.update({f"Omega{i}.{p}": v for i, pair in enumerate(draft["omega"]) for p, v in zip(("re", "im"), pair)})
        notes = user["notes"] + "\n" + "\n".join(draft["origin"]["changes"])
        provenance = api.Provenance(kind="user_supplied", source_id=user["source_id"],
            source_revision=user["source_revision"], locator=user["locator"], literal_values=literal, notes=notes)
        parameters = api.Parameters(**{k: float.fromhex(resolved[k]) for k in ("eps", "g", "phase_strength")},
                                    k=tuple(float.fromhex(v) for v in resolved["k"]))
        initial = api.State(omega=tuple(complex(float.fromhex(pair[0]), float.fromhex(pair[1])) for pair in resolved["omega"]),
                            update_index=int(resolved["update_index"]))
        init_provenance = provenance
        parameter_provenance = provenance
        if draft["origin"]["parameters"] == "L01":
            reference = requests.help_data()["presets"]["L01"]["parameters"]
            if any(draft[k] != reference[k] for k in ("eps", "g", "k")) or draft["phase_strength"] not in ("0", "0.001"):
                raise ValueError("Edited parameter values cannot retain the L01 reference label")
            parameter_provenance = api.Provenance(kind="historical_preset", source_id="L01",
                source_revision=requests.help_data()["source_commit"], locator="K0 ledger L01",
                literal_values=literal, notes=notes + "\nReference fill; original rationale O02 unresolved.")
        if draft["origin"]["seed"]:
            seed = api.historical_seed(draft["origin"]["seed"])
            if tuple((z.real.hex(), z.imag.hex()) for z in initial.omega) != tuple((z.real.hex(), z.imag.hex()) for z in seed.omega):
                raise ValueError("Edited seed cannot retain historical preset provenance")
            init_provenance = seed.provenance
        if parent is not None:
            if not isinstance(parent, api.RunRecord):
                raise TypeError("Checkpoint requires a RunRecord")
            if payload["observer_reset"] != "reinitialize_selected":
                raise ValueError("Checkpoint requires explicit reinitialize_selected observer policy")
            index = requests.integer(payload["sample_index"], "sample_index")
            samples = parent.data["samples"]
            if index >= len(samples):
                raise ValueError("Checkpoint sample index is outside the parent record")
            sample = samples[index]
            initial = api.State(omega=tuple(complex(f64(v["re"]), f64(v["im"])) for v in sample["omega"]),
                                update_index=int(sample["update_index"]))
            if tuple((z.real.hex(), z.imag.hex()) for z in initial.omega) != tuple(tuple(pair) for pair in resolved["omega"]) or str(initial.update_index) != resolved["update_index"]:
                raise ValueError("Checkpoint draft state must exactly match the selected parent sample")
            init_provenance = api.Provenance(kind="checkpoint", source_id=parent.deterministic_sha256,
                source_revision=parent.data["implementation"]["commit"], locator=f"samples[{index}]",
                literal_values={**literal, "parent_digest": parent.deterministic_sha256, "sample_index": str(index)},
                notes=notes + "\nNew run from checkpoint; selected observer descriptors explicitly initialized.")
        observers = tuple(materialize_observer(value) for value in draft["observers"])
        return api.run(initial, parameters, topology=resolved["topology"], updates=int(resolved["updates"]),
                       parameter_provenance=parameter_provenance, initialization_provenance=init_provenance,
                       observers=observers, readouts=tuple(resolved["readouts"]), diagnostics=tuple(resolved["diagnostics"]))

    if operation == "run":
        keys(("draft", "resolved")); record = run()
    elif operation == "new_checkpoint_run":
        keys(("draft", "resolved", "record_json", "sample_index", "observer_reset"))
        record = run(load(payload["record_json"]))
    elif operation == "resume":
        keys(("record_json", "updates"))
        record = api.resume(load(payload["record_json"]), updates=requests.integer(payload["updates"], "updates"))
    elif operation == "load_record":
        keys(("record_json",)); record = load(payload["record_json"])
    else:
        keys(("definition_id", "fields", "exact_nodes"))
        checked = requests.geometry_request(payload["definition_id"], payload["fields"])["payload"]
        if checked != payload: raise ValueError("Exact spellings and expression nodes disagree")
        nodes = payload["exact_nodes"]
        options = ({"section_heights": [materialize_exact(v) for v in nodes["section_heights"]]}
            if payload["definition_id"] == "C01" else {k: v if k == "construction" else materialize_exact(v) for k, v in nodes.items()})
        record = api.get_geometry(payload["definition_id"], options=options)
    canonical = record.to_json()
    # Completion requires the public loader, as well as successful production.
    checked = load(canonical)
    data = checked.data
    produced = operation != "load_record"
    if produced and data["implementation"]["commit"] != kernel_lock()["source_commit"]:
        raise ValueError("Current kernel source does not match the selected certified artifact lock")
    return {"result_kind": "record", "canonical_json": canonical, "record_type": data["record_type"],
            "deterministic_sha256": checked.deterministic_sha256,
            "source_commit": data["implementation"]["commit"], "produced_current": produced}


def materialize_exact(node):
    from sympy import Integer, Rational, pi, Add, Mul, Pow, sin, cos
    kind, value = next(iter(node.items()))
    if kind == "integer": return Integer(value)
    if kind == "rational": return Rational(int(value["numerator"]), int(value["denominator"]))
    if kind == "pi": return pi
    if kind == "add": return Add(*(materialize_exact(v) for v in value))
    if kind == "mul": return Mul(*(materialize_exact(v) for v in value))
    if kind == "pow": return Pow(materialize_exact(value["base"]), materialize_exact(value["exponent"]))
    if kind in ("sin", "cos"): return (sin if kind == "sin" else cos)(materialize_exact(value))
    raise ValueError("Unknown exact node")


def materialize_observer(value):
    from kernel_physics import api
    resolved = requests.resolve_observer(value)
    if value["mode"] == "preset": return api.historical_observer(value["name"])
    config = (api.StagedConfig if value["variant"] == "staged" else api.EMAConfig)(**{k: float.fromhex(v) for k, v in resolved["config"].items()})
    clock = api.Clock(**{k: float.fromhex(v) if k == "t" else int(v) for k, v in resolved["clock"].items()})
    literal = {"observer_id": value["observer_id"], "variant": value["variant"], "initialization": value["initialization"], "dt": value["dt"]}
    literal.update({"clock." + k: v for k, v in value["clock"].items()})
    literal.update({"config." + k: v for k, v in value["config"].items()})
    if value["memory"] is not None: literal["memory.m"] = value["memory"]["m"]
    p = value["provenance"]
    provenance = api.Provenance(kind="user_supplied", source_id=p["source_id"], source_revision=p["source_revision"],
        locator=p["locator"], notes=p["notes"] + ("\nHistorical origin: " + value["origin"] if value["origin"] else ""), literal_values=literal)
    memory = api.EMAState(m=float.fromhex(resolved["memory"]["m"])) if resolved["memory"] is not None else None
    return api.ObserverRequest(observer_id=value["observer_id"], config=config, clock=clock, memory=memory,
        dt=float.fromhex(resolved["dt"]), initialization=value["initialization"], provenance=provenance)


def lossless(value):
    """Application data codec, distinct from public record authority."""
    if value is None or isinstance(value, (str, bool, int)): return value
    if isinstance(value, float): return {"f64": value.hex()}
    if isinstance(value, complex): return {"re": lossless(value.real), "im": lossless(value.imag)}
    if is_dataclass(value): return {f.name: lossless(getattr(value, f.name)) for f in fields(value)}
    if isinstance(value, Mapping): return {str(k): lossless(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)): return [lossless(v) for v in value]
    if type(value).__module__.startswith("numpy") and hasattr(value, "tolist"): return lossless(value.tolist())
    raise TypeError(f"Unsupported detached result representation: {type(value).__name__}")


def passive_analysis(payload):
    if set(payload) != {"analysis_type", "inputs", "source"}: raise ValueError("Malformed passive-analysis payload")
    kind, original, source = payload["analysis_type"], payload["inputs"], payload["source"]
    requests.analysis_request(kind, original, source=source)
    if kind in requests.AXIAL_TYPES:
        return axial_analysis(kind, original, source)
    from kernel_physics import api
    inputs = json.loads(json.dumps(original)); context = {"request": original, "source": {k: v for k, v in source.items() if k != "record_json"}}
    parent = None; sample_index = None
    if source["mode"] == "record":
        parent = api.RunRecord.from_json(source["record_json"])
        if int(parent.data["state_size"]) != 3 or parent.data["topology"] != "triad": raise ValueError("Stored passive analysis requires an explicit triad record; no ring aggregate")
        samples = parent.data["samples"]
        sample_index = requests.integer(source["sample_index"], "sample ordinal")
        if sample_index >= len(samples): raise ValueError("Selected sample is outside parent record")
        sample = samples[sample_index]
        omega_text = [[repr(f64(p[k])) for k in ("re", "im")] for p in sample["omega"]]
        if "omega" in inputs: inputs["omega"] = omega_text
        if "state" in inputs: inputs["state"] = {"omega": omega_text, "update_index": sample["update_index"]}
        context["resolved_stored_state"] = {"omega": sample["omega"], "update_index": sample["update_index"]}
    def keys(value, expected):
        if not isinstance(value, dict) or set(value) != set(expected): raise ValueError("Missing or unsupported explicit analysis fields")
    def real(value, field): return requests.number(value, field)
    def vector(value):
        if not isinstance(value, list) or len(value) != 3: raise ValueError("Explicit vector requires three values")
        return [real(v, "vector") for v in value]
    def omega(value):
        if not isinstance(value, list) or any(not isinstance(p, list) or len(p) != 2 for p in value): raise ValueError("Explicit Omega pairs required")
        return tuple(complex(real(p[0], "Omega.re"), real(p[1], "Omega.im")) for p in value)
    def parameters(value):
        keys(value, ("eps", "g", "phase_strength", "k"))
        return api.Parameters(**{k: real(value[k], k) for k in ("eps", "g", "phase_strength")}, k=tuple(vector(value["k"])))
    def clock(value):
        keys(value, ("q", "N", "t", "q_step"))
        return api.Clock(**{k: real(v, "Clock.t") if k == "t" else requests.signed_integer(v, k) for k, v in value.items()})
    def memory(value):
        keys(value, ("m",)); return api.EMAState(m=real(value["m"], "memory.m"))
    if kind in requests.HISTORY_TYPES:
        if parent is None: raise ValueError("History requires a selected stored record")
        oid = inputs["observer_id"]
        if not isinstance(oid, str) or not oid or any(oid not in s["observer_results"] or oid not in s["observer_states"] for s in samples):
            raise ValueError("Selected observer history not recorded in every sample")
        sample_index = None
        context["sample_ordinals"] = list(range(len(samples)))
        if kind == "direct_history_coordinates":
            key = inputs["key"]
            if key not in ("Z_macro", "Z_chiral", "Z_total"): raise ValueError("Choose explicit Z_macro/Z_chiral/Z_total")
            history = {key: [[f64(v) for v in s["observer_results"][oid][key]] for s in samples]}
            context["stored_paths"] = [f"samples[*].observer_results.{oid}.{key}"]
            result = api.direct_history_coordinates(history, key=key)
        else:
            path = inputs["kappa_source"]
            if path not in requests.KAPPA_SOURCES: raise ValueError("Choose a supported recorded kappa source")
            diagnostic, field = path.split(".")
            if any(diagnostic not in s["diagnostics"] or field not in s["diagnostics"][diagnostic] for s in samples):
                raise ValueError("Kappa diagnostic source not recorded for every sample; no recomputation")
            values = [f64(s["diagnostics"][diagnostic][field]) for s in samples]
            if any(v < 0 for v in values): raise ValueError("Kappa display derivation requires nonnegative stored diagnostic values")
            history = {"kappa": [math.sqrt(v) for v in values],
                "z": [f64(s["observer_results"][oid]["z"]) for s in samples],
                "phi_index": [int(s["observer_states"][oid]["q"]) for s in samples]}
            context["display_derivation"] = "DISPLAY_DERIVATION_ONLY: sqrt(" + path + "); no physical amplitude interpretation"
            context["stored_paths"] = [f"samples[*].diagnostics.{path}", f"samples[*].observer_results.{oid}.z", f"samples[*].observer_states.{oid}.q"]
            N = requests.signed_integer(inputs["N"], "N")
            result = (api.cylinder_history_coordinates(history, N=N) if kind == "cylinder_history_coordinates" else
                api.history_torus_coordinates(history, N=N, R=real(inputs["R"], "R"), r_max=real(inputs["r_max"], "r_max")))
        context["assembled_history"] = lossless(history)
    elif kind == "step_preview":
        keys(inputs["state"], ("omega", "update_index"))
        result = api.step(api.State(omega=omega(inputs["state"]["omega"]), update_index=requests.integer(inputs["state"]["update_index"], "update_index")), parameters(inputs["parameters"]), topology=inputs["topology"])
    elif kind == "advance_clock": result = api.advance_clock(clock(inputs["clock"]), real(inputs["dt"], "dt"))
    elif kind == "advance_ema": result = api.advance_ema(omega(inputs["omega"]), memory(inputs["memory"]))
    elif kind in ("observe_staged", "observe_ema"):
        variant = kind[8:]; keys(inputs["config"], requests.CONFIG_FIELDS[variant])
        config = (api.StagedConfig if variant == "staged" else api.EMAConfig)(**{k: real(v, k) for k, v in inputs["config"].items()})
        args = (omega(inputs["omega"]), clock(inputs["clock"]), config)
        result = api.observe_staged(*args) if variant == "staged" else api.observe_ema(*args, memory(inputs["memory"]))
    elif kind == "quadratic_form": result = api.quadratic_form(vector(inputs["vector"]))
    elif kind == "readout_accounting":
        value = inputs["readout"]; keys(value, ("z", "Z_macro", "Z_chiral", "Z_total", "variant", "initialization"))
        readout = api.ZReadout(z=real(value["z"], "z"), **{k: vector(value[k]) for k in ("Z_macro", "Z_chiral", "Z_total")}, variant=value["variant"], initialization=value["initialization"])
        result = api.readout_accounting(readout, alpha=real(inputs["alpha"], "alpha"), beta=real(inputs["beta"], "beta"))
    elif kind == "chiral_area_accounting": result = api.chiral_area_accounting(omega(inputs["omega"]))
    elif kind == "intensity_budget": result = api.intensity_budget(omega(inputs["omega"]), parameters(inputs["parameters"]))
    elif kind == "potential": result = api.potential(omega(inputs["omega"]), parameters(inputs["parameters"]))
    elif kind == "historical_alignment": result = api.historical_alignment(*(vector(inputs[k]) for k in ("macro", "chiral", "total_vector")))
    elif kind == "cylinder_point": result = api.cylinder_point(real(inputs["kappa"], "kappa"), requests.signed_integer(inputs["q"], "q"), real(inputs["z"], "z"), N=requests.signed_integer(inputs["N"], "N"))
    else: raise ValueError("Unsupported passive analysis")
    return {"result_kind": "analysis", "analysis_type": kind, "parent_digest": parent.deterministic_sha256 if parent else None,
        "parent_source_commit": parent.data["implementation"]["commit"] if parent else None, "sample_index": sample_index,
        "inputs": lossless(context), "data": lossless(result),
        "qualification": "Detached current-public-API analysis. Parent record identity shown separately; current implementation identity is not independently exposed. Not a RunRecord, GeometryRecord or scientific replay certificate. Observer-vector coordinates — not physical placement. Step preview is not a recorded trajectory; standalone observe calls recompute their readout."}


def axial_analysis(kind, inputs, source):
    from trioctagon_ui.axial_identity import verify_installed_axial
    from trioctagon_ui.axial_inputs import resolve
    from trioctagon_ui import axial_artifacts
    identity = verify_installed_axial()  # Verify bytes before loading/calling science.
    from kernel_physics import api
    if api.AXIAL_OBSERVATION_API_VERSION != '1.0.0' or api.AXIAL_OBSERVER_REVISION != 'AXIAL_M1_V1':
        raise ValueError('Installed axial API/revision mismatch')
    parent = api.RunRecord.from_json(source['record_json']) if source['mode'] == 'record' else None
    if parent and parent.to_json() != source['record_json']:
        raise ValueError('Axial parent must be the canonical RunRecord bytes returned by the public loader')
    binding = resolve(kind, inputs, source, lossless(parent.data) if parent else None)
    resolved = binding['resolved_inputs_hex']
    def omega(state): return tuple(complex(f64(v['re']), f64(v['im'])) for v in state['omega'])
    def state(value): return api.State(omega=omega(value), update_index=value['update_index'])
    if kind == 'axial_snapshot': data = {'snapshot': lossless(api.axial_snapshot(omega(resolved['states'][0])))}
    elif kind == 'axial_history': data = {'snapshots': [lossless(api.axial_snapshot(omega(s))) for s in resolved['states']]}
    else:
        p = resolved['parameters']; states = resolved['states']
        parameters = api.Parameters(**{k: f64(p[k]) for k in ('eps', 'g', 'phase_strength')}, k=tuple(f64(v) for v in p['k']))
        result = api.axial_source_budget(state(states[0]), parameters, after=state(states[1]) if len(states) == 2 else None)
        status = 'RECORDED_ADJACENT_PAIR' if parent and len(states) == 2 else result.comparison_status
        data = {'budget': lossless(result), 'comparison_status': status, 'comparison_availability': binding['comparison_availability']}
    artifact = axial_artifacts.create(kind, binding, identity, data)
    return {'result_kind': 'analysis', 'analysis_type': kind,
        'parent_digest': parent.deterministic_sha256 if parent else None,
        'parent_source_commit': parent.data['implementation']['commit'] if parent else None,
        'sample_index': binding['selection'][0]['sample_ordinal'] if kind != 'axial_history' else None,
        'inputs': {'request': inputs, 'source': {k: v for k, v in source.items() if k != 'record_json'}},
        'data': artifact, 'qualification': axial_artifacts.QUALIFICATION}


def respond(envelope):
    response = {"ui_response_version": 2, "request_id": envelope.get("request_id"),
                "operation": envelope.get("operation"), "status": "failed"}
    try:
        response["result"] = execute(envelope)
        response["status"] = "completed"
    except Exception as exc:
        # Preserve the specific class, including ResponsePrecisionError before
        # any interpretation as a generic arithmetic failure. No fallback run.
        response["error"] = {"exception_class": type(exc).__name__, "message": str(exc),
                             "field_or_action": envelope.get("operation"), "traceback": traceback.format_exc()}
    response["imports"] = {"gui": sorted(n for n in sys.modules if n.startswith(("PySide6", "matplotlib"))),
                           "models": sorted(n for n in sys.modules if n.startswith(("torch", "tensorflow", "transformers")))}
    return response


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--response", type=Path, required=True)
    args = parser.parse_args(argv)
    attempts = []
    def audit(event, values):
        if event in ("socket.connect", "socket.getaddrinfo", "urllib.Request"):
            attempts.append(event)
            raise RuntimeError("Network is forbidden in the scientific worker")
    sys.addaudithook(audit)
    try:
        envelope = json.loads(args.request.read_text(encoding="utf-8"))
        if not isinstance(envelope, dict):
            raise ValueError("Request envelope must be an object")
        response = respond(envelope)
    except Exception as exc:
        response = {"ui_response_version": 2, "request_id": None, "operation": None, "status": "failed",
                    "error": {"exception_class": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}}
    response["runtime_network_attempts"] = attempts
    response["isolated"] = bool(sys.flags.isolated)
    if response["status"] != "completed":
        print(response["error"]["traceback"], file=sys.stderr)
    atomic_text(args.response, json.dumps(response, ensure_ascii=False, allow_nan=False))
    return 0 if response["status"] == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
