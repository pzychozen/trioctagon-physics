"""Bounded publication document checks, distinct from historical preparation checks.

Reads retained records and the built PDF; never runs scientific checkers.
Does not require HEAD/index to equal the historical preparation baseline.
"""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding='utf-8')
try:
 from pypdf import PdfReader
except ImportError:
 sys.path.append('C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/site-packages')
 from pypdf import PdfReader
def sha(data):return hashlib.sha256(data).hexdigest()
main=(ROOT/'main.tex').read_text(encoding='utf-8')
refs=(ROOT/'references.tex').read_text(encoding='utf-8')
old=json.loads((ROOT/'verification/reviewed_manifest.json').read_text())
oldhash={x['path']:x['sha256'] for x in old['files']}
changes=json.loads((ROOT/'verification/publication_editorial_changes.json').read_text())
build=json.loads((ROOT/'verification/publication_build_record.json').read_text())
visual=json.loads((ROOT/'verification/publication_visual_review.json').read_text())
checks={}
reconstructed=main
for e in reversed(changes['edits']):
 assert reconstructed.count(e['after'])==1,e['kind']
 reconstructed=reconstructed.replace(e['after'],e['before'])
checks['only_recorded_authorized_manuscript_edits']=sha(reconstructed.encode('utf-8'))==oldhash['main.tex']
normalized=main.replace(r'Let $\Delta\le D_0$ be the width of the current phase interval, and rotate this interval so that its bisector is the positive real axis.','Rotate the current phase interval to its bisector.')
mathpattern=r'\$[^$]*\$|\\\[[\s\S]*?\\\]|\\begin\{(?:equation|align|gather)\*?\}[\s\S]*?\\end\{(?:equation|align|gather)\*?\}'
checks['math_tokens_unchanged_except_approved_inline_definition']=re.findall(mathpattern,normalized)==re.findall(mathpattern,reconstructed)
equations=r'\\begin\{(equation|align|gather)\*?\}([\s\S]*?)\\end\{\1\*?\}'
checks['all_display_equation_environments_unchanged']=re.findall(equations,main)==re.findall(equations,reconstructed)
prov=json.loads((ROOT/'evidence/PROVENANCE.json').read_text())
scientific=[x for x in prov['retained_files'] if Path(x['file']).suffix in ('.py','.json')]
assert len(scientific)==6
checks['six_scientific_evidence_hashes_unchanged']=all(sha((ROOT/x['file']).read_bytes())==x['sha256'] for x in scientific)
unchanged=['references.tex','make_figures.py','verify_review.py','evidence/MANUSCRIPT_WORK_ORDER.txt','evidence/PROVENANCE.json','evidence/README.md','verification/build_record.json','verification/verification_receipt.json','verification/visual_review.json','tables/areas.tex','tables/budgets.tex','tables/increments.tex','figures/FIGURE_DATA.json']
checks['historical_records_bibliography_figure_source_and_tables_unchanged']=all(sha((ROOT/p).read_bytes())==oldhash[p] for p in unchanged)
handoff=(ROOT/'REVIEW_HANDOFF.md').read_bytes().split(b'\n\n',1)[1]
checks['historical_handoff_only_has_prepended_notice']=sha(handoff)==oldhash['REVIEW_HANDOFF.md']
labels=re.findall(r'\\label\{([^}]+)\}',main)
refs_used=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',main)
cites=[x for block in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',main) for x in block.split(',')]
bib=re.findall(r'\\bibitem\{([^}]+)\}',refs)
checks['labels_and_references_resolve']=len(labels)==len(set(labels)) and set(refs_used)<=set(labels)
checks['citations_resolve']=set(cites)<=set(bib)
links=re.findall(r'\\href\{([^}]+)\}',main+refs)
checks['relative_evidence_links_exist']=all((ROOT/x).is_file() for x in links if not x.startswith('http'))
inputs=re.findall(r'\\(?:input|includegraphics)(?:\[[^\]]*\])?\{([^}]+)\}',main)
checks['required_package_inputs_exist']=all((ROOT/(x if Path(x).suffix else x+'.tex')).is_file() for x in inputs)
reader=PdfReader(ROOT/'REVIEW.pdf');pages=len(reader.pages)
text='\n'.join(p.extract_text() or '' for p in reader.pages)
pdfhash=sha((ROOT/'REVIEW.pdf').read_bytes())
checks['pdf_matches_final_build_source_and_hash']=build['pdf_sha256']==pdfhash and build['source_sha256']['main.tex']==sha((ROOT/'main.tex').read_bytes()) and build['source_sha256']['references.tex']==sha((ROOT/'references.tex').read_bytes()) and build['returncode']==0
checks['compiler_warnings_absent']=not build['warnings']
checks['pdf_all_pages_have_text_and_no_unresolved_reference_markers']=all((p.extract_text() or '').strip() for p in reader.pages) and '??' not in text
checks['publication_pdf_metadata']=('repository research edition v0.1' in (reader.metadata.subject or ''))
checks['visual_inspection_matches_actual_artifact']=visual['status']=='PASS' and visual['pdf_sha256']==pdfhash and visual['pdf_pages']==pages and visual['pages_inspected']==list(range(1,pages+1)) and not visual['remaining_layout_defects_found']
pdfuris=[]
for p in reader.pages:
 for a in p.get('/Annots',[]):
  action=a.get_object().get('/A',{})
  if '/URI' in action:pdfuris.append(str(action['/URI']))
checks['pdf_preserves_all_source_and_evidence_uri_links']=set(links)<=set(pdfuris)
checks['current_manuscript_has_no_pending_review_status']=not any(s in main for s in ['WORKING REVIEW DRAFT','This draft awaits','remain the next agreed steps','not a publication approval'])
mds=[ROOT/x for x in ['README.md','CLAIM_SOURCE_MAP.md','PUBLICATION_DISPOSITION.md','REVIEW_HANDOFF.md','verification/README.md']]
bad=[]
for p in mds:
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if not link.startswith(('https:','http:')) and not (p.parent/link.split('#')[0]).is_file():bad.append((str(p),link))
checks['affected_markdown_links_resolve']=not bad
if bad:print(json.dumps({'broken_markdown_links':bad},indent=2))
result={'status':'PASS' if all(checks.values()) else 'FAIL','edition':'Author-authorized repository research edition v0.1','date':'2026-10-28','scientific_baseline':prov['baseline'],'reviewed_source_sha256':oldhash['main.tex'],'reviewed_pdf_sha256':oldhash['REVIEW.pdf'],'final_source_sha256':sha((ROOT/'main.tex').read_bytes()),'final_pdf_sha256':pdfhash,'pdf_pages':pages,'equation_environments_preserved':len(re.findall(equations,main)),'labels':len(labels),'bibliography_entries':len(bib),'pdf_uri_links':len(pdfuris),'checks':checks,'scientific_checker_replays':0,'state_updates':0,'root_solves':0,'historical_preparation_verifier_executed':False,'scope':'Publication document/evidence checks only. No claim that historical HEAD/index invariance holds after publication. Git preservation and outgoing payload are checked separately.'}
(ROOT/'verification/publication_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
if not all(checks.values()):raise SystemExit(1)
