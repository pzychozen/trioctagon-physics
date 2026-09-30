"""Application-owned approval DATA. B1 neither deploys nor authenticates a root."""
from . import schema as s
from .common import KernelSelection, embedded, provider_schema
from .digests import (ApprovalDigest, CatalogueDigest, DescriptorDigest, ManifestDigest,
                      PolicyDigest, ProducerBuildIdentity, content_digest)
from .errors import require

class ApprovalRoot(s.Document):
    __slots__ = ()
    schema = s.obj(
        catalogue=s.digest(CatalogueDigest), descriptor=s.digest(DescriptorDigest),
        providers=s.seq(provider_schema, 1), attestor_build=s.digest(ProducerBuildIdentity),
        dependency_policy=s.digest(PolicyDigest), runtime_policy=s.digest(PolicyDigest),
        resource_policy=s.digest(PolicyDigest), kernel=embedded(KernelSelection),
        deployment=s.obj(receipt_id=s.text, approver=s.text, approved_at=s.text,
            manifest=s.digest(ManifestDigest), method=s.literal("LOCAL_REVIEWED_DIGEST_PIN")),
        qualification=s.literal("HASH != AUTHORSHIP; HASH != SIGNATURE"))

    @classmethod
    def validate(cls, value):
        builds = [p["build"]["sha256"] for p in value["providers"]]
        require(len(builds) == len(set(builds)), "UNSUPPORTED_PROVIDER", "duplicate approved provider")

    @property
    def identity(self):
        return content_digest(ApprovalDigest, self.to_bytes())

    def validate_catalogue(self, catalogue):
        from .catalogue import Catalogue
        from .common import ResourcePolicy
        require(type(catalogue) is Catalogue, "INVALID_SCHEMA", "Catalogue required")
        a = self.to_dict()
        d = catalogue.descriptor.to_dict()
        require(a["catalogue"] == catalogue.identity.to_dict() and
                a["descriptor"] == catalogue.descriptor.identity.to_dict(),
                "AUTHORITY_MISMATCH", "catalogue/descriptor differs from application approval")
        require(a["providers"] == d["providers"], "UNSUPPORTED_PROVIDER", "approval/provider allowlist mismatch")
        require(a["resource_policy"] == ResourcePolicy(d["resource_policy"]).identity.to_dict(),
                "RESOURCE_POLICY_UNAPPROVED", "resource policy differs from approval root")
