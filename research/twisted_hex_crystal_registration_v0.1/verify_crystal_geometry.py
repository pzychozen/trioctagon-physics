"""Bounded historical reconstruction and reusable mesh checks. No model evolution.
Run with Python >=3.12, numpy, sympy. Writes only beside this file.
The supplied script is NEVER run as a whole; its reviewed geometry prefix is
extracted by AST, after validating the exact preserved source SHA against baseline.
"""
from pathlib import Path
from collections import Counter, defaultdict, deque
import ast, hashlib, itertools, json, platform
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
TOL = 1e-10

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dump(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf8")

def topology(vertices, faces):
    vertices = np.asarray(vertices, float)
    incid = defaultdict(list)
    for j, f in enumerate(faces):
        for a,b in zip(f, f[1:]+f[:1]):
            incid[tuple(sorted((a,b)))].append((j, 1 if a<b else -1))
    boundary = [list(e) for e,v in incid.items() if len(v)==1]
    nonmanifold = [list(e) for e,v in incid.items() if len(v)>2]
    # Connected vertex links must be paths or cycles for a surface.
    bad_links = []
    for v in range(len(vertices)):
        link = defaultdict(list)
        for f in faces:
            if v in f:
                a,b = [x for x in f if x != v]
                link[a].append(b); link[b].append(a)
        if not link: continue
        seen = set(); stack = [next(iter(link))]
        while stack:
            u=stack.pop()
            if u not in seen: seen.add(u); stack.extend(link[u])
        degrees = list(map(len, link.values()))
        if len(seen)!=len(link) or any(d>2 for d in degrees) or degrees.count(1) not in (0,2):
            bad_links.append(v)
    # Solve orientation consistency even for nonmanifold vertex complexes.
    adj = defaultdict(list)
    for e, members in incid.items():
        if len(members)==2:
            (a,sa),(b,sb)=members
            adj[a].append((b,-sa*sb)); adj[b].append((a,-sa*sb))
    signs={}; orientable=not nonmanifold; components=0
    for start in range(len(faces)):
        if start in signs: continue
        components+=1; signs[start]=1; queue=[start]
        while queue:
            u=queue.pop()
            for v,rel in adj[u]:
                expected=signs[u]*rel
                if v in signs:
                    if signs[v]!=expected: orientable=False
                else: signs[v]=expected; queue.append(v)
    bgraph=defaultdict(set)
    for a,b in boundary: bgraph[a].add(b); bgraph[b].add(a)
    unseen=set(bgraph); bcomponents=[]
    while unseen:
        todo=[min(unseen)]; comp=set()
        while todo:
            u=todo.pop()
            if u in comp: continue
            comp.add(u); todo.extend(bgraph[u]-comp)
        unseen-=comp; bcomponents.append(sorted(comp))
    edges=sorted(incid)
    lengths=sorted(np.linalg.norm(vertices[a]-vertices[b]) for a,b in edges)
    clusters=[]
    for x in lengths:
        if clusters and abs(clusters[-1]["length"]-x)<1e-8:
            clusters[-1]["count"]+=1
        else: clusters.append({"length":float(x),"count":1})
    return {"V":len(vertices),"E":len(edges),"F":len(faces),
            "euler_characteristic":len(vertices)-len(edges)+len(faces),
            "edge_incidence_histogram":dict(Counter(len(x) for x in incid.values())),
            "boundary_edge_count":len(boundary),"boundary_edges":boundary,
            "boundary_components":bcomponents,
            "boundary_is_cycles":all(len(v)==2 for v in bgraph.values()),
            "nonmanifold_edges":nonmanifold,"nonmanifold_vertices":bad_links,
            "orientation_constraints_consistent":orientable,
            "surface_orientable":orientable if not bad_links else "NOT_A_SURFACE",
            "face_edge_connected_components":components,
            "closed":not boundary and not nonmanifold and not bad_links,
            "duplicate_faces":len(faces)-len({tuple(sorted(f)) for f in faces}),
            "edge_length_clusters_numeric":clusters}

def point_on_shared(p, shared):
    if len(shared)==0:return False
    if len(shared)==1:return np.linalg.norm(p-shared[0])<TOL*10
    a,b=shared[:2]; d=b-a
    t=np.dot(p-a,d)/np.dot(d,d)
    return -TOL<t<1+TOL and np.linalg.norm(p-a-t*d)<TOL*10

def cut_triangle(tri, normal, offset):
    ds=tri@normal-offset; pts=[]
    for i in range(3):
        a,b=tri[i],tri[(i+1)%3]; da,db=ds[i],ds[(i+1)%3]
        if abs(da)<TOL:pts.append(a)
        if da*db<0 and abs(da)>TOL and abs(db)>TOL:
            pts.append(a+(b-a)*da/(da-db))
    return pts

def coplanar_intersection(a,b,n):
    # Convex polygon clipping; preserve 3D coordinates.
    k=int(np.argmax(abs(n))); keep=[i for i in range(3) if i!=k]
    cross2=lambda u,v:u[0]*v[1]-u[1]*v[0]
    sign=np.sign(cross2((b[1]-b[0])[keep],(b[2]-b[0])[keep]))
    poly=list(a)
    for j in range(3):
        p,q=b[j],b[(j+1)%3]; edge=(q-p)[keep]
        side=lambda x:sign*cross2(edge,(x-p)[keep])
        out=[]
        if not poly:break
        for x,y in zip(poly,poly[1:]+poly[:1]):
            dx,dy=side(x),side(y)
            if dx>=-TOL:out.append(x)
            if (dx> TOL and dy< -TOL) or (dx< -TOL and dy> TOL):
                out.append(x+(y-x)*dx/(dx-dy))
        poly=out
    return poly

def intersections(vertices, faces):
    """All pairs, including adjacent faces; remove only their shared simplex.
    Numerical diagnostic, not an exact proof; canonical family has separate proof.
    """
    v=np.asarray(vertices,float); found=[]; pairs=0
    for i,j in itertools.combinations(range(len(faces)),2):
        pairs+=1; a=v[faces[i]]; b=v[faces[j]]
        shared=v[sorted(set(faces[i]) & set(faces[j]))]
        if np.any(np.maximum(a.min(axis=0),b.min(axis=0)) > np.minimum(a.max(axis=0),b.max(axis=0))+TOL):continue
        na=np.cross(a[1]-a[0],a[2]-a[0]); na/=np.linalg.norm(na)
        nb=np.cross(b[1]-b[0],b[2]-b[0]); nb/=np.linalg.norm(nb)
        da=a@nb-b[0]@nb; db=b@na-a[0]@na
        if min(da)>TOL or max(da)<-TOL or min(db)>TOL or max(db)<-TOL:continue
        line=np.cross(na,nb); norm=np.linalg.norm(line)
        if norm<TOL:
            if max(abs(da))>TOL:continue
            pts=coplanar_intersection(a,b,na); kind="coplanar"
        else:
            # Distinct planes containing the same edge intersect only on that edge.
            if len(shared)==2:continue
            line/=norm
            ca=cut_triangle(a,nb,b[0]@nb); cb=cut_triangle(b,na,a[0]@na)
            if not ca or not cb:continue
            ia=sorted(float(x@line) for x in ca); ib=sorted(float(x@line) for x in cb)
            lo=max(ia[0],ib[0]); hi=min(ia[-1],ib[-1])
            if hi<lo-TOL:continue
            anchor=ca[0]
            pts=[anchor+(lo-anchor@line)*line,anchor+(hi-anchor@line)*line]
            kind="noncoplanar"
        # Reject unstable nearly-parallel plane-line constructions off either triangle.
        def on_triangle(p,tri):
            mat=np.column_stack((tri[1]-tri[0],tri[2]-tri[0]))
            uv=np.linalg.lstsq(mat,p-tri[0],rcond=None)[0]
            return min(uv)>=-TOL*10 and sum(uv)<=1+TOL*10 and np.linalg.norm(mat@uv-(p-tri[0]))<TOL*10
        pts=[p for p in pts if on_triangle(p,a) and on_triangle(p,b)]
        extra=[p for p in pts if not point_on_shared(p,shared)]
        if extra:
            found.append({"faces":[i,j],"kind":kind,"points":[p.tolist() for p in pts],
                          "diameter":float(max((np.linalg.norm(p-q) for p in pts for q in pts),default=0))})
    return {"all_face_pairs_tested":pairs,"tolerance":TOL,"unexpected_intersections":found,
            "unexpected_pair_count":len(found)}

def axial_symmetry(vertices, faces, axis=2):
    """Finite candidates fixed by the equilateral apex triples: C6 * two reflections.
    For the historical near-radical geometry, 1e-8 matching explicitly idealizes
    binary trig/decimal discrepancies. Face permutations themselves are discrete.
    """
    v=np.asarray(vertices,float)
    if axis==1:v=v[:,[0,2,1]]
    fs={tuple(sorted(f)) for f in faces}; ops=[]
    for k,h,mir in itertools.product(range(6),(1,-1),(1,-1)):
        angle=k*np.pi/3
        R=np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,h]])
        # vertical reflection y->-y; historical apexes are at 90deg, also a mirror axis.
        M=R@np.diag([1,mir,1])
        w=v@M.T; perm=[]; error=0
        for p in w:
            distances=np.linalg.norm(v-p,axis=1); ix=int(np.argmin(distances))
            error=max(error,float(distances[ix])); perm.append(ix)
        if error>1e-8 or len(set(perm))<len(v):continue
        ops.append({"rotation_steps_60":k,"horizontal_sign":h,"vertical_reflection":mir==-1,
                    "determinant":int(round(np.linalg.det(M))),
                    "vertex_residual":error,
                    "faces_preserved":{tuple(sorted(perm[x] for x in f)) for f in faces}==fs})
    return {"matching_tolerance":1e-8,"vertex_operations":ops,
            "face_symmetry_order":sum(x["faces_preserved"] for x in ops)}

def historical():
    source=HERE/"source_evidence/tri_oct.py"
    baseline=json.loads((HERE/"PRESERVATION_BEFORE.json").read_text(encoding="utf8"))
    expected=baseline["external_sources"][r"C:\Users\Notandi\Downloads\tri_oct.py"]
    assert sha(source)==expected
    tree=ast.parse(source.read_text(encoding="utf8"))
    prefix=[]
    for node in tree.body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="fig" for t in node.targets):break
        if isinstance(node,(ast.Import,ast.ImportFrom)):continue
        if isinstance(node,ast.Expr):continue  # only the reviewed print
        prefix.append(node)
    # Exact copy of already inspected geometry definitions, loops and NumPy calls.
    code=ast.unparse(ast.Module(body=prefix,type_ignores=[]))+"\n"
    assert not any(word in code for word in ("plt.","os.","open(","save","system("))
    (HERE/"source_evidence/geometry_prefix_executed.py").write_text(code,encoding="utf8")
    env={"np":np}
    exec(compile(ast.Module(body=prefix,type_ignores=[]),str(source)+"[geometry-prefix]","exec"),env)
    vertices=np.vstack([env["top_hex"],env["bot_hex"],env["top_apexes"],env["bot_apexes"]])
    face_arrays=env["all_tris"]+env["top_faces"]+env["bot_faces"]+env["twist_faces"]
    faces=[]
    for tri in face_arrays:
        f=[]
        for p in tri:
            ds=np.linalg.norm(vertices-p,axis=1); ix=int(np.argmin(ds))
            assert ds[ix]==0
            f.append(ix)
        faces.append(f)
    # Independent rewrite of literal primitive generation, with same operation order.
    a,b,c,h=.27059805,.38268343,.92387953,.46868957
    independent=[]
    for deg in (0,120,240):
        theta=np.radians(deg); ct,st=np.cos(theta),np.sin(theta)
        R=np.array([[ct,0,st],[0,1,0],[-st,0,ct]])
        for sign in (-1,1):
            independent.append(np.array([[a,sign*b,0],[0,sign*c,h],[-a,sign*b,0]])@R.T)
    assert np.array_equal(np.asarray(independent),np.asarray(env["all_tris"]))
    topo=topology(vertices,faces); ints=intersections(vertices,faces)
    sym=axial_symmetry(vertices,faces,axis=1)
    sh=sp.sin(sp.pi/8); ch=sp.cos(sp.pi/8)
    exacts=[sh/sp.sqrt(2),sh,ch,sp.sqrt(6)*sh/2]
    errors=[abs(float(e)-x) for e,x in zip(exacts,[a,b,c,h])]
    cap_assignments=[[f[2]-(12 if k==0 else 15) for f in faces[6+6*k:12+6*k]] for k in range(2)]
    # Exact idealized cap ties, using the decimal radii but exact 120deg rotations.
    aa,bb,cc,hh=map(sp.Rational,["0.27059805","0.38268343","0.92387953","0.46868957"])
    ring=[sp.Matrix([aa*sp.cos(k*sp.pi/3),bb,aa*sp.sin(k*sp.pi/3)]) for k in range(6)]
    apex=[sp.Matrix([hh*sp.cos(sp.pi/2+2*k*sp.pi/3),cc,hh*sp.sin(sp.pi/2+2*k*sp.pi/3)]) for k in range(3)]
    tie_records=[]
    for k in range(6):
        mid=(ring[k]+ring[(k+1)%6])/2
        ds=[sp.simplify((p-mid).dot(p-mid)) for p in apex]
        minimum=min(ds,key=lambda e:float(e))
        tied=[i for i,e in enumerate(ds) if sp.simplify(e-minimum)==0]
        tie_records.append({"edge":[k,(k+1)%6],"nearest_apex_indices":tied,
                            "squared_distances":[str(e) for e in ds]})
    # Exact symbolic intersection of the first two radical primitive triangles.
    A=sh/sp.sqrt(2); B=sh; C=ch; H=sp.sqrt(6)*sh/2
    tri0=sp.Matrix([[A,B,0],[0,C,H],[-A,B,0]])
    R=sp.Matrix([[-sp.Rational(1,2),0,sp.sqrt(3)/2],[0,1,0],[-sp.sqrt(3)/2,0,-sp.Rational(1,2)]])
    tri1=tri0*R.T
    # The intersection exits at midpoint of a primitive apex-to-base leg.
    start=sp.Matrix([0,B,0])
    end=(tri0.row(1).T+tri0.row(0).T)/2
    # Find actual common segment via exact barycentric plane constraints.
    normals=[]
    for tri in (tri0,tri1):
        rows=[tri.row(i).T for i in range(3)]
        normals.append((rows[1]-rows[0]).cross(rows[2]-rows[0]))
    direction=sp.simplify(normals[0].cross(normals[1]))
    lam=sp.symbols("lam",real=True)
    bary=sp.symbols("u v",real=True)
    bounds=[]
    for tri in (tri0,tri1):
        rows=[tri.row(i).T for i in range(3)]
        sol=sp.solve(rows[0]+bary[0]*(rows[1]-rows[0])+bary[1]*(rows[2]-rows[0])-start-lam*direction,bary)
        weights=[sp.simplify(1-sol[bary[0]]-sol[bary[1]]),sol[bary[0]],sol[bary[1]]]
        for w in weights:
            slope=sp.simplify(sp.diff(w,lam)); intercept=sp.simplify(w.subs(lam,0))
            if slope!=0:bounds.append((sp.simplify(-intercept/slope),1 if float(slope)>0 else -1))
    low=max([v for v,k in bounds if k==1],key=float)
    high=min([v for v,k in bounds if k==-1],key=float)
    seg2=sp.trigsimp(sp.simplify((high-low)**2*direction.dot(direction)))
    checks={
        "source_hash_matches":sha(source)==expected,
        "independent_literal_primitives_bitwise_equal":True,
        "18_vertices_60_edges_30_faces":(topo["V"],topo["E"],topo["F"])==(18,60,30),
        "30_boundary_edges":topo["boundary_edge_count"]==30,
        "no_nonmanifold_edges":not topo["nonmanifold_edges"],
        "has_nonmanifold_vertices":bool(topo["nonmanifold_vertices"]),
        "six_primitive_and_six_primitive_cap_crossing_pairs":sorted(x["faces"] for x in ints["unexpected_intersections"])==[[0,2],[0,4],[0,14],[1,3],[1,5],[1,8],[2,4],[3,5],[4,12],[4,16],[5,6],[5,10]],
        "symbolic_crossing_length_squared_a_squared":sp.simplify(sp.expand_trig(seg2-A**2))==0,
        "radical_values_round_to_literals":all(round(float(e),8)==x for e,x in zip(exacts,[a,b,c,h])),
        "three_exact_nearest_apex_ties":sum(len(x["nearest_apex_indices"])==2 for x in tie_records)==3,
        "full_face_symmetry_is_C1_at_declared_tolerance":sym["face_symmetry_order"]==1}
    probes=[
        ("separated",[[0,0,0],[1,0,0],[0,1,0],[0,0,1],[1,0,1],[0,1,1]],[[0,1,2],[3,4,5]],0),
        ("proper_crossing",[[0,0,0],[2,0,0],[0,2,0],[.5,.5,-1],[.5,.5,1],[1.5,.5,0]],[[0,1,2],[3,4,5]],1),
        ("shared_edge",[[0,0,0],[1,0,0],[0,1,0],[0,0,1]],[[0,1,2],[1,0,3]],0),
        ("coplanar_overlap",[[0,0,0],[2,0,0],[0,2,0],[.25,.25,0],[.5,.25,0],[.25,.5,0]],[[0,1,2],[3,4,5]],1),
        ("shared_vertex_only",[[0,0,0],[1,0,0],[0,1,0],[-1,0,0],[0,-1,0]],[[0,1,2],[0,3,4]],0)]
    for name,v,f,expected_count in probes:
        checks['intersection_probe_'+name]=intersections(v,f)['unexpected_pair_count']==expected_count
    checks['edge_length_class_counts_match_Claude_note']=[x['count'] for x in topo['edge_length_clusters_numeric']]==[12,6,12,18,6,6]
    data={"label":"HISTORICAL_AS_CODED","source_sha256":sha(source),
          "runtime":{"python":platform.python_version(),"numpy":np.__version__,"sympy":sp.__version__},
          "frame":{"axis":"+Y","azimuth":"atan2(z,x)"},
          "vertices":vertices.tolist(),
          "vertices_binary64_hex":[[float(x).hex() for x in p] for p in vertices],
          "vertex_blocks":{"top_ring":[0,6],"bottom_ring":[6,12],"top_apexes":[12,15],"bottom_apexes":[15,18]},
          "faces":faces,"face_blocks":{"primitives":[0,6],"top_caps":[6,12],"bottom_caps":[12,18],"sides":[18,30]},
          "literal_dimensions":{"ring_radius":a,"ring_half_height":b,"apex_half_height":c,"apex_radius":h},
          "historical_registration_diagnostic":{"fixed_height_scale":0.5/c,"apex_radius_at_host_half_height":h/(2*c),"radial_residual_to_host_target":float(sp.sqrt(3)/6)-h/(2*c),"not_used_for_new_candidate":True},
          "cap_assignments":cap_assignments,"cap_counts":[dict(Counter(x)) for x in cap_assignments],
          "topology":topo,"intersections_numeric":ints,"symmetry_numeric":sym,
          "radical_interpretation":{"status":"SUPPORTED_IDEALIZATION_NOT_UNIQUE_FROM_ROUNDED_DECIMALS",
             "expressions":[str(e) for e in exacts],"literal_errors":errors,
             "primitive_crossing_length_squared":"sin(pi/8)**2/2 (verified by symbolic equality)",
             "exact_nearest_cap_ties":tie_records},
          "claude_note_correction":"The claim of only six crossings is false: six additional primitive-cap crossings occur. Rounded decimals also cannot determine a unique exact radical model without a restricted model class.",
          "checks":checks,"pass":all(checks.values())}
    dump("HISTORICAL_CRYSTAL.json",data)
    print(json.dumps({"historical_checks":checks,"pass":data["pass"]},indent=2))
    return data

if __name__=="__main__":
    result=historical()
    raise SystemExit(0 if result["pass"] else 1)
