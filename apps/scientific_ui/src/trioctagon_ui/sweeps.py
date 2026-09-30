"""Finite explicit request enumeration and sequential dataset orchestration."""
from copy import deepcopy
from decimal import Decimal, localcontext, ROUND_HALF_EVEN
import hashlib
import itertools
import json
import math
from pathlib import Path

from PySide6.QtCore import QObject, QTimer, Signal
from trioctagon_ui import requests
from trioctagon_ui.record_views import atomic_text

DIMENSIONS = ("eps", "g", "phase_strength", "k0", "k1", "k2")
DEFAULT_CASE_GUARD = 10_000
STATUSES = ("pending", "running", "completed", "failed", "cancelled", "not_run")


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def expand_dimension(spec):
    """Decimal precision 50, half-even; endpoint spellings retained verbatim."""
    if not isinstance(spec, dict): raise ValueError("Dimension requires an explicit list or range object")
    if set(spec) == {"values"}:
        values = spec["values"]
        if not isinstance(values, list) or not values: raise ValueError("Explicit value list must be nonempty")
        values = values[:]
    elif set(spec) == {"start", "stop", "count"}:
        count = requests.integer(spec["count"], "range count")
        if count < 2: raise ValueError("Range count must be >=2; use an explicit list for one value")
        if count > 100_000: raise ValueError("Range expansion UI RESOURCE GUARD: 100000 values; use smaller explicit plans")
        for key in ("start", "stop"): requests.number(spec[key], key)
        with localcontext() as ctx:
            ctx.prec = 50; ctx.rounding = ROUND_HALF_EVEN
            start, stop = Decimal(spec["start"]), Decimal(spec["stop"])
            values = [spec["start"]] + [str(start + (stop - start) * Decimal(i) / Decimal(count - 1)) for i in range(1, count - 1)] + [spec["stop"]]
    else: raise ValueError("Use {values:[text,...]} or {start:text,stop:text,count:text}")
    rows = []; prior = {}
    for ordinal, text in enumerate(values):
        resolved = requests.number(text, "sweep value").hex()
        rows.append({"ordinal": ordinal, "text": text, "f64": resolved, "same_binary64_as": prior.get(resolved)})
        prior.setdefault(resolved, ordinal)
    return rows


def request_identity(envelope):
    return digest({"operation": envelope["operation"], **envelope["payload"]})


def case_request(base, substituted):
    draft = deepcopy(base)
    for name in DIMENSIONS:
        if name not in substituted: continue
        text = substituted[name]
        old = draft["k"][int(name[1])] if name.startswith("k") else draft[name]
        if text != old: draft = requests.mark_edited(draft, "k" if name.startswith("k") else name)
        if name.startswith("k"): draft["k"][int(name[1])] = text
        else: draft[name] = text
    return requests.run_request(draft)


def make_plan(base, dimensions, lock, *, stop_after_failure=False, case_guard=DEFAULT_CASE_GUARD, override_ack=False):
    requests.resolve_draft(base)
    if not isinstance(dimensions, dict) or not dimensions or set(dimensions) - set(DIMENSIONS):
        raise ValueError("Select one or more of eps, g, phase_strength, k0, k1, k2 only")
    if type(stop_after_failure) is not bool or type(override_ack) is not bool: raise ValueError("Explicit boolean orchestration policy required")
    if type(case_guard) is not int or case_guard < 1 or case_guard > 100_000:
        raise ValueError("UI RESOURCE GUARD must be an explicit integer in 1..100000; not scientific domain")
    if case_guard > DEFAULT_CASE_GUARD and not override_ack: raise ValueError("Explicitly acknowledge resource-guard override")
    expanded = {name: expand_dimension(dimensions[name]) for name in DIMENSIONS if name in dimensions}
    count = math.prod(len(rows) for rows in expanded.values())
    if count > case_guard: raise ValueError(f"UI RESOURCE GUARD exceeded: {count} cases > {case_guard}; explicitly increase the guard and acknowledge")
    samples = count * (int(base["updates"]) + 1)
    specification = {"base_draft": deepcopy(base), "dimensions": deepcopy(dimensions), "expanded": expanded,
        "kernel_identity": deepcopy(lock), "stop_after_failure": stop_after_failure,
        "case_guard": case_guard, "override_ack": override_ack,
        "range_policy": "Decimal precision=50, ROUND_HALF_EVEN; start+(stop-start)*i/(count-1); both literal endpoints retained"}
    cases = []
    for ordinal, selected in enumerate(itertools.product(*expanded.values()), 1):
        values = {name: row["text"] for name, row in zip(expanded, selected)}
        resolved = {name: row["f64"] for name, row in zip(expanded, selected)}
        request_sha = request_identity(case_request(base, values))
        cases.append({"case_id": f"case-{ordinal:06d}-{request_sha[:12]}", "request_sha256": request_sha,
            "substituted_values": values, "resolved_values": resolved, "status": "pending",
            "record_path": None, "record_digest": None, "record_source_commit": None, "error": None, "requires_rerun_reason": None})
    return {"manifest_type": "TRIOCTAGON_UI_SWEEP_MANIFEST", "manifest_version": 1, "app_version": "0.1.1",
        "spec_sha256": digest(specification), "specification": specification,
        "fixed_configuration": {k: deepcopy(base[k]) for k in ("topology", "updates", "observers", "readouts", "diagnostics")},
        "case_count": count, "total_requested_samples": samples,
        "confirmation_required": count > 100 or samples > 100_000, "cases": cases}


def validate_manifest(value):
    if not isinstance(value, dict): raise ValueError("Manifest must be an object")
    spec = value["specification"]
    expected = make_plan(spec["base_draft"], spec["dimensions"], spec["kernel_identity"],
        stop_after_failure=spec["stop_after_failure"], case_guard=spec["case_guard"], override_ack=spec["override_ack"])
    if set(value) != set(expected) or any(value[k] != expected[k] for k in expected if k != "cases"):
        raise ValueError("Sweep specification identity mismatch")
    if len(value["cases"]) != len(expected["cases"]): raise ValueError("Every requested case must remain represented")
    fixed = ("case_id", "request_sha256", "substituted_values", "resolved_values")
    for current, planned in zip(value["cases"], expected["cases"]):
        if set(current) != set(planned) or any(current[k] != planned[k] for k in fixed) or current["status"] not in STATUSES:
            raise ValueError("Sweep case request identity/status mismatch")
        if current["record_path"] is not None:
            path = Path(current["record_path"])
            if path.is_absolute() or path.parts[0] != "records" or ".." in path.parts or len(path.parts) != 2:
                raise ValueError("Record path must be a relative file under records/")
    return deepcopy(value)


def save_manifest(directory, manifest):
    atomic_text(Path(directory) / "sweep-manifest.json", canonical(manifest))


def load_manifest(path):
    return validate_manifest(json.loads(Path(path).read_text(encoding="utf-8")))


def record_matches_request(record, envelope, expected_source):
    """Representation checks only, after the worker's public record loader."""
    draft, resolved = envelope["payload"]["draft"], envelope["payload"]["resolved"]
    if record["record_type"] != "KERNEL_RUN_RECORD" or record["implementation"]["commit"] != expected_source:
        raise ValueError("Record type/source differs from dataset kernel identity")
    if record["continuation"] is not None or record["topology"] != resolved["topology"] or int(record["state_size"]) != len(resolved["omega"]):
        raise ValueError("Record topology/size or continuation differs from independent case request")
    expected_parameters = {k: {"f64": resolved[k]} for k in ("eps", "g", "phase_strength")}
    expected_parameters["k"] = [{"f64": v} for v in resolved["k"]]
    expected_omega = [{"re": {"f64": p[0]}, "im": {"f64": p[1]}} for p in resolved["omega"]]
    if record["parameters"] != expected_parameters or record["initialization"]["omega"] != expected_omega or record["initialization"]["update_index"] != resolved["update_index"]:
        raise ValueError("Record parameter or initial-state request mismatch")
    samples = record["samples"]
    if len(samples) != int(resolved["updates"]) + 1 or [int(s["update_index"]) for s in samples] != list(range(int(resolved["update_index"]), int(resolved["update_index"]) + len(samples))):
        raise ValueError("Record sample range differs from requested updates")
    literal = record["parameter_provenance"]["literal_values"]
    wanted = {k: draft[k] for k in ("eps", "g", "phase_strength", "updates", "update_index")}
    wanted.update({f"k{i}": v for i, v in enumerate(draft["k"])})
    wanted.update({f"Omega{i}.{p}": v for i, pair in enumerate(draft["omega"]) for p, v in zip(("re", "im"), pair)})
    if literal != wanted: raise ValueError("Record literal request identity mismatch")
    if bool(draft["origin"]["parameters"]) != (record["parameter_provenance"]["kind"] == "historical_preset"):
        raise ValueError("Record parameter provenance mismatch")
    user = draft["provenance"]
    notes = user["notes"] + "\n" + "\n".join(draft["origin"]["changes"])
    user_provenance = {**user, "kind": "user_supplied", "literal_values": wanted, "notes": notes}
    expected_provenance = user_provenance
    if draft["origin"]["parameters"] == "L01":
        expected_provenance = {"kind": "historical_preset", "source_id": "L01", "source_revision": requests.help_data()["source_commit"],
            "locator": "K0 ledger L01", "literal_values": wanted, "notes": notes + "\nReference fill; original rationale O02 unresolved."}
    if record["parameter_provenance"] != expected_provenance: raise ValueError("Record visible parameter provenance request mismatch")
    seed = draft["origin"]["seed"]
    if seed:
        if record["initialization"].get("preset_id") != seed or record["initialization"]["provenance"]["source_id"] != seed:
            raise ValueError("Record historical seed identity mismatch")
    elif record["initialization"]["provenance"] != user_provenance:
        raise ValueError("Record initialization provenance request mismatch")
    selection = record["selection"]
    if sorted(selection["readouts"]) != sorted(draft["readouts"]) or sorted(selection["diagnostics"]) != sorted(draft["diagnostics"]):
        raise ValueError("Record output selection mismatch")
    observers = {o["observer_id"]: o for o in record["observers"]}
    if set(observers) != {o["observer_id"] for o in resolved["observers"]}: raise ValueError("Record observer selection mismatch")
    for original in draft["observers"]:
        value = requests.preset_to_custom(original) if original["mode"] == "preset" else original
        explicit = requests.resolve_observer(value); stored = observers[explicit["observer_id"]]
        expected = {"variant": value["variant"], "initialization": value["initialization"], "dt": {"f64": explicit["dt"]},
            "config": {k: {"f64": v} for k, v in explicit["config"].items()},
            "m": None if explicit["memory"] is None else {"f64": explicit["memory"]["m"]},
            **{k: {"f64": v} if k == "t" else v for k, v in explicit["clock"].items()}}
        if any(stored[k] != v for k, v in expected.items()): raise ValueError("Record observer clock/config/memory request mismatch")
        if original["mode"] == "custom":
            literals = {k: value[k] for k in ("observer_id", "variant", "initialization", "dt")}
            literals.update({"clock." + k: v for k, v in value["clock"].items()})
            literals.update({"config." + k: v for k, v in value["config"].items()})
            if value["memory"] is not None: literals["memory.m"] = value["memory"]["m"]
            provenance = {**value["provenance"], "kind": "user_supplied", "literal_values": literals,
                "notes": value["provenance"]["notes"] + ("\nHistorical origin: " + value["origin"] if value["origin"] else "")}
            if stored["provenance"] != provenance: raise ValueError("Record visible observer provenance request mismatch")
        elif stored["provenance"]["kind"] != "historical_preset" or stored["provenance"]["source_id"] != original["name"]:
            raise ValueError("Record observer preset provenance mismatch")
    return True


class SweepController(QObject):
    """One JobManager; validate old records before skipping, never infer science."""
    changed = Signal()
    finished = Signal()
    record_ready = Signal(dict)
    persistence_failed = Signal(dict)

    def __init__(self, jobs, parent=None):
        super().__init__(parent)
        self.jobs = jobs; self.manifest = None; self.directory = None; self.active = False
        self.phase = None; self.index = None; self.queue = []; self.owned = set(); self.cancel_requested = False
        jobs.completed.connect(self._completed); jobs.failed.connect(self._failed); jobs.cancelled.connect(self._cancelled)

    def handles(self, request_id): return request_id in self.owned

    def create(self, manifest, directory):
        if self.active or self.jobs.busy: raise ValueError("Wait for the active scientific job")
        directory = Path(directory).resolve()
        if directory.exists() and any(directory.iterdir()): raise ValueError("A new dataset requires an empty chosen directory")
        directory.mkdir(parents=True, exist_ok=True); (directory / "records").mkdir(exist_ok=True)
        self.manifest = validate_manifest(manifest); self.directory = directory
        if not self._persist(): raise OSError("Dataset manifest could not be persisted; no scientific worker started")

    def load(self, path):
        if self.active or self.jobs.busy: raise ValueError("Wait for the active scientific job")
        self.manifest = load_manifest(path); self.directory = Path(path).resolve().parent
        self.changed.emit()

    def _persist(self):
        try: save_manifest(self.directory, self.manifest)
        except Exception as exc:
            self.active = False; self.queue.clear()
            self.persistence_failed.emit({"exception_class": type(exc).__name__, "message": str(exc), "operation": "dataset manifest persistence",
                "qualification": "Sweep stopped. Existing manifest and completed records preserved; explicitly reload/continue to validate any orphan record."})
            self.changed.emit(); self.finished.emit(); return False
        self.changed.emit(); return True

    def start(self, *, confirmed=False):
        if self.active or self.jobs.busy or self.manifest is None: raise ValueError("Dataset is unavailable or a worker is active")
        if self.manifest["confirmation_required"] and not confirmed: raise ValueError("Confirm application safeguard: >100 cases or >100000 samples")
        validate_manifest(self.manifest)
        self.active = True; self.cancel_requested = False
        self.queue = list(range(len(self.manifest["cases"]))); self.index = None
        self.changed.emit(); QTimer.singleShot(0, self._next)

    def _candidate(self, case):
        if case["record_path"]:
            path = (self.directory / case["record_path"]).resolve()
            if not path.is_relative_to((self.directory / "records").resolve()): raise ValueError("Dataset record path escaped records directory")
            if not path.is_file(): raise ValueError("Previously completed record is missing; rerun required")
            return path
        files = list((self.directory / "records").glob(case["case_id"] + "-*.json"))
        if len(files) > 1: raise ValueError("Multiple orphan records require explicit rerun; none skipped by filename")
        if files:
            path = files[0].resolve()
            if not path.is_relative_to((self.directory / "records").resolve()): raise ValueError("Orphan record path escaped dataset")
            return path
        if case["status"] == "completed": raise ValueError("Completed record path missing; rerun required")
        return None

    def _next(self):
        if not self.active: return
        if self.cancel_requested: self._finish_cancel(); return
        if not self.queue:
            self.active = False; self.index = None; self.changed.emit(); self.finished.emit(); return
        self.index = self.queue.pop(0); case = self.manifest["cases"][self.index]
        try:
            candidate = self._candidate(case)
            if candidate is not None:
                self.phase = "verify"; self.candidate = candidate
                self._submit(requests.request("load_record", {"record_json": candidate.read_text(encoding="utf-8")})); return
        except (ValueError, OSError) as exc:
            case["requires_rerun_reason"] = str(exc); case["status"] = "pending"
            if not self._persist(): return
        self._run_case()

    def _submit(self, envelope):
        self.owned.add(envelope["request_id"])
        try: self.jobs.start(envelope)
        except Exception as exc: self._failed({"exception_class": type(exc).__name__, "message": str(exc), "request_id": envelope["request_id"]})

    def _run_case(self):
        if self.cancel_requested: self._finish_cancel(); return
        case = self.manifest["cases"][self.index]
        self.phase = "run"; case["status"] = "running"; case["error"] = None
        if not self._persist(): return
        self._submit(case_request(self.manifest["specification"]["base_draft"], case["substituted_values"]))

    def _completed(self, response):
        if not self.active or not self.handles(response.get("request_id")): return
        case = self.manifest["cases"][self.index]
        try:
            result = response["result"]; data = json.loads(result["canonical_json"])
            request = case_request(self.manifest["specification"]["base_draft"], case["substituted_values"])
            if request_identity(request) != case["request_sha256"]: raise ValueError("Case request digest mismatch")
            record_matches_request(data, request, self.manifest["specification"]["kernel_identity"]["source_commit"])
            if self.phase == "verify":
                if case["record_digest"] is not None and (case["record_digest"] != result["deterministic_sha256"] or case["record_source_commit"] != result["source_commit"]):
                    raise ValueError("Previously completed record digest/source mismatch; rerun required")
                path = self.candidate
            else:
                path = self.directory / "records" / (case["case_id"] + "-" + result["deterministic_sha256"] + ".json")
                atomic_text(path, result["canonical_json"])
            case.update(status="completed", record_path=path.relative_to(self.directory).as_posix(),
                record_digest=result["deterministic_sha256"], record_source_commit=result["source_commit"], error=None)
            if not self._persist(): return
            self.record_ready.emit(response)
        except Exception as exc:
            self._failed({"exception_class": type(exc).__name__, "message": str(exc), "request_id": response["request_id"]}); return
        QTimer.singleShot(0, self._next)

    def _failed(self, error):
        if not self.active or not self.handles(error.get("request_id")): return
        case = self.manifest["cases"][self.index]
        if self.phase == "verify":
            case.update(status="pending", requires_rerun_reason=error["message"])
            if not self._persist(): return
            QTimer.singleShot(0, self._run_case); return
        case.update(status="failed", error={"exception_class": error["exception_class"], "message": error["message"], "request_sha256": case["request_sha256"]})
        if self.manifest["specification"]["stop_after_failure"]:
            for index in self.queue:
                if self.manifest["cases"][index]["status"] != "completed": self.manifest["cases"][index]["status"] = "not_run"
            self.queue.clear()
        if self._persist(): QTimer.singleShot(0, self._next)

    def cancel(self):
        if not self.active: return
        self.cancel_requested = True
        if self.jobs.busy: self.jobs.cancel()
        else: self._finish_cancel()

    def _cancelled(self):
        if self.active: self.cancel_requested = True; self._finish_cancel()

    def _finish_cancel(self):
        if self.index is not None:
            case = self.manifest["cases"][self.index]
            if case["status"] != "completed": case["status"] = "cancelled"
        for index in self.queue:
            case = self.manifest["cases"][index]
            if case["status"] != "completed": case["status"] = "not_run"
        self.queue.clear(); self.active = False; self.index = None
        if self._persist(): self.finished.emit()
