"""Document-only transcription/formatting of saved accepted values; no proof replay."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
import sympy as sp
ROOT=Path(__file__).resolve().parents[1];S=ROOT/'evidence/outer_envelope/submitted';V=ROOT/'verification';O=ROOT/'tables';O.mkdir(exist_ok=True);V.mkdir(exist_ok=True)
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
x=sp.Symbol('x');r=sp.sqrt(2)
def poly(rows):return sum((sp.Rational(a)+sp.Rational(b)*r)*x**i for i,(a,b) in enumerate(rows))
def tex(value):return sp.latex(value).replace('\\sqrt{2}','r')
def cycle(labels):return ', '.join('\\br{'+s+'}' for s in labels)
check=read(S/'data/CHECKER_RESULT.json');cert=read(S/'data/exact_certificate.json');rep=read(S/'data/FACE_REPRESENTATIVES.json');tr=read(S/'data/TRANSITION_READOUT.json')
main=(ROOT/'main.tex').read_text(encoding='utf-8');records=[]
rows=[]
for key,label,expected in [('A','$A$ (inherited)',(18,48,32)),('C1','$A<x<\\xs$',(42,96,56)),('T','$x=\\xs$',(42,84,44)),('C2','$\\xs<x<B$',(42,90,50)),('B','$B$ (inherited)',(18,36,20))]:
    data=check['endpoints'][key] if key in ['A','B'] else check['domains'][key]
    assert tuple(data[z] for z in ['V','E','F'])==expected
    hist={int(k):v for k,v in data['face_histogram'].items()};phrases=[str(hist[k])+' '+{3:'triangles',4:'quadrilaterals',6:'hexagons'}[k] for k in sorted(hist)]
    rows.append(label+' & '+' & '.join(str(data[z]) for z in ['V','E','F'])+' & '+', '.join(phrases)+r' \\')
    records.append({'type':'classification','domain':key,'VEF':expected,'histogram':hist})
(O/'classification.tex').write_text('\\begin{table}[h]\\centering\\small\n\\caption{Complete closed A--B classification. Edges are true polygon sides; facets are maximal supporting polygons.}\\label{tab:classification}\n\\begin{tabularx}{\\linewidth}{@{}lrrrX@{}}\\toprule\nParameter & V & E & F & Facet sizes\\\\\\midrule\n'+'\n'.join(rows)+'\n\\bottomrule\\end{tabularx}\n\\src{Accepted proof, Section 3, full incidence records and GPT review, Section 1~\\cite{investigation,review}.}\n\\end{table}\n',encoding='utf-8')
reslines=[];sourcevalues=check['candidate']['residuals_at_transition_divided_by_sqrt3'];covered=[]
for line in (S/'data/CANDIDATE_RESIDUAL_TABLE.md').read_text(encoding='utf-8').splitlines():
    if not line.startswith('| `'):continue
    value,labels=[s.strip() for s in line.split('|')[1:3]];expr=sp.sympify(value.strip('`'));labels=labels.split(', ')
    for label in labels:assert sp.expand(expr-poly([sourcevalues[label]]))==0
    covered+=labels;reslines.append('$'+sp.latex(expr)+'$ & '+cycle(labels)+r' \\')
assert sorted(covered)==sorted(cert['points']) and len(reslines)==13
(O/'residuals.tex').write_text('\\begin{table}[h]\\centering\\small\n\\caption{Complete residual classes at $\\xs$. Values are $(n_*\\cdot p-d_*)/\\sqrt3$; every nonzero row is strictly negative.}\\label{tab:residuals}\n\\begin{tabular}{@{}ll@{}}\\toprule\nExact residual & Branch labels\\\\\\midrule\n'+'\n'.join(reslines)+'\n\\bottomrule\\end{tabular}\n\\src{Accepted candidate residual table~\\cite{investigation}. For example, $(7-5\\sqrt2)/2<0$ because $49<50$.}\n\\end{table}\n',encoding='utf-8')
patch=next(p for p in tr['six_local_changes'] if p['transition_face']==check['candidate']['transition_facet_id']);patchrows=[]
for domain,text in [('C1','$A<x<\\xs$'),('C2','$\\xs<x<B$')]:
    for f in patch[domain]:patchrows.append(text+' & '+str(f['polygon_size'])+' & '+cycle(f['cycle'])+r' \\')
assert patch['transition_cycle']==['E05+','E16-','E21+','E09+','E17+','E10-']
(O/'patch.tex').write_text('\\begin{table}[h]\\centering\\small\n\\caption{The exact cycles adjacent to the representative hexagon.}\\label{tab:patch}\n\\begin{tabular}{@{}lcl@{}}\\toprule\nDomain & Size & Outward cycle\\\\\\midrule\n'+'\n'.join(patchrows)+'\n\\bottomrule\\end{tabular}\n\\src{Accepted transition readout, patch T/F30~\\cite{investigation}.}\n\\end{table}\n',encoding='utf-8')
assert tr['unchanged_full_facets_across_transition']==38 and len(tr['six_local_changes'])==6 and len(tr['edges_lost_from_C1'])==12 and len(tr['edges_gained_in_C2'])==6
limits=tr['limit_image_dimension_histograms'];assert [limits['C1->A'][str(k)] for k in [2,1,0]]==[32,18,6] and [limits['C2->B'][str(k)] for k in [2,1,0]]==[20,24,6]
(O/'limits.tex').write_text(r'''\begin{table}[h]\centering
\caption{Images of the chamber facets at the inherited endpoints.}\label{tab:limits}
\begin{tabular}{@{}lrrr@{}}\toprule
Limit & Facet images & Edge images & Point images\\\midrule
C1 $\to A$ & 32 & 18 & 6\\
C2 $\to B$ & 20 & 24 & 6\\\bottomrule
\end{tabular}
\src{Accepted limit maps and review, Section 3.5~\cite{investigation,review}.}
\end{table}
''',encoding='utf-8')
for domain,filename,title in [('C1','orbits_c1.tex','First open chamber: $A<x<\\xs$'),('T','orbits_star.tex','Transition: $x=\\xs$'),('C2','orbits_c2.tex','Second open chamber: $\\xs<x<B$')]:
    bookmark={'C1':'First open chamber: A < x < x*','T':'Transition: x = x*','C2':'Second open chamber: x* < x < B'}[domain]
    output=['\\subsection{\\texorpdfstring{'+title+'}{'+bookmark+'}}\\label{app:'+domain+'}',r'\begingroup\small\renewcommand{\arraystretch}{1.03}',r'\begin{longtable}{@{}p{16mm}p{146mm}@{}}','\\caption{Exact outward planes and full zero cycles for '+domain+'. Here $r=\\sqrt2$; coordinates are $(X,Y,Z)$.}\\label{tab:orbits-'+domain+'}\\\\',r'\toprule Rep. & Plane $n\cdot(X,Y,Z)\le d$ and cyclic zero set\\\midrule\endfirsthead',r'\toprule Rep. & Plane and cyclic zero set (continued)\\\midrule\endhead',r'\bottomrule\endfoot']
    these=[v for v in rep['records'] if v['domain']==domain];assert len(these)==(8 if domain=='T' else 9)
    dom=next(d for d in cert['domains'] if d['id']==domain)
    for row in these:
        polynomials=[*row['normal_polynomials'],row['offset_polynomial']];expressions=[sp.sympify(s,locals={'x':x}) for s in row['display_formulas']]
        assert all(sp.expand(e-poly(p))==0 for e,p in zip(expressions,polynomials))
        face=next(f for f in dom['faces'] if f['id']==row['representative']);orbit=next(o for o in dom['D3h_face_orbits'] if o['representative']==row['representative'])
        assert row['cycle']==face['cycle'] and row['orbit_size']==orbit['size']
        math='n&=\\bigl('+','.join(tex(e) for e in expressions[:3])+r'\bigr),\\d&='+tex(expressions[3])+'.'
        output.append('\\rep{'+row['representative']+'}{'+str(row['orbit_size'])+'}{'+math+'}{'+cycle(row['cycle'])+'}')
        records.append({'type':'orbit','domain':domain,'id':row['representative'],'size':row['orbit_size'],'cycle':row['cycle'],'source_display_formulas':row['display_formulas'],'printed_math':math,'raw_coefficients_match':True})
    output+=['\\end{longtable}\\endgroup',r'\src{Saved exact representative records and full certificate~\cite{investigation}; no plane or orbit was regenerated for this manuscript.}']
    (O/filename).write_text('\n'.join(output)+'\n',encoding='utf-8')
for table in O.glob('*.tex'):
    content=table.read_text(encoding='utf-8')
    if '\\begin{table}' in content:
        content=content.replace('\\begin{table}', '\\par\n\\begin{table}').replace('\\end{table}', '\\end{table}\\par')
        table.write_text(content,encoding='utf-8')
# Compare manuscript formulas with their saved polynomial records, not with a rerun of geometry.
h=(r-1)/2;physical=[0,-1,sp.sqrt(3)*(x-h)/2];saved=[poly(p) for p in check['candidate']['plane_normal_transformed_divided_by_sqrt3']]
assert all(sp.expand(a-b)==0 for a,b in zip(physical,[sp.sqrt(3)*saved[0],saved[1],sp.sqrt(3)*saved[2]]))
printed_d=sp.sqrt(6)*x*x/4+(sp.sqrt(6)-sp.sqrt(3))*x/4+sp.sqrt(3)/24+sp.sqrt(6)/16
assert sp.expand(printed_d-sp.sqrt(3)*poly(check['candidate']['plane_offset_divided_by_sqrt3']))==0
assert cert['transition']['parameter']==['-3/2','3/2'] and cert['transition']['minimal_polynomial_integer_coefficients_ascending']==[-9,12,4] and cert['transition']['radius_squared']==['85/12','-9/2']
factor=-r*(x-3*(r-1)/2)*(x-(1+r)/2)/4;assert sp.expand(factor-poly(check['candidate']['two_nonpersistent_residual_factor']))==0
assert all(t in main for t in [r'\frac{85}{12}-\frac{9\sqrt2}{2}',r'4\xs^2+12\xs-9=0',r'-\frac{\sqrt6}{4}(x-\xs)(x-B)',r'\frac{3(\sqrt2-1)}2'])
orig=check['accounting'];review=read(ROOT/'evidence/outer_envelope/reviewer/INDEPENDENT_EXACT_CHECK.json')
assert [review[k] for k in ['support_residual_checks','polygon_side_checks','distinct_sign_proofs','max_bernstein_leaves']]==[6300,972,255,1]
assert orig['residual_sign_checks']==6300 and orig['polygon_side_checks']==972 and orig['distinct_monic_sign_forms_by_domain']==254
fig=ROOT/'figures';fig.mkdir(exist_ok=True)
for ext in ['png','svg']:shutil.copyfile(S/('figures/local_facet_transition.'+ext),fig/('local_facet_transition.'+ext));assert sha(fig/('local_facet_transition.'+ext))==sha(S/('figures/local_facet_transition.'+ext))
receipt={'status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'scope':'Saved-data transcription and expression formatting only; no geometry, root, sign-proof, hull, scientific checker or reviewer code executed.','sympy_use':'Parse saved exact expression strings, compare their coefficients with saved arrays, and emit LaTeX. No scientific engine imported.','sympy_version':sp.__version__,'records':records,'residual_classes':13,'residual_labels':42,'patch_cycle_rows':len(patchrows),'transition_counts':{'six_patches':6,'persistent_label_sets':38,'lost_edges':12,'gained_edges':6},'endpoint_images':[[32,18,6],[20,24,6]],'historical_submitted_counts':[6300,972,254],'historical_reviewer_counts':[6300,972,255],'printed_formulas_match_saved_values':True,'new_scientific_runs':0,'source_hashes':{p.relative_to(ROOT).as_posix():sha(p) for p in [S/'data/exact_certificate.json',S/'data/FACE_REPRESENTATIVES.json',S/'data/CHECKER_RESULT.json',S/'data/TRANSITION_READOUT.json',S/'data/CANDIDATE_RESIDUAL_TABLE.md']},'generated_table_hashes':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(O.glob('*.tex'))}}
(V/'TRANSCRIPTION_CHECK.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('PASS document transcription: five domains, 13 residual classes, 26 plane/orbit rows; no scientific replay.')
