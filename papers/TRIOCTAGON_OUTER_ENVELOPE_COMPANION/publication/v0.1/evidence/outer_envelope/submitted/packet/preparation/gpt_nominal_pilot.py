"""GPT planning diagnostic, not a proof or certified hull classification.
Uses Paper C fold maps as transcribed in the spherical-edge synthesis.
No project kernel code is imported, and no repo files are changed.
"""
import json
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
w=1.; h=(np.sqrt(2)-1)/2
local=[(-.5,-h),(-h,-.5),(h,-.5),(.5,-h),(.5,h),(h,.5),(-h,.5),(-.5,h)]
F=[lambda u,z:np.array([-.25-u/2,np.sqrt(3)/4-np.sqrt(3)*u/2,z]),lambda u,z:np.array([u,0,z]),lambda u,z:np.array([.25-u/2,np.sqrt(3)/4+np.sqrt(3)*u/2,z])]
o=np.array([0,np.sqrt(3)/6,0]);verts=[];faces=[]
for f in F:
 face=[]
 for u,z in local:
  p=f(u,z)-o
  k=next((i for i,v in enumerate(verts) if np.linalg.norm(p-v)<1e-12),None)
  if k is None:k=len(verts);verts.append(p)
  face.append(k)
 faces.append(face)
edges=sorted(set(tuple(sorted((face[i],face[(i+1)%8]))) for face in faces for i in range(8)))
m=np.array([(verts[i]+verts[j])/2 for i,j in edges]);directions=np.array([(verts[j]-verts[i])/(2*h) for i,j in edges])
def hull(x):
 pts=np.concatenate([m+x*directions,m-x*directions]);pp=[]
 for p in pts:
  if not any(np.linalg.norm(p-q)<1e-9 for q in pp):pp.append(p)
 pp=np.array(pp);cv=ConvexHull(pp)
 groups=[]
 for eq in cv.equations:
  if not any(np.linalg.norm(eq-e)<1e-7 for e in groups):groups.append(eq)
 facets=[np.where(np.abs(pp@eq[:3]+eq[3])<1e-7)[0] for eq in groups]
 hist={str(n):sum(len(f)==n for f in facets) for n in sorted(set(map(len,facets)))}
 return {'x':float(x),'R_over_w':float(np.sqrt(1/3+x*x)),'vertices':len(pp),'facets':len(facets),'facet_sizes':hist}
xs=[h,.21,.25,.3,.4,.49,.5,.51,.6,.7071067811865476,.8,1.,1.1,(1+np.sqrt(2))/2,1.21,1.3,1.5,2.,3.,10.,100.]
r={'status':'UNCERTIFIED_PLANNING_DIAGNOSTIC','source':'Paper C fold formulas and spherical-edge synthesis eq:fold, eq:exits','method':'binary64 ConvexHull; approximate coplanarity grouping only','point_counts':{'vertices':len(verts),'edges':len(edges)},'samples':[hull(x) for x in xs]}
Path('/mnt/data/outer_geometry_prep/PILOT_RESULTS.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2))
