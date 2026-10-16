"""Independent BOUNDARY-11 exact-geometry review; no submitted scripts imported.
Reads the isolated extracted submission and writes only reviewer outputs.
Uses exact Q(sqrt(2),sqrt(3)) field arithmetic and independently transcribed
Paper C local maps. No evolving state, physics kernel, or random sampling.
"""
from pathlib import Path
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
import ast, hashlib, json, math, stat, time, zipfile
import sympy as sp

BASE=Path('/mnt/data/boundary11_submission')
OUT=Path('/mnt/data/BOUNDARY11_GPT_REVIEW_v0.1')
ZIP=Path('/mnt/data/BOUNDARY11_REVIEW_PACKAGE.zip')
start=time.monotonic()
K=sp.QQ.algebraic_field(sp.sqrt(2),sp.sqrt(3))
zero=K.zero;one=K.one
r2=K.from_sympy(sp.sqrt(2));r3=K.from_sympy(sp.sqrt(3))
q=lambda n,d=1:K.convert(sp.Rational(n,d))
h=(r2-one)/2; a2=q(1,3); p=r3/6; rho2=a2+h*h
checks=[]
def check(name, cond):
    if not cond: raise AssertionError(name)
    checks.append(name)
@lru_cache(None)
def parse(text, tau_value=None):
    def rec(n):
        if isinstance(n,ast.Constant) and type(n.value) is int:return q(n.value)
        if isinstance(n,ast.Name) and n.id=='tau' and tau_value is not None:return q(tau_value)
        if isinstance(n,ast.UnaryOp):
            v=rec(n.operand)
            if isinstance(n.op,ast.USub):return -v
            if isinstance(n.op,ast.UAdd):return v
        if isinstance(n,ast.BinOp):
            a,b=rec(n.left),rec(n.right)
            if isinstance(n.op,ast.Add):return a+b
            if isinstance(n.op,ast.Sub):return a-b
            if isinstance(n.op,ast.Mult):return a*b
            if isinstance(n.op,ast.Div):return a/b
            if isinstance(n.op,ast.Pow) and isinstance(n.right,ast.Constant) and type(n.right.value) is int:return a**n.right.value
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='sqrt' and len(n.args)==1:
            assert isinstance(n.args[0],ast.Constant)
            arg=n.args[0].value
            if arg==2:return r2
            if arg==3:return r3
            if arg==6:return r2*r3
        raise ValueError(ast.dump(n))
    return rec(ast.parse(str(text),mode='eval').body)
@lru_cache(None)
def f(v):return float(K.to_sympy(v).evalf(20))
def s(v):return str(sp.expand(K.to_sympy(v)))
def vec(v):return tuple(parse(str(x)) for x in v)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),zero)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def vzero(a):return all(x==zero for x in a)
def matrix_moment(points):return [[sum((v[i]*v[j] for v in points),zero) for j in range(3)] for i in range(3)]
def ro(v):return (-v[0]/2-r3*v[1]/2,r3*v[0]/2-v[1]/2,v[2])
def sv(v):return (-v[0],v[1],v[2])
def sh(v):return (v[0],v[1],-v[2])
def group(v):
    vals=[]
    for iz in range(2):
        for ix in range(2):
            x=sh(v) if iz else v;x=sv(x) if ix else x
            for k in range(3):vals.append(x);x=ro(x)
    return set(vals)
def orbits(points):
    rem=set(points);sizes=[]
    while rem:
        g=group(next(iter(rem)));assert g<=rem
        sizes.append(len(g));rem-=g
    return sorted(sizes)

with zipfile.ZipFile(ZIP) as z:
    info=z.infolist(); names=z.namelist();manifest=json.loads(z.read('MANIFEST_SHA256.json'))['files']
    check('safe unique archive names',len(names)==len(set(names))==len({x.casefold() for x in names}) and all(not Path(x).is_absolute() and '..' not in Path(x).parts and '\\' not in x for x in names))
    check('no archive symlinks',not any(stat.S_ISLNK(i.external_attr>>16) for i in info))
    check('CRC',z.testzip() is None)
    check('complete archive manifest',set(names)=={'MANIFEST_SHA256.json'}|{r['path'] for r in manifest})
    for row in manifest:
        b=z.read(row['path']);check('archive:'+row['path'],len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'])

D=json.loads((BASE/'data/geometry_inventory.json').read_text())
uv=[(-q(1,2),-h),(-h,-q(1,2)),(h,-q(1,2)),(q(1,2),-h),(q(1,2),h),(h,q(1,2)),(-h,q(1,2)),(-q(1,2),h)]
o=(zero,p,zero)
maps=[lambda u,z:(-q(1,4)-u/2,r3/4-r3*u/2,z),lambda u,z:(u,zero,z),lambda u,z:(q(1,4)-u/2,r3/4+r3*u/2,z)]
V=[];faces=[]
for fn in maps:
    face=[]
    for u,z in uv:
        v=sub(fn(u,z),o)
        if v not in V:V.append(v)
        face.append(V.index(v))
    faces.append(face)
check('18 welded vertices and source face cycles',len(V)==18 and faces==D['faces'])
for row,v in zip(D['vertices'],V):
    check('vertex:'+str(row['id']),v==vec(row['centered_exact']) and add(v,o)==vec(row['original_exact']))
check('source vertex radius',all(dot(v,v)==rho2 for v in V))
check('source centroid',vzero(tuple(sum((v[k] for v in V),zero) for k in range(3))))
edge_ids=sorted({tuple(sorted((face[i],face[(i+1)%8]))) for face in faces for i in range(8)})
check('21 edges',len(edge_ids)==21)
records=[];branches=[];kinds=[]
for ix,(i,j) in enumerate(edge_ids):
    row=D['edges'][ix];m=mul(q(1,2),add(V[i],V[j]));d=mul(q(1,2),sub(V[j],V[i]));u=mul(one/h,d)
    kind='seam' if d[0]==d[1]==zero else 'horizontal' if d[2]==zero else 'chamfer'
    check('edge:'+row['id'],row['id']==f'E{ix+1:02d}' and row['vertices']==[i,j] and m==vec(row['midpoint_exact']) and d==vec(row['half_edge_exact']) and u==vec(row['unit_direction_exact']) and row['class']==kind)
    check('midsphere/tangency:'+row['id'],dot(m,m)==a2 and dot(m,d)==zero and dot(d,d)==h*h and dot(u,u)==one)
    records.append((m,d,u));kinds.append(kind)
    branches.extend([(row['id']+'-',m,mul(-one,d)),(row['id']+'+',m,d)])
check('edge classes',Counter(kinds)=={'seam':3,'horizontal':6,'chamfer':12})

# Independent exact least-squares scalar projection, followed by zero residual;
# compares all outcomes including negative/non-admissible roots.
submitted=json.loads((BASE/'evidence/all_branch_coincidence_checks.json').read_text())
roots=set();root_counts=Counter();bc=[]
for k,(i,j) in enumerate(combinations(range(42),2)):
    ni,mi,di=branches[i];nj,mj,dj=branches[j]
    A=sub(mi,mj);B=sub(di,dj);bb=dot(B,B)
    x=None if bb==zero else -dot(A,B)/bb
    if x is not None and not vzero(add(A,mul(x,B))):x=None
    row=submitted[k]
    admiss=x is not None and bool(K.to_sympy(x)>=1)
    check('branchpair:'+str(k),row['branch_a']==ni and row['branch_b']==nj and ((row['tau'] is None and x is None) or (row['tau'] is not None and x is not None and parse(row['tau'])==x)) and row['admissible_tau_ge_1']==admiss)
    if admiss:roots.add(x);root_counts[s(x)]+=1
    bc.append({'pair':[ni,nj],'tau':None if x is None else s(x),'admissible':admiss})
expected_roots={one,one+r2,q(3)+2*r2}
check('only three admissible roots',roots==expected_roots)
line_counts=Counter();line_roots=set()
for i,j in combinations(range(21),2):
    mi,di,_=records[i];mj,dj,_=records[j];cr=cross(di,dj);ab=sub(mj,mi)
    if vzero(cr):
        check('distinct parallel:'+str((i,j)),not vzero(cross(ab,di)));line_counts['parallel']+=1;continue
    if dot(ab,cr)!=zero:line_counts['skew']+=1;continue
    aa=dot(cross(ab,dj),cr)/dot(cr,cr)
    bb=dot(cross(ab,di),cr)/dot(cr,cr)
    check('line meet:'+str((i,j)),add(mi,mul(aa,di))==add(mj,mul(bb,dj)) and aa*aa==bb*bb)
    line_counts['intersecting']+=1
    if bool(abs(K.to_sympy(aa))>=1):line_roots.add(aa if f(aa)>0 else -aa)
check('independent 210-line roots',line_roots==expected_roots)

# Angular coefficients independently computed and checked at every labelled pair.
angle=json.loads((BASE/'data/angular_separations.json').read_text());expected_angles={}
for i,j in combinations(range(42),2):
    ni,mi,di=branches[i];nj,mj,dj=branches[j]
    expected_angles[(ni,nj)]=(dot(mi,mj),dot(mi,dj)+dot(di,mj),dot(di,dj))
seen=set();coefs=set()
for cl in angle['classes']:
    coef=vec(cl['numerator_coefficients_ascending']);coefs.add(coef)
    check('angle class count:'+cl['id'],len(cl['branch_pairs'])==cl['multiplicity'])
    for pair in cl['branch_pairs']:
        key=tuple(pair);check('angle:'+str(key),key not in seen and expected_angles[key]==coef);seen.add(key)
check('861 angular pairs / 60 functions',len(seen)==861 and len(coefs)==len(angle['classes'])==60)
check('angular denominator',vec(angle['denominator_coefficients_ascending'])==(a2,zero,h*h))

# Parameter-polynomial symmetry: both coefficients must transform into a branch.
sig={(m,d) for _,m,d in branches}
for name,fn in [('C3',ro),('sigma_v',sv),('sigma_h',sh)]:check('symbolic symmetry:'+name,{(fn(m),fn(d)) for m,d in sig}==sig)
# Generic moment has degree 2. Exact three-value agreement identifies it fully.
for v in [0,1,2]:
    moment=matrix_moment([add(m,mul(q(v),d)) for _,m,d in branches]);tt=h*h*q(v*v)
    exp=[[zero]*3 for _ in range(3)]
    exp[0][0]=exp[1][1]=12*tt+4;exp[2][2]=18*tt+6
    check('moment coefficient test:'+str(v),moment==exp and all(moment[j][j]==parse(D['generic_second_moment_diagonal'][j],v) for j in range(3)))
# Generic orbits obtained at non-event tau=2; symbolic generators already checked.
check('generic orbit sizes',orbits([add(m,mul(q(2),d)) for _,m,d in branches])==[6,12,12,12])
event_results=[]
for row in D['coincidence_events']:
    val=parse(row['tau_exact']);groups=defaultdict(list)
    for n,m,d in branches:groups[add(m,mul(val,d))].append(n)
    check('event group exact:'+row['tau_exact'],{pt:tuple(labels) for pt,labels in groups.items()}=={vec(g['coordinates_exact']):tuple(g['branches']) for g in row['groups']})
    counts=Counter(map(len,groups.values()));M=matrix_moment(groups)
    check('18 event positions:'+row['tau_exact'],len(groups)==18 and counts=={2:12,3:6})
    check('event moment:'+row['tau_exact'],M[2][2]-M[0][0]==q(3,2) and all(M[i][i]==parse(row['unique_second_moment_diagonal'][i]) for i in range(3)))
    R2=a2+h*h*val*val;check('event radius:'+row['tau_exact'],R2==parse(row['R_squared_over_w_squared']))
    # Classify each original panel's eight segments by cyclic endpoint step.
    panel_steps=[]
    for fi,face in enumerate(faces):
        panel_edges=[ix for ix,(i,j) in enumerate(edge_ids) if any({i,j}=={face[k],face[(k+1)%8]} for k in range(8))]
        pts={add(m,mul(sign*val,d)) for ix in panel_edges for sign in [-one,one] for m,d,_ in [records[ix]]}
        check('8 panel event points:'+str((row['tau_exact'],fi)),len(pts)==8)
        # Projection basis along first nonzero horizontal panel direction and z.
        center=tuple(sum((pt[k] for pt in pts),zero)/8 for k in range(3))
        b=sub(V[face[3]],V[face[0]]);b=(b[0],b[1],zero)
        ordered=sorted(pts,key=lambda pt:math.atan2(f(pt[2]-center[2]),f(dot(sub(pt,center),b))))
        idx={pt:i for i,pt in enumerate(ordered)};steps=set()
        for ix in panel_edges:
            m,d,_=records[ix];ii=idx[add(m,mul(val,d))];jj=idx[sub(m,mul(val,d))];gap=(ii-jj)%8;steps.add(min(gap,8-gap))
        panel_steps.append(sorted(steps))
    event_results.append({'tau':s(val),'t':s(h*val),'R_squared':s(R2),'R':math.sqrt(f(R2)),'unique_points':len(groups),'multiplicities':dict(counts),'D3h_orbits':orbits(groups),'per_panel_support_steps':panel_steps})
check('panel connectivity 1/2/3',[[x[0] for x in e['per_panel_support_steps']] for e in event_results]==[[1]*3,[2]*3,[3]*3])

# Explicit latitude construction independently compared coefficient-by-coefficient.
# Values at t=0 and t=1 identify each affine branch uniquely.
ez=(zero,zero,one);n=(zero,-one,zero);b=(one,zero,zero);closed=[]
for k in range(3):
    seam=mul(-2*p,n)
    for sg in [-one,one]:closed.append((seam,mul(sg,ez)))
    for ep in [-one,one]:
        for nu in [-one,one]:
            closed.append((add(mul(p,n),mul(nu/2,ez)),mul(ep,b)))
            for sg in [-one,one]:
                m=add(add(mul(p,n),mul(sg/(2*r2),b)),mul(nu/(2*r2),ez))
                u=add(mul(sg*ep/r2,b),mul(-nu*ep/r2,ez));closed.append((m,u))
    n=ro(n);b=ro(b)
check('compact coordinate formula',set(closed)=={(m,mul(one/h,d)) for _,m,d in branches})

# Hexagon levels and regular 16-gon angular interleaving.
pat=json.loads((BASE/'data/polygon_patterns.json').read_text());hex_results=[]
for row in pat['regular_latitude_hexagons']:
    t=parse(row['t_over_w']);z=(q(1,2)+t)/r2
    pts={add(m,mul(t/h,d)) for _,m,d in branches if add(m,mul(t/h,d))[2]==z}
    check('hexagon size:'+row['t_over_w'],len(pts)==6)
    for v in pts:check('regular hexagon metric:'+s(v[0]),Counter(dot(sub(v,other),sub(v,other)) for other in pts)==Counter({zero:1,q(1,9):2,q(1,3):2,q(4,9):1}))
    check('hex radius:'+row['t_over_w'],a2+t*t==parse(row['R_squared_over_w_squared']))
    hex_results.append({'t':s(t),'R':math.sqrt(f(a2+t*t)),'ring_side':'1/3','point_count':6})
for b in [3,5,7]:
    ang={(4*k+sg*b)%32 for k in range(8) for sg in [-1,1]}
    check('16gon:'+str(b),ang==set(range(1,32,2)))

directions={mul(sign,u) for _,_,u in records for sign in [-one,one]}
check('20 limiting directions',len(directions)==20)
check('limit latitudes',Counter(s(v[2]) for v in directions)==Counter({'-1':1,'1':1,'0':6,'sqrt(2)/2':6,'-sqrt(2)/2':6}))
check('limit moment',matrix_moment(directions)==[[q(6),zero,zero],[zero,q(6),zero],[zero,zero,q(8)]])
rot60=lambda v:(v[0]/2-r3*v[1]/2,r3*v[0]/2+v[1]/2,v[2])
check('D6h limit',{rot60(v) for v in directions}==directions and {sv(v) for v in directions}==directions and {sh(v) for v in directions}==directions)

# Compare all supplied fixed display coordinates; finite checks, not a rollout.
examples=json.loads((BASE/'data/numerical_display_examples.json').read_text());maxerr=0.0;raderr=0.0
for row in examples:
    R=row['R_over_w'];tt=math.sqrt(R*R-1/3)
    for ix,(m,_,u) in enumerate(records):
        for si,sg in enumerate([-1,1]):
            point=[f(m[k])+sg*tt*f(u[k]) for k in range(3)]
            maxerr=max(maxerr,max(abs(x-y) for x,y in zip(point,row['points'][ix][si])))
            raderr=max(raderr,abs(math.sqrt(sum(x*x for x in point))-R))
check('all 252 display coordinates',maxerr<2e-15)
# Additional reviewer observation, not an original Codex theorem claim.
check('event distance ratios',q(1,2)/h==one+r2 and ((one+r2)/2)/q(1,2)==one+r2)

result={'verdict':'PASS','archive':{'bytes':ZIP.stat().st_size,'sha256':hashlib.sha256(ZIP.read_bytes()).hexdigest(),'members':45,'manifested_payloads':44},
        'independent_checks':len(checks),'counts':{'vertices':18,'edges':21,'branches':42,'branch_pairs':861,'line_pairs':210,'angular_pairs':861,'angular_function_classes':60,'display_radii':len(examples),'display_points':len(examples)*42},
        'line_pair_categories':dict(line_counts),'admissible_branch_pair_counts':dict(root_counts),'events':event_results,'hexagon_events':hex_results,
        'display_max_coordinate_difference':maxerr,'display_max_radial_residual':raderr,'limiting_direction_count':20,
        'additional_review_deduction':'Successive exceptional t distances have ratio 1+sqrt(2). This is not the ratio of sphere radii, not a dynamics law and not an infinite recurrence.',
        'seconds':time.monotonic()-start,'passed_checks':checks,
        'execution_scope':'Reviewer-written exact/static geometry only; no submitted Python checker imports/runs; no physics engine, simulation, RNG, source changes or Git writes.'}
(OUT/'INDEPENDENT_GEOMETRY_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'INDEPENDENT_BRANCH_PAIRS.json').write_text(json.dumps(bc,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='passed_checks'},indent=2))
