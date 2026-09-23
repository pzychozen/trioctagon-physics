"""Printed equations (1)-(5); exact comparison with the preserved geometry."""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
from publication_runtime import bootstrap_python
bootstrap_python()
import sympy as s
ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
sys.path.insert(0, str(REPO))
from kernel_physics import geometry
assert Path(geometry.__file__).resolve().is_relative_to(REPO), "Geometry escaped the declared checkout."
M = s.Matrix
ez = M([0, 0, 1])
side = s.sqrt(2)-1
local = [(-s.Rational(1,2),-side/2),(-side/2,-s.Rational(1,2)),
         (side/2,-s.Rational(1,2)),(s.Rational(1,2),-side/2),
         (s.Rational(1,2),side/2),(side/2,s.Rational(1,2)),
         (-side/2,s.Rational(1,2)),(-s.Rational(1,2),side/2)]
centres = [M([-s.Rational(1,4),s.sqrt(3)/4,0]), M([0,0,0]),
           M([s.Rational(1,4),s.sqrt(3)/4,0])]
normals = [M([-s.sqrt(3)/2,s.Rational(1,2),0]),M([0,-1,0]),
           M([s.sqrt(3)/2,s.Rational(1,2),0])]
tangents = [ez.cross(n) for n in normals]
R = M([[-s.Rational(1,2),-s.sqrt(3)/2,0],
       [s.sqrt(3)/2,-s.Rational(1,2),0],[0,0,1]])
P = M([[0,0,1],[1,0,0],[0,1,0]])
H = s.diag(1,1,-1)
V = s.diag(-1,1,1)
S = M([[0,0,1],[0,1,0],[1,0,0]])
origin = M([0,s.sqrt(3)/6,0])
polygons = [[c+u*t+z*ez for u,z in local] for c,t in zip(centres,tangents)]
def zero(x):
    return all(s.simplify(y)==0 for y in x) if isinstance(x,s.MatrixBase) else s.simplify(x)==0
def compare_source():
    mesh = geometry.folded_module()
    assert len(mesh.vertices)==18 and len(mesh.faces)==3
    for i,face in enumerate(mesh.faces):
        assert zero(normals[i]-M(mesh.face_normal(i)))
        for expected,index in zip(polygons[i],face):
            assert zero(expected-M(mesh.vertices[index]))
        for u,z in local:
            assert zero(centres[i]+u*tangents[i]+z*ez-M(geometry.panel_point(i+1,u,z)))
    return {"source":"kernel_physics/geometry.py","exact_vertex_comparisons":24,
            "exact_panel_map_comparisons":24,"exact_normal_comparisons":3,"matched":True}
def transport(i,j):
    return tangents[i]*tangents[j].T+ez*ez.T
