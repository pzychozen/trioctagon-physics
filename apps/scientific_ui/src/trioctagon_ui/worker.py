"""Installed, GUI-free scientific boundary. All scientific calls use the facade."""
import argparse
import json
from pathlib import Path
import sys
import traceback

from trioctagon_ui import requests
from trioctagon_ui.record_views import atomic_text, f64, kernel_lock


def execute(envelope):
    requests.validate_envelope(envelope)
    from kernel_physics import api
    payload, operation = envelope["payload"], envelope["operation"]

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
            if payload["observer_reset"] != "reinitialize_named":
                raise ValueError("Checkpoint requires explicit reinitialize_named observer policy")
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
                notes=notes + "\nNew run from checkpoint; named observers explicitly reinitialized.")
        observers = tuple(api.historical_observer(name) for name in resolved["observers"])
        return api.run(initial, parameters, topology="triad", updates=int(resolved["updates"]),
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
        keys(("definition_id", "s"))
        if payload["definition_id"] == "C01":
            if payload["s"] is not None:
                raise ValueError("C01 accepts no editable s")
            record = api.get_geometry("C01", options={"section_heights": []})
        elif payload["definition_id"] == "D03":
            record = api.get_geometry("D03", options={"construction": "regular", "s": requests.rational(payload["s"])})
        else:
            raise ValueError("K4b geometry requires C01 or D03 regular")
    canonical = record.to_json()
    # Completion requires the public loader, as well as successful production.
    checked = load(canonical)
    data = checked.data
    produced = operation != "load_record"
    if produced and data["implementation"]["commit"] != kernel_lock()["source_commit"]:
        raise ValueError("Current kernel source does not match the selected certified artifact lock")
    return {"canonical_json": canonical, "record_type": data["record_type"],
            "deterministic_sha256": checked.deterministic_sha256,
            "source_commit": data["implementation"]["commit"], "produced_current": produced}


def respond(envelope):
    response = {"ui_response_version": 1, "request_id": envelope.get("request_id"),
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
        response = {"ui_response_version": 1, "request_id": None, "operation": None, "status": "failed",
                    "error": {"exception_class": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}}
    response["runtime_network_attempts"] = attempts
    response["isolated"] = bool(sys.flags.isolated)
    if response["status"] != "completed":
        print(response["error"]["traceback"], file=sys.stderr)
    atomic_text(args.response, json.dumps(response, ensure_ascii=False, allow_nan=False))
    return 0 if response["status"] == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
