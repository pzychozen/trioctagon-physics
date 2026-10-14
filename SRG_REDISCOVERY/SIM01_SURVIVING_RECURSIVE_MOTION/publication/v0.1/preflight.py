"""Exactly twelve detached full-system calls. Refuses any repeat execution."""
import hashlib
import json
import numpy as np
from engine_api import ROOT,load_engine,observed_step,rng_json,state_copy,set_state,write_json

ledger_path=ROOT/'evidence/PREFLIGHT_CALL_LEDGER.json'
assert not ledger_path.exists(), 'Preflight has already started; no automatic retry is authorized.'
ledger={'budget':12,'calls':[],'status':'RUNNING'}
write_json(ledger_path,ledger)
results=[]


def serial(state):
    return {k:(v.tolist() if v is not None else None) for k,v in state.items()}


def case(name,label,p,v,frame,seed=1,bits=None):
    initial={'positions':np.array(p,dtype=float),'velocities':np.array(v,dtype=float),
             'bits':None if bits is None else np.array(bits,dtype=int)}
    engine=load_engine(name)
    np.random.seed(seed); checkpoint=np.random.get_state()
    outputs=[]; records=[]; rngs=[]
    for observed in [False,True]:
        set_state(engine,initial); np.random.set_state(checkpoint)
        assert len(ledger['calls'])<12
        ledger['calls'].append({'source':name,'case':label,'observed':observed,'frame':frame,'status':'STARTED'})
        write_json(ledger_path,ledger)
        record=observed_step(engine,name,frame,observed=observed,snapshots=observed)
        ledger['calls'][-1]['status']='COMPLETED';write_json(ledger_path,ledger)
        outputs.append(state_copy(engine));records.append(record);rngs.append(rng_json())
    for k in initial:
        if initial[k] is not None: assert np.array_equal(outputs[0][k],outputs[1][k]),(name,label,k)
    assert rngs[0]==rngs[1]
    for k in ['t','H','G']: assert records[0][k]==records[1][k]
    trace=records[1]['trace'];n=len(p)
    assert len(trace)==2*n
    for i in range(n):
        before=np.array(trace[2*i]['positions'])
        assert trace[2*i]['event']=='before' and trace[2*i]['i']==i
        assert np.array_equal(before[:i],outputs[1]['positions'][:i])
        assert np.array_equal(before[i:],initial['positions'][i:])
    L=2 if name=='A' else 10;dt=.05 if name=='A' else .1
    raw=outputs[1]['positions']-initial['positions']
    minimal=np.mod(raw+L/2,L)-L/2
    displacement_residual=float(np.max(np.abs(minimal-dt*outputs[1]['velocities'])))
    assert displacement_residual<1e-14
    if 'boundary' in label: assert np.any(np.abs(raw)>L/2)
    if 'coincident' in label:
        assert np.array_equal(outputs[1]['positions'],initial['positions'])
        assert np.array_equal(outputs[1]['velocities'],initial['velocities'])
    if name=='C':
        if label=='boundary_gate_open':
            assert records[1]['G']>.5 and len(records[1]['draws'])==8
            assert [d['body'] for d in records[1]['draws']]==list(range(8))
            expected=(np.array([d['value'] for d in records[1]['draws']])<.01).astype(int)
            assert np.array_equal(outputs[1]['bits'],expected)
            assert expected.sum()==1 and expected[2]==1
        else:
            assert records[1]['G']<.5 and not records[1]['draws']
            assert rngs[1]==rng_json(checkpoint)
            assert engine.GRF(engine.positions,records[1]['t'])>.5
        # Original energy/detector observers preserve every carried state and RNG.
        before=state_copy(engine);r_before=rng_json()
        engine.compute_energy(engine.positions,engine.velocities)
        engine.detect_teleport(initial['positions'],engine.positions)
        assert r_before==rng_json()
        for k in before: assert np.array_equal(before[k],state_copy(engine)[k])
    results.append({'source':name,'case':label,'frame':frame,'seed':seed,'initial':serial(initial),
        'successor':serial(outputs[1]),'observed_unobserved_state_bitwise_equal':True,
        'observed_unobserved_rng_equal':True,'sequential_trace_checks':n,
        'position_velocity_residual':displacement_residual,
        'source_metadata':{k:v for k,v in records[1].items() if k!='trace'},
        'state_and_rng_determine_successor':'No extra evolving state exists in extracted functions; equality persists for equal future frame inputs.'})


try:
    extraction=json.loads((ROOT/'evidence/EXTRACTION_MAP.json').read_text())
    for e in extraction.values():
        assert e['round_trip_ast_equal'] and e['helpers_ast_equal'] and e['initialization_ast_equal']
        assert hashlib.sha256((ROOT/e['detached']).read_bytes()).hexdigest()==e['detached_sha256']
    case('A','boundary',[[.999,.2],[-.999,-.2],[.1,.8]],[[.3,0],[-.3,.1],[.01,-.2]],199)
    case('A','coincident',np.zeros((3,2)),np.zeros((3,2)),0)
    bp=np.array([[9.999,2,3],[.001,3,4],[2,4,5],[3,5,6],[4,6,7],[5,7,8],[6,8,9],[7,9,1.]])
    bv=np.zeros((8,3));bv[0,0]=.3;bv[1,0]=-.3
    case('B','boundary',bp,bv,199)
    case('B','coincident',np.full((8,3),4.5),np.zeros((8,3)),0)
    case('C','boundary_gate_open',bp,bv,199,bits=np.zeros(8,dtype=int))
    cv=np.zeros((8,3));cv[0,0]=20
    case('C','frozen_gate_closed',np.full((8,3),3.),cv,0,bits=np.zeros(8,dtype=int))
    assert len(ledger['calls'])==12
    ledger['status']='PASS'
    write_json(ROOT/'evidence/PREFLIGHT_RESULTS.json',{'status':'PASS','numerical_calls':12,
        'method':'AST-equal source extraction plus six observed/unobserved fixture pairs; no original top-level imports.',
        'fixtures':results,'conditional_switch_fixtures':0,
        'note':'C uses actual source-style MT19937 draws. No prescribed or additional random samples were inserted.'})
except Exception as e:
    ledger['status']='FAIL';ledger['error']=repr(e)
    raise
finally:
    write_json(ledger_path,ledger)
print(json.dumps({'preflight':'PASS','numerical_calls':len(ledger['calls']),'fixtures':len(results)}))
