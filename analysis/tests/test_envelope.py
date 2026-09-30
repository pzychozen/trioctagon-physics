"""UI-P0 inspection fixtures are claims, never production execution evidence."""
from dataclasses import FrozenInstanceError
import json
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

import pytest
import trioctagon_analysis
from trioctagon_analysis import (ArtifactEnvelopeHint, ArtifactFamilyHint,
    CanonicalParseState, probe_artifact_envelope)
from trioctagon_analysis.codec import ParseLimits
from trioctagon_analysis.coordinator import parse_request_or_receipt
from trioctagon_analysis.errors import ProtocolError
from trioctagon_analysis.records import DerivedAnalysisRecord, AttemptReceipt
from support import record_claim, core_bytes

# Approved viewer ceilings only, not provider execution limits.
VIEWER_LIMITS = ParseLimits(16 * 1024 * 1024, 32)
MAX_DISPLAY_DIAGNOSTIC_BYTES = 8 * 1024


def encoded(value):
    return json.dumps(value, separators=(",", ":"), sort_keys=True).encode()


def test_canonical_derived_receipt_catalogue_and_request_hints():
    record, _ = record_claim()
    receipt = parse_request_or_receipt(b'not JSON', VIEWER_LIMITS,
        attempt_id="TEST_ONLY_PROBE", diagnostic_limit=512)
    assert type(receipt) is AttemptReceipt
    for raw, family, profile in (
        (record.to_bytes(), ArtifactFamilyHint.TRIOCTAGON_DERIVED_ANALYSIS_RECORD, "CORE"),
        (receipt.to_bytes(), ArtifactFamilyHint.TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT, None),
        (encoded(record.to_dict()["catalogue"]), ArtifactFamilyHint.TRIOCTAGON_ANALYSIS_CATALOGUE, None),
        (encoded(record.to_dict()["request"]), ArtifactFamilyHint.TRIOCTAGON_ANALYSIS_REQUEST, "CORE"),
    ):
        hint = probe_artifact_envelope(raw, VIEWER_LIMITS)
        assert type(hint) is ArtifactEnvelopeHint
        assert (hint.family_hint, hint.schema_hint, hint.profile_hint_if_present) == (family, "1.0.0", profile)
        assert hint.canonical_parse_state is CanonicalParseState.PARSED_CANONICALITY_UNCHECKED


@pytest.mark.parametrize("family", ["KERNEL_RUN_RECORD", "GEOMETRY_RECORD"])
def test_core_discriminator_is_a_hint_not_core_validation(family):
    # Intentionally incomplete as a Core record: probing must not validate Core.
    raw = encoded({"record_type": family, "schema_version": "1.0.0"})
    assert probe_artifact_envelope(raw, VIEWER_LIMITS).family_hint.value == family
    assert probe_artifact_envelope(core_bytes(), VIEWER_LIMITS).family_hint is ArtifactFamilyHint.KERNEL_RUN_RECORD


@pytest.mark.parametrize("value", [{}, {"family": "FUTURE_RECORD"},
    {"record_type": "FUTURE_CORE_RECORD", "schema_version": "2.0.0"}])
def test_unknown_is_closed_and_does_not_return_arbitrary_identifiers(value):
    hint = probe_artifact_envelope(encoded(value), VIEWER_LIMITS)
    assert hint.family_hint is ArtifactFamilyHint.UNKNOWN
    assert not hasattr(hint, "__dict__")
    with pytest.raises((FrozenInstanceError, AttributeError)):
        hint.schema_hint = "9.9.9"


@pytest.mark.parametrize("value", [
    {"record_type": "KERNEL_RUN_RECORD", "family": "TRIOCTAGON_DERIVED_ANALYSIS_RECORD"},
    {"family": "KERNEL_RUN_RECORD"}, {"record_type": "TRIOCTAGON_ANALYSIS_REQUEST"},
    {"family": "TRIOCTAGON_ANALYSIS_REQUEST", "schema_version": "1.0.0"},
    {"record_type": "GEOMETRY_RECORD", "schema": "1.0.0"},
    {"schema": "1.0.0", "schema_version": "1.0.0"},
    {"family": ["TRIOCTAGON_ANALYSIS_REQUEST", "TRIOCTAGON_ANALYSIS_CATALOGUE"]},
    {"family": None}, {"family": True}, {"family": 1}, {"family": ""},
    {"family": "provider:execute"}, {"family": "A" * 129},
    {"profile": None}, {"profile": "core"}, {"family": "\\ud800"},
    {"schema": None}, {"schema": 1}, {"schema": True}, {"schema": "1"},
    {"schema": "01.0.0"}, {"schema": "1.0.0\n"}, {"schema": "1.0.0-beta"},
    {"schema": "1" * 65 + ".0.0"}, [], "not an object", None,
])
def test_malformed_or_conflicting_envelopes_rejected(value):
    with pytest.raises(ProtocolError) as caught:
        probe_artifact_envelope(encoded(value), VIEWER_LIMITS)
    assert caught.value.category == "INVALID_SCHEMA"
    assert len(str(caught.value).encode()) <= MAX_DISPLAY_DIAGNOSTIC_BYTES


@pytest.mark.parametrize("raw", [
    b'{"family":"A","family":"B"}', b'{"family":"A","family":"A"}',
    b'{"x":{"schema":"1.0.0","schema":"2.0.0"}}',
    b'\xef\xbb\xbf{}', b'{"family":"\xff"}', b'{"x":1.0}', b'{"x":1e0}',
    b'{"x":NaN}', b'{"x":Infinity}', b'{"x":-Infinity}', b'{"x":-0}', b'{',
])
def test_invalid_codec_input_uses_existing_parser(raw):
    with pytest.raises(ProtocolError) as caught:
        probe_artifact_envelope(raw, VIEWER_LIMITS)
    assert caught.value.category == "INVALID_CODEC"


def test_caller_limits_and_approved_viewer_boundaries():
    at_limit = b'{"padding":"' + b' ' * (VIEWER_LIMITS.max_bytes - 14) + b'"}'
    assert len(at_limit) == VIEWER_LIMITS.max_bytes
    assert probe_artifact_envelope(at_limit, VIEWER_LIMITS).family_hint is ArtifactFamilyHint.UNKNOWN
    with pytest.raises(ProtocolError, match="byte limit"):
        probe_artifact_envelope(at_limit + b' ', VIEWER_LIMITS)
    for depth in (32, 33):
        raw = b'{"x":' + b'[' * (depth - 1) + b'0' + b']' * (depth - 1) + b'}'
        if depth == 32:
            assert probe_artifact_envelope(raw, VIEWER_LIMITS).family_hint is ArtifactFamilyHint.UNKNOWN
        else:
            with pytest.raises(ProtocolError, match="depth limit"):
                probe_artifact_envelope(raw, VIEWER_LIMITS)
    assert probe_artifact_envelope(b'{"text":"[[[["}', ParseLimits(100, 1))
    for raw, limits in ((b'{}', None), ('{}', VIEWER_LIMITS), (bytearray(b'{}'), VIEWER_LIMITS)):
        with pytest.raises(ProtocolError): probe_artifact_envelope(raw, limits)
    for limits in ((0, 32), (16, 0), (True, 32)):
        with pytest.raises(ProtocolError): ParseLimits(*limits)


def test_unsupported_schema_and_profile_are_unvalidated_hints():
    raw = encoded({"family": "TRIOCTAGON_DERIVED_ANALYSIS_RECORD", "schema": "2.0.0", "profile": "HISTORICAL"})
    hint = probe_artifact_envelope(raw, VIEWER_LIMITS)
    assert hint.schema_hint == "2.0.0" and hint.profile_hint_if_present == "HISTORICAL"
    with pytest.raises(ProtocolError): DerivedAnalysisRecord.from_bytes(raw, VIEWER_LIMITS)


def test_noncanonical_input_never_becomes_validation_or_replacement_bytes():
    record, _ = record_claim()
    raw = json.dumps(record.to_dict(), indent=2).encode() + b'\n'
    before = bytes(raw)
    with patch.object(DerivedAnalysisRecord, "from_bytes", side_effect=AssertionError("strict loader invoked")), \
         patch.object(AttemptReceipt, "from_bytes", side_effect=AssertionError("strict loader invoked")):
        hint = probe_artifact_envelope(raw, VIEWER_LIMITS)
    assert hint.canonical_parse_state is CanonicalParseState.PARSED_CANONICALITY_UNCHECKED
    assert raw == before and not hasattr(hint, "canonical_bytes")
    # Existing strict codecs canonicalize; UI-P1 must additionally reject byte inequality.
    assert raw != DerivedAnalysisRecord.from_bytes(raw, VIEWER_LIMITS).to_bytes()
    damaged = record.to_dict(); damaged["semantic_result_digest"]["sha256"] = "0" * 64
    assert probe_artifact_envelope(encoded(damaged), VIEWER_LIMITS).family_hint == hint.family_hint
    with pytest.raises(ProtocolError): DerivedAnalysisRecord.from_bytes(encoded(damaged), VIEWER_LIMITS)


def test_probe_imports_and_effects_are_inert_in_fresh_interpreter():
    program = r'''
import importlib.abc, json, sys
sys.path.insert(0, sys.argv[1])
blocked = ('kernel_physics', 'trioctagon_ui', 'PySide6', 'trioctagon_analysis.provider',
    'trioctagon_analysis.coordinator', 'trioctagon_analysis.attestation', 'trioctagon_analysis.records',
    'trioctagon_analysis.b2a_worker', 'trioctagon_analysis.b2a_proof')
class Deny(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if any(fullname == n or fullname.startswith(n + '.') for n in blocked):
            raise AssertionError('forbidden import: ' + fullname)
sys.meta_path.insert(0, Deny())
def audit(event, values):
    if event.startswith('socket.') or event in ('urllib.Request', 'subprocess.Popen', 'os.system'):
        raise AssertionError('forbidden effect: ' + event)
sys.addaudithook(audit)
from trioctagon_analysis import probe_artifact_envelope, ArtifactFamilyHint
from trioctagon_analysis.codec import ParseLimits
payload = {'family':'TRIOCTAGON_DERIVED_ANALYSIS_RECORD','schema':'1.0.0',
    'provider':{'entry_point':'rogue.module:run'}, 'locator':'https://invalid.example/execute'}
hint = probe_artifact_envelope(json.dumps(payload).encode(), ParseLimits(16*1024*1024, 32))
assert hint.family_hint is ArtifactFamilyHint.TRIOCTAGON_DERIVED_ANALYSIS_RECORD
assert not any(n == p or n.startswith(p + '.') for n in sys.modules for p in blocked)
print('INERT_PROBE_PASS')
'''
    parent = str(Path(trioctagon_analysis.__file__).resolve().parent.parent)
    result = subprocess.run([sys.executable, '-I', '-B', '-c', program, parent],
                            capture_output=True, text=True, check=True, timeout=30)
    assert result.stdout.strip() == 'INERT_PROBE_PASS'
