"""Closed shared identity/policy schemas, distinct from Core record classes."""
from . import schema as s
from .digests import (InputByteDigest, ManifestDigest, PolicyDigest, ProducerBuildIdentity,
                      content_digest)
from .errors import require

def embedded(cls):
    def validate(value, path, integers):
        cls.schema(value, path, integers)
        cls.validate(value)
    return validate

provider_schema = s.obj(id=s.literal("core.app04.recorded_copy"), revision=s.literal(1),
                       build=s.digest(ProducerBuildIdentity))

authority_schema = s.seq(s.obj(id=s.text, edition=s.text, locator=s.text,
                              sha256=s.hex256, qualification=s.text), 1)
status_schema = s.seq(s.obj(subject=s.text, status=s.enum(
    "CURRENT_ACCEPTED_MATH", "HISTORICAL_RECONSTRUCTED_MATH", "EXPERIMENTAL_ENGINE",
    "EMPIRICAL_FINITE_HISTORY", "MODEL_CHOICE", "OPEN_PHYSICAL_INTERFACE",
    "PUBLICATION_EVIDENCE", "INFRASTRUCTURE", "UNKNOWN_REQUIRES_REVIEW")), 1)

class ResourcePolicy(s.Document):
    __slots__ = ()
    schema = s.obj(
        state=s.enum("PROPOSED", "APPROVED"),
        proposal=s.digest(ManifestDigest),
        logical=s.obj(parents=s.literal(1), sample_ordinals=s.literal(1),
            fields_min=s.literal(1), fields_max=s.literal(16), numeric_leaves=s.literal(20),
            external_data=s.literal(0), concurrent_jobs=s.literal(1)),
        limits=s.nullable(s.obj(input_bytes=s.positive, samples=s.positive,
            json_depth=s.positive, output_bytes=s.positive, wall_milliseconds=s.positive,
            memory_bytes=s.positive, diagnostic_characters=s.positive)))

    @classmethod
    def validate(cls, value):
        require(value["state"] != "APPROVED" or value["limits"] is not None,
                "RESOURCE_POLICY_UNAPPROVED", "approved policy requires every finite limit")

    @property
    def identity(self):
        return content_digest(PolicyDigest, self.to_bytes())

class KernelSelection(s.Document):
    __slots__ = ()
    schema = s.obj(distribution=s.literal("trioctagon-physics"), version=s.literal("0.1.0"),
        source_repository=s.text, source_revision=s.revision,
        lock=s.digest(InputByteDigest), actual_archive=s.digest(InputByteDigest),
        selection=s.enum("PREFERRED_EXACT_ARCHIVE", "CERTIFIED_RECONSTRUCTION"),
        stable_members=s.digest(ManifestDigest), certification=s.digest(ManifestDigest))

class ProducerBuild(s.Document):
    __slots__ = ()
    schema = s.obj(distribution=s.literal("trioctagon-analysis"), version=s.literal("0.1.0"),
        provider_id=s.literal("core.app04.recorded_copy"), provider_revision=s.literal(1),
        entry_point=s.literal("trioctagon_analysis.provider:copy_recorded"),
        source=s.obj(repository=s.text, revision=s.revision, content=s.digest(ManifestDigest)),
        archive=s.digest(InputByteDigest), build_inputs=s.digest(ManifestDigest),
        dependency_policy=s.digest(PolicyDigest), runtime_policy=s.digest(PolicyDigest),
        members=s.seq(s.obj(path=s.text, size=s.positive, digest=s.digest(InputByteDigest)), 1))

    @classmethod
    def validate(cls, value):
        paths = [v["path"] for v in value["members"]]
        require(paths == sorted(set(paths)) and len({p.casefold() for p in paths}) == len(paths),
                "WRONG_PRODUCER", "member paths must be sorted, unique and case-disjoint")
        for path in paths:
            require(not path.startswith("/") and "\\" not in path and ":" not in path and
                    all(p not in ("", ".", "..") and p == p.rstrip(" .") for p in path.split("/")),
                    "WRONG_PRODUCER", "unsafe member path")

    @property
    def identity(self):
        return content_digest(ProducerBuildIdentity, self.to_bytes())

source_claims_schema = s.obj(repository=s.text, commit=s.revision, package_version=s.text,
    api_version=s.literal("1.0.0"), tracked_dirty=s.boolean,
    modules=s.seq(s.obj(path=s.text, sha256=s.hex256), 14, 14))
