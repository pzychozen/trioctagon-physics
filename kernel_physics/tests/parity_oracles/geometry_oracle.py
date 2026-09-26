"""Printed Paper C coordinate/face tables and Paper D (1)–(29), exactly.

C symmetry data are known vertex permutations, not a transform engine.
D scaffold coordinates use the expanded printed table, independently of the
runtime's radial/tangential construction. No floating input rationalization.
"""

from collections import Counter
import sympy as sp


H = sp.Rational(1,2)
R2,R3,R6 = sp.sqrt(2),sp.sqrt(3),sp.sqrt(6)
C_VERTICES = (
    (0,R3/2,(1-R2)/2),(-H+R2/4,R6/4,-H),(-R2/4,R3/2-R6/4,-H),
    (-H,0,(1-R2)/2),(-H,0,(-1+R2)/2),(-R2/4,R3/2-R6/4,H),
    (-H+R2/4,R6/4,H),(0,R3/2,(-1+R2)/2),((1-R2)/2,0,-H),
    ((-1+R2)/2,0,-H),(H,0,(1-R2)/2),(H,0,(-1+R2)/2),
    ((-1+R2)/2,0,H),((1-R2)/2,0,H),(R2/4,R3/2-R6/4,-H),
    (H-R2/4,R6/4,-H),(H-R2/4,R6/4,H),(R2/4,R3/2-R6/4,H),
)
C_FACES = ((0,1,2,3,4,5,6,7),(3,8,9,10,11,12,13,4),(10,14,15,0,7,16,17,11))
C_INCIDENCE = Counter(tuple(sorted((face[j],face[(j+1)%8]))) for face in C_FACES for j in range(8))
C_EDGES = tuple(sorted(C_INCIDENCE))
C_SEAMS = ((0,7),(3,4),(10,11))
C_LOOPS = ((0,1,2,3,8,9,10,14,15),(4,5,6,7,16,17,11,12,13))
C_NORMALS = ((-R3/2,H,0),(0,-1,0),(R3/2,H,0))
C_ROTATE = (3,8,9,10,11,12,13,4,14,15,0,7,16,17,1,2,5,6)
C_VERTICAL = (0,15,14,10,11,17,16,7,9,8,3,4,13,12,2,1,6,5)
C_HORIZONTAL = (7,6,5,4,3,2,1,0,13,12,11,10,9,8,17,16,15,14)


def octagon(s):
    s = sp.sympify(s)
    a,b = (1+R2)*s/2,s/2
    return ((a,-b),(a,b),(b,a),(-b,a),(-a,b),(-a,-b),(-b,-a),(b,-a))


def scaffold(s,gap):
    s,gap = map(sp.sympify,(s,gap))
    p = (s+2*gap)/(2*R3)
    return ((p,-s/2),(p,s/2),((s-gap)/(2*R3),(s+gap)/2),
            (-(2*s+gap)/(2*R3),gap/2),(-(2*s+gap)/(2*R3),-gap/2),
            ((s-gap)/(2*R3),-(s+gap)/2))


def support(s,gap):
    p = (sp.sympify(s)+2*sp.sympify(gap))/(2*R3)
    return ((p,R3*p),(-2*p,0),(p,-R3*p))


def halfplanes(s,gap):
    p = (s+2*gap)/(2*R3)
    q = (2*s+gap)/(2*R3)
    return (((1,0),p),((-H,R3/2),p),((-H,-R3/2),p),
            ((H,R3/2),q),((-1,0),q),((H,-R3/2),q))


def planar(i,x,y,s,gap):
    radius = (s+2*gap)/(2*R3)+(1+R2)*s/2
    return ((radius+x,y),(-(radius+x)/2-R3*y/2,R3*(radius+x)/2-y/2),
            (-(radius+x)/2+R3*y/2,-R3*(radius+x)/2-y/2))[i]


def vertical(i,xi,z,s,gap):
    p = (s+2*gap)/(2*R3)
    return ((p,xi,z),(-p/2-R3*xi/2,R3*p/2-xi/2,z),
            (-p/2+R3*xi/2,-R3*p/2-xi/2,z))[i]


def paper_c_panel(panel,xi,z,s):
    a = (1+R2)*s/2
    return ((-a/2-xi/2,R3*a/2-R3*xi/2,z),(xi,0,z),
            (a/2-xi/2,R3*a/2+R3*xi/2,z))[panel-1]
