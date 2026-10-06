"""Independent, unvalidated midpoint reproduction of D1's 12 table fixtures.
No interval certificates are replayed. All fixtures are already in D1.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=110
A=1/mp.sqrt(2)
roots=[mp.exp(2j*mp.pi*j/3) for j in range(3)]

def start_jet(h,eta):
    d=3*h-1
    P=108*h**3+27*h**2+828*h-760
    Q=54*h**3-270*h**2-261*h+592
    U=972*h**5+2025*h**4+12744*h**3+96570*h**2+132*h+64568
    W=972*h**5-8667*h**4+112212*h**3-521514*h**2+98412*h-206440
    u1=-(3*h+2)/d
    v1=mp.sqrt(3)*(3*h-10)/(3*d)
    u2e=-P/(6*d**3); u2m=-Q/(3*d**3)
    v2=-mp.sqrt(3)*(3*h-10)*(45*h-68)/(2*d**3)
    u3=-U/(6*d**5); v3=mp.sqrt(3)*W/(18*d**5)
    nu3=-mp.sqrt(3)*(33*h**2-240*h+688)/(3*d**3)
    return (eta*u1+eta**2*u2e+eta**3*u3,eta**2*u2m,-eta*u1+eta**2*u2e-eta**3*u3,
            eta*v1+eta**2*v2+eta**3*v3,-2*eta*v1-2*eta**3*v3,eta*v1-eta**2*v2+eta**3*v3,
            eta**3*nu3)

def make_residual(h,eta):
    k=[1-eta,mp.mpf(1),1+eta]
    def residual(*x):
        z=[A*roots[j]*(1+x[j]+1j*x[3+j]) for j in range(3)]
        nu=x[6]
        amp=[z[j]*(k[j]-abs(z[j])**2)+(sum(z[l] for l in range(3) if l!=j)-2*z[j])/6 for j in range(3)]
        if h==0:
            theta=[mp.arg(v) for v in z]
            kick=[sum(mp.sin(3*(theta[l]-theta[j])) for l in range(3) if l!=j)/30 for j in range(3)]
            diff=[amp[j]+1j*z[j]*(kick[j]-nu) for j in range(3)]
        else:
            pre=[z[j]+h*amp[j] for j in range(3)]
            theta=[mp.arg(v) for v in pre]
            kick=[h*sum(mp.sin(3*(theta[l]-theta[j])) for l in range(3) if l!=j)/30 for j in range(3)]
            diff=[(pre[j]*mp.exp(1j*kick[j])-z[j]*mp.exp(1j*h*nu))/h for j in range(3)]
        return tuple(mp.re(d) for d in diff)+tuple(mp.im(d) for d in diff)+(sum(x[3:6])/3,)
    return residual

reported={
'0':['3.96847183606590e-7','4.96412883151119e-8','6.20618242410550e-9'],
'0.1':['1.12177163091642e-6','1.39907430589031e-7','1.74764433349168e-8'],
'0.01':['4.33329030539714e-7','5.42025801905918e-8','6.77634944420660e-9'],
'0.001':['4.00302531755321e-7','5.00733550033525e-8','6.26019299725693e-9']}
records=[]
for hs,printed in reported.items():
    h=mp.mpf(hs)
    for es,published in zip(['0.001','0.0005','0.00025'],printed):
        eta=mp.mpf(es);fun=make_residual(h,eta)
        sol=mp.findroot(fun,start_jet(h,eta),tol=mp.mpf('1e-100'),maxsteps=30)
        residual=max(abs(v) for v in fun(*sol))
        rel=abs(sol[6]-mp.mpf(published))/abs(sol[6])
        assert residual<mp.mpf('1e-98')
        assert rel<mp.mpf('5e-15')
        records.append({'h':hs,'eta':es,'nu':mp.nstr(sol[6],70),'printed_rate':published,
                        'relative_difference_from_rounded_printed_rate':mp.nstr(rel,10),
                        'max_original_equation_residual':mp.nstr(residual,12),
                        'coordinates':[mp.nstr(x,70) for x in sol]})
print('Matched',len(records),'printed finite-rate fixtures; max residual',max(mp.mpf(r['max_original_equation_residual']) for r in records))
result={'kind':'UNVALIDATED NUMERICAL EVIDENCE','dps':mp.mp.dps,'fixtures':'Only the 12 already listed in D1 section 6',
        'method':'Direct high-precision original two-stage formula and generator endpoint; Newton solves initialized with reported jet.',
        'not_done':'No interval proof, no independent continuation certificate, no trajectory, no parameter sweep.', 'records':records}
Path(__file__).with_name('midpoint_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
