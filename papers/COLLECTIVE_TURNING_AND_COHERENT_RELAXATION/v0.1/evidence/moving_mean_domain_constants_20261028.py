"""Small exact-bound arithmetic check for the fixed-domain analytic proof.

No states are propagated. No scientific project modules are imported.
All inequalities use fractions and integer square-root bounds. Decimal output
is outward rounded; repository access is read-only.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt
import sys,json,subprocess,hashlib
sys.dont_write_bytecode=True
sys.stdout.reconfigure(encoding='utf-8')
REPO=Path('C:/TORMENT/TRIOCTAGON_new/trioctagon-physics')
PIN='ad8a6e88b4a78d8b1955b34d5ff80b6c21713ade'
OUT=Path(__file__).with_suffix('.json')
assert not OUT.is_relative_to(REPO)
def git(*args):return subprocess.run(['git',*args],cwd=REPO,capture_output=True,check=True).stdout
status=git('--no-optional-locks','status','--porcelain=v1','--untracked-files=all')
branch=git('branch','--show-current')
assert git('rev-parse','HEAD').decode().strip()==PIN
def root(n):
    scale=10**24;lo=isqrt(n*scale*scale)
    assert lo*lo<=n*scale*scale<(lo+1)*(lo+1)
    return Q(lo,scale),Q(lo+1,scale)
sqrt2=root(2);sqrt6=root(6)
cosD=tuple((sqrt2[j]+sqrt6[j])/4 for j in range(2))
hull_radius_squared=tuple(Q(81,200)*(1+x) for x in cosD)
eps=Q(1,10);g=Q(1,60);lam=Q(1,300)
kmin=Q(999,1000);kmax=Q(1001,1000);r=Q(9,10);R=Q(11,10)
a_min=1-2*g+eps*(kmin-R*R)
a_max=1-2*g+eps*(kmax-r*r)
radial_derivative_min=1-2*g+eps*kmin-3*eps*R*R
assert a_min==Q(28367,30000)>0
assert a_max==Q(29573,30000)
assert radial_derivative_min==Q(21107,30000)>0
lower_modulus=tuple((1-2*g+eps*(kmin-r*r))*r+2*g*r*x for x in cosD)
upper_modulus=R*(1+eps*(kmax-R*R))
assert lower_modulus[0]>r
assert upper_modulus==Q(107701,100000)<R
c=1-3*g+eps
H_radial_min=c-3*eps*R*R
assert H_radial_min==Q(687,1000)>0
H_lipschitz=(c-eps*hull_radius_squared[1],c-eps*hull_radius_squared[0])
q=tuple(x+eps*Q(1,1000) for x in H_lipschitz)
assert 0<q[0]<=q[1]<1
qphase=(1-Q(3,200)*sqrt2[1],1-Q(3,200)*sqrt2[0])
assert 0<qphase[0]<=qphase[1]<1
sigma=tuple(x/1000 for x in sqrt2)
forcing=tuple(eps*R*x for x in sigma)
residual=(forcing[0]/(1-q[0]),forcing[1]/(1-q[1]))
residual_squared=tuple(x*x for x in residual)
assert residual[1]<Q(5270,1000000)
assert residual_squared[1]<Q(2778,100000000)
def ceil(q):return -((-q.numerator)//q.denominator)
def decimal_integer(n,places):
    sign='-' if n<0 else '';s=str(abs(n)).zfill(places+1)
    return sign+s[:-places]+'.'+s[-places:]
def interval(x,places=14):
    lo,hi=x;scale=10**places
    return {'exact_rational_lower':str(lo),'exact_rational_upper':str(hi),
      'decimal_lower':decimal_integer((lo*scale).numerator//(lo*scale).denominator,places),
      'decimal_upper':decimal_integer(ceil(hi*scale),places)}
paths=['kernel_physics/dynamics.py','papers/NATIVE_RESPONSE_GEOMETRY/manuscript/response.tex','papers/NATIVE_RESPONSE_GEOMETRY/manuscript/spectral.tex','papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/drift/manuscript.tex']
sources=[]
for path in paths:
    data=git('show',PIN+':'+path)
    assert data==(REPO/path).read_bytes()
    sources.append({'path':path,'commit':PIN,'sha256':hashlib.sha256(data).hexdigest()})
assert git('--no-optional-locks','status','--porcelain=v1','--untracked-files=all')==status
assert git('branch','--show-current')==branch
result={'result':'PASS','purpose':'Check constants only; analytical proofs establish the theorem.',
 'fixed_parameters':{'epsilon':str(eps),'g':str(g),'lambda':str(lam),'k':['999/1000','1','1001/1000']},
 'domain':{'radius_lower':str(r),'radius_upper':str(R),'ordinary_phase_width':'pi/12'},
 'coefficient_min':str(a_min),'coefficient_max':str(a_max),'radial_magnitude_derivative_min':str(radial_derivative_min),
 'cos_D':interval(cosD),'convex_hull_radius_squared_lower_bound':interval(hull_radius_squared),
 'prestage_lower_modulus_bound':interval(lower_modulus),'prestage_upper_modulus_bound':str(upper_modulus),
 'H_derivative_radial_lower_bound':str(H_radial_min),'H_lipschitz_constant':interval(H_lipschitz),
 'q':interval(q),'phase_separation_factor':interval(qphase),'sigma_k':interval(sigma),
 'uniform_forcing_epsilon_R_sigma_k':interval(forcing),'E_residual_upper_bound_value':interval(residual),
 'S_residual_upper_bound_value':interval(residual_squared),
 'rigorous_coarse_bounds':{'E_limsup_less_than':'5270/1000000','S_limsup_less_than':'2778/100000000'},
 'proof_scope':{'state_updates':0,'parameter_sweeps':0,'old_certificate_replays':0,'repository_writes':0,'git_status_and_branch_unchanged':True},
 'sources':sources,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('sources','checker_sha256')},indent=2))
print('Receipt:',OUT)
