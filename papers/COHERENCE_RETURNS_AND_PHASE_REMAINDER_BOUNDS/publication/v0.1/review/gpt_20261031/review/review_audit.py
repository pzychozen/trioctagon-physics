from pathlib import Path
import json,hashlib,zipfile,collections,re,sys,platform
import fitz
ROOT=Path(__file__).resolve().parent
R=ROOT/'received'
sha=lambda b:hashlib.sha256(b).hexdigest()
checks=[]
def ck(name, ok, detail=None):
 checks.append({'name':name,'passed':bool(ok),'detail':detail})
 if not ok: raise AssertionError(name)
manifest=json.loads((R/'OUTPUT_HASHES.json').read_text())['files']
bad=[]
for p,expected in manifest.items():
 b=(R/p).read_bytes()
 if len(b)!=expected['bytes'] or sha(b)!=expected['sha256']: bad.append(p)
ck('344 output-manifest members match',len(manifest)==344 and not bad,{'listed':len(manifest),'mismatch':bad})
actual={p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file()}
ck('complete extracted-member coverage',actual==set(manifest)|{'OUTPUT_HASHES.json'},{'actual':len(actual)})
ck('separate START_HERE equals archive member',(R/'START_HERE.md').read_bytes()==Path('/mnt/data/START_HERE(20261031-165633).md').read_bytes())
P=R/'packet/NCM_PAPER_01_Codex_Packet_v0.1'
for name in ['NCM_DUAL_02_v0.1_REVIEW.zip','NCM_DUAL_03_v0.1_REVIEW.zip']:
 ck('original retained evidence archive '+name,(P/'evidence'/name).read_bytes()==(Path('/mnt/data')/name).read_bytes())
with zipfile.ZipFile('/mnt/data/NCM_PAPER_01_Codex_Packet_v0.1.zip') as z:
 mismatch=[]; members=0
 for i in z.infolist():
  if i.is_dir():continue
  parts=Path(i.filename).parts
  if parts[0]=='NCM_PAPER_01_Codex_Packet_v0.1':parts=parts[1:]
  target=P.joinpath(*parts);members+=1
  if not target.exists() or target.read_bytes()!=z.read(i.filename):mismatch.append(i.filename)
 ck('delivered source packet contents unchanged',not mismatch,{'members':members,'mismatch':mismatch})
sm=json.loads((R/'SOURCE_MANIFEST.json').read_text())
ck('source before/after records consistent',all(x['before']==x['after'] and x['unchanged'] for x in sm['sources'].values()),{'records':len(sm['sources']),'qualification':'Live Windows source bytes not inspected'})
ck('recorded scientific-source comparison consistent',all(x['current']==x['prior'] and x['match'] for x in sm['source_comparison_to_prior'].values()),{'records':len(sm['source_comparison_to_prior'])})
for x in sm['packet_members']:
 b=(R/x['path']).read_bytes()
 ck('packet before/after '+x['path'],x['before']==x['after'] and x['after']['sha256']==sha(b) and x['after']['bytes']==len(b))
extract=json.loads((R/'evidence/RETAINED_ATTEMPT_METRICS.json').read_text())
with zipfile.ZipFile(P/'evidence/NCM_DUAL_03_v0.1_REVIEW.zip') as z:
 ledger=[json.loads(l) for l in z.read('phase_b/attempt_ledger.jsonl').decode().splitlines() if l.strip()]
 summary=json.loads(z.read('phase_b/discovery_summary.json'))
 ck('60 retained ledger entries match summary',len(ledger)==60 and ledger==summary['attempts'])
 classifications=collections.Counter();reasons=collections.Counter();attempts=0
 for row in ledger:
  i=row['id']; b=z.read(f'phase_b/attempts/{i}.json'); o=json.loads(b); e=extract[i]
  ck('retained data extraction '+i,e['member_sha256']==sha(b) and e['metrics']==o['metrics'] and e['classification']==o['classification']==row['classification'] and e['stop_reason']==o['stop_reason']==row['stop_reason'])
  classifications[o['classification']]+=1;reasons[o['stop_reason']]+=1;attempts+=o['F_attempts']
 groups=json.loads(z.read('phase_b/numerical_groups.json'))
 ck('seven groups extracted without modification',len(groups['groups'])==7 and groups==json.loads((R/'evidence/RETAINED_GROUPS_EXTRACT.json').read_text()))
 ck('outcome reconciliation',dict(classifications)=={'solver_failed':18,'lower_period_one_numerical':42} and reasons['line_search_failed']==17 and reasons['max_iterations']==1 and attempts==8211,{'classifications':dict(classifications),'stop_reasons':dict(reasons),'historical_discovery_F_attempts':attempts})
a=json.loads((R/'proof_review/SYMBOLIC_RESULTS.json').read_text());b=json.loads((ROOT/'symbolic_replay/proof_review/SYMBOLIC_RESULTS.json').read_text())
ck('current 29 algebra-check replay matches',a['checks']==b['checks'] and len(b['checks'])==29 and all(x['passed'] for x in b['checks']))
ck('phase-bound formatting matches',a['phase_bound_degrees_formatting_only']==b['phase_bound_degrees_formatting_only'])
tex=(R/'manuscript/main.tex').read_text()
snap=json.loads((R/'manuscript/content_snapshot.json').read_text())
source_eq=[x[1] for x in snap['blocks'] if x[0]=='eq']
def norm(s):
 s=re.sub(r'\\frac\s*([A-Za-z0-9])\s*([A-Za-z0-9])',r'\\frac{\1}{\2}',s)
 s=re.sub(r'\\frac\s*([A-Za-z0-9])(?=\{)',r'\\frac{\1}',s)
 s=re.sub(r'\\sqrt\s*([A-Za-z0-9])',r'\\sqrt{\1}',s)
 return re.sub(r'\\(le|ge|ne)(?![A-Za-z])',lambda m:'\\'+{'le':'leq','ge':'geq','ne':'neq'}[m[1]],s)
texeq=re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',tex,re.S)
ck('30 TeX equation expressions match content snapshot',len(texeq)==30 and texeq==list(map(norm,source_eq)))
ck('seven tables in both snapshot and TeX',sum(x[0]=='table' for x in snap['blocks'])==7 and tex.count(r'\begin{tabularx}')==7)
pdf=R/'manuscript/REVIEW.pdf';doc=fitz.open(pdf)
links=[(i+1,l) for i,p in enumerate(doc) for l in p.get_links()]
internal=[l for _,l in links if l['kind']==fitz.LINK_GOTO]
external=[l for _,l in links if l['kind']!=fitz.LINK_GOTO]
ck('19 PDF pages',len(doc)==19)
ck('all internal citations target bibliography',len(internal)==36 and all(x['page']==18 for x in internal))
ck('12 relative evidence links exist',len(external)==12 and all((pdf.parent / x.get('file',x.get('uri','')).split('#')[0]).resolve().is_file() for x in external),[x.get('file',x.get('uri','')) for x in external])
ck('PDF digest matches recorded structure',sha(pdf.read_bytes())==json.loads((R/'qa/PDF_STRUCTURE.json').read_text())['pdf_sha256'])
ck('no blank or replacement-character text pages',all(p.get_text().strip() and '\ufffd' not in p.get_text() for p in doc))
# Preserve original CRLF conventions in optional source-only repair candidate.
fix=ROOT/'tex_fix_candidate'
orig=(R/'manuscript/main.tex').read_bytes()
updated,n=re.subn(rb'(?m)^(\\par\\textit\{[^\r\n]*\})(\r?\n)',lambda m:m[1]+b'\\par'+m[2],orig)
ck('source-only repair inserts exactly seven paragraph breaks',n==7)
(fix/'main.tex').write_bytes(updated)
old=(R/'manuscript/build_manuscript.py').read_bytes()
needle=b"tex.extend([r'\\par\\textit{'+tex_inline(caption)+'}',r'\\begingroup\\small',"
repl=b"tex.extend([r'\\par\\textit{'+tex_inline(caption)+r'}\\par',r'\\begingroup\\small',"
ck('single generator-line repair',old.count(needle)==1)
(fix/'build_manuscript.py').write_bytes(old.replace(needle,repl))
source_fix={p:{'before_sha256':sha((R/'manuscript'/p).read_bytes()),'candidate_sha256':sha((fix/p).read_bytes())} for p in ['main.tex','build_manuscript.py']}
out={'review_type':'document, proof, and retained-data review; no native evaluations', 'python':sys.version,'platform':platform.platform(),'symbolic_replay':{'python':b['python'],'sympy':b['sympy']},'input_archive_sha256':sha(Path('/mnt/data/NCM_PAPER_01_v0.1_REVIEW.zip').read_bytes()),'pdf_sha256':sha(pdf.read_bytes()),'checks':checks,'counts':{'output_members':344,'attempt_records_read':60,'groups':7,'current_symbolic_checks':29,'pdf_pages':19,'internal_citation_links':len(internal),'relative_evidence_links':len(external)},'native_F_evaluations':0,'search_reruns':0,'old_scientific_scripts_executed':0,'live_windows_sources_inspected':False,'source_fix':source_fix}
(ROOT/'REVIEW_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['checks','source_fix']},indent=2))
print('All document/data checks passed:',len(checks))
