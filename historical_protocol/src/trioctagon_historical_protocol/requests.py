"""Closed raw-triad request claims; no execution, modules, services or parent conversion."""
from .schema import (s,Document,protocol_schema,omega_schema,literal_tree,number,typed_bytes,
                     PROFILE,CONTRACT,IMPLEMENTATION)
from .packets import K_NAMES,READOUTS,provider_key_schema,authority_packet,constants_packet
from .definitions import operation_index,resolved_constants,numerical_policy
from .digests import (CatalogueDigest,DescriptorDigest,AuthorityDigest,ConstantsDigest,
                      ResourcePolicyDigest,RequestDigest,content_digest)
from .errors import require

_ARGS=(s.obj(k_profile=s.enum(*K_NAMES)),
       s.obj(k_profile=s.enum(*K_NAMES),updates=s.integer,readout=s.enum(*READOUTS)),
       s.obj(q=s.integer,t=s.f64),s.obj(q=s.integer,t=s.f64,memory=s.f64),s.obj())


def body_schema(value,path,integers):
    require(type(value) is dict)
    i=operation_index(value.get("operation"))
    args=value.get("arguments")
    _ARGS[i](args,(*path,"arguments"),integers)
    validator=s.obj(protocol=protocol_schema,operation=s.literal(value["operation"]),revision=s.literal(1),
        profile=s.literal(PROFILE),contract=s.literal(CONTRACT),implementation_policy=s.literal(IMPLEMENTATION),
        catalogue=s.digest(CatalogueDigest),descriptor=s.digest(DescriptorDigest),authority=s.digest(AuthorityDigest),
        constants_packet=s.digest(ConstantsDigest),provider=provider_key_schema,resource_policy=s.digest(ResourcePolicyDigest),
        input=s.obj(kind=s.literal("EXPLICIT_RAW_TRIAD"),omega=omega_schema),arguments=_ARGS[i],
        resolved_constants=literal_tree(resolved_constants(value["operation"],args)),
        numerical_policy=s.literal(numerical_policy(value["operation"],args)))
    validator(value,path,integers)
    if i in (2,3):
        require(args["q"]<12 and number(args["t"])>=0,"INVALID_DOMAIN_ARGUMENT","q/t outside Historical domain")
    if i==3:require(-1<=number(args["memory"])<=1,"INVALID_DOMAIN_ARGUMENT","bounded memory required")
    require(value["authority"]==authority_packet().identity.to_dict(),"AUTHORITY_MISMATCH")
    require(value["constants_packet"]==constants_packet().identity.to_dict(),"CONSTANT_MISMATCH")


projection_schema=s.obj(family=s.literal("TRIOCTAGON_HISTORICAL_ANALYSIS_REQUEST"),schema=s.literal("1.0.0"),body=body_schema)


def request_digest(value):
    projection={key:value[key] for key in ("family","schema","body")}
    return content_digest(RequestDigest,typed_bytes(projection,projection_schema))


class Request(Document):
    __slots__=()
    schema=s.obj(family=s.literal("TRIOCTAGON_HISTORICAL_ANALYSIS_REQUEST"),schema=s.literal("1.0.0"),
                 body=body_schema,request_digest=s.digest(RequestDigest))

    @classmethod
    def validate(cls,value):
        require(value["request_digest"]==request_digest(value).to_dict(),"RESULT_BINDING_FAILURE","request digest differs")

    @property
    def identity(self):
        return request_digest(self.to_dict())

    def validate_context(self,catalogue,resource,build):
        from .catalogue import Catalogue
        from .packets import ResourcePolicy,ProviderBuild
        require(type(catalogue) is Catalogue and type(resource) is ResourcePolicy and type(build) is ProviderBuild)
        q=self.to_dict()["body"]
        c=catalogue.to_dict()
        require(q["catalogue"]==catalogue.identity.to_dict() and q["descriptor"]==catalogue.descriptor(q["operation"]).identity.to_dict(),"AUTHORITY_MISMATCH")
        require(q["resource_policy"]==c["resource_policy"]==resource.identity.to_dict(),"RESOURCE_POLICY_NOT_ADMITTED")
        require(q["provider"] in c["provider_builds"] and q["provider"]["build"]==build.identity.to_dict(),"PROVIDER_IDENTITY_MISMATCH")
