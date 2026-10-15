"""Summaries of the single completed interval pass; no bound re-evaluation."""
from common import ROOT,write_csv
from radial import FAMILIES
import numpy as np,math,json
def stats(values,locators):
 items=[(float(x),loc) for x,loc in zip(values,locators) if x is not None and math.isfinite(float(x))]
 out={'count':len(items),'masked':len(values)-len(items),'exact_zero':sum(x==0 for x,_ in items)}
 if not items:
  out.update({k:None for k in ('min','p05','median','p95','max','mean','min_locator','p05_locator','median_locator','p95_locator','max_locator')});return out
 a=np.array([x for x,_ in items]);order=np.argsort(a,kind='stable')
 for label,q in [('min',0),('p05',.05),('median',.5),('p95',.95),('max',1)]:
  z=(len(a)-1)*q;lo=math.floor(z);hi=math.ceil(z)
  out[label]=float(np.quantile(a,q,method='linear'))
  out[label+'_locator']={'lower':items[int(order[lo])][1],'upper':items[int(order[hi])][1],'upper_weight':z-lo}
 out['mean']=math.fsum(a)/len(a);return out
def loc(r):return {k:r[k] for k in ('pair_id','cycle_c','cycle_d','phase','view','center') if k in r}
def csv_stat(scope,family,metric,units,s):
 return {k:json.dumps(v,separators=(',',':')) if isinstance(v,(dict,list)) else v for k,v in {'scope':scope,'family':family,'metric':metric,'units':units,**s}.items()}
def categories(rows,bound,outcome,floor):
 resolved=[r for r in rows if r[outcome]>=floor]
 return {'resolved':len(resolved),'unresolved':len(rows)-len(resolved),'outcome_exact_zero':sum(r[outcome]==0 for r in rows),
 'bound_exact_zero':sum(r[bound]==0 for r in rows),'utilization_unresolved':sum(r[bound]<floor for r in rows),
 **{f'within_factor_{k}':sum(r[bound]<=k*r[outcome] for r in resolved) for k in (2,5,10)}}
def summarize(pairs,views,center):
 groups={'all_pairs':pairs,'new_four_pairs':[r for r in pairs if r['cycle_d']>0]}
 for c,d in [(1,0),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)]:groups[f'pair_{c}_{d}']=[r for r in pairs if r['cycle_c']==c and r['cycle_d']==d]
 summary={};cats={};boundrows=[];gaprows=[];gaps={};counts={};aggregate={};conditions={}
 rawfamilies=tuple(f'J{J}_raw_{kind}_upper' for J in (1,4) for kind in ('unsigned','signed'))
 metrics=['gap_P_to_unsigned4','gap_unsigned4_to_signed4','gap_signed4_to_S','gap_P_to_S',
 'refinement_signed_J1_to_J4','refinement_unsigned_J1_to_J4']
 for J in (1,4):metrics += [f'J{J}_'+s for s in ('mean_radius','raw_mean_radius','cancellation','midpoint','mean_abs_midpoint','signed_lower','raw_to_effective_unsigned','raw_to_effective_signed','radius_minus_remaining_slack')]
 for scope,rs in groups.items():
  ls=[loc(r) for r in rs];summary[scope]={};cats[scope]={};gaps[scope]={};counts[scope]={}
  for f in (*FAMILIES,*rawfamilies):
   summary[scope][f]={}
   for metric,col,unit in [('bound',f,'speed'),('gap',f+'_gap','speed'),('factor',f+'_factor','dimensionless'),('utilization',f+'_utilization','dimensionless')]:
    s=stats([r[col] for r in rs],ls);summary[scope][f][metric]=s;boundrows.append(csv_stat(scope,f,metric,unit,s))
   cats[scope][f]=categories(rs,f,'observed_S',1e-12)
  for k in metrics:
   s=stats([r[k] for r in rs],ls);gaps[scope][k]=s;gaprows.append(csv_stat(scope,'interval_diagnostics',k,'speed',s))
  for J in (1,4):
   pre=f'J{J}_';counts[scope][pre]={
    'mixed_resolved_center_signs':sum(r[pre+'mixed_resolved_signs'] for r in rs),
    'collective_positive':sum(r[pre+'collective_sign']==1 for r in rs),'collective_negative':sum(r[pre+'collective_sign']==-1 for r in rs),
    'collective_unresolved':sum(r[pre+'collective_sign']==0 for r in rs),
    'cancellation_positive_over_tolerance':sum(r[pre+'cancellation']>1e-12 for r in rs),
    'cancellation_exact_zero':sum(r[pre+'cancellation']==0 for r in rs),
    'unsigned_equals_P_exact':sum(r[f'RADIAL_{J}_UNSIGNED']==r['P_PROFILE'] for r in rs),
    'unsigned_equals_P_within_tolerance':sum(abs(r[f'RADIAL_{J}_UNSIGNED']-r['P_PROFILE'])<=1e-12 for r in rs),
    'signed_equals_P_exact':sum(r[f'RADIAL_{J}_SIGNED']==r['P_PROFILE'] for r in rs),
    'signed_equals_P_within_tolerance':sum(abs(r[f'RADIAL_{J}_SIGNED']-r['P_PROFILE'])<=1e-12 for r in rs),
    'prior_intersection_active_pairs':sum(r[pre+'prior_active_centers']>0 for r in rs),
    'roundoff_affected_pairs':sum(r[pre+'roundoff_centers']>0 for r in rs)}
  counts[scope]['refinement']={k:{'strict_over_tolerance':sum(r[k]>1e-12 for r in rs),'exact_zero':sum(r[k]==0 for r in rs)} for k in ('refinement_signed_J1_to_J4','refinement_unsigned_J1_to_J4')}
 for view in ('all_five','new_four'):
  rs=[r for r in views if r['view']==view];ls=[loc(r) for r in rs]
  summary[view]={};cats[view]={};conditions[view]={}
  aggregate[view]={'actual_RMS_phase_SD':{s:math.sqrt(math.fsum(r[s+'_variance'] for r in rs)/200) for s in ('incoming','pre_damping','post')},'bounds':{}}
  for f in (*FAMILIES,*rawfamilies):
   summary[view][f]={};cats[view][f]={}
   W=math.fsum(r[f+'_variance_upper'] for r in rs)/200;SD=math.sqrt(W);out=aggregate[view]['actual_RMS_phase_SD']['post']
   aggregate[view]['bounds'][f]={'mean_variance_upper':W,'RMS_phase_SD_upper':SD,'SD_factor':SD/out if out>=1e-12 else None}
   for kind,floor,unit in [('variance',1e-24,'speed_squared'),('SD',1e-12,'speed')]:
    for metric,col,u in [('bound',f+'_'+kind+'_upper',unit),('gap',f+'_'+kind+'_gap',unit),('factor',f+'_'+kind+'_factor','dimensionless'),('utilization',f+'_'+kind+'_utilization','dimensionless')]:
     s=stats([r[col] for r in rs],ls);summary[view][f][kind+'_'+metric]=s;boundrows.append(csv_stat(view,f,kind+'_'+metric,u,s))
    cats[view][f][kind]=categories(rs,f+'_'+kind+'_upper','post_'+kind,floor)
  for J in (1,4):
   pre=f'J{J}_';W=math.fsum(r[pre+'variance_lower'] for r in rs)/200
   aggregate[view][pre+'lower']={'mean_variance_lower':W,'RMS_phase_SD_lower':math.sqrt(W)}
   conditions[view][pre]={}
   for ref in ('incoming','pre_damping'):
    cc={}
    for test in ('decrease','increase'):
     key=pre+ref+'_'+test
     cc[test]={'counts':{label:sum(r[key+'_class']==label for r in rs) for label in ('PASS','NOT_ESTABLISHED','UNRESOLVED')},
      'exact_zero':sum(r[key+'_margin']==0 for r in rs),'margin':stats([r[key+'_margin'] for r in rs],ls),
      'PASS_phases':[r['phase'] for r in rs if r[key+'_class']=='PASS']}
    cc['actual']={label:sum(r[ref+'_actual_class']==label for r in rs) for label in ('DECREASE','INCREASE','UNRESOLVED')}
    conditions[view][pre][ref]=cc
 centerstats={}
 for J in (1,4):
  pre=f'J{J}_';s=center[pre+'sign'];centerstats[pre]={
   'positive':int(np.sum(s==1)),'negative':int(np.sum(s==-1)),'unresolved':int(np.sum(s==0)),
   'raw_hulls':int(np.sum(center[pre+'raw_hull_flag'])),'effective_hulls':int(np.sum(center[pre+'effective_hull_flag'])),
   'prior_active_lower':int(np.sum(center[pre+'P_active_lo'])),'prior_active_upper':int(np.sum(center[pre+'P_active_hi'])),
   'prior_active_either':int(np.sum(center[pre+'P_active_lo']|center[pre+'P_active_hi'])),
   'effective_unchanged_from_raw':int(np.sum((center[pre+'lo']==center[pre+'raw_lo'])&(center[pre+'hi']==center[pre+'raw_hi'])))}
 phase=[]
 for j in range(200):
  rs=[r for r in pairs if r['phase']==j];row={'phase':j,'pairs':10}
  for k in list(FAMILIES)+list(rawfamilies)+['observed_S']+metrics:row[k+'_mean']=math.fsum(r[k] for r in rs)/10
  phase.append(row)
 write_csv(ROOT/'analysis/bound_summary.csv',boundrows);write_csv(ROOT/'analysis/gap_summary.csv',gaprows);write_csv(ROOT/'analysis/phase_interval_means.csv',phase)
 extreme={k:[{**loc(r),'value':r[k],'S':r['observed_S'],'P':r['P_PROFILE'],'U4':r['RADIAL_4_UNSIGNED'],'B4':r['RADIAL_4_SIGNED']} for r in sorted((r for r in pairs if r[k] is not None),key=lambda r:r[k],reverse=True)[:5]] for k in ('gap_P_to_unsigned4','gap_unsigned4_to_signed4','gap_signed4_to_S','RADIAL_4_SIGNED_factor')}
 return {'summary':summary,'factor_categories':cats,'gaps':gaps,'counts':counts,'center_counts':centerstats,
 'aggregate':aggregate,'conditions':conditions,'fixed_extreme_locators':extreme,
 'conventions':{'quantiles':'linear','locators':'bracketing observations plus upper weight','aggregate_SD':'sqrt(mean phase variance)',
 'speed_ratio_floor':1e-12,'variance_ratio_floor':1e-24,'no_clipping':True,'factor_categories':'native-unit products, descriptive only'}}
