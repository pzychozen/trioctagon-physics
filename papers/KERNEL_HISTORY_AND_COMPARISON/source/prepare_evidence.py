"""Read accepted inert P3 results; never import or execute either kernel.
Creates only the minimal local-review plot/table projection and its source map.
Redistribution of the external authority remains separately pending.
"""
from pathlib import Path
import argparse,hashlib,json,math,sys
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--p3',type=Path,required=True);a=parser.parse_args();P=a.p3.resolve()
used={}
def read(name):
 p=P/name;raw=p.read_bytes();used[name]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def save(name,value):(ROOT/'evidence'/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
F=read('inputs.json');O=read('one_comparison.json');G=read('one_gate.json');T=read('trajectory_comparison.json');S=read('trajectory_summary.json');I=read('insights.json');B=read('bindings.json');V=read('validation.json');HI=read('history_comparison.json')
assert len(F['vectors'])==26 and len(O['control'])==78 and G['shared_successes']==75 and G['shared_refusals']==3
assert all(r['status_equal'] and (r.get('exact_tokens') and r.get('prephase_exact_tokens') or r.get('both_refused')) for r in O['control'])
assert T['matched_updates']==76800 and T['matched_samples']==76875 and len(T['controls'])==75 and not T['unexpected']
assert all(r['samples']==1025 and r['all_tokens_and_statuses_match'] and not r['mismatches'] for r in T['controls'])
assert all(r['mapped_rows_and_terminal_exact'] for r in HI) and len(HI)==16
assert V['H2_one_exact']==39 and V['H2_multistep_exact']==640 and V['H6B_state_clock_memory_observers_exact']==640
index={(r['profile'],r['vector']):r for r in read('current_trajectory_index.json')}
hindex={(r['profile'],r['vector']):r for r in read('historical_trajectory_index.json')}
projection={};field_counts={}
for p in F['profiles']:
 r=index[p,'gate_seed'];rows=read(r['path']);assert used[r['path']]==r['sha256']
 if p!='CURRENT_L01':
  h=hindex[p,'gate_seed'];hist=read(h['path']);assert used[h['path']]==h['sha256']
  assert all(x['omega']==y['omega'] and x['prephase']==y['prephase'] for x,y in zip(hist[1:],rows[1:]))
  assert all(x['staged']==y['staged'] and x['ema']==y['ema'] and x['memory']==y['memory'] for x,y in zip(hist,rows))
  summary=next(r for r in S if r['profile']==p and r['vector']=='gate_seed')
  metrics=read('metrics/'+p+'__gate_seed.json')
 else:summary=None;metrics=None
 points=[]
 for n,row in enumerate(rows):
  # Use all n for distance/EMA; channel plot needs the first 129 and terminal.
  v=[complex(float.fromhex(x),float.fromhex(y)) for x,y in row['omega']]
  point={'n':n,'m':row['memory']['value']}
  if n<=128 or n==1024:point['magnitudes']=[abs(z) for z in v]
  if metrics:point.update(raw=metrics[n]['difference']['l2'],aligned=metrics[n]['difference']['aligned_l2'])
  points.append(point)
 projection[p]={'k_hex':F['profiles'][p]['k'],'points':points,'terminal':I[p],'summary':None if summary is None else {k:summary[k] for k in ['terminal_difference','historical_settling','max_phase_angle']}}
for lane in ['historical','current']:
 closure=read(lane+'_trajectory_closure.json');assert closure['numpy']=='2.4.4' and not any(n.split('.')[0] in closure['forbidden_roots'] for n in closure['modules'])
 field_counts[lane]={'python':closure['version'],'numpy':closure['numpy']}
data={'status':'LOCAL_REVIEW_DERIVED_EXCERPT_NOT_APPROVED_FOR_PUBLIC_REDISTRIBUTION','baseline':'9c9e579e97aac0cdc7524b0d05430d0d76e39ce4','seed_id':'gate_seed','omega_hex':F['vectors']['gate_seed']['omega'],'eps_hex':F['profiles']['CURRENT_L01']['eps'],'g_hex':F['profiles']['CURRENT_L01']['g'],'lambda_hex':F['profiles']['CURRENT_L01']['phase'],'horizon':1024,'profiles':projection,'population':{'inputs':26,'one_success':75,'one_refused':3,'paired_trajectories':75,'updates':76800,'samples':76875,'history_mappings':16,'observer_counts':T['counts']},'source_sha256':used}
save('figure_table_data.json',data)
save('source_identities.json',{'scope':'Source identities only; no original reports, archives or raw full trajectories redistributed. P3 root supplied by the reviewer.','p3_members':used,'environments':field_counts,'wheels':{k:{'sha256':v['wheel_sha256'],'scientific_member_count':len(v['members'])} for k,v in B.items()}})
save('data_consistency.json',{'status':'PASS','source_data_executed':False,'kernels_imported':False,'checks':['26 deterministic inputs; 78 matched first-step records = 75 successes + 3 joint overflow refusals','75 paired controls, each 1025 samples = 76800 updates plus 75 initial samples','All accepted control fields/statuses exact; gate-seed raw records independently rechecked for state/prephase and both observer/memory values','Separate H6B/H2 population 39 and 640 retained, not added to P3 counts','16 history mappings exact','All seven selected raw trajectories match accepted index hashes','Python 3.11.15 and NumPy 2.4.4 recorded independently for both P3 environments'],'source_files_read':len(used)})
assert not any(x.startswith(('kernel_physics','trioctagon_historical_kernel')) for x in sys.modules)
print('PASS: accepted inert evidence checked; local-review projection written; no scientific execution.')
