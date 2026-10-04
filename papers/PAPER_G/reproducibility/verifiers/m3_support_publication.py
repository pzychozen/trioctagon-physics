"""Codex bounded certificate audit, reusing Claude's unchanged interval replay.

No new trajectory implementation. Extra predicates use exact Fraction endpoints.
The supplied script writes only to its new replay directory. The documentary
check labels in that replay remain historical verbatim text; corrected notation
and the coordinate-gap diagnostic are recorded separately here.
"""
from pathlib import Path
from fractions import Fraction as Q
import contextlib, hashlib, json, platform, runpy, sys

# Publication adaptation: explicit CLI inputs and external output directory.
ROOT=Path(sys.argv[1]).resolve()
REPLAY=ROOT
script=REPLAY/'m3_claude_review_v0_2.py'
argv0=list(sys.argv)
sys.argv=[str(script),str(REPLAY/'m2_recomputed.json'),str(REPLAY/'m3_nominal_seed.json'),'80']
with (REPLAY/'m3_interval.log').open('w',encoding='utf-8') as f, contextlib.redirect_stdout(f):
    ns=runpy.run_path(str(script),run_name='__main__')
sys.argv=argv0
LO,HI,frac,absup=[ns[n] for n in ('LO','HI','frac_t','absup')]
iv=ns['iv']; mp=ns['mp']
checks={}; values={}
def check(name, predicate):
    checks[name]=bool(predicate)
    print(('PASS ' if predicate else 'FAIL ')+name)
    assert predicate, name
def ends(x): return [str(LO(x)),str(HI(x))]
def display(x): return mp.nstr(mp.mpf(x.numerator)/x.denominator,25)
Up,Em,JJ,Kr=[ns[n] for n in ('Up','Um','JJ','Kr')]
r=[frac(x._mpf_) for x in ns['rb']]
c=[frac(x._mpf_) for x in ns['zplus']]
check('supplied_28_verdicts_pass', len(ns['R']['checks'])==28 and all(ns['R']['checks'].values()))
check('exact_positive_parameters_basis_denominators', LO(ns['eps'])>0 and LO(ns['g'])>0 and LO(ns['mu'])>0 and LO(ns['a12'])>0 and LO(ns['nr'])>0 and LO(ns['m1_iv'])>0 and LO(ns['disc'])>0 and all(LO(x)>0 for x in ns['u_iv']))
check('fixed_host_in_strict_M2_box', all(LO(ns['Xbox'][i])<LO(ns['u_iv'][i])<=HI(ns['u_iv'][i])<HI(ns['Xbox'][i]) for i in range(3)))
check('all_301_recenterings_checked', ns['MV_COUNT']['steps']==301 and ns['MV_COUNT']['centre_in_box'])
check('chosen_centers_and_positive_weights_valid', all(LO(Up[i])<c[i]<HI(Up[i]) and r[i]>0 for i in range(5)))
check('exact_direct_X301_strict_entry', all(LO(Up[i])<LO(ns['q301'][i])<=HI(ns['q301'][i])<HI(Up[i]) for i in range(5)))
check('exact_alternative_X300_in_HUp', all(LO(ns['HUp'][i])<LO(ns['qbox'][i])<=HI(ns['qbox'][i])<HI(ns['HUp'][i]) for i in range(5)))
check('exact_F2_image_strict_self_inclusion', all(LO(Up[i])<LO(ns['Zw'][i])<=HI(ns['Zw'][i])<HI(Up[i]) for i in range(5)))
qrows=[sum(absup(JJ[i][j])*r[j] for j in range(5))/r[i] for i in range(5)]
check('outward_public_q_bound_0_9578', max(qrows)<Q('0.9578')<1)
# This is diagnostic only: an outer image that fails containment is not an escape.
check('old_outer_enclosure_does_not_certify_next_inclusion', not ns['box_level'])
gaps=[max(LO(Em[i])-HI(Up[i]),LO(Up[i])-HI(Em[i])) for i in range(5)]
check('disjoint_period_two_coordinate_5', gaps[4]>Q('0.87') and ns['disj'])
values['corrected_largest_separating_coordinate_gap']=dict(exact=str(max(gaps)),display=display(max(gaps)),one_based_coordinate=gaps.index(max(gaps))+1)
values['old_mislabelled_gap_display']=ns['R']['values']['G: separation between U_plus and U_minus (largest coordinate gap)']

# Validate the chosen approximate inverse as a fixed matrix.  It need not be
# the exact inverse. ||I-Y(DG-I)||_r<1 proves nonsingularity and contraction
# of the residual fixed-point operator; Kr gives strict self-inclusion.
Y=ns['Y']; Yi=ns['Yiv']; DG=ns['DG']
check('preconditioner_intervals_contain_fixed_dyadics', all(LO(Yi[i][j])<=frac(Y[i,j]._mpf_)<=HI(Yi[i][j]) for i in range(5) for j in range(5)))
E=[[iv.mpf(int(i==j))-sum((Yi[i][l]*(DG[l][j]-iv.mpf(int(l==j))) for l in range(5)),iv.mpf(0)) for j in range(5)] for i in range(5)]
erows=[sum(absup(E[i][j])*r[j] for j in range(5))/r[i] for i in range(5)]
check('preconditioner_nonsingular_by_interval_defect_norm', max(erows)<1)
check('H_equation_Krawczyk_strict_interior', all(LO(Up[i])<LO(Kr[i])<=HI(Kr[i])<HI(Up[i]) for i in range(5)))
values['Krawczyk_defect_weighted_norm']=dict(exact=str(max(erows)),display=display(max(erows)))

# Residual centre values are enclosures; approximate centers are legitimate
# choices. The slice and phase denominators must be valid in the whole boxes.
q_ad=ns['q_ad']
Fcenter=[x.v for x in q_ad(ns['c_pt'])]
F2center=[x.v for x in q_ad(Fcenter)]
check('interval_F2_center_recomputed_identically', all(ends(F2center[i])==ends(ns['F2c'][i]) for i in range(5)))
slice_lower=[]
for bx in (Up,Em,ns['HUp']):
    slice_dot=sum((ns['u_iv'][i]*(ns['u_iv'][i]+bx[i]) for i in range(3)),iv.mpf(0))
    slice_lower.append(LO(slice_dot))
check('representative_positive_slice_on_trap_and_image', min(slice_lower)>0)
check('all_recorded_chart_and_gauge_lower_bounds_positive', ns['full_log']['min_radius_lo']>0 and LO(ns['dr']*ns['dr']+ns['di']*ns['di'])>0 and all(ns['saved'][k]>0 and ns['qlog'][k]>0 for k in ('pr_lo','gauge_lo','rad_lo')))
check('parity_phase_bounds_nonzero_opposite', LO(ns['th_p'])>Q('0.058') and HI(ns['th_p'])<Q('0.06') and HI(ns['th_hp'])<0 and LO(ns['th_p']+ns['th_hp'])<=0<=HI(ns['th_p']+ns['th_hp']))

# Observable ranges over the trapping box, using the existing definition.
x=[ns['u_iv'][i]+Up[i] for i in range(3)]
y=[Up[3]*ns['v1_iv'][i]+Up[4]*ns['v2_iv'][i] for i in range(3)]
C=[x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
Gamma=sum(C,iv.mpf(0)); W=[-C[0]/2+C[1]-C[2]/2,iv.sqrt(iv.mpf(3))*(C[2]-C[0])/2,iv.mpf(0)]
check('W_and_Gamma_nonzero_on_Uplus', LO(W[0])>0 and LO(W[1])>0 and HI(Gamma)<0)
values['observables_Uplus']=dict(W=[ends(a) for a in W],Gamma=ends(Gamma),display_W=[[display(LO(a)),display(HI(a))] for a in W],display_Gamma=[display(LO(Gamma)),display(HI(Gamma))])

# A small adversarial endpoint witness, no random or parameter scan.
third=iv.mpf(1)/3
parts=str(third)[1:-1].split(',')
parsed=[frac(mp.mpf(s)._mpf_) for s in parts]
check('old_string_endpoint_policy_has_inward_witness', parsed[0]>LO(third) or parsed[1]<HI(third))
values['string_endpoint_witness']=dict(exact=ends(third),parsed=[str(x) for x in parsed],lower_inward=parsed[0]>LO(third),upper_inward=parsed[1]<HI(third))

# Historical precision-record comparisons omitted: this is a fresh replay.
accepted=json.loads((ROOT/'m3_accepted_support.json').read_text())
check('recomputed_Up_equals_accepted_exact_box', [ends(x) for x in Up]==accepted['values']['exact_receipts']['Up'])
check('recomputed_weights_equal_accepted_weights', [str(x) for x in r]==accepted['values']['exact_receipts']['positive_weights'])
check('recomputed_X301_equals_accepted_receipt', [ends(x) for x in ns['q301']]==accepted['values']['exact_receipts']['q301'])

values['exact_receipts']={name:[ends(x) for x in ns[name]] for name in ('Up','Um','HUp','qbox','q301','Zw','Kr','F2c','u_iv','v1_iv','v2_iv')}
values['exact_receipts'].update(dict(lambda_c=ends(ns['lam_c_tight']),lambda_parameter=ends(ns['lam']),positive_weights=[str(x) for x in r],centers=[str(x) for x in c],weighted_row_bounds=[str(x) for x in qrows],max_q_display=display(max(qrows)),slice_lower_bounds=[str(x) for x in slice_lower],gauge_theta_Uplus=ends(ns['th_p']),gauge_theta_HUp=ends(ns['th_hp'])))
result=dict(kind='PAPER_G_M3_PUBLICATION_REPLAY',attribution='Supplied Claude interval engine replayed unchanged; new Codex exact predicates audit its proof dependencies. This is not a new independently implemented propagation.',checks=checks,summary=f'{sum(checks.values())}/{len(checks)}',values=values,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),replayed_script_sha256=ns['R']['script_sha256'],versions=dict(python=sys.version,mpmath=mp.__version__,platform=platform.platform(),interval_digits=iv.dps,point_digits=mp.mp.dps))
(ROOT/'codex_m3_support_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('SUMMARY',result['summary'])
