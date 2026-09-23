"""Bounded checks of new manuscript expansions and exact figure inputs.

Does not import project kernels or rerun the preserved 31/42-predicate suites.
Writes only evidence/manuscript_checks.json; stdout is captured by the caller.
"""
import runtime
from runtime import ROOT
from geometry_coordinates import *
import json,hashlib
checks=[]
def zero(v):return all(S.simplify(x)==0 for x in v) if isinstance(v,S.MatrixBase) else S.simplify(v)==0
def check(name,condition,scope):
    ok=bool(condition);checks.append({'name':name,'pass':ok,'scope':scope});print(('PASS ' if ok else 'FAIL ')+name)
s,gap=S.symbols('s gap',positive=True);d=scaffold(s,gap)
# New support-line exposition, not a re-execution of the accepted theorem suite.
n=S.Matrix([[S.Rational(1,2),-r3/2],[r3/2,S.Rational(1,2)]])*U[0]
check('connector_support_distance',zero(n.dot(d['B'][0])-(2*s+gap)/(2*r3)),'Equation 13 derivation')
check('incircle_distance_difference',zero(d['p']-(2*s+gap)/(2*r3)-(gap-s)/(2*r3)),'Equation 13 regularity qualification')
W=s+2*gap;threshold=1-gap/W
check('barycentric_cut_threshold',zero(threshold-S.Rational(1,2)-s/(2*W)),'Proposition 4 strict disjointness proof')
check('corner_endpoint_barycentric_coordinates',zero(d['B'][0]-threshold*d['V'][0]-(gap/W)*d['V'][2]) and zero(d['A'][1]-threshold*d['V'][0]-(gap/W)*d['V'][1]),'Proposition 4 new global nonoverlap proof')
# All three Figure 9 panels start from width-one data and have equal plot scales.
s0=r2-1;a0=S.Rational(1,2);p0=a0/r3;lam=(1+r2)/3;sp=S.Rational(1,3);ap=(1+r2)/6
check('shrink_width_one_side',zero(lam*s0-sp),'New detailed width-one example / Figure 9')
check('shrink_top_height',zero(metrics(sp)[0]-ap) and ap<a0,'Changed top height in Figure 9')
check('fixed_centres_in_shrink_diagram',all(zero(sum(vertical_frames(s0,p0)[i],S.zeros(3,1))/8-sum(vertical_frames(sp,p0)[i],S.zeros(3,1))/8) for i in range(3)),'Figure 9 actual finite-face vertices')
check('shrink_support_side',zero(2*r3*p0-1),'Worked support triangle remains side one')
check('shrink_hexagon_area',zero(3*r3*sp**2/2-r3/6),'New worked area')
check('shrink_panel_distance',zero(r3*p0-ap-(2-r2)/6),'New width-one finite-face separation')
check('translation_keeps_top_height',all(zero(max(v[2] for v in face)-a0) for face in vertical_frames(s0,r3*s0/2)),'Figure 9 translated panel heights')
check('all_shrunk_top_connector_heights',all(zero(max(v[2] for v in face)-ap) for face in vertical_frames(sp,p0)),'Figure 9 new top plane for every finite face')
manifest=json.loads((ROOT/'figures/figure_manifest.json').read_text())
assets=[]
for f in manifest['figures']:
    paths=[ROOT/'figures'/(f['id']+e) for e in ('.pdf','.svg','.png')]
    assets.append({'figure':f['id'],'pass':all(p.is_file() and p.stat().st_size>1000 for p in paths),'files':[{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]})
report={'attribution':'New Codex manuscript/figure verification, 2026-09-23; no historical run.','exact_predicates':checks,'exact_passed':sum(c['pass'] for c in checks),'exact_total':len(checks),'figure_asset_groups':assets,'accepted_31_suite_rerun':False,'prior_42_suite_rerun':False,'kernel_tests_rerun':False}
(ROOT/'evidence').mkdir(exist_ok=True);(ROOT/'evidence/manuscript_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(f"Exact manuscript/figure predicates: {report['exact_passed']}/{len(checks)}; asset groups: {sum(a['pass'] for a in assets)}/{len(assets)}")
if not all(c['pass'] for c in checks) or not all(a['pass'] for a in assets):raise SystemExit(1)
