"""Scope-distinct immutable hashes. Hashes are neither signatures nor authorship."""
from dataclasses import dataclass
import hashlib
import re
from typing import ClassVar

from .codec import CODEC
from .errors import require

@dataclass(frozen=True, slots=True)
class Digest:
    sha256: str
    scope: ClassVar[str]
    codec: ClassVar[str] = CODEC

    def __post_init__(self):
        require(type(self) is not Digest and type(self.sha256) is str and
                re.fullmatch(r"[0-9a-f]{64}", self.sha256) is not None,
                "INVALID_SCHEMA", "invalid typed SHA-256")

    def to_dict(self):
        return {"scope": self.scope, "algorithm": "SHA-256", "codec": self.codec,
                "sha256": self.sha256}

    @classmethod
    def from_dict(cls, value):
        require(type(value) is dict and set(value) == {"scope", "algorithm", "codec", "sha256"},
                "INVALID_SCHEMA", "strict digest object required")
        require((value["scope"], value["algorithm"], value["codec"]) ==
                (cls.scope, "SHA-256", cls.codec), "INVALID_SCHEMA", "digest scope/codec mismatch")
        return cls(value["sha256"])

class InputByteDigest(Digest):
    __slots__ = ()
    scope = "INPUT_BYTE_DIGEST"
    codec = "RAW_BYTES"

class ParentSemanticDigest(Digest):
    __slots__ = ()
    scope = "PARENT_SEMANTIC_DIGEST"
    codec = "KERNEL_RUN_RECORD_1.0.0_NATIVE"

class ParentCanonicalByteDigest(Digest):
    __slots__ = ()
    scope = "PARENT_CANONICAL_BYTE_DIGEST"
    codec = "KERNEL_RUN_RECORD_1.0.0_CANONICAL_UTF8"

class ProducerBuildIdentity(Digest):
    __slots__ = ()
    scope = "PRODUCER_BUILD_IDENTITY"

class RequestDigest(Digest):
    __slots__ = ()
    scope = "REQUEST_DIGEST"

class SemanticResultDigest(Digest):
    __slots__ = ()
    scope = "SEMANTIC_RESULT_DIGEST"

class FullArtifactDigest(Digest):
    __slots__ = ()
    scope = "FULL_ARTIFACT_DIGEST"
    codec = "RAW_BYTES"

class CatalogueDigest(Digest):
    __slots__ = ()
    scope = "CATALOGUE_DIGEST"

class DescriptorDigest(Digest):
    __slots__ = ()
    scope = "DESCRIPTOR_DIGEST"

class PolicyDigest(Digest):
    __slots__ = ()
    scope = "POLICY_DIGEST"

class ManifestDigest(Digest):
    __slots__ = ()
    scope = "MANIFEST_DIGEST"

class ApprovalDigest(Digest):
    __slots__ = ()
    scope = "APPROVAL_ROOT_DIGEST"

class PayloadDigest(Digest):
    __slots__ = ()
    scope = "RESULT_PAYLOAD_DIGEST"

class EvidenceDigest(Digest):
    __slots__ = ()
    scope = "ATTESTATION_EVIDENCE_DIGEST"

CONTENT_TYPES = frozenset({ProducerBuildIdentity, RequestDigest, SemanticResultDigest,
    CatalogueDigest, DescriptorDigest, PolicyDigest, ManifestDigest, ApprovalDigest,
    PayloadDigest, EvidenceDigest})
BYTE_TYPES = frozenset({InputByteDigest, ParentCanonicalByteDigest, FullArtifactDigest})

def preimage(digest_type, canonical):
    require(digest_type in CONTENT_TYPES and type(canonical) is bytes,
            "INVALID_SCHEMA", "canonical hash scope and bytes required")
    return b"TRIOCTAGON\x00" + digest_type.scope.encode("ascii") + b"\x00V1\x00" + canonical

def content_digest(digest_type, canonical):
    return digest_type(hashlib.sha256(preimage(digest_type, canonical)).hexdigest())

def byte_digest(digest_type, raw):
    require(digest_type in BYTE_TYPES and type(raw) is bytes,
            "INVALID_SCHEMA", "raw-byte digest scope and bytes required")
    return digest_type(hashlib.sha256(raw).hexdigest())

def require_digest(value, digest_type):
    require(type(value) is digest_type, "INVALID_SCHEMA", "wrong digest type")
    return value
