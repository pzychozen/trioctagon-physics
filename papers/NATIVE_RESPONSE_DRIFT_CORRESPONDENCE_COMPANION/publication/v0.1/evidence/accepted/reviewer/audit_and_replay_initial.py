from pathlib import Path, PurePosixPath
import hashlib, json, io, zipfile, stat, subprocess, sys, platform, time
BASE=Path('/mnt/data/rd_correspondence_gpt_review')
SUB=BASE/'submitted'; OUT=BASE/'reviewer'; ROOT=Path('/mnt/data')
sha=lambda b:hashlib.sha256(b).hexdigest()
report={'status':'RUNNING','scope':'Local archive/source-byte audit and corroborating replay of delivered SymPy exact checker; no remote or Windows validation.'}
def safe(z):
    ns=z.namelist()
    assert len(ns)==len(set(ns)), 'duplicate paths'
    assert len(ns)==len(set(n.casefold() for n in ns)), 'case duplicates'
    for i in z.infolist():
        p=PurePosixPath(i.filename)
        assert not p.is_absolute() and '..' not in p.parts and '\\' not in i.filename
        assert not stat.S_ISLNK(i.external_attr>>16)
    assert z.testzip() is None

def audit_manifest(z,name):
    obj=json.loads(z.read(name)); entries=obj.get('files',obj.get('entries'))
    if entries is None: raise RuntimeError(str(obj)[:1200])
    assert len(entries)==len(set(e.get('path',e.get('packet_path')) for e in entries))
    paths=[]
    for e in entries:
        p=e.get('path',e.get('packet_path'));b=z.read(p);paths.append(p)
        assert len(b)==e.get('bytes',e.get('size_bytes')),(p,'length')
        assert sha(b)==e['sha256'],(p,'sha')
    assert set(paths)|{name}==set(z.namelist())
    return len(entries)

archive=ROOT/'NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_REVIEW.zip'
archive_bytes=archive.read_bytes(); assert sha(archive_bytes)==Path(str(archive)+'.sha256').read_text().split()[0]
with zipfile.ZipFile(io.BytesIO(archive_bytes)) as z:
    safe(z);report['archive_members']=len(z.namelist());report['manifest_entries']=audit_manifest(z,'MANIFEST.json')
    for name in z.namelist(): assert (SUB/name).read_bytes()==z.read(name),name
    for external,internal in [('PROOF_REPORT(2).md','PROOF_REPORT.md'),('RESULT_SUMMARY(6).md','RESULT_SUMMARY.md')]:
        assert (ROOT/external).read_bytes()==z.read(internal)
    source_records=json.loads(z.read('CONSUMED_SOURCE_INVENTORY.json'))['records']
    checked_sources=[];git_checked=0
    for e in source_records:
        b=z.read(e['delivered_path']);assert len(b)==e['bytes'] and sha(b)==e['sha256'],e['id']
        g=e.get('git_blob_sha1')
        if g:
            actual=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
            assert actual==g,(e['id'],'git blob');git_checked+=1
        checked_sources.append({'path':e['delivered_path'],'sha256':sha(b)})
    report['source_records']=len(checked_sources); report['git_blob_identities_locally_checked']=git_checked
    report['sources']=checked_sources
    nb=z.read('incoming/NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_CODEX_PACKET.zip')
    assert nb==(ROOT/'NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_CODEX_PACKET.zip').read_bytes()
    with zipfile.ZipFile(io.BytesIO(nb)) as nz:
        safe(nz);report['incoming_packet_members']=len(nz.namelist())
        report['incoming_manifest_entries']=audit_manifest(nz,'PACKET_MANIFEST.json')
        count=0
        for e in source_records:
            if e['origin']=='unchanged_packet_member':
                assert nz.read(e['id'])==z.read(e['delivered_path']);count+=1
        report['inherited_packet_sources_unchanged']=count
    audits=[json.loads((ROOT/n).read_text()) for n in ['FINAL_ARCHIVE_AUDIT(3).json','FINAL_ARCHIVE_AUDIT(4).json']]
    assert audits[0]==audits[1]; ad=audits[0]
    assert ad['sha256']==sha(archive_bytes) and ad['archive_members']==len(z.namelist())
    assert {e['path'] for e in ad['member_audit']}==set(z.namelist())
    for e in ad['member_audit']:
        b=z.read(e['path']);assert len(b)==e['bytes'] and sha(b)==e['sha256']
    report['supplied_duplicate_audits_identical']=True
    cl=json.loads(z.read('CLAIM_LEDGER.json')); assert [c['id'] for c in cl['claims']]==['RD01','RD02','RD03','RD04','RD05']
    for c in cl['claims']:
        for e in c['evidence']: assert e in z.namelist()
    report['claim_records_and_evidence_paths_checked']=5
    for e in z.namelist(): assert sha(z.read(e))==sha((SUB/e).read_bytes())
# Inspect checker source separately before this wrapper is run. It is portable and has no environment guard.
script=SUB/'checks/exact_check.py';t=time.monotonic()
cmd=[sys.executable,'-B',str(script),str(OUT/'replay')]
p=subprocess.run(cmd,cwd=OUT,capture_output=True,text=True,timeout=120)
(OUT/'exact_replay.stdout.txt').write_text(p.stdout)
(OUT/'exact_replay.stderr.txt').write_text(p.stderr)
assert p.returncode==0,p.stderr
fresh=json.loads((OUT/'replay/EXACT_RESULTS.json').read_text()); old=json.loads((SUB/'checks/EXACT_RESULTS.json').read_text())
assert fresh['checks']==old['checks'];assert fresh['formulas']==old['formulas']
assert fresh['status']=='PASS' and fresh['identity_and_control_count']==60
assert all(c['pass'] for c in fresh['checks'])
report.update(status='PASS',archive_sha256=sha(archive_bytes),replay={'argv':cmd,'exit_status':p.returncode,'elapsed_seconds':time.monotonic()-t,'checks':len(fresh['checks']),'exact_checks_and_formulas_match':True,'checker_bytes_unchanged':True,'environment_adaptation':'None; portable checker executed directly; Windows process wrapper not used.','python':platform.python_version(),'sympy':fresh['sympy'],'platform':platform.platform(),'classification':'Replay of same submitted checker and same SymPy backend; not an independent implementation.'})
# Recheck immutable submission after replay.
with zipfile.ZipFile(archive) as z:
    for n in z.namelist(): assert z.read(n)==(SUB/n).read_bytes()
report['submitted_extraction_unchanged_after_replay']=True
(OUT/'AUDIT_AND_REPLAY.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='sources'},indent=2))
