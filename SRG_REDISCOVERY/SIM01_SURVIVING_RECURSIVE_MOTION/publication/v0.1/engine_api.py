"""Detached loading and passive observation; no replacement numerical operator."""
import importlib.util
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent


def load_engine(name):
    spec=importlib.util.spec_from_file_location('detached_'+name,ROOT/'detached'/f'engine_{name}.py')
    engine=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(engine)
    return engine


def rng_json(state=None):
    s=np.random.get_state() if state is None else state
    return {'algorithm':s[0],'keys':s[1].tolist(),'position':int(s[2]),
            'has_gauss':int(s[3]),'cached_gaussian':float(s[4])}


def state_copy(engine):
    return {'positions':engine.positions.copy(),'velocities':engine.velocities.copy(),
            'bits':engine.rule_state.copy() if hasattr(engine,'rule_state') else None}


def set_state(engine,state):
    engine.positions=state['positions'].copy()
    engine.velocities=state['velocities'].copy()
    if state['bits'] is not None: engine.rule_state=state['bits'].copy()


def observed_step(engine,name,frame,observed=True,snapshots=False):
    previous=engine.positions.copy()
    draws=[]; trace=[]; current={'i':None}
    def visit(event,i,p,v):
        current['i']=int(i)
        if snapshots:
            trace.append({'event':event,'i':int(i),'positions':p.copy().tolist(),
                          'velocities':v.copy().tolist()})
    original_rand=np.random.rand
    def logged_rand(*args):
        value=original_rand(*args)
        assert not args, 'Source C gate must use a scalar draw'
        draws.append({'body':current['i'],'value':float(value)})
        return value
    try:
        if observed and name=='C': np.random.rand=logged_rand
        meta=engine.numerical_step(frame,_trace=visit if observed else None)
    finally:
        np.random.rand=original_rand
    if observed:
        if name=='C':
            meta['energy']=float(engine.compute_energy(engine.positions,engine.velocities))
            events=engine.detect_teleport(previous,engine.positions)
            meta['detector_events']=[{'body':int(i),'distance':float(d),
                'new':new.copy().tolist(),'previous':old.copy().tolist()} for i,d,new,old in events]
        meta['draws']=draws
        meta['trace']=trace
    return meta


def write_json(path,obj):
    path=Path(path)
    path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n',encoding='utf-8')
