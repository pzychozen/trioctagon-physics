"""Bounded Codex reconstruction, 2026-09-23. No legacy source writes/import UI.

Run with Python 3.12, numpy, matplotlib (optional --deps directory):
  python -B verify_historical_z.py --baseline
  python -B verify_historical_z.py --deps PATH
  python -B verify_historical_z.py --seal
Preserved source bodies run via a synthetic package or selected AST definitions.
No CLI/UI, RSB, latent-foreclosure probe or sweep is launched.
"""
import argparse, ast, csv, hashlib, importlib.util, json, math, subprocess, sys, types
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REPO = ROOT / 'trioctagon-physics'
OLD = ROOT / 'kernel_TO'
EMA = ROOT / 'reconstruction/recursive_state_archaeology/codex_verification_I/source_snapshots/model_core.py'
REPORT = HERE.parent / 'HISTORICAL_Z_MANIFOLD_AND_SIX_GAP_RECONSTRUCTION_v0.1.md'

def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda: f.read(1048576), b''): h.update(b)
    return h.hexdigest()

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args]).decode('utf-8').strip()

def dump(p, obj):
    def clean(v):
        if isinstance(v,float) and not math.isfinite(v): return str(v)
        if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
        if isinstance(v,list): return [clean(x) for x in v]
        return v
    p.write_text(json.dumps(clean(obj), indent=2, ensure_ascii=False, allow_nan=False)+'\n', encoding='utf-8')

def baseline():
    target = HERE/'preservation_before.json'
    if target.exists(): raise SystemExit('Baseline already exists; never replace it.')
    paths = {REPO/p for p in git('ls-files').splitlines()}
    paths.update(OLD.glob('*.py'))
    paths.update(p for d in ('vrec_ts_critical', 'vrec_ts_subcritical') for p in (OLD/d).iterdir() if p.is_file())
    paths.update([EMA, ROOT/'reconstruction/KERNEL_SOURCE_TO_MODEL.md',
                  ROOT/'reconstruction/continuity_closeout_20260922/PROJECT_STATUS_RECOVERY.md'])
    paths.update(ROOT.glob('**/INTEGRATED_TOY_MODEL_SPEC*.md'))
    dump(target, {'head':git('rev-parse','HEAD'), 'status':git('status','--porcelain=v1','-uall'),
                  'index_entries':git('ls-files','--stage'),
                  'files':{str(p):sha(p) for p in sorted(paths) if p.is_file()}})
    print('Baseline:', len(json.loads(target.read_text(encoding='utf-8'))['files']), 'files')

def seal():
    before = json.loads((HERE/'preservation_before.json').read_text(encoding='utf-8'))
    mismatches = [p for p,h in before['files'].items() if not Path(p).is_file() or sha(p)!=h]
    after = {'head':git('rev-parse','HEAD'), 'status':git('status','--porcelain=v1','-uall'), 'index_entries':git('ls-files','--stage')}
    result = {'attribution':'Codex verification, new outputs only', 'protected_files':len(before['files']),
              'mismatches':mismatches, 'git_unchanged':all(after[k]==before[k] for k in after),
              'starting_head':before['head'], 'final_head':after['head'],
              'tracked_status':git('status','--porcelain=v1','-uno'),
              'untracked_count':sum(s.startswith('?? ') for s in after['status'].splitlines()),
              'package_hashes':{str(p.relative_to(HERE.parent)):sha(p) for p in [REPORT,*sorted(HERE.rglob('*'))]
                                if p.is_file() and p.name!='preservation_receipt.json' and '.mplconfig' not in p.parts}}
    dump(HERE/'preservation_receipt.json', result)
    assert not mismatches and result['git_unchanged'], result
    print('Preservation PASS:', result['protected_files'], 'files; Git unchanged')

def verify(deps):
    if deps: sys.path.insert(0,str(Path(deps).resolve()))
    import os
    os.environ['MPLCONFIGDIR'] = str(HERE/'.mplconfig')
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    sys.dont_write_bytecode = True
    pkg = types.ModuleType('_preserved_z'); pkg.__path__ = [str(OLD)]; sys.modules[pkg.__name__] = pkg
    def load(name, path=None):
        full = pkg.__name__+'.'+name
        spec = importlib.util.spec_from_file_location(full, path or OLD/(name+'.py'))
        mod = importlib.util.module_from_spec(spec); sys.modules[full]=mod; spec.loader.exec_module(mod)
        return mod
    core=load('model_core'); defs=load('definitions'); geo=load('geometry_3d'); alt=load('geometry_embeddings')
    const=sys.modules[pkg.__name__+'.constants_selector']; prov=load('provenance'); ema=load('ema',EMA)
    def selected(path, names, ns):
        tree=ast.parse(path.read_text(encoding='utf-8-sig'))
        nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
        assert len(nodes)==len(names)
        exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path),'exec'), ns)
        return ns
    ns=selected(OLD/'z_spike_diagnostic.py', ['run_triocta_once','pick_spikes'],
                dict(np=np,default_k_triplet=const.default_k_triplet,ModelParams=core.ModelParams,
                     ModelState=core.ModelState,TriOctaPhaseLockModel=core.TriOctaPhaseLockModel,
                     make_run_meta=prov.make_run_meta,compute_jeff_series=defs.compute_jeff_series))
    viewer=selected(OLD/'toy_3d_triocta.py',['embed_on_torus'],dict(np=np))
    checks={}
    def check(name, cond): checks[name]=bool(cond); assert cond,name
    def norm(x): return np.linalg.norm(x,axis=-1)
    def fmax(x):
        x=np.asarray(x); x=x[np.isfinite(x)]; return float(x.max()) if x.size else None
    def chiral(x): return np.cross(x.real,x.imag)
    def run(seed=42, dt=.05, steps=300, module=core, **kw):
        k=const.default_k_triplet('theta_soft').copy(); k[2]*=kw.pop('k3_scale',1.)
        p=module.ModelParams(k_vals=k,**kw)
        rng=np.random.default_rng(seed); o=.1*(rng.standard_normal(3)+1j*rng.standard_normal(3)); o/=norm(o)+1e-12
        h=module.TriOctaPhaseLockModel(p).run(module.ModelState(o),n_steps=steps,dt=dt)
        return h,p
    def audit(h,p):
        o=h['Omega'][1:]; q=h['phi_index'][1:]; t=h['t'][1:]; kap=norm(o); th=2*np.pi*q/p.d24_steps
        z=p.lambda_vp*kap/(1+kap)*np.cos(3*(th-p.theta_lock))*np.exp(-p.gamma*t)
        m=z[:,None]*np.column_stack((np.cos(th),np.sin(th),np.ones(len(th)))); c=chiral(o)
        errs={k:float(np.max(np.abs(a-b))) for k,a,b in [('z',z,h['z'][1:]),('macro',m,h['Z_macro'][1:]),
             ('chiral',c,h['Z_chiral'][1:]),('total',p.z_alpha*m+p.z_beta*c,h['Z_total'][1:])]}
        check('readout_formulas_'+str(len(checks)),max(errs.values())<2e-13)
        return errs
    def stats(h):
        out={}
        for key in ('Z_macro','Z_chiral','Z_total'):
            v,c=defs.compute_recursive_velocity_geom(h,z_key=key,return_components=True)
            d=defs.vrec_geom_direction(h,z_key=key)
            out[key]={'norm_max_finite':fmax(norm(h[key])),'norm_final_finite':fmax(norm(h[key][-1])),
                      'dZ_max_finite':fmax(c['dZ']),'v_max_finite':fmax(v),'v_ge_0.8':int((np.isfinite(v)&(v>=.8)).sum()),
                      'direction_max_finite':fmax(d), 'tail_step_max_finite':fmax(norm(np.diff(h[key][-60:],axis=0)))}
        out['kappa_max_finite']=fmax(h['kappa'])
        out['first_nonfinite_Omega']=next((i for i,o in enumerate(h['Omega']) if not np.isfinite(o).all()),None)
        out['first_nonfinite_Z']=next((i for i,z in enumerate(h['Z_total']) if not np.isfinite(z).all()),None)
        return out
    base,p=run(); errors=audit(base,p)
    pre=base['Omega'][:-1]+p.eps*base['Omega'][:-1]*(p.k_vals-abs(base['Omega'][:-1])**2)+p.g*(base['Omega'][:-1]@np.array([[-2,1,1],[1,-2,1],[1,1,-2]]).T)
    phases=np.angle(pre); shift=p.lambda_phase*np.sin(3*(phases[:,None,:]-phases[:,:,None])).sum(axis=2)
    check('independent_Omega_recurrence',np.allclose(abs(pre)*np.exp(1j*(phases+shift)),base['Omega'][1:],atol=1e-14,rtol=0))
    vx,vy,vz=viewer['embed_on_torus'](base['Omega'])
    check('viewer_channel_anchors',np.allclose(vy[0],0) and np.allclose(vy[1],-np.sqrt(3)*vx[1]) and np.allclose(vy[2],np.sqrt(3)*vx[2]))
    cases={'viewer_default':base}; sensitivities=[]
    changes=[('eps_minus',{'eps':.045}),('eps_plus',{'eps':.055}),('g_minus',{'g':.18}),('g_plus',{'g':.22}),
             ('k3_minus',{'k3_scale':.9}),('k3_plus',{'k3_scale':1.1}),('phase_off',{'lambda_phase':0}),
             ('phase_double',{'lambda_phase':.002}),('seed43',{'seed':43}),('dt_double',{'dt':.1}),
             ('lock_shift',{'theta_lock':.344}),('lambda_plus',{'lambda_vp':.7416}),('gamma_zero',{'gamma':0}),
             ('alpha_zero',{'z_alpha':0}),('beta_zero',{'z_beta':0}),('beta_double',{'z_beta':1})]
    for name,kw in changes:
        h,pp=run(**kw); audit(h,pp); cases[name]=h
        sensitivities.append({'case':name,'overrides':kw,'max_Omega_difference':float(np.max(np.abs(h['Omega']-base['Omega']))),
                              'max_Z_difference':float(norm(h['Z_total']-base['Z_total']).max()),**stats(h)})
    for name in ('dt_double','lock_shift','lambda_plus','gamma_zero','alpha_zero','beta_zero','beta_double'):
        check(name+'_no_Omega_feedback',np.array_equal(cases[name]['Omega'],base['Omega']))
    check('history_initial_Z_zero',np.all(base['Z_total'][0]==0) and np.all(base['Z_chiral'][0]==0))
    check('history_pre_step_time',np.allclose(base['t'],np.arange(300)*.05))
    check('Z_alias',np.array_equal(base['Z_total'],base['Z_vec']))
    for key,a,b in [('dot_vec_macro','Z_total','Z_macro'),('dot_chiral_macro','Z_chiral','Z_macro'),('dot_vec_chiral','Z_total','Z_chiral')]:
        expected=np.array([core._unit(x)@core._unit(y) for x,y in zip(base[a],base[b])])
        check(key,np.array_equal(expected,base[key]))
    old,oldp=run(module=ema); cases['EMA']=old
    check('EMA_same_Omega',np.array_equal(old['Omega'],base['Omega']))
    mem=0.; ez=[]
    for o,q in zip(old['Omega'][1:],old['phi_index'][1:]):
        j=float(np.imag(o[0]*o[1].conjugate()*o[2])); mem=.99*mem+.01*j/(1+abs(j))
        ez.append(oldp.lambda_vp*norm(o)/(1+norm(o))*np.cos(3*(2*np.pi*q/12-oldp.theta_lock))+mem)
    check('EMA_formula',np.allclose(ez,old['z'][1:],atol=2e-15,rtol=0))
    # Exact stored diagnostic settings, independently re-executed source bodies.
    saved={}; critical={}
    for label,g in [('subcritical',.664),('critical',.667)]:
        h=ns['run_triocta_once'](2158500047,.0005,g,.1,.02776,2000); critical[label]=h
        v,comp=defs.compute_recursive_velocity_geom(h,return_components=True); ns['v_rec_series']=v
        ix,threshold=ns['pick_spikes'](v,'abs',.8)
        folder=OLD/('vrec_ts_'+label); src=next(folder.glob('*_series.csv'))
        raw=np.genfromtxt(src,delimiter=',',names=True)
        vec=np.column_stack([raw[n] for n in ('Zx','Zy','Zz')]); oldv=raw['v_rec'][1:]
        savedix=np.flatnonzero(np.isfinite(oldv)&(oldv>=.8))
        windows=next(folder.glob('*_spikes_*.csv'))
        expected=[(sid,int(j+1),i) for sid,j in enumerate(savedix) for i in range(max(0,j+1-25),min(len(raw)-1,j+1+25)+1)]
        with windows.open(newline='') as f: actual=[(int(r['spike_id']),int(r['center_i']),int(r['i'])) for r in csv.DictReader(f)]
        check(label+'_saved_window_alignment',expected==actual)
        mask=np.isfinite(vec).all(axis=1)&np.isfinite(h['Z_total']).all(axis=1)
        err=float(np.max(np.abs(vec[mask]-h['Z_total'][mask])))
        vm=np.isfinite(v)&np.isfinite(oldv)
        delta=np.max(np.abs(vec-h['Z_total']),axis=1)
        firstdiff=next((int(i) for i in np.flatnonzero(mask) if delta[i]>1e-12),None)
        saved[label]={'source_csv':str(src),'saved_count':len(savedix),'new_count':len(ix),
                      'saved_finite_Z_rows':int(np.isfinite(vec).all(axis=1).sum()),'new_finite_Z_rows':int(np.isfinite(h['Z_total']).all(axis=1).sum()),
                      'max_Z_error_common_finite':err,'max_v_error_common_finite':float(np.max(np.abs(v[vm]-oldv[vm]))),
                      'first_Z_difference_gt_1e-12':firstdiff,'first_Z_difference_vector':(vec[firstdiff]-h['Z_total'][firstdiff]).tolist() if firstdiff is not None else None,
                      'initial_J_error':float(abs(raw['J_eff'][0]-h['J_eff'][0])),
                      'same_finiteness':bool(np.array_equal(np.isfinite(vec),np.isfinite(h['Z_total']))),
                      'window_rows':len(actual),'spike_indices_new':ix.tolist(),
                      'at_max_finite_v':{k:float(comp[k][np.argmax(np.where(np.isfinite(v),v,-np.inf))]) for k in ('dZ','dphi','dcorr','dkappa')},
                      'phase_clock_alone_ge_0.8':int((np.sqrt(comp['dphi']**2+.25*comp['dcorr']**2)>=.8).sum()),
                      'dZ_alone_ge_0.8_finite':int((np.isfinite(comp['dZ'])&(comp['dZ']>=.8)).sum()),**stats(h)}
        # One bounded provenance hypothesis, not fitting: saved metadata omits lambda_phase.
        # The inspected older 17766958 core lacks the triad synchronizer.
        rng=np.random.default_rng(2158500047); oi=rng.standard_normal(3)+1j*rng.standard_normal(3); oi/=norm(oi)+1e-12
        pp=core.ModelParams(eps=.0005,g=g,k_vals=const.default_k_triplet(),lambda_phase=0.)
        hh=core.TriOctaPhaseLockModel(pp).run(core.ModelState(oi),n_steps=2000,dt=.02776)
        vv=defs.compute_recursive_velocity_geom(hh); mm=np.isfinite(vec).all(axis=1)&np.isfinite(hh['Z_total']).all(axis=1); mv=np.isfinite(vv)&np.isfinite(oldv)
        saved[label]['phase_off_provenance_hypothesis']={'lambda_phase':0.,'count':int((np.isfinite(vv)&(vv>=.8)).sum()),
            'max_Z_error_common_finite':float(np.max(np.abs(vec[mm]-hh['Z_total'][mm]))),
            'max_v_error_common_finite':float(np.max(np.abs(vv[mv]-oldv[mv]))),
            'same_Z_finiteness':bool(np.array_equal(np.isfinite(vec),np.isfinite(hh['Z_total'])))}
        check(label+'_phase_off_full_Z_parity',np.array_equal(vec,hh['Z_total'],equal_nan=True))
        check(label+'_phase_off_full_v_parity',np.array_equal(oldv,vv,equal_nan=True))
        check(label+'_saved_time_grid',np.array_equal(raw['t'],np.arange(2000)*.02776))
        saved[label]['phase_off_provenance_hypothesis']['J_max_error_common_finite']=fmax(abs(raw['J_eff']-defs.compute_jeff_series(hh)))
        # CSV comparison is a reported result, not assumed equality to an unidentified old core.
        check(label+'_v_formula',np.allclose(v,np.sqrt(comp['dZ']**2+comp['dphi']**2+.25*comp['dcorr']**2),equal_nan=True))
    h2=ns['run_triocta_once'](2158500047,.0005,.664,2.,.02776,2000)
    check('spike_CLI_k3_ignored',np.array_equal(h2['Omega'],critical['subcritical']['Omega']))
    # Geometric identities and counterexamples: no scaffold coordinates fabricated.
    th=np.linspace(0,2*np.pi,721); z=np.cos(3*(th-.244)); m=z[:,None]*np.column_stack((np.cos(th),np.sin(th),np.ones(len(th))))
    ext=.244+np.arange(6)*np.pi/3; ev=np.cos(3*(ext-.244)); em=ev[:,None]*np.column_stack((np.cos(ext),np.sin(ext),np.ones(6)))
    check('harmonic_extrema_derivative_zero',np.max(np.abs(-3*np.sin(3*(ext-.244))))<1e-13)
    check('harmonic_extrema_alternate',np.allclose(ev,(-1.)**np.arange(6)))
    check('macro_double_cone',np.max(np.abs(m[:,0]**2+m[:,1]**2-m[:,2]**2))<1e-14)
    check('extrema_three_vertical_pairs',all(np.allclose(em[j,:2],em[j+3,:2]) and np.isclose(em[j,2],-em[j+3,2]) for j in range(3)))
    q=np.arange(12); sample=np.cos(3*(q*np.pi/6-.244))
    check('four_sector_repeat',np.allclose(sample,np.tile([np.cos(.732),np.sin(.732),-np.cos(.732),-np.sin(.732)],3)))
    check('default_not_extrema_aligned',not np.any(np.isclose(abs(sample),1,atol=1e-12)))
    for h in [base,*critical.values()]:
        kap=h['kappa'][1:]; good=np.isfinite(kap)&(kap<1e50)&(kap>0)
        check('chiral_bound_finite_scaled_'+str(len(checks)),np.all(norm(h['Z_chiral'][1:][good]/kap[good,None]**2)<=.5+1e-13))
    o=np.array([1+1j,2-1j,.5+2j]); c=chiral(o)
    check('conjugation_reverses_C',np.array_equal(chiral(o.conjugate()),-c))
    check('global_phase_preserves_C',np.allclose(chiral(o*np.exp(.7j)),c))
    check('J_not_global_phase_invariant',not np.isclose(np.imag(o[0]*o[1].conjugate()*o[2]),np.imag((o*np.exp(.7j))[0]*(o*np.exp(.7j))[1].conjugate()*(o*np.exp(.7j))[2])))
    # Same kappa/clock/scalar, different phases and C: not a coordinate change of A/B.
    oa=np.array([1,1,1],complex); ob=np.array([1,1j,1],complex)
    check('same_kappa_different_C',norm(oa)==norm(ob) and not np.array_equal(chiral(oa),chiral(ob)))
    check('alternate_cylinder_agrees',np.array_equal(geo.history_to_xyz(base),alt.history_to_xyz(base)))
    check('alternate_torus_agrees',np.array_equal(geo.history_to_torus_xyz(base),alt.history_to_torus_xyz(base,alt.TorusConfig(2,1)) ))
    synthetic={}
    for name,zpts in [('radial',[[1,0,0],[10,0,0]]),('near_zero_flip',[[1e-8,0,0],[-1e-8,0,0]]),('clock_only',[[1,0,0],[1,0,0]])]:
        h={'Z_total':np.array(zpts,float),'phi_index':np.array([0,1] if name=='clock_only' else [0,0])}
        synthetic[name]={'v':float(defs.compute_recursive_velocity_geom(h)[0]),'direction':float(defs.vrec_geom_direction(h)[0])}
    ns['v_rec_series']=np.full(10,.5); tied,_=ns['pick_spikes'](ns['v_rec_series'],'pctl',.99)
    check('percentile_ties_all_selected',len(tied)==10)
    ns['v_rec_series']=np.array([0.,2.,0.]); stale,_=ns['pick_spikes'](np.array([2.,0.,0.]),'abs',1.)
    check('picker_global_dependency',stale.tolist()==[1])
    # Bounded large-input witness: balanced real line, equal k, no C despite amplitude growth.
    a=10.; growth=[]
    for _ in range(4): growth.append(a); a=a*(1+.05*(1-a*a))
    check('radial_blowup_witness',all(abs(growth[j+1])>abs(growth[j]) for j in range(3)))
    # Six reproducible figures, mathematical/display coordinates only, equal 3D units.
    figdir=HERE/'figures'; figdir.mkdir(exist_ok=True)
    plt.rcParams.update({'font.size':10,'axes.titlesize':11,'figure.dpi':140})
    def ax3(fig,pos,pts,title,lim=None):
        ax=fig.add_subplot(pos,projection='3d'); ax.plot(*pts.T,lw=.7); ax.set_title(title)
        ax.set_xlabel('Z1'); ax.set_ylabel('Z2'); ax.set_zlabel('Z3'); ax.set_box_aspect((1,1,1))
        center=(pts.max(axis=0)+pts.min(axis=0))/2; radius=max(float(np.ptp(pts,axis=0).max()/2),1e-12)*1.1
        if lim is not None: center=np.zeros(3); radius=lim
        ax.set_xlim(center[0]-radius,center[0]+radius); ax.set_ylim(center[1]-radius,center[1]+radius); ax.set_zlim(center[2]-radius,center[2]+radius)
        return ax
    def save(fig,name):
        fig.set_layout_engine(None); fig.subplots_adjust(left=.055,right=.95,bottom=.11,top=.92,wspace=.25,hspace=.40)
        fig.savefig(figdir/(name+'.png'),dpi=160,bbox_inches='tight',pad_inches=.22); plt.close(fig)
    f=plt.figure(figsize=(12,5),layout='constrained'); ax=f.add_subplot(121)
    ax.plot(th*180/np.pi,z,label='continuous, frozen amplitude A=1'); ax.scatter(q*30,sample,label='12 sectors, lock=0.244'); ax.scatter(ext*180/np.pi,ev,marker='x',label='six signed extrema')
    ax.set(xlabel='clock angle (degrees)',ylabel='z / A',title='Third harmonic; no scaffold registration'); ax.legend(fontsize=8)
    ax=ax3(f,122,m,'Direct macro: extrema form three vertical pairs'); ax.scatter(*em.T,c=np.arange(6),cmap='viridis',s=45)
    for i,e in enumerate(em): ax.text(*e,str(i),fontsize=8)
    save(f,'01_harmonic_and_macro')
    f=plt.figure(figsize=(15,5),layout='constrained'); lim=max(norm(base[k]).max() for k in ('Z_macro','Z_chiral','Z_total'))*1.05
    for j,k in enumerate(('Z_macro','Z_chiral','Z_total')): ax3(f,131+j,base[k],k+' | viewer-default recurrence',lim)
    save(f,'02_direct_components')
    f=plt.figure(figsize=(14,9),layout='constrained')
    for row,label in enumerate(('subcritical','critical')):
        h=critical[label]; v,comp=defs.compute_recursive_velocity_geom(h,return_components=True); t=h['t'][1:]; ix=np.flatnonzero(np.isfinite(v)&(v>=.8))
        ax=f.add_subplot(2,2,2*row+1)
        for values,l in [(v,'v_rec'),(comp['dZ'],'dZ'),(comp['dphi'],'phase jump'),(.5*comp['dcorr'],'clock term')]: ax.plot(t,values,label=l,lw=.8)
        ax.axhline(.8,color='gray',ls='--'); ax.set(xlabel='historical t',ylabel='diagnostic (display clipped at 4)',ylim=(0,4),title=f'{label}: g={.664 if row==0 else .667}, {len(ix)} finite events'); ax.legend(fontsize=8)
        ax=ax3(f,222+2*row,h['Z_total'][:400],label+' direct total; first 400 points')
        ix=ix[(ix+1)<400]; ax.scatter(*h['Z_total'][ix+1].T,color='red',s=4,alpha=.3)
    save(f,'03_preserved_settings_spikes')
    f=plt.figure(figsize=(15,5),layout='constrained')
    maps=[np.array(geo.history_to_xyz(base)).T,np.array(geo.history_to_torus_xyz(base)).T,base['Z_total']]
    for j,(points,title) in enumerate(zip(maps,['A: cylinder (kappa cos theta, kappa sin theta, z)','B: history-normalized torus','C: direct Z_total'])):
        ax=ax3(f,131+j,points,title); ax.set_xlabel('display X'); ax.set_ylabel('display Y'); ax.set_zlabel('display Z')
    save(f,'04_distinct_embeddings')
    f=plt.figure(figsize=(14,9),layout='constrained')
    for j,name in enumerate(('viewer_default','EMA','gamma_zero','beta_zero')):
        ax3(f,221+j,cases[name]['Z_total'],name+' | equal spatial units')
    save(f,'05_envelope_memory_blend')
    f=plt.figure(figsize=(15,5),layout='constrained'); h={k:v[:400] for k,v in critical['critical'].items() if isinstance(v,np.ndarray)}
    lim=max(norm(h['Z_macro']).max(),norm(.5*h['Z_chiral']).max(),norm(h['Z_total']).max())*1.05
    for j,(pts,title) in enumerate([(h['Z_macro'],'Macro'),(.5*h['Z_chiral'],'Weighted chirality (beta=0.5)'),(h['Z_total'],'Total')]): ax3(f,131+j,pts,title+' | critical first 400',lim)
    save(f,'06_critical_component_separation')
    source_paths=[OLD/(x+'.py') for x in ('model_core','definitions','geometry_3d','geometry_embeddings','z_spike_diagnostic','toy_3d_triocta','constants_selector','phase_triad_sync','su3_basis','identity_rules','latent_foreclosure','provenance','analysis_tools','chirality_lab','diagnose_bottom_lid','cp_windows','dual_tetra_mapper','side_zchiral_probe','run_triocta_structural_3body_probe','triocta_probe_utils','run_sim','toy_ui','tangent_corridor_analysis','semantic_diagnostics','edge_map','rgd_connection_diagnostics')]
    source_paths += [EMA,REPO/'kernel_physics/readouts.py',REPO/'kernel_physics/dynamics.py',REPO/'papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md',REPO/'research_files/sources/Zenodo_research/tri_octagon_Model/17766958/model_core.py']
    sources={str(p):sha(p) for p in source_paths}
    result={'attribution':'New Codex source-body re-execution, not original captured run or new independent Claude review',
            'environment':{'python':sys.version,'numpy':np.__version__,'matplotlib':matplotlib.__version__},
            'execution_scope':'17 viewer-setting runs + one EMA + three 2000-step spike-setting runs + two explicitly labelled phase-off provenance hypotheses; no sweeps/UI/RSB',
            'source_hashes':sources,'checks':checks,'pass_count':len(checks),'readout_max_errors':errors,
            'defaults':{'k_theta_scaled':const.default_k_triplet().tolist(),'k_theta_soft':p.k_vals.tolist(),
                        'eps':p.eps,'g':p.g,'lambda_phase':p.lambda_phase,'theta_lock':p.theta_lock,'lambda_vp':p.lambda_vp,'gamma':p.gamma,'alpha':p.z_alpha,'beta':p.z_beta},
            'harmonic':{'extrema_radians':ext.tolist(),'q_samples':sample.tolist(),'direct_extrema':em.tolist()},
            'baseline_stats':stats(base),'EMA_stats':stats(old),'parameter_comparisons':sensitivities,
            'preserved_diagnostics':saved,'synthetic_metric_witnesses':synthetic,'large_input_balanced_amplitudes':growth,
            'same_kappa_different_C':{'Omega_a':'(1,1,1)','Omega_b':'(1,i,1)','C_a':chiral(oa).tolist(),'C_b':chiral(ob).tolist()},
            'figures':[p.name for p in sorted(figdir.glob('*.png'))],
            'registration':'NOT_FOUND within inspected source/display/diagnostic closure; no spatial gap coordinates supplied'}
    dump(HERE/'verification_results.json',result)
    print('PASS',len(checks),'checks; six figures. Saved/default/phase-off spike counts:',
          {k:(v['saved_count'],v['new_count'],v['phase_off_provenance_hypothesis']['count']) for k,v in saved.items()})

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--baseline',action='store_true'); ap.add_argument('--seal',action='store_true'); ap.add_argument('--deps')
    args=ap.parse_args()
    if args.baseline: baseline()
    elif args.seal: seal()
    else: verify(args.deps)
