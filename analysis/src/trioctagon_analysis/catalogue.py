"""One operation only. Catalogue construction is not approval or deployment."""
from . import schema as s
from .common import ResourcePolicy, authority_schema, embedded, provider_schema, status_schema
from .constants import (AUTHORITY_REFERENCES, EFFECTS, FIELDS, NUMERICAL, OPERATION,
                        QUALIFICATION, REPRODUCIBILITY, STATUS_ASSERTIONS)
from .digests import CatalogueDigest, DescriptorDigest, content_digest
from .errors import require

def fixed_descriptor():
    # Fresh detached trees; callers cannot mutate the catalogue via shared constants.
    import copy
    return copy.deepcopy({
        "operation": OPERATION, "revision": 1, "domain": "CORE", "support": "SUPPORTED",
        "profile": "CORE", "lifecycle": "B1_COPY_ONLY_VERIFIED_LANE_DISABLED",
        "parent": {"family": "KERNEL_RUN_RECORD", "schema": "1.0.0", "api": "1.0.0",
                   "topology": "triad", "state_size": "3"},
        "selection": "ONE_ZERO_BASED_ORDINAL_AND_EXPECTED_STORED_UPDATE_INDEX",
        "field_allowlist": list(FIELDS), "vector_axes": ["0", "1", "2"],
        "output_schema": "APP04_RECORDED_COPY_PAYLOAD_1",
        "authority": AUTHORITY_REFERENCES, "statuses": STATUS_ASSERTIONS,
        "qualification": QUALIFICATION, "assumptions": [
            "Public loader validates structure/digest, not equations or authorship.",
            "Only stored tokens; no inference, resampling, conversion or state advancement."],
        "numerical": NUMERICAL, "reproducibility": REPRODUCIBILITY, "effects": EFFECTS,
        "failure": "MISSING_REQUESTED_FIELD_REFUSES_WHOLE_REQUEST_NO_FALLBACK",
    })

class Descriptor(s.Document):
    __slots__ = ()
    schema = s.obj(operation=s.literal(OPERATION), revision=s.literal(1),
        domain=s.literal("CORE"), support=s.literal("SUPPORTED"), profile=s.literal("CORE"),
        lifecycle=s.literal("B1_COPY_ONLY_VERIFIED_LANE_DISABLED"),
        parent=s.obj(family=s.literal("KERNEL_RUN_RECORD"), schema=s.literal("1.0.0"),
            api=s.literal("1.0.0"), topology=s.literal("triad"), state_size=s.literal("3")),
        selection=s.text, field_allowlist=s.seq(s.text, 16, 16),
        vector_axes=s.seq(s.text, 3, 3), output_schema=s.literal("APP04_RECORDED_COPY_PAYLOAD_1"),
        authority=authority_schema, statuses=status_schema, qualification=s.text,
        assumptions=s.seq(s.text, 2, 2), numerical=s.text, reproducibility=s.text,
        effects=s.seq(s.text, 3, 3), failure=s.text,
        providers=s.seq(provider_schema, 1), resource_policy=embedded(ResourcePolicy))

    @classmethod
    def validate(cls, value):
        require(all(value[k] == v for k, v in fixed_descriptor().items()),
                "AUTHORITY_MISMATCH", "APP04 semantics/authority/effects cannot be changed")
        identities = [p["build"]["sha256"] for p in value["providers"]]
        require(len(identities) == len(set(identities)), "UNSUPPORTED_PROVIDER", "duplicate provider build")

    @property
    def identity(self):
        return content_digest(DescriptorDigest, self.to_bytes())

class Catalogue(s.Document):
    __slots__ = ()
    schema = s.obj(family=s.literal("TRIOCTAGON_ANALYSIS_CATALOGUE"), schema=s.literal("1.0.0"),
                   descriptors=s.seq(embedded(Descriptor), 1, 1))

    @property
    def descriptor(self):
        return Descriptor(self.to_dict()["descriptors"][0])

    @property
    def identity(self):
        return content_digest(CatalogueDigest, self.to_bytes())

def candidate_catalogue(providers, resource_policy):
    require(type(resource_policy) is ResourcePolicy, "INVALID_SCHEMA", "ResourcePolicy required")
    descriptor = Descriptor({**fixed_descriptor(), "providers": providers,
                             "resource_policy": resource_policy.to_dict()})
    return Catalogue({"family": "TRIOCTAGON_ANALYSIS_CATALOGUE", "schema": "1.0.0",
                      "descriptors": [descriptor.to_dict()]})
