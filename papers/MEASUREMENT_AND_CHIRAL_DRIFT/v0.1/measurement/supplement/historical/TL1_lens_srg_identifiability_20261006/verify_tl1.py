# Public path-only source derivative. Historical writer: DO NOT EXECUTE IN PLACE.
# Use tools/smoke.py for the bounded path; raw source identity is recorded in the export map.
"""Bounded TL1 symbolic/API checks; writes only this lane's TL1_RESULTS.json.

Run: python -X utf8 -B verify_tl1.py
The written proof is in TL1_LENS_SRG_INITIALIZER_IDENTIFIABILITY.md.
No recurrence trajectory, parameter sweep or predecessor test suite is run.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import math
import subprocess
import sys

sys.dont_write_bytecode = True
import mpmath as mp
import numpy as np
import sympy as sp

ROOT = Path('project-source')
REPO = ROOT / 'trioctagon-physics'
OUT = Path(__file__).resolve().parent
assert OUT == ROOT / 'research/TL1_lens_srg_identifiability_20261006'
RESULT = OUT / 'TL1_RESULTS.json'
record = json.loads(RESULT.read_text(encoding='utf-8'))
sys.path.insert(0, str(REPO))
from kernel_physics import boundary_response as br, srg

checks = []
measurements = {}


def check(name, result, evidence, detail=None):
    checks.append({'name': name, 'pass': bool(result), 'evidence': evidence, 'detail': detail})


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args]).decode('utf-8')


def inventory(path):
    rows = {}
    total = 0
    for f in sorted(path.rglob('*')):
        if f.is_file() and '.git' not in f.relative_to(path).parts and not f.is_relative_to(OUT):
            data = f.read_bytes()
            rows[f.relative_to(path).as_posix()] = sha(data)
            total += len(data)
    return {'files': len(rows), 'bytes': total,
            'sha256': sha(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode())}


# Exact symbolic support. Strict inequalities for all inputs are proved in text.
t = sp.symbols('t', real=True)
r, d, alpha = sp.symbols('r d alpha', positive=True)
I = (2*t-sp.sin(2*t))/sp.pi
check('common scale cancels from d/(2r)', sp.cancel(alpha*d/(2*alpha*r)-d/(2*r)) == 0,
      'DERIVED IDENTITY')
check('area derivative is 4 sin(theta)^2/pi',
      sp.trigsimp(sp.diff(I,t)-4*sp.sin(t)**2/sp.pi) == 0, 'DERIVED IDENTITY')
check('area endpoints are zero and one', I.subs(t,0) == 0 and I.subs(t,sp.pi/2) == 1,
      'DERIVED IDENTITY')
x = sp.symbols('x', real=True)
J = (2*sp.acos(x/2)-x*sp.sqrt(1-x*x/4))/sp.pi
check('ratio derivative is -sqrt(4-x^2)/pi in the interior',
      sp.simplify(sp.diff(J,x)+sp.sqrt(4-x*x)/sp.pi) == 0, 'DERIVED IDENTITY')
a,b,c,e = sp.symbols('a b c e', real=True)
chi_s = sp.Matrix([a+sp.I*b,c+sp.I*e])
perp_s = sp.Matrix([-c+sp.I*e,a-sp.I*b])
check('explicit nonzero orthogonal incident construction has zero overlap',
      sp.expand((sp.conjugate(chi_s).T*perp_s)[0]) == 0, 'DERIVED IDENTITY')
check('orthogonal construction preserves incident norm',
      sp.expand((sp.conjugate(perp_s).T*perp_s)[0]-(sp.conjugate(chi_s).T*chi_s)[0]) == 0,
      'DERIVED IDENTITY')
q_s=sp.exp(-sp.Rational(423,1000)); r_s=sp.exp(sp.Rational(577,1000)); c_s=sp.Rational(191,500)
check('fixed transfer cycle simplifies to a strictly positive expression',
      sp.simplify(r_s*q_s**2*c_s**2-sp.exp(-sp.Rational(269,1000))*c_s**2) == 0
      and c_s > 0, 'DERIVED IDENTITY')

# Independent 100-digit evaluation of the exact decimal-literal mathematics.
mp.mp.dps=100
mp_i=mp.j
beta=mp.pi*mp.mpf(61)/250
alpha_B=2*beta
tau=mp.cos(alpha_B)*mp.cos(beta)
B=mp.matrix([[mp.exp(-mp_i*alpha_B)*mp.cos(beta),
              -mp_i*mp.exp(-mp_i*alpha_B)*mp.sin(beta)],
             [-mp_i*mp.exp(mp_i*alpha_B)*mp.sin(beta),
              mp.exp(mp_i*alpha_B)*mp.cos(beta)]])
bchi=tau-mp_i*mp.sqrt(1-tau*tau)
projector=(B-mp.conj(bchi)*mp.eye(2))/(bchi-mp.conj(bchi))
pivot=max(range(2),key=lambda i:mp.re(projector[i,i]))
chi=projector[:,pivot]/mp.sqrt(mp.re(projector[pivot,pivot]))
xi=mp.matrix([1+2*mp_i,-1+mp_i])
xi_api=np.array([1+2j,-1+1j],complex)
n=5
m,j=divmod(n,3)
q=mp.exp(-mp.mpf(423)/1000); rs=mp.exp(mp.mpf(577)/1000); cs=mp.mpf(191)/500
hn=(rs*q*q*cs*cs)**m*[mp.mpf(1),q,q*q*cs][j]
w=mp.exp(2*mp.pi*mp_i/3)
fj=mp.matrix([1,w**(-j),w**j])/mp.sqrt(3)
overlap=(chi.H*xi)[0]
v=overlap*bchi**n*hn*fj
norm=lambda z:mp.sqrt(mp.fsum(abs(a)**2 for a in z))


def area(theta):
    if theta == 0:
        return mp.mpf(0)
    if theta == mp.pi/2:
        return mp.mpf(1)
    return (2*theta-mp.sin(2*theta))/mp.pi


def exact_formula(radius,separation):
    theta=mp.acos(separation/(2*radius))
    return mp.sqrt(area(theta))*v


def inverse_area(value):
    # Bracket inversion, never a fitted inverse or an unguarded Newton step.
    low,high=mp.mpf(0),mp.pi/2
    for _ in range(360):
        mid=(low+high)/2
        if area(mid)<value:
            low=mid
        else:
            high=mid
    return (low+high)/2


branch='negative_imag'


def native(radius,separation,incident=xi_api):
    theta=br.theta_from_lens(radius,separation)
    return srg.handoff_area_response(theta,incident,transfer_count=n,
                                    branch=branch,response=br.RESPONSE_ID).omega


base=native(1,.75)
scale_cases=[]
for radius,separation in [(1,.75),(8,6),(.125,.09375),(17,12.75)]:
    got=native(radius,separation)
    scale_cases.append({'r':radius,'d':separation,'bitwise_equal_to_base':bool(np.array_equal(base,got))})
check('four scale-related dyadic-ratio native cases agree bitwise',
      all(row['bitwise_equal_to_base'] for row in scale_cases),'NUMERICAL EVIDENCE',scale_cases)
scale_mp=exact_formula(mp.mpf(1),mp.mpf(3)/4)
scales=[mp.mpf(1)/10,mp.sqrt(2),mp.mpf(1000)]
residual_scale=max(norm(exact_formula(s,s*mp.mpf(3)/4)-scale_mp) for s in scales)
check('three additional high-precision common scales give the same output',
      residual_scale < mp.mpf('1e-95'),'NUMERICAL EVIDENCE',mp.nstr(residual_scale,12))
recoveries=[]
for ratio in [mp.mpf(1)/4,mp.mpf(3)/4,mp.mpf(3)/2]:
    omega=exact_formula(mp.mpf(1),ratio)
    gain=norm(omega)/norm(v)
    recovered_theta=inverse_area(gain*gain)
    recovered_ratio=2*mp.cos(recovered_theta)
    api=native(1,float(ratio))
    reference=np.array([complex(z) for z in omega])
    api_error=float(np.max(np.abs(api-reference)))
    recoveries.append({'d_over_r':str(ratio),'recovered_d_over_r':mp.nstr(recovered_ratio,45),
                       'ratio_absolute_error':mp.nstr(abs(recovered_ratio-ratio),12),
                       'api_absolute_error':api_error})
check('three interior ratio inversions recover the input at 100 digits',
      all(mp.mpf(row['ratio_absolute_error'])<mp.mpf('1e-90') for row in recoveries),
      'NUMERICAL EVIDENCE',recoveries)
check('three interior native outputs agree with independent high precision',
      all(row['api_absolute_error']<2e-15 for row in recoveries), 'NUMERICAL EVIDENCE')
coincident=native(1,0)
v_api_ref=np.array([complex(z) for z in v])
check('coincidence endpoint has gain one and is scale invariant',
      br.lens_area_gain(math.pi/2)==1 and
      np.max(np.abs(coincident-v_api_ref))<2e-15 and
      np.array_equal(coincident,native(7,0)), 'NUMERICAL EVIDENCE')
check('tangency endpoint gives the exact zero vector at both scales',
      np.array_equal(native(1,2),np.zeros(3,complex)) and
      np.array_equal(native(7,14),np.zeros(3,complex)), 'NUMERICAL EVIDENCE')
check('zero incident vector gives zero at an interior lens',
      np.array_equal(native(1,.75,np.zeros(2,complex)),np.zeros(3,complex)), 'NUMERICAL EVIDENCE')
perp=mp.matrix([-mp.conj(chi[1]),mp.conj(chi[0])])
orth_res=abs((chi.H*perp)[0])
mode=srg.helicity_mode(branch)
perp_api=np.array([-np.conj(mode.chi[1]),np.conj(mode.chi[0])])
orth_omega=native(1,.75,perp_api)
check('nonzero eigenbra-orthogonal incident is admitted and extracts zero',
      abs(norm(perp)-1)<mp.mpf('1e-95') and orth_res<mp.mpf('1e-95') and
      np.linalg.norm(perp_api)>.9 and np.array_equal(orth_omega,np.zeros(3,complex)),
      'NUMERICAL EVIDENCE',{'high_precision_overlap':mp.nstr(orth_res,12),
                             'native_output':[str(z) for z in orth_omega],
                             'qualification':'Exact orthogonality follows from symbolic construction, not this floating zero.'})
measurements.update(precision_digits=mp.mp.dps,branch=branch,transfer_count=n,incident=['1+2i','-1+i'],
                    abs_incident_overlap=mp.nstr(abs(overlap),30),h_n=mp.nstr(hn,30),
                    fixed_vector_norm=mp.nstr(norm(v),30),
                    largest_api_absolute_error=max(row['api_absolute_error'] for row in recoveries),
                    largest_ratio_recovery_error=mp.nstr(max(mp.mpf(row['ratio_absolute_error']) for row in recoveries),12))

sources={}
for rel in ['kernel_physics/boundary_response.py','kernel_physics/srg.py','kernel_physics/_response_numeric.py',
            'research/mathematical_atlas/entry_08_boundary_srg_handoff/TRIOCTAGON_ATLAS_08_BOUNDARY_SRG_HANDOFF_SOURCE_PACKET_v0.1.md']:
    p=REPO/rel
    sources[rel]={'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
protected_after={str(p):inventory(p) for p in map(Path,record['protected_before'])}
for p,before in record['protected_before'].items():
    check('protected path/content inventory unchanged: '+p,protected_after[p]==before,'SOURCE FACT')
head_after=git('rev-parse','HEAD').strip()
status_after=git('status','--short')
index_after=sha(git('ls-files','--stage','-z').encode())
check('HEAD unchanged',head_after==record['head_before'],'SOURCE FACT')
check('working-tree status unchanged',status_after==record['status_before'],'SOURCE FACT')
check('index unchanged',index_after==record['index_before'],'SOURCE FACT')
record.update(status='TL1 COMPLETE' if all(c['pass'] for c in checks) else 'TL1 CHECK FAILURE',
              checks=checks,measurements=measurements,sources=sources,protected_after=protected_after,
              head_after=head_after,status_after=status_after,index_after=index_after,
              script_sha256=sha(Path(__file__).read_bytes()),
              counts={'total':len(checks),'pass':sum(c['pass'] for c in checks),
                      'by_evidence':dict(Counter(c['evidence'] for c in checks))})
report=OUT/'TL1_LENS_SRG_INITIALIZER_IDENTIFIABILITY.md'
if report.exists():
    record['report_sha256']=sha(report.read_bytes())
RESULT.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':record['status'],'counts':record['counts'],
                  'measurements':measurements,'failed':[c for c in checks if not c['pass']]},indent=2))
raise SystemExit(0 if all(c['pass'] for c in checks) else 1)
