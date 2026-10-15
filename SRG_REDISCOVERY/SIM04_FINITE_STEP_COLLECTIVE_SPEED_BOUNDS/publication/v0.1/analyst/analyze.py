"""One selected-data preparation and one analytic evaluation per fixed pair/phase."""
from common import *
import math, traceback
import numpy as np
from bounds import FAMILIES,source_pair,geometry,norm,profile,mean
COUNTERS={'selected_updates':0,'selected_center_records':0,'analytic_pair_phase_evaluations':0,
    'labeled_center_pairs':0,'outcome_pair_phase_joins':0,'view_phase_summaries':0}
RESIDUALS={};QA={}
def progress(stage):
    update(ROOT/'evidence/PRIMARY_PROGRESS.json',{'utc':utc(),'stage':stage,'counters':COUNTERS,'bytes':cap()})
def check(name,residual,tol,kind,axes):
    a=np.asarray(residual,dtype=np.float64)
    need(np.isfinite(a).all(),'nonfinite residual '+name)
    RESIDUALS[name]=a.copy()
    hi=np.unravel_index(int(np.argmax(a)),a.shape);lo=np.unravel_index(int(np.argmin(a)),a.shape)
    ab=np.unravel_index(int(np.argmax(np.abs(a))),a.shape)
    item={'kind':kind,'tolerance':tol,'shape':list(a.shape),'axes':axes,'min_signed':float(a[lo]),
        'min_index':list(map(int,lo)),'max_signed':float(a[hi]),'max_index':list(map(int,hi)),
        'max_abs':float(abs(a[ab])),'max_abs_index':list(map(int,ab))}
    QA[name]=item
    failed=item['max_abs']>tol if kind=='equality' else item['max_signed']>tol
    if failed:
        save(ROOT/'evidence/NUMERICAL_FAILURE.json',{'name':name,'check':item,'counters':COUNTERS})
        raise AssertionError('Numerical gate: '+name)
def save_npz(path,arrays):
    with lp(path).open('xb') as f:np.savez_compressed(f,**arrays)
def ratio(x,y,floor):
    valid=y>=floor
    return (float(x/y) if valid else None),bool(valid)
def classification(margin):
    return 'PASS' if margin>1e-14 else 'NOT_ESTABLISHED' if margin< -1e-14 else 'UNRESOLVED'
def centered_var(values):
    mu=mean(values);return math.fsum((float(x)-mu)**2 for x in values)/len(values)
def flatten_center(x):
    a=np.asarray(x);return a.reshape((-1,)+a.shape[2:])
def main():
    start=time.monotonic();spec=load(ROOT/'received/SIM04_EXPERIMENT_SPEC_v0.1.json')
    gate=load(ROOT/'evidence/IMPLEMENTATION_GATE.json');need(gate['status']=='PASS','implementation gate')
    for n,x in gate['frozen_files'].items():need(ident(ROOT/n)==x,'frozen scientific code/spec changed '+n)
    preserved()
    path=ROOT/'inputs/analysis/center_decomposition.npz'
    ids=load(ROOT/'received/SIM04_INPUT_IDENTITIES_AND_SCHEMAS.json')
    access=[]
    with np.load(lp(path),allow_pickle=False) as src:
        meta={k:src[k] for k in ids['npz_join_fields']}
        for field in meta.values():field.flags.writeable=False
        access.append({'utc':utc(),'stage':'metadata','fields':list(meta)})
        join={}
        for row,(ds,n,c) in enumerate(zip(meta['dataset_id'],meta['update_index'],meta['center'])):
            key=(int(ds),int(n),int(c));need(key not in join,'duplicate source join key');join[key]=row
        sel=[];mapping=[]
        for cycle in range(5):
            for phase in range(200):
                n=cycle*200+phase;ds=0 if cycle==0 else 2
                for center in range(8):
                    key=(ds,n,center);need(key in join,'missing selected key')
                    row=join[key];sel.append(row)
                    need(bool(meta['complete'][row]),'incomplete selected row')
                    need(int(meta['phase'][row])==phase and int(meta['block'][row])==cycle,'phase/cycle metadata')
                    need(int(meta['source_frame'][row])==phase,'source frame schedule')
                    need(abs(float(meta['source_time'][row])-0.1*phase)<=1e-12,'source time schedule')
                    mapping.append({'selected_row':len(sel)-1,'source_row':row,'record_id':int(meta['record_id'][row]),
                        'update_row':int(meta['update_row'][row]),'dataset_id':ds,'update_index':n,
                        'cycle':cycle,'phase':phase,'center':center,'source_frame':int(meta['source_frame'][row])})
                COUNTERS['selected_updates']+=1;COUNTERS['selected_center_records']+=8
        need(len(sel)==8000 and len(set(sel))==8000,'selected unique count')
        needed=[i for i in range(len(meta['dataset_id'])) if int(meta['dataset_id'][i]) in (0,2)]
        need(set(sel)==set(needed),'selected population completeness')
        index=np.asarray(sel,dtype=np.int32).reshape(5,200,8)
        data={}
        for k in ids['npz_allowed_bound_fields']:
            a=src[k][index].copy();need(np.isfinite(a).all(),'nonfinite selected '+k);a.flags.writeable=False;data[k]=a
        access.append({'utc':utc(),'stage':'allowed pre-output fields','fields':list(data)})
        need(np.isin(data['bit_plus'],[0,1]).all(),'bit domain')
        v=data['incoming_velocity'];a=data['impulse'];w=data['w'];d=data['d'];H=data['H'];G=data['G'];bits=data['bit_plus']
        incoming=np.array([[mean(norm(v[c,j])) for j in range(200)] for c in range(5)],dtype=np.float64)
        pre=np.array([[mean(norm(w[c,j])) for j in range(200)] for c in range(5)],dtype=np.float64)
        gg=geometry(d.reshape(-1,3),bits.reshape(-1)).reshape(5,200,8,3)
        check('input_w_minus_v_plus_a',w-(v+a),1e-12,'equality',['cycle','phase','center','component'])
        check('input_impulse_factorization',a-(.1*H*G)[...,None]*gg,1e-12,'equality',['cycle','phase','center','component'])
        check('input_G_from_incoming',G-1/(1+incoming[...,None]),1e-12,'equality',['cycle','phase','center'])
        check('input_H_common_centers',H-H[...,:1],1e-12,'equality',['cycle','phase','center'])
        check('input_H_common_cycles',H-H[:1,:,:],1e-12,'equality',['cycle','phase','center'])
        check('input_G_common_centers',G-G[...,:1],1e-12,'equality',['cycle','phase','center'])
        check('input_geometry_norm_minus_one',norm(gg)-1,1e-12,'inequality',['cycle','phase','center'])
        write_csv(ROOT/'analysis/selected_record_map.csv',mapping)
        progress('selected_input_preparation_complete')
        prep_seconds=time.monotonic()-start
        pairrows=[];centers={}
        for pair_id,(c,dd) in enumerate(spec['comparisons']['unordered_pairs']):
            for j in range(200):
                row,ctr=source_pair(v[c,j],a[c,j],w[c,j],d[c,j],float(H[c,j,0]),float(G[c,j,0]),bits[c,j],
                    v[dd,j],a[dd,j],w[dd,j],d[dd,j],float(H[dd,j,0]),float(G[dd,j,0]),bits[dd,j])
                pairrows.append({'pair_id':pair_id,'cycle_c':c,'cycle_d':dd,'phase':j,'update_c':200*c+j,
                    'update_d':200*dd+j,**row})
                for k,val in ctr.items():centers.setdefault(k,[]).append(val)
                COUNTERS['analytic_pair_phase_evaluations']+=1;COUNTERS['labeled_center_pairs']+=8
            progress('pre_output_bounds_pair_family_'+str(pair_id))
        center_arrays={k:flatten_center(vals) for k,vals in centers.items()}
        pair_arrays={k:np.asarray([r[k] for r in pairrows]) for k in pairrows[0]}
        q=pair_arrays['Q_VECTOR'];k=pair_arrays['K_COMPONENT'];pp=pair_arrays['P_PROFILE'];best=pair_arrays['BEST_PRE']
        for low,high in [('Q_VECTOR','T_TRIANGLE'),('T_TRIANGLE','GAMMA_SOURCE'),('GAMMA_SOURCE','OMEGA_COARSE'),
                         ('BEST_PRE','K_COMPONENT'),('BEST_PRE','P_PROFILE'),('K_COMPONENT','Q_VECTOR'),('P_PROFILE','Q_VECTOR')]:
            check('pair_'+low+'_minus_'+high,pair_arrays[low]-pair_arrays[high],1e-12,'inequality',['pair_phase_row'])
        check('difference_alignment_identity',center_arrays['alignment_residual'],1e-12,'equality',['center_pair_row'])
        for low,high in [('K_center','Q_center'),('P_center','Q_center'),('Q_center','T_center')]:
            check('center_'+low+'_minus_'+high,center_arrays[low]-center_arrays[high],1e-12,'inequality',['center_pair_row'])
        for key in ('kappa','lambda'):
            check(key+'_minus_one',center_arrays[key]-1,1e-12,'inequality',['center_pair_row','component'])
            check('negative_'+key,-center_arrays[key],1e-12,'inequality',['center_pair_row','component'])
        packed={'pair__'+k:v for k,v in pair_arrays.items()}
        packed.update({'center__'+k:v for k,v in center_arrays.items()})
        packed['center__pair_phase_row']=np.repeat(np.arange(2000,dtype=np.int32),8)
        packed['center__center']=np.tile(np.arange(8,dtype=np.int8),2000)
        save_npz(ROOT/'analysis/PRE_OUTPUT_BOUNDS.npz',packed)
        seal={'utc':utc(),'status':'SEALED_BEFORE_OUTCOME_JOIN','identity':ident(ROOT/'analysis/PRE_OUTPUT_BOUNDS.npz'),
            'pair_phase_rows':2000,'center_pair_rows':16000,'allowed_bound_fields':ids['npz_allowed_bound_fields'],
            'outcome_fields_loaded_so_far':[],'bound_functions':'analyst/bounds.py','bound_function_identity':ident(ROOT/'analyst/bounds.py')}
        save(ROOT/'analysis/PRE_OUTPUT_BOUNDS_SEAL.json',seal)
        progress('pre_output_bounds_sealed')
        bound_seconds=time.monotonic()-start-prep_seconds
        # First scientific loading of successor values occurs only after the file/hash seal above.
        saved=src['saved_successor_velocity'][index].copy()
        saved.flags.writeable=False;need(np.isfinite(saved).all(),'nonfinite saved outcomes')
        access.append({'utc':utc(),'stage':'post-seal outcome join','fields':['saved_successor_velocity'],
            'preceding_bound_seal':seal['identity']})
    need(ident(ROOT/'analysis/PRE_OUTPUT_BOUNDS.npz')==seal['identity'],'sealed bounds changed')
    post_norm=norm(saved)
    post=np.array([[mean(post_norm[c,j]) for j in range(200)] for c in range(5)],dtype=np.float64)
    outcome_center={k:[] for k in ('post_delta_velocity','post_profile_delta','post_signed_distance','post_profile_distance',
        'signed_speed_difference','individual_abs_speed_difference')}
    for row in pairrows:
        c,dd,j=row['cycle_c'],row['cycle_d'],row['phase']
        dy=saved[c,j]-saved[dd,j];dp=profile(saved[c,j])-profile(saved[dd,j])
        signed=post_norm[c,j]-post_norm[dd,j];zs=norm(dy);zp=norm(dp);tn=np.abs(signed)
        S=abs(float(post[c,j]-post[dd,j]));Zs=mean(zs);Zp=mean(zp);Tn=mean(tn)
        Zstar=Zs if row['best_is_K'] else Zp
        row.update(observed_S=S,signed_collective_difference=float(post[c,j]-post[dd,j]),Zsigned=Zs,Zprofile=Zp,
            Tnorm=Tn,Zstar=Zstar,gap_Q_to_BEST=row['Q_VECTOR']-row['BEST_PRE'],
            gap_BEST_to_Zstar=row['BEST_PRE']-Zstar,gap_Zstar_to_Tnorm=Zstar-Tn,gap_Tnorm_to_S=Tn-S,
            gap_Q_to_S=row['Q_VECTOR']-S)
        row['gap_telescope_residual']=row['gap_Q_to_S']-sum(row[x] for x in ('gap_Q_to_BEST','gap_BEST_to_Zstar','gap_Zstar_to_Tnorm','gap_Tnorm_to_S'))
        for family in FAMILIES:
            bound=row[family];row[family+'_gap']=bound-S
            row[family+'_utilization'],row[family+'_utilization_valid']=ratio(S,bound,1e-12)
            row[family+'_factor_over_outcome'],row[family+'_factor_valid']=ratio(bound,S,1e-12)
        for family in ('K_COMPONENT','P_PROFILE','BEST_PRE'):
            row[family+'_improvement']=row['Q_VECTOR']-row[family]
            row[family+'_over_Q'],row[family+'_over_Q_valid']=ratio(row[family],row['Q_VECTOR'],1e-12)
        for key,val in [('post_delta_velocity',dy),('post_profile_delta',dp),('post_signed_distance',zs),
                        ('post_profile_distance',zp),('signed_speed_difference',signed),('individual_abs_speed_difference',tn)]:
            outcome_center[key].append(val)
        COUNTERS['outcome_pair_phase_joins']+=1
    outcomes={k:flatten_center(vals) for k,vals in outcome_center.items()}
    get=lambda k:np.asarray([r[k] for r in pairrows],dtype=np.float64)
    for family in FAMILIES:check('outcome_S_minus_'+family,get('observed_S')-get(family),1e-12,'inequality',['pair_phase_row'])
    for low,high in [('Tnorm','Zsigned'),('Zsigned','K_COMPONENT'),('Tnorm','Zprofile'),('Zprofile','P_PROFILE'),('observed_S','Tnorm')]:
        check('diagnostic_'+low+'_minus_'+high,get(low)-get(high),1e-12,'inequality',['pair_phase_row'])
    check('gap_telescope',get('gap_telescope_residual'),1e-12,'equality',['pair_phase_row'])
    for gap in ('gap_Q_to_BEST','gap_BEST_to_Zstar','gap_Zstar_to_Tnorm','gap_Tnorm_to_S'):
        check('negative_'+gap,-get(gap),1e-12,'inequality',['pair_phase_row'])
    check('center_post_signed_minus_K',outcomes['post_signed_distance']-center_arrays['K_center'],1e-12,'inequality',['center_pair_row'])
    check('center_post_profile_minus_P',outcomes['post_profile_distance']-center_arrays['P_center'],1e-12,'inequality',['center_pair_row'])
    for k in ('post_signed_distance','post_profile_distance'):
        check('center_abs_speed_minus_'+k,outcomes['individual_abs_speed_difference']-outcomes[k],1e-12,'inequality',['center_pair_row'])
    # Accepted readout references are joined on metadata, never passed to analytic bounds.
    curves=list(csv.DictReader(io.StringIO(read(ROOT/'inputs/analysis/repeated_phase_curves.csv').decode())))
    curve_map={(int(r['cycle']),int(r['phase'])):r for r in curves}
    need(len(curves)==len(curve_map)==1000,'reference curve keys')
    speedrows=[];ref_res={k:[] for k in ('incoming','pre_damping','post')}
    for c in range(5):
        for j in range(200):
            ref=curve_map[c,j]
            need(ref['dataset']==('PREFIX' if c==0 else 'REPEATED') and int(ref['update_index'])==c*200+j,'reference curve join')
            speedrows.append({'cycle':c,'phase':j,'update_index':200*c+j,'incoming':float(incoming[c,j]),
                'pre_damping':float(pre[c,j]),'post':float(post[c,j])})
            for key,arr,col in [('incoming',incoming,'incoming_mean_speed'),('pre_damping',pre,'pre_damping_mean_speed'),('post',post,'post_mean_speed')]:
                ref_res[key].append(float(arr[c,j])-float(ref[col]))
    for key,vals in ref_res.items():check('reference_speed_'+key,vals,1e-12,'equality',['cycle_phase_row'])
    spread=list(csv.DictReader(io.StringIO(read(ROOT/'inputs/analysis/phase_spread.csv').decode())))
    spreadmap={(r['view'],int(r['phase'])):r for r in spread}
    need(len(spread)==len(spreadmap)==400,'reference spread keys')
    by_pair={(r['cycle_c'],r['cycle_d'],r['phase']):r for r in pairrows}
    dispersion=[];var_res={key:[] for key in ('incoming','pre_damping','post')};refvar={key:[] for key in var_res}
    for view,conf in spec['comparisons']['views'].items():
        cycles=conf['cycles'];m=conf['m'];pairs=[(c,dd) for c,dd in spec['comparisons']['unordered_pairs'] if c in cycles and dd in cycles]
        need(len(pairs)==conf['unordered_pairs'],'view pair count')
        for j in range(200):
            refs=[by_pair[c,dd,j] for c,dd in pairs]
            row={'view':view,'phase':j,'cycles':m,'pairs':len(pairs)}
            sr=spreadmap[view,j]
            for key,arr in [('incoming',incoming),('pre_damping',pre),('post',post)]:
                vals=arr[cycles,j];var=centered_var(vals)
                pairvar=math.fsum((float(arr[c,j])-float(arr[dd,j]))**2 for c,dd in pairs)/(m*m)
                row[key+'_variance']=var;row[key+'_SD']=math.sqrt(var);row[key+'_pair_variance']=pairvar
                var_res[key].append(pairvar-var)
                refcol={'incoming':'incoming_mean_speed_population_std','pre_damping':'pre_damping_mean_speed_population_std','post':'post_mean_speed_population_std'}[key]
                refvar[key].append(var-float(sr[refcol])**2)
            for family in FAMILIES:
                W=math.fsum(float(r[family])**2 for r in refs)/(m*m);E=math.sqrt(W)
                row[family+'_variance_upper']=W;row[family+'_SD_upper']=E
                row[family+'_variance_gap']=W-row['post_variance'];row[family+'_SD_gap']=E-row['post_SD']
                for unit,out,bound,floor in [('variance',row['post_variance'],W,1e-24),('SD',row['post_SD'],E,1e-12)]:
                    row[family+'_'+unit+'_utilization'],row[family+'_'+unit+'_utilization_valid']=ratio(out,bound,floor)
                    row[family+'_'+unit+'_factor'],row[family+'_'+unit+'_factor_valid']=ratio(bound,out,floor)
            for ref in ('incoming','pre_damping'):
                margin=row[ref+'_variance']-row['BEST_PRE_variance_upper']
                actual=row[ref+'_variance']-row['post_variance']
                row[ref+'_condition_margin']=margin;row[ref+'_condition_class']=classification(margin)
                row[ref+'_actual_margin']=actual;row[ref+'_actual_class']=classification(actual)
            dispersion.append(row);COUNTERS['view_phase_summaries']+=1
    for key in var_res:
        check('pair_population_identity_'+key,var_res[key],1e-14,'equality',['view_phase_row'])
        check('reference_variance_'+key,refvar[key],1e-14,'equality',['view_phase_row'])
    for family in FAMILIES:
        check('post_variance_minus_'+family,[r['post_variance']-r[family+'_variance_upper'] for r in dispersion],1e-14,'inequality',['view_phase_row'])
    progress('outcomes_and_dispersion_complete')
    packed.update({'outcome__'+k:v for k,v in outcomes.items()})
    save_npz(ROOT/'analysis/center_pair_bounds.npz',packed)
    save_npz(ROOT/'analysis/NUMERICAL_RESIDUALS.npz',RESIDUALS)
    write_csv(ROOT/'analysis/pair_phase_bounds.csv',pairrows)
    write_csv(ROOT/'analysis/phase_dispersion_bounds.csv',dispersion)
    write_csv(ROOT/'analysis/cycle_phase_speeds.csv',speedrows)
    outcome_seconds=time.monotonic()-start-prep_seconds-bound_seconds
    from summarize import summarize
    results=summarize(pairrows,dispersion,center_arrays,outcomes)
    results.update(counts=dict(COUNTERS),stage_seconds={'selected_input_preparation':prep_seconds,
        'pre_output_bounds_and_seal':bound_seconds,'outcome_join_and_tables':outcome_seconds,
        'total_primary_worker':time.monotonic()-start},pre_output_seal=seal,
        no_new_motion_updates=0,new_source_reconstructions=0,new_scientific_analysis=True)
    save(ROOT/'analysis/RESULTS.json',results)
    save(ROOT/'evidence/NUMERICAL_QA.json',{'status':'PASS','checks':QA,'residual_archive':'analysis/NUMERICAL_RESIDUALS.npz',
        'locators':'pair_phase_row=row in pair_phase_bounds.csv; center_pair_row=8*pair_phase_row+center; view_phase_row=row in phase_dispersion_bounds.csv; selected arrays indexed cycle, phase, center, component',
        'counters':COUNTERS,'clipping':False,'relative_tolerance':0})
    save(ROOT/'evidence/DATA_ACCESS_LOG.json',{'access':access,'outcome_load_follows_seal':True,
        'D_evaluations_on_saved_records':0,'raw_state_loads':0,'reference_CSV_numeric_join':'after pre-output seal',
        'earlier_file_inspection':'CSV field names and dataset/cycle/view metadata only; not bound inputs'})
    schemas={}
    for name,arrs in [('PRE_OUTPUT_BOUNDS.npz',{k:v for k,v in packed.items() if not k.startswith('outcome__')}),
                      ('center_pair_bounds.npz',packed),('NUMERICAL_RESIDUALS.npz',RESIDUALS)]:
        schemas[name]={k:{'shape':list(v.shape),'dtype':str(v.dtype)} for k,v in arrs.items()}
    tables={}
    for f in sorted(lp(ROOT/'analysis').glob('*.csv')):
        with f.open(encoding='utf-8',newline='') as h:
            rr=csv.reader(h);cols=next(rr);count=sum(1 for _ in rr)
        tables[f.name]={'columns':cols,'rows':count}
    save(ROOT/'evidence/OUTPUT_SCHEMAS.json',{'npz':schemas,'csv':tables,'units_and_masks':'OUTPUT_FIELD_GUIDE.md'})
    need(COUNTERS=={'selected_updates':1000,'selected_center_records':8000,'analytic_pair_phase_evaluations':2000,
        'labeled_center_pairs':16000,'outcome_pair_phase_joins':2000,'view_phase_summaries':400},'execution population')
    need(ident(ROOT/'analysis/PRE_OUTPUT_BOUNDS.npz')==seal['identity'],'post-output bounds changed')
    progress('primary_complete')
    save(ROOT/'evidence/PRIMARY_RESULT.json',{'status':'PASS','utc':utc(),'counters':COUNTERS,
        'seconds':time.monotonic()-start,'bytes':cap(),'output_schemas':ident(ROOT/'evidence/OUTPUT_SCHEMAS.json')})
    print(json.dumps({'status':'PASS','counters':COUNTERS,'seconds':time.monotonic()-start,'bytes':size()}))
if __name__=='__main__':
    try:main()
    except BaseException:
        update(ROOT/'evidence/PRIMARY_WORKER_FAILURE.json',{'utc':utc(),'counters':COUNTERS,'exception':traceback.format_exc()})
        raise
