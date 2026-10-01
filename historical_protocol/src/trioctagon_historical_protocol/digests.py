"""Historical-owned digest types. Core scope classes and allowlists are untouched."""
import hashlib

from trioctagon_analysis.digests import Digest, InputByteDigest, FullArtifactDigest
from .errors import require


class RequestDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_REQUEST_DIGEST"
class AuthorityDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_AUTHORITY_DIGEST"
class ConstantsDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_CONSTANTS_DIGEST"
class BasisDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_BASIS_DIGEST"
class CatalogueDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_CATALOGUE_DIGEST"
class DescriptorDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_DESCRIPTOR_DIGEST"
class ResourcePolicyDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_RESOURCE_POLICY_DIGEST"
class ProviderBuildDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_PROVIDER_BUILD_DIGEST"
class ManifestDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_MANIFEST_DIGEST"
class ConformanceDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_CONFORMANCE_DIGEST"
class PayloadDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_PAYLOAD_DIGEST"
class InstallationObservationDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_INSTALLATION_OBSERVATION_DIGEST"
class ExecutionEvidenceDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_EXECUTION_EVIDENCE_DIGEST"
class SemanticResultDigest(Digest):
    __slots__ = ()
    scope = "HISTORICAL_SEMANTIC_RESULT_DIGEST"


CONTENT_TYPES = frozenset({RequestDigest, AuthorityDigest, ConstantsDigest, BasisDigest,
    CatalogueDigest, DescriptorDigest, ResourcePolicyDigest, ProviderBuildDigest,
    ManifestDigest, ConformanceDigest, PayloadDigest, InstallationObservationDigest,
    ExecutionEvidenceDigest, SemanticResultDigest})


def preimage(kind, canonical):
    require(kind in CONTENT_TYPES and type(canonical) is bytes)
    return b"TRIOCTAGON\x00" + kind.scope.encode("ascii") + b"\x00V1\x00" + canonical


def content_digest(kind, canonical):
    return kind(hashlib.sha256(preimage(kind, canonical)).hexdigest())


def byte_digest(kind, raw):
    require(kind in (InputByteDigest, FullArtifactDigest) and type(raw) is bytes)
    return kind(hashlib.sha256(raw).hexdigest())
