"""Independent, read-only BOUNDARY-12 review.
Reconstructs Paper C geometry; certifies new graph/hull data and fixed scalar cases.
Does not import or execute submitted analysis/checker scripts or run dynamics.
"""
from pathlib import Path, PurePosixPath
from itertools import combinations
from collections import Counter, defaultdict
from functools import lru_cache
import ast, hashlib, json, zipfile, stat, time, sys
import sympy as sp
import mpmath as mp

BASE=Path('/mnt/data/boundary12_submission')
OUT=Path('/mnt/data/BOUNDARY12_GPT_SCIENTIFIC_REVIEW_v0.1')
START=time.monotonic(); checks=[]; results={}
def ck(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def load(name):return json.loads((BASE/name).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')

K=sp.QQ.algebraic_field(sp.sqrt(2),sp.sqrt(3));z=K.zero;one=K.one
q=lambda a,b=1:K.convert(sp.Rational(a,b))
r2=K.from_sympy(sp.sqrt(2));r3=K.from_sympy(sp.sqrt(3))
@lru_cache(None)
def expr(x):return sp.expand(K.to_sympy(x))
@lru_cache(None)
def sg(x):
    if x==z:return 0
    p=expr(x)
    if p.is_positive is True:return 1
    if p.is_negative is True:return -1
    raise ArithmeticError('Undecided exact sign '+str(p))
@lru_cache(None)
def fl(x):return float(expr(x).evalf(40))
@lru_cache(None)
def parse(text):
    def rec(n):
        if isinstance(n,ast.Constant) and type(n.value) is int:return q(n.value)
        if isinstance(n,ast.UnaryOp):
            a=rec(n.operand)
            if isinstance(n.op,ast.USub):return -a
            if isinstance(n.op,ast.UAdd):return a
        if isinstance(n,ast.BinOp):
            a,b=rec(n.left),rec(n.right)
            if isinstance(n.op,ast.Add):return a+b
            if isinstance(n.op,ast.Sub):return a-b
            if isinstance(n.op,ast.Mult):return a*b
            if isinstance(n.op,ast.Div):return a/b
            if isinstance(n.op,ast.Pow) and isinstance(n.right,ast.Constant):return a**int(n.right.value)
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='sqrt' and len(n.args)==1:
            if isinstance(n.args[0],ast.Constant):return {2:r2,3:r3,6:r2*r3}[n.args[0].value]
        raise ValueError(ast.dump(n))
    return rec(ast.parse(str(text),mode='eval').body)
vec=lambda v:tuple(parse(str(x)) for x in v)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
scale=lambda c,a:tuple(c*x for x in a)
dot=lambda a,b:sum((x*y for x,y in zip(a,b)),z)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def zero(v):return all(x==z for x in v)
def rot(v):return(-v[0]/2-r3*v[1]/2,r3*v[0]/2-v[1]/2,v[2])
def transform(v,k,fx,fz):
    v=((-v[0] if fx else v[0]),v[1],(-v[2] if fz else v[2]))
    for _ in range(k):v=rot(v)
    return v

def archive_check(path,manifest_name,manifest_dict=True):
    with zipfile.ZipFile(path) as Z:
        names=Z.namelist(); infos=Z.infolist()
        ck('archive names '+path.name,len(names)==len(set(names))==len({s.casefold() for s in names}) and all(not PurePosixPath(s).is_absolute() and '..' not in PurePosixPath(s).parts and '\\' not in s and ':' not in s for s in names))
        ck('archive no symlink '+path.name,all(stat.S_IFMT(i.external_attr>>16)!=stat.S_IFLNK and not i.is_dir() for i in infos))
        ck('archive CRC '+path.name,Z.testzip() is None)
        m=json.loads(Z.read(manifest_name))['files']
        if isinstance(m,list):m={r['path']:r for r in m}
        ck('archive coverage '+path.name,set(names)==set(m)|{manifest_name})
        for n,r in m.items():
            b=Z.read(n);ck('archive payload '+n,len(b)==r['bytes'] and sha(b)==r['sha256'])
        return {'bytes':path.stat().st_size,'sha256':sha(path.read_bytes()),'members':len(names),'manifested_payloads':len(m),'raw_bytes':sum(i.file_size for i in infos)}

results['archive']=archive_check(Path('/mnt/data/BOUNDARY12_GPT_REVIEW.zip'),'REVIEW_MANIFEST.json')
ck('separate report matches archive',(BASE/'BOUNDARY12_REPORT.md').read_bytes()==Path('/mnt/data/BOUNDARY12_REPORT.md').read_bytes())
# Compare all inherited handoff bytes to the actual earlier handoff, not newly claimed copies.
with zipfile.ZipFile('/mnt/data/BOUNDARY12_CODEX_HANDOFF_v0.1_20261016.zip') as Z:
    matched=[]
    for n in Z.namelist():
        if n.endswith('/'):continue
        p=BASE/'incoming'/n
        ck('actual handoff '+n,p.exists() and p.read_bytes()==Z.read(n));matched.append(n)
    results['handoff_members_verified']=len(matched)
with zipfile.ZipFile('/mnt/data/BOUNDARY11_REVIEW_PACKAGE.zip') as Z:
    selected=[]
    for p in (BASE/'incoming/reference/BOUNDARY11').rglob('*'):
        if p.is_file():
            n=p.relative_to(BASE/'incoming/reference/BOUNDARY11').as_posix()
            ck('actual B11 selected '+n,p.read_bytes()==Z.read(n));selected.append(n)
    ck('same Plotly library',(BASE/'assets/plotly-3.1.0.min.js').read_bytes()==Z.read('assets/plotly-3.1.0.min.js'))
    results['B11_selected_members_verified']=selected
ck('actual complete B11 review',(BASE/'incoming/reference/BOUNDARY11_GPT_REVIEW_v0.1.zip').read_bytes()==Path('/mnt/data/BOUNDARY11_GPT_REVIEW_v0.1.zip').read_bytes())

# Independent source construction (width one).
h=(r2-one)/2; tt=[h,q(1,2),(one+r2)/2];evnames=['original','A','B']
uv=[(-q(1,2),-h),(-h,-q(1,2)),(h,-q(1,2)),(q(1,2),-h),(q(1,2),h),(h,q(1,2)),(-h,q(1,2)),(-q(1,2),h)]
origin=(z,r3/6,z)
maps=[lambda u,v:(-q(1,4)-u/2,r3/4-r3*u/2,v),lambda u,v:(u,z,v),lambda u,v:(q(1,4)-u/2,r3/4+r3*u/2,v)]
V=[];FC=[]
for fn in maps:
    face=[]
    for u,v in uv:
        x=sub(fn(u,v),origin)
        if x not in V:V.append(x)
        face.append(V.index(x))
    FC.append(face)
edges=sorted({tuple(sorted((a,b))) for f in FC for a,b in zip(f,f[1:]+f[:1])})
D=load('incoming/reference/BOUNDARY11/data/geometry_inventory.json')
ck('original geometry counts',len(V)==18 and len(edges)==21)
ck('original face indexing',FC==D['faces'])
ck('source vertices',V==[vec(v['centered_exact']) for v in D['vertices']])
E={}
for j,(a,b) in enumerate(edges,1):
    id=f'E{j:02d}';m=scale(q(1,2),add(V[a],V[b]));u=scale(one/(2*h),sub(V[b],V[a]));raw=D['edges'][j-1]
    ck(id+' source incidence',id==raw['id'] and [a,b]==raw['vertices'])
    ck(id+' midpoint unit',m==vec(raw['midpoint_exact']) and u==vec(raw['unit_direction_exact']) and dot(u,u)==one and dot(m,u)==z and dot(m,m)==q(1,3))
    E[id]=(m,u,a,b,raw['class'])
P=[];BR=[];GP=[]
for k,t in enumerate(tt):
    branches={id+sign:add(m,scale(t*(1 if sign=='+' else -1),u)) for id,(m,u,*_) in E.items() for sign in ['-','+']}
    groups=defaultdict(list)
    for id,pt in branches.items():groups[pt].append(id)
    pts=list(groups);P.append(pts);BR.append(branches);GP.append(groups)
    ck(evnames[k]+' counts and norms',len(pts)==18 and Counter(map(len,groups.values()))=={2:12,3:6} and all(dot(x,x)==q(1,3)+t*t for x in pts))
    ck(evnames[k]+' accepted groups',[(vec(g['coordinates_exact']),g['branches']) for g in D['coincidence_events'][k]['groups']]==list(groups.items()))
# Reuse B11's exhaustive classification, do not resolve its branch-pair equations.
cat=load('incoming/reference/BOUNDARY11/evidence/all_branch_coincidence_checks.json')
roots={parse(r['tau'])**2 for r in cat if r['tau'] is not None and r['branch_a'][:3]!=r['branch_b'][:3]}
ck('accepted classification roots',roots=={(t/h)**2 for t in tt})
LT=load('data/terminations_and_lengths.json');ck('42 ray records',len(LT['rays'])==42)
for k,r in enumerate(LT['length_table']):
    ck('length table '+r['event'],[parse(r[key]) for key in ['t_over_w','C_over_w','ell_over_w','total_added_over_w','R2_over_w2']]==[tt[k],2*tt[k],tt[k]-h,2*(tt[k]-h),q(1,3)+tt[k]*tt[k]])
for r in LT['rays']:
    id=r['branch'];m,u,a,b,_=E[id[:3]];sgn=1 if id[-1]=='+' else -1
    ck('ray source '+id,r['original_endpoint_vertex']==(b if sgn==1 else a) and vec(r['outward_unit_direction_exact'])==scale(q(sgn),u))
    for k,key in enumerate(['original','first_new_meeting','last_finite_meeting']):
        rr=r[key];point=BR[k][id]
        ck('ray meeting '+id+' '+key,vec(rr['coordinates_exact'])==point and rr['incident_branches']==GP[k][point] and rr['outer_dot_id']==f'{evnames[k]}:P{P[k].index(point)+1:02d}')
    ck('ray extensions '+id,parse(r['first_extension_over_w'])==tt[1]-h and parse(r['last_extension_over_w'])==one)
ck('unit length facts and progression',2*tt[1]==one and tt[2]-h==one and tt[1]-h==(r2-one)/r2 and tt[1]/tt[0]==tt[2]/tt[1]==one+r2)
results['source_and_termination']={'vertices':18,'edges':21,'rays':42,'event_groups_checked':54,'accepted_catalogue_rows_consumed':len(cat),'old_equations_resolved':0}

# Exact hull generation: all triples; compare zero sets, plane equations, metrics and topology.
results['events']=[];allGP=[];all_vertices=[]
for k,name in enumerate(evnames):
    print('Review exact hull',name,flush=True)
    pts=P[k];source=load(f'data/hull_{name}.json');graph=load(f'data/graph_{name}.json')
    ck(name+' hull points',pts==[vec(r['exact']) for r in source['vertices']])
    seen=set();facets={};collinear=0
    for i,j,l in combinations(range(18),3):
        n=cross(sub(pts[j],pts[i]),sub(pts[l],pts[i]))
        if zero(n):collinear+=1;continue
        d=dot(n,pts[i]);pivot=next(x for x in (*n,d) if x!=z)
        key=(*scale(one/pivot,n),d/pivot)
        if key in seen:continue
        seen.add(key);n=key[:3];d=key[3]
        residual=[dot(n,p)-d for p in pts];signs={sg(x) for x in residual}
        if {-1,1}<=signs:continue
        if 1 in signs:n=scale(-one,n);d=-d;residual=[-x for x in residual]
        ids=frozenset(i for i,x in enumerate(residual) if x==z)
        ck(name+' origin inside support',sg(d)>0)
        facets[ids]=(n,d)
    sf={frozenset(f['vertices']):f for f in source['faces']}
    ck(name+' complete facets',set(facets)==set(sf) and len(sf)==len(source['faces']))
    ck(name+' enumeration',source['enumeration']=={'triples':816,'distinct_noncollinear_planes':len(seen),'collinear_triples':collinear,'rejected_planes':len(seen)-len(facets)})
    planes=[];edgefaces=defaultdict(list);plane_by_id={};typed=Counter();face_orbits=[]
    for ids,(n,d) in facets.items():
        f=sf[ids];nn=vec(f['normal_exact']);dd=parse(f['offset_exact']);cy=f['vertices']
        ck(name+' plane '+f['id'],sg(dd)>0 and scale(dd,n)==scale(d,nn))
        res=[dot(nn,p)-dd for p in pts]
        ck(name+' residuals '+f['id'],res==[parse(x) for x in f['all_outer_point_residuals_exact']] and all(sg(x)<=0 for x in res))
        planes.append((nn,dd,f['id']));plane_by_id[f['id']]=(nn,dd)
        sides=[sub(pts[b],pts[a]) for a,b in zip(cy,cy[1:]+cy[:1])]
        lens=[dot(x,x) for x in sides];turns=[dot(sides[j-1],sides[j]) for j in range(len(sides))]
        ck(name+' side metrics '+f['id'],lens==list(map(parse,f['side_squared_exact'])) and turns==list(map(parse,f['turn_dot_exact'])))
        ck(name+' convex face order '+f['id'],all(sg(dot(cross(sides[j],sub(pts[v],pts[cy[j]])),nn))>=0 for j in range(len(cy)) for v in cy) and all(sg(dot(cross(sides[j-1],sides[j]),nn))>0 for j in range(len(cy))))
        regular=len(set(lens))==len(set(turns))==1
        ck(name+' regular flag '+f['id'],f['regular']==regular)
        kind=f'{len(cy)}-gon '+('regular' if regular else 'nonregular')
        if len(cy)==3 and not regular:kind='isosceles triangle' if len(set(lens))==2 else 'scalene triangle'
        if len(cy)==4:
            if all(x==z for x in turns):kind='square' if len(set(lens))==1 else 'rectangle'
            else:
                para=[j for j in [0,1] if zero(cross(sides[j],sides[j+2]))]
                if len(para)==1 and lens[(para[0]+1)%4]==lens[(para[0]+3)%4]:kind='isosceles trapezoid'
        ck(name+' face type '+f['id'],kind==f['type']);typed[kind]+=1
        for a,b in zip(cy,cy[1:]+cy[:1]):edgefaces[tuple(sorted((a,b)))].append(f['id'])
        if kind=='isosceles trapezoid':ck(name+' trapezoid lengths '+f['id'],Counter(lens)==Counter([one,one,one,(one+r2/2)**2]))
    ck(name+' hull edge table',{tuple(r['vertices']):set(r['faces']) for r in source['edges']}=={pair:set(fs) for pair,fs in edgefaces.items()})
    ck(name+' closed manifold edges',all(len(fs)==2 for fs in edgefaces.values()))
    ck(name+' hull VEF',source['V']==18 and source['E']==len(edgefaces) and source['F']==len(facets) and 18-len(edgefaces)+len(facets)==2 and dict(typed)==source['face_types'])
    for v in range(18):
        link=defaultdict(set)
        for f in source['faces']:
            cy=f['vertices']
            if v in cy:
                j=cy.index(v);a,b=cy[j-1],cy[(j+1)%len(cy)];link[a].add(b);link[b].add(a)
        used=set();todo=[next(iter(link))]
        while todo:
            x=todo.pop()
            if x not in used:used.add(x);todo.extend(link[x]-used)
        ck(name+' vertex link '+str(v),used==set(link) and all(len(a)==2 for a in link.values()))
    pindex={pt:i for i,pt in enumerate(pts)}
    ck(name+' exact D3h maps',all(transform(p,j,fx,fz) in pindex for p in pts for j in range(3) for fx in range(2) for fz in range(2)))
    remaining=set(sf)
    while remaining:
        face=next(iter(remaining));orbit={frozenset(pindex[transform(pts[v],j,fx,fz)] for v in face) for j in range(3) for fx in range(2) for fz in range(2)}
        ck(name+' facet orbit',orbit<=remaining);remaining-=orbit;face_orbits.append({sf[f]['id'] for f in orbit})
    ck(name+' orbit inventory',{frozenset(o) for o in face_orbits}=={frozenset(o['face_ids']) for o in source['D3h_face_orbits']})
    ck(name+' source panel containment',all(sg(dot(n,v)-d)<=0 for n,d,_ in planes for v in V))
    # Graph coordinates, sorted line intervals, exact lengths and interior/edge classification.
    all_vertices.extend(pts);allGP.extend((name,pt,GP[k][pt]) for pt in pts)
    gpts=[vec(v['exact']) for v in graph['vertices']];gindex={v:i for i,v in enumerate(gpts)}
    ck(name+' graph vertex set',len(gindex)==len(gpts) and set(gpts)==set(all_vertices))
    expected_edges={};expected_adj=defaultdict(set)
    for id,(m,u,a,b,cls) in E.items():
        ts=[-t for t in reversed(tt[:k+1])]+tt[:k+1]
        ii=[gindex[add(m,scale(t,u))] for t in ts]
        for j in range(len(ii)-1):
            a,b=ii[j:j+2];key=(id,a,b);ta,tb=ts[j:j+2];expected_edges[key]=(ta,tb,cls)
            expected_adj[a].add(b);expected_adj[b].add(a)
    ck(name+' graph edge set',set(expected_edges)=={(e['source_edge'],*e['vertices']) for e in graph['edges']} and len(expected_edges)==len(graph['edges']))
    locus=Counter();vertex_loci=Counter();vactive={}
    for v,pt in enumerate(gpts):
        res=[dot(n,pt)-d for n,d,_ in planes];ck(name+' graph containment '+str(v),all(sg(x)<=0 for x in res))
        active={planes[i][2] for i,x in enumerate(res) if x==z};vactive[v]=active;vertex_loci['boundary' if active else 'strict_interior']+=1
        vr=graph['vertices'][v]
        ck(name+' graph vertex record '+str(v),vr['id']==v and set(vr['adjacency'])==expected_adj[v] and vr['degree']==len(expected_adj[v]))
        matching=[(en,groups[pt],idx.index(pt)) for en,idx,groups in zip(evnames[:k+1],P[:k+1],GP[:k+1]) if pt in groups]
        en,labels,gid=matching[0]
        ck(name+' graph incidence labels '+str(v),vr['event']==en and vr['dot_id']==f'{en}:P{gid+1:02d}' and vr['branch_labels']==labels)
    for e in graph['edges']:
        id=e['source_edge'];a,b=e['vertices'];ta,tb,cls=expected_edges[(id,a,b)];active=vactive[a]&vactive[b]
        lc='hull_edge' if len(active)>=2 else 'face_interior' if active else 'hull_interior';locus[lc]+=1
        kind='original' if ta==-h and tb==h else 'added';ray=None if kind=='original' else id+('+' if sg(ta)>=0 else '-')
        ck(name+' graph edge record '+e['id'],parse(e['length_exact'])==tb-ta and list(map(parse,e['t_interval_exact']))==[ta,tb] and e['source_class']==cls and e['segment_kind']==kind and e['source_ray']==ray and e['relative_open_segment_locus']==lc and set(e['support_faces'])==active)
        ck(name+' geometric edge length '+e['id'],dot(sub(gpts[b],gpts[a]),sub(gpts[b],gpts[a]))==(tb-ta)**2)
    used=set();components=[]
    for v in range(len(gpts)):
        if v in used:continue
        cc=set();todo=[v]
        while todo:
            a=todo.pop()
            if a not in cc:cc.add(a);todo.extend(expected_adj[a]-cc)
        used|=cc;components.append(sorted(cc))
    deg=Counter(map(len,expected_adj.values()))
    ck(name+' graph summary',graph['components']==components and graph['component_count']==1 and graph['V']==18*(k+1) and graph['E']==21*(2*k+1) and graph['cycle_rank']==4+24*k and graph['degree_counts']=={str(a):b for a,b in deg.items()} and graph['segment_locus_counts']==dict(locus))
    ck(name+' nested hulls',all(sg(dot(n,pt)-d)<=0 for pt in all_vertices for n,d,_ in planes))
    # Compare independently generated certificate to submitted final written-data certificate.
    cert=load('evidence/FINAL_GEOMETRY_CERTIFICATES.json')['events'][k]
    ck(name+' final certificate counts',cert['counts']==dict(vertex_loci))
    for row in cert['vertices']:ck(name+' final vertex certificate '+str(row['graph_vertex']),set(row['active_faces'])==vactive[row['graph_vertex']])
    results['events'].append({'event':name,'support_triples':816,'distinct_planes':len(seen),'facets':len(facets),'hull_edges':len(edgefaces),'face_types':dict(typed),'face_orbit_sizes':sorted(map(len,face_orbits)),'graph_vertices':len(gpts),'graph_edges':len(expected_edges),'graph_cycle_rank':len(expected_edges)-len(gpts)+1,'vertex_loci':dict(vertex_loci),'segment_loci':dict(locus),'PASS':True})

# Scalar and prescribed sample verification: no new radius search.
mp.mp.dps=85
phi=(1+mp.sqrt(5))/2;T=mp.pi*mp.e*phi;ga=mp.zeta(3)/T;ll=mp.log(phi)
I=mp.quad(lambda x: x*x/mp.tanh(x) if x else mp.mpf(0),[0,ll])
SC=load('data/scalar_comparisons.json')
for key,val in [('T',T),('gamma_star',ga),('I2',I)]:ck('scalar '+key,abs(mp.mpf(SC[key])-val)<mp.mpf('1e-58'))
ck('integral identity check',abs(I-mp.zeta(3)/10)<mp.mpf('1e-80'))
RR=[mp.sqrt(mp.mpf(13)/12-mp.sqrt(2)/2),mp.sqrt(mp.mpf(7)/12),mp.sqrt(mp.mpf(13)/12+mp.sqrt(2)/2)]
ratios=[RR[1]/RR[0],RR[2]/RR[1],RR[2]/RR[0],1+mp.sqrt(2)]
for rr,expect in zip(SC['ratios'],ratios):
    for key,val,tol in [('value',expect,'1e-46'),('T_over_10',T/10,'1e-46'),('signed_difference_ratio_minus_T10',expect-T/10,'1e-46'),('relative_difference_over_T10',(expect-T/10)/(T/10),'1e-37')]:
        ck(rr['ratio']+' '+key,abs(mp.mpf(rr[key])-val)<mp.mpf(tol))
for key,powr in [('length',1),('area',mp.mpf(1)/2),('volume',mp.mpf(1)/3)]:ck('conditional units '+key,abs(mp.mpf(SC['conditional_linear_ratios_for_same_positive_measure'][key])-(T/10)**powr)<mp.mpf('1e-38'))

def mnum(x):return mp.mpf(str(expr(x).evalf(87)))
rs=RR+[mp.mpf(1),2/mp.sqrt(3),mp.mpf(10),T];maxerr=mp.mpf(0)
F=load('data/fixed_presets.json');expected_viewer=[]
for j,(r,preset) in enumerate(zip(rs,F)):
    t=mp.sqrt(r*r-mp.mpf(1)/3);hv=(mp.sqrt(2)-1)/2
    nums={'R_over_w':r,'t_over_w':t,'C_over_w':2*t,'ell_over_w':t-hv}
    ck('preset scalars '+preset['id'],all(abs(mp.mpf(v)-nums[key])<mp.mpf('4e-15') for key,v in preset['numeric'].items()))
    pts=[]
    for row in preset['points']:
        id=row['branch'];m,u,*_=E[id[:3]];sn=1 if id[-1]=='+' else -1
        expected=[mnum(m[i])+sn*t*mnum(u[i]) for i in range(3)]
        err=max(abs(mp.mpf(row['xyz'][i])-expected[i]) for i in range(3));maxerr=max(maxerr,err)
        ck('preset point '+preset['id']+' '+id,err<mp.mpf('4e-15'))
        pts.append({'branch':id,'xyz_over_w':list(map(float,expected))})
    ck('preset count '+preset['id'],preset['unique_point_count']==(18 if j<3 else 42))
    expected_viewer.append({'preset_id':preset['id'],'numeric':{a:float(b) for a,b in nums.items()},'points':pts})
results['scalar_verification']={'decimal_precision':85,'I2_residual':str(I-mp.zeta(3)/10),'fixed_presets':7,'branch_coordinates':294,'max_saved_coordinate_error':str(maxerr),'ratio_comparisons':4,'no_fitted_comparisons':True}
save('EXPECTED_VIEWER_POINTS.json',expected_viewer)
# Sealed embedded datasets must equal checked inventories.
VD=load('data/viewer_data.json')
ck('viewer original geometry dataset',VD['geometry']==D)
ck('viewer presets dataset',VD['presets']==F)
for k,name in enumerate(evnames):
    ck('viewer graph dataset '+name,VD['graphs'][name]==load(f'data/graph_{name}.json'))
    ck('viewer hull dataset '+name,VD['hulls'][name]==load(f'data/hull_{name}.json'))
    ck('viewer event dataset '+name,VD['events'][name]==D['coincidence_events'][k])
# Provided validation histories and local preservation evidence, not live filesystem access.
pr=load('evidence/SOURCE_PRESERVATION.json')
ck('81 unique provided preservation rows',len(pr['files'])==pr['unique_files']==81 and len({r['path'] for r in pr['files']})==81)
ck('all preservation identities agree',all(r['expected_sha256']==r['actual_sha256'] and r['unchanged'] for r in pr['files']))
available=0
for r in pr['files']:
    fn=Path('/mnt/data')/r['path'].replace('\\','/').rsplit('/',1)[-1]
    if fn.exists() and fn.is_file():
        if sha(fn.read_bytes())==r['expected_sha256']:available+=1
results['preservation']={'submitted_rows_agree':81,'current_Windows_access':False,'available_direct_basename_matches':available,'source_directory_limit':'Exact handoff and prior B11 archive comparisons above, not independent inspection of all Windows files.'}
EX=load('evidence/NEW_EXACT_GEOMETRY_CHECKS.json');VC=load('evidence/VIEWER_CHECKS.json')
results['submitted_check_records']={'exact_geometry':{k:v for k,v in EX.items() if k!='predicates'},'viewer':{k:v for k,v in VC.items() if k not in ['checks','rows','cases']}}
results['independent_checks_passed']=len(checks);results['check_labels']=checks
results['elapsed_seconds']=time.monotonic()-START;results['PASS']=True
save('INDEPENDENT_GEOMETRY_RESULTS.json',results)
print(json.dumps({k:v for k,v in results.items() if k not in ['check_labels','submitted_check_records']},indent=2),flush=True)
