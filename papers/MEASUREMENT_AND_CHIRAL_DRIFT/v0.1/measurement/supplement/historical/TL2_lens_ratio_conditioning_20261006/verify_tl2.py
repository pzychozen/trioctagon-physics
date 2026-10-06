# Public path-only source derivative. Historical writer: DO NOT EXECUTE IN PLACE.
# Use tools/smoke.py for the bounded path; raw source identity is recorded in the export map.
"""Bounded TL2 mathematics checks. Writes only this lane's TL2_RESULTS.json.

Run with python -X utf8 -B verify_tl2.py.
No native initializer change, trajectory, parameter scan or predecessor rerun.
"""
from pathlib import Path
from collections import Counter
import ast
import hashlib
import json
import subprocess
import sys
sys.dont_write_bytecode = True
import mpmath as mp
import sympy as sp

ROOT=Path('project-source')
REPO=ROOT/'trioctagon-physics'
OUT=Path(__file__).resolve().parent
assert OUT == ROOT/'research/TL2_lens_ratio_conditioning_20261006'
RESULT=OUT/'TL2_RESULTS.json'
record=json.loads(RESULT.read_text(encoding='utf-8'))
checks=[]
tables={}


def check(name, passed, evidence, details=None):
    checks.append(dict(name=name, passed=bool(passed), evidence=evidence, details=details))


def sha(data): return hashlib.sha256(data).hexdigest()


def inventory(path):
    rows={};total=0
    for p in sorted(path.rglob('*')):
        if p.is_file() and '.git' not in p.relative_to(path).parts and not p.is_relative_to(OUT):
            b=p.read_bytes();rows[p.relative_to(path).as_posix()]=sha(b);total+=len(b)
    return dict(files=len(rows),bytes=total,sha256=sha(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()))


def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args]).decode('utf-8')


# Symbolic algebra supports the written proofs; positivity/regularity arguments
# on intervals are not replaced by finite samples.
th=sp.symbols('theta',positive=True)
I=(2*th-sp.sin(2*th))/sp.pi
t=sp.sqrt(I)
q=2*sp.cos(th)
dt_dq=-sp.sin(th)/(sp.pi*t)
dq_dt=-sp.pi*t/sp.sin(th)
dth_dt=sp.pi*t/(2*sp.sin(th)**2)
check('dt/dq chain rule',sp.trigsimp(sp.diff(t,th)/sp.diff(q,th)-dt_dq)==0,'DERIVED IDENTITY')
check('dq/dt reciprocal derivative',sp.simplify(dt_dq*dq_dt-1)==0,'DERIVED IDENTITY')
check('dtheta/dt reciprocal derivative',sp.trigsimp(sp.diff(t,th)*dth_dt-1)==0,'DERIVED IDENTITY')
check('coincidence endpoint derivatives',dt_dq.subs(th,sp.pi/2)==-1/sp.pi and
      dq_dt.subs(th,sp.pi/2)==-sp.pi and dth_dt.subs(th,sp.pi/2)==sp.pi/2,'DERIVED IDENTITY')
ratio_derivative=4*(sp.sin(th)-th*sp.cos(th))/(sp.pi*sp.sin(th)**3)
check('monotonic ratio identity supporting global q Lipschitz bound',
      sp.trigsimp(sp.diff(I/sp.sin(th)**2,th)-ratio_derivative)==0,'DERIVED IDENTITY')
z=sp.symbols('z',positive=True)
theta_z=2*sp.asin(z/2)  # z = sqrt(delta)
I_z=(2*theta_z-sp.sin(2*theta_z))/sp.pi
theta_poly=z+z**3/24+3*z**5/640
I_poly=4*z**3/(3*sp.pi)-z**5/(10*sp.pi)-z**7/(224*sp.pi)
check('theta(delta) expansion through delta^(5/2)',
      sp.series(theta_z,z,0,7).removeO()==theta_poly,'ASYMPTOTIC RESULT')
check('I(delta) expansion through delta^(7/2)',
      sp.expand(sp.series(I_z,z,0,9).removeO()-I_poly)==0,'ASYMPTOTIC RESULT')
normalized_gain=sp.sqrt(I_z/(4*z**3/(3*sp.pi)))
check('G(delta) normalized correction -3 delta/80',
      sp.series(normalized_gain,z,0,4).removeO()==1-sp.Rational(3,80)*z*z,'ASYMPTOTIC RESULT')
u=sp.symbols('u',positive=True)
# y=(t/a)^(4/3)=delta-delta^2/20+O(delta^3).
inverse_composition=sp.series((u+u*u/20)-(u+u*u/20)**2/20,u,0,3).removeO()
check('delta(t) inverse correction is +y^2/20',sp.expand(inverse_composition-u)==0,'ASYMPTOTIC RESULT')
k_theta=(2*th-sp.sin(2*th))/(2*th*sp.sin(th)**2)
k_q=(2*th-sp.sin(2*th))/(2*sp.sin(th)*sp.cos(th))
k_delta=(2*th-sp.sin(2*th))/(2*(1-sp.cos(th))*sp.sin(th))
check('tangency relative-condition limits',
      sp.limit(k_theta,th,0,dir='+')==sp.Rational(2,3) and
      sp.limit(k_q,th,0,dir='+')==0 and
      sp.limit(k_delta,th,0,dir='+')==sp.Rational(4,3),'ASYMPTOTIC RESULT')
check('coincidence relative-condition limits',
      sp.limit(k_theta,th,sp.pi/2,dir='-')==1 and
      sp.limit(k_q,th,sp.pi/2,dir='-')==sp.oo and
      sp.limit(k_delta,th,sp.pi/2,dir='-')==sp.pi/2,'ASYMPTOTIC RESULT')
r,d,scale=sp.symbols('r d scale',positive=True)
check('exact unidentifiable scale direction remains',sp.cancel(scale*d/(scale*r)-d/r)==0,
      'INFORMATION-INTERFACE RESULT')

# Three tangency points, two small-error endpoint points, one complex-vector
# fixture, four transfer counts, three overlap magnitudes: all declared here.
mp.mp.dps=100
a=2/mp.sqrt(3*mp.pi)
B=(3*mp.pi/4)**(mp.mpf(1)/3)
A=B*B


def gain(theta):
    if theta==0:return mp.mpf(0)
    if theta==mp.pi/2:return mp.mpf(1)
    return mp.sqrt((2*theta-mp.sin(2*theta))/mp.pi)


def theta_of_t(t):
    if t==0:return mp.mpf(0)
    if t==1:return mp.pi/2
    lo,hi=mp.mpf(0),mp.pi/2
    for _ in range(360):
        mid=(lo+hi)/2
        if gain(mid)<t:lo=mid
        else:hi=mid
    return (lo+hi)/2


def gap_of_t(t):return 4*mp.sin(theta_of_t(t)/2)**2


def fmt(x):return mp.nstr(x,30)


tangent_rows=[]
for delta in map(mp.mpf,['1e-4','1e-8','1e-12']):
    theta=2*mp.asin(mp.sqrt(delta)/2)
    tt=gain(theta)
    kt=mp.pi*tt*tt/(2*theta*mp.sin(theta)**2)
    kq=mp.pi*tt*tt/((2-delta)*mp.sin(theta))
    kd=mp.pi*tt*tt/(delta*mp.sin(theta))
    vals={'delta':delta,'t':tt,'theta_over_leading':theta/mp.sqrt(delta),
          'I_over_leading':tt*tt/(a*a*delta**mp.mpf('1.5')),
          'G_over_leading':tt/(a*delta**mp.mpf('.75')),
          'delta_over_inverse_leading':delta/(A*tt**(mp.mpf(4)/3)),
          'k_theta':kt,'k_q':kq,'k_delta':kd}
    tangent_rows.append({k:fmt(v) for k,v in vals.items()})
check('three tangency asymptotic fixtures',
      all(abs(mp.mpf(row[key])-1)<mp.mpf(row['delta'])/5 for row in tangent_rows
          for key in ['theta_over_leading','I_over_leading','G_over_leading','delta_over_inverse_leading']),
      'NUMERICAL EVIDENCE',tangent_rows)
check('smallest tangency point agrees with relative-condition limits',
      abs(mp.mpf(tangent_rows[-1]['k_theta'])-mp.mpf(2)/3)<mp.mpf('1e-11') and
      abs(mp.mpf(tangent_rows[-1]['k_delta'])-mp.mpf(4)/3)<mp.mpf('1e-11') and
      mp.mpf(tangent_rows[-1]['k_q'])<mp.mpf('1e-11'),'NUMERICAL EVIDENCE')
endpoint_rows=[]
for error in map(mp.mpf,['1e-3','1e-6']):
    theta=theta_of_t(error);gap=gap_of_t(error)
    endpoint_rows.append({'E':fmt(error),'theta':fmt(theta),'gap':fmt(gap),
                          'theta_over_B_E_two_thirds':fmt(theta/(B*error**(mp.mpf(2)/3))),
                          'gap_over_A_E_four_thirds':fmt(gap/(A*error**(mp.mpf(4)/3)))})
check('two exact-tangency error-floor fixtures',
      all(abs(mp.mpf(row['gap_over_A_E_four_thirds'])-1)<mp.mpf('2e-5') and
          abs(mp.mpf(row['theta_over_B_E_two_thirds'])-1)<mp.mpf('2e-5') for row in endpoint_rows),
      'NUMERICAL EVIDENCE',endpoint_rows)

w=mp.exp(2j*mp.pi/3)
f0=mp.matrix([1,1,1])/mp.sqrt(3)
f2=mp.matrix([1,w,w*w])/mp.sqrt(3)
v=(2-1j)*f2
norm=lambda x:mp.sqrt(mp.fsum(abs(y)**2 for y in x))
V=norm(v)
true_t=mp.mpf('.4')
parallel=mp.mpf('.03');quadrature=mp.mpf('-.04')
e=(parallel+1j*quadrature)*v+mp.mpc('.02','.01')*f0
observed=true_t*v+e
estimate=mp.re((v.H*observed)[0])/(V*V)
eta=2*norm(e)
residual=observed-estimate*v
radius=mp.sqrt(eta*eta-norm(residual)**2)/V
check('complex error decomposition leaves scalar error equal to real parallel component',
      abs(estimate-true_t-parallel)<mp.mpf('1e-95') and abs(estimate-true_t)<=norm(e)/V,
      'NUMERICAL EVIDENCE')
check('sharp feasible interval uses orthogonal residual budget',
      estimate-radius<true_t<estimate+radius and
      max(abs(norm(observed-s*v)-eta) for s in [estimate-radius,estimate+radius])<mp.mpf('1e-95'),
      'NUMERICAL EVIDENCE')
eta_sat=mp.mpf('.02')
e_sat=eta_sat*v/V
sat=mp.re((v.H*e_sat)[0])/(V*V)
check('norm bound attained by real parallel error',abs(sat-eta_sat/V)<mp.mpf('1e-95'),
      'NUMERICAL EVIDENCE')
tables['vector_fixture']={'true_t':fmt(true_t),'t_hat':fmt(estimate),'V':fmt(V),
                           'error_norm':fmt(norm(e)),'eta':fmt(eta),'feasible_lower':fmt(estimate-radius),
                           'feasible_upper':fmt(estimate+radius)}

# Read native literal values without executing or modifying source modules.
source=REPO/'kernel_physics/srg.py'
tree=ast.parse(source.read_text(encoding='utf-8'))
definition=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='NovemberParameters')
params={n.target.id:mp.mpf(str(ast.literal_eval(n.value))) for n in definition.body if isinstance(n,ast.AnnAssign)}
qs=mp.exp(-params['eta']);rs=mp.exp(params['gamma']);cs=1-params['lambda_c']
Ds=rs*qs*qs*cs*cs
rho=Ds**(mp.mpf(1)/3)
p=[mp.mpf(1),qs,qs*qs*cs]
hn=lambda n:Ds**(n//3)*p[n%3]
count_rows=[{'n':n,'h_n':fmt(hn(n)),'inverse_h_n':fmt(1/hn(n))} for n in [0,3,12,30]]
check('four transfer-count fixtures match positive exponential decay',
      0<Ds<1 and all(hn(n)>0 and abs(hn(n)/(p[n%3]*rho**(-(n%3))*rho**n)-1)<mp.mpf('1e-95') for n in [0,3,12,30]),
      'NUMERICAL EVIDENCE',count_rows)
overlap_rows=[{'overlap':fmt(b),'V_at_n_3':fmt(b*hn(3)),
               'absolute_error_amplifier':fmt(1/(b*hn(3)))} for b in map(mp.mpf,['1','1e-3','1e-6'])]
check('three nonzero-overlap fixtures have exactly reciprocal amplification scaling',
      all(abs(mp.mpf(row['absolute_error_amplifier'])*mp.mpf(row['overlap'])*hn(3)-1)<mp.mpf('1e-27') for row in overlap_rows),
      'NUMERICAL EVIDENCE',overlap_rows)
tables.update(tangency=tangent_rows,endpoint_error=endpoint_rows,transfer_counts=count_rows,overlap=overlap_rows,
              constants={'D_s':fmt(Ds),'rho':fmt(rho),'inverse_D_s':fmt(1/Ds),'inverse_rho':fmt(1/rho),
                         'gamma':fmt(-mp.log(rho)),'A':fmt(A),'B':fmt(B),'a':fmt(a)})

source_paths=[REPO/'kernel_physics/boundary_response.py',REPO/'kernel_physics/srg.py',
              ROOT/'research/TL1_lens_srg_identifiability_20261006/TL1_LENS_SRG_INITIALIZER_IDENTIFIABILITY.md']
sources={str(p):dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in source_paths}
protected_after={str(p):inventory(p) for p in map(Path,record['protected_before'])}
for p,before in record['protected_before'].items():
    check('protected inventory unchanged: '+p,protected_after[p]==before,'PRESERVATION')
head_after=git('rev-parse','HEAD').strip();status_after=git('status','--short');index_after=sha(git('ls-files','--stage','-z').encode())
check('HEAD unchanged',head_after==record['head_before'],'PRESERVATION')
check('working-tree status unchanged',status_after==record['status_before'],'PRESERVATION')
check('index unchanged',index_after==record['index_before'],'PRESERVATION')
record.update(status='TL2 COMPLETE' if all(x['passed'] for x in checks) else 'TL2 CHECK FAILURE',
              checks=checks,tables=tables,sources=sources,protected_after=protected_after,
              head_after=head_after,status_after=status_after,index_after=index_after,
              script_sha256=sha(Path(__file__).read_bytes()),precision_digits=mp.mp.dps,
              counts={'total':len(checks),'pass':sum(x['passed'] for x in checks),
                      'by_evidence':dict(Counter(x['evidence'] for x in checks))})
report=OUT/'TL2_CONDITIONING_OF_LENS_RATIO_RECOVERY.md'
if report.exists():record['report_sha256']=sha(report.read_bytes())
RESULT.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':record['status'],'counts':record['counts'],'constants':tables['constants'],
                  'failures':[x for x in checks if not x['passed']]},indent=2))
raise SystemExit(0 if all(x['passed'] for x in checks) else 1)
