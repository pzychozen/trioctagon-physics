"""Exact C/D parity; finite geometry remains independent of Omega."""

from unittest.mock import patch
import sympy as sp

from kernel_physics import geometry as c, reference_scaffold as d, dynamics
from kernel_physics.tests.parity_oracles import geometry_oracle as o
from kernel_physics.tests.test_parity_oracle_boundaries import ParityCase


def canonical(point):
    return tuple(sp.simplify(v) for v in point)


class P11Tests(ParityCase):
    """PASS SUPPORTS: accepted exact C mesh, existing D3h generators, and D's
    closed sets, complete frames, role qualifications and two constructions.
    PASS DOES NOT SUPPORT: any Omega-to-geometry map or additional geometry.
    """

    def test_c_printed_coordinates_topology_and_indexing(self):
        mesh = c.folded_module()
        self.exact("P11","C printed 18-vertex table",mesh.vertices,o.C_VERTICES)
        self.discrete("P11","C oriented face cycles",mesh.faces,o.C_FACES)
        self.discrete("P11","C 21 edges",mesh.edges,o.C_EDGES)
        self.discrete("P11","C seams",mesh.seam_edges,o.C_SEAMS)
        self.discrete("P11","C two nine-edge boundary loops",mesh.boundary_loops,o.C_LOOPS)
        self.discrete("P11","C Euler and counts",(len(mesh.vertices),len(mesh.edges),len(mesh.faces),len(mesh.seam_edges),tuple(map(len,mesh.boundary_loops)),mesh.euler_characteristic),(18,21,3,3,(9,9),0))
        s = sp.sqrt(2)-1
        local = ((-o.H,-s/2),(-s/2,-o.H),(s/2,-o.H),(o.H,-s/2),(o.H,s/2),(s/2,o.H),(-s/2,o.H),(-o.H,s/2))
        for face_index,face in enumerate(o.C_FACES):
            panel_id = face_index+1
            for j,(u,z) in enumerate(local):
                self.exact("P11",f"C face_index={face_index} panel_id={panel_id} vertex={j}",c.panel_point(panel_id,u,z),o.C_VERTICES[face[j]])
            self.exact("P11",f"C outward normal {face_index}",mesh.face_normal(face_index),o.C_NORMALS[face_index])
        for first,second in ((0,1),(1,2),(2,0)):
            self.exact("P11",f"C dihedral {first,second}",[mesh.normal_separation(first,second),mesh.interior_dihedral(first,second)],[2*sp.pi/3,sp.pi/3])
        with self.assertRaises(ValueError):
            c.panel_point(0,0,0)
        with self.assertRaises(IndexError):
            mesh.face_normal(3)

    def test_c_section_curve_and_closed_domain(self):
        s = sp.sqrt(2)-1
        for height in (-s/2,0,s/4,s/2):
            corners = ((-o.H,0,height),(o.H,0,height),(0,sp.sqrt(3)/2,height))
            expected = tuple((corners[i],corners[(i+1)%3]) for i in range(3))
            actual = c.central_section(height)
            self.exact("P11",f"central section endpoints h={height}",[v for edge in actual for v in edge],[v for edge in expected for v in edge])
            self.discrete("P11",f"three segments h={height}",len(actual),3)
            centroid = sp.Matrix([0,sp.sqrt(3)/6,height])
            self.falsifier("P11",f"section is not filled cap h={height}",all((sp.Matrix(b)-sp.Matrix(a)).cross(centroid-sp.Matrix(a)) != sp.zeros(3,1) for a,b in actual))
        for height in (s,sp.I,sp.Symbol("h",real=True)):
            with self.assertRaises(ValueError):
                c.central_section(height)
        self.discrete("P11","section domain rejections",True,True)

    def test_existing_d3h_generators_and_twelve_actions(self):
        mesh = c.folded_module()
        generators = ((c.rotate_c3,o.C_ROTATE),(c.reflect_vertical,o.C_VERTICAL),(c.reflect_horizontal,o.C_HORIZONTAL))
        for fn,permutation in generators:
            for i,point in enumerate(mesh.vertices):
                self.exact("P11",f"{fn.__name__} vertex {i}",fn(point),o.C_VERTICES[permutation[i]])
        identity = tuple(range(18))
        lookup = {canonical(v):i for i,v in enumerate(o.C_VERTICES)}
        actions = set()
        for h in range(2):
            for v in range(2):
                for r in range(3):
                    points = mesh.vertices
                    for _ in range(r):
                        points = tuple(map(c.rotate_c3,points))
                    if v:
                        points = tuple(map(c.reflect_vertical,points))
                    if h:
                        points = tuple(map(c.reflect_horizontal,points))
                    permutation = tuple(lookup[canonical(point)] for point in points)
                    actions.add(permutation)
                    self.discrete("P11",f"D3h edge action {r,v,h}",set(tuple(sorted((permutation[a],permutation[b]))) for a,b in o.C_EDGES),set(o.C_EDGES))
                    self.discrete("P11",f"D3h face action {r,v,h}",set(frozenset(permutation[i] for i in face) for face in o.C_FACES),set(map(frozenset,o.C_FACES)))
        self.discrete("P11","twelve distinct existing-generator actions",len(actions),12)
        self.discrete("P11","identity action present",identity in actions,True)
        for i,p in enumerate(mesh.vertices):
            self.exact("P11",f"R cubed {i}",c.rotate_c3(c.rotate_c3(c.rotate_c3(p))),p)
            self.exact("P11",f"V squared {i}",c.reflect_vertical(c.reflect_vertical(p)),p)
            self.exact("P11",f"H squared {i}",c.reflect_horizontal(c.reflect_horizontal(p)),p)
            self.exact("P11",f"VRV=R inverse {i}",c.reflect_vertical(c.rotate_c3(c.reflect_vertical(p))),c.rotate_c3(c.rotate_c3(p)))
            self.exact("P11",f"HR=RH {i}",c.reflect_horizontal(c.rotate_c3(p)),c.rotate_c3(c.reflect_horizontal(p)))
            self.exact("P11",f"HV=VH {i}",c.reflect_horizontal(c.reflect_vertical(p)),c.reflect_vertical(c.reflect_horizontal(p)))

    def test_d_octagon_scaffold_area_and_radius(self):
        s,gap = sp.symbols("s gap",positive=True)
        model = d.ReferenceScaffold(s,gap)
        octagon = model.octagon
        self.exact("P11","D exact octagon vertices",octagon.vertices,o.octagon(s))
        self.exact("P11","D exact octagon metrics",[octagon.a,octagon.b,octagon.w,octagon.R_oct**2],[(1+sp.sqrt(2))*s/2,s/2,(1+sp.sqrt(2))*s,s*s/(4*sp.sin(sp.pi/8)**2)])
        for a,b in octagon.outline:
            self.exact("P11","D regular octagon edge metric",[sum((x-y)**2 for x,y in zip(a,b))],[s*s])
        self.exact("P11","D octagon filled generators",octagon.filled.vertices,o.octagon(s))
        vertices = o.scaffold(s,gap)
        self.exact("P11","D expanded Eq11 scaffold",model.vertices,vertices)
        self.exact("P11","D p L q_H",[model.p,model.L,model.q_H],[(s+2*gap)/(2*sp.sqrt(3)),(s+2*gap)/(2*sp.sqrt(3))+(1+sp.sqrt(2))*s/2,(2*s+gap)/(2*sp.sqrt(3))])
        shoelace = sum(vertices[i][0]*vertices[(i+1)%6][1]-vertices[(i+1)%6][0]*vertices[i][1] for i in range(6))/2
        self.exact("P11","D area independently from shoelace",[model.area],[shoelace])
        for i,point in enumerate(vertices):
            self.exact("P11",f"D circumradius vertex {i}",[model.circumradius_squared],[sum(v*v for v in point)])
            following = vertices[(i+1)%6]
            self.exact("P11",f"D alternating side length {i}",[sum((x-y)**2 for x,y in zip(point,following))],[(s if i%2 == 0 else gap)**2])
        self.discrete("P11","D E/G role sequence",model.edge_roles,("E","G")*3)
        self.exact("P11","D ordered selected edge endpoints",[v for edge in model.selected_edges for v in edge],vertices)
        self.exact("P11","D ordered connector endpoints",[v for edge in model.connectors for v in edge],[vertices[j] for i in range(3) for j in (2*i+1,(2*i+2)%6)])
        self.exact("P11","D from_radius parameter equivalence",d.ReferenceScaffold.from_radius(s,(s+2*gap)/(2*sp.sqrt(3))).vertices,vertices)
        for args in ((s,s/(2*sp.sqrt(3))),(s,s/(4*sp.sqrt(3)))):
            with self.assertRaises(ValueError):
                d.ReferenceScaffold.from_radius(*args)

    def test_d_closed_halfplanes_support_and_corner_cells(self):
        s,gap = sp.Integer(2),sp.Integer(1)
        model = d.ReferenceScaffold(s,gap)
        for i,(plane,(normal,offset)) in enumerate(zip(model.support_halfplanes+model.connector_halfplanes,o.halfplanes(s,gap))):
            self.exact("P11",f"D halfplane {i}",(*plane.normal,plane.offset),(*normal,offset))
        self.exact("P11","D support triangle printed intersections",model.support_triangle.vertices,o.support(s,gap))
        self.exact("P11","D support width",[model.W],[s+2*gap])
        vertices = o.scaffold(s,gap)
        apex = o.support(s,gap)
        for i,cell in enumerate(model.corner_cells):
            expected = (vertices[2*i+1],apex[i],vertices[(2*i+2)%6])
            self.exact("P11",f"D corner closed hull {i}",cell.vertices,expected)
            for j in range(3):
                self.exact("P11",f"D equilateral corner {i,j}",[sum((x-y)**2 for x,y in zip(expected[j],expected[(j+1)%3]))],[gap*gap])
            # Apex belongs to the closed corner boundary, so subtracting only
            # its open interior would leave this explicitly excluded point.
            self.discrete("P11",f"closed hexagon excludes corner apex {i}",model.filled_hexagon.contains(apex[i]),False)
            self.discrete("P11",f"closed hexagon retains connector midpoint {i}",model.filled_hexagon.contains(tuple((x+y)/2 for x,y in zip(expected[0],expected[2]))),True)
        for v in vertices:
            self.discrete("P11","closed hexagon includes every boundary vertex",model.filled_hexagon.contains(v),True)
        self.discrete("P11","closed hexagon interior origin",model.filled_hexagon.contains((0,0)),True)
        self.falsifier("P11","closed region differs from open-corner subtraction",not model.filled_hexagon.contains(apex[0]))

    def test_d_full_frames_regular_member_and_roles(self):
        s,gap = sp.Rational(3,2),sp.Rational(5,4)
        model = d.ReferenceScaffold(s,gap)
        for i in range(3):
            self.exact("P11",f"D complete planar frame {i}",model.planar_frames[i].vertices,[o.planar(i,x,y,s,gap) for x,y in o.octagon(s)])
            self.exact("P11",f"D complete vertical frame {i}",model.vertical_frames[i].vertices,[o.vertical(i,x,y,s,gap) for x,y in o.octagon(s)])
            self.exact("P11",f"D planar centre {i}",model.planar_centres[i],o.planar(i,0,0,s,gap))
            self.exact("P11",f"D vertical centre {i}",model.vertical_centres[i],o.vertical(i,0,0,s,gap))
            self.exact("P11",f"D reversed inward selected side {i}",[model.planar_frames[i].vertices[j] for j in (4,5)],[o.scaffold(s,gap)[2*i+1],o.scaffold(s,gap)[2*i]])
            self.exact("P11",f"D top selected side {i}",model.top_selected_edges[i],[o.vertical(i,xi,(1+sp.sqrt(2))*s/2,s,gap) for xi in (-s/2,s/2)])
        s = sp.Integer(2)
        regular = d.ReferenceScaffold.regular(s)
        self.exact("P11","D regular vertices",regular.vertices,[(s*sp.cos(-sp.pi/6+j*sp.pi/3),s*sp.sin(-sp.pi/6+j*sp.pi/3)) for j in range(6)])
        self.exact("P11","D regular area radius",[regular.area,regular.circumradius_squared],[3*sp.sqrt(3)*s*s/2,s*s])
        self.discrete("P11","regular predicate",regular.is_regular,True)
        # 60 degrees advances one vertex/edge and exchanges E/G. 120 advances
        # two and preserves classes. Reflection reverses traversal, preserves E/G.
        roles = regular.edge_roles
        r60 = sp.Matrix([[o.H,-sp.sqrt(3)/2],[sp.sqrt(3)/2,o.H]])
        reflect = sp.diag(1,-1)
        for i,point in enumerate(regular.vertices):
            self.exact("P11",f"regular hexagon actual 60-degree vertex action {i}",r60*sp.Matrix(point),regular.vertices[(i+1)%6])
            self.exact("P11",f"regular hexagon actual reflection action {i}",reflect*sp.Matrix(point),regular.vertices[(1-i)%6])
        for i,frame in enumerate(regular.planar_frames):
            self.exact("P11",f"full planar frame actual 120-degree action {i}",[tuple(r60*r60*sp.Matrix(p)) for p in frame.vertices],regular.planar_frames[(i+1)%3].vertices)
            reflected = set(canonical(reflect*sp.Matrix(p)) for p in frame.vertices)
            self.discrete("P11",f"full planar frame reflected set {i}",reflected,set(map(canonical,regular.planar_frames[(-i)%3].vertices)))
        self.falsifier("P11","unmarked D6 does not preserve E/G roles",all(roles[(i+1)%6] != roles[i] for i in range(6)))
        self.discrete("P11","120-degree role preservation",tuple(roles[(i+2)%6] for i in range(6)),roles)
        self.discrete("P11","reflection role preservation",tuple(roles[(-i)%6] for i in range(6)),roles)
        centres = set(map(canonical,regular.planar_centres))
        radius = regular.L
        self.falsifier("P11","complete frames do not acquire D6",canonical((radius/2,sp.sqrt(3)*radius/2)) not in centres)

    def test_d_paper_c_comparison_translation_and_shrink(self):
        s = sp.sqrt(2)-1
        source = d.paper_c_member(s)
        self.exact("P11","Paper C member radius and gap",[source.p,source.g_gap],[1/(2*sp.sqrt(3)),s/sp.sqrt(2)])
        for i,panel in enumerate((3,1,2)):
            mapped = [d.paper_c_rigid_map(p,s) for p in source.vertical_frames[i].vertices]
            expected = [o.paper_c_panel(panel,xi,z,s) for xi,z in o.octagon(s)]
            self.exact("P11",f"D to C finite frame {i} panel {panel}",mapped,expected)
            self.discrete("P11",f"D mapped finite face equals printed C panel {panel}",set(map(canonical,mapped)),set(canonical(o.C_VERTICES[j]) for j in o.C_FACES[panel-1]))
        translated = d.translate_paper_c_to_regular(s)
        shrunk = d.shrink_paper_c_at_fixed_centres(s)
        lam = (1+sp.sqrt(2))/3
        self.exact("P11","translation preserves side and top",[translated.s,translated.octagon.a],[s,sp.Rational(1,2)])
        self.exact("P11","translation radial increment",[translated.p-source.p],[(2-sp.sqrt(2))*s/(2*sp.sqrt(3))])
        self.exact("P11","shrink scale and radius",[shrunk.s,shrunk.g_gap,shrunk.p,shrunk.octagon.a],[sp.Rational(1,3),sp.Rational(1,3),source.p,lam/2])
        self.exact("P11","shrink fixed vertical centres",shrunk.vertical_centres,source.vertical_centres)
        self.exact("P11","width-one shrink metrics",[shrunk.W,shrunk.circumradius_squared,shrunk.area,shrunk.octagon.w],[1,sp.Rational(1,9),sp.sqrt(3)/6,lam])
        displacement = []
        for i in range(3):
            displacement.append(sp.Matrix(translated.vertical_centres[i])-sp.Matrix(source.vertical_centres[i]))
            centre = sp.Matrix(source.vertical_centres[i])
            for j,p in enumerate(source.vertical_frames[i].vertices):
                expected = centre+lam*(sp.Matrix(p)-centre)
                self.exact("P11",f"whole finite-face shrink about centre {i,j}",shrunk.vertical_frames[i].vertices[j],expected)
        self.falsifier("P11","translations are not one common rigid translation",displacement[0] != displacement[1])
        self.falsifier("P11","translation differs from fixed-centre shrink",sp.simplify(translated.s-shrunk.s) != 0 and canonical(shrunk.planar_centres[0]) != canonical(source.planar_centres[0]))

    def test_substitution_first_exact_domain_and_no_state_coupling(self):
        x = sp.Symbol("x",positive=True)
        length = 1/(1+sp.sqrt(x))
        # First operation on returned coordinates is substitution. Simplifying
        # differences beforehand could conceal a spurious removable pole at x=1.
        with patch.object(dynamics,"step3",side_effect=AssertionError("geometry advanced state")):
            for s,gap,side,g in ((length,length,o.H,o.H),(length,1,o.H,sp.Integer(1)),(1,length,sp.Integer(1),o.H)):
                model = d.ReferenceScaffold(s,gap)
                returned = [*model.vertices,*model.support_vertices]
                expected = [*o.scaffold(side,g),*o.support(side,g)]
                for i in range(3):
                    returned += list(model.planar_frames[i].vertices)+list(model.vertical_frames[i].vertices)
                    expected += [o.planar(i,u,v,side,g) for u,v in o.octagon(side)]+[o.vertical(i,u,v,side,g) for u,v in o.octagon(side)]
                for i,(point,target) in enumerate(zip(returned,expected,strict=True)):
                    specialized = [sp.sympify(v).subs(x,1) for v in point]
                    self.assertTrue(all(v.is_real is True and v.is_finite is True and not v.has(sp.Float,sp.nan,sp.zoo,sp.oo,-sp.oo) for v in specialized))
                    self.exact("P11",f"substitution-first s={s} gap={gap} point={i}",specialized,target)
        for bad in (.5,sp.Float(.5),1+sp.Float(.25)):
            with self.assertRaises(TypeError):
                d.ReferenceScaffold(bad,1)
        self.discrete("P11","no floats admitted by exact D constructor",True,True)
