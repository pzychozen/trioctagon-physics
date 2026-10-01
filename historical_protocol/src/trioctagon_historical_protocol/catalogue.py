"""Closed catalogue claim schema and descriptor templates, not an admission registry."""
from .schema import s,Document,embedded,protocol_schema,literal_tree,PROFILE,CONTRACT,IMPLEMENTATION
from .packets import provider_key_schema,frozen,authority_packet,constants_packet
from .definitions import OPERATIONS,operation_index,descriptor_template
from .digests import CatalogueDigest,DescriptorDigest,AuthorityDigest,ConstantsDigest,ResourcePolicyDigest
from .errors import require


def descriptor_schema(value,path,integers):
    require(type(value) is dict)
    operation=value.get("operation")
    operation_index(operation)
    literal_tree(descriptor_template(operation))(value,path,integers)


class Descriptor(Document):
    __slots__=()
    digest_type=DescriptorDigest
    schema=staticmethod(descriptor_schema)


class Catalogue(Document):
    __slots__=()
    digest_type=CatalogueDigest
    schema=s.obj(family=s.literal("TRIOCTAGON_HISTORICAL_ANALYSIS_CATALOGUE"),schema=s.literal("1.0.0"),
        protocol=protocol_schema,profile=s.literal(PROFILE),contract=s.literal(CONTRACT),
        implementation_policy=s.literal(IMPLEMENTATION),authority=s.digest(AuthorityDigest),
        constants_packet=s.digest(ConstantsDigest),provider_builds=s.seq(provider_key_schema,1),
        resource_policy=s.digest(ResourcePolicyDigest),descriptors=s.seq(embedded(Descriptor),5,5),
        comparison_evidence=literal_tree(frozen("comparison")))

    @classmethod
    def validate(cls,value):
        require([d["operation"] for d in value["descriptors"]]==list(OPERATIONS),"UNKNOWN_OPERATION","five descriptors in fixed order required")
        ids=[p["build"]["sha256"] for p in value["provider_builds"]]
        require(ids==sorted(set(ids)),"PROVIDER_IDENTITY_MISMATCH","unique sorted build references required")
        require(value["authority"]==authority_packet().identity.to_dict(),"AUTHORITY_MISMATCH")
        require(value["constants_packet"]==constants_packet().identity.to_dict(),"CONSTANT_MISMATCH")

    def descriptor(self,operation):
        return Descriptor(self.to_dict()["descriptors"][operation_index(operation)])
