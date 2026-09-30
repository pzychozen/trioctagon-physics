"""APP04 stored copy only. The sole kernel call is api.RunRecord.from_json."""
from dataclasses import dataclass
import copy

from . import schema as s
from .codec import ParseLimits, decode
from .common import embedded
from .constants import FIELDS, NUMERICAL, REPRODUCIBILITY, VECTOR_FIELDS
from .digests import (InputByteDigest, ParentCanonicalByteDigest, ParentSemanticDigest,
                      PayloadDigest, byte_digest, content_digest)
from .errors import ProtocolError, require
from .requests import ParentReference, Selection

@dataclass(frozen=True, slots=True)
class ParentLoadLimits:
    parsing: ParseLimits
    max_samples: int

    def __post_init__(self):
        require(type(self.parsing) is ParseLimits and type(self.max_samples) is int and
                self.max_samples > 0, "RESOURCE_LIMIT", "explicit finite parent limits required")

@dataclass(frozen=True, slots=True, init=False)
class ParentSnapshot:
    """Inert, publicly validated parent; NOT a producer or replay attestation."""
    original: bytes
    canonical: bytes
    reference: ParentReference

    def __init__(self, raw, limits):
        require(type(limits) is ParentLoadLimits, "RESOURCE_LIMIT", "ParentLoadLimits required")
        require(type(raw) is bytes, "WRONG_PARENT_FAMILY", "parent must be retained record bytes")
        data = decode(raw, limits.parsing)
        require(type(data) is dict and data.get("record_type") == "KERNEL_RUN_RECORD",
                "WRONG_PARENT_FAMILY", "APP04 requires a Core RunRecord")
        require(data.get("schema_version") == "1.0.0" and data.get("api_version") == "1.0.0",
                "PARENT_VALIDATION", "unsupported Core schema/API")
        require(data.get("topology") == "triad" and data.get("state_size") == "3",
                "WRONG_PARENT_FAMILY", "triad only; no three-state ring")
        samples = data.get("samples")
        require(type(samples) is list and len(samples) <= limits.max_samples,
                "RESOURCE_LIMIT", "sample inventory limit")
        try:
            from kernel_physics import api
            record = api.RunRecord.from_json(raw.decode("utf-8"))
        except (TypeError, ValueError, OverflowError, RecursionError) as exc:
            raise ProtocolError("PARENT_VALIDATION", "public RunRecord validation failed") from exc
        canonical = record.to_json().encode("utf-8")
        data = decode(canonical, limits.parsing)
        claims = copy.deepcopy(data["implementation"])
        reference = ParentReference({"role": "source", "family": "KERNEL_RUN_RECORD",
            "schema": "1.0.0", "semantic": ParentSemanticDigest(record.deterministic_sha256).to_dict(),
            "original_bytes": byte_digest(InputByteDigest, raw).to_dict(),
            "canonical_bytes": byte_digest(ParentCanonicalByteDigest, canonical).to_dict(),
            "source_claims": claims})
        object.__setattr__(self, "original", raw)
        object.__setattr__(self, "canonical", canonical)
        object.__setattr__(self, "reference", reference)

    def to_dict(self):
        # Owned, already validated canonical bytes; caller receives a detached tree.
        import json
        return json.loads(self.canonical)

    def require_reference(self, expected):
        require(type(expected) is ParentReference, "INVALID_SCHEMA", "typed parent reference required")
        actual, wanted = self.reference.to_dict(), expected.to_dict()
        for field, category in (
            ("semantic", "PARENT_SEMANTIC_MISMATCH"),
            ("original_bytes", "INPUT_BYTE_MISMATCH"),
            ("canonical_bytes", "PARENT_CANONICAL_MISMATCH"),
            ("source_claims", "PARENT_SEMANTIC_MISMATCH")):
            require(actual[field] == wanted[field], category, "bound parent identity differs: " + field)

def _numeric_value(value, path, integers):
    if type(value) is list:
        s.seq(s.f64, 3, 3)(value, path, integers)
    else:
        s.f64(value, path, integers)

def source_path(ordinal, field):
    if field == FIELDS[0]:
        suffix = "raw_readouts/z_chiral"
    else:
        suffix = "diagnostics/chiral_area_accounting/" + field[2:]
    return "/samples/" + str(ordinal) + "/" + suffix

class CopyPayload(s.Document):
    """Unattested data payload, never a successful analysis record by itself."""
    __slots__ = ()
    schema = s.obj(schema=s.literal("APP04_RECORDED_COPY_PAYLOAD_1"),
        ordinal=s.integer, update_index=s.counter, fields=s.seq(s.obj(
            field=s.enum(*FIELDS), source_path=s.text, value=_numeric_value), 1, 16),
        scientific_recomputation=s.literal("NOT_PERFORMED"),
        numerical=s.literal(NUMERICAL), reproducibility=s.literal(REPRODUCIBILITY))

    @classmethod
    def validate(cls, value):
        names = [row["field"] for row in value["fields"]]
        require(len(names) == len(set(names)), "FORBIDDEN_SELECTION", "duplicate result fields")
        for row in value["fields"]:
            require((type(row["value"]) is list) == (row["field"] in VECTOR_FIELDS),
                    "COPIED_VALUE_MISMATCH", "scalar/vector output shape mismatch")
            require(row["source_path"] == source_path(value["ordinal"], row["field"]),
                    "SAMPLE_INDEX_MISMATCH", "result path does not bind ordinal")

    @property
    def identity(self):
        return content_digest(PayloadDigest, self.to_bytes())

def copy_recorded(parent, selection):
    """Explicit low-level inspection; no record issuance and no scientific calls."""
    require(type(parent) is ParentSnapshot and type(selection) is Selection,
            "WRONG_PARENT_FAMILY", "validated immutable parent and typed selection required")
    data, chosen = parent.to_dict(), selection.to_dict()
    ordinal = chosen["ordinal"]
    require(ordinal < len(data["samples"]), "SAMPLE_INDEX_MISMATCH", "sample ordinal outside record")
    sample = data["samples"][ordinal]
    require(sample["update_index"] == chosen["expected_update_index"],
            "SAMPLE_INDEX_MISMATCH", "ordinal differs from expected stored update index")
    rows = []
    for field in chosen["fields"]:
        container = sample["raw_readouts"] if field == FIELDS[0] else sample["diagnostics"].get(
            "chiral_area_accounting", {})
        key = "z_chiral" if field == FIELDS[0] else field[2:]
        require(key in container, "MISSING_RECORDED_FIELD", "not recorded: " + field)
        rows.append({"field": field, "source_path": source_path(ordinal, field),
                     "value": copy.deepcopy(container[key])})
    return CopyPayload({"schema": "APP04_RECORDED_COPY_PAYLOAD_1", "ordinal": ordinal,
        "update_index": sample["update_index"], "fields": rows,
        "scientific_recomputation": "NOT_PERFORMED", "numerical": NUMERICAL,
        "reproducibility": REPRODUCIBILITY})

def verify_copy(payload, parent, selection):
    require(type(payload) is CopyPayload, "INVALID_SCHEMA", "typed copy payload required")
    expected = copy_recorded(parent, selection)
    require(payload.to_bytes() == expected.to_bytes(), "COPIED_VALUE_MISMATCH",
            "result tokens/selection differ from the stored parent")
