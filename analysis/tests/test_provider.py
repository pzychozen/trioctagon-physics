import copy
import json
from contextlib import ExitStack
from unittest.mock import patch

import pytest

from trioctagon_analysis.constants import FIELDS, VECTOR_FIELDS
from trioctagon_analysis.coordinator import attempt_inspection
from trioctagon_analysis.errors import ProtocolError
from trioctagon_analysis.provider import CopyPayload, ParentSnapshot, copy_recorded, verify_copy
from trioctagon_analysis.requests import Selection
from support import LIMITS, PARSING, context, core_bytes, core_data, raw_only, record_claim

def test_full_accounting_copy_field_order_and_exact_tokens():
    parent, request, *_ = context(fields=tuple(reversed(FIELDS)), ordinal=1, index="8")
    selection = Selection(request.to_dict()["selection"])
    result = copy_recorded(parent, selection)
    rows = result.to_dict()["fields"]
    assert [r["field"] for r in rows] == list(reversed(FIELDS))
    assert sum(3 if r["field"] in VECTOR_FIELDS else 1 for r in rows) == 20
    assert result.to_dict()["ordinal"] == 1 and result.to_dict()["update_index"] == "8"
    verify_copy(result, parent, selection)
    assert parent.original == core_bytes()

def test_raw_only_success_and_missing_diagnostic_refusal():
    parent, request, *_ = context(raw_only(), fields=(FIELDS[0],))
    result = copy_recorded(parent, Selection(request.to_dict()["selection"]))
    assert len(result.data["fields"]) == 1
    with pytest.raises(ProtocolError) as caught:
        copy_recorded(parent, Selection({"ordinal": 0, "expected_update_index": "7", "fields": ["D.chiral"]}))
    assert caught.value.category == "MISSING_RECORDED_FIELD"

def test_signed_zero_residual_sign_and_two_chirality_sources_are_not_reconciled():
    parent, request, *_ = context()
    rows = {r["field"]: r["value"] for r in copy_recorded(
        parent, Selection(request.to_dict()["selection"])).to_dict()["fields"]}
    assert rows["D.chiral"][0] == {"f64": "0x0.0p+0"}
    assert rows["D.chiral"][1] == {"f64": "-0x0.0p+0"}
    assert rows[FIELDS[0]][0] == {"f64": "-0x0.0p+0"}
    assert rows["D.gram_residual"] == {"f64": "-0x1.0000000000000p-40"}
    assert rows["D.slack_residual"] == {"f64": "0x1.0000000000000p-41"}

def test_old_source_is_distinct_from_selected_validator():
    parent, request, *_ = context()
    assert parent.reference.data["source_claims"]["commit"] != request.data["kernel"]["source_revision"]
    assert copy_recorded(parent, Selection(request.to_dict()["selection"]))

def test_pretty_printed_original_bytes_differ_canonical_parent_matches():
    compact, pretty = ParentSnapshot(core_bytes(), LIMITS), ParentSnapshot(core_bytes(pretty=True), LIMITS)
    assert compact.reference.data["semantic"] == pretty.reference.data["semantic"]
    assert compact.reference.data["canonical_bytes"] == pretty.reference.data["canonical_bytes"]
    assert compact.reference.data["original_bytes"] != pretty.reference.data["original_bytes"]

def test_environment_only_difference_native_digest_vs_complete_canonical_bytes():
    original = ParentSnapshot(core_bytes(), LIMITS)
    data = core_data()
    data["execution_metadata"][0]["platform"] = "TEST_ONLY_CHANGED_ENVIRONMENT"
    changed = ParentSnapshot(core_bytes(data), LIMITS)
    assert original.reference.data["semantic"] == changed.reference.data["semantic"]
    assert original.reference.data["canonical_bytes"] != changed.reference.data["canonical_bytes"]

def test_public_loader_only_no_scientific_calls_or_private_imports():
    from kernel_physics import api
    names = ("chiral_area_accounting", "z_chiral", "run", "step", "resume", "observe_staged",
             "observe_ema", "advance_clock", "advance_ema", "get_geometry", "historical_observer",
             "historical_seed", "readout_accounting", "intensity_budget", "potential")
    with ExitStack() as stack:
        forbidden = [stack.enter_context(patch.object(api, name, side_effect=AssertionError(name))) for name in names]
        public_load = stack.enter_context(patch.object(api.RunRecord, "from_json", wraps=api.RunRecord.from_json))
        parent, request, catalogue, approval, _ = context()
        payload = copy_recorded(parent, Selection(request.to_dict()["selection"]))
        assert payload.data["scientific_recomputation"] == "NOT_PERFORMED"
        public_load.assert_called_once()
        for mock in forbidden:
            mock.assert_not_called()

def test_inert_record_claim_roundtrip_and_parent_copy_verification():
    record, parent = record_claim()
    from trioctagon_analysis.records import DerivedAnalysisRecord
    decoded = DerivedAnalysisRecord.from_bytes(record.to_bytes(), PARSING)
    assert decoded.to_bytes() == record.to_bytes()
    decoded.verify_parent_copy(parent)
    assert decoded.data["producer"]["snapshot_id"] == "TEST_ONLY_NO_SNAPSHOT"

def test_nested_views_and_request_are_immutable_detached():
    parent, request, *_ = context()
    with pytest.raises((AttributeError, TypeError)):
        parent.canonical = b"changed"
    with pytest.raises(TypeError):
        request.data["selection"]["ordinal"] = 99
    altered = request.to_dict()
    altered["selection"]["fields"].clear()
    assert len(request.data["selection"]["fields"]) == 16
    with pytest.raises((AttributeError, TypeError)):
        request.extra = "not allowed"
