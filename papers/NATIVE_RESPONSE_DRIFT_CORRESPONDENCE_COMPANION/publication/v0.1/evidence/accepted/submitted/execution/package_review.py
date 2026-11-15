from audit import *
import shutil, io, ast, re
delivery=ROOT/'delivery';delivery.mkdir(exist_ok=True)
before=json.loads((ROOT/'private/before.json').read_text())
after=json.loads((ROOT/'private/after.json').read_text())
differences=[k for k in before if before[k]!=after.get(k)]
assert not differences,differences
write(OUT/'records/REPOSITORY_PRESERVATION.json',{
 'status':'PASS','repository':str(REPO),'head':before['head'],'branch':before['branch'],
 'modified_or_untracked_files_compared':len(before['files']),
 'equal_fields':['HEAD','branch','refs','local config','raw index','status','staged diff','unstaged diff','all enumerated modified/untracked raw file identities'],
 'differences':differences,'raw_unrelated_inventories_distributed':False,
 'scope':'Tracked changes detected through unchanged staged/unstaged differences; individual raw hashes for modified/untracked files. Ignored files are not an all-machine snapshot.',
 'repository_writes':0,'commits':0,'pushes':0})
inv=json.loads((OUT/'CONSUMED_SOURCE_INVENTORY.json').read_text())['records']
for r in inv:
    b=(OUT/r['delivered_path']).read_bytes()
    assert len(b)==r['bytes'] and sha(b)==r['sha256'],r['id']
    if r['origin']=='local_file':assert Path(r['original_path']).read_bytes()==b
for name in ['audit.py','source_gate.py','finalize.py','run_python.cmd','package_review.py']:
    shutil.copyfile(ROOT/name,OUT/'execution'/name)
initial=json.loads((OUT/'checks/initial_completed/EXACT_RESULTS.json').read_text())
final=json.loads((OUT/'checks/EXACT_RESULTS.json').read_text())
assert initial['checks']==final['checks'] and initial['formulas']==final['formulas']
assert final['status']=='PASS' and len(final['checks'])==60 and all(c['pass'] for c in final['checks'])
run=json.loads((OUT/'checks/RUN_RECORD.json').read_text())
assert sha((OUT/'checks/exact_check.py').read_bytes())==run['worker_sha256']
assert sha((OUT/'checks/run_exact.py').read_bytes())==run['runner_sha256']
assert run['returncode']==0 and run['termination_reason'] is None
standalones=[]
for name,member in [('NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_CODEX_WORK_ORDER.md','NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_CODEX_WORK_ORDER.md'),('NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_GPT_ANALYTICAL_START.md','GPT_ANALYTICAL_START.md'),('NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_PRIOR_WORK_COMPARISON.md','PRIOR_WORK_COMPARISON.md')]:
    p=Path(r'C:\Users\Notandi\Downloads')/name
    if p.exists():
        b=p.read_bytes(); assert b==(ROOT/'packet'/member).read_bytes()
        standalones.append({'name':name,'packet_member':member,'sha256':sha(b),'match':True})
write(OUT/'records/STANDALONE_INPUT_MATCHES.json',standalones)
ledger=json.loads((OUT/'CLAIM_LEDGER.json').read_text())
assert [r['id'] for r in ledger['claims']]==['RD01','RD02','RD03','RD04','RD05']
for claim in ledger['claims']:
    for path in claim['evidence']:assert (OUT/path).is_file(),path
proof=(OUT/'PROOF_REPORT.md').read_text(encoding='utf-8')
assert proof.count('\\[')==proof.count('\\]')
assert proof.count('\\(')==proof.count('\\)')
assert re.findall(r'\\tag\{(\d+)\}',proof)==[str(i) for i in range(1,26)]
for p in OUT.rglob('*.py'):ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
write(OUT/'records/REVIEW_PREFLIGHT.json',{'status':'PASS','claims':5,'distinct_exact_algebra_controls':60,'completed_new_symbolic_workers':2,'same_predicates_and_formulas_on_portable_reproduction':True,'worker_source_hash_match':True,'proof_equation_tags':25,'math_delimiters_balanced':True,'consumed_sources_unchanged':len(inv),'local_repository_preserved':True,'new_numerical_fixtures':0,'historical_scientific_executions':0,'subagents':0,'no_network_requests':True,'package_scope':'Proof review only; no PDF/manuscript/publication'})
# The original compressed input is the sole authoritative packet archive.
packet_name='NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_CODEX_PACKET.zip'
original=Path(r'C:\Users\Notandi\Downloads')/packet_name
assert (OUT/'incoming'/packet_name).read_bytes()==original.read_bytes()
members=[]
for p in sorted(OUT.rglob('*')):
    if p.is_file() and p.name!='MANIFEST.json':
        rel=p.relative_to(OUT).as_posix()
        assert not any(part in ('private','__pycache__') for part in Path(rel).parts)
        b=p.read_bytes();members.append({'path':rel,'bytes':len(b),'sha256':sha(b)})
write(OUT/'MANIFEST.json',{'self_excluded':'MANIFEST.json','files':members})
zpath=delivery/'NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_REVIEW.zip'
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(OUT.rglob('*')):
        if p.is_file():z.write(p,p.relative_to(OUT).as_posix())
member_audit=[]
with zipfile.ZipFile(zpath) as z:
    names=z.namelist();assert len(names)==len(set(x.casefold() for x in names))
    assert all(not n.startswith(('/','\\')) and ':' not in n and '..' not in Path(n).parts for n in names)
    assert set(names)=={r['path'] for r in members}|{'MANIFEST.json'}
    saved=json.loads(z.read('MANIFEST.json'));assert saved['files']==members
    for r in members:
        b=z.read(r['path']);assert len(b)==r['bytes'] and sha(b)==r['sha256']
        assert b==(OUT/r['path']).read_bytes()
        member_audit.append({**r,'pass':True})
    assert z.testzip() is None
    packet_bytes=z.read('incoming/'+packet_name);assert packet_bytes==original.read_bytes()
    with zipfile.ZipFile(io.BytesIO(packet_bytes)) as inner:
        inner_manifest=json.loads(inner.read('PACKET_MANIFEST.json'))
        assert set(inner.namelist())=={r['path'] for r in inner_manifest['files']}|{'PACKET_MANIFEST.json'}
        for r in inner_manifest['files']:
            b=inner.read(r['path']);assert sha(b)==r['sha256'] and len(b)==r['bytes']
        for r in inv:
            if r['origin']=='unchanged_packet_member':assert inner.read(r['id'])==z.read(r['delivered_path'])
        assert inner.testzip() is None
zbytes=zpath.read_bytes();digest=sha(zbytes)
(delivery/(zpath.name+'.sha256')).write_text(digest+'  '+zpath.name+'\n',encoding='ascii')
audit={'status':'PASS','task':'NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01','audited_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive':zpath.name,'bytes':len(zbytes),'sha256':digest,'archive_members':len(names),'self_excluding_manifest_entries':len(members),'manifest_member_sha256':sha((OUT/'MANIFEST.json').read_bytes()),'all_members_reopened_and_compared':True,'safe_case_unique_paths':True,'crc_pass':True,'nested_incoming_members':len(inner_manifest['files'])+1,'nested_incoming_sha256':sha(packet_bytes),'unchanged_packet_sources':18,'all_consumed_source_records':len(inv),'repository_preservation':'PASS','exact_predicates':60,'member_audit':member_audit}
write(delivery/'FINAL_ARCHIVE_AUDIT.json',audit)
print(json.dumps({k:v for k,v in audit.items() if k!='member_audit'},indent=2))
