"""One bounded passive pass over 1,800 saved updates. Never evolves positions."""
from common import *
from algebra import budget
import numpy as np
import time, traceback

FLOATS=('r m t v2 w2 z2 impulse_norm I A L L_direct L_stable_minus_direct B C R R_stable '
        'R_stable_minus_direct cosine retention chi square_internal_residual square_direct_internal_residual '
        'speed_internal_residual speed_stable_internal_residual').split()
MASKS=('cosine_valid retention_valid chi_valid budget_zero_denominator damping_zero_denominator').split()
EXTRA=('H G source_time d_norm q q2 h impulse_factor_residual I_factor_residual post_norm post_squared '
       'square_saved_residual square_direct_saved_residual speed_saved_residual speed_stable_saved_residual').split()
VECTORS=['incoming_velocity','saved_successor_velocity','centroid','d','impulse','w','z','velocity_residual']
DTYPE=np.dtype([('record_id','i4'),('update_row','i4'),('dataset_id','i1'),('update_index','i4'),
    ('source_frame','i4'),('center','i1'),('block','i1'),('phase','i2'),('bit_minus','i1'),('bit_plus','i1'),
    ('bit_changed','?'),('H_sign','i1'),('complete','?')]+[(k,'f8') for k in FLOATS+EXTRA]+[(k,'?') for k in MASKS]+[(k,'f8',(3,)) for k in VECTORS])
PROGRESS={'updates_started':0,'updates_completed':0,'centers_started':0,'centers_completed':0,
          'primary_passes_started':0,'primary_passes_completed':0,'engine_calls':0,'rollout_updates':0,
          'initializations':0,'RNG_samples':0,'RNG_restorations':0,'old_checker_runs':0,'old_preflight_reanalyses':0}
LABELS=['PREFIX','CONTINUOUS','REPEATED']
FLOOR=1e-12
QA={}

def progress():
    save(ROOT/'evidence/PROGRESS.json',{**PROGRESS,'utc':utc()})
def fsum(a):return math.fsum(float(x) for x in a)
def mean(a):return fsum(a)/len(a)
def ratio(x,y):
    valid=abs(y)>=FLOOR
    return (float(x/y) if valid else None),valid
def null_float(x):return float(x) if math.isfinite(float(x)) else None
def describe(a):
    a=np.asarray(a,dtype=float);a=a[np.isfinite(a)]
    if not len(a):return {'count':0,'mean':None,'min':None,'p05':None,'p25':None,'p50':None,'p75':None,'p95':None,'max':None}
    qs=np.quantile(a,[.05,.25,.5,.75,.95],method='linear')
    return dict(count=len(a),mean=mean(a),min=float(a.min()),**dict(zip(['p05','p25','p50','p75','p95'],map(float,qs))),max=float(a.max()))
def locator(data,k):
    r=data[k];return {'dataset':LABELS[int(r['dataset_id'])],'update_index':int(r['update_index']),'center':int(r['center'])}
def check_center(data,key,tol=1e-12):
    a=np.asarray(data[key]);need(np.isfinite(a).all(),'nonfinite residual '+key)
    flat=int(np.argmax(np.abs(a)));loc=np.unravel_index(flat,a.shape)
    record={'max_abs_residual':float(np.max(np.abs(a))),'signed_at_max':float(a[loc]),'locator':locator(data,loc[0]),'tolerance':tol}
    if len(loc)>1:record['locator']['component']=int(loc[1])
    QA[key]=record;need(record['max_abs_residual']<=tol,'QA residual '+key+' '+str(record))
def check_update(rows,key,tol=1e-12):
    a=np.array([r[key] for r in rows]);need(np.isfinite(a).all(),'nonfinite update residual '+key)
    k=int(np.argmax(abs(a)));QA[key]={'max_abs_residual':float(abs(a[k])),'signed_at_max':float(a[k]),
        'locator':{x:rows[k][x] for x in ('dataset','update_index')},'tolerance':tol}
    need(abs(a[k])<=tol,'QA update residual '+key)
def bound(data,key,lo,hi,valid=None):
    a=np.asarray(data[key]);mask=np.ones(len(a),bool) if valid is None else np.asarray(data[valid])
    need(np.isfinite(a[mask]).all(),'nonfinite diagnostic '+key)
    if not mask.any():
        QA[key+'_bounds']={'valid':0,'undefined':len(a),'min':None,'max':None};return
    inds=np.flatnonzero(mask);amin=int(inds[np.argmin(a[mask])]);amax=int(inds[np.argmax(a[mask])])
    lower=float(a[amin]-lo);upper=None if hi is None else float(hi-a[amax])
    QA[key+'_bounds']={'valid':int(mask.sum()),'undefined':int((~mask).sum()),'min':float(a[amin]),'max':float(a[amax]),
        'min_locator':locator(data,amin),'max_locator':locator(data,amax),'lower_margin':lower,'upper_margin':upper,'slack':1e-12}
    need(lower>=-1e-12 and (upper is None or upper>=-1e-12),'diagnostic bound '+key)

def update_row(data,ds,n,frame,H,G):
    row=dict(dataset=ds,update_index=int(n),response_state_index=int(n)+1,block=int(n)//200,phase=int(n)%200,
        inherited=ds=='PREFIX',source_frame=int(frame),H=float(H),H_sign=int(np.sign(H)),h=.1*abs(float(H)),G=float(G),G_squared=float(G*G))
    for field,key in [('incoming_mean_speed','r'),('pre_damping_mean_speed','m'),('reconstructed_post_mean_speed','t'),
        ('post_mean_speed','post_norm'),('incoming_mean_squared_speed','v2'),('pre_damping_mean_squared_speed','w2'),
        ('reconstructed_post_mean_squared_speed','z2'),('post_mean_squared_speed','post_squared')]:
        row[field]=mean(data[key])
    for k in ['I','A','L','L_direct','B','C','R','R_stable','q','q2','impulse_norm']:
        row['mean_'+k]=mean(data[k])
    for k in ['A','C']:
        signed=fsum(data[k]);activity=fsum(abs(data[k]))
        row[k+'_signed_center_sum']=signed;row[k+'_absolute_center_sum']=activity
        row['mean_abs_'+k]=activity/8
        raw=None if activity==0 else 1-abs(signed)/activity
        row[k+'_cancellation_raw']=raw;row[k+'_cancellation_defined']=activity>0
        row[k+'_cancellation_report_valid']=activity>=FLOOR
        row[k+'_cancellation']=raw if activity>=FLOOR else None
    row['q_min']=float(min(data['q']));row['q_max']=float(max(data['q']))
    for threshold,label in [(.9,'090'),(.99,'099'),(.999,'0999')]:
        row['q_fraction_ge_'+label]=float(np.mean(data['q']>=threshold))
    for k,mask in [('cosine','cosine_valid'),('retention','retention_valid'),('chi','chi_valid')]:
        valid=data[mask];row[k+'_valid_count']=int(valid.sum())
        row[k+'_mean']=mean(data[k][valid]) if valid.any() else None
    row['bit_change_count']=int(data['bit_changed'].sum())
    row['observed_delta_speed']=row['post_mean_speed']-row['incoming_mean_speed']
    row['observed_delta_squared_speed']=row['post_mean_squared_speed']-row['incoming_mean_squared_speed']
    row['budget_delta_speed']=fsum([row['mean_B'],row['mean_C'],-row['mean_R']])
    row['budget_delta_squared_speed']=fsum([row['mean_I'],row['mean_A'],-row['mean_L']])
    row['update_saved_speed_residual']=row['observed_delta_speed']-row['budget_delta_speed']
    row['update_saved_square_residual']=row['observed_delta_squared_speed']-row['budget_delta_squared_speed']
    row['update_internal_speed_residual']=row['reconstructed_post_mean_speed']-row['incoming_mean_speed']-row['budget_delta_speed']
    row['update_internal_square_residual']=row['reconstructed_post_mean_squared_speed']-row['incoming_mean_squared_speed']-row['budget_delta_squared_speed']
    row['h_squared']=row['h']**2;row['factorized_mean_I']=row['h_squared']*row['G_squared']*row['mean_q2']
    row['update_I_factor_residual']=row['mean_I']-row['factorized_mean_I']
    row['update_G_residual']=row['G']-1/(1+row['incoming_mean_speed'])
    return row

def cycle_rows(data,updates):
    out=[]
    for ds in LABELS:
        blocks=[0] if ds=='PREFIX' else [1,2,3,4]
        for block in blocks:
            u=[r for r in updates if r['dataset']==ds and r['block']==block]
            d=data[(data['dataset_id']==LABELS.index(ds))&(data['block']==block)]
            need(len(u)==200 and len(d)==1600,'block population')
            r={'dataset':ds,'block':block,'updates':200,'centers':1600,'inherited':ds=='PREFIX',
                'post_mean_speed_mean':mean([a['post_mean_speed'] for a in u]),
                'incoming_speed_start':u[0]['incoming_mean_speed'],'post_speed_end':u[-1]['post_mean_speed'],
                'incoming_square_start':u[0]['incoming_mean_squared_speed'],'post_square_end':u[-1]['post_mean_squared_speed']}
            for k in ['I','A','L','B','C','R']:
                r['sum_mean_'+k]=fsum(a['mean_'+k] for a in u)
            for k in ['A','C']:
                signed=fsum(d[k]);activity=fsum(abs(d[k]))
                r[k+'_center_total']=signed;r[k+'_absolute_activity_total']=activity
                r['sum_mean_abs_'+k]=activity/8
                r[k+'_total_cancellation_raw']=1-abs(signed)/activity if activity>0 else None
                r[k+'_total_cancellation_report_valid']=activity>=FLOOR
            for kind,delta,budgetkey,start,end,terms in [
                ('speed','observed_delta_speed','budget_delta_speed','incoming_mean_speed','post_mean_speed',['B','C','R']),
                ('square','observed_delta_squared_speed','budget_delta_squared_speed','incoming_mean_squared_speed','post_mean_squared_speed',['I','A','L'])]:
                boundary=u[-1][end]-u[0][start]
                r[kind+'_boundary_delta']=boundary;r[kind+'_sum_observed_deltas']=fsum(a[delta] for a in u)
                r[kind+'_sum_budget_deltas']=fsum(a[budgetkey] for a in u)
                r[kind+'_telescoping_observed_residual']=r[kind+'_sum_observed_deltas']-boundary
                r[kind+'_telescoping_budget_residual']=r[kind+'_sum_budget_deltas']-boundary
                r[kind+'_term_sum_residual']=fsum([r['sum_mean_'+terms[0]],r['sum_mean_'+terms[1]],-r['sum_mean_'+terms[2]]])-boundary
                for key in [kind+'_telescoping_observed_residual',kind+'_telescoping_budget_residual',kind+'_term_sum_residual']:
                    need(abs(r[key])<=1e-10,'cycle closure '+ds+str(block)+' '+key)
            for k in ['q','cosine','impulse_norm','m','retention','chi']:
                for q,x in describe(d[k]).items():r[k+'_'+q]=x
            for threshold,label in [(.9,'090'),(.99,'099'),(.999,'0999')]:r['q_fraction_ge_'+label]=float(np.mean(d['q']>=threshold))
            r['bit_changes']=int(d['bit_changed'].sum())
            out.append(r)
    return out

def strata_rows(data):
    groups=[('ALL',np.ones(len(data),bool))]
    for ds in LABELS:groups.append((ds,data['dataset_id']==LABELS.index(ds)))
    for ds in LABELS:
        for c in ([0] if ds=='PREFIX' else [1,2,3,4]):groups.append((ds+'_block_'+str(c),(data['dataset_id']==LABELS.index(ds))&(data['block']==c)))
    rows=[]
    for group,mask in groups:
        splits=[('all',mask)]
        splits += [('H_'+label,mask&(data['H_sign']==value)) for label,value in [('positive',1),('negative',-1),('zero',0)]]
        splits += [('bit_'+label,mask&(data['bit_changed']==value)) for label,value in [('changed',True),('unchanged',False)]]
        splits += [('H_'+label+'_bit_'+bl,mask&(data['H_sign']==value)&(data['bit_changed']==bv))
            for label,value in [('positive',1),('negative',-1),('zero',0)] for bl,bv in [('changed',True),('unchanged',False)]]
        for label,selection in splits:
            d=data[selection];r={'group':group,'stratum':label,'center_count':len(d)}
            for k in ['q','impulse_norm','r','m','cosine','retention','chi','G','I','A','L','B','C','R']:
                for q,x in describe(d[k]).items():r[k+'_'+q]=x
            for k in ['A','C']:
                r[k+'_signed_total']=fsum(d[k]);r[k+'_absolute_total']=fsum(abs(d[k]))
                r[k+'_positive_count']=int(np.sum(d[k]>0));r[k+'_negative_count']=int(np.sum(d[k]<0))
                r[k+'_cancellation']=None if r[k+'_absolute_total']<FLOOR else 1-abs(r[k+'_signed_total'])/r[k+'_absolute_total']
                r[k+'_cancellation_report_valid']=r[k+'_absolute_total']>=FLOOR
            for threshold,label2 in [(.9,'090'),(.99,'099'),(.999,'0999')]:
                r['q_count_ge_'+label2]=int(np.sum(d['q']>=threshold))
                r['q_fraction_ge_'+label2]=float(np.mean(d['q']>=threshold)) if len(d) else None
            rows.append(r)
    return rows

def comparison(data,updates,left,right,tags):
    a=data[left*8:(left+1)*8];b=data[right*8:(right+1)*8];u=updates[left];v=updates[right]
    row=dict(tags);vectors={}
    for label,key in [('incoming','incoming_velocity'),('pre_damping','w'),('post_damping','saved_successor_velocity'),('reconstructed_post','z')]:
        dist=np.linalg.norm(a[key]-b[key],axis=1);vectors[label]=dist
        row[label+'_distance_mean']=mean(dist);row[label+'_distance_max']=float(max(dist));row[label+'_distance_RMS']=math.sqrt(mean(dist**2))
    slack=vectors['post_damping']-vectors['pre_damping'];internal=vectors['reconstructed_post']-vectors['pre_damping']
    need(float(max(slack))<=1e-12 and float(max(internal))<=1e-12,'center damping nonexpansion '+str(tags))
    row['nonexpansion_max_signed_excess']=float(max(slack));row['internal_nonexpansion_max_signed_excess']=float(max(internal))
    row['nonexpansion_center_at_max']=int(np.argmax(slack))
    for stat in ['mean','max','RMS']:
        num=row['post_damping_distance_'+stat];den=row['pre_damping_distance_'+stat]
        row['damping_distance_ratio_'+stat],row['damping_distance_ratio_'+stat+'_valid']=ratio(num,den)
    for k in ['incoming_mean_speed','pre_damping_mean_speed','post_mean_speed','mean_I','mean_A','mean_L','mean_B','mean_C','mean_R','mean_q','G','H','mean_abs_A','mean_abs_C']:
        row[k+'_difference']=u[k]-v[k]
    gi=abs(u['G']-v['G']);rhs=abs(u['incoming_mean_speed']-v['incoming_mean_speed'])/((1+u['incoming_mean_speed'])*(1+v['incoming_mean_speed']))
    row['gain_difference_identity_residual']=gi-rhs
    need(abs(gi-rhs)<=1e-12,'gain difference identity')
    return row,vectors

def phase_spread(updates,indices):
    metrics=['incoming_mean_speed','pre_damping_mean_speed','post_mean_speed','mean_R','mean_I','mean_A','mean_L',
        'mean_B','mean_C','mean_abs_A','mean_abs_C','h','G','G_squared','mean_q','mean_q2','factorized_mean_I']
    rows=[]
    for view,cycles in spec()['phase_spread_views'].items():
        for phase in range(200):
            u=[updates[int(indices[c,phase])] for c in cycles]
            r={'view':view,'phase':phase,'cycle_count':len(cycles)}
            for k in metrics:
                a=np.array([x[k] for x in u]);mu=float(np.mean(a));sd=float(np.std(a,ddof=0))
                r[k+'_mean']=mu;r[k+'_min']=float(a.min());r[k+'_max']=float(a.max())
                r[k+'_range']=float(np.ptp(a));r[k+'_population_std']=sd
                r[k+'_std_over_abs_mean'],r[k+'_std_over_abs_mean_valid']=ratio(sd,abs(mu))
            pre=np.array([x['pre_damping_mean_speed'] for x in u]);post=np.array([x['post_mean_speed'] for x in u]);loss=np.array([x['mean_R'] for x in u])
            vp=float(np.var(pre));vz=float(np.var(post));vl=float(np.var(loss));cov=float(np.mean((pre-pre.mean())*(loss-loss.mean())))
            residual=vz-(vp+vl-2*cov)
            need(abs(residual)<=1e-12,'scalar dispersion closure')
            r.update(pre_damping_variance=vp,post_damping_variance=vz,loss_variance=vl,covariance_pre_damping_loss=cov,
                variance_balance_residual=residual,variance_change=vz-vp,scalar_variance_decreased=vz<vp,
                scalar_variance_increased=vz>vp,scalar_increase_exceeds_slack=vz-vp>1e-12)
            r['post_over_pre_variance'],r['variance_ratio_valid']=ratio(vz,vp)
            rows.append(r)
    return rows

def summarize(data,updates):
    cycles=cycle_rows(data,updates);write_csv(ROOT/'analysis/cycle_summary.csv',cycles)
    strata=strata_rows(data);write_csv(ROOT/'analysis/factor_stratum_summary.csv',strata)
    ri=np.concatenate([np.arange(200),np.arange(1000,1800)]).reshape(5,200)
    repeated=[dict(updates[int(k)],cycle=c) for c in range(5) for k in ri[c]]
    write_csv(ROOT/'analysis/repeated_phase_curves.csv',repeated)
    spreads=phase_spread(updates,ri);write_csv(ROOT/'analysis/phase_spread.csv',spreads)
    pairrows=[];pairvectors=[];pairsummary=[]
    for c,d in spec()['same_phase_unique_pairs']:
        current=[]
        for j in range(200):
            tags={'cycle':c,'reference_cycle':d,'phase':j,'update_index':200*c+j,'reference_update_index':200*d+j,
                  'response_state_index':200*c+j+1,'reference_response_state_index':200*d+j+1}
            row,vectors=comparison(data,updates,int(ri[c,j]),int(ri[d,j]),tags);pairrows.append(row);current.append(row);pairvectors.append(vectors)
        summary={'cycle':c,'reference_cycle':d,'phase_rows':200}
        for label in ['incoming','pre_damping','post_damping']:
            for stat in ['mean','max','RMS']:
                a=[r[label+'_distance_'+stat] for r in current]
                summary[label+'_'+stat+'_phase_mean']=mean(a);summary[label+'_'+stat+'_phase_max']=max(a)
        for stat in ['mean','max','RMS']:
            vals=[r['damping_distance_ratio_'+stat] for r in current if r['damping_distance_ratio_'+stat+'_valid']]
            summary['ratio_'+stat+'_masked']=200-len(vals)
            for key,val in describe(vals).items():summary['ratio_'+stat+'_'+key]=val
        delta=np.array([r['post_mean_speed_difference'] for r in current])
        summary['post_mean_speed_difference_RMS']=float(np.sqrt(np.mean(delta**2)))
        summary['post_mean_speed_difference_max_abs']=float(max(abs(delta)))
        summary['forcing_increases_mean_labeled_distance_phases']=sum(r['pre_damping_distance_mean']>r['incoming_distance_mean'] for r in current)
        summary['nonexpansion_max_signed_excess']=max(r['nonexpansion_max_signed_excess'] for r in current)
        pairsummary.append(summary)
    need(len(pairrows)==1400 and len({(r['cycle'],r['reference_cycle'],r['phase']) for r in pairrows})==1400,'same-phase population')
    write_csv(ROOT/'analysis/same_phase_comparisons.csv',pairrows);write_csv(ROOT/'analysis/same_phase_summary.csv',pairsummary)
    cross=[];crossvectors=[]
    for k in range(800):
        row,vectors=comparison(data,updates,1000+k,200+k,{'update_index':200+k,'response_state_index':201+k,'block':(200+k)//200,'phase':k%200,'difference_order':'REPEATED minus CONTINUOUS'})
        cross.append(row);crossvectors.append(vectors)
    write_csv(ROOT/'analysis/cross_arm_comparisons.csv',cross)
    crossblocks=[]
    for c in range(1,5):
        rows=cross[(c-1)*200:c*200];r={'block':c,'updates':200}
        for k in [x for x in rows[0] if x.endswith('_difference')]:
            r[k+'_sum']=fsum(x[k] for x in rows);r[k+'_mean']=mean([x[k] for x in rows])
        for key in ['incoming_distance_mean','pre_damping_distance_mean','post_damping_distance_mean']:
            r[key+'_phase_mean']=mean([x[key] for x in rows])
        crossblocks.append(r)
    write_csv(ROOT/'analysis/cross_arm_block_summary.csv',crossblocks)
    np.savez_compressed(ROOT/'analysis/comparison_center_distances.npz',
        **{'same_phase_'+k:np.array([r[k] for r in pairvectors]) for k in pairvectors[0]},
        **{'cross_arm_'+k:np.array([r[k] for r in crossvectors]) for k in crossvectors[0]},
        same_phase_cycle=np.array([r['cycle'] for r in pairrows]),same_phase_reference_cycle=np.array([r['reference_cycle'] for r in pairrows]),
        same_phase_phase=np.array([r['phase'] for r in pairrows]),cross_arm_update_index=np.arange(200,1000))
    # Fixed descriptive bins declared before the data pass; no fitted or tuned classification.
    orientation=[]
    medges=[0.,.01,.05,.1,.25,.5,1.,float('inf')];cedges=[1/3-1e-12,.45,.6,.8,1+1e-12]
    for lo,hi in zip(medges[:-1],medges[1:]):
        for cl,ch in zip(cedges[:-1],cedges[1:]):
            mask=data['chi_valid']&(data['m']>=lo)&(data['m']<hi)&(data['chi']>=cl)&(data['chi']<ch)
            d=data[mask];r={'m_lower':lo,'m_upper':hi if math.isfinite(hi) else None,'chi_lower':cl,'chi_upper':ch,'count':len(d)}
            for k in ['m','chi','retention']:
                for label,val in describe(d[k]).items():r[k+'_'+label]=val
            orientation.append(r)
    need(sum(r['count'] for r in orientation)==int(data['chi_valid'].sum()),'orientation bin population')
    write_csv(ROOT/'analysis/retention_orientation_summary.csv',orientation)
    spreadsummary={}
    for view in spec()['phase_spread_views']:
        rows=[r for r in spreads if r['view']==view];r={}
        for metric in ['incoming_mean_speed','pre_damping_mean_speed','post_mean_speed','mean_R','mean_I','mean_A','mean_L','mean_B','mean_C']:
            std=np.array([x[metric+'_population_std'] for x in rows])
            r[metric]={'mean_phase_population_std':mean(std),'RMS_phase_population_std':float(np.sqrt(np.mean(std**2))),
                'max_phase_population_std':float(max(std)),'max_std_phase':int(np.argmax(std)),
                'mean_phase_range':mean([x[metric+'_range'] for x in rows]),
                'mean_curve':mean([x[metric+'_mean'] for x in rows]),
                'normalized_std_masked_phases':sum(not x[metric+'_std_over_abs_mean_valid'] for x in rows)}
        r['scalar_variance_decreased_phases']=sum(x['scalar_variance_decreased'] for x in rows)
        r['scalar_variance_increased_phases']=sum(x['scalar_variance_increased'] for x in rows)
        r['scalar_increase_exceeds_slack_phases']=sum(x['scalar_increase_exceeds_slack'] for x in rows)
        r['increased_phase_indices']=[x['phase'] for x in rows if x['scalar_variance_increased']]
        r['max_variance_balance_residual']=max(abs(x['variance_balance_residual']) for x in rows)
        r['mean_pre_variance']=mean([x['pre_damping_variance'] for x in rows]);r['mean_post_variance']=mean([x['post_damping_variance'] for x in rows])
        r['mean_loss_variance']=mean([x['loss_variance'] for x in rows]);r['mean_covariance']=mean([x['covariance_pre_damping_loss'] for x in rows])
        r['variance_ratio_masked_phases']=sum(not x['variance_ratio_valid'] for x in rows)
        spreadsummary[view]=r
    return {'cycles':cycles,'overall_strata':[r for r in strata if r['group'] in ['ALL','PREFIX','CONTINUOUS','REPEATED']],
        'same_phase_summary':pairsummary,'phase_spread_summary':spreadsummary,'cross_arm_block_summary':crossblocks,
        'comparison_counts':{'same_phase':len(pairrows),'same_phase_center_pairs':len(pairrows)*8,'cross_arm':len(cross)},
        'pair_nonexpansion_max_signed_excess':max(r['nonexpansion_max_signed_excess'] for r in pairrows),
        'cross_arm_nonexpansion_max_signed_excess':max(r['nonexpansion_max_signed_excess'] for r in cross),
        'gain_difference_identity_max_abs_residual':max(abs(r['gain_difference_identity_residual']) for r in pairrows+cross)}

def main():
    start=time.monotonic();save(ROOT/'evidence/PRIMARY_STARTED.json',{'utc':utc(),'one_primary_pass':True},True)
    need(load(ROOT/'evidence/INPUT_GATE.json')['status']=='PASS' and load(ROOT/'evidence/ALGEBRA_GATE.json')['status']=='PASS','prerequisite gates')
    selected_preservation()
    np.seterr(over='raise',divide='raise',invalid='raise',under='ignore')
    data=np.lib.format.open_memmap(ROOT/'tmp/center_checkpoint.npy',mode='w+',dtype=DTYPE,shape=(14400,))
    data['complete']=False;data.flush();updates=[];PROGRESS['primary_passes_started']=1;progress()
    try:
        for dsid,record in enumerate(spec()['records']):
            ds=record['dataset']
            with np.load(lp(ROOT/'inputs/accepted_sim02'/record['path']),allow_pickle=False) as z:
                arrays={k:z[k] for k in ['positions','velocities','bits','update_index','source_frame','source_time','H','G']}
            for a in arrays.values():a.setflags(write=False)
            for j,n in enumerate(arrays['update_index']):
                PROGRESS['updates_started']+=1;progress()
                uidx=len(updates);begin=uidx*8
                pm=arrays['positions'][j];pp=arrays['positions'][j+1]
                vm=arrays['velocities'][j];vp=arrays['velocities'][j+1];bp=arrays['bits'][j+1];bm=arrays['bits'][j]
                H=arrays['H'][j];G=arrays['G'][j]
                for i in range(8):
                    PROGRESS['centers_started']+=1;progress()
                    # Exactly the prescribed saved mixed array; no calculated position is ever used.
                    mixed=pm.copy();mixed[:i]=pp[:i]
                    centroid=np.mean(mixed,axis=0)
                    diff=centroid-pm[i];diff=np.mod(diff+10.0/2,10.0)-10.0/2
                    norm_regularized=np.linalg.norm(diff)+0.01
                    sign=-1 if bp[i] else 1
                    force=diff/norm_regularized*H*sign
                    impulse=0.1*force*G
                    b=budget(vm[i],impulse);k=begin+i;r=data[k]
                    for field in FLOATS+MASKS:r[field]=b[field]
                    r['record_id']=k;r['update_row']=uidx;r['dataset_id']=dsid;r['update_index']=n;r['source_frame']=arrays['source_frame'][j]
                    r['source_time']=arrays['source_time'][j];r['center']=i;r['block']=int(n)//200;r['phase']=int(n)%200
                    r['bit_minus']=bm[i];r['bit_plus']=bp[i];r['bit_changed']=bm[i]!=bp[i];r['H_sign']=np.sign(H)
                    r['H']=H;r['G']=G;r['h']=.1*abs(H);r['d_norm']=np.linalg.norm(diff);r['q']=r['d_norm']/norm_regularized;r['q2']=r['q']**2
                    r['incoming_velocity']=vm[i];r['saved_successor_velocity']=vp[i];r['centroid']=centroid;r['d']=diff;r['impulse']=impulse
                    r['w']=b['w'];r['z']=b['z'];r['velocity_residual']=b['z']-vp[i]
                    r['post_norm']=np.linalg.norm(vp[i]);r['post_squared']=np.dot(vp[i],vp[i])
                    r['impulse_factor_residual']=b['impulse_norm']-r['h']*G*r['q']
                    r['I_factor_residual']=b['I']-r['h']**2*G**2*r['q2']
                    r['square_saved_residual']=(r['post_squared']-b['v2'])-(b['I']+b['A']-b['L'])
                    r['square_direct_saved_residual']=(r['post_squared']-b['v2'])-(b['I']+b['A']-b['L_direct'])
                    r['speed_saved_residual']=(r['post_norm']-b['r'])-(b['B']+b['C']-b['R'])
                    r['speed_stable_saved_residual']=(r['post_norm']-b['r'])-(b['B']+b['C']-b['R_stable'])
                    for key in FLOATS+EXTRA+VECTORS:
                        if key not in ['cosine','retention','chi']:need(np.isfinite(r[key]).all(),'nonfinite primary '+key)
                    for key in ['velocity_residual','square_saved_residual','square_direct_saved_residual','speed_saved_residual',
                                'speed_stable_saved_residual','square_internal_residual','speed_internal_residual',
                                'square_direct_internal_residual','speed_stable_internal_residual','L_stable_minus_direct',
                                'R_stable_minus_direct','impulse_factor_residual','I_factor_residual']:
                        need(np.max(np.abs(r[key]))<=1e-12,'primary residual '+ds+'/'+str(n)+'/'+str(i)+'/'+key)
                    r['complete']=True;PROGRESS['centers_completed']+=1
                data.flush()
                updates.append(update_row(data[begin:begin+8],ds,n,arrays['source_frame'][j],H,G))
                PROGRESS['updates_completed']+=1;progress()
                if PROGRESS['updates_completed']%200==0:
                    output_cap();print('Completed passive updates '+str(PROGRESS['updates_completed'])+'/1800',flush=True)
        need(PROGRESS['updates_started']==PROGRESS['updates_completed']==1800,'update population')
        need(PROGRESS['centers_started']==PROGRESS['centers_completed']==14400 and data['complete'].all(),'center population')
        need(len({(int(r['dataset_id']),int(r['update_index']),int(r['center'])) for r in data})==14400,'duplicate center keys')
        PROGRESS['primary_passes_completed']=1;progress()
        for key in ['velocity_residual','square_saved_residual','square_direct_saved_residual','speed_saved_residual','speed_stable_saved_residual',
                    'square_internal_residual','square_direct_internal_residual','speed_internal_residual','speed_stable_internal_residual',
                    'L_stable_minus_direct','R_stable_minus_direct','impulse_factor_residual','I_factor_residual']:
            check_center(data,key)
        for key,lo,hi,mask in [('I',0,None,None),('L',0,None,None),('L_direct',0,None,None),('R',0,None,None),
                    ('q',0,1,None),('cosine',-1,1,'cosine_valid'),('retention',0,1,'retention_valid'),('chi',1/3,1,'chi_valid')]:
            bound(data,key,lo,hi,mask)
        for key in ['update_saved_speed_residual','update_saved_square_residual','update_internal_speed_residual',
                    'update_internal_square_residual','update_I_factor_residual','update_G_residual']:check_update(updates,key)
        np.savez_compressed(ROOT/'analysis/center_decomposition.npz',**{k:np.asarray(data[k]) for k in data.dtype.names})
        write_csv(ROOT/'analysis/update_budgets.csv',updates)
        results=summarize(data,updates)
        selected_preservation();need(baseline()==load(ROOT/'evidence/BASELINE.json'),'repository preservation')
        elapsed=time.monotonic()-start;need(elapsed<300,'analysis wall cap')
        masks={k:int((~data[k]).sum()) for k in ['cosine_valid','retention_valid','chi_valid']}
        masks.update({k:int(data[k].sum()) for k in ['budget_zero_denominator','damping_zero_denominator']})
        save(ROOT/'evidence/QA.json',{'status':'PASS','utc':utc(),'checks':QA,'undefined_or_zero_counts':masks,
            'counts':dict(PROGRESS),'distinct_blocks':9,'component_positions':43200,'comparison_counts':results['comparison_counts'],
            'same_phase_nonexpansion_max_signed_excess':results['pair_nonexpansion_max_signed_excess'],
            'cross_arm_nonexpansion_max_signed_excess':results['cross_arm_nonexpansion_max_signed_excess'],
            'gain_difference_identity_max_abs_residual':results['gain_difference_identity_max_abs_residual'],
            'cycle_telescoping_max_abs_residual':max(abs(r[k]) for r in results['cycles'] for k in r if k.endswith('_residual')),
            'phase_variance_balance_max_abs_residual':max(r['max_variance_balance_residual'] for r in results['phase_spread_summary'].values()),
            'absolute_tolerances':spec()['absolute_tolerances'],'analysis_elapsed_seconds':elapsed,
            'aggregate_bytes_at_analysis_close':aggregate_bytes(),'preservation':'PASS'},True)
        results.update(status='PASS',utc=utc(),accounting=dict(PROGRESS),analysis_elapsed_seconds=elapsed,
            undefined_counts=masks,record_population={'PREFIX':200,'CONTINUOUS':800,'REPEATED':800},
            output_bytes_at_analysis_close=aggregate_bytes(),interpretation='Passive observed-path decomposition; no interventions or independent-trial inference.')
        save(ROOT/'analysis/RESULTS.json',results,True);output_cap()
        print(json.dumps({'status':'PASS','accounting':PROGRESS,'elapsed_seconds':elapsed,
            'max_velocity_residual':QA['velocity_residual'],'phase_spread':results['phase_spread_summary']}),flush=True)
    except BaseException as e:
        data.flush();progress()
        save(ROOT/'evidence/FAILURE.json',{'utc':utc(),'error':str(e),'traceback':traceback.format_exc(),'counters':dict(PROGRESS),
            'partial_centers':'tmp/center_checkpoint.npy; complete mask identifies retained successful rows','no_retry':True},True)
        raise

if __name__=='__main__':main()
