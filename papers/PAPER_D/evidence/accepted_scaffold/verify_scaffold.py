"""Codex exact checks of the author's clarified reference scaffold, 2026-09-23.

New independent coordinate transcription, not a historical run or kernel test.
Imports no project code. Writes only results in this script's directory.
"""
import json
from pathlib import Path
import sympy as S

OUT = Path(__file__).resolve().parent
s, g = S.symbols('s g', positive=True)
r2, r3 = S.sqrt(2), S.sqrt(3)
a = (1+r2)*s/2
p = (s+2*g)/(2*r3)
U = [S.Matrix([1,0]), S.Matrix([-S.Rational(1,2),r3/2]),
     S.Matrix([-S.Rational(1,2),-r3/2])]
J = S.Matrix([[0,-1],[1,0]])
T = [J*u for u in U]
R60 = S.Matrix([[S.Rational(1,2),-r3/2],[r3/2,S.Rational(1,2)]])
R120 = R60**2
A = [p*U[i]-s*T[i]/2 for i in range(3)]
B = [p*U[i]+s*T[i]/2 for i in range(3)]
H = [v for pair in zip(A,B) for v in pair]
D = [H[(k+1)%6]-H[k] for k in range(6)]
lengths = [s,g,s,g,s,g]
checks = []

def zero(x):
    if isinstance(x, S.MatrixBase):
        return all(S.simplify(y) == 0 for y in x)
    return S.simplify(x) == 0

def check(name, condition, detail):
    ok = bool(condition)
    checks.append({'name':name, 'pass':ok, 'detail':detail})
    print(('PASS ' if ok else 'FAIL ')+name, flush=True)

def cross(x,y):
    return S.det(S.Matrix.hstack(x,y))

def key(v):
    return tuple(S.simplify(x) for x in v)

check('explicit_six_vertices', all(zero(x-y) for x,y in zip(H,[
    S.Matrix([p,-s/2]), S.Matrix([p,s/2]),
    S.Matrix([(s-g)/(2*r3),(s+g)/2]),
    S.Matrix([-(2*s+g)/(2*r3),g/2]),
    S.Matrix([-(2*s+g)/(2*r3),-g/2]),
    S.Matrix([(s-g)/(2*r3),-(s+g)/2])])), 'General positive s,g; p=(s+2g)/(2sqrt(3)).')
check('edge_and_connector_vectors', all(zero(D[2*i]-s*T[i]) and
    zero(D[2*i+1]-g*R60*T[i]) for i in range(3)), 'Three selected edges and three deliberately added connectors.')
check('placement_law', zero(r3*p-s/2-g), 'g=sqrt(3)p-s/2.')
check('six_exact_lengths', all(zero(D[k].dot(D[k])-lengths[k]**2) for k in range(6)), 'Alternating s,g,s,g,s,g.')
check('six_interior_angles', all(zero((-D[k-1]).dot(D[k])+lengths[k-1]*lengths[k]/2) for k in range(6)), 'Interior cosine=-1/2; lengths positive.')
check('six_positive_turns', all(zero(cross(D[k-1],D[k])-r3*s*g/2) for k in range(6)), 'Exterior turns +60 degrees.')
check('exact_closure', zero(sum(D,S.zeros(2,1))), 'Closed by the same cyclic endpoints.')
check('C3_covariance', all(zero(R120*H[k]-H[(k+2)%6]) for k in range(6)), 'Rotation preserves edge/connector roles.')
reflection = S.diag(1,-1)
check('reflection_symmetry', {key(reflection*h) for h in H} == {key(h) for h in H}, 'Uncoloured planar polygon has D3 symmetry.')
radius2=(s*s+s*g+g*g)/3
check('general_circumcircle', all(zero(h.dot(h)-radius2) for h in H), 'All six points lie on one circle.')
area=sum(cross(H[k],H[(k+1)%6]) for k in range(6))/2
check('general_area', zero(area-r3*(s*s+4*s*g+g*g)/4), 'Signed area positive for s,g>0.')
q=(2*s+g)/(2*r3)
check('supporting_line_distances', all(zero(cross(H[k],D[k])**2-lengths[k]**2*(p if k%2==0 else q)**2) for k in range(6)), 'Selected-edge distance p; connector distance q.')
check('regularity_iff_equal_lengths', S.solve(S.Eq(p,q),g)==[s] and zero((s*s-g*g)-(s-g)*(s+g)), 'Necessary from side equality; sufficient with the proved 60-degree turns and s,g>0.')
Hs=[h.subs(g,s) for h in H]
check('regular_hexagon_metrics', all(zero(h.dot(h)-s*s) for h in Hs) and zero(p.subs(g,s)-r3*s/2) and zero(area.subs(g,s)-3*r3*s*s/2), 'Circumradius s, inradius sqrt(3)s/2, area 3sqrt(3)s^2/2.')
check('regular_hexagon_D6', {key(R60*h) for h in Hs}=={key(h) for h in Hs}, 'Uncoloured hexagon only; R60 exchanges E and G roles.')
V=[]
for i in range(3):
    v=S.Matrix.vstack(U[i].T,U[(i+1)%3].T).inv()*S.Matrix([p,p])
    V.append(v)
check('three_equilateral_gap_cells', all(zero((x-y).dot(x-y)-g*g) for i in range(3) for x,y in [(B[i],V[i]),(V[i],A[(i+1)%3]),(A[(i+1)%3],B[i])]), 'Reference corner triangles, not claims of material void components.')
check('support_triangle_and_partition', all(zero((V[(i+1)%3]-V[i]).dot(V[(i+1)%3]-V[i])-(s+2*g)**2) for i in range(3)) and zero(r3*(s+2*g)**2/4-area-3*r3*g*g/4), 'Support triangle side s+2g; corner interiors disjoint because s>0.')

# Ordered vertices of a regular octagon; these are new reference figures.
O=[(a,-s/2),(a,s/2),(s/2,a),(-s/2,a),(-a,s/2),(-a,-s/2),(-s/2,-a),(s/2,-a)]
check('regular_octagon_side_lengths', all(zero(sum((O[(k+1)%8][j]-O[k][j])**2 for j in range(2))-s*s) for k in range(8)), 'Apothem a=(1+sqrt(2))s/2; no octagon distortion.')
frames=[[ (p+a)*U[i]+x*U[i]+y*T[i] for x,y in O] for i in range(3)]
check('complete_planar_octagon_reference_realization', all(zero(frames[i][5]-A[i]) and zero(frames[i][4]-B[i]) for i in range(3)), 'Centres L u_i, L=p+a; selected inward sides.')
check('complete_frame_C3', all(zero(R120*frames[i][k]-frames[(i+1)%3][k]) for i in range(3) for k in range(8)), 'Exact coordinate differences, not syntactic equality of radical expressions; covariant orientations are an explicit added assumption, not P02 equation (2).')
Lstar=(1+r2+r3)*s/2
check('planar_centre_placement', zero((p+a).subs(g,s)-Lstar), 'Regular derived hexagon at L=(1+sqrt(2)+sqrt(3))s/2.')

# Paper-C vertical-face family, compared in its original rigid coordinate frame.
p0=a/r3
pstar=r3*s/2
R30=S.Matrix([[r3/2,-S.Rational(1,2)],[S.Rational(1,2),r3/2]])
u,z=S.symbols('u z', real=True)
old=[S.Matrix([-a/2-u/2,r3*a/2-r3*u/2,z]), S.Matrix([u,0,z]),
     S.Matrix([a/2-u/2,r3*a/2+r3*u/2,z])]
images=[]
for i in range(3):
    xy=R30*(p0*U[i]+u*T[i])+S.Matrix([0,a/r3])
    images.append(S.Matrix([xy[0],xy[1],z]))
check('Paper_C_rigid_coordinate_match', all(zero(images[i]-old[j]) for i,j in enumerate([2,0,1])), 'Transcribed Paper-C maps agree for all local u,z, not just vertices.')
check('Paper_C_ratio', zero((r3*p0-s/2)/s-1/r2), 'p0=a/sqrt(3), g0=s/sqrt(2).')
check('outward_translation_parameter', zero((pstar-p0)-(2-r2)*s/(2*r3)) and zero(pstar/p0-3/(1+r2)), 'Same face size/orientation, increased selected-edge midpoint radius.')
lam=(1+r2)/3
check('fixed_face_centre_shrink', zero(r3*p0-lam*s/2-lam*s), 'Vertical Paper-C faces shrink uniformly about their own fixed centres; not a global rescale.')
k=S.symbols('k', positive=True)
check('global_rescale_does_not_tune_ratio', zero((r3*k*p-k*s/2)/(k*s)-g/s), 'All lengths scaled together leave g/s invariant.')
intersection=S.Matrix([p,r3*p])
check('adjacent_plane_intersection', zero(U[0].dot(intersection)-p) and zero(U[1].dot(intersection)-p) and zero(T[0].dot(intersection)-r3*p) and zero(T[1].dot(intersection)+r3*p), 'Pairwise plane intersections require local u=+/-sqrt(3)p.')
check('regular_scaffold_breaks_Paper_C_welding', zero(r3*pstar-a-(2-r2)*s/2) and (2-r2).is_positive, 'sqrt(3)pstar>a; infinite-plane intersection is outside finite octagons.')
X,Y,delta,dz=S.symbols('X Y delta dz', nonnegative=True)
diff=S.Matrix([r3*(delta+Y)/2,-delta/2-X+Y/2,dz])
check('exact_panel_separation_distance', zero(diff.dot(diff)-(delta**2+delta*(X+Y)+(X-Y)**2+X*Y+dz**2)), 'delta=sqrt(3)p-a>=0, X=a-u>=0, Y=a+v>=0; minimum delta attained at u=a,v=-a and equal z.')

def mesh_counts(pp):
    faces=[]
    for i in range(3):
        face=[]
        for uu,zz in O:
            xy=pp*U[i]+uu*T[i]
            face.append(key(S.Matrix([xy[0],xy[1],zz])))
        faces.append(face)
    edge_use={}
    for f in faces:
        for j in range(8):
            edge=frozenset([f[j],f[(j+1)%8]])
            edge_use[edge]=edge_use.get(edge,0)+1
    boundary=[e for e,n in edge_use.items() if n==1]
    todo=set(boundary); component_edges=[]
    while todo:
        group={todo.pop()}; verts=set(next(iter(group)))
        change=True
        while change:
            new={e for e in todo if e & verts}
            change=bool(new)
            group |= new; todo -= new
            for e in new: verts.update(e)
        component_edges.append(len(group))
    return {'vertices':len({v for f in faces for v in f}), 'edges':len(edge_use),
            'faces':3, 'shared_seams':sum(n==2 for n in edge_use.values()),
            'boundary_cycle_lengths':sorted(component_edges)}

c0,cs=mesh_counts(p0),mesh_counts(pstar)
check('original_Paper_C_mesh_counts', c0=={'vertices':18,'edges':21,'faces':3,'shared_seams':3,'boundary_cycle_lengths':[9,9]}, str(c0))
check('separated_hypothetical_face_counts', cs=={'vertices':24,'edges':24,'faces':3,'shared_seams':0,'boundary_cycle_lengths':[8,8,8]}, str(cs))
result={'attribution':'New Codex exact supporting predicates for the author clarification; not historical output or independent external review.',
        'assumptions':['s>0,g>0','Tangentially aligned selected edges at C3-related midpoint radius p','Connectors are added reference segments','Planar-frame and vertical-face completions are explicitly separate realizations'],
        'sympy_version':S.__version__, 'passed':sum(c['pass'] for c in checks), 'total':len(checks),
        'checks':checks, 'Paper_C_original_counts':c0, 'hypothetical_separated_counts':cs,
        'dimensionless_parameters':{'p0_over_s':str(S.simplify(p0/s)), 'pstar_over_s':str(pstar/s),
         'pstar_over_p0':str(S.simplify(pstar/p0)), 'delta_p_over_s':str(S.simplify((pstar-p0)/s)),
         'fixed_vertical_face_centre_shrink':str(lam)}}
(OUT/'scaffold_exact_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f"RESULT: {result['passed']}/{result['total']} exact supporting predicates pass")
if result['passed'] != result['total']:
    raise SystemExit(1)
