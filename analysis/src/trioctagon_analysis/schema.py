"""Small closed validators; no user callbacks or dynamic schema/operation loading."""
from dataclasses import dataclass
import json
import re
from types import MappingProxyType

from .codec import _parse_json, canonical_bytes, validate_f64
from .errors import require

def text(value, path, integers):
    require(type(value) is str and bool(value), "INVALID_SCHEMA", "nonempty string at " + repr(path))

def integer(value, path, integers):
    require(type(value) is int and value >= 0, "INVALID_SCHEMA", "nonnegative integer at " + repr(path))
    integers.add(path)

def boolean(value, path, integers):
    require(type(value) is bool, "INVALID_SCHEMA", "boolean required at " + repr(path))

def positive(value, path, integers):
    integer(value, path, integers)
    require(value > 0, "INVALID_SCHEMA", "positive integer required")

def literal(expected):
    def check(value, path, integers):
        require(type(value) is type(expected) and value == expected, "INVALID_SCHEMA",
                "literal mismatch at " + repr(path))
        if type(expected) is int:
            integers.add(path)
    return check

def enum(*choices):
    def check(value, path, integers):
        text(value, path, integers)
        require(value in choices, "INVALID_SCHEMA", "unknown discriminator at " + repr(path))
    return check

def matching(pattern):
    def check(value, path, integers):
        text(value, path, integers)
        require(re.fullmatch(pattern, value) is not None, "INVALID_SCHEMA", "invalid string at " + repr(path))
    return check

hex256 = matching(r"[0-9a-f]{64}")
revision = matching(r"[0-9a-f]{40}|[0-9a-f]{64}")
counter = matching(r"0|[1-9][0-9]*")

def obj(**fields):
    def check(value, path, integers):
        require(type(value) is dict and set(value) == set(fields), "INVALID_SCHEMA",
                "missing/unknown fields at " + repr(path))
        for key, validator in fields.items():
            validator(value[key], (*path, key), integers)
    return check

def seq(item, minimum=0, maximum=None):
    def check(value, path, integers):
        require(type(value) is list and len(value) >= minimum and
                (maximum is None or len(value) <= maximum), "INVALID_SCHEMA", "invalid array at " + repr(path))
        for index, child in enumerate(value):
            item(child, (*path, index), integers)
    return check

def nullable(validator):
    def check(value, path, integers):
        if value is not None:
            validator(value, path, integers)
    return check

def digest(kind):
    def check(value, path, integers):
        kind.from_dict(value)
    return check

def f64(value, path, integers):
    validate_f64(value)

def freeze(value):
    if type(value) is dict:
        return MappingProxyType({k: freeze(v) for k, v in value.items()})
    if type(value) is list:
        return tuple(freeze(v) for v in value)
    return value

@dataclass(frozen=True, slots=True, init=False)
class Document:
    """Immutable canonical bytes. Parsing validates claims, never authenticates them."""
    _raw: bytes

    def __init__(self, value):
        integers = set()
        type(self).schema(value, (), integers)
        type(self).validate(value)
        object.__setattr__(self, "_raw", canonical_bytes(value, integer_paths=integers))

    @classmethod
    def validate(cls, value):
        pass

    @classmethod
    def from_bytes(cls, raw, limits):
        return cls(_parse_json(raw, limits))

    def to_bytes(self):
        return self._raw

    def to_dict(self):
        return json.loads(self._raw)

    @property
    def data(self):
        return freeze(self.to_dict())
