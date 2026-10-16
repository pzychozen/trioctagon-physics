"""Isolated exact BOUNDARY-11 geometry. No imports from scientific project code."""
from pathlib import Path
import hashlib, itertools, json, os, sys
from collections import Counter, defaultdict
import sympy as sp

assert os.environ.get('CONDA_DEFAULT_ENV') == 'torment'
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
(OUT/'evidence').mkdir(exist_ok=True)
(OUT/'data').mkdir(exist_ok=True)
Q = sp.Rational
rt2, rt3, rt6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
s = rt2-1
h = s/2
rho2 = Q(13,12)-rt2/2
a2 = Q(1,3)
tau = sp.Symbol('tau', real=True)
def c(x): return sp.expand(sp.radsimp(sp.sympify(x)))
def vc(v): return sp.Matrix([c(x) for x in v])
def zero(v): return all(c(x)==0 for x in v)
def key(v): return tuple(c(x) for x in v)
def js(v): return [str(c(x)) for x in v]
def numeric(v): return [float(x) for x in v]
def save(path,obj): (OUT/path).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

# Paper C section 4, unchanged welded vertex numbering; w=1, then centre at o.
original = [
 [0,rt3/2,(1-rt2)/2],[-Q(1,2)+rt2/4,rt6/4,-Q(1,2)],[-rt2/4,rt3/2-rt6/4,-Q(1,2)],
 [-Q(1,2),0,(1-rt2)/2],[-Q(1,2),0,(rt2-1)/2],[-rt2/4,rt3/2-rt6/4,Q(1,2)],
 [-Q(1,2)+rt2/4,rt6/4,Q(1,2)],[0,rt3/2,(rt2-1)/2],[(1-rt2)/2,0,-Q(1,2)],
 [(rt2-1)/2,0,-Q(1,2)],[Q(1,2),0,(1-rt2)/2],[Q(1,2),0,(rt2-1)/2],
 [(rt2-1)/2,0,Q(1,2)],[(1-rt2)/2,0,Q(1,2)],[rt2/4,rt3/2-rt6/4,-Q(1,2)],
 [Q(1,2)-rt2/4,rt6/4,-Q(1,2)],[Q(1,2)-rt2/4,rt6/4,Q(1,2)],
 [rt2/4,rt3/2-rt6/4,Q(1,2)]]
o=sp.Matrix([0,rt3/6,0])
V=[vc(sp.Matrix(v)-o) for v in original]
faces=[[0,1,2,3,4,5,6,7],[3,8,9,10,11,12,13,4],[10,14,15,0,7,16,17,11]]
edges=sorted({tuple(sorted((f[k],f[(k+1)%8]))) for f in faces for k in range(8)})
assert len(edges)==21 and len(set(map(key,V)))==18
tests=[]
def check(name,condition):
    assert condition,name
    tests.append({'name':name,'pass':True})

# Independently reconstruct all three rigid panels from the accepted local maps.
uv=[(-Q(1,2),-h),(-h,-Q(1,2)),(h,-Q(1,2)),(Q(1,2),-h),
    (Q(1,2),h),(h,Q(1,2)),(-h,Q(1,2)),(-Q(1,2),h)]
maps=[lambda u,z:sp.Matrix([-Q(1,4)-u/2,rt3/4-rt3*u/2,z])-o,
      lambda u,z:sp.Matrix([u,0,z])-o,
      lambda u,z:sp.Matrix([Q(1,4)-u/2,rt3/4+rt3*u/2,z])-o]
for fi,(f,fn) in enumerate(zip(faces,maps)):
    check(f'panel map {fi+1} matches all eight numbered vertices',all(zero(fn(*p)-V[i]) for p,i in zip(uv,f)))
check('all vertex squared radii',all(c(v.dot(v)-rho2)==0 for v in V))
check('vertex centroid is origin',zero(sum(V,sp.zeros(3,1))))
records=[]; branches=[]
for ei,(i,j) in enumerate(edges,1):
    m=vc((V[i]+V[j])/2); d=vc((V[j]-V[i])/2); u=vc(d/h)
    kind='seam' if d[0]==d[1]==0 else ('horizontal' if d[2]==0 else 'chamfer')
    check(f'E{ei:02d} length midpoint orthogonality tangent sphere',
          c(d.dot(d)-h*h)==0 and c(m.dot(d))==0 and c(m.dot(m)-a2)==0)
    records.append({'id':f'E{ei:02d}','vertices':[i,j],'class':kind,
                    'midpoint_exact':js(m),'half_edge_exact':js(d),'unit_direction_exact':js(u),
                    'midpoint':numeric(m),'half_edge':numeric(d),'unit_direction':numeric(u),
                    'faces':[k+1 for k,f in enumerate(faces) if i in f and j in f],
                    'point_formula':'midpoint +/- tau*half_edge; tau=sqrt((R/w)^2-1/3)/((sqrt(2)-1)/2)'})
    for sign in [-1,1]:
        branches.append((f'E{ei:02d}'+('+' if sign>0 else '-'),m,sign*d))
check('edge orbit sizes 3 6 12',Counter(r['class'] for r in records)=={'seam':3,'horizontal':6,'chamfer':12})
events=defaultdict(list); pair_results=[]
for bi,bj in itertools.combinations(range(42),2):
    ni,mi,di=branches[bi]; nj,mj,dj=branches[bj]
    delta=vc(mi-mj); velocity=vc(di-dj)
    nz=[k for k in range(3) if velocity[k]!=0]
    if not nz:
        check('no coincident distinct entire branches '+ni+nj,not zero(delta))
        solution=None
    else:
        k=nz[0]; val=c(-delta[k]/velocity[k])
        solution=val if zero(delta+val*velocity) else None
    admissible=solution is not None and bool(solution>=1)
    if admissible: events[solution].append([ni,nj])
    pair_results.append({'branch_a':ni,'branch_b':nj,'tau':str(solution) if solution is not None else None,'admissible_tau_ge_1':admissible})

# Independent 210-line incidence test using rank/linear equations, not branch pairs.
la,lb=sp.symbols('la lb')
line_events=set(); parallel=skew=0
for i,j in itertools.combinations(range(21),2):
    mi=branches[2*i][1]; di=branches[2*i+1][2]
    mj=branches[2*j][1]; dj=branches[2*j+1][2]
    cross=vc(di.cross(dj))
    if zero(cross):
        parallel+=1
        check(f'distinct parallel lines {i} {j}',not zero((mi-mj).cross(di)))
        continue
    if c((mj-mi).dot(cross))!=0:
        skew+=1; continue
    sol=sp.solve(list(mi+la*di-mj-lb*dj),(la,lb))
    ai,aj=c(sol[la]),c(sol[lb])
    check(f'equal radial line parameters {i} {j}',c(ai*ai-aj*aj)==0)
    av=abs(ai)
    if bool(av>=1): line_events.add(c(av))
check('independent line-event method agrees',line_events==set(events))

event_data=[]
for val in sorted(events,key=float):
    groups=defaultdict(list)
    for n,m,d in branches: groups[key(m+val*d)].append(n)
    R2=c(a2+h*h*val*val)
    event_data.append({'tau_exact':str(val),'t_over_w_exact':str(c(h*val)),
                       'R_squared_over_w_squared':str(R2),'R_over_w':float(sp.sqrt(R2)),
                       'unique_points':len(groups),'multiplicities':dict(sorted(Counter(map(len,groups.values())).items())),
                       'groups':[{'coordinates_exact':js(q),'coordinates':numeric(q),'branches':ns} for q,ns in groups.items()]})

# Complete exact angular inventory: cos(gamma)=(A+B*tau+C*tau^2)/(1/3+h^2*tau^2).
angle_classes=defaultdict(list)
for i,j in itertools.combinations(range(42),2):
    ni,mi,di=branches[i]; nj,mj,dj=branches[j]
    coeff=tuple(c(x) for x in [mi.dot(mj),mi.dot(dj)+di.dot(mj),di.dot(dj)])
    angle_classes[coeff].append([ni,nj])
angle_data=[{'id':f'A{k:03d}','numerator_coefficients_ascending':js(coef),'multiplicity':len(pairs),'branch_pairs':pairs}
            for k,(coef,pairs) in enumerate(sorted(angle_classes.items(),key=lambda x:tuple(float(v) for v in x[0])),1)]
save('data/angular_separations.json',{'parameter':'tau>=1','denominator_coefficients_ascending':['1/3','0',str(c(h*h))],
    'formula':'central_angle_radians = acos((A+B*tau+C*tau^2)/(1/3+((sqrt(2)-1)/2)^2*tau^2)); arc length = R*central_angle',
    'all_labelled_pairs':861,'classes':angle_data})

# Verify D3h on the whole 42-branch family, including all parameter values.
rot=sp.Matrix([[-Q(1,2),-rt3/2,0],[rt3/2,-Q(1,2),0],[0,0,1]])
sv=sp.diag(-1,1,1); sh=sp.diag(1,1,-1)
signature={(key(m),key(d)) for _,m,d in branches}
for name,G in [('C3',rot),('vertical reflection',sv),('horizontal reflection',sh)]:
    check(name+' preserves every symbolic branch',all((key(G*m),key(G*d)) in signature for _,m,d in branches))
cov=sp.zeros(3,3)
for _,m,d in branches:
    q=m+tau*d;cov+=q*q.T
cov=cov.applyfunc(c)
check('generic covariance horizontal degeneracy',cov[0,0]==cov[1,1] and all(cov[i,j]==0 for i in range(3) for j in range(3) if i!=j))
for event in event_data:
    pts=[sp.Matrix([sp.sympify(x) for x in row['coordinates_exact']]) for row in event['groups']]
    cv=sum((p*p.T for p in pts),sp.zeros(3,3)).applyfunc(c)
    event['unique_second_moment_diagonal']=js(cv.diagonal())
    check('special-event distinct vertical second moment '+event['tau_exact'],c(cv[2,2]-cv[0,0])>0)

sources=[ROOT/'trioctagon-physics/papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md',
         ROOT/'research/BOUNDARY10_20261016/BOUNDARY10_REPORT.tex',ROOT/'research/BOUNDARY10_20261016/BOUNDARY10_REPORT.pdf']
identities=[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources]
save('evidence/source_identities.json',identities)
data={'normalization':'w=1; coordinates relative to Paper C centre o=(0,sqrt(3)/6,0); multiply by w and add o for original coordinates',
      'source':'Paper C v1.0.1 section 4 and face cycles','s_exact':str(s),'h_exact':str(h),
      'inner_radius_exact':'sqrt(3)/3','inner_radius':float(sp.sqrt(a2)),
      'rho_squared_exact':str(rho2),'rho':float(sp.sqrt(rho2)),
      'vertices':[{'id':i,'original_exact':js(v),'centered_exact':js(V[i]),'centered':numeric(V[i])} for i,v in enumerate(original)],
      'faces':faces,'edges':records,'coincidence_events':event_data,
      'generic_unique_points':42,'generic_second_moment_diagonal':js(cov.diagonal()),
      'angular_function_classes':len(angle_data)}
save('data/geometry_inventory.json',data)
save('evidence/all_branch_coincidence_checks.json',pair_results)
save('evidence/exact_checks.json',{'environment':sys.executable,'checks':tests,'passed':len(tests),
     'line_pair_analysis':{'total':210,'parallel_distinct':parallel,'skew':skew,'intersecting':210-parallel-skew},
     'branch_pair_analysis':{'total':861,'finite_admissible_event_count':len(events)},'scientific_project_imports':[]})
print(json.dumps({'edge_classes':dict(Counter(r['class'] for r in records)),
    'events':[{k:v for k,v in e.items() if k!='groups'} for e in event_data],
    'angle_classes':len(angle_data),'generic_second_moment_diagonal':js(cov.diagonal()),'checks_passed':len(tests)},indent=2))
