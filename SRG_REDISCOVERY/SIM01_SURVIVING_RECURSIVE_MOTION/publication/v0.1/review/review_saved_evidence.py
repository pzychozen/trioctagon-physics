"""Independent, passive SRG-SIM01 review.

Reads an already-extracted review bundle. Never imports historical/detached engines,
advances a carried trajectory, reruns preflight, or writes inside the input bundle.
Each transition residual starts afresh from its saved predecessor. Source C's saved
outcome bits are checked against its saved draws; its RNG is separately replayed
without producing motion. Requires Python 3 and NumPy.
"""
from __future__ import annotations
import argparse, ast, copy, csv, hashlib, json, platform
from pathlib import Path
import numpy as np

TOL = 1e-13

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def readj(p: Path):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def structural(nodes):
    return ast.dump(ast.Module(body=nodes, type_ignores=[]), include_attributes=False)

def model_h(t):
    return (2.0*np.exp(-0.5*t)*np.cos(t) + np.exp(-0.3*t)*np.sin(t)
            + 1.5*np.exp(-0.7*t) + np.exp(-0.4*t))

def residual_from_saved(name, old_p, old_v, frame, target_bits=None):
    # Scratch evaluation of one recorded transition, NOT a new trajectory.
    p, v = old_p.copy(), old_v.copy()
    dt = .05 if name == 'A' else .1
    h = model_h(frame*dt)
    g = None if name == 'A' else 1.0/(1.0+np.mean(np.linalg.norm(v,axis=1)))
    for i in range(len(p)):
        if name == 'A':
            force = np.zeros(2)
            for j in range(len(p)):
                if j == i:
                    continue
                d = (p[j]-p[i]+1.0) % 2.0 - 1.0
                force += d/(np.linalg.norm(d)+.001)
            v[i] += dt*h*force
        else:
            d = (np.mean(p,axis=0)-p[i]+5.0)%10.0-5.0
            force = d/(np.linalg.norm(d)+.01)*h
            if name == 'C':
                force = force*(-1 if target_bits[i] else 1)
            v[i] += dt*force*g
        v[i] = v[i]/(1.0+np.log1p(np.abs(v[i])))
        if name == 'A':
            p[i] = (p[i]+dt*v[i]+1.0)%2.0-1.0
        else:
            p[i] += dt*v[i]
            p[i] %= 10.0
    return p, v, h, g

def state_tuple(s):
    return (s['algorithm'], np.asarray(s['keys'],dtype=np.uint32),
            s['position'], s['has_gauss'], s['cached_gaussian'])

def same_rng(a,b):
    return (a[0]==b[0] and np.array_equal(a[1],b[1]) and a[2:]==b[2:])

def mean_distance(p,L):
    ii,jj=np.triu_indices(len(p),1)
    d=(p[jj]-p[ii]+L/2)%L-L/2
    return float(np.linalg.norm(d,axis=1).mean())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bundle-root',type=Path,required=True)
    ap.add_argument('--output-dir',type=Path,required=True)
    args=ap.parse_args()
    root=args.bundle_root.resolve(); out=args.output_dir.resolve()
    if out==root or root in out.parents:
        raise ValueError('Output directory must be outside input review bundle')
    out.mkdir(parents=True,exist_ok=True)
    files={p.relative_to(root).as_posix():sha(p) for p in root.rglob('*') if p.is_file()}
    manifest=readj(root/'REVIEW_MANIFEST.json')['files']
    assert set(files)==set(manifest)|{'REVIEW_MANIFEST.json'}
    for rel,row in manifest.items():
        p=root/rel
        assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],rel
    result={'status':'PASS','environment':{'python':platform.python_version(),'numpy':np.__version__},
            'method':'Independently written saved-input residuals, static AST comparison, saved-array readouts and isolated RNG replay. No motion rollout or engine import.',
            'new_rollout_updates':0,'payloads_verified':len(manifest),'static_source_checks':{},'replay_records':{},'historical_records':{}}
    specs={'A':(5,7,[10,11],['H','RPCO','TGMO']),
           'B':(8,12,[15,16],['wrap_position','H','RPCO','GRF']),
           'C':(10,14,[17,18,152],['wrap_position','H','RPCO','GRF','compute_energy','detect_teleport'])}
    for name,(lo,hi,initlines,helpers) in specs.items():
        src=ast.parse((root/f'sources/source_{name}.py').read_text())
        det=ast.parse((root/f'detached/engine_{name}.py').read_text())
        sf={n.name:n for n in src.body if isinstance(n,ast.FunctionDef)}
        df={n.name:n for n in det.body if isinstance(n,ast.FunctionDef)}
        for h in helpers:
            assert structural([sf[h]])==structural([df[h]])
        constants=[n for n in src.body if lo<=n.lineno<=hi]
        assert structural(constants)==structural([n for n in det.body if isinstance(n,ast.Assign)])
        initial=[n for n in src.body if n.lineno in initlines]
        assert structural(initial)==structural(df['initialize'].body[1:])
        if name=='A':
            b=copy.deepcopy(next(n for n in src.body if isinstance(n,ast.For)).body)
            b=[n for n in b if n.lineno not in (42,59)]
            inner=next(n for n in b if isinstance(n,ast.For))
            inner.body=[n for n in inner.body if n.lineno!=57]
            b.insert(0,ast.Global(names=['positions','velocities']))
        else:
            cap=96 if name=='B' else 126
            b=copy.deepcopy([n for n in sf['update'].body if n.lineno<=cap and not(name=='C' and n.lineno==107)])
        db=copy.deepcopy(df['numerical_step'].body[:-1])
        loop=next(n for n in db if isinstance(n,ast.For))
        loop.body=[n for n in loop.body if not(isinstance(n,ast.If) and ast.unparse(n.test)=='_trace is not None')]
        assert structural(b)==structural(db),name
        result['static_source_checks'][name]={'helpers_constants_initialization_update_AST_equal':True}
    data={}
    for name,N in [('A',500),('B',2000),('C',200)]:
        with np.load(root/f'runs/{name}/states.npz',allow_pickle=False) as f:
            a={k:f[k] for k in f.files}
        data[name]=a
        p,v,bits=a['positions'],a['velocities'],a['bits']
        assert len(p)==N+1 and p.shape==v.shape
        assert np.isfinite(p).all() and np.isfinite(v).all()
        assert np.array_equal(a['source_frame'],np.arange(N))
        rng=np.random.RandomState(2038)
        ir=readj(root/f'runs/{name}/RNG_INITIAL.json')
        assert same_rng(rng.get_state(),state_tuple(ir['before_original_initialization']))
        p0=rng.rand(3,2)*2-1 if name=='A' else rng.rand(8,3)*10
        v0=np.zeros((3,2)) if name=='A' else (rng.rand(8,3)-.5)*.2
        assert np.array_equal(p0,p[0]) and np.array_equal(v0,v[0])
        assert same_rng(rng.get_state(),state_tuple(ir['after_original_initialization']))
        errp=errv=errh=errg=erre=0.0
        for k in range(N):
            pp,vv,h,g=residual_from_saved(name,p[k],v[k],int(a['source_frame'][k]),bits[k+1] if name=='C' else None)
            errp=max(errp,float(np.max(np.abs(pp-p[k+1]))))
            errv=max(errv,float(np.max(np.abs(vv-v[k+1]))))
            errh=max(errh,float(abs(h-a['H'][k])))
            if g is not None:errg=max(errg,float(abs(g-a['G'][k])))
            if name=='C':
                expected=bits[k].copy()
                if g>.5:
                    draw=rng.rand(8)
                    assert a['draw_count'][k]==8 and np.array_equal(draw,a['draws'][k])
                    expected[draw<.01]=1-expected[draw<.01]
                else:
                    assert a['draw_count'][k]==0 and np.isnan(a['draws'][k]).all()
                assert np.array_equal(expected,bits[k+1])
                e=.5*np.sum(np.linalg.norm(v[k+1],axis=1)**2)
                erre=max(erre,float(abs(e-a['energy'][k])))
        assert same_rng(rng.get_state(),state_tuple(readj(root/f'runs/{name}/RNG_FINAL.json')))
        assert max(errp,errv,errh,errg,erre)<TOL
        L=2.0 if name=='A' else 10.0;dt=.05 if name=='A' else .1
        raw=np.diff(p,axis=0); minimal=(raw+L/2)%L-L/2
        assert np.array_equal(raw,a['raw_displacements'])
        assert np.array_equal(minimal,a['minimal_image_displacements'])
        assert np.array_equal(np.concatenate([p[:1],p[:1]+np.cumsum(minimal,axis=0)]),a['unwrapped_positions'])
        step=np.linalg.norm(minimal,axis=2)
        pverr=float(np.max(np.abs(minimal-dt*v[1:])))
        assert pverr<TOL and np.max(np.abs(dt*v[1:]))<L/2
        speed=np.linalg.norm(v,axis=2).mean(axis=1)
        row={'stored_updates_checked':N,'position_residual_max':errp,'velocity_residual_max':errv,
             'H_residual_max':errh,'G_residual_max':errg,'energy_residual_max':erre,
             'initial_state_and_full_RNG_checkpoints_match':True,
             'mean_speed_peak':float(speed.max()),'mean_speed_final':float(speed[-1]),
             'mean_pair_distance_initial':mean_distance(p[0],L),'mean_pair_distance_final':mean_distance(p[-1],L),
             'coordinate_crossing_body_updates':int(np.any(np.abs(raw)>L/2,axis=2).sum()),
             'maximum_minimal_image_step':float(step.max()),'unwrapping_velocity_residual':pverr}
        if name=='C':
            det=np.linalg.norm(raw%10,axis=2)
            assert np.array_equal(det,a['detector_distance'])
            assert np.array_equal(det>1,a['detector_flags'])
            row.update({'switch_count':int(np.count_nonzero(np.diff(bits,axis=0))),
                        'draw_count':int(a['draw_count'].sum()),'gate_open_updates':int((a['G']>.5).sum()),
                        'legacy_detector_events':int((det>1).sum()),'minimal_image_events_gt1':int((step>1).sum()),
                        'final_bits':bits[-1].tolist()})
        result['replay_records'][name]=row
    for path in sorted((root/'data').glob('*.csv')):
        with path.open(newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
        assert len(rows)%8==0
        assert all(int(float(row['Tetrahedron']))==i%8 for i,row in enumerate(rows))
        p=np.array([[float(row[c]) for c in ['X','Y','Z']] for row in rows]).reshape(-1,8,3)
        v=np.array([[float(row[c]) for c in ['VX','VY','VZ']] for row in rows]).reshape(-1,8,3)
        b=np.array([int(float(row['Rule_State'])) for row in rows]).reshape(-1,8)
        f=np.array([int(float(row['Step'])) for row in rows]).reshape(-1,8)
        e=np.array([float(row['Energy']) for row in rows]).reshape(-1,8)
        g=np.array([float(row['GRF']) for row in rows]).reshape(-1,8)
        assert np.all(f==f[:,[0]])
        ep=ev=eg=ee=0.0
        for k in range(len(p)-1):
            pp,vv,h,gg=residual_from_saved('C',p[k],v[k],int(f[k+1,0]),b[k+1])
            ep=max(ep,float(np.max(np.abs(pp-p[k+1]))));ev=max(ev,float(np.max(np.abs(vv-v[k+1]))))
            eg=max(eg,float(np.max(np.abs(gg-g[k+1]))))
            ee=max(ee,float(np.max(np.abs(.5*np.sum(np.linalg.norm(v[k+1],axis=1)**2)-e[k+1]))))
        assert max(ep,ev,eg,ee)<TOL
        raw=np.diff(p,axis=0); minimal=(raw+5)%10-5
        result['historical_records'][path.name]={'adjacent_transitions_checked':len(p)-1,'rows':len(rows),
            'position_residual_max':ep,'velocity_residual_max':ev,'G_residual_max':eg,'energy_residual_max':ee,
            'legacy_detector_events':int((np.linalg.norm(raw%10,axis=2)>1).sum()),
            'minimal_image_events_gt1':int((np.linalg.norm(minimal,axis=2)>1).sum()),
            'maximum_minimal_image_step':float(np.linalg.norm(minimal,axis=2).max()),
            'repeated_frame_successions':int((np.diff(f[:,0])==0).sum()),
            'decreasing_frame_successions':int((np.diff(f[:,0])<0).sum()),
            'bit_changes':int(np.count_nonzero(np.diff(b,axis=0)))}
    # Reviewer-only equal-duration comparison: no new trajectories or changed report.
    b,c=data['B'],data['C'];bp=b['positions'][:201];cp=c['positions']
    bv=b['velocities'][:201];cv=c['velocities']
    changed=np.any(bp!=cp,axis=(1,2))|np.any(bv!=cv,axis=(1,2))
    gap=(bp[-1]-cp[-1]+5)%10-5
    result['reviewer_only_common_200_update_comparison']={
        'method':'Align existing B prefix and C by stored update count; not a new randomized intervention.',
        'initial_positions_equal':bool(np.array_equal(bp[0],cp[0])),
        'initial_velocities_equal':bool(np.array_equal(bv[0],cv[0])),
        'H_inputs_equal':bool(np.array_equal(b['H'][:200],c['H'])),
        'first_different_state_index':int(np.flatnonzero(changed)[0]),
        'first_switch_update_index':int(np.argwhere(np.diff(c['bits'],axis=0)!=0)[0,0]),
        'B_mean_pair_distance_after_200':mean_distance(bp[-1],10),
        'C_mean_pair_distance_after_200':mean_distance(cp[-1],10),
        'mean_periodic_bodywise_separation_B_vs_C_after_200':float(np.linalg.norm(gap,axis=1).mean()),
        'B_mean_speed_after_200':float(np.linalg.norm(bv[-1],axis=1).mean()),
        'C_mean_speed_after_200':float(np.linalg.norm(cv[-1],axis=1).mean())}
    ledger=readj(root/'evidence/PREFLIGHT_CALL_LEDGER.json')
    assert len(ledger['calls'])==12 and all(r['status']=='COMPLETED' for r in ledger['calls'])
    result['preflight_ledger']={'recorded_calls':12,'reexecuted_calls':0}
    assert files=={p.relative_to(root).as_posix():sha(p) for p in root.rglob('*') if p.is_file()}
    result['input_bundle_unchanged']=True
    result['passive_transition_total']=2700+1530
    (out/'INDEPENDENT_REVIEW_RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
