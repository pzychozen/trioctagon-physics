"""Immutable request bodies. No status override, plugin name, resume or conversion."""
from . import schema as s
from .common import KernelSelection, embedded, provider_schema, source_claims_schema
from .constants import FIELDS, OPERATION
from .digests import (CatalogueDigest, DescriptorDigest, InputByteDigest, ParentCanonicalByteDigest,
                      ParentSemanticDigest, PolicyDigest, RequestDigest, content_digest)
from .errors import require

class ParentReference(s.Document):
    __slots__ = ()
    schema = s.obj(role=s.literal("source"), family=s.literal("KERNEL_RUN_RECORD"),
        schema=s.literal("1.0.0"), semantic=s.digest(ParentSemanticDigest),
        original_bytes=s.digest(InputByteDigest), canonical_bytes=s.digest(ParentCanonicalByteDigest),
        source_claims=source_claims_schema)

class Selection(s.Document):
    __slots__ = ()
    schema = s.obj(ordinal=s.integer, expected_update_index=s.counter,
                   fields=s.seq(s.text, 1, 16))

    @classmethod
    def validate(cls, value):
        fields = value["fields"]
        require(len(fields) == len(set(fields)) and set(fields) <= set(FIELDS),
                "FORBIDDEN_SELECTION", "select unique allowlisted fields in explicit order")

class Request(s.Document):
    __slots__ = ()
    schema = s.obj(family=s.literal("TRIOCTAGON_ANALYSIS_REQUEST"), schema=s.literal("1.0.0"),
        protocol=s.obj(family=s.literal("TRIOCTAGON_ANALYSIS_PROTOCOL"), version=s.literal(1)),
        catalogue=s.digest(CatalogueDigest), descriptor=s.digest(DescriptorDigest),
        operation=s.literal(OPERATION), revision=s.literal(1), profile=s.literal("CORE"),
        provider=provider_schema, parents=s.seq(embedded(ParentReference), 1, 1),
        selection=embedded(Selection), parameters=s.obj(),
        external_inputs=s.seq(s.text, 0, 0), resource_policy=s.digest(PolicyDigest),
        kernel=embedded(KernelSelection))

    @property
    def identity(self):
        return content_digest(RequestDigest, self.to_bytes())

    def validate_context(self, catalogue, approval):
        from .approval import ApprovalRoot
        require(type(approval) is ApprovalRoot, "INVALID_SCHEMA", "application ApprovalRoot required")
        approval.validate_catalogue(catalogue)
        q, a = self.to_dict(), approval.to_dict()
        require(q["catalogue"] == a["catalogue"] and q["descriptor"] == a["descriptor"],
                "AUTHORITY_MISMATCH", "request catalogue is not approved")
        require(q["provider"] in a["providers"], "UNSUPPORTED_PROVIDER", "provider/build not approved")
        require(q["kernel"] == a["kernel"], "KERNEL_MISMATCH", "selected kernel differs")
        require(q["resource_policy"] == a["resource_policy"],
                "RESOURCE_POLICY_UNAPPROVED", "request resource policy differs")
