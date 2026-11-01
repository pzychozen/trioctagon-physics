"""Document-only validation: hashes, source locators, transcription, rounding and links.
No old code imports, geometry evaluation, source-budget evaluation or native states.
"""
from pathlib import Path,PurePosixPath
from decimal import Decimal,localcontext
import json,hashlib,re,zipfile,datetime,ast
R=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(f):return (R/f).read_text(encoding='utf-8')
def load(f):return json.loads(read(f),parse_float=Decimal)
def dump(f,x):(R/f).write_text(json.dumps(x,indent=2,ensure_ascii=False,default=str)+'\n',encoding='utf-8')
def write(f,s):(R/f).write_text(s.strip()+'\n',encoding='utf-8')
def get(f,p):
 x=load(f)
 for k in p.strip('/').split('/'):
  k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
 return x
checks=[]
def ok(name,detail):checks.append({'check':name,'passed':True,'detail':detail})
sm=load('SOURCE_MANIFEST.json')
for e in sm['original_consulted_files']:
 p=Path(e['path']);assert p.stat().st_size==e['before']['bytes'] and sha(p)==e['before']['sha256']
for e in sm['copied_inputs']:
 p=R/e['path'];assert p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
ok('bounded original and copied-input hash preservation',{'originals':2,'copies':len(sm['copied_inputs']),'whole_repository_audit':False})
for e in load('EXTRACTION_MANIFEST.json'):
 with zipfile.ZipFile(R/e['archive']) as z:assert z.read(e['member'])==(R/e['extracted_path']).read_bytes()
ok('extracted members byte-equal to original archives',38)
archives=[]
for p in sorted((R/'packet').rglob('*.zip')):
 with zipfile.ZipFile(p) as z:
  names=z.namelist();assert len(names)==len(set(names))==len({n.casefold() for n in names})
  assert z.testzip() is None
  for e in z.infolist():
   n=e.filename;q=PurePosixPath(n)
   assert not q.is_absolute() and '..' not in q.parts and ':' not in n and '\\' not in n
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  archives.append({'file':p.relative_to(R).as_posix(),'members':len(names),'CRC':True,'safe_unique_casefold_names':True})
ok('six direct retained review/evidence archives safety and CRC',archives)
cells=load('manuscript/tables/TABLE_PROVENANCE.json')['cells'];bytable={}
for c in cells:
 x=get(c['source_file'],c['json_pointer']);original=x if isinstance(x,list) else str(x)
 assert original==c['original_token'],c
 if c['rule'].startswith('Decimal'):
  digits=int(re.search(r'(\d+) places',c['rule']).group(1))
  with localcontext() as ctx:ctx.prec=140;s=format(Decimal(str(x)),('+' if 'explicit sign' in c['rule'] else '')+f'.{digits}f')
 else:s=', '.join(map(str,x)) if isinstance(x,list) else str(x)
 assert s==c['display'],c
 bytable.setdefault(c['table'],{}).setdefault(str(c['row']),[]).append(c['display'])
for name,rows in bytable.items():
 data=[[x.strip() for x in s.strip('|').split('|')] for s in read(f'manuscript/tables/{name}.md').splitlines()[2:]]
 assert len(data)==len(rows)
 for row,values in zip(data,rows.values()):assert row[1:]==values,(name,row,values)
ok('generated table scalar pointers, original tokens, rounding and cell positions',{'tables':len(bytable),'cells':len(cells)})
sumchecks=[]
for name,keys,digits in [('intensity',['onsite','coupling','finite_increment_square'],6),('radial',['macro_magnitude','chiral_magnitude','cross_alignment'],9)]:
 for i in range(4):
  row={c['column']:Decimal(c['display']) for c in cells if c['table']==name and c['row']==i}
  residual=sum(row[k] for k in keys)-row['total'];bound=Decimal(2)*Decimal(10)**(-digits);assert abs(residual)<=bound
  sumchecks.append({'table':name,'row':i,'rounded_sum_minus_rounded_total':str(residual),'rounding_allowance':str(bound)})
ok('eight rounded table totals; ordinary addition only',sumchecks)
manual=load('manuscript/tables/MANUAL_TABLE_PROVENANCE.json')
for c in manual:
 if 'json_pointer' in c:assert get(c['source_file'],c['json_pointer'])==c['original_token']
 if 'line' in c:assert c['original_token'] in read(c['source_file']).splitlines()[c['line']-1]
ok('manual history and inherited-verification table provenance',len(manual))

# Selected prose quantities that are not fully displayed in the numeric tables.
prose=[]
def pval(claim,f,p,display,magnitude=False):
 raw=get(f,p);d=Decimal(str(raw));shown=Decimal(display);d=abs(d) if magnitude else d
 with localcontext() as ctx:
  ctx.prec=140;assert d.quantize(Decimal(1).scaleb(shown.as_tuple().exponent))==shown,(claim,p,raw,display)
 prose.append({'claim':claim,'source_file':f,'json_pointer':p,'original_token':str(raw),'display':display,'rule':'ROUND_HALF_EVEN at displayed decimal place'+('; magnitude explicitly described in prose' if magnitude else '')})
fb='evidence/Z03/FROZEN_Z_SOURCE_BUDGET.json';rb='evidence/Z03/RADIAL_TRANSVERSE_ACCOUNTING.json';ib='evidence/Z03/NATIVE_INTENSITY_BUDGET.json'
for i,display in [(0,'-0.182919'),(1,'-0.0133118'),(2,'0.00164299'),(3,'0.0154716')]:pval(f'C{41+i}',fb,f'/runs/120/{i}/frozen/macro_displacement/0',display)
for i,vec in [(0,['0.289380','0.124479','0.070342']),(3,['-0.000670044','0.0211527','-0.0166755'])]:
 for j,s in enumerate(vec):pval(f'C{41+i}',fb,f'/runs/120/{i}/frozen/chiral_displacement/{j}',s)
pval('C42',fb,'/runs/120/1/frozen/chiral_displacement/0','0.0141878')
pval('C43',fb,'/runs/120/2/frozen/chiral_displacement/2','-0.00322774')
pval('C40',rb,'/runs/120/2/radial_transverse/radial_cancellation/sum_abs_over_abs_net','223.9')
pval('C44',rb,'/runs/120/3/radial_transverse/y_terms/phase_symmetric_pair','0.0144813')
pval('C44',rb,'/runs/120/3/radial_transverse/signed_radius_squared_terms/C~1phase_symmetric_pair','-0.00478717')
for k,s in [('macro_magnitude','0.009772971461'),('chiral_magnitude','-0.001044366176'),('cross_alignment','-0.005091184838')]:pval('C44',rb,'/runs/120/3/radial_transverse/coarse_endpoint_difference/'+k,s)
pval('C44',rb,'/runs/120/3/radial_transverse/actual_delta_radius_squared','0.003637420448')
pval('C44',rb,'/runs/120/3/radial_transverse/actual_delta_radius','0.007800865379')
pval('Guide page 2',rb,'/runs/120/3/radial_transverse/actual_delta_radius','0.00780087')
for i,s in [(1,'0.0369743'),(2,'0.0606040')]:pval('C19','evidence/Z02/GAP_COMPARISON.json',f'/evaluations/F{i}/gap/best_distance',s)
dump('PROSE_NUMERIC_PROVENANCE.json',prose);ok('supplemental prose numeric transcription and rounding',len(prose))

claims=load('CLAIM_SOURCE_MAP.json');ids={c['id'] for c in claims};used=set(re.findall(r'\[(C\d\d)\]',read('manuscript/NOTE.md')))
assert ids==used=={f'C{i:02d}' for i in range(1,52)}
pointers=0
for c in claims:
 d=c['report'];assert read(d['file']).splitlines()[d['line']-1]==d['heading']
 for d in c['ledger_references']:get(d['file'],d['pointer']);pointers+=1
 for d in c['definitions']:assert (R/d['file']).is_file()
 if 'review' in c:assert (R/c['review']['file']).is_file()
ok('central claim coverage, report headings and exact JSON locators',{'claims':51,'ledger_pointers':pointers})
for f in ['evidence/Z01/inputs/retained.motion.json','evidence/Z02/inputs/SELECTED_HISTORY.json']:assert (R/f).is_file()
assert sha(R/'evidence/Z01/inputs/retained.motion.json')=='071f6f7dc74128d638b0e96e33897b1366b2f8bcb98ca741c11fe0af5ed0e1e7'
assert sha(R/'evidence/Z02/inputs/SELECTED_HISTORY.json')=='a294a4b0bf181adaa2054aa52379c1832a7833e3faa7614d0785aecd709ea09c'
assert get('packet/reading/Z03/NUMERIC_POLICY.json','/actual_indices')==[0,1,2,3,4]
assert get('packet/reading/Z02/ADMISSION_AND_PLAN.json','/window/excluded_suffix_rows')==0
ok('separate history identities, five-state reuse and full admitted window','History table and exact native/observer constants reconciled to manual-table provenance and accepted source presets; no state evaluation.')
figs=load('FIGURE_PROVENANCE.json')
for f in figs:assert (R/f['source_extracted_file']).read_bytes()==(R/f['manuscript_file']).read_bytes() and sha(R/f['manuscript_file'])==f['sha256']
ok('original figures unchanged and uncropped',3)

# Directly inspected final PDF pages; human/model visual judgments are declared,
# not inferred from a renderer exit code. All 20 images were viewed individually.
notes=[
'Title, author accents, opening distinctions and footer clear.',
'History table and corrected two-column notation table complete; no pipe truncation.',
'Norm/gain/harmonic/placement and sphere radicals readable; preset separates native coefficients.',
'Telescope equations and global-freeze equation fit; native/chiral allocation unambiguous.',
'All three endpoint/chord tables fit; signs, labels and page footer clear.',
'Complete top sheet, legend and all five markers retained; projected upper/lower overlap qualified.',
'Both side views, upper/lower and near/far arcs, patch distinction and caption readable.',
'Common-phase, envelope cross product and EMA distinctions readable.',
'Margin and mirror-height inequality signs correct; clock sign sequence intact.',
'Intensity parent/child formula, signed table and residual explanation intact.',
'Five amplitude terms, two phase terms and S/A sign convention readable.',
'Finite divided difference and transverse identities legible, including both-zero exception.',
'Fine and coarse radial equations separate; signed table fits; cancellation qualification present.',
'First two span accounts, small x explanation and displacement table readable.',
'Final outward step signs and later-onsite reviewer inference clear.',
'Original four-panel radial chart uncropped with independent-scale warning and readable labels.',
'Residual exponent and inherited-check table legible; counts are not claimed as new runs.',
'References, claim-map route, placement and stopping boundary fit without clipping.'
]
build=load('BUILD_RECORD.json');vr=[]
for out in build['outputs']:
 assert sha(R/out['pdf'])==out['sha256'];pages=sorted((R/out['render_directory']).glob('page-*.png'));assert len(pages)==out['pages']
 data=[]
 for i,p in enumerate(pages,1):data.append({'page':i,'render_sha256':sha(p),'render_bytes':p.stat().st_size,'review':'pass','observation':notes[i-1] if out['pages']==18 else ['Title and three distinctions, both histories and boundary/ray qualifications fit with clear footer.','All four spans, inward/outward versus height and limitations readable; no clipping.'][i-1]})
 vr.append({'pdf':out['pdf'],'pdf_sha256':out['sha256'],'pages':out['pages'],'render_dpi':120,'review_method':'Every final full page opened individually with view_image; no contact-sheet-only acceptance.','page_reviews':data})
dump('VISUAL_REVIEW.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'Codex','artifacts':vr,'visual_defects_remaining':0,'final_hashes_bound':True})
ok('final PDF hashes, page counts and individual full-page visual review',{'PDFs':2,'pages':20})
eq=load('manuscript/EQUATION_TRANSCRIPTION.json');source_eq=[]
for block in re.findall(r'\$\$\s*\n(.*?)\n\$\$',read('manuscript/NOTE.md'),re.S):source_eq.append(' '.join(s.strip() for s in block.splitlines()))
assert source_eq==[e['latex'] for e in eq]
ok('display equations transcribed exactly from canonical editable source',{'display_blocks':len(eq),'definition_review':'Compared by reading source/report identities and mapped C07-C39; notation changes explicit. No symbolic/numeric scientific evaluation.'})
layout=load('tmp/LAYOUT_RECORD.json');assert all(p['bottom_content_pt']>=46 for a in layout for p in a['pages'])
assert not build['warnings'];ok('layout and glyph diagnostics','Page bottoms above 46 pt; no missing glyph warnings; table column counts and text/equation widths checked by builder.')

prefix='call C:\\Users\\Notandi\\miniconda3\\condabin\\conda.bat activate torment && python -X utf8 -I -B '
commands=['NCM-Z-DOC-01: actual document-only command/operation register','Shell: cmd.exe, login=false. Existing torment interpreter; no installs. Paths below are actual task paths. Repeated read-only type/rg/more/dir inspections are summarized by input manifest rather than claimed as scientific executions.','Core artifact commands executed:']
for file in ['intake.py','verify_extract.py','inspect_ledgers.py','extract_document_data.py','manuscript/build_document.py','tmp/inspect_document_sources.py','tmp/locate_fields.py','make_review_documents.py','document_qa.py']:
 commands.append(prefix+str(R/file))
commands+=['Build attempts: mathtext bmod failure; mathtext tfrac failure; missing pdftotext failure; successful draft; final successful rebuild after notation-table fix. Both final PDFs were rendered and all final pages viewed.','Metadata builder: first locator validation stopped on /evaluations/F1/host_notches; corrected locator /evaluations/F1/gap/host_notches resolved against the retained JSON. No data changed.','A read-only python -c command intended to print work-order section 7 failed with SyntaxError from CMD quoting. No Python inspection code ran in that attempt.','PDF skill creation marker, executed successfully once before first authoring:',r'node C:\Users\Notandi\.codex\plugins\cache\openai-primary-runtime\pdf\26.1020.11618\skills\pdf\container_tools\mark_artifact_operation_started.mjs --operation-kind create --expected-output-count 2 --output-format pdf','Poppler commands actually dispatched by the build helper:']
for out in build['outputs']:
 commands.append(' '.join(map(str,out['render_command'])));commands.append(str(load('ENVIRONMENT.json')['executables']['pdfinfo'])+' '+str(R/out['pdf']))
commands+=['Document QA first stopped when its link detector mistook a bracketed display-equation expression for a Markdown link. Display-math blocks were excluded from link parsing; the corrected document-only QA passed. This changed neither the equation nor the PDF.','Read-only inspections: type/more/rg on the supplied work order, supplied reports/reviews/source snapshots, new Markdown and helper scripts; dir/where for existing executables and fresh-root selection. PDF runtime dependency discovery was read-only. No archived Python source was imported.','File edits: apply_patch and new document-only Python helpers, only beneath '+str(R)+'.','Visual review: view_image on the original figure sheets and each final Poppler page image. No image generation or scientific figure production.','Package command executed after successful document QA:',prefix+str(R/'package_review.py'),'The scripts are supplied as exact editable build/QA inputs. Historical reproduction commands in packet/evidence/reviews remain inactive.']
write('COMMANDS.txt','\n\n'.join(commands))
write('CLOSEOUT.txt',f'''NCM-Z-DOC-01 v0.1 — completed documentation consolidation
Actual fresh external root: {R}
Draft status: ready for GPT/author documentation review; no publication acceptance implied.

Deliverables: complete canonical Markdown methods note and 18-page review PDF; short editable companion and 2-page PDF; claim/source map; references; evidence and provenance indexes; original archives/figures; document build and QA helpers; ZIP and outside receipt.
51 central claims mapped. 83 generated table cells preserve original tokens and exact JSON pointers; 25 additional manual-table provenance records. Both final PDFs have been rendered and all 20 pages visually inspected individually. Current QA counts describe documents, not scientific experiments.

New native map evaluations: 0
New prestage evaluations: 0
New phase-kick evaluations: 0
New source-budget evaluations: 0
New observer evaluations: 0
New EMA evaluations/advances: 0
New history states: 0
Old scientific producer/checker/figure-generator replays: 0
Git commands: 0
Model, kernel, application and earlier-paper changes: 0
Online research, installation, publication: 0

CMD activated the existing torment environment. Existing Matplotlib PdfPages/mathtext generated PDFs; existing Poppler rendered them. No TeX compiler or pdftotext was available; this is not compiled LaTeX. QA therefore combines source/table/equation transcription, file identity, layout diagnostics and full-page visual inspection; no PDF text-extraction claim is made.

The bounded consulted-original preservation set is exactly the Downloads packet ZIP and standalone documentation work order. Both match their intake hashes. Packaged sources and extracted copies are checked separately. No claim is made to a live-original or whole-repository audit.

The two histories remain separate; Z03 reuses Z02. All four five-state spans and final outward step are explained. Physical motion/flux/support/duality identification remains unresolved. Rounded retained values, scalar residuals and 80/120 agreement are numerical corroboration, not interval certification or full complex-state authentication.

No material blocker remains for documentation review. Recommend a project methods guide with the short application-reading companion; an appendix is a secondary placement. The next decision is placement/adoption after review, not an automatic new investigation.
''')
authored=list((R/'manuscript').rglob('*.md'))+[R/x for x in ['START_HERE.md','PLAIN_LANGUAGE_GUIDE.md','CLAIM_SOURCE_MAP.md','EVIDENCE_INDEX.md','PLACEMENT_AND_CONTRIBUTION.md','CORRECTIONS_AND_DISPOSITION.md']]
links=[]
for p in authored:
 prose_only=re.sub(r'\$\$.*?\$\$','',p.read_text(encoding='utf-8'),flags=re.S)
 for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',prose_only):
  target=match.group(1);assert not re.match(r'\w+://',target)
  dest=(p.parent/target.split('#')[0]).resolve();assert dest.is_relative_to(R) and (dest.is_file() or dest==R/'DOCUMENT_QA.json'),(p,target)
  links.append({'file':p.relative_to(R).as_posix(),'target':target})
ok('portable authored-document links resolve inside review tree',len(links));dump('LINK_QA.json',links)
for p in [R/'manuscript/NOTE.md',R/'PLAIN_LANGUAGE_GUIDE.md']:
 text=p.read_text(encoding='utf-8');assert not any(s in text for s in ['TODO','TBD','INSERT HERE','turn0search'])
ok('no unfinished narrative placeholders',2)
imports={}
for file in ['intake.py','verify_extract.py','inspect_ledgers.py','extract_document_data.py','manuscript/build_document.py','make_review_documents.py','document_qa.py','package_review.py']:
 p=R/file
 if not p.exists():continue
 tree=ast.parse(p.read_text(encoding='utf-8'));names=[]
 for n in ast.walk(tree):
  if isinstance(n,ast.Import):names.extend(a.name for a in n.names)
  elif isinstance(n,ast.ImportFrom):names.append(n.module)
 assert not any(n and (n.startswith('kernel_physics') or n.startswith('evidence.') or n.startswith('packet.')) for n in names)
 imports[file]=names
ok('new helper imports inspected; no project or historical modules imported',imports)
dump('DOCUMENT_QA.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'task':'NCM-Z-DOC-01 v0.1','status':'PASS','checks':checks,'group_count':len(checks),'scientific_evaluations':{'native':0,'prestage':0,'kick':0,'budget':0,'observer':0,'EMA':0,'new_states':0,'historical_science_replays':0},'counter_basis':'Executed operations were current document helpers and direct file/image reads; no scientific modules or historical scripts were run. Counts are task execution accounting, not instrumented native-kernel counters.','limitations':['No pdftotext; source/renderer/visual QA used.','No current live producer authenticity or whole-repository audit.','Retained scientific assertions were not rerun.']})
for link in links:assert (R/link['file']).parent.joinpath(link['target'].split('#')[0]).resolve().is_file()
print(json.dumps({'document_QA':'PASS','groups':len(checks),'claims':51,'table_cells':len(cells),'prose_values':len(prose),'authored_links':len(links),'final_pages_inspected':20}))
