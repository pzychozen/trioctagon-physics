"""Artifact assembly after actual local checks; this module performs no scientific work."""
from datetime import datetime, timezone
from trioctagon_historical_protocol.schema import PROTOCOL,PROFILE,CONTRACT,IMPLEMENTATION
from trioctagon_historical_protocol.definitions import ISSUANCE,qualification
from trioctagon_historical_protocol.digests import InputByteDigest,byte_digest
from trioctagon_historical_protocol.packets import authority_packet,constants_packet,provider_binding,ProviderBuild
from trioctagon_historical_protocol.catalogue import Catalogue
from trioctagon_historical_protocol.evidence import ASSURANCE,CHECKS,UNAVAILABLE,ExecutionEvidence,InstallationObservation
from trioctagon_historical_protocol.records import DerivedRecord,AttemptReceipt,semantic_digest,RESULT_FAMILY,RECEIPT_FAMILY

BASE=dict(schema="1.0.0",protocol=PROTOCOL,profile=PROFILE,contract=CONTRACT,implementation_policy=IMPLEMENTATION)


def not_reached():
    return {**{name:dict(state="NOT_REACHED",evidence=None,reason="NOT_REACHED") for name,_,_ in CHECKS},
            "execution_snapshot_attestation":dict(UNAVAILABLE)}


def complete_claim(request,payload,admission,attempt,raw,before,after,wall_ms,peak_bytes):
    """Private worker assembly; caller supplies observations it actually performed."""
    a=admission.to_dict();b=ProviderBuild(a["build"]);c=Catalogue(a["catalogue"])
    observation=InstallationObservation(dict(method="UNPROTECTED_INSTALLED_MEMBER_HASH_SCAN",before=before,after=after,
        match="MATCH",protected_during_execution=False))
    digests=(c.identity,authority_packet().identity,b.identity,observation.identity,request.identity,payload.identity,b.identity)
    checks={name:dict(state="LOCAL_CHECK_PASSED",evidence=digest.to_dict(),reason=reason)
            for (name,_,reason),digest in zip(CHECKS,digests)}
    checks["execution_snapshot_attestation"]=dict(UNAVAILABLE)
    libraries=[{key:row[key] for key in ("id","version","manifest_sha256")} for row in a["build"]["dependencies"] if row["role"]=="NUMERIC_LIBRARY"]
    evidence=ExecutionEvidence(dict(schema="HISTORICAL_EXECUTION_EVIDENCE_1",method="LOCAL_OBSERVATIONS_WITHOUT_EXECUTION_ATTESTATION",
        attempt_id=attempt,request_digest=request.identity.to_dict(),payload_digest=payload.identity.to_dict(),provider_build=b.identity.to_dict(),
        installation_observation=observation.to_dict(),runtime=dict(**a["runtime"],numeric_libraries=libraries,
            rounding_mode="NEAREST_EVEN",subnormal_mode="GRADUAL"),
        resource_observation=dict(method="LOCAL_MONITOR_OBSERVATION_NOT_EXECUTION_ATTESTATION",wall_milliseconds=wall_ms,peak_memory_bytes=peak_bytes),checks=checks))
    if any(len(value.to_bytes())>a['resource']['limits']['manifest_bytes'] for value in (b,evidence,observation)):
        raise MemoryError('embedded build/evidence manifest limit')
    body=request.to_dict()["body"]
    record=dict(family=RESULT_FAMILY,**BASE,issuance_class=ISSUANCE,request=request.to_dict(),
        contract_bundle=dict(catalogue=a["catalogue"],authority_packet=authority_packet().to_dict(),constants_packet=constants_packet().to_dict(),
            provider_build=a["build"],resource_policy=a["resource"]),provider_binding=provider_binding(body["provider"]),payload=payload.to_dict(),
        qualifications=qualification(body["operation"]),assurance=ASSURANCE,execution_evidence=evidence.to_dict(),
        completion=dict(state="COMPLETE",attempt_id=attempt,request_digest=request.identity.to_dict(),payload_digest=payload.identity.to_dict(),evidence_digest=evidence.identity.to_dict()),
        metadata=dict(created_at=datetime.now(timezone.utc).isoformat(),attempt_id=attempt,
            submitted_request_bytes=byte_digest(InputByteDigest,raw).to_dict(),source_locators=[]))
    record["semantic_result_digest"]=semantic_digest(record).to_dict()
    return DerivedRecord(record)


def receipt(raw,request,attempt,category,stage,progress,limit,*,checks=None,staging="NOT_CREATED",diagnostic=None):
    diagnostic=category if diagnostic is None else diagnostic
    diagnostic=diagnostic.encode("utf-8")[:limit].decode("utf-8",errors="ignore") or "?"
    body=None if request is None else request.to_dict()["body"]
    is_run=body is not None and body["operation"]=="historical.triad.run.inspect"
    reached=stage in ("COMPUTATION","RESULT_BINDING","PERSISTENCE","CANCELLATION")
    return AttemptReceipt(dict(family=RECEIPT_FAMILY,**BASE,attempt_id=attempt,
        submitted_request_bytes=byte_digest(InputByteDigest,raw).to_dict(),request=None if request is None else request.to_dict(),
        request_digest=None if request is None else request.identity.to_dict(),outcome="CANCELLED" if category=="CANCELLED" else "FAILED" if reached else "REFUSED",
        stage=stage,category=category,argument_field=None,checks=not_reached() if checks is None else checks,
        provider=None if body is None else body["provider"],updates_completed=progress if is_run and reached else None,
        diagnostic=diagnostic,diagnostic_limit_bytes=limit,staging=staging,created_at=datetime.now(timezone.utc).isoformat()))
