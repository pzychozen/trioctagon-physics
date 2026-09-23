"""Four fixed source-body replays for figure data; no sweep or original writes.
This is optional regeneration of the bundled plot_data.npz, not a PDF prerequisite.
"""
import runtime
from runtime import ROOT
import ast,importlib.util,sys,types,json,hashlib,warnings
from pathlib import Path
import numpy as np
SRC=ROOT/'evidence/source_snapshots/staged'
pkg=types.ModuleType('_paper_e_source');pkg.__path__=[str(SRC)];sys.modules[pkg.__name__]=pkg
def load(name,path=None):
    spec=importlib.util.spec_from_file_location(pkg.__name__+'.'+name,path or SRC/(name+'.py'))
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m
core=load('model_core');defs=load('definitions');const=load('constants_selector')
ema=load('ema',ROOT/'evidence/source_snapshots/committed_ema/model_core.py')
data={};records={}
def run(name,module,seed,steps,dt,soft,**kw):
    rng=np.random.default_rng(seed);o=rng.standard_normal(3)+1j*rng.standard_normal(3)
    if soft:o*=.1
    o/=np.linalg.norm(o)+1e-12
    p=module.ModelParams(k_vals=const.default_k_triplet('theta_soft' if soft else 'theta_scaled'),**kw)
    h=module.TriOctaPhaseLockModel(p).run(module.ModelState(o),n_steps=steps,dt=dt)
    v,c=defs.compute_recursive_velocity_geom(h,return_components=True)
    for k,a in h.items():
        if isinstance(a,np.ndarray):data[name+'__'+k]=a
    data[name+'__J']=defs.compute_jeff_series(h);data[name+'__v']=v
    for k in ['dZ','dphi','dcorr','dkappa']:data[name+'__'+k]=c[k]
    rec={'seed':seed,'steps':steps,'dt':dt,'eps':p.eps,'g':p.g,'lambda_phase':p.lambda_phase,'k':p.k_vals.tolist()}
    if not soft:
        path=next((ROOT/'evidence/preserved_runs').glob('*'+('869bf44ed4' if name=='subcritical' else '37abc4f4f9')+'*_series.csv'))
        raw=np.genfromtxt(path,delimiter=',',names=True);Z=np.column_stack([raw[k] for k in ('Zx','Zy','Zz')])
        rec.update(Z_equal=bool(np.array_equal(Z,h['Z_total'],equal_nan=True)),v_equal=bool(np.array_equal(raw['v_rec'][1:],v,equal_nan=True)),
                   J_equal=bool(np.array_equal(raw['J_eff'],data[name+'__J'],equal_nan=True)),
                   finite_event_count=int(np.sum(np.isfinite(v)&(v>=.8))),
                   first_nonfinite_Z=next((int(i) for i in np.flatnonzero(~np.isfinite(Z).all(axis=1))),None),
                   first_nonfinite_v=next((int(i+1) for i in np.flatnonzero(~np.isfinite(v))),None),
                   first_nonfinite_J=next((int(i) for i in np.flatnonzero(~np.isfinite(raw['J_eff']))),None))
        assert rec['Z_equal'] and rec['v_equal'] and rec['J_equal'],rec
        data[name+'__saved_Z']=Z;data[name+'__saved_v']=raw['v_rec'];data[name+'__csv_t']=raw['t']
    records[name]=rec
with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter('always')
    run('baseline',core,42,300,.05,True)
    run('ema',ema,42,300,.05,True)
    run('subcritical',core,2158500047,2000,.02776,False,eps=.0005,g=.664,lambda_phase=0.)
    run('critical',core,2158500047,2000,.02776,False,eps=.0005,g=.667,lambda_phase=0.)
np.savez_compressed(ROOT/'evidence/plot_data.npz',**data)
record={'attribution':'New Codex fixed source-body replays for figures, not original captured runs',
        'runs':records,'warnings':sorted(set(str(w.message) for w in ws)),
        'data_sha256':hashlib.sha256((ROOT/'evidence/plot_data.npz').read_bytes()).hexdigest(),
        'numpy':np.__version__,'python':sys.version}
(ROOT/'evidence/plot_data_results.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,indent=2))
