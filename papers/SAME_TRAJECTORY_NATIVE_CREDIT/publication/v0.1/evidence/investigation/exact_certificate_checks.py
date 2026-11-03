"""Exact algebra supporting the written certificate; no trajectory/PDE evolution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
import sympy as s

W=Path(__file__).resolve().parent
checks=[]
def zero(identifier,purpose,expression):
    entries=list(expression) if isinstance(expression,s.MatrixBase) else [expression]
    residuals=[s.simplify(s.trigsimp(v)) for v in entries]
    assert all(v==0 for v in residuals),(identifier,residuals)
    checks.append({'id':identifier,'purpose':purpose,'pass':True,'simplified_residuals':[str(v) for v in residuals]})

phi,delta=s.symbols('phi delta',real=True)
G,eps=s.symbols('G epsilon_c',positive=True)
alpha,beta,eta,kappa,c,m,d,omega,tau,T=s.symbols('alpha beta eta_N kappa c m d omega tau T',positive=True)
R,k,F,A,u0,D=s.symbols('R k F_max A abs_f0 D',positive=True)
coord=s.symbols('s',real=True)
normal=s.Matrix([[0,2,s.sqrt(3)],[0,2,-s.sqrt(3)]])/s.sqrt(7)
rotation=s.Matrix([[s.cos(delta),-s.sin(delta),0],[s.sin(delta),s.cos(delta),0],[0,0,1]])
K=G*normal*rotation
gram=K*K.T
zero('S01','Registration Gram matrix, valid for every yaw',gram-G**2*s.Matrix([[1,s.Rational(1,7)],[s.Rational(1,7),1]]))
q=s.symbols('q')
zero('S02','Two squared singular values; their maximum is 8G^2/7 by positivity',gram.charpoly(q).as_expr()-(q-8*G**2/7)*(q-6*G**2/7))
a0=s.Matrix([1,s.cos(phi),1]);b0=s.Matrix([0,s.sin(phi),0]);f0=K*a0.cross(b0)
zero('S03','Launch norm squared is exactly three',a0.dot(a0)+b0.dot(b0)-3)
expected=G*s.sin(phi)/s.sqrt(7)*s.Matrix([-2*s.sin(delta)+s.sqrt(3),-2*s.sin(delta)-s.sqrt(3)])
zero('S04','Both registered launch drive entries with the original signs',f0-expected)
zero('S05','Nonzero port difference coefficient; positivity uses 0<phi<pi/12 and G>0',f0[0]-f0[1]-2*s.sqrt(3)*G*s.sin(phi)/s.sqrt(7))
zero('S06','Exact squared launch drive norm',f0.dot(f0)-G**2*s.sin(phi)**2*(6+8*s.sin(delta)**2)/7)
tent=(1-coord/eps)/eps
zero('S07','Normalized continuous tent mass',2*s.integrate(tent,(coord,0,eps))-1)
zero('S08','Single tent squared L2 norm',2*s.integrate(tent**2,(coord,0,eps))-2/(3*eps))
zero('S09','Single tent squared first weak derivative norm, using its affine halves',2*s.integrate(s.diff(tent,coord)**2,(coord,0,eps))-2/eps**3)

# Chain-rule coefficients: all fields denote their scaled values at tau=kappa*t.
xt,pt,rt,zt,rs,ps,Jy,Bf,Bz,y=s.symbols('x_tau p_tau r_tau z_tau r_s p_s JTy Bf Bz yhat')
original=[kappa*xt+eta/(2*alpha)*(eta/kappa)*Jy,
          eta*pt+c*eta/kappa*rs-(eta*Bf-eta*Bz),
          eta*rt+c*eta/kappa*ps,
          eta*zt-kappa/beta*(eta/kappa)*y]
scaled=[xt+eta**2/(2*alpha*kappa**2)*Jy,
        pt+c/kappa*rs-Bf+Bz,rt+c/kappa*ps,zt-y/beta]
zero('S10','Exact four rescaled equations after the chain rule',s.Matrix([original[i]/[kappa,eta,eta,eta][i]-scaled[i] for i in range(4)]))
fy=s.symbols('f_dot_yhat')
zero('S11','Original total native power conversion',eta*(eta/kappa)*fy-eta**2/kappa*fy)
yp,ym,zp,zm=s.symbols('y_plus y_minus z_plus z_minus')
zero('S12','Weighted collocated receiver/carrier energy terms cancel',-yp*zp-ym*zm+beta*(zp*yp/beta+zm*ym/beta))
coeff_p=s.sin(omega*tau)/omega;coeff_z=1-s.cos(omega*tau)
zero('S13','Comparison p and z solve their driven equations and start at zero',s.Matrix([
    s.diff(coeff_p,tau)-(1-coeff_z),
    (s.diff(coeff_z,tau)-m*coeff_p/beta).subs(m,beta*omega**2),
    coeff_p.subs(tau,0),coeff_z.subs(tau,0)]))
witness=3*s.pi/(2*omega)
zero('S14','Comparison witness has z coefficient one and negative total-power coefficient',s.Matrix([
    coeff_z.subs(tau,witness)-1,m*u0**2*coeff_p.subs(tau,witness)+m*u0**2/omega]))
integral=s.integrate(s.sin(omega*tau),(tau,0,s.pi/omega))-s.integrate(s.sin(omega*tau),(tau,s.pi/omega,witness))
zero('S15','Absolute sine integral through three quadrants',integral-3/omega)
drift=s.integrate(eta**2*k*R*m*F*tau/(2*alpha*kappa**2),(tau,0,T))
zero('S16','Core drift factor one-fourth from integration',drift-eta**2*k*R*m*F*T**2/(4*alpha*kappa**2))
Aval=eta**2*k**2*R**2*m*F/(4*alpha)
zero('S17','Drive drift constant from the ball Lipschitz bound',k*R*drift-Aval*T**2/kappa**2)
Bprimef=s.symbols('Bprime_f0')
linear_on_comparison_r=-c/kappa*coeff_p*Bprimef
comparison_r_tau=s.Integer(0)
zero('S18','Signed propagation residual is L_kappa V0 minus V0_tau in the r equation',linear_on_comparison_r-comparison_r_tau-(-c/kappa*Bprimef*s.sin(omega*tau)/omega))
zero('S19','Integrated drive forcing error has factor one-third',s.integrate(s.sqrt(m)*A*tau**2/kappa**2,(tau,0,T))-s.sqrt(m)*A*T**3/(3*kappa**2))
zero('S20','Finite propagation forcing bound at T',c*s.sqrt(d)*u0/(kappa*omega)*integral-3*c*s.sqrt(d)*u0/(kappa*omega**2))
C1=3*c*s.sqrt(m*d)*u0**2/omega**2
C2=m*A*T**3*(F+u0/3)
error=A*T**2/kappa**2*m*F*T+u0*s.sqrt(m)*(3*c*s.sqrt(d)*u0/(kappa*omega**2)+s.sqrt(m)*A*T**3/(3*kappa**2))
zero('S21','Exact collection of both total-power error terms',error-C1/kappa-C2/kappa**2)
zero('S22','Threshold allocations give D/4 for each error term and leave -D/2',s.Matrix([
    C1/(4*C1/D)-D/4,C2/(s.sqrt(4*C2/D)**2)-D/4,-D+D/4+D/4+D/2]))
width=s.symbols('delta_interval',positive=True)
zero('S23','Half-margin over a symmetric interval gives the claimed native gain',s.integrate(eta**2*D/(4*kappa),(tau,-width,width))-eta**2*D*width/(2*kappa))
Vnorm=s.symbols('Vnorm',nonnegative=True)
zero('S24','External stock scaling and uniform window upper bound',((eta/kappa)**2*Vnorm**2/2).subs(Vnorm,s.sqrt(m)*F*T)-eta**2*m*F**2*T**2/(2*kappa**2))

# Exponents in the inherited unit basis (U,L,T,amplitude). Addition of these
# exponent vectors represents multiplication of quantities, not physical units.
units={
 'm':s.Matrix([0,-1,0,0]),'d':s.Matrix([0,-3,0,0]),
 'c':s.Matrix([0,1,-1,0]),'k':s.Matrix([1,1,-1,-2]),'R':s.Matrix([0,0,0,1]),
 'F':s.Matrix([1,1,-1,0]),'alpha':s.Matrix([2,1,0,-2]),'beta':s.Matrix([0,-1,2,0]),
 'T':s.Matrix([0,0,1,0])}
du=units
du['omega']=(du['m']-du['beta'])/2
du['A']=2*du['k']+2*du['R']+du['m']+du['F']-du['alpha']
du['D']=du['m']-du['omega']+2*du['F']
du['C1']=du['c']+(du['m']+du['d'])/2+2*du['F']-2*du['omega']
du['C2']=du['m']+du['A']+3*du['T']+du['F']
zero('S25','Threshold ratios dimensionless, A has drive/time^2, D and both C terms have power units',s.Matrix.vstack(
    du['C1']-du['D'],du['C2']-du['D'],du['A']-(du['F']-2*du['T']),du['D']-s.Matrix([2,1,-1,0])))

record={'executed_utc':datetime.now(timezone.utc).isoformat(),'python':sys.executable,'python_version':sys.version,
    'sympy_version':s.__version__,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'purpose':'New exact finite-expression checks of this proposed certificate only. No PDE evolution, simulation, parameter sweep, model import or prior scientific helper replay.',
    'limitations':'These checks do not establish strong regularity, the energy inequality, operator domains, disjoint profile supports, order inequalities, continuity or the PDE theorem; those are justified in the written proof. Positivity and quantifiers are analytical hypotheses.',
    'checks':checks,'passed':len(checks),'total':len(checks),'all_passed':all(r['pass'] for r in checks),
    'unit_exponents_basis':['U','L','T','native_amplitude'],'unit_exponents':{key:list(map(str,v)) for key,v in units.items()},
    'historical_checks_reexecuted':False}
(W/'EXACT_CERTIFICATE_RESULTS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'total':len(checks),'sympy':s.__version__,'scope':'Exact algebra only; analytical proof separate'}))
