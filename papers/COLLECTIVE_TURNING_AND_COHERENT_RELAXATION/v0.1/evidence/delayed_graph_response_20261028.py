"""Exact rational polynomial check for the requested phase-off graph response.

Only the specified entrance, epsilon and k are used. g is a formal real
indeterminate; numerical substitution is limited to 0 and 1/60. No project
modules, floating arithmetic, interval replay, trajectory sweep or solver.
All repository access is read-only; this file and its receipt live outside it.
"""
from fractions import Fraction as Q
from pathlib import Path
import sys, json, hashlib, subprocess
sys.dont_write_bytecode=True
sys.stdout.reconfigure(encoding='utf-8')
REPO=Path('C:/TORMENT/TRIOCTAGON_new/trioctagon-physics')
PIN='ad8a6e88b4a78d8b1955b34d5ff80b6c21713ade'
OUT=Path(__file__).with_suffix('.json')
assert not OUT.is_relative_to(REPO)
Z=(Q(0),Q(0))
def c(x=0,y=0):return Q(x),Q(y)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def conj(a):return a[0],-a[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,s):return a[0]*s,a[1]*s
def sq(a):return a[0]**2+a[1]**2
def csum(v):
    out=Z
    for x in v:out=add(out,x)
    return out
def mean(v):return scale(csum(v),Q(1,3))
def cross(a,b):return mul(conj(a),b)[1]
def dot(a,b):return mul(conj(a),b)[0]
def ptrim(p):
    while len(p)>1 and p[-1]==Z:p.pop()
    return p
def padd(a,b):return ptrim([add(a[i] if i<len(a) else Z,b[i] if i<len(b) else Z) for i in range(max(len(a),len(b)))])
def pscale(a,s):return ptrim([scale(x,s) for x in a])
def pmul(a,b):
    out=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=add(out[i+j],mul(x,y))
    return ptrim(out)
def pconj(a):return [conj(x) for x in a]
def peval(a,g):
    out=Z
    for x in reversed(a):out=add(scale(out,g),x)
    return out
def psum(v):
    out=[Z]
    for x in v:out=padd(out,x)
    return out
def pmean(v):return pscale(psum(v),Q(1,3))

eps=Q(1,10);k=[Q(999,1000),Q(1),Q(1001,1000)];gs=Q(1,60)
initial=[c(1,1),c(1,1),c(1,-2)]
def f(z,ki):return scale(z,ki-sq(z))
def L(z):
    total=csum(z)
    return [sub(total,scale(x,3)) for x in z]
def advance(z,g):return [add(add(x,scale(f(x,ki),eps)),scale(dx,g)) for x,ki,dx in zip(z,k,L(z))]
def formal_advance(z):
    total=psum(z);out=[]
    for zi,ki in zip(z,k):
        nonlinear=pmul(pmul(zi,pconj(zi)),zi)
        onsite=padd(pscale(zi,ki),pscale(nonlinear,-1))
        graph=padd(total,pscale(zi,-3))
        out.append(padd(padd(zi,pscale(onsite,eps)),[Z]+graph))
    return out
def git(*args):return subprocess.run(['git',*args],cwd=REPO,capture_output=True,check=True).stdout
before=git('--no-optional-locks','status','--porcelain=v1','--untracked-files=all')
assert git('rev-parse','HEAD').decode().strip()==PIN
branch_before=git('branch','--show-current')

a=[add(z,scale(f(z,ki),eps)) for z,ki in zip(initial,k)]
d=L(initial);assert csum(d)==Z
c_i=[dot(ai,di) for ai,di in zip(a,d)]
Plinear=scale(csum([scale(di,ki) for di,ki in zip(d,k)]),eps/3)
Pcubic1=scale(csum([add(scale(di,sq(ai)),scale(ai,2*ci)) for ai,di,ci in zip(a,d,c_i)]),-eps/3)
P1=add(Plinear,Pcubic1)
P2=scale(csum([add(scale(di,2*ci),scale(ai,sq(di))) for ai,di,ci in zip(a,d,c_i)]),-eps/3)
P3=scale(csum([scale(di,sq(di)) for di in d]),-eps/3)
P=[P1,P2,P3]
# Independent formal-polynomial propagation of the original full phase-off map.
formal1=formal_advance([[z] for z in initial]);formal2=formal_advance(formal1)
assert formal1==[[ai,di] for ai,di in zip(a,d)]
assert pmean(formal1)==[mean(a)]
mpoly=pmean(formal2)
assert len(mpoly)==4 and mpoly[1:]==P
state20=advance(a,Q(0));m0=mean(initial);m1=mean(a);m20=mean(state20)
assert mpoly[0]==m20
s=sub(m1,m0);t0=sub(m20,m1)
Jcoeff=[cross(s,p) for p in P];Rcoeff=[cross(t0,p) for p in P]
Qcoeff=[dot(t0,p) for p in P]
star1=advance(initial,gs);star2=advance(star1,gs)
assert mean(star1)==m1
tg=sub(mean(star2),m1);D=sub(mean(star2),m20)
assert D==peval([Z]+P,gs)
Dlin=scale(Plinear,gs);Dcubic=sub(D,Dlin)
assert Dcubic==scale(csum([sub(scale(x,sq(x)),scale(ai,sq(ai))) for x,ai in zip(star1,a)]),-eps/3)
K0=cross(s,t0);Kg=cross(s,tg);J=Kg-K0;R=cross(t0,tg);inner=dot(t0,tg)
assert Kg==Q(3158587023292997,300000000000000000)
assert J==cross(s,D)==sum(q*gs**(i+1) for i,q in enumerate(Jcoeff))
assert R==cross(t0,D)==sum(q*gs**(i+1) for i,q in enumerate(Rcoeff))
assert inner==sq(t0)+sum(q*gs**(i+1) for i,q in enumerate(Qcoeff))
assert K0>Kg>0 and J<0 and R>0 and inner>0
assert sq(s)>0 and sq(t0)>0 and sq(tg)>0
assert Plinear!=Z and Pcubic1!=Z and P1!=Z and Jcoeff[0]!=0 and Rcoeff[0]!=0

def dec(q,places=14):
    # Rounded display only; every proof comparison above uses exact fractions.
    den=10**places;n=(abs(q.numerator)*den*2+q.denominator)//(2*q.denominator)
    text=str(n).zfill(places+1)
    return ('-' if q<0 else '')+text[:-places]+'.'+text[-places:]
def qr(q):return {'exact':str(q),'decimal_display':dec(q)}
def cr(z):return {'real':qr(z[0]),'imag':qr(z[1])}
source_paths=['kernel_physics/dynamics.py','papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/manuscript.tex','papers/PAPER_G/v0.1.1/source/paper_g.tex','SRG_REDISCOVERY/FINAL_MATHEMATICAL_BRIDGE/publication/v0.1/SRG_FINAL_MATHEMATICAL_BRIDGE_v0.1.md']
sources=[]
for path in source_paths:
    raw=git('show',PIN+':'+path);assert (REPO/path).read_bytes()==raw
    sources.append({'path':path,'sha256':hashlib.sha256(raw).hexdigest(),'commit':PIN})
assert git('--no-optional-locks','status','--porcelain=v1','--untracked-files=all')==before
assert git('branch','--show-current')==branch_before
assert git('rev-parse','HEAD').decode().strip()==PIN
result={
 'result':'PASS','scope':'lambda=0; formal real g; fixed entrance, epsilon and k; exact comparison at 0 and 1/60',
 'epsilon':str(eps),'k':list(map(str,k)),'g_star':str(gs),'lambda':'0',
 'initial':[cr(z) for z in initial],'a':[cr(z) for z in a],'d':[cr(z) for z in d],
 'P':[cr(z) for z in P],'P1_linear':cr(Plinear),'P1_cubic':cr(Pcubic1),
 's':cr(s),'t0':cr(t0),'t_star':cr(tg),
 'D_star':cr(D),'D_linear_star':cr(Dlin),'D_cubic_star':cr(Dcubic),
 'J_coefficients':[qr(q) for q in Jcoeff],'R_coefficients':[qr(q) for q in Rcoeff],
 'direction_dot_coefficients':[qr(q) for q in Qcoeff],
 'K0':qr(K0),'K_star':qr(Kg),'J_star':qr(J),'R_star':qr(R),'direction_dot_star':qr(inner),'tan_angle_difference':qr(R/inner),
 'signs':{'K0_positive':K0>0,'K_star_positive':Kg>0,'turn_statistic_reduced':J<0,'counterclockwise_direction_change':R>0,'acute_direction_change':inner>0},
 'verification':{'original_map_formal_polynomial_matches_derived_coefficients':True,'matched_point_direct_rational_map_matches_response':True,'previous_phase_off_K_consistency':True,'all_signs_exact_rational':True,'only_point_substitutions':['0','1/60'],'previous_interval_certification_repeated':False,'repository_contents_written':False,'repository_git_status_unchanged':True,'branch_and_commit_unchanged':True},
 'sources':sources,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:result[key] for key in ('P','P1_linear','P1_cubic','s','t0','t_star','D_star','D_linear_star','D_cubic_star','J_coefficients','R_coefficients','K0','K_star','J_star','R_star','direction_dot_star','tan_angle_difference','signs')},indent=2))
print('PASS: exact original-map polynomial and fixed comparison verified; repository unchanged.')
print('Receipt:',OUT)
