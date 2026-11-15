from audit import *
import re
CHECKPOINT='ae2c02c80c49dfcf266d3b27ebd21be76a938de1'
selected={
'current_catalog':'README.md',
'turning':'papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex',
'alternating':'papers/NATIVE_ALTERNATING_BRANCH_CONNECTION_COMPANION/publication/v0.1/main.tex',
'capture':'papers/NATIVE_TURNING_CAPTURE_COMPANION/publication/v0.1/main.tex',
'potential_minimum':'papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/minimum.tex',
'potential_coordinates':'papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/coordinates.tex',
'potential_setting':'papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/setting.tex',
}
base=OUT/'sources/later';base.mkdir(parents=True,exist_ok=True)
rows=[]
idx=REPO/'docs/RESEARCH_INDEX.md';b=idx.read_bytes();dst=base/'current_index.md';dst.write_bytes(b)
rows.append({'id':'current_index','origin':'local_file','original_path':str(idx),'delivered_path':dst.relative_to(OUT).as_posix(),'bytes':len(b),'sha256':sha(b)})
for name,path in selected.items():
    b=git('show',CHECKPOINT+':'+path)
    p=base/(name+Path(path).suffix);p.write_bytes(b)
    rows.append({'id':name,'origin':'local_git_object','checkpoint':CHECKPOINT,'repository_path':path,'delivered_path':p.relative_to(OUT).as_posix(),'bytes':len(b),'sha256':sha(b)})
for name in ['GRAVITY_OPEN_QUESTIONS.md','GRAVITY_NEXT_INVESTIGATION.md','GRAVITY_ESTABLISHED_RESULTS.md']:
    p=Path(r'C:\TORMENT\TRIOCTAGON_new\research\GRAVITY_NATIVE_RECOVERY_01')/name
    b=p.read_bytes(); dst=base/name;dst.write_bytes(b)
    rows.append({'id':name,'origin':'local_file','original_path':str(p),'delivered_path':dst.relative_to(OUT).as_posix(),'bytes':len(b),'sha256':sha(b)})
# Broad bounded local source search. No remote/global novelty claim.
patterns=[r'cycle.{0,100}\b(drift|rate)\b',r'\b(drift|rate)\b.{0,100}cycle',r'response circulation versus trajectory drift',r'112500|28125|1612500',r'matched.{0,35}(parameter|famil)',r'\\nu.{0,50}\\mathcal\s*\{?C']
scopes=[REPO/'papers',Path(r'C:\TORMENT\TRIOCTAGON_new\research')]
searches=[]
for i,pattern in enumerate(patterns):
    cmd=['rg','-n','-i','--glob','*.md','--glob','*.tex','--glob','!**/remote/**','--glob','!**/fresh_remote*/**','--glob','!**/node_modules/**',pattern,*map(str,scopes)]
    p=subprocess.run(cmd,capture_output=True)
    assert p.returncode in (0,1),(cmd,p.stderr)
    (ROOT/'private'/f'gate_search_{i}.txt').write_bytes(p.stdout)
    # Preserve only relevant paths/text in compact matches; bulk duplicates remain private.
    lines=p.stdout.decode('utf-8',errors='replace').splitlines()
    unique=[];seen=set()
    for ln in lines:
        content=re.split(r':\d+:',ln,maxsplit=1)[-1]
        locator=re.split(r':\d+:',ln,maxsplit=1)[0].replace('\\','/')
        locator=locator.rsplit('/papers/',1)[-1] if '/papers/' in locator else locator
        relevant=re.search(r'GRAVITY_NATIVE_RECOVERY|D0_|D1_|CHIRAL_DRIFT|NATIVE_RESPONSE_GEOMETRY|NATIVE_POTENTIAL_AND_CLOSED|PHASE_RECONSTRUCTION|COLLECTIVE_TURNING|COHERENCE_RETURNS|NCM_DUAL|NATIVE_AB_|NATIVE_ALTERNATING|NATIVE_TURNING_CAPTURE',locator,re.I)
        if relevant and content not in seen: seen.add(content); unique.append(ln)
    (OUT/'records'/f'SOURCE_SEARCH_{i}.txt').write_text('\n'.join(unique)+'\n',encoding='utf-8')
    searches.append({'argv':cmd,'returncode':p.returncode,'raw_lines':len(lines),'unique_text_lines':len(unique),'raw_output_sha256':sha(p.stdout),'deduplicated_output':f'records/SOURCE_SEARCH_{i}.txt','stderr':p.stderr.decode()})
write(OUT/'records/LATER_SOURCE_INVENTORY.json',rows)
write(OUT/'records/SEARCH_LOG.json',searches)
print('Recovered',len(rows),'later/navigation sources; search counts:',[(s['raw_lines'],s['unique_text_lines']) for s in searches])
