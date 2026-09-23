"""Independent algebra audit of the uploaded Paper D v0.1.

This imports no project/kernel code and executes none of Codex's verifiers.
Exact simplification checks supplement the accompanying written proof review.
The number of check groups is not a theorem count.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sympy as S

s, gap = S.symbols('s gap', positive=True)
p = (s + 2*gap)/(2*S.sqrt(3))
a = (1+S.sqrt(2))*s/2
u = [S.Matrix([1,0]), S.Matrix([-S.Rational(1,2),S.sqrt(3)/2]),
     S.Matrix([-S.Rational(1,2),-S.sqrt(3)/2])]
J = S.Matrix([[0,-1],[1,0]])
t = [J*x for x in u]
R60=S.Matrix([[S.Rational(1,2),-S.sqrt(3)/2],[S.sqrt(3)/2,S.Rational(1,2)]])
R120=S.simplify(R60**2)
A=[p*u[i]-s*t[i]/2 for i in range(3)]
B=[p*u[i]+s*t[i]/2 for i in range(3)]
H=[x for pair in zip(A,B) for x in pair]
D=[S.simplify(H[(i+1)%6]-H[i]) for i in range(6)]
lengths=[s,gap]*3
results=[]

def zero(expr):
    vals=list(expr) if isinstance(expr,S.MatrixBase) else [expr]
    return all(S.simplify(v)==0 for v in vals)
def det(v,w): return S.det(S.Matrix.hstack(v,w))
def record(name, predicates):
    vals=[bool(x) for x in predicates]
    results.append({'group':name,'evaluated_conditions':len(vals),'passed':all(vals)})
    if not all(vals):
        raise AssertionError((name,[i for i,v in enumerate(vals) if not v]))
O=[S.Matrix(x) for x in [(a,-s/2),(a,s/2),(s/2,a),(-s/2,a),(-a,s/2),(-a,-s/2),(-s/2,-a),(s/2,-a)]]
OD=[S.simplify(O[(i+1)%8]-O[i]) for i in range(8)]
record('octagon metrics and equal 45-degree turns',
 [zero(a-s/(2*S.tan(S.pi/8)))] +
 [zero(v.dot(v)-s*s) for v in OD] +
 [zero(OD[i].dot(OD[(i+1)%8])-s*s/S.sqrt(2)) for i in range(8)] +
 [zero(det(OD[i],OD[(i+1)%8])-s*s/S.sqrt(2)) for i in range(8)])
record('orthonormal C3 frames',
 [zero(u[i].dot(t[i])) and zero(u[i].dot(u[i])-1) and zero(t[i].dot(t[i])-1)
  and zero(R120*u[i]-u[(i+1)%3]) for i in range(3)])
record('directed edges and connectors',
 [zero(B[i]-A[i]-s*t[i]) and zero(A[(i+1)%3]-B[i]-gap*R60*t[i]) for i in range(3)])
record('closure and six turns',
 [zero(sum(D,S.zeros(2,1)))] +
 [zero(D[i].dot(D[i])-lengths[i]**2) and
  zero(D[i-1].dot(D[i])-lengths[i-1]*lengths[i]/2) and
  zero(det(D[i-1],D[i])-S.sqrt(3)*s*gap/2) for i in range(6)])
printed=[S.Matrix(x) for x in [(p,-s/2),(p,s/2),((s-gap)/(2*S.sqrt(3)),(s+gap)/2),
 (-(2*s+gap)/(2*S.sqrt(3)),gap/2),(-(2*s+gap)/(2*S.sqrt(3)),-gap/2),
 ((s-gap)/(2*S.sqrt(3)),-(s+gap)/2)]]
record('printed six vertices',[zero(H[i]-printed[i]) for i in range(6)])
V=[p*u[i]+S.sqrt(3)*p*t[i] for i in range(3)]
W=s+2*gap
record('support triangle vertices and length',
 [zero(u[i].dot(V[i])-p) and zero(u[(i+1)%3].dot(V[i])-p) and
  zero((V[(i+1)%3]-V[i]).dot(V[(i+1)%3]-V[i])-W*W) for i in range(3)])
record('equilateral corner cells and strict nonoverlap bound',
 [zero((V[i]-B[i]).dot(V[i]-B[i])-gap*gap) and
  zero((V[i]-A[(i+1)%3]).dot(V[i]-A[(i+1)%3])-gap*gap) for i in range(3)] +
 [zero(1-gap/W-S.Rational(1,2)-s/(2*W)),bool((s/(2*W)).is_positive)])
qh=(2*s+gap)/(2*S.sqrt(3))
nG=[R60*x for x in u]
record('closed halfplane hexagon: all vertices feasible and all boundary edges matched',
 [bool(S.simplify(p-u[i].dot(x)).is_nonnegative) and
  bool(S.simplify(qh-nG[i].dot(x)).is_nonnegative) for i in range(3) for x in H] +
 [zero(nG[i].dot(B[i])-qh) and zero(nG[i].dot(A[(i+1)%3])-qh) for i in range(3)])
area=S.simplify(sum(det(H[i],H[(i+1)%6]) for i in range(6))/2)
record('cyclic radius and area',
 [zero(x.dot(x)-(s*s+s*gap+gap*gap)/3) for x in H] +
 [zero(area-S.sqrt(3)*(s*s+4*s*gap+gap*gap)/4),
  zero(area-S.sqrt(3)*(W*W-3*gap*gap)/4)])
record('incircle criterion and regular coordinates',
 [zero(p-qh-(gap-s)/(2*S.sqrt(3)))] +
 [zero(H[i].subs(gap,s)-s*S.Matrix([S.cos(-S.pi/6+i*S.pi/3),S.sin(-S.pi/6+i*S.pi/3)])) for i in range(6)])
reflection=S.diag(1,-1)
record('C3, reflections, and regular-case C6 actions',
 [zero(R120*H[i]-H[(i+2)%6]) and zero(reflection*H[i]-H[(1-i)%6]) and
  zero((R60*H[i]-H[(i+1)%6]).subs(gap,s)) for i in range(6)])
record('complete octagon selected edges',
 [zero((p+a)*u[i]-a*u[i]-s*t[i]/2-A[i]) and
  zero((p+a)*u[i]-a*u[i]+s*t[i]/2-B[i]) for i in range(3)])
xi,z,zp=S.symbols('xi z zp', real=True)
pp=S.symbols('p',positive=True)
u3=[S.Matrix([*x,0]) for x in u]
t3=[S.Matrix([*x,0]) for x in t]
ez=S.Matrix([0,0,1])
def F(i,x,zz,pr): return pr*u3[i]+x*t3[i]+zz*ez
R30=S.Matrix([[S.sqrt(3)/2,-S.Rational(1,2),0],[S.Rational(1,2),S.sqrt(3)/2,0],[0,0,1]])
p0=a/S.sqrt(3)
P=[S.Matrix([-a/2-xi/2,S.sqrt(3)*a/2-S.sqrt(3)*xi/2,z]),
   S.Matrix([xi,0,z]),S.Matrix([a/2-xi/2,S.sqrt(3)*a/2+S.sqrt(3)*xi/2,z])]
record('Paper C printed rigid coordinate match',
 [zero(R30*F(i,xi,z,p0)+S.Matrix([0,a/S.sqrt(3),0])-P[j]) for i,j in enumerate([2,0,1])] +
 [zero(S.sqrt(3)*p0-s/2-s/S.sqrt(2))])
lam=(1+S.sqrt(2))/3
pstar=S.sqrt(3)*s/2
record('translation and fixed-centre shrink',
 [zero(pstar-p0-(2-S.sqrt(2))*s/(2*S.sqrt(3))),
  zero(S.sqrt(3)*p0-lam*s/2-lam*s),
  zero(lam*(S.sqrt(2)-1)-S.Rational(1,3)),
  zero(lam/S.Integer(2)-(1+S.sqrt(2))/6),bool((1-lam).is_positive)])
X,Y=S.symbols('X Y',nonnegative=True)
delta=S.sqrt(3)*pp-a
record('finite filled-face separation decomposition',
 [zero((F(i,a-X,z,pp)-F((i+1)%3,-a+Y,zp,pp)).dot(
        F(i,a-X,z,pp)-F((i+1)%3,-a+Y,zp,pp))-
       (delta**2+delta*(X+Y)+(X-Y)**2+X*Y+(z-zp)**2)) for i in range(3)] +
 [zero((S.sqrt(3)*pstar-a)-(2-S.sqrt(2))*s/2),zero(S.Rational(1,2)-lam/2-(2-S.sqrt(2))/6)])
q=S.symbols('q0:3',real=True); h=S.symbols('h0:3',real=True)
k=S.symbols('k0:3',real=True); eps,c=S.symbols('eps coupling',real=True)
r2=[q[i]**2+h[i]**2 for i in range(3)]
potential=eps*sum(r2[i]**2/4-k[i]*r2[i]/2 for i in range(3))+c*sum(
 (q[i]-q[j])**2+(h[i]-h[j])**2 for i in range(3) for j in range(i+1,3))/2
record('negative real gradient of the quoted pre-sync potential',
 [zero(-S.diff(potential,v[i])-(eps*v[i]*(k[i]-r2[i])+c*(sum(v)-3*v[i])))
  for v in [q,h] for i in range(3)])
# A scoped witness for precision of the corner-removal wording, not a new model.
# V_0 is not in the open interior of its own triangle, but violates the connector halfplane.
record('corner-removal boundary clarification witness',
 [zero(nG[0].dot(V[0])-qh-S.sqrt(3)*gap/2),bool((S.sqrt(3)*gap/2).is_positive)])
root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--pdf',type=Path,default=root/'PAPER_D_REFERENCE_SCAFFOLD_v0.1.pdf')
parser.add_argument('--output',type=Path,default=root/'GPT_PAPER_D_ALGEBRA_RESULTS_v0.1.json')
args=parser.parse_args()
pdf=args.pdf
if not pdf.is_file():
    parser.error(f'PDF not found: {pdf}; supply --pdf PATH')
out={'scope':'independent exact algebra; no project imports, no Codex-script rerun',
     'reviewed_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
     'sympy_version':S.__version__,'groups':results,
     'group_count':len(results),'all_passed':all(x['passed'] for x in results),
     'interpretation':'The written review, not a group count, supplies the mathematical disposition.'}
args.output.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
