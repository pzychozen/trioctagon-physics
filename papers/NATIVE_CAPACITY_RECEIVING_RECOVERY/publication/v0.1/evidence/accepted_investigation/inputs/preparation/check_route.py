"""Preparatory algebra checks for a proposed certificate, not independent proof."""
import sympy as s
import json, sys, argparse
from pathlib import Path
G,alpha,eta,m,beta,kappa,phi,t=s.symbols('G alpha eta m beta kappa phi t', positive=True)
v=s.Matrix([1,1,1]); e=s.Matrix([1,-1,0])/s.sqrt(2)
K=G/s.sqrt(7)*s.Matrix([[s.sqrt(2),s.sqrt(2),s.sqrt(3)], [s.sqrt(2),s.sqrt(2),-s.sqrt(3)]])
def crossmat(x):
    return s.Matrix([[0,-x[2],x[1]],[x[2],0,-x[0]],[-x[1],x[0],0]])
B=K*crossmat(v); ell=s.simplify(B*e)
results=[]
def zero(name, expr):
    expr=s.simplify(expr)
    if isinstance(expr,s.MatrixBase): passed=all(s.simplify(i)==0 for i in expr)
    else: passed=expr==0
    results.append({'name':name,'passed':bool(passed),'residual':str(expr)})
    assert passed,(name,expr)
def positive(name,expr):
    expr=s.simplify(expr)
    assert expr.is_positive,(name,expr)
    results.append({'name':name,'passed':True,'exact_positive_gap':str(expr)})
zero('rank-one tangent drive',B-ell*e.T)
zero('ell norm',ell.dot(ell)-20*G**2/7)
zero('native rate squared / nu squared', (eta**2*m*ell.dot(ell)/(2*alpha))/(eta**2*m*(8*G**2/7)*3/(2*alpha))-s.Rational(5,6))
q0=s.Matrix([0,s.cos(phi)-1,0]); b0=s.Matrix([0,s.sin(phi),0])
C=alpha*(1-s.cos(phi))
zero('augmented initial norm squared',2*alpha*(q0.dot(q0)+b0.dot(b0))-4*C)
zero('active reference capacity',alpha*(e.dot(b0))**2 - C*s.cos(phi/2)**2)
a,b,w=s.symbols('a b w',positive=True)
x0=s.symbols('x0',real=True)
w2=a*a+b*b
w=s.sqrt(w2)
X=x0*(b*b+a*a*s.cos(w*t))/w2
P=x0*a/w*s.sin(w*t)
Z=x0*a*b/w2*(1-s.cos(w*t))
zero('reference native equation',s.diff(X,t)+a*P)
zero('reference carrier equation',(s.diff(P,t)-(a*X-b*Z)).subs(w**2,w2))
zero('reference receiver equation',s.diff(Z,t)-b*P)
nu=s.symbols('nu',positive=True)
zero('reference half-period receiver amplitude', (2*a*b/(a*a+b*b)).subs({a:s.sqrt(s.Rational(5,6))*nu,b:nu/3})-2*s.sqrt(30)/17)
zero('reference omega squared', ((a*a+b*b).subs({a:s.sqrt(s.Rational(5,6))*nu,b:nu/3})/nu**2)-s.Rational(17,18))
positive('rate condition gap',s.Rational(1,4)-s.Rational(1,9)-s.Rational(1,10000))
positive('T*nu < 20/3 squared bound',(s.Rational(20,3))**2-(s.Rational(44,7))**2*s.Rational(18,17))
positive('1/sqrt3 < 3/5 squared',s.Rational(9,25)-s.Rational(1,3))
positive('sqrt2 < 10/7 squared',s.Rational(100,49)-2)
positive('propagation coefficient < 4 squared',16-(s.Rational(72,17)**2)*s.Rational(5,6))
zero('combined error sum',s.Rational(5,84)+s.Rational(1,25)-s.Rational(209,2100))
positive('uniform error below 1/10',s.Rational(1,10)-s.Rational(209,2100))
positive('receiving reference amplitude > 5/8 squared',s.Rational(120,289)-s.Rational(25,64))
positive('cos(phi/2)>24/25 at maximal phase',1-s.Rational(1,80000)-s.Rational(24,25))
zero('receiver margin',s.Rational(5,8)*s.Rational(24,25)-s.Rational(1,10)-s.Rational(1,2))
zero('receiver share',s.Rational(1,4)/(s.Rational(1,4)+s.Rational(1,100))-s.Rational(25,26))
positive('native recovery from access time >24/25',1-s.Rational(1,100)/s.Rational(1053,4096)-s.Rational(24,25))
# Check the substitution used only for incompatibility of sufficient bounds.
nu0,om,Fmax,fmag,q=s.symbols('nu0 om Fmax fmag q',positive=True)
A=nu0**2*Fmax/2
B2_over_Lambda=om*A*(2*s.pi/om)**3/(3*fmag)
zero('old threshold ratio substitution', 2*B2_over_Lambda*om**2/(q*nu0**2)-8*s.pi**3*Fmax/(3*q*fmag))
x=s.symbols('x')
zero('elementary pi upper bound identity',s.integrate(x**4*(1-x)**4/(1+x*x),(x,0,1))-(s.Rational(22,7)-s.pi))
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path('PREPARATORY_ALGEBRA.json'))
args=parser.parse_args()
args.output.write_text(json.dumps({'status':'preparatory, not independently accepted', 'python':sys.version,'sympy':s.__version__,'count':len(results),'checks':results},indent=2)+'\n')
print(json.dumps({'passed':len(results),'ell':str(ell),'linear_tangent':str(B)},indent=2))
