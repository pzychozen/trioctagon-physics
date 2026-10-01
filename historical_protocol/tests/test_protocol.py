"""TEST_ONLY H6A contract tests. Stored numeric claims intentionally do not solve equations."""
from copy import deepcopy
import json
from pathlib import Path
import pytest
import support as t
from trioctagon_historical_protocol import digests as d
from trioctagon_historical_protocol.codec import ParseLimits, canonical_bytes, decode
from trioctagon_historical_protocol.errors import ProtocolError,CATEGORIES
from trioctagon_historical_protocol.schema import HProtocol, PROTOCOL, ZERO
from trioctagon_historical_protocol.packets import (AuthorityPacket,ConstantsPacket,ResourcePolicy,ProviderBuild,
    authority_packet,constants_packet,default_resource_policy,READOUTS,K_NAMES)
from trioctagon_historical_protocol.catalogue import Catalogue, Descriptor
from trioctagon_historical_protocol.requests import Request, request_digest
from trioctagon_historical_protocol.payloads import Payload,StepPayload,RunPayload,StagedPayload,EMAPayload,ChartPayload
from trioctagon_historical_protocol.records import DerivedRecord,AttemptReceipt,semantic_digest
from trioctagon_historical_protocol.evidence import ExecutionEvidence,InstallationObservation
from trioctagon_analysis.errors import ProtocolError as CoreError

LIMITS=ParseLimits(2000000,64)  # TEST_ONLY parsing budget, not runtime admission.
OWNERS=(StepPayload,RunPayload,StagedPayload,EMAPayload,ChartPayload)


@pytest.mark.parametrize("i",range(5))
@pytest.mark.parametrize("k",K_NAMES)
def test_each_operation_roundtrip_and_detached_immutable_claim(i,k):
    q=t.request(i,k_profile=k)
    p=t.payload(q)
    p.validate_request(q)
    assert OWNERS[i](p.to_dict()).to_bytes()==p.to_bytes()
    r=DerivedRecord(t.record(i,k_profile=k))
    assert DerivedRecord.from_bytes(r.to_bytes(),LIMITS).identity==r.identity
    assert Request.from_bytes(json.dumps(q.to_dict(),indent=2).encode(),LIMITS).identity==q.identity
    changed=r.to_dict(); changed["metadata"]["attempt_id"]="changed"
    assert r.to_dict()["metadata"]["attempt_id"]=="TEST_ONLY"
    with pytest.raises((TypeError,AttributeError)):r.data["family"]="changed"
    with pytest.raises((TypeError,AttributeError)):r._raw=b"{}"
    with pytest.raises(ProtocolError):DerivedRecord.from_bytes(r.to_bytes()+b"\n",LIMITS)


@pytest.mark.parametrize("n",[0,1,2,12,13])
@pytest.mark.parametrize("mode",READOUTS)
def test_run_N0_counts_constructor_terminal_q_memory(n,mode):
    r=DerivedRecord(t.record(1,updates=n,readout=mode))
    p=r.to_dict()["payload"]
    assert len(p["rows"])==n and p["terminal"]["update_index"]==n
    assert p["terminal"]["q"]==n%12


def change(value,path,replacement):
    for key in path[:-1]:value=value[key]
    value[path[-1]]=deepcopy(replacement)


# Each labelled mutation is a concrete portion of the frozen N01-N40 matrix.
REQUEST_CASES=[
    ("N03",("body","profile"),"CORE"),("N03",("body","contract"),"OTHER"),
    ("N03",("body","implementation_policy"),"CURRENT_STEP3_REUSE_ALLOWED"),
    ("N04",("body","revision"),2),("N04",("body","operation"),"historical.execute"),
    ("N05",("body","authority"),t.fake(d.AuthorityDigest,"b")),
    ("N06",("body","provider","id"),"arbitrary.plugin"),
    ("N07",("body","arguments","k_profile"),"L01"),
    ("N08",("body","resolved_constants","dynamics","epsilon"),t.TOKEN),
    ("N09",("body","observer_list"),[]),("N10",("body","source_path"),"C:/source.py"),
    ("N10",("body","module"),"kernel_TO"),("N11",("body","service"),"torment_service"),
    ("N12",("body","resolved_constants","dynamics","harmonic"),4),
    ("N12",("body","resolved_constants","dynamics","phase_strength"),ZERO),
    ("N13",("body","seed"),1),("N13",("body","resolved_constants","dynamics","sigma"),t.TOKEN),
    ("N14",("body","input","omega"),t.OMEGA[:2]),("N14",("body","input","omega"),[t.OMEGA[0]]*4),
    ("N15",("body","geometry"),"C01"),("N16",("body","corridor"),["cx","cy"]),
    ("N21",("body","resume"),True),("N22",("body","input","kind"),"CORE_PARENT"),
    ("N22",("body","parents"),[]),("N23",("body","input","omega",0,"real"),True),
    ("N23",("body","input","omega",0,"real"),0.5),
    ("N23",("body","input","omega",0,"real"),{"f64":"nan"}),
    ("N23",("body","input","omega",0,"real"),{"f64":"inf"}),
    ("N23",("body","input","omega",0,"real"),{"f64":"0x1p+0"}),
    ("N23",("body","input","dtype"),"complex128"),
    ("N24",("body","input","omega",0,"imag"),ZERO),
    ("N35",("request_digest","scope"),"REQUEST_DIGEST"),
    ("N35",("full_artifact_digest",),t.fake(d.FullArtifactDigest)),
    ("N39",("body","embeddings"),[]),("N39",("body","gates"),[])]


@pytest.mark.parametrize("case,path,replacement",REQUEST_CASES,ids=[f"{row[0]}-{i}" for i,row in enumerate(REQUEST_CASES)])
def test_request_negative_matrix(case,path,replacement):
    value=t.request().to_dict(); change(value,path,replacement)
    with pytest.raises(ProtocolError):Request(value)


PAYLOAD_CASES=[
    ("N02",0,("schema",),"APP04_COPY_PAYLOAD_1"),("N04",0,("schema",),"H_RUN_1"),
    ("N09",0,("history",),[]),("N12",0,("update_count",),2),
    ("N17",1,("completed_updates",),1),("N25",1,("row_count",),3),
    ("N25",1,("rows",0,"row_ordinal"),1),("N25",1,("terminal","update_index"),3),
    ("N25",1,("terminal","q"),3),("N26",1,("rows",0,"initialization"),"AFTER_UPDATE"),
    ("N26",1,("rows",0,"t"),{"f64":"-0x0.0p+0"}),
    ("N27",2,("memory",),ZERO),("N27",2,("initialization",),"HISTORICAL_CONSTRUCTOR_ZERO"),
    ("N28",3,("memory_update_count",),1),("N28",3,("memory_output",),ZERO),
    ("N29",1,("readout_profile",),[READOUTS[1],READOUTS[2]]),
    ("N30",4,("chart_order",),["cx","cy","cu"]),("N30",4,("warnings",),["SQUARE_UNDERFLOW"]),
    ("N30",4,("underflow_flags","square_to_zero"),[True]*3),
    ("N32",0,("provider_binding","current_kernel_role"),"PARTICIPATING"),
    ("N32",0,("provider_binding","scientific_delegations"),["kernel_physics"]),
    ("N34",0,("qualifications","physical_validation"),"VERIFIED")]


@pytest.mark.parametrize("case,i,path,replacement",PAYLOAD_CASES,ids=[f"{row[0]}-{i}" for i,row in enumerate(PAYLOAD_CASES)])
def test_payload_negative_matrix(case,i,path,replacement):
    value=t.payload(t.request(i)).to_dict(); change(value,path,replacement)
    with pytest.raises(ProtocolError):Payload(value)


def test_N25_N26_N29_run_closed_shape_and_constructor_readouts():
    for mode in READOUTS[1:]:
        original=t.payload(t.request(1,readout=mode)).to_dict()
        for path,value in [(('rows',0,'readout','z'),t.TOKEN),(('rows',0,'readout','initialization'),'RECOMPUTED'),
            (('rows',0,'readout','M'),[ZERO,ZERO,t.TOKEN]),(('terminal','readout','profile'),'NONE')]:
            p=deepcopy(original);change(p,path,value)
            with pytest.raises(ProtocolError):Payload(p)
        p=deepcopy(original);p['rows'].append(p['terminal']);p['row_count']+=1
        with pytest.raises(ProtocolError):Payload(p)
        if mode==READOUTS[2]:
            p=deepcopy(original);p['terminal']['readout']['memory_update_count']=0
            with pytest.raises(ProtocolError):Payload(p)


@pytest.mark.parametrize("owner,factory",[(Request,lambda:t.request().to_dict()),(Payload,lambda:t.payload(t.request()).to_dict()),
    (DerivedRecord,t.record),(AttemptReceipt,t.receipt),(AuthorityPacket,lambda:authority_packet().to_dict()),
    (ConstantsPacket,lambda:constants_packet().to_dict()),(Catalogue,lambda:t.context()[0].to_dict()),
    (ResourcePolicy,lambda:t.context()[1].to_dict()),(ProviderBuild,lambda:t.context()[2].to_dict())])
def test_missing_and_unknown_root_keys(owner,factory):
    original=factory()
    for key in original:
        value=deepcopy(original);del value[key]
        with pytest.raises(ProtocolError):owner(value)
    value=deepcopy(original);value['extension']=None
    with pytest.raises(ProtocolError):owner(value)


def test_N05_N07_N08_frozen_packets_and_descriptors():
    a=authority_packet().to_dict();a['h5_contract_sha256']='b'*64
    with pytest.raises(ProtocolError):AuthorityPacket(a)
    c=constants_packet().to_dict();c['ema']['innovation']=t.TOKEN
    with pytest.raises(ProtocolError):ConstantsPacket(c)
    for op in t.OPERATIONS:
        v=t.descriptor_template(op);v['effects'].append('EXECUTE')
        with pytest.raises(ProtocolError):Descriptor(v)
    assert HProtocol(PROTOCOL).to_dict()==PROTOCOL


def test_N06_N36_context_consistency_is_not_admission():
    c,r,b,key=t.context();q=t.request()
    q.validate_context(c,r,b)
    altered=b.to_dict();altered['archive_sha256']='c'*64
    with pytest.raises(ProtocolError):q.validate_context(c,r,ProviderBuild(altered))
    value=q.to_dict();value['body']['catalogue']=t.fake(d.CatalogueDigest,'b')
    value['request_digest']=request_digest(value).to_dict()
    claim=Request(value) # A structurally valid digest reference does not approve anything.
    with pytest.raises(ProtocolError):claim.validate_context(c,r,b)


@pytest.mark.parametrize('path,value',[
    (('execution_evidence','checks','execution_snapshot_attestation','state'),'VERIFIED'),
    (('execution_evidence','checks','inputs_bound','state'),'VERIFIED'),
    (('assurance','producer_execution_attestation','state'),'VERIFIED'),
    (('assurance','artifact_structure_integrity','scientific_equations_replayed'),True),
    (('completion','request_digest'),t.fake(d.RequestDigest,'b')),
    (('metadata','attempt_id'),'OTHER'),(('metadata','created_at'),'2026-10-01'),
    (('execution_evidence','resource_observation','wall_milliseconds'),1001)])
def test_N19_N34_N35_N37_result_claims_fail_closed(path,value):
    r=t.record();change(r,path,value)
    with pytest.raises(ProtocolError):DerivedRecord(r)


def test_N37_pending_policy_cannot_describe_success():
    assert default_resource_policy().to_dict()['limits'] is None
    r=t.record();r['contract_bundle']['resource_policy']=default_resource_policy().to_dict()
    with pytest.raises(ProtocolError):DerivedRecord(r)
    p=default_resource_policy().to_dict();p['state']='MEASURED_ADMITTED_LOCAL'
    with pytest.raises(ProtocolError):ResourcePolicy(p)


def test_N40_relocation_and_submission_whitespace_control():
    r=DerivedRecord(t.record());v=r.to_dict()
    v['metadata']['source_locators'][0]['locator']='C:/relocated/never-opened.py'
    v['metadata']['submitted_request_bytes']=t.fake(d.InputByteDigest,'e')
    moved=DerivedRecord(v)
    assert moved.identity==r.identity and moved.to_bytes()!=r.to_bytes()
    assert d.byte_digest(d.FullArtifactDigest,moved.to_bytes())!=d.byte_digest(d.FullArtifactDigest,r.to_bytes())
    v['metadata']['source_locators'][0]['source_id']='UNKNOWN'
    with pytest.raises(ProtocolError):DerivedRecord(v)


def test_N34_scientifically_incorrect_but_self_consistent_claim_parses():
    # Three weights of 0.5 and stored sum 0.5 are intentionally inconsistent arithmetic.
    # H6A compares stored domains/flags, never sums or applies a scientific equation.
    r=DerivedRecord(t.record(4))
    assert r.to_dict()['payload']['weights']==[t.TOKEN]*3
    assert r.to_dict()['assurance']['mathematical_reconstruction_status']['per_result_math_verification']=='NOT_PERFORMED'


@pytest.mark.parametrize('category',sorted(CATEGORIES))
def test_receipt_roundtrip(category):
    v=t.receipt(category=category)
    r=AttemptReceipt(v)
    assert AttemptReceipt.from_bytes(r.to_bytes(),LIMITS).to_dict()==v


def test_N17_N18_receipt_failure_progress_and_utf8_bounds():
    q=t.request(1)
    v=t.receipt(q,category='RESOURCE_LIMIT',stage='COMPUTATION');v['updates_completed']=1
    r=AttemptReceipt(v);r.validate_context(*t.context()[:3])
    with pytest.raises(ProtocolError):DerivedRecord(v)
    for key,bad in [('updates_completed',3),('outcome','COMPLETE'),('payload',{}),('diagnostic_limit_bytes',2)]:
        badv=deepcopy(v);badv[key]=bad
        with pytest.raises(ProtocolError):AttemptReceipt(badv)
    v['diagnostic']='é';v['diagnostic_limit_bytes']=1
    with pytest.raises(ProtocolError):AttemptReceipt(v)
    v['diagnostic_limit_bytes']=2;AttemptReceipt(v)


def test_receipt_null_request_and_passed_candidate_constraints():
    v=t.receipt();v['request_digest']=t.fake(d.RequestDigest)
    with pytest.raises(ProtocolError):AttemptReceipt(v)
    v=t.receipt();v['checks']['inputs_bound']=dict(state='LOCAL_CHECK_PASSED',evidence=t.fake(d.RequestDigest),reason=t.CHECKS[4][2])
    with pytest.raises(ProtocolError):AttemptReceipt(v)
    v=t.receipt(t.request(),category='PERSISTENCE_FAILURE',stage='PERSISTENCE');v['staging']='DISCARDED'
    v['checks']['payload_validated']=dict(state='LOCAL_CHECK_PASSED',evidence=t.fake(d.PayloadDigest),reason=t.CHECKS[5][2])
    AttemptReceipt(v)
    v['stage']='REQUEST'
    with pytest.raises(ProtocolError):AttemptReceipt(v)


def test_N30_chart_zero_underflow_and_ordered_flags():
    p=t.payload(t.request(4)).to_dict()
    p.update(input_omega=[dict(real=ZERO,imag=ZERO)]*3,a=[ZERO]*3,sum=ZERO,weights=[ZERO]*3,chart=[ZERO]*3,
        zero_classification='EXACT_ZERO_INPUT')
    Payload(p)
    p['weights']=[t.TOKEN]*3
    with pytest.raises(ProtocolError):Payload(p)
    p['weights']=[ZERO]*3;p['input_omega']=t.OMEGA;p['zero_classification']='NONZERO_INPUT_SQUARED_TO_ZERO'
    p['underflow_flags']['square_to_zero']=[True]*3;p['warnings']=['NONZERO_INPUT_ZERO_BRANCH','SQUARE_UNDERFLOW']
    Payload(p)
    p['warnings'].reverse()
    with pytest.raises(ProtocolError):Payload(p)
    p=t.payload(t.request(4)).to_dict();sub={'f64':'0x0.0000000000001p-1022'}
    p.update(a=[sub]*3,sum=sub,weights=[sub]*3)
    p['underflow_flags'].update(subnormal_square=[True]*3,subnormal_weight=[True]*3,subnormal_sum=True)
    p['warnings']=['SUBNORMAL_SQUARED_MAGNITUDE','SUBNORMAL_WEIGHT','SUBNORMAL_SUM'];Payload(p)


@pytest.mark.parametrize('raw',[b'{"family":1,"family":2}',b'{"v":1.0}',b'{"v":NaN}',b'{"f64":"Infinity"}',
    b'{"x":"\\ud800"}',b'\xef\xbb\xbf{}',b'"\xff"'])
def test_N23_malformed_codec_bytes(raw):
    with pytest.raises((ProtocolError,CoreError)):Request.from_bytes(raw,LIMITS)


def test_codec_identity_limits_and_digest_immutability():
    from trioctagon_analysis.codec import canonical_bytes as core_canonical
    from trioctagon_analysis.digests import CONTENT_TYPES
    assert canonical_bytes is core_canonical
    assert not CONTENT_TYPES.intersection(d.CONTENT_TYPES)
    for kind in d.CONTENT_TYPES:
        with pytest.raises((TypeError,AttributeError)):setattr(kind('a'*64),'scope','WRONG')
    q=t.request()
    with pytest.raises(ProtocolError):Request.from_bytes(q.to_bytes(),ParseLimits(1,64))
    with pytest.raises(ProtocolError):Request.from_bytes(q.to_bytes(),ParseLimits(2000000,2))
    with pytest.raises(CoreError):canonical_bytes({'n':1})
    assert canonical_bytes({'n':1},integer_paths={('n',)})==b'{"n":1}'


@pytest.mark.parametrize('name',['kernel_physics','kernel-physics','kernel.physics','kernel_TO','torment_service','trioctagon-physics'])
def test_N31_forbidden_scientific_build_dependency_claim(name):
    value=t.context()[2].to_dict()
    value['dependencies']=[dict(id=name,version='TEST_ONLY',manifest_sha256='a'*64,role='RUNTIME')]
    with pytest.raises(ProtocolError):ProviderBuild(value)


@pytest.mark.parametrize('path',['../escape','/absolute','C:/absolute','a\\b','a//b','a/CON.txt','a./b','a/NUL','x:stream'])
def test_build_inventory_rejects_unsafe_paths(path):
    value=t.context()[2].to_dict();value['members'][0]['path']=path
    with pytest.raises(ProtocolError):ProviderBuild(value)


def test_N24_signed_zero_payload_echo_and_new_request_identity():
    q=t.request();v=q.to_dict();v['body']['input']['omega'][0]['imag']=ZERO
    v['request_digest']=request_digest(v).to_dict();changed=Request(v)
    assert changed.identity!=q.identity
    with pytest.raises(ProtocolError):t.payload(q).validate_request(changed)


def test_N35_basis_and_framing_are_independently_bound():
    c=constants_packet().to_dict()['chart']
    projection={k:c[k] for k in ('basis_order','basis_rows')}
    assert d.content_digest(d.BasisDigest,canonical_bytes(projection)).to_dict()==c['basis_digest']
    assert authority_packet().to_dict()['h5_contract_sha256']=='615fa946afc57d41e3239bc2ece5f67112e20dba1d04aed7a9379aa15ff27699'
    with pytest.raises(ProtocolError):d.content_digest(d.FullArtifactDigest,b'{}')
    with pytest.raises(ProtocolError):d.byte_digest(d.RequestDigest,b'{}')


def test_N19_recomputed_digest_cannot_upgrade_assurance():
    from trioctagon_historical_protocol.schema import typed_bytes
    from trioctagon_historical_protocol.records import SEMANTIC_SCHEMA
    value=t.record();value['assurance']['producer_execution_attestation']['state']='VERIFIED'
    # Even the semantic-projection validator independently refuses the forged upgrade.
    with pytest.raises((ProtocolError,CoreError)):semantic_digest(value)
    with pytest.raises(ProtocolError):DerivedRecord(value)
