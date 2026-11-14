"""Finite numerical nomination followed by exact certificate construction, no validation claims."""
from common import *
from geometry import *
import numpy as np
from scipy.spatial import ConvexHull
from collections import Counter,defaultdict
from math import atan2
assert (R/'PRIOR_WORK_COMPARISON.md').read_text(encoding='utf-8').find('Disposition: DISTINCT_GAP')>=0
points=inventory_family();labels=list(points);actions=symmetry(points)
def nominate(sample,is_event):
    values={k:veval(v,sample) for k,v in points.items()};xyz=np.array([[float(c) for c in values[k]] for k in labels]);hull=ConvexHull(xyz)
    found={}
    for tri in hull.simplices:
        cycle=[labels[int(i)] for i in tri];constant={k:constpoint(v) for k,v in values.items()};n,d=plane(constant,cycle)
        residuals={k:peval(residual(n,d,v),ZERO) for k,v in constant.items()};signs={q.sign() for q in residuals.values()}-{0}
        assert len(signs)==1,'Floating candidate is not an exact supporting plane'
        zeros=tuple(sorted(k for k,q in residuals.items() if not q));assert len(zeros)>=3
        found[zeros]=zeros
    faces=[]
    for j,zeros in enumerate(sorted(found),1):
        # Floating angular order is a proposal, verified independently and uniformly later.
        arr=np.array([[float(c) for c in values[k]] for k in zeros]);center=arr.mean(axis=0);u=arr[0]-center;u/=np.linalg.norm(u)
        normal=np.cross(arr[1]-arr[0],arr[2]-arr[0]);normal/=np.linalg.norm(normal)
        if normal@center<0:normal=-normal
        v=np.cross(normal,u);indices=sorted(range(len(zeros)),key=lambda k:atan2((arr[k]-center)@v,(arr[k]-center)@u));cycle=[zeros[k] for k in indices]
        # Fix a deterministic outward cycle and exact polynomial plane.
        first=cycle.index(min(cycle));cycle=cycle[first:]+cycle[:first]
        work=constant if is_event else points;n,d=plane(work,cycle)
        r=[peval(residual(n,d,p),sample) for p in work.values()];nonzero=next(x for x in r if x)
        if nonzero.sign()>0:cycle=[cycle[0],*reversed(cycle[1:])];n,d=plane(work,cycle)
        faces.append({'id':f'F{j:02}','labels':list(zeros),'cycle':cycle,'plane_basis':cycle[:3],'normal_polynomials':vdump(n),'offset_polynomial':pdump(d),'zero_set_rule':'constant exact evaluation' if is_event else 'identically zero polynomial','residual_polynomials':{k:pdump(residual(n,d,p)) for k,p in work.items()}})
    return faces,{'parameter':sample.dump(),'parameter_display':float(sample),'qhull_triangle_count':len(hull.simplices),'proposed_maximal_face_count':len(faces),'proposed_face_histogram':dict(Counter(map(lambda f:len(f['labels']),faces))),'authority':'Floating nomination only. Exact validation is separate.'}
domains=[];explore=[]
for ident,kind,lo,hi,sample in [('C1','open',A,T,Q(F(3,5))),('T','point',T,T,T),('C2','open',T,B,Q(F(2,3)))]:
    faces,nom=nominate(sample,kind=='point');nom['domain_id']=ident;explore.append(nom)
    domains.append({'id':ident,'kind':kind,'lower':lo.dump(),'upper':hi.dump(),'nomination_parameter':sample.dump(),'faces':faces,'D3h_face_orbits':face_orbits(faces,actions)})
endpoints={}
for name,t in [('A',A),('B',B)]:
    source=endpoint_input(name);values={k:veval(p,t) for k,p in points.items()};mapping={}
    for v in source['vertices']:
        xyz=svector(v['exact']);group=sorted(k for k,p in values.items() if p==xyz);assert group
        mapping[str(v['id'])]={'source_outer_dot_id':v['outer_dot_id'],'labels':group,'coordinates_transformed':[q.dump() for q in xyz]}
    assert sorted(k for row in mapping.values() for k in row['labels'])==sorted(points)
    endpoints[name]={'parameter':t.dump(),'vertex_mapping':mapping,'faces':[{'source_face_id':f['id'],'source_vertex_cycle':f['vertices'],'label_groups':[mapping[str(i)]['labels'] for i in f['vertices']]} for f in source['faces']]}
certificate={'schema':'TRIOCTAGON_OUTER_ENVELOPE_EXACT_CERTIFICATE_v1','status':'Candidate awaiting independent checker','coordinate_basis':'(physical_X/w,physical_Y/(sqrt(3)*w),physical_Z/w)','field':'Q(sqrt(2)); each pair [a,b] means rational a+b*sqrt(2); polynomial arrays ascend in x','domain':[A.dump(),B.dump()],'transition':{'parameter':T.dump(),'minimal_polynomial_integer_coefficients_ascending':[-9,12,4],'isolating_interval_rational':['6213/10000','6214/10000'],'radius_squared':(Q(F(1,3))+T*T).dump()},'points':{k:vdump(v) for k,v in points.items()},'symmetry_actions':actions,'domains':domains,'endpoints':endpoints}
write(D/'exact_certificate.json',certificate);write(D/'EXPLORATORY_NOMINATION.json',{'new_nominal_evaluations':3,'new_bisection_evaluations':0,'records':explore,'not_a_completeness_proof':True})
for row in explore:print(row)
print('Candidate certificate written; no final classification claim yet.')
