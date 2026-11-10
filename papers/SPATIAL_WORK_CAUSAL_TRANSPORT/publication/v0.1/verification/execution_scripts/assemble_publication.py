"""Assemble only the authorized paper, evidence and catalog entry. No scientific rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, re, shutil, subprocess
R=Path(__file__).resolve().parents[1]; P=R/'packet'; V=R/'verification'; W=R.parents[1]/'wt-swct-pub01'
prefix='papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1'
E=W/prefix; C=R/'candidate/v0.1'; pdf='SPATIAL_WORK_CAUSAL_TRANSPORT_v0.1.pdf'
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,obj): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def copy(a,b): b.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(a,b)
def git(*args): return subprocess.check_output(['git','-c','core.longpaths=true',*args],cwd=W)
assert git('status','--porcelain=v1','-uno') in [b'',b' M README.md\n']
doc=json.loads((V/'DOCUMENT_CHECKS.json').read_text(encoding='utf-8'))
assert doc['pdf_sha256']==sha(C/pdf) and doc['pages']==25
notes=[
'Title, full accented author, date, authorization status and revised abstract readable; credit note intact.',
'Contents and reading guide fit; all section/page entries visible.',
'Introduction paragraphs and citation text readable; footer clear.',
'Status table, geometry definitions and clearance equations fit within margins.',
'Proposition 2.1 and corrected adjacent-unit-direction proof readable; ball/cylindrical radius distinction visible.',
'Retained exchange and C6 equations readable with resolved citations.',
'History estimate and point-evaluation counterexample fit; no missing mathematical glyphs.',
'Temporal-adjoint formula, support proof and qualification readable.',
'History witness and regional-work equations fit; section transition clear.',
'Signed-prehistory box and spatial-factorization definitions readable.',
'Gram/kernel statement, characteristics and stock/trace formulas readable.',
'Trace proof and boxed closed-model equations intact, without overlap.',
'Figure 1 arrows, labels, powers and caption readable; abstract channel semantics explicit.',
'Global mild-evolution theorem and construction proof fit; equation numbers visible.',
'Continuation, conservation and dependence proof readable through receiving-reversibility remark.',
'Loaded C6 and compatible-history boxes readable; native tuple visible.',
'Native-step account and D01 statement complete; zero-coupling qualifications readable.',
'Latency and carrier-preload receiving propositions legible; equations clear.',
'Strict receiving and incoming-return proof inequalities fit without clipping.',
'Figure 2 time supports, open endpoints, labels and caption readable; schematic meaning explicit.',
'Physical-correspondence limits, Q01 and approved open-question closing wording intact.',
'Notation crosswalk and declared dimensional assignment readable; all rows fit.',
'Signed-prehistory illustration and first coverage-table segment clear; continued table intentional.',
'Repeated coverage header and remaining claims including D01 visible; reproducibility prose readable.',
'All twelve references, immutable links and preserved-source paths readable.'
]
assert len(notes)==25
visual={'task':R.name,'inspected_utc':datetime.now(timezone.utc).isoformat(),'pdf_sha256':sha(C/pdf),'pages':25,
 'method':'All 25 individual 125-dpi Poppler PNGs opened with view_image and visually inspected by Codex; not inferred from rendering or prior inspections.',
 'disposition':'PASS','defects':[], 'checks':['readable text/equations/figures','no clipping/overlap/missing glyphs','headers/footers/page numbers','tables/captions/reference layout'],
 'page_inspections':[{'page':i,'render_path':f'verification/pages/page-{i:02}.png','render_sha256':sha(V/f'pages/page-{i:02}.png'),'result':'PASS','note':n} for i,n in enumerate(notes,1)]}
write(V/'VISUAL_INSPECTION.json',visual)
assert not git('ls-tree','HEAD','papers/SPATIAL_WORK_CAUSAL_TRANSPORT'), 'Do not overwrite an existing tracked paper'
shutil.copytree(C,E,dirs_exist_ok=True)
shutil.copytree(P/'inputs',E/'inputs',dirs_exist_ok=True)
shutil.copytree(R/'review_basis_extracted/provenance',E/'provenance/historical_submission',dirs_exist_ok=True)
copy(R/'review_basis_extracted/provenance/historical/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_CODEX_WORK_ORDER.md',E/'provenance/historical/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_CODEX_WORK_ORDER.md')
for name in ['GPT_ACCEPTANCE.json','GPT_MANUSCRIPT_REVIEW.md','CORRECTIONS.json','CORRECTIONS.diff','CLAIM_SOURCE_LEDGER_GPT_CORRECTED.json','CODEX_FIX_AND_PUBLISH_WORK_ORDER.md','PACKET_MANIFEST.json']:
    copy(P/name,E/'review'/name)
copy(P/'corrected_edition/v0.1'/pdf,E/'review/SPATIAL_WORK_CAUSAL_TRANSPORT_v0.1_GPT_REVIEWED.pdf')
for p in (P/'verification').rglob('*'):
    if p.is_file() and p.suffix.lower() in ['.json','.txt','.log','.aux','.toc']:
        copy(p,E/'review/verification'/p.relative_to(P/'verification'))
copy(P/'NOTATION_CROSSWALK.md',E/'NOTATION_CROSSWALK.md')
copy(R/'review_basis_extracted/CLAIM_SOURCE_LEDGER.json',E/'review/historical_submission/CLAIM_SOURCE_LEDGER.json')
for name in ['ENVIRONMENT.json','INPUT_IDENTITIES.json','DOCUMENT_CHECKS.json','VISUAL_INSPECTION.json','BUILD_EXECUTION.json','BUILD_EXECUTION.txt','AUDIT_EXECUTION.txt','EXTRACTED_TEXT.txt','EXTRACTED_LAYOUT.txt','PDFINFO.txt','RENDER_LOG.txt']:
    copy(V/name,E/'verification'/name)
for name in ['BUILD_RECEIPT.json','compiler.txt','main.aux','main.toc','main.log']:
    copy(V/'publication_build01'/name,E/'verification/publication_build01'/name)
for name in ['prepare.py','build_and_audit.py','audit_document.py','assemble_publication.py']:
    copy(R/'scripts'/name,E/'verification/execution_scripts'/name)
ledger=json.loads((P/'CLAIM_SOURCE_LEDGER_GPT_CORRECTED.json').read_text(encoding='utf-8'))
ledger.update(task=R.name,pdf_sha256=sha(E/pdf),status='Research edition v0.1 — project-internal review complete; author-authorized for repository publication.',
 path_base='Repository root; all active paths are repository-relative.',build_kind='Final Windows Tectonic 0.17.0 build in conda torment; no scientific-suite replay.',
 notation_crosswalk=prefix+'/NOTATION_CROSSWALK.md',source_identities=prefix+'/inputs/SOURCE_IDENTITIES.json',
 incoming_ledger=prefix+'/review/CLAIM_SOURCE_LEDGER_GPT_CORRECTED.json',generated_utc=datetime.now(timezone.utc).isoformat(),
 span_convention='Inclusive 1-based lines; span SHA-256 uses UTF-8 joined LF lines and one trailing LF. Manuscript spans cover the containing TeX environment, or the label line.')
counts={'manuscript':0,'retained':0,'proofs':0,'acceptances':0}
def verify_source(loc):
    f=E/loc['path']; assert f.is_file(),f
    assert sha(f)==loc['sha256'],f
    lines=f.read_text(encoding='utf-8').splitlines()
    if 'line' in loc: assert lines[loc['line']-1]==loc['line_text'],loc
    if 'start_line' in loc:
        span=('\n'.join(lines[loc['start_line']-1:loc['end_line']])+'\n').encode()
        assert hashlib.sha256(span).hexdigest()==loc['span_sha256'],loc
    loc['path']=prefix+'/'+loc['path']
for claim in ledger['claims']:
    for loc in claim['manuscript_locations']:
        rel=loc['path'].removeprefix('corrected_edition/v0.1/')
        f=E/rel; txt=f.read_text(encoding='utf-8'); lines=txt.splitlines()
        found=[i for i,l in enumerate(lines,1) if '\\label{'+loc['label']+'}' in l]
        assert len(found)==1,(loc['label'],found)
        line=found[0]; pos=txt.index('\\label{'+loc['label']+'}')
        stack=[]; containers=[]
        for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',txt):
            if m[1]=='begin': stack.append((m[2],m.start()))
            else:
                assert stack and stack[-1][0]==m[2],(f,m[0])
                env,start=stack.pop()
                if start<=pos<m.end(): containers.append((start,m.end(),env))
        if containers:
            start,end,env=max(containers,key=lambda x:x[0]); lo=txt[:start].count('\n')+1; hi=txt[:end].count('\n')+1
        else: lo=hi=line; env='label-line'
        loc.update(path=prefix+'/'+rel,line=line,line_text=lines[line-1],sha256=sha(f),**doc['labels'][loc['label']],start_line=lo,end_line=hi,span_kind=env,
          span_sha256=hashlib.sha256(('\n'.join(lines[lo-1:hi])+'\n').encode()).hexdigest())
        counts['manuscript']+=1
    verify_source(claim['controlling_proof']); counts['proofs']+=1
    for loc in claim['current_acceptance']: verify_source(loc); counts['acceptances']+=1
    for loc in claim['retained_equation_source_locations']: verify_source(loc); counts['retained']+=1
assert counts['manuscript']==99 and counts['retained']==107 and len(ledger['claims'])==13,counts
write(E/'CLAIM_SOURCE_LEDGER.json',ledger)
identities=[]
for p in sorted((P/'inputs').rglob('*')):
    if p.is_file():
        q=E/'inputs'/p.relative_to(P/'inputs'); assert p.read_bytes()==q.read_bytes()
        identities.append({'path':q.relative_to(E).as_posix(),'sha256':sha(q),'bytes':q.stat().st_size})
approved=[]
for p in sorted((P/'corrected_edition/v0.1').rglob('*')):
    if p.is_file() and p.name not in [pdf,'README.md','BUILD.md']:
        q=E/p.relative_to(P/'corrected_edition/v0.1'); assert p.read_bytes()==q.read_bytes()
        approved.append({'path':q.relative_to(E).as_posix(),'sha256':sha(q)})
payload_check={'checked_utc':datetime.now(timezone.utc).isoformat(),'pdf_sha256':sha(E/pdf),'counts':counts,'claim_ids':[x['id'] for x in ledger['claims']],'approved_edition_files_unchanged':approved,'unchanged_input_files':identities,'status':'PASS','scientific_suites_rerun':False}
access='''# Publication access map

All paths below are relative to this edition, unless stated otherwise. The current claim ledger uses repository-root-relative paths and binds the final Windows PDF.

| Material | Published location |
|---|---|
| Complete editable manuscript and canonical PDF | `main.tex`, `sections/`, `references.tex`, `figures/`, `build.py`, `SPATIAL_WORK_CAUSAL_TRANSPORT_v0.1.pdf` |
| Readable accepted W/T proofs and decisions | `inputs/accepted/spatial_work/`, `inputs/accepted/causal_transport/` |
| Complete unchanged W/T acceptance archives | `inputs/evidence/spatial_work/`, `inputs/evidence/causal_transport/` |
| Sources printed as `sources/CC/...` and `sources/RX/...` in the bibliography | `inputs/sources/CC/...`, `inputs/sources/RX/...` respectively; the printed names are relative to the retained input root |
| Other retained foundations | `inputs/accepted/`, `inputs/sources/`, `inputs/SOURCE_IDENTITIES.json`, `inputs/SOURCE_MAP.md` |
| Recovered historical order for the D01 context | `provenance/historical/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_CODEX_WORK_ORDER.md` |
| Current coverage and notation | `CLAIM_SOURCE_LEDGER.json`, `NOTATION_CROSSWALK.md` |
| GPT manuscript acceptance, exact edits and reference PDF | `review/`; its unchanged paths are relative to the incoming packet, not this edition |
| Current Windows build and document/visual checks | `verification/`, including `publication_build01/` |
| Original submission provenance and ledger | `provenance/historical_submission/`, `review/historical_submission/` |

The incoming packet, complete original manuscript submission ZIP, individual final-page PNGs, fresh remote downloads and post-push publication receipt are retained in the local publication closeout ZIP supplied to the author. Their identities are recorded here. These bulky archival items are not required to read the public W/T proofs, preserved equations or acceptance archives. The page inspection records bind every PNG to the final PDF. The earlier reviewer render records certify only their stated Linux reviewer PDF.

`BUILD.md` documents an explicitly local existing Tectonic path and a portable `--tectonic` override. Absolute paths in execution receipts record where those commands actually ran; historical evidence retains its original paths and status. The document-verification scripts are retained execution evidence, not commands to run the historical work orders. Reproduction of the manuscript itself uses the edition's `build.py` and an existing populated TeX cache.

All 84 original input members are unchanged. Historical orders and pending-review wording in those records remain historical. Current authority is the supplied fix-and-publish order and the author's explicit approval. No external peer review or machine proof certification is claimed. Existing repository rights and licensing scope remain unchanged; public visibility does not grant a new manuscript license.
'''
(E/'ACCESS_MAP.md').write_text(access,encoding='utf-8')
with (E/'README.md').open('a',encoding='utf-8',newline='\n') as f:
    f.write('\nCurrent publication materials: [access map](ACCESS_MAP.md), [claim/source ledger](CLAIM_SOURCE_LEDGER.json), [notation crosswalk](NOTATION_CROSSWALK.md), [publication disposition](PUBLICATION_DISPOSITION.md), [manifest](PUBLICATION_MANIFEST.json), and [Windows document checks](verification/DOCUMENT_CHECKS.json). The exact GPT-reviewed reference PDF and acceptance remain under `review/`. Final-page renders and the post-push receipt are supplied in the local closeout archive.\n')
with (E/'BUILD.md').open('a',encoding='utf-8',newline='\n') as f:
    f.write('\nThe final publication build is now recorded in `verification/publication_build01/`; `verification/BUILD_EXECUTION.json` records the actual Windows command and successful exit. `verification/DOCUMENT_CHECKS.json` and `verification/VISUAL_INSPECTION.json` certify the final 25-page PDF. See `ACCESS_MAP.md` for the public evidence layout and local closeout contents. The historical build08 and Linux reviewer build are distinct retained evidence.\n')
(E/'PUBLICATION_DISPOSITION.md').write_text(f'''# Publication disposition

Research edition v0.1 — project-internal review complete; author-authorized for repository publication.

The author approved the one-pass fix-and-publish order. All 16 approved M01–M03 replacements in seven files were independently matched to the supplied corrected edition. All 79 displayed math environments and two additional bracket displays are unchanged from the submitted manuscript. Figures and all 84 input members remain unchanged. The final TeX, bibliography, figure assets and build helper are byte-identical to the accepted corrected sources. Only README/BUILD access guidance is appended for this publication layout; no scientific change is made.

The faithful Windows Tectonic 0.17.0 build ran under Command Prompt with conda `torment`, using cached/untrusted mode and external intermediates. Its PDF is {doc['pdf_bytes']:,} bytes, 25 pages, SHA-256 `{sha(E/pdf)}`. All 118 labels and 12 citations resolve; all 20 fonts are embedded; no compiler warnings were found. Every final page was rendered and individually visually inspected. The current ledger binds 99 manuscript locations and 107 retained source locators to this publication tree and final PDF. These are document checks, not scientific-suite replays.

The GPT Linux review PDF remains preserved separately (SHA-256 `79654f41c90a0935d2287c8c1134d6e1927f155c725bc85450c0d5da6cab4a86`). Its different engine and byte identity do not replace the Windows records. The incoming publication ZIP's external `.sha256` sidecar was absent from Downloads; no external-checksum match is claimed. Its internal manifest, acceptance source hashes, original submission archive and standalone reference attachments were verified. See `verification/INPUT_IDENTITIES.json`.

The authorized scope is this new paper and one root catalog addition. Earlier editions, runtime, native kernel, dependencies, CI definitions and application files are outside the change. Physical embedding, material storage interpretation and clock calibration remain open correspondence questions; no further research is commissioned here. Existing rights/licensing remain unchanged.

This disposition records artifact readiness and authority. The post-push receipt in the local closeout records the actual commit, fresh remote byte matches and actual CI outcome; it is deliberately not self-inserted in a second commit.
''',encoding='utf-8')
paper=E.parents[1]
(paper/'README.md').write_text('''# Spatial Observation and Causal Transport with Storage in the Reciprocal Chiral Exchange Candidate

**Hilmir Frímann Halldórsson (pzychozen)** — research edition v0.1, 10 November 2026.

[Read the 25-page paper](publication/v0.1/SPATIAL_WORK_CAUSAL_TRANSPORT_v0.1.pdf) · [Editable edition and evidence](publication/v0.1/README.md)

The paper joins the accepted spatial-observation assessment W01–W05 with the declared causal transport/storage extension T01–T07, retaining D01. It distinguishes causal history observation and its finite-window temporal adjoint from a stateful connection with positive stocks, global forward mild evolution and matched work. A carrier-preload witness establishes strict receiving and later incoming boundary activity within the stated scope. Physical route, material and clock correspondence remain open.

Project-internal manuscript review is complete and repository publication is author-authorized. No external peer review is claimed. The edition includes the unchanged accepted proofs and evidence, corrected manuscript sources, the final Windows build and hash-bound page inspection. See the [access map](publication/v0.1/ACCESS_MAP.md) and [publication disposition](publication/v0.1/PUBLICATION_DISPOSITION.md).
''',encoding='utf-8')
entry='\n- [Spatial Observation and Causal Transport with Storage in the Reciprocal Chiral Exchange Candidate](papers/SPATIAL_WORK_CAUSAL_TRANSPORT/README.md), v0.1 — bounded causal history observation, its qualified temporal adjoint, and a declared transport/storage connection with matched work, forward mild evolution and a carrier-preload activity witness. Physical route and material correspondence remain open. [PDF](papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/SPATIAL_WORK_CAUSAL_TRANSPORT_v0.1.pdf) | [Edition and evidence](papers/SPATIAL_WORK_CAUSAL_TRANSPORT/publication/v0.1/README.md).\n'
catalog=W/'README.md'; original=git('show','HEAD:README.md'); assert catalog.read_bytes() in [original,original+entry.encode('utf-8')]
catalog.write_bytes(original+entry.encode('utf-8'))
payload_check['publication_guidance_appends']=[]
for name in ['README.md','BUILD.md']:
    before=P/'corrected_edition/v0.1'/name; after=E/name
    assert after.read_bytes().startswith(before.read_bytes())
    payload_check['publication_guidance_appends'].append({'path':name,'accepted_source_sha256':sha(before),'publication_sha256':sha(after),'change':'Append publication evidence/access guidance only; full accepted original prefix retained.'})
write(E/'verification/LEDGER_AND_PAYLOAD_CHECKS.json',payload_check)
write(E/'PUBLICATION_MANIFEST.json',{'scope':'All edition files except this manifest; paths relative to edition. Paper-root README and root catalog are covered by the staged/committed scope manifest in the local closeout.','excludes':['PUBLICATION_MANIFEST.json'],'files':[{'path':p.relative_to(E).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(E.rglob('*')) if p.is_file() and p.name!='PUBLICATION_MANIFEST.json']})
print(json.dumps({'edition_files':len([p for p in E.rglob('*') if p.is_file()]),'ledger_counts':counts,'pdf_bytes':doc['pdf_bytes'],'pdf_sha256':sha(E/pdf),'pages_inspected':25},indent=2))
