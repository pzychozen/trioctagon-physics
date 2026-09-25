"""Bounded exact family analysis. Imports accepted geometry without running builds.
All writes remain in family_analysis. No kernel evolution or parameter sweep.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
from math import isqrt
import itertools, json, sys, hashlib, datetime
import sympy as sp
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
import verify_host_registration as source
from verify_crystal_geometry import intersections,topology

u=sp.symbols("u",real=True)
t=sp.symbols("t",real=True)
lam=sp.symbols("ell",real=True)
s=source.S;d=source.D;r=source.R0;a=d/2;h=s/2;H=sp.Rational(1,2);U=s/2
J=source.J
v=source.canonical_points(u)
F=source.candidate_faces()
CHECKS={}
def simp(x):return sp.factor(sp.cancel(sp.expand(x),extension=True),extension=True)
def eq(x):return sp.simplify(sp.expand(x))==0
def veq(x):return all(eq(e) for e in x)
def check(name,condition):
    CHECKS[name]=bool(condition)
    if not condition:raise AssertionError(name)
def dump(name,obj):(HERE/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
def num(x):return float(sp.N(x,17))
def serialize_matrix(m):return [str(sp.simplify(x)) for x in m]
def squared(p):return simp(p.dot(p))
def polygroup(items):
    groups=[]
    for key,expr in items:
        expr=simp(expr)
        found=next((g for g in groups if eq(g["expr"]-expr)),None)
        if found:found["members"].append(key)
        else:groups.append({"expr":expr,"members":[key]})
    return groups
def bernstein(poly,L=sp.Rational(1,4)):
    P=sp.Poly(poly,u,extension=True)
    if P.is_zero:return [sp.Integer(0)]
    n=P.degree()
    return [sp.simplify(sum(P.nth(i)*sp.binomial(k,i)/sp.binomial(n,i)*L**i for i in range(k+1))) for k in range(n+1)]
def positive_b(poly):
    bs=bernstein(poly)
    return all(b.is_positive is True for b in bs),bs

# Rigorous rational intervals for algebraic expressions with square roots.
BITS=100
def addi(A,B):return A[0]+B[0],A[1]+B[1]
def muli(A,B):
    products=[x*y for x in A for y in B];return min(products),max(products)
def powi(A,n):
    if n<0:
        assert A[0]*A[1]>0
        return powi((1/A[1],1/A[0]),-n)
    out=(Fraction(1),Fraction(1))
    for _ in range(n):out=muli(out,A)
    return out
def sqrt_i(A):
    assert A[0]>=0
    Q=1<<BITS
    lower=isqrt(A[0].numerator*Q*Q//A[0].denominator)
    upper=isqrt(A[1].numerator*Q*Q//A[1].denominator)+1
    return Fraction(lower,Q),Fraction(upper,Q)
def interval(expr):
    if expr.is_Rational:
        x=Fraction(int(expr.p),int(expr.q));return x,x
    if expr.is_Add:
        result=(Fraction(0),Fraction(0))
        for arg in expr.args:result=addi(result,interval(arg))
        return result
    if expr.is_Mul:
        result=(Fraction(1),Fraction(1))
        for arg in expr.args:result=muli(result,interval(arg))
        return result
    if expr.is_Pow:
        base,exponent=expr.args
        if exponent.is_Integer:return powi(interval(base),int(exponent))
        if exponent.q==2:return powi(sqrt_i(interval(base)),int(exponent.p))
    raise ValueError("unsupported interval expression: "+str(expr))
def strict_sign(expr):
    lo,hi=interval(expr)
    if lo>0:return 1
    if hi<0:return -1
    if lo==hi==0:return 0
    raise ArithmeticError("interval does not resolve sign")

def root_record(root):
    if isinstance(root,sp.polys.rootoftools.ComplexRootOf):
        root.eval_rational(n=15)
        bracket=root._get_interval()
        left,right=sp.Rational(bracket.a),sp.Rational(bracket.b)
        check("root_isolation_"+str(root),root.poly.count_roots(left,right)==1)
        return {"exact":str(root),"minimal_or_defining_polynomial":str(root.poly.as_expr()),
                "root_index":root.index,"isolating_interval":[str(left),str(right)],"approx":num(root)}
    return {"exact":str(root),"approx":num(root)}

def roots_in_domain(expr):
    P=sp.Poly(expr,u,extension=True)
    if P.is_zero:return {"identical":True,"polynomial":"0","interior":[],"zero":True}
    roots=P.real_roots(radicals=False)
    inside=[]
    for root in roots:
        if bool(root>0) and bool(root<U) and not any(root==x for x in inside):inside.append(root)
    return {"identical":False,"polynomial":str(P.as_expr()),
            "interior":[root_record(x) for x in inside],"zero":eq(P.eval(0)),
            "endpoint":eq(P.eval(U)),
            "method":"Exact real-root isolation over the algebraic coefficient field; filter by exact comparisons to 0 and (sqrt(2)-1)/2."}

def signed_and_sections():
    R=sp.diag(-1,1)
    A=sp.eye(2)-(t/r)*J
    check("signed_reflection_R_A_t_R_equals_A_minus_t",veq(R*A*R-(sp.eye(2)+(t/r)*J)))
    check("full_map_is_isotropic_scaling",veq(A.T*A-(1+(t/r)**2)*sp.eye(2)))
    M=sp.eye(2)-lam*(t/r)*J
    check("corresponding_index_interpolation",veq(M-((1-lam)*sp.eye(2)+lam*A)))
    check("interpolation_polar_metric",veq(M.T*M-(1+(lam*t/r)**2)*sp.eye(2)))
    perm=[(-i)%6 for i in range(6)]+[6+(-i)%6 for i in range(6)]+[12+(-i)%3 for i in range(3)]+[15+(-i)%3 for i in range(3)]
    P=sp.diag(-1,1,1);vt=source.canonical_points(t)
    vm=source.canonical_points(-t)
    check("signed_vertices_reflect_with_relabeling",all(veq(P*vt[i]-vm[perm[i]]) for i in range(18)))
    Fminus=[[perm[i] for i in f] for f in F]
    norms=[]
    for k in (1,2):
        angle=k*sp.pi/3
        rot=sp.Matrix([[sp.cos(angle),-sp.sin(angle)],[sp.sin(angle),sp.cos(angle)]])
        C=(1-lam)*sp.eye(2)+lam*rot*(sp.eye(2)-(u/r)*J)
        c=1-lam+lam*(sp.cos(angle)+(u/r)*sp.sin(angle))
        b=lam*(sp.sin(angle)-(u/r)*sp.cos(angle))
        check(f"true_section_orbit_{k}_matrix",veq(C-c*sp.eye(2)-b*J))
        check(f"true_section_orbit_{k}_polar",veq(C.T*C-(c*c+b*b)*sp.eye(2)))
        section_point=(1-lam)*v[0][:2,0]+lam*v[6+k][:2,0]
        check(f"true_section_orbit_{k}_matches_mesh_edges",veq(section_point-C*v[0][:2,0]))
        norms.append({"m":k,"real_coefficient":str(sp.expand(c)),"J_coefficient":str(sp.expand(b)),
                      "radius_squared":str(simp(a*a*(c*c+b*b))),"angle":"atan2(J_coefficient, real_coefficient)"})
    zero_mid=[sp.simplify(sp.sympify(x["radius_squared"],locals={"u":u,"ell":lam}).subs({u:0,lam:sp.Rational(1,2)})) for x in norms]
    check("zero_midsection_has_two_distinct_radii",eq(zero_mid[0]-3*a*a/4) and eq(zero_mid[1]-a*a/4))
    return {"vertex_relabeling":perm,"F_plus":F,"F_minus_in_common_labels":Fminus,
        "signed_domain":"-(sqrt(2)-1)/2 <= t <= (sqrt(2)-1)/2",
        "full_map":"A(t)=I-(t/r0)J=sqrt(1+(t/r0)^2) R[-atan(t/r0)]",
        "corresponding_index_interpolation":"I-lambda*(t/r0)J",
        "interpolation_radius":"a*sqrt(1+(lambda*t/r0)^2)",
        "interpolation_angle":"-atan(lambda*t/r0)",
        "interpolation_scope":"Corresponding-index ruled interpolation only; NOT the cross-section of the verified one-step triangulated mesh.",
        "actual_surface_sections_plus":norms,
        "actual_surface_sections_minus":"Reflection of PLUS at magnitude |t|; replace both step-angle and footprint sign.",
        "actual_surface_section_vertex_count":12,"zero_midsection_radii_squared":list(map(str,zero_mid))}

def skeleton():
    n=source.NORMALS
    top=[sp.Matrix([r*x[0],r*x[1],H]) for x in n]
    bottom=[sp.Matrix([*(r*x-t*J*x),-H]) for x in n]
    checks={"upper_triangle_edge_squared":(top[0]-top[1]).dot(top[0]-top[1])-sp.Rational(1,4),
      "lower_triangle_edge_squared":(bottom[0]-bottom[1]).dot(bottom[0]-bottom[1])-(sp.Rational(1,4)+3*t*t),
      "corresponding_spoke_squared":(top[0]-bottom[0]).dot(top[0]-bottom[0])-(1+t*t),
      "forward_cross_diagonal_squared":(top[0]-bottom[1]).dot(top[0]-bottom[1])-(sp.Rational(5,4)+t*t-t/2),
      "backward_cross_diagonal_squared":(top[0]-bottom[2]).dot(top[0]-bottom[2])-(sp.Rational(5,4)+t*t+t/2)}
    for name,e in checks.items():check("skeleton_"+name,eq(e))
    cross=sp.det(sp.Matrix.hstack(top[0][:2,0],bottom[0][:2,0]))
    check("skeleton_signed_orientation",eq(cross+r*t))
    G=sp.Matrix([0,0,H])
    volume=sp.det(sp.Matrix.hstack(G,top[0],bottom[0]))/6
    check("auxiliary_tetrahedron_oriented_volume",eq(volume+r*t/12))
    lower_area2=squared((bottom[1]-bottom[0]).cross(bottom[2]-bottom[0]))/4
    check("lower_triangle_area_squared",eq(lower_area2-(sp.sqrt(3)/16+3*sp.sqrt(3)*t*t/4)**2))
    check("tangent_is_orthogonal_to_radius",eq(n[0].dot(J*n[0])))
    lower_center=sp.Matrix([r*n[0][0],r*n[0][1],-H])
    check("vertical_right_triangle_orthogonality",eq((top[0]-lower_center).dot(bottom[0]-lower_center)))
    check("upper_O_distance",eq(squared(top[0])-sp.Rational(1,3)))
    check("lower_O_distance",eq(squared(bottom[0])-sp.Rational(1,3)-t*t))
    return {"minimal_graph":"Six contact/apex vertices; upper and lower C3 triangles plus 3 corresponding spokes (9 edges). O is a reference point.",
       "upper_edge":"1/2","lower_edge":"sqrt(1/4+3*t^2)","corresponding_spoke":"sqrt(1+t^2)",
       "other_cross_diagonals":["sqrt(5/4+t^2-t/2)","sqrt(5/4+t^2+t/2)"],
       "O_upper":"1/sqrt(3)","O_lower":"sqrt(1/3+t^2)",
       "upper_triangle_area":"sqrt(3)/16","lower_triangle_area":"sqrt(3)/16+3*sqrt(3)*t^2/4",
       "tangent_triangle_area":"r0*abs(t)/2","vertical_right_triangle_area":"abs(t)/2",
       "signed_planar_measure":"kappa=-r0*t","oriented_auxiliary_tetrahedron_volume":"-r0*t/12",
       "volume_scope":"Tetrahedron (O, upper centroid, U0, B0) only. The open annulus has no enclosed-volume interpretation.",
       "even":["same-level side lengths","corresponding spokes","triangle areas","covariance eigenvalues"],
       "odd":["kappa","auxiliary oriented volume","difference of the two cross-diagonal squared lengths"],
       "zero":"Upper/lower triangles congruent and aligned; all corresponding spokes vertical.",
       "endpoint":"Lower contact reaches a finite host-edge endpoint; no face degeneration."}

def metrics_and_special():
    edges=sorted({tuple(sorted(e)) for f in F for e in zip(f,f[1:]+f[:1])})
    edge_groups=polygroup([(list(e),squared(v[e[0]]-v[e[1]])) for e in edges])
    normals=[(v[b]-v[a]).cross(v[c]-v[a]) for a,b,c in F]
    area_groups=polygroup([(i,squared(n)/4) for i,n in enumerate(normals)])
    check("eight_distinct_edge_functions",len(edge_groups)==8)
    check("four_distinct_face_area_functions",len(area_groups)==4)
    check("edge_counts_42",sum(len(g["members"]) for g in edge_groups)==42)
    check("face_counts_24",sum(len(g["members"]) for g in area_groups)==24)
    # Human-readable formulas independently compared with direct vertex metrics.
    q=u/r
    formulas=[
      a*a,
      s*s+a*a*(1+q*q-sp.sqrt(3)*q),
      s*s+a*a*(3+q*q-sp.sqrt(3)*q),
      (r-a)**2+d*d,
      r*r+a*a-r*a+d*d,
      a*a*(1+q*q),
      (r-a)**2*(1+q*q)+d*d,
      (r*r+a*a-r*a)*(1+q*q)+d*d]
    for i,(g,f) in enumerate(zip(edge_groups,formulas)):check(f"edge_formula_{i}",eq(g["expr"]-f))
    P0=(a*a*s*s+a**4*(sp.sqrt(3)/2-q)**2)/4
    P1=(a*a*(1+q*q)*s*s+a**4*(sp.sqrt(3)*(1+q*q)/2-q)**2)/4
    P2=a*a*(4*d*d+3*(r-a)**2)/16
    P3=a*a*(1+q*q)*(4*d*d+3*(r-a)**2*(1+q*q))/16
    for i,(g,p) in enumerate(zip(area_groups,(P0,P1,P2,P3))):
        check(f"compact_face_area_formula_{i}",eq(g["expr"]-p))
    check("full_mesh_cannot_be_equi_edge",positive_b(formulas[1]-formulas[0])[0])
    eqedge=[]
    for i,j in itertools.combinations(range(len(edge_groups)),2):
        result=roots_in_domain(edge_groups[i]["expr"]-edge_groups[j]["expr"])
        eqedge.append({"classes":[f"E{i}",f"E{j}"],**result})
    eqarea=[]
    for i,j in itertools.combinations(range(len(area_groups)),2):
        eqarea.append({"classes":[f"A{i}",f"A{j}"],**roots_in_domain(area_groups[i]["expr"]-area_groups[j]["expr"])})
    areas=[g["expr"] for g in area_groups]
    total=sum(len(g["members"])*sp.sqrt(g["expr"]) for g in area_groups)
    derivative=sp.diff(total,u)
    convex=[]
    for i,P in enumerate(areas):
        positive,bs=positive_b(P)
        check(f"area_squared_{i}_positive_full_domain",positive)
        N=simp(2*P*sp.diff(P,u,2)-sp.diff(P,u)**2)
        if eq(N):convex.append({"class":i,"constant":True});continue
        positive,bern=positive_b(N)
        check(f"sqrt_area_{i}_strict_convexity_certificate",positive)
        convex.append({"class":i,"numerator_2PPdd_minus_Pd_squared":str(N),
                       "Bernstein_interval":["0","1/4"],"positive_coefficients":list(map(str,bern))})
    lo=sp.Rational(0);hi=sp.Rational(1,5)
    check("area_derivative_at_zero_negative",strict_sign(derivative.subs(u,lo))<0)
    check("area_derivative_at_one_fifth_positive",strict_sign(derivative.subs(u,hi))>0)
    check("one_fifth_inside_admitted_interval",bool(hi<U))
    while hi-lo>sp.Rational(1,10**13):
        mid=(lo+hi)/2
        if strict_sign(derivative.subs(u,mid))<0:lo=mid
        else:hi=mid
    signs=[interval(derivative.subs(u,x)) for x in (lo,hi)]
    stationary={"classification":"EXACT_IMPLICIT_RIGOROUSLY_ISOLATED",
       "equation":"d/du [6*(sqrt(A0_squared)+sqrt(A1_squared)+sqrt(A2_squared)+sqrt(A3_squared))] = 0",
       "isolating_interval":[str(lo),str(hi)],"approx":num((lo+hi)/2),
       "endpoint_derivative_intervals":[list(map(str,p)) for p in signs],
       "unique":"Strict positive second derivative on 0<=u<=1/4 by the stored Bernstein certificates.",
       "signed_members":"t=+u_star and t=-u_star","area_approx":num(total.subs(u,(lo+hi)/2))}
    incidence=defaultdict(list)
    for k,f in enumerate(F):
        for e in zip(f,f[1:]+f[:1]):incidence[tuple(sorted(e))].append(k)
    def cosine2(edge):
        i,j=incidence[tuple(sorted(edge))]
        A,B=normals[i],normals[j]
        return sp.cancel(sp.expand(A.dot(B)**2)/sp.expand(A.dot(A)*B.dot(B)),extension=True)
    selected=[(0,8),(0,7),(0,12),(6,15)]
    cosines=[cosine2(e) for e in selected]
    eqd=[]
    for i,j in ((0,1),(2,3)):
        numerator=sp.Poly(sp.cancel(cosines[i]-cosines[j],extension=True).as_numer_denom()[0],u,extension=True).monic().as_expr()
        eqd.append({"selected_plane_angle_indices":[i,j],**roots_in_domain(numerator)})
    check("band_plane_angle_equality_cubic",eq(sp.Poly(sp.sympify(eqd[0]["polynomial"],locals={"u":u}),u).monic().as_expr()-(u**3-sp.Rational(7,12)*u*u+sp.Rational(5,6)*u-sp.Rational(1,48))))
    # Quad planarity and covariance absence have direct exact certificates.
    quad_det=simp(sp.det(sp.Matrix.hstack(v[1]-v[0],v[8]-v[0],v[7]-v[0])))
    check("no_quad_planarity_in_admitted_interval",roots_in_domain(quad_det)["interior"]==[] and not eq(quad_det.subs(u,0)) and not eq(quad_det.subs(u,U)))
    covxy=(2+(u/r)**2)*(d*d/24+r*r/12)
    covz=(2*s*s+1)/12
    covariance=sum((p*p.T for p in v),sp.zeros(3,3))/18
    check("covariance_direct_vertex_comparison",veq(covariance-sp.diag(covxy,covxy,covz)))
    check("covariance_vertical_separated_full_domain",(sp.simplify(covz-covxy.subs(u,U))).is_positive is True)
    check("nonzero_twist_below_triangle_reflection_period",bool(U/r<sp.sqrt(3)))
    check("no_interior_face_area_equalities",all(not x["interior"] for x in eqarea))
    check("no_full_equi_area_even_at_zero",not eq(areas[0].subs(u,0)-areas[2]))
    check("lower_triangle_area_strictly_increasing_for_u_positive",sp.diff(sp.sqrt(3)/16+3*sp.sqrt(3)*u*u/4,u)==3*sp.sqrt(3)*u/2)
    host_angle_t=r*sp.tan(sp.pi/8)
    check("octagonal_angle_member_in_interval",bool(host_angle_t>0) and bool(host_angle_t<U))
    labels=["upper_ring","cross_ring_strut","band_tessellation_diagonal","upper_apex_middle_ring","upper_apex_outer_ring","lower_ring","lower_apex_middle_ring","lower_apex_outer_ring"]
    metrics={"parameter":"u=abs(t) for the mirrored-hand family; physical host-width-one units. Multiply lengths by 2 and areas by 4 for canonical coordinates.",
      "edge_classes":[{"id":f"E{i}","name":labels[i],"squared_length":str(g["expr"]),"count":len(g["members"]),"members":g["members"],"classification":"EXACT_CLOSED_FORM"} for i,g in enumerate(edge_groups)],
      "face_area_classes":[{"id":f"A{i}","squared_area":str(g["expr"]),"count":len(g["members"]),"faces":g["members"],"classification":"EXACT_CLOSED_FORM"} for i,g in enumerate(area_groups)],
      "total_triangulated_area":str(total),"area_classification":"EXACT_CLOSED_FORM",
      "selected_plane_angles":[{"edge":list(e),"cos_squared":str(c),"definition":"acos(sqrt(cos_squared)) in [0,pi/2]; unoriented plane angle, not a solid interior dihedral","classification":"EXACT_CLOSED_FORM"} for e,c in zip(selected,cosines)],
      "quad_scalar_triple_product":str(quad_det),
      "covariance_eigenvalues":[str(covxy),str(covxy),str(covz)],
      "ring_radii":["a","a*sqrt(1+(u/r0)^2)"],
      "same_level_apex_ring_distances_squared":"d^2+rho^2*(r0^2+a^2-2*r0*a*cos(k*pi/3)), k=0..5; rho=1 above, rho=sqrt(1+(u/r0)^2) below.",
      "aspect_ratios":{"ring_over_apex_radius":"a/r0 on both levels (built in, not a selecting equality)","axial_extent_over_lower_apex_diameter":"1/(2*sqrt(r0^2+u^2))"}}
    special={"search_scope":["all 28 pairs of 8 edge-length functions","all 6 pairs of 4 face-area functions","band diagonal vs cross-strut plane angle","upper vs lower apex-fan rib plane angle","quad planarity","Euclidean symmetry enhancement","covariance degeneracy","total area stationary points","lower apex-triangle area stationary points","offset equality with the existing octagonal half-angle pi/8"],
        "edge_equalities":eqedge,"area_equalities":eqarea,"selected_plane_angle_equalities":eqd,
        "total_area_stationary_point":stationary,"strict_convexity_certificates":convex,
        "octagonal_half_angle_coincidence":{"exact":str(sp.simplify(host_angle_t)),"approx":num(host_angle_t),"reason":"delta=pi/8; a named host-angle equality, not a contact requirement."},
        "no_equi_edge_full_surface":"E0 remains constant and is strictly below the cross-ring classes throughout the interval.",
        "no_equi_area_full_surface":"No common positive root of all six pair comparisons; inspect the complete pair table.",
        "absence_scope":"Only listed predicates and admitted interval. No assertion about every conceivable functional.",
        "no_preferred_member":True}
    return metrics,special

def zero_state(signed):
    vz=source.canonical_points(sp.Integer(0))
    fs={tuple(sorted(f)) for f in F}
    lookup={tuple(sp.simplify(x) for x in p):i for i,p in enumerate(vz)}
    ops=[]
    for k,mirror,flip in itertools.product(range(3),(False,True),(False,True)):
        angle=2*k*sp.pi/3
        R=sp.Matrix([[sp.cos(angle),-sp.sin(angle),0],[sp.sin(angle),sp.cos(angle),0],[0,0,1]])
        M=R*(sp.diag(-1,1,1) if mirror else sp.eye(3))*(sp.diag(1,1,-1) if flip else sp.eye(3))
        perm=[lookup[tuple(sp.simplify(x) for x in M*p)] for p in vz]
        preserves={tuple(sorted(perm[i] for i in f)) for f in F}==fs
        ops.append({"k":k,"vertical_mirror":mirror,"horizontal_flip":flip,"determinant":int(M.det()),"faces_preserved":preserves})
    check("zero_vertex_D3h_12_operations",len(ops)==12)
    check("zero_surface_D3_six_proper_operations",sum(o["faces_preserved"] for o in ops)==6 and all(o["determinant"]==1 for o in ops if o["faces_preserved"]))
    norms=[(vz[b]-vz[a]).cross(vz[c]-vz[a]) for a,b,c in F]
    check("zero_no_degenerate_triangles",all(squared(n).is_positive for n in norms))
    coplanar=[]
    for i,j in itertools.combinations(range(24),2):
        if veq(norms[i].cross(norms[j])) and eq(norms[i].dot(vz[F[j][0]]-vz[F[i][0]])):
            coplanar.append({"faces":[i,j],"shared_vertices":sorted(set(F[i])&set(F[j]))})
    Fminus=signed["F_minus_in_common_labels"]
    # A generic rational interior point: the centroid happens to lie on the
    # other hand too, so it is not a separating witness.
    witness=sum((weight*vz[k] for weight,k in zip((2,5,11),F[0])),sp.zeros(3,1))/18
    containing=[]
    X,Y=sp.symbols("X Y",real=True)
    for i,f in enumerate(Fminus):
        A,B,C=[vz[k] for k in f]
        if not eq((B-A).cross(C-A).dot(witness-A)):continue
        sol=sp.solve(A+X*(B-A)+Y*(C-A)-witness,(X,Y))
        if sol and bool(sol[X]>=0) and bool(sol[Y]>=0) and bool(sol[X]+sol[Y]<=1):containing.append(i)
    check("zero_plus_minus_surface_supports_distinct",not containing)
    # Extend old exact cross-section argument to delta=0, 0<lambda<1.
    l=sp.symbols("l",positive=True)
    S=(1-l)*vz[0][:2,0]+l*vz[7][:2,0]
    D=(1-l)*vz[0][:2,0]+l*vz[8][:2,0]
    Sn=(1-l)*vz[1][:2,0]+l*vz[8][:2,0]
    check("zero_band_first_oriented_determinant",eq(sp.det(sp.Matrix.hstack(S,D))-sp.sqrt(3)*a*a*l*l/2))
    check("zero_band_second_oriented_determinant",eq(sp.det(sp.Matrix.hstack(D,Sn))-sp.sqrt(3)*a*a*(1-l)**2/2))
    check("zero_no_coplanar_triangle_pairs",not coplanar)
    numerical=intersections(source.num(vz),F)
    check("zero_numeric_all_pairs_no_extra_intersection",numerical["unexpected_pair_count"]==0)
    return {"vertex_symmetry":"D3h (order 12)","face_symmetry":"D3 (order 6), each handed face limit separately",
       "operations":ops,"coplanar_triangle_pairs":coplanar,"degenerate_triangles":0,
       "embedded":"YES. The positive-section determinant proof remains strict at delta=0 for 0<lambda<1; caps retain their disjoint slabs/sectors.",
       "numerical_crosscheck":numerical,
       "mirror_support_separation_witness":serialize_matrix(witness),
       "witness_on_Fminus_faces":containing,
       "vertex_chirality_reversal":True,
       "surface_chirality_reversal_for_prescribed_mirrored_family":False,
       "zero_vertex_handedness":"ACHIRAL","zero_face_handedness":"STILL_CHIRAL; two distinct mirror limits",
       "fixed_Fplus_extension":"Vertices and triangles depend continuously on signed t. A local embedded deformation through zero exists by stability of this nondegenerate finite embedded PL surface; the negative side uses Fplus, NOT the prescribed Fminus mirrored branch.",
       "global_fixed_Fplus_negative_interval":"NOT_CLAIMED_OR_NEEDED; no separate extension selected",
       "signed_prescribed_surface_family_continuous_at_zero":False,
       "surface_limit_reason":"The interior point (2*T0+5*T1+11*B2)/18 of Fplus face 0 belongs to no Fminus triangle at zero. Changing to the mirrored connectivity jumps the surface despite common vertex positions."}

def stacking():
    pitch=sp.Integer(1)
    check("full_height_pitch_is_twice_half_height",eq(pitch-2*H))
    check("rings_do_not_coincide_at_full_height_pitch",not eq(pitch-2*h))
    # At the sole common-height plane, only apex tips can meet.
    q=r*source.NORMALS[0]-u*J*source.NORMALS[0]
    check("interface_radius_mismatch_exact_u_squared",eq(q.dot(q)-r*r-u*u))
    return {"scope":"One bounded repeat test at the geometric full-height pitch: physical dz=1, canonical dz=2. No arbitrary offsets or pitch search.",
       "direct_translation":{"nonzero_vertex_coincidences":0,"ring_coincidences":0,"matching_boundary_loops":0,"face_intersections":0,"zero_state_contacts":"3 apex points only","period":"Translation by 1 for the disjoint copy set"},
       "translation_plus_C3":"Identical copy set to direct translation because each member already has C3 symmetry.",
       "translation_opposite_hand":{"nonzero_vertex_coincidences":0,"ring_coincidences":0,"matching_boundary_loops":0,"face_intersections":0,"zero_state_contacts":"3 apex points only","alternating_copy_period":2},
       "proof":"Adjacent slabs [-1/2,1/2] and [1/2,3/2] only meet at z=1/2. Only upper/lower apex tips reach that plane; their radii r0 and sqrt(r0^2+u^2) differ for u>0. For u=0 three isolated tips coincide, while boundary loops also contain ring vertices at different heights.",
       "simple_joined_axial_repeat_found":False,"status":"NO_SIMPLE_AXIAL_REPEAT_SELECTED",
       "screw_scope":"Translation+C3 is a tautological screw symmetry of a disconnected periodic copy set, not a new joining rule."}

def main():
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    signed=signed_and_sections();print("Signed/section identities checked",flush=True)
    sk=skeleton();metrics,special=metrics_and_special();print("Metric roots and stationary point certified",flush=True)
    zero=zero_state(signed);stack=stacking()
    dump("SIGNED_AND_SECTION_DATA.json",signed)
    dump("SKELETON_EXACT.json",sk)
    dump("METRICS_EXACT.json",metrics)
    dump("SPECIAL_MEMBER_RESULTS.json",special)
    dump("ZERO_AND_STACKING_RESULTS.json",{"zero":zero,"stacking":stack})
    sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE.parent/"verify_host_registration.py",HERE.parent/"CANONICAL_CRYSTAL_CANDIDATE.json",HERE.parent/"HOST_GEOMETRY.json"]}
    result={"started_utc":started,"completed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "sympy":sp.__version__,"source_identities":sources,"checks":CHECKS,"passed":sum(CHECKS.values()),"total":len(CHECKS),"pass":all(CHECKS.values()),
        "count_scope":"Predicate bookkeeping, not theorem count. Symbolic identities and exact root isolation supplement explicit proofs in the reports.",
        "exact_arithmetic":"SymPy algebraic real-root isolation; 100-bit outward rational square-root intervals for area derivative signs; Bernstein coefficient positivity for global strict convexity.",
        "no_model_runs":True,"no_parameter_sweep":True}
    dump("family_validation.json",result)
    print(json.dumps({"checks":len(CHECKS),"pass":result["pass"],"area_minimum":special["total_area_stationary_point"]["approx"],
      "edge_specials":[(q["classes"],[r["approx"] for r in q["interior"]]) for q in special["edge_equalities"] if q["interior"]],
      "area_specials":[(q["classes"],[r["approx"] for r in q["interior"]]) for q in special["area_equalities"] if q["interior"]],
      "dihedral_specials":[(q["selected_plane_angle_indices"],[r["approx"] for r in q["interior"]]) for q in special["selected_plane_angle_equalities"] if q["interior"]],
      "zero_coplanar":zero["coplanar_triangle_pairs"]},indent=2))
if __name__=="__main__":main()
