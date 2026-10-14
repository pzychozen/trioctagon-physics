"""One authorized source-style initialization and one monotone finite replay."""
import argparse
import json
import os
import platform
import sys
import time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR']=str(ROOT/'cache/matplotlib')
os.environ['TMP']=os.environ['TEMP']=str(ROOT/'tmp')
from engine_api import load_engine,observed_step,rng_json,write_json
import numpy as np

parser=argparse.ArgumentParser();parser.add_argument('source',choices=['A','B','C']);args=parser.parse_args()
name=args.source;N={'A':500,'B':2000,'C':200}[name]
out=ROOT/'runs'/name
out.mkdir(exist_ok=False)
write_json(out/'STARTED.json',{'source':name,'requested_updates':N,'seed':2038,'restart_allowed':False})
started=time.monotonic()
engine=load_engine(name)
np.random.seed(2038)
before_init=rng_json()
engine.initialize()
initial_rng=rng_json()
initial_p=engine.positions.copy();initial_v=engine.velocities.copy()
size=initial_p.shape
positions=np.empty((N+1,)+size);velocities=np.empty_like(positions)
positions[0]=initial_p;velocities[0]=initial_v
bits=np.zeros((N+1,len(initial_p)),dtype=np.int8) if name=='C' else np.empty((N+1,0),dtype=np.int8)
if name=='C': bits[0]=engine.rule_state
h=np.empty(N);g=np.full(N,np.nan);source_time=np.empty(N)
draws=np.full((N,len(initial_p)),np.nan);draw_count=np.zeros(N,dtype=np.int16)
energy=np.full(N,np.nan);detector_flags=np.zeros((N,len(initial_p)),dtype=bool)
detector_distance=np.full((N,len(initial_p)),np.nan)
write_json(out/'RNG_INITIAL.json',{'generator':'NumPy legacy global RandomState / MT19937',
    'seed':2038,'before_original_initialization':before_init,'after_original_initialization':initial_rng})
np.savez_compressed(out/'initial_state.npz',positions=initial_p,velocities=initial_v,bits=bits[0])
progress={'source':name,'requested':N,'started':0,'completed':0,'status':'RUNNING'}
completed=0;status='COMPLETE';error=None
try:
    for frame in range(N):
        progress['started']=frame+1;write_json(out/'PROGRESS.json',progress)
        meta=observed_step(engine,name,frame,observed=True)
        completed=frame+1
        positions[completed]=engine.positions;velocities[completed]=engine.velocities
        h[frame]=meta['H'];source_time[frame]=meta['t']
        if meta['G'] is not None:g[frame]=meta['G']
        if name=='C':
            bits[completed]=engine.rule_state;energy[frame]=meta['energy']
            for d in meta['draws']:draws[frame,d['body']]=d['value']
            draw_count[frame]=len(meta['draws'])
            for e in meta['detector_events']:detector_flags[frame,e['body']]=True
            detector_distance[frame]=np.linalg.norm(np.mod(positions[completed]-positions[completed-1],10),axis=1)
            assert np.array_equal(detector_flags[frame],detector_distance[frame]>1)
        progress['completed']=completed;write_json(out/'PROGRESS.json',progress)
        if not (np.isfinite(engine.positions).all() and np.isfinite(engine.velocities).all()):
            status='NONFINITE_STOP';break
except Exception as e:
    status='ERROR_STOP';error=repr(e)
finally:
    progress['status']=status;write_json(out/'PROGRESS.json',progress)
    write_json(out/'RNG_FINAL.json',rng_json())
    p=positions[:completed+1];v=velocities[:completed+1]
    L=2. if name=='A' else 10.
    raw=np.diff(p,axis=0)
    minimal=np.mod(raw+L/2,L)-L/2
    unwrapped=np.concatenate([p[:1],p[:1]+np.cumsum(minimal,axis=0)],axis=0)
    np.savez_compressed(out/'states.npz',positions=p,velocities=v,bits=bits[:completed+1],
        update_index=np.arange(completed),source_frame=np.arange(completed),source_time=source_time[:completed],
        H=h[:completed],G=g[:completed],energy=energy[:completed],draws=draws[:completed],
        draw_count=draw_count[:completed],detector_flags=detector_flags[:completed],
        detector_distance=detector_distance[:completed],raw_displacements=raw,
        minimal_image_displacements=minimal,unwrapped_positions=unwrapped)
    record={'source':name,'status':status,'requested_updates':N,'started_updates':progress['started'],
        'completed_updates':completed,'error':error,'elapsed_seconds':time.monotonic()-started,
        'numpy':np.__version__,'python':sys.version,'platform':platform.platform(),
        'output_bytes':sum(x.stat().st_size for x in out.iterdir() if x.is_file()),
        'clock':'One numerical call per source index, in increasing order; no GUI playback clock.',
        'missing_observables':'NaN in NPZ G/energy/detector arrays for inapplicable sources, and undrawn random slots; not a nonfinite state.'}
    write_json(out/'RUN_RESULT.json',record)
    print(json.dumps(record))
if status!='COMPLETE': raise SystemExit(2)
