from pathlib import Path
import json,re,sys
from ledger_typesetting import STATEMENTS
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parents[1]
def esc(s):
 return ''.join({'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}','→':r'$\to$','±':r'$\pm$','†':r'$\dagger$','–':'--','—':'---','§':r'\S{}'}.get(c,c) for c in str(s))
def ordinals(values):
 nums=sorted(values); groups=[]
 for n in nums:
  if groups and n==groups[-1][-1]+1:groups[-1].append(n)
  else:groups.append([n])
 return ', '.join(str(g[0]) if len(g)==1 else str(g[0])+'--'+str(g[-1]) for g in groups)
d=json.loads((P/'provenance/theorem_ledger.json').read_text(encoding='utf-8'))
pred=json.loads((P/'verification/retained_predicates.json').read_text(encoding='utf-8'))['predicates']
for r in d['records']:
 assert r['manuscript_proof_label'].startswith('sec:')
 if 'predicate_search' in r:
  pat=r.pop('predicate_search');r['supporting_verification_predicates']=[x for x in pred.get(r['checkpoint'],[]) if pat and re.search(pat,x['name'],re.I)]
 if not r['supporting_verification_predicates']:r.setdefault('verification_note','Written proof/source statement is authority; no individually matched predicate claimed.')
 elif 'verification_note' in r:del r['verification_note']
(P/'provenance/theorem_ledger.json').write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
md=['# Theorem and claim ledger','',d['stage'],'','45 records classify results, definitions, limits and questions, not 45 new theorems. Retained total: 429 heterogeneous checks, not 429 theorems.','']
tex=[r'\section{Complete theorem and claim ledger}\label{app:ledger}',r'This is the anti-overstatement ledger. Predicate ordinals resolve to the named lists in \texttt{verification/retained\_predicates.json}; checks do not replace proof locations.\par',r'\begingroup\footnotesize\raggedright']
cw=['# Paper-source-proof crosswalk','','| Ledger | Manuscript proof anchor | Exact source locator | Prior ownership |','|---|---|---|---|']
for r in d['records']:
 md+=['## '+r['id']+' — '+r['name'],'']
 for k,v in r.items():
  if k in ('id','name'):continue
  if k=='supporting_verification_predicates':v='; '.join(str(x['ordinal'])+': '+x['name'] for x in v) or 'Analytic proof/source statement; no individually matched predicate claimed.'
  md+=['**'+k.replace('_',' ').capitalize()+':** '+str(v),'']
 tex += [r'\par\noindent\begin{minipage}{\linewidth}',r'\subsection*{'+esc(r['id']+' '+r['name'])+'}',r'\textbf{'+esc(r['classification'])+'}. '+STATEMENTS.get(r['id'],esc(r['statement']))+r'\par',
  r'\textbf{Domain:} '+esc(r['hypotheses'])+r'\par',r'\textbf{Authority/proof:} '+esc(r['checkpoint']+' '+r['source_section_equation'])+r'; main text \S\ref{'+r['manuscript_proof_label']+r'}.\par',
  r'\textbf{Prior ownership:} '+esc(r['known_before_GR0'])+r'\par',r'\textbf{Qualification:} '+esc(r['qualifications'])+r'\par',r'\textbf{Interpretation limit:} '+esc(r['interpretation_limit'])+r'\par',
  r'\textbf{Supporting predicates:} '+esc(r['checkpoint']+' ordinals '+ordinals(x['ordinal'] for x in r['supporting_verification_predicates']) if r['supporting_verification_predicates'] else 'Analytic proof/source statement; no individually matched predicate claimed.')+r'\par',r'\end{minipage}\par\medskip']
 cw+=['| '+r['id']+' '+r['name']+' | '+r['manuscript_proof_label']+' | '+r['checkpoint']+' '+r['source_section_equation']+' | '+r['known_before_GR0']+' |']
tex += [r'\endgroup']
(P/'provenance/THEOREM_LEDGER.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
(P/'provenance/PAPER_SOURCE_CROSSWALK.md').write_text('\n'.join(cw)+'\n',encoding='utf-8')
(P/'manuscript/ledger.tex').write_text('\n'.join(tex)+'\n',encoding='utf-8')
print('Ledger validated and rendered:',len(d['records']))
