"""Archive and file integrity only; does not execute any enclosed checker."""
from pathlib import Path,PurePosixPath
import json,hashlib,zipfile,io
from prepare_manuscript import ROOT,S4,S5,digest,dump
src=Path('C:/Users/Notandi/Downloads/SRG_SIM04_SIM05_MANUSCRIPT_CODEX_HANDOFF.zip')
assert not (ROOT/'HANDOFF_GATE.json').exists()
b=src.read_bytes();z=zipfile.ZipFile(io.BytesIO(b))
def check(z,name):
    manifest=json.loads(z.read(name));fs=manifest.get('files',manifest)
    if isinstance(fs,dict):fs=[dict(path=k,**v) for k,v in fs.items()]
    for f in fs:
        n=f.get('path',f.get('relative_path'));bb=z.read(n);assert digest(bb)['sha256']==f['sha256'],n
    assert z.testzip() is None
    return len(fs)
check(z,'HANDOFF_MANIFEST.json')
assert z.read('SRG_VOLUME_II_SIM04_SIM05_CODEX_MANUSCRIPT_WORK_ORDER.md')==(ROOT/'evidence/AUTHORITATIVE_WORK_ORDER.md').read_bytes()
for n in ['HANDOFF_MANIFEST.json','INPUT_MANIFEST.json','START_HERE.md']:
    (ROOT/'evidence'/('HANDOFF_'+n if n=='START_HERE.md' else n)).write_bytes(z.read(n))
mi=json.loads(z.read('INPUT_MANIFEST.json'))
for f in mi['files']:assert digest(z.read(f['path']))=={k:f[k] for k in ('bytes','sha256')}
assert z.read('inputs/SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip')==(ROOT/'evidence/inputs/SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip').read_bytes()
review=z.read('inputs/SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip')
(ROOT/'evidence/inputs/SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip').write_bytes(review)
r=zipfile.ZipFile(io.BytesIO(review));count=check(r,'GPT_REVIEW_MANIFEST.json');matched=0
for n in r.namelist():
    p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts
    if n.endswith('/'):continue
    if n.startswith('source_package/'):
        rel=n[len('source_package/'):];assert (S5/rel).read_bytes()==r.read(n),rel;matched+=1
    elif not n.endswith('.py'):
        q=ROOT/'evidence/reviews/SIM05'/n;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(r.read(n))
dump('HANDOFF_BASELINE.json',[dict(original_path=str(src),candidate_path=None,**digest(b))])
dump('HANDOFF_GATE.json',dict(handoff=digest(b),input_manifest_matches=True,separate_work_order_matches=True,review_manifest_members=count,local_SIM05_source_package_members_match=matched,scientific_scripts_executed=0))
gate=json.loads((ROOT/'INPUT_GATE.json').read_text());gate['SIM05_new_GPT_review']='RECEIVED AND IDENTITY VERIFIED';dump('INPUT_GATE.json',gate)
print(json.dumps(dict(review_members_verified=count,local_members_match=matched,scientific_execution=0)))
