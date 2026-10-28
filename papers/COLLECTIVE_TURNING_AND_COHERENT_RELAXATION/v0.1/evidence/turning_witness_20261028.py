"""Two fixed native-map steps and one phase-off control, with exact rational bounds.

No project modules are imported. Repository access is read-only. Integer endpoints
represent closed intervals divided by 2**200. All arithmetic rounds outward.
The only transcendental evaluations are square roots and short-angle sin/cos.
"""
import sys, json, math, hashlib, subprocess
from pathlib import Path
from fractions import Fraction as Q
sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding='utf-8')
S = 1 << 200
REPO = Path('C:/TORMENT/TRIOCTAGON_new/trioctagon-physics')
COMMIT = 'ad8a6e88b4a78d8b1955b34d5ff80b6c21713ade'
OUT = Path(__file__).with_suffix('.json')
assert not OUT.is_relative_to(REPO)
def ceildiv(a,b): return -((-a)//b)
class I:
    def __init__(self, value=0, *, bounds=None):
        if bounds is not None: self.lo,self.hi=bounds
        else:
            v=Q(value);self.lo=(v.numerator*S)//v.denominator;self.hi=ceildiv(v.numerator*S,v.denominator)
        assert self.lo<=self.hi
    def __add__(a,b):
        b=iv(b);return I(bounds=(a.lo+b.lo,a.hi+b.hi))
    __radd__=__add__
    def __neg__(a):return I(bounds=(-a.hi,-a.lo))
    def __sub__(a,b):return a+-iv(b)
    def __rsub__(a,b):return iv(b)+-a
    def __mul__(a,b):
        b=iv(b);v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi]
        return I(bounds=(min(v)//S,ceildiv(max(v),S)))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=iv(b);assert b.lo>0 or b.hi<0
        v=[Q(a.lo*S,b.lo),Q(a.lo*S,b.hi),Q(a.hi*S,b.lo),Q(a.hi*S,b.hi)]
        lo=min(v);hi=max(v)
        return I(bounds=(lo.numerator//lo.denominator,ceildiv(hi.numerator,hi.denominator)))
    def __rtruediv__(a,b):return iv(b)/a
    def square(a):
        v=(a.lo*a.lo,a.hi*a.hi)
        return I(bounds=(0 if a.lo<=0<=a.hi else min(v)//S,ceildiv(max(v),S)))
    def sqrt(a):
        assert a.lo>=0
        lo=math.isqrt(a.lo*S);hi=math.isqrt(a.hi*S)
        if hi*hi<a.hi*S:hi+=1
        return I(bounds=(lo,hi))
    def exact_record(a):return {'lo_numerator':str(a.lo),'hi_numerator':str(a.hi),'denominator':str(S)}
def iv(x):return x if isinstance(x,I) else I(x)
def cadd(a,b):return a[0]+b[0],a[1]+b[1]
def csub(a,b):return a[0]-b[0],a[1]-b[1]
def cmul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def cscale(a,b):return a[0]*b,a[1]*b
def conj(a):return a[0],-a[1]
def csum(z):return sum(a[0] for a in z),sum(a[1] for a in z)
def mean(z):return cscale(csum(z),Q(1,3))
def sqabs(z):
    if isinstance(z[0],I):return z[0].square()+z[1].square()
    return z[0]*z[0]+z[1]*z[1]
def abs_bound(x):return Q(max(abs(x.lo),abs(x.hi)),S)
def sincos(x):
    assert abs_bound(x)<Q(1,100)
    # sin through degree 19, cos through degree 20; Lagrange remainders.
    x2=x.square();st=x;ct=I(1);sn=st;cs=ct
    for j in range(1,10):
        st=-st*x2/((2*j)*(2*j+1));sn=sn+st
    for j in range(1,11):
        ct=-ct*x2/((2*j-1)*(2*j));cs=cs+ct
    sr=Q(1,100)**21/math.factorial(21)
    cr=Q(1,100)**22/math.factorial(22)
    se=ceildiv(sr.numerator*S,sr.denominator);ce=ceildiv(cr.numerator*S,cr.denominator)
    return I(bounds=(sn.lo-se,sn.hi+se)),I(bounds=(cs.lo-ce,cs.hi+ce))

eps=Q(1,10);g=Q(1,60);lam=Q(1,300);k=[Q(999,1000),Q(1),Q(1001,1000)]
initial=[(Q(1),Q(1)),(Q(1),Q(1)),(Q(1),Q(-2))]
def amplitude(z):
    total=csum(z)
    return [cadd(cscale(a,1+eps*(k[i]-sqabs(a))-3*g),cscale(total,g)) for i,a in enumerate(z)]
def advance(z):
    a=amplitude(z)
    assert all(sqabs(v).lo>S for v in a),'Expected regular witness with all prestage moduli >1'
    units=[cscale(v,1/sqabs(v).sqrt()) for v in a]
    kicks=[]
    for i in range(3):
        s=I(0)
        for j in range(3):
            if i==j:continue
            pair=cmul(units[j],conj(units[i]))
            s=s+cmul(cmul(pair,pair),pair)[1]
        kicks.append(lam*s)
    nxt=[]
    for a_i,d in zip(a,kicks):
        sn,cs=sincos(d);nxt.append(cmul(a_i,(cs,sn)))
    onsite=mean([cscale(v,eps*(k[i]-sqabs(v))) for i,v in enumerate(z)])
    sync=mean([csub(b,a_i) for b,a_i in zip(nxt,a)])
    assert all(sqabs(v).lo>S for v in nxt)
    return nxt,{'prestage':a,'kicks':kicks,'onsite_mean_increment':onsite,'synchronizer_mean_increment':sync}
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def W(z):
    c=cross([v[0] for v in z],[v[1] for v in z])
    return [-c[0]/2+c[1]-c[2]/2,I(3).sqrt()*(c[2]-c[0])/2,I(0)]
def turning(means):return cmul(conj(csub(means[1],means[0])),csub(means[2],means[1]))[1]
def dec_int(n,digits):
    sign='-' if n<0 else '';s=str(abs(n)).zfill(digits+1)
    return sign+s[:-digits]+'.'+s[-digits:]
def coarse(x,digits=10):
    x=iv(x);ten=10**digits
    return [dec_int(x.lo*ten//S,digits),dec_int(ceildiv(x.hi*ten,S),digits)]
def enc(obj):
    if isinstance(obj,I):return {'decimal_enclosure':coarse(obj),'exact_interval':obj.exact_record()}
    if isinstance(obj,Q):return {'exact_fraction':str(obj),'decimal_enclosure':coarse(obj)}
    if isinstance(obj,dict):return {key:enc(v) for key,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [enc(v) for v in obj]
    return obj
def git(*args):return subprocess.run(['git',*args],cwd=REPO,capture_output=True,check=True).stdout
status_before=git('--no-optional-locks','status','--porcelain=v1','--untracked-files=all')
assert git('rev-parse','HEAD').decode().strip()==COMMIT

states=[[(I(x),I(y)) for x,y in initial]];stages=[]
for _ in range(2):
    nxt,stage=advance(states[-1]);states.append(nxt);stages.append(stage)
means=[mean(z) for z in states]
increments=[csub(means[j+1],means[j]) for j in range(2)]
K=turning(means)
assert K.lo>0
off=[initial]
for _ in range(2):off.append(amplitude(off[-1]))
off_means=[mean(z) for z in off];off_K=turning(off_means)
assert off_K>0
assert all(sqabs(v)>1 for z in off for v in z)
ratio0=Q(2,5);pre0=amplitude(initial);ratio1=sqabs(pre0[0])/sqabs(pre0[2])
assert ratio0!=ratio1
readouts=[W(z) for z in states]
assert readouts[1][0].hi<readouts[0][0].lo
assert readouts[2][0].hi<readouts[1][0].lo
sources=[
 'kernel_physics/dynamics.py',
 'SRG_REDISCOVERY/FINAL_MATHEMATICAL_BRIDGE/publication/v0.1/SRG_FINAL_MATHEMATICAL_BRIDGE_v0.1.md',
 'papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/manuscript.tex',
 'papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex',
 'papers/PAPER_G/v0.1.1/source/paper_g.tex']
source_records=[]
for path in sources:
    raw=git('show',COMMIT+':'+path)
    assert raw==(REPO/path).read_bytes()
    source_records.append({'path':path,'sha256':hashlib.sha256(raw).hexdigest(),'commit':COMMIT})
assert git('--no-optional-locks','status','--porcelain=v1','--untracked-files=all')==status_before
record=enc({'result':'PASS','parameter_point':{'eps':eps,'g':g,'lambda':lam,'k':k,'documented_point':'D2/D41: h=1/10, eta=1/1000'},'initial_state':initial,'states':states,'means':means,'increments':increments,'turning':K,'stage_budgets':stages,'W':readouts,'shape_ratio_squared':{'n0':ratio0,'n1':ratio1},'phase_off':{'states':off,'means':off_means,'increments':[csub(off_means[j+1],off_means[j]) for j in range(2)],'turning':off_K,'W':[W([(I(x),I(y)) for x,y in z]) for z in off]},'conjugate_control':'Exact real-parameter conjugation equivariance gives conjugate states/means/increments, identical intensities and amplitude ratios, and negative K and W. Initial mean is 1 for both. No second numerical trajectory required.','regularity':'Every input/prestage/output component over these two updates has modulus strictly greater than 1, including the phase-off comparison. Native Arg0(0)=0 is unchanged.','bounds_method':{'scale_denominator':str(S),'arithmetic':'integer-endpoint outward-rounded intervals; exact rational phase-off arithmetic','sqrt':'integer isqrt lower bound and ceiling upper bound','phase_sine':'Im[(u_j conjugate(u_i))^3], u_i=A_i/|A_i|; no angle branch substitution','sin_cos':'Taylor degrees 19/20, |kick|<1/100; absolute remainders at most (1/100)^21/21! and (1/100)^22/22!','state_updates':'two full-map updates; two phase-off updates; no sweep or branch solve'},'sources':source_records,'repository_status_unchanged':True})
OUT.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'result':'PASS','means':[[coarse(x) for x in m] for m in means],'increments':[[coarse(x) for x in d] for d in increments],'K':coarse(K),'budget':[{key:[coarse(x) for x in s[key]] for key in ('onsite_mean_increment','synchronizer_mean_increment')} for s in stages],'W':[[coarse(x) for x in w] for w in readouts],'ratio0':str(ratio0),'ratio1':str(ratio1),'ratio1_enclosure':coarse(ratio1),'phase_off_increments':[[coarse(x) for x in csub(off_means[j+1],off_means[j])] for j in range(2)],'phase_off_K_exact':str(off_K),'phase_off_K_enclosure':coarse(off_K),'phase_off_W':[[coarse(x) for x in W([(I(a),I(b)) for a,b in z])] for z in off],'receipt':str(OUT)},indent=2))
