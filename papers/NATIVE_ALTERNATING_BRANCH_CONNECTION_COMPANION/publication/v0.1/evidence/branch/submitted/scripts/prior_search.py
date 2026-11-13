from common import *
pattern=r'M2.{0,90}M3|M3.{0,90}M2|continu.{0,80}(flip|onset|branch|1/200|0\.005)|near.onset|sufficiently small|implicit.function|U_\+|U_plus'
roots=[P/'inputs',REPO/'papers/PAPER_G',REPO/'papers/COHERENCE_RETURNS',REPO/'papers/NATURAL_CORE_MOTION']
research=R.parents[1]
roots += [p for p in research.iterdir() if p.is_dir() and p.name.startswith('NATURAL_CORE_MOTION') and 'PUBLICATION' not in p.name and 'DOCUMENTATION' not in p.name]
roots=[p for p in roots if p.exists()]
records=[]
for i,root in enumerate(roots):
    cmd=['rg','-n','-i','--max-count','6','-g','*.md','-g','*.tex','-g','!**/publication_worktree/**','-g','!**/source_context/**',pattern,str(root)]
    result=run(cmd,'prior_search_'+str(i),check=False)
    assert result.returncode in [0,1]
    lines=result.stdout.decode('utf-8',errors='replace').splitlines()
    records.append({'root':str(root),'hit_lines':len(lines),'log':'logs/prior_search_'+str(i)+'.stdout','command':cmd})
    print(str(root),len(lines))
    for line in lines:
        if any(s in line.lower() for s in ['not been established','not establish','not a continuation','unproved','local persistence','branch connection','same branch']):print(line[:700])
write(L/'PRIOR_SEARCH_RECORDS.json',{'observed_utc':now(),'bounded_search':True,'not_exhaustive_novelty_claim':True,'records':records})
