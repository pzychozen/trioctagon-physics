"""Curate the bounded review payload and reopen every archive member."""
from common import *
from pathlib import PurePosixPath
import shutil,zipfile,stat
assert read(D/'FINAL_PRESERVATION_CHECK.json')['status']=='PASS'
assert read(D/'CURRENT_DISPOSITION.json')['status']=='COMPLETE_A_TO_B_RETURNED_FOR_GPT_AUTHOR_REVIEW'
stage=R/'payload';delivery=R/'delivery';assert not stage.exists();stage.mkdir();delivery.mkdir(exist_ok=True)
selection={}
def add(name,source):
    p=PurePosixPath(name);assert not p.is_absolute() and '..' not in p.parts and ':' not in name and '\\' not in name
    assert name not in selection and name.casefold() not in {x.casefold() for x in selection}
    assert source.is_file() and not source.is_symlink();selection[name]=source
for folder in ['data','sources','packet','scripts','figures']:
    for p in sorted((R/folder).rglob('*')):
        if p.is_file():
            assert p.suffix not in ['.pyc','.ttf','.otf','.tfm','.aux','.xdv']
            add(folder+'/'+p.relative_to(R/folder).as_posix(),p)
for name in ['RESULT_SUMMARY.md','PROOF_REPORT.md','PRIOR_WORK_COMPARISON.md','CLAIM_LEDGER.json','METHOD_AND_RESOURCE_PLAN.md','REPRODUCIBILITY.md','run_python.cmd']:add(name,R/name)
omitted=[]
for p in sorted(L.iterdir()):
    if not p.is_file():continue
    if p.name.startswith(('private_','checkpoint_tree_paths.')):omitted.append(p.name);continue
    add('logs/'+p.name,p)
incoming=Path(r'C:\Users\Notandi\Downloads\TRIOCTAGON_OUTER_ENVELOPE_01_CODEX_PACKET.zip');identity=read(D/'INPUT_VERIFICATION.json');assert sha(incoming.read_bytes())==identity['packet_sha256'];add('incoming/'+incoming.name,incoming)
for name,source in selection.items():
    p=stage/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,p);assert p.read_bytes()==source.read_bytes()
write(stage/'data/REVIEW_PAYLOAD_SCOPE.json',{'created_utc':now(),'included':'New proof/report/checker/certificate, complete relevant original sources and original packet, actual scientific and documentary execution logs, computed illustration and review records.','excluded':'Whole-repository status/diff/path dumps and private baseline, external scratch, font/config caches, unrelated repository content.','omitted_private_log_names':omitted,'interpretation':'The execution ledger retains the read-only command records; raw unrelated user-edit contents are intentionally not bundled.','no_repository_writes':True})
files=[]
for p in sorted(stage.rglob('*')):
    if p.is_file():
        b=p.read_bytes();files.append({'path':p.relative_to(stage).as_posix(),'bytes':len(b),'sha256':sha(b)})
manifest={'format':'TRIOCTAGON_OUTER_ENVELOPE_REVIEW_RAW_BYTE_MANIFEST_v1','created_utc':now(),'task':'TRIOCTAGON_OUTER_ENVELOPE_01','self_exclusion':'PAYLOAD_MANIFEST.json only; manifest and finished archive hashes are bound by the external FINAL_ARCHIVE_AUDIT.json.','files':files}
write(stage/'PAYLOAD_MANIFEST.json',manifest)
name='TRIOCTAGON_OUTER_ENVELOPE_01_REVIEW.zip';dest=delivery/name;assert not dest.exists()
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
    for p in sorted(stage.rglob('*')):
        if p.is_file():z.write(p,p.relative_to(stage).as_posix())
expected={r['path']:r for r in files};mp=stage/'PAYLOAD_MANIFEST.json';expected['PAYLOAD_MANIFEST.json']={'bytes':mp.stat().st_size,'sha256':sha(mp.read_bytes())};audited=[]
with zipfile.ZipFile(dest) as z:
    names=z.namelist();assert len(names)==len(set(names))==len({n.casefold() for n in names}) and set(names)==set(expected);assert z.testzip() is None
    for info in z.infolist():
        p=PurePosixPath(info.filename);assert not p.is_absolute() and '..' not in p.parts and ':' not in info.filename and '\\' not in info.filename
        assert not stat.S_ISLNK(info.external_attr>>16)
        b=z.read(info);r=expected[info.filename];assert len(b)==r['bytes'] and sha(b)==r['sha256'],info.filename
        audited.append({'path':info.filename,'bytes':len(b),'sha256':sha(b),'result':'MATCH'})
    assert z.read('data/exact_certificate.json')==(D/'exact_certificate.json').read_bytes()
    assert z.read('incoming/'+incoming.name)==incoming.read_bytes()
    with zipfile.ZipFile(incoming) as old:
        assert old.testzip() is None and len(old.namelist())==identity['packet_members']
        for n in old.namelist():assert old.read(n)==z.read('packet/'+n),n
    for row in read(S/'SOURCE_IDENTITY_MANIFEST.json')['sources']:assert sha(z.read('sources/'+row['path']))==row['sha256']
    assert sha(z.read('figures/local_facet_transition.png'))==read(R/'figures/VISUAL_INSPECTION.json')['final_png_sha256']
digest=sha(dest.read_bytes());(delivery/(name+'.sha256')).write_text(digest+'  '+name+'\n',encoding='ascii')
write(delivery/'FINAL_ARCHIVE_AUDIT.json',{'status':'PASS','checked_utc':now(),'archive':str(dest),'archive_bytes':dest.stat().st_size,'archive_sha256':digest,'archive_member_count':len(expected),'manifest_entries':len(files),'manifest_sha256':sha(mp.read_bytes()),'every_member_reopened_and_full_size_sha256_checked':True,'crc':'PASS','safe_unique_case_unique_paths_and_no_symlinks':True,'original_packet_bytes_preserved':True,'original_packet_members_cross_compared':identity['packet_members'],'authenticated_source_files_rechecked':len(read(S/'SOURCE_IDENTITY_MANIFEST.json')['sources']),'exact_certificate_sha256':sha((D/'exact_certificate.json').read_bytes()),'final_inspected_figure_bound':True,'repository_preservation_record':'data/FINAL_PRESERVATION_CHECK.json','scientific_result_status':'Complete A-B classification; returned for GPT/author review, not published or externally peer reviewed.','members':audited})
write(delivery/'RETURN_RECEIPT.json',{'task':'TRIOCTAGON_OUTER_ENVELOPE_01','recorded_utc':now(),'status':'COMPLETE_RETURNED_FOR_REVIEW','review_zip':name,'bytes':dest.stat().st_size,'sha256':digest,'members':len(expected),'member_audit':'FINAL_ARCHIVE_AUDIT.json','prior_work_gate':'DISTINCT_GAP','new_result':'Exactly one interior noncollision face-lattice transition at x=3(sqrt(2)-1)/2; complete A-B maximal-face certificate.','interior_VEF':[[42,96,56],[42,84,44],[42,90,50]],'ten_vertex_maximal_facets':0,'checker_and_controls':'PASS','repository_and_all_originals':'UNCHANGED','commit_push_publication':False,'next_step':'GPT/author review; no automatic sequel.'})
print(json.dumps({'status':'PASS','archive':str(dest),'bytes':dest.stat().st_size,'sha256':digest,'members_reopened':len(expected),'manifest_entries':len(files)},indent=2))
