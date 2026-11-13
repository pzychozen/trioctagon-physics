"""Exact symbolic identities, input normalization and independent rounding probes.
These support the written derivation, not a new host or M2 theorem replay.
"""
from common import *
from model import *
import sympy as sp
checks={}
def record(name,condition):
    checks[name]=bool(condition);assert condition,name
u,x,y,ep,k=sp.symbols('u x y ep k',real=True)
real=(u+x)*(1+ep*(k-(u+x)**2-y**2))
expanded=u*(1+ep*(k-u**2))+(1+ep*(k-3*u**2))*x-ep*(3*u*x**2+u*y**2+x**3+x*y**2)
record('exact_real_cubic_expansion',sp.expand(real-expanded)==0)
imag=y*(1+ep*(k-(u+x)**2-y**2))
expanded=(1+ep*(k-u**2))*y-ep*(2*u*x*y+x**2*y+y**3)
record('exact_imaginary_cubic_expansion',sp.expand(imag-expanded)==0)
a,xi,xj,yi,yj=sp.symbols('a xi xj yi yj',real=True)
P0=xj*xi+a*a*yj*yi;Q=yj*xi-xj*yi
cube=sp.expand(((xj+sp.I*a*yj)*(xi-sp.I*a*yi))**3)
record('harmonic_three_identity',sp.simplify(sp.im(cube)-a*(3*P0**2*Q-a*a*Q**3))==0)
t,f0,fd,g0,gd=sp.symbols('t f0 fd g0 gd',nonzero=True)
record('exact_divided_product',sp.expand((f0+t*fd)*(g0+t*gd)-(f0*g0+t*(fd*g0+f0*gd+t*fd*gd)))==0)
record('exact_divided_quotient',sp.cancel(((f0+t*fd)/(g0+t*gd)-f0/g0)/t-(fd*g0-f0*gd)/(g0*(g0+t*gd)))==0)
p,p0=sp.symbols('p p0',positive=True)
record('exact_divided_sqrt_rationalization',sp.cancel((p-p0)-(p*p-p0*p0)/(p+p0))==0)
mu,nu=sp.symbols('mu nu',positive=True);yy=sp.symbols('yy',real=True);tt=mu/nu;aa=sp.sqrt(tt)
lower=sp.Matrix([aa,aa*tt*yy]).jacobian([yy,nu])
record('physical_chart_determinant',sp.simplify(tt**3*lower.det()-tt**5/(2*nu))==0)
case=read(P/'EXACT_CASE.json');record('exact_family_strings',case['epsilon']=='1/20' and case['g']=='1/5' and case['k']==['1','1.2208964704604097','6.35310346037241'])
c=constants(True);m2=read(S/'m2_accepted_certificate.json')['integer_interval_certificate'];cert=read(D/'CONNECTION_CERTIFICATE.json')
def source_interval(row):return IV.bounds(F(int(row['lo_numerator']),2**row['denominator_power_of_two']),F(int(row['hi_numerator']),2**row['denominator_power_of_two']))
def included(outer,inner):return outer.lo<=inner.lo and inner.hi<=outer.hi
for key in ['m1','m2','lc','sigma']:record('tight_'+key+'_inside_accepted_bound',included(source_interval(m2['critical_data'][key]),c[key]))
for i in range(2):record('critical_vector_sign_and_normalization_'+str(i),included(source_interval(m2['critical_data']['q'][i]),c['e'][i]))
for i in range(3):
    old=source_interval(m2['normal_form_data']['w'][i])/2
    record('onset_X_equals_inherited_w_over_two_enclosure_'+str(i),included(IV.bounds(*map(F,cert['onset']['root_enclosure'][i])),old))
oldnu=source_interval(m2['normal_form_data']['c'])/source_interval(m2['critical_data']['sigma'])
record('onset_nu_contains_inherited_c_over_sigma',included(IV.bounds(*map(F,cert['onset']['root_enclosure'][4])),oldnu))
# Exact-rational independent endpoint checks of elementary rounded operations.
probe=[(F(-7,3),F(-1,5)),(F(-2,7),F(3,11)),(F(1,19),F(13,7))]
for i,(lo,hi) in enumerate(probe):
    A=IV.bounds(lo,hi);record('rational_conversion_'+str(i),F(A.lo,SCALE)<=lo<=hi<=F(A.hi,SCALE))
    square=A**2;exactlo=0 if lo<=0<=hi else min(lo*lo,hi*hi);exacthi=max(lo*lo,hi*hi)
    record('square_'+str(i),F(square.lo,SCALE)<=exactlo<=exacthi<=F(square.hi,SCALE))
    if not lo<=0<=hi:
        inv=A.inv();record('reciprocal_'+str(i),F(inv.lo,SCALE)<=1/hi<=1/lo<=F(inv.hi,SCALE))
Q=IV.bounds(F(1,7),F(11,3));root=Q.sqrt();record('sqrt_outward',F(root.lo,SCALE)**2<=F(Q.lo,SCALE) and F(root.hi,SCALE)**2>=F(Q.hi,SCALE))
N=18
for shift in [2,3]:
    ratio=F(1,(2*N+shift+1)*(2*N+shift+2));dratio=F(N+1,N)*ratio
    record('entire_value_tail_ratio_'+str(shift),ratio<F(1,2));record('entire_derivative_tail_ratio_'+str(shift),dratio<F(1,2))
result={'status':'PASS','checked_utc':now(),'checks':checks,'count':len(checks),'method':'Sympy exact polynomial/rational identities; Fraction rounding probes; accepted-input normalization containment. No finite differences or historical theorem replay.','host_role':'Accepted exact root in the inherited Krawczyk image; no new host theorem','onset_nu_accepted_enclosure':oldnu.out()}
write(D/'ALGEBRA_AND_SOURCE_CHECKS.json',result)
print(json.dumps(result,indent=2))
