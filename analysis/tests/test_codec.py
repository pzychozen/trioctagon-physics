import json
from pathlib import Path

import pytest

from trioctagon_analysis.codec import ParseLimits, canonical_bytes, decode, validate_f64
from trioctagon_analysis.digests import *
from trioctagon_analysis.errors import ProtocolError

LIMITS = ParseLimits(100000, 32)

def test_canonical_golden_vectors():
    vectors = json.loads((Path(__file__).parent / "fixtures/golden_vectors.json").read_bytes())
    for row in vectors["codec"]:
        paths = {tuple(p) for p in row["integer_paths"]}
        expected = bytes.fromhex(row["canonical_hex"])
        assert canonical_bytes(row["value"], integer_paths=paths) == expected
        assert decode(expected, LIMITS, integer_paths=paths) == row["value"]
        assert not expected.startswith(b"\xef\xbb\xbf") and not expected.endswith(b"\n")
    kinds = {kind.scope: kind for kind in CONTENT_TYPES}
    for row in vectors["digests"]:
        kind = kinds[row["scope"]]
        raw = bytes.fromhex(row["canonical_hex"])
        assert preimage(kind, raw).hex() == row["preimage_hex"]
        assert content_digest(kind, raw).sha256 == row["sha256"]
    byte_kinds = {kind.scope: kind for kind in BYTE_TYPES}
    for row in vectors["raw_digests"]:
        assert byte_digest(byte_kinds[row["scope"]], bytes.fromhex(row["bytes_hex"])).sha256 == row["sha256"]

@pytest.mark.parametrize("raw", [
    b'{"x":1,"x":2}', b'{"v":1.0}', b'{"v":NaN}', b'{"v":Infinity}',
    b'{"x":"\\ud800"}', b'{"x":"\\udfff"}', b'"\xff"', b'\xef\xbb\xbf{}',
    b'{"x":1}', b'{"x":{"f64":"nan"}}', b'{"f64":"0x0p+0"}',
    b'{"f64":"0X0.0P+0"}', b'{"f64":"-inf"}', b'{"f64":"0x0.0p+0","extra":0}',
])
def test_invalid_codec_vectors(raw):
    with pytest.raises(ProtocolError):
        decode(raw, LIMITS)

def test_only_schema_typed_integers_no_bool_confusion():
    assert canonical_bytes({"ordinal": 7}, integer_paths={("ordinal",)}) == b'{"ordinal":7}'
    with pytest.raises(ProtocolError):
        canonical_bytes({"ordinal": 7})
    with pytest.raises(ProtocolError):
        canonical_bytes({"x": .5})
    with pytest.raises(ProtocolError):
        canonical_bytes({3: "not a string key"})

def test_signed_zero_and_subnormal_tokens_are_preserved():
    for token in ("0x0.0p+0", "-0x0.0p+0", "0x0.0000000000001p-1022"):
        value = {"f64": token}
        assert decode(canonical_bytes(value), LIMITS) == value

def test_parse_limits_before_loading_nested_json():
    with pytest.raises(ProtocolError, match="byte limit"):
        decode(b"[]", ParseLimits(1, 3))
    with pytest.raises(ProtocolError, match="depth limit"):
        decode(b"[[[[]]]]", ParseLimits(100, 3))
    assert decode(b'{"s":"[[[["}', ParseLimits(100, 1)) == {"s": "[[[["}

def test_digest_types_cannot_be_substituted_or_mutated():
    data = b""
    original = byte_digest(InputByteDigest, data)
    artifact = byte_digest(FullArtifactDigest, data)
    assert original.sha256 == artifact.sha256 and original != artifact
    with pytest.raises(ProtocolError):
        FullArtifactDigest.from_dict(original.to_dict())
    with pytest.raises(ProtocolError):
        content_digest(ParentSemanticDigest, b"{}")
    with pytest.raises(ProtocolError):
        byte_digest(RequestDigest, b"{}")
    with pytest.raises((AttributeError, TypeError)):
        original.scope = "FULL_ARTIFACT_DIGEST"
    assert ParentSemanticDigest("a" * 64).codec == "KERNEL_RUN_RECORD_1.0.0_NATIVE"

def test_all_canonical_hash_scopes_are_disjoint():
    assert len({content_digest(k, b"{}").sha256 for k in CONTENT_TYPES}) == len(CONTENT_TYPES)

def test_negative_integer_zero_not_silently_normalized():
    with pytest.raises(ProtocolError):
        decode(b'{"i":-0}', LIMITS, integer_paths={("i",)})
