"""Named manuscript-local substitutions, not inherited research suites."""
from pathlib import Path
import json,os,re,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
for name in ['TEMP','TMP','XDG_CACHE_HOME']:os.environ[name]=str(ROOT/'cache')
import sympy as s
import numpy as np
rows=[]
def check(name,value,detail):
    ok=bool(value);rows.append({'name':name,'pass':ok,'detail':detail})
def zero(x):
    if isinstance(x,s.MatrixBase):return all(s.simplify(v)==0 for v in x)
    return s.simplify(x)==0
def load(rel):return json.loads((ROOT/'input'/rel).read_text(encoding='utf8'))
g=load('retained_srg02/figures/coordinates.json');om=load('retained_srg03/OBSERVER_MAP.json');sm=load('retained_srg04/SPATIAL_MAP.json')
sq=s.sqrt;c=sq(3)/2;d=1-sq(2)/2;h0=(sq(2)-1)/2;r0=1/sq(3);K=sq(3)/12+sq(6)/4;a=s.simplify(K/(1+c));rad=sq(7)*a/2
O=s.Matrix([0,sq(3)/6,0]);ez=s.Matrix([0,0,1]);us=[s.Matrix([-s.sin(2*s.pi*j/3),s.cos(2*s.pi*j/3),0]) for j in range(3)]
normals=[(2*u+sign*sq(3)*ez)/sq(7) for u in us for sign in [1,-1]]
N=s.Matrix.vstack(*(n.T for n in normals));G=s.diag(s.Rational(12,7),s.Rational(12,7),s.Rational(18,7))
vertices=[s.Matrix([s.sympify(x) for x in row['exact']]) for row in g['vertices']]
check('M01_shell_vertex_ball',all(zero((v-O).dot(v-O)-(s.Rational(13,12)-sq(2)/2)) for v in vertices),'All 18 displayed/source vertices share the stated radius; panel containment uses convexity proof.')
check('M02_contact_barycentrics',all(zero(sum((s.sympify(b)*vertices[i] for b,i in zip(reg['barycentrics'],reg['ids'])),s.zeros(3,1))-s.Matrix([s.sympify(x) for x in reg['contact']['exact']])) for reg in g['regions']),'Six exact retained barycentric identities.')
check('M03_normals_from_vertex_order',all(zero((vertices[reg['ids'][1]]-vertices[reg['ids'][0]]).cross(vertices[reg['ids'][2]]-vertices[reg['ids'][0]])-d*d*s.Matrix([s.sympify(x) for x in reg['normal']['exact']])*sq(7)/2) for reg in g['regions']),'Cross product equals d^2 sqrt(7)/2 times signed normal.')
check('M04_circle_normal_condition',zero(2*(a-K)+sq(3)*a) and zero((a-K)**2+a*a-rad*rad),'Circle centre/radius equations.')
intervals=[(2,'1.41421356237','1.41421356238'),(3,'1.73205080756','1.73205080757'),(6,'2.44948974278','2.44948974279')]
lo=[s.Rational(x) for _,x,_ in intervals];hi=[s.Rational(y) for _,_,y in intervals]
bound=s.Rational(113,6)+s.Rational(13,2)*lo[0]-s.Rational(133,12)*hi[1]-s.Rational(7,2)*hi[2]
check('M05_seam_rational_certificate',all(s.Rational(x)**2<n<s.Rational(y)**2 for n,x,y in intervals) and bound>s.Rational('0.2556109383')>s.Rational(1,4),'Squared endpoint certificates and exact rational lower bound '+str(bound))
nu=s.symbols('nu',real=True);res=a*s.cos(3*nu)*(s.cos(nu)+c)-K
check('M06_grazing_derivatives',zero(res.subs(nu,0)) and zero(s.diff(res,nu).subs(nu,0)) and zero(s.diff(res,nu,2).subs(nu,0)+a*(10+9*c)),'Same contact, zero first normal derivative, negative second derivative.')
phi=s.symbols('phi',real=True);B=s.Matrix([[s.cos(phi),0,s.sin(phi)],[s.sin(phi),0,-s.cos(phi)],[0,1,0]])
check('M07_frame_gram_and_mirror',zero(B.T*B-s.eye(3)) and zero(B.T*s.diag(1,1,-1)*B-s.diag(1,-1,1)),'One symbolic orthonormal frame implies H^T H=12 I; mirror matrix.')
check('M08_patch_gram_and_half',zero(N.T*N-G) and all(zero((n.T*G.inv()*n)[0]-s.Rational(1,2)) for n in normals),'Exact Gram and all six leverage halves.')
x1,x2,x3,y1,y2,y3=s.symbols('x1 x2 x3 y1 y2 y3',real=True);x=s.Matrix([x1,x2,x3]);y=s.Matrix([y1,y2,y3]);C=x.cross(y);I=x.dot(x)+y.dot(y);J=s.Matrix([I,*C]).jacobian([x1,x2,x3,y1,y2,y3]);U=(-y).col_join(x);V=C.cross(x).col_join(C.cross(y))
check('M09_invisible_directions',zero(J*U) and zero(J*V) and zero(U.dot(U)*V.dot(V)-U.dot(V)**2-C.dot(C)*(I**2-4*C.dot(C))),'Symbolic tangent nullspace and Gram determinant identity.')
fixtures={'regular':[1,0,0,0,2,0],'collinear':[1,0,0,0,0,0],'maximal':[1,0,0,0,1,0],'zero':[0]*6};ranks={k:int(J.subs(dict(zip([x1,x2,x3,y1,y2,y3],vals))).rank()) for k,vals in fixtures.items()}
check('M10_rank_strata_fixtures',ranks=={'regular':4,'collinear':3,'maximal':3,'zero':0},ranks)
z=s.Matrix([1,sq(3)/2+s.I/2,1]);zc=[s.simplify(s.im(v[0]*s.conjugate(v[1])*v[2])) for v in [z,-z]]
check('M11_cubic_sign_counterexample',zc==[-s.Rational(1,2),s.Rational(1,2)],'Same quadratic invariants; opposite singleton cubic values.')
e0,e1=s.symbols('e0 e1');D=s.diag(e0,e0,e1,e1,e1,e1);Basis=s.Matrix.hstack(us[0],ez.cross(us[0]),ez);transfer=Basis.T*G.inv()*N.T*D*N*Basis
check('M12_aligned_transfer',zero(transfer-s.diag((2*e0+e1)/3,e1,(e0+2*e1)/3)),'Exact two-phasor transfer.')
Da=s.diag(e0,e1,e0,e1,e0,e1)
check('M13_axial_transfer',zero(G.inv()*N.T*Da*N-(e0+e1)*s.eye(3)/2),'Exact axial cancellation at opposite phasors.')
av=float(a.evalf(25));numerical=[]
for R in [2,3,4]:
    near=np.sqrt((R-av)**2+av**2);far=np.sqrt(R*R+av*R+2*av*av);gain=(5+4*np.cos(np.pi*(far-near)/(2*av)))/9
    numerical.append([R,round(near,6),round(far,6),round(gain,6)])
check('M14_printed_radius_table',numerical==[[2,1.645240,2.267142,.225148],[3,2.625981,3.247376,.225732],[4,3.617283,4.236859,.227840]],numerical)
centres=[tuple(round(v,12) for v in probe['center']['numeric']) for fam in sm['fixtures'].values() for ring in fam for probe in ring['probes']]
check('M15_label_union',len(centres)==96 and len(set(centres))==84,{'labels':len(centres),'distinct_sites':len(set(centres))})
check('M16_clearance_margin',abs(av-float(s.sqrt(s.Rational(13,12)-sq(2)/2))/2-.0988331215339471)<1e-12,'Fixed H inter-ring margin, not an optimization.')
Nn=np.array(N.evalf(),dtype=float);Gn=np.array(G,dtype=float);maxerr=0
for ring in sm['fixtures']['H']+sm['fixtures']['R']:
    for pr in ring['probes']:
        frame=np.array(pr['frame_numeric']);maxerr=max(maxerr,float(np.max(np.abs(frame.T@frame-np.eye(3)))))
check('M17_figure_frame_consistency',maxerr<1e-12,'Retained figure frames orthonormal; max residual '+str(maxerr))
w=np.array(om['figure_fixture']['delta_W_C']['numeric']);errs=[]
for pr,dy in zip(om['geometry']['probes'],om['figure_fixture']['probe_C_differences']):errs.append(np.max(np.abs(np.array(pr['frame_numeric']).T@w-np.array(dy['numeric']))))
check('M18_retained_state_plot',max(errs)<1e-12,'Plotted differences agree with the printed formula, maximum residual '+str(max(errs)))
texts='\n'.join((ROOT/f).read_text(encoding='utf8') for f in ['manuscript.tex','geometry.tex','observation.tex','delay.tex','closing.tex','references.tex'])
labels=re.findall(r'\\label\{([^}]+)\}',texts);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',texts);bibs=re.findall(r'\\bibitem\{([^}]+)\}',texts);cites=[k for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',texts) for k in group.split(',')]
check('M19_label_and_citation_targets',len(labels)==len(set(labels)) and set(refs)<=set(labels) and set(cites)<=set(bibs),{'labels':len(labels),'references':len(refs),'bibliography_items':len(bibs),'unresolved_refs':list(set(refs)-set(labels)),'unresolved_citations':list(set(cites)-set(bibs))})
check('M20_no_model_imports',not any(re.search(r'^\s*(?:from|import)\s+(?:kernel|input|retained|torment)',(ROOT/'tools'/f).read_text(),re.M) for f in ['check_manuscript.py','render_figures.py']),'New check and renderer import only mathematical/plotting and standard libraries.')
check('M21_rendered_command_spelling',not re.search(r'(?<![\\A-Za-z])(sqrt|lambda_s)\b',texts),'Caught and repaired missing backslash at onset radical during page QA; scan final source for bare macro spellings.')
result={'scope':'MANUSCRIPT_LOCAL_ONLY','old_suites_executed':False,'python':sys.version,'sympy':s.__version__,'numpy':np.__version__,'checks':rows,'passed':sum(r['pass'] for r in rows),'total':len(rows)}
(ROOT/'evidence/manuscript_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
for r in rows:print(('PASS' if r['pass'] else 'FAIL'),r['name'])
if not all(r['pass'] for r in rows):raise SystemExit(1)
