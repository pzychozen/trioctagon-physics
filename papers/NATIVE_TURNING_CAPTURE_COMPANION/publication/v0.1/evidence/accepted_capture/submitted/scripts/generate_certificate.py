"""N03 directed dyadic interval generation. No imported native or old checker code.

All endpoints are integers divided by 2**512. Only integer/rational operations
and integer square root control inclusion; numerical discovery only chooses N
and a rational terminal direction. Every recorded padding enlarges its interval.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,math,os
R=Path(__file__).resolve().parents[1]; S=1<<512
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
assert json.loads((R/'logs/PRIOR_GATE.json').read_text())['outcome']=='DISTINCT_GAP'
def up(n,d):assert d>0;return -((-n)//d)
class Box:
    def __init__(self,lo,hi):self.lo=int(lo);self.hi=int(hi);assert self.lo<=self.hi
    @staticmethod
    def q(x):
        x=F(x);return Box((x.numerator*S)//x.denominator,up(x.numerator*S,x.denominator))
    def __add__(self,other):
        b=conv(other);return Box(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return Box(-self.hi,-self.lo)
    def __sub__(self,other):return self+-conv(other)
    def __rsub__(self,other):return conv(other)+-self
    def __mul__(self,other):
        b=conv(other);p=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return Box(min(p)//S,up(max(p),S))
    __rmul__=__mul__
    def reciprocal(self):
        assert self.lo>0
        return Box((S*S)//self.hi,up(S*S,self.lo))
    def __truediv__(self,other):return self*conv(other).reciprocal()
    def sq(self):
        a,b=self.lo*self.lo,self.hi*self.hi
        return Box(0 if self.lo<=0<=self.hi else min(a,b)//S,up(max(a,b),S))
    def root(self):
        assert self.lo>=0
        a=math.isqrt(self.lo*S);b=math.isqrt(self.hi*S)
        return Box(a,b+(b*b<self.hi*S))
    def pad(self,factor):
        mid=(self.lo+self.hi)//2;rad=max(mid-self.lo,self.hi-mid)+1
        return Box(mid-factor*rad,mid+factor*rad)
    def serial(self):return [str(self.lo),str(self.hi)]
def conv(x):return x if isinstance(x,Box) else Box.q(x)
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def times(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(z,a):return(z[0]*a,z[1]*a)
def conj(z):return(z[0],-z[1])
def norm2(z):return z[0].sq()+z[1].sq()
def serial(z):return [a.serial() for a in z]
def trigonometric(x):
    assert max(abs(x.lo),abs(x.hi))*100<S
    t=x.sq()
    # Horner polynomials: sin degree 47, cos degree 48, zero next coefficients.
    ps=Box.q(F((-1)**23,math.factorial(47)))
    pc=Box.q(F(1,math.factorial(48)))
    for j in range(22,-1,-1):ps=Box.q(F((-1)**j,math.factorial(2*j+1)))+t*ps
    for j in range(23,-1,-1):pc=Box.q(F((-1)**j,math.factorial(2*j)))+t*pc
    sn=x*ps;cs=pc
    er_s=up(S,100**49*math.factorial(49));er_c=up(S,100**50*math.factorial(50))
    return Box(sn.lo-er_s,sn.hi+er_s).pad(4),Box(cs.lo-er_c,cs.hi+er_c).pad(4)
eps=F(1,10);g=F(1,60);lam=F(1,300);k=[F(999,1000),F(1),F(1001,1000)]
z=[(Box.q(1),Box.q(1)),(Box.q(1),Box.q(1)),(Box.q(1),Box.q(-2))]
explore=json.loads((R/'data/EXPLORATION.json').read_text()); N=explore['candidate_N']; direction=explore['candidate_rational_direction']
assert N==50 and direction==[987395,158274]
states=[[serial(x) for x in z]]; steps=[]
for n in range(N):
    v=[]
    for i,x in enumerate(z):
        # Uncombined original expression deliberately retained in the generator.
        graph=(Box.q(0),Box.q(0))
        for j in range(3):
            if j!=i:graph=plus(graph,plus(z[j],scale(x,-1)))
        out=plus(plus(x,scale(x,eps*(k[i]-norm2(x)))),scale(graph,g))
        v.append(tuple(t.pad(2) for t in out))
    rho=[norm2(x).root() for x in v]; assert all(r.lo*100>87*S for r in rho)
    delta=[];sines=[];cosines=[]
    for i in range(3):
        acc=Box.q(0)
        for j in range(3):
            if j==i:continue
            c=times(v[j],conj(v[i]));cube=times(times(c,c),c)
            denom=rho[i]*rho[i]*rho[i]*rho[j]*rho[j]*rho[j]
            acc=acc+cube[1]/denom
        d=(lam*acc).pad(4);delta.append(d)
        si,co=trigonometric(d);sines.append(si);cosines.append(co)
    z=[tuple(t.pad(2) for t in times(v[i],(cosines[i],sines[i]))) for i in range(3)]
    states.append([serial(x) for x in z]);steps.append({'n':n,'prestage':[serial(x) for x in v],'moduli':[r.serial() for r in rho],'kicks':[d.serial() for d in delta],'sines':[s.serial() for s in sines],'cosines':[c.serial() for c in cosines]})
terminal=[]
for x in z:
    rad=norm2(x).root(); low=(rad.lo*1000000)//S; high=up(rad.hi*1000000,S)
    re=direction[0]*x[0]+direction[1]*x[1];im=direction[0]*x[1]-direction[1]*x[0]
    margin=re.lo-8*max(abs(im.lo),abs(im.hi));assert margin>0
    terminal.append({'amplitude_bounds':[str(F(low,1000000)),str(F(high,1000000))],'rotated_real':re.serial(),'rotated_imag':im.serial(),'cone_margin_numerator':str(margin),'cone_margin_lower_integer':margin//S})
result={'task':'NATIVE_TURNING_CAPTURE_01','kind':'Directed interval certificate for exact original seed; independently check before accepting','created_utc':datetime.now(timezone.utc).isoformat(),'N':N,'denominator':str(S),'precision_bits':512,'parameters':{'epsilon':'1/10','g':'1/60','lambda':'1/300','k':['999/1000','1','1001/1000']},'initial_state':[['1','1'],['1','1'],['1','-2']],'states':states,'steps':steps,'terminal':terminal,'direction':direction,'phase_test':'Re((a-ib)z)>8*abs(Im((a-ib)z)); width < 2 arctan(1/8) < 1/4 < pi/12.','trigonometry':{'sin_degree':47,'cos_degree':48,'argument_bound':'1/100','sin_remainder':'(1/100)^49 / 49!','cos_remainder':'(1/100)^50 / 50!'},'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'data/CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
maxwidth=max((hi-lo for state in states for z in state for lo,hi in [(int(v[0]),int(v[1])) for v in z]),default=0)
print(json.dumps({'N':N,'terminal_amplitude_bounds':[x['amplitude_bounds'] for x in terminal],'cone_margins_at_least':[x['cone_margin_lower_integer'] for x in terminal],'all_prestage_moduli_lower':'87/100','largest_coordinate_width_numerator':str(maxwidth),'denominator':str(S),'certificate_bytes':(R/'data/CERTIFICATE.json').stat().st_size},indent=2))
