from common import *
extras=[
'README.md',
'papers/PAPER_C/publication/v1.0.1/README.md',
'papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md',
'research/spherical_edge_extensions/README.md',
'research/spherical_edge_extensions/accepted/boundary10/BOUNDARY10_REPORT.tex',
'research/spherical_edge_extensions/reviews/boundary11/BOUNDARY11_GPT_SCIENTIFIC_REVIEW.md',
'papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/README.md',
'papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/GEO_ORIGINS01_v0.2.tex',
'papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/retained_mathematics.tex',
'papers/GEOMETRIC_ORIGINS_AND_NORMALIZATION/publication/v0.2/ACCESS_AND_EVIDENCE_MAP.md',
'apps/scientific_ui/publication/shell_observer/v0.1/README.md',
'apps/scientific_ui/src/trioctagon_ui/shell_observer.py',
'apps/scientific_ui/src/trioctagon_ui/geometry_view.py',
]
records=[]
for n,path in enumerate(extras,11):
    b=git(['show',CHECKPOINT+':'+path],'additional_source_'+str(n)).stdout
    p=S/path;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
    working=(REPO/path).read_bytes()
    records.append({'id':'S'+str(n),'path':path,'bytes':len(b),'sha256':sha(b),'git_blob_sha1':blob(b),'mode':'read_only_git_show','reading_commit':CHECKPOINT,'working_sha256':sha(working),'working_git_blob_sha1':blob(working),'working_matches_pinned_bytes':working==b})
src=R.parents[1]/'TSZ01_shell_distance_zeta_20261017/attempt_001/TSZ01_FINDINGS_AND_NEXT_QUESTIONS.md'
assert src.exists(),src
p=S/'external/TSZ01_FINDINGS_AND_NEXT_QUESTIONS.md';p.parent.mkdir(exist_ok=True);b=src.read_bytes();p.write_bytes(b)
records.append({'id':'S24','path':p.relative_to(S).as_posix(),'original_path':str(src),'bytes':len(b),'sha256':sha(b),'git_blob_sha1':None,'mode':'unchanged_local_context_copy','review_status':'Historical submission context; not promoted into new acceptance.'})
write(S/'ADDITIONAL_SOURCE_IDENTITIES.json',{'sources':records,'science_executed':False})
listing=git(['ls-tree','-r','--name-only',CHECKPOINT],'checkpoint_tree_paths').stdout.decode()
terms=['outer','envelope','spherical','geometric_origins','shell_observer','boundary','tsz']
related=[p for p in listing.splitlines() if any(t in p.lower() for t in terms) and p.endswith(('.md','.tex','.py','.json')) and not any(t in p.lower() for t in ['draft_v','cache/','figures/','evidence/','data/','verification/'])]
write(D/'PRIOR_WORK_NAVIGATION.json',{'reading_checkpoint':CHECKPOINT,'targeted_source_paths':related,'root_navigation':'sources/README.md','interpretation':'Search narrows the project-source comparison; novelty depends on the inspected definitions and theorem scope, not absent text hits.'})
q=run(['rg','-n','-i',r'convex hull|generic|maximal face|transition|coplanar|t/h\s*=\s*3|3h|envelope',S/'papers',S/'research',S/'apps','--glob','*.md','--glob','*.tex','--glob','*.py'],'prior_work_terms',check=False)
assert q.returncode in [0,1]
print('Collected',len(records),'additional/context sources; targeted index paths',len(related))
for name in ['geometry_inventory.json','hull_A.json','hull_B.json']:
    p=next(S.rglob(name));x=read(p);print(name,list(x))
    for k,v in x.items():
        if isinstance(v,list):print(k,len(v),'FIRST',v[:1])
