"""File identity, document QA, and review ZIP only. No scientific computations.

--prepare writes the evidence inventory, figure register, preservation and QA.
--package additionally requires the explicit human/model page-inspection record.
"""
from pathlib import Path
import hashlib, json, re, subprocess, sys, zipfile
ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]

def digest(p):
    b = Path(p).read_bytes()
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def readj(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))

def writej(p, data):
    (ROOT / p).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

archives = ['SRG_SIMULATION_STUDY_04_SEED_EXPLORER_REVIEW.zip', 'SIM05_GPT_REVIEW_AND_ADDITIONAL_FINDINGS.zip']
expected = ['1a10bb9c2ad94789efc6d16d7a579a5e60346275ed8c44ac4a386e7799879025', 'ae4fe33903410b211544f8f17cf4b79473b983bf4920c26c4406b27f55d37736']
archive_index = []
for name, sha in zip(archives, expected):
    p = ROOT / 'evidence/inputs' / name
    assert digest(p)['sha256'] == sha
    with zipfile.ZipFile(p) as z:
        assert z.testzip() is None
        members = [{'path': v.filename, 'bytes': v.file_size} for v in z.infolist() if not v.is_dir()]
        archive_index.append({'path': p.relative_to(ROOT).as_posix(), **digest(p), 'members': members})
writej('ARCHIVE_MEMBER_INDEX.json', archive_index)

baseline = readj('INPUT_BASELINE.json') + readj('HANDOFF_BASELINE.json')
checked = []
for row in baseline:
    got = digest(row['original_path'])
    assert all(got[k] == row[k] for k in ('bytes','sha256')), row['original_path']
    cp = row.get('candidate_path')
    if cp:
        assert digest(ROOT / cp) == got, cp
    checked.append({'original_path': row['original_path'], 'candidate_path': cp, **got, 'unchanged': True})
fig_inputs = readj('FIGURE_INPUT_IDENTITIES.json')
for f in fig_inputs:
    assert digest(f['original']) == digest(ROOT / f['path']) == {k:f[k] for k in ('bytes','sha256')}

with zipfile.ZipFile(ROOT / 'evidence/inputs' / archives[1]) as z:
    review_copies = []
    for p in sorted((ROOT/'evidence/reviews/SIM05').glob('*')):
        assert p.is_file()
        b = z.read(p.name)
        assert b == p.read_bytes(), p
        review_copies.append({'candidate':p.relative_to(ROOT).as_posix(),'archive_member':p.name,**digest(p)})
status = subprocess.run(['git','status','--porcelain=v1','--untracked-files=no'],cwd=REPO,capture_output=True,text=True,check=True).stdout
head = subprocess.run(['git','rev-parse','HEAD'],cwd=REPO,capture_output=True,text=True,check=True).stdout.strip()
assert not status, status
assert head == '63469551eb04c17bfbedb6b8fce057c5890cbba8', head
writej('PRESERVATION_RECEIPT.json', {
    'scope':'Inputs actually used and named preservation anchors; not a repository-wide content inventory',
    'protected_input_count':len(checked),'protected_inputs':checked,
    'figure_originals_and_copies_unchanged':len(fig_inputs),'review_copies_verified_against_accepted_archive':review_copies,
    'required_archives':[{k:v for k,v in row.items() if k!='members'} for row in archive_index],
    'repository_head':head,'tracked_and_index_status':status,
    'operations':{'new_simulations':0,'new_rng_draws':0,'scientific_checker_reruns':0,'git_writes':0,'publication':False},
    'write_scope':'Only this new candidate directory. Accepted sources, studies, canonical ledger, Volume I and kernels not edited.'})

figure_info = {
 'F06_SIM04_context.png':(1,'fig:orientation','OBSERVED IN HISTORICAL DATA','SIM04 original coordinates','0,5,10,20','All50; highlighted10,15,27,30,33,47','Fixed equal-aspect world coordinates','A5: source_package/figures/F06_SIM04_context.png'),
 'S4_overview.png':(2,'fig:s4overview','OBSERVED IN HISTORICAL DATA','SIM04 original states/metrics','0–20, motion1–20','All50','Separate original metric axes','A4: figures/F01_recorded_overview.png'),
 'S4_six_review.png':(3,'fig:sixrank','OBSERVED IN HISTORICAL DATA','SIM04 original states; GPT accepted review','diameter5–20; rank20','10,15,27,30,33,47 plus final other44','Log diameter; endpoint sorted R','A5: source_package/context/SIM04_GPT_REVIEW/additional_figure/SIM04_six_point_component.png'),
 'F07_SIM04_scale_and_shape.png':(4,'fig:s4shape','OBSERVED IN HISTORICAL DATA / retained geometry','Accepted SIM04 addendum','3D5,10,20; traces5–20','10,15,27,30,33,47','Centered/Rg, equal aspect, no alignment; original scales and normalized diagnostics below','A5: source_package/figures/F07_SIM04_scale_and_shape.png'),
 'S4_episodes.png':(5,'fig:s4episodes','OBSERVED IN HISTORICAL DATA','SIM04 original states','0–20','3,40,38; pairs38/23/8;5/43; all pairs','Original amplitude and echo scales; log pair-distance panel','A4: figures/F03_identifiable_episodes.png'),
 'F01_SIM05_whole_field.png':(6,'fig:world5','REPRODUCED','Accepted SIM05 captured states','0,20,100,200','All50 stable IDs','Equal-aspect fixed world limits[-5.5,5.5]','A5: source_package/figures/F01_SIM05_whole_field.png'),
 'F05_SIM05_geometry_and_motion.png':(7,'fig:geometry5','REPRODUCED','Accepted SIM05 field geometry and graph tables','0–200; displacement1–200','All50','Original metrics; graph at saved boundary drives next pass','A5: source_package/figures/F05_SIM05_geometry_and_motion.png'),
 'F02_SIM05_selected_groups.png':(8,'fig:groups5','REPRODUCED','Accepted selected-group saved geometry','20,100,200','Final group containing3 (13IDs) and10 (6IDs); exact IDs in AppendixC','Centered/Rg, equal aspect, fixed normalized limits; no alignment;13ID group retrospective at20','A5: source_package/figures/F02_SIM05_selected_groups.png'),
 'F03_SIM05_stages.png':(9,'fig:stages','DERIVED FROM REPRODUCED STATES','Accepted saved stage budget','1–200','All50;150 coordinates','RMS and log axes as labeled; plotted c_p=.08699sin(...), manuscript g_p=.01c_p','A5: source_package/figures/F03_SIM05_stages.png'),
 'F04_SIM05_second_field.png':(10,'fig:second','REPRODUCED','Accepted captured R,D and component records','0–200; scatter200','All50 stable IDs','Heatmap, amplitude/squared-sum scales, endpoint fields','A5: source_package/figures/F04_SIM05_second_field.png')
}
figures=[]
for f in fig_inputs:
    name = Path(f['path']).name
    if name not in figure_info:
        continue
    n,label,cls,data,passes,ids,scaling,origin=figure_info[name]
    archive_id, member = origin.split(': ',1)
    ai = 0 if archive_id=='A4' else 1
    with zipfile.ZipFile(ROOT / 'evidence/inputs' / archives[ai]) as z:
        assert z.read(member)==(ROOT/f['path']).read_bytes(), origin
    figures.append({'figure_number':n,'tex_label':label,'path':f['path'],'bytes':f['bytes'],'sha256':f['sha256'],'archive_locator':origin,'evidence_class':cls,'data_origin':data,'passes':passes,'selection':ids,'scaling_and_timing':scaling,'presentation_changes':'LaTeX page placement and proportional sizing only; no image-byte changes','supported_conclusion':'See exact manuscript caption and linked claim matrix'})
writej('FIGURE_REGISTER.json',{'selected':sorted(figures,key=lambda v:v['figure_number']), 'unused_alternatives':[{'path':f['path'],'sha256':f['sha256'],'reason':'Preserved locally; alternate SIM04 position/term panels omitted to avoid redundant figure plates; available in A4'} for f in fig_inputs if Path(f['path']).name not in figure_info], 'new_scientific_figures':0})

receipts=sorted((ROOT/'qa').glob('BUILD_*_RECEIPT.json'))
receipt=json.loads(receipts[-1].read_text(encoding='utf-8'))
assert receipt['exit_code']==0 and not receipt['warnings']
assert receipt['pdf_sha256']==digest(ROOT/'manuscript.pdf')['sha256']
assert receipt['tex_sha256']==digest(ROOT/'manuscript.tex')['sha256']
writej('FINAL_BUILD_RECEIPT.json',receipt)
tex=(ROOT/'manuscript.tex').read_text(encoding='utf-8')
bib=(ROOT/'references.tex').read_text(encoding='utf-8')
labels=re.findall(r'\\label\{([^}]+)\}',tex)
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
# Labels in the plate macro are expanded arguments; include the ten fixed labels.
defined=set(labels)|{row['tex_label'] for row in figures}
assert not(set(refs)-defined),set(refs)-defined
cites={c.strip() for group in re.findall(r'\\cite\{([^}]+)\}',tex) for c in group.split(',')}
keys=set(re.findall(r'\\bibitem\{([^}]+)\}',bib))
assert cites<=keys,(cites-keys)
assert tex.count('\\begin{proposition}')==4
assert len(figures)==10
links=[]
for source,content in [('manuscript.tex',tex),('references.tex',bib)]:
    for target in re.findall(r'\\href\{([^}]+)\}',content):
        assert (ROOT/target).exists(),(source,target)
        links.append({'from':source,'target':target})
for p in sorted(ROOT.glob('*.md')):
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        target=target.split('#')[0]
        if target and '://' not in target:
            # Documents refer to records written at package finalization.
            if target in ('PAGE_INSPECTION.json','REVIEW_ZIP_IDENTITY.json','DOCUMENT_QA.json'):
                continue
            assert (ROOT/target).exists(),(p.name,target)
            links.append({'from':p.name,'target':target})
writej('DOCUMENT_QA.json',{'scope':'Document integrity and links only; scientific claims manually transcribed/read back, no result recomputation',
 'pdf_sha256':digest(ROOT/'manuscript.pdf')['sha256'],'pages':receipt['pages'],'tex_sha256':receipt['tex_sha256'],'build_warnings':receipt['warnings'],
 'propositions':4,'figure_plates':10,'bibliography_entries':len(keys),'cited_keys':sorted(cites),'unresolved_tex_references':[],
 'relative_links_checked':links,'all_pdf_fonts_embedded':all(receipt['embedded_fonts'].values()),
 'scientific_runs':0,'rng_draws':0,'preservation_checks_passed':True})

if '--package' not in sys.argv:
    print(json.dumps({'prepared':True,'protected_inputs':len(checked),'figures':len(figures),'pages':receipt['pages'],'archive_prefixes':[[x['path'],sorted({r['path'].split('/')[0] for r in x['members']})] for x in archive_index]}))
    raise SystemExit(0)

inspection=readj('PAGE_INSPECTION.json')
assert inspection['pdf_sha256']==digest(ROOT/'manuscript.pdf')['sha256']
assert len(inspection['pages'])==receipt['pages']
assert all(r['status']=='PASS' for r in inspection['pages'])
root_names=['manuscript.pdf','manuscript.tex','references.tex','START_HERE.md','CLAIM_EVIDENCE_MATRIX.md','FIGURE_REGISTER.json','EDITORIAL_AND_VERIFICATION_NOTES.md','EVIDENCE_INDEX.md','BUILD_INSTRUCTIONS.md','INPUT_BASELINE.json','HANDOFF_BASELINE.json','INPUT_GATE.json','HANDOFF_GATE.json','FIGURE_INPUT_IDENTITIES.json','ARCHIVE_MEMBER_INDEX.json','PRESERVATION_RECEIPT.json','FINAL_BUILD_RECEIPT.json','DOCUMENT_QA.json','PAGE_INSPECTION.json','build_document.py','finalize_package.py','prepare_manuscript.py','receive_review.py']
paths=[ROOT/p for p in root_names]+[ROOT/f['path'] for f in figures]
excluded='evidence/inputs/SRG_SIMULATION_STUDY_05_INFINITY_REVIEW.zip'
paths += [p for p in (ROOT/'evidence').rglob('*') if p.is_file() and p.relative_to(ROOT).as_posix()!=excluded]
paths=sorted(set(paths),key=lambda p:p.relative_to(ROOT).as_posix())
rows=[{'path':p.relative_to(ROOT).as_posix(),**digest(p)} for p in paths]
manifest={'candidate':'SRG Volume II SIM04/SIM05 v0.1 for GPT and Hilmir review','scope':'Exact delivered review payload; excludes itself and external ZIP identity to avoid circular hashes','payload_file_count':len(rows),'files':rows,'excluded_working_material':['cache/','tmp/','build/','renders/','qa/','fontconfig.xml','CACHE_RECEIPT.json',excluded,'unused figure alternatives','outer handoff wrapper'],'note':'Required immutable archives contain their own unchanged manifests and original accepted methods.'}
writej('MANIFEST.json',manifest)
zip_path=ROOT/'SRG_VOLUME_II_SIM04_SIM05_CANDIDATE_v0.1_REVIEW.zip'
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in paths+[ROOT/'MANIFEST.json']:
        info=zipfile.ZipInfo(p.relative_to(ROOT).as_posix(),date_time=(2026,10,23,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(info,p.read_bytes())
with zipfile.ZipFile(zip_path) as z:
    assert z.testzip() is None
    assert set(z.namelist())=={r['path'] for r in rows}|{'MANIFEST.json'}
    for row in rows:
        b=z.read(row['path'])
        assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'],row['path']
writej('REVIEW_ZIP_IDENTITY.json',{'path':zip_path.name,**digest(zip_path),'total_files':len(rows)+1,'manifest_sha256':digest(ROOT/'MANIFEST.json')['sha256'],'pdf_sha256':digest(ROOT/'manuscript.pdf')['sha256'],'crc_and_all_payload_bytes_read_back':True,'identity_is_external_to_zip':True})
print(json.dumps(readj('REVIEW_ZIP_IDENTITY.json')))
