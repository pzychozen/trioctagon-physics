"""Independent SIM03 review: immutable saved inputs, no engine imports or RNG use.

Reconstructs each intermediate from its own saved predecessor/successor. Never
calculates a position successor or passes a reconstructed velocity to another
center or update. Uses NumPy and the Python standard library only.

Example:
  python -B review_sim03_saved_evidence.py --bundle-root EXTRACTED_SIM03 \
    --output-dir SEPARATE_REVIEW_DIR --reference-paper-zip SIM02_PAPER_v0.1_GPT_REVIEW.zip
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, platform, stat, sys, zipfile
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import numpy as np

LABELS = ['PREFIX', 'CONTINUOUS', 'REPEATED']
PATHS = ['inputs/runs/C/states.npz', 'runs/CONTINUOUS/states.npz', 'runs/REPEATED/states.npz']
PAIRS = [(1,0),(2,1),(3,2),(4,3),(2,0),(3,0),(4,0)]
TOL, BLOCK_TOL, FLOOR = 1e-12, 1e-10, 1e-12
CHECKS: dict[str, dict] = {}

def sha(b: bytes) -> str: return hashlib.sha256(b).hexdigest()
def ident(p: Path) -> dict:
    b = p.read_bytes(); return {'bytes':len(b), 'sha256':sha(b)}
def js(p: Path): return json.loads(p.read_text(encoding='utf-8'))
def total(x): return math.fsum(float(v) for v in np.ravel(x))
def avg(x): return total(x)/np.size(x)
def norm(x): return float(np.linalg.norm(x))
def desc(x):
    a = np.asarray(x, dtype=float); a = a[np.isfinite(a)]
    if a.size == 0: return dict(count=0, **{k:None for k in ['mean','min','p05','p25','p50','p75','p95','max']})
    q = np.quantile(a, [.05,.25,.5,.75,.95], method='linear')
    return dict(count=int(a.size), mean=avg(a), min=float(a.min()), max=float(a.max()),
                **dict(zip(['p05','p25','p50','p75','p95'],map(float,q))))

def check(name, actual, expected, tol=TOL):
    """Record max residual; compare metadata and validity exactly."""
    a,b = np.asarray(actual), np.asarray(expected)
    if a.shape != b.shape: raise AssertionError(f'{name}: shape {a.shape} != {b.shape}')
    if a.dtype.kind in 'OUSb' or b.dtype.kind in 'OUSb' or (a.dtype.kind in 'iu' and b.dtype.kind in 'iu'):
        if not np.array_equal(a,b): raise AssertionError(f'{name}: exact metadata mismatch')
        CHECKS[name]={'entries':int(a.size),'exact':True}; return
    a,b = a.astype(float),b.astype(float)
    if not np.array_equal(np.isnan(a), np.isnan(b)): raise AssertionError(f'{name}: NaN mask mismatch')
    valid=~np.isnan(a)
    if not np.isfinite(a[valid]).all() or not np.isfinite(b[valid]).all(): raise AssertionError(name+': nonfinite')
    r=np.zeros(a.shape);r[valid]=a[valid]-b[valid]
    m=float(np.max(np.abs(r),initial=0.0))
    k=np.unravel_index(int(np.argmax(abs(r))),r.shape) if r.size else ()
    CHECKS[name]={'entries':int(a.size),'max_abs_residual':m,'index_at_max':list(map(int,k)), 'tolerance':tol}
    if m>tol: raise AssertionError(f'{name}: residual {m} > {tol}')

def table(path: Path):
    with path.open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))

def verify_table(path: Path, expected: list[dict], tol=TOL):
    actual=table(path)
    if len(actual)!=len(expected): raise AssertionError(path.name+': row count')
    keys=set(expected[0])
    if any(set(r)!=keys for r in expected): raise AssertionError(path.name+': reviewer schema inconsistent')
    if set(actual[0])!=keys: raise AssertionError(f'{path.name}: columns diff {set(actual[0])^keys}')
    for k in sorted(keys):
        ex=[r[k] for r in expected]
        nonnull=next((v for v in ex if v is not None),None)
        if isinstance(nonnull,(bool,np.bool_)):
            if any(r[k] not in ['True','False'] for r in actual): raise AssertionError(path.name+'/'+k)
            ac=[r[k]=='True' for r in actual]
        elif isinstance(nonnull,str): ac=[r[k] for r in actual]
        else:
            ac=[float(r[k]) if r[k]!='' else np.nan for r in actual]
            ex=[np.nan if v is None else float(v) for v in ex]
        if k.endswith('_std_over_abs_mean'):
            # The signed mean can nearly cancel. Verify the unnormalized
            # relation at the original absolute tolerance, not an arbitrary
            # absolute tolerance on an amplified dimensionless quotient.
            prefix=k[:-len('_std_over_abs_mean')]
            mu=np.array([r[prefix+'_mean'] for r in expected],dtype=float)
            sd=np.array([r[prefix+'_population_std'] for r in expected],dtype=float)
            valid=np.array([r[k+'_valid'] for r in expected],dtype=bool)
            av=np.asarray(ac,dtype=float);ev=np.asarray(ex,dtype=float)
            if not np.array_equal(np.isnan(av),~valid):raise AssertionError(path.name+'/'+k+': mask')
            check(path.name+'/'+k+'/numerator_identity',av[valid]*abs(mu[valid]),sd[valid],tol)
            diff=abs(av[valid]-ev[valid]);arg=int(np.argmax(diff)) if diff.size else 0
            CHECKS[path.name+'/'+k+'/quotient_diagnostic']={
                'entries':int(diff.size),'max_abs_ratio_difference':float(diff.max(initial=0.)),
                'absolute_ratio_equality_is_not_the_acceptance_test':True,
                'row_at_max':int(np.flatnonzero(valid)[arg]) if diff.size else None,
                'mean_denominator_at_max':float(abs(mu[valid][arg])) if diff.size else None,
                'actual_ratio_at_max':float(av[valid][arg]) if diff.size else None,
                'expected_ratio_at_max':float(ev[valid][arg]) if diff.size else None}
        else:
            check(path.name+'/'+k,ac,ex,tol)
    return actual

def archive_inputs(root, reference):
    manifest=js(root/'SIM03_REVIEW_MANIFEST.json')
    for n,row in manifest['files'].items():
        if ident(root/n)!={k:row[k] for k in ('bytes','sha256')}: raise AssertionError('payload '+n)
    mapping=js(root/'evidence/INPUT_MAP.json')['files']
    original_count=0
    with zipfile.ZipFile(reference) as old:
        prefix='payload/SRG_REDISCOVERY/SIM02_REPEATED_DRIVE_AND_RETAINED_STATE/publication/v0.1/'
        for n,row in mapping.items():
            b=(root/'inputs/accepted_sim02'/n).read_bytes()
            if {'bytes':len(b),'sha256':sha(b)}!={k:row[k] for k in ('bytes','sha256')}: raise AssertionError(n)
            if b!=old.read(prefix+n): raise AssertionError('prior approved payload mismatch '+n)
            original_count+=1
    base=js(root/'evidence/BASELINE.json');close=js(root/'evidence/CLOSEOUT_CHECKS.json')
    if base!=close['final_baseline']: raise AssertionError('preservation receipt discrepancy')
    gate=js(root/'evidence/IMPLEMENTATION_GATE.json')['syntax_and_static_call_scan']
    for n,row in gate.items():
        if ident(root/n)!=row['identity']: raise AssertionError('frozen implementation mismatch '+n)
    return {'payload_hashes_checked':len(manifest['files']), 'selected_inputs_matching_prior_approved_payload':original_count,
            'before_after_baseline_records_equal':True,'dirty_file_receipts':len(base['modified_tracked']),
            'frozen_implementation_hashes':len(gate), 'windows_filesystem_independently_accessed':False}

def primary(root):
    chunks=[];saved_sources=[];max_source=[]
    for did,(name,path) in enumerate(zip(LABELS,PATHS)):
        with np.load(root/'inputs/accepted_sim02'/path,allow_pickle=False) as z:
            a={k:z[k] for k in ['positions','velocities','bits','H','G','update_index','source_frame','source_time']}
        for x in a.values():x.setflags(write=False)
        N=200 if did==0 else 800
        assert a['positions'].shape==a['velocities'].shape==(N+1,8,3)
        assert a['bits'].shape==(N+1,8)
        assert a['positions'].dtype==a['velocities'].dtype==np.dtype('float64')
        assert np.isfinite(a['positions']).all() and np.isfinite(a['velocities']).all()
        assert np.isin(a['bits'],[0,1]).all()
        ns=np.arange(0,200) if did==0 else np.arange(200,1000)
        frames=ns%200 if did==2 else ns
        check('source/'+name+'/updates',a['update_index'],ns)
        check('source/'+name+'/frames',a['source_frame'],frames)
        check('source/'+name+'/times',a['source_time'],frames*.1,0.)
        check('source/'+name+'/G',a['G'],1/(1+np.linalg.norm(a['velocities'][:-1],axis=2).mean(axis=1)))
        if did:
            for key in ['positions','velocities','bits']:check('source/'+name+'/branch_'+key,a[key][0],saved_sources[0][key][-1],0.)
        if did==2:check('source/repeated_waveform',a['H'].reshape(4,200),np.tile(saved_sources[0]['H'],(4,1)),0.)
        for j,n in enumerate(ns):
            for i in range(8):
                # Only saved successors populate earlier center positions.
                mixed=np.concatenate((a['positions'][j+1,:i],a['positions'][j,i:]),axis=0)
                centroid=np.mean(mixed,axis=0)
                d=((centroid-a['positions'][j,i]+5.)%10.)-5.
                dn=norm(d);H=a['H'][j];G=a['G'][j];sign=1-2*int(a['bits'][j+1,i])
                impulse=.1*(d/(dn+.01)*H*sign)*G
                v=a['velocities'][j,i];post=a['velocities'][j+1,i]
                w=v+impulse;ell=np.log1p(np.abs(w));out=w/(1+ell)
                r,m,t=norm(v),norm(w),norm(out)
                v2=total(v*v);w2=total(w*w);z2=total(out*out)
                In=total(impulse*impulse);An=2*total(v*impulse)
                ld=w2-z2;ls=total(w*w*ell*(2+ell)/(1+ell)**2)
                B=In/(m+r) if m+r else 0.;C=An/(m+r) if m+r else 0.
                R=m-t;rs=ls/(m+t) if m+t else 0.
                q=dn/(dn+.01);an=norm(impulse);pn=norm(post);p2=total(post*post)
                k=len(chunks)
                row=dict(record_id=k,update_row=k//8,dataset_id=did,update_index=int(n),source_frame=int(frames[j]),
                    center=i,block=int(n)//200,phase=int(n)%200,bit_minus=int(a['bits'][j,i]),bit_plus=int(a['bits'][j+1,i]),
                    bit_changed=bool(a['bits'][j,i]!=a['bits'][j+1,i]),H_sign=int(np.sign(H)),complete=True,
                    r=r,m=m,t=t,v2=v2,w2=w2,z2=z2,impulse_norm=an,I=In,A=An,L=ls,L_direct=ld,
                    L_stable_minus_direct=ls-ld,B=B,C=C,R=R,R_stable=rs,R_stable_minus_direct=rs-R,
                    cosine=total(v*impulse)/(r*an) if r*an else np.nan,
                    retention=t/m if m else np.nan,chi=total(w**4)/(w2*w2) if m else np.nan,
                    square_internal_residual=(z2-v2)-(In+An-ls),square_direct_internal_residual=(z2-v2)-(In+An-ld),
                    speed_internal_residual=(t-r)-(B+C-R),speed_stable_internal_residual=(t-r)-(B+C-rs),
                    H=float(H),G=float(G),source_time=float(a['source_time'][j]),d_norm=dn,q=q,q2=q*q,h=.1*abs(H),
                    impulse_factor_residual=an-.1*abs(H)*G*q,I_factor_residual=In-(.1*abs(H))**2*G**2*q*q,
                    post_norm=pn,post_squared=p2,square_saved_residual=(p2-v2)-(In+An-ls),
                    square_direct_saved_residual=(p2-v2)-(In+An-ld),speed_saved_residual=(pn-r)-(B+C-R),
                    speed_stable_saved_residual=(pn-r)-(B+C-rs),cosine_valid=bool(r and an),retention_valid=bool(m),chi_valid=bool(m),
                    budget_zero_denominator=(m+r==0),damping_zero_denominator=(m+t==0),
                    incoming_velocity=v.copy(),saved_successor_velocity=post.copy(),centroid=centroid,d=d,impulse=impulse,
                    w=w,z=out,velocity_residual=out-post)
                chunks.append(row)
        saved_sources.append(a)
    x={k:np.array([r[k] for r in chunks]) for k in chunks[0]}
    with np.load(root/'analysis/center_decomposition.npz',allow_pickle=False) as z:
        assert set(x)==set(z.files)
        for k,v in x.items(): check('center/'+k,z[k],v)
    for did,name in enumerate(LABELS):
        v=x['velocity_residual'][x['dataset_id']==did]
        check('reconstructed_saved_velocity/'+name,v,np.zeros_like(v))
        max_source.append({'dataset':name,'max_abs_residual':float(np.max(abs(v))),
                           'exact_component_matches':int(np.sum(v==0)),'components':int(v.size)})
    for key in ['square_internal_residual','speed_internal_residual','square_saved_residual','speed_saved_residual']:
        check('identity/'+key,x[key],np.zeros(14400))
    for key,lo,hi in [('I',0,np.inf),('L',0,np.inf),('R',0,np.inf),('q',0,1),('cosine',-1,1),('retention',0,1),('chi',1/3,1)]:
        assert np.all((x[key]>=lo-TOL)&(x[key]<=hi+TOL)),key
    return x,max_source

def updates_from(x):
    out=[]
    meanfields={'incoming_mean_speed':'r','pre_damping_mean_speed':'m','reconstructed_post_mean_speed':'t','post_mean_speed':'post_norm',
        'incoming_mean_squared_speed':'v2','pre_damping_mean_squared_speed':'w2','reconstructed_post_mean_squared_speed':'z2','post_mean_squared_speed':'post_squared'}
    for u in range(1800):
        sl=slice(8*u,8*u+8);i=8*u;n=int(x['update_index'][i]);did=int(x['dataset_id'][i])
        r=dict(dataset=LABELS[did],update_index=n,response_state_index=n+1,block=n//200,phase=n%200,inherited=did==0,
               source_frame=int(x['source_frame'][i]),H=float(x['H'][i]),H_sign=int(x['H_sign'][i]),h=float(x['h'][i]),G=float(x['G'][i]),G_squared=float(x['G'][i]**2))
        for k,v in meanfields.items():r[k]=avg(x[v][sl])
        for k in ['I','A','L','L_direct','B','C','R','R_stable','q','q2','impulse_norm']:r['mean_'+k]=avg(x[k][sl])
        for k in ['A','C']:
            s=total(x[k][sl]);ab=total(abs(x[k][sl]));raw=1-abs(s)/ab if ab>0 else None
            r.update({k+'_signed_center_sum':s,k+'_absolute_center_sum':ab,'mean_abs_'+k:ab/8,
                      k+'_cancellation_raw':raw,k+'_cancellation_defined':ab>0,k+'_cancellation_report_valid':ab>=FLOOR,
                      k+'_cancellation':raw if ab>=FLOOR else None})
        r['q_min']=float(x['q'][sl].min());r['q_max']=float(x['q'][sl].max())
        for val,lab in [(.9,'090'),(.99,'099'),(.999,'0999')]:r['q_fraction_ge_'+lab]=float(np.mean(x['q'][sl]>=val))
        for k in ['cosine','retention','chi']:
            v=x[k+'_valid'][sl];r[k+'_valid_count']=int(v.sum());r[k+'_mean']=avg(x[k][sl][v]) if v.any() else None
        r['bit_change_count']=int(x['bit_changed'][sl].sum())
        r['observed_delta_speed']=r['post_mean_speed']-r['incoming_mean_speed']
        r['observed_delta_squared_speed']=r['post_mean_squared_speed']-r['incoming_mean_squared_speed']
        r['budget_delta_speed']=total([r['mean_B'],r['mean_C'],-r['mean_R']])
        r['budget_delta_squared_speed']=total([r['mean_I'],r['mean_A'],-r['mean_L']])
        r['update_saved_speed_residual']=r['observed_delta_speed']-r['budget_delta_speed']
        r['update_saved_square_residual']=r['observed_delta_squared_speed']-r['budget_delta_squared_speed']
        r['update_internal_speed_residual']=r['reconstructed_post_mean_speed']-r['incoming_mean_speed']-r['budget_delta_speed']
        r['update_internal_square_residual']=r['reconstructed_post_mean_squared_speed']-r['incoming_mean_squared_speed']-r['budget_delta_squared_speed']
        r['h_squared']=r['h']**2;r['factorized_mean_I']=r['h_squared']*r['G_squared']*r['mean_q2']
        r['update_I_factor_residual']=r['mean_I']-r['factorized_mean_I']
        r['update_G_residual']=r['G']-1/(1+r['incoming_mean_speed'])
        out.append(r)
    return out

def verify_cycles(root,x,u):
    rows=[]
    for did,ds in enumerate(LABELS):
        for block in ([0] if did==0 else [1,2,3,4]):
            v=[r for r in u if r['dataset']==ds and r['block']==block]
            mask=(x['dataset_id']==did)&(x['block']==block)
            r=dict(dataset=ds,block=block,updates=200,centers=1600,inherited=did==0,
                post_mean_speed_mean=avg([a['post_mean_speed'] for a in v]),incoming_speed_start=v[0]['incoming_mean_speed'],
                post_speed_end=v[-1]['post_mean_speed'],incoming_square_start=v[0]['incoming_mean_squared_speed'],post_square_end=v[-1]['post_mean_squared_speed'])
            for k in ['I','A','L','B','C','R']:r['sum_mean_'+k]=total([a['mean_'+k] for a in v])
            for k in ['A','C']:
                s=total(x[k][mask]);ab=total(abs(x[k][mask]))
                r.update({k+'_center_total':s,k+'_absolute_activity_total':ab,'sum_mean_abs_'+k:ab/8,
                          k+'_total_cancellation_raw':1-abs(s)/ab if ab else None,k+'_total_cancellation_report_valid':ab>=FLOOR})
            for kind,obs,bud,start,end,terms in [
              ('speed','observed_delta_speed','budget_delta_speed','incoming_mean_speed','post_mean_speed',['B','C','R']),
              ('square','observed_delta_squared_speed','budget_delta_squared_speed','incoming_mean_squared_speed','post_mean_squared_speed',['I','A','L'])]:
                delta=v[-1][end]-v[0][start];so=total([a[obs] for a in v]);sb=total([a[bud] for a in v])
                term=total([r['sum_mean_'+terms[0]],r['sum_mean_'+terms[1]],-r['sum_mean_'+terms[2]]])
                r.update({kind+'_boundary_delta':delta,kind+'_sum_observed_deltas':so,kind+'_sum_budget_deltas':sb,
                          kind+'_telescoping_observed_residual':so-delta,kind+'_telescoping_budget_residual':sb-delta,kind+'_term_sum_residual':term-delta})
                assert max(abs(so-delta),abs(sb-delta),abs(term-delta))<BLOCK_TOL
            for k in ['q','cosine','impulse_norm','m','retention','chi']:
                r.update({k+'_'+a:b for a,b in desc(x[k][mask]).items()})
            for val,lab in [(.9,'090'),(.99,'099'),(.999,'0999')]:r['q_fraction_ge_'+lab]=float(np.mean(x['q'][mask]>=val))
            r['bit_changes']=int(x['bit_changed'][mask].sum());rows.append(r)
    verify_table(root/'analysis/cycle_summary.csv',rows,BLOCK_TOL)
    return rows

def verify_strata(root,x):
    groups={'ALL':np.ones(14400,bool)}
    for did,ds in enumerate(LABELS):groups[ds]=(x['dataset_id']==did)
    for did,ds in enumerate(LABELS):
        for b in ([0] if did==0 else [1,2,3,4]):groups[f'{ds}_block_{b}']=(x['dataset_id']==did)&(x['block']==b)
    splits={'all':np.ones(14400,bool),'H_positive':x['H_sign']==1,'H_negative':x['H_sign']==-1,'H_zero':x['H_sign']==0,
            'bit_changed':x['bit_changed'],'bit_unchanged':~x['bit_changed']}
    for s in ['positive','negative','zero']:
        for b in ['changed','unchanged']:splits[f'H_{s}_bit_{b}']=splits['H_'+s]&splits['bit_'+b]
    rows=[]
    for g,mask in groups.items():
        for st,s in splits.items():
            z=mask&s;r=dict(group=g,stratum=st,center_count=int(z.sum()))
            for k in ['q','impulse_norm','r','m','cosine','retention','chi','G','I','A','L','B','C','R']:
                r.update({k+'_'+a:b for a,b in desc(x[k][z]).items()})
            for k in ['A','C']:
                su=total(x[k][z]);ab=total(abs(x[k][z]))
                r.update({k+'_signed_total':su,k+'_absolute_total':ab,k+'_positive_count':int(np.sum(x[k][z]>0)),
                   k+'_negative_count':int(np.sum(x[k][z]<0)),k+'_cancellation':1-abs(su)/ab if ab>=FLOOR else None,
                   k+'_cancellation_report_valid':ab>=FLOOR})
            for val,lab in [(.9,'090'),(.99,'099'),(.999,'0999')]:
                count=int(np.sum(x['q'][z]>=val));r['q_count_ge_'+lab]=count;r['q_fraction_ge_'+lab]=count/int(z.sum()) if z.any() else None
            rows.append(r)
    verify_table(root/'analysis/factor_stratum_summary.csv',rows,BLOCK_TOL)
    orient=[]
    ms=[0,.01,.05,.1,.25,.5,1,np.inf];cs=[1/3-TOL,.45,.6,.8,1+TOL]
    for lo,hi in zip(ms[:-1],ms[1:]):
        for cl,ch in zip(cs[:-1],cs[1:]):
            z=(x['m']>=lo)&(x['m']<hi)&(x['chi']>=cl)&(x['chi']<ch)&x['chi_valid']
            r=dict(m_lower=lo,m_upper=float(hi) if np.isfinite(hi) else None,chi_lower=cl,chi_upper=ch,count=int(z.sum()))
            for k in ['m','chi','retention']:r.update({k+'_'+a:b for a,b in desc(x[k][z]).items()})
            orient.append(r)
    verify_table(root/'analysis/retention_orientation_summary.csv',orient)
    return rows

def comparisons(root,x,u):
    rep=np.r_[0:200,1000:1800].reshape(5,200)
    stagekeys={'incoming':'incoming_velocity','pre_damping':'w','post_damping':'saved_successor_velocity','reconstructed_post':'z'}
    inputs=[('same_phase',[(int(rep[c,j]),int(rep[d,j]),dict(cycle=c,reference_cycle=d,phase=j,update_index=200*c+j,
             reference_update_index=200*d+j,response_state_index=200*c+j+1,reference_response_state_index=200*d+j+1)) for c,d in PAIRS for j in range(200)]),
            ('cross_arm',[(1000+k,200+k,dict(update_index=200+k,response_state_index=201+k,block=(200+k)//200,phase=k%200,
             difference_order='REPEATED minus CONTINUOUS')) for k in range(800)])]
    rowsets={};vecs={}
    for label,items in inputs:
        rows=[];vv={s:[] for s in stagekeys}
        for left,right,tags in items:
            r=dict(tags);d={};l=slice(left*8,left*8+8);b=slice(right*8,right*8+8)
            for s,key in stagekeys.items():
                d[s]=np.linalg.norm(x[key][l]-x[key][b],axis=1);vv[s].append(d[s])
                r[s+'_distance_mean']=avg(d[s]);r[s+'_distance_max']=float(d[s].max());r[s+'_distance_RMS']=math.sqrt(avg(d[s]**2))
            excess=d['post_damping']-d['pre_damping'];internal=d['reconstructed_post']-d['pre_damping']
            assert excess.max()<=TOL and internal.max()<=TOL
            r['nonexpansion_max_signed_excess']=float(excess.max());r['internal_nonexpansion_max_signed_excess']=float(internal.max())
            r['nonexpansion_center_at_max']=int(np.argmax(excess))
            for stat in ['mean','max','RMS']:
                den=r['pre_damping_distance_'+stat];r['damping_distance_ratio_'+stat]=r['post_damping_distance_'+stat]/den if den>=FLOOR else None
                r['damping_distance_ratio_'+stat+'_valid']=den>=FLOOR
            for k in ['incoming_mean_speed','pre_damping_mean_speed','post_mean_speed','mean_I','mean_A','mean_L','mean_B','mean_C','mean_R','mean_q','G','H','mean_abs_A','mean_abs_C']:
                r[k+'_difference']=u[left][k]-u[right][k]
            vl=u[left]['incoming_mean_speed'];vr=u[right]['incoming_mean_speed']
            r['gain_difference_identity_residual']=abs(r['G_difference'])-abs(vl-vr)/((1+vl)*(1+vr))
            rows.append(r)
        verify_table(root/f'analysis/{label}_comparisons.csv',rows)
        rowsets[label]=rows
        for k,v in vv.items():vecs[label+'_'+k]=np.array(v)
    with np.load(root/'analysis/comparison_center_distances.npz',allow_pickle=False) as z:
        for k,v in vecs.items():check('distance_array/'+k,z[k],v)
        check('pair_keys/cycle',z['same_phase_cycle'],[c for c,d in PAIRS for _ in range(200)])
        check('pair_keys/reference',z['same_phase_reference_cycle'],[d for c,d in PAIRS for _ in range(200)])
        check('pair_keys/phase',z['same_phase_phase'],np.tile(np.arange(200),7))
        check('pair_keys/cross_arm',z['cross_arm_update_index'],np.arange(200,1000))
    summaries=[]
    for k,(c,d) in enumerate(PAIRS):
        p=rowsets['same_phase'][200*k:200*k+200];r=dict(cycle=c,reference_cycle=d,phase_rows=200)
        for s in ['incoming','pre_damping','post_damping']:
            for st in ['mean','max','RMS']:
                a=[z[s+'_distance_'+st] for z in p];r[s+'_'+st+'_phase_mean']=avg(a);r[s+'_'+st+'_phase_max']=max(a)
        for st in ['mean','max','RMS']:
            a=[z['damping_distance_ratio_'+st] for z in p if z['damping_distance_ratio_'+st+'_valid']]
            r['ratio_'+st+'_masked']=200-len(a);r.update({'ratio_'+st+'_'+f:v for f,v in desc(a).items()})
        a=np.array([z['post_mean_speed_difference'] for z in p]);r['post_mean_speed_difference_RMS']=float(np.sqrt(np.mean(a*a)))
        r['post_mean_speed_difference_max_abs']=float(abs(a).max())
        r['forcing_increases_mean_labeled_distance_phases']=sum(z['pre_damping_distance_mean']>z['incoming_distance_mean'] for z in p)
        r['nonexpansion_max_signed_excess']=max(z['nonexpansion_max_signed_excess'] for z in p);summaries.append(r)
    verify_table(root/'analysis/same_phase_summary.csv',summaries)
    crosssum=[]
    for b in range(1,5):
        p=rowsets['cross_arm'][200*(b-1):200*b];r=dict(block=b,updates=200)
        for k in [f for f in p[0] if f.endswith('_difference')]:
            r[k+'_sum']=total([z[k] for z in p]);r[k+'_mean']=avg([z[k] for z in p])
        for k in ['incoming_distance_mean','pre_damping_distance_mean','post_damping_distance_mean']:r[k+'_phase_mean']=avg([z[k] for z in p])
        crosssum.append(r)
    verify_table(root/'analysis/cross_arm_block_summary.csv',crosssum,BLOCK_TOL)
    return rowsets,summaries,crosssum

def spreads(root,u):
    rep=np.r_[0:200,1000:1800].reshape(5,200)
    repeated=[dict(u[int(rep[c,j])],cycle=c) for c in range(5) for j in range(200)]
    verify_table(root/'analysis/repeated_phase_curves.csv',repeated)
    metrics=['incoming_mean_speed','pre_damping_mean_speed','post_mean_speed','mean_R','mean_I','mean_A','mean_L','mean_B','mean_C',
             'mean_abs_A','mean_abs_C','h','G','G_squared','mean_q','mean_q2','factorized_mean_I']
    rows=[];derived={}
    for view,cycles in [('all_five',range(5)),('new_four',range(1,5))]:
        for j in range(200):
            selected=[u[int(rep[c,j])] for c in cycles];r=dict(view=view,phase=j,cycle_count=len(cycles))
            for k in metrics:
                a=np.array([z[k] for z in selected]);mu=float(np.mean(a));sd=float(np.std(a,ddof=0))
                r.update({k+'_mean':mu,k+'_min':float(a.min()),k+'_max':float(a.max()),k+'_range':float(np.ptp(a)),
                    k+'_population_std':sd,k+'_std_over_abs_mean':sd/abs(mu) if abs(mu)>=FLOOR else None,k+'_std_over_abs_mean_valid':abs(mu)>=FLOOR})
            pre=np.array([z['pre_damping_mean_speed'] for z in selected]);post=np.array([z['post_mean_speed'] for z in selected]);loss=np.array([z['mean_R'] for z in selected])
            vp=float(np.var(pre));vo=float(np.var(post));vl=float(np.var(loss));co=float(np.mean((pre-pre.mean())*(loss-loss.mean())))
            res=vo-vp-vl+2*co
            assert abs(res)<TOL
            r.update(pre_damping_variance=vp,post_damping_variance=vo,loss_variance=vl,covariance_pre_damping_loss=co,
                variance_balance_residual=res,variance_change=vo-vp,scalar_variance_decreased=vo<vp,scalar_variance_increased=vo>vp,
                scalar_increase_exceeds_slack=vo-vp>TOL,post_over_pre_variance=vo/vp if vp>=FLOOR else None,variance_ratio_valid=vp>=FLOOR)
            rows.append(r)
        z=rows[-200:];ds={}
        for k in metrics:
            ds[k]={'rms_phase_sd':float(np.sqrt(np.mean([a[k+'_population_std']**2 for a in z]))),'mean':avg([a[k+'_mean'] for a in z])}
        ds['variance_decreased_phases']=sum(a['scalar_variance_decreased'] for a in z)
        ds['minimum_pre_minus_post_variance']=min(a['pre_damping_variance']-a['post_damping_variance'] for a in z)
        ds['mean_pre_variance']=avg([a['pre_damping_variance'] for a in z]);ds['mean_post_variance']=avg([a['post_damping_variance'] for a in z])
        ds['mean_loss_variance']=avg([a['loss_variance'] for a in z]);ds['mean_covariance']=avg([a['covariance_pre_damping_loss'] for a in z])
        ds['maximum_variance_balance_residual']=max(abs(a['variance_balance_residual']) for a in z)
        # Reviewer-only indexing consequence, not a new trajectory or mechanism control.
        vi=np.array([[u[int(rep[c,j])]['incoming_mean_speed'] for j in range(200)] for c in cycles])
        vo=np.array([[u[int(rep[c,j])]['post_mean_speed'] for j in range(200)] for c in cycles])
        assert np.array_equal(vi[:,1:],vo[:,:-1])
        lhs=float(np.mean(np.var(vo,axis=0))-np.mean(np.var(vi,axis=0)))
        rhs=float((np.var(vo[:,-1])-np.var(vi[:,0]))/200)
        ds['reviewer_indexing_identity']={'mean_variance_post_minus_incoming':lhs,'boundary_variance_difference_over_200':rhs,'residual':lhs-rhs,
          'incoming_boundary_variance':float(np.var(vi[:,0])),'outgoing_boundary_variance':float(np.var(vo[:,-1]))}
        assert abs(lhs-rhs)<TOL
        derived[view]=ds
    verify_table(root/'analysis/phase_spread.csv',rows)
    return rows,derived

def fixtures(root):
    gate=js(root/'evidence/ALGEBRA_GATE.json');cases=gate['nine_algebra_fixtures']
    assert len(cases)==9
    for c in cases:
        v=np.array(c['fixture']['v']);a=np.array(c['fixture']['impulse']);w=v+a;z=w/(1+np.log1p(abs(w)))
        r,m,t=norm(v),norm(w),norm(z);I=total(a*a);A=2*total(v*a);L=total(w*w)-total(z*z)
        B=I/(m+r) if m+r else 0.;C=A/(m+r) if m+r else 0.;R=m-t
        for k,val in dict(I=I,A=A,L=L,B=B,C=C,R=R).items():check('fixed_algebra/'+c['fixture']['name']+'/'+k,c['results'][k],val)
        assert abs((t-r)-(B+C-R))<TOL
    return 9

def main():
    pa=argparse.ArgumentParser(description=__doc__);pa.add_argument('--bundle-root',type=Path,required=True);pa.add_argument('--output-dir',type=Path,required=True)
    pa.add_argument('--reference-paper-zip',type=Path,required=True);args=pa.parse_args()
    root=args.bundle_root.resolve();out=args.output_dir.resolve()
    if out==root or root in out.parents:raise ValueError('Review outputs must be outside submitted inputs')
    out.mkdir(parents=True,exist_ok=True);dest=out/'INDEPENDENT_REVIEW_RESULTS.json'
    if dest.exists():raise FileExistsError('Refusing to overwrite completed independent results')
    np.seterr(over='raise',divide='raise',invalid='raise',under='ignore')
    provenance=archive_inputs(root,args.reference_paper_zip)
    nfixtures=fixtures(root)
    x,maxsource=primary(root);u=updates_from(x)
    verify_table(root/'analysis/update_budgets.csv',u)
    cycles=verify_cycles(root,x,u);strata=verify_strata(root,x)
    pairs,ps,cs=comparisons(root,x,u);spread,ss=spreads(root,u)
    # Machine-readable scientific summaries must agree with their independently checked tables.
    results=js(root/'analysis/RESULTS.json')
    for key,ours in [('cycles',cycles),('same_phase_summary',ps),('cross_arm_block_summary',cs)]:
        for j,row in enumerate(ours):
            for k,v in row.items():
                if v is None:assert results[key][j][k] is None
                else:check('RESULTS/'+key+'/'+str(j)+'/'+k,results[key][j][k],v,BLOCK_TOL)
    selected=[r for r in strata if r['group'] in ['ALL','PREFIX','CONTINUOUS','REPEATED']]
    for j,row in enumerate(selected):
        for k,v in row.items():
            if v is None:assert results['overall_strata'][j][k] is None
            else:check('RESULTS/strata/'+str(j)+'/'+k,results['overall_strata'][j][k],v,BLOCK_TOL)
    for view in ss:
        original=results['phase_spread_summary'][view]
        for k in ['incoming_mean_speed','pre_damping_mean_speed','post_mean_speed','mean_R','mean_I','mean_A','mean_L','mean_B','mean_C']:
            check('RESULTS/spread/'+view+'/'+k+'/rms',original[k]['RMS_phase_population_std'],ss[view][k]['rms_phase_sd'])
            check('RESULTS/spread/'+view+'/'+k+'/mean',original[k]['mean_curve'],ss[view][k]['mean'])
        for k in ['mean_pre_variance','mean_post_variance','mean_loss_variance','mean_covariance']:check('RESULTS/spread/'+view+'/'+k,original[k],ss[view][k])
        check('RESULTS/spread/'+view+'/decrease',original['scalar_variance_decreased_phases'],ss[view]['variance_decreased_phases'])
    # Report exception checks and aggregate anchors; no extra trajectory processing.
    exception=(x['q']<.9);ix=int(np.argmin(x['q']))
    assert exception.sum()==30 and np.all(x['dataset_id'][exception]==2) and np.all(x['center'][exception]==1)
    assert np.array_equal(x['update_index'][exception],np.arange(485,515))
    reports={}
    for did,ds in enumerate(LABELS):
        m=x['dataset_id']==did
        reports[ds]={'center_updates':int(m.sum()),'negative_alignment':int(np.sum(x['A'][m]<0)),
                     'bit_changes':int(x['bit_changed'][m].sum()),'q':desc(x['q'][m]),
                     'mean_budgets':{k:avg(x[k][m]) for k in ['I','A','L','B','C','R']}}
    reports['low_q_exception']={'count':30,'dataset':'REPEATED','center':1,'updates':[485,514],
                             'minimum_update':int(x['update_index'][ix]),'q_min':float(x['q'][ix]),'distance':float(x['d_norm'][ix]),
                             'impulse_norm':float(x['impulse_norm'][ix]),'H':float(x['H'][ix]),'G':float(x['G'][ix])}
    qbound=5*math.sqrt(3)/(5*math.sqrt(3)+.01)
    outcome={'status':'PASS','review_utc':datetime.now(timezone.utc).isoformat(),
      'environment':{'python':sys.version,'numpy':np.__version__,'platform':platform.platform()},
      'review_scope':'New independent saved-evidence verification; no submitted scientific scripts imported or executed.',
      'accounting':{'saved_updates':1800,'center_update_decompositions':14400,'velocity_components':43200,
          'shared_prefix_updates_counted_once':200,'same_phase_pair_phase_rows':1400,'same_phase_center_pairs':11200,
          'cross_arm_update_rows':800,'cross_arm_center_pairs':6400,'fixed_algebra_fixtures':nfixtures,
          'new_rollout_updates':0,'engine_calls':0,'position_successors_calculated':0,'RNG_samples':0,'RNG_restorations':0,
          'submitted_checkers_executed':0,'old_preflight_reanalyses':0},
      'provenance':provenance,'source_reconstruction':maxsource,
      'scalar_dispersion':ss,'report_anchors':reports,
      'same_phase_nonexpansion_max_signed_excess':max(a['nonexpansion_max_signed_excess'] for a in pairs['same_phase']),
      'cross_arm_nonexpansion_max_signed_excess':max(a['nonexpansion_max_signed_excess'] for a in pairs['cross_arm']),
      'reviewer_mathematical_notes':{'q_upper_bound_from_periodic_box':qbound,'threshold_0_999_unattainable':qbound<.999,
        'phase_mean_incoming_post_variance_difference_is_a_boundary_term':True},
      'all_csv_tables_checked':10,'numerical_and_metadata_check_groups':len(CHECKS),'checks':CHECKS}
    # Verify read-only inputs still match the archive manifest after all calculations.
    for n,row in js(root/'SIM03_REVIEW_MANIFEST.json')['files'].items():assert ident(root/n)=={k:row[k] for k in ('bytes','sha256')}
    with dest.open('x',encoding='utf-8') as f:json.dump(outcome,f,indent=2,ensure_ascii=False,allow_nan=False);f.write('\n')
    print(json.dumps({k:outcome[k] for k in ['status','accounting','source_reconstruction','numerical_and_metadata_check_groups']},indent=2))

if __name__=='__main__': main()
