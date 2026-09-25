"""Exact accepted-host extraction, one-parameter candidate and bounded validation.
No source mutation, model evolution, optimizer, or parameter sweep.
The illustrated t=s/4 is a demonstrator, NOT a host-selected or fitted constant.
"""
from pathlib import Path
import importlib.util, itertools, json
import numpy as np
import sympy as sp
from verify_crystal_geometry import HERE, REPO, dump, sha, topology, intersections, axial_symmetry

S = sp.sqrt(2)-1
D = 1-sp.sqrt(2)/2
R0 = sp.sqrt(3)/6
O = sp.Matrix([0,R0,0])
T = sp.symbols("t", positive=True)
J = sp.Matrix([[0,-1],[1,0]])
HALF = sp.Rational(1,2)
NORMALS = [sp.Matrix([0,-1]),sp.Matrix([sp.sqrt(3)/2,HALF]),sp.Matrix([-sp.sqrt(3)/2,HALF])]
PAPER = "papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md"
MODULE = "kernel_physics/geometry.py"
CHECKS={}
DETAILS={}

def check(name, condition, detail=None):
    if isinstance(condition,sp.MatrixBase): condition=all(sp.simplify(x)==0 for x in condition)
    elif isinstance(condition,sp.Expr) and condition not in (sp.true,sp.false): condition=sp.simplify(condition)==0
    CHECKS[name]=bool(condition)
    if detail is not None:DETAILS[name]=detail

def exact(x):
    if isinstance(x,sp.MatrixBase):return [str(sp.simplify(v)) for v in x]
    if isinstance(x,(tuple,list)):return [exact(v) for v in x]
    return str(sp.simplify(x))

def num(points):
    return np.array([[float(x) for x in p] for p in points])

def point(panel,u,z):
    u,z=sp.sympify(u),sp.sympify(z)
    if panel==1:return sp.Matrix([-sp.Rational(1,4)-u/2,sp.sqrt(3)/4-sp.sqrt(3)*u/2,z])
    if panel==2:return sp.Matrix([u,0,z])
    return sp.Matrix([sp.Rational(1,4)-u/2,sp.sqrt(3)/4+sp.sqrt(3)*u/2,z])

def canonical_points(t=T, hand=1):
    """Physical centered coordinates, block order rings then apexes.
    Minus is the exact vertical reflection x -> -x, with the SAME indexing.
    This avoids the historical naive negative-index mirror mistake.
    """
    top=[]
    for i in range(6):
        theta=-sp.pi/2+i*sp.pi/3
        xy=D/2*sp.Matrix([sp.cos(theta),sp.sin(theta)])
        top.append(sp.Matrix([xy[0],xy[1],S/2]))
    bottom=[]
    M=sp.eye(2)-(t/R0)*J
    for p in top:
        xy=M*p[:2,0]
        bottom.append(sp.Matrix([xy[0],xy[1],-S/2]))
    apex_top=[sp.Matrix([R0*n[0],R0*n[1],HALF]) for n in NORMALS]
    apex_bottom=[]
    for n in NORMALS:
        xy=R0*n-t*J*n
        apex_bottom.append(sp.Matrix([xy[0],xy[1],-HALF]))
    pts=top+bottom+apex_top+apex_bottom
    if hand==-1:pts=[sp.diag(-1,1,1)*p for p in pts]
    return [p.applyfunc(sp.simplify) for p in pts]

def candidate_faces():
    f=[]
    # True next-vertex quadrilateral boundary, consistently triangulated.
    # +2 diagonals are declared tessellation edges, not extra physical struts.
    for i in range(6):
        f += [[i,(i+1)%6,6+(i+2)%6],[i,6+(i+2)%6,6+(i+1)%6]]
    # Each apex owns two symmetric adjacent ring edges; no nearest-point ties.
    for offset,ap in ((0,12),(6,15)):
        for k in range(3):
            a=(2*k-1)%6; b=2*k; c=(2*k+1)%6
            f += [[offset+a,offset+b,ap+k],[offset+b,offset+c,ap+k]]
    return f

def build():
    # Read-only import of the already inspected accepted geometry module.
    import sys
    spec=importlib.util.spec_from_file_location("accepted_geometry_readonly",REPO/MODULE)
    geom=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=geom; spec.loader.exec_module(geom)
    local=[(-HALF,-S/2),(-S/2,-HALF),(S/2,-HALF),(HALF,-S/2),
           (HALF,S/2),(S/2,HALF),(-S/2,HALF),(-HALF,S/2)]
    panels=[[point(k,u,z) for u,z in local] for k in (1,2,3)]
    for k,points in enumerate(panels,1):
        for j,p in enumerate(points):
            check(f"host_panel_{k}_vertex_{j}_exact_code_parity",p-sp.Matrix(geom.panel_point(k,*local[j])))
    check("host_center_exact_code_parity",O-sp.Matrix(geom.CENTROID))
    check("all_octagon_edges_exact_s",all(sp.simplify((pts[(i+1)%8]-pts[i]).dot(pts[(i+1)%8]-pts[i])-S**2)==0 for pts in panels for i in range(8)))
    panel_order=[2,3,1]
    upper=[point(k,0,HALF) for k in panel_order]
    lower=[point(k,0,-HALF) for k in panel_order]
    check("upper_centroid_axis",sum(upper,sp.zeros(3,1))/3-O-sp.Matrix([0,0,HALF]))
    check("upper_triangle_sides_one_half",all(sp.simplify((upper[i]-upper[j]).dot(upper[i]-upper[j])-sp.Rational(1,4))==0 for i,j in itertools.combinations(range(3),2)))
    check("lower_targets_horizontal_reflections",all(upper[k]-lower[k]==sp.Matrix([0,0,1]) for k in range(3)))
    C3=sp.Matrix([[-HALF,-sp.sqrt(3)/2,0],[sp.sqrt(3)/2,-HALF,0],[0,0,1]])
    check("targets_exact_C3_orbit",all((C3*(upper[k]-O)-(upper[(k+1)%3]-O)).applyfunc(sp.simplify)==sp.zeros(3,1) for k in range(3)))
    planes=[]
    for panel,n in zip(panel_order,NORMALS):
        planes.append({"panel":panel,"outward_normal":exact([n[0],n[1],0]),"equation_centered":"n dot (X-O) = sqrt(3)/6"})
        check(f"panel_{panel}_plane_exact",all(sp.simplify(n.dot(p[:2,0]-O[:2,0])-R0)==0 for p in panels[panel-1]))
    module=geom.folded_module()
    host={"label":"ACCEPTED_PAPER_C_WIDTH_ONE_HOST","sources":[{"path":PAPER,"sha256":sha(REPO/PAPER),"locators":"Sections 2-4, 6-9 and Appendix B"},{"path":MODULE,"sha256":sha(REPO/MODULE),"locators":"LOCAL_OCTAGON, panel_point, folded_module, CENTROID, rotate_c3"}],
          "center":exact(O),"principal_axis":["0","0","1"],"width":"1",
          "edge_length":exact(S),"chamfer_cutback":exact(D),"central_band_half_height":exact(S/2),
          "support_triangle_inradius":exact(R0),"panels":[{"panel":k,"center":exact(point(k,0,0)),"vertices":exact(pts)} for k,pts in enumerate(panels,1)],
          "plane_equations":planes,"welded_vertices":exact([sp.Matrix(p) for p in module.vertices]),"welded_faces":[list(f) for f in module.faces],
          "target_choice":"USER_CONFIRMED_HIGHEST_HORIZONTAL_EDGE_MIDPOINT",
          "target_panel_order_C3":panel_order,"upper_local_edge":[5,6],"lower_local_edge":[1,2],
          "upper_targets":exact(upper),"lower_targets":exact(lower),
          "upper_targets_numeric":num(upper).tolist(),"lower_targets_numeric":num(lower).tolist(),
          "upper_lower_angular_stagger":"0","target_side_length":"1/2","target_circumradius":exact(R0),
          "notch_metrics":{"legs":exact(S),"base":exact(D),"tip_angle":"acos(3/4)","vertical_rise":exact(D),"radial_rise":exact(sp.sqrt(3)*D/2)},
          "host_status":"OPEN_THREE_PANEL_SHELL_NOT_A_CLOSED_SOLID",
          "alternative_upper_chamfer_midpoints":{"local_u":["+sqrt(2)/4","-sqrt(2)/4"],"height":"sqrt(2)/4","circumradius":"sqrt(5/24)","used":False}}
    dump("HOST_GEOMETRY.json",host)

    alpha=R0/sp.sqrt(R0**2+T**2)
    delta=sp.atan(T/R0)
    pts=canonical_points()
    # Physical scale is forced by fixed canonical heights +-1 and host heights +-.5.
    check("canonical_upper_heights_plus_one",all(sp.simplify(2*pts[k][2]-1)==0 for k in range(12,15)))
    check("canonical_lower_heights_minus_one",all(sp.simplify(2*pts[k][2]+1)==0 for k in range(15,18)))
    check("all_vertex_centroid_exact_O",sum(pts,sp.zeros(3,1)))
    check("upper_registration_exact_for_all_t",all((pts[12+k]+O-upper[k]).applyfunc(sp.simplify)==sp.zeros(3,1) for k in range(3)))
    check("lower_prediction_tangential_displacement",all((pts[15+k]+O-lower[k]+T*sp.Matrix([*(J*NORMALS[k]),0])).applyfunc(sp.simplify)==sp.zeros(3,1) for k in range(3)))
    check("lower_residual_squared_exact_t_squared",all(sp.simplify((pts[15+k]+O-lower[k]).dot(pts[15+k]+O-lower[k])-T**2)==0 for k in range(3)))
    M=(sp.eye(2)-(T/R0)*J)
    check("lower_to_upper_similarity_exact",sp.simplify((sp.eye(2)+(T/R0)*J)/(1+(T/R0)**2)*M-sp.eye(2)))
    check("alpha_equals_cos_delta",sp.simplify(alpha-sp.cos(delta)))
    check("delta_bound_less_than_60_degrees",bool(S/(2*R0)<sp.sqrt(3)))
    ring_bound2=sp.simplify((D/2)**2*(1+(S/(2*R0))**2))
    check("lower_ring_strictly_inside_support_triangle_entire_family",bool(ring_bound2<R0**2))
    covariance_z=(2*S**2+1)/12
    covariance_xy_max=(2+(S/(2*R0))**2)*(D**2/24+R0**2/12)
    covariance_xy=(2+(T/R0)**2)*(D**2/24+R0**2/12)
    covariance=sum((p*p.T for p in pts),sp.zeros(3,3))/18
    check("covariance_formula_matches_symbolic_vertices",covariance-sp.diag(covariance_xy,covariance_xy,covariance_z))
    check("vertex_covariance_forces_unique_axis_entire_family",bool(sp.simplify(covariance_z-covariance_xy_max)>0))
    check("lower_tips_within_other_host_halfspaces_entire_family",bool(-R0/2+sp.sqrt(3)*S/4<R0))
    t_unrestricted=sp.symbols("t_unrestricted",real=True)
    check("all_six_center_fit_forces_t_zero",sp.solve(sp.Eq(t_unrestricted**2,0),t_unrestricted)==[0])
    # Historical uniform similarity fails even for radical idealization.
    ratio_historical=(2+sp.sqrt(2))/3
    check("historical_uniform_scale_registration_fails",sp.simplify(1-ratio_historical)!=0)
    # Independent exact counterexample to Claude's 'no primitive-cap crossings'.
    sh=sp.sin(sp.pi/8); a=sh/sp.sqrt(2); b=sh; c=sp.cos(sp.pi/8); h=sp.sqrt(6)*sh/2
    v0=sp.Matrix([a,b,0]); apex0=sp.Matrix([0,c,h])
    ring60=sp.Matrix([a/2,b,sp.sqrt(3)*a/2])
    apex330=sp.Matrix([sp.sqrt(3)*h/2,c,-h/2])
    endpoint=sp.simplify((3*v0+apex0)/4)
    check("exact_extra_primitive_cap_crossing_endpoint",endpoint-(3*ring60+apex330)/4)
    check("extra_crossing_length_squared_sinpi8_squared_over_4",sp.trigsimp((endpoint-v0).dot(endpoint-v0)-sh**2/4))
    # Band cross-sections: every segment stays in a consecutive angular wedge.
    lam,a0,b0,dd=sp.symbols("lambda a b delta",real=True)
    def polar(theta):return sp.Matrix([sp.cos(theta),sp.sin(theta)])
    st=(1-lam)*a0*polar(0)+lam*b0*polar(sp.pi/3-dd)
    diag=(1-lam)*a0*polar(0)+lam*b0*polar(2*sp.pi/3-dd)
    st_next=(1-lam)*a0*polar(sp.pi/3)+lam*b0*polar(2*sp.pi/3-dd)
    det=lambda x,y:sp.det(sp.Matrix.hstack(x,y))
    positive1=sp.sqrt(3)/2*(lam*b0)**2+lam*(1-lam)*a0*b0*sp.sin(dd)
    positive2=sp.sqrt(3)/2*((1-lam)*a0)**2+lam*(1-lam)*a0*b0*sp.sin(dd)
    check("band_first_consecutive_cross_product_identity",sp.trigsimp(sp.expand_trig(det(st,diag)-positive1)))
    check("band_second_consecutive_cross_product_identity",sp.trigsimp(sp.expand_trig(det(diag,st_next)-positive2)))
    details={"band_determinants":[str(positive1),str(positive2)],
             "domain":"0<t<=s/2; delta=atan(t/r0), 0<delta<pi/3; 0<lambda<1; a,b>0",
             "reason":"Both determinants positive. The section vertices S_i,D_i,S_(i+1) advance strictly within each 60-degree wedge, giving a simple star-shaped 12-gon. Caps lie in disjoint vertical slabs and disjoint 120-degree azimuth wedges.",
             "cap_geometry":"Each fan comprises two triangles with ring endpoints at apex azimuth -60,0,+60 degrees, and the apex on the middle ray."}
    DETAILS["exact_embedded_family_proof"]=details
    # Single exact, illustrated witness plus its mirror. Not a sweep or fitted choice.
    t_example=S/4
    faces=candidate_faces()
    variants=[]
    for hand in (1,-1):
        pp=canonical_points(t_example,hand); vv=num(pp)
        topo=topology(vv,faces); ints=intersections(vv,faces); sy=axial_symmetry(vv,faces)
        name="TWIST_PLUS" if hand==1 else "TWIST_MINUS"
        target_permutation=[0,1,2] if hand==1 else [0,2,1]
        symbolic_hand=canonical_points(T,hand)
        check(name+"_upper_contacts_exact_entire_family",all((symbolic_hand[12+k]+O-upper[target_permutation[k]]).applyfunc(sp.simplify)==sp.zeros(3,1) for k in range(3)))
        check(name+"_lower_center_residual_exact_entire_family",all(sp.simplify((symbolic_hand[15+k]+O-lower[target_permutation[k]]).dot(symbolic_hand[15+k]+O-lower[target_permutation[k]])-T**2)==0 for k in range(3)))
        check(name+"_topology_18_42_24",(topo["V"],topo["E"],topo["F"])==(18,42,24))
        check(name+"_two_boundary_loops_12_boundary_edges",len(topo["boundary_components"])==2 and topo["boundary_is_cycles"] and topo["boundary_edge_count"]==12)
        check(name+"_orientable_manifold",topo["surface_orientable"] is True and not topo["nonmanifold_vertices"] and not topo["nonmanifold_edges"])
        check(name+"_no_numerical_self_intersections",ints["unexpected_pair_count"]==0)
        check(name+"_face_symmetry_C3",sy["face_symmetry_order"]==3)
        clearance=[]
        for p in pp:
            clearance.append([float(sp.simplify(R0-n.dot(p[:2,0]))) for n in NORMALS])
        check(name+"_host_halfspace_clearance_numeric",np.min(clearance)>-1e-12)
        # No top-to-bottom straight mirrored struts. Shift+2 is only a tessellation.
        variants.append({"name":name,"physical_centered_vertices_exact":exact(pp),
                         "target_correspondence":target_permutation,
                         "canonical_vertices_exact":exact([2*p for p in pp]),
                         "physical_host_vertices_numeric":num([p+O for p in pp]).tolist(),
                         "canonical_vertices_numeric":(2*vv).tolist(),
                         "faces":faces,"topology":topo,"intersections_numeric":ints,
                         "symmetry_numeric":sy,"host_plane_clearances":clearance})
    # Mirrors have equal unordered host contact and clearance data.
    mirror=sp.diag(-1,1,1)
    check("handed_variants_exact_reflections",all((mirror*a-b).applyfunc(sp.simplify)==sp.zeros(3,1) for a,b in zip(canonical_points(t_example,1),canonical_points(t_example,-1))))
    # Skew side quads remain nonplanar; triangle split must be explicit.
    quad=pts[0],pts[1],pts[8],pts[7]
    skew=sp.factor(sp.det(sp.Matrix.hstack(quad[1]-quad[0],quad[2]-quad[0],quad[3]-quad[0])))
    check("candidate_side_quads_are_not_planar",sp.simplify(skew.subs(T,t_example))!=0)
    candidate={"label":"CANONICAL_INTENT_CANDIDATE_NOT_ADOPTED","status":"RESEARCH_FAMILY_WITH_EXPLICIT_NEW_FACE_AND_RING_RULES",
       "fit_class":"B_FAMILY_OF_EXACT_UPPER_CONTACT_AND_LOWER_EDGE_FITS",
       "all_six_corresponding_center_fit":"D_NO_FIT_FOR_STRICT_ALPHA_LT_1_AND_NONZERO_DELTA",
       "canonical_half_height":"1","physical_scale":"1/2","origin":exact(O),"axis":["0","0","1"],
       "free_parameter":{"name":"t","domain":"0 < t <= (sqrt(2)-1)/2","meaning":"absolute lower-tip tangential edge offset in host width-one units"},
       "alpha":str(alpha),"delta_plus":str(delta),"delta_minus":str(-delta),
       "alpha_selected_by_host":False,"delta_selected_by_host":False,
       "upper_registration":"EXACT","upper_residual":"0","lower_center_alignment":"RESIDUAL","lower_center_residual":"t",
       "lower_edge_membership":"EXACT","host_lower_stagger":"0",
       "symbolic_physical_centered_vertices":exact(pts),
       "symbolic_canonical_vertices":exact([2*p for p in pts]),
       "ring_rule":{"label":"NEW_ASSUMPTION_NOT_FORCED_BY_CONTACTS","top_ring_half_height_physical":str(S/2),"top_ring_radius_physical":str(D/2),
                    "rationale":"Reuse host central-band height and half the host notch base as a economical ring placement; no uniqueness is claimed.",
                    "bottom_ring_rule":"Apply I-(t/r0)J to top xy and reflect z; same planar similarity as apexes."},
       "face_rule":{"label":"NEW_OPEN_SURFACE_CANDIDATE","band":"Q_i=(t_i,t_(i+1),b_(i+2),b_(i+1)); diagonal t_i--b_(i+2)",
                    "fans":"Each apex covers the two edges about its radially aligned ring vertex; 6 cap triangles per level.",
                    "primitive_diameter_faces":"Omitted from new face surface; retained without alteration in historical evidence.",
                    "quad_nonplanarity_determinant":str(skew),
                    "diagonals":"The +2 edges are declared triangle tessellation edges, not independent strut requests. No vertical mirrored strut remains."},
       "illustrative_witness":{"t":str(t_example),"chosen_by":"CODEX_ILLUSTRATION_ONLY_NOT_HOST_OR_AUTHOR_SELECTION",
                    "alpha":exact(alpha.subs(T,t_example)),"alpha_numeric":float(alpha.subs(T,t_example)),
                    "delta_radians":exact(delta.subs(T,t_example)),"delta_degrees_numeric":float(delta.subs(T,t_example)*180/sp.pi),
                    "lower_residual_numeric":float(t_example)},
       "variants":variants,"exact_family_embedding_argument":details,
       "symmetry":"C3 for strict-domain vertices and this face complex; two mirror-related enantiomers",
       "symmetry_upper_bound_proof":{"covariance_z":str(covariance_z),"covariance_xy_upper_bound":str(covariance_xy_max),"argument":"The distinct vertical covariance eigenvalue fixes the unoriented axis. Unequal upper/lower apex radii forbid z reversal. The upper triangle allows D3, but the lower triangle is rotated by delta with 0<delta<pi/3, eliminating every common reflection. Exactly C3 remains; this proves chirality for the vertex set as well as the proposed face complex."},
       "host_handedness_preference":"NONE_MIRROR_DEGENERACY",
       "physical_interpretation":"NOT_ESTABLISHED",
       "limitations":["Upper-contact data do not select t, a 22.5-degree offset, ring rule, or face topology.",
                      "The host is an open shell; clearance here means no penetration of the three panel halfspaces, not a recovered physical container.",
                      "Exact lower CENTER alignment contradicts strict contraction; exact lower EDGE alignment is a separate conditional construction."]}
    dump("CANONICAL_CRYSTAL_CANDIDATE.json",candidate)
    validation={"checks":CHECKS,"passed":sum(CHECKS.values()),"total":len(CHECKS),"pass":all(CHECKS.values()),
                "details":DETAILS,"method_scope":"Symbolic equalities + exact inequalities, full-family embedding argument, one exact algebraic witness and its mirror; no parameter sweep.",
                "historical_uniform_similarity_ratio_residual":str(sp.simplify(1-ratio_historical))}
    dump("REGISTRATION_VALIDATION.json",validation)
    print(json.dumps({"passed":validation["passed"],"total":validation["total"],"failed":[k for k,v in CHECKS.items() if not v]},indent=2))
    return validation

if __name__=="__main__":
    result=build()
    raise SystemExit(0 if result["pass"] else 1)
