"""TEST ONLY: handcrafted records and MOCK attestation. Never a production attestor."""
import copy
import hashlib
import json
from pathlib import Path

from trioctagon_analysis.approval import ApprovalRoot
from trioctagon_analysis.attestation import CHECKS, ProducerEvidence
from trioctagon_analysis.catalogue import candidate_catalogue
from trioctagon_analysis.codec import ParseLimits, canonical_bytes
from trioctagon_analysis.common import KernelSelection, ProducerBuild, ResourcePolicy
from trioctagon_analysis.constants import FIELDS, OPERATION, QUALIFICATION, REPRODUCIBILITY
from trioctagon_analysis.digests import *
from trioctagon_analysis.provider import ParentLoadLimits, ParentSnapshot, copy_recorded
from trioctagon_analysis.records import DerivedAnalysisRecord, semantic_result_digest
from trioctagon_analysis.requests import Request, Selection

HERE = Path(__file__).parent
PARSING = ParseLimits(16 * 1024 * 1024, 64)  # synthetic-test budget, NOT deployment approval
LIMITS = ParentLoadLimits(PARSING, 10000)

def named(kind, name):
    return kind(hashlib.sha256(("TEST_ONLY_NOT_APPROVED:" + name).encode()).hexdigest()).to_dict()

def core_data():
    return json.loads((HERE / "fixtures/core_record.json").read_bytes())

def core_bytes(data=None, pretty=False):
    data = copy.deepcopy(core_data() if data is None else data)
    # Test-only use of the documented native digest projection to construct inert fixtures.
    semantic = {k: v for k, v in data.items() if k not in ("deterministic_sha256", "execution_metadata")}
    data["deterministic_sha256"] = hashlib.sha256(json.dumps(semantic, sort_keys=True,
        separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return json.dumps(data, sort_keys=True, ensure_ascii=False,
        **({"indent": 2} if pretty else {"separators": (",", ":")})).encode()

def raw_only():
    data = core_data()
    data["selection"]["diagnostics"] = []
    data["definition_ids"].remove("E07")
    for sample in data["samples"]:
        sample["diagnostics"] = {}
    return core_bytes(data)

def context(raw=None, fields=FIELDS, *, ordinal=0, index="7", approved=True):
    raw = core_bytes() if raw is None else raw
    parent = ParentSnapshot(raw, LIMITS)
    resource = ResourcePolicy({"state": "APPROVED" if approved else "PROPOSED",
        "proposal": named(ManifestDigest, "resource-proposal"),
        "logical": {"parents": 1, "sample_ordinals": 1, "fields_min": 1, "fields_max": 16,
                    "numeric_leaves": 20, "external_data": 0, "concurrent_jobs": 1},
        "limits": {"input_bytes": PARSING.max_bytes, "samples": LIMITS.max_samples,
                   "json_depth": PARSING.max_depth, "output_bytes": PARSING.max_bytes,
                   "wall_milliseconds": 30000, "memory_bytes": 512 * 1024 * 1024,
                   "diagnostic_characters": 512} if approved else None})
    build = ProducerBuild({"distribution": "trioctagon-analysis", "version": "0.1.0",
        "provider_id": "core.app04.recorded_copy", "provider_revision": 1,
        "entry_point": "trioctagon_analysis.provider:copy_recorded",
        "source": {"repository": "test-only://synthetic-provider", "revision": "1" * 40,
                   "content": named(ManifestDigest, "source")},
        "archive": named(InputByteDigest, "archive"), "build_inputs": named(ManifestDigest, "build"),
        "dependency_policy": named(PolicyDigest, "dependencies"),
        "runtime_policy": named(PolicyDigest, "runtime"),
        "members": [{"path": "trioctagon_analysis/provider.py", "size": 1,
                     "digest": named(InputByteDigest, "not-real-installed-bytes")}]})
    selected = {"id": "core.app04.recorded_copy", "revision": 1, "build": build.identity.to_dict()}
    catalogue = candidate_catalogue([selected], resource)
    kernel = KernelSelection({"distribution": "trioctagon-physics", "version": "0.1.0",
        "source_repository": "test-only://synthetic-selected-kernel", "source_revision": "2" * 40,
        "lock": named(InputByteDigest, "kernel-lock"),
        "actual_archive": named(InputByteDigest, "actual-kernel-archive"),
        "selection": "CERTIFIED_RECONSTRUCTION", "stable_members": named(ManifestDigest, "kernel-members"),
        "certification": named(ManifestDigest, "kernel-certification")})
    approval = ApprovalRoot({"catalogue": catalogue.identity.to_dict(),
        "descriptor": catalogue.descriptor.identity.to_dict(), "providers": [selected],
        "attestor_build": named(ProducerBuildIdentity, "MOCK-ATTESTOR-NOT-DEPLOYED"),
        "dependency_policy": build.to_dict()["dependency_policy"],
        "runtime_policy": build.to_dict()["runtime_policy"], "resource_policy": resource.identity.to_dict(),
        "kernel": kernel.to_dict(), "deployment": {"receipt_id": "TEST_ONLY_NO_APPROVAL",
            "approver": "TEST_ONLY_NOT_A_REAL_REVIEW", "approved_at": "TEST_ONLY",
            "manifest": named(ManifestDigest, "TEST_ONLY_deployment"), "method": "LOCAL_REVIEWED_DIGEST_PIN"},
        "qualification": "HASH != AUTHORSHIP; HASH != SIGNATURE"})
    request = Request({"family": "TRIOCTAGON_ANALYSIS_REQUEST", "schema": "1.0.0",
        "protocol": {"family": "TRIOCTAGON_ANALYSIS_PROTOCOL", "version": 1},
        "catalogue": catalogue.identity.to_dict(), "descriptor": catalogue.descriptor.identity.to_dict(),
        "operation": OPERATION, "revision": 1, "profile": "CORE", "provider": selected,
        "parents": [parent.reference.to_dict()],
        "selection": {"ordinal": ordinal, "expected_update_index": index, "fields": list(fields)},
        "parameters": {}, "external_inputs": [], "resource_policy": resource.identity.to_dict(),
        "kernel": kernel.to_dict()})
    return parent, request, catalogue, approval, build

class TEST_ONLY_MockAttestor:
    """Synthetic evidence generation used ONLY to exercise inert record codecs."""
    @staticmethod
    def evidence(request, approval, build, payload):
        return ProducerEvidence({"method": "B2_EXECUTION_SNAPSHOT",
            "request": request.identity.to_dict(), "attempt_id": "TEST_ONLY_NO_EXECUTION",
            "approval": approval.identity.to_dict(), "build": build.to_dict(),
            "attestor_build": approval.to_dict()["attestor_build"],
            "environment": {"runtime_manifest": named(ManifestDigest, "runtime-manifest"),
                "interpreter": named(InputByteDigest, "interpreter"), "dependency_policy": build.to_dict()["dependency_policy"],
                "runtime_policy": build.to_dict()["runtime_policy"], "platform": "TEST_ONLY", "architecture": "TEST_ONLY",
                "configuration": named(ManifestDigest, "configuration")},
            "installation_manifest": named(ManifestDigest, "installation"), "snapshot_id": "TEST_ONLY_NO_SNAPSHOT",
            "imports_manifest": named(ManifestDigest, "imports"), "kernel": request.to_dict()["kernel"],
            "kernel_roles": ["parent_validation"], "scientific_recomputation": "NOT_PERFORMED",
            "payload": payload.identity.to_dict(),
            "checks": {key: {"state": "VERIFIED", "evidence": named(ManifestDigest, "MOCK_" + key),
                            "reason": "TEST ONLY MOCK; NOT REAL VERIFICATION"} for key in CHECKS}})

def record_claim():
    parent, request, catalogue, approval, build = context()
    payload = copy_recorded(parent, Selection(request.to_dict()["selection"]))
    evidence = TEST_ONLY_MockAttestor.evidence(request, approval, build, payload)
    value = {"family": "TRIOCTAGON_DERIVED_ANALYSIS_RECORD", "schema": "1.0.0", "profile": "CORE",
        "catalogue": catalogue.to_dict(), "approval": approval.to_dict(), "request": request.to_dict(),
        "request_digest": request.identity.to_dict(), "parents": [parent.reference.to_dict()],
        "producer": evidence.to_dict(), "authority": catalogue.descriptor.to_dict()["authority"],
        "statuses": catalogue.descriptor.to_dict()["statuses"], "result": payload.to_dict(),
        "qualification": QUALIFICATION, "reproducibility": REPRODUCIBILITY, "warnings": [],
        "completion": {"state": "COMPLETE", "attempt_id": "TEST_ONLY_NO_EXECUTION",
            "request": request.identity.to_dict(), "payload": payload.identity.to_dict(),
            "evidence": evidence.identity.to_dict(), "started_at": "2000-01-01T00:00:00+00:00",
            "completed_at": "2000-01-01T00:00:01+00:00"}}
    value["semantic_result_digest"] = semantic_result_digest(value).to_dict()
    return DerivedAnalysisRecord(value), parent
