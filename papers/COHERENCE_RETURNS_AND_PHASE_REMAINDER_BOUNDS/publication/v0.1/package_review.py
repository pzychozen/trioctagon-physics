"""Package the review artifacts and verify every archived byte; no science."""
from pathlib import Path
import json,hashlib,zipfile,datetime
ROOT=Path(__file__).resolve().parent
ZIP=ROOT/'NCM_PAPER_01_v0.1_REVIEW.zip'
assert not ZIP.exists(),'Refuse to overwrite an already completed review archive.'
def fp(b): return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def save(name,obj): (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=json.loads((ROOT/'qa/REVIEW_VERIFICATION.json').read_text())
assert qa['failures']==[] and qa['native_F_evaluations']==0
source=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
for r in source['sources'].values():
    assert fp(Path(r['path']).read_bytes())==r['before']
for r in source['packet_members']:
    assert fp((ROOT/r['path']).read_bytes())==r['after']
assert fp(Path(source['packet_zip']['path']).read_bytes())==source['packet_zip']['before']

assetmap=json.loads((ROOT/'manuscript/math_asset_manifest.json').read_text())
activeassets={'manuscript/math_assets/'+v['file'] for v in assetmap.values()}
files=[]
excluded={'OUTPUT_HASHES.json','ARCHIVE_RECEIPT.json',ZIP.name}
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT).as_posix()
    if rel in excluded or rel.split('/')[0] in {'scratch','mplconfig'}:continue
    if '__pycache__' in p.parts or p.suffix.lower() in {'.pyc','.ttf','.otf','.woff','.woff2'}:continue
    if rel.startswith('manuscript/math_assets/') and rel not in activeassets:continue
    assert not p.is_symlink(),rel
    files.append((p,rel))
hashes={rel:fp(p.read_bytes()) for p,rel in files}
save('OUTPUT_HASHES.json',{'scope':'Files included in the review ZIP, excluding this manifest itself. ZIP and external receipt are excluded to avoid self-reference.','files':hashes})
files.append((ROOT/'OUTPUT_HASHES.json','OUTPUT_HASHES.json'))
with zipfile.ZipFile(ZIP,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p,rel in files:z.write(p,rel)
with zipfile.ZipFile(ZIP) as z:
    assert len(z.namelist())==len(files)==len(set(z.namelist()))
    assert z.testzip() is None
    archived=json.loads(z.read('OUTPUT_HASHES.json'))
    assert archived['files']==hashes
    for p,rel in files:
        assert z.read(rel)==p.read_bytes(),rel
        if rel!='OUTPUT_HASHES.json':assert fp(z.read(rel))==hashes[rel]
receipt={'archive':ZIP.name,**fp(ZIP.read_bytes()),'entry_count':len(files),
         'manifest_file_count':len(hashes),'archived_member_verification':'PASS: every member matches local bytes; all manifest-listed members match size and SHA-256; ZIP CRC test passed.',
         'output_hashes_sha256':fp((ROOT/'OUTPUT_HASHES.json').read_bytes())['sha256'],
         'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'native_F_evaluations':0,'old_scientific_scripts_executed':0,
         'source_preservation':'PASS: all bounded inputs rechecked immediately before archive construction.',
         'status':'Research draft v0.1 — for GPT/author review; not publication approval.'}
save('ARCHIVE_RECEIPT.json',receipt)
print(json.dumps(receipt,ensure_ascii=False,indent=2))
