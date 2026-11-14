"""Reviewer certificate check without importing the submitted arithmetic/geometry/checker.
Uses SymPy algebraic-field polynomials and exact Bernstein sign certificates rather
than the submission's Fraction quadratic engine and Sturm root counts. No new hull
nomination or old scientific suite is executed.
"""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from math import isqrt,comb
from collections import Counter,defaultdict
from datetime import datetime,timezone
import hashlib,json,time
import sympy as sp
from sympy.polys.rings import ring
ROOT=Path(__file__).resolve().parents[1]; SUB=ROOT/'submitted'; OUT=ROOT/'reviewer'
K=sp.QQ.algebraic_field(sp.sqrt(2)); P,x=ring('x',K); rt=K.unit; zero=K.zero; one=K.one
start=time.monotonic()
def q(s):return K.from_sympy(sp.Rational(str(s)))
def field(row):return q(row[0])+q(row[1])*rt
def loadp(rows):return P.from_dict({(i,):field(v) for i,v in enumerate(rows) if field(v)})
def enc(v):
 a=v.to_list();a=[sp.QQ.zero]*(2-len(a))+a
 return [str(a[1]),str(a[0])]
def pencode(v):
 if not v:return []
 return [enc(v.get((i,),zero)) for i in range(v.degree()+1)]
@lru_cache(maxsize=100000)
def sgn(v):
 if not v:return 0
 a=v.to_list();a=[sp.QQ.zero]*(2-len(a))+a
 b=Fraction(a[0].numerator,a[0].denominator);c=Fraction(a[1].numerator,a[1].denominator)
 for bits in [64,128,256,512,1024,2048,4096]:
  den=1<<bits; num=isqrt(2*den*den);lo=Fraction(num,den);hi=Fraction(num+1,den)
  left=c+b*(lo if b>=0 else hi);right=c+b*(hi if b>=0 else lo)
  if left>0:return 1
  if right<0:return -1
 raise AssertionError('Nonzero algebraic coefficient sign unresolved')
def dot(a,b):return sum((u*v for u,v in zip(a,b)),P.zero)
def sub(a,b):return tuple(u-v for u,v in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def at(p,t):return p.evaluate(x,t)
def pointat(v,t):return tuple(P(at(p,t)) for p in v)
def plane(points,cyc):
 a,b,c=[points[k] for k in cyc[:3]];n=cross(sub(b,a),sub(c,a));return n,dot(n,a)
# A different exact positivity certificate: power-to-Bernstein on the interval.
# Every Bernstein basis function is positive in its open interval. All nonnegative
# coefficients with at least one positive coefficient imply strict positivity.
# At subdividing boundaries strict positive point values are checked separately.
def bernstein_positive(p,lo,hi,depth=0):
 assert sgn(hi-lo)>0 and p
 r=p.compose(x,P(lo)+(hi-lo)*x); n=r.degree()
 bs=[sum((r.get((j,),zero)*q(Fraction(comb(k,j),comb(n,j))) for j in range(k+1)),zero) for k in range(n+1)]
 signs=[sgn(v) for v in bs]
 if min(signs)>=0 and max(signs)>0:
  return [{'lower':enc(lo),'upper':enc(hi),'bernstein_coefficients':[enc(v) for v in bs]}]
 assert depth<12, 'Bernstein proof incomplete within reviewer subdivision bound'
 mid=(lo+hi)/q(2); assert sgn(at(p,mid))==1,'Interior nonpositive witness'
 return bernstein_positive(p,lo,mid,depth+1)+bernstein_positive(p,mid,hi,depth+1)
cache={};sign_records=[]
def require_sign(p,expected,kind,lo,hi):
 if not p:
  assert expected==0;return
 assert expected!=0
 # Normalize by a positive algebraic scalar to reuse proofs across equivalent planes.
 lead=p.LC;norm=p.mul_ground(one/(lead if sgn(lead)>0 else -lead))
 key=(tuple(norm.terms()),expected,kind,lo,hi)
 if key in cache:return
 if kind=='point':
  assert sgn(at(norm,lo))==expected
  rec={'kind':'point','polynomial':pencode(norm),'expected_sign':expected,'parameter':enc(lo),'evaluated':enc(at(norm,lo))}
 else:
  leaves=bernstein_positive(norm.mul_ground(q(expected)),lo,hi)
  rec={'kind':'open','polynomial':pencode(norm),'expected_sign':expected,'lower':enc(lo),'upper':enc(hi),'positive_bernstein_subintervals':leaves}
 sign_records.append(rec);cache[key]=True
h=(rt-one)/q(2); half=q('1/2');A=half;T=q(3)*h;B=(one+rt)/q(2)
local=[(-half,-h),(-h,-half),(h,-half),(half,-h),(half,h),(h,half),(-h,half),(-half,h)]
verts=[];cycles=[]
for panel in range(3):
 cyc=[]
 for u,z in local:
  # Centred Paper C fold, with Y = physical_y/sqrt(3).
  v=((-q('1/4')-u/q(2),q('1/12')-u/q(2),z) if panel==0 else ((u,-q('1/6'),z) if panel==1 else (q('1/4')-u/q(2),q('1/12')+u/q(2),z)))
  if v not in verts:verts.append(v)
  cyc.append(verts.index(v))
 cycles.append(cyc)
edges=sorted({tuple(sorted([cyc[i],cyc[(i+1)%8]])) for cyc in cycles for i in range(8)})
assert len(verts)==18 and len(edges)==21
points={}
for i,(j,k) in enumerate(edges,1):
 m=tuple((a+b)/q(2) for a,b in zip(verts[j],verts[k]));d=tuple((b-a)/(q(2)*h) for a,b in zip(verts[j],verts[k]))
 for suffix,sign in [('+',1),('-',-1)]:points[f'E{i:02}'+suffix]=tuple(P(a)+q(sign)*b*x for a,b in zip(m,d))
raw=(SUB/'data/exact_certificate.json').read_bytes();c=json.loads(raw)
assert points=={k:tuple(loadp(a) for a in v) for k,v in c['points'].items()}
for p in points.values():assert p[0]**2+q(3)*p[1]**2+p[2]**2==P(q('1/3'))+x*x
assert field(c['transition']['parameter'])==T and field(c['transition']['radius_squared'])==q('1/3')+T*T
assert at(4*x*x+12*x-9,T)==zero and sgn(T-A)==sgn(B-T)==1
assert len({tuple(at(p,T) for p in v) for v in points.values()})==42
results=[];support_count=0;order_count=0;all_face_sets={};all_edges={}
for dom,expected in zip(c['domains'],[('C1','open',A,T),('T','point',T,T),('C2','open',T,B)]):
 name,kind,lo,hi=expected
 assert dom['id']==name and dom['kind']==kind and field(dom['lower'])==lo and field(dom['upper'])==hi
 work={k:pointat(v,lo) for k,v in points.items()} if kind=='point' else points
 faces=dom['faces']; sets=set();es=defaultdict(list); graph={f['id']:set() for f in faces}
 n,d=plane(work,['E02-','E02+','E06-']);tet=dot(n,work['E15-'])-d
 sign=sgn(at(tet,(lo+hi)/q(2)));assert sign!=0;require_sign(tet,sign,kind,lo,hi)
 for f in faces:
  cyc=f['cycle'];assert len(set(cyc))==len(cyc)>=3 and set(cyc)==set(f['labels'])
  n,d=plane(work,cyc);assert n==tuple(loadp(a) for a in f['normal_polynomials']) and d==loadp(f['offset_polynomial'])
  require_sign(dot(n,n),1,kind,lo,hi);zeros=[]
  for lab,p in work.items():
   res=dot(n,p)-d;assert res==loadp(f['residual_polynomials'][lab]);support_count+=1
   if not res:zeros.append(lab)
   else:require_sign(res,-1,kind,lo,hi)
  assert set(zeros)==set(cyc) and frozenset(cyc) not in sets;sets.add(frozenset(cyc))
  for i,a in enumerate(cyc):
   b=cyc[(i+1)%len(cyc)];es[tuple(sorted([a,b]))].append(f['id'])
   for lab in cyc:
    if lab not in (a,b):
     require_sign(dot(n,cross(sub(work[b],work[a]),sub(work[lab],work[a]))),1,kind,lo,hi);order_count+=1
 assert set(l for e in es for l in e)==set(points)
 for e,fs in es.items():
  assert len(fs)==2 and len(set(fs))==2
  a,b=fs;graph[a].add(b);graph[b].add(a)
 visited=set();todo=[next(iter(graph))]
 while todo:
  k=todo.pop()
  if k not in visited:visited.add(k);todo.extend(graph[k]-visited)
 assert visited==set(graph)
 assert 42-len(es)+len(faces)==2
 hist=Counter(len(f['cycle']) for f in faces)
 results.append({'id':name,'V':42,'E':len(es),'F':len(faces),'face_histogram':dict(hist),'exact_support_and_maximal_zero_sets':True,'true_polygon_sides':True,'ridge_closure':True,'connected_dual_graph':True})
 all_face_sets[name]=sets;all_edges[name]=set(es)
 print('Independent exact domain',name,results[-1],flush=True)
assert len(all_face_sets['C1']&all_face_sets['T']&all_face_sets['C2'])==38
assert all_edges['T']==all_edges['C1']&all_edges['C2']
assert len(all_edges['C1']-all_edges['T'])==12 and len(all_edges['C2']-all_edges['T'])==6
# Test the reviewer positivity route, including interior zeros and both signs.
mid=(A+T)/q(2)
try:bernstein_positive((x-mid)**2,A,T)
except AssertionError:double_rejected=True
else:raise AssertionError('Reviewer even-root challenge unexpectedly accepted')
bernstein_positive(-(x-A)**2*(x-T),A,T)
result={'status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'certificate_sha256':hashlib.sha256(raw).hexdigest(),'arithmetic':'SymPy QQ.algebraic_field(sqrt(2)) and sparse polynomial-ring operations; exact rational enclosures of sqrt(2) for order signs','interval_method':'Exact Bernstein coefficient positivity, with strict subdivision-point checks. No submitted Sturm or arithmetic code imported.','domains':results,'fold_coordinate_concordance':True,'transition_distinct_points':42,'support_residual_checks':support_count,'polygon_side_checks':order_count,'distinct_sign_proofs':len(sign_records),'max_bernstein_leaves':max([len(r.get('positive_bernstein_subintervals',[])) for r in sign_records]),'unchanged_facets':38,'edges_lost':12,'edges_gained':6,'even_root_challenge_rejected':double_rejected,'endpoint_only_root_positive_control_passed':True,'limits':'Checks the submitted new-domain certificate; does not rerun old A/B enumeration, external novelty review, or proof-assistant verification. SymPy and Python remain trusted dependencies.'}
(OUT/'INDEPENDENT_EXACT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'BERNSTEIN_SIGN_CERTIFICATES.json').write_text(json.dumps({'certificate_sha256':result['certificate_sha256'],'proofs':sign_records},indent=2)+'\n')
print(json.dumps(result,indent=2))
