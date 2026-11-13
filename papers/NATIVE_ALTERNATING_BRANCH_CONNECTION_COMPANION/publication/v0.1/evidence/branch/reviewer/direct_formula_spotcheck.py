"""Independent numerical formula/derivative spot checks; NOT interval proof.
No trajectories, continuation solves or host solves. Uses a midpoint of the
accepted host enclosure only for a 100-digit diagnostic calculation.
The actual proof still uses the enclosure of the accepted exact host.
"""
from pathlib import Path
import json,sys
from fractions import Fraction
import mpmath as mp
R=Path(__file__).resolve().parent.parent;S=R/'submitted';mp.mp.dps=100
sys.path.insert(0,str(R/'replay_work/scripts'))
from model import constants,regularized
from arithmetic import IV
cert=json.loads((S/'data/CONNECTION_CERTIFICATE.json').read_text())
host=json.loads((S/'sources/m2_accepted_certificate.json').read_text())['integer_interval_certificate']
def cv(f):
 f=Fraction(f);return mp.mpf(f.numerator)/f.denominator
u=mp.matrix([cv(Fraction(int(z['lo_numerator'])+int(z['hi_numerator']),2**(z['denominator_power_of_two']+1))) for z in host['krawczyk_image']])
eps=mp.mpf(1)/20;g=mp.mpf(1)/5;k=list(map(mp.mpf,['1','1.2208964704604097','6.35310346037241']))
a12=mp.sqrt(u[0]**2+u[1]**2);ru=mp.norm(u)
V=mp.matrix([[u[1]/a12,u[0]*u[2]/(a12*ru)],[-u[0]/a12,u[1]*u[2]/(a12*ru)],[0,-a12/ru]])
M=mp.matrix([[int(i==j)*(1+eps*(k[i]-u[i]**2))+g*(1-3*int(i==j)) for j in range(3)] for i in range(3)])
B=V.T*M*V;m1=(B[0,0]+B[1,1]+mp.sqrt((B[0,0]-B[1,1])**2+4*B[0,1]**2))/2
lc=(1+1/m1)/9;e=mp.matrix([B[0,1],m1-B[0,0]]);e=e/mp.norm(e);ep=mp.matrix([-e[1],e[0]])
def quotient(z,mu):
 O=[u[i]+z[i]+1j*sum(V[i,j]*z[3+j] for j in range(2)) for i in range(3)]
 v=[O[i]+eps*O[i]*(k[i]-abs(O[i])**2)+g*sum(O[j]-O[i] for j in range(3) if j!=i) for i in range(3)]
 phase=[mp.arg(vv) for vv in v]
 w=[v[i]*mp.exp(1j*(lc+mu)*sum(mp.sin(3*(phase[j]-phase[i])) for j in range(3) if j!=i)) for i in range(3)]
 proj=sum(u[i]*w[i] for i in range(3));w=[vv*mp.conj(proj)/abs(proj) for vv in w]
 return [mp.re(w[i])-u[i] for i in range(3)]+[sum(V[i,j]*mp.im(w[i]) for i in range(3)) for j in range(2)]
def residual(x,mu):
 t=mu/x[4];a=mp.sqrt(t);eta=a*(e+t*x[3]*ep)
 z=[t*x[i] for i in range(3)]+list(eta);q=quotient(z,mu)
 return [(q[i]-z[i])/t for i in range(3)]+[(q[i]+z[i])/a**3 for i in range(3,5)]
c=constants(True);rows=[]
for idx in [0,32,64,96,127]:
 p=cert['patches'][idx];muq=sum(map(Fraction,p['mu']))/2;mu=cv(muq);x=list(map(cv,p['center']))
 rr,_=regularized([IV.make(Fraction(y)) for y in p['center']],IV.make(muq),c,parameter_derivative=True)
 vals=residual(x,mu);der=mp.matrix(5,6)
 for i in range(5):
  for j in range(6):
   if j<5:
    def fun(q):
     z=x[:];z[j]=q;return residual(z,mu)[i]
    der[i,j]=mp.diff(fun,x[j])
   else:der[i,j]=mp.diff(lambda q:residual(x,q)[i],mu)
 def contains(I,v):
  a,b=I.out();return cv(a)<=v<=cv(b)
 value_pass=all(contains(rr[i].v,vals[i]) for i in range(5))
 derivative_pass=all(contains(rr[i].d[j],der[i,j]) for i in range(5) for j in range(6))
 rows.append({'patch':idx,'mu':str(muq),'direct_values_inside_supplied_point_enclosures':value_pass,'direct_derivatives_inside_supplied_point_enclosures':derivative_pass})
 assert value_pass and derivative_pass,rows[-1]
out={'status':'PASS','precision_decimal_digits':100,'points':rows,'scope':'Five independent direct-form numerical residual/derivative samples. Neither an interval proof nor an independent enclosure engine; the host midpoint is diagnostic, not an exact root. No trajectory or nonlinear solve performed.'}
(Path(__file__).parent/'DIRECT_FORMULA_SPOTCHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
