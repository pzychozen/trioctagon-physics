"""TRIOCTAGON_CANONICAL_JSON_1. See SPECIFICATION.md for exact bytes."""
from dataclasses import dataclass
import json
import math

from .errors import ProtocolError, require

CODEC = "TRIOCTAGON_CANONICAL_JSON_1"

@dataclass(frozen=True, slots=True)
class ParseLimits:
    """Caller-selected parsing budget; there is no default production policy."""
    max_bytes: int
    max_depth: int

    def __post_init__(self):
        require(all(type(v) is int and v > 0 for v in (self.max_bytes, self.max_depth)),
                "RESOURCE_LIMIT", "finite positive parser limits required")

def validate_f64(value):
    require(type(value) is dict and set(value) == {"f64"} and type(value["f64"]) is str,
            "INVALID_CODEC", "expected exact f64 tag")
    try:
        number = float.fromhex(value["f64"])
        valid = math.isfinite(number) and number.hex() == value["f64"]
    except (ValueError, OverflowError):
        valid = False
    require(valid, "INVALID_CODEC", "noncanonical or nonfinite f64 token")

def _string(value):
    require(not any(0xD800 <= ord(c) <= 0xDFFF for c in value),
            "INVALID_CODEC", "unpaired Unicode surrogate")

def _walk(value, path, integer_paths):
    if value is None or type(value) is bool:
        return
    if type(value) is str:
        _string(value)
    elif type(value) is int:
        require(path in integer_paths, "INVALID_CODEC", "untyped JSON integer: " + repr(path))
    elif type(value) is list:
        for i, item in enumerate(value):
            _walk(item, (*path, i), integer_paths)
    elif type(value) is dict:
        require(all(type(k) is str for k in value), "INVALID_CODEC", "object keys must be strings")
        for key in value:
            _string(key)
        if "f64" in value:
            validate_f64(value)
        for key, item in value.items():
            _walk(item, (*path, key), integer_paths)
    else:
        raise ProtocolError("INVALID_CODEC", "unsupported value type; JSON floats prohibited")

def canonical_bytes(value, *, integer_paths=()):
    """Integers require explicit schema-owned paths, never automatic discovery."""
    try:
        _walk(value, (), frozenset(integer_paths))
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                          allow_nan=False).encode("utf-8")
    except (RecursionError, UnicodeError, OverflowError) as exc:
        raise ProtocolError("INVALID_CODEC", "unencodable canonical value") from exc

def _parse_json(raw, limits):
    """Internal parser: owning schemas must validate integer types before encoding."""
    require(type(raw) is bytes and isinstance(limits, ParseLimits),
            "INVALID_CODEC", "bytes and explicit ParseLimits required")
    require(len(raw) <= limits.max_bytes, "RESOURCE_LIMIT", "input byte limit")
    require(not raw.startswith(b"\xef\xbb\xbf"), "INVALID_CODEC", "UTF-8 BOM prohibited")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError as exc:
        raise ProtocolError("INVALID_CODEC", "invalid UTF-8") from exc
    # Bound nesting BEFORE json.loads; braces in escaped strings are not containers.
    depth = 0
    quoted = escaped = False
    for c in text:
        if quoted:
            if escaped:
                escaped = False
            elif c == "\\":
                escaped = True
            elif c == '"':
                quoted = False
        elif c == '"':
            quoted = True
        elif c in "[{":
            depth += 1
            require(depth <= limits.max_depth, "RESOURCE_LIMIT", "JSON depth limit")
        elif c in "]}":
            depth -= 1
    def pairs(items):
        result = {}
        for key, item in items:
            require(key not in result, "INVALID_CODEC", "duplicate object key")
            result[key] = item
        return result
    def no_number(token):
        raise ProtocolError("INVALID_CODEC", "JSON float/nonfinite number prohibited")
    def integer_token(token):
        require(token != "-0", "INVALID_CODEC", "negative zero requires an f64 tag")
        return int(token)
    try:
        return json.loads(text, object_pairs_hook=pairs, parse_float=no_number,
                          parse_constant=no_number, parse_int=integer_token)
    except (ValueError, RecursionError) as exc:
        if isinstance(exc, ProtocolError):
            raise
        raise ProtocolError("INVALID_CODEC", "invalid JSON") from exc

def decode(raw, limits, *, integer_paths=()):
    value = _parse_json(raw, limits)
    canonical_bytes(value, integer_paths=integer_paths)
    return value
