"""Atlas 03: independent exact geometry, separate API parity, read-only sources.

Run in conda environment torment, with Python -B, from any working directory:
  python -B TRIOCTAGON_ATLAS_03_EXACT_CHECKS.py --output <external-results.json>
The optional --integrity-dir reads separately captured before.json/after.json.
This file never fingerprints or writes any protected tree itself. It reconstructs
the octagon from support lines and the panels from rotations, not kernel imports.
Only the separate API_PARITY group executes geometry.py using runpy, with bytecode
disabled. Finite predicates supplement the analytic proofs in the source packet.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import platform
import runpy
import subprocess
import sys

sys.dont_write_bytecode = True
import sympy as S

REPO = Path(r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics")
OLD = Path(r"C:\TORMENT\TRIOCTAGON_new\kernel_TO")
PROD = Path(r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric")
BASELINE = "0fa3b582c086e51371e8a784bc3dd145f88cfb2b"
PROD_HEAD = "a06edcc5c9df5d3b56405085d9f2942b768dc203"
SOURCES = {
    "C_CODE": REPO / "kernel_physics/geometry.py",
    "C_PAPER": REPO / "papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md",
    "C_TESTS": REPO / "kernel_physics/tests/test_geometry.py",
    "C_ORACLE": REPO / "kernel_physics/tests/parity_oracles/geometry_oracle.py",
    "C_SYMBOLS": REPO / "papers/PAPER_C/PAPER_C_SYMBOLS_AND_IDENTITIES_v0.2.md",
    "C_AUDIT": REPO / "papers/PAPER_C/PAPER_C_PROOF_AUDIT_v0.2.2.md",
    "C_SPEC": REPO / "research_files/reconstruction/TRIOCTAGON_ACTUAL_GEOMETRY_SPEC_v0.2.md",
    "B_CODE": REPO / "kernel_physics/face_state.py",
    "B_PAPER": REPO / "papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md",
    "DYNAMICS": REPO / "kernel_physics/dynamics.py",
    "OLD_3D": OLD / "geometry_3d.py",
    "OLD_EMBEDDINGS": OLD / "geometry_embeddings.py",
    "OLD_TETRA": OLD / "dual_tetra_mapper.py",
    "OLD_CURVES": OLD / "analysis_tools.py",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sim(x):
    return S.simplify(S.trigsimp(x))


def vec(x):
    return S.Matrix(x)


def key(x):
    return tuple(S.expand(sim(v)) for v in x)


def same(a, b):
    if isinstance(a, S.MatrixBase) or isinstance(b, S.MatrixBase):
        a, b = vec(a), vec(b)
        return a.shape == b.shape and all(sim(x - y) == 0 for x, y in zip(a, b))
    return sim(a - b) == 0


def allsame(pairs):
    return all(same(a, b) for a, b in pairs)


def edges(cycle):
    return list(zip(cycle, cycle[1:] + cycle[:1]))


def length2(v):
    return sim(vec(v).dot(vec(v)))


def length(v):
    # Principal nonnegative length; denest exact radicals before comparison.
    return sim(S.sqrtdenest(S.sqrt(length2(v))))


def area2(points):
    return sim(abs(sum(a[0]*b[1] - a[1]*b[0] for a, b in edges(points))) / 2)


def rotation(angle):
    return S.Matrix([[S.cos(angle), -S.sin(angle), 0],
                     [S.sin(angle), S.cos(angle), 0], [0, 0, 1]])


def connected(adjacency):
    if not adjacency:
        return False
    seen, todo = set(), [next(iter(adjacency))]
    while todo:
        n = todo.pop()
        if n not in seen:
            seen.add(n)
            todo.extend(adjacency[n])
    return seen == set(adjacency)


def incidence(faces):
    return Counter(tuple(sorted(e)) for f in faces for e in edges(f))


def boundary_cycles(faces):
    adj = defaultdict(list)
    for (a, b), count in incidence(faces).items():
        if count == 1:
            adj[a].append(b)
            adj[b].append(a)
    if not all(len(v) == 2 for v in adj.values()):
        raise ValueError("Boundary degrees are not two")
    unseen, loops = set(adj), []
    while unseen:
        start = min(unseen)
        loop, prev, cur = [start], start, min(adj[start])
        while cur != start:
            if cur in loop:
                raise ValueError("Premature cycle")
            loop.append(cur)
            nxt = next(v for v in adj[cur] if v != prev)
            prev, cur = cur, nxt
        unseen.difference_update(loop)
        loops.append(tuple(loop))
    return loops, dict(adj)


def cycle_sign(image, target):
    image, target = tuple(image), tuple(target)
    for sign, seq in [(1, target), (-1, target[::-1])]:
        for k in range(len(seq)):
            if image == seq[k:] + seq[:k]:
                return sign
    return 0


def wire(x):
    if isinstance(x, S.MatrixBase):
        return [wire(v) for v in x]
    if isinstance(x, S.Basic):
        return str(x)
    if isinstance(x, dict):
        return {str(k): wire(v) for k, v in x.items()}
    if isinstance(x, (list, tuple, set)):
        return [wire(v) for v in x]
    return x


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--integrity-dir", type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if any(output == p.resolve() or p.resolve() in output.parents for p in (REPO, OLD, PROD)):
        raise SystemExit("Refusing output inside a protected source tree")
    source_hashes = {name: {"path": str(path), "sha256": sha(path)} for name, path in SOURCES.items()}
    checks = []

    def check(group, name, condition, evidence=None):
        passed = bool(condition)
        checks.append({"group": group, "name": name, "passed": passed, "evidence": wire(evidence)})
        if not passed:
            print("FAIL:", group, name, flush=True)

    a = S.Rational(1, 2)
    s, h = S.sqrt(2)-1, (S.sqrt(2)-1)/2
    d = a-h
    ez = vec([0, 0, 1])
    origin = vec([0, S.sqrt(3)/6, 0])
    u, z, beta = S.symbols("u z beta", real=True)
    support = [vec([S.cos(S.pi+j*S.pi/4), S.sin(S.pi+j*S.pi/4)]) for j in range(8)]
    local = []
    for j in range(8):
        matrix = S.Matrix.vstack(support[j].T, support[(j+1) % 8].T)
        local.append(vec(key(matrix.inv()*vec([a, a]))))
    printed_local = [(-a, -h), (-h, -a), (h, -a), (a, -h),
                     (a, h), (h, a), (-h, a), (-a, h)]
    r45 = rotation(S.pi/4)[:2, :2]
    check("EXACT_MATH", "octagon_support_intersections_match_material_order", allsame(zip(local, printed_local)), local)
    check("EXACT_MATH", "octagon_convex_eight_distinct_support_vertices", len(set(map(key, local))) == 8 and all(sim(n.dot(v)-a) <= 0 for n in support for v in local))
    check("EXACT_MATH", "octagon_rotation_transitive_regular", allsame((r45*local[j], local[(j+1) % 8]) for j in range(8)))
    check("EXACT_MATH", "octagon_edges_and_interior_angles", all(same(length2(q-p), s*s) for p, q in edges(local)) and all(same((local[(j-1)%8]-local[j]).dot(local[(j+1)%8]-local[j])/s**2, -S.sqrt(2)/2) for j in range(8)))
    check("EXACT_MATH", "octagon_apothem_circumradius_and_width", all(same(length2(n), 1) for n in support) and all(same(length2(p), 1/(2+S.sqrt(2))) for p in local) and same(max(p[0] for p in local)-min(p[0] for p in local), 1))
    diagonal_sq = [s*s, 2-S.sqrt(2), S.Integer(1), 4-2*S.sqrt(2)]
    check("EXACT_MATH", "octagon_all_four_chord_classes", all(same(length2(local[(j+m)%8]-local[j]), diagonal_sq[m-1]) for m in range(1,5) for j in range(8)), diagonal_sq)
    check("EXACT_MATH", "octagon_centroid_and_area", same(sum(local, S.zeros(2,1)), S.zeros(2,1)) and same(area2(local), 2*s))
    local_mirrors = []
    for j in range(8):
        v = vec([S.cos(j*S.pi/8), S.sin(j*S.pi/8)])
        matrix = 2*v*v.T-S.eye(2)
        local_mirrors.append(all(key(matrix*p) in set(map(key, local)) for p in local))
    check("EXACT_MATH", "octagon_eight_reflection_axes", all(local_mirrors))

    # Construct from hinge rotations; compare to independently transcribed formulas.
    left, right, reverse = vec([-a,0,0]), vec([a,0,0]), vec([-u,0,z])
    maps = [left+rotation(beta)*(reverse-left), vec([u,0,z]), right+rotation(-beta)*(reverse-right)]
    formulas = [vec([-a+(a-u)*S.cos(beta), (a-u)*S.sin(beta), z]),
                vec([u,0,z]), vec([a-(a+u)*S.cos(beta), (a+u)*S.sin(beta), z])]
    check("EXACT_MATH", "general_maps_from_hinge_rotations", allsame(zip(maps, formulas)), maps)
    jacobians = [p.jacobian([u,z]) for p in maps]
    normals_beta = [p.diff(u).cross(p.diff(z)) for p in maps]
    check("EXACT_MATH", "all_real_beta_panel_isometries", all(same(j.T*j, S.eye(2)) for j in jacobians))
    check("EXACT_MATH", "fixed_two_hinges_for_all_real_beta", same(maps[0].subs(u,a), maps[1].subs(u,-a)) and same(maps[2].subs(u,-a), maps[1].subs(u,a)))
    gap = (maps[2].subs(u,a)-maps[0].subs(u,-a)).applyfunc(sim)
    check("EXACT_MATH", "free_edges_identical_y_z_and_exact_x_gap", same(gap, vec([1-2*S.cos(beta),0,0])), gap)
    closing = S.solveset(gap[0], beta, domain=S.Interval(0,S.pi))
    check("EXACT_MATH", "restricted_closure_unique_pi_over_3", closing == S.FiniteSet(S.pi/3), closing)
    check("EXACT_MATH", "general_normal_relations", all(same(length2(n), 1) for n in normals_beta) and same(sum(normals_beta, S.zeros(3,1)), vec([0,2*S.cos(beta)-1,0])) and same(normals_beta[0].dot(normals_beta[2]), S.cos(2*beta)))
    V, H = S.diag(-1,1,1), S.diag(1,1,-1)
    check("EXACT_MATH", "general_beta_vertical_and_horizontal_set_symmetries", same(V*maps[0], maps[2].subs(u,-u)) and same(V*maps[1], maps[1].subs(u,-u)) and all(same(H*p, p.subs(z,-z)) for p in maps))

    def build(angle):
        verts, index, faces, aliases = [], {}, [], defaultdict(list)
        for panel, p in enumerate(maps):
            cycle = []
            for j, q in enumerate(local):
                xyz = key(p.subs({beta:angle, u:q[0], z:q[1]}))
                if xyz not in index:
                    index[xyz] = len(verts)
                    verts.append(vec(xyz))
                idx = index[xyz]
                cycle.append(idx)
                aliases[idx].append(f"P{panel+1}:v{j}")
            faces.append(tuple(cycle))
        return verts, faces, aliases

    vertices, faces, aliases = build(S.pi/3)
    expected_vertices = [
        (0,S.sqrt(3)/2,-h),(-a+S.sqrt(2)/4,S.sqrt(6)/4,-a),(-S.sqrt(2)/4,S.sqrt(3)/2-S.sqrt(6)/4,-a),
        (-a,0,-h),(-a,0,h),(-S.sqrt(2)/4,S.sqrt(3)/2-S.sqrt(6)/4,a),(-a+S.sqrt(2)/4,S.sqrt(6)/4,a),
        (0,S.sqrt(3)/2,h),(-h,0,-a),(h,0,-a),(a,0,-h),(a,0,h),(h,0,a),(-h,0,a),
        (S.sqrt(2)/4,S.sqrt(3)/2-S.sqrt(6)/4,-a),(a-S.sqrt(2)/4,S.sqrt(6)/4,-a),
        (a-S.sqrt(2)/4,S.sqrt(6)/4,a),(S.sqrt(2)/4,S.sqrt(3)/2-S.sqrt(6)/4,a)]
    expected_faces = [(0,1,2,3,4,5,6,7),(3,8,9,10,11,12,13,4),(10,14,15,0,7,16,17,11)]
    check("EXACT_MATH", "welded_coordinates_match_paper_C_table", len(vertices)==18 and allsame(zip(vertices, expected_vertices)))
    check("EXACT_MATH", "outward_face_cycles_match_paper_C", faces == expected_faces, faces)
    check("EXACT_MATH", "six_pair_merges_no_triple", Counter(map(len, aliases.values())) == Counter({1:12,2:6}), aliases)
    inc = incidence(faces)
    seams = sorted(e for e,n in inc.items() if n==2)
    boundary = sorted(e for e,n in inc.items() if n==1)
    check("EXACT_MATH", "edge_incidence_21_with_3_seams_18_boundary", len(inc)==21 and len(boundary)==18 and seams==[(0,7),(3,4),(10,11)] and set(inc.values())=={1,2}, sorted(inc))
    check("EXACT_MATH", "all_mesh_edges_length_s", all(same(length2(vertices[i]-vertices[j]),s*s) for i,j in inc))
    directed = Counter(e for face in faces for e in edges(face))
    check("EXACT_MATH", "coherent_face_orientation", max(directed.values())==1 and all(directed[a,b]==directed[b,a]==1 for a,b in seams))
    adjacency = defaultdict(set)
    for i,j in inc:
        adjacency[i].add(j); adjacency[j].add(i)
    face_adjacency = {i: {j for j,f in enumerate(faces) if j!=i and len(set(faces[i])&set(f))==2} for i in range(3)}
    check("EXACT_MATH", "one_skeleton_and_panel_graph_connected", connected(adjacency) and connected(face_adjacency) and all(len(v)==2 for v in face_adjacency.values()))
    links = {}
    for vertex in range(len(vertices)):
        link = defaultdict(set)
        link_edges = []
        for face in faces:
            if vertex in face:
                pos = face.index(vertex)
                x,y = face[pos-1],face[(pos+1)%len(face)]
                link[x].add(y);link[y].add(x);link_edges.append((x,y))
        links[vertex] = {"edges":link_edges, "degrees":sorted(map(len,link.values())), "connected":connected(link)}
    check("EXACT_MATH", "all_18_vertex_links_intervals", all(v["connected"] and v["degrees"] in ([1,1],[1,1,2]) for v in links.values()) and Counter(len(v["edges"]) for v in links.values())==Counter({1:12,2:6}), links)
    loops, boundary_adj = boundary_cycles(faces)
    check("EXACT_MATH", "two_degree_two_nine_edge_rims", loops==[(0,1,2,3,8,9,10,14,15),(4,5,6,7,16,17,11,12,13)] and len(boundary_adj)==18, loops)
    check("EXACT_MATH", "rim_sign_separation_and_induced_orientation", all(vertices[j][2]<0 for j in loops[0]) and all(vertices[j][2]>0 for j in loops[1]) and all(directed[e]==1 for loop in loops for e in edges(loop)))
    chi = len(vertices)-len(inc)+len(faces)
    check("EXACT_MATH", "euler_and_conditional_genus_arithmetic", chi==0 and S.Rational(2-len(loops)-chi,2)==0, {"V":18,"E":21,"F":3,"chi":chi,"b":len(loops),"g_given_surface_hypotheses":0})

    canonical_maps = [p.subs(beta,S.pi/3) for p in maps]
    centres = [sum((vertices[j] for j in face), S.zeros(3,1))/8 for face in faces]
    normals = []
    for face in faces:
        p,q,r = [vertices[j] for j in face[:3]]
        n = (q-p).cross(r-p)
        normals.append((n/length(n)).applyfunc(sim))
    normal_table = [vec([-S.sqrt(3)/2,a,0]), vec([0,-1,0]), vec([S.sqrt(3)/2,a,0])]
    check("EXACT_MATH", "normals_derived_from_oriented_faces", allsame(zip(normals,normal_table)) and allsame((n,p.subs(beta,S.pi/3)) for n,p in zip(normals,normals_beta)), normals)
    check("EXACT_MATH", "normals_unit_pair_120_sum_zero_rank_two", all(same(length2(n),1) for n in normals) and all(same(normals[i].dot(normals[j]),-a) for i in range(3) for j in range(i+1,3)) and same(sum(normals,S.zeros(3,1)),S.zeros(3,1)) and S.Matrix.hstack(*normals).rank()==2)
    check("EXACT_MATH", "normal_cyclic_cross_handedness", all(same(normals[i].cross(normals[(i+1)%3]),S.sqrt(3)/2*ez) for i in range(3)))
    check("EXACT_MATH", "centres_outward_plane_offsets", all(same(c,origin+S.sqrt(3)/6*n) for c,n in zip(centres,normals)) and all(same(normals[i].dot(vertices[j]-origin),S.sqrt(3)/6) for i,f in enumerate(faces) for j in f), centres)
    check("EXACT_MATH", "three_support_halfspaces_and_only_seam_equalities", all(sim(normals[i].dot(v-origin)-S.sqrt(3)/6)<=0 for i in range(3) for v in vertices) and all({j for j,v in enumerate(vertices) if same(normals[i].dot(v-origin),S.sqrt(3)/6)}==set(faces[i]) for i in range(3)))
    check("EXACT_MATH", "pair_plane_intersections_are_vertical_seam_lines", all(same(length2(normals[i].cross(normals[j])),S.Rational(3,4)) and all(same(normals[k].dot(vertices[q]-origin),S.sqrt(3)/6) for k in (i,j) for q in set(faces[i])&set(faces[j])) for i in range(3) for j in range(i+1,3)))
    check("EXACT_MATH", "surface_vertex_and_area_centroids", same(sum(vertices,S.zeros(3,1))/18,origin) and same(sum(centres,S.zeros(3,1))/3,origin))
    pairdist = [length(centres[i]-centres[j]) for i in range(3) for j in range(i+1,3)]
    check("EXACT_MATH", "ambient_panel_centre_distances", all(same(x,a) for x in pairdist), pairdist)
    face_areas = [sim(length(sum((vertices[i].cross(vertices[j]) for i,j in edges(face)),S.zeros(3,1)))/2) for face in faces]
    check("EXACT_MATH", "panel_and_total_material_areas", all(same(x,2*s) for x in face_areas) and same(sum(face_areas),6*s), face_areas)
    check("EXACT_MATH", "material_unique_seam_boundary_lengths", same(sum(length(vertices[i]-vertices[j]) for i,j in seams),3*s) and same(sum(length(vertices[i]-vertices[j]) for i,j in boundary),18*s) and same(sum(length(vertices[i]-vertices[j]) for i,j in inc),21*s) and same(sum(len(f)*s for f in faces),24*s))
    bounds = [(min(p[j] for p in vertices),max(p[j] for p in vertices)) for j in range(3)]
    check("EXACT_MATH", "ambient_bounding_box", bounds==[(-a,a),(S.Integer(0),S.sqrt(3)/2),(-a,a)], bounds)
    chamfers = [(i,j) for i,j in boundary if vertices[i][2]!=vertices[j][2]]
    check("EXACT_MATH", "twelve_chamfer_edges_45_degrees", len(chamfers)==12 and all(same((vertices[i][2]-vertices[j][2])**2,d*d) and same(sum((vertices[i][k]-vertices[j][k])**2 for k in (0,1)),d*d) for i,j in chamfers))
    check("EXACT_MATH", "three_angle_conventions", same(S.acos(normals[0].dot(normals[1])),2*S.pi/3) and same(S.pi-S.acos(normals[0].dot(normals[1])),S.pi/3) and same(left+rotation(-2*S.pi/3)*(vec([u-1,0,z])-left),canonical_maps[0]))

    corners = [vec([-a,0,0]),vec([a,0,0]),vec([0,S.sqrt(3)/2,0])]
    section_endpoints = [key(p.subs({u:t,z:0})) for p in canonical_maps for t in (-a,a)]
    check("EXACT_MATH", "section_all_three_segments_corners", Counter(section_endpoints)==Counter({key(c):2 for c in corners}) and all(same(length(q-p),1) for p,q in edges(corners)))
    triangle_area = area2(corners)
    check("EXACT_MATH", "enclosed_triangle_area_altitude_radii", same(triangle_area,S.sqrt(3)/4) and same(length((corners[2]-corners[0]).cross(corners[1]-corners[0]))/length(corners[1]-corners[0]),S.sqrt(3)/2) and same(triangle_area/(S.Rational(3,2)),S.sqrt(3)/6) and all(same(length(c-origin),S.sqrt(3)/3) for c in corners))
    check("FALSIFIER", "central_centroid_not_on_shell_or_cap", all(not same(n.dot(origin-c),0) for n,c in zip(normals,centres)) and len(faces)==3)
    # Support inequalities give |u|<=a and |u|+|z|<=a+h; this is a symbolic
    # boundary identity plus endpoints, not a sampled proof of all-height sections.
    w_outer = 2*(a+h-z)
    check("EXACT_MATH", "central_and_chamfer_width_formula_join", same(w_outer.subs(z,h),1) and same(w_outer.subs(z,a),s) and same(w_outer,1+s-2*z) and all(same(abs(q[0])+abs(q[1]),a+h) for q in local))
    notch_records = []
    for tip in sorted(set(q for seam in seams for q in seam)):
        nbr = sorted(boundary_adj[tip])
        e1,e2 = [vertices[j]-vertices[tip] for j in nbr]
        proj1,proj2 = vec([e1[0],e1[1],0]),vec([e2[0],e2[1],0])
        cross = e1.cross(e2)
        notch_records.append({"tip":tip,"neighbors":nbr,"tip_cos":sim(e1.dot(e2)/s**2),"area":length(cross)/2})
        check("EXACT_MATH", f"notch_{tip}_spatial_projected_angles_areas_plane", same(length(e1),s) and same(length(e2),s) and same(length(e1-e2),d) and same(e1.dot(e2)/s**2,S.Rational(3,4)) and same((-e1).dot(e2-e1)/(s*d),S.sqrt(2)/4) and all(same(length(v),d) for v in [proj1,proj2,proj1-proj2]) and same(length(cross)/2,S.sqrt(7)/8*s**2) and same(length(proj1.cross(proj2))/2,S.sqrt(3)/8*s**2) and same((cross[0]**2+cross[1]**2)/cross[2]**2,S.Rational(4,3)))
    hex_ids = (5,6,16,17,12,13)
    hexagon = [vertices[j] for j in hex_ids]
    hex_lengths = [length(q-p) for p,q in edges(hexagon)]
    check("EXACT_MATH", "rim_hexagon_alternating_sides_equiangular", allsame(zip(hex_lengths,[s,d,s,d,s,d])) and all(same((hexagon[j-1]-hexagon[j]).dot(hexagon[(j+1)%6]-hexagon[j])/(s*d),-a) for j in range(6)))
    hex_area = area2(hexagon)
    check("EXACT_MATH", "hexagon_and_projected_notch_partition", same(hex_area,S.sqrt(3)/4*(1-3*d*d)) and same(hex_area,-7*S.sqrt(3)/8+3*S.sqrt(6)/4) and same(hex_area+3*S.sqrt(3)/8*s*s,triangle_area))
    check("EXACT_MATH", "rim_projection_side_partition_and_lengths", same(2*d+s,1) and all(same(sum(length(vertices[j]-vertices[i]) for i,j in edges(loop)),9*s) and same(sum(length(vec([vertices[j][0]-vertices[i][0],vertices[j][1]-vertices[i][1],0])) for i,j in edges(loop)),3) for loop in loops))
    check("FALSIFIER", "rims_nonplanar_and_hexagon_not_regular", S.Matrix.hstack(vertices[6]-vertices[5],vertices[16]-vertices[5],vertices[7]-vertices[5]).det()!=0 and not same(s,d))

    R = rotation(2*S.pi/3)
    lookup = {key(v):j for j,v in enumerate(vertices)}
    def permutation(matrix):
        return tuple(lookup[key(origin+matrix*(v-origin))] for v in vertices)
    generators = {"R":R,"V":V,"H":H}
    generator_records = {}
    def action(matrix):
        perm = permutation(matrix)
        face_perm, signs = [], []
        for f in faces:
            image = tuple(perm[j] for j in f)
            target = next(i for i,g in enumerate(faces) if set(g)==set(image))
            face_perm.append(target+1);signs.append(cycle_sign(image,faces[target]))
        seam_perm = [seams.index(tuple(sorted(perm[q] for q in e))) for e in seams]
        rim_perm, rim_signs = [], []
        for loop in loops:
            image = tuple(perm[j] for j in loop)
            target = next(i for i,g in enumerate(loops) if set(g)==set(image))
            rim_perm.append(target);rim_signs.append(cycle_sign(image,loops[target]))
        return {"vertices":perm,"faces_1based":face_perm,"seams_sorted_0based":seam_perm,"rims_0based":rim_perm,"face_orientation":signs,"rim_orientation":rim_signs,"determinant":matrix.det()}
    for name,matrix in generators.items():
        rec = action(matrix);generator_records[name]=rec
        check("EXACT_MATH", f"generator_{name}_face_edge_seam_rim_orientation", sorted(rec["vertices"])==list(range(18)) and set(tuple(sorted((rec["vertices"][i],rec["vertices"][j]))) for i,j in inc)==set(inc) and all(v==matrix.det() for v in rec["face_orientation"]+rec["rim_orientation"]), rec)
    check("EXACT_MATH", "D3h_generator_relations", same(R**3,S.eye(3)) and R!=S.eye(3) and same(V**2,S.eye(3)) and same(H**2,S.eye(3)) and same(V*R*V,R**2) and same(H*R,R*H) and same(H*V,V*H))
    group = {}
    for k in range(3):
        for v in range(2):
            for hpow in range(2):
                name = f"R^{k} V^{v} H^{hpow}"
                matrix = R**k*V**v*H**hpow
                group[name]=action(matrix)
    group_perms = {tuple(rec["vertices"]) for rec in group.values()}
    check("EXACT_MATH", "twelve_distinct_group_elements_closed_under_composition", len(group_perms)==12 and all(tuple(p[q[j]] for j in range(18)) in group_perms for p in group_perms for q in group_perms))
    check("EXACT_MATH", "six_proper_six_improper_actions", Counter(int(rec["determinant"]) for rec in group.values())==Counter({1:6,-1:6}) and all(all(sign==rec["determinant"] for sign in rec["face_orientation"]) for rec in group.values()))
    covariance = sum(((v-origin)*(v-origin).T for v in vertices),S.zeros(3,3))/18
    check("EXACT_MATH", "vertex_covariance_vertical_axis_distinct", same(covariance,S.diag((1+s*s)/12,(1+s*s)/12,(2+s*s)/12)) and not same(covariance[0,0],covariance[2,2]))
    check("EXACT_MATH", "seams_parallel_equal_midpoint_triangle", all(same(vertices[j]-vertices[i],s*ez) for i,j in seams) and same(sum(((vertices[i]+vertices[j])/2 for i,j in seams),S.zeros(3,1))/3,origin))
    check("FALSIFIER", "whole_shell_not_30_or_45_degree_rotation_symmetric", all(any(key(origin+rotation(angle)*(v-origin)) not in lookup for v in vertices) for angle in (S.pi/6,S.pi/4)))
    check("FALSIFIER", "not_24_distinct_vertices_and_not_closed_torus", len(vertices)!=24 and len(loops)!=0 and S.Rational(2-len(loops)-chi,2)!=1)
    check("FALSIFIER", "three_normals_not_orthogonal_3D_basis", S.Matrix.hstack(*normals).det()==0 and not same(normals[0].dot(normals[1]),0))
    quarter_vertices,quarter_faces,_ = build(S.pi/2)
    quarter_inc = incidence(quarter_faces)
    quarter_loops,_ = boundary_cycles(quarter_faces)
    check("FALSIFIER", "nonclosing_pi_over_2_has_different_combinatorics", same(gap.subs(beta,S.pi/2),vec([1,0,0])) and (len(quarter_vertices),len(quarter_inc),len(quarter_faces),len(quarter_loops))==(20,22,3,1) and sum(v==2 for v in quarter_inc.values())==2, {"angle":"pi/2","V":len(quarter_vertices),"E":len(quarter_inc),"F":3,"b":len(quarter_loops)})
    flat_vertices,flat_faces,_ = build(0)
    check("FALSIFIER", "beta_zero_panels_overlap", len(flat_vertices)==8 and set(flat_faces[0])==set(flat_faces[1])==set(flat_faces[2]))
    reflected_origin = vec([0,-S.sqrt(3)/6,0])
    check("FALSIFIER", "negative_closing_branch_material_normals_are_inward", same(gap.subs(beta,-S.pi/3),S.zeros(3,1)) and all(same(n.subs(beta,-S.pi/3).dot(p.subs({beta:-S.pi/3,u:0,z:0})-reflected_origin),-S.sqrt(3)/6) for n,p in zip(normals_beta,maps)))

    tangents = [ez.cross(n) for n in normals]
    check("INTERFACE_GEOMETRY", "Paper_B_tangent_frames_from_geometry_only", all(same(t, p.diff(u)) and same(S.Matrix.hstack(t,ez,n).T*S.Matrix.hstack(t,ez,n),S.eye(3)) and same(S.Matrix.hstack(t,ez,n).det(),1) for t,n,p in zip(tangents,normals,canonical_maps)), {"centres":centres,"normals":normals,"vertical":ez,"tangents":tangents})

    # API comparisons are deliberately separate from the independent mathematics.
    api = runpy.run_path(str(SOURCES["C_CODE"]),run_name="__atlas03_geometry_parity__")
    mesh = api["folded_module"]()
    check("API_PARITY", "geometry_api_welded_vertices_faces", len(mesh.vertices)==len(vertices) and allsame(zip(mesh.vertices,vertices)) and list(mesh.faces)==faces)
    check("API_PARITY", "geometry_api_edges_seams_rims_euler", list(mesh.edges)==sorted(inc) and list(mesh.seam_edges)==seams and list(mesh.boundary_edges)==boundary and list(mesh.boundary_loops)==loops and mesh.euler_characteristic==chi)
    check("API_PARITY", "geometry_api_general_maps", all(same(vec(api["panel_point"](i+1,u,z,beta)),maps[i]) for i in range(3)))
    check("API_PARITY", "geometry_api_normals_and_dihedrals", all(same(vec(mesh.face_normal(i)),normals[i]) for i in range(3)) and all(same(mesh.normal_separation(i,j),2*S.pi/3) and same(mesh.interior_dihedral(i,j),S.pi/3) for i in range(3) for j in range(i+1,3)))
    check("API_PARITY", "geometry_api_symmetry_generators", all(same(vec(api[fn](tuple(p))),origin+matrix*(p-origin)) for fn,matrix in [("rotate_c3",R),("reflect_vertical",V),("reflect_horizontal",H)] for p in vertices))
    section_heights = (-h,S.Integer(0),h)
    check("API_PARITY", "geometry_api_central_sections", all(all(same(vec(pair[0]),corners[i]+height*ez) and same(vec(pair[1]),corners[(i+1)%3]+height*ez) for i,pair in enumerate(api["central_section"](height))) for height in section_heights))
    rejected = []
    for height in (a, S.I, S.Symbol("undecided")):
        try:
            api["central_section"](height)
        except ValueError:
            rejected.append(str(height))
    check("API_PARITY", "geometry_api_rejects_outside_nonreal_undecidable_sections", len(rejected)==3,rejected)

    import ast
    geo_ast = ast.parse(SOURCES["C_CODE"].read_text(encoding="utf-8-sig"))
    dyn_ast = ast.parse(SOURCES["DYNAMICS"].read_text(encoding="utf-8-sig"))
    def imports(tree):
        out = []
        for node in ast.walk(tree):
            if isinstance(node,ast.Import): out.extend(x.name for x in node.names)
            if isinstance(node,ast.ImportFrom): out.extend([node.module or ""]+[x.name for x in node.names])
        return out
    check("SOURCE_BOUNDARY", "direct_imports_do_not_couple_geometry_and_dynamics", not any("dynamics" in name for name in imports(geo_ast)) and not any("geometry" in name for name in imports(dyn_ast)), {"geometry_imports":imports(geo_ast),"dynamics_imports":imports(dyn_ast),"scope":"Direct imports only; not a theorem about all repository call paths. See packet boundary analysis."})
    check("SOURCE_BOUNDARY", "geometry_public_signatures_have_no_Omega_argument", all(not any(arg.arg.lower()=="omega" for arg in node.args.args) for node in ast.walk(geo_ast) if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef))), "Static API observation, not a physical inference; Paper B supplies a separate optional representation.")
    check("SOURCE_BOUNDARY", "all_consulted_sources_unchanged_during_checks", all(sha(SOURCES[name])==item["sha256"] for name,item in source_hashes.items()))

    integrity = {"status":"NOT_ATTACHED","method":"Full file SHA-256 maps excluding .git; see external snapshot option."}
    if args.integrity_dir:
        before = json.loads((args.integrity_dir/"before.json").read_text(encoding="utf-8-sig"))
        after = json.loads((args.integrity_dir/"after.json").read_text(encoding="utf-8-sig"))
        integrity = {"status":"ATTACHED","scopes":{},"snapshot_paths":{"before":str(args.integrity_dir/"before.json"),"after":str(args.integrity_dir/"after.json")},"snapshot_sha256":{"before":sha(args.integrity_dir/"before.json"),"after":sha(args.integrity_dir/"after.json")},"excluded":".git administrative contents; timestamps, ACLs and empty directories are not fingerprinted"}
        for label in ("current","old","torment_kernel","torment_checkout"):
            b,aft = before[label],after[label]
            def digest_map(item):
                return hashlib.sha256(json.dumps(item["files"],sort_keys=True,separators=(",",":")).encode()).hexdigest()
            check("INTEGRITY",f"{label}_fingerprint_unchanged",b["files"]==aft["files"] and b["tree_sha256"]==digest_map(b)==aft["tree_sha256"]==digest_map(aft))
            integrity["scopes"][label]={"root":b["root"],"before_count":b["count"],"after_count":aft["count"],"before_sha256":b["tree_sha256"],"after_sha256":aft["tree_sha256"],"before_start":b["start_utc"],"before_end":b["end_utc"],"after_start":aft["start_utc"],"after_end":aft["end_utc"],"changed_paths":sorted(k for k in set(b["files"])|set(aft["files"]) if b["files"].get(k)!=aft["files"].get(k))}
        for label,root,expected in [("current",REPO,BASELINE),("torment_checkout",PROD,PROD_HEAD)]:
            def git(*cmd):
                return subprocess.check_output(["git","--no-optional-locks","-C",str(root),*cmd],text=True).strip()
            head,status = git("rev-parse","HEAD"),git("status","--porcelain","--untracked-files=no")
            integrity["scopes"][label].update({"git_head_after":head,"git_tracked_status_after":status})
            check("INTEGRITY",f"{label}_HEAD_and_tracked_status",head==expected and status=="")

    result = {
        "atlas":"03","version":"0.1","generated_utc":datetime.now(timezone.utc).isoformat(),
        "python":platform.python_version(),"sympy":S.__version__,"interpreter":sys.executable,
        "frozen_baseline":BASELINE,"script_path":str(Path(__file__).resolve()),"script_sha256":sha(__file__),
        "summary":{"total":len(checks),"passed":sum(c["passed"] for c in checks),"failed":sum(not c["passed"] for c in checks),"by_group":{g:{"total":sum(c["group"]==g for c in checks),"passed":sum(c["group"]==g and c["passed"] for c in checks)} for g in sorted({c["group"] for c in checks})}},
        "checks":checks,"sources":source_hashes,"integrity":integrity,
        "mesh":{"vertices":[{"index":j,"xyz":wire(p),"material_aliases":aliases[j]} for j,p in enumerate(vertices)],"faces":faces,"edges":[{"edge":e,"incidence":inc[e]} for e in sorted(inc)],"seams":seams,"boundary_edges":boundary,"boundary_loops":[{"indices":loop,"coordinates":wire([vertices[j] for j in loop]),"length":wire(9*s)} for loop in loops],"vertex_links":links,"centres":wire(centres),"normals":wire(normals),"tangents":wire(tangents),"bounds":wire(bounds)},
        "symmetry":{"generators":generator_records,"elements":group,"surface_group":"D3h = D3 x Cs","upper_bound":"Analytic crease-component proof in packet; finite enumeration establishes a 12-element lower bound."},
        "metrics":wire({"s":s,"h":h,"d":d,"face_area":2*s,"material_area":6*s,"seam_total":3*s,"boundary_total":18*s,"rim_each":9*s,"triangle_enclosed_area":triangle_area,"section_curve_planar_area":S.Integer(0),"hexagon_virtual_area":hex_area,"notches":notch_records}),
        "scope_notes":["No mesh faces are added for virtual enclosed measurement regions.","Manifold classification, full symmetry upper bound, all-height sections and all-real closure family have analytic proofs in the packet; finite checks are not substitutes.","Source-boundary observations do not prove a physical law. No physical point attachment from Omega is specified by the reviewed geometry contract.","Commits and pushes performed by this work order: zero; the script performs neither."],
        "boundary_flags":["PAPER_C_GEOMETRY != OMEGA_DYNAMICS","NO_PHYSICAL_POINT_ATTACHMENT_FROM_OMEGA"],
    }
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(wire(result),indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(result["summary"],indent=2))
    print("OUTPUT",output)
    return 1 if result["summary"]["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
