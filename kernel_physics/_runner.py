"""One recurrence, independent passive observers, and inert record assembly."""
from dataclasses import replace

from . import dynamics as _dynamics, readouts as _readouts, z_manifold as _z, z_diagnostics as _d
from ._contract_types import (State, Parameters, Clock, EMAState, ObserverRequest, Provenance,
                              _integer, _require, _topology, _values, _provenance_data)
from ._presets import historical_seed
from ._records import (RunRecord, _READOUTS, _DIAGNOSTICS, _OBSERVER_DIAGNOSTICS, _encode,
                       _signed, _implementation, _environment, _papers, _definition_ids,
                       _parse, _parameters, _config, _provenance, _complex, _f64, _int)


def _step(state, parameters, *, topology):
    _topology(state, topology)
    _require(parameters, Parameters, "parameters")
    advance = _dynamics.step3 if topology == "triad" else _dynamics.step_ring
    omega = advance(state.omega, parameters._native())
    return State(omega=omega, update_index=state.update_index + 1)


def _selection(values, allowed, name):
    if not isinstance(values, tuple):
        raise TypeError(f"{name} must be an explicit tuple")
    if any(not isinstance(value, str) for value in values):
        raise TypeError(f"{name} must contain strings")
    if any(value not in allowed for value in values) or len(values) != len(set(values)):
        raise ValueError(f"unknown or duplicate {name}")


def _descriptor(observer):
    return _encode({"observer_id": observer.observer_id, "variant": observer.variant,
                    "config": observer.config, **_values(observer.clock),
                    "m": None if observer.memory is None else observer.memory.m,
                    "dt": observer.dt, "initialization": observer.initialization,
                    "provenance": _provenance_data(observer.provenance)})


def _observe(state, observer, initial):
    if initial and observer.initialization == "historical_constructor_zero":
        return _z.historical_constructor_zero(
            state.omega, observer.clock._native(), observer.config._native()).readout
    if observer.variant == "staged":
        return _z.observe_staged(state.omega, observer.clock._native(), observer.config._native())
    return _z.observe_ema(state.omega, observer.clock._native(), observer.config._native(), observer.memory._native())


def _advance(state, observer):
    clock = Clock(**_values(_z.advance_clock(observer.clock._native(), observer.dt)))
    memory = observer.memory
    if memory is not None:
        memory = EMAState(m=_z.advance_ema(state.omega, memory._native()).m)
    return replace(observer, clock=clock, memory=memory, initialization="recomputed")


def _sample(state, parameters, observers, readouts, diagnostics, count, *, initial, results=None):
    if results is None:
        results = {observer.observer_id: _observe(state, observer, initial) for observer in observers}
    snapshot = {observer.observer_id: {
        "q": observer.clock.q, "t": observer.clock.t,
        "m": None if observer.memory is None else observer.memory.m,
        "observer_update_count": count} for observer in observers}
    raw = {name: _readouts.z_chiral(state.omega) for name in readouts}
    diagnostic_results = {}
    for name in diagnostics:
        if name == "chiral_area_accounting":
            value = _d.chiral_area_accounting(state.omega)
        elif name == "intensity_budget":
            value = _d.intensity_budget(state.omega, parameters._native())
        elif name == "potential":
            value = _d.potential(state.omega, parameters._native())
        elif name == "readout_accounting":
            value = {o.observer_id: _d.readout_accounting(results[o.observer_id], alpha=o.config.alpha,
                                                        beta=o.config.beta) for o in observers}
        else:
            value = {o.observer_id: _d.historical_alignment(results[o.observer_id].Z_macro,
                      results[o.observer_id].Z_chiral, results[o.observer_id].Z_total) for o in observers}
        diagnostic_results[name] = value
    return _encode({"update_index": state.update_index, "omega": state.omega,
                    "observer_states": snapshot, "raw_readouts": raw,
                    "observer_results": results, "diagnostics": diagnostic_results})


def _append(data, state, parameters, observers, updates):
    selection = data["selection"]
    count = len(data["samples"]) - 1
    for offset in range(1, updates + 1):
        state = _step(state, parameters, topology=data["topology"])
        advanced, results = [], {}
        for observer in observers:
            observer = _advance(state, observer)
            results[observer.observer_id] = _observe(state, observer, False)
            advanced.append(observer)
        observers = tuple(advanced)
        data["samples"].append(_sample(state, parameters, observers, selection["readouts"],
                                       selection["diagnostics"], count + offset, initial=False, results=results))
    return state


def run(initial_state: State, parameters: Parameters, *, topology: str, updates: int,
        parameter_provenance: Provenance, initialization_provenance: Provenance,
        observers: tuple, readouts: tuple, diagnostics: tuple) -> RunRecord:
    _topology(initial_state, topology)
    _require(parameters, Parameters, "parameters")
    updates = _integer(updates, "updates", minimum=0)
    _require(parameter_provenance, Provenance, "parameter_provenance")
    _require(initialization_provenance, Provenance, "initialization_provenance")
    _selection(readouts, _READOUTS, "readouts")
    _selection(diagnostics, _DIAGNOSTICS, "diagnostics")
    if not isinstance(observers, tuple):
        raise TypeError("observers must be an explicit tuple")
    for observer in observers:
        _require(observer, ObserverRequest, "observer")
        if observer.initialization == "historical_constructor_zero" and initial_state.update_index != 0:
            raise ValueError("constructor-zero requires update index zero")
        if observer.provenance.kind == "historical_preset" and observer.provenance.source_id not in (
                "paper_e_staged_v1", "paper_e_ema_v1"):
            raise ValueError("unknown historical observer provenance")
    ids = [o.observer_id for o in observers]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate observer IDs")
    if topology == "ring" and (observers or readouts or diagnostics):
        raise ValueError("ring observations are not supported in v1")
    if not observers and any(name in diagnostics for name in _OBSERVER_DIAGNOSTICS):
        raise ValueError("observer diagnostic requires an observer")
    init = {"kind": "explicit", "provenance": _provenance_data(initialization_provenance),
            "update_index": str(initial_state.update_index), "omega": _encode(initial_state.omega)}
    if initialization_provenance.kind == "historical_preset":
        seed = historical_seed(initialization_provenance.source_id)
        if _encode(seed.omega) != init["omega"]:
            raise ValueError("historical seed provenance does not match initial omega")
        init.update(kind="historical_seed", preset_id=seed.name)
    elif initialization_provenance.kind == "checkpoint":
        init["kind"] = "checkpoint"
    data = {"record_type": "KERNEL_RUN_RECORD", "schema_version": "1.0.0", "api_version": "1.0.0",
            "ledger_version": "0.1", "topology": topology, "state_size": str(len(initial_state.omega)),
            "parameters": _encode(parameters), "parameter_provenance": _provenance_data(parameter_provenance),
            "initialization": init, "selection": {"readouts": list(readouts), "diagnostics": list(diagnostics),
                                                   "observer_ids": ids},
            "observers": [_descriptor(observer) for observer in observers], "continuation": None,
            "implementation": _implementation()}
    data["definition_ids"] = _definition_ids(data)
    papers = {"A"}
    if "B01" in data["definition_ids"]:
        papers.update(("B", "E"))
    if observers or diagnostics:
        papers.add("E")
    if init["kind"] == "historical_seed":
        papers.add("F")
    data["paper_references"] = _papers(papers)
    data["samples"] = [_sample(initial_state, parameters, observers, readouts, diagnostics, 0, initial=True)]
    last = _append(data, initial_state, parameters, observers, updates)
    data["execution_metadata"] = [_environment(initial_state.update_index, last.update_index)]
    return RunRecord(_signed(data))


def resume(record: RunRecord, *, updates: int) -> RunRecord:
    _require(record, RunRecord, "record")
    updates = _integer(updates, "updates", minimum=0)
    data = _parse(RunRecord.from_json(record.to_json()).to_json())
    implementation = _implementation()
    if any(data["implementation"][key] != implementation[key] for key in ("commit", "modules")):
        raise ValueError("resume requires matching source revision and module hashes; start a checkpoint run")
    last = data["samples"][-1]
    state = State(omega=[_complex(v) for v in last["omega"]], update_index=_int(last["update_index"]))
    observers = []
    for descriptor in data["observers"]:
        snapshot = last["observer_states"][descriptor["observer_id"]]
        observers.append(ObserverRequest(observer_id=descriptor["observer_id"],
            config=_config(descriptor["config"], descriptor["variant"]),
            clock=Clock(q=_int(snapshot["q"]), N=_int(descriptor["N"]), t=_f64(snapshot["t"]),
                        q_step=_int(descriptor["q_step"])),
            memory=None if snapshot["m"] is None else EMAState(m=_f64(snapshot["m"])),
            dt=_f64(descriptor["dt"]), initialization="recomputed", provenance=_provenance(descriptor["provenance"])))
    data["continuation"] = {"parent_digest": record.deterministic_sha256, "junction_index": str(state.update_index)}
    final = _append(data, state, _parameters(data["parameters"]), tuple(observers), updates)
    data["execution_metadata"].append(_environment(state.update_index, final.update_index))
    return RunRecord(_signed(data))
