from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
import json,zipfile,io,stat,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'received'; SUB=ROOT/'submitted'; OUT=ROOT/'reviewer'
def sha(b): return hashlib.sha256(b).hexdigest()
def blob(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
zip_path=BASE/'TRIOCTAGON_OUTER_ENVELOPE_01_REVIEW.zip'
b=zip_path.read_bytes(); sidecar=(BASE/(zip_path.name+'.sha256')).read_text().split()[0]
audit=read(BASE/'FINAL_ARCHIVE_AUDIT(1).json')
assert sha(b)==sidecar==audit['archive_sha256']
assert len(b)==audit['archive_bytes']
rows=[]
with zipfile.ZipFile(io.BytesIO(b)) as z:
 names=z.namelist();assert len(names)==len(set(names))==len(set(n.casefold() for n in names))==143
 assert z.testzip() is None
 for i in z.infolist():
  p=PurePosixPath(i.filename)
  assert not p.is_absolute() and '..' not in p.parts and '\\' not in i.filename and not stat.S_ISLNK(i.external_attr>>16)
 manifest=json.loads(z.read('PAYLOAD_MANIFEST.json'))
 mm={r['path']:r for r in manifest['files']};assert set(mm)==set(names)-{'PAYLOAD_MANIFEST.json'} and len(mm)==142
 aa={r['path']:r for r in audit['members']};assert set(aa)==set(names)
 assert sha(z.read('PAYLOAD_MANIFEST.json'))==audit['manifest_sha256']
 for n in names:
  data=z.read(n);assert (SUB/n).read_bytes()==data
  for row in [aa[n]]+([mm[n]] if n in mm else []):assert len(data)==row['bytes'] and sha(data)==row['sha256']
  rows.append({'path':n,'bytes':len(data),'sha256':sha(data),'result':'MATCH'})
 packet=z.read('incoming/TRIOCTAGON_OUTER_ENVELOPE_01_CODEX_PACKET.zip')
 assert packet==(BASE/'TRIOCTAGON_OUTER_ENVELOPE_01_CODEX_PACKET.zip').read_bytes()
 with zipfile.ZipFile(io.BytesIO(packet)) as pz:
  pnames=pz.namelist();assert pz.testzip() is None
  for n in pnames:assert pz.read(n)==z.read('packet/'+n)
 for loose,n in [('RESULT_SUMMARY(5).md','RESULT_SUMMARY.md'),('PROOF_REPORT(1).md','PROOF_REPORT.md')]:assert (BASE/loose).read_bytes()==z.read(n)
source_rows=[]
for filename in ['SOURCE_COPY_RECEIPT.json','ADDITIONAL_SOURCE_IDENTITIES.json']:
 obj=read(SUB/'sources'/filename)
 lists=[v for v in obj.values() if isinstance(v,list) and v and isinstance(v[0],dict) and 'path' in v[0] and 'sha256' in v[0]]
 assert len(lists)==1
 for r in lists[0]:
  data=(SUB/'sources'/r['path']).read_bytes()
  assert len(data)==r['bytes'] and sha(data)==r['sha256']
  if r.get('git_blob_sha1'):assert blob(data)==r['git_blob_sha1']
  source_rows.append({'id':r['id'],'path':r['path'],'sha256':sha(data),'git_blob_sha1':blob(data) if r.get('git_blob_sha1') else None,'result':'MATCH'})
assert len(source_rows)==24 and len({r['id'] for r in source_rows})==24
result={'status':'PASS','reviewed_utc':datetime.now(timezone.utc).isoformat(),'archive':zip_path.name,'archive_bytes':len(b),'archive_sha256':sha(b),'members':rows,'member_count':len(rows),'manifest_count':len(mm),'packet_member_count':len(pnames),'source_count':len(source_rows),'source_rows':source_rows,'standalone_reports_match':True,'external_sidecar_matches':True,'external_audit_matches':True,'source_identity_scope':'Compared local bytes, recorded SHA-256 and Git blob identities; no new remote retrieval or Windows checkout audit.','scientific_proof_scope':'Integrity audit only; hashes do not establish the theorem.'}
(OUT/'SUBMISSION_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','archive_sha256','member_count','manifest_count','packet_member_count','source_count']},indent=2))
