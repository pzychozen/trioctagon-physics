"""Bounded exact checks of displayed manuscript identities; no scientific sweep."""
import sys, json, itertools
from pathlib import Path
sys.dont_write_bytecode=True
import sympy as s
from accepted_coordinates import *
results=[]
def check(name,claim):
    assert bool(claim), name
    results.append({"claim":name,"status":"PASS"})
check("printed geometry equals preserved source",compare_source()["matched"])
q=s.symbols("q_A q_B q_C",real=True);p=s.symbols("p_A p_B p_C",real=True)
a=M(q);b=M(p);om=a+s.I*b
vs=[q[i]*tangents[i]+p[i]*ez for i in range(3)]
A=M(3,3,lambda i,j:q[i]*p[j]-p[i]*q[j]);chir=a.cross(b)
for i in range(3):
    n,t=normals[i],tangents[i];v=vs[i]
    J=M([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
    Pi=transport(i,i)
    check(f"face {i}: J, inverse, norm and ambient projector",
          zero(J*J+Pi) and zero(t.dot(v)+s.I*ez.dot(v)-om[i])
          and zero(v.dot(v)-q[i]**2-p[i]**2) and zero(Pi-(s.eye(3)-n*n.T)))
    check(f"face {i}: affine cyclic placement",zero(origin+R*(centres[i]-origin)-centres[(i+1)%3]))
check("all nine transports equal projected matched rotations",
      all(zero(transport(i,j)-transport(i,i)*R**((i-j)%3)) for i in range(3) for j in range(3)))
check("all 27 full ambient compositions",
      all(zero(transport(i,j)*transport(j,k)-transport(i,k)) for i,j,k in itertools.product(range(3),repeat=3)))
check("all nine transported signed areas",
      all(zero(normals[i].dot(vs[i].cross(transport(i,j)*vs[j]))-A[i,j]) for i in range(3) for j in range(3)))
check("antisymmetry, diagonal and cyclic triple",zero(A+A.T) and zero(M([A[1,2],A[2,0],A[0,1]])-chir))
eps,g=s.symbols("eps g",real=True);ks=s.symbols("k_A k_B k_C",real=True)
L=s.ones(3)-3*s.eye(3)
pre=om+eps*M([om[i]*(ks[i]-q[i]**2-p[i]**2) for i in range(3)])+g*L*om
for i in range(3):
    f=vs[i]+eps*(ks[i]-vs[i].dot(vs[i]))*vs[i]+g*sum((transport(i,j)*vs[j]-vs[i] for j in range(3) if j!=i),s.zeros(3,1))
    check(f"face {i}: pre-sync equation-to-coordinate identity",zero(tangents[i].dot(f)+s.I*ez.dot(f)-pre[i]))
delta=s.symbols("delta",real=True)
check("phase rotation dictionary",zero(s.cos(delta)*q[0]-s.sin(delta)*p[0]+s.I*(s.sin(delta)*q[0]+s.cos(delta)*p[0])-(q[0]+s.I*p[0])*(s.cos(delta)+s.I*s.sin(delta))))
for name,G,Q in [("C3",R,P),("horizontal",H,s.eye(3)),("vertical",V,S)]:
    perm=[list(Q[:,i]).index(1) for i in range(3)]
    vv=[None]*3
    for i in range(3):vv[perm[i]]=G*vs[i]
    AA=M(3,3,lambda i,j:s.expand(normals[i].dot(vv[i].cross(transport(i,j)*vv[j]))))
    ZZ=M([AA[1,2],AA[2,0],AA[0,1]])
    check(name+": spatial area matrix and two-determinant law",zero(AA-G.det()*Q*A*Q.T) and zero(ZZ-G.det()*Q.det()*Q*chir))
check("all six pure channel permutations",
      all(zero((Q*a).cross(Q*b)-Q.det()*Q*chir) for Q in (s.eye(3)[:,perm] for perm in itertools.permutations(range(3)))))
cr,ci=s.symbols("c_r c_i",real=True)
check("complex scaling and common-phase specialization",zero((cr*a-ci*b).cross(ci*a+cr*b)-(cr**2+ci**2)*chir))
check("conjugation oddness",zero(a.cross(-b)+chir))
check("coupling projector identity",zero(L+3*(s.eye(3)-s.ones(3)/3)))
e=M([1,0,0]);w=P*e-R*e
check("realizable cyclic witness has squared difference 2-sqrt(3)",zero(M([0,1,0]).cross(M([0,0,1]))-e) and zero(w.dot(w)-(2-s.sqrt(3))) and not zero(w))
check("Figure 4 signed area",s.Rational(30,100)*s.Rational(28,100)-s.Rational(8,100)*s.Rational(10,100)==s.Rational(76,1000))
check("Figure 5 cyclic slot order",list(P*M([1,2,3]))==[3,1,2])
out={"attribution":"Codex manuscript algebra checks, 2026-09-23","sympy":s.__version__,
     "scope":"Displayed identities only; proofs remain in manuscript; no trajectory, sweep or new model.",
     "check_groups":len(results),"all_passed":True,"results":results}
(ROOT/"evidence/manuscript_algebra.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf8")
print(json.dumps(out))
