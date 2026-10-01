"""Inert producer observations. Parsing a passed claim performs no scan or execution."""
from .schema import s, Document, embedded, literal_tree, attempt_schema, safe_members, sorted_ids
from .digests import (CatalogueDigest, AuthorityDigest, ProviderBuildDigest, RequestDigest,
    PayloadDigest, InstallationObservationDigest, ExecutionEvidenceDigest)
from .packets import observation_member_schema
from .errors import require, CATEGORIES

ASSURANCE = {
    "artifact_structure_integrity": {"state":"SCHEMA_AND_BINDINGS_VALID", "scientific_equations_replayed":False},
    "mathematical_reconstruction_status": {"state":"HISTORICAL_RECONSTRUCTION_CLAIM", "per_result_math_verification":"NOT_PERFORMED"},
    "producer_execution_attestation": {"state":"UNAVAILABLE", "windows_execution_binding":"NOT_PROVEN", "production_attestation_enabled":False}}
CHECKS = (
    ("catalogue_contract_valid", CatalogueDigest, "HISTORICAL_CATALOGUE_CONTRACT_MATCH"),
    ("historical_authority_bound", AuthorityDigest, "FROZEN_AUTHORITY_PACKET_MATCH"),
    ("implementation_build_identified", ProviderBuildDigest, "DECLARED_INDEPENDENT_BUILD_MATCH"),
    ("installed_content_integrity", InstallationObservationDigest, "UNPROTECTED_BEFORE_AFTER_MEMBER_HASHES_MATCH"),
    ("inputs_bound", RequestDigest, "CANONICAL_REQUEST_AND_INPUT_TOKENS_BOUND"),
    ("payload_validated", PayloadDigest, "SCHEMA_AND_BINDINGS_ONLY_NO_SCIENTIFIC_REPLAY"),
    ("participating_kernel_identity", ProviderBuildDigest, "INDEPENDENT_HISTORICAL_IMPLEMENTATION_IDENTIFIED_CURRENT_NOT_USED"))
UNAVAILABLE = {"state":"UNAVAILABLE", "evidence":None, "reason":"B2_WINDOWS_EXECUTION_BINDING_NOT_PROVEN"}


def checks_schema(receipt=False):
    def check(kind, reason):
        def validate(value, path, integers):
            if receipt:
                s.obj(state=s.enum("NOT_REACHED","LOCAL_CHECK_PASSED","FAILED","UNAVAILABLE"),
                    evidence=s.nullable(s.digest(kind)),reason=s.enum("NOT_REACHED",reason,*sorted(CATEGORIES)))(value,path,integers)
                if value["state"]=="LOCAL_CHECK_PASSED":
                    require(value["evidence"] is not None and value["reason"]==reason)
                elif value["state"]=="NOT_REACHED":
                    require(value["evidence"] is None and value["reason"]=="NOT_REACHED")
                else:
                    require(value["reason"] in CATEGORIES)
            else:
                s.obj(state=s.literal("LOCAL_CHECK_PASSED"),evidence=s.digest(kind),reason=s.literal(reason))(value,path,integers)
        return validate
    return s.obj(**{name:check(kind,reason) for name,kind,reason in CHECKS},
                 execution_snapshot_attestation=literal_tree(UNAVAILABLE))


class InstallationObservation(Document):
    __slots__=()
    digest_type=InstallationObservationDigest
    schema=s.obj(method=s.literal("UNPROTECTED_INSTALLED_MEMBER_HASH_SCAN"),
        before=s.seq(observation_member_schema,1),after=s.seq(observation_member_schema,1),
        match=s.literal("MATCH"),protected_during_execution=s.literal(False))

    @classmethod
    def validate(cls,value):
        safe_members(value["before"])
        safe_members(value["after"])
        require(value["before"]==value["after"],"PROVIDER_IDENTITY_MISMATCH")


class ExecutionEvidence(Document):
    __slots__=()
    digest_type=ExecutionEvidenceDigest
    schema=s.obj(schema=s.literal("HISTORICAL_EXECUTION_EVIDENCE_1"),
        method=s.literal("LOCAL_OBSERVATIONS_WITHOUT_EXECUTION_ATTESTATION"),
        attempt_id=attempt_schema,request_digest=s.digest(RequestDigest),payload_digest=s.digest(PayloadDigest),
        provider_build=s.digest(ProviderBuildDigest),installation_observation=embedded(InstallationObservation),
        runtime=s.obj(implementation=s.text,version=s.text,platform=s.text,architecture=s.text,
            numeric_libraries=s.seq(s.obj(id=s.text,version=s.text,manifest_sha256=s.hex256)),
            rounding_mode=s.literal("NEAREST_EVEN"),subnormal_mode=s.literal("GRADUAL")),
        resource_observation=s.obj(method=s.literal("LOCAL_MONITOR_OBSERVATION_NOT_EXECUTION_ATTESTATION"),
            wall_milliseconds=s.integer,peak_memory_bytes=s.integer),checks=checks_schema())

    @classmethod
    def validate(cls,value):
        sorted_ids(value["runtime"]["numeric_libraries"])
        expected={"installed_content_integrity":InstallationObservation(value["installation_observation"]).identity.to_dict(),
            "inputs_bound":value["request_digest"],"payload_validated":value["payload_digest"],
            "implementation_build_identified":value["provider_build"],"participating_kernel_identity":value["provider_build"]}
        require(all(value["checks"][key]["evidence"]==digest for key,digest in expected.items()),"RESULT_BINDING_FAILURE")

    def validate_context(self,request,payload,catalogue,build,resource):
        value=self.to_dict()
        require(value["request_digest"]==request.identity.to_dict() and value["payload_digest"]==payload.identity.to_dict()
            and value["provider_build"]==build.identity.to_dict(),"RESULT_BINDING_FAILURE")
        require(value["checks"]["catalogue_contract_valid"]["evidence"]==catalogue.identity.to_dict() and
            value["checks"]["historical_authority_bound"]["evidence"]==request.to_dict()["body"]["authority"],"RESULT_BINDING_FAILURE")
        b=build.to_dict()
        members=[{key:row[key] for key in ("path","bytes","sha256")} for row in b["members"]]
        require(value["installation_observation"]["before"]==members,"PROVIDER_IDENTITY_MISMATCH")
        libraries=[{key:row[key] for key in ("id","version","manifest_sha256")}
                   for row in b["dependencies"] if row["role"]=="NUMERIC_LIBRARY"]
        require(value["runtime"]["numeric_libraries"]==libraries,"PROVIDER_IDENTITY_MISMATCH")
        limits=resource.to_dict()["limits"]
        require(limits is not None,"RESOURCE_POLICY_NOT_ADMITTED")
        observed=value["resource_observation"]
        require(observed["wall_milliseconds"]<=limits["wall_milliseconds"] and
            observed["peak_memory_bytes"]<=limits["memory_bytes"],"RESOURCE_LIMIT")
