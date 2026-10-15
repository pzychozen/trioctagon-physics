"""Aggregate the completed fixed pair/phase tables; never evaluates a new bound."""
import json,math
import numpy as np
from common import ROOT,write_csv
from bounds import FAMILIES
def stats(values,locs):
    valid=[(float(x),loc) for x,loc in zip(values,locs) if x is not None and math.isfinite(float(x))]
    vals=np.asarray([x[0] for x in valid],dtype=np.float64)
    out={'count':len(valid),'masked':len(values)-len(valid),'exact_zero':int(np.sum(vals==0))}
    if not valid:
        for key in ('min','p05','median','p95','max','mean','min_locator','p05_locator','median_locator','p95_locator','max_locator'):out[key]=None
        return out
    order=np.argsort(vals,kind='stable');sv=vals[order]
    for key,q in [('min',0),('p05',.05),('median',.5),('p95',.95),('max',1)]:
        pos=(len(sv)-1)*q;lo=int(math.floor(pos));hi=int(math.ceil(pos))
        out[key]=float(np.quantile(vals,q,method='linear'))
        out[key+'_locator']={'lower':valid[int(order[lo])][1],'upper':valid[int(order[hi])][1],'upper_weight':pos-lo}
    out['mean']=math.fsum(vals)/len(vals)
    return out
def loc(r):
    return {k:r[k] for k in ('pair_id','cycle_c','cycle_d','view','phase') if k in r}
def csv_stats(scope,family,metric,units,s):
    result={'scope':scope,'family':family,'metric':metric,'units':units,**s}
    return {k:json.dumps(v,separators=(',',':')) if isinstance(v,(dict,list)) else v for k,v in result.items()}
def summarize(pairrows,dispersion,center,outcomes):
    rows=[];summary={};factor_counts={};aggregate={}
    groups={'all_pairs':pairrows,'new_four_pairs':[r for r in pairrows if r['cycle_d']>0]}
    for c,d in [(1,0),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)]:
        groups[f'pair_{c}_{d}']=[r for r in pairrows if r['cycle_c']==c and r['cycle_d']==d]
    for scope,rs in groups.items():
        summary[scope]={};factor_counts[scope]={};locations=[loc(r) for r in rs]
        for f in FAMILIES:
            summary[scope][f]={}
            for metric,col,units in [('bound',f,'speed'),('outcome','observed_S','speed'),('gap',f+'_gap','speed'),
                                     ('utilization',f+'_utilization','dimensionless'),('factor',f+'_factor_over_outcome','dimensionless')]:
                s=stats([r[col] for r in rs],locations);summary[scope][f][metric]=s;rows.append(csv_stats(scope,f,metric,units,s))
            factors=[r[f+'_factor_over_outcome'] for r in rs if r[f+'_factor_valid']]
            factor_counts[scope][f]={'resolved':len(factors),'unresolved':len(rs)-len(factors),
                'outcome_exact_zero':sum(r['observed_S']==0 for r in rs),'bound_exact_zero':sum(r[f]==0 for r in rs),
                'utilization_unresolved':sum(not r[f+'_utilization_valid'] for r in rs),
                **{'within_factor_'+str(k):sum(x<=k for x in factors) for k in (2,5,10)}}
    conditions={}
    for view in ('all_five','new_four'):
        rs=[r for r in dispersion if r['view']==view];locations=[loc(r) for r in rs]
        summary[view]={};factor_counts[view]={}
        actual={key:math.sqrt(math.fsum(r[key+'_variance'] for r in rs)/len(rs)) for key in ('incoming','pre_damping','post')}
        aggregate[view]={'RMS_phase_SD':actual,'bounds':{}}
        conditions[view]={}
        for ref in ('incoming','pre_damping'):
            conditions[view][ref]={'sufficient':{label:sum(r[ref+'_condition_class']==label for r in rs) for label in ('PASS','NOT_ESTABLISHED','UNRESOLVED')},
                'actual':{label:sum(r[ref+'_actual_class']==label for r in rs) for label in ('PASS','NOT_ESTABLISHED','UNRESOLVED')},
                'condition_exact_zero':sum(r[ref+'_condition_margin']==0 for r in rs),
                'actual_exact_zero':sum(r[ref+'_actual_margin']==0 for r in rs),
                'condition_margin':stats([r[ref+'_condition_margin'] for r in rs],locations),
                'actual_margin':stats([r[ref+'_actual_margin'] for r in rs],locations)}
        for f in FAMILIES:
            summary[view][f]={};factor_counts[view][f]={}
            W=math.fsum(r[f+'_variance_upper'] for r in rs)/len(rs);E=math.sqrt(W)
            aggregate[view]['bounds'][f]={'mean_variance_upper':W,'RMS_phase_SD_upper':E,
                'SD_factor_over_observed':E/actual['post'] if actual['post']>=1e-12 else None,
                'SD_utilization':actual['post']/E if E>=1e-12 else None}
            for kind in ('variance','SD'):
                for metric,col,units in [('bound',f+'_'+kind+'_upper','speed_squared' if kind=='variance' else 'speed'),
                                         ('outcome','post_'+kind,'speed_squared' if kind=='variance' else 'speed'),
                                         ('gap',f+'_'+kind+'_gap','speed_squared' if kind=='variance' else 'speed'),
                                         ('utilization',f+'_'+kind+'_utilization','dimensionless'),
                                         ('factor',f+'_'+kind+'_factor','dimensionless')]:
                    s=stats([r[col] for r in rs],locations);summary[view][f][kind+'_'+metric]=s
                    rows.append(csv_stats(view,f,kind+'_'+metric,units,s))
                fs=[r[f+'_'+kind+'_factor'] for r in rs if r[f+'_'+kind+'_factor_valid']]
                factor_counts[view][f][kind]={'resolved':len(fs),'unresolved':len(rs)-len(fs),
                    'outcome_exact_zero':sum(r['post_'+kind]==0 for r in rs),
                    'bound_exact_zero':sum(r[f+'_'+kind+'_upper']==0 for r in rs),
                    'utilization_unresolved':sum(not r[f+'_'+kind+'_utilization_valid'] for r in rs),
                    **{'within_factor_'+str(k):sum(x<=k for x in fs) for k in (2,5,10)}}
    write_csv(ROOT/'analysis/bound_summary.csv',rows)
    slackrows=[];slacks={}
    metrics=['T_minus_Q','gap_Q_to_BEST','gap_BEST_to_Zstar','gap_Zstar_to_Tnorm','gap_Tnorm_to_S','gap_Q_to_S']
    metrics.extend(f+'_'+suffix for f in ('K_COMPONENT','P_PROFILE','BEST_PRE') for suffix in ('improvement','over_Q'))
    for scope,rs in groups.items():
        slacks[scope]={};locations=[loc(r) for r in rs]
        for metric in metrics:
            s=stats([r[metric] for r in rs],locations);slacks[scope][metric]=s
            slackrows.append(csv_stats(scope,'proof_slack',metric,'dimensionless' if metric.endswith('over_Q') else 'speed',s))
    centerloc=[{**loc(pairrows[i//8]),'center':i%8} for i in range(16000)]
    for metric,unit in [('difference_alignment','speed_squared'),('triangle_slack','speed'),('difference_cosine','dimensionless')]:
        s=stats(center[metric],centerloc);slacks['center_'+metric]=s;slackrows.append(csv_stats('all_center_pairs','alignment',metric,unit,s))
    write_csv(ROOT/'analysis/proof_slack_summary.csv',slackrows)
    phasecurves=[]
    for j in range(200):
        rs=[r for r in pairrows if r['phase']==j]
        r={'phase':j,'pair_families':10}
        for key in list(FAMILIES)+['observed_S']+metrics[:6]:
            r[key+'_mean']=math.fsum(x[key] for x in rs)/10
        phasecurves.append(r)
    write_csv(ROOT/'analysis/phase_bound_means.csv',phasecurves)
    rankings={}
    for metric in ('gap_Q_to_S','gap_BEST_to_Zstar','gap_Zstar_to_Tnorm','gap_Tnorm_to_S','BEST_PRE_factor_over_outcome'):
        valid=[r for r in pairrows if r[metric] is not None]
        rankings[metric]=[{**loc(r),'value':r[metric],'S':r['observed_S'],'Q':r['Q_VECTOR'],'K':r['K_COMPONENT'],
            'P':r['P_PROFILE'],'BEST':r['BEST_PRE']} for r in sorted(valid,key=lambda r:r[metric],reverse=True)[:5]]
    return {'summary':summary,'factor_categories':factor_counts,'aggregate':aggregate,'conditions':conditions,
        'proof_slack':slacks,'fixed_extreme_locators':rankings,'alignment_counts':{
            'negative':int(np.sum(center['difference_alignment']<0)),'zero':int(np.sum(center['difference_alignment']==0)),
            'positive':int(np.sum(center['difference_alignment']>0)),'cosine_unresolved':int(np.sum(~center['difference_cosine_valid']))},
        'refinement_winners':{'K_including_ties':sum(r['best_is_K'] for r in pairrows),
            'P_strict':sum(not r['best_is_K'] for r in pairrows),'exact_ties':sum(r['K_COMPONENT']==r['P_PROFILE'] for r in pairrows)},
        'signed_interval_contains_zero':{'count':int(center['contains_zero'].sum()),'total':int(center['contains_zero'].size)},
        'summary_conventions':{'quantiles':'linear','quantile_locators':'two bracketing observations and interpolation weight',
            'aggregate_SD':'sqrt(mean phase variance), not mean phase SD','no_ratio_or_gap_clipping':True,
            'speed_floor':1e-12,'variance_floor':1e-24,'factor_categories_descriptive_only':[2,5,10]}}

