"""Additional saved-array readouts; zero transition evaluations or RNG draws.

Usage: python -B review_sim02_readouts.py --bundle-root EXTRACTED_SUBMISSION \
    --output-dir SEPARATE_REVIEW_OUTPUT
"""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
import numpy as np

def load(path):
    with np.load(path,allow_pickle=False) as z:return {k:z[k] for k in z.files}

def check(ok,message):
    if not bool(ok):raise AssertionError(message)

def eq(a,b,label):
    check(abs(float(a)-float(b))<=1e-13,label)

def dist(p,q,v,w,b,d):
    pp=np.linalg.norm((p-q+5)%10-5,axis=-1);vv=np.linalg.norm(v-w,axis=-1)
    return dict(position_mean=pp.mean(axis=-1),position_max=pp.max(axis=-1),
                velocity_mean=vv.mean(axis=-1),velocity_max=vv.max(axis=-1),bit_hamming=(b!=d).sum(axis=-1))

def main(root,out):
    root=root.resolve();out=out.resolve();check(not out.is_relative_to(root),'output inside input')
    prefix=load(root/'inputs/runs/C/states.npz')
    runs={a:load(root/f'runs/{a}/states.npz') for a in ('CONTINUOUS','REPEATED')}
    joined={a:{k:np.concatenate([prefix[k][:-1],z[k]]) for k in ('positions','velocities','bits')} for a,z in runs.items()}
    r=joined['REPEATED'];res={}
    for name,a in runs.items():
        first_update=int(np.flatnonzero(a['bit_changes'].any(axis=1))[0]+200)
        centers=np.flatnonzero(a['bit_changes'][first_update-200]).tolist()
        res[name]=dict(first_new_toggle_update=first_update,first_new_toggle_successor=first_update+1,
                       first_new_toggle_centers=centers,no_toggle_at_update_200=not bool(a['bit_changes'][0].any()),
                       no_toggle_at_update_201=not bool(a['bit_changes'][1].any()))
    curves=load(root/'analysis/comparison_arrays.npz')
    read=lambda name:list(csv.DictReader((root/'analysis'/name).open(newline='',encoding='utf-8')))
    cycle_rows=read('repeated_cycle_summary.csv')
    for row in cycle_rows:
        c=int(row['cycle'])
        for name in ('H','G','mean_speed','mean_pair_separation'):
            q=curves['phase_'+name][c]
            for suffix,val in [('mean',q.mean()),('min',q.min()),('max',q.max()),('first',q[0]),('last',q[-1])]:
                eq(row[name+'_'+suffix],val,'cycle scalar CSV')
        flips=(r['bits'][200*c+1:200*c+201]!=r['bits'][200*c:200*c+200]).sum()
        eq(row['switches'],flips,'cycle switches')
    boundary_rows=read('repeated_cycle_boundaries.csv')
    for row in boundary_rows:
        k=int(row['state_index']);eq(row['mean_speed'],curves['REPEATED_mean_speed'][k],'boundary speed')
        eq(row['mean_pair_separation'],curves['REPEATED_mean_pair_separation'][k],'boundary separation')
        check(row['bits']==''.join(str(int(b)) for b in r['bits'][k]),'boundary bits')
        if k:
            delta=dist(r['positions'][k],r['positions'][k-200],r['velocities'][k],r['velocities'][k-200],r['bits'][k],r['bits'][k-200])
            for key,v in delta.items():eq(row[key],v,'boundary residual')
    summary_rows=read('same_phase_summary.csv');summaries={}
    for row in summary_rows:
        c,d=int(row['cycle']),int(row['reference_cycle']);sl=slice(200*c+1,200*c+201);tl=slice(200*d+1,200*d+201)
        delta=dist(r['positions'][sl],r['positions'][tl],r['velocities'][sl],r['velocities'][tl],r['bits'][sl],r['bits'][tl])
        for key,v in delta.items():
            eq(row[key+'_min'],v.min(),'phase min');eq(row[key+'_max'],v.max(),'phase max')
        ep=np.all(r['positions'][sl]==r['positions'][tl],axis=(1,2));ev=np.all(r['velocities'][sl]==r['velocities'][tl],axis=(1,2));eb=np.all(r['bits'][sl]==r['bits'][tl],axis=1)
        near=(delta['position_mean']<=1e-12)&(delta['position_max']<=1e-12)&(delta['velocity_mean']<=1e-12)&(delta['velocity_max']<=1e-12)&(delta['bit_hamming']==0)
        for key,values in [('exact_position_phases',ep),('exact_velocity_phases',ev),('exact_bit_phases',eb),('exact_all_phases',ep&ev&eb),('near_repeat_phases',near)]:eq(row[key],values.sum(),'phase counts')
        summaries[(row['comparison'],c,d)]=dict(exact_position=ep,exact_velocity=ev,exact_bits=eb,near_repeat=near)
    phase_rows=read('same_phase_labeled_differences.csv')
    for row in phase_rows:
        c,d,j=int(row['cycle']),int(row['reference_cycle']),int(row['phase'])
        check(int(row['response_state_index'])==200*c+j+1 and int(row['reference_state_index'])==200*d+j+1,'phase CSV indices')
        for key,v in summaries[(row['comparison'],c,d)].items():check((row[key]=='True')==bool(v[j]),'phase flag '+key)
    data={'status':'PASS','accounting':{'transition_evaluations':0,'RNG_draws':0,'new_rollout_updates':0},
          'additional_observation':'Schedule divergence at S_201 precedes first new toggle at update 202 / successor S_203.',
          'first_new_toggle':res,
          'additional_CSV_checks':{'repeated_cycle_summary.csv':len(cycle_rows),'repeated_cycle_boundaries.csv':len(boundary_rows),
                                   'same_phase_summary.csv':len(summary_rows),'same_phase_labeled_differences.csv_exact_near_flags':len(phase_rows)}}
    out.mkdir(parents=True,exist_ok=True)
    (out/'ADDITIONAL_READOUTS.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--bundle-root',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True)
    a=p.parse_args();main(a.bundle_root,a.output_dir)
