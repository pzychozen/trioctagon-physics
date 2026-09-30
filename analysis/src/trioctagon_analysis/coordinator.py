"""B1 coordinator always ends in a receipt. No attestor injection or success bypass."""
from threading import Lock
from .attestation import CHECKS, unavailable_evidence
from .codec import canonical_bytes
from .digests import InputByteDigest, ManifestDigest, byte_digest, content_digest
from .errors import ProtocolError, require
from .provider import ParentSnapshot, copy_recorded
from .records import AttemptReceipt
from .requests import ParentReference, Request, Selection

_LANE = Lock()

def attempt_inspection(request, catalogue, approval, parent_bytes, *, limits,
                       attempt_id, diagnostic_limit, cancelled=False):
    """One active inspection per process lane; concurrent submissions are refused."""
    require(type(request) is Request and type(diagnostic_limit) is int and diagnostic_limit > 0,
            "INVALID_SCHEMA", "typed request and explicit diagnostic bound required")
    if not _LANE.acquire(blocking=False):
        return AttemptReceipt({"family": "TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT", "schema": "1.0.0",
            "request": request.to_dict(), "request_digest": request.identity.to_dict(),
            "submitted_bytes": None, "attempt_id": attempt_id, "outcome": "REFUSED", "stage": "REQUEST",
            "category": "RESOURCE_LIMIT", "checks_completed": [],
            "checks": {name: {"state": "UNAVAILABLE", "evidence": None, "reason": "Lane already active."}
                       for name in CHECKS}, "producer": None,
            "diagnostic": "Inspection lane already active."[:diagnostic_limit],
            "diagnostic_limit": diagnostic_limit, "staging": "NOT_CREATED"})
    try:
        return _attempt_inspection(request, catalogue, approval, parent_bytes, limits=limits,
            attempt_id=attempt_id, diagnostic_limit=diagnostic_limit, cancelled=cancelled)
    finally:
        _LANE.release()

def _attempt_inspection(request, catalogue, approval, parent_bytes, *, limits,
                       attempt_id, diagnostic_limit, cancelled=False):
    """Exercise bounded validation/copy then refuse issuance pending B2.

    Resource policies are claims; even an APPROVED policy and a hand-constructed
    approval root cannot open the verified lane. There is no attestor argument.
    """
    require(type(request) is Request, "INVALID_SCHEMA", "typed request required")
    require(type(diagnostic_limit) is int and diagnostic_limit > 0 and type(cancelled) is bool,
            "RESOURCE_LIMIT", "explicit diagnostic bound and boolean cancellation required")
    checks = {name: {"state": "UNAVAILABLE", "evidence": None,
                    "reason": "Not independently verified by B1."} for name in CHECKS}
    completed = []
    stage = "APPROVAL"
    evidence = None
    try:
        if cancelled:
            stage = "CANCELLED"
            raise ProtocolError("CANCELLED", "Cancellation accepted before publication.")
        request.validate_context(catalogue, approval)
        completed.append("request_catalogue_approval_bindings")
        policy = catalogue.descriptor.to_dict()["resource_policy"]
        require(policy["state"] == "APPROVED", "RESOURCE_POLICY_UNAPPROVED",
                "Finite production resource policy is not approved.")
        # Explicit inspection budgets cannot broaden the request's declared limits.
        bounds = policy["limits"]
        require(limits.parsing.max_bytes <= bounds["input_bytes"] and
                limits.parsing.max_depth <= bounds["json_depth"] and
                limits.max_samples <= bounds["samples"] and
                diagnostic_limit <= bounds["diagnostic_characters"],
                "RESOURCE_LIMIT", "inspection budget broadens the declared policy")
        stage = "PARENT"
        parent = ParentSnapshot(parent_bytes, limits)
        parent.require_reference(ParentReference(request.to_dict()["parents"][0]))
        completed.append("public_parent_structure_and_bound_bytes")
        checks["inputs_verified"] = {"state": "VERIFIED",
            "evidence": content_digest(ManifestDigest, parent.reference.to_bytes()).to_dict(),
            "reason": "Bound original/canonical/native identities validated; no replay."}
        stage = "COPY"
        payload = copy_recorded(parent, Selection(request.to_dict()["selection"]))
        require(len(payload.to_bytes()) <= bounds["output_bytes"], "RESOURCE_LIMIT", "payload byte limit")
        completed.append("exact_recorded_selection_copy")
        checks["payload_validated"] = {"state": "VERIFIED",
            "evidence": content_digest(ManifestDigest, payload.to_bytes()).to_dict(),
            "reason": "Selected stored tokens copied without scientific computation."}
        stage = "ATTESTATION"
        evidence = unavailable_evidence(request, approval, attempt_id)
        # Unconditional B1 boundary. B2 requires a separately reviewed implementation.
        raise ProtocolError("B1_VERIFIED_LANE_DISABLED",
                            "B1 has no verified execution snapshot, import binding or installed approval deployment.")
    except Exception as failure:
        exc = failure if isinstance(failure, ProtocolError) else ProtocolError(
            "PROVIDER_FAILURE", "Provider attempt failed: " + type(failure).__name__)
        if stage in ("PARENT", "COPY"):
            key = "inputs_verified" if stage == "PARENT" else "payload_validated"
            checks[key] = {"state": "FAILED", "evidence": None, "reason": exc.category}
        return AttemptReceipt({"family": "TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT", "schema": "1.0.0",
            "request": request.to_dict(), "request_digest": request.identity.to_dict(),
            "submitted_bytes": None, "attempt_id": attempt_id,
            "outcome": "CANCELLED" if exc.category == "CANCELLED" else
                       "FAILED" if exc.category == "PROVIDER_FAILURE" else "REFUSED", "stage": stage,
            "category": exc.category, "checks_completed": completed, "checks": checks,
            "producer": evidence.to_dict() if evidence is not None else None,
            "diagnostic": str(exc)[:diagnostic_limit], "diagnostic_limit": diagnostic_limit,
            "staging": "NOT_CREATED"})

def parse_request_or_receipt(raw, parsing_limits, *, attempt_id, diagnostic_limit):
    """Malformed submissions retain their byte identity without inventing a request ID."""
    require(type(raw) is bytes and type(diagnostic_limit) is int and diagnostic_limit > 0,
            "INVALID_SCHEMA", "bounded byte submission required")
    try:
        return Request.from_bytes(raw, parsing_limits)
    except ProtocolError as exc:
        return AttemptReceipt({"family": "TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT", "schema": "1.0.0",
            "request": None, "request_digest": None,
            "submitted_bytes": byte_digest(InputByteDigest, raw).to_dict(), "attempt_id": attempt_id,
            "outcome": "REFUSED", "stage": "REQUEST", "category": exc.category,
            "checks_completed": [], "checks": {name: {"state": "UNAVAILABLE", "evidence": None,
                "reason": "No valid request."} for name in CHECKS}, "producer": None,
            "diagnostic": str(exc)[:diagnostic_limit], "diagnostic_limit": diagnostic_limit,
            "staging": "NOT_CREATED"})
