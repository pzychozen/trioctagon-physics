"""Atlas 05 independent exact geometry, separated from API and integrity checks.

Run in conda environment torment with -B. No protected source writes occur.
Reference octagon vertices are support-line intersections. Scaffold endpoints
are independently recovered from selected/connector line intersections.
Optional --integrity-dir reads separately captured full before/after inventories.
"""
from __future__ import annotations
import argparse
import ast
from dataclasses import FrozenInstanceError
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import platform
import subprocess
import sys
from datetime import datetime, timezone

sys.dont_write_bytecode=True
import sympy as S

REPO=Path(r'C:\TORMENT\TRIOCTAGON_new\trioctagon-physics')
OLD=Path(r'C:\TORMENT\TRIOCTAGON_new\kernel_TO')
PROD=Path(r'C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric')
BASELINE='0fa3b582c086e51371e8a784bc3dd145f88cfb2b'
SOURCES={
 'D_CODE':REPO/'kernel_physics/reference_scaffold.py',
 'D_PAPER':REPO/'papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md',
 'D_TESTS':REPO/'kernel_physics/tests/test_reference_scaffold.py',
 'D_COORDINATES':REPO/'papers/PAPER_D/v0.1.1/geometry_coordinates.py',
 'D_SYMBOLS':REPO/'papers/PAPER_D/v0.1.1/SYMBOLS_AND_THEOREMS.md',
 'EARLIER_NOTE':REPO/'research_notes/reference_scaffold/note_source.json',
 'GEOMETRY_RECORDS':REPO/'kernel_physics/_geometry_records.py',
 'C_CODE':REPO/'kernel_physics/geometry.py',
 'C_PAPER':REPO/'papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md',
 'B_CODE':REPO/'kernel_physics/face_state.py',
 'B_PAPER':REPO/'papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md',
 'DYNAMICS':REPO/'kernel_physics/dynamics.py',
 'READOUTS':REPO/'kernel_physics/readouts.py',
 'CENSUS':Path(r'C:\Users\Notandi\.codex\reports\TRIOCTAGON_OLD_NEW_KERNEL_ARCHAEOLOGY_CENSUS_v0.1.md'),
 'OLD_VIEWER':OLD/'toy_3d_triocta.py',
 'OLD_3D':OLD/'geometry_3d.py',
 'OLD_TETRA':OLD/'dual_tetra_mapper.py',
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def sim(v):return S.simplify(S.trigsimp(S.expand(v)))
def vec(v):return S.Matrix(v)
def key(v):return tuple(S.expand(sim(x)) for x in v)
def eq(a,b):
 if isinstance(a,S.MatrixBase) or isinstance(b,S.MatrixBase):
  a,b=vec(a),vec(b)
  return a.shape==b.shape and all(sim(x-y)==0 for x,y in zip(a,b))
 return sim(a-b)==0
def rot(a):return S.Matrix([[S.cos(a),-S.sin(a)],[S.sin(a),S.cos(a)]])
def det(v,w):return S.det(S.Matrix.hstack(v,w))
def edges(v):return list(zip(v,v[1:]+v[:1]))
def norm2(v):return sim(v.dot(v))
def area(v):return sim(sum(det(a,b) for a,b in edges(v))/2)
def intersect(n1,b1,n2,b2):
 return S.Matrix.vstack(n1.T,n2.T).inv()*vec([b1,b2])
def serialize(v):
 if isinstance(v,S.MatrixBase):return [[serialize(v[i,j]) for j in range(v.cols)] for i in range(v.rows)]
 if isinstance(v,S.Basic):return str(v)
 if isinstance(v,dict):return {str(k):serialize(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [serialize(x) for x in v]
 return v


def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',required=True,type=Path)
 parser.add_argument('--integrity-dir',type=Path)
 args=parser.parse_args();out=args.output.resolve()
 if any(out==p.resolve() or p.resolve() in out.parents for p in (REPO,OLD,PROD)):
  raise SystemExit('Output inside a protected tree is forbidden')
 source_hashes={k:{'path':str(p),'sha256':sha(p)} for k,p in SOURCES.items()}
 checks=[]
 def check(group,name,condition,evidence=None):
  ok=bool(condition);checks.append({'group':group,'name':name,'passed':ok,'evidence':serialize(evidence)})
  if not ok:print('FAIL',group,name,flush=True)
 s,g=S.symbols('s g_gap',positive=True)
 pr=S.Symbol('p_radius',positive=True)
 r2,r3=S.sqrt(2),S.sqrt(3);half=S.Rational(1,2)
 a=(1+r2)*s/2;b=s/2;p=(s+2*g)/(2*r3);L=p+a;qH=(2*s+g)/(2*r3)
 J=S.Matrix([[0,-1],[1,0]]);R=rot(2*S.pi/3);R60=rot(S.pi/3);mirror=S.diag(1,-1)
 U=[vec([S.cos(2*S.pi*i/3),S.sin(2*S.pi*i/3)]) for i in range(3)]
 T=[J*u for u in U];NG=[R60*u for u in U]
 normals8=[vec([S.cos(j*S.pi/4),S.sin(j*S.pi/4)]) for j in range(8)]
 octagon=[intersect(normals8[j],a,normals8[(j-1)%8],a).applyfunc(sim) for j in range(8)]
 expected_local=[(a,-b),(a,b),(b,a),(-b,a),(-a,b),(-a,-b),(-b,-a),(b,-a)]
 check('EXACT_GEOMETRY','octagon_support_line_derivation_and_order',all(eq(x,vec(y)) for x,y in zip(octagon,expected_local)) and all(sim(a-n.dot(x)).is_nonnegative is True for n in normals8 for x in octagon))
 check('EXACT_GEOMETRY','octagon_metrics_radical_reduction',eq(s/(2*S.tan(S.pi/8)),a) and eq((s/(2*S.sin(S.pi/8)))**2,(2+r2)*s*s/2) and eq(a-b,s/r2) and eq(2*a,(1+r2)*s))
 check('EXACT_GEOMETRY','octagon_regular_rotation_edges_radius_area',all(eq(rot(S.pi/4)*v,octagon[(i+1)%8]) for i,v in enumerate(octagon)) and all(eq(norm2(y-x),s*s) for x,y in edges(octagon)) and all(eq(norm2(v),a*a+b*b) for v in octagon) and eq(area(octagon),2*(1+r2)*s*s))
 check('EXACT_GEOMETRY','radial_tangent_frames_and_C3',all(eq(u.dot(u),1) and eq(t.dot(t),1) and eq(u.dot(t),0) and eq(det(u,t),1) and eq(R*u,U[(i+1)%3]) and eq(R*t,T[(i+1)%3]) for i,(u,t) in enumerate(zip(U,T))))
 A_radius=[pr*u-s*t/2 for u,t in zip(U,T)];B_radius=[pr*u+s*t/2 for u,t in zip(U,T)]
 check('EXACT_GEOMETRY','connector_vector_and_gap_from_radius',all(eq(B_radius[i]-A_radius[i],s*T[i]) and eq(A_radius[(i+1)%3]-B_radius[i],(r3*pr-s/2)*R60*T[i]) for i in range(3)))
 check('EXACT_GEOMETRY','positive_domain_and_parameter_inverse',eq(r3*p-s/2,g) and sim(p-s/(2*r3)).is_positive is True and S.solve(r3*pr-s/2-g,pr)==[p])
 # Recover each endpoint from two support-line equations, independent of API construction.
 A=[intersect(U[i],p,NG[(i-1)%3],qH).applyfunc(sim) for i in range(3)]
 B=[intersect(U[i],p,NG[i],qH).applyfunc(sim) for i in range(3)]
 H=[v for pair in zip(A,B) for v in pair]
 printed=[(p,-s/2),(p,s/2),((s-g)/(2*r3),(s+g)/2),(-(2*s+g)/(2*r3),g/2),(-(2*s+g)/(2*r3),-g/2),((s-g)/(2*r3),-(s+g)/2)]
 check('EXACT_GEOMETRY','support_intersections_match_endpoints_and_printed_vertices',all(eq(A[i],p*U[i]-s*T[i]/2) and eq(B[i],p*U[i]+s*T[i]/2) for i in range(3)) and all(eq(x,vec(y)) for x,y in zip(H,printed)),H)
 D=[y-x for x,y in edges(H)];lengths=[s,g]*3
 check('EXACT_GEOMETRY','all_six_positive_edges_turns_and_closure',all(eq(norm2(D[k]),lengths[k]**2) and eq(D[k-1].dot(D[k]),lengths[k-1]*lengths[k]/2) and eq(det(D[k-1],D[k]),r3*s*g/2) for k in range(6)) and eq(sum(D,S.zeros(2,1)),S.zeros(2,1)))
 planes=list(zip(U,[p]*3))+list(zip(NG,[qH]*3))
 slacks=[[sim(off-n.dot(v)) for n,off in planes] for v in H]
 active=[[i for i,t in enumerate(row) if t==0] for row in slacks]
 check('EXACT_GEOMETRY','all_vertex_inequalities_and_two_active_edges',all(all(t.is_nonnegative is True for t in row) and sum(t==0 for t in row)==2 for row in slacks) and active==[[0,5],[0,3],[1,3],[1,4],[2,4],[2,5]],slacks)
 intersections=[]
 for i,j in itertools.combinations(range(6),2):
  n1,b1=planes[i];n2,b2=planes[j]
  if det(n1,n2)==0:continue
  v=intersect(n1,b1,n2,b2).applyfunc(sim)
  signs=[sim(off-n.dot(v)).is_nonnegative for n,off in planes]
  if all(x is True for x in signs):intersections.append(v)
  else:assert False in signs,('undecidable intersection',i,j)
 check('EXACT_GEOMETRY','all_pair_line_intersections_give_exactly_six_feasible_vertices',len(intersections)==6 and set(map(key,intersections))==set(map(key,H)))
 support=[intersect(U[i],p,U[(i+1)%3],p).applyfunc(sim) for i in range(3)]
 W=s+2*g;cells=[[B[i],support[i],A[(i+1)%3]] for i in range(3)]
 check('EXACT_GEOMETRY','support_triangle_coordinates_and_side',all(eq(support[i],p*(U[i]+r3*T[i])) for i in range(3)) and all(eq(norm2(y-x),W*W) for x,y in edges(support)) and eq(W,2*r3*p))
 check('EXACT_GEOMETRY','all_three_corner_cells_equilateral',all(eq(norm2(y-x),g*g) for cell in cells for x,y in edges(cell)) and all(eq(abs(area(cell)),r3*g*g/4) for cell in cells))
 check('EXACT_GEOMETRY','corner_nonoverlap_barycentric_certificate',eq(1-g/W-half,s/(2*W)) and sim(1-g/W-half).is_positive is True and eq(W-2*g,s))
 tau=S.Symbol('tau',real=True)
 check('EXACT_GEOMETRY','closed_connector_retained_apex_outer_legs_removed',all(eq(qH-NG[i].dot((1-tau)*B[i]+tau*A[(i+1)%3]),0) and eq(qH-NG[i].dot(support[i]),-r3*g/2) and all(eq(qH-NG[i].dot((1-tau)*endpoint+tau*support[i]),-tau*r3*g/2) for endpoint in (B[i],A[(i+1)%3])) for i in range(3)))
 areaH=area(H);RH2=(s*s+s*g+g*g)/3
 check('EXACT_GEOMETRY','circumcircle_perimeter_and_independent_shoelace_area',all(eq(norm2(v),RH2) for v in H) and eq(sum(lengths),3*(s+g)) and eq(areaH,r3*(s*s+4*s*g+g*g)/4) and eq(areaH,area(support)-sum(abs(area(cell)) for cell in cells)))
 check('EXACT_GEOMETRY','two_support_distances_and_incircle_criterion',all(eq(U[i].dot(A[i]),p) and eq(NG[i].dot(B[i]),qH) for i in range(3)) and eq(p-qH,(g-s)/(2*r3)))
 cx,cy,r=S.symbols('cx cy radius',real=True)
 sol=S.solve([p-u.dot(vec([cx,cy]))-r for u in U],(cx,cy,r),dict=True)
 check('EXACT_GEOMETRY','incircle_centre_forced_by_three_selected_supports',len(sol)==1 and all(eq(sol[0][k],v) for k,v in ((cx,0),(cy,0),(r,p))),sol)
 check('EXACT_GEOMETRY','regular_member_metrics_coordinates',all(eq(v.subs(g,s),s*vec([S.cos(-S.pi/6+k*S.pi/3),S.sin(-S.pi/6+k*S.pi/3)])) for k,v in enumerate(H)) and eq(RH2.subs(g,s),s*s) and eq(areaH.subs(g,s),3*r3*s*s/2) and eq(p.subs(g,s),r3*s/2))
 collapsed=[v.subs(g,0) for v in H]
 check('EXACT_LIMIT','zero_gap_three_vertices_support_triangle',len(set(map(key,collapsed)))==3 and set(map(key,collapsed))==set(key(v.subs(g,0)) for v in support) and all(eq(B[i].subs(g,0),A[(i+1)%3].subs(g,0)) for i in range(3)) and eq(areaH.subs(g,0),r3*s*s/4))

 check('EXACT_GEOMETRY','generic_C3_and_role_reflection_permutations',all(eq(R*v,H[(k+2)%6]) and eq(mirror*v,H[(1-k)%6]) for k,v in enumerate(H)))
 regular=[v.subs(g,s) for v in H];lookup={key(v):i for i,v in enumerate(regular)};symmetry=[]
 selected={frozenset((2*i,2*i+1)) for i in range(3)}
 for k,f in itertools.product(range(6),range(2)):
  M=rot(k*S.pi/3)*mirror**f;perm=tuple(lookup[key(M*v)] for v in regular)
  roles={frozenset((perm[2*i],perm[2*i+1])) for i in range(3)}==selected
  symmetry.append({'k60':k,'reflection':f,'permutation':perm,'roles_preserved':roles,'traversal_preserved':f==0})
 check('EXACT_GEOMETRY','regular_D6_role_D3_traversal_C3',len({v['permutation'] for v in symmetry})==12 and sum(v['roles_preserved'] for v in symmetry)==6 and sum(v['roles_preserved'] and v['traversal_preserved'] for v in symmetry)==3)
 witness=[v.subs({s:2,g:1}) for v in H]
 check('EXACT_FALSIFIER','C3_alone_does_not_imply_regular_or_D6',set(key(R*v) for v in witness)==set(map(key,witness)) and set(key(R60*v) for v in witness)!=set(map(key,witness)) and len({norm2(y-x) for x,y in edges(witness)})==2)
 check('EXACT_FALSIFIER','regular_60_degree_rotation_exchanges_E_G',{frozenset((lookup[key(R60*regular[2*i])],lookup[key(R60*regular[2*i+1])])) for i in range(3)}=={frozenset((2*i+1,(2*i+2)%6)) for i in range(3)})
 x,y,z=S.symbols('x y z',real=True)
 planar=lambda i,x,y:(L+x)*U[i]+y*T[i]
 vertical=lambda i,xi,z:vec([p*U[i][0]+xi*T[i][0],p*U[i][1]+xi*T[i][1],z])
 planar_frames=[[planar(i,*v) for v in octagon] for i in range(3)]
 vertical_frames=[[vertical(i,*v) for v in octagon] for i in range(3)]
 check('EXACT_GEOMETRY','complete_planar_isometric_octagons_and_selected_edge_orientation',all(eq(S.Matrix.hstack(U[i],T[i]).T*S.Matrix.hstack(U[i],T[i]),S.eye(2)) and eq(planar_frames[i][4],B[i]) and eq(planar_frames[i][5],A[i]) and eq(sum(planar_frames[i],S.zeros(2,1))/8,L*U[i]) and all(eq(norm2(v-u),s*s) for u,v in edges(planar_frames[i])) for i in range(3)))
 check('EXACT_GEOMETRY','complete_planar_frames_C3_D3_centre_upper_bound',all(set(key(R*v) for v in planar_frames[i])==set(map(key,planar_frames[(i+1)%3])) and set(key(mirror*v) for v in planar_frames[i])==set(map(key,planar_frames[(-i)%3])) for i in range(3)) and set(key(R60*(L*u)) for u in U)!=set(key(L*u) for u in U))
 check('EXACT_GEOMETRY','vertical_frame_centres_normals_top_edges_and_full_octagons',all(eq(sum(vertical_frames[i],S.zeros(3,1))/8,vertical(i,0,0)) and eq(vertical(i,x,z).diff(x).cross(vertical(i,x,z).diff(z)),vec([*U[i],0])) and eq(vertical(i,-s/2,a),vec([*A[i],a])) and eq(vertical(i,s/2,a),vec([*B[i],a])) and all(eq(norm2(v-u),s*s) for u,v in edges(vertical_frames[i])) for i in range(3)))
 check('EXACT_GEOMETRY','vertical_collection_extra_horizontal_reflection',all(set(key(S.diag(1,1,-1)*v) for v in frame)==set(map(key,frame)) for frame in vertical_frames))

 p0=a/r3;g0=s/r2;pstar=r3*s/2;dp=(2-r2)*s/(2*r3);lam=(1+r2)/3
 R30=S.diag(1,1,1);R30[:2,:2]=rot(S.pi/6)
 rigid=lambda point:R30*point+vec([0,a/r3,0])
 c_panels=[vec([-a/2-x/2,r3*a/2-r3*x/2,z]),vec([x,0,z]),vec([a/2-x/2,r3*a/2+r3*x/2,z])]
 perm=[2,0,1]
 check('EXACT_GEOMETRY','paper_C_member_gap_and_scaled_affine_panel_identity',eq(p.subs(g,g0),p0) and all(eq(rigid(vertical(i,x,z).subs(g,g0)),c_panels[perm[i]]) for i in range(3)) and eq(R30.T*R30,S.eye(3)) and eq(R30.det(),1))
 check('EXACT_FALSIFIER','paper_C_member_is_not_regular',sim(g0-s).is_negative is True and eq(g0/s,1/r2))
 check('EXACT_GEOMETRY','radial_translation_preserves_size_height_and_tunes_gap',eq(pstar-p0,dp) and dp.is_positive is True and all(eq(vertical(i,x,z).subs(g,s)-vertical(i,x,z).subs(g,g0),vec([*(dp*U[i]),0])) for i in range(3)))
 check('EXACT_FALSIFIER','radial_translation_is_not_common_rigid_translation',not eq(dp*U[0],dp*U[1]) and eq(sum((dp*u for u in U),S.zeros(2,1)),S.zeros(2,1)) and eq(norm2(pstar*(U[0]-U[1]))-norm2(p0*(U[0]-U[1])),3*(pstar*pstar-p0*p0)))
 la=S.Symbol('lambda_scale',positive=True)
 solution=S.solve(r3*p0-la*s/2-la*s,la)
 check('EXACT_GEOMETRY','special_shrink_factor_derived_only_from_paper_C_start',len(solution)==1 and eq(solution[0],lam) and sim(lam).is_positive is True and sim(1-lam).is_positive is True)
 snew=lam*s;anew=lam*a
 vf_shrunk=lambda i,xi,z:vec([p0*U[i][0]+lam*xi*T[i][0],p0*U[i][1]+lam*xi*T[i][1],lam*z])
 check('EXACT_GEOMETRY','shrink_about_vertical_centres_scales_both_local_coordinates',all(eq(vf_shrunk(i,x,z)-vec([*(p0*U[i]),0]),lam*(vertical(i,x,z).subs(g,g0)-vec([*(p0*U[i]),0]))) for i in range(3)) and eq(r3*p0-snew/2,snew))
 check('EXACT_GEOMETRY','fixed_p_changes_planar_centres_and_top_height',eq((p0+anew)-(p0+a),(lam-1)*a) and sim(a-anew).is_positive is True)
 wrongp=p0+a-lam*a
 check('EXACT_FALSIFIER','fixed_planar_centres_is_different_operation',eq(wrongp-p0,(1-lam)*a) and sim(wrongp-p0).is_positive is True and eq(r3*wrongp-snew/2-snew,r3*(1-lam)*a))
 check('EXACT_FALSIFIER','special_lambda_not_universal_for_arbitrary_starting_p',not eq(r3*pstar-lam*s/2,lam*s) and S.solve(r3*pr-la*s/2-la*s,la)==[2*r3*pr/(3*s)])
 scale=S.Symbol('scale',positive=True)
 check('EXACT_GEOMETRY','global_similarity_preserves_gap_ratio',eq((r3*(scale*p)-(scale*s)/2)/(scale*s),g/s) and eq(areaH.subs({s:scale*s,g:scale*g},simultaneous=True),scale**2*areaH))
 s0=r2-1;sub0={s:s0}
 check('EXACT_GEOMETRY','width_one_shrink_all_exact_metrics',eq(a.subs(sub0),half) and eq(snew.subs(sub0),S.Rational(1,3)) and eq(p0.subs(sub0),1/(2*r3)) and eq((2*anew).subs(sub0),lam) and eq(anew.subs(sub0),(1+r2)/6) and eq(2*r3*p0.subs(sub0),1) and eq((3*r3*snew*snew/2).subs(sub0),r3/6))
 delta,X,Y=S.symbols('delta X Y',nonnegative=True);zp=S.Symbol('z_prime',real=True)
 # Enforce the proven finite-separation domain by p=(a+delta)/sqrt(3).
 vg=lambda i,xi,z:vec([((a+delta)/r3)*U[i][0]+xi*T[i][0],((a+delta)/r3)*U[i][1]+xi*T[i][1],z])
 check('EXACT_GEOMETRY','all_three_finite_face_distance_decompositions',all(eq(norm2(vg(i,a-X,z)-vg((i+1)%3,-a+Y,zp)),delta**2+delta*(X+Y)+(X-Y)**2+X*Y+(z-zp)**2) and eq(norm2(vg(i,a,0)-vg((i+1)%3,-a,0)),delta**2) for i in range(3)))
 check('EXACT_GEOMETRY','plane_intersection_and_full_paper_C_side_seams',all(eq(vertical(i,r3*p,z),vertical((i+1)%3,-r3*p,z)) and eq(vertical(i,a,z).subs(g,g0),vertical((i+1)%3,-a,z).subs(g,g0)) for i in range(3)))
 check('EXACT_GEOMETRY','separation_vs_gap_and_regularization_values',eq(r3*p-a,g-s/r2) and eq(r3*pstar-a,(2-r2)*s/2) and eq((r3*p0-anew).subs(sub0),(2-r2)/6))
 crossp=p.subs(g,s/2)
 check('EXACT_FALSIFIER','negative_signed_delta_is_not_negative_distance',sim(r3*crossp-a).is_negative is True and sim(a-r3*crossp).is_positive is True and eq(vertical(0,r3*p,0).subs(g,s/2),vertical(1,-r3*p,0).subs(g,s/2)),{'chosen_gap':'s/2','plane_intersection_local_xi':r3*crossp,'signed_delta':sim(r3*crossp-a)})
 def weld_count(frames):
  lookup={};cycles=[]
  for frame in frames:
   cycle=[]
   for v in frame:
    k=key(v)
    if k not in lookup:lookup[k]=len(lookup)
    cycle.append(lookup[k])
   cycles.append(cycle)
  edgecount={}
  for f in cycles:
   for i,j in edges(f):
    e=tuple(sorted((i,j)));edgecount[e]=edgecount.get(e,0)+1
  return {'V':len(lookup),'E':len(edgecount),'F':len(cycles),'seams':sum(n==2 for n in edgecount.values())}
 original_frames=[[v.subs({s:s0,g:s0/r2},simultaneous=True) for v in f] for f in vertical_frames]
 translated_frames=[[v.subs({s:s0,g:s0},simultaneous=True) for v in f] for f in vertical_frames]
 shrunk_frames=[[vf_shrunk(i,*v).subs(s,s0) for v in octagon] for i in range(3)]
 counts={'paper_C':weld_count(original_frames),'translated_regular':weld_count(translated_frames),'shrunk_regular':weld_count(shrunk_frames)}
 check('EXACT_FALSIFIER','regular_reference_polygon_does_not_preserve_material_seams',counts=={'paper_C':{'V':18,'E':21,'F':3,'seams':3},'translated_regular':{'V':24,'E':24,'F':3,'seams':0},'shrunk_regular':{'V':24,'E':24,'F':3,'seams':0}},counts)

 # Implementation lane. No API objects are used to form the reference checks above.
 sys.path.insert(0,str(REPO))
 from kernel_physics import reference_scaffold as api
 def raises(fn,errors):
  try:fn()
  except errors:return True
  return False
 def points_equal(xs,ys):return len(xs)==len(ys) and all(eq(vec(x),vec(y)) for x,y in zip(xs,ys))
 model=api.ReferenceScaffold(s,g)
 check('API_EXACT','loaded_authoritative_scaffold_and_parameter_metrics',Path(api.__file__).resolve()==SOURCES['D_CODE'].resolve() and all(eq(getattr(model,k),v) for k,v in {'p':p,'L':L,'area':areaH,'circumradius_squared':RH2,'q_H':qH,'W':W,'regularity_residual':g-s}.items()))
 check('API_EXACT','octagon_vertices_outline_filled_and_metrics',points_equal(model.octagon.vertices,octagon) and model.octagon.outline==tuple(edges(model.octagon.vertices)) and model.octagon.filled.vertices==model.octagon.vertices and eq(model.octagon.a,a) and eq(model.octagon.w,2*a) and eq(model.octagon.R_oct**2,a*a+b*b))
 check('API_EXACT','scaffold_vertices_roles_segments_and_closed_regions',points_equal(model.vertices,H) and points_equal(model.A,A) and points_equal(model.B,B) and model.outline[::2]==model.selected_edges and model.outline[1::2]==model.connectors and model.edge_roles==('E','G')*3 and model.side_lengths==(s,g)*3 and points_equal(model.support_triangle.vertices,support) and all(points_equal(h.vertices,c) for h,c in zip(model.corner_cells,cells)))
 check('API_EXACT','halfplane_definitions_boundary_inclusion_and_apex_exclusion',all(eq(vec(h.normal),n) and eq(h.offset,o) for h,(n,o) in zip(model.filled_hexagon.halfplanes,planes)) and all(model.filled_hexagon.contains(tuple(v)) is True for v in H) and all(model.filled_hexagon.contains(tuple(v)) is False for v in support) and model.filled_hexagon.contains((0,0)) is True)
 check('API_EXACT','complete_planar_and_vertical_frames',all(points_equal(model.planar_frames[i].vertices,planar_frames[i]) and points_equal(model.vertical_frames[i].vertices,vertical_frames[i]) and eq(vec(model.planar_centres[i]),L*U[i]) and eq(vec(model.vertical_centres[i]),vertical(i,0,0)) for i in range(3)))
 check('API_EXACT','top_edges_have_expected_horizontal_endpoints_and_height',all(points_equal(model.top_selected_edges[i],[vec([*A[i],a]),vec([*B[i],a])]) for i in range(3)))
 old=api.paper_c_member(s);moved=api.translate_paper_c_to_regular(s);shrunk=api.shrink_paper_c_at_fixed_centres(s)
 check('API_EXACT','three_named_constructors_have_distinct_semantics',eq(old.p,p0) and eq(old.g_gap,g0) and old.is_regular is False and eq(moved.s,s) and eq(moved.p,pstar) and moved.is_regular is True and eq(shrunk.s,snew) and eq(shrunk.p,p0) and eq(shrunk.octagon.a,anew) and shrunk.is_regular is True)
 check('API_EXACT','rigid_map_formula_on_arbitrary_points',eq(vec(api.paper_c_rigid_map((x,y,z),s)),rigid(vec([x,y,z]))))
 from kernel_physics import geometry as geo
 mesh=geo.folded_module();member0=api.paper_c_member(s0)
 def edge_set(vs):return {frozenset((key(a),key(b))) for a,b in edges(vs)}
 check('API_EXACT','width_one_finite_face_vertex_and_edge_equivalence_to_C',all(set(key(api.paper_c_rigid_map(v,s0)) for v in member0.vertical_frames[i].vertices)==set(key(mesh.vertices[j]) for j in mesh.faces[perm[i]]) and edge_set([api.paper_c_rigid_map(v,s0) for v in member0.vertical_frames[i].vertices])==edge_set([mesh.vertices[j] for j in mesh.faces[perm[i]]]) for i in range(3)))
 check('API_CONTRACT','strict_exact_types_and_positive_domains',api.ReferenceScaffold(Fraction(1,3),2).s==S.Rational(1,3) and all(raises(lambda v=v:api.ReferenceScaffold(v,1),(TypeError,ValueError)) for v in (True,1.0,S.Float(1),'1',S.I,S.oo,0,-1,S.Symbol('unknown'))) and raises(lambda:api.ReferenceScaffold(s,0),ValueError) and raises(lambda:api.ReferenceScaffold.from_radius(s,s/(2*r3)),ValueError) and raises(lambda:api.ReferenceScaffold.from_radius(s,S.Symbol('p_unrelated',positive=True)),ValueError))
 check('API_CONTRACT','three_valued_regularity_and_membership',model.is_regular is None and api.ReferenceScaffold(s,2*s).is_regular is False and api.ReferenceScaffold.regular(s).is_regular is True and model.filled_hexagon.contains((x,0)) is None)
 hull=api.ConvexHull([(0,0),(1,0),(2,0)]);hp=api.HalfPlane((2,0),2)
 check('API_CONTRACT','hull_is_supplied_generator_prescription_not_hull_algorithm',hull.vertices==((0,0),(1,0),(2,0)) and not hasattr(hull,'contains') and eq(hp.slack((1,0)),0) and eq(hp.slack((0,0)),2) and raises(lambda:api.HalfPlane((0,0),1),ValueError))
 check('API_CONTRACT','immutability_and_coordinate_validation',raises(lambda:setattr(model,'s',2),FrozenInstanceError) and raises(lambda:api.paper_c_rigid_map((0,0,0.0),1),TypeError) and raises(lambda:model.planar_point(True,0,0),TypeError) and raises(lambda:model.vertical_point(3,0,0),IndexError) and raises(lambda:model.filled_hexagon.contains((0,0,0)),ValueError))
 xp=S.Symbol('x_positive',positive=True);composite=1/(1+S.sqrt(xp));mc=api.ReferenceScaffold.regular(composite);mhalf=api.ReferenceScaffold.regular(half)
 specialized=[tuple(c.subs(xp,1) for c in v) for v in mc.vertices]
 check('API_CONTRACT','composite_positive_length_substitution_before_simplification',all(c.is_real is True and c.is_finite is True and not c.has(S.zoo,S.nan,S.oo,S.Float) for v in specialized for c in v) and points_equal(specialized,mhalf.vertices) and all(mc.filled_hexagon.contains(v) is True for v in mc.vertices))
 imports=set()
 tree=ast.parse(SOURCES['D_CODE'].read_text(encoding='utf-8-sig'))
 for n in ast.walk(tree):
  if isinstance(n,ast.Import):imports.update(a.name for a in n.names)
  if isinstance(n,ast.ImportFrom):imports.add(n.module)
 check('INTERFACE_BOUNDARY','scaffold_has_no_direct_dynamics_or_state_imports',imports=={'dataclasses','fractions','sympy'},sorted(imports))
 names={n.id for n in ast.walk(tree) if isinstance(n,ast.Name)}
 check('INTERFACE_BOUNDARY','no_Omega_FaceState_or_chirality_input_in_scaffold',not {'Omega','omega','FaceState','z_chiral'}.intersection(names),{'scope':'Static module boundary, supported by Paper D open-interface statement; not proof of absence in all historical software.'})
 freshcode="import sys; import kernel_physics.reference_scaffold as r; r.ReferenceScaffold.regular(1).vertical_frames; assert not any(x in sys.modules for x in ['kernel_physics.geometry','kernel_physics.dynamics','kernel_physics.face_state','kernel_physics.readouts'])"
 child=subprocess.run([sys.executable,'-B','-c',freshcode],cwd=REPO,capture_output=True,text=True)
 check('INTERFACE_BOUNDARY','fresh_process_reference_construction_has_no_state_import',child.returncode==0,{'returncode':child.returncode,'stderr':child.stderr})
 from kernel_physics import dynamics
 config=dynamics.DynamicsConfig(0,0,0,(0,0,0))
 check('INTERFACE_BOUNDARY','gap_length_not_recurrence_coefficient_by_domain_and_scale',config.g==0 and raises(lambda:api.ReferenceScaffold(1,0),ValueError) and eq(api.ReferenceScaffold(2,6).g_gap,2*api.ReferenceScaffold(1,3).g_gap) and config.g==0,{'geometry_units':'mathematical_length','dynamics_role':'coefficient multiplying a state-valued increment; no geometric length calibration','no_relation':'changing scaffold scale does not write DynamicsConfig'})
 check('SOURCE_INTEGRITY','all_consulted_sources_unchanged',all(sha(SOURCES[k])==v['sha256'] for k,v in source_hashes.items()))

 integrity={'status':'NOT_ATTACHED'}
 if args.integrity_dir:
  before=json.loads((args.integrity_dir/'before.json').read_text());after=json.loads((args.integrity_dir/'after.json').read_text());git_before=json.loads((args.integrity_dir/'git_before.json').read_text())
  integrity={'status':'ATTACHED','scopes':{},'git_before':git_before,'git_after':{},'snapshot_files':{}}
  for fn in ('before.json','after.json','git_before.json'):
   pp=args.integrity_dir/fn;integrity['snapshot_files'][fn]={'path':str(pp),'sha256':sha(pp)}
  for label in ('current','old','torment_kernel','torment_checkout'):
   bef,aft=before[label],after[label]
   digest=lambda v:hashlib.sha256(json.dumps(v['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
   changed=sorted(k for k in set(bef['files'])|set(aft['files']) if bef['files'].get(k)!=aft['files'].get(k))
   check('TREE_INTEGRITY',label+'_paths_and_content_unchanged',not changed and bef['tree_sha256']==digest(bef)==aft['tree_sha256']==digest(aft))
   integrity['scopes'][label]={'root':bef['root'],'before_count':bef['count'],'after_count':aft['count'],'before_sha256':bef['tree_sha256'],'after_sha256':aft['tree_sha256'],'changed_paths':changed,'before_interval':[bef['start_utc'],bef['end_utc']],'after_interval':[aft['start_utc'],aft['end_utc']]}
  for label in ('current','torment_checkout'):
   git=lambda *cmd:subprocess.check_output(['git','--no-optional-locks','-C',before[label]['root'],*cmd],text=True).strip()
   ga={'head':git('rev-parse','HEAD'),'tracked_status':git('status','--porcelain','--untracked-files=no')};integrity['git_after'][label]=ga
   check('TREE_INTEGRITY',label+'_git_HEAD_status_unchanged',ga==git_before[label] and ga['tracked_status']=='' and (label!='current' or ga['head']==BASELINE))
  integrity['required_flags']={
   'CURRENT_REPO_CHANGED':'NO' if not integrity['scopes']['current']['changed_paths'] and integrity['git_after']['current']==git_before['current'] else 'YES',
   'OLD_KERNEL_CHANGED':'NO' if not integrity['scopes']['old']['changed_paths'] else 'YES',
   'TORMENT_CHANGED':'NO' if all(not integrity['scopes'][k]['changed_paths'] for k in ('torment_kernel','torment_checkout')) and integrity['git_after']['torment_checkout']==git_before['torment_checkout'] else 'YES',
   'COMMITS':0,'PUSHES':0}
 summary={'total':len(checks),'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'groups':{g:{'total':sum(c['group']==g for c in checks),'passed':sum(c['group']==g and c['passed'] for c in checks)} for g in sorted({c['group'] for c in checks})}}
 result={'atlas':'05','version':'0.1','generated_utc':datetime.now(timezone.utc).isoformat(),'baseline':BASELINE,'interpreter':sys.executable,'python':platform.python_version(),'sympy':S.__version__,'script_sha256':sha(__file__),'summary':summary,'checks':checks,'sources':source_hashes,'integrity':integrity,'exact_data':{'s':s,'g_gap':g,'a':a,'p':p,'L':L,'q_H':qH,'octagon_vertices':octagon,'radial':U,'tangent':T,'hexagon_vertices':H,'vertex_halfplane_slacks':slacks,'active_halfplanes':active,'support_vertices':support,'corner_cells':cells,'area':areaH,'circumradius_squared':RH2,'perimeter':3*(s+g),'regular_symmetry_actions':symmetry,'p0':p0,'p_star':pstar,'delta_p':dp,'shrink_factor':lam,'signed_face_separation':g-s/r2,'finite_face_counts':counts},'scope':['Analytic proofs and finite predicates are distinct.','The g_gap=0 limit is analyzed without admitting it to the runtime domain.','Finite-face distance sqrt(3)*p-a requires p>=a/sqrt(3); signed negativity is not a negative distance.','Historical claims are bounded to referenced sources; missing scripts were not reconstructed.'],'boundary_flags':['PAPER_D_REFERENCE_SCAFFOLD != PAPER_C_MATERIAL_SHELL','g_gap IS A GEOMETRIC LENGTH','g_gap != recurrence coupling g','OMEGA_TO_GAP_INTERFACE = OPEN / UNSPECIFIED'],'actions':{'commits':0,'pushes':0}}
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(serialize(result),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(json.dumps(summary,indent=2));print('OUTPUT',out)
 return int(summary['failed']!=0)

if __name__=='__main__':raise SystemExit(main())
