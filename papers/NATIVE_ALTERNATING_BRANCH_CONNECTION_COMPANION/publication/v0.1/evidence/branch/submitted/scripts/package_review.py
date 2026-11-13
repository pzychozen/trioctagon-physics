"""Seal one review return and verify every actual final archive member."""
from common import *
from pathlib import PurePosixPath
import zipfile,shutil
started=now();assert read(L/'FINAL_PRESERVATION_AND_CLAIM_AUDIT.json')['status']=='PASS'
assert read(D/'CERTIFICATE_CHECK.json')['status']=='PASS'
out=R/'delivery';out.mkdir(exist_ok=True)
archive=out/'NATIVE_ALTERNATING_BRANCH_CONNECTION_01_REVIEW.zip';assert not archive.exists()
write(L/'PACKAGE_EXECUTION.json',{'started_utc':started,'command':['run_python.cmd','scripts\\package_review.py'],'shell':'Windows Command Prompt','conda_environment':os.environ['CONDA_DEFAULT_ENV'],'python':sys.version,'executable':sys.executable,'script_sha256':sha(Path(__file__).read_bytes()),'final_exit_and_archive_identity':'External NATIVE_ALTERNATING_BRANCH_CONNECTION_01_FINAL_DELIVERY_AUDIT.json; written after final archive reopen'})
roots=['data','logs','packet','received','scripts','sources']
paths=[]
for folder in roots:paths += [p for p in (R/folder).rglob('*') if p.is_file()]
paths += [p for p in R.iterdir() if p.is_file() and p.name!='REVIEW_MANIFEST.json']
assert all('__pycache__' not in p.parts and p.suffix!='.pyc' for p in paths)
rows=[]
for p in sorted(paths):
    b=p.read_bytes();rows.append({'path':p.relative_to(R).as_posix(),'bytes':len(b),'sha256':sha(b)})
write(R/'REVIEW_MANIFEST.json',{'task':'NATIVE_ALTERNATING_BRANCH_CONNECTION_01','disposition':'Full connection certified for review; full-range stability unresolved','self_excluded':'REVIEW_MANIFEST.json','count_excluding_self':len(rows),'files':rows})
manifest=R/'REVIEW_MANIFEST.json';rows.append({'path':manifest.name,'bytes':manifest.stat().st_size,'sha256':sha(manifest.read_bytes())})
with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for row in sorted(rows,key=lambda x:x['path']):z.write(R/row['path'],row['path'])
with zipfile.ZipFile(archive,'r') as z:
    names=z.namelist();expected={row['path']:row for row in rows}
    assert len(names)==len(set(names))==len(expected) and set(names)==set(expected)
    assert z.testzip() is None
    for name in names:
        path=PurePosixPath(name);assert not path.is_absolute() and '..' not in path.parts and '\\' not in name
        b=z.read(name);row=expected[name]
        assert len(b)==row['bytes'] and sha(b)==row['sha256'] and b==(R/name).read_bytes()
archive_sha=sha(archive.read_bytes())
(out/(archive.name+'.sha256')).write_text(archive_sha+'  '+archive.name+'\n',encoding='ascii')
for name in ['RESULT_SUMMARY.md','PROOF_REPORT.md']:shutil.copy2(R/name,out/name)
audit={'status':'PASS','finished_utc':now(),'command':['run_python.cmd','scripts\\package_review.py'],'exit_status':0,'archive':str(archive),'archive_bytes':archive.stat().st_size,'archive_sha256':archive_sha,'actual_member_count':len(rows),'crc_check':'PASS','all_names_unique_safe_and_exact':True,'every_member_complete_bytes_and_sha256_match_manifest_and_source':True,'manifest_self_excluded':True,'source_and_operator_preservation':'PASS; logs/FINAL_PRESERVATION_AND_CLAIM_AUDIT.json','new_certificate_check':'PASS','exact_algebra_and_source_checks':31,'rejection_controls':4,'standalone_outputs':{name:{'path':str(out/name),'bytes':(out/name).stat().st_size,'sha256':sha((out/name).read_bytes())} for name in ['RESULT_SUMMARY.md','PROOF_REPORT.md']},'members':sorted(rows,key=lambda x:x['path'])}
write(out/'NATIVE_ALTERNATING_BRANCH_CONNECTION_01_FINAL_DELIVERY_AUDIT.json',audit)
print(json.dumps({k:audit[k] for k in ['status','archive','archive_bytes','archive_sha256','actual_member_count','standalone_outputs']},indent=2))
