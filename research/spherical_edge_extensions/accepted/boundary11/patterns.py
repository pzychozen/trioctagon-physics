"""Additional exact orbit and naturally defined polygon checks, isolated from project code."""
from pathlib import Path
import json,os
from collections import defaultdict
import sympy as S
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
O=Path(__file__).resolve().parent;d=json.loads((O/'data/geometry_inventory.json').read_text())
rt2,rt3=S.sqrt(2),S.sqrt(3);Q=S.Rational
def c(x):return S.expand(S.radsimp(S.sympify(x)))
def key(v):return tuple(c(x) for x in v)
rot=S.Matrix([[-Q(1,2),-rt3/2,0],[rt3/2,-Q(1,2),0],[0,0,1]])
sv=S.diag(-1,1,1);sh=S.diag(1,1,-1)
group=[rot**k*sv**j*sh**i for k in range(3) for j in range(2) for i in range(2)]
def orbits(points):
    remaining=set(map(key,points));result=[]
    while remaining:
        p=S.Matrix(next(iter(remaining)));orb={key(G*p) for G in group}
        assert orb<=remaining
        result.append(len(orb));remaining-=orb
    return sorted(result)
event_orbits=[]
for event in d['coincidence_events']:
    pts=[S.Matrix([S.sympify(x) for x in p['coordinates_exact']]) for p in event['groups']]
    event_orbits.append({'R_squared':event['R_squared_over_w_squared'],'orbit_sizes':orbits(pts)})
normals=[rot**k*S.Matrix([0,-1,0]) for k in range(3)]
tangents=[rot**k*S.Matrix([1,0,0]) for k in range(3)]
p=rt3/6
t=S.Symbol('t',real=True)
branches=[S.Matrix([S.sympify(x) for x in e['midpoint_exact']])+sg*t*S.Matrix([S.sympify(x) for x in e['unit_direction_exact']]) for e in d['edges'] for sg in [-1,1]]
generic_orbits=orbits(branches)
assert generic_orbits==[6,12,12,12]
closed=[]
for k in range(3):
    for sg in [-1,1]:closed.append(rot**k*S.Matrix([0,rt3/3,sg*t]))
    n,b=normals[k],tangents[k]
    for eps in [-1,1]:
        for nu in [-1,1]:
            closed.append(p*n+eps*t*b+S.Matrix([0,0,nu*Q(1,2)]))
            for sigma in [-1,1]:closed.append(p*n+sigma*(Q(1,2)+eps*t)/rt2*b+S.Matrix([0,0,nu*(Q(1,2)-eps*t)/rt2]))
assert set(map(key,closed))==set(map(key,branches))
directions={key(sg*S.Matrix([S.sympify(x) for x in e['unit_direction_exact']])) for e in d['edges'] for sg in [-1,1]}
assert len(directions)==20
rot60=S.Matrix([[Q(1,2),-rt3/2,0],[rt3/2,Q(1,2),0],[0,0,1]])
for G in [rot60,sv,sh]:assert {key(G*S.Matrix(v)) for v in directions}==directions
moment=sum((S.Matrix(v)*S.Matrix(v).T for v in directions),S.zeros(3,3)).applyfunc(c)
assert moment==S.diag(6,6,8)
for event in d['coincidence_events']:
    diag=list(map(S.sympify,event['unique_second_moment_diagonal']))
    assert c(diag[2]-diag[0])==Q(3,2)
hex_events=[]
for sign in [-1,1]:
    t=Q(1,2)+sign*rt2/6;z=c((Q(1,2)+t)/rt2);u=c((Q(1,2)-t)/rt2)
    pts=[p*n+sg*u*b+S.Matrix([0,0,z]) for n,b in zip(normals,tangents) for sg in [-1,1]]
    unique=set(map(key,pts));assert len(unique)==6
    for v in pts:
        dist=sorted([c((v-w).dot(v-w)) for w in pts],key=float)
        assert dist==[0,Q(1,9),Q(1,9),Q(1,3),Q(1,3),Q(4,9)]
    hex_events.append({'t_over_w':str(t),'R_squared_over_w_squared':str(c(Q(1,3)+t*t)),
                       'R_over_w':float(S.sqrt(Q(1,3)+t*t)),'latitude_height_over_w':str(z),
                       'ring_circumradius_over_w':'1/3','unique_points_on_each_hexagon':6})
panel16=[]
for numerator in [3,5,7]:
    beta=numerator*S.pi/16
    R2=Q(1,12)+1/(4*S.cos(beta)**2)
    # Angles are multiples of pi/16; verify the two eight-point grids interleave every 2 steps.
    grid={(4*k+sg*numerator)%32 for k in range(8) for sg in [-1,1]}
    assert len(grid)==16 and grid==set(range(1,32,2))
    panel16.append({'beta':str(beta),'R_squared_over_w_squared':str(R2),'R_over_w':float(S.sqrt(R2)),
                    'per_panel_regular_polygon_vertices':16})
result={'special_point_set_D3h_orbits':event_orbits,'regular_latitude_hexagons':hex_events,
        'regular_panel_16_gons':panel16,'generic_labelled_point_orbits':generic_orbits,
        'compressed_coordinate_formula_matches_all_42_symbolic_branches':True,
        'exact_direction_D6h_generators_verified':True,
        'limit_direction_second_moment_diagonal':[6,6,8],
        'limiting_normalized_directions':{'count':20,'poles':2,'equator':6,'latitude_plus45':6,'latitude_minus45':6,
             'symmetry':'D6h; a limit only, not finite-R symmetry'},
        'scope':'Natural latitude rings and complete panel-circle point sets; no claim classifying arbitrary selected subsets.'}
(O/'data/polygon_patterns.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
