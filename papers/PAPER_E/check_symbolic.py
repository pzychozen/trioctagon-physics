"""Bounded exact algebra accompanying Paper E; no kernel import, scans or figures."""
import runtime
from runtime import ROOT
import sympy as S,json,sys
checks={}
def zero(name,expr):
    out=S.trigsimp(S.expand_trig(S.expand(expr)))
    checks[name]=bool(out==0);assert out==0,(name,out)
th,l,A,d=S.symbols('theta ell A d',real=True)
z=A*S.cos(3*(th-l)); M=S.Matrix([z*S.cos(th),z*S.sin(th),z])
zero('macro_cone',M[0]**2+M[1]**2-M[2]**2)
zero('macro_norm_squared',M.dot(M)-2*z*z)
zero('harmonic_second_derivative',S.diff(z,th,2)+9*z)
zero('planar_Mx',M[0]-A*(S.cos(4*th-3*l)+S.cos(2*th-3*l))/2)
zero('planar_My',M[1]-A*(S.sin(4*th-3*l)-S.sin(2*th-3*l))/2)
def R(a):return S.Matrix([[S.cos(a),-S.sin(a),0],[S.sin(a),S.cos(a),0],[0,0,1]])
def vector(name,x):
    for j,v in enumerate(x):zero(name+'_'+str(j),v)
vector('C3',M.subs(th,th+2*S.pi/3)-R(2*S.pi/3)*M)
vector('horizontal_reflection',M.subs(th,th+S.pi)-S.diag(1,1,-1)*M)
vector('theta_reflection',M.subs(th,-th)-S.diag(1,-1,1)*M.subs(l,-l))
vector('lock_shift',M.subs(l,l+d)-R(d)*M.subs(th,th-d))
for k in range(6):
    zero('extremum_'+str(k),z.subs(th,l+k*S.pi/3)-A*(-1)**k)
    zero('critical_point_'+str(k),S.diff(z,th).subs(th,l+k*S.pi/3))
    idx=[0,2,1,0,2,1][k];sgn=(-1)**k
    vector('visiting_order_'+str(k),M.subs(th,l+k*S.pi/3)-A*S.Matrix([S.cos(l+2*S.pi*idx/3),S.sin(l+2*S.pi*idx/3),sgn]))
x=S.Matrix(S.symbols('x0:3',real=True));y=S.Matrix(S.symbols('y0:3',real=True));C=x.cross(y)
zero('Gram_determinant',C.dot(C)-x.dot(x)*y.dot(y)+x.dot(y)**2)
zero('chirality_bound_slack',((x.dot(x)+y.dot(y))/2)**2-C.dot(C)-(x.dot(x)-y.dot(y))**2/4-x.dot(y)**2)
a,b=S.symbols('a b',real=True)
vector('complex_scaling',(a*x-b*y).cross(b*x+a*y)-(a*a+b*b)*C)
vector('conjugation',x.cross(-y)+C)
mx,my,mz,cx,cy,cz,alpha,beta=S.symbols('mx my mz cx cy cz alpha beta',real=True)
mm=S.Matrix([mx,my,mz]);cc=S.Matrix([cx,cy,cz]);tt=alpha*mm+beta*cc
zero('blend_norm',tt.dot(tt)-alpha**2*mm.dot(mm)-beta**2*cc.dot(cc)-2*alpha*beta*mm.dot(cc))
Q=lambda v:v[0]**2+v[1]**2-v[2]**2
zero('cone_defect',Q(tt)-alpha**2*Q(mm)-beta**2*Q(cc)-2*alpha*beta*(mx*cx+my*cy-mz*cz))
eps,g=S.symbols('eps g',real=True);ks=S.symbols('k0:3',real=True)
L=S.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]])
r=[x[j]**2+y[j]**2 for j in range(3)]
dx=S.Matrix([eps*(ks[j]-r[j])*x[j] for j in range(3)])+g*L*x
dy=S.Matrix([eps*(ks[j]-r[j])*y[j] for j in range(3)])+g*L*y
edges=sum((x[i]-x[j])**2+(y[i]-y[j])**2 for i in range(3) for j in range(i+1,3))
zero('Laplacian_sign',x.dot(L*x)+y.dot(L*y)+edges)
zero('intensity_budget',(x+dx).dot(x+dx)+(y+dy).dot(y+dy)-sum(r)-2*eps*sum(ks[j]*r[j]-r[j]**2 for j in range(3))+2*g*edges-dx.dot(dx)-dy.dot(dy))
V=eps*sum(r[j]**2/4-ks[j]*r[j]/2 for j in range(3))+g*edges/2
for j in range(3):zero('gradient_x_'+str(j),S.diff(V,x[j])+dx[j]);zero('gradient_y_'+str(j),S.diff(V,y[j])+dy[j])
vold=3*(S.Rational(2)**4/4-S.Rational(2)**2/2);vnew=3*(S.Rational(-4)**4/4-S.Rational(-4)**2/2)
checks['potential_increase_exact_witness']=bool(vold==6 and vnew==168)
assert checks['potential_increase_exact_witness']
results={'attribution':'New Codex bounded symbolic checks; proofs and hypotheses remain in manuscript',
         'python':sys.version,'sympy':S.__version__,'predicates':checks,'passed':sum(checks.values()),
         'potential_witness':{'eps':1,'k':[1,1,1],'omega_initial':[2,2,2],'omega_next':[-4,-4,-4],'V_initial':6,'V_next':168},
         'scope':'Polynomial/trigonometric identities, not historical-source execution or spatial-gap certification'}
(ROOT/'evidence/symbolic_results.json').write_text(json.dumps(results,indent=2)+'\n')
print('PASS',len(checks),'exact symbolic predicates')
