"""Analytic construction diagrams for the Paper-D manuscript, not model code.

The accepted coordinate definitions are transcribed from derivation section 6.
SymPy holds coordinates exactly; conversion to floats occurs only for drawing.
"""
import runtime
import sympy as S
r2,r3=S.sqrt(2),S.sqrt(3)
U=[S.Matrix([1,0]),S.Matrix([-S.Rational(1,2),r3/2]),S.Matrix([-S.Rational(1,2),-r3/2])]
J=S.Matrix([[0,-1],[1,0]])
T=[J*u for u in U]
def metrics(s):
    s=S.sympify(s);a=(1+r2)*s/2
    return a,2*a,s/(2*S.sin(S.pi/8))
def octagon(s):
    s=S.sympify(s);a=metrics(s)[0];b=s/2
    return [S.Matrix(v) for v in [(a,-b),(a,b),(b,a),(-b,a),(-a,b),(-a,-b),(-b,-a),(b,-a)]]
def scaffold(s,gap):
    s,gap=map(S.sympify,(s,gap));p=(s+2*gap)/(2*r3)
    A=[p*U[i]-s*T[i]/2 for i in range(3)]
    B=[p*U[i]+s*T[i]/2 for i in range(3)]
    H=[v for pair in zip(A,B) for v in pair]
    V=[p*U[i]+r3*p*T[i] for i in range(3)]
    return {'s':s,'gap':gap,'p':p,'a':metrics(s)[0],'A':A,'B':B,'H':H,'V':V}
def planar_frames(s,gap):
    d=scaffold(s,gap)
    return [[(d['p']+d['a'])*U[i]+v[0]*U[i]+v[1]*T[i] for v in octagon(s)] for i in range(3)]
def vertical_frames(s,p):
    return [[S.Matrix([p*U[i][0]+v[0]*T[i][0],p*U[i][1]+v[0]*T[i][1],v[1]]) for v in octagon(s)] for i in range(3)]

