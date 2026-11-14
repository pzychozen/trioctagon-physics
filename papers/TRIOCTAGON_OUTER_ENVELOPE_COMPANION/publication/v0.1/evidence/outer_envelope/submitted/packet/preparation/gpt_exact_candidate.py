"""New GPT symbolic planning check, not the requested complete hull proof.
Coordinates are a transcription of the inherited written fold maps.
"""
import json,sys
from pathlib import Path
import sympy as S
x=S.symbols('x',real=True);h=(S.sqrt(2)-1)/2;half=S.Rational(1,2)
loc=[(-half,-h),(-h,-half),(h,-half),(half,-h),(half,h),(h,half),(-h,half),(-half,h)]
o=S.Matrix([0,S.sqrt(3)/6,0]);vv=[];faces=[]
for k in range(3):
 face=[]
 for u,z in loc:
  v=[S.Matrix([-S.Rational(1,4)-u/2,S.sqrt(3)/4-S.sqrt(3)*u/2,z]),S.Matrix([u,0,z]),S.Matrix([S.Rational(1,4)-u/2,S.sqrt(3)/4+S.sqrt(3)*u/2,z])][k]-o
  v=v.applyfunc(S.simplify)
  i=next((i for i,q in enumerate(vv) if all(S.simplify(a-b)==0 for a,b in zip(v,q))),None)
  if i is None:i=len(vv);vv.append(v)
  face.append(i)
 faces.append(face)
edges=sorted(set(tuple(sorted((f[i],f[(i+1)%8]))) for f in faces for i in range(8)))
m=[(vv[i]+vv[j])/2 for i,j in edges];u=[((vv[j]-vv[i])/(2*h)).applyfunc(S.simplify) for i,j in edges]
q=[(a+x*b).applyfunc(S.expand) for a,b in zip(m,u)]+[(a-x*b).applyfunc(S.expand) for a,b in zip(m,u)]
ids=[4,8,16,20,30,36]
N=(q[ids[1]]-q[ids[0]]).cross(q[ids[2]]-q[ids[0]]).applyfunc(S.simplify)
d=S.simplify(N.dot(q[ids[0]]))
res=[S.factor(S.expand(N.dot(p)-d),extension=S.sqrt(2)) for p in q]
xstar=3*h
rx=[S.simplify(v.subs(x,xstar)) for v in res]
sg=[S.sign(v) for v in rx]
zero=[i for i,v in enumerate(rx) if v==0]
print('N=',N,'d=',d,'candidate x=',xstar,'R2=',S.expand(S.Rational(1,3)+xstar**2))
print('zero',zero,'nonzero signs',sorted(set(map(str,sg))))
print('res factors subset',[(i,str(res[i])) for i in ids])
record={'status':'PROPOSED_SYMBOLIC_LOCAL_WITNESS_NOT_FULL_CLASSIFICATION','basis':'inherited fold-map transcription, material cycles verified against source','sympy_version':S.__version__,'python_version':sys.version,'parameter':'x=t/w','faces':faces,'edges':edges,'point_order':'q[0:21]=E01+...E21+; q[21:42]=E01-...E21-','candidate_x':str(xstar),'candidate_R_squared_over_w_squared':str(S.expand(S.Rational(1,3)+xstar**2)),'chosen_ids_zero_based':ids,'plane_normal':[str(v) for v in N],'plane_offset':str(d),'residuals':[str(v) for v in res],'candidate_zero_ids':zero,'candidate_residual_signs':[str(s) for s in sg],'scope':'Only one proposed six-point supporting plane; no exhaustive interval, orbit, facet or uniqueness assertion.'}
Path('/mnt/data/outer_geometry_prep/EXACT_CANDIDATE_CHECK.json').write_text(json.dumps(record,indent=2))
