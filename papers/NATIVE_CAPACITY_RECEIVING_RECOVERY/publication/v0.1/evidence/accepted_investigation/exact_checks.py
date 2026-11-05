"""Independent focused exact-algebra checks for the new receiving/recovery proof.

This script was written from the published equations and the independently
derived argument. It does not import, read or execute the preparatory script,
historical suites, numerical trajectories or parameter scans.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,platform,sys,time
import sympy as s

results=[]
def zero(expr):
    if isinstance(expr,s.MatrixBase):
        assert all(s.simplify(s.trigsimp(x))==0 for x in expr),expr
    else:assert s.simplify(s.trigsimp(expr))==0,expr
def group(code,name,payload):
    results.append({"id":code,"name":name,"status":"PASS","exact_results":payload})
def rational_positive(x):
    x=s.factor(x);assert x.is_Rational and x>0,x
    return str(x)
start=time.perf_counter()
alpha,beta,eta,kappa,m,d,c,G,k,R,nu,Fmax,fmag,q=s.symbols(
    "alpha beta eta kappa m d c G k R nu Fmax fmag q",positive=True)
phi=s.symbols("phi",real=True)
omega=s.sqrt(m/beta)
old_A=nu**2*Fmax/2
old_S=2*s.pi/omega
old_B2=s.sqrt(m)*old_A*old_S**3/3
old_Lambda=s.sqrt(beta)*fmag
threshold=s.simplify((2*old_B2/(q*old_Lambda))*omega**2/nu**2)
zero(threshold-8*s.pi**3*Fmax/(3*q*fmag))
compat=s.Rational(1,4)-(s.Rational(1,10000)+s.Rational(1,9))
group("EC01","P3 threshold substitution and new-regime P4 compatibility",{
 "old_squared_rate_lower_bound":str(threshold),"new_rate_condition_squared_gap":rational_positive(compat),
 "scope":"The Fmax/fmag >= 1 and 0<q<=1/5 argument is proved in prose; no old recovery fraction is imported."})

K=G/s.sqrt(7)*s.Matrix([[s.sqrt(2),s.sqrt(2),s.sqrt(3)],[s.sqrt(2),s.sqrt(2),-s.sqrt(3)]])
def cross(v):
    x,y,z=v;return s.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])
v=s.Matrix([1,1,1]);e=s.Matrix([1,-1,0])/s.sqrt(2)
D=K*cross(v);ell=s.simplify(D*e);ell2=s.simplify(ell.dot(ell))
zero(D-ell*e.T);zero(K*e)
assert K.rank()==2 and D.rank()==1
zero(ell2-20*G**2/7)
ratio=s.simplify(ell2/((8*G**2/7)*3));zero(ratio-s.Rational(5,6))
group("EC02","Exact rank-two registration and rank-one tangent",{
 "D":str(D),"ell":str(ell),"ell_squared":str(ell2),"K_rank":K.rank(),"D_rank":D.rank(),
 "native_rate_squared_over_nu_squared":str(ratio)})

a=s.Matrix(s.symbols("a1:4",real=True));b=s.Matrix(s.symbols("b1:4",real=True))
u=s.Matrix(s.symbols("u1:4",real=True));y=s.Matrix(s.symbols("y1:3",real=True))
w=K.T*y;mu=eta/(2*alpha)
drive=K*a.cross(b)
J=drive.jacobian(list(a)+list(b))
native=-mu*J.T*y
zero(native-s.Matrix.vstack(mu*w.cross(b),-mu*w.cross(a)))
subs={a[i]:v[i]+u[i] for i in range(3)}
zero(drive.subs(subs)-D*b-K*u.cross(b))
native_shift=native.subs(subs)
lin=s.Matrix.vstack(s.zeros(3,1),-mu*D.T*y)
nonlinear=s.Matrix.vstack(mu*w.cross(b),-mu*w.cross(u))
zero(native_shift-lin-nonlinear)
group("EC03","Jacobian differentiation and exact nonlinear decomposition",{
 "native_cross_product_identity":"PASS","shifted_drive_equals_Db_plus_K_u_cross_b":"PASS",
 "all_six_native_residual_components":"identically zero"})

linmat=s.zeros(7)
linmat[:3,3:5]=-eta*s.sqrt(m)/(2*alpha)*D.T
linmat[3:5,:3]=eta*s.sqrt(m)*D
linmat[3:5,5:7]=-kappa*s.sqrt(m/beta)*s.eye(2)
linmat[5:7,3:5]=kappa*s.sqrt(m/beta)*s.eye(2)
weight=s.diag(2*alpha,2*alpha,2*alpha,1,1,1,1)
zero(weight*linmat+linmat.T*weight)
XN,V=s.symbols("X_N V",nonnegative=True)
gap=s.expand((XN**2+V**2)**2-(XN**2*V**2+XN**4/4))
zero(gap-(3*XN**4/4+XN**2*V**2+V**4))
assert all(a>=0 for a in s.Poly(gap,XN,V).coeffs())
group("EC04","Auxiliary factor 2 alpha and nonlinear norm coefficient",{
 "weighted_tangent_native_port_receiver_matrix":"W A + A^T W = 0",
 "nonlinear_squared_bound_gap":str(gap),
 "scope":"The spatial periodic product rule and norm regularization are written analytical arguments."})

u0=s.Matrix([0,s.cos(phi)-1,0]);b0=s.Matrix([0,s.sin(phi),0])
C=alpha*(1-s.cos(phi))
zero(2*alpha*(u0.dot(u0)+b0.dot(b0))-4*C)
h0=(e.T*b0)[0];X0=s.sqrt(2*alpha)*h0
zero(X0+s.sqrt(alpha)*s.sin(phi))
bperp=s.simplify(b0-e*h0)
zero(D*bperp)
zero(s.expand_trig(X0**2/2-C*s.cos(phi/2)**2))
zero(K*(v+u0).cross(b0)-D*b0)
group("EC05","Exact initial deviation and static reference components",{
 "initial_auxiliary_norm_squared":"4*C","active_X0":str(X0),"inactive_imaginary_component":str(bperp),
 "D_times_inactive_component":"zero","active_half_stock":"C*cos(phi/2)^2",
 "sign":"X0<0 on the declared positive phase interval; inequality justified in the written proof."})

wn,wr,t=s.symbols("omega_N omega_R t",positive=True)
x0=s.symbols("X0",real=True);wp=s.sqrt(wn**2+wr**2)
XX=x0*(wr**2+wn**2*s.cos(wp*t))/wp**2
PP=x0*wn*s.sin(wp*t)/wp
ZZ=x0*wn*wr*(1-s.cos(wp*t))/wp**2
zero(s.diff(XX,t)+wn*PP)
zero(s.diff(PP,t)-wn*XX+wr*ZZ)
zero(s.diff(ZZ,t)-wr*PP)
zero(s.Matrix([XX.subs(t,0)-x0,PP.subs(t,0),ZZ.subs(t,0)]))
zero(s.trigsimp(s.expand(XX**2+PP**2+ZZ**2-x0**2)))
zero(PP.subs(t,s.pi/wp))
zero(s.Matrix([PP.subs(t,2*s.pi/wp),ZZ.subs(t,2*s.pi/wp)]))
group("EC06","Coupled active oscillator, exact data and reference landmarks",{
 "three_ODE_residuals":"identically zero","initial_residuals":"zero",
 "active_norm_conservation":"X^2+P^2+Z^2=X0^2","carrier_at_tR":"zero","external_at_tF":"zero"})

ellnorm=s.sqrt(ell2);n=s.simplify(ell/ellnorm)
zero(n.dot(n)-1);zero(D.T*n-ellnorm*e)
wn_def=eta*s.sqrt(m)*ellnorm/s.sqrt(2*alpha)
wr_def=kappa*s.sqrt(m/beta)
zero(wn_def**2/(eta**2*m*(8*G**2/7)*3/(2*alpha))-s.Rational(5,6))
# The carrier is scalar in physical space. Keep its weak derivatives as
# independent formal symbols, and subtract the two full linear operators.
ps,rs,Bp,Bm=s.symbols("p_s r_s B_plus B_minus",real=True)
z=s.Matrix(s.symbols("z1:3",real=True))
profile=s.Matrix([[Bp,Bm]])
def linear_operator(speed):
    return s.Matrix.vstack(
        s.zeros(3,1),-mu*D.T*y,
        s.Matrix([-speed*rs+(eta*profile*D*b-kappa*profile*z)[0]]),
        s.Matrix([-speed*ps]),kappa*y/beta)
residual=(linear_operator(c)-linear_operator(0)).subs(rs,0)
zero(residual-s.Matrix([0,0,0,0,0,0,0,-c*ps,0,0]))
gamma=c*s.sqrt(d/m)
zero(c**2*d/m-gamma**2)
tau=s.symbols("tau",real=True)
abs_sine=s.integrate(s.sin(tau),(tau,0,s.pi))-s.integrate(s.sin(tau),(tau,s.pi,2*s.pi))
zero(abs_sine-4)
group("EC07","Reference embedding, first-derivative residual coefficient and full-period integral",{
 "D_transpose_n":"|ell|*e","propagation_residual":"(0,0,0,-c*p0_s,0) in block coordinates",
 "squared_residual_norm_coefficient":"gamma^2=c^2*d/m","absolute_sine_period_integral":str(abs_sine),
 "scope":"No second spatial derivative or PDE regularity inference is made by this finite check."})

L,Y0,T=s.symbols("L Y0 T",positive=True)
majorant=Y0/(1-L*Y0*t)
zero(s.diff(majorant,t)-L*majorant**2)
primitive=Y0/(1-L*Y0*t)-Y0
zero(s.diff(primitive,t)-L*majorant**2)
theta=s.symbols("theta",positive=True)
zero(primitive.subs(t,T)-Y0*(L*Y0*T)/(1-L*Y0*T))
Ldef=eta*k*s.sqrt(m)/(2*alpha)
nudeff=eta*k*R*s.sqrt(m/(2*alpha))
halfphase=s.symbols("h",positive=True)
zero((Ldef*2*s.sqrt(alpha)*halfphase*T)/(nudeff*T)-s.sqrt(2)*halfphase/R)
group("EC08","Majorant integral and normalized theta identity",{
 "rational_envelope_differential_identity":"M=Y0/(1-L*Y0*t) satisfies M'=L*M^2; the proof's Q satisfies Q'<=L*Q^2",
 "integrated_nonlinear_bound":"Y0*theta/(1-theta)",
 "theta":"sqrt(2)/R*sqrt(1-cos(phi))*nu*T in normalized amplitudes",
 "scope":"Positive-denominator comparison for the actual norm is supplied separately in prose."})

x=s.symbols("x",real=True)
numer=x**4*(1-x)**4
quot,rem=s.div(s.expand(numer),1+x*x)
zero(quot-(x**6-4*x**5+5*x**4-4*x**2+4));zero(rem+4)
polyint=s.integrate(quot,(x,0,1));zero(polyint-s.Rational(22,7))
zero(1/(1+x*x)-(1-x*x)-x**4/(1+x*x))
group("EC09","Elementary exact pi bounds",{
 "positive_integrand_division_quotient":str(quot),"remainder":str(rem),
 "polynomial_integral":str(polyint),
 "identity":"integral_0^1 x^4(1-x)^4/(1+x^2) dx = 22/7-pi",
 "lower_bound_identity":"1/(1+x^2)-(1-x^2)=x^4/(1+x^2); hence pi>8/3",
 "scope":"Strict positivity on (0,1), and integral arctan(1)=pi/4, are justified analytically."})

margins={
 "time_square_gap":s.Rational(20,3)**2-(2*s.Rational(22,7))**2*s.Rational(18,17),
 "inverse_R_square_gap":s.Rational(3,5)**2-s.Rational(1,3),
 "propagation_factor_square_gap":16-s.Rational(72,17)**2*s.Rational(5,6),
 "sqrt2_square_gap":s.Rational(10,7)**2-2,
 "error_margin_below_one_tenth":s.Rational(1,10)-(s.Rational(5,84)+s.Rational(1,25)),
 "theta_denominator_at_limit":1-s.Rational(1,25)}
for val in margins.values():rational_positive(val)
zero(s.Rational(10,7)*(s.Rational(1,25)/(1-s.Rational(1,25)))-s.Rational(5,84))
zero(s.Rational(5,84)+s.Rational(1,25)-s.Rational(209,2100))
zero(s.Rational(5,6)+s.Rational(1,9)-s.Rational(17,18))
group("EC10","Strict time, theta, propagation and total-error rational margins",{k:str(v) for k,v in margins.items()})

coefficient=s.simplify(2*(s.sqrt(s.Rational(5,6)))*(s.Rational(1,3))/s.Rational(17,18))
zero(coefficient-2*s.sqrt(30)/17)
recv_margins={
 "receiver_factor_square_gap":s.Rational(120,289)-s.Rational(25,64),
 "phase_cosine_floor_gap":1-s.Rational(1,100)**2/8-s.Rational(24,25),
 "positive_reverse_triangle_margin":s.Rational(3,5)-s.Rational(1,10)}
for val in recv_margins.values():rational_positive(val)
zero(s.Rational(5,8)*s.Rational(24,25)-s.Rational(3,5))
zero((s.Rational(1,2)**2*2)/2-s.Rational(1,4))
zero((s.Rational(1,10)**2*2)/2-s.Rational(1,100))
group("EC11","Reference reception, positive reverse triangle and storage factors",{
 "reference_receiver_factor":str(coefficient),**{k:str(v) for k,v in recv_margins.items()},
 "original_stock_conversion":"1/2 times squared weighted norm; thresholds C/4 and C/100"})

Cap,aex,bgap,fgap,rex=s.symbols("C a b f r",positive=True)
HR=Cap*(s.Rational(1,4)+aex)
HC=Cap*(s.Rational(1,100)-bgap)
EF=Cap*(s.Rational(1,100)-fgap)
ER=Cap*(s.Rational(1,4)+rex)
zero(HR/(HR+HC)-s.Rational(25,26)-Cap*(aex+25*bgap)/(26*(HR+HC)))
zero(s.Rational(1,25)-EF/HR-Cap*(aex+25*fgap)/(25*HR))
zero(1-EF/ER-s.Rational(24,25)-Cap*(rex+25*fgap)/(25*ER))
zero(ER-EF-s.Rational(6,25)*Cap-Cap*(rex+fgap))
exact_RA=1-s.Rational(1,100)/s.Rational(1053,4096)
zero(exact_RA-s.Rational(25301,26325))
group("EC12","All stock-ratio and net-recovery arithmetic",{
 "receiver_share_positive_gap":"C*(a+25*b)/(26*(HR+HC))",
 "receiver_retention_upper_gap":"C*(a+25*f)/(25*HR)",
 "recovery_R_positive_gap":"C*(r+25*f)/(25*ER)",
 "capacity_amount_excess":"C*(r+f)",
 "precise_recovery_A_lower_bound":str(exact_RA),
 "gap_above_24_over_25":rational_positive(exact_RA-s.Rational(24,25)),
 "scope":"Positivity of actual denominators and range restrictions on residual gaps are proved in prose."})

target=s.symbols("nu_target",positive=True)
eta_choice=target*s.sqrt(2*alpha)/(k*R*s.sqrt(m))
kappa_choice=target*s.sqrt(beta/m)/3
zero(nudeff.subs(eta,eta_choice)-target)
zero(wr_def.subs(kappa,kappa_choice)-target/3)
group("EC13","Finite fixed parameter construction",{
 "native_rate_under_eta_selection":"nu_target","receiver_rate_under_kappa_selection":"nu_target/3",
 "requirement":"nu_target >= 100*c*sqrt(d/m), fixed before phase"})

U,Len,Time,Amp=s.symbols("U Length Time NativeAmplitude",positive=True)
da=U**2*Len/Amp**2;db=Time**2/Len;dk=U*Len/(Time*Amp**2)
dm=1/Len;dd=1/Len**3;dc=Len/Time;dR=Amp;dell=dk*Amp
expected_units={
 "nu_squared":(dm*dk**2*dR**2/da,Time**-2),
 "omega_N_squared":(dm*dell**2/da,Time**-2),
 "omega_R_squared":(dm/db,Time**-2),
 "gamma_squared":(dc**2*dd/dm,Time**-2),
 "nonlinear_L":(dk*s.sqrt(dm)/da,1/(U*s.sqrt(Len)*Time)),
 "theta":((dk*s.sqrt(dm)/da)*(U*s.sqrt(Len))*Time,1),
 "eta_threshold":((dc*s.sqrt(dd/dm))*s.sqrt(da)/(dk*dR*s.sqrt(dm)),1),
 "kappa_selection":((1/Time)*s.sqrt(db/dm),1)}
for actual,targetunit in expected_units.values():zero(actual-targetunit)
group("EC14","Restored native-amplitude and storage units",{
 key:str(s.simplify(value[0])) for key,value in expected_units.items()})

assert len(results)==14 and all(r["status"]=="PASS" for r in results)
ap=argparse.ArgumentParser();ap.add_argument("--output-dir",type=Path,default=Path(__file__).resolve().parent)
args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
script=Path(__file__).read_bytes()
out={"utc":datetime.now(timezone.utc).isoformat(),"status":"PASS","independent_check_groups":len(results),"groups":results,
 "script_sha256":hashlib.sha256(script).hexdigest(),
 "limits":"Exact finite-dimensional algebra/arithmetic checks only. The written proof supplies global regularity, periodic Sobolev integration, zero-norm regularization, nonlinear scalar comparison, positivity, quantifiers and interpretation. No trajectories, parameter scans, inherited suites or preparatory scientific script were executed."}
(args.output_dir/"EXACT_ALGEBRA_RESULTS.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
execution={"utc":out["utc"],"status":"PASS","python":sys.executable,"python_version":sys.version,"sympy_version":s.__version__,
 "platform":platform.platform(),"argv":sys.argv,"isolated_mode":sys.flags.isolated,"dont_write_bytecode":sys.dont_write_bytecode,
 "elapsed_seconds":time.perf_counter()-start,"script_sha256":out["script_sha256"],"check_groups":len(results),
 "results_sha256":hashlib.sha256((args.output_dir/"EXACT_ALGEBRA_RESULTS.json").read_bytes()).hexdigest(),
 "preparatory_or_historical_scientific_code_executed":False}
(args.output_dir/"EXACT_CHECK_EXECUTION.json").write_text(json.dumps(execution,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"PASS","independent_groups":len(results),"sympy":s.__version__,"python":sys.version.split()[0],"script_sha256":out["script_sha256"]},indent=2))
