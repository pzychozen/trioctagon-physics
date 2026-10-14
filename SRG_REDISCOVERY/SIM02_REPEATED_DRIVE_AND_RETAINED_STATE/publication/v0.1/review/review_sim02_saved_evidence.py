"""Independent passive SIM02 review. No imports from the submission; no rollout.

Each scratch transition starts from its saved predecessor. Its output is never
used as input for another transition. Isolated RNG replay checks recorded draws
and complete checkpoints; it does not drive a simulated trajectory.

Usage: python -B review_sim02_saved_evidence.py --bundle-root EXTRACTED_ZIP \
    --archive SIM02_GPT_REVIEW.zip --output-dir SEPARATE_REVIEW_OUTPUT
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import zipfile
import numpy as np

TOL = 1e-13
PINS = {
 'sources/source_C.py':'e13b92df8ac6df78cfee75b95dacea3b106e96bd5be9bf798cdcf39ccc5bc75c',
 'detached/engine_C.py':'05866296f874c5ec462426cf39bfd3518d8d9b3ea9274cb0f4915811532d395b',
 'engine_api.py':'05b0fc0ca4fef819b779b948696b6271070f9443c76ce6a5c3259d8c0d823e0a',
 'worker_replay.py':'2d47fb3de7956694120407691f6819736dc1adcd243162714b0818a5254728c3',
 'runs/C/states.npz':'693dd94699259b8d9d855c8a513b692d3f4616f6df481ec05eb0be7502134685',
 'runs/C/RNG_FINAL.json':'4a93dd4c6999db4e47e96c5c1032e85e0c042a81ae86dc8adecd223d25cecc3e',
 'SIM01_REPORT.md':'0a3f19ff7c0bc45c6665f4a780653dd9681e288bfe0b9016e2cda25d11ed9e48',
 'review/SIM01_GPT_SCIENTIFIC_REVIEW.md':'6c8cd8cd27d6a01f675d3bc545782bc90173a70a61893982a5405e32533d350b',
 'ACCESS_AND_EVIDENCE_MAP.md':'a272a627979d4a0ffa3b391c218041da84ce680fed0d0724a97aec3668314cc9',
}

def require(value, message):
    if not bool(value): raise AssertionError(message)

def read_json(path): return json.loads(Path(path).read_text(encoding='utf-8'))

def ident(path):
    data = Path(path).read_bytes()
    return {'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()}

def load_npz(path):
    with np.load(path, allow_pickle=False) as z: return {k:z[k] for k in z.files}

def maxerr(a,b):
    a,b=np.asarray(a),np.asarray(b)
    require(a.shape==b.shape, 'shape disagreement')
    return float(np.max(np.abs(a.astype(float)-b.astype(float)), initial=0))

def near(a,b,label,tol=TOL):
    e=maxerr(a,b); require(e<=tol, f'{label}: residual {e} > {tol}');return e

def exact(a,b,label):
    require(np.array_equal(a,b,equal_nan=True),label)

def state_ident(a):
    return {k:{'shape':list(v.shape),'dtype':str(v.dtype),
               'sha256':hashlib.sha256(v.tobytes(order='C')).hexdigest()} for k,v in a.items()}

def checkpoint_dict(rng):
    a,k,p,g,c=rng.get_state()
    return dict(algorithm=a,keys=k.tolist(),position=int(p),has_gauss=int(g),cached_gaussian=float(c))

def rng_restore(data):
    require(data['algorithm']=='MT19937' and len(data['keys'])==624,'RNG schema')
    # Constructor seed is overwritten before any sample. Does not touch global RNG.
    r=np.random.RandomState(0)
    r.set_state((data['algorithm'],np.asarray(data['keys'],dtype=np.uint32),
                 data['position'],data['has_gauss'],data['cached_gaussian']))
    require(checkpoint_dict(r)==data,'RNG roundtrip')
    return r

def h_of_frame(f):
    t=int(f)*0.1
    return (2.0*np.exp(-0.5*t)*np.cos(t)+1.0*np.exp(-0.3*t)*np.sin(t)
            +1.5*np.exp(-0.7*t)+1.0*np.exp(-0.4*t))

def scratch_successor(p0,v0,b0,frame,draws):
    """One independent recorded-transition evaluation, never a chained rollout."""
    p=p0.copy();v=v0.copy();b=b0.copy()
    g=1.0/(1.0+np.mean(np.linalg.norm(v,axis=1)))
    h=h_of_frame(frame)
    for i in range(8):
        center=np.mean(p,axis=0)
        d=np.mod(center-p[i]+5.0,10.0)-5.0
        norm=np.linalg.norm(d)+0.01
        if g>0.5:
            require(np.isfinite(draws[i]),'open gate missing saved draw')
            if draws[i]<0.01: b[i]=1-b[i]
        else: require(np.isnan(draws[i]),'closed gate has saved draw')
        force=d/norm*h*(-1 if b[i] else 1)
        v[i]+=0.1*force*g
        v[i]=v[i]/(1+np.log1p(np.abs(v[i])))
        p[i]+=0.1*v[i]
        p[i]=np.mod(p[i],10.0)
    return p,v,b,g,h

def speed(v): return np.linalg.norm(v,axis=-1).mean(axis=-1)

def separation(p):
    # Independent explicit 28-pair readout.
    return np.stack([np.linalg.norm((p[...,i,:]-p[...,j,:]+5)%10-5,axis=-1)
                     for i in range(8) for j in range(i+1,8)],axis=-1).mean(axis=-1)

def differences(p,q,v,w,b,d):
    dp=np.linalg.norm((p-q+5)%10-5,axis=-1);dv=np.linalg.norm(v-w,axis=-1)
    return {'position_mean':dp.mean(axis=-1),'position_max':dp.max(axis=-1),
            'velocity_mean':dv.mean(axis=-1),'velocity_max':dv.max(axis=-1),
            'bit_hamming':(b!=d).sum(axis=-1)}

def scalar(x): return x.item() if isinstance(x,np.generic) else x

def first(mask,offset=0):
    q=np.flatnonzero(mask);return None if not len(q) else int(q[0]+offset)

def audit_archive(root, archive):
    manifest=read_json(root/'SIM02_REVIEW_MANIFEST.json')
    names=set(manifest['files'])|{'SIM02_REVIEW_MANIFEST.json'}
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    require(names==actual,'manifest file inventory')
    for name,record in manifest['files'].items():
        ii=ident(root/name)
        require(all(ii[k]==record[k] for k in ii),'manifest identity '+name)
    with zipfile.ZipFile(archive) as z:
        nn=z.namelist()
        require(len(nn)==len(set(nn))==len({n.casefold() for n in nn}),'ZIP collision')
        require(set(nn)==names,'ZIP inventory')
        require(z.testzip() is None,'ZIP CRC')
        for n in nn:
            require(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts
                    and '\\' not in n and ':' not in n,'unsafe ZIP path')
            require(z.read(n)==(root/n).read_bytes(),'extracted identity '+n)
    publication=read_json(root/'inputs/PUBLICATION_MANIFEST.json')['files']
    for path,pin in PINS.items():
        ii=ident(root/'inputs'/path)
        require(ii['sha256']==pin,'independent accepted anchor '+path)
        require(ii==publication[path],'accepted publication entry '+path)
    before=read_json(root/'evidence/INPUTS_BEFORE.json')
    after=read_json(root/'evidence/PRESERVATION_AFTER.json')['after']
    require(before==after,'before/after preservation receipts disagree')
    for name,ii in before['accepted_inputs'].items():
        require(ident(root/'inputs'/name)=={k:ii[k] for k in ['bytes','sha256']},'copied input '+name)
    spec=read_json(root/'EXPERIMENT_SPEC.json')
    require(ident(root/'EXPERIMENT_SPEC.json')=={k:read_json(root/'evidence/CHECKPOINT_GATE.json')['spec_identity'][k]
                                             for k in ['bytes','sha256']},'frozen spec')
    for name,ii in spec['initial_wrapper_identities'].items():
        require(ident(root/name)=={k:ii[k] for k in ['bytes','sha256']},'frozen script '+name)
    return dict(status='PASS',archive=ident(archive),archive_members=len(names),
                verified_manifest_payloads=len(manifest['files']),accepted_pinned_payloads=len(PINS),
                copied_inputs_checked=len(before['accepted_inputs']),
                protected_file_receipts_equal=len(before['modified_tracked']),
                frozen_scripts_checked=len(spec['initial_wrapper_identities']),
                uncompressed_archive_payload_bytes=sum((root/n).stat().st_size for n in names),
                external_transport_seal_supplied=(root/'SIM02_TRANSPORT_SEAL.json').exists(),
                preservation_boundary='Submitted receipts and copied inputs; no direct Windows filesystem inspection.')

def audit_arm(root, arm, prefix, rng0):
    a=load_npz(root/f'runs/{arm}/states.npz')
    require(a['positions'].shape==(801,8,3) and a['velocities'].shape==(801,8,3),'state shape')
    require(a['positions'].dtype==np.float64 and a['velocities'].dtype==np.float64,'state dtype')
    require(a['bits'].shape==(801,8) and a['bits'].dtype==np.int64,'native bit dtype')
    for k in ('positions','velocities','bits'):exact(a[k][0],prefix[k][-1],'branch '+k)
    require(np.isfinite(a['positions']).all() and np.isfinite(a['velocities']).all(),'finite state')
    require(((a['positions']>=0)&(a['positions']<10)).all() and np.isin(a['bits'],[0,1]).all(),'state domains')
    exact(a['state_index'],np.arange(200,1001),'state labels')
    exact(a['update_index'],np.arange(200,1000),'update labels')
    frames=np.arange(200,1000) if arm=='CONTINUOUS' else np.arange(200,1000)%200
    exact(a['source_frame'],frames,'frame schedule');exact(a['source_time'],frames*.1,'source clock')
    gg=1/(1+speed(a['velocities'][:-1]));near(gg,a['G'],'incoming G')
    exact(a['gate'],gg>.5,'gate');exact(a['draw_count'],np.where(a['gate'],8,0),'draw counts')
    exact(a['draw_mask'],np.isfinite(a['draws']),'draw mask')
    exact(a['draw_mask'],np.broadcast_to(a['gate'][:,None],(800,8)),'frozen gate masks')
    exact(a['bit_changes'],a['bits'][1:]!=a['bits'][:-1],'bit differences')
    exact(a['bit_changes'],a['draw_mask']&(a['draws']<.01),'toggle source rule')
    rng=rng_restore(rng0)
    require(read_json(root/f'runs/{arm}/rng/S0200.json')==rng0,'branch RNG file')
    branch=read_json(root/f'runs/{arm}/BRANCH.json')
    require(branch['rng']==rng0 and branch['state']==state_ident({k:a[k][0] for k in ('positions','velocities','bits')}),'branch signatures')
    errs={'position':0.,'velocity':0.,'H':0.,'G':0.};offset=0
    for j in range(800):
        if a['gate'][j]:
            expected=np.array([rng.random_sample() for _ in range(8)])
            exact(expected,a['draws'][j],'native RNG stream')
            exact(a['draw_offset'][j],np.arange(offset,offset+8),'stream offset');offset+=8
        else: exact(a['draw_offset'][j],np.full(8,-1),'closed offsets')
        pp,vv,bb,g,h=scratch_successor(a['positions'][j],a['velocities'][j],a['bits'][j],frames[j],a['draws'][j])
        for key,x,y in [('position',pp,a['positions'][j+1]),('velocity',vv,a['velocities'][j+1]),
                        ('H',h,a['H'][j]),('G',g,a['G'][j])]:
            errs[key]=max(errs[key],near(x,y,arm+' '+key))
        exact(bb,a['bits'][j+1],'scratch successor bits')
        if (j+1)%200==0:
            k=j+201
            require(checkpoint_dict(rng)==read_json(root/f'runs/{arm}/rng/S{k:04d}.json'),'boundary RNG')
            boundary=read_json(root/f'runs/{arm}/boundaries/S{k:04d}.json')
            require(boundary['state']==state_ident({key:a[key][j+1] for key in ('positions','velocities','bits')}),'boundary state hash')
            require(boundary['branch_draws_consumed']==offset,'boundary draw count')
    require(checkpoint_dict(rng)==read_json(root/f'runs/{arm}/RNG_FINAL.json'),'final RNG')
    raw=np.diff(a['positions'],axis=0);mi=(raw+5)%10-5
    exact(raw,a['raw_displacements'],'raw displacement');exact(mi,a['minimal_image_displacements'],'minimal displacement')
    det=np.linalg.norm(raw%10,axis=-1);near(det,a['detector_distance'],'detector norms')
    exact(det>1,a['detector_flags'],'detector flags')
    energy=.5*np.sum(np.linalg.norm(a['velocities'][1:],axis=2)**2,axis=1)
    ee=near(energy,a['energy'],'post source energy')
    inc=.1*a['velocities'][1:];lift=np.abs(inc-mi).max(axis=(1,2))
    near(np.abs(inc).max(axis=(1,2)),a['max_component_increment'],'increments')
    near(lift,a['max_lift_residual'],'lift residual series')
    require(np.abs(inc).max()<5 and lift.max()<=1e-12,'lift premise')
    journal=[json.loads(s) for s in (root/f'runs/{arm}/UPDATE_JOURNAL.jsonl').read_text().splitlines()]
    require(len(journal)==800,'journal count')
    for j,row in enumerate(journal):
        require(row['update_index']==j+200 and row['state_index']==j+201 and row['source_frame']==int(frames[j]),'journal indices')
        for key in ('positions','velocities','bits'):exact(row[key],a[key][j+1],'journal state '+key)
        for key in ('H','G','energy'):exact(row['meta'][key],a[key][j],'journal '+key)
        require(row['meta']['t']==a['source_time'][j],'journal time')
        require(row['branch_draw_offset_before']==int(a['draw_count'][:j].sum()),'journal offset')
        dr=row['meta']['draws'];require(len(dr)==int(a['draw_count'][j]),'journal draws')
        for i,d in enumerate(dr):require(d=={'body':i,'value':float(a['draws'][j,i])},'journal draw value/assignment')
        require([x['body'] for x in row['meta']['detector_events']]==np.flatnonzero(det[j]>1).tolist(),'journal detector bodies')
    stream=[json.loads(s) for s in (root/f'runs/{arm}/DRAW_STREAM.jsonl').read_text().splitlines()]
    slots=np.argwhere(a['draw_mask']);require(len(stream)==offset,'stream length')
    for q,(row,(j,i)) in enumerate(zip(stream,slots)):
        require(row=={'branch_draw_offset':q,'dynamics_draw_offset':q+1600,'update_index':int(j+200),
                      'center':int(i),'value':float(a['draws'][j,i])},'draw stream row')
    ss=speed(a['velocities']);sep=separation(a['positions'])
    summary={'transitions_checked':800,'RNG_scalar_values_reproduced':offset,'full_RNG_checkpoints_verified':5,
             'max_transition_residuals':errs,'max_energy_residual':ee,
             'final_mean_speed':float(ss[-1]),'final_mean_pair_separation':float(sep[-1]),
             'final_source_energy':float(energy[-1]),'final_bits':a['bits'][-1].tolist(),
             'new_mean_speed_mean':float(ss[1:].mean()),'new_speed_cycle_means':ss[1:].reshape(4,200).mean(axis=1).tolist(),
             'new_cycle_speed_peaks':ss[1:].reshape(4,200).max(axis=1).tolist(),
             'new_first_responses':ss[1:].reshape(4,200)[:,0].tolist(),
             'gate_open_updates':int(a['gate'].sum()),'G_min':float(gg.min()),'G_max':float(gg.max()),
             'new_switches':int(a['bit_changes'].sum()),'legacy_flags':int((det>1).sum()),
             'minimal_image_steps_above_1':int((np.linalg.norm(mi,axis=-1)>1).sum()),
             'wrapped_body_crossings':int((np.abs(raw-mi)>1e-12).any(axis=-1).sum()),
             'max_minimal_image_step':float(np.linalg.norm(mi,axis=-1).max()),
             'max_absolute_increment_component':float(np.abs(inc).max()),'max_lift_residual':float(lift.max()),
             'journal_successors_checked':len(journal),'draw_stream_rows_checked':len(stream)}
    return a,summary

def audit_preflight(root,prefix,rng0):
    rows=[]
    for name,frame in [('01_C_UNOBSERVED',200),('02_C_OBSERVED',200),('03_R_UNOBSERVED',0),('04_R_OBSERVED',0)]:
        d=root/'evidence/preflight'/name
        before=load_npz(d/'before.npz');after=load_npz(d/'after.npz');meta=read_json(d/'META.json')
        for k in ('positions','velocities','bits'):exact(before[k],prefix[k][-1],'preflight branch')
        require(read_json(d/'BRANCH.json')['rng']==rng0,'preflight branch RNG')
        rng=rng_restore(rng0);draws=np.array([rng.random_sample() for _ in range(8)])
        require(checkpoint_dict(rng)==read_json(d/'RNG_AFTER.json'),'preflight RNG successor')
        pp,vv,bb,g,h=scratch_successor(before['positions'],before['velocities'],before['bits'],frame,draws)
        erp=near(pp,after['positions'],'preflight p');erv=near(vv,after['velocities'],'preflight v');exact(bb,after['bits'],'preflight b')
        near(h,meta['H'],'preflight H');near(g,meta['G'],'preflight G')
        if 'draws' in meta:
            require(meta['draws']==[dict(body=i,value=float(draws[i])) for i in range(8)],'preflight logged draws')
            require([(x['event'],x['i']) for x in meta['trace']]==[(ev,i) for i in range(8) for ev in ('before','after')],'trace sequence')
            for x in meta['trace']:
                i=x['i'];count=i+(x['event']=='after')
                for key in ('positions','velocities'):
                    expected=before[key].copy();expected[:count]=after[key][:count]
                    exact(expected,x[key],'preflight sequential trace')
        progress=read_json(d/'PROGRESS.json');require(progress['started']==progress['completed']==1,'preflight counts')
        rows.append(dict(id=name,frame=frame,max_position_residual=erp,max_velocity_residual=erv))
    for a,b in [('01_C_UNOBSERVED','02_C_OBSERVED'),('03_R_UNOBSERVED','04_R_OBSERVED')]:
        x=load_npz(root/'evidence/preflight'/a/'after.npz');y=load_npz(root/'evidence/preflight'/b/'after.npz')
        for k in x:
            require(x[k].dtype==y[k].dtype and x[k].tobytes()==y[k].tobytes(),'preflight pair byte equality')
        require(read_json(root/'evidence/preflight'/a/'RNG_AFTER.json')==read_json(root/'evidence/preflight'/b/'RNG_AFTER.json'),'pair full RNG')
    return rows

def audit_comparisons(root,prefix,runs):
    joined={}
    for arm,a in runs.items():
        z={k:np.concatenate([prefix[k][:-1],a[k]]) for k in ('positions','velocities','bits')}
        for k in ('H','G','source_time','source_frame','energy','draw_count'):z[k]=np.concatenate([prefix[k],a[k]])
        z['mean_speed']=speed(z['velocities']);z['mean_pair_separation']=separation(z['positions'])
        joined[arm]=z
    C,R=joined['CONTINUOUS'],joined['REPEATED'];arrays=load_npz(root/'analysis/comparison_arrays.npz')
    expected={f'{arm}_{k}':a[k] for arm,a in joined.items() for k in ('mean_speed','mean_pair_separation','G','H')}
    cross=differences(C['positions'],R['positions'],C['velocities'],R['velocities'],C['bits'],R['bits'])
    expected.update({'cross_'+k:v for k,v in cross.items()})
    for k in ('mean_speed','mean_pair_separation','G','H'):
        expected['phase_'+k]=(R[k][1:] if k.startswith('mean_') else R[k]).reshape(5,200)
    exact(expected['phase_H'],np.tile(expected['phase_H'][0],(5,1)),'all phase H waveforms')
    summaries=[]
    for label,pairs in [('successive',[(c,c-1) for c in range(1,5)]),('versus_inherited',[(c,0) for c in range(1,5)])]:
        for c,d in pairs:
            sl=slice(200*c+1,200*c+201);tl=slice(200*d+1,200*d+201)
            diff=differences(R['positions'][sl],R['positions'][tl],R['velocities'][sl],R['velocities'][tl],R['bits'][sl],R['bits'][tl])
            expected.update({f'{label}_{c}_{d}_{k}':v for k,v in diff.items()})
            near_repeat=(diff['position_mean']<=1e-12)&(diff['position_max']<=1e-12)&(diff['velocity_mean']<=1e-12)&(diff['velocity_max']<=1e-12)&(diff['bit_hamming']==0)
            summaries.append({'comparison':label,'cycle':c,'reference_cycle':d,'near_repeat_phases':int(near_repeat.sum()),
                              'exact_position_phases':int(np.all(R['positions'][sl]==R['positions'][tl],axis=(1,2)).sum()),
                              'exact_velocity_phases':int(np.all(R['velocities'][sl]==R['velocities'][tl],axis=(1,2)).sum()),
                              'exact_bit_phases':int(np.all(R['bits'][sl]==R['bits'][tl],axis=1).sum()),
                              **{k+'_min':float(v.min()) for k,v in diff.items()},
                              **{k+'_max':float(v.max()) for k,v in diff.items()}})
    require(set(arrays)==set(expected),'comparison array keys');errs={k:near(v,arrays[k],'comparison '+k) for k,v in expected.items()}
    csv_counts={}
    for name in ['cross_arm_all_states.csv','cross_arm_boundaries.csv']:
        rows=list(csv.DictReader((root/'analysis'/name).open(newline='',encoding='utf-8')));csv_counts[name]=len(rows)
        for row in rows:
            k=int(row['state_index'])
            for field,v in cross.items():near(float(row[field]),v[k],'CSV cross '+field)
    rows=list(csv.DictReader((root/'analysis/scalar_readouts.csv').open(newline='',encoding='utf-8')))
    csv_counts['scalar_readouts.csv']=len(rows)
    for row in rows:
        n=int(row['update_index']);a=joined[row['arm']]
        require(int(row['response_state_index'])==n+1 and int(row['source_frame'])==int(a['source_frame'][n]),'scalar CSV indices')
        for field,value in [('source_time',a['source_time'][n]),('H',a['H'][n]),('incoming_G',a['G'][n]),
                            ('post_mean_speed',a['mean_speed'][n+1]),('post_mean_pair_separation',a['mean_pair_separation'][n+1]),
                            ('post_source_energy',a['energy'][n]),('draw_count',a['draw_count'][n])]:near(float(row[field]),value,'scalar CSV '+field)
    rows=list(csv.DictReader((root/'analysis/repeated_phase_curves.csv').open(newline='',encoding='utf-8')))
    csv_counts['repeated_phase_curves.csv']=len(rows)
    for row in rows:
        c,j=int(row['cycle']),int(row['phase'])
        for key in ('H','G','mean_speed','mean_pair_separation'):near(float(row[key]),expected['phase_'+key][c,j],'CSV phase')
    rows=list(csv.DictReader((root/'analysis/same_phase_labeled_differences.csv').open(newline='',encoding='utf-8')))
    csv_counts['same_phase_labeled_differences.csv']=len(rows)
    for row in rows:
        pre=f"{row['comparison']}_{row['cycle']}_{row['reference_cycle']}_";j=int(row['phase'])
        for key in cross:near(float(row[key]),expected[pre+key][j],'CSV same-phase')
    result=read_json(root/'analysis/RESULTS.json')
    for s,t in zip(summaries,result['same_phase_summary']):
        for k in s:
            if isinstance(s[k],str):require(s[k]==t[k],'phase result category')
            else:near(s[k],t[k],'phase result '+k)
    for arm,z in joined.items():
        for key,value in [('final_mean_speed',z['mean_speed'][-1]),('final_mean_pair_separation',z['mean_pair_separation'][-1]),
                          ('final_source_energy',z['energy'][-1])]:near(value,result['arms'][arm][key],'result endpoint')
    require(np.array_equal(runs['CONTINUOUS']['draws'],runs['REPEATED']['draws'],equal_nan=True),'cross-arm draws')
    exact(C['bits'],R['bits'],'cross-arm bits')
    divergence={k:first(np.any(C[field]!=R[field],axis=tuple(range(1,C[field].ndim))))
                for k,field in [('positions','positions'),('velocities','velocities'),('bits','bits')]}
    boundaries=[{'state_index':k,**{name:scalar(a[k]) for name,a in cross.items()}} for k in [200,400,600,800,1000]]
    cblock=C['mean_speed'][1:].reshape(5,200).mean(axis=1);rblock=R['mean_speed'][1:].reshape(5,200).mean(axis=1)
    return dict(comparison_arrays_checked=len(expected),max_comparison_array_residual=max(errs.values()),
                csv_rows_checked=csv_counts,first_cross_arm_state_difference=divergence,
                same_phase_summary=summaries,unique_cycle_pair_comparisons=7,unique_same_phase_pairs=1400,
                cross_arm_boundaries=boundaries,all_cross_arm_draw_assignments_equal=True,all_cross_arm_bits_equal=True,
                repeated_H_exactly_equal_all_five_cycles=True,
                cycles=[dict(cycle=c,continuous_mean_speed=float(cblock[c]),repeated_mean_speed=float(rblock[c]),
                             ratio=float(rblock[c]/cblock[c]),repeated_peak_speed=float(expected['phase_mean_speed'][c].max())) for c in range(5)],
                reviewer_derived_ratios={'final_mean_speed_R_over_C':float(R['mean_speed'][-1]/C['mean_speed'][-1]),
                                        'all_new_post_update_mean_speed_R_over_C':float(R['mean_speed'][201:].mean()/C['mean_speed'][201:].mean())})

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bundle-root',type=Path,required=True);ap.add_argument('--archive',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True)
    args=ap.parse_args();root=args.bundle_root.resolve();out=args.output_dir.resolve()
    require(not out.is_relative_to(root),'Output must be outside evidence inputs')
    out.mkdir(parents=True,exist_ok=True)
    archive=audit_archive(root,args.archive)
    prefix=load_npz(root/'inputs/runs/C/states.npz');rng0=read_json(root/'inputs/runs/C/RNG_FINAL.json')
    preflight=audit_preflight(root,prefix,rng0)
    runs={};arms={}
    for arm in ['CONTINUOUS','REPEATED']:runs[arm],arms[arm]=audit_arm(root,arm,prefix,rng0)
    comparisons=audit_comparisons(root,prefix,runs)
    ledger=read_json(root/'evidence/BUDGET_LEDGER.json');require(ledger['accounting']['started']==ledger['accounting']['completed']==1604,'call accounting')
    for p in ledger['processes']:
        require(p['status']=='COMPLETE' and p['returncode']==0 and p['elapsed_seconds']<=p['wall_cap_seconds'],'process cap/completion')
    require(read_json(root/'evidence/PREFLIGHT_GATE.json')['elapsed_seconds_total']<=60,'preflight cap')
    require(ledger['peak_observed_aggregate_bytes']<=268435456,'recorded output cap')
    require(audit_archive(root,args.archive)==archive,'review altered evidence')
    result=dict(status='PASS',environment={'python':sys.version,'numpy':np.__version__},
                passive_transition_absolute_tolerance=TOL,
                accounting={'new_rollout_updates':0,'source_engine_calls':0,'new_saved_continuation_transition_evaluations':1600,
                            'saved_preflight_transition_evaluations':4,'inherited_SIM01_transition_evaluations':0,
                            'isolated_reviewer_RNG_variates_reproduced':12832,
                            'inherited_SIM01_RNG_variates_regenerated':0},
                archive=archive,preflight=preflight,arms=arms,comparisons=comparisons,
                execution_receipt_checks={'started':1604,'completed':1604,'supervised_processes':len(ledger['processes']),
                                          'recorded_caps_pass':True,'external_post_archive_aggregate_not_independently_inspected':True})
    for name,obj in [('INDEPENDENT_REVIEW_RESULTS.json',result),('ARCHIVE_REVIEW.json',archive)]:
        (out/name).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','accounting':result['accounting'],'archive':archive,'arms':arms,
                      'comparison_ratios':comparisons['reviewer_derived_ratios']},indent=2))

if __name__=='__main__':main()
