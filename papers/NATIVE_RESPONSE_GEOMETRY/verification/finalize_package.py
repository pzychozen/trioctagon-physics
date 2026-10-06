"""Validate final records; write a proposed allowlist and package hash manifest.

Does not stage, commit, push or modify any file outside this publication lane.
"""
from pathlib import Path
import json,hashlib,re
L=Path(__file__).resolve().parents[1]
R=L.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((L/p).read_text(encoding='utf8'))
local=read('verification/paper_local_results.json')
build=read('publication/build_record.json');qa=read('publication/pdf_qa_results.json')
pres=read('provenance/preservation.json');audit=read('provenance/word_occurrence_audit.json')
assert local['passed'] and local['paper_local_predicate_count']==61
assert pres['protected_checkout_unchanged'] and not pres['changed_checkpoints']
assert qa['all_pages_rendered'] and qa['automated_checks_passed'] and qa['page_count']>0
assert sha(L/build['pdf'])==build['pdf_sha256']==qa['pdf_sha256']
for path,h in build['inputs'].items():assert sha(L/path)==h,path
for path,h in local['inputs_sha256'].items():assert sha(L/path)==h,path
for name,h in audit['manuscript_sha256'].items():assert sha(L/'manuscript'/name)==h,name
log=(L/'publication/main.log').read_text(encoding='utf8',errors='replace')
assert not re.search(r'Overfull|Missing character|undefined|LaTeX Warning|^!',log,re.M)
allow=L/'provenance/COMMIT_ALLOWLIST.txt';manifest=L/'provenance/package_manifest.json'
paths=sorted({p for p in L.rglob('*') if p.is_file() and 'tmp' not in p.relative_to(L).parts and '__pycache__' not in p.parts}|{allow,manifest},key=lambda p:p.as_posix())
assert all(p.is_relative_to(L) for p in paths)
allow.write_text('\n'.join(p.relative_to(R).as_posix() for p in paths)+'\n',encoding='utf8')
data={'status':'PROPOSED ONLY - nothing staged or published','source_head':pres['after']['head'],'relative_to':'papers/NATIVE_RESPONSE_GEOMETRY','intended_file_count':len(paths),'excluded':'tmp/ scratch render directory and Python bytecode','manifest_self_hash_omitted':True,'files':[{'path':p.relative_to(L).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths if p!=manifest]}
manifest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
for md in [L/'README.md',L/'PUBLICATION_PROPOSAL.md']:
    for target in re.findall(r'\]\(([^)]+)\)',md.read_text(encoding='utf8')):
        assert (md.parent/target).exists(),target
print('Final records consistent;',len(paths),'proposed files; no Git write performed.')
