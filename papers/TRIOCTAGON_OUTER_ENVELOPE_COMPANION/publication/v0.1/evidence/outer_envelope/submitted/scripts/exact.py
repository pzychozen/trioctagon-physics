"""Exact ordered Q(sqrt(2)) and univariate polynomials; no floating sign decisions."""
from fractions import Fraction as F
from functools import lru_cache
class Q:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        if isinstance(a,Q):self.a,self.b=a.a,a.b
        else:self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=Q(o);return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,o):return self+-Q(o)
    def __rsub__(self,o):return Q(o)+-self
    def __mul__(self,o):
        o=Q(o);return Q(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Q(o);den=o.a*o.a-2*o.b*o.b
        if not den:raise ZeroDivisionError
        return self*Q(o.a/den,-o.b/den)
    def __rtruediv__(self,o):return Q(o)/self
    def __pow__(self,n):
        assert isinstance(n,int)
        if n<0:return (1/self)**(-n)
        r=Q(1);v=self
        while n:
            if n&1:r=r*v
            v=v*v;n//=2
        return r
    def __eq__(self,o):
        if not isinstance(o,(Q,int,F)):return False
        o=Q(o);return self.a==o.a and self.b==o.b
    def __hash__(self):return hash((self.a,self.b))
    def __bool__(self):return bool(self.a or self.b)
    def sign(self):
        a,b=self.a,self.b
        if not b:return (a>0)-(a<0)
        if not a:return (b>0)-(b<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        diff=a*a-2*b*b
        assert diff!=0 # sqrt(2) irrational; nonzero rational a,b
        return ((diff>0)-(diff<0))*(1 if a>0 else -1)
    def __float__(self):return float(self.a)+float(self.b)*2**.5
    def __repr__(self):return f'Q({str(self.a)!r},{str(self.b)!r})'
    def dump(self):return [str(self.a),str(self.b)]
    @staticmethod
    def load(row):return Q(*row)
ZERO=Q();ONE=Q(1);SQ2=Q(0,1)
A=Q(F(1,2));B=(ONE+SQ2)/2;T=3*(SQ2-1)/2
def poly(seq):
    a=[Q(x) for x in seq]
    while a and not a[-1]:a.pop()
    return tuple(a)
def pc(q):return poly([q])
X=poly([0,1])
def padd(a,b):return poly([(a[i] if i<len(a) else ZERO)+(b[i] if i<len(b) else ZERO) for i in range(max(len(a),len(b)))])
def pneg(a):return tuple(-x for x in a)
def psub(a,b):return padd(a,pneg(b))
def pmul(a,b):
    if not a or not b:return ()
    out=[ZERO]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
    return poly(out)
def pscale(a,c):return poly([x*c for x in a])
def peval(a,x):
    r=ZERO
    for c in reversed(a):r=r*x+c
    return r
def pder(a):return poly([i*a[i] for i in range(1,len(a))])
def pdiv(a,b):
    if not b:raise ZeroDivisionError
    r=poly(a);q=[ZERO]*max(0,len(a)-len(b)+1)
    while r and len(r)>=len(b):
        k=len(r)-len(b);c=r[-1]/b[-1];q[k]=c;r=psub(r,(ZERO,)*k+pscale(b,c))
    return poly(q),r
def pmonic(a):return pscale(a,1/a[-1]) if a else ()
def pgcd(a,b):
    while b:a,b=b,pdiv(a,b)[1]
    return pmonic(a)
def pdump(a):return [x.dump() for x in a]
def pload(a):return poly([Q.load(x) for x in a])
def vadd(a,b):return tuple(padd(x,y) for x,y in zip(a,b))
def vsub(a,b):return tuple(psub(x,y) for x,y in zip(a,b))
def vscale(a,c):return tuple(pscale(x,c) for x in a)
def dot(a,b):
    r=()
    for x,y in zip(a,b):r=padd(r,pmul(x,y))
    return r
def cross(a,b):return tuple(psub(pmul(a[i],b[j]),pmul(a[j],b[i])) for i,j in [(1,2),(2,0),(0,1)])
def veval(v,x):return tuple(peval(p,x) for p in v)
def constpoint(v):return tuple(pc(q) for q in v)
def vdump(v):return [pdump(p) for p in v]
def vload(v):return tuple(pload(p) for p in v)
def residual(n,d,p):return psub(dot(n,p),d)
def plane(points,cycle):
    a,b,c=(points[i] for i in cycle[:3]);n=cross(vsub(b,a),vsub(c,a));return n,dot(n,a)
def variation(values):
    signs=[v.sign() for v in values if v]
    return sum(a!=b for a,b in zip(signs,signs[1:]))
@lru_cache(maxsize=50000)
def root_count_open(p,lo,hi):
    assert (hi-lo).sign()>0
    p=poly(p);assert p
    # Remove boundary roots exactly; all subsequent Sturm evaluations have
    # a nonzero first entry, so ordinary zero-skipping endpoint variation applies.
    for t in [lo,hi]:
        while len(p)>1 and not peval(p,t):
            p,rem=pdiv(p,poly([-t,1]));assert not rem
    if len(p)==1:return 0
    seq=[p,pder(p)]
    while seq[-1]:
        rem=pneg(pdiv(seq[-2],seq[-1])[1])
        if not rem:break
        # Positive scaling controls rational growth without changing variations.
        lead=rem[-1];seq.append(pscale(rem,1/(lead if lead.sign()>0 else -lead)))
    result=variation([peval(q,lo) for q in seq])-variation([peval(q,hi) for q in seq])
    assert 0<=result<=len(p)-1
    return result
@lru_cache(maxsize=50000)
def uniform_sign(p,lo,hi):
    if not p:return 0
    roots=root_count_open(pmonic(p),lo,hi)
    if roots:raise ValueError('Interior polynomial root: '+repr((p,lo,hi,roots)))
    sign=peval(p,(lo+hi)/2).sign();assert sign
    return sign
def svalue(text,axis=0):
    # Strictly source-expression parsing; signs/roots use the rational engine above.
    import sympy as sp
    v=sp.sympify(text,locals={'sqrt':sp.sqrt})
    if axis==1:v=v/sp.sqrt(3)
    v=sp.expand(sp.radsimp(v));b=v.coeff(sp.sqrt(2));a=sp.expand(v-b*sp.sqrt(2))
    assert a.is_Rational and b.is_Rational,(text,v)
    return Q(F(int(a.p),int(a.q)),F(int(b.p),int(b.q)))
def svector(row):return tuple(svalue(s,i) for i,s in enumerate(row))
def qtext(q):
    if not q.b:return str(q.a)
    if not q.a:return f'({q.b})*sqrt(2)'
    return f'({q.a})+({q.b})*sqrt(2)'
