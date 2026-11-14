from common import S,read
from exact import *
INV=S/'research/spherical_edge_extensions/accepted/boundary11/data/geometry_inventory.json'
def inventory_family():
    inv=read(INV);points={}
    for row in inv['edges']:
        m=svector(row['midpoint_exact']);u=svector(row['unit_direction_exact'])
        for suffix,sign in [('+',1),('-',-1)]:points[row['id']+suffix]=tuple(poly([a,sign*b]) for a,b in zip(m,u))
    return points
def folded_family():
    h=(SQ2-1)/2;half=Q(F(1,2));local=[(-half,-h),(-h,-half),(h,-half),(half,-h),(half,h),(h,half),(-h,half),(-half,h)]
    vertices=[];faces=[]
    for k in range(3):
        face=[]
        for u,z in local:
            if k==0:v=(-Q(F(1,4))-u/2,Q(F(1,12))-u/2,z)
            elif k==1:v=(u,-Q(F(1,6)),z)
            else:v=(Q(F(1,4))-u/2,Q(F(1,12))+u/2,z)
            if v not in vertices:vertices.append(v)
            face.append(vertices.index(v))
        faces.append(face)
    edges=sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in faces for i in range(len(f))})
    points={};records=[]
    for i,(a,b) in enumerate(edges,1):
        m=tuple((v+w)/2 for v,w in zip(vertices[a],vertices[b]));u=tuple((w-v)/(2*h) for v,w in zip(vertices[a],vertices[b]));eid=f'E{i:02}'
        records.append({'id':eid,'vertices':[a,b],'midpoint':m,'unit_direction':u})
        for suffix,sign in [('+',1),('-',-1)]:points[eid+suffix]=tuple(poly([v,sign*w]) for v,w in zip(m,u))
    return points,vertices,faces,records
def symmetry(points):
    def rotate(p):return (padd(pscale(p[0],Q(F(-1,2))),pscale(p[1],Q(F(-3,2)))),padd(pscale(p[0],Q(F(1,2))),pscale(p[1],Q(F(-1,2)))),p[2])
    lookup={v:k for k,v in points.items()};assert len(lookup)==42;actions=[]
    for k in range(3):
        for rx in range(2):
            for rz in range(2):
                perm={}
                for label,p in points.items():
                    v=(pscale(p[0],-1 if rx else 1),p[1],pscale(p[2],-1 if rz else 1))
                    for _ in range(k):v=rotate(v)
                    assert v in lookup;perm[label]=lookup[v]
                actions.append({'rotation_120_power':k,'reflect_x':bool(rx),'reflect_z':bool(rz),'permutation':perm})
    assert len({tuple(a['permutation'].values()) for a in actions})==12
    return actions
def face_orbits(faces,actions):
    lookup={frozenset(f['labels']):f['id'] for f in faces};assert len(lookup)==len(faces);seen=set();orbits=[]
    for f in faces:
        if f['id'] in seen:continue
        ids=sorted({lookup[frozenset(a['permutation'][l] for l in f['labels'])] for a in actions});seen.update(ids)
        orbits.append({'representative':f['id'],'size':len(ids),'face_ids':ids,'polygon_size':len(f['labels'])})
    assert seen=={f['id'] for f in faces};return orbits
def endpoint_input(name):return read(S/f'research/spherical_edge_extensions/accepted/boundary12/data/hull_{name}.json')
