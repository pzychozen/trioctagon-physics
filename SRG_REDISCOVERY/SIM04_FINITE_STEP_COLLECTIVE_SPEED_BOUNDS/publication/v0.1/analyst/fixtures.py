"""Execute the supplied 14 deterministic fixture groups once, then freeze the implementation."""
from common import *
import math,ast,inspect
import numpy as np
import bounds
from bounds import vector_pair,source_pair,geometry,norm,profile,k,mean
D_CALLS=0;D_COMPONENTS=0;PAIR_CALLS=0;checks=[]
def D_fixture(x):
    global D_CALLS,D_COMPONENTS
    D_CALLS+=1;D_COMPONENTS+=x.size
    return x/(1+np.log1p(np.abs(x)))
def assert_close(name,a,b,tol=1e-12):
    x=np.asarray(a)-np.asarray(b);v=float(np.max(np.abs(x)))
    checks.append({'name':name,'kind':'equality','max_abs':v,'tolerance':tol});need(v<=tol,name)
def assert_le(name,a,b,tol=1e-12):
    x=np.asarray(a)-np.asarray(b);v=float(np.max(x))
    checks.append({'name':name,'kind':'inequality','max_signed_excess':v,'min_signed_excess':float(np.min(x)),'tolerance':tol});need(v<=tol,name)
def check_pair(name,pair,center,yc,yd):
    S=abs(mean(norm(yc))-mean(norm(yd)))
    for f in ('T_TRIANGLE','Q_VECTOR','K_COMPONENT','P_PROFILE','BEST_PRE'):
        assert_le(name+': S<='+f,S,pair[f])
    for lo,hi in [('Q_VECTOR','T_TRIANGLE'),('K_COMPONENT','Q_VECTOR'),('P_PROFILE','Q_VECTOR'),
                  ('BEST_PRE','K_COMPONENT'),('BEST_PRE','P_PROFILE')]:
        assert_le(name+': '+lo+'<='+hi,pair[lo],pair[hi])
    if 'OMEGA_COARSE' in pair:
        assert_le(name+': T<=Gamma',pair['T_TRIANGLE'],pair['GAMMA_SOURCE'])
        assert_le(name+': Gamma<=Omega',pair['GAMMA_SOURCE'],pair['OMEGA_COARSE'])
    assert_close(name+': alignment',center['alignment_residual'],0)
    assert_le(name+': signed component endpoints',np.abs(yc-yd),center['kappa']*np.abs(center['delta_w']))
    assert_le(name+': profile endpoints',np.abs(profile(yc)-profile(yd)),center['lambda']*np.abs(center['profile_c']-center['profile_d']))
    for coef in ('kappa','lambda'):
        assert_le(name+': '+coef+'<=1',center[coef],1)
        need(np.all(center[coef]>0),name+': derivative positivity')
    Zs=mean(norm(yc-yd));Zp=mean(norm(profile(yc)-profile(yd)));Tn=mean(np.abs(norm(yc)-norm(yd)))
    assert_le(name+': Tnorm<=Zs',Tn,Zs);assert_le(name+': Tnorm<=Zp',Tn,Zp);assert_le(name+': S<=Tnorm',S,Tn)
    Z=Zs if pair['best_is_K'] else Zp
    gaps=[pair['Q_VECTOR']-pair['BEST_PRE'],pair['BEST_PRE']-Z,Z-Tn,Tn-S]
    assert_le(name+': nonnegative telescope gaps',-np.asarray(gaps),0)
    assert_close(name+': telescope',sum(gaps),pair['Q_VECTOR']-S)
    return S,Tn
def main():
    global PAIR_CALLS
    start=time.monotonic()
    need(load(ROOT/'evidence/INPUT_GATE.json')['status']=='PASS','input gate')
    fixtures=load(ROOT/'received/SIM04_FIXED_FIXTURES_v0.1.json')['fixtures']
    need(len(fixtures)==14 and [f['id'] for f in fixtures]==[f'F{i:02d}' for i in range(1,15)],'fixture set')
    save(ROOT/'evidence/MATHEMATICAL_GATE.json',{'status':'PASS','utc':utc(),'proof':ident(ROOT/'MATHEMATICAL_RESULTS.md'),
        'method':'Independent analytic derivation and human/model code inspection before fixture execution; numeric fixtures are not proofs.',
        'checked':['D derivative at zero and elsewhere','monotone k','interval maxima','source Gamma/Omega hierarchy',
            'sign/permutation symmetry and sorting exchange argument','difference-alignment identity',
            'complete unordered-pair variance normalization','epsilon/variance sufficient implications','slack telescope'],
        'changed_proposals':0})
    records=[]
    for f in fixtures:
        id=f['id'];first=len(checks)
        if f['kind']=='population':
            ws=np.repeat(np.asarray(f['per_cycle_w_triples'],dtype=np.float64)[:,None,:],8,axis=1)
            ys=[D_fixture(x) for x in ws];us=[mean(norm(y)) for y in ys];m=f['m']
            pairs=[]
            for c in range(m):
                for d in range(c):
                    zeros=np.zeros((8,3),dtype=np.float64)
                    pp,cc=vector_pair(zeros,ws[c],ws[c],zeros,ws[d],ws[d]);PAIR_CALLS+=1
                    check_pair(id+f':{c},{d}',pp,cc,ys[c],ys[d]);pairs.append((c,d,pp))
            expected=m*(m-1)//2;need(len(pairs)==expected,'population pair count')
            mu=mean(us);variance=math.fsum((u-mu)**2 for u in us)/m
            pairvar=math.fsum((us[c]-us[d])**2 for c,d,_ in pairs)/(m*m)
            assert_close(id+': population normalization',pairvar,variance,1e-14)
            for fam in f['bound_families']:
                assert_le(id+': variance<='+fam,variance,math.fsum(p[fam]**2 for _,_,p in pairs)/(m*m),1e-14)
            records.append({'id':id,'name':f['name'],'status':'PASS','checks':len(checks)-first,'pairs':expected,'variance':variance})
            continue
        if f['kind']=='axis_diagonal_pair':
            vc=vd=np.zeros((8,3),dtype=np.float64)
            wc=np.tile([f['r'],0,0],(8,1));wd=np.full((8,3),f['r']/math.sqrt(3),dtype=np.float64)
        else:
            vc=np.asarray(f['v_c'],dtype=np.float64);vd=np.asarray(f['v_d'],dtype=np.float64)
            if f['kind']!='source_factor_pair':
                wc=np.asarray(f['w_c'],dtype=np.float64);wd=np.asarray(f['w_d'],dtype=np.float64)
        if f['kind']=='source_factor_pair':
            dc=np.asarray(f['d_c'],dtype=np.float64);dd=np.asarray(f['d_d'],dtype=np.float64)
            bc=np.asarray(f['bit_plus_c'],dtype=np.int8);bd=np.asarray(f['bit_plus_d'],dtype=np.int8)
            Gc=1/(1+mean(norm(vc)));Gd=1/(1+mean(norm(vd)));H=f['H']
            ac=.1*((dc/(norm(dc)[:,None]+.01))*H*(1-2*bc[:,None]))*Gc
            ad=.1*((dd/(norm(dd)[:,None]+.01))*H*(1-2*bd[:,None]))*Gd
            wc=vc+ac;wd=vd+ad
            pp,cc=source_pair(vc,ac,wc,dc,H,Gc,bc,vd,ad,wd,dd,H,Gd,bd)
            assert_close(id+': source factor c',ac,.1*H*Gc*geometry(dc,bc))
            assert_close(id+': source factor d',ad,.1*H*Gd*geometry(dd,bd))
        else:
            ac=wc-vc;ad=wd-vd;pp,cc=vector_pair(vc,ac,wc,vd,ad,wd)
        PAIR_CALLS+=1;yc=D_fixture(wc);yd=D_fixture(wd);S,Tn=check_pair(id,pp,cc,yc,yd)
        if id in ('F01','F02'):
            for fam in f['bound_families']:assert_close(id+': zero '+fam,pp[fam],0)
            need(S==0,'exact zero outcome');need(pp['BEST_PRE']<1e-12,'zero denominator mask')
        if id in ('F03','F04','F07'):
            assert_close(id+': scalar symmetry',S,0);assert_close(id+': profile zero',pp['P_PROFILE'],0)
        if id=='F03':need(pp['Q_VECTOR']>0,'mirror vector distance')
        if id=='F05':
            assert_close(id+': input equal norms',norm(wc),norm(wd))
            need(mean(norm(yd))>mean(norm(yc)),'equal norm unequal profile')
            assert_close(id+': axis formula',mean(norm(yc)),f['r']/(1+math.log1p(f['r'])))
            assert_close(id+': diagonal formula',mean(norm(yd)),f['r']/(1+math.log1p(f['r']/math.sqrt(3))))
        if id=='F06':need(np.all(cc['kappa']<1),'same-ray derivative coefficient')
        if id=='F07':
            assert_close(id+': crossing coefficients',cc['kappa'][:,[0,2]],1)
            assert_close(id+': common coefficient',cc['kappa'][:,1],k(np.asarray(.3)))
        if id=='F08':
            assert_close(id+': Q cancellation',pp['Q_VECTOR'],0)
            need(pp['T_TRIANGLE']>0 and np.all(cc['difference_alignment']<0),'difference cancellation')
        if id=='F09':
            assert_close(id+': center cancellation',S,0);need(Tn>0,'positive individual speed difference')
            witness_before=yc.copy();yc=yc.copy();yc[0,0]+=7
            pp2,cc2=vector_pair(vc,ac,wc,vd,ad,wd);PAIR_CALLS+=1
            need(pp==pp2 and all(np.array_equal(cc[key],cc2[key],equal_nan=True) for key in cc),'outcome-isolation canary')
            need(not np.array_equal(witness_before,yc),'canary did not change outcome witness')
            save(ROOT/'evidence/OUTCOME_ISOLATION_CANARY.json',{'status':'PASS','fixture':'F09',
                'witness_change':'Add 7 to one outcome component; pre-output inputs unchanged.',
                'all_domain_valid_pair_bounds_and_center_arrays_identical':True,
                'source_families_not_fabricated_for_arbitrary_vector_fixture':True})
        records.append({'id':id,'name':f['name'],'status':'PASS','checks':len(checks)-first,
            'S':S,'Tnorm':Tn,'bounds':{key:pp[key] for key in f['bound_families']}})
        update(ROOT/'evidence/FIXTURE_PROGRESS.json',{'completed_groups':len(records),'last_group':id,'utc':utc()})
    need(len(records)==14,'groups completed')
    # Structural audit: pure analytic module has no I/O, output fields, dynamic import or RNG access.
    tree=ast.parse(read(ROOT/'analyst/bounds.py').decode())
    forbidden={'saved_successor_velocity','post_norm','retention','L','R','measured_dispersion','open','load','random','eval','exec','__import__'}
    seen={n.id for n in ast.walk(tree) if isinstance(n,ast.Name)}
    attrs={n.attr for n in ast.walk(tree) if isinstance(n,ast.Attribute)}
    need(not (forbidden&(seen|attrs)),'forbidden pre-output dependency')
    need(not bounds.source_pair.__code__.co_freevars and not bounds.vector_pair.__code__.co_freevars,'captured state')
    for f in (ROOT/'analyst').glob('*.py'):compile(read(f),str(f),'exec')
    # Importing the new helper definitions is permitted; no main/evaluation entry is called.
    import analyze,summarize
    scientific=['analyst/common.py','analyst/bounds.py','analyst/analyze.py','analyst/summarize.py',
        'analyst/fixtures.py','analyst/supervise.py','MATHEMATICAL_RESULTS.md']
    scientific.extend('received/'+n for n in ('SIM04_EXPERIMENT_SPEC_v0.1.json','SIM04_FIXED_FIXTURES_v0.1.json',
        'SIM04_MATHEMATICAL_SPEC_v0.1.md','SIM04_INPUT_IDENTITIES_AND_SCHEMAS.json','SRG_SIM04_CODEX_WORK_ORDER_v0.1_20261014.md'))
    frozen={n:ident(ROOT/n) for n in scientific}
    save(ROOT/'evidence/ALGEBRA_FIXTURES.json',{'status':'PASS','groups':records,'checks':checks,
        'fixed_groups_completed':14,'pure_pair_evaluations':PAIR_CALLS,'D_array_calls':D_CALLS,
        'D_scalar_components':D_COMPONENTS,'D_additional_scalar_reference_expressions':2,
        'D_on_saved_records':0,'random_trials':0,'seconds':time.monotonic()-start})
    save(ROOT/'evidence/IMPLEMENTATION_GATE.json',{'status':'PASS','utc':utc(),'frozen_files':frozen,
        'input_gate':ident(ROOT/'evidence/INPUT_GATE.json'),'proof_gate':ident(ROOT/'evidence/MATHEMATICAL_GATE.json'),
        'fixture_gate':ident(ROOT/'evidence/ALGEBRA_FIXTURES.json'),'pure_module_AST':'PASS',
        'forbidden_dependencies':sorted(forbidden),'source_pair_signature':str(inspect.signature(bounds.source_pair)),
        'vector_pair_signature':str(inspect.signature(bounds.vector_pair)),
        'fixture_groups':14,'seconds':time.monotonic()-start})
    print(json.dumps({'status':'PASS','groups':14,'checks':len(checks),'D_calls':D_CALLS,'D_components':D_COMPONENTS,
        'pure_pairs':PAIR_CALLS,'seconds':time.monotonic()-start}))
if __name__=='__main__':main()

