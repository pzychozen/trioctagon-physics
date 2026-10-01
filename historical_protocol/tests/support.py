"""TEST_ONLY synthetic claims: no provider exists and no scientific equation was run."""
from copy import deepcopy
from trioctagon_historical_protocol.schema import PROTOCOL, PROFILE, CONTRACT, IMPLEMENTATION, ZERO
from trioctagon_historical_protocol import digests as d
from trioctagon_historical_protocol.packets import *
from trioctagon_historical_protocol.definitions import *
from trioctagon_historical_protocol.catalogue import Catalogue, Descriptor
from trioctagon_historical_protocol.requests import Request, request_digest
from trioctagon_historical_protocol.payloads import Payload, TERMINAL
from trioctagon_historical_protocol.evidence import ASSURANCE, CHECKS, UNAVAILABLE, InstallationObservation, ExecutionEvidence
from trioctagon_historical_protocol.records import RESULT_FAMILY, RECEIPT_FAMILY, semantic_digest

TEST_ONLY = "Synthetic H6A schema claims. No scientific computation, build admission, installation scan or execution occurred."
BASE=dict(schema="1.0.0",protocol=PROTOCOL,profile=PROFILE,contract=CONTRACT,implementation_policy=IMPLEMENTATION)
OMEGA=[dict(real={"f64":"0x1.0000000000000p+0"},imag={"f64":"-0x0.0p+0"}) for _ in range(3)]
TOKEN={"f64":"0x1.0000000000000p-1"}


def fake(kind, digit="a"):
    return kind(digit*64).to_dict()


def context():
    build=ProviderBuild(dict(family="TRIOCTAGON_HISTORICAL_PROVIDER_BUILD",schema="1.0.0",
        provider_id="historical.reference",provider_revision=1,implementation_policy=IMPLEMENTATION,
        source=dict(repository_id="TEST_ONLY_NO_IMPLEMENTATION",revision=None,content_manifest_digest=fake(d.ManifestDigest)),
        archive_sha256="a"*64,members=[dict(path="TEST_ONLY_NO_SCIENCE.txt",bytes=0,sha256="b"*64,role="SCIENTIFIC_IMPLEMENTATION")],
        dependencies=[],numerical_policy_ids=list(NUMERICAL_POLICIES),conformance_digest=fake(d.ConformanceDigest)))
    resource=ResourcePolicy(dict(family="TRIOCTAGON_HISTORICAL_RESOURCE_POLICY",schema="1.0.0",state="MEASURED_ADMITTED_LOCAL",
        measurement_manifest=fake(d.ManifestDigest),limits=dict(max_updates=100,input_bytes=1000000,output_bytes=2000000,
        json_depth=64,wall_milliseconds=1000,memory_bytes=1000000,diagnostic_bytes=256,manifest_bytes=500000)))
    key=dict(id="historical.reference",revision=1,build=build.identity.to_dict())
    catalogue=Catalogue(dict(family="TRIOCTAGON_HISTORICAL_ANALYSIS_CATALOGUE",**BASE,authority=authority_packet().identity.to_dict(),
        constants_packet=constants_packet().identity.to_dict(),provider_builds=[key],resource_policy=resource.identity.to_dict(),
        descriptors=[descriptor_template(op) for op in OPERATIONS],comparison_evidence=frozen("comparison")))
    return catalogue,resource,build,key


def request(i=0,readout="NONE",updates=2,k_profile=K_NAMES[0],omega=None):
    catalogue,resource,build,key=context()
    args=(dict(k_profile=k_profile),dict(k_profile=k_profile,updates=updates,readout=readout),
        dict(q=3,t=TOKEN),dict(q=3,t=TOKEN,memory=TOKEN),{})[i]
    body=dict(protocol=PROTOCOL,operation=OPERATIONS[i],revision=1,profile=PROFILE,contract=CONTRACT,
        implementation_policy=IMPLEMENTATION,catalogue=catalogue.identity.to_dict(),descriptor=catalogue.descriptor(OPERATIONS[i]).identity.to_dict(),
        authority=authority_packet().identity.to_dict(),constants_packet=constants_packet().identity.to_dict(),provider=key,
        resource_policy=resource.identity.to_dict(),input=dict(kind="EXPLICIT_RAW_TRIAD",omega=OMEGA if omega is None else omega),
        arguments=args,resolved_constants=resolved_constants(OPERATIONS[i],args),numerical_policy=numerical_policy(OPERATIONS[i],args))
    value=dict(family="TRIOCTAGON_HISTORICAL_ANALYSIS_REQUEST",schema="1.0.0",body=body)
    value["request_digest"]=request_digest(value).to_dict()
    return Request(deepcopy(value))


def sample(index,mode,omega,terminal=False):
    value=dict(update_index=index,omega=omega,q=index%12,t=ZERO if index==0 else TOKEN,
        initialization="CONSTRUCTOR_INITIAL" if index==0 else "AFTER_UPDATE")
    value.update({"label":TERMINAL} if terminal else {"row_ordinal":index})
    if mode!="NONE":
        value["readout"]=dict(profile=mode,initialization="HISTORICAL_CONSTRUCTOR_ZERO" if index==0 else "RECOMPUTED",
            z=ZERO if index==0 else TOKEN,M=[ZERO]*3,C=[ZERO]*3,T=[ZERO]*3)
        if mode==READOUTS[2]:value["readout"].update(memory=ZERO if index==0 else TOKEN,memory_update_count=index)
    return value


def payload(q):
    b=q.to_dict()["body"]
    i=OPERATIONS.index(b["operation"])
    a=b["arguments"]
    value=dict(schema=PAYLOAD_SCHEMAS[i],operation=b["operation"],revision=1,input_omega=b["input"]["omega"],
        resolved_constants=b["resolved_constants"],numerical_policy=b["numerical_policy"],authority_digest=b["authority"],
        provider_binding=provider_binding(b["provider"]),qualifications=qualification(b["operation"]))
    if i==0:value.update(k_profile=a["k_profile"],output_omega=OMEGA,update_count=1)
    if i==1:
        n=a["updates"]
        value.update(k_profile=a["k_profile"],readout_profile=a["readout"],requested_updates=n,completed_updates=n,row_count=n,
            rows=[sample(j,a["readout"],b["input"]["omega"]) for j in range(n)],terminal=sample(n,a["readout"],b["input"]["omega"],True))
    if i in (2,3):
        value.update(q=a["q"],t=a["t"],z=TOKEN,M=[TOKEN]*3,C=[TOKEN]*3,T=[TOKEN]*3,
            initialization="RECOMPUTED",clock_qualification="USER_SUPPLIED_CLOCK")
    if i==3:value.update(memory_input=a["memory"],memory_output=a["memory"],memory_update_count=0,
        memory_qualification="SUPPLIED_MEMORY_NOT_HISTORY_VERIFIED")
    if i==4:
        value.update(a=[TOKEN]*3,sum=TOKEN,weights=[TOKEN]*3,chart=[TOKEN]*3,
            basis_digest=b["resolved_constants"]["chart"]["basis_digest"],chart_order=["cu","cx","cy"],zero_classification="NORMALIZED_NONZERO",
            underflow_flags=dict(square_to_zero=[False]*3,subnormal_square=[False]*3,normalized_weight_to_zero=[False]*3,
                subnormal_weight=[False]*3,subnormal_sum=False),warnings=[])
    return Payload(deepcopy(value))


def record(i=0,**kwargs):
    q=request(i,**kwargs)
    p=payload(q)
    c,r,b,key=context()
    members=[{key:row[key] for key in ("path","bytes","sha256")} for row in b.to_dict()["members"]]
    obs=InstallationObservation(dict(method="UNPROTECTED_INSTALLED_MEMBER_HASH_SCAN",before=members,after=members,match="MATCH",protected_during_execution=False))
    digests=[c.identity,authority_packet().identity,b.identity,obs.identity,q.identity,p.identity,b.identity]
    checks={name:dict(state="LOCAL_CHECK_PASSED",evidence=digest.to_dict(),reason=reason)
        for (name,_,reason),digest in zip(CHECKS,digests)}
    checks["execution_snapshot_attestation"]=UNAVAILABLE
    evidence=ExecutionEvidence(dict(schema="HISTORICAL_EXECUTION_EVIDENCE_1",method="LOCAL_OBSERVATIONS_WITHOUT_EXECUTION_ATTESTATION",
        attempt_id="TEST_ONLY",request_digest=q.identity.to_dict(),payload_digest=p.identity.to_dict(),provider_build=b.identity.to_dict(),
        installation_observation=obs.to_dict(),runtime=dict(implementation="TEST_ONLY",version="TEST_ONLY",platform="TEST_ONLY",
            architecture="TEST_ONLY",numeric_libraries=[],rounding_mode="NEAREST_EVEN",subnormal_mode="GRADUAL"),
        resource_observation=dict(method="LOCAL_MONITOR_OBSERVATION_NOT_EXECUTION_ATTESTATION",wall_milliseconds=0,peak_memory_bytes=0),checks=checks))
    value=dict(family=RESULT_FAMILY,**BASE,issuance_class=ISSUANCE,request=q.to_dict(),
        contract_bundle=dict(catalogue=c.to_dict(),authority_packet=authority_packet().to_dict(),constants_packet=constants_packet().to_dict(),
            provider_build=b.to_dict(),resource_policy=r.to_dict()),provider_binding=provider_binding(key),payload=p.to_dict(),
        qualifications=qualification(OPERATIONS[i]),assurance=ASSURANCE,execution_evidence=evidence.to_dict(),
        completion=dict(state="COMPLETE",attempt_id="TEST_ONLY",request_digest=q.identity.to_dict(),payload_digest=p.identity.to_dict(),evidence_digest=evidence.identity.to_dict()),
        metadata=dict(created_at="2026-10-01T00:00:00+00:00",attempt_id="TEST_ONLY",submitted_request_bytes=d.byte_digest(d.InputByteDigest,q.to_bytes()).to_dict(),
            source_locators=[dict(source_id="K_MODEL",locator="TEST_ONLY/display/source.py")]))
    value["semantic_result_digest"]=semantic_digest(value).to_dict()
    return deepcopy(value)


def receipt(q=None,category="MALFORMED_REQUEST",stage="REQUEST"):
    return deepcopy(dict(family=RECEIPT_FAMILY,**BASE,attempt_id="TEST_ONLY",submitted_request_bytes=fake(d.InputByteDigest),
        request=None if q is None else q.to_dict(),request_digest=None if q is None else q.identity.to_dict(),
        outcome="CANCELLED" if category=="CANCELLED" else "REFUSED",stage=stage,category=category,argument_field=None,
        checks={**{name:dict(state="NOT_REACHED",evidence=None,reason="NOT_REACHED") for name,_,_ in CHECKS},"execution_snapshot_attestation":UNAVAILABLE},
        provider=None if q is None else q.to_dict()["body"]["provider"],updates_completed=None,diagnostic="TEST_ONLY – synthetic failure",
        diagnostic_limit_bytes=256,staging="NOT_CREATED",created_at="2026-10-01T00:00:00Z"))
