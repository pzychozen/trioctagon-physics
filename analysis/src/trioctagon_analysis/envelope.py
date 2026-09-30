"""Bounded envelope hints only; no artifact validation or executable dispatch."""
from dataclasses import dataclass
from enum import Enum
import re

from .codec import ParseLimits, _parse_json
from .errors import require


class ArtifactFamilyHint(str, Enum):
    UNKNOWN = "UNKNOWN"
    KERNEL_RUN_RECORD = "KERNEL_RUN_RECORD"
    GEOMETRY_RECORD = "GEOMETRY_RECORD"
    TRIOCTAGON_DERIVED_ANALYSIS_RECORD = "TRIOCTAGON_DERIVED_ANALYSIS_RECORD"
    TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT = "TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT"
    TRIOCTAGON_ANALYSIS_CATALOGUE = "TRIOCTAGON_ANALYSIS_CATALOGUE"
    TRIOCTAGON_ANALYSIS_REQUEST = "TRIOCTAGON_ANALYSIS_REQUEST"


class CanonicalParseState(str, Enum):
    PARSED_CANONICALITY_UNCHECKED = "PARSED_CANONICALITY_UNCHECKED"


@dataclass(frozen=True, slots=True)
class ArtifactEnvelopeHint:
    """Untrusted literal hints. No field attests validity, identity or execution."""
    family_hint: ArtifactFamilyHint
    schema_hint: str | None
    profile_hint_if_present: str | None
    canonical_parse_state: CanonicalParseState = CanonicalParseState.PARSED_CANONICALITY_UNCHECKED


_CORE = frozenset((ArtifactFamilyHint.KERNEL_RUN_RECORD, ArtifactFamilyHint.GEOMETRY_RECORD))
_KNOWN = {kind.value: kind for kind in ArtifactFamilyHint if kind is not ArtifactFamilyHint.UNKNOWN}


def _literal(value, label):
    require(type(value) is str and re.fullmatch(r"[A-Z][A-Z0-9_]{0,127}", value) is not None,
            "INVALID_SCHEMA", "malformed envelope " + label)
    return value


def probe_artifact_envelope(raw_bytes: bytes, limits: ParseLimits) -> ArtifactEnvelopeHint:
    """Inspect top-level discriminators through the existing bounded parser.

    ProtocolError rejects malformed/ambiguous envelopes. Unknown but well-formed
    families map to UNKNOWN. Schema versions are hints, not a support assertion.
    Nested schema-owned integers/tokens are left to strict family loaders. Even
    canonical input returns PARSED_CANONICALITY_UNCHECKED. No bytes are rewritten.
    """
    value = _parse_json(raw_bytes, limits)
    require(type(value) is dict, "INVALID_SCHEMA", "artifact envelope must be an object")
    core, analysis = "record_type" in value, "family" in value
    require(not (core and analysis), "INVALID_SCHEMA", "conflicting family discriminators")
    require(not ("schema" in value and "schema_version" in value),
            "INVALID_SCHEMA", "conflicting schema discriminators")
    require(not (core and "schema" in value) and not (analysis and "schema_version" in value),
            "INVALID_SCHEMA", "schema discriminator belongs to a different family mechanism")
    family = ArtifactFamilyHint.UNKNOWN
    if core or analysis:
        name = _literal(value["record_type" if core else "family"], "family")
        family = _KNOWN.get(name, ArtifactFamilyHint.UNKNOWN)
        require(family is ArtifactFamilyHint.UNKNOWN or (family in _CORE) == core,
                "INVALID_SCHEMA", "family uses the wrong discriminator")
    schema = None
    for key in ("schema", "schema_version"):
        if key in value:
            schema = value[key]
            require(type(schema) is str and len(schema) <= 64 and
                    re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", schema) is not None,
                    "INVALID_SCHEMA", "malformed envelope schema")
    profile = _literal(value["profile"], "profile") if "profile" in value else None
    return ArtifactEnvelopeHint(family, schema, profile)
