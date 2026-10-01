"""External, caller-pinned local admission. No request may choose this authority."""
import hashlib
from pathlib import Path
from trioctagon_historical_protocol.schema import s, Document, embedded, literal_tree
from trioctagon_historical_protocol.codec import ParseLimits
from trioctagon_historical_protocol.catalogue import Catalogue
from trioctagon_historical_protocol.packets import ProviderBuild, ResourcePolicy, observation_member_schema, safe_members
from trioctagon_historical_protocol.requests import Request
from trioctagon_historical_protocol.digests import ConformanceDigest, ManifestDigest
from .installation import DISTRIBUTIONS, manifest_sha, runtime

runtime_schema = s.obj(implementation=s.text, version=s.text, platform=s.text, architecture=s.text)
inventory_schema = s.obj(id=s.enum(*DISTRIBUTIONS), version=s.text, members=s.seq(observation_member_schema,1))


class AdmissionFailure(ValueError):
    def __init__(self, category, message):
        self.category = category
        super().__init__(message)


class Admission(Document):
    """An exact external bundle explicitly pinned by trusted local configuration."""
    __slots__ = ()
    persisted = True
    schema = s.obj(schema=s.literal("H6B_LOCAL_ADMISSION_1"), catalogue=embedded(Catalogue), build=embedded(ProviderBuild),
        resource=embedded(ResourcePolicy), runtime=runtime_schema, installed=s.seq(inventory_schema,4,4),
        conformance=s.digest(ConformanceDigest), measurement=s.digest(ManifestDigest),
        review=s.obj(state=s.literal("LOCAL_REVIEW_ACCEPTED"), scope=s.literal("UNATTESTED_HISTORICAL_ONLY"),
                     windows_execution_binding=s.literal("NOT_PROVEN"), production_attestation_enabled=s.literal(False)))

    @classmethod
    def validate(cls, value):
        c, b, r = Catalogue(value["catalogue"]), ProviderBuild(value["build"]), ResourcePolicy(value["resource"])
        if value["resource"]["state"] != "MEASURED_ADMITTED_LOCAL":
            raise ValueError("pending resource policy cannot admit execution")
        if value["resource"]["measurement_manifest"] != value["measurement"] or value["build"]["conformance_digest"] != value["conformance"]:
            raise ValueError("reviewed measurement/conformance reference mismatch")
        if value["catalogue"]["resource_policy"] != r.identity.to_dict():
            raise ValueError("catalogue/policy mismatch")
        expected_key = dict(id="historical.reference", revision=1, build=b.identity.to_dict())
        if value["catalogue"]["provider_builds"] != [expected_key]:
            raise ValueError("catalogue must pin exactly the reviewed independent build")
        inventories = value["installed"]
        if [row["id"] for row in inventories] != sorted(DISTRIBUTIONS):
            raise ValueError("fixed installed dependency inventory required")
        for inv in inventories:
            safe_members(inv["members"])
        own = next(inv for inv in inventories if inv["id"] == "trioctagon-historical-kernel")
        members = [{key:row[key] for key in ("path","bytes","sha256")} for row in value["build"]["members"]]
        if own["members"] != members:
            raise ValueError("complete installed implementation/build mismatch")
        deps = [dict(id=inv["id"], version=inv["version"], manifest_sha256=manifest_sha(inv),
            role="NUMERIC_LIBRARY" if inv["id"] == "numpy" else "NONSCIENTIFIC_INFRASTRUCTURE")
            for inv in inventories if inv is not own]
        if value["build"]["dependencies"] != deps:
            raise ValueError("declared dependency closure differs from installed inventories")

    @classmethod
    def load_pinned(cls, path, expected_sha256):
        if type(expected_sha256) is not str or len(expected_sha256) != 64:
            raise ValueError("an explicit reviewed admission byte pin is required")
        # Finite bootstrap parser cap, never a computation resource admission.
        with Path(path).open("rb") as stream:
            raw = stream.read(4*1024*1024+1)
        if hashlib.sha256(raw).hexdigest() != expected_sha256:
            raise ValueError("local admission pin mismatch")
        return cls.from_bytes(raw, ParseLimits(4*1024*1024,64))

    def validate_request(self, request):
        if type(request) is not Request:
            raise TypeError("Historical Request required")
        value = self.to_dict()
        request.validate_context(Catalogue(value["catalogue"]), ResourcePolicy(value["resource"]), ProviderBuild(value["build"]))
        if value["runtime"] != runtime():
            raise AdmissionFailure("PROVIDER_IDENTITY_MISMATCH", "runtime differs from the reviewed local admission")
        body = request.to_dict()["body"]
        if body["operation"] == "historical.triad.run.inspect" and body["arguments"]["updates"] > value["resource"]["limits"]["max_updates"]:
            raise AdmissionFailure("RESOURCE_LIMIT", "run exceeds locally measured update limit")
