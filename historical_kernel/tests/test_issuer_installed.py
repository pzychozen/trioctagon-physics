"""TEST_ONLY installed worker/resource/atomicity conformance, with synthetic local review pins."""
import os
from pathlib import Path
import threading
import pytest
from trioctagon_historical_kernel.issuer import LocalIssuer
from trioctagon_historical_kernel import issuer
from trioctagon_historical_protocol.records import DerivedRecord,AttemptReceipt
from trioctagon_historical_kernel.admission import Admission
from installed_support import admission,request

pytestmark=pytest.mark.skipif(not os.environ.get('H6B_TEST_WHEEL'),reason='installed-only worker certification lane')


@pytest.fixture
def context(tmp_path):
    return admission(tmp_path,os.environ['H6B_TEST_WHEEL'])


@pytest.mark.parametrize('index',range(5))
def test_actual_local_issuer_all_operations(context,tmp_path,index):
    a,path,pin=context;destination=tmp_path/'result.json'
    result=LocalIssuer(path,pin).issue(request(a,index).to_bytes(),destination)
    assert type(result) is DerivedRecord,result.to_dict()
    assert destination.read_bytes()==result.to_bytes()
    assert result.to_dict()['assurance']['producer_execution_attestation']['state']=='UNAVAILABLE'


def test_N06_N36_pin_and_unknown_build_fail_closed(context,tmp_path):
    a,path,pin=context
    with pytest.raises(ValueError):LocalIssuer(path,'0'*64)
    value=a.to_dict();value['build']['archive_sha256']='a'*64
    with pytest.raises(ValueError):Admission(value)
    from test_provider import request as unrelated_request
    destination=tmp_path/'absent.json'
    result=LocalIssuer(path,pin).issue(unrelated_request().to_bytes(),destination)
    assert type(result) is AttemptReceipt and not destination.exists()


@pytest.mark.parametrize('kind',['numeric','cancel','publication','binding','concurrent','malformed','oversized'])
def test_N17_failure_atomicity(context,tmp_path,monkeypatch,kind):
    a,path,pin=context;destination=tmp_path/'must-not-exist.json';cancel=threading.Event()
    raw=request(a,1).to_bytes();expected=None
    if kind=='numeric':
        omega=[dict(real={'f64':(1e308).hex()},imag={'f64':(0.).hex()})]*3
        raw=request(a,1,omega=omega).to_bytes();expected='NUMERICAL_DOMAIN_FAILURE'
    elif kind=='cancel':cancel.set();expected='CANCELLED'
    elif kind=='publication':
        def fail(*args):raise OSError('TEST_ONLY persistence failure')
        monkeypatch.setattr(issuer,'_publish',fail);expected='PERSISTENCE_FAILURE'
    elif kind=='binding':
        def fail(*args,**kwargs):raise ValueError('TEST_ONLY result-binding failure')
        monkeypatch.setattr(issuer.DerivedRecord,'from_bytes',fail);expected='RESULT_BINDING_FAILURE'
    elif kind=='malformed':raw=b'{"bad":1.0}';expected='MALFORMED_REQUEST'
    elif kind=='oversized':raw=b' '*32769;expected='RESOURCE_LIMIT'
    elif kind=='concurrent':issuer._LANE.acquire();expected='RESOURCE_LIMIT'
    try:result=LocalIssuer(path,pin).issue(raw,destination,cancellation=cancel)
    finally:
        if kind=='concurrent':issuer._LANE.release()
    assert type(result) is AttemptReceipt and result.to_dict()['category']==expected,result.to_dict()
    assert not destination.exists() and not list(tmp_path.glob('.historical-stage-*'))
    assert not any(k in result.to_dict() for k in ('payload','rows','omega','result'))


@pytest.mark.parametrize('limits',[{'max_updates':0},{'wall_milliseconds':1},{'memory_bytes':8*1024*1024},{'output_bytes':100},{'manifest_bytes':100}])
def test_N37_actual_worker_and_declared_limits(tmp_path,limits):
    a,path,pin=admission(tmp_path,os.environ['H6B_TEST_WHEEL'],**limits)
    destination=tmp_path/'absent.json'
    result=LocalIssuer(path,pin).issue(request(a,1,updates=2).to_bytes(),destination)
    assert type(result) is AttemptReceipt and result.to_dict()['category']=='RESOURCE_LIMIT',result.to_dict()
    assert not destination.exists()


def test_publication_never_overwrites_existing(context,tmp_path):
    a,path,pin=context;destination=tmp_path/'existing.json';destination.write_bytes(b'KEEP')
    result=LocalIssuer(path,pin).issue(request(a).to_bytes(),destination)
    assert type(result) is AttemptReceipt and result.to_dict()['category']=='PERSISTENCE_FAILURE'
    assert destination.read_bytes()==b'KEEP'


def test_installed_tamper_refuses_before_computation(context,tmp_path):
    import trioctagon_historical_kernel
    a,path,pin=context
    package=Path(trioctagon_historical_kernel.__file__).resolve().parent
    import sys
    assert package.is_relative_to(Path(sys.prefix).resolve())
    extra=package/'TEST_ONLY_unlisted.txt'
    assert not extra.exists()
    try:
        extra.write_bytes(b'not admitted')
        result=LocalIssuer(path,pin).issue(request(a).to_bytes(),tmp_path/'absent.json')
        assert type(result) is AttemptReceipt
        assert not (tmp_path/'absent.json').exists()
    finally:extra.unlink()


@pytest.mark.parametrize('kind',['numerical','cancellation'])
def test_failure_after_completed_updates_is_receipt_only(context,tmp_path,monkeypatch,kind):
    a,path,pin=context;cancel=threading.Event();omega=None
    if kind=='numerical':
        omega=[dict(real={'f64':(100.).hex()},imag={'f64':(0.).hex()})]*3
    else:
        original=issuer.queue.Queue.get
        def get(self,*args,**kwargs):
            event=original(self,*args,**kwargs)
            if type(event) is dict and event.get('kind')=='progress':cancel.set()
            return event
        monkeypatch.setattr(issuer.queue.Queue,'get',get)
    destination=tmp_path/'absent.json'
    result=LocalIssuer(path,pin).issue(request(a,1,updates=64,omega=omega).to_bytes(),destination,cancellation=cancel)
    assert type(result) is AttemptReceipt,result.to_dict()
    assert result.to_dict()['category']==('CANCELLED' if kind=='cancellation' else 'NUMERICAL_DOMAIN_FAILURE')
    assert 0<result.to_dict()['updates_completed']<64
    assert not destination.exists()


@pytest.mark.parametrize('state',['missing','pending'])
def test_N37_missing_or_pending_policy_cannot_admit(context,state):
    a,_,_=context;value=a.to_dict()
    if state=='missing':value.pop('resource')
    else:value['resource'].update(state='MEASUREMENT_REQUIRED_BEFORE_ADMISSION',limits=None,measurement_manifest=None)
    with pytest.raises(ValueError):Admission(value)


def test_live_runtime_closure_rejects_injected_scientific_module(monkeypatch):
    import sys,types
    from trioctagon_historical_kernel.installation import verify_runtime_closure
    verify_runtime_closure()
    monkeypatch.setitem(sys.modules,'kernel_physics',types.ModuleType('kernel_physics'))
    with pytest.raises(ValueError,match='forbidden scientific runtime import'):verify_runtime_closure()


@pytest.mark.parametrize('after_link',[False,True])
def test_publication_is_supervised_and_rolled_back_on_timeout(tmp_path,monkeypatch,after_link):
    import time
    a,path,pin=admission(tmp_path,os.environ['H6B_TEST_WHEEL'],wall_milliseconds=2500)
    original=issuer.subprocess.Popen
    bootstrap="import os,time,runpy\noriginal=os.link\ndef delayed(*args):\n "
    bootstrap+=("original(*args); " if after_link else "")+"time.sleep(60)\nos.link=delayed\nrunpy.run_module('trioctagon_historical_kernel.worker',run_name='__main__')"
    def instrument(command,*args,**kwargs):
        assert command[1:5]==['-I','-B','-m','trioctagon_historical_kernel.worker']
        return original([command[0],'-I','-B','-c',bootstrap,*command[5:]],*args,**kwargs)
    monkeypatch.setattr(issuer.subprocess,'Popen',instrument)
    started=time.perf_counter();destination=tmp_path/'absent.json'
    result=LocalIssuer(path,pin).issue(request(a).to_bytes(),destination)
    assert time.perf_counter()-started<8
    assert type(result) is AttemptReceipt and result.to_dict()['category']=='RESOURCE_LIMIT',result.to_dict()
    assert not destination.exists() and not list(tmp_path.glob('.historical-stage-*'))
