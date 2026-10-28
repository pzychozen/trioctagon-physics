"""Bounded transcription, identity, link and package checks; no dynamics."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.stdout.reconfigure(encoding='utf-8')
try:
 from pypdf import PdfReader
except ImportError:
 sys.path.append('C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/site-packages')
 from pypdf import PdfReader
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git','--no-optional-locks',*a],cwd=REPO,stderr=subprocess.DEVNULL)
prov=json.loads((ROOT/'evidence/PROVENANCE.json').read_text())
base=json.loads((ROOT/'verification/baseline.json').read_text())
main=(ROOT/'main.tex').read_text(encoding='utf-8');refs=(ROOT/'references.tex').read_text(encoding='utf-8')
checks={}
checks['retained_copies_match_origins_and_recorded_hashes']=all(sha((ROOT/x['file']).read_bytes())==x['sha256'] and (ROOT/x['file']).read_bytes()==Path(x['origin']).read_bytes() for x in prov['retained_files'])
checks['eight_sources_match_pinned_git_blobs']=all(sha(git('show',x['commit']+':'+x['path']))==x['sha256'] and (REPO/x['path']).read_bytes()==git('show',x['commit']+':'+x['path']) for x in prov['accepted_sources'])
labels=re.findall(r'\\label\{([^}]+)\}',main)
references=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',main)
cites=[x for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',main) for x in group.split(',')]
bib=re.findall(r'\\bibitem\{([^}]+)\}',refs)
checks['unique_labels']=len(labels)==len(set(labels))
checks['all_equation_section_references_resolve']=set(references)<=set(labels)
checks['all_citations_resolve']=set(cites)<=set(bib)
links=re.findall(r'\\href\{([^}]+)\}',main+refs)
local_links=[x for x in links if not x.startswith('http')]
checks['all_package_relative_tex_links_exist']=all((ROOT/x).is_file() for x in local_links)
checks['all_figure_and_table_inputs_exist']=all((ROOT/(x if Path(x).suffix else x+'.tex')).is_file() for x in re.findall(r'\\(?:input|includegraphics)(?:\[[^\]]*\])?\{([^}]+)\}',main))
turn=json.loads((ROOT/'evidence/turning_witness_20261028.json').read_text())
graph=json.loads((ROOT/'evidence/delayed_graph_response_20261028.json').read_text())
checks['certified_turn_endpoints_transcribed']=all(x in main for x in turn['turning']['decimal_enclosure'])
def texfrac(s):
 if '/' not in s:return s
 a,b=s.split('/');sign='-' if a.startswith('-') else ''
 return sign+'\\frac{'+a.lstrip('-')+'}{'+b+'}'
checks['prescribed_exact_fractions_transcribed']=all(texfrac(graph[k]['exact']) in main for k in ['K0','K_star','J_star','R_star','direction_dot_star'])
checks['exact_amplitude_ratio_transcribed']=texfrac(turn['shape_ratio_squared']['n1']['exact_fraction']) in main
checks['head_branch_index_and_tracked_work_unchanged']=(git('rev-parse','HEAD').decode().strip()==base['commit'] and git('branch','--show-current').decode().strip()==base['branch'] and sha(git('diff','--binary'))==base['tracked_diff_sha256'] and sha(git('diff','--cached','--binary'))==base['staged_diff_sha256'])
prefix=ROOT.relative_to(REPO).as_posix().split('/v0.1')[0]+'/'
status='\n'.join(x for x in git('status','--porcelain=v1','--untracked-files=all').decode().splitlines() if prefix not in x)
checks['outside_draft_git_status_unchanged']=status==base['outside_status']
pdf=PdfReader(ROOT/'REVIEW.pdf')
text='\n'.join(page.extract_text() or '' for page in pdf.pages)
(ROOT/'tmp').mkdir(exist_ok=True)
(ROOT/'tmp'/'review_extracted.txt').write_text(text,encoding='utf-8')
checks['pdf_all_pages_have_text']=all(bool(p.extract_text().strip()) for p in pdf.pages)
checks['pdf_no_unresolved_reference_markers']='??' not in text
build=json.loads((ROOT/'verification/build_record.json').read_text())
checks['no_overfull_missing_character_or_undefined_warnings']=not any(any(s in x for s in ['Overfull','Missing character','undefined']) for x in build['warnings'])
pdf_links=[]
for p in pdf.pages:
 for a in p.get('/Annots',[]):
  obj=a.get_object();action=obj.get('/A',{})
  if '/URI' in action:pdf_links.append(str(action['/URI']))
checks['pdf_retains_external_and_evidence_links']=all(x in pdf_links for x in local_links) and any('openstax.org' in x for x in pdf_links) and any(prov['baseline'] in x for x in pdf_links)
receipt={'status':'PASS' if all(checks.values()) else 'CHECK_FAILED','checks':checks,'baseline':prov['baseline'],'pdf_pages':len(pdf.pages),'approximate_extracted_word_count':len(text.split()),'tex_labels':len(labels),'bibliography_entries':len(bib),'pdf_uri_links':len(pdf_links),'pdf_sha256':sha((ROOT/'REVIEW.pdf').read_bytes()),'build_warnings':build['warnings'],'visual_review':'Recorded separately in REVIEW_HANDOFF.md after page inspection.','scientific_checker_replays':0,'state_updates':0,'root_solves':0,'scope':'Transcription and document validation, not recertification of completed mathematics.'}
(ROOT/'verification/verification_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
if not all(checks.values()):raise SystemExit(1)
