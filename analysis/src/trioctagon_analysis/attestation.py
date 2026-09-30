"""Evidence and B2 hook only. B1 has no verified snapshot implementation."""
from typing import Protocol

from . import schema as s
from .common import KernelSelection, ProducerBuild, embedded
from .digests import (ApprovalDigest, EvidenceDigest, InputByteDigest, ManifestDigest,
                      PayloadDigest, PolicyDigest, ProducerBuildIdentity, RequestDigest,
                      content_digest)
from .errors import require

CHECKS = ("catalogue_approved", "build_evidence_accepted", "installed_content_verified",
          "execution_snapshot_bound", "actual_imports_origins_bound", "inputs_verified",
          "payload_validated", "participating_kernel_verified")
check_schema = s.obj(state=s.enum("VERIFIED", "FAILED", "NOT_APPLICABLE", "UNAVAILABLE"),
                     evidence=s.nullable(s.digest(ManifestDigest)), reason=s.text)
checks_schema = s.obj(**{key: check_schema for key in CHECKS})
attempt_id_schema = s.matching(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}")

class ProducerEvidence(s.Document):
    __slots__ = ()
    schema = s.obj(
        method=s.enum("UNAVAILABLE_B1", "B2_EXECUTION_SNAPSHOT"),
        request=s.digest(RequestDigest), attempt_id=attempt_id_schema,
        approval=s.digest(ApprovalDigest), build=s.nullable(embedded(ProducerBuild)),
        attestor_build=s.nullable(s.digest(ProducerBuildIdentity)),
        environment=s.nullable(s.obj(runtime_manifest=s.digest(ManifestDigest),
            interpreter=s.digest(InputByteDigest), dependency_policy=s.digest(PolicyDigest),
            runtime_policy=s.digest(PolicyDigest), platform=s.text, architecture=s.text,
            configuration=s.digest(ManifestDigest))),
        installation_manifest=s.nullable(s.digest(ManifestDigest)),
        snapshot_id=s.nullable(s.text), imports_manifest=s.nullable(s.digest(ManifestDigest)),
        kernel=s.nullable(embedded(KernelSelection)),
        kernel_roles=s.seq(s.literal("parent_validation"), 1, 1),
        scientific_recomputation=s.literal("NOT_PERFORMED"),
        payload=s.nullable(s.digest(PayloadDigest)), checks=checks_schema)

    @classmethod
    def validate(cls, value):
        for check in value["checks"].values():
            require(check["state"] != "VERIFIED" or check["evidence"] is not None,
                    "UNVERIFIED_PRODUCER", "verified check needs evidence reference")
        if value["method"] == "UNAVAILABLE_B1":
            require(all(c["state"] != "VERIFIED" for c in value["checks"].values()),
                    "UNVERIFIED_PRODUCER", "B1 unavailable evidence cannot claim verification")

    @property
    def identity(self):
        return content_digest(EvidenceDigest, self.to_bytes())

    def require_verified_claim(self, request, approval, payload):
        """Validate consistency of an imported claim; DOES NOT perform attestation."""
        e, a, q = self.to_dict(), approval.to_dict(), request.to_dict()
        require(e["method"] == "B2_EXECUTION_SNAPSHOT" and
                all(c["state"] == "VERIFIED" for c in e["checks"].values()),
                "UNVERIFIED_PRODUCER", "every APP04 verification check is applicable and required")
        required = ("build", "attestor_build", "environment", "installation_manifest",
                    "snapshot_id", "imports_manifest", "kernel", "payload")
        require(all(e[k] is not None for k in required), "UNVERIFIED_PRODUCER", "incomplete producer claim")
        build = ProducerBuild(e["build"])
        require(e["request"] == request.identity.to_dict() and e["approval"] == approval.identity.to_dict()
                and e["payload"] == payload.identity.to_dict(),
                "RESULT_BINDING_MISMATCH", "evidence is bound to a different request/root/payload")
        require(build.identity.to_dict() == q["provider"]["build"] and
                e["attestor_build"] == a["attestor_build"], "WRONG_PRODUCER", "build/attestor mismatch")
        require(e["kernel"] == q["kernel"] == a["kernel"], "KERNEL_MISMATCH", "actual kernel claim mismatch")
        for key in ("dependency_policy", "runtime_policy"):
            require(e["environment"][key] == a[key] == e["build"][key],
                    "WRONG_PRODUCER", "producer dependency/runtime policy mismatch")

class SnapshotBindingRequest(s.Document):
    """B2 must enforce these requirements, not merely echo these strings."""
    __slots__ = ()
    schema = s.obj(request=s.digest(RequestDigest), approval=s.digest(ApprovalDigest),
        attempt_id=attempt_id_schema, absolute_runtime=s.text, fixed_import_paths=s.seq(s.text, 1),
        expected_closure=s.digest(ManifestDigest),
        policy=s.literal("TRUSTED_OS_COORDINATOR_USER_REVIEWED_PROVIDER_NO_MUTABLE_EXECUTABLES"))

    @classmethod
    def validate(cls, value):
        from pathlib import PureWindowsPath
        paths = [value["absolute_runtime"], *value["fixed_import_paths"]]
        require(all(PureWindowsPath(p).is_absolute() and ".." not in PureWindowsPath(p).parts for p in paths),
                "INVALID_SCHEMA", "B2 hook requires fixed absolute Windows paths")

class SnapshotAttestor(Protocol):
    """No implementation is shipped. A B2 coordinator owns this interface."""
    def bind(self, request: SnapshotBindingRequest) -> ProducerEvidence: ...

def unavailable_evidence(request, approval, attempt_id):
    return ProducerEvidence({"method": "UNAVAILABLE_B1", "request": request.identity.to_dict(),
        "attempt_id": attempt_id, "approval": approval.identity.to_dict(),
        "build": None, "attestor_build": None, "environment": None,
        "installation_manifest": None, "snapshot_id": None, "imports_manifest": None,
        "kernel": None, "kernel_roles": ["parent_validation"], "scientific_recomputation": "NOT_PERFORMED",
        "payload": None, "checks": {name: {"state": "UNAVAILABLE", "evidence": None,
            "reason": "B1 does not deploy or verify execution-bound producer attestation."} for name in CHECKS}})
