"""New candidate algebra only. Infinite-dimensional claims are proved in the review."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,sys
import sympy as S
ROOT=Path(__file__).resolve().parent.parent
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
groups=[]
def zero(expr):
    if isinstance(expr,S.MatrixBase):assert all(S.simplify(x)==0 for x in expr),expr
    else:assert S.simplify(expr)==0,expr
def record(id,title,details):
    groups.append({'id':id,'status':'PASS','title':title,'details':details});print(id+' PASS: '+title)

chi=S.symbols('chi',real=True)
M,L,delta,gain,kappa,beta,P,eps=S.symbols('M L delta a_o kappa beta_G P epsilon',positive=True)
d0=S.symbols('distance',positive=True)
tangent=S.Matrix([0,-S.sin(chi),S.cos(chi)])
A=S.Matrix([[1,0],[0,tangent[0]],[0,tangent[1]],[0,tangent[2]]])
zero(A.T*A-S.eye(2));zero(M*(1/S.sqrt(M))**2-1)
zero((gain*S.sqrt(M)/d0)/S.sqrt(M)-gain/d0)
Gram=S.diag(1,0,0,0);Gram[1:4,1:4]=tangent*tangent.T
zero(A*A.T-Gram)
inactive=S.Matrix([0,1,0,0]);zero(A.T*inactive)
zero(S.sqrt(2)*S.sqrt(2)*kappa-2*kappa)
record('E01','Tangent embedding, duplication normalization, Gram kernel and direct C6 factor',{'A':str(A),'pointwise_Gram_factor':'a_o^2 M / distance^2','inactive_receiving_direction':str(inactive),'note':'Nonzero normal-vector receiving fields lie in ker(C*); no inverse or contraction is assumed.'})

near=S.Matrix(S.symbols('en0:2',real=True));b=S.Matrix(S.symbols('b0:2',real=True))
far=S.Matrix(S.symbols('eg0:2',real=True));c=S.Matrix(S.symbols('c0:2',real=True))
a=S.sqrt(2)*near-b;d=S.sqrt(2)*far-c
PN=(a.dot(a)-b.dot(b))/2;PG=(c.dot(c)-d.dot(d))/2
rx=-near.dot(near)+S.sqrt(2)*near.dot(b)
receiving=-far.dot(far)+S.sqrt(2)*far.dot(c)
zero(rx+PN);zero(receiving-PG);zero(rx+(PN-PG)+receiving)
Nwork,Rwork=S.symbols('P_NC P_CR',real=True)
zero(-Nwork+(Nwork-Rwork+rx)+Rwork+PN)
record('E02','Near/far wave signs, sqrt(2) factors and full augmented cancellation',{'RX_added_power':str(S.expand(rx)),'receiving_power':str(S.expand(receiving)),'total_residual':'0','scope':'Bilinear identities for arbitrary effort vectors; no bound ||C||<=1.'})

# Exact polynomial characteristic check for arbitrary symbolic delay, on both sides of t=theta.
xi,t,theta=S.symbols('xi t theta',positive=True)
up0=xi+1;um0=2*xi+1
ain=lambda time:time+2
din=lambda time:3*time+1
up_early=S.integrate(ain(t-xi)**2,(xi,0,t))+S.integrate(up0.subs(xi,xi-t)**2,(xi,t,theta))
um_early=S.integrate(um0.subs(xi,xi+t)**2,(xi,0,theta-t))+S.integrate(din(t-theta+xi)**2,(xi,theta-t,theta))
Eearly=(up_early+um_early)/2
cearly=up0.subs(xi,theta-t);bearly=um0.subs(xi,t)
Powerearly=(ain(t)**2-bearly**2-cearly**2+din(t)**2)/2
zero(S.diff(Eearly,t)-Powerearly)
Elate=(S.integrate(ain(t-xi)**2,(xi,0,theta))+S.integrate(din(t-theta+xi)**2,(xi,0,theta)))/2
Powerlate=(ain(t)**2-din(t-theta)**2-ain(t-theta)**2+din(t)**2)/2
zero(S.diff(Elate,t)-Powerlate)
Einitial=S.integrate(up0**2+um0**2,(xi,0,theta))/2
zero(Eearly.subs(t,0)-Einitial);zero(Eearly.subs(t,theta)-Elate.subs(t,theta))
record('E03','Both characteristic orientations and energy across startup/fully delayed regimes',{'initial_profiles':['xi+1','2 xi+1'],'incoming_boundaries':['a(t)=t+2','d(t)=3t+1'],'initial_energy':str(S.expand(Einitial)),'early_energy':str(S.expand(Eearly)),'late_energy':str(S.expand(Elate)),'derivative_residuals':['0','0'],'corner_compatibility':'Intentionally not assumed; identity is integrated/energy-space.','scope':'Exact corroboration for symbolic positive theta, not a substitute for the L2 proof.'})

# Exponents in (U,L,T,G_o), with multiplication represented by addition.
R=S.Rational
def unit(*v):return S.Matrix(v)
uQ=unit(1,0,0,0);us=unit(0,1,0,0);ut=unit(0,0,1,0);ug=unit(0,0,0,1)
uk=-ut/2;uw=uQ-(us+ut)/2;uz=uQ-ug-ut/2;ub=2*ug+ut
zero(uk+uQ-us/2-uw)
zero(uk+us/2+uw-(uQ-ut))
zero(ug+us/2+uw-(ub+uz-ut))
zero(ug-us/2+uz-uw)
zero(2*uw+ut+2*us-(2*uQ+us))
zero(ub+2*uz+us-(2*uQ+us))
zero(ub+2*us-2*ug-2*us-ut)
record('E04','Abstract units for both ports, added force, stocks and witness time bound',{'basis':['U','L','T','G_o'],'wave_exponents':list(map(str,uw)),'zeta_exponents':list(map(str,uz)),'beta_G_exponents':list(map(str,ub)),'stock_exponents':list(map(str,2*uQ+us)),'force_exponents':list(map(str,uQ-ut)),'interpretation':'Consistent proposed bookkeeping, not physical calibration.'})

Cc_bound=2*S.sqrt(2)*kappa*gain*P*L/delta
zeta_slope=S.sqrt(2)*Cc_bound/beta
zero(zeta_slope-4*kappa*gain*P*L/(beta*delta))
effort_bound=S.sqrt(2)*gain*S.sqrt(M)/delta*zeta_slope*eps
direct_lower=kappa*P/S.sqrt(2*M)
critical=beta*delta**2/(16*gain**2*M*L)
zero((effort_bound/direct_lower).subs(eps,critical)-S.Rational(1,2))
record('E05','Early-arrival bound and exact factor 16 in the return witness',{'zeta_slope':str(zeta_slope),'effort_to_direct_ratio':str(S.simplify(effort_bound/direct_lower)),'critical_epsilon':str(critical),'ratio_at_critical':'1/2','strict_conclusion':'epsilon below the critical value gives effort < direct_lower/2; with direct > lower, return < -direct_lower/2.','scope':'Positivity intervals and positive-measure delay sublevels are proved analytically.'})

result={'task':'NATIVE_CAUSAL_TRANSPORT_STORAGE_01','observed_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'sympy':S.__version__,'status':'PASS','group_count':len(groups),'groups':groups,'scope':'Five new exact-algebra corroboration groups. No accepted scientific suite rerun, no simulation or parameter scan, no inference of infinite-dimensional existence from algebra.'}
(ROOT/'logs/EXACT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','new_algebra_groups':len(groups)},indent=2))
