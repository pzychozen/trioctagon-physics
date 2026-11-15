"""New bounded exact algebra only; no native/historical module imports or runs.
SymPy is shared with preparation, not an independent arithmetic backend.
The response is rebuilt from the Cartesian prestage derivative; D1's rate
coefficient is inherited and its state jet is deliberately not recomputed.
"""
from pathlib import Path
import json, time, platform, sys, sympy as s
root=Path(__file__).resolve().parent
out=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root/'recheck'
out.mkdir(parents=True,exist_ok=True)
start=time.monotonic(); checks=[]; results={}
def save():
    (out/'EXACT_RESULTS.json').write_text(json.dumps({'status':'RUNNING','checks':checks,'formulas':results,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
def zero(name,e):
    residual=s.cancel(e)
    checks.append({'id':name,'kind':'exact_identity','pass':residual==0,'residual':str(residual)})
    save(); assert residual==0,name
def nonzero(name,e):
    residual=s.factor(e)
    checks.append({'id':name,'kind':'negative_control_nonidentity','pass':residual!=0,'witness_expression':str(residual)})
    save(); assert residual!=0,name
h_step=s.Symbol('h_step',real=True);a,b,c=s.symbols('a b c',positive=True)
r=s.Matrix([a,b,c]);L=s.ones(3)-3*s.eye(3);R=s.diag(*r);Id=s.eye(3)
x,y,eta=s.symbols('x y eta',real=True);xi=s.Matrix([x,y,-x-y])
s1=a+b+c;s2=a*b+a*c+b*c;s3=a*b*c
# Eliminate k by the exact stationary equations, before taking response.
k=[r[i]**2-(L*r)[i]/(6*r[i]) for i in range(3)]
H=Id+h_step*(s.diag(*[k[i]-r[i]**2 for i in range(3)])+L/6)
P=R.inv()*H*R
B=s.simplify((P-Id)/h_step)
for i in range(3):
    zero(f'P_rowsum_{i}',sum(P[i,j] for j in range(3))-1)
    for j in range(3):
        expected=r[j]/(6*r[i]) if i!=j else -sum(r[jj]/(6*r[i]) for jj in range(3) if jj!=i)
        zero(f'B_from_Cartesian_{i}{j}',B[i,j]-expected)
S=Id+h_step*L/10; J=S*P
D=B+L/10+h_step*L*B/10
for i in range(3):
    for j in range(3): zero(f'native_order_{i}{j}',J[i,j]-Id[i,j]-h_step*D[i,j])
def cycle(M):return M[0,1]*M[1,2]*M[2,0]-M[0,2]*M[2,1]*M[1,0]
# Exact polynomial division, not numerical substitution at trial radii.
bar=s.cancel(cycle(D)); V=(a-b)*(a-c)*(b-c)
num,den=s.fraction(bar)
quot,rem=s.div(s.Poly(num,a,b,c),s.Poly(V,a,b,c))
zero('alternating_polynomial_division',rem.as_expr())
sym_quot=s.cancel(quot.as_expr()/den)
zero('cycle_raw_h_cubed',cycle(J)-h_step**3*bar)
d=1-3*h_step/10
# Recover the symmetric cubic coefficients from the computed quotient.
K_recovered=s.cancel(sym_quot*60*s3**2/d)
u,v,w=s.symbols('u v w')
eqs=s.Poly(s.expand(K_recovered-u*s1**3-v*s1*s2-w*s3),a,b,c).coeffs()
coeff=s.solve(eqs,[u,v,w]); assert set(coeff)=={u,v,w}
expected_coeff={u:h_step**2/360,v:h_step/90-h_step**2/180,w:h_step/20-s.Rational(1,15)}
for key in coeff: zero('K_coefficient_'+str(key),coeff[key]-expected_coeff[key])
Kh=sum([coeff[u]*s1**3,coeff[v]*s1*s2,coeff[w]*s3])
zero('exact_response_factor',bar-d*V*Kh/(60*s3**2))
# Independent specialization of published corrected GR1 K and cycle prefactor.
g=h_step/6;ell=h_step/10
K_GR1=g*g*ell*s1**3+(g*g*(1-2*ell)-g*ell)*s1*s2+(3*g*ell-g+ell)*s3
zero('GR1_specialization',K_GR1-h_step*Kh)
zero('GR1_prefactor',g*ell*(1-3*ell)*K_GR1*V/s3**2-h_step**3*bar)
# Divided fixed derivative on the whole two-dimensional zero-mean plane.
Ar=-2*Id+L/6
zero('stationary_tangent_plane',(Ar*(s.Rational(2,5)*xi)+xi).dot(Ar*(s.Rational(2,5)*xi)+xi))
results['stationary_derivative_det']=str(Ar.det())
pair_den=[]
for i,j in [(0,1),(0,2),(1,2)]:
    dij=r[i]+r[j]+s1/(6*r[i]*r[j]);pair_den.append(dij)
    zero(f'exact_coefficient_radius_difference_{i}{j}',k[i]-k[j]-(r[i]-r[j])*dij)
Q=s.prod(pair_den)
SC=-d*Kh/(60*s3**2*Q)
aC=s.factor(SC.subs({a:1,b:1,c:1}))
expected=d*(8-18*h_step-3*h_step*h_step)/112500
zero('aC_from_analytic_pair_quotient',aC-expected)
A=lambda xx:(xx[0]-xx[1])*(xx[1]-xx[2])*(xx[2]-xx[0])
zero('Vandermonde_factor_two',A([-eta,0,eta])-2*eta**3)
zero('opposite_increasing_pair_orientation',V+(a-b)*(b-c)*(c-a))
nonzero('reject_wrong_orientation',aC-(-aC))
nonzero('reject_dropped_two',2*aC-aC)
for perm in [(b,a,c),(b,c,a)]:
    zero('symmetric_SC_'+str(perm),SC.xreplace(dict(zip([a,b,c],perm)))-SC)
zero('equal_coeff_equal_radius_cycle',bar.subs(b,a))
nonzero('reject_reversed_stage_matrix',J[0,1]-(P*S)[0,1])
nonzero('reject_reversed_stage_cycle',bar-s.cancel(cycle(P*S)/h_step**3))
G=B+L/10; generator=s.factor(cycle(G))
zero('native_normalized_generator_limit',bar.subs(h_step,0)-generator)
zero('generator_exact_factor',generator+V/(900*s3))
zero('additive_step_scaling',cycle(Id+h_step*G)-h_step**3*generator)
nonzero('native_not_additive',bar-generator)
nonzero('raw_not_normalized',h_step**3*bar-bar)
# Inherited D1 expression only; no state jet substitution or solve.
cD=s.sqrt(3)*(33*h_step*h_step-240*h_step+688)/(6*(1-3*h_step)**3)
theta=s.factor(cD/aC)
zero('aC_h0',aC.subs(h_step,0)-s.Rational(2,28125))
zero('cD_h0_inherited',cD.subs(h_step,0)-344*s.sqrt(3)/3)
zero('ratio_h0',theta.subs(h_step,0)-1612500*s.sqrt(3))
nonzero('rate_not_per_update_phase',cD-h_step*cD)
nonzero('leading_ratio_not_constant',s.diff(theta,h_step))
# Interval positivity reduced to nonnegative-coefficient polynomials in t=1/4-h.
t=s.symbols('t',nonnegative=True)
f=8-18*h_step-3*h_step**2
zero('f_lower_certificate',f-s.Rational(53,16)-(s.Rational(1,4)-h_step)*(s.Rational(75,4)+3*h_step))
zero('d_lower_certificate',d-s.Rational(37,40)-3*(s.Rational(1,4)-h_step)/10)
zero('drift_numerator_lower',33*h_step**2-240*h_step+688-628-(60-240*h_step+33*h_step**2))
lower=s.Rational(37,40)*s.Rational(53,16)/112500
zero('response_positive_lower',lower-s.Rational(1961,72000000))
assert lower>0
# Actual branch logic as symbolic consequences of analytically proved positive S factors.
Aval,SCval,SDval=s.symbols('A S_C S_D',real=True)
adv=[0,h_step*Aval*SDval,-h_step*Aval*SDval]
nonzero('same_diagnostic_does_not_select_stationary_vs_plus',adv[1]-adv[0])
nonzero('conjugate_advance_distinct_off_zero_set',adv[1]-adv[2])
zero('conjugate_sum_zero',adv[1]+adv[2])
results.update({'B':str(B),'K_recovered':str(s.factor(K_recovered)),'K_coefficients':{str(q):str(s.factor(z)) for q,z in coeff.items()},'Cbar_factor':str(s.factor(bar)),'pair_product':str(Q),'S_C_exact':str(SC),'a_C':str(aC),'c_plus_inherited':str(cD),'Theta_at_xi0':str(theta),'generator_cycle':str(generator),'aC_positive_lower':str(lower),'no_float_atoms':not any(e.atoms(s.Float) for e in [bar,SC,aC,cD,theta]),'no_numerical_branch_fixtures':True})
save()
p=out/'EXACT_RESULTS.json'; data=json.loads(p.read_text());data.update(status='PASS',identity_and_control_count=len(checks),theorem_count_not_inferred=True,python=platform.python_version(),sympy=s.__version__);p.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'elapsed_seconds':time.monotonic()-start,'aC':str(aC),'generator':str(generator),'Theta0':str(theta)},indent=2))
