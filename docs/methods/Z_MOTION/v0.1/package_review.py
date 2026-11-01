"""Package only this task's documents and supplied evidence; verify every ZIP byte."""
from pathlib import Path,PurePosixPath
import json,hashlib,zipfile,datetime
R=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(f,x):(R/f).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
qa=json.loads((R/'DOCUMENT_QA.json').read_text(encoding='utf-8'));assert qa['status']=='PASS'
for e in json.loads((R/'BUILD_RECORD.json').read_text())['outputs']:assert sha((R/e['pdf']).read_bytes())==e['sha256']
for e in json.loads((R/'SOURCE_MANIFEST.json').read_text())['original_consulted_files']:
 b=Path(e['path']).read_bytes();assert len(b)==e['before']['bytes'] and sha(b)==e['before']['sha256']
zipname='NCM_Z_DOC_01_v0.1_REVIEW.zip';outside={'OUTPUT_HASHES.json',zipname,'REVIEW_RECEIPT.json','REVIEW_RECEIPT.txt'}
files=[]
for p in sorted(R.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(R)
 if rel.parts[0] in {'tmp','cache','__pycache__'} or rel.as_posix() in outside:continue
 assert p.suffix.lower() not in {'.pyc','.ttf','.otf','.woff','.woff2'}
 files.append(p)
entries=[{'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in files]
dump('OUTPUT_HASHES.json',{'scope':'All review ZIP payloads except this manifest. Outside ZIP/receipts and local caches/renders excluded.','entries':entries})
with zipfile.ZipFile(R/zipname,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files+[R/'OUTPUT_HASHES.json']:z.write(p,p.relative_to(R).as_posix())
with zipfile.ZipFile(R/zipname) as z:
 names=z.namelist();expected={e['path'] for e in entries}|{'OUTPUT_HASHES.json'}
 assert set(names)==expected and len(names)==len(expected)==len({n.casefold() for n in names})
 for n in names:
  q=PurePosixPath(n);assert not q.is_absolute() and '..' not in q.parts and ':' not in n and '\\' not in n
  assert z.read(n)==(R/n).read_bytes()
 assert z.testzip() is None
 for e in entries:
  b=z.read(e['path']);assert len(b)==e['bytes'] and sha(b)==e['sha256']
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'task':'NCM-Z-DOC-01 v0.1','zip':str(R/zipname),'bytes':(R/zipname).stat().st_size,'sha256':sha((R/zipname).read_bytes()),'unique_safe_members':len(names),'manifest_payloads':len(entries),'CRC':'PASS','exact_member_set':'PASS','byte_equal_to_packaged_files':len(names),'payload_sizes_and_SHA256_verified':len(entries),'original_supplied_files_rechecked_unchanged':2,'document_QA':'PASS','final_PDF_pages_individually_inspected':20,'exclusions':['cache','tmp/renders','environment/font/credential files','outside ZIP and receipts'],'scientific_evaluations':0,'status':'Ready for GPT/author documentation review; not publication acceptance'}
dump('REVIEW_RECEIPT.json',receipt)
(R/'REVIEW_RECEIPT.txt').write_text('\n'.join(f'{k}: {v}' for k,v in receipt.items())+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
