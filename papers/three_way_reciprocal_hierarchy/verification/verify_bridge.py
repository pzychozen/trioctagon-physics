"""Exact checks of formulas already independently defined in shell/readout sources.
No kernel imports, fitting, new dictionary, or parameter scans.
"""
from pathlib import Path
import json
import sympy as S
checks=[]
def eq(name,expr):
    ok=S.simplify(expr)==0
    checks.append(dict(name=name,passed=bool(ok)))
    assert ok,name
sg=S.sqrt(2)-1;d=1-S.sqrt(2)/2
ell=S.Rational(2,3)
rc=1/S.sqrt(3)-S.sqrt(3)*d*ell/2
hc=sg/2+d*ell
eq('centroid radius',rc-S.sqrt(6)/6)
eq('centroid height',hc-(1+S.sqrt(2))/6)
eq('centroid dimensionless ratio',rc/hc-(2*S.sqrt(3)-S.sqrt(6)))
eq('fixed patch side ratio',d/sg-1/S.sqrt(2))
length=S.symbols('length',positive=True)
apothem=(1+S.sqrt(2))*length/2
eq('Paper C scaffold gap ratio',(S.sqrt(3)*(apothem/S.sqrt(3))-length/2)/length-1/S.sqrt(2))
theta=S.symbols('theta',real=True)
area=(2*theta-S.sin(2*theta))/S.pi
eq('lens derivative',S.diff(area,theta)-4*S.sin(theta)**2/S.pi)
eq('lens left endpoint',area.subs(theta,0))
eq('lens right endpoint',area.subs(theta,S.pi/2)-1)
def J(v):return S.im(v[0]*S.conjugate(v[1])*v[2])
eq('cubic readout initial witness',J((1,S.I,1))+1)
eq('cubic readout cyclic witness',J((S.I,1,1))-1)
out=dict(exact_checks=len(checks),checks=checks,sympy=S.__version__,scope='Source formula checks only; no continuous bridge introduced.')
Path(__file__).with_name('bridge_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
