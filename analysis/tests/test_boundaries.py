"""A0 N01-N30: B1 conformance. OS/snapshot enforcement itself is deferred to B2."""
import ast
import copy
import inspect
import json
from pathlib import Path
from unittest.mock import patch

import pytest

from trioctagon_analysis import coordinator
from trioctagon_analysis.approval import ApprovalRoot
from trioctagon_analysis.attestation import CHECKS, ProducerEvidence, unavailable_evidence
from trioctagon_analysis.catalogue import Catalogue, Descriptor
from trioctagon_analysis.codec import canonical_bytes
from trioctagon_analysis.common import ResourcePolicy
from trioctagon_analysis.coordinator import attempt_inspection, parse_request_or_receipt
from trioctagon_analysis.digests import *
from trioctagon_analysis.errors import ProtocolError
from trioctagon_analysis.provider import CopyPayload, ParentSnapshot, copy_recorded, verify_copy
from trioctagon_analysis.records import AttemptReceipt, DerivedAnalysisRecord, semantic_result_digest
from trioctagon_analysis.requests import ParentReference, Request, Selection
from support import *

def refused(call, category=None):
    with pytest.raises(ProtocolError) as error:
        call()
    if category:
        assert error.value.category == category
    return error.value

def attempt(ctx, raw=None, **changes):
    parent, request, catalogue, approval, _ = ctx
    return attempt_inspection(request, catalogue, approval, parent.original if raw is None else raw,
        limits=LIMITS, attempt_id="TEST_ONLY_ATTEMPT", diagnostic_limit=512, **changes)

@pytest.mark.parametrize("family", ["KERNEL_GEOMETRY_RECORD", "TRIOCTAGON_DERIVED_ANALYSIS_RECORD",
                                  "TRIOCTAGON_EXPERIMENTAL_RECORD"])
def test_N01_wrong_parent_family(family):
    value = core_data()
    value["record_type"] = family
    refused(lambda: ParentSnapshot(core_bytes(value), LIMITS), "WRONG_PARENT_FAMILY")
    refused(lambda: copy_recorded({}, Selection({"ordinal": 0, "expected_update_index": "7", "fields": ["D.A"]})),
            "WRONG_PARENT_FAMILY")

@pytest.mark.parametrize("key,value", [("schema_version", "2.0.0"), ("api_version", "9"),
                                       ("topology", "ring")])
def test_N02_unsupported_schema_and_three_state_ring(key, value):
    data = core_data()
    data[key] = value
    refused(lambda: ParentSnapshot(core_bytes(data), LIMITS))

def test_N03_altered_original_bytes():
    parent, request, *_ = context()
    changed = ParentSnapshot(core_bytes(pretty=True), LIMITS)
    refused(lambda: changed.require_reference(ParentReference(request.to_dict()["parents"][0])),
            "INPUT_BYTE_MISMATCH")

def test_N04_environment_only_alteration_caught_by_canonical_scope():
    parent, request, *_ = context()
    data = core_data()
    data["execution_metadata"][0]["platform"] = "TEST_ONLY_CHANGE"
    changed = ParentSnapshot(core_bytes(data), LIMITS)
    expected = parent.reference.to_dict()
    expected["original_bytes"] = changed.reference.to_dict()["original_bytes"]
    refused(lambda: changed.require_reference(ParentReference(expected)), "PARENT_CANONICAL_MISMATCH")

def test_N05_wrong_native_semantic_identity():
    parent, *_ = context()
    expected = parent.reference.to_dict()
    expected["semantic"] = named(ParentSemanticDigest, "wrong-semantic")
    refused(lambda: parent.require_reference(ParentReference(expected)), "PARENT_SEMANTIC_MISMATCH")
    data = core_data()
    data["deterministic_sha256"] = "0" * 64
    refused(lambda: ParentSnapshot(json.dumps(data).encode(), LIMITS), "PARENT_VALIDATION")

def test_N06_wrong_producer_even_when_version_matches():
    record, _ = record_claim()
    value = record.to_dict()
    value["producer"]["build"]["source"]["revision"] = "f" * 40
    refused(lambda: DerivedAnalysisRecord(value), "WRONG_PRODUCER")

def test_N07_unverified_producer_no_production_success_even_with_mock_claims():
    ctx = context()
    receipt = attempt(ctx)
    assert type(receipt) is AttemptReceipt
    assert receipt.data["category"] == "B1_VERIFIED_LANE_DISABLED"
    assert receipt.data["producer"]["checks"]["execution_snapshot_bound"]["state"] == "UNAVAILABLE"
    assert "attestor" not in inspect.signature(attempt_inspection).parameters
    record, _ = record_claim()
    value = record.to_dict()
    value["producer"]["checks"]["execution_snapshot_bound"]["state"] = "UNAVAILABLE"
    refused(lambda: DerivedAnalysisRecord(value), "UNVERIFIED_PRODUCER")

@pytest.mark.parametrize("field,value", [("operation", "core.app04.recompute"), ("revision", 2)])
def test_N08_unsupported_operation_revision(field, value):
    _, request, *_ = context()
    data = request.to_dict()
    data[field] = value
    refused(lambda: Request(data))

def test_N09_unsupported_provider_or_build():
    _, request, catalogue, approval, _ = context()
    data = request.to_dict()
    data["provider"]["build"] = named(ProducerBuildIdentity, "unknown")
    refused(lambda: Request(data).validate_context(catalogue, approval), "UNSUPPORTED_PROVIDER")
    data["provider"]["id"] = "historical.arbitrary_plugin"
    refused(lambda: Request(data))

def test_N10_mismatched_authority_catalogue_and_request_status_override():
    _, request, catalogue, approval, _ = context()
    data = request.to_dict()
    data["catalogue"] = named(CatalogueDigest, "other-catalogue")
    refused(lambda: Request(data).validate_context(catalogue, approval), "AUTHORITY_MISMATCH")
    data = catalogue.descriptor.to_dict()
    data["authority"][0]["sha256"] = "f" * 64
    refused(lambda: Descriptor(data), "AUTHORITY_MISMATCH")
    data = request.to_dict()
    data["status"] = "CURRENT_ACCEPTED_MATH"
    refused(lambda: Request(data))

def test_N11_external_data_is_not_accepted_or_looked_up():
    _, request, *_ = context()
    data = request.to_dict()
    data["external_inputs"] = ["missing.csv"]
    refused(lambda: Request(data))

@pytest.mark.parametrize("ordinal,index", [(0, "0"), (1, "7"), (2, "9")])
def test_N12_ordinal_expected_index_mismatch(ordinal, index):
    ctx = context(ordinal=ordinal, index=index)
    receipt = attempt(ctx)
    assert receipt.data["category"] == "SAMPLE_INDEX_MISMATCH"

@pytest.mark.parametrize("ordinal", [-1, True, 1.5])
def test_N12_invalid_selector_types(ordinal):
    refused(lambda: Selection({"ordinal": ordinal, "expected_update_index": "7", "fields": ["D.A"]}))

def test_N13_missing_requested_field_receipt_no_subset_or_substitution():
    ctx = context(raw_only(), fields=("S.raw_readouts.z_chiral", "D.chiral"))
    receipt = attempt(ctx)
    assert type(receipt) is AttemptReceipt and receipt.data["category"] == "MISSING_RECORDED_FIELD"
    assert receipt.data["staging"] == "NOT_CREATED"
    assert receipt.data["checks"]["inputs_verified"]["state"] == "VERIFIED"
    data = core_data()
    del data["samples"][0]["diagnostics"]["chiral_area_accounting"]["h"]
    refused(lambda: ParentSnapshot(core_bytes(data), LIMITS), "PARENT_VALIDATION")

@pytest.mark.parametrize("fields", [["D.*"], ["D.A", "D.A"], ["D.chiral[0]"],
                                    ["S.observer_results.Z_chiral"], []])
def test_N14_forbidden_field_wildcard_component_or_duplicate(fields):
    refused(lambda: Selection({"ordinal": 0, "expected_update_index": "7", "fields": fields}))

def test_N15_historical_provider_under_core():
    _, request, *_ = context()
    value = request.to_dict()
    value["provider"]["id"] = "historical.M09"
    refused(lambda: Request(value))
    record, _ = record_claim()
    value = record.to_dict()
    value["producer"]["build"]["provider_id"] = "historical.M09"
    refused(lambda: DerivedAnalysisRecord(value))

@pytest.mark.parametrize("profile", ["HISTORICAL", "EXPERIMENTAL_ANALYSIS", "EXPERIMENTAL"])
def test_N16_experimental_or_historical_result_masquerading_as_core(profile):
    record, _ = record_claim()
    value = record.to_dict()
    value["profile"] = profile
    refused(lambda: DerivedAnalysisRecord(value))

def test_N17_immutable_parent_and_detached_views():
    parent, request, *_ = context()
    before = parent.original, parent.canonical
    value = parent.to_dict()
    value["samples"][0]["diagnostics"].clear()
    assert (parent.original, parent.canonical) == before
    with pytest.raises((TypeError, AttributeError)):
        parent.reference = request
    assert copy_recorded(parent, Selection(request.to_dict()["selection"]))

def test_N18_no_implicit_recompute_fallback():
    from kernel_physics import api
    ctx = context(raw_only())
    with patch.object(api, "chiral_area_accounting", side_effect=AssertionError("forbidden")) as forbidden:
        receipt = attempt(ctx)
    forbidden.assert_not_called()
    assert receipt.data["category"] == "MISSING_RECORDED_FIELD"

@pytest.mark.parametrize("operation", ["resume", "checkpoint", "step", "run"])
def test_N19_unsupported_resume_or_advancement(operation):
    _, request, *_ = context()
    data = request.to_dict()
    data["operation"] = operation
    refused(lambda: Request(data))

def test_N20_unsupported_cross_domain_conversion():
    _, request, *_ = context()
    data = request.to_dict()
    data["parameters"] = {"convert_experimental_to_core": True}
    refused(lambda: Request(data))

def test_N21_import_origin_and_snapshot_claims_must_not_be_missing():
    record, _ = record_claim()
    for key in ("imports_manifest", "snapshot_id", "installation_manifest"):
        value = record.to_dict()
        value["producer"][key] = None
        refused(lambda: DerivedAnalysisRecord(value), "UNVERIFIED_PRODUCER")
    # Actual origin prevention is B2; B1 never accepts a verified execution attempt.
    assert attempt(context()).data["category"] == "B1_VERIFIED_LANE_DISABLED"

def test_N22_false_kernel_attribution():
    record, _ = record_claim()
    value = record.to_dict()
    value["producer"]["kernel"]["source_revision"] = value["parents"][0]["source_claims"]["commit"]
    refused(lambda: DerivedAnalysisRecord(value), "KERNEL_MISMATCH")
    value = record.to_dict()
    value["producer"]["kernel_roles"] = ["scientific_analysis"]
    refused(lambda: DerivedAnalysisRecord(value))

def test_N23_stale_attempt_or_request_completion():
    record, _ = record_claim()
    for group, field, replacement in [
        ("completion", "attempt_id", "OTHER_ATTEMPT"),
        ("completion", "request", named(RequestDigest, "OTHER_REQUEST")),
        ("producer", "payload", named(PayloadDigest, "OTHER_PAYLOAD")),
    ]:
        value = record.to_dict()
        value[group][field] = replacement
        refused(lambda: DerivedAnalysisRecord(value), "RESULT_BINDING_MISMATCH")

def test_N24_exact_copy_does_not_allow_numerical_tolerance():
    parent, request, *_ = context(fields=("D.chiral",))
    selection = Selection(request.to_dict()["selection"])
    value = copy_recorded(parent, selection).to_dict()
    value["fields"][0]["value"][1]["f64"] = "0x0.0p+0"
    refused(lambda: verify_copy(CopyPayload(value), parent, selection), "COPIED_VALUE_MISMATCH")

def test_N25_no_attestation_gap_or_claimed_b1_verification():
    ctx = context()
    evidence = unavailable_evidence(ctx[1], ctx[3], "TEST_ONLY")
    value = evidence.to_dict()
    value["checks"]["execution_snapshot_bound"] = {
        "state": "VERIFIED", "evidence": named(ManifestDigest, "fake"), "reason": "fake"}
    refused(lambda: ProducerEvidence(value), "UNVERIFIED_PRODUCER")
    record, _ = record_claim()
    value = record.to_dict()
    value["producer"]["checks"]["installed_content_verified"]["state"] = "NOT_APPLICABLE"
    refused(lambda: DerivedAnalysisRecord(value), "UNVERIFIED_PRODUCER")

def test_N26_resource_policy_is_finite_and_unapproved_stays_closed():
    receipt = attempt(context(approved=False))
    assert receipt.data["category"] == "RESOURCE_POLICY_UNAPPROVED"
    _, _, catalogue, *_ = context()
    data = catalogue.descriptor.to_dict()["resource_policy"]
    data["limits"] = None
    refused(lambda: ResourcePolicy(data), "RESOURCE_POLICY_UNAPPROVED")
    data = catalogue.descriptor.to_dict()
    data["effects"].append("NETWORK")
    refused(lambda: Descriptor(data))

def test_N26_one_active_attempt_per_lane():
    from concurrent.futures import ThreadPoolExecutor
    from threading import Event
    entered, release = Event(), Event()
    ctx = context()
    original = coordinator.ParentSnapshot
    def paused(*args, **kwargs):
        entered.set()
        assert release.wait(5)
        return original(*args, **kwargs)
    with patch.object(coordinator, "ParentSnapshot", side_effect=paused):
        with ThreadPoolExecutor(max_workers=1) as pool:
            active = pool.submit(attempt, ctx)
            assert entered.wait(5)
            try:
                busy = attempt(ctx)
                assert busy.data["category"] == "RESOURCE_LIMIT"
                assert busy.data["stage"] == "REQUEST"
            finally:
                release.set()
            assert active.result().data["category"] == "B1_VERIFIED_LANE_DISABLED"

def test_N27_cancellation_and_failures_are_receipts_only():
    from kernel_physics import api
    ctx = context()
    with patch.object(api.RunRecord, "from_json", side_effect=AssertionError("must not load")) as load:
        cancelled = attempt(ctx, cancelled=True)
    load.assert_not_called()
    assert cancelled.data["outcome"] == "CANCELLED" and cancelled.data["category"] == "CANCELLED"
    assert "result" not in cancelled.data
    with patch.object(api.RunRecord, "from_json", side_effect=RuntimeError("provider error")):
        failure = attempt(ctx)
    assert failure.data["outcome"] == "FAILED" and failure.data["category"] == "PROVIDER_FAILURE"

def test_N29_legacy_cache_and_sidecar_cannot_gain_new_identity():
    for legacy in ({"result_kind": "analysis", "parent_source_commit": "f" * 40},
                   {"export_schema_version": 1, "app_version": "0.1.0"}):
        refused(lambda: DerivedAnalysisRecord(legacy))

def test_N30_scientific_overclaim_and_new_derived_quantities_rejected():
    record, _ = record_claim()
    value = record.to_dict()
    value["statuses"][0]["status"] = "EXPERIMENTAL_ENGINE"
    refused(lambda: DerivedAnalysisRecord(value), "SCIENTIFIC_OVERCLAIM")
    value = record.to_dict()
    value["result"]["sharpness_score"] = {"f64": "0x0.0p+0"}
    refused(lambda: DerivedAnalysisRecord(value))
    value = record.to_dict()
    value["qualification"] = "Exact equality proof"
    refused(lambda: DerivedAnalysisRecord(value))

def test_malformed_request_receipt_does_not_invent_valid_identity():
    receipt = parse_request_or_receipt(b'{"invalid":1.0}', PARSING,
                                      attempt_id="TEST_ONLY", diagnostic_limit=100)
    assert receipt.data["request"] is None and receipt.data["request_digest"] is None
    assert receipt.data["submitted_bytes"]["scope"] == "INPUT_BYTE_DIGEST"
    assert len(receipt.data["diagnostic"]) <= 100

def test_receipt_cannot_claim_success_or_publish_incomplete_result():
    receipt = attempt(context())
    value = receipt.to_dict()
    value["outcome"] = "COMPLETE"
    refused(lambda: AttemptReceipt(value))
