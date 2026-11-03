"""Focused read/copy/hash provenance only. No Git operations or model imports."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, importlib.util, json, sys

W=Path(__file__).resolve().parent
E=W.parent/'NATIVE_RECIPROCAL_EXCHANGE_PAPER_PUBLISH_01/publication_worktree/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1'
ORDER=Path('C:/Users/Notandi/Downloads/NATIVE_SAME_TRAJECTORY_RETURN_01_CODEX_WORK_ORDER.md')
START=Path('C:/Users/Notandi/Downloads/START_HERE(20261103-055023).md')
REF='273b1a6faaab19ea58748d00576439166eeef9ab'
expected={
 'manuscript/candidate.tex':'babb811ccf53415dc77c19c3f00c7a281924713728d6816f9478f2522e2c43e5',
 'manuscript/power.tex':'2d302fb32d0a5e825ae4929e7cc1e7aceb4772937cc5457bed951e717a2cfc89',
 'manuscript/wellposed.tex':'0cb9c047931c4b2c8484012ade0799417bee4168e5d6fc8de3a1b9e951636895',
 'manuscript/activity.tex':'da5a775458e50475d37a280770302fe46742efa88f4a0c8db8dacf97adcc5054',
 'manuscript/capacity.tex':'b5a67749c6b1f4a313ef34e7e82d6a7b28e0fd770c43dded6692655d9f0749be',
 'manuscript/interpretation.tex':'c55dd6c7179483d8720f13d72ccc363802a39cdbe6d0258043854c69c7af939c',
 'evidence/accepted_proof.md':'ea3e40a0bd3de11308771a9cd83600912b449534808a1d540bb489b45d7edb86',
}
def identity(p):
    b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def dump(name,value):(W/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
assert not (W/'SOURCE_IDENTITIES.json').exists(),'Do not overwrite the initial source snapshot'
instructions=set()
for target in [W,ORDER,START,*[E/p for p in expected]]:
    parent=target if target.is_dir() else target.parent
    for ancestor in [parent,*parent.parents]:instructions.add(ancestor/'AGENTS.md')
found=[str(p) for p in sorted(instructions) if p.is_file()]
dump('AGENTS_CHECK.json',{'checked':[str(p) for p in sorted(instructions)],'found':found})
assert not found,'Read applicable instructions before proceeding: '+repr(found)
sources=[]
for rel,digest in expected.items():
    source=E/rel;ident=identity(source);assert ident['sha256']==digest,rel
    target=W/'sources'/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(source.read_bytes())
    assert identity(target)==ident
    sources.append({'id':Path(rel).stem.upper(),'path':str(source),'retained_as':'sources/'+rel,
        'edition_path':rel,'commit':REF,'immutable_url':'https://github.com/pzychozen/trioctagon-physics/blob/'+REF+'/papers/RECIPROCAL_CHIRAL_EXCHANGE/publication/v0.1/'+rel,
        **ident,'identity_basis':'Local complete file matches SHA-256 explicitly supplied in section 8 of the new order; no new Git/network operation.',
        'reading_scope':'Complete manuscript section' if rel.startswith('manuscript/') else 'Focused defining proof S1-S4, A1-A16 and B1-B4 (file lines 1-325); full original retained.'})
(W/'SUPPLIED_WORK_ORDER.md').write_bytes(ORDER.read_bytes())
(W/'START_HERE_CONTEXT.md').write_bytes(START.read_bytes())
review_candidates=[{'name':p.name,**identity(p)} for p in ORDER.parent.iterdir() if p.is_file() and ('SAME_TRAJECTORY' in p.name.upper() or p.name.upper().startswith('START_HERE'))]
context={'order':{'path':str(ORDER),'retained_as':'SUPPLIED_WORK_ORDER.md',**identity(ORDER)},
         'start_here':{'path':str(START),'retained_as':'START_HERE_CONTEXT.md',**identity(START)}}
dump('SOURCE_IDENTITIES.json',{'recorded_utc':datetime.now(timezone.utc).isoformat(),'publication_commit':REF,
    'sources':sources,'context':context,'narrow_downloads_candidates':review_candidates,
    'handoff_availability':'Named complete handoff ZIP and its separate review documents not found in the focused top-level Downloads search. Standalone START_HERE context was available. Its report of a later GPT final-page review is attributed to that document; this investigation did not inspect that review. The seven hash-pinned defining files were all available locally.',
    'scope':'Seven defining publication files and the two received context/order files only; not a repository-wide preservation audit. No Git, network retrieval or model import performed.'})
modules={name:bool(importlib.util.find_spec(name)) for name in ['sympy']}
dump('ENVIRONMENT.json',{'utc':datetime.now(timezone.utc).isoformat(),'python':sys.executable,'version':sys.version,
    'invocation':'Windows Command Prompt: call conda activate torment; python -I -B prepare_sources.py',
    'modules':modules,'installations':[],'git_operations':False})
print(json.dumps({'sources_matched':len(sources),'context_files':len(context),'applicable_agents':found,'modules':modules}))
