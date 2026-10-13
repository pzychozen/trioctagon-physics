"""Independent exact checks and bounded finite illustrations; no native imports."""
import json, sys
from pathlib import Path
import sympy as s
import mpmath as mp

OUT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,actual,expected=0):
    if isinstance(actual,s.MatrixBase):
        residual=(actual-expected).applyfunc(s.simplify)
        ok=residual==s.zeros(*residual.shape)
    else:
        residual=s.simplify(s.trigsimp(actual-expected))
        ok=residual==0
    if not ok: raise AssertionError((name,residual))
    checks.append({'name':name,'category':'exact','passed':True,'residual':str(residual)})
def fact(name,value):
    assert value,name
    checks.append({'name':name,'category':'exact','passed':True})

q,z,x,t,tau=s.symbols('q z x t tau',real=True)
L,m,hbar,a,p=s.symbols('L m hbar a p',positive=True)
k=s.symbols('k',integer=True)
N=s.symbols('N',integer=True,positive=True)
check('Fourier_multiplier',2-s.exp(2*s.I*q)-s.exp(-2*s.I*q),4*s.sin(q)**2)
check('paired_sine',s.sin(s.pi-q),s.sin(q))
check('fixed_mode_limit_via_sinc',s.limit((2*s.pi*k/L)**2*(s.sin(q)/q)**2,q,0),(2*s.pi*k/L)**2)
check('trace_limit_p_three_halves',2*(L/(2*s.pi))**3*s.zeta(3),L**3*s.zeta(3)/(4*s.pi**3))
check('cubic_length_scale',(4/L**2)**(-s.Rational(3,2)),L**3/8)
check('inverse_cube_difference_factor',(q-z)*(q*q+q*z+z*z),q**3-z**3)
check('uniform_error_inequality_coefficient',(q**3/6)*(3*q**2)/(2*q/s.pi)**3,s.pi**3*q**2/16)
check('summed_error_coefficient',L**3/(4*s.pi**3)*s.pi**3/16*s.pi**2/N**2,L**3*s.pi**2/(64*N**2))
check('tail_integral',s.integrate(x**-3,(x,a,s.oo)),1/(2*a**2))
check('dispersion_series',s.series((s.sin(q)/q)**2,q,0,6).removeO(),1-q*q/3+2*q**4/45)
check('dispersion_inequality_square_certificate',(1-q*q/6)**2-(1-q*q/3),q**4/36)
check('midpoint_dispersion',(s.sin(s.pi/2)/(s.pi/2))**2,4/s.pi**2)

for n in (3,4,5,6):
    B=s.zeros(n)
    incidence=s.zeros(n)
    for j in range(n):
        B[j,j]=2
        B[j,(j-1)%n]=-1
        B[j,(j+1)%n]=-1
        incidence[j,j]=-1
        incidence[j,(j+1)%n]=1
    check(f'quadratic_form_N{n}',incidence.T*incidence,B)
    check(f'self_adjoint_N{n}',B.T,B)
    check(f'zero_mode_N{n}',B*s.ones(n,1),s.zeros(n,1))
    expected=[s.simplify(4*s.sin(s.pi*j/n)**2) for j in range(n)]
    polynomial=s.prod(z-val for val in expected)
    cp=B.charpoly()
    check(f'characteristic_polynomial_N{n}',cp.as_expr().subs(cp.gen,z),polynomial)
    P=s.ones(n)/n
    pseudoinverse=(B+P).inv()-P
    check(f'finite_inverse_trace_N{n}',s.trace(pseudoinverse)/n**2,(1-s.Rational(1,n*n))/12)
    full=sum((n*n*val)**(-s.Rational(3,2)) for val in expected[1:])
    if n==3: target=2/(81*s.sqrt(3))
    elif n==4: target=(1+4*s.sqrt(2))/512
    elif n==5:
        target=s.Rational(2,125)*(((5-s.sqrt(5))/2)**(-s.Rational(3,2))+((5+s.sqrt(5))/2)**(-s.Rational(3,2)))
    else: target=2*s.Rational(36)**(-s.Rational(3,2))+2*s.Rational(108)**(-s.Rational(3,2))+s.Rational(144)**(-s.Rational(3,2))
    check(f'exact_T_N{n}',full,target)
    check(f'exact_sine_sum_N{n}',sum(s.sin(s.pi*j/n) for j in range(1,n)),s.cot(s.pi/(2*n)))

for n in (3,4,5,6,16,32):
    M=(n-1)//2
    indices=[j for k0 in range(1,M+1) for j in (k0,n-k0)]
    if n%2==0: indices.append(n//2)
    fact(f'complete_pair_partition_N{n}',sorted(indices)==list(range(1,n)))

wave=s.exp(2*s.pi*s.I*k*x/L)/s.sqrt(L)
E=hbar**2/(2*m)*(2*s.pi*k/L)**2
check('continuum_eigen_equation',-hbar**2/(2*m)*s.diff(wave,x,2),E*wave)
check('periodic_wave',wave.subs(x,x+L),wave)
check('periodic_derivative',s.diff(wave,x).subs(x,x+L),s.diff(wave,x))
check('normalization_continuum',s.integrate(s.conjugate(wave)*wave,(x,0,L)),1)
check('quantum_trace_scaling',(hbar**2*a/(2*m))**(-p),(2*m/hbar**2)**p*a**(-p))
check('unitary_spectral_factor',s.conjugate(s.exp(-s.I*t*E/hbar))*s.exp(-s.I*t*E/hbar),1)
check('unitary_group_law',s.exp(-s.I*t*E/hbar)*s.exp(-s.I*tau*E/hbar),s.exp(-s.I*(t+tau)*E/hbar))
check('Schrodinger_phase_equation',s.I*hbar*s.diff(s.exp(-s.I*t*E/hbar),t),E*s.exp(-s.I*t*E/hbar))
check('finite_band_coefficient',E*s.pi**2*k*k/(3*N*N)/hbar,2*hbar*s.pi**4*k**4/(3*m*L**2*N**2))
phi=(1+s.sqrt(5))/2
limit=L**3*s.zeta(3)/(4*s.pi**3)
gamma=s.zeta(3)/(s.pi*s.E*phi)
check('historical_calibration',4*s.pi**2/(s.E*phi)*limit/L**3,gamma)
check('quantum_calibration_mass_cancellation',4*s.pi**2/(s.E*phi*L**3)*(hbar**2/(2*m))**s.Rational(3,2)*(2*m/hbar**2)**s.Rational(3,2)*limit,gamma)
check('cosecant_expansion',s.series(1/s.sin(z)**2,z,0,2).removeO(),z**-2+s.Rational(1,3))
check('finite_inverse_trace_factor',(N*N-1)/3/(4*N*N),(1-N**-2)/12)
finitepart=1/(2*s.pi*z)*s.cot(s.pi*z/2)-1/(s.pi**2*z*z)
check('negative_finite_part_series',s.series(finitepart,z,0,4).removeO(),-s.Rational(1,12)-s.pi**2*z*z/720)
check('zeta_minus_one',s.zeta(-1),-s.Rational(1,12))
check('bulk_integral',N/(2*s.pi)*s.integrate(s.sin(s.pi*x/N),(x,0,N)),N*N/s.pi**2)
check('Mellin_single_mode',s.integrate(x**(p-1)*s.exp(-a*x),(x,0,s.oo))/s.gamma(p),a**(-p))

# Dimension vectors use the order (mass, length, time).
mass=s.Matrix([1,0,0]); length=s.Matrix([0,1,0]); time=s.Matrix([0,0,1])
hbar_dim=mass+2*length-time
energy_dim=mass+2*length-2*time
check('energy_units',2*hbar_dim-mass-2*length,energy_dim)
check('inverse_energy_trace_units',s.Rational(3,2)*(mass-2*hbar_dim)+3*length,-s.Rational(3,2)*energy_dim)

mp.mp.dps=60
lim=mp.zeta(3)/(4*mp.pi**3)
illustrations=[]
for n in (3,4,5,6,16,32):
    vals=[4*n*n*mp.sin(mp.pi*j/n)**2 for j in range(1,n)]
    full=mp.fsum(v**(-mp.mpf('1.5')) for v in vals)
    M=(n-1)//2; even=int(n%2==0)
    paired=2*mp.fsum(vals[k0-1]**(-mp.mpf('1.5')) for k0 in range(1,M+1))+even/(mp.mpf(8)*n**3)
    bound=mp.pi**2*mp.fsum(mp.mpf(1)/j for j in range(1,M+1))/(64*n*n)+1/(8*mp.pi**3*M*M)+even/(mp.mpf(8)*n**3)
    residual=abs(full-paired)
    assert residual<mp.mpf('1e-55') and abs(full-lim)<=bound
    illustrations.append({'N':n,'T_unit':mp.nstr(full,50),'ratio':mp.nstr(full/lim,50),
                          'absolute_error':mp.nstr(abs(full-lim),50),'proved_error_bound':mp.nstr(bound,50),
                          'pairing_residual':mp.nstr(residual,8),'numerical_checks_passed':True,
                          'table_T':mp.nstr(full,12),'table_ratio':mp.nstr(full/lim,9)})
record={'date':'2026-10-13','python':sys.version,'executable':sys.executable,'sympy':s.__version__,
        'mpmath':mp.__version__,'exact_check_count':len(checks),'all_exact_passed':True,
        'exact_checks':checks,'finite_illustrations_precision_digits':60,'finite_illustrations':illustrations,
        'limit_unit':mp.nstr(lim,50),'limit_table':mp.nstr(lim,12),
        'scope':'Symbolic identities and six fixed finite spectral sums, no historical or production imports, trajectories, simulations or parameter searches. Infinite-limit and inequality proofs are in the manuscript.'}
(OUT/'evidence/CHECK_RESULTS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
texpath=OUT/'SRG_QUANTUM_RING_v0.1.tex'
tex=texpath.read_text(encoding='utf-8')
if '--fill-table' in sys.argv:
    for row in illustrations:
        tex=tex.replace(r'\text{TABLE'+str(row['N'])+'}',row['table_T'])
        tex=tex.replace(r'\text{RATIO'+str(row['N'])+'}',row['table_ratio'])
    tex=tex.replace(r'\text{TABLEINF}',record['limit_table'])
    texpath.write_text(tex,encoding='utf-8')
else:
    for row in illustrations:
        assert row['table_T'] in tex and row['table_ratio'] in tex
    assert record['limit_table'] in tex
print(json.dumps({'exact_checks_passed':len(checks),'finite_illustrations':len(illustrations),'limit':record['limit_table']}))
