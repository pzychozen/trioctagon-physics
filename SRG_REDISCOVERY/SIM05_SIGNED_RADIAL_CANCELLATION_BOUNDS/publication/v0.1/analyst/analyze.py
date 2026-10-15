"""One fixed saved-profile pass, sealed before saved-outcome joins. No D/F or source reconstruction."""
from common import *
import numpy as np,traceback
from radial import evaluate,FAMILIES,variance_bounds,margin_class,ratio
from summarize import summarize
np.seterr(all='raise')
PAIRS=[(1,0),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)]
COUNTS={'represented_unique_updates':1000,'represented_unique_centers':8000,'primary_pair_phase_evaluations':0,
 'center_pairs':0,'component_pairs':0,'derivative_node_slots':0,'outcome_pair_phase_joins':0,'view_phase_summaries':0}
qa={};residuals={};access=[]
def progress(stage):update(ROOT/'evidence/PRIMARY_PROGRESS.json',{'utc':utc(),'stage':stage,'counts':COUNTS,'bytes':cap()})
def check(name,value,tol=1e-12,kind='equality',axes=None):
 a=np.asarray(value,dtype=np.float64);need(np.all(np.isfinite(a)),'nonfinite residual '+name)
 residuals[name]=a
 ix=lambda flat:list(np.unravel_index(int(flat),a.shape)) if a.shape else []
 qa[name]={'kind':kind,'tolerance':tol,'shape':list(a.shape),'axes':axes or [],'min_signed':float(np.min(a)),
  'min_index':[int(v) for v in ix(np.argmin(a))],'max_signed':float(np.max(a)),'max_index':[int(v) for v in ix(np.argmax(a))],
  'max_abs':float(np.max(np.abs(a))),'max_abs_index':[int(v) for v in ix(np.argmax(np.abs(a)))]}
 need(bool(np.all(np.abs(a)<=tol)) if kind=='equality' else bool(np.all(a<=tol)),'numerical QA failed '+name)
def rows_csv(path):
 with lp(path).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def pairkey(r):return (int(r['cycle_c']),int(r['cycle_d']),int(r['phase']))
def load_keyed_npz(path,fields,stage):
 access.append({'utc':utc(),'stage':stage,'file':str(path.relative_to(ROOT)),'fields':fields})
 with np.load(lp(path),allow_pickle=False) as z:data={k:z[k] for k in fields}
 for v in data.values():v.setflags(write=False)
 return data
def source_keys(data):
 n=len(data['pair__pair_id']);keys={};centers={}
 for row in range(n):
  c=int(data['pair__cycle_c'][row]);d=int(data['pair__cycle_d'][row]);j=int(data['pair__phase'][row]);key=(c,d,j)
  need(key not in keys and (c,d) in PAIRS and 0<=j<200,'pair key')
  need(int(data['pair__pair_id'][row])==PAIRS.index((c,d)),'pair_id schedule')
  need(int(data['pair__update_c'][row])==200*c+j and int(data['pair__update_d'][row])==200*d+j,'update schedule')
  keys[key]=row
 need(set(keys)=={(c,d,j) for c,d in PAIRS for j in range(200)},'complete pair keys')
 reverse={row:key for key,row in keys.items()}
 for row,(pr,i) in enumerate(zip(data['center__pair_phase_row'],data['center__center'])):
  need(int(pr) in reverse and 0<=int(i)<8,'center metadata')
  key=(*reverse[int(pr)],int(i));need(key not in centers,'duplicate center key');centers[key]=row
 need(len(centers)==16000 and all((*k,i) in centers for k in keys for i in range(8)),'center key coverage')
 return keys,centers
def arrays_from_rows(rows,prefix):return {prefix+k:np.asarray([r[k] for r in rows]) for k in rows[0]}
def addratios(row,f,actual,floor=1e-12):
 B=row[f];S=actual;row[f+'_gap']=B-S
 row[f+'_factor'],row[f+'_factor_valid']=ratio(B,S,floor)
 row[f+'_utilization'],row[f+'_utilization_valid']=ratio(S,B,floor)
def main():
 started=time.monotonic();preserved();progress('selected input loading')
 ids=load(ROOT/'evidence/INPUT_MAP.json');fields=ids['analytic_loaded_fields']
 data=load_keyed_npz(ROOT/'inputs/analysis/PRE_OUTPUT_BOUNDS.npz',fields,'allowed analytic inputs')
 pk,ck=source_keys(data)
 meta=rows_csv(ROOT/'inputs/analysis/selected_record_map.csv');need(len(meta)==8000,'represented source map count')
 sk={(int(r['dataset_id']),int(r['update_index']),int(r['center'])) for r in meta}
 need(sk=={(0 if c==0 else 2,200*c+j,i) for c in range(5) for j in range(200) for i in range(8)},'represented source coverage')
 pairrows=[];center_lists={};join=[];P_res=[]
 for pid,(c,d) in enumerate(PAIRS):
  for j in range(200):
   key=(c,d,j);src=pk[key];ix=np.array([ck[(*key,i)] for i in range(8)])
   p=data['center__profile_c'][ix];q=data['center__profile_d'][ix];P=data['center__P_center'][ix]
   center,row=evaluate(p,q,P);stored=float(data['pair__P_PROFILE'][src]);need(math.isfinite(stored) and stored>=0,'pair prior')
   P_res.append(row['P_PROFILE']-stored);row['P_PROFILE']=stored
   row={'pair_id':pid,'cycle_c':c,'cycle_d':d,'phase':j,'update_c':200*c+j,'update_d':200*d+j,**row}
   pairrows.append(row)
   for k,v in center.items():center_lists.setdefault(k,[]).append(v)
   for i,source_row in enumerate(ix):join.append({'pair_phase_row':len(pairrows)-1,'center':i,'cycle_c':c,'cycle_d':d,'phase':j,
      'input_pair_source_row':src,'input_center_source_row':int(source_row)})
   COUNTS['primary_pair_phase_evaluations']+=1;COUNTS['center_pairs']+=8;COUNTS['component_pairs']+=24;COUNTS['derivative_node_slots']+=120
   if len(pairrows)%100==0:progress('analytic fixed intervals')
 center={k:np.concatenate(v,axis=0) for k,v in center_lists.items()};del center_lists
 check('prior_center_mean_minus_pair',P_res,axes=['pair_phase_row'])
 check('stable_h_minus_direct_squares',center['h_residual'],axes=['center_pair_row','component'])
 check('theta_node_monotonicity',np.diff(center['theta_nodes'],axis=-1),kind='inequality',axes=['center_pair_row','component','node_gap'])
 get=lambda k:np.array([r[k] for r in pairrows])
 for J in (1,4):
  s=f'J{J}_'
  for a,b in [('numerator_lo','numerator_hi'),('raw_lo_original','raw_hi_original'),('effective_lo_original','effective_hi_original'),('lo','hi')]:
   check(s+a+'_minus_'+b,center[s+a]-center[s+b],kind='inequality',axes=['center_pair_row'])
  check(s+'effective_hi_minus_prior',center[s+'hi']-center['P_center'],kind='inequality',axes=['center_pair_row'])
  check(s+'minus_prior_minus_effective_lo',-center['P_center']-center[s+'lo'],kind='inequality',axes=['center_pair_row'])
  for variant in ('','raw_'):
   check(s+variant+'signed_minus_unsigned',get(s+variant+'signed_upper')-get(s+variant+'unsigned_upper'),kind='inequality',axes=['pair_phase_row'])
   for k in ('midpoint_identity_residual','unsigned_identity_residual','cancellation_identity_residual'):check(s+variant+k,get(s+variant+k),axes=['pair_phase_row'])
  check(s+'unsigned_minus_P',get(s+'unsigned_upper')-get('P_PROFILE'),kind='inequality',axes=['pair_phase_row'])
  check(s+'signed_lower_minus_upper',get(s+'signed_lower')-get(s+'signed_upper'),kind='inequality',axes=['pair_phase_row'])
 for variant in ('','raw_'):
  check(variant+'nesting_lower',center['J1_'+variant+'lo']-center['J4_'+variant+'lo'],kind='inequality',axes=['center_pair_row'])
  check(variant+'nesting_upper',center['J4_'+variant+'hi']-center['J1_'+variant+'hi'],kind='inequality',axes=['center_pair_row'])
 for kind in ('signed','unsigned'):check(kind+'_J4_minus_J1',get('J4_'+kind+'_upper')-get('J1_'+kind+'_upper'),kind='inequality',axes=['pair_phase_row'])
 check('lower_J1_minus_J4',get('J1_signed_lower')-get('J4_signed_lower'),kind='inequality',axes=['pair_phase_row'])
 viewrows=[]
 for view,cycles in [('all_five',list(range(5))),('new_four',list(range(1,5)))]:
  for j in range(200):
   rs=[r for r in pairrows if r['phase']==j and r['cycle_c'] in cycles and r['cycle_d'] in cycles]
   need(len(rs)==(10 if view=='all_five' else 6),'view pair count')
   row={'view':view,'phase':j,'cycles':len(cycles),'pairs':len(rs),**variance_bounds(rs,len(cycles))}
   # Give raw families the same suffix convention as primary families.
   for J in (1,4):
    for kind in ('signed','unsigned'):row[f'J{J}_raw_{kind}_upper_variance_upper']=row.pop(f'J{J}_raw_{kind}_variance_upper')
   viewrows.append(row);COUNTS['view_phase_summaries']+=1
 # Seal ALL center, pair and population analytic arrays before any numerical outcome read.
 pre={**{'center__'+k:v for k,v in center.items()},**arrays_from_rows(pairrows,'pair__'),**arrays_from_rows(viewrows,'view__')}
 pre['center__pair_phase_row']=np.repeat(np.arange(2000),8);pre['center__center']=np.tile(np.arange(8),2000)
 npzsave(ROOT/'analysis/PRE_OUTPUT_INTERVALS.npz',pre)
 seal={'status':'SEALED_BEFORE_OUTCOMES','utc':utc(),'identity':ident(ROOT/'analysis/PRE_OUTPUT_INTERVALS.npz'),
  'counts':dict(COUNTS),'allowed_fields':fields,'outcome_fields_loaded':[],'pure_code':ident(ROOT/'analyst/radial.py')}
 save(ROOT/'analysis/PRE_OUTPUT_INTERVALS_SEAL.json',seal);progress('analytic seal complete')
 outcome_keys=[k for k in fields if k.startswith('pair__') and k!='pair__P_PROFILE']+['center__pair_phase_row','center__center']
 od=load_keyed_npz(ROOT/'inputs/analysis/center_pair_bounds.npz',outcome_keys+ids['outcome_loaded_fields_after_seal'],'post-seal outcomes')
 op,oc=source_keys(od);delta=[];absdelta=[]
 for r in join:
  key=(r['cycle_c'],r['cycle_d'],r['phase'],r['center']);src=oc[key]
  r['outcome_center_source_row']=src
  delta.append(od['outcome__signed_speed_difference'][src]);absdelta.append(od['outcome__individual_abs_speed_difference'][src])
 delta=np.asarray(delta);absdelta=np.asarray(absdelta);need(np.all(np.isfinite(delta)) and np.all(np.isfinite(absdelta)),'nonfinite saved difference')
 check('saved_absolute_difference',absdelta-np.abs(delta),axes=['center_pair_row'])
 refs=rows_csv(ROOT/'inputs/analysis/pair_phase_bounds.csv');refmap={pairkey(r):r for r in refs};need(set(refmap)==set(pk) and len(refs)==2000,'reference pair keys')
 rawfamilies=tuple(f'J{J}_raw_{kind}_upper' for J in (1,4) for kind in ('unsigned','signed'))
 for n,row in enumerate(pairrows):
  ds=delta[8*n:8*n+8];signed=math.fsum(ds)/8;S=abs(signed);ref=refmap[pairkey(row)]
  row.update(signed_collective_difference=signed,observed_S=S,accepted_signed_collective_difference=float(ref['signed_collective_difference']),
    collective_reduction_residual=signed-float(ref['signed_collective_difference']),prior_reference_residual=row['P_PROFILE']-float(ref['P_PROFILE']),
    observed_Tnorm=math.fsum(absdelta[8*n:8*n+8])/8)
  for f in (*FAMILIES,*rawfamilies):addratios(row,f,S)
  for J in (1,4):row[f'J{J}_radius_minus_remaining_slack']=row[f'J{J}_mean_radius']-(row[f'RADIAL_{J}_SIGNED']-S)
  row.update(gap_P_to_unsigned4=row['P_PROFILE']-row['RADIAL_4_UNSIGNED'],gap_unsigned4_to_signed4=row['RADIAL_4_UNSIGNED']-row['RADIAL_4_SIGNED'],
   gap_signed4_to_S=row['RADIAL_4_SIGNED']-S,gap_P_to_S=row['P_PROFILE']-S,
   refinement_signed_J1_to_J4=row['RADIAL_1_SIGNED']-row['RADIAL_4_SIGNED'],refinement_unsigned_J1_to_J4=row['RADIAL_1_UNSIGNED']-row['RADIAL_4_UNSIGNED'])
  row['gap_telescope_residual']=row['gap_P_to_S']-(row['gap_P_to_unsigned4']+row['gap_unsigned4_to_signed4']+row['gap_signed4_to_S'])
  COUNTS['outcome_pair_phase_joins']+=1
 check('collective_reduction_order',get('collective_reduction_residual'),axes=['pair_phase_row'])
 check('prior_reference_identity',get('prior_reference_residual'),axes=['pair_phase_row'])
 for J in (1,4):
  s=f'J{J}_'
  for variant in ('','raw_'):
   check(s+variant+'center_lower_minus_outcome',center[s+variant+'lo']-delta,kind='inequality',axes=['center_pair_row'])
   check(s+variant+'outcome_minus_center_upper',delta-center[s+variant+'hi'],kind='inequality',axes=['center_pair_row'])
   check(s+variant+'collective_lower_minus_outcome',get(s+variant+'lo')-get('signed_collective_difference'),kind='inequality',axes=['pair_phase_row'])
   check(s+variant+'outcome_minus_collective_upper',get('signed_collective_difference')-get(s+variant+'hi'),kind='inequality',axes=['pair_phase_row'])
  check(s+'absolute_lower_minus_S',get(s+'signed_lower')-get('observed_S'),kind='inequality',axes=['pair_phase_row'])
 for f in (*FAMILIES,*rawfamilies):check('S_minus_'+f,get('observed_S')-get(f),kind='inequality',axes=['pair_phase_row'])
 for k in ('gap_P_to_unsigned4','gap_unsigned4_to_signed4','gap_signed4_to_S'):check('negative_'+k,-get(k),kind='inequality',axes=['pair_phase_row'])
 check('gap_telescope',get('gap_telescope_residual'),axes=['pair_phase_row'])
 access.append({'utc':utc(),'stage':'post-seal scalar references','files':['cycle_phase_speeds.csv','pair_phase_bounds.csv','phase_dispersion_bounds.csv']})
 speeds=rows_csv(ROOT/'inputs/analysis/cycle_phase_speeds.csv');sm={(int(r['cycle']),int(r['phase'])):r for r in speeds}
 need(len(speeds)==1000 and set(sm)=={(c,j) for c in range(5) for j in range(200)},'speed reference keys')
 oldviews=rows_csv(ROOT/'inputs/analysis/phase_dispersion_bounds.csv');vm={(r['view'],int(r['phase'])):r for r in oldviews}
 need(len(oldviews)==400 and len(vm)==400,'view reference keys')
 for row in viewrows:
  view=row['view'];j=row['phase'];cycles=list(range(5)) if view=='all_five' else list(range(1,5));m=len(cycles);ref=vm[(view,j)]
  for stage in ('incoming','pre_damping','post'):
   vals={c:float(sm[(c,j)][stage]) for c in cycles};need(all(math.isfinite(v) for v in vals.values()),'nonfinite reference speed')
   mu=math.fsum(vals.values())/m;var=math.fsum((v-mu)**2 for v in vals.values())/m
   pv=math.fsum((vals[c]-vals[d])**2 for c,d in PAIRS if c in cycles and d in cycles)/(m*m)
   row[stage+'_variance']=var;row[stage+'_SD']=math.sqrt(var);row[stage+'_pair_variance']=pv
   row[stage+'_pair_identity_residual']=pv-var;row[stage+'_reference_residual']=var-float(ref[stage+'_variance'])
  row['P_variance_reference_residual']=row['P_PROFILE_variance_upper']-float(ref['P_PROFILE_variance_upper'])
  for f in (*FAMILIES,*rawfamilies):
   row[f+'_SD_upper']=math.sqrt(row[f+'_variance_upper'])
   for kind,floor in [('variance',1e-24),('SD',1e-12)]:
    B=row[f+'_'+kind+'_upper'];S=row['post_'+kind]
    row[f+'_'+kind+'_gap']=B-S
    row[f+'_'+kind+'_factor'],row[f+'_'+kind+'_factor_valid']=ratio(B,S,floor)
    row[f+'_'+kind+'_utilization'],row[f+'_'+kind+'_utilization_valid']=ratio(S,B,floor)
  for refname in ('incoming','pre_damping'):
   actual=row[refname+'_variance']-row['post_variance'];row[refname+'_actual_margin']=actual
   row[refname+'_actual_class']='DECREASE' if actual>1e-14 else 'INCREASE' if actual< -1e-14 else 'UNRESOLVED'
   for J in (1,4):
    s=f'J{J}_';row[s+'SD_lower']=math.sqrt(row[s+'variance_lower'])
    for test,margin in [('decrease',row[refname+'_variance']-row[f'RADIAL_{J}_SIGNED_variance_upper']),('increase',row[s+'variance_lower']-row[refname+'_variance'])]:
     col=s+refname+'_'+test;row[col+'_margin']=margin;row[col+'_class']=margin_class(margin)
     need(not (row[col+'_class']=='PASS' and row[refname+'_actual_class']==('INCREASE' if test=='decrease' else 'DECREASE')),'certificate contradicts actual direction')
 vg=lambda k:np.array([r[k] for r in viewrows])
 for stage in ('incoming','pre_damping','post'):
  for suffix in ('pair_identity_residual','reference_residual'):check(stage+'_'+suffix,vg(stage+'_'+suffix),1e-14,axes=['view_phase_row'])
 check('P_variance_reference',vg('P_variance_reference_residual'),1e-14,axes=['view_phase_row'])
 for f in (*FAMILIES,*rawfamilies):check('post_variance_minus_'+f,vg('post_variance')-vg(f+'_variance_upper'),1e-14,'inequality',['view_phase_row'])
 for J in (1,4):check(f'J{J}_lower_variance_minus_post',vg(f'J{J}_variance_lower')-vg('post_variance'),1e-14,'inequality',['view_phase_row'])
 check('variance_upper_refinement',vg('RADIAL_4_SIGNED_variance_upper')-vg('RADIAL_1_SIGNED_variance_upper'),1e-14,'inequality',['view_phase_row'])
 check('variance_lower_refinement',vg('J1_variance_lower')-vg('J4_variance_lower'),1e-14,'inequality',['view_phase_row'])
 write_csv(ROOT/'analysis/join_map.csv',join);write_csv(ROOT/'analysis/pair_phase_intervals.csv',pairrows);write_csv(ROOT/'analysis/phase_dispersion_intervals.csv',viewrows)
 npzsave(ROOT/'analysis/center_intervals_and_outcomes.npz',{**{'center__'+k:v for k,v in center.items()},
   'center__pair_phase_row':np.repeat(np.arange(2000),8),'center__center':np.tile(np.arange(8),2000),
   'outcome__signed_speed_difference':delta,'outcome__individual_abs_speed_difference':absdelta})
 npzsave(ROOT/'analysis/NUMERICAL_RESIDUALS.npz',residuals)
 save(ROOT/'evidence/NUMERICAL_QA.json',{'status':'PASS','checks':qa,'counts':COUNTS,'relative_tolerance':0,'clipping':False,
 'locator_axes':'pair_phase_row and view_phase_row are CSV row indices; center_pair_row=8*pair_phase_row+center; components 0..2, nodes 0..4'})
 result=summarize(pairrows,viewrows,center)
 result.update(execution_counts=dict(COUNTS),pre_output_seal=seal,stage_seconds=time.monotonic()-started,source_D_or_F_evaluations=0,
   new_motion_updates=0,RNG_operations=0,source_reconstructions=0,numerical_check_arrays=len(qa))
 save(ROOT/'analysis/RESULTS.json',result)
 save(ROOT/'evidence/DATA_ACCESS_LOG.json',{'access':access,'outcome_join_after_seal':True,'raw_state_loads':0,'prior_engine_or_checker_runs':0})
 # Metadata only: enumerate saved schemas without rerunning any scientific calculation.
 schemas={'npz':{},'csv':{},'field_guide':'OUTPUT_FIELD_GUIDE.md'}
 for path in lp(ROOT/'analysis').glob('*.npz'):
  with zipfile.ZipFile(path) as z:
   fieldschema={}
   for n in z.namelist():
    with z.open(n) as f:
     ver=np.lib.format.read_magic(f);reader=np.lib.format.read_array_header_1_0 if ver==(1,0) else np.lib.format.read_array_header_2_0
     shape,order,dtype=reader(f);fieldschema[n[:-4]]={'shape':list(shape),'dtype':str(dtype)}
   schemas['npz'][path.name]=fieldschema
 for path in lp(ROOT/'analysis').glob('*.csv'):
  with path.open(encoding='utf-8',newline='') as f:
   rd=csv.reader(f);header=next(rd);n=sum(1 for _ in rd)
  schemas['csv'][path.name]={'columns':header,'rows':n}
 save(ROOT/'evidence/OUTPUT_SCHEMAS.json',schemas)
 need(COUNTS=={k:v for k,v in load(ROOT/'received/SIM05_EXPERIMENT_SPEC_v0.1.json')['counts'].items() if k not in ('fixture_groups','primary_attempts')},'final exact counts')
 preserved();progress('complete')
 save(ROOT/'evidence/PRIMARY_RESULT.json',{'status':'PASS','utc':utc(),'counts':COUNTS,'seconds':time.monotonic()-started,
 'numerical_check_arrays':len(qa),'bytes':cap(),'preservation':preserved()})
 print(json.dumps(load(ROOT/'evidence/PRIMARY_RESULT.json')))
if __name__=='__main__':
 try:main()
 except Exception as e:
  save(ROOT/'evidence/PRIMARY_FAILURE_DETAIL.json',{'status':'FAILED','utc':utc(),'counts':COUNTS,'exception':repr(e),'traceback':traceback.format_exc(),'checks_so_far':qa})
  if residuals and not lp(ROOT/'analysis/PARTIAL_RESIDUALS.npz').exists():npzsave(ROOT/'analysis/PARTIAL_RESIDUALS.npz',residuals)
  raise
