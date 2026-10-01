"""Immutable Historical result/receipt claims. No issuer, coordinator or provider exists."""
from .schema import (s, Document, embedded, literal_tree, protocol_schema, attempt_schema,
    timestamp, typed_bytes, PROFILE, CONTRACT, IMPLEMENTATION)
from .digests import (RequestDigest, CatalogueDigest, DescriptorDigest, AuthorityDigest,
    ConstantsDigest, ResourcePolicyDigest, ProviderBuildDigest, PayloadDigest,
    ExecutionEvidenceDigest, SemanticResultDigest, InputByteDigest, content_digest)
from .requests import Request
from .catalogue import Catalogue
from .packets import (AuthorityPacket, ConstantsPacket, ResourcePolicy, ProviderBuild,
    provider_key_schema, provider_binding_schema, provider_binding, frozen)
from .payloads import Payload
from .definitions import ISSUANCE, OPERATIONS, qualification, qualification_schema
from .evidence import ASSURANCE, CHECKS, ExecutionEvidence, checks_schema
from .errors import CATEGORIES, require

BUNDLE = s.obj(catalogue=embedded(Catalogue),authority_packet=embedded(AuthorityPacket),
    constants_packet=embedded(ConstantsPacket),provider_build=embedded(ProviderBuild),resource_policy=embedded(ResourcePolicy))
BASE = dict(schema=s.literal("1.0.0"),protocol=protocol_schema,profile=s.literal(PROFILE),
            contract=s.literal(CONTRACT),implementation_policy=s.literal(IMPLEMENTATION))
RESULT_FAMILY="TRIOCTAGON_HISTORICAL_DERIVED_ANALYSIS_RECORD"
RECEIPT_FAMILY="TRIOCTAGON_HISTORICAL_ANALYSIS_ATTEMPT_RECEIPT"
SEMANTIC_SCHEMA=s.obj(family=s.literal(RESULT_FAMILY),**BASE,issuance_class=s.literal(ISSUANCE),
    request_digest=s.digest(RequestDigest),catalogue_digest=s.digest(CatalogueDigest),
    descriptor_digest=s.digest(DescriptorDigest),authority_digest=s.digest(AuthorityDigest),
    constants_digest=s.digest(ConstantsDigest),resource_policy_digest=s.digest(ResourcePolicyDigest),
    provider_build_digest=s.digest(ProviderBuildDigest),provider_binding=provider_binding_schema,
    comparison_evidence=literal_tree(frozen("comparison")),payload_digest=s.digest(PayloadDigest),
    qualifications=qualification_schema,assurance=literal_tree(ASSURANCE))


def semantic_projection(value):
    """Project an already schema-validated record; never accept a caller's alternate projection."""
    request=Request(value["request"])
    body=request.to_dict()["body"]
    result={key:value[key] for key in ("family",*BASE,"issuance_class","provider_binding","qualifications","assurance")}
    result.update(request_digest=request.identity.to_dict(),catalogue_digest=body["catalogue"],
        descriptor_digest=body["descriptor"],authority_digest=body["authority"],constants_digest=body["constants_packet"],
        resource_policy_digest=body["resource_policy"],provider_build_digest=body["provider"]["build"],
        comparison_evidence=value["contract_bundle"]["catalogue"]["comparison_evidence"],
        payload_digest=Payload(value["payload"]).identity.to_dict())
    return result


def semantic_digest(value):
    return content_digest(SemanticResultDigest,typed_bytes(semantic_projection(value),SEMANTIC_SCHEMA))


class DerivedRecord(Document):
    """Parsing checks stored structure/bindings, never science, admission or producer execution."""
    __slots__=()
    persisted=True
    schema=s.obj(family=s.literal(RESULT_FAMILY),**BASE,issuance_class=s.literal(ISSUANCE),
        request=embedded(Request),contract_bundle=BUNDLE,provider_binding=provider_binding_schema,
        payload=embedded(Payload),qualifications=qualification_schema,assurance=literal_tree(ASSURANCE),
        execution_evidence=embedded(ExecutionEvidence),completion=s.obj(state=s.literal("COMPLETE"),
            attempt_id=attempt_schema,request_digest=s.digest(RequestDigest),payload_digest=s.digest(PayloadDigest),
            evidence_digest=s.digest(ExecutionEvidenceDigest)),semantic_result_digest=s.digest(SemanticResultDigest),
        metadata=s.obj(created_at=s.text,attempt_id=attempt_schema,submitted_request_bytes=s.digest(InputByteDigest),
            source_locators=s.seq(s.obj(source_id=s.text,locator=s.text))))

    @classmethod
    def validate(cls,value):
        bundle=value["contract_bundle"]
        catalogue=Catalogue(bundle["catalogue"])
        resource=ResourcePolicy(bundle["resource_policy"])
        build=ProviderBuild(bundle["provider_build"])
        request=Request(value["request"])
        payload=Payload(value["payload"])
        evidence=ExecutionEvidence(value["execution_evidence"])
        request.validate_context(catalogue,resource,build)
        payload.validate_request(request)
        require(resource.to_dict()["state"]=="MEASURED_ADMITTED_LOCAL","RESOURCE_POLICY_NOT_ADMITTED")
        evidence.validate_context(request,payload,catalogue,build,resource)
        body=request.to_dict()["body"]
        require(value["provider_binding"]==provider_binding(body["provider"]),"PROVIDER_IDENTITY_MISMATCH")
        require(value["qualifications"]==qualification(body["operation"]),"RESULT_BINDING_FAILURE")
        completion=value["completion"]
        require(completion["request_digest"]==request.identity.to_dict() and completion["payload_digest"]==payload.identity.to_dict()
            and completion["evidence_digest"]==evidence.identity.to_dict(),"RESULT_BINDING_FAILURE")
        metadata=value["metadata"]
        require(completion["attempt_id"]==metadata["attempt_id"]==evidence.to_dict()["attempt_id"],"RESULT_BINDING_FAILURE")
        timestamp(metadata["created_at"])
        ids=[row["source_id"] for row in metadata["source_locators"]]
        a=bundle["authority_packet"]
        allowed={row["id"] for key in ("audits","architecture_protocol","sources") for row in a[key]}
        allowed.update(row["id"] for row in bundle["catalogue"]["comparison_evidence"])
        allowed.add(build.to_dict()["source"]["repository_id"])
        allowed.update(row["id"] for row in build.to_dict()["dependencies"])
        require(ids==sorted(set(ids)) and set(ids)<=allowed,"AUTHORITY_MISMATCH","unknown or unsorted display locator IDs")
        require(value["semantic_result_digest"]==semantic_digest(value).to_dict(),"RESULT_BINDING_FAILURE")
        limits=resource.to_dict()["limits"]
        require(body["operation"]!=OPERATIONS[1] or body["arguments"]["updates"]<=limits["max_updates"],"RESOURCE_LIMIT")
        require(len(request.to_bytes())<=limits["input_bytes"],"RESOURCE_LIMIT")
        require(all(len(owner.to_bytes())<=limits["manifest_bytes"] for owner in (build,evidence,catalogue,
            AuthorityPacket(bundle["authority_packet"]),ConstantsPacket(bundle["constants_packet"]),resource)),"RESOURCE_LIMIT")

    def __init__(self,value):
        super().__init__(value)
        limits=value["contract_bundle"]["resource_policy"]["limits"]
        require(len(self.to_bytes())<=limits["output_bytes"],"RESOURCE_LIMIT")
        # Bound complete artifact nesting using schema data; no scientific replay.
        def depth(item):
            children=item.values() if type(item) is dict else item if type(item) is list else ()
            return (1+max((depth(v) for v in children),default=0)) if type(item) in (dict,list) else 0
        require(depth(value)<=limits["json_depth"],"RESOURCE_LIMIT")

    @property
    def identity(self):
        return SemanticResultDigest.from_dict(self.to_dict()["semantic_result_digest"])


class AttemptReceipt(Document):
    __slots__=()
    persisted=True
    schema=s.obj(family=s.literal(RECEIPT_FAMILY),**BASE,attempt_id=attempt_schema,
        submitted_request_bytes=s.digest(InputByteDigest),request=s.nullable(embedded(Request)),
        request_digest=s.nullable(s.digest(RequestDigest)),outcome=s.enum("REFUSED","FAILED","CANCELLED"),
        stage=s.enum("REQUEST","CONTRACT","INPUT","RESOURCE","COMPUTATION","RESULT_BINDING","PERSISTENCE","CANCELLATION"),
        category=s.enum(*sorted(CATEGORIES)),argument_field=s.nullable(s.enum("omega","q","t","memory","updates","k_profile","readout","resolved_constants")),
        checks=checks_schema(receipt=True),provider=s.nullable(provider_key_schema),updates_completed=s.nullable(s.integer),
        diagnostic=s.text,diagnostic_limit_bytes=s.positive,staging=s.enum("NOT_CREATED","DISCARDED","QUARANTINED"),created_at=s.text)

    @classmethod
    def validate(cls,value):
        timestamp(value["created_at"])
        require(len(value["diagnostic"].encode("utf-8"))<=value["diagnostic_limit_bytes"],"RESOURCE_LIMIT")
        require((value["outcome"]=="CANCELLED")== (value["category"]=="CANCELLED"))
        request=None if value["request"] is None else Request(value["request"])
        require(value["request_digest"]==(None if request is None else request.identity.to_dict()),"RESULT_BINDING_FAILURE")
        if request is None:
            require(value["provider"] is None and value["updates_completed"] is None)
            require(all(value["checks"][key]["state"]!="LOCAL_CHECK_PASSED" for key in ("inputs_bound","payload_validated")))
        else:
            body=request.to_dict()["body"]
            require(value["provider"] is None or value["provider"]==body["provider"],"PROVIDER_IDENTITY_MISMATCH")
            if value["updates_completed"] is not None:
                require(body["operation"]==OPERATIONS[1] and value["stage"] in ("COMPUTATION","RESULT_BINDING","PERSISTENCE","CANCELLATION")
                    and value["updates_completed"]<=body["arguments"]["updates"])
            expected=dict(catalogue_contract_valid=body["catalogue"],historical_authority_bound=body["authority"],
                implementation_build_identified=body["provider"]["build"],participating_kernel_identity=body["provider"]["build"],inputs_bound=request.identity.to_dict())
            require(all(value["checks"][key]["state"]!="LOCAL_CHECK_PASSED" or value["checks"][key]["evidence"]==digest
                        for key,digest in expected.items()),"RESULT_BINDING_FAILURE")
        if value["checks"]["payload_validated"]["state"]=="LOCAL_CHECK_PASSED":
            require(value["stage"] in ("PERSISTENCE","CANCELLATION") and value["staging"]!="NOT_CREATED")

    def validate_context(self,catalogue,resource,build):
        """Optional external context consistency; this never approves the context for execution."""
        value=self.to_dict()
        if value["request"] is not None:
            Request(value["request"]).validate_context(catalogue,resource,build)
