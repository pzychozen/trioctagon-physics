"""Bounded final-publication smoke; does not regenerate historical suites.
The adapter loads original D1 function/class bodies unchanged via AST
from the explicitly labeled path-only public source derivative.
It omits only module-level path assertions, I/O and main dispatch.
"""
from pathlib import Path
import ast,json,sys,hashlib,platform,argparse
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
import numpy as np
import sympy as s
import mpmath as mp
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run():
    checks=[];details={}
    def ck(name,value,kind):
        checks.append({'name':name,'passed':bool(value),'kind':kind})
        assert value,name
    sys.path.insert(0,str(ROOT/'measurement/supplement/native'))
    from kernel_physics.srg import fixed_november_srg,fourier_basis,helicity_mode,handoff_area_response
    from kernel_physics.boundary_response import lens_area_gain,RESPONSE_ID
    ops=fixed_november_srg();f=fourier_basis();q=np.exp(-.423);r=np.exp(.577);c=.382
    ck('SRG negative-exponent basis/action',max(np.linalg.norm(ops.A@f[:,0]-q*f[:,1]),np.linalg.norm(ops.A@f[:,1]-q*c*f[:,2]),np.linalg.norm(ops.A@f[:,2]-r*c*f[:,0]))<2e-14,'binary64 smoke')
    theta=np.arccos(.5)
    kw={'transfer_count':5,'branch':'positive_imag','response':RESPONSE_ID}
    first=handoff_area_response(theta,[1,0],**kw).omega
    values=[handoff_area_response(np.arccos(d/(2*rr)),[1,0],**kw).omega for rr,d in [(1,1),(2,2),(.25,.25)]]
    ck('Scale-related lens inputs',max(np.linalg.norm(v-first) for v in values)<2e-14,'binary64 smoke')
    ck('Endpoint gains',lens_area_gain(0)==0 and abs(lens_area_gain(np.pi/2)-1)<2e-14,'binary64 smoke')
    # No original module initialization is executed; all selected bodies are unedited.
    src=ROOT/'drift/supplement/historical/D1_chiral_drift_20261006/verify_d1.py'
    result=src.with_name('D1_RESULTS.json')
    record=json.loads(result.read_text(encoding='utf-8'))
    exports=json.loads((ROOT/'provenance/public_export_map.json').read_text(encoding='utf-8'))['files']
    source_export=next(v for v in exports if v['path']==src.relative_to(ROOT).as_posix())
    result_export=next(v for v in exports if v['path']==result.relative_to(ROOT).as_posix())
    assert sha(src)==source_export['public_sha256']
    assert sha(result)==result_export['public_sha256']
    # These entire scientific objects were compared directly with the raw original.
    # Recheck their public fingerprints before consuming the derivative.
    for key in ['roots_plus','exact_jet']:
        encoded=json.dumps(record[key],sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
        assert hashlib.sha256(encoded).hexdigest()==result_export['scientific_subtree_sha256'][key]
    tree=ast.parse(src.read_text(encoding='utf-8'))
    definitions=[node for node in tree.body if isinstance(node,(ast.FunctionDef,ast.ClassDef))]
    env={'s':s,'mp':mp,'Path':Path,'sys':sys,'json':json,'hashlib':hashlib,'h':s.symbols('h',real=True),'I':s.I,'rt3':s.sqrt(3),'N':3,'rot':[1,(-1+s.I*s.sqrt(3))/2,(-1-s.I*s.sqrt(3))/2],'record':record,'jet_cache':{},'__name__':'portable_d1_adapter'}
    exec(compile(ast.Module(body=definitions,type_ignores=[]),'<unchanged D1 function bodies>','exec'),env)
    mp.mp.dps=110;mp.iv.dps=100
    residuals=[]
    for hh in ['0.0','0.1','0.01','0.001']:
        root=next(v for v in record['roots_plus'] if mp.mpf(v['h'])==mp.mpf(hh) and mp.mpf(v['eta'])==mp.mpf('0.00025'))
        x=mp.matrix([mp.mpf(v) for v in root['certificate']['point_center']])
        F,J,aux=env['system'](x,mp.mpf(hh),mp.mpf(root['eta']))
        err=max(abs(v) for v in F);residuals.append(mp.nstr(err,20))
        ck('D1 retained midpoint h='+hh,err<mp.mpf('1e-90'),'110-digit residual smoke, not new continuation')
        if hh=='0.1':
            C=mp.inverse(mp.matrix(J))
            cert,_=env['certificate'](x,C,mp.mpf(hh),mp.mpf(root['eta']),mp.mpf(root['eta']),mp.mpf('1e-60'))
            ck('One original D1 fixed-root enclosure',cert['certified'],'same 100-digit interval routine; one point only')
            details['one_point_certificate']=cert
    details['midpoint_absolute_residuals']=residuals
    details['adapter']={'public_source_sha256':sha(src),'raw_source_sha256':source_export['original_raw_sha256'],'public_result_sha256':sha(result),'raw_result_sha256':result_export['original_raw_sha256'],'method':'AST function/class bodies unchanged; module path/I-O/assertion/main side effects excluded; public scientific input fingerprints checked','precision':{'mpmath':110,'interval':100},'full_133_suite_replayed':False,'historical_preservation_checks_replayed':False}
    return {'status':'PASS','checks':checks,'passed':len(checks),'total':len(checks),'details':details,'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':s.__version__,'mpmath':mp.__version__}}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'results/portable_smoke.json');a=p.parse_args()
    a.output.parent.mkdir(parents=True,exist_ok=True)
    result=run();a.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'final_smoke_checks':result['total'],'output':str(a.output)}))
