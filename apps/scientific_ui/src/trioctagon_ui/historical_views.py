"""Presentation of strictly validated Historical bytes; no scientific arithmetic."""
from collections.abc import Mapping
from dataclasses import dataclass, field

from .artifact_loading import bounded_text
from .artifact_views import integrity
from .historical_loading import LoadedHistoricalResult, LoadedHistoricalReceipt
from .record_views import freeze

ASSURANCE = (
    "A. Artifact structure / integrity: schema and internal bindings valid; exact canonical bytes retained.\n"
    "B. Mathematical reconstruction: ORIGINAL ARTIFACT CLAIM; equations have not been replayed by this viewer.\n"
    "C. Producer execution attestation: UNAVAILABLE. WINDOWS EXECUTION BINDING = NOT PROVEN.\n"
    "PRODUCTION ATTESTATION = NOT ENABLED. Parsing does not authenticate execution or historical authorship, "
    "establish physical validation, or prove production TORMENT execution. LOCAL_CHECK_PASSED is not VERIFIED."
)
OPERATION_SCHEMAS = {
    "historical.triad.step.inspect": "H_STEP_1",
    "historical.triad.run.inspect": "H_RUN_1",
    "historical.readout.staged_z.inspect": "H_STAGED_1",
    "historical.readout.ema_z.inspect": "H_EMA_1",
    "historical.probability_chart.inspect": "H_CHART_1",
}


def stored_rows(value, precision=17, path=""):
    """Flatten owned data for display. Only f64 decoding/decimal formatting occurs."""
    if type(precision) is not int or not 1 <= precision <= 17:
        raise ValueError("Display precision must be between 1 and 17")
    if isinstance(value, Mapping):
        if set(value) == {"f64"}:
            token = value["f64"]
            yield path, token, format(float.fromhex(token), f".{precision}g")
        else:
            for key, child in value.items():
                yield from stored_rows(child, precision, f"{path}.{key}" if path else key)
    elif isinstance(value, (tuple, list)):
        labels = {"C": ("23", "31", "12"), "chart": ("cu", "cx", "cy")}.get(path.split(".")[-1])
        for i, child in enumerate(value):
            label = labels[i] if labels else str(i + 1)
            yield from stored_rows(child, precision, f"{path}[{label}]")
        if not value:
            yield path, "[]", ""
    else:
        yield path, bounded_text("null" if value is None else value), ""


def observations(item, *, result):
    return {**integrity(item), "schema_valid": True,
        "semantic_digest_matches": True if result else "NOT_APPLICABLE — receipt",
        "authority_context": "MATCHES_PINNED_PROTOCOL" if result else "RECEIPT_SCHEMA_ONLY",
        "provider_build": "STRUCTURALLY_BOUND_IF_PRESENT; execution not authenticated",
        "equations_replayed": False, "producer_execution_attestation": "UNAVAILABLE",
        "historical_authorship_authenticated": False, "physical_validation": "NONE",
        "production_attestation_enabled": False, "windows_execution_binding": "NOT_PROVEN"}


@dataclass(frozen=True)
class HistoricalResultView:
    artifact: object
    panels: object = field(init=False)
    payload: object = field(init=False)
    values: object = field(init=False)
    qualification_fields: object = field(init=False)
    summary: str = field(init=False)
    note: str = field(init=False)
    heading: str = "HISTORICAL MATHEMATICAL RECONSTRUCTION"
    qualification: str = ASSURANCE

    def __post_init__(self):
        if type(self.artifact) is not LoadedHistoricalResult:
            raise TypeError("Historical result inspector requires a Historical result handle")
        data = self.artifact.document.to_dict()
        payload = data["payload"]
        operation = payload["operation"]
        if OPERATION_SCHEMAS.get(operation) != payload["schema"] or payload["revision"] != 1:
            raise ValueError("Unsupported Historical operation/revision")
        request = data["request"]["body"]
        identity = {"operation": operation, "revision": payload["revision"], "profile": data["profile"],
            "compatibility_contract": data["contract"], "issuance_class": data["issuance_class"],
            "independent_provider": data["provider_binding"], "historical_authority": payload["authority_digest"],
            "k_profile": payload.get("k_profile", "NOT_APPLICABLE"), "numerical_policy": payload["numerical_policy"],
            "semantic_result_identity": data["semantic_result_digest"]}
        summary = (f"{operation}@{payload['revision']} · {data['profile']} · {data['contract']} · {data['issuance_class']}\n"
            f"Provider: {request['provider']['id']}@{request['provider']['revision']} · k: {identity['k_profile']}\n"
            f"Numerical policy: {payload['numerical_policy']}\n"
            f"Semantic result: {data['semantic_result_digest']['sha256']}")
        note = "Exact binary64 tokens are authoritative. Decimal values are display approximations only. Ω components are ordered 1, 2, 3."
        if payload["schema"] == "H_STEP_1":
            note += " Harmonic = 3; phase strength = .001; update count = 1."
        if payload["schema"] == "H_RUN_1":
            summary += (f"\nRequested updates: {payload['requested_updates']} · completed: {payload['completed_updates']} · "
                f"rows: {payload['row_count']} · readout: {payload['readout_profile']}")
            note += " Rows are 0…N−1. Terminal is separate. HISTORICAL_CONSTRUCTOR_ZERO denotes cached constructor values; RECOMPUTED denotes the recorded readout marker."
            if not payload["rows"]:
                note += " N=0: no rows; terminal is constructor state."
        if payload["schema"] in ("H_STAGED_1", "H_EMA_1", "H_RUN_1"):
            note += " Raw C pair order is 23,31,12; C is not physical XYZ."
        if payload["schema"] in ("H_STAGED_1", "H_EMA_1"):
            note += " RECOMPUTED · USER_SUPPLIED_CLOCK."
        if payload["schema"] == "H_EMA_1":
            note += (" Memory input == memory output (exact stored token equality); memory update count = 0. "
                "NO MEMORY ADVANCE OCCURRED. SUPPLIED_MEMORY_NOT_HISTORY_VERIFIED. Detached numeric EMA variable; not application/TORMENT memory.")
        if payload["schema"] == "H_CHART_1":
            note += " Ordered chart (cu, cx, cy); not spatial XYZ. Stored weights and underflow flags are displayed without recomputation."
        panels = {"Historical identity": identity,
            "ORIGINAL ARTIFACT CLAIMS": {k: data[k] for k in ("assurance", "execution_evidence", "provider_binding", "contract_bundle", "completion", "metadata", "request")},
            "CURRENT VIEWER OBSERVATIONS": observations(self.artifact, result=True)}
        excluded = {"rows", "terminal", "qualifications", "provider_binding", "authority_digest", "operation", "revision", "schema", "numerical_policy"}
        for name, value in (("payload", payload), ("values", {k:v for k,v in payload.items() if k not in excluded}),
                            ("panels", panels), ("qualification_fields", data["qualifications"])):
            object.__setattr__(self, name, freeze(value))
        object.__setattr__(self, "summary", bounded_text(summary))
        object.__setattr__(self, "note", note)

    @property
    def run_rows(self):
        return self.payload.get("rows", ())

    @property
    def terminal(self):
        return self.payload.get("terminal")


@dataclass(frozen=True)
class HistoricalReceiptView:
    artifact: object
    panels: object = field(init=False)
    values: object = field(init=False)
    summary: str = field(init=False)
    heading: str = "HISTORICAL ATTEMPT RECEIPT — NOT A SCIENTIFIC RESULT"
    qualification: str = ("Artifact structure / integrity: receipt schema valid. Mathematical reconstruction: NOT A RESULT.\n"
        "Producer execution attestation: UNAVAILABLE. WINDOWS EXECUTION BINDING = NOT PROVEN.\n"
        "PRODUCTION ATTESTATION = NOT ENABLED. Parsing authenticates neither producer execution nor historical authorship; "
        "it establishes no physical validation or production execution. LOCAL_CHECK_PASSED is not VERIFIED.")

    def __post_init__(self):
        if type(self.artifact) is not LoadedHistoricalReceipt:
            raise TypeError("Historical receipt inspector requires a Historical receipt handle")
        data = self.artifact.document.to_dict()
        fields = ("outcome", "stage", "category", "argument_field", "updates_completed", "diagnostic", "provider", "checks", "staging", "request_digest")
        values = {k: bounded_text(data[k]) if k == "diagnostic" else data[k] for k in fields}
        object.__setattr__(self, "values", freeze(values))
        object.__setattr__(self, "summary", f"{data['outcome']} · {data['stage']} · {data['category']} · staging: {data['staging']}")
        object.__setattr__(self, "panels", freeze({"ORIGINAL ARTIFACT CLAIMS": data,
            "CURRENT VIEWER OBSERVATIONS": observations(self.artifact, result=False)}))
