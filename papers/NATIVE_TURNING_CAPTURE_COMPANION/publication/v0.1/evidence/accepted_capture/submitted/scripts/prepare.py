"""Input identity and targeted overlap-source collection only; no native updates."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,platform,re,shutil,sys,zipfile
R=Path(__file__).resolve().parents[1]; P=R/'packet'; W=Path(r'C:\TORMENT\TRIOCTAGON_new\wt-swct-pub01')
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
def digest(b):return hashlib.sha256(b).hexdigest()
def write(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
archive=R/'received/NATIVE_TURNING_CAPTURE_01_CODEX_PACKET.zip'; expected=(R/'received/NATIVE_TURNING_CAPTURE_01_CODEX_PACKET.zip.sha256').read_text().split()[0]
assert digest(archive.read_bytes())==expected
manifest=json.loads((P/'PACKET_MANIFEST.json').read_text())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    names=[n for n in z.namelist() if not n.endswith('/')]
    assert set(names)=={i['path'] for i in manifest['files']}|{'PACKET_MANIFEST.json'}
    for n in names:assert (P/n).read_bytes()==z.read(n)
for item in manifest['files']:
    b=(P/item['path']).read_bytes();assert digest(b)==item['sha256'] and len(b)==item['bytes']
assert (R/'received/NATIVE_TURNING_CAPTURE_01_CODEX_WORK_ORDER.md').read_bytes()==(P/'NATIVE_TURNING_CAPTURE_01_CODEX_WORK_ORDER.md').read_bytes()
assert (R/'received/NATIVE_TURNING_CAPTURE_01_PRIOR_WORK_COMPARISON.md').read_bytes()==(P/'PRIOR_WORK_COMPARISON.md').read_bytes()
sources=[]
def add(p,key,role):
    b=p.read_bytes(); out=R/'sources'/key;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b)
    sources.append({'id':key,'path':out.relative_to(R).as_posix(),'original_path':str(p),'bytes':len(b),'sha256':digest(b),'git_blob_computed_without_git':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'role':role,'checkpoint_context':'Local published corpus from previous publication at 564810272703403af413e60ee2d44b32effbd79a; no fresh remote/archival audit or Git command in this investigation.'})
named={
'catalog.md':'README.md',
'atlas.md':'research/mathematical_atlas/README.md',
'atlas09.md':'research/mathematical_atlas/entry_09_bounded_operating_region/TRIOCTAGON_ATLAS_09_BOUNDED_OPERATING_REGION_SOURCE_PACKET_v0.1.md',
'collective/main.tex':'papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex',
'collective/CLAIM_SOURCE_MAP.md':'papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/CLAIM_SOURCE_MAP.md',
'collective/references.tex':'papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/references.tex',
'collective/turning.json':'papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/evidence/turning_witness_20261028.json',
'collective/turning.py':'papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/evidence/turning_witness_20261028.py',
'collective/domain.json':'papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/evidence/moving_mean_domain_constants_20261028.json',
'dynamics.py':'kernel_physics/dynamics.py',
'returns/main.tex':'papers/COHERENCE_RETURNS_AND_PHASE_REMAINDER_BOUNDS/publication/v0.1/manuscript/main.tex',
'returns/EVIDENCE_INDEX.md':'papers/COHERENCE_RETURNS_AND_PHASE_REMAINDER_BOUNDS/publication/v0.1/EVIDENCE_INDEX.md',
'paper_g.tex':'papers/PAPER_G/v0.1.1/source/paper_g.tex',
'M3_ACCEPTANCE.md':'papers/PAPER_G/v0.1.1/reproducibility/authorities/M3_JOINT_ACCEPTANCE.md',
'drift.tex':'papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/manuscript.tex',
'D0.md':'papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/supplement/historical/D0_chiral_reference_20261006/D0_CHIRAL_REFERENCE_AND_RECONCILIATION.md',
'D1_CLOSEOUT.md':'papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/supplement/reviewer/D1_GPT_REVIEW/D1_SCIENTIFIC_CLOSEOUT.md',
'NRG_LEDGER.md':'papers/NATIVE_RESPONSE_GEOMETRY/provenance/THEOREM_LEDGER.md',
'strength_pattern.tex':'papers/STRENGTH_PATTERN_IDENTIFIABILITY/v0.1/source/SPR01_STRENGTH_PATTERN_IDENTIFIABILITY_v0.1.tex',
'Z/EVIDENCE_INDEX.md':'docs/methods/Z_MOTION/v0.1/EVIDENCE_INDEX.md',
'Z/CLAIM_SOURCE_MAP.md':'docs/methods/Z_MOTION/v0.1/CLAIM_SOURCE_MAP.md',
'central_route_discussion.tex':'papers/CENTRAL_ROUTE_SIX_OPENING_CORRESPONDENCE/publication/v0.1/sections/09_discussion.tex',
'transport_discussion.tex':'papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/sections/09_discussion.tex',
}
for key,rel in named.items():
    p=W/rel
    if p.exists():add(p,key,'Controlling theorem/evidence or targeted N01 overlap and scope reading; historical scripts not executed.')
    else: print('Optional source path not found:',rel)
for tag,rel in [('potential','papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript'),('phase','papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/publication/v0.1/manuscript'),('NRG','papers/NATIVE_RESPONSE_GEOMETRY/manuscript')]:
    for p in sorted((W/rel).glob('*.tex')):add(p,tag+'/'+p.name,'N01 full-source keyword and theorem/hypothesis comparison.')
ctx=W/'papers/COHERENCE_RETURNS_AND_PHASE_REMAINDER_BOUNDS/publication/v0.1/packet/NCM_PAPER_01_Codex_Packet_v0.1/context'
for name in ['NCM_DUAL_01_REPORT.md','NCM_DUAL_02_REPORT.md','NCM_DUAL_03_REPORT.md','NCM_DUAL_03_PLAN.md','NCM_DUAL_03_ATTEMPTS.md']:
    add(ctx/name,'NCM/'+name,'N01 natural-motion/return scope and retained numerical-search evidence; no replay.')
for tag in ['Z01','Z02','Z03']:
    add(W/f'docs/methods/Z_MOTION/v0.1/packet/reading/{tag}/REPORT.md',f'Z/{tag}.md','N01 observer source/history/accounting scope reading; no trajectories run.')
add(Path(r'C:\TORMENT\TRIOCTAGON_new\trioctagon-physics\docs\RESEARCH_INDEX.md'),'LOCAL_RESEARCH_INDEX.md','Local scientific index used to identify additional relevant titles; historical snapshot.')
assert (R/'sources/dynamics.py').read_bytes()==(P/'inputs/reference/dynamics.py').read_bytes()
assert next(s for s in sources if s['id']=='collective/main.tex')['git_blob_computed_without_git']=='de060bd217261af9bc87a52f0a79fe6fa4f6495d'
scans=[]
pattern=re.compile(r'captur|basin|turning|same.trajectory|1\s*\+\s*i|1\s*[-−]\s*2i|global.*converg',re.I)
for s in sources:
    p=R/s['path']
    if p.suffix in ['.md','.tex']:
        for i,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
            if pattern.search(line):scans.append({'source':s['id'],'line':i,'text':line})
write(R/'logs/PRIOR_SEARCH_HITS.json',{'pattern':pattern.pattern,'sources_searched':len(sources),'hits':scans,'interpretation':'Navigation only; gate requires theorem/hypothesis comparison, not absence of keywords.'})
instructions=[Path(x) for x in [r'C:\AGENTS.md',r'C:\TORMENT\AGENTS.md',r'C:\TORMENT\TRIOCTAGON_new\AGENTS.md',r'C:\TORMENT\TRIOCTAGON_new\research\AGENTS.md',str(R.parent/'AGENTS.md'),str(R/'AGENTS.md')]]
assert not any(p.exists() for p in instructions),'Read applicable instruction before proceeding'
write(R/'SOURCE_IDENTITIES.json',{'task':'NATIVE_TURNING_CAPTURE_01','registered_utc':datetime.now(timezone.utc).isoformat(),'sources':sources,'packet_source_entries':[i for i in manifest['files']],'instruction_scope':{'searched':[str(p) for p in instructions],'present':[],'controlling_order':'packet/NATIVE_TURNING_CAPTURE_01_CODEX_WORK_ORDER.md','historical_instructions':'Evidence only; no publication, code import or suite replay authority.'}})
import mpmath,numpy
write(R/'logs/ENVIRONMENT.json',{'utc':datetime.now(timezone.utc).isoformat(),'python':sys.executable,'python_version':sys.version,'platform':platform.platform(),'conda_environment':os.environ.get('CONDA_DEFAULT_ENV'),'mpmath':mpmath.__version__,'numpy':numpy.__version__,'command_prompt_wrapper':'run_python.cmd','installed_dependencies':False})
write(R/'logs/INPUT_CHECKS.json',{'packet_sha256':expected,'packet_bytes':archive.stat().st_size,'external_checksum_match':True,'manifest_entries_verified':len(manifest['files']),'archive_members_verified':len(names),'standalone_documents_match':True,'primary_blob_match':True,'native_reference_bytes_match':True,'sources_preserved':len(sources),'new_trajectories_executed':False})
print(json.dumps({'sources':len(sources),'search_hits':len(scans),'input_checks':'PASS','new_trajectories':0},indent=2))
