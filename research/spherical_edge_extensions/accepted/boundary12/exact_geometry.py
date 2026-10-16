"""New BOUNDARY-12 constructions from accepted data; no old checker or scientific module imports."""
from pathlib import Path
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import combinations
import json,math,os,time
import sympy as S
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
O=Path(__file__).resolve().parent;D=json.loads((O/'incoming/reference/BOUNDARY11/data/geometry_inventory.json').read_text())
catalog=json.loads((O/'incoming/reference/BOUNDARY11/evidence/all_branch_coincidence_checks.json').read_text())
K=S.QQ.algebraic_field(S.sqrt(2),S.sqrt(3));zero=K.zero;one=K.one
def parse(s):return K.from_sympy(S.sympify(s))
def q(a,b=1):return K.from_sympy(S.Rational(a,b))
r2=parse('sqrt(2)');r3=parse('sqrt(3)');h=(r2-one)/2
@lru_cache(None)
def expr(x):return S.expand(K.to_sympy(x))
def st(x):return str(expr(x))
@lru_cache(None)
def sign(x):
 if x==zero:return 0
 e=expr(x);positive=e.is_positive;negative=e.is_negative
 assert positive is True or negative is True,('unresolved exact sign',str(e))
 return 1 if positive else -1
def num(x):return float(expr(x))
def vec(v):return tuple(parse(x) for x in v)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(s,v):return tuple(s*x for x in v)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),zero)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def zero_v(a):return all(x==zero for x in a)
def sv(v):return [st(x) for x in v]
def nv(v):return [num(x) for x in v]
def save(path,obj):
 p=O/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,indent=2)+'\n')
checks=[]
def check(label,b):assert b,label;checks.append(label)
edges={e['id']:{**e,'m':vec(e['midpoint_exact']),'u':vec(e['unit_direction_exact'])} for e in D['edges']}
events={name:{'name':name,'t':parse(old['t_over_w_exact']),'R2':parse(old['R_squared_over_w_squared']),'old':old} for name,old in zip(['original','A','B'],D['coincidence_events'])}

# Consume the already accepted exhaustive incidence result, without solving those pairs again.
accepted_roots={parse(row['tau']) for row in catalog if row['tau'] is not None and row['branch_a'][:3]!=row['branch_b'][:3]}
check('accepted nonzero root magnitudes are just the three event parameters',
 {x*x for x in accepted_roots}=={parse(e['old']['tau_exact'])**2 for e in events.values()})
branch_events=defaultdict(list)
for name,event in events.items():
 for gi,oldgroup in enumerate(event['old']['groups'],1):
  for branch in oldgroup['branches']:branch_events[branch].append({'event':name,'outer_dot_id':f'{name}:P{gi:02d}','incident_branches':oldgroup['branches'],'coordinates_exact':oldgroup['coordinates_exact']})
check('every branch participates in every event',len(branch_events)==42 and all([r['event'] for r in x]==['original','A','B'] for x in branch_events.values()))
termination=[]
for branch,rows in sorted(branch_events.items()):
 e=edges[branch[:3]];sg=1 if branch[-1]=='+' else -1
 termination.append({'branch':branch,'edge':e['id'],'original_endpoint_vertex':e['vertices'][1 if sg==1 else 0],
 'ray_formula':'original endpoint + extension * outward unit direction; extension > 0',
 'outward_unit_direction_exact':sv(mul(q(sg),e['u'])),
 'original':rows[0],'first_new_meeting':rows[1],'last_finite_meeting':rows[2],
 'first_extension_over_w':st(events['A']['t']-h),'last_extension_over_w':st(events['B']['t']-h)})
lengths=[{'event':n,'t_over_w':st(e['t']),'C_over_w':st(2*e['t']),'ell_over_w':st(e['t']-h),'total_added_over_w':st(2*(e['t']-h)),'R2_over_w2':st(e['R2'])} for n,e in events.items()]
check('A whole chord equals w',2*events['A']['t']==one)
check('A cutback equals s/sqrt2',events['A']['t']-h==(r2-one)/r2)
check('B per-end extension equals w',events['B']['t']-h==one)
check('three-term octagonal ratio',events['A']['t']/h==events['B']['t']/events['A']['t']==one+r2)
save('data/terminations_and_lengths.json',{'normalization':'w=1; all distances scale by w','length_table':lengths,'rays':termination,'classification_source':'accepted BOUNDARY11 catalogue; no old pair solver rerun'})

def hull(name,pts,source_vertices):
 # All triples nominate planes. Every sign, equality, containment and face turn is certified exactly.
 seen=set();faces=[];rejected=0;collinear=0
 for i,j,k in combinations(range(len(pts)),3):
  n=cross(sub(pts[j],pts[i]),sub(pts[k],pts[i]))
  if zero_v(n):collinear+=1;continue
  d=dot(n,pts[i]);pivot=next(x for x in n if x!=zero);key=(*mul(one/pivot,n),d/pivot)
  if key in seen:continue
  seen.add(key);n=key[:3];d=key[3]
  residual=[dot(n,x)-d for x in pts];ss={sign(x) for x in residual}
  if -1 in ss and 1 in ss:rejected+=1;continue
  if 1 in ss:n=mul(-one,n);d=-d;residual=[-x for x in residual]
  check(f'{name} outward support {len(faces)}',sign(d)>0 and all(sign(x)<=0 for x in residual))
  ids=[i for i,x in enumerate(residual) if x==zero]
  center=mul(q(1,len(ids)),tuple(sum((pts[i][j] for i in ids),zero) for j in range(3)))
  b=sub(pts[ids[0]],center);c=cross(n,b)
  order=sorted(ids,key=lambda i:math.atan2(num(dot(sub(pts[i],center),c))/math.sqrt(num(dot(c,c))),num(dot(sub(pts[i],center),b))/math.sqrt(num(dot(b,b)))))
  check(f'{name} oriented convex face {len(faces)}',all(sign(dot(cross(sub(pts[order[(j+1)%len(order)]],pts[order[j]]),sub(pts[k],pts[order[j]])),n))>=0 for j in range(len(order)) for k in order))
  sides=[sub(pts[order[(j+1)%len(order)]],pts[order[j]]) for j in range(len(order))]
  lens=[dot(x,x) for x in sides];turns=[dot(sides[j-1],sides[j]) for j in range(len(sides))]
  regular=len(set(lens))==1 and len(set(turns))==1
  kind=f'{len(order)}-gon'+(' regular' if regular else ' nonregular')
  if len(order)==3 and not regular:kind='isosceles triangle' if len(set(lens))==2 else 'scalene triangle'
  if len(order)==4:
   if all(x==zero for x in turns):kind='square' if len(set(lens))==1 else 'rectangle'
   elif len(set(lens))==1:kind='rhombus'
  faces.append({'id':f'F{len(faces)+1:02d}','vertices':order,'normal_exact':sv(n),'offset_exact':st(d),'inequality':'normal dot x <= offset','normal':nv(n),'offset':num(d),
   'side_squared_exact':[st(x) for x in lens],'turn_dot_exact':[st(x) for x in turns],'type':kind,'regular':regular,
   'all_outer_point_residuals_exact':[st(x) for x in residual],
   '_n':n,'_d':d})
 edgefaces=defaultdict(list)
 for f in faces:
  cyc=f['vertices']
  for a,b in zip(cyc,cyc[1:]+cyc[:1]):edgefaces[tuple(sorted((a,b)))].append(f['id'])
 check(f'{name} closed manifold edges',all(len(x)==2 for x in edgefaces.values()))
 check(f'{name} Euler',len(pts)-len(edgefaces)+len(faces)==2)
 check(f'{name} all 18 points extreme vertices',set(i for pair in edgefaces for i in pair)==set(range(18)))
 # Vertex link is a connected cycle, independent of Euler's necessary condition.
 for v in range(len(pts)):
  link=defaultdict(set)
  for f in faces:
   if v in f['vertices']:
    cyc=f['vertices'];j=cyc.index(v);a,b=cyc[j-1],cyc[(j+1)%len(cyc)];link[a].add(b);link[b].add(a)
  todo=[next(iter(link))];visited=set()
  while todo:
   u=todo.pop()
   if u not in visited:visited.add(u);todo.extend(link[u]-visited)
  check(f'{name} vertex link {v}',len(visited)==len(link) and all(len(s)==2 for s in link.values()))
 check(f'{name} all original panels contained',all(sign(dot(f['_n'],v)-f['_d'])<=0 for f in faces for v in source_vertices))
 return {'event':name,'V':len(pts),'E':len(edgefaces),'F':len(faces),'euler':2,'face_types':dict(Counter(f['type'] for f in faces)),
  'vertices':[{'id':i,'outer_dot_id':f'{name}:P{i+1:02d}','exact':sv(v),'xyz':nv(v)} for i,v in enumerate(pts)],
  'faces':faces,'edges':[{'vertices':list(e),'faces':fs} for e,fs in sorted(edgefaces.items())],
  'enumeration':{'triples':816,'distinct_noncollinear_planes':len(seen),'collinear_triples':collinear,'rejected_planes':rejected},
  'symmetry':'exactly D3h: every sphere point is extreme, so hull symmetries equal the accepted vertex-set symmetries'}

source_vertices=[vec(v['centered_exact']) for v in D['vertices']]
summaries=[];allprior=[]
for name,event in events.items():
 outer=[vec(g['coordinates_exact']) for g in event['old']['groups']]
 H=hull(name,outer,source_vertices)
 allprior.append(name);pts=[];vrecords=[];pointidx={}
 for earlier in allprior:
  for gi,g in enumerate(events[earlier]['old']['groups'],1):
   v=vec(g['coordinates_exact']);check('distinct event graph point',v not in pointidx);pointidx[v]=len(pts);pts.append(v)
   vrecords.append({'id':len(pts)-1,'event':earlier,'dot_id':f'{earlier}:P{gi:02d}','exact':sv(v),'xyz':nv(v),'branch_labels':g['branches']})
 gedges=[];adj=defaultdict(set)
 for eid,e in edges.items():
  on=[]
  for i,v in enumerate(pts):
   if zero_v(cross(sub(v,e['m']),e['u'])):on.append((dot(sub(v,e['m']),e['u']),i))
  on.sort(key=lambda p:num(p[0]))
  check(f'{name} exact line order {eid}',all(sign(y[0]-x[0])>0 for x,y in zip(on,on[1:])))
  check(f'{name} line clipped endpoints {eid}',on[0][0]==-event['t'] and on[-1][0]==event['t'])
  for (ta,i),(tb,j) in zip(on,on[1:]):
   active=[f['id'] for f in H['faces'] if dot(f['_n'],pts[i])==f['_d'] and dot(f['_n'],pts[j])==f['_d']]
   locus='hull_edge' if len(active)>=2 else 'face_interior' if len(active)==1 else 'hull_interior'
   segment_kind='original' if ta==-h and tb==h else 'added'
   ray=None if segment_kind=='original' else eid+('+' if sign(ta)>=0 else '-')
   gedges.append({'id':f'G{len(gedges)+1:03d}','vertices':[i,j],'source_edge':eid,'source_ray':ray,'source_class':e['class'],'t_interval_exact':[st(ta),st(tb)],'length_exact':st(tb-ta),'segment_kind':segment_kind,'relative_open_segment_locus':locus,'support_faces':active})
   adj[i].add(j);adj[j].add(i)
 check(name+' geometric edge dedup',len({tuple(sorted(e['vertices'])) for e in gedges})==len(gedges))
 check(name+' graph contained in hull',all(sign(dot(f['_n'],v)-f['_d'])<=0 for f in H['faces'] for v in pts))
 # The finite exact planes make endpoint-sign tests sufficient for the whole straight interval.
 remaining=set(range(len(pts)));components=[]
 while remaining:
  todo=[next(iter(remaining))];comp=set()
  while todo:
   x=todo.pop()
   if x not in comp:comp.add(x);todo.extend(adj[x]-comp)
  components.append(sorted(comp));remaining-=comp
 for v in vrecords:v['adjacency']=sorted(adj[v['id']]);v['degree']=len(adj[v['id']])
 graph={'event':name,'V':len(pts),'E':len(gedges),'components':components,'component_count':len(components),'cycle_rank':len(gedges)-len(pts)+len(components),'degree_counts':dict(Counter(v['degree'] for v in vrecords)),'segment_locus_counts':dict(Counter(e['relative_open_segment_locus'] for e in gedges)),'vertices':vrecords,'edges':gedges,
  'spatial_intersections':'Union of accepted event incidence groups at or inside radius; no projected crossings inserted','boundary_classification':'Relative interior of each split graph edge; isolated boundary endpoints are retained in vertices'}
 check(name+' connected',len(components)==1)
 for f in H['faces']:del f['_n'];del f['_d']
 save(f'data/graph_{name}.json',graph);save(f'data/hull_{name}.json',H)
 summary={'event':name,'graph':{k:graph[k] for k in ['V','E','component_count','cycle_rank','degree_counts','segment_locus_counts']},'hull':{k:H[k] for k in ['V','E','F','face_types']}}
 summaries.append(summary);print(json.dumps(summary),flush=True)
save('data/geometry_summary.json',summaries)
save('evidence/NEW_EXACT_GEOMETRY_CHECKS.json',{'pass':True,'checks_passed':len(checks),'checks':checks,'arithmetic':'QQ(sqrt(2),sqrt(3)); exact algebraic sign certification','scope':'Three new graph/hull constructions; accepted coincidence classification reused, not rerun','hull_ordering':'Float atan2 nominates vertex order only; all supporting signs and oriented convex turns checked exactly'})
