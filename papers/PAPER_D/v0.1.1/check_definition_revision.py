"""New Codex D-01/D-02 substitution checks only. No predecessor suite imports.

Coordinates and figure sources remain byte-identical to reviewed v0.1.
These four grouped checks support definition precision, not four new theorems.
"""
import runtime
from runtime import ROOT
import sympy as S
import hashlib,json
s,g=S.symbols('s g',positive=True);r=S.sqrt(3);a=(1+S.sqrt(2))*s/2;p=(s+2*g)/(2*r)
u=[S.Matrix([1,0]),S.Matrix([-S.Rational(1,2),r/2]),S.Matrix([-S.Rational(1,2),-r/2])]
J=S.Matrix([[0,-1],[1,0]]);T=[J*v for v in u];R=S.Matrix([[S.Rational(1,2),-r/2],[r/2,S.Rational(1,2)]])
A=[p*u[i]-s*T[i]/2 for i in range(3)];B=[p*u[i]+s*T[i]/2 for i in range(3)];H=[x for pair in zip(A,B) for x in pair]
qh=(2*s+g)/(2*r);n=[R*x for x in u];V=[p*u[i]+r*p*T[i] for i in range(3)];checks=[]
def z(x):return all(S.simplify(v)==0 for v in x) if isinstance(x,S.MatrixBase) else S.simplify(x)==0
def check(name,values):
    values=[bool(v) for v in values];checks.append({'name':name,'evaluated_predicates':len(values),'pass':all(values)});assert all(values),name
# The whole side is a convex combination of its two listed vertices. Its image
# therefore belongs to the affine image of the filled convex hull, not an 8-point set.
t=S.symbols('t',real=True)
def F(i,x,h,rad=p):return S.Matrix([rad*u[i][0]+x*T[i][0],rad*u[i][1]+x*T[i][1],h])
height=(2*t-1)*s/2
check('D01 continuous side, affine image and full seam identities',[z((1-t)*S.Matrix([a,-s/2])+t*S.Matrix([a,s/2])-S.Matrix([a,height]))]+
 [z(F(i,a,height)-((1-t)*F(i,a,-s/2)+t*F(i,a,s/2))) for i in range(3)]+
 [z(F(i,a,height,a/r)-F((i+1)%3,-a,height,a/r)) for i in range(3)])
check('D02 all six vertices satisfy both halfplane families',[S.simplify(p-u[i].dot(x)).is_nonnegative for i in range(3) for x in H]+[S.simplify(qh-n[i].dot(x)).is_nonnegative for i in range(3) for x in H])
check('D02 intended connector endpoints lie on cut lines',[z(n[i].dot(B[i])-qh) and z(n[i].dot(A[(i+1)%3])-qh) for i in range(3)])
check('D02 strict corner-apex exclusion witness',[z(n[i].dot(V[i])-qh-r*g/2) and (r*g/2).is_positive for i in range(3)])
out={'attribution':'New Codex bounded definition-revision check, 2026-09-23','groups':checks,'passed':sum(x['pass'] for x in checks),'total':len(checks),'old_31_42_suites_rerun':False,'supplied_GPT_17_suite_rerun':False,'new_geometry':False}
(ROOT/'evidence/definition_revision_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
