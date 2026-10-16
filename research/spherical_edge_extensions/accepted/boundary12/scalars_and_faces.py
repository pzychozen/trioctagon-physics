from pathlib import Path
from collections import Counter
from itertools import product
import json,os,datetime
import sympy as S
import mpmath as mp
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
O=Path(__file__).resolve().parent;mp.mp.dps=70
def c(x):return S.expand(S.radsimp(x))
def key(v):return tuple(c(x) for x in v)
def save(p,x):(O/p).write_text(json.dumps(x,indent=2)+'\n')
rt2,rt3=S.sqrt(2),S.sqrt(3);q=S.Rational
rot=S.Matrix([[-q(1,2),-rt3/2,0],[rt3/2,-q(1,2),0],[0,0,1]])
group=[rot**k*S.diag(-1,1,1)**j*S.diag(1,1,-1)**i for k,j,i in product(range(3),range(2),range(2))]
orbit_summary=[]
for name in ['original','A','B']:
 H=json.loads((O/f'data/hull_{name}.json').read_text());V=[S.Matrix(list(map(S.sympify,v['exact']))) for v in H['vertices']]
 index={key(v):i for i,v in enumerate(V)}
 maps=[[index[key(g*v)] for v in V] for g in group]
 faces={frozenset(f['vertices']):f for f in H['faces']}
 for f in H['faces']:
  if f['type']=='4-gon nonregular':
   vs=[V[i] for i in f['vertices']];sides=[vs[(j+1)%4]-vs[j] for j in range(4)];lens=list(map(S.sympify,f['side_squared_exact']))
   parallel=[j for j in [0,1] if all(c(x)==0 for x in sides[j].cross(sides[j+2]))]
   if len(parallel)==1:
    j=parallel[0];assert c(lens[(j+1)%4]-lens[(j+3)%4])==0
    f['type']='isosceles trapezoid';f['parallel_opposite_side_indices']=[j,j+2]
 remaining=set(faces);orbits=[]
 while remaining:
  face=min(remaining,key=lambda k:faces[k]['id']);orb={frozenset(pm[i] for i in face) for pm in maps}
  assert orb<=remaining
  rep=faces[face];orbits.append({'size':len(orb),'face_ids':sorted(faces[x]['id'] for x in orb),'representative':{k:rep[k] for k in ['id','type','vertices','normal_exact','offset_exact','side_squared_exact','turn_dot_exact']}})
  remaining-=orb
 H['face_types']=dict(Counter(f['type'] for f in H['faces']));H['D3h_face_orbits']=orbits
 save(f'data/hull_{name}.json',H);orbit_summary.append({'event':name,'face_orbits':orbits})
 save(f'evidence/FACE_ORBITS_{name}.json',{'all_group_permutations':maps,'all_facets_preserved':True,'orbits':orbits})
summary=json.loads((O/'data/geometry_summary.json').read_text())
for row in summary:row['hull']['face_types']=json.loads((O/f'data/hull_{row["event"]}.json').read_text())['face_types']
save('data/geometry_summary.json',summary);save('data/hull_face_orbits.json',orbit_summary)

phi=(1+mp.sqrt(5))/2;T=mp.pi*mp.e*phi;gam=mp.zeta(3)/T;L=mp.log(phi)
I2=mp.quad(lambda x: x*x/mp.tanh(x) if x else mp.mpf(0),[0,L])
assert abs(I2-mp.zeta(3)/10)<mp.mpf('1e-68')
assert abs(T/10-I2/gam)<mp.mpf('1e-68')
rho=S.sqrt(q(13,12)-rt2/2);A=S.sqrt(q(7,12));B=S.sqrt(q(13,12)+rt2/2)
fixed=[('original',rho,'original'),('A',A,'A'),('B',B,'B'),('R_equals_w',S.Integer(1),None),('t_equals_w',2/rt3,None),('assigned_R10',S.Integer(10),None),('assigned_RT',S.pi*S.E*(1+S.sqrt(5))/2,None)]
h=(rt2-1)/2;presets=[]
D=json.loads((O/'incoming/reference/BOUNDARY11/data/geometry_inventory.json').read_text())
for name,R,event in fixed:
 t=S.simplify(S.sqrt(R**2-q(1,3)));C=2*t;ell=S.simplify(t-h)
 fm=lambda x:float(x.evalf(50))
 rn,tn=fm(R),fm(t)
 points=[]
 for e in D['edges']:
  m=list(map(S.sympify,e['midpoint_exact']));u=list(map(S.sympify,e['unit_direction_exact']))
  for sg in [-1,1]:points.append({'branch':e['id']+('+' if sg>0 else '-'),'xyz':[fm(m[j]+sg*t*u[j]) for j in range(3)]})
 presets.append({'id':name,'exact_event':event,'kind':'exact event' if event else 'assigned comparison','exact':{'R_over_w':str(R),'t_over_w':str(t),'C_over_w':str(C),'ell_over_w':str(ell)},'numeric':{'R_over_w':rn,'t_over_w':tn,'C_over_w':fm(C),'ell_over_w':fm(ell)},'unique_point_count':18 if event else 42,'points':points})
comparisons=[]
for label,ratio in [('R_A/rho',A/rho),('R_B/R_A',B/A),('R_B/rho',B/rho),('t1/t0=t2/t1',1+rt2)]:
 val=mp.mpf(str(ratio.evalf(72)));delta=val-T/10
 comparisons.append({'ratio':label,'exact':str(S.simplify(ratio)),'value':mp.nstr(val,50),'T_over_10':mp.nstr(T/10,50),'signed_difference_ratio_minus_T10':mp.nstr(delta,50),'relative_difference_over_T10':mp.nstr(delta/(T/10),40)})
save('data/fixed_presets.json',presets)
save('data/scalar_comparisons.json',{'precision_decimal_digits':70,'T':mp.nstr(T,65),'gamma_star':mp.nstr(gam,65),'I2':mp.nstr(I2,65),'I2_minus_zeta3_over_10':mp.nstr(I2-mp.zeta(3)/10,12),'T10_minus_I2_over_gamma_star':mp.nstr(T/10-I2/gam,12),'ratios':comparisons,'conditional_linear_ratios_for_same_positive_measure':{'length':mp.nstr(T/10,40),'area':mp.nstr(mp.sqrt(T/10),40),'volume':mp.nstr((T/10)**(mp.mpf(1)/3),40)},'scope':'Fixed scalar comparisons only; no fitting, constants aggregation or dynamical claim'})
print(json.dumps({'face_orbits':[{ 'event':r['event'],'orbits':[(v['size'],v['representative']['type'],v['representative']['normal_exact'],v['representative']['offset_exact']) for v in r['face_orbits']]} for r in orbit_summary],'ratios':comparisons},indent=2))
