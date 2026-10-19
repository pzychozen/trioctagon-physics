"""Bounded checks of displayed identities and inherited transcription. No old suite/import/evolution."""
from pathlib import Path
import os,json,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
for k in ['TEMP','TMP','XDG_CACHE_HOME']:os.environ[k]=str(ROOT/'cache')
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sympy as s
import numpy as np
def read(n):return json.loads((ROOT/n).read_text(encoding='utf8'))
rows=[]
def ck(n,b,d):rows.append({'name':n,'pass':bool(b),'detail':d})
def zero(x):return all(s.simplify(t)==0 for t in x) if isinstance(x,s.MatrixBase) else s.simplify(s.expand_complex(x))==0
sq=s.sqrt;I=s.I
K=sq(3)/12+sq(6)/4;a=K/(1+sq(3)/2);R=sq(7)*a/2
cg=sq(s.Rational(3,7));sg=2/sq(7)
ck('M01_contact_quadrants_and_tangent',zero(K-R*cg-a) and zero(R*sg-a) and zero(cg**2+sg**2-1),'Actual negative cosine, positive/negative sine; no antipodal replacement.')
ck('M02_contact_trace_and_determinant',zero(2*(cg**2-sg**2)+s.Rational(2,7)) and zero(2*sg*cg-4*sq(3)/7),'Rational trace and sin(2 theta) used in the proof.')
eps=s.symbols('eps',positive=True);x=s.symbols('x',real=True);tent=(1-x/eps)/eps
ck('M03_finite_tent_norms',zero(2*s.integrate(tent,(x,0,eps))-1) and zero(2*s.integrate(tent**2,(x,0,eps))-2/(3*eps)) and zero(2*eps/eps**4-2/eps**3),'Closed-form norms, no numerical quadrature.')
p,r,c,gs=s.symbols('p r c g',real=True);ps,rs=s.symbols('p_s r_s',real=True)
ck('M04_local_work_sign',zero(p*(gs-c*rs)+r*(-c*ps)+c*(ps*r+p*rs)-p*gs),'Independent product-rule substitution in local account.')
wp=(p+r)/sq(2);wm=(p-r)/sq(2)
ck('M05_characteristic_normalization',zero((wp**2+wm**2)/2-(p**2+r**2)/2) and zero(c*(wp**2-wm**2)/2-c*p*r),'Normalized/unnormalized conversion and account factors.')
om,k,g=s.symbols('omega k g',real=True);vec=s.Matrix([I*om*g,-I*c*k*g])/(c*c*k*k-om*om)
ck('M06_modal_resolvent',zero(I*s.Matrix([[om,c*k],[c*k,om]])*vec-s.Matrix([g,0])),'Nonresonant matrix inversion; excluded denominator kept.')
A,B=s.symbols('A B',real=True);tap=s.Matrix([[-I*s.cos(A-B),0],[0,s.sin(A-B)],[-I*s.cos(B),0],[0,-s.sin(B)]])
half=tap.subs(A,s.pi/2)
ck('M07_two_tap_half_frequency_Gram',zero(half.conjugate().T*half-s.eye(2)),'Both source columns, without sampling frequencies.')
H,Sm,Cm=s.symbols('H Sm Cm',complex=True);ph=s.symbols('phi',real=True);Q=s.Matrix([[H*s.exp(-I*ph),H*s.exp(I*ph)],[I*Sm*s.exp(-I*ph),I*Sm*s.exp(I*ph)],[Cm*s.exp(-I*ph),-Cm*s.exp(I*ph)]])
U=s.Matrix([[s.exp(I*ph),s.exp(I*ph)],[s.exp(-I*ph),-s.exp(-I*ph)]])/sq(2)
diag=s.diag(2*(H*s.conjugate(H)+Sm*s.conjugate(Sm)),2*Cm*s.conjugate(Cm))
ck('M08_complex_transfer_singular_values',zero((Q*U).conjugate().T*(Q*U)-diag),'Complex moments retained; second vector column sign tested.')
ck('M09_height_minor',zero(s.det(s.Matrix([[H*s.exp(-I*ph),H*s.exp(I*ph)],[H*s.exp(I*ph),H*s.exp(-I*ph)]]))+2*I*H**2*s.sin(2*ph)),'Mirror row ordering and signed determinant.')
controls=[s.Matrix([1/sq(2),0]),s.Matrix([0,1/sq(2)]),s.Matrix([s.exp(I*s.pi/4)/2,s.exp(-I*s.pi/4)/2])]
ck('M10_shifted_standing_scalar_collision',all(zero(sum(v)-1/sq(2)) for v in controls) and all(zero((v.conjugate().T*v)[0]-s.Rational(1,2)) for v in controls),'Equal storage and exact common scalar sum.')
bb=s.symbols('b',positive=True);fs,fa=s.symbols('Fs Fa',real=True)
N=bb*s.Matrix([[cg,-I*sg],[cg,I*sg]])/2
ck('M11_source_map_and_static_mean',zero(s.det(N)-I*bb**2*cg*sg/2) and zero((N.conjugate().T*N)[0,1]),'Invertible source map; sector cross term cancels globally only.')
tr=s.symbols('t',real=True);h=(1-s.cos(tr))/2
mom={n:s.simplify(s.integrate(s.expand_trig(h)*s.exp(I*n*tr),(tr,0,2*s.pi))) for n in [0,1,2]}
ck('M12_pulse_exceptional_moments',mom=={0:s.pi,1:-s.pi/2,2:0},'Three manuscript transcription checks only; all-integer proof is written.')
Emean=fs**2/2;Eh=bb**2*(cg**2*fs**2+sg**2*fa**2)/4
fp,fm=s.symbols('Fu Fl',real=True);as_=s.Rational(1,2)+3*bb**2/28;aa=bb**2/7
ck('M13_port_work_cross_term',zero((Emean+Eh).subs({fs:(fp+fm)/2,fa:(fp-fm)/2})-((as_+aa)*(fp**2+fm**2)+2*(as_-aa)*fp*fm)/4),'No independent-port work assumption.')
ck('M14_antisymmetric_endpoint_sign',zero((-2*bb**2*sg**2)+8*bb**2/7) and bool(8*s.Rational(1,7)>0),'Negative limiting trace; continuity supplies the interval proof.')
ur,ui,vr,vi,th=s.symbols('ur ui vr vi theta',real=True);fu=ur+I*ui;fl=vr+I*vi
ap=s.exp(-I*th)*s.conjugate(fu)+s.exp(I*th)*s.conjugate(fl);am=s.exp(I*th)*s.conjugate(fu)+s.exp(-I*th)*s.conjugate(fl)
ck('M15_temporal_cross_phase_sign',zero(ap*s.conjugate(ap)-am*s.conjugate(am)+4*s.sin(2*th)*s.im(fu*s.conjugate(fl))),'Independent four-real-variable amplitude expansion.')
ck('M16_reference_origin_conversion',zero(s.exp(I*2*s.pi*(s.Rational(3,2)-1))+1),'T to 3T/2 gives minus, never per-control rephasing.')
ratio=(cg-sg)/(cg+sg)
ck('M17_quarter_weaker_direction',zero(ratio-(4*sq(3)-7)) and ratio!=0,'Retains nonzero weaker direction.')
dt,w=s.symbols('dt w',positive=True);u0,u1,l0,l1=s.symbols('u0 u1 l0 l1',real=True)
cross=(u0+u1*s.exp(I*w*dt))*(l0+l1*s.exp(-I*w*dt))
ck('M18_two_row_hold_sign',zero(s.im(cross)+(u0*l1-u1*l0)*s.sin(w*dt)),'Symbolic cadence retained; no held native trajectory generated.')
z0=s.Matrix([1,1+I,2]);nextz=s.Matrix([z0[j]+s.Rational(1,20)*z0[j]*(1-z0[j]*s.conjugate(z0[j]))+s.Rational(1,5)*sum(z0[m]-z0[j] for m in range(3) if m!=j) for j in range(3)])
expected=s.Matrix([s.Rational(6,5)+I/5,s.Rational(23,20)+11*I/20,s.Rational(13,10)+I/5]);c0=s.re(z0).cross(s.im(z0));c1=s.re(nextz).cross(s.im(nextz))
ck('M19_single_displayed_polynomial_substitution',zero(nextz-expected) and c0==s.Matrix([-2,0,1]) and c1==s.Matrix([-s.Rational(97,200),s.Rational(1,50),s.Rational(43,100)]),'One exact displayed substitution only, no source import, iteration or second successor.')
ell=s.symbols('ell',real=True);wr0=s.cos(ell)*c0[0]+s.sin(ell)*c0[1];wr1=s.cos(ell)*c1[0]+s.sin(ell)*c1[1]
ck('M20_native_chiral_determinant',zero(wr0*c1[2]-c0[2]*wr1+3*s.cos(ell)/8+s.sin(ell)/50),'Source-defined C determinant with unchanged registration.')
d=read('data/exterior_response.json');sp=read('data/spatial.json');sites=[tuple(round(x,12) for x in p['center']['numeric']) for rings in sp['fixtures'].values() for ring in rings for p in ring['probes']]
ck('M21_array_aliases',len(sites)==96 and len(set(sites))==84 and len(d['sites'])==84,'Complete admitted H/R geometry, no Cartesian product.')
stacks={'H+2':(.00946563,.05460398,.21704541,.19008006),'H+1':(.00521440,.02915133,.22368205,.18961117),'H0':(0,0,.22604866,.18924224),'R1':(0,0,.35548794,.30194822),'R3':(0,0,.16712416,.13941997),'H':(.01927634,.09275635,.49542995,.42564193),'R':(0,0,.45321095,.38265295),'H_union_R_unique':(.01927634,.09275635,.63226023,.54016822)}
err=0
for name,vals in stacks.items():
 got=[d['ring_and_array_results'][str(nu)][name][key][-1] for key in ['scalar_singular_values','full_singular_values'] for nu in [0,1]]
 err=max(err,max(abs(x-y) for x,y in zip(got,vals)))
ck('M22_exterior_table_transcription',err<5.1e-9,{'max_rounding_difference':err,'old_quadrature_rerun':False})
t=read('data/timing_response.json');b=float(s.sinc(s.pi/32)**2);vals=[]
for key,alpha in [('CO',0),('LOWER_LATE_Q',np.pi/2),('LOWER_LATE_H',np.pi)]:
 row=t['controls'][key];theta=float(s.atan(2/sq(3)));ep=b*b/16*(1+np.cos(2*theta-alpha));em=b*b/16*(1+np.cos(2*theta+alpha));vals.extend([abs(row['E_plus']-ep),abs(row['E_minus']-em),abs(row['E_total']-(.5+ep+em))])
ck('M23_fixed_timing_table_and_mean',max(vals)<1e-14 and t['controls']['ZERO']['imbalance_osc'] is None,{'max_difference':max(vals),'zero_ratio_undefined':True})
pt=read('data/pulse_plot.json');tt=read('data/timing_plot.json');ck('M24_figure_storage_data',np.allclose(np.array(pt['storage_mean'])+np.array(pt['storage_harmonic']),pt['storage_total'],rtol=0,atol=1e-15) and np.allclose(np.sum(tt['storage_rows'],axis=1),[t['controls'][n]['E_total'] for n in tt['control_order']],rtol=0,atol=1e-15),'Only transcribes retained plotted data; common scales.')
texts='\n'.join(q.read_text(encoding='utf8') for q in ROOT.glob('*.tex'));labels=re.findall(r'\\label\{([^}]+)\}',texts);refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',texts);bibs=re.findall(r'\\bibitem\{([^}]+)\}',texts);cites=[k for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',texts) for k in group.split(',')]
ck('M25_label_citation_and_text_closure',len(labels)==len(set(labels)) and set(refs)<=set(labels) and set(cites)<=set(bibs) and not any(ord(c)<32 and c not in '\n\r' for c in texts),{'labels':len(labels),'bibliography':len(bibs),'unresolved':list(set(refs)-set(labels))})
deps=re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',texts);ck('M26_figure_dependency_boundary',len(deps)==5 and all((ROOT/p).exists() for p in deps) and not re.search(r'(?i)[A-Z]:[/\\]+Users[/\\]|rough sketch|awaiting GPT',texts),'Five computed figure PDFs; no private image or personal-account source path.')
result={'scope':'MANUSCRIPT_LOCAL_ONLY','old_suites_executed':False,'quadrature':False,'model_execution':False,'checks':rows,'passed':sum(x['pass'] for x in rows),'total':len(rows),'python':sys.version,'sympy':s.__version__,'numpy':np.__version__}
n=len(list((ROOT/'evidence').glob('manuscript_checks_*.json')))+1
(ROOT/'evidence'/f'manuscript_checks_{n:03d}.json').write_text(json.dumps(result,indent=2),encoding='utf8');(ROOT/'evidence/manuscript_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
for row in rows:print('PASS' if row['pass'] else 'FAIL',row['name'])
if not all(row['pass'] for row in rows):raise SystemExit(1)
