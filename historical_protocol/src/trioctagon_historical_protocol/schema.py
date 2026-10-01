"""Historical owning types reuse only the unchanged generic validation infrastructure."""
from datetime import datetime
import re

from trioctagon_analysis import schema as s
from trioctagon_analysis.errors import ProtocolError as GenericError
from .codec import canonical_bytes
from .digests import content_digest
from .errors import ProtocolError, require

PROFILE = "HISTORICAL"
CONTRACT = "H4_COMPATIBILITY_V1"
IMPLEMENTATION = "INDEPENDENT_HISTORICAL_REFERENCE_1"
PROTOCOL = {"family": "TRIOCTAGON_HISTORICAL_ANALYSIS_PROTOCOL", "version": 1}
protocol_schema = s.obj(family=s.literal(PROTOCOL["family"]), version=s.literal(1))
omega_schema = s.seq(s.obj(real=s.f64, imag=s.f64), 3, 3)
vector_schema = s.seq(s.f64, 3, 3)
mask_schema = s.seq(s.boolean, 3, 3)
attempt_schema = s.matching(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}")
ZERO = {"f64": "0x0.0p+0"}


def number(token):
    """Decode a validated token for domain/metadata comparisons, never scientific evaluation."""
    return float.fromhex(token["f64"])


def embedded(owner):
    def check(value, path, integers):
        owner.schema(value, path, integers)
        owner.validate(value)
    return check


def union(discriminator, owners):
    def check(value, path, integers):
        require(type(value) is dict and type(value.get(discriminator)) is str and value[discriminator] in owners)
        owners[value[discriminator]](value, path, integers)
    return check


def literal_tree(expected):
    """Closed, schema-owned literal tree, including each exact integer path."""
    if type(expected) is dict:
        return s.obj(**{key:literal_tree(value) for key,value in expected.items()})
    if type(expected) is list:
        validators=[literal_tree(value) for value in expected]
        def check(value,path,integers):
            require(type(value) is list and len(value)==len(validators))
            for i,validator in enumerate(validators):validator(value[i],(*path,i),integers)
        return check
    return s.literal(expected)


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(value)
        valid = parsed.tzinfo is not None and parsed.utcoffset() is not None
    except (ValueError, TypeError, OverflowError):
        valid = False
    require(valid, message="timezone-qualified ISO timestamp required")


def safe_members(rows, key="path"):
    paths = [r[key] for r in rows]
    require(paths == sorted(set(paths)) and len({p.casefold() for p in paths}) == len(paths),
            message="sorted, unique, case-disjoint inventory required")
    reserved = {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1,10)), *(f"LPT{i}" for i in range(1,10))}
    for path in paths:
        require(not path.startswith("/") and "\\" not in path and ":" not in path and
                all(part not in ("", ".", "..") and part == part.rstrip(" .") and
                    part.split(".")[0].upper() not in reserved and
                    not re.search(r'[\x00-\x1f<>"|?*]', part) for part in path.split("/")),
                message="safe relative inventory paths required")


def sorted_ids(rows):
    ids = [r["id"] for r in rows]
    require(ids == sorted(set(ids)), message="sorted unique identities required")


class Document(s.Document):
    """Immutable canonical claim. Construction/parsing never approves or executes it."""
    __slots__ = ()
    persisted = False

    def __init__(self, value):
        try:
            super().__init__(value)
        except GenericError as exc:
            raise ProtocolError(exc.category if exc.category in {"INVALID_CODEC", "INVALID_SCHEMA", "RESOURCE_LIMIT"}
                                else "INVALID_SCHEMA", str(exc)) from exc

    @classmethod
    def from_bytes(cls, raw, limits):
        try:
            obj = super().from_bytes(raw, limits)
        except GenericError as exc:
            raise ProtocolError(exc.category if exc.category in {"INVALID_CODEC", "INVALID_SCHEMA", "RESOURCE_LIMIT"}
                                else "INVALID_SCHEMA", str(exc)) from exc
        require(not cls.persisted or raw == obj.to_bytes(), "INVALID_CODEC", "persisted claim must be canonical")
        return obj

    @property
    def identity(self):
        return content_digest(self.digest_type, self.to_bytes())


def typed_bytes(value, validator):
    integers = set()
    validator(value, (), integers)
    return canonical_bytes(value, integer_paths=integers)


class HProtocol(Document):
    __slots__ = ()
    schema = staticmethod(protocol_schema)
