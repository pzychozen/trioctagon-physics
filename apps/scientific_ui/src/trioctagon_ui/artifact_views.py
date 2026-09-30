"""Immutable presentation adapters for documents validated by their owning codec."""
from dataclasses import asdict, dataclass, field
from .artifact_loading import LoadedAttemptArtifact, bounded_text
from .record_views import freeze

QUALIFICATION = ("Artifact structure and internal digest bindings are valid.\n"
    "Producer verification claims are present in the saved artifact (CLAIMED_ONLY).\n"
    "This viewer has not independently verified the producer's execution (UNAVAILABLE).\n"
    "Production execution verification unavailable.\n"
    "Windows execution binding has not been proven for this provider lane (NOT_PROVEN).")


def integrity(item):
    return {"selected_local_file": str(item.source), "observed_complete_artifact_sha256": item.sha256,
        "external_expected_sha256": item.external_expected_sha256 or "UNAVAILABLE — not supplied",
        "external_identity_source": item.external_identity_source or "UNAVAILABLE",
        "canonical_equality": "PASS — exact original bytes retained",
        "viewer_loader_identity": asdict(item.loader)}


@dataclass(frozen=True)
class DerivedArtifactView:
    artifact: object
    panels: object = field(init=False)
    tokens: tuple = field(init=False)
    heading: str = "Derived analysis record — stored artifact inspection"
    qualification: str = QUALIFICATION

    def __post_init__(self):
        if isinstance(self.artifact, LoadedAttemptArtifact):
            raise TypeError("A receipt is not a scientific result")
        data = self.artifact.document.to_dict()
        request, producer = data["request"], data["producer"]
        descriptor = data["catalogue"]["descriptors"][0]
        panels = {
            "Identity": {**{k: data[k] for k in ("family", "profile", "schema")},
                **{k: request[k] for k in ("operation", "revision", "catalogue", "descriptor")},
                "request_identity": data["request_digest"]},
            "Parent": {"reference": data["parents"][0], "selection": request["selection"],
                "availability": "UNAVAILABLE — parent not loaded or resolved by this viewer"},
            "Producer": {"provider": request["provider"], "analysis_build": producer["build"],
                "environment": producer["environment"], "attestor_claim": producer["attestor_build"],
                "recorded_verification_vector": producer["checks"], "recorded_evidence": producer,
                "viewer_independent_verification": "UNAVAILABLE", "claim_status": "CLAIMED_ONLY"},
            "Participating kernel": {"selection": producer["kernel"], "roles": producer["kernel_roles"],
                "scientific_recomputation": producer["scientific_recomputation"]},
            "Authority / scientific meaning": {"descriptor": descriptor,
                **{k: data[k] for k in ("authority", "statuses", "qualification", "reproducibility")},
                "numerical_policy": data["result"]["numerical"]},
            "Integrity": {"semantic_result_digest": data["semantic_result_digest"],
                "completion_claim": data["completion"], **integrity(self.artifact)},
        }
        tokens = []
        for row in data["result"]["fields"]:
            vector = isinstance(row["value"], list)
            values = row["value"] if vector else [row["value"]]
            for axis, value in enumerate(values):
                tokens.append((row["field"], str(axis) if vector else "", row["source_path"], value["f64"]))
        object.__setattr__(self, "panels", freeze(panels))
        object.__setattr__(self, "tokens", tuple(tokens))

    @property
    def sample_summary(self):
        parent = self.panels["Parent"]
        return bounded_text("Recorded selected-sample Core data\nScientific recomputation: none\n"
            f"Parent native semantic SHA-256: {parent['reference']['semantic']['sha256']}\n"
            f"Sample ordinal: {parent['selection']['ordinal']}\n"
            f"Stored update index: {parent['selection']['expected_update_index']}\n"
            "Producer execution verification: unavailable in this viewer")

    def rows(self, precision=17):
        if type(precision) is not int or not 1 <= precision <= 17:
            raise ValueError("Display precision must be between 1 and 17")
        # Decode only the stored token; perform no scientific arithmetic.
        return tuple((*row, format(float.fromhex(row[3]), f".{precision}g")) for row in self.tokens)


@dataclass(frozen=True)
class AttemptReceiptView:
    artifact: LoadedAttemptArtifact
    panels: object = field(init=False)
    heading: str = field(init=False)
    qualification: str = ("A receipt records a refused, failed or cancelled attempt; it is not a scientific result.\n"
        "Production execution verification unavailable. Windows execution binding NOT_PROVEN.")

    def __post_init__(self):
        data = self.artifact.document.to_dict()
        diagnostic = bounded_text(data.pop("diagnostic"))
        object.__setattr__(self, "heading", "Analysis attempt receipt — " + data["outcome"])
        object.__setattr__(self, "panels", freeze({"Attempt": data, "Diagnostic": diagnostic,
            "Integrity": integrity(self.artifact)}))
