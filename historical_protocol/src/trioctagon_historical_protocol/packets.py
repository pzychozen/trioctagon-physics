"""Immutable authority/literal packets and inert policy/build schemas. No admission."""
import copy
import json
import re
from importlib.resources import files

from .schema import (s, Document, embedded, omega_schema, vector_schema, PROFILE,
                     CONTRACT, IMPLEMENTATION, safe_members, sorted_ids)
from .digests import (AuthorityDigest, ConstantsDigest, BasisDigest, ManifestDigest,
                      ResourcePolicyDigest, ProviderBuildDigest, ConformanceDigest)
from .errors import require

_DATA = {name: files(__package__).joinpath("data", name + ".json").read_bytes()
         for name in ("authority", "constants", "comparison")}


def frozen(name):
    return json.loads(_DATA[name])


K_NAMES = ("HISTORICAL_THETA_SCALED", "HISTORICAL_THETA_SOFT", "HISTORICAL_SIMPLE")
READOUTS = ("NONE", "HISTORICAL_STAGED_Z_K", "HISTORICAL_COGNITIVE_EMA_Z_H")
NUMERICAL_POLICIES = ("H5_INDEPENDENT_STEP_1", "H5_INDEPENDENT_RUN_NONE_1",
    "H5_INDEPENDENT_RUN_K_1", "H5_INDEPENDENT_RUN_H_1", "H5_INDEPENDENT_STAGED_1",
    "H5_INDEPENDENT_EMA_1", "H4_LEGACY_NAIVE_BINARY64_FINITE_WITH_UNDERFLOW_FLAGS_1")
identity_row = s.obj(id=s.text, sha256=s.hex256)
dynamics_schema = s.obj(epsilon=s.f64, g=s.f64, k=vector_schema, phase_strength=s.f64,
                       harmonic=s.literal(3), delta=omega_schema, sigma=s.f64)
clock_schema = s.obj(sectors=s.literal(12), q_step=s.literal(1), dt=s.f64, pi=s.f64)
staged_schema = s.obj(lambda_vp=s.f64, gamma=s.f64, theta_lock=s.f64, alpha=s.f64,
                      beta=s.f64, harmonic=s.literal(3))
ema_schema = s.obj(lambda_vp=s.f64, theta_lock=s.f64, alpha=s.f64, beta=s.f64,
                   harmonic=s.literal(3), innovation=s.f64, retention=s.f64)
chart_schema = s.obj(basis_order=s.seq(s.text,3,3), basis_rows=s.seq(vector_schema,3,3),
                     basis_digest=s.digest(BasisDigest))


class AuthorityPacket(Document):
    __slots__ = ()
    digest_type = AuthorityDigest
    schema = s.obj(family=s.literal("TRIOCTAGON_HISTORICAL_AUTHORITY_PACKET"),
        schema=s.literal("1.0.0"), contract=s.literal(CONTRACT), implementation_policy=s.literal(IMPLEMENTATION),
        audits=s.seq(identity_row,5,5), architecture_protocol=s.seq(identity_row,3,3),
        amendment_sha256=s.hex256, h5_contract_sha256=s.hex256, constants_source_sha256=s.hex256,
        sources=s.seq(s.obj(id=s.text,sha256=s.hex256,snapshot=s.text),5,5))

    @classmethod
    def validate(cls, value):
        require(value == frozen("authority"), "AUTHORITY_MISMATCH", "accepted H0-H5/amendment/source packet differs")


class ConstantsPacket(Document):
    __slots__ = ()
    digest_type = ConstantsDigest
    schema = s.obj(family=s.literal("TRIOCTAGON_HISTORICAL_CONSTANTS_PACKET"),
        schema=s.literal("1.0.0"),contract=s.literal(CONTRACT),source_packet_sha256=s.hex256,
        profiles=s.obj(**{name:dynamics_schema for name in K_NAMES}),clock=clock_schema,
        staged=staged_schema,ema=ema_schema,chart=chart_schema)

    @classmethod
    def validate(cls, value):
        require(value == frozen("constants"), "CONSTANT_MISMATCH", "frozen literal tokens differ")


def authority_packet():
    return AuthorityPacket(frozen("authority"))


def constants_packet():
    return ConstantsPacket(frozen("constants"))


class ResourcePolicy(Document):
    __slots__ = ()
    digest_type = ResourcePolicyDigest
    schema = s.obj(family=s.literal("TRIOCTAGON_HISTORICAL_RESOURCE_POLICY"),schema=s.literal("1.0.0"),
        state=s.enum("MEASUREMENT_REQUIRED_BEFORE_ADMISSION","MEASURED_ADMITTED_LOCAL"),
        measurement_manifest=s.nullable(s.digest(ManifestDigest)),
        limits=s.nullable(s.obj(max_updates=s.integer,input_bytes=s.positive,output_bytes=s.positive,
            json_depth=s.positive,wall_milliseconds=s.positive,memory_bytes=s.positive,
            diagnostic_bytes=s.positive,manifest_bytes=s.positive)))

    @classmethod
    def validate(cls, value):
        pending=value["state"]=="MEASUREMENT_REQUIRED_BEFORE_ADMISSION"
        require(value["limits"] is None if pending else value["limits"] is not None and value["measurement_manifest"] is not None,
                "RESOURCE_POLICY_NOT_ADMITTED", "policy state and limits disagree")


def default_resource_policy():
    return ResourcePolicy(dict(family="TRIOCTAGON_HISTORICAL_RESOURCE_POLICY",schema="1.0.0",
        state="MEASUREMENT_REQUIRED_BEFORE_ADMISSION",measurement_manifest=None,limits=None))


provider_key_schema = s.obj(id=s.literal("historical.reference"),revision=s.literal(1),build=s.digest(ProviderBuildDigest))
member_schema = s.obj(path=s.text,bytes=s.integer,sha256=s.hex256,
                     role=s.enum("SCIENTIFIC_IMPLEMENTATION","GENERIC_INFRASTRUCTURE","PACKAGE_METADATA"))
observation_member_schema = s.obj(path=s.text,bytes=s.integer,sha256=s.hex256)


class ProviderBuild(Document):
    """A build claim, not a real admitted provider. H6A supplies no runtime instance."""
    __slots__ = ()
    digest_type = ProviderBuildDigest
    schema = s.obj(family=s.literal("TRIOCTAGON_HISTORICAL_PROVIDER_BUILD"),schema=s.literal("1.0.0"),
        provider_id=s.literal("historical.reference"),provider_revision=s.literal(1),
        implementation_policy=s.literal(IMPLEMENTATION),
        source=s.obj(repository_id=s.text,revision=s.nullable(s.revision),content_manifest_digest=s.digest(ManifestDigest)),
        archive_sha256=s.hex256,members=s.seq(member_schema,1),
        dependencies=s.seq(s.obj(id=s.text,version=s.text,manifest_sha256=s.hex256,
            role=s.enum("RUNTIME","NUMERIC_LIBRARY","NONSCIENTIFIC_INFRASTRUCTURE"))),
        numerical_policy_ids=s.seq(s.text,len(NUMERICAL_POLICIES),len(NUMERICAL_POLICIES)),
        conformance_digest=s.digest(ConformanceDigest))

    @classmethod
    def validate(cls, value):
        safe_members(value["members"])
        sorted_ids(value["dependencies"])
        require(value["numerical_policy_ids"]==list(NUMERICAL_POLICIES))
        require(any(m["role"]=="SCIENTIFIC_IMPLEMENTATION" for m in value["members"]),
                "PROVIDER_IDENTITY_MISMATCH", "independent scientific member identity required")
        forbidden={"kernel-physics","kernel-to","torment-service","trioctagon-physics"}
        require(not any(re.sub(r"[-_.]+", "-", d["id"].lower()) in forbidden for d in value["dependencies"]),
                "FORBIDDEN_SCIENTIFIC_DELEGATION", "forbidden scientific dependency claim")


def provider_binding(provider):
    return dict(provider=copy.deepcopy(provider),strategy="CLEAN_INDEPENDENT_REIMPLEMENTATION",
                current_kernel_role="NOT_USED",scientific_delegations=[])


provider_binding_schema = s.obj(provider=provider_key_schema,strategy=s.literal("CLEAN_INDEPENDENT_REIMPLEMENTATION"),
    current_kernel_role=s.literal("NOT_USED"),scientific_delegations=s.seq(s.text,0,0))
