"""Only passive saved-input reevaluations; no fresh rollout or RNG draws."""
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('gpt_passive_checker',ROOT/'received/inspect_saved_records.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
supplied=json.loads((ROOT/'received/SAVED_RECORD_INSPECTION.json').read_text())
results=[]
for expected in supplied['logs']:
    path=ROOT/'data'/expected['path']
    result=module.inspect_log(path)
    for key in ['sha256','rows','blocks','saved_input_re_evaluations','unique_frame_labels',
                'frame_labels','repeated_step_body_keys','same_frame_successions',
                'descending_frame_successions','observed_binary_rule_flips']:
        assert result[key]==expected[key],key
    for key in ['max_velocity_residual','max_position_prediction_residual',
                'max_saved_velocity_position_residual','max_grf_residual','max_energy_residual']:
        assert result[key]<1e-12,(key,result[key])
    df=pd.read_csv(path,float_precision='round_trip')
    frames=df.Step.to_numpy().reshape(-1,8)[:,0]
    pos=df[['X','Y','Z']].to_numpy().reshape(-1,8,3)
    raw=pos[1:]-pos[:-1]
    minimal=np.mod(raw+5,10)-5
    historical=np.linalg.norm(np.mod(raw,10),axis=2)
    speed=np.linalg.norm(minimal,axis=2)
    extra={'descending_block_indices':(np.flatnonzero(np.diff(frames)<0)+1).tolist(),
        'same_frame_block_indices':(np.flatnonzero(np.diff(frames)==0)+1).tolist(),
        'historical_detector_events':int(np.sum(historical>1)),
        'minimal_image_events_above_same_threshold':int(np.sum(speed>1)),
        'max_minimal_image_step':float(speed.max()),
        'scope':'Adjacent saved blocks only; first block has no recorded predecessor.'}
    result['passive_observers']=extra
    result['supplied_residuals']={k:v for k,v in expected.items() if 'residual' in k}
    results.append(result)
record={'status':'PASS','method':'Supplied inspection function independently executed against hash-verified local copies; each prediction restarts from a saved block and uses destination frame and bits.',
    'python':sys.version,'numpy':np.__version__,'pandas':pd.__version__,
    'saved_input_calculations':sum(r['saved_input_re_evaluations'] for r in results),
    'fresh_numerical_update_calls':0,'rng_draws':0,'logs':results}
(ROOT/'evidence/SAVED_RECORD_LOCAL_VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
