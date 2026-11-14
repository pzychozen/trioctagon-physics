"""Exact readouts of the already checked face list; presentation is separately labelled."""
from common import *
from geometry import *
from collections import Counter,defaultdict
import sympy as sp
cert=read(D/'exact_certificate.json');result=read(D/'CHECKER_RESULT.json');need_hash=sha((D/'exact_certificate.json').read_bytes());assert result['certificate_sha256']==need_hash and result['status']=='PASS'
sx=sp.Symbol('x')
def expr(p):return sum((sp.Rational(q.a.numerator,q.a.denominator)+sp.Rational(q.b.numerator,q.b.denominator)*sp.sqrt(2))*sx**i for i,q in enumerate(p))
def formula(p):return sp.sstr(sp.factor(expr(p),extension=sp.sqrt(2)))
def primitive(f,dom):
    entries=[*vload(f['normal_polynomials']),pload(f['offset_polynomial'])];g=()
    for p in entries:g=pgcd(g,p)
    sample=Q.load(dom['nomination_parameter']);positive_g=g if peval(g,sample).sign()>0 else pneg(g)
    if dom['kind']=='open':assert uniform_sign(positive_g,Q.load(dom['lower']),Q.load(dom['upper']))==1
    out=[]
    for p in entries:q,rem=pdiv(p,positive_g);assert not rem;out.append(q)
    first=next(p for p in out[:3] if p);lead=first[-1];scale=lead if lead.sign()>0 else -lead;return [pscale(p,1/scale) for p in out]
md=['# Exact supporting-plane orbit representatives','','These are readouts of the checked certificate, not new nominated faces. Coordinates are `X=physical_x/w`, `Y=physical_y/(sqrt(3)*w)`, `Z=physical_z/w`. Each row means `n_X X + n_Y Y + n_Z Z <= d`. Coefficients are exact over Q(sqrt(2)); polynomial formulas use the observation parameter x. The positive common-factor normalization preserves outward inequality direction throughout the stated domain. The full zero set equals the listed cycle. Apply the 12 coefficient-verified D3h actions in `exact_certificate.json` to recover every face; face IDs are local to each domain.','']
rep_records=[]
for dom in cert['domains']:
    md+=['## '+dom['id'],'','| Representative | Orbit size | Full zero-set cyclic order | n_X | n_Y | n_Z | d |','|---|---:|---|---|---|---|---|']
    for orbit in dom['D3h_face_orbits']:
        f=next(f for f in dom['faces'] if f['id']==orbit['representative']);ps=primitive(f,dom);forms=[formula(p) for p in ps]
        md.append('| '+f['id']+' | '+str(orbit['size'])+' | '+', '.join(f['cycle'])+' | '+' | '.join('`'+s+'`' for s in forms)+' |')
        rep_records.append({'domain':dom['id'],'representative':f['id'],'orbit_size':orbit['size'],'cycle':f['cycle'],'normal_polynomials':vdump(ps[:3]),'offset_polynomial':pdump(ps[3]),'display_formulas':forms})
    md+=['']
(D/'FACE_REPRESENTATIVES.md').write_text('\n'.join(md)+'\n',encoding='utf-8');write(D/'FACE_REPRESENTATIVES.json',{'certificate_sha256':need_hash,'records':rep_records,'coordinate_basis':cert['coordinate_basis']})
grouped=defaultdict(list)
for k,v in result['candidate']['residuals_at_transition_divided_by_sqrt3'].items():grouped[tuple(v)].append(k)
lines=['# Candidate supporting-plane residuals at x*','','All entries are `(n_* dot p - d_*)/sqrt(3)`. The Q(sqrt(2)) ordered-field sign test makes every nonzero row strictly negative. The zero row is complete.','','| Exact residual divided by sqrt(3) | Branch labels |','|---|---|']
for pair,labels in sorted(grouped.items(),key=lambda a:(Q.load(a[0]).sign(),a[0])):lines.append('| `'+formula(pc(Q.load(pair)))+'` | '+', '.join(labels)+' |')
(D/'CANDIDATE_RESIDUAL_TABLE.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
doms={d['id']:d for d in cert['domains']};transition=[]
for eventid in result['candidate']['D3h_orbit']['face_ids']:
    f=next(f for f in doms['T']['faces'] if f['id']==eventid);entry={'transition_face':eventid,'transition_cycle':f['cycle']}
    for chamber in ['C1','C2']:
        ids=[r['chamber_face'] for r in result['limits'][chamber+'->T'] if r['containing_event_facets']==[eventid]]
        entry[chamber]=[{'face_id':g['id'],'cycle':g['cycle'],'polygon_size':len(g['cycle'])} for g in doms[chamber]['faces'] if g['id'] in ids]
    assert sorted(r['polygon_size'] for r in entry['C1'])==[3,3,4] and sorted(r['polygon_size'] for r in entry['C2'])==[4,4]
    transition.append(entry)
edge_sets={k:{tuple(e['vertices']) for e in result['domains'][k]['edges']} for k in doms}
assert edge_sets['T']==edge_sets['C1']&edge_sets['C2']
common=set.intersection(*[{frozenset(f['labels']) for f in doms[k]['faces']} for k in doms]);assert len(common)==38
limits_summary={k:dict(Counter(row['dimension'] for row in rows)) for k,rows in result['limits'].items()}
readout={'certificate_sha256':need_hash,'six_local_changes':transition,'unchanged_full_facets_across_transition':38,'edges_at_event_are_intersection_of_chamber_edge_sets':True,'edges_lost_from_C1':sorted(edge_sets['C1']-edge_sets['T']),'edges_gained_in_C2':sorted(edge_sets['C2']-edge_sets['T']),'limit_image_dimension_histograms':limits_summary,'largest_facet_size_on_closed_A_B':6,'ten_vertex_maximal_facets':0,'scope':'Readout of the proved complete maximal-face lists, including inherited A/B endpoints. Does not classify selected sections/subsets/projections/other enclosures.'}
write(D/'TRANSITION_READOUT.json',readout)
write(D/'FACE_INCIDENCE_RECORDS.json',{'certificate_sha256':need_hash,'interior_domains':{k:{**{n:v for n,v in r.items() if n not in ['support_checks']},'faces':doms[k]['faces']} for k,r in result['domains'].items()},'endpoints':result['endpoints'],'limits':result['limits']})
print('Orbit representatives:',len(rep_records),'candidate residual classes:',len(grouped),'unchanged facets:',len(common),'lost/gained edges:',len(readout['edges_lost_from_C1']),len(readout['edges_gained_in_C2']))
print('Endpoint limit dimensions:',limits_summary)
print('Named local patch:',next(r for r in transition if r['transition_face']==result['candidate']['transition_facet_id']))
