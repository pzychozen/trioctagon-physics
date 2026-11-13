"""Outward integer intervals and first derivatives. No floating proof endpoints.

Dyadic arithmetic follows the inspected accepted M2 engine's rounding design;
implemented here for the new divided system. No historical verifier is imported.
"""
from fractions import Fraction as F
from math import isqrt,factorial,sqrt as fsqrt
BITS=240; SCALE=1<<BITS
def ceildiv(a,b):return -((-a)//b)
class IV:
    __slots__=('lo','hi')
    def __init__(self,lo,hi):
        self.lo=int(lo);self.hi=int(hi)
        assert self.lo<=self.hi
    @classmethod
    def make(cls,x):
        if isinstance(x,IV):return x
        f=x if isinstance(x,F) else F(str(x))
        return cls(f.numerator*SCALE//f.denominator,ceildiv(f.numerator*SCALE,f.denominator))
    @classmethod
    def bounds(cls,a,b):return cls(cls.make(a).lo,cls.make(b).hi)
    def __add__(self,b):
        if isinstance(b,(AD,DD)):return NotImplemented
        b=IV.make(b);return IV(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,b):return self+-b if isinstance(b,(IV,AD,DD)) else self+-IV.make(b)
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if isinstance(b,(AD,DD)):return NotImplemented
        b=IV.make(b);v=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return IV(min(v)//SCALE,ceildiv(max(v),SCALE))
    __rmul__=__mul__
    def inv(self):
        assert not self.lo<=0<=self.hi,'Zero-containing denominator'
        return IV(SCALE*SCALE//self.hi,ceildiv(SCALE*SCALE,self.lo))
    def __truediv__(self,b):
        if isinstance(b,(AD,DD)):return NotImplemented
        return self*IV.make(b).inv()
    def __rtruediv__(self,b):return self.inv()*b
    def __pow__(self,n):
        assert isinstance(n,int)
        if n<0:return self.inv()**(-n)
        if n==0:return IV.make(1)
        if n==2:
            v=[self.lo*self.lo,self.hi*self.hi];return IV(0 if self.lo<=0<=self.hi else min(v)//SCALE,ceildiv(max(v),SCALE))
        out=IV.make(1)
        for _ in range(n):out=out*self
        return out
    def sqrt(self):
        assert self.lo>=0,'Negative square root'
        a=isqrt(self.lo*SCALE);b=isqrt(self.hi*SCALE)
        return IV(a,b+int(b*b<self.hi*SCALE))
    def absup(self):return max(abs(self.lo),abs(self.hi))
    def mid(self):return (self.lo+self.hi)/(2*SCALE)
    def out(self):return [str(F(self.lo,SCALE)),str(F(self.hi,SCALE))]
    def __repr__(self):return f'IV({self.lo/SCALE:.9g},{self.hi/SCALE:.9g})'
class AD:
    __slots__=('v','d')
    def __init__(self,v,d):self.v=v;self.d=list(d)
    def const(self,b):return b if isinstance(b,AD) else AD(b,[self.v*0]*len(self.d))
    def __add__(self,b):
        if isinstance(b,DD):return NotImplemented
        b=self.const(b);return AD(self.v+b.v,[x+y for x,y in zip(self.d,b.d)])
    __radd__=__add__
    def __neg__(self):return AD(-self.v,[-x for x in self.d])
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if isinstance(b,DD):return NotImplemented
        b=self.const(b);return AD(self.v*b.v,[x*b.v+self.v*y for x,y in zip(self.d,b.d)])
    __rmul__=__mul__
    def inv(self):return AD(1/self.v,[-x/(self.v**2) for x in self.d])
    def __truediv__(self,b):
        if isinstance(b,DD):return NotImplemented
        return self*self.const(b).inv()
    def __rtruediv__(self,b):return self.inv()*b
    def __pow__(self,n):
        if n==0:return self.const(1)
        return AD(self.v**n,[n*(self.v**(n-1))*x for x in self.d])
    def sqrt(self):
        value=sqrt(self.v);return AD(value,[x/(2*value) for x in self.d])
def sqrt(x):
    if isinstance(x,(IV,AD,DD)):return x.sqrt()
    if isinstance(x,float):return fsqrt(x)
    import mpmath as mp
    return mp.sqrt(x)
def value(x):return x.v if isinstance(x,AD) else x
def const_like(x,a):
    if isinstance(x,AD):return x.const(const_like(x.v,a))
    return IV.make(a) if isinstance(x,IV) else float(a) if isinstance(x,float) else type(x)(a.numerator)/a.denominator if isinstance(a,F) else type(x)(a)
def entire_tail(w,kind):
    """C1(w)=(cos(sqrt(w))-1)/w or S1(w)=(sinc(sqrt(w))-1)/w.
    Eighteen Taylor terms plus explicit uniform value/derivative tail on |w|<=1.
    The formulas are entire; no evaluation uses sqrt(w) or divides by w.
    """
    wv=value(w)
    if isinstance(wv,IV):assert wv.absup()<=SCALE,'Entire-series domain exceeded'
    else:assert abs(wv)<=1
    shift=2 if kind=='C' else 3;N=18
    out=const_like(w,F((-1)**N,factorial(2*(N-1)+shift)))
    for n in range(N-2,-1,-1):out=out*w+const_like(w,F((-1)**(n+1),factorial(2*n+shift)))
    if isinstance(wv,IV):
        err=IV.bounds(-F(2,factorial(2*N+shift)),F(2,factorial(2*N+shift)))
        derr=IV.bounds(-F(2*N,factorial(2*N+shift)),F(2*N,factorial(2*N+shift)))
        if isinstance(out,AD):out=AD(out.v+err,[d+derr*dw for d,dw in zip(out.d,w.d)])
        else:out=out+err
    return out
class DD:
    """Exact divided difference: f(t)=c+t*d. No truncated Taylor approximation.
    c=f(0) and d=(f(t)-f(0))/t with its removable continuation at zero.
    t may itself depend smoothly on the AD variables.
    """
    __slots__=('c','d','t')
    def __init__(self,c,d,t):self.c=c;self.d=d;self.t=t
    def full(self):return self.c+self.t*self.d
    def const(self,b):return b if isinstance(b,DD) else DD(b,self.d*0,self.t)
    def __add__(self,b):
        b=self.const(b);return DD(self.c+b.c,self.d+b.d,self.t)
    __radd__=__add__
    def __neg__(self):return DD(-self.c,-self.d,self.t)
    def __sub__(self,b):return self+-b
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        b=self.const(b);return DD(self.c*b.c,self.d*b.c+self.c*b.d+self.t*self.d*b.d,self.t)
    __rmul__=__mul__
    def __truediv__(self,b):
        b=self.const(b);return DD(self.c/b.c,(self.d*b.c-self.c*b.d)/(b.c*b.full()),self.t)
    def __rtruediv__(self,b):return self.const(b)/self
    def __pow__(self,n):
        if n==0:return self.const(1)
        out=self
        for _ in range(n-1):out=out*self
        return out
    def sqrt(self):
        c=sqrt(self.c);return DD(c,self.d/(c+sqrt(self.full())),self.t)
