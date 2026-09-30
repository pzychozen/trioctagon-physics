"""Strict inert artifact codecs. Loading an evidence claim is not authenticating it."""
from datetime import datetime

from . import schema as s
from .approval import ApprovalRoot
from .attestation import ProducerEvidence, attempt_id_schema, checks_schema
from .catalogue import Catalogue
from .codec import canonical_bytes
from .common import authority_schema, embedded, status_schema
from .constants import QUALIFICATION, REPRODUCIBILITY
from .digests import (EvidenceDigest, InputByteDigest, PayloadDigest, RequestDigest,
                      SemanticResultDigest, content_digest)
from .errors import CATEGORIES, require
from .provider import CopyPayload, verify_copy
from .requests import ParentReference, Request, Selection

def semantic_result_digest(value):
    """Closed scientific/provenance projection; receipt and environment are full-only."""
    from .common import ProducerBuild
    from .digests import ManifestDigest
    request = Request(value["request"])
    payload = CopyPayload(value["result"])
    build = ProducerBuild(value["producer"]["build"])
    # All nested integer-containing objects were validated; represent them as
    # canonical JSON strings here, avoiding untyped generic integer traversal.
    body = {"family": "TRIOCTAGON_DERIVED_ANALYSIS_RECORD", "schema": "1.0.0",
        "profile": "CORE", "request": request.identity.to_dict(),
        "catalogue": Catalogue(value["catalogue"]).identity.to_dict(),
        "producer_build": build.identity.to_dict(),
        "kernel": value["producer"]["kernel"], "kernel_roles": ["parent_validation"],
        "parents": value["parents"], "result_payload": payload.to_bytes().decode("utf-8"),
        "authority": value["authority"], "statuses": value["statuses"],
        "qualification": value["qualification"], "reproducibility": value["reproducibility"],
        "warnings": value["warnings"]}
    return content_digest(SemanticResultDigest, canonical_bytes(body))

class DerivedAnalysisRecord(s.Document):
    """Core-profile claims only. No producer or verified-execution factory exists in B1."""
    __slots__ = ()
    schema = s.obj(family=s.literal("TRIOCTAGON_DERIVED_ANALYSIS_RECORD"),
        schema=s.literal("1.0.0"), profile=s.literal("CORE"),
        catalogue=embedded(Catalogue), approval=embedded(ApprovalRoot),
        request=embedded(Request), request_digest=s.digest(RequestDigest),
        parents=s.seq(embedded(ParentReference), 1, 1),
        producer=embedded(ProducerEvidence), authority=authority_schema, statuses=status_schema,
        result=embedded(CopyPayload), qualification=s.literal(QUALIFICATION),
        reproducibility=s.literal(REPRODUCIBILITY), warnings=s.seq(s.text, 0, 0),
        semantic_result_digest=s.digest(SemanticResultDigest),
        completion=s.obj(state=s.literal("COMPLETE"), attempt_id=attempt_id_schema,
            request=s.digest(RequestDigest), payload=s.digest(PayloadDigest),
            evidence=s.digest(EvidenceDigest), started_at=s.text, completed_at=s.text))

    @classmethod
    def validate(cls, value):
        request = Request(value["request"])
        catalogue, approval = Catalogue(value["catalogue"]), ApprovalRoot(value["approval"])
        request.validate_context(catalogue, approval)
        descriptor = catalogue.descriptor.to_dict()
        require(descriptor["resource_policy"]["state"] == "APPROVED",
                "RESOURCE_POLICY_UNAPPROVED", "successful record claims require approved finite limits")
        require(value["request_digest"] == request.identity.to_dict() and
                value["parents"] == value["request"]["parents"],
                "RESULT_BINDING_MISMATCH", "request/parent binding mismatch")
        payload = CopyPayload(value["result"])
        selected = value["request"]["selection"]
        result = value["result"]
        require((result["ordinal"], result["update_index"], [r["field"] for r in result["fields"]]) ==
                (selected["ordinal"], selected["expected_update_index"], selected["fields"]),
                "RESULT_BINDING_MISMATCH", "payload selection differs from request")
        evidence = ProducerEvidence(value["producer"])
        evidence.require_verified_claim(request, approval, payload)
        require(value["authority"] == descriptor["authority"] and value["statuses"] == descriptor["statuses"],
                "SCIENTIFIC_OVERCLAIM", "result authority/status differs from reviewed catalogue")
        completion = value["completion"]
        require(completion["attempt_id"] == value["producer"]["attempt_id"] and
                completion["request"] == request.identity.to_dict() and
                completion["payload"] == payload.identity.to_dict() and
                completion["evidence"] == evidence.identity.to_dict(),
                "RESULT_BINDING_MISMATCH", "completion receipt mismatch")
        try:
            start, end = (datetime.fromisoformat(completion[k]) for k in ("started_at", "completed_at"))
            valid = start.tzinfo is not None and end.tzinfo is not None and start <= end
        except (ValueError, TypeError):
            valid = False
        require(valid, "INVALID_SCHEMA", "bounded chronological timezone-aware completion timestamps required")
        require(value["semantic_result_digest"] == semantic_result_digest(value).to_dict(),
                "INVALID_SCHEMA", "semantic result digest mismatch")

    def verify_parent_copy(self, parent):
        value = self.to_dict()
        parent.require_reference(ParentReference(value["parents"][0]))
        verify_copy(CopyPayload(value["result"]), parent, Selection(value["request"]["selection"]))

class AttemptReceipt(s.Document):
    __slots__ = ()
    schema = s.obj(family=s.literal("TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT"),
        schema=s.literal("1.0.0"), request=s.nullable(embedded(Request)),
        request_digest=s.nullable(s.digest(RequestDigest)),
        submitted_bytes=s.nullable(s.digest(InputByteDigest)), attempt_id=attempt_id_schema,
        outcome=s.enum("REFUSED", "FAILED", "CANCELLED"),
        stage=s.enum("REQUEST", "APPROVAL", "PARENT", "COPY", "ATTESTATION", "PERSISTENCE", "CANCELLED"),
        category=s.enum(*sorted(CATEGORIES)), checks_completed=s.seq(s.text),
        checks=checks_schema, producer=s.nullable(embedded(ProducerEvidence)),
        diagnostic=s.text, diagnostic_limit=s.positive,
        staging=s.enum("NOT_CREATED", "DISCARDED", "QUARANTINED"))

    @classmethod
    def validate(cls, value):
        request = value["request"]
        expected = Request(request).identity.to_dict() if request is not None else None
        require(value["request_digest"] == expected, "RESULT_BINDING_MISMATCH", "receipt request identity mismatch")
        if request is None:
            require(value["stage"] == "REQUEST" and value["submitted_bytes"] is not None and
                    value["producer"] is None and not value["checks_completed"] and
                    all(c["state"] != "VERIFIED" for c in value["checks"].values()),
                    "RESULT_BINDING_MISMATCH", "unparsed request cannot claim completed verification")
        require(len(value["diagnostic"]) <= value["diagnostic_limit"],
                "RESOURCE_LIMIT", "receipt diagnostic exceeds explicit bound")
        require(len(value["checks_completed"]) == len(set(value["checks_completed"])),
                "INVALID_SCHEMA", "duplicate completed check")
        require((value["outcome"] == "CANCELLED") == (value["category"] == "CANCELLED"),
                "INVALID_SCHEMA", "cancellation outcome/category mismatch")
        for check in value["checks"].values():
            require(check["state"] != "VERIFIED" or check["evidence"] is not None,
                    "UNVERIFIED_PRODUCER", "receipt verified check needs evidence")
        if value["producer"] is not None:
            require(request is not None and value["producer"]["request"] == expected and
                    value["producer"]["attempt_id"] == value["attempt_id"],
                    "RESULT_BINDING_MISMATCH", "receipt producer binding mismatch")
