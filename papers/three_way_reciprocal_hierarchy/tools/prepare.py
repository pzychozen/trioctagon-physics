"""Freeze read-only inputs and protected-file identities for Paper II."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
BASE=REPO.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for d in ['source','figures','verification/hierarchy','verification/cubic','provenance/sources','records','output/pdf']:
    (ROOT/d).mkdir(parents=True,exist_ok=True)
baseline=ROOT/'records/baseline.json'
if not baseline.exists():
    tracked=subprocess.check_output(['git','ls-files','-z'],cwd=REPO).decode().split('\0')
    protected={REPO/x for x in tracked if x}
    for d in ['papers/three_way_reconstruction','kernel_physics','apps/scientific_ui']:
        protected.update(p for p in (REPO/d).rglob('*') if p.is_file())
    for d in ['three_way_reciprocal_hierarchy_20261005','three_way_cubic_elliptic_20261005']:
        protected.update(p for p in (BASE/'research'/d).rglob('*') if p.is_file())
    baseline.write_text(json.dumps(dict(head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),status=subprocess.check_output(['git','status','--short'],cwd=REPO,text=True),files={str(p):sha(p) if p.is_file() else None for p in sorted(protected)}),indent=2),encoding='utf-8')
sources={
'HIERARCHY':BASE/'research/three_way_reciprocal_hierarchy_20261005/THREE_WAY_RECIPROCAL_HIERARCHY_n2_n4_v0.1.md',
'CUBIC':BASE/'research/three_way_cubic_elliptic_20261005/THREE_WAY_CUBIC_ELLIPTIC_CORRESPONDENCE_v0.1.md',
'PATCH':REPO/'research/GATE_TORUS_INVESTIGATION_v0.1/REPORT.md',
'SCAFFOLD':REPO/'kernel_physics/reference_scaffold.py',
'BOUNDARY':REPO/'kernel_physics/boundary_response.py',
'SRG':REPO/'kernel_physics/srg.py',
'OPERATING':REPO/'kernel_physics/operating_region.py',
'GEOMETRY':REPO/'kernel_physics/geometry.py',
'Z_READOUT':REPO/'kernel_physics/z_manifold.py',
'SCAFFOLD_PROOF':BASE/'research/GPT_proof/TRIOCTAGON_HEXAGON_CORE_DERIVATION_v0.1.md',
}
manifest=[]
for key,p in sources.items():
    dest=ROOT/'provenance/sources'/(key+p.suffix)
    shutil.copyfile(p,dest)
    lines=p.read_text(encoding='utf-8-sig').splitlines()
    (ROOT/'provenance/sources'/(key+'.numbered.txt')).write_text('\n'.join(f'{i:04d}: {line}' for i,line in enumerate(lines,1))+'\n',encoding='utf-8')
    manifest.append(dict(id=key,original=str(p),snapshot=str(dest.relative_to(ROOT)),sha256=sha(p),lines=len(lines)))
for key,folder,script in [('hierarchy','three_way_reciprocal_hierarchy_20261005','verify_hierarchy.py'),('cubic','three_way_cubic_elliptic_20261005','verify_cubic_elliptic.py')]:
    p=BASE/'research'/folder/script
    dest=ROOT/'verification'/key/script
    shutil.copyfile(p,dest)
    manifest.append(dict(id=key.upper()+'_VERIFIER',original=str(p),snapshot=str(dest.relative_to(ROOT)),sha256=sha(p)))
(ROOT/'provenance/source_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
shutil.copyfile('C:/Users/Notandi/.codex/attachments/52953260-a514-4c7c-ad1c-3737105b99bc/Pasted text.txt',ROOT/'provenance/work_order.txt')
print('Prepared',len(manifest),'sources; protected',len(json.loads(baseline.read_text())['files']),'file identities.')
