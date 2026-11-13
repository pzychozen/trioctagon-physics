#!/usr/bin/env python3
"""Independent M2 review. No repository imports, finite-difference derivatives,
long trajectories, or calls to Claude's scripts. The central coefficient is
computed from exact third-order algebra and outward-rounded dyadic intervals.

mpmath only supplies a candidate Newton center and displays numerical values;
all interval certificate operations use Python integer arithmetic. A computed
certificate remains subject to independent review of this script and derivation.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from pathlib import Path
import argparse, hashlib, json, sys
import mpmath as mp

BITS = 240
SCALE = 1 << BITS

def cdiv(a:int,b:int)->int:
    if b < 0: a,b=-a,-b
    return -((-a)//b)

@dataclass(frozen=True)
class IV:
    lo:int
    hi:int
    def __post_init__(self):
        if self.lo > self.hi: raise ValueError('Reversed interval')
    @classmethod
    def make(cls,x):
        if isinstance(x,cls): return x
        if isinstance(x,Fraction): f=x
        else: f=Fraction(str(x))
        return cls((f.numerator*SCALE)//f.denominator, cdiv(f.numerator*SCALE,f.denominator))
    @classmethod
    def point_from_mp(cls,x):
        # Chosen EXACT dyadic rational, NOT an enclosure of x.
        n=int(mp.floor(x*SCALE)); return cls(n,n)
    def __add__(self,b):
        b=IV.make(b); return IV(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,b):return self+-IV.make(b)
    def __rsub__(self,b):return IV.make(b)+-self
    def __mul__(self,b):
        b=IV.make(b)
        v=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return IV(min(v)//SCALE,cdiv(max(v),SCALE))
    __rmul__=__mul__
    def recip(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('Interval contains zero')
        return IV((SCALE*SCALE)//self.hi,cdiv(SCALE*SCALE,self.lo))
    def __truediv__(self,b):return self*IV.make(b).recip()
    def __rtruediv__(self,b):return IV.make(b)*self.recip()
    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError('Integer powers only')
        if n<0:return self.recip()**(-n)
        if n==0:return IV.make(1)
        if n==2:
            hi=max(self.lo*self.lo,self.hi*self.hi)
            lo=0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
            return IV(lo//SCALE,cdiv(hi,SCALE))
        result=IV.make(1)
        for _ in range(n):result=result*self
        return result
    def sqrt(self):
        if self.lo<0:raise ValueError('Negative sqrt interval')
        a=isqrt(self.lo*SCALE); b=isqrt(self.hi*SCALE)
        return IV(a,b+(b*b<self.hi*SCALE))
    def positive(self):return self.lo>0
    def contains(self,x):
        # Inclusion of the exact rational named by x.
        f=Fraction(str(x));return self.lo*f.denominator<=f.numerator*SCALE<=self.hi*f.denominator
    def abs_upper(self):return max(abs(self.lo),abs(self.hi))
    def out(self):
        # Decimal strings are convenience only. Integers plus scale are authoritative.
        return {'lo_numerator':str(self.lo),'hi_numerator':str(self.hi),'denominator_power_of_two':BITS,
                'display_lo':mp.nstr(mp.mpf(self.lo)/SCALE,45),
                'display_hi':mp.nstr(mp.mpf(self.hi)/SCALE,45),
                'display_width':mp.nstr(mp.mpf(self.hi-self.lo)/SCALE,8)}

def sqrt(x):return x.sqrt() if isinstance(x,IV) else mp.sqrt(x)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))]for i in range(len(a))]
def mv(a,b):return [dot(r,b)for r in a]
def tr(a):return list(map(list,zip(*a)))
def matminus(a,b):return [[x-y for x,y in zip(ar,br)]for ar,br in zip(a,b)]
def ident(n,make):return [[make(int(i==j))for j in range(n)]for i in range(n)]
def det(a):
    n=len(a)
    if n==1:return a[0][0]
    return sum((1 if j%2==0 else -1)*a[0][j]*det([r[:j]+r[j+1:]for r in a[1:]])for j in range(n))
def inverse3(a):
    d=det(a)
    return [[((-1)**(i+j))*det([r[:i]+r[i+1:]for ri,r in enumerate(a)if ri!=j])/d for j in range(3)]for i in range(3)]

def operators(u,make):
    ep=make(1)/20;g=make(1)/5;k=[make(1),make('1.2208964704604097'),make('6.35310346037241')]
    M=[[(1+ep*(k[i]-u[i]**2) if i==j else make(0))+g*(1-3*int(i==j))for j in range(3)]for i in range(3)]
    JR=[[M[i][j]-(2*ep*u[i]**2 if i==j else 0)for j in range(3)]for i in range(3)]
    return ep,g,k,M,JR

def residual(u,make):
    ep,g,k,_,_=operators(u,make)
    return [ep*u[i]*(k[i]-u[i]**2)+g*(sum(u)-3*u[i])for i in range(3)]

def compressed_data(u,make):
    ep,g,k,M,JR=operators(u,make)
    a=sqrt(u[0]**2+u[1]**2); norm=sqrt(dot(u,u))
    v1=[u[1]/a,-u[0]/a,make(0)]
    v2=[u[0]*u[2]/(a*norm),u[1]*u[2]/(a*norm),-(u[0]**2+u[1]**2)/(a*norm)]
    V=tr([v1,v2]);K=mm(mm(tr(V),M),V)
    # The exact matrix is symmetric; use its (0,1) entry in the closed form.
    disc=sqrt((K[0][0]-K[1][1])**2+4*K[0][1]**2)
    m1=(K[0][0]+K[1][1]+disc)/2;m2=(K[0][0]+K[1][1]-disc)/2
    q=[K[0][1],m1-K[0][0]]; qnorm=sqrt(dot(q,q));q=[v/qnorm for v in q]
    eta=mv(V,q);lc=(1+1/m1)/9;sig=9*m1
    return {'u':u,'ep':ep,'g':g,'k':k,'M':M,'JR':JR,'V':V,'K':K,'m1':m1,'m2':m2,'q':q,'eta':eta,'lc':lc,'sigma':sig}

# Truncated formal series. Coefficients are ordinary Taylor coefficients (not
# derivatives). All functions below operate modulo t^4. No evaluation at t != 0.
class Jet:
    def __init__(self,coefs):
        self.v=list(coefs)+[coefs[0]*0]*(4-len(coefs))
        self.v=self.v[:4]
    def __add__(self,b):
        if not isinstance(b,Jet):b=Jet([self.v[0]*0+b])
        return Jet([a+x for a,x in zip(self.v,b.v)])
    __radd__=__add__
    def __neg__(self):return Jet([-x for x in self.v])
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,Jet):return Jet([x*b for x in self.v])
        return Jet([sum(self.v[j]*b.v[n-j]for j in range(n+1))for n in range(4)])
    __rmul__=__mul__
    def __truediv__(self,b):
        if not isinstance(b,Jet):return Jet([x/b for x in self.v])
        o=[]
        for n in range(4):o.append((self.v[n]-sum(b.v[j]*o[n-j]for j in range(1,n+1)))/b.v[0])
        return Jet(o)
    def __pow__(self,n):
        r=Jet([self.v[0]*0+1])
        for _ in range(n):r=r*self
        return r
    def sqrt(self):
        o=[sqrt(self.v[0])]
        for n in range(1,4):o.append((self.v[n]-sum(o[j]*o[n-j]for j in range(1,n)))/(2*o[0]))
        return Jet(o)
    def atan_zero(self):return self-self**3/3
    def sin_zero(self):return self-self**3/6
    def cos_zero(self):return 1-self**2/2

def quotient_jet(D,x2):
    """Exact third-order Taylor image of u + (t^2/2)x2 + i*t*eta.
    The identity M(u)u=u holds for the certified exact host; using the expanded
    amplitude substep makes that constraint explicit, avoiding point-root drift.
    """
    u,ep,M,JR,eta,lc=[D[k]for k in ('u','ep','M','JR','eta','lc')]
    z=u[0]*0
    xi=[Jet([z,z,x/2])for x in x2]; yi=[Jet([z,x])for x in eta]
    rt=[];it=[]
    for i in range(3):
        rt.append(Jet([u[i]])+sum(xi[j]*JR[i][j]for j in range(3))-
                  (xi[i]**2*(3*u[i])+yi[i]**2*u[i]+xi[i]**3+xi[i]*yi[i]**2)*ep)
        it.append(sum(yi[j]*M[i][j]for j in range(3))-
                  (xi[i]*yi[i]*(2*u[i])+xi[i]**2*yi[i]+yi[i]**3)*ep)
    ph=[(it[i]/rt[i]).atan_zero()for i in range(3)]
    angle=[ph[i]+sum(((ph[j]-ph[i])*3).sin_zero()for j in range(3)if j!=i)*lc for i in range(3)]
    radius=[(rt[i]**2+it[i]**2).sqrt()for i in range(3)]
    rr=[radius[i]*angle[i].cos_zero()for i in range(3)]
    ii=[radius[i]*angle[i].sin_zero()for i in range(3)]
    gauge=(sum(ii[i]*u[i]for i in range(3))/sum(rr[i]*u[i]for i in range(3))).atan_zero()
    cosg=gauge.cos_zero();sing=gauge.sin_zero()
    R=[rr[i]*cosg+ii[i]*sing for i in range(3)]
    I=[ii[i]*cosg-rr[i]*sing for i in range(3)]
    return R,I

def coefficient(D,make):
    zero=make(0);u=D['u'];eta=D['eta']
    r0,i0=quotient_jet(D,[zero]*3)
    bqq=[2*r0[i].v[2]for i in range(3)]
    w=mv(inverse3(matminus(ident(3,make),D['JR'])),bqq)
    r,imag=quotient_jet(D,w)
    direct=sum(eta[i]*i0[i].v[3]for i in range(3))
    c=sum(eta[i]*imag[i].v[3]for i in range(3))
    Cq=cross(u,eta);T=[[-make(1)/2,make(1),-make(1)/2],[-sqrt(make(3))/2,zero,sqrt(make(3))/2],[zero]*3]
    Wq=mv(T,Cq);wn=sqrt(dot(Wq,Wq));Gq=sum(Cq)
    return {'Bqq':bqq,'w':w,'direct':direct,'slaved':c-direct,'c':c,'Cq':Cq,'Wq':Wq,'Wq_norm':wn,'Gamma_q':Gq,
            'W_sqrt_coefficient':wn*sqrt(D['sigma']/c),'Gamma_W_ratio':-Gq/wn}

def mp_center():
    mp.mp.dps=90
    u=list(map(mp.mpf,['1.55','1.57','2.09']))
    for _ in range(14):
        _,_,_,_,JR=operators(u,mp.mpf)
        J=mp.matrix(matminus(JR,ident(3,mp.mpf)))
        du=mp.lu_solve(J,mp.matrix(residual(u,mp.mpf)))
        u=[u[i]-du[i]for i in range(3)]
    return u

def certificate(center):
    make=IV.make
    u0=[IV.point_from_mp(x)for x in center]
    rad=make('1e-30');X=[a+IV(-rad.hi,rad.hi)for a in u0]
    _,_,_,_,JR0=operators(center,mp.mpf)
    Ynum=mp.inverse(mp.matrix(matminus(JR0,ident(3,mp.mpf))))
    Y=[[IV.point_from_mp(Ynum[i,j])for j in range(3)]for i in range(3)]
    f0=residual(u0,make)
    _,_,_,_,JRX=operators(X,make)
    JX=matminus(JRX,ident(3,make))
    E=matminus(ident(3,make),mm(Y,JX));rho=mv(E,[X[i]-u0[i]for i in range(3)])
    yf=mv(Y,f0)
    K=[u0[i]-yf[i]+rho[i]for i in range(3)]
    inside=all(X[i].lo<K[i].lo<=K[i].hi<X[i].hi for i in range(3))
    contraction_num=max(sum(v.abs_upper()for v in row)for row in E)
    assert inside and contraction_num<SCALE and not(det(Y).lo<=0<=det(Y).hi)
    D=compressed_data(X,make); C=coefficient(D,make)
    assert D['m1'].positive() and (1-D['m1']).positive()
    assert D['m2'].positive() and (D['m1']-D['m2']).positive()
    # Strict 0 < J_R < .7 I by Sylvester (symmetric exact matrix).
    radial=[]
    for A in [D['JR'],matminus([[make('0.7')*int(i==j)for j in range(3)]for i in range(3)],D['JR'])]:
        minors=[det([r[:n]for r in A[:n]])for n in range(1,4)]
        assert all(m.positive()for m in minors);radial.append([m.out()for m in minors])
    assert C['c'].positive()
    assert (C['c']-make('0.0865248497217')).positive()
    assert (make('0.0865248497219')-C['c']).positive()
    assert C['Wq_norm'].positive()
    def out(x):
        if isinstance(x,IV):return x.out()
        if isinstance(x,list):return [out(y)for y in x]
        return x
    return {'precision_bits':BITS,'exact_parameter_policy':'Decimal strings/1/20/1/5 converted directly as rational intervals, never singleton rounded mpf',
            'center':[out(v)for v in u0],'host_box':[out(v)for v in X],
            'F_exact_rational_center_enclosure':out(f0),'preconditioner_exact_dyadic':out(Y),
            'krawczyk_image':out(K),'krawczyk_strict_inclusion':inside,
            'contraction_upper_numerator':str(contraction_num),'contraction_denominator_power_of_two':BITS,
            'radial_sylvester_positive_minors':radial,
            'critical_data':{k:out(D[k])for k in ['m1','m2','q','eta','lc','sigma','K']},
            'normal_form_data':{k:out(v)for k,v in C.items()},
            'simple_crossing_radial_stability_and_c_positive':True,
            'certificate_status':'INDEPENDENT_GPT_COMPUTED_CERTIFICATE_AWAITING_REVIEW_NOT_JOINT_ACCEPTANCE'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(Path(__file__).with_suffix('.json')));args=ap.parse_args()
    center=mp_center();D=compressed_data(center,mp.mpf);C=coefficient(D,mp.mpf)
    cert=certificate(center)
    def display(v):
        if isinstance(v,list):return [display(x)for x in v]
        return mp.nstr(v,65)
    numerical={k:display(v)for k,v in C.items()};numerical.update({k:display(D[k])for k in ['u','m1','m2','lc','sigma','eta']})
    out={'purpose':__doc__,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'python':sys.version,'mpmath':mp.__version__,'mp_working_digits':mp.mp.dps,
         'analytic_taylor_numerical_values':numerical,'integer_interval_certificate':cert,
         'not_run':['Claude original scripts','kernel/repository modules','long trajectories','entrance/basin experiments'],
         'no_repository_changes':True}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(numerical,indent=2))
    print('C interval:',cert['normal_form_data']['c']['display_lo'],cert['normal_form_data']['c']['display_hi'])
    print('HOST:',cert['krawczyk_strict_inclusion'],'certified coefficient positive:',cert['simple_crossing_radial_stability_and_c_positive'])
if __name__=='__main__':main()
