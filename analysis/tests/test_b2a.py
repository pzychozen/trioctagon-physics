"""TEST_SUPPORT: B2A admission/refusal tests for disabled proof infrastructure.

Mock launchers are test-only and are never packaged in the runtime wheel.
Passing these tests does not prove Windows execution binding.
"""
import copy
import hashlib
import json
import os
from pathlib import Path
from unittest.mock import patch

import pytest

from trioctagon_analysis.b2a_snapshot import (FrozenSnapshot, SnapshotExpectation,
    admit_expectation, safe_member, sha, verify_tree)
from trioctagon_analysis.b2a_proof import NativeGate, NativeOriginRefusal, run_proof, validate_observation, publish_evidence
from trioctagon_analysis.b2a_windows import AppContainer, ReadLease
from trioctagon_analysis.codec import ParseLimits
from trioctagon_analysis.errors import ProtocolError
from trioctagon_analysis.provider import ParentSnapshot, copy_recorded
from trioctagon_analysis.records import DerivedAnalysisRecord
from trioctagon_analysis.requests import Selection
from support import context, core_bytes, LIMITS

pytestmark = pytest.mark.skipif(os.name != 'nt', reason='B2A proves Windows behavior only')


def fixture(tmp_path):
    candidate = tmp_path/'candidate'
    candidate.mkdir()
    values = {'runtime/pythonw.exe': b'TEST_ONLY_NOT_AN_INTERPRETER',
        'runtime/python311._pth': b'Lib\nDLLs\n../site\n',
        'runtime/Lib/json.py': b'# TEST_ONLY\n', 'runtime/DLLs/example.pyd': b'TEST_ONLY',
        'site/trioctagon_analysis/b2a_worker.py': b'# TEST_ONLY\n',
        'site/trioctagon_analysis/provider.py': b'# TEST_ONLY\n'}
    rows = []
    for name, raw in sorted(values.items()):
        p = candidate/name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(raw)
        rows.append({'path': name, 'size': len(raw), 'sha256': sha(raw), 'authority': 'TEST_ONLY_ARTIFACT'})
    parent, request, catalogue, approval, build = context()
    native = Path(os.environ['SystemRoot'])/'System32/kernel32.dll'
    raw = native.read_bytes()
    manifest = SnapshotExpectation({'family':'TRIOCTAGON_B2A_SNAPSHOT_EXPECTATION','version':1,
        'mode':'B2A_VALIDATION_ONLY','analysis_version':'0.1.0','provider':'trioctagon_analysis.provider:copy_recorded',
        'kernel_archive':request.to_dict()['kernel']['actual_archive']['sha256'],
        'kernel_lock':request.to_dict()['kernel']['lock']['sha256'],
        'archives':[{'name':'TEST_ONLY','sha256':'1'*64,'authority':'TEST_ONLY'}],
        'members':rows,'os_members':[{'path':str(native),'size':len(raw),'sha256':sha(raw)}],
        'runtime':'runtime/pythonw.exe','worker':'site/trioctagon_analysis/b2a_worker.py',
        'import_paths':['runtime/Lib','runtime/DLLs','site'],
        'qualification':'HASH != SIGNATURE; HASH != AUTHORSHIP; B2A PROOF ONLY'})
    return candidate, manifest, parent, request, catalogue, approval


@pytest.mark.parametrize('name', ['../escape.py', 'C:/escape.py', 'a\\b.py', 'a:stream',
    'a//b', 'AUX.py', 'con', 'a. /x.py', 'a/../x', 'rogue.pth', 'editable.egg-link',
    'x.pyc', 'x/__pycache__/thing.py'])
def test_alias_editable_startup_members_rejected(name):
    with pytest.raises(ProtocolError):
        safe_member(name)


@pytest.mark.parametrize('field,value', [('provider','rogue.provider:run'), ('analysis_version','9.9.9'),
    ('runtime','other/pythonw.exe'), ('import_paths',['runtime/Lib','runtime/DLLs','checkout'])])
def test_wrong_provider_version_or_checkout_path(tmp_path, field, value):
    _, manifest, *_ = fixture(tmp_path)
    data = manifest.to_dict(); data[field] = value
    with pytest.raises(ProtocolError): SnapshotExpectation(data)


def test_expected_manifest_needs_separate_pin(tmp_path):
    _, manifest, *_ = fixture(tmp_path)
    with pytest.raises(ProtocolError, match='pin'):
        admit_expectation(manifest.to_bytes(), '0'*64, ParseLimits(100000,16))
    assert admit_expectation(manifest.to_bytes(),sha(manifest.to_bytes()),ParseLimits(100000,16)) == manifest


@pytest.mark.parametrize('change', ['modified_analysis','extra_module','alternate_same_name','rogue_pth','editable','missing_member'])
def test_candidate_drift_member_set_and_startup_influence(tmp_path, change):
    candidate, manifest, *_ = fixture(tmp_path)
    provider = candidate/'site/trioctagon_analysis/provider.py'
    if change == 'modified_analysis': provider.write_bytes(b'changed')
    elif change == 'missing_member': provider.unlink()
    else:
        name = {'extra_module':'unexpected.py','alternate_same_name':'provider.py',
                'rogue_pth':'startup.pth','editable':'editable.egg-link'}[change]
        (candidate/'site'/name).write_bytes(b'UNAPPROVED')
    with pytest.raises(ProtocolError): verify_tree(candidate, manifest)


def test_hardlink_alias_rejected(tmp_path):
    candidate, manifest, *_ = fixture(tmp_path)
    source = candidate/'site/trioctagon_analysis/provider.py'
    alias = tmp_path/'alias.py'
    os.link(source, alias)
    try:
        with pytest.raises(ProtocolError, match='hard-link'): verify_tree(candidate,manifest)
    finally: alias.unlink()


@pytest.mark.parametrize('operation', ['write','unlink','replace','rename'])
def test_real_windows_lease_rejects_active_mutation(tmp_path, operation):
    target = tmp_path/'member.py'; target.write_bytes(b'ADMITTED')
    replacement = tmp_path/'replacement.py'; replacement.write_bytes(b'UNAPPROVED')
    with ReadLease(target):
        with pytest.raises(OSError):
            if operation == 'write': target.write_bytes(b'changed')
            elif operation == 'unlink': target.unlink()
            elif operation == 'replace': os.replace(replacement,target)
            else: target.rename(tmp_path/'renamed.py')
        assert target.read_bytes() == b'ADMITTED'


def test_lease_refuses_preexisting_writer(tmp_path):
    target = tmp_path/'member.py';target.write_bytes(b'x')
    with target.open('r+b'):
        with pytest.raises(OSError): ReadLease(target)


def test_fresh_snapshot_dacl_member_set_and_cleanup(tmp_path):
    candidate, manifest, *_ = fixture(tmp_path)
    with FrozenSnapshot(candidate,tmp_path,manifest,None) as snapshot:
        target = snapshot.root/'site/trioctagon_analysis/provider.py'
        with pytest.raises(OSError): target.write_bytes(b'replacement')
        with pytest.raises(OSError): (snapshot.root/'extra.py').write_bytes(b'extra')
        with pytest.raises(OSError): snapshot.root.rename(tmp_path/'alias')
        snapshot.verify_after()
        owned = snapshot.root
    assert not owned.exists()
    verify_tree(candidate,manifest)


def test_native_image_not_admitted_by_location_or_plausible_name(tmp_path):
    candidate, manifest, *_ = fixture(tmp_path)
    alien = tmp_path/'kernel32.dll';alien.write_bytes(b'not the approved OS')
    gate = NativeGate(candidate,manifest,{})
    try:
        with ReadLease(alien) as lease:
            with pytest.raises(NativeOriginRefusal,match='UNEXPECTED_NATIVE_IMAGE'):gate.inspect(lease.handle)
        with pytest.raises(NativeOriginRefusal,match='HANDLE_UNAVAILABLE'):gate.inspect(None)
    finally: gate.close()


@pytest.mark.parametrize('change', ['approval','kernel','parent_after_capture'])
def test_prelaunch_identity_refusals_never_issue_result(tmp_path,change):
    candidate,manifest,parent,request,catalogue,approval=fixture(tmp_path)
    approval_pin=sha(approval.to_bytes())
    if change=='approval': approval_pin='0'*64
    elif change=='kernel':
        data=manifest.to_dict();data['kernel_archive']='0'*64;manifest=SnapshotExpectation(data)
    else: parent=ParentSnapshot(parent.original+b' ',LIMITS)
    result=run_proof(candidate,tmp_path,manifest,request,parent,catalogue,approval,
        expectation_pin=sha(manifest.to_bytes()),approval_pin=approval_pin)
    assert result['windows_execution_binding']=='NOT_PROVEN'
    assert not result['production_attestation_enabled'] and result['observation'] is None
    assert result['failures']


@pytest.mark.parametrize('mismatch',['nonce','request'])
def test_wrong_request_after_plausible_copy_is_rejected(tmp_path,mismatch):
    _,_,parent,request,_,_=fixture(tmp_path)
    payload=copy_recorded(parent,Selection(request.to_dict()['selection']))
    value={'family':'TRIOCTAGON_B2A_WORKER_OBSERVATION','mode':'B2A_VALIDATION_ONLY','producer_verified':False,
        'request':request.identity.to_dict(),'attempt_nonce':'current','snapshot':tmp_path.name,
        'provider':'trioctagon_analysis.provider:copy_recorded',
        'entry_origin':str(tmp_path/'site/trioctagon_analysis/provider.py'),
        'payload':payload.to_dict(),'payload_digest':payload.identity.to_dict()}
    if mismatch=='nonce':value['attempt_nonce']='stale'
    else:value['request']['sha256']='0'*64
    with pytest.raises(ProtocolError):validate_observation(value,request,parent,'current',tmp_path)


def test_cleanup_failure_remains_failure(tmp_path):
    candidate,manifest,parent,request,catalogue,approval=fixture(tmp_path)
    class TEST_ONLY_FailedLauncher:
        sid_string=None
        def launch(self,*args,**kwargs):
            (Path(args[3])/'observation.json').write_text('{"plausible_output":true}')
            raise OSError('TEST_ONLY attestation failed after plausible output ' + 'X'*2000)
        def close(self):raise OSError('TEST_ONLY cleanup failed')
    with patch('trioctagon_analysis.b2a_proof.AppContainer',TEST_ONLY_FailedLauncher):
        result=run_proof(candidate,tmp_path,manifest,request,parent,catalogue,approval,
            expectation_pin=sha(manifest.to_bytes()),approval_pin=sha(approval.to_bytes()))
    assert result['cleanup']=='FAILED' and result['observation'] is None
    assert result['windows_execution_binding']=='NOT_PROVEN'
    assert any('CLEANUP_FAILURE' in x for x in result['failures'])
    assert all(len(x)<=1024 for x in result['failures'])


def test_proof_evidence_is_not_a_successful_derived_record():
    with pytest.raises(ProtocolError):
        DerivedAnalysisRecord({'family':'TRIOCTAGON_B2A_PROOF_EVIDENCE',
                               'windows_execution_binding':'NOT_PROVEN'})


def test_empty_unadmitted_directory_is_rejected(tmp_path):
    candidate, manifest, *_ = fixture(tmp_path)
    (candidate/'site/namespace_extra').mkdir()
    with pytest.raises(ProtocolError,match='directory set'):verify_tree(candidate,manifest)


def test_b2a_evidence_reuses_no_replace_persistence(tmp_path):
    value={'family':'TRIOCTAGON_B2A_PROOF_EVIDENCE','windows_execution_binding':'NOT_PROVEN',
           'production_attestation_enabled':False,'mode':'B2A_VALIDATION_ONLY'}
    path, identity=publish_evidence(value,tmp_path)
    original=path.read_bytes()
    assert publish_evidence(value,tmp_path)==(path,identity)
    path.write_bytes(b'corrupt existing evidence')
    with pytest.raises(ProtocolError):publish_evidence(value,tmp_path)
    assert path.read_bytes()==b'corrupt existing evidence'
    assert not list(tmp_path.glob('.b2a-*.tmp'))
    value['production_attestation_enabled']=True
    with pytest.raises(ProtocolError):publish_evidence(value,tmp_path)


def test_mutation_after_copy_before_launch_refuses_and_cleans(tmp_path):
    candidate,manifest,*_=fixture(tmp_path)
    original=FrozenSnapshot.freeze
    def TEST_ONLY_mutation(snapshot):
        (snapshot.root/'site/trioctagon_analysis/provider.py').write_bytes(b'changed before launch')
        original(snapshot)
    with patch.object(FrozenSnapshot,'freeze',TEST_ONLY_mutation):
        with pytest.raises(ProtocolError,match='bytes mismatch'):
            FrozenSnapshot(candidate,tmp_path,manifest,None)
    assert not list(tmp_path.glob('snapshot-*'))


def test_checkout_candidate_is_rejected(tmp_path):
    candidate,manifest,*_=fixture(tmp_path)
    (tmp_path/'.git').mkdir()
    with pytest.raises(ProtocolError,match='outside a checkout'):verify_tree(candidate,manifest)
