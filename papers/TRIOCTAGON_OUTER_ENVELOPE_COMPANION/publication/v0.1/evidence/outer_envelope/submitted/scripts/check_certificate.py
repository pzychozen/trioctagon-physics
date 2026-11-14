"""Read-only decisive checker. Reconstructs source geometry; ignores saved success flags."""
from common import *
from geometry import *
from collections import defaultdict,Counter
import argparse,itertools,time

def need(condition,message):
    if not condition:raise ValueError(message)
def connected(adj):
    if not adj:return False
    seen=set();stack=[next(iter(adj))]
    while stack:
        v=stack.pop()
        if v in seen:continue
        seen.add(v);stack.extend(adj[v]-seen)
    return seen==set(adj)
def source_concordance():
    points,vertices,cycles,edges=folded_family();inv=read(INV)
    need(len(vertices)==18 and len(edges)==21,'source dimension/count')
    need(cycles==inv['faces'],'material face-cycle mapping')
    for row,v in zip(inv['vertices'],vertices):need(svector(row['centered_exact'])==v,'source vertex mapping')
    for a,b in zip(edges,inv['edges']):
        need(a['id']==b['id'] and a['vertices']==b['vertices'],'source edge mapping')
        need(a['midpoint']==svector(b['midpoint_exact']),'source midpoint')
        need(a['unit_direction']==svector(b['unit_direction_exact']),'source direction/sign')
    for label,p in points.items():
        norm=padd(padd(pmul(p[0],p[0]),pscale(pmul(p[1],p[1]),3)),pmul(p[2],p[2]))
        need(norm==poly([Q(F(1,3)),0,1]),'common sphere identity '+label)
    need(points==inventory_family(),'independent folds/inventory family mismatch')
    return points,inv
def topology(faces,vertices):
    edges=defaultdict(list);links={v:defaultdict(set) for v in vertices};adj={f['id']:set() for f in faces}
    need(len(adj)==len(faces),'duplicate face ID')
    for f in faces:
        c=f['cycle'];need(len(c)==len(set(c))>=3,'invalid polygon cycle')
        for i,v in enumerate(c):
            prev,nxt=c[i-1],c[(i+1)%len(c)];edges[tuple(sorted((v,nxt)))].append(f['id']);links[v][prev].add(nxt);links[v][nxt].add(prev)
    need(set(v for e in edges for v in e)==set(vertices),'uncovered vertex')
    for e,fs in edges.items():
        need(len(fs)==2 and len(set(fs))==2,'ridge closure: edge '+str(e)+' does not have exactly two distinct facets')
        adj[fs[0]].add(fs[1]);adj[fs[1]].add(fs[0])
    need(connected(adj),'facet graph disconnected')
    for v,link in links.items():need(all(len(a)==2 for a in link.values()) and connected(link),'vertex link not one cycle '+str(v))
    need(len(vertices)-len(edges)+len(faces)==2,'Euler diagnostic')
    return {'V':len(vertices),'E':len(edges),'F':len(faces),'face_histogram':dict(sorted(Counter(len(f['cycle']) for f in faces).items())),'edges':[{'vertices':list(e),'facets':fs} for e,fs in sorted(edges.items())],'vertex_facets':{v:sorted(f['id'] for f in faces if v in f['cycle']) for v in vertices},'facet_adjacency':{f:sorted(a) for f,a in adj.items()},'vertex_links':{v:{p:sorted(ns) for p,ns in graph.items()} for v,graph in links.items()}}
def candidate_check(points,domains):
    h=(SQ2-1)/2;n=((),pc(-1),poly([-h/2,Q(F(1,2))]));d=poly([Q(F(1,24))+SQ2/16,(SQ2-1)/4,SQ2/4])
    residuals={k:residual(n,d,p) for k,p in points.items()};persistent=['E05+','E09+','E17+','E16-'];expected=sorted(persistent+['E21+','E10-'])
    need(all(not residuals[k] for k in persistent),'proposed persistent coplanarity fails')
    factor=pscale(pmul(poly([-T,1]),poly([-B,1])),-SQ2/4)
    need(all(residuals[k]==factor for k in ['E21+','E10-']),'proposed residual factor fails')
    evaluated={k:peval(v,T) for k,v in residuals.items()};need(all(q.sign()<=0 for q in evaluated.values()),'candidate plane not supporting')
    need(sorted(k for k,q in evaluated.items() if not q)==expected,'candidate zero set incomplete')
    matching=[f for f in domains['T']['faces'] if f['labels']==expected];need(len(matching)==1,'candidate not certified maximal facet')
    orbit=next(o for o in domains['T']['D3h_face_orbits'] if matching[0]['id'] in o['face_ids']);need(orbit['size']==6,'candidate orbit is not six')
    return {'parameter':T.dump(),'R_squared':(Q(F(1,3))+T*T).dump(),'plane_normal_transformed_divided_by_sqrt3':vdump(n),'plane_offset_divided_by_sqrt3':pdump(d),'residual_polynomials_divided_by_sqrt3':{k:pdump(v) for k,v in residuals.items()},'residuals_at_transition_divided_by_sqrt3':{k:q.dump() for k,q in evaluated.items()},'persistent_four_labels':persistent,'transition_zero_set':expected,'transition_facet_id':matching[0]['id'],'D3h_orbit':orbit,'two_nonpersistent_residual_factor':pdump(factor),'left_sign':uniform_sign(factor,A,T),'right_sign':uniform_sign(factor,T,B),'description':'Six distinct exposed points in a maximal supporting polygon; no point collision.'}
def check(cert):
    begin=time.monotonic();points,inv=source_concordance();need({k:vload(v) for k,v in cert['points'].items()}==points,'certificate branch label/coordinate mapping')
    need(cert['domain']==[A.dump(),B.dump()],'overall domain changed')
    trans=cert['transition'];t=Q.load(trans['parameter']);need(t==T,'false transition parameter')
    need(Q.load(trans['radius_squared'])==Q(F(1,3))+t*t,'false transition radius')
    need(trans['minimal_polynomial_integer_coefficients_ascending']==[-9,12,4] and peval(poly([-9,12,4]),t)==0,'transition polynomial')
    bounds=list(map(F,trans['isolating_interval_rational']));need((t-bounds[0]).sign()>0 and (bounds[1]-t).sign()>0 and root_count_open(poly([-9,12,4]),Q(bounds[0]),Q(bounds[1]))==1,'transition isolation')
    need((T-A).sign()>0 and (B-T).sign()>0,'transition outside A-B')
    actions=symmetry(points);need(actions==cert['symmetry_actions'],'incorrect D3h label action')
    domains={d['id']:d for d in cert['domains']};need(set(domains)=={'C1','T','C2'},'partition coverage/domain IDs')
    for name,kind,lo,hi in [('C1','open',A,T),('T','point',T,T),('C2','open',T,B)]:
        d=domains[name];need(d['kind']==kind and d['lower']==lo.dump() and d['upper']==hi.dump(),'coverage gap or overlapping/wrong interval '+name)
    output={};residual_counts=0;polygon_tests=0;sign_forms=set()
    for name in ['C1','T','C2']:
        dom=domains[name];lo=Q.load(dom['lower']);hi=Q.load(dom['upper']);point=dom['kind']=='point';work={k:constpoint(veval(v,lo)) for k,v in points.items()} if point else points
        if point:need(len({veval(p,lo) for p in work.values()})==42,'transition point collision')
        def sign(p):
            nonlocal sign_forms
            if not p:return 0
            sign_forms.add((name,pmonic(p)))
            return peval(p,lo).sign() if point else uniform_sign(p,lo,hi)
        tetra=['E02-','E02+','E06-','E15-'];n0,d0=plane(work,tetra);need(sign(residual(n0,d0,work[tetra[3]]))!=0,'hull lacks full dimension')
        sets=set();checks=[]
        for f in dom['faces']:
            cycle=f['cycle'];need(set(cycle)==set(f['labels']) and len(cycle)==len(f['labels']),'face cycle/zero set mismatch')
            need(f['plane_basis']==cycle[:3],'wrong plane basis')
            n,d=plane(work,cycle);need(n==vload(f['normal_polynomials']) and d==pload(f['offset_polynomial']),'stored plane not exact basis plane')
            need(sign(dot(n,n))==1,'zero face normal')
            zeros=[];signs={}
            need(set(f['residual_polynomials'])==set(points),'missing point residual')
            for label,p in work.items():
                r=residual(n,d,p);need(r==pload(f['residual_polynomials'][label]),'stored residual mismatch')
                s=sign(r);residual_counts+=1;signs[label]=s
                need(s<=0,'face fails support '+name+'/'+f['id']+'/'+label)
                if s==0:zeros.append(label)
            need(sorted(zeros)==f['labels'],'incomplete or incorrect full zero set')
            key=frozenset(zeros);need(key not in sets,'duplicate maximal facet');sets.add(key)
            for a,b in zip(cycle,cycle[1:]+cycle[:1]):
                for c in cycle:
                    if c in [a,b]:continue
                    turn=dot(n,cross(vsub(work[b],work[a]),vsub(work[c],work[a])))
                    need(sign(turn)==1,'invalid polygon cyclic edge '+name+'/'+f['id']);polygon_tests+=1
            checks.append({'facet':f['id'],'complete_zero_set':zeros,'all_point_signs':signs,'normal_nonzero':True,'polygon_side_order':'strict exact inward-side tests for every other face vertex'})
        topo=topology(dom['faces'],list(points));orbits=face_orbits(dom['faces'],actions);need(orbits==dom['D3h_face_orbits'],'face orbit mismatch')
        output[name]={'kind':dom['kind'],'lower':dom['lower'],'upper':dom['upper'],**topo,'D3h_face_orbits':orbits,'support_checks':checks,'completeness_basis':'Every listed maximal facet is actual; every polygon edge is a true ridge with both incident facets listed. Connected facet graph of the full-dimensional convex hull excludes any omitted facet, at every parameter in the domain.'}
        print('Exact domain',name,'V/E/F',topo['V'],topo['E'],topo['F'],'histogram',topo['face_histogram'],flush=True)
    endpoint_output={}
    for name,t in [('A',A),('B',B)]:
        saved=endpoint_input(name);claim=cert['endpoints'][name];need(claim['parameter']==t.dump(),'endpoint parameter')
        values={k:veval(p,t) for k,p in points.items()};unique={v:i for i,v in enumerate(sorted(set(values.values()),key=repr))};need(len(unique)==18,'endpoint unique count')
        source_map={str(v['id']):svector(v['exact']) for v in saved['vertices']};mapping={}
        for v in saved['vertices']:
            labels=sorted(k for k,p in values.items() if p==source_map[str(v['id'])]);need(bool(labels),'inherited endpoint position not recovered')
            mapping[str(v['id'])]={'source_outer_dot_id':v['outer_dot_id'],'labels':labels,'coordinates_transformed':[q.dump() for q in source_map[str(v['id'])]]}
        need(mapping==claim['vertex_mapping'],'broken endpoint label mapping')
        need(sorted(k for m in mapping.values() for k in m['labels'])==sorted(points),'endpoint label coverage')
        inv_event=next(e for e in inv['coincidence_events'] if svalue(e['t_over_w_exact'])==t)
        need({frozenset(v['labels']) for v in mapping.values()}=={frozenset(g['branches']) for g in inv_event['groups']},'endpoint inherited branch groups')
        faces=[]
        for f in saved['faces']:
            cycle=list(map(str,f['vertices']));work={k:constpoint(v) for k,v in source_map.items()};n,d=plane(work,cycle)
            residuals={k:peval(residual(n,d,p),t) for k,p in work.items()};need(all(r.sign()<=0 for r in residuals.values()),'inherited endpoint correspondence support')
            need(set(k for k,r in residuals.items() if not r)==set(cycle),'endpoint zero-set correspondence')
            for a,b in zip(cycle,cycle[1:]+cycle[:1]):
                for c in cycle:
                    if c not in [a,b]:need(peval(dot(n,cross(vsub(work[b],work[a]),vsub(work[c],work[a]))),t).sign()>0,'endpoint cycle correspondence')
            faces.append({'id':f['id'],'cycle':cycle,'labels':cycle})
        need(claim['faces']==[{'source_face_id':f['id'],'source_vertex_cycle':f['vertices'],'label_groups':[mapping[str(i)]['labels'] for i in f['vertices']]} for f in saved['faces']],'endpoint face record mapping')
        topo=topology(faces,list(source_map));need((topo['V'],topo['E'],topo['F'])==(saved['V'],saved['E'],saved['F']),'endpoint topology mismatch')
        need({tuple(sorted(e['vertices'])) for e in topo['edges']}=={tuple(sorted(map(str,e['vertices']))) for e in saved['edges']},'endpoint inherited true edges')
        endpoint_output[name]={'parameter':t.dump(),'mapping':mapping,**topo,'basis':'Comparison with authenticated saved exact endpoint facets; no 816-triple hull enumeration.'}
    candidate=candidate_check(points,domains)
    # Match every limiting chamber polygon to the actual exceptional face or edge.
    limits={}
    for chamber,event,t in [('C1','A',A),('C1','T',T),('C2','T',T),('C2','B',B)]:
        rows=[]
        if event=='T':targetfaces={f['id']:set(f['labels']) for f in domains['T']['faces']};map_label={k:k for k in points}
        else:
            targetfaces={f['source_face_id']:set(map(str,f['source_vertex_cycle'])) for f in cert['endpoints'][event]['faces']}
            map_label={label:idx for idx,m in cert['endpoints'][event]['vertex_mapping'].items() for label in m['labels']}
        for face in domains[chamber]['faces']:
            image=set(map_label[k] for k in face['labels']);targets=sorted(f for f,s in targetfaces.items() if image<=s)
            need(bool(targets),'chamber limit not in inherited/transition boundary')
            rows.append({'chamber_face':face['id'],'image_vertices':sorted(image),'image_vertex_count':len(image),'containing_event_facets':targets,'dimension':min(2,len(image)-1)})
        if event=='T':need(all(len(r['containing_event_facets'])==1 for r in rows),'ambiguous full-dimensional transition facet')
        need({f for row in rows if row['dimension']==2 for f in row['containing_event_facets']}==set(targetfaces),'limit does not cover every event facet')
        limits[chamber+'->'+event]=rows
    return {'status':'PASS','checked_utc':now(),'elapsed_seconds':time.monotonic()-begin,'source_concordance':{'vertices':18,'edges':21,'labels':42,'all_centered_vertices_midpoints_directions_cycles_match':True,'common_sphere_identity':'X^2+3*Ytilde^2+Z^2 = 1/3+x^2'},'domains':output,'endpoints':endpoint_output,'candidate':candidate,'limits':limits,'accounting':{'new_nominal_evaluations':3,'residual_sign_checks':residual_counts,'polygon_side_checks':polygon_tests,'distinct_monic_sign_forms_by_domain':len(sign_forms),'historical_enumerations_replayed':0},'trust_basis':'Python integer/Fraction arithmetic; explicit ordered Q(sqrt(2)); Euclidean polynomial division and Sturm variation. SymPy parses exact source expressions. Generator/checker share this arithmetic engine; their geometry and decisive verification organization are separate, not two independent arithmetic implementations.','proof_assistant_verification':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',type=Path,default=D/'exact_certificate.json');ap.add_argument('--output',type=Path,default=D/'CHECKER_RESULT.json');args=ap.parse_args()
    result=check(read(args.certificate));result['certificate_sha256']=sha(args.certificate.read_bytes());write(args.output,result);print('PASS: complete exact A-B certificate; no saved flags trusted.')
