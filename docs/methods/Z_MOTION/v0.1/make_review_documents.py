"""Create documentary indexes and provenance from retained files. No model imports."""
from pathlib import Path
from decimal import Decimal
import json,hashlib,re,zipfile,datetime
R=Path(__file__).resolve().parent
def read(f):return (R/f).read_text(encoding='utf-8')
def load(f):return json.loads(read(f),parse_float=Decimal)
def dump(f,x):(R/f).write_text(json.dumps(x,indent=2,ensure_ascii=False,default=str)+'\n',encoding='utf-8')
def write(f,s):(R/f).write_text(s.strip()+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def at(f,p):
 x=load(f)
 for k in p.strip('/').split('/'):
  k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
 return x
report={z:f'packet/reading/{z}/REPORT.md' for z in ['Z01','Z02','Z03']}
review={z:f'packet/reviews/NCM_Z_{z[-2:]}_GPT_REVIEW.md' for z in report}
obs='evidence/Z02/accepted_sources/observer.py';staged='evidence/Z01/source_snapshots/z.py'
dyn='evidence/Z03/sources/kernel_physics/dynamics.py';axial='evidence/Z03/sources/kernel_physics/axial_observables.py';diag='evidence/Z03/sources/kernel_physics/z_diagnostics.py'
paper='evidence/Z03/sources/papers/PAPER_G/v0.1.1/source/paper_g.tex'
g2='evidence/Z02/GAP_COMPARISON.json';o2='evidence/Z02/OBSERVATIONS.json';tr='evidence/Z02/TRANSITIONS.json'
ib='evidence/Z03/NATIVE_INTENSITY_BUDGET.json';fb='evidence/Z03/FROZEN_Z_SOURCE_BUDGET.json';rb='evidence/Z03/RADIAL_TRANSVERSE_ACCOUNTING.json';ss='evidence/Z03/STATE_SNAPSHOTS.json'
plan='packet/reading/Z02/ADMISSION_AND_PLAN.json';policy='packet/reading/Z03/NUMERIC_POLICY.json'
D='inherited definition or proved identity';E='previously reviewed elementary consequence';N='retained numerical result';I='source-grounded explanatory inference';U='unresolved interpretation'
claims=[]
def claim(n,title,classes,z,heading,defs=None,refs=None,reviewloc=None,limit=''):
 f=report[z];lines=read(f).splitlines();hits=[i for i,s in enumerate(lines,1) if s.lstrip('# ').startswith(heading)];assert len(hits)==1,(n,heading,hits)
 row={'id':f'C{n:02d}','claim':title,'evidence_classes':classes.split(';'),'source_id':z,'report':{'file':f,'heading':lines[hits[0]-1],'line':hits[0]},'definitions':defs or [],'ledger_references':refs or [],'scope':limit}
 if reviewloc:row['review']={'file':review[z],'locator':reviewloc}
 for d in row['definitions']:assert (R/d['file']).is_file()
 for d in row['ledger_references']:at(d['file'],d['pointer'])
 claims.append(row)
def definition(f,loc):return {'file':f,'locator':loc}
def ref(f,p):return {'file':f,'pointer':p}
def rr(f,p):return [ref(f,p)]
claim(1,'State, face vectors, staged readout and stationary measurement geometry',D+';'+I,'Z01','Typed map',[definition(obs,'decode, _placed, reference_geometry; lines 159-164, 199-239'),definition(staged,'state_norm, staged_scalar, macro_vector, observe_staged; lines 103-201')])
claim(2,'Frozen readout changes and native-source closure over all four spans',N+';'+I,'Z03','Finding',refs=[ref(fb,f'/runs/120/{i}/frozen/actual_displacement') for i in range(4)])
claim(3,'Author motivation, comparison lanes and absent physical identification',U+';'+I,'Z01','Limits, verdict',limit='Author intent is supplied by this work order section 5A and conversation; no fixed-support implementation or golden-ratio controller is claimed.')
claim(4,'Two distinct histories and five-state reuse; history table',N,'Z02','Admission before outcomes',refs=[ref(plan,'/selected'),ref(policy,'/native_exact'),ref('evidence/Z01/inputs/parent_run_record.json','/parameters')],limit='Full parameter tokens and row identities also in MANUAL_TABLE_PROVENANCE.json.')
claim(5,'Outcome-independent whole-window admission before opening results',N,'Z02','Admission before outcomes',refs=[ref(plan,'/window'),ref(plan,'/frozen_utc'),ref('evidence/Z02/ADMISSION_FREEZE_RECEIPT.json','/movement_calculations_started')])
claim(6,'Notation table, units and deliberate renamings',D+';'+I,'Z03','Inherited native identities',[definition(obs,'decode and _placed'),definition(axial,'_sa, _area, axial_source_budget')],limit='P is source prestage M; macro M remains macro M. Native map is ℱ, frozen point F_n, scheduled point S_n. S without index is pair matrix; Lp is placement, L native graph.')
claim(7,'I, kappa, C, K, E, H, M, Z and X equations',D,'Z01','Typed map',[definition(staged,'lines 103-201: state_norm through observe_staged'),definition(obs,'lines 177-204: _linear_place, _clock, _envelope_and_direction, _placed'),definition('evidence/Z03/sources/kernel_physics/readouts.py','z_chiral')])
claim(8,'Actual shared staged preset and clock equations',D+';'+N,'Z02','Definitions, fixed geometry',[definition(obs,'ObserverConfig lines 87-100 and _clock lines 184-189')],rr(plan,'/observer'))
claim(9,'Three fixed face vectors; raw C distinct from ambient W',D,'Z01','Typed map',[definition(obs,'TANGENTS and CENTER lines 20-28; decode lines 159-162'),definition(paper,'raw C, attached W and congruence definitions, lines 66-103')])
claim(10,'Fixed PLUS tau=0 geometry, original sphere, arcs versus patches',D+';'+N,'Z01','Six finite central opening boundaries',[definition('evidence/Z02/accepted_sources/central.tex','geometry and original sphere lines 181-224; boundaries lines 331-373'),definition('evidence/Z02/accepted_sources/host.tex','folded vertices lines 235-242, panels 283-285')],rr(plan,'/geometry'))
claim(11,'Frozen and scheduled are same-state comparisons; camera differs',D+';'+I,'Z02','Definitions, fixed geometry',[definition(obs,'_snapshot and _placed')])
claim(12,'Ordered native-envelope-clock telescope',D,'Z01','The ordered native',[definition(obs,'_attribute lines 262-276')],limit='Exact telescoping identity; mixed allocation depends on replacement order.')
claim(13,'Previous-scheduled interval-native term differs from global first freeze',D+';'+E,'Z02','Ordered attribution and the two freezes',[definition(obs,'_attribute and _snapshot')])
claim(14,'Same-index chiral cancellation and noncausal accounting',E,'Z02','Ordered attribution and the two freezes',reviewloc='Section 4.4, same-index observer difference')
claim(15,'Two-state radii, nearest labels and clock replacement clarification',N+';'+E,'Z01','Controlled comparisons',refs=rr('evidence/Z01/OBSERVATIONS.json','/samples'),reviewloc='Section 4, reviewer clarification using retained intermediate values only',limit='Exact numeric and label pointers in TABLE_PROVENANCE.json, table z01_points; one span has no successive chord angle.')
claim(16,'Five frozen labels and scheduled sequence; three clock-step switches',N,'Z02','Complete endpoint results',refs=[ref(g2,f'/evaluations/{m}{i}/gap/unique_winner') for m in ['F','S'] for i in range(5)],limit='Attribution in REPORT section Ordered attribution; TABLE_PROVENANCE contains radii.')
claim(17,'Discrete chord angles at the three middle indices',N,'Z02','Displacements and chord turns',refs=[ref(tr,f'/intervals/{i}/turn_at_middle_stored_index') for i in [1,2,3]],limit='No smooth path, period, velocity or acceleration inferred.')
claim(18,'Figure 1: unchanged top comparison with overlapping projected levels',N+';'+I,'Z02','Figures and QA',[definition('evidence/Z02/figures/01_top.png','Complete unchanged original; FIGURE_PROVENANCE.json entry 0')])
claim(19,'Nearest is not approaching: frozen 1 to 2 example',N+';'+I,'Z02','Every stored interval',refs=[ref(g2,f'/evaluations/F{i}/gap/best_distance') for i in [1,2]]+[ref(o2,f'/samples/{i}/frozen/spatial/radius') for i in [1,2]])
claim(20,'Figure 2: both sides, both levels and separate finite patches',N+';'+I,'Z02','Figures and QA',[definition('evidence/Z02/figures/02_opposite_sides.png','Complete unchanged original; FIGURE_PROVENANCE.json entry 1')])
claim(21,'Inside sphere; no point membership; F1 ray hits N+0 only',N+';'+U,'Z02','Complete endpoint results',refs=rr(g2,'/evaluations/F1/gap/host_notches'),limit='Z01 REPORT sections Six finite central opening boundaries and Finite host notch patches supply the separate two-state result. No aperture-passage interpretation.')
claim(22,'Common phase invariance of fixed staged Z and its measurements',E,'Z01','Two exact corollaries',[definition(staged,'state_norm, _observe, observe_staged')],reviewloc='Section 5, common-phase corollary',limit='Not an assertion for every observer or the whole native map; face arrows need not be invariant.')
claim(23,'Envelope cross-product identity and retained direction change',E+';'+N,'Z01','Two exact corollaries',reviewloc='Section 5, envelope-only direction',limit='Numeric example in REPORT Controlled comparisons; source equations staged_scalar and blend_vectors.')
claim(24,'EMA is phase-sensitive with cubic innovation and memory',D+';'+I,'Z01','Typed map',[definition(staged,'cubic_j, normalized_cubic, advance_ema, ema_scalar, observe_ema; lines 226-275')],limit='Read as text only; no EMA evaluation.')
claim(25,'Lipschitz sufficient margin and nonrigorous numerical allowance',E+';'+N,'Z02','Independently verified margin bound',refs=rr(plan,'/numeric'),limit='Triangle inequality proof retained; failed sufficient condition is inconclusive.')
claim(26,'Height-sign mirror-pair bound at tau=0',E,'Z02','Definitions, fixed geometry',[definition('evidence/Z02/accepted_sources/central.tex','mirror-related tau=0 boundary levels')],reviewloc='Section 4.1, upper/lower identity; exact paired squared-distance difference 4wt',limit='Requires h>0 and tau=0; not a same-level winner rule or nonzero-tau theorem.')
claim(27,'Sampled harmonic signs come from the declared observer clock',E,'Z02','Definitions, fixed geometry',refs=rr(plan,'/observer'),reviewloc='Section 4.2; cos(n*pi/2-3*lock)',limit='Full height also has beta*C_z; no native periodicity inferred.')
claim(28,'Simultaneous prestage and exact three-parent intensity identity',D,'Z03','Inherited native identities',[definition(dyn,'_advance lines 87-96'),definition(diag,'intensity_budget lines 256-287')])
claim(29,'Square children replace their parent; phase preserves modulus',D,'Z03','Inherited native identities',[definition(diag,'intensity_budget'),definition(dyn,'phase_sync')],reviewloc='Section 3.1')
claim(30,'Intensity table and saved-after residual distinct from API observed_delta',N+';'+D,'Z03','Inherited native identities',[definition(diag,'intensity_budget observed_delta and remainder')],refs=[ref(ib,f'/runs/120/{i}/intensity') for i in range(4)],limit='TABLE_PROVENANCE intensity entries point to each displayed scalar.')
claim(31,'S/A/C signs and conjugate-pair convention',D,'Z03','Inherited native identities',[definition(axial,'_sa and _area lines 158-178'),definition(paper,'Section 3, coherence/area convention')])
claim(32,'Congruence, polynomial cofactor and five amplitude terms',D,'Z03','Inherited native identities',[definition(axial,'axial_source_budget lines 220-269'),definition(paper,'Section 3, cofactor propagation')],reviewloc='Section 3.2; singular matrices require no inverse')
claim(33,'Source Arg0 kicks, zero bypass and normalized pair cube',D,'Z03','Inherited native identities',[definition(dyn,'arg0 and phase_sync lines 57-84')],reviewloc='Section 3.2',limit='No kick reconstruction in this documentation pass.')
claim(34,'Two entrywise phase-area terms; seven triples and R_C',D,'Z03','Inherited native identities',[definition(axial,'axial_source_budget'),definition(paper,'Section 3 phase-pair rotation, lines 123-145')],refs=rr('evidence/Z03/NATIVE_CHIRAL_BUDGET.json','/runs/120'),limit='Mixed prestage dependencies retained; not independent interventions or closed full dynamics.')
claim(35,'Finite gain identity including equal and both-zero cases',E,'Z03','Derived finite readout',reviewloc='Section 3.3',limit='Subtract rational gains; cancel no zero denominator; a=b>0 allowed, a=b=0 leaves q undefined.')
claim(36,'Signed intensity/chiral displacement pathways and separate residuals',E+';'+N,'Z03','Derived finite readout',refs=[ref(fb,f'/runs/120/{i}/frozen/model_to_data_residual_vector') for i in range(4)]+[ref(fb,f'/runs/120/{i}/frozen/readout_roundoff_residual') for i in range(4)],reviewloc='Section 3.3')
claim(37,'Frozen transverse, centered y and x-minus-z identities',E,'Z03','Derived finite readout',reviewloc='Section 3.3',limit='Z02 review section 4.3 is the prior observation. H nonzero; absolute X_y includes O_y; anchor dependent.')
claim(38,'Fine radial and ordinary-radius ledgers with residuals',E+';'+N,'Z03','Derived finite readout',refs=[ref(rb,f'/runs/120/{i}/radial_transverse') for i in range(4)],reviewloc='Section 3.4',limit='Ordinary-radius division only for nonzero sum of endpoint radii.')
claim(39,'Coarse radial identity and its separate endpoint table',E+';'+N,'Z03','Derived finite readout',refs=[ref(rb,f'/runs/120/{i}/radial_transverse/coarse_endpoint_difference') for i in range(4)],reviewloc='Section 3.4',limit='Cross term includes magnitude and alignment; no mixing fine and coarse allocations.')
claim(40,'223.9 cancellation ratio is decomposition dependent',N+';'+I,'Z03','2→3:',refs=rr(rb,'/runs/120/2/radial_transverse/radial_cancellation/sum_abs_over_abs_net'),reviewloc='Section 4, Middle balance')
for i,title in enumerate(['Large loss and essential finite square','Small x from opposing larger components','Increasing intensity and decreasing radius','Final outward radius with decreasing height']):
 claim(41+i,title,N+';'+I,'Z03',f'{i}→{i+1}:',refs=[ref(ib,f'/runs/120/{i}/intensity'),ref(fb,f'/runs/120/{i}/frozen'),ref(rb,f'/runs/120/{i}/radial_transverse')],limit='Each scalar shown in generated tables has its own pointer; prose uses rounded retained subfields. No source-budget reevaluation.')
claim(45,'Reviewer inference for positive later onsite terms',E,'Z03','Endpoints and all four',refs=[ref(ss,f'/runs/120/{i}/I') for i in [1,2,3]]+[ref(policy,'/native_exact')],reviewloc='Section 4, Additional explanatory inference from the retained values',limit='s_i <= I < 0.3 < min k_i=2 with epsilon>0. Nonnegative at a zero component; no long-term theorem.')
claim(46,'Figure 3: unchanged signed coarse radial balances',N,'Z03','Endpoints and all four',[definition('evidence/Z03/figures/03_radial_balance.png','Full original; FIGURE_PROVENANCE.json entry 2')],limit='Independent panel scales; index spans not calibrated time.')
claim(47,'Bounded explanation and unresolved physical interpretations',I+';'+U,'Z03','Verification, uncertainty',reviewloc='Section 5',limit='No force, flux, gravity, core orbit, support motion or duality mechanism established or rejected.')
claim(48,'Binary64 versus decimal semantics, screens and retained residuals',N,'Z03','Identity, source authority',refs=[ref(policy,'/screen'),ref('packet/reading/Z03/RESIDUAL_SUMMARY.json','/120/model_to_data_max_absolute_residual')],limit='Z01 REPORT Reproduction and numeric meaning; Z02 REPORT Definitions, fixed geometry and numerical meaning. Agreement is not interval certification.')
claim(49,'I/C agreement cannot certify every complex state component',E+';'+U,'Z03','Verification, uncertainty',reviewloc='Section 5, Consistency is not full-state certification',limit='Common-phase loss; no hidden phase trajectory recovered.')
claim(50,'Historical check counts, budget counts and Linux review scope',N,'Z03','Verification, uncertainty',refs=[ref('evidence/Z01/checks_results.json','/tests_run'),ref('evidence/Z02/checks_results.json','/tests_run'),ref('packet/reading/Z03/COUNTS.json','/primary_pair_budget_evaluations'),ref('packet/reading/Z03/COUNTS.json','/synthetic_full_pair_budgets')],reviewloc='Section 6; Z01 review section 6 and Z02 review section 5 for platform differences',limit='1851 and 80 are retained REPORT lines 128 and 130 outcomes, not current runs or independent experiment counts.')
claim(51,'Recommended documentation placement and stopping boundary',I,'Z03','Verification, uncertainty',reviewloc='Section 7',limit='Current work order sections 1 and 9 authorize consolidation only. Placement recommendation is documentary judgment, not publication acceptance.')
assert len(claims)==51
dump('CLAIM_SOURCE_MAP.json',claims)
parts=['# Claim-to-source map','All paths below resolve inside an extracted copy of this review package. Each report line is a locator in the unchanged file, not a new run. Evidence classes separate definitions, prior elementary deductions, retained numbers, explanatory inference and unresolved physical interpretation. Tables carry exact scalar pointers in [TABLE_PROVENANCE.json](manuscript/tables/TABLE_PROVENANCE.json); manual tables in [MANUAL_TABLE_PROVENANCE.json](manuscript/tables/MANUAL_TABLE_PROVENANCE.json).']
for c in claims:
 x=c['report'];s=f"## {c['id']}: {c['claim']}\n\nClass: {'; '.join(c['evidence_classes'])}. Source {c['source_id']}: [{x['heading'].lstrip('# ')}]({x['file']}), line {x['line']}."
 for d in c['definitions']:s+=f"\n\nDefinition: [{Path(d['file']).name}]({d['file']}), {d['locator']}."
 if 'review' in c:
  d=c['review'];s+=f"\n\nPrior review: [{Path(d['file']).name}]({d['file']}), {d['locator']}."
 for d in c['ledger_references']:s+=f"\n\nLedger: [{Path(d['file']).name}]({d['file']}), JSON pointer `{d['pointer']}`."
 if c['scope']:s+='\n\nScope: '+c['scope']
 parts.append(s)
parts.append('## Plain-language guide crosswalk\n\nGuide page 1: C01-C05, C10-C21. Guide page 2: C22-C24, C28-C49, C51. The guide adds no separate scientific claim or numerical evaluation.')
write('CLAIM_SOURCE_MAP.md','\n\n'.join(parts))

# Manual table cells: exact stored identities, not recomputed state observables.
manual=[]
def cell(table,row,column,f,p,display):manual.append({'table':table,'row':row,'column':column,'source_file':f,'json_pointer':p,'original_token':at(f,p),'display':display,'policy':'Retained identity/token; literal formatting or documented parameter notation only'})
parent='evidence/Z01/inputs/parent_run_record.json'
for k,s in [('eps','.05'),('g','.2'),('phase_strength','.001')]:cell('histories','Z01',k,parent,f'/parameters/{k}/f64',s)
for j in range(3):cell('histories','Z01',f'k[{j}]',parent,f'/parameters/k/{j}/f64','1')
for k in ['epsilon','g','lambda_phase','k']:cell('histories','Z02/Z03',k,policy,f'/native_exact/{k}',str(at(policy,f'/native_exact/{k}')))
for k in ['original_precision_dps','output_precision_significant_digits']:cell('histories','Z02/Z03',k,plan,f'/selected/source_lineage/{k}',str(at(plan,f'/selected/source_lineage/{k}')))
cell('histories','Z02/Z03','indices',policy,'/actual_indices','0, 1, 2, 3, 4')
for z in ['Z01','Z02']:cell('historical_verification',z,'assertions',f'evidence/{z}/checks_results.json','/tests_run',str(at(f'evidence/{z}/checks_results.json','/tests_run')))
for k in ['primary_pair_budget_evaluations','primary_precisions','synthetic_named_fixtures','synthetic_full_pair_budgets']:cell('historical_verification','Z03',k,'packet/reading/Z03/COUNTS.json','/'+k,str(at('packet/reading/Z03/COUNTS.json','/'+k)))
for value,needle in [('1,851','All 1,851 logged assertions passed'),('80','All 80 checks passed')]:
 lines=read(report['Z03']).splitlines();n=next(i for i,s in enumerate(lines,1) if needle in s)
 manual.append({'table':'historical_verification','row':'Z03','column':'retained check count','source_file':report['Z03'],'line':n,'original_token':value,'display':value,'policy':'Literal from retained report; not executed now'})
for z in ['Z01','Z02','Z03']:
 lines=read(review[z]).splitlines();n=next(i for i,s in enumerate(lines,1) if 'date:' in s.lower())
 manual.append({'table':'historical_verification','row':z,'column':'review date','source_file':review[z],'line':n,'original_token':lines[n-1],'policy':'Review date, not a claim about a second Windows certification'})
manual.append({'table':'notation','row':'all','source':'CLAIM_SOURCE_MAP.json C06-C10 and C28-C39','policy':'Definitions and deliberate symbol renamings; no extracted numerical results'})
dump('manuscript/tables/MANUAL_TABLE_PROVENANCE.json',manual)

# Portable inventory links; archives remain intact rather than recursively unpacked.
index=['# Evidence index','This package includes the three full original review archives, the three supplied GPT reviews and their evidence archives, plus 38 compact extracted copies. Historical scripts and work orders are inert evidence. Do not use their reproduction instructions for this documentation task.','## Reading route']
for z in report:
 index.append(f"- {z}: [report]({report[z]}), [prior GPT review]({review[z]}), [unchanged full review archive](packet/evidence/NCM_Z_{z[-2:]}_v0.1_REVIEW.zip).")
index+=['','[Source index supplied with the packet](packet/SOURCE_INDEX.json) records archive hashes, report headings and the reading-copy crosswalk. [Input verification](INPUT_VERIFICATION.json) records this pass\'s bounded integrity checks. [Extraction manifest](EXTRACTION_MANIFEST.json) records every extracted member and its hash.','## Compact extracted files']
for e in load('EXTRACTION_MANIFEST.json'):index.append(f"- [{e['extracted_path']}]({e['extracted_path']}) — archive member `{e['member']}` of [{Path(e['archive']).name}]({e['archive']}); SHA-256 `{e['sha256']}`.")
index+=['','## Evidence kept inside archives','The Z03 archive additionally retains `CHECKS.json`, `PRIMARY_EVALUATIONS.jsonl`, `PORTABLE_VERIFICATION.json`, `PASSIVE_PRESTAGES.json`, `SOURCES.json` and preservation records. These are **archive members**, not links to nonexistent extracted paths. The Z02 archive retains its source lineage and prior producer snapshots; Z01 retains its source audit. No archived program was imported or executed.','## Prior review evidence archives']
for p in sorted((R/'packet/reviews').glob('*.zip')):index.append(f'- [{p.name}]({p.relative_to(R).as_posix()}) — unchanged, not recursively extracted or run.')
index+=['','## Figures and tables','[Figure provenance](FIGURE_PROVENANCE.json) binds the three copied originals. [Numeric table provenance](manuscript/tables/TABLE_PROVENANCE.json) contains 83 stored cells; [manual-table provenance](manuscript/tables/MANUAL_TABLE_PROVENANCE.json) supplies history and inherited-verification identities. [Claim source map](CLAIM_SOURCE_MAP.md) supplies definitions, deductions and exact ledger row routes.','## Two histories','Z01: [two-state export](evidence/Z01/inputs/retained.motion.json), 27,068 bytes, SHA-256 `071f6f7dc74128d638b0e96e33897b1366b2f8bcb98ca741c11fe0af5ed0e1e7`.','Z02/Z03: [same five-state input](evidence/Z02/inputs/SELECTED_HISTORY.json), 8,871 bytes, SHA-256 `a294a4b0bf181adaa2054aa52379c1832a7833e3faa7614d0785aecd709ea09c`. Z03\'s corresponding archive member is `packet/NCM_Z_03_Packet_v0.1/inputs/SELECTED_HISTORY.json`; byte equality was checked.']
write('EVIDENCE_INDEX.md','\n\n'.join(index))
refs=['# Local reference register','All scientific references are supplied local evidence, not external peer-review claims. Nothing was fetched online. Canonical report titles are retained here; notation changes are declared in NOTE.md section 2.']
for z in report:refs.append(f"- {z}: [{read(report[z]).splitlines()[0].lstrip('# ')}](../{report[z]}). Prior internal review: [{read(review[z]).splitlines()[0].lstrip('# ')}](../{review[z]}).")
refs+=['','Source definitions and equation locators: [claim map](../CLAIM_SOURCE_MAP.md). Archive/member/byte route: [evidence index](../EVIDENCE_INDEX.md). Each editable display equation is recorded verbatim, with generated page and type size, in [EQUATION_TRANSCRIPTION.json](EQUATION_TRANSCRIPTION.json). This is a Matplotlib/mathtext PDF, not compiled LaTeX.']
write('manuscript/references.md','\n\n'.join(refs))
write('PLACEMENT_AND_CONTRIBUTION.md','''# Placement and contribution

Recommend adoption, after author/GPT review, as a project methods guide with the short companion alongside application help. The long note supplies definitions, observation controls, source accounting and provenance; the companion helps a reader interpret a displayed Z point. An explanatory appendix is an appropriate secondary placement when another manuscript needs these distinctions.

The contribution is the connected account of existing mathematics and two bounded historical examples. It preserves the difference between internal evolution, observer changes and fixed measuring geometry, and explains the four frozen displacements without adding a motion rule. The inherited budgets and elementary identities are not new fundamental laws. Reviewers' later deductions are explicitly labeled; none is advertised as external peer review.

A standalone physics publication is not the default recommendation. The examples do not demonstrate a material core trajectory, energy flux, gravity, a mechanical support or the wider dual arrangement. I/C agreement is not a full complex-state certificate; rounded histories and numeric screens are not interval proofs. These limitations do not prevent the completed explanatory note from being useful now.

This package is ready for documentation review. Placement remains a later editorial decision. No destination was edited, no paper was submitted or published, and no successor investigation is prescribed or started.
''')
write('CORRECTIONS_AND_DISPOSITION.md','''# Corrections and disposition

No material contradiction was found in the supplied accepted scientific baseline. No scientific input, equation coefficient, history, archive or original figure was repaired or changed.

1. Notation: native map ℱ versus frozen F_n; pair matrix S versus scheduled S_n; native prestage matrix P replaces the source symbol M so macro vector M stays unambiguous. Lp denotes placement while L remains the native graph. Centered r_y is distinguished from absolute X_y.
2. Terminology: the source API's finite-square "remainder" is an exact finite-step term. Its three children replace that parent. The coarse "cross alignment" includes size as well as alignment; fine and coarse radial accounts remain separate.
3. Reviewed additions: the Z01 clock-replacement label clarification, Z02 mirror-height and sampled-harmonic deductions, and Z03 later-onsite inference are attributed as reviewer consequences. They were checked by reading the given elementary arguments, not by executing scientific helpers.
4. Source differences already disposed in Z01: the historical whole-file current_records.py mismatch is retained as reported context; it is not treated as permission to repair the current application or replace the accepted source snapshot. No live checkout equivalence is assumed.
5. Build attempts: mathtext rejected LaTeX commands \\bmod and \\tfrac; equivalent \\mathrm{mod} and \\frac syntax was substituted. The missing pdftotext executable caused an initial document-only build attempt to stop; extraction is now explicitly optional. Available Poppler pdfinfo and pdftoppm provide page counts/renders, with source-based transcription checks and direct full-page visual review. No tools were installed.
6. Visual QA found literal norm pipes splitting the two-column Markdown notation table and dropping text. The canonical row now reads "Native squared norm I and norm κ=√I"; the exact norm equation remains on page 3. The builder now rejects inconsistent column counts. Final PDFs were rebuilt and every final page inspected.
7. One late read-only python -c inspection command failed on CMD quoting before executing its code. A new document-only inspection file was used instead. This affected no evidence.

Unresolved physical interpretations stay unresolved: no aperture passage, energy emission, gravity, core orbit or fixed-support/duality mechanism is inferred. No optional new scientific lane was opened. No blocker remains for documentary review; this is not publication acceptance or new certification of the underlying histories.
''')
write('START_HERE.md',f'''# Understanding Z Motion: review package

Z can move even while the observer and surrounding geometry are held fixed. In the five-state example it first moves inward and then outward; the existing intensity and chirality accounts explain all four changes. Changing the observer can change the placed point and its nearest-opening label as well. Distance from the center, height and native intensity are different quantities.

This is **NCM-Z-DOC-01 v0.1**, a complete documentation draft for GPT/author review, not publication acceptance.

## Read first

- [Two-page plain-language PDF](PLAIN_LANGUAGE_GUIDE_v0.1.pdf) and [editable guide](PLAIN_LANGUAGE_GUIDE.md).
- [18-page methods note PDF](manuscript/NCM_Z_DOCUMENTATION_v0.1.pdf) and [canonical Markdown](manuscript/NOTE.md).
- [Claim-to-source map](CLAIM_SOURCE_MAP.md), [evidence index](EVIDENCE_INDEX.md) and [reference register](manuscript/references.md).
- [Placement recommendation](PLACEMENT_AND_CONTRIBUTION.md), [corrections and dispositions](CORRECTIONS_AND_DISPOSITION.md).
- [Document QA](DOCUMENT_QA.json), [final PDF visual-review record](VISUAL_REVIEW.json), [build record](BUILD_RECORD.json), [closeout](CLOSEOUT.txt).

## Keep the histories separate

Z01 uses two saved states (0,1), with ε=.05, g=.2, phase=.001, k=(1,1,1) and preserved binary64 identities. Z02 uses five nominal saved states (0-4), with ε=1/10, g=1/5, phase=17/100, k=(2,3,4), from historical 120-digit working arithmetic. Z03 reuses that same five-state file. It is not a third history, continuation of Z01 or independent repeat. The selected five-state initialization was deliberately constructed; its full window was admitted before opening results.

The note preserves ordered attribution versus the global first-sample freeze, raw C versus W, points versus rays, finite central arcs versus separate notch patches, parent/child intensity hierarchy, seven chiral terms, fine versus coarse radial accounts and all residual/numerical limitations. Exact definitions and prior elementary consequences are distinguished from rounded retained numerical results.

## Scope and build

Actual new root: `{R}`. All new files, caches and renders are beneath it. The source checkout and earlier studies were not modified. Only the supplied ZIP and standalone work order form the bounded original-file before/after preservation set.

CMD activated the existing torment environment. PDF generation used installed Matplotlib PdfPages/mathtext, followed by existing Poppler rendering and full-page review. This is not a LaTeX compilation. No installation or online research occurred. See COMMANDS.txt and BUILD_RECORD.json for exact current-document operations. The editable build inputs are included; historical scripts inside the evidence archives are inactive and must not be replayed as part of this task.

The package includes unchanged source archives, compact readable evidence, tables with token/pointer provenance, and figures copied byte-for-byte. The output manifest excludes itself and the outside ZIP/receipt. Temporary page renders and caches remain local and are excluded from the ZIP; VISUAL_REVIEW.json binds their inspection to the final PDF hashes.

Zero new native, prestage, phase-kick, source-budget, observer or EMA evaluations; zero new states; no old scientific producer/checker replay, Git, application/kernel changes or publication. Recommend a project methods guide plus application-reading companion. No successor investigation starts here.
''')
# Current originals only: do not pretend to audit historical live paths.
before=load('SOURCE_MANIFEST_BEFORE.json');originals=[]
for e in before:
 p=Path(e['path']);after={'bytes':p.stat().st_size,'sha256':sha(p)};assert after['bytes']==e['bytes'] and after['sha256']==e['sha256']
 originals.append({'path':e['path'],'before':{'bytes':e['bytes'],'sha256':e['sha256']},'after':after,'unchanged':True})
copied=[{'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for folder in ['packet','evidence'] for p in sorted((R/folder).rglob('*')) if p.is_file()]
dump('SOURCE_MANIFEST.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'original_consulted_files':originals,'copied_inputs':copied,'scope':'Two original supplied files plus packaged copies. No live original paths behind older preservation records or whole-repository preservation audit claimed.'})
print(json.dumps({'claims':len(claims),'manual_table_records':len(manual),'copied_inputs':len(copied),'originals_rechecked_unchanged':len(originals)}))
