"""Independent, read-only SIM04 verifier. No imports of submitted scientific code.

Usage:
  python -B review_sim04_saved_evidence.py --submission <extracted SIM04 ZIP> \
      --archive <SIM04_GPT_REVIEW.zip> --seal <SIM04_TRANSPORT_SEAL.json> \
      --upstream-candidate <SIM03...CANDIDATE.zip> --handoff <SRG_SIM04...zip> \
      --output <new reviewer output directory>

Calculates only the fixed inequalities from accepted stored intermediates.
D is evaluated only on the supplied deterministic synthetic fixtures.
No trajectory, centroid, position update, RNG operation, or network access.
"""
from __future__ import annotations
import argparse, ast, csv, hashlib, json, math, platform, stat, sys, time, zipfile
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import numpy as np

FAMILIES = ('OMEGA_COARSE','GAMMA_SOURCE','T_TRIANGLE','Q_VECTOR','K_COMPONENT','P_PROFILE','BEST_PRE')
PAIRS = [(c,d) for c in range(1,5) for d in range(c)]
LOG, ISSUES, RES = {}, [], {}
COUNTS = dict(primary_pair_phase=0, selected_updates=0, selected_center_records=0,
              labeled_center_pairs=0, outcome_pair_phase=0, view_phase=0,
              fixture_groups=0, fixture_pair_calls=0, fixture_D_array_calls=0,
              fixture_D_scalar_components=0, fixture_D_scalar_reference_expressions=0)

def now(): return datetime.now(timezone.utc).isoformat()
def ident(raw): return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def oid(raw): return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def readj(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def writej(path, obj): Path(path).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
def exact(name,a,b):
    ok=a==b
    LOG[name]={'status':'PASS' if ok else 'FAIL'}
    if not ok: ISSUES.append(name)
    return ok

def check(name,a,b=0.0,tol=1e-12,inequality=False):
    a,b=np.asarray(a),np.asarray(b)
    if a.shape != b.shape and b.ndim != 0:
        LOG[name]={'status':'FAIL','shape_a':list(a.shape),'shape_b':list(b.shape)};ISSUES.append(name);return
    if a.dtype.kind in 'biu' and b.dtype.kind in 'biu' and not inequality:
        ok=bool(np.array_equal(a,b)); LOG[name]={'status':'PASS' if ok else 'FAIL','shape':list(a.shape),'exact':True}
        if not ok: ISSUES.append(name)
        return
    af,bf=a.astype(float),b.astype(float)
    same_nan=np.array_equal(np.isnan(af),np.isnan(np.broadcast_to(bf,af.shape)))
    x=af-bf; vals=x[~np.isnan(x)].reshape(-1)
    finite=bool(np.isfinite(vals).all())
    value=float(np.max(vals) if inequality else np.max(np.abs(vals))) if len(vals) else 0.0
    ok=same_nan and finite and value<=tol
    LOG[name]={'status':'PASS' if ok else 'FAIL','shape':list(a.shape),'max_abs_difference':float(np.max(np.abs(vals))) if len(vals) else 0.,
               'min_signed':float(np.min(vals)) if len(vals) else 0.,'max_signed':float(np.max(vals)) if len(vals) else 0.,
               'tolerance':tol,'inequality':inequality,'same_nan_mask':same_nan}
    if not ok: ISSUES.append(name)

def native(name,a,tol=1e-12,ineq=False):
    RES[name]=np.asarray(a,dtype=float)
    check('native/'+name,RES[name],tol=tol,inequality=ineq)

def avg(x): return math.fsum(map(float,x))/len(x)
def norm(x): return np.sqrt(np.sum(np.asarray(x)*np.asarray(x),axis=-1))
def prof(x): return np.sort(np.abs(x),axis=-1)
def slope(s):
    ell=np.log1p(s)
    return ((1+ell)-s/(1+s))/((1+ell)*(1+ell))
def var(x):
    m=avg(x);return math.fsum((float(t)-m)**2 for t in x)/len(x)
def geom(d,b): return (d*(1.0-2.0*np.asarray(b)[:,None]))/(norm(d)[:,None]+0.01)

def evaluate_pair(vc,ac,wc,vd,ad,wd,source=None):
    # Entire analytic function is outcome-free and has no I/O.
    dv=vc-vd; da=ac-ad; dw=wc-wd
    vn=norm(dv); an=norm(da); wn=norm(dw)
    crosses=(np.minimum(wc,wd)<=0)&(np.maximum(wc,wd)>=0)
    ell=np.minimum(np.abs(wc),np.abs(wd)).copy(); ell[crosses]=0
    kap=slope(ell)
    pc,pd=prof(wc),prof(wd); lam=slope(np.minimum(pc,pd))
    kc,pp=norm(kap*dw),norm(lam*(pc-pd))
    alignment=2*np.sum(dv*da,axis=-1)
    valid=(vn>0)&(an>0);cos=np.full(8,np.nan)
    np.divide(alignment,2*vn*an,out=cos,where=valid)
    V,J=avg(vn),avg(an); Q,K,P=avg(wn),avg(kc),avg(pp)
    pair=dict(T_TRIANGLE=V+J,Q_VECTOR=Q,K_COMPONENT=K,P_PROFILE=P,BEST_PRE=min(K,P),V=V,J=J,
              best_is_K=bool(K<=P),T_minus_Q=V+J-Q)
    center=dict(delta_v=dv,delta_a=da,delta_w=dw,v_distance=vn,a_distance=an,Q_center=wn,
        K_center=kc,P_center=pp,T_center=vn+an,difference_alignment=alignment,
        difference_cosine=cos,difference_cosine_valid=valid,alignment_residual=wn*wn-vn*vn-an*an-alignment,
        triangle_slack=vn+an-wn,contains_zero=crosses,ell=ell,kappa=kap,**{'lambda':lam},
        profile_c=pc,profile_d=pd,profile_distance=norm(pc-pd))
    if source is not None:
        dc,bc,Hc,Gc,dd,bd,Hd,Gd=source
        gc,gd=geom(dc,bc),geom(dd,bd);rg=avg(norm(gc-gd));qc,qd=avg(norm(gc)),avg(norm(gd))
        h=abs(0.1*Hc);dg=abs(Gc-Gd)
        gam1=V+h*(dg*qc+Gd*rg);gam2=V+h*(dg*qd+Gc*rg)
        pair.update(GAMMA_SOURCE=min(gam1,gam2),OMEGA_COARSE=(1+h)*V+h*min(Gc,Gd)*rg,
                    Gamma_c_given_d=gam1,Gamma_d_given_c=gam2,Rg=rg,qbar_c=qc,qbar_d=qd,
                    G_c=Gc,G_d=Gd,abs_delta_G=dg,H_c=Hc,H_d=Hd,h=h)
        center.update(g_c=gc,g_d=gd)
    return pair,center

def synthetic_D(x):
    COUNTS['fixture_D_array_calls']+=1;COUNTS['fixture_D_scalar_components']+=x.size
    return x/(1+np.log1p(np.abs(x)))

def fixture_check(name,p,c,yc,yd):
    S=abs(avg(norm(yc))-avg(norm(yd))); Tn=avg(np.abs(norm(yc)-norm(yd)))
    for fam in FAMILIES:
        if fam in p:check(name+'/S<='+fam,S,p[fam],inequality=True)
    for lo,hi in [('Q_VECTOR','T_TRIANGLE'),('K_COMPONENT','Q_VECTOR'),('P_PROFILE','Q_VECTOR'),
                  ('BEST_PRE','K_COMPONENT'),('BEST_PRE','P_PROFILE'),('T_TRIANGLE','GAMMA_SOURCE'),('GAMMA_SOURCE','OMEGA_COARSE')]:
        if hi in p:check(name+'/'+lo+'<='+hi,p[lo],p[hi],inequality=True)
    check(name+'/signed_endpoint',np.abs(yc-yd),c['kappa']*np.abs(c['delta_w']),inequality=True)
    check(name+'/profile_endpoint',np.abs(prof(yc)-prof(yd)),c['lambda']*np.abs(c['profile_c']-c['profile_d']),inequality=True)
    check(name+'/alignment',c['alignment_residual'])
    for coeff in ['kappa','lambda']:
        check(name+'/'+coeff+'<=1',c[coeff],1,inequality=True)
        exact(name+'/'+coeff+'>0',bool((c[coeff]>0).all()),True)
    Zs,Zp=avg(norm(yc-yd)),avg(norm(prof(yc)-prof(yd)))
    Z=Zs if p['best_is_K'] else Zp
    for lo,hi,k in [(S,Tn,'center_triangle'),(Tn,Zs,'signed_norm'),(Tn,Zp,'profile_norm'),(Z,p['BEST_PRE'],'derivative')]:
        check(name+'/'+k,lo,hi,inequality=True)
    gap=[p['Q_VECTOR']-p['BEST_PRE'],p['BEST_PRE']-Z,Z-Tn,Tn-S]
    check(name+'/gap_nonnegative',-np.array(gap),inequality=True)
    check(name+'/gap_sum',math.fsum(gap),p['Q_VECTOR']-S)
    return S,Tn

def fixtures(root):
    fixed=readj(root/'received/SIM04_FIXED_FIXTURES_v0.1.json')['fixtures']
    evidence=readj(root/'evidence/ALGEBRA_FIXTURES.json')
    exact('fixtures/count',len(fixed),14);exact('fixtures/submitted_assertion_count',len(evidence['checks']),607)
    for q in evidence['checks']:
        val=q['max_abs'] if q['kind']=='equality' else q['max_signed_excess']
        exact('fixture_receipt/'+q['name'],val<=q['tolerance'],True)
    records=[]
    for f,stored in zip(fixed,evidence['groups']):
        tag=f['id'];zero=np.zeros((8,3));kind=f['kind'];before=len(LOG)
        if kind=='population':
            m=f['m']; ws=np.repeat(np.asarray(f['per_cycle_w_triples'],float)[:,None,:],8,axis=1)
            ys=[synthetic_D(w) for w in ws];us=[avg(norm(y)) for y in ys];pairs=[]
            for c in range(m):
                for d in range(c):
                    p,z=evaluate_pair(zero,ws[c],ws[c],zero,ws[d],ws[d]);COUNTS['fixture_pair_calls']+=1
                    fixture_check(tag+f'/{c}_{d}',p,z,ys[c],ys[d]);pairs.append((c,d,p))
            vv=var(us);pv=math.fsum((us[c]-us[d])**2 for c,d,_ in pairs)/(m*m)
            check(tag+'/variance_identity',vv,pv,tol=1e-14)
            check(tag+'/stored_variance',vv,stored['variance'],tol=1e-14)
            for fam in f['bound_families']:
                check(tag+'/variance_'+fam,vv,math.fsum(p[fam]**2 for _,_,p in pairs)/(m*m),tol=1e-14,inequality=True)
        else:
            if kind=='axis_diagonal_pair':
                vc=vd=zero;wc=np.tile([f['r'],0.,0.],(8,1));wd=np.full((8,3),f['r']/math.sqrt(3))
            else:
                vc,vd=np.asarray(f['v_c'],float),np.asarray(f['v_d'],float)
                if kind!='source_factor_pair':wc,wd=np.asarray(f['w_c'],float),np.asarray(f['w_d'],float)
            source=None
            if kind=='source_factor_pair':
                dc,dd=np.asarray(f['d_c'],float),np.asarray(f['d_d'],float)
                bc,bd=np.asarray(f['bit_plus_c']),np.asarray(f['bit_plus_d'])
                Gc,Gd=1/(1+avg(norm(vc))),1/(1+avg(norm(vd)));H=f['H']
                ac=.1*(dc/(norm(dc)[:,None]+.01)*H*(1-2*bc[:,None]))*Gc
                ad=.1*(dd/(norm(dd)[:,None]+.01)*H*(1-2*bd[:,None]))*Gd
                wc,wd=vc+ac,vd+ad;source=(dc,bc,H,Gc,dd,bd,H,Gd)
            else:ac,ad=wc-vc,wd-vd
            p,z=evaluate_pair(vc,ac,wc,vd,ad,wd,source);COUNTS['fixture_pair_calls']+=1
            yc,yd=synthetic_D(wc),synthetic_D(wd);S,Tn=fixture_check(tag,p,z,yc,yd)
            check(tag+'/stored_S',S,stored['S']);check(tag+'/stored_Tnorm',Tn,stored['Tnorm'])
            for fam,expected in stored['bounds'].items():check(tag+'/stored_'+fam,p[fam],expected)
            if tag in ['F01','F02','F03','F04','F07','F09']:check(tag+'/zero_target',S,0.)
            if tag in ['F03','F04','F07']:check(tag+'/zero_profile',p['P_PROFILE'],0.)
            if tag=='F05':
                r=f['r'];check(tag+'/equal_input_norms',norm(wc),norm(wd))
                check(tag+'/axis',avg(norm(yc)),r/(1+math.log1p(r)))
                check(tag+'/diagonal',avg(norm(yd)),r/(1+math.log1p(r/math.sqrt(3))))
                exact(tag+'/unequal_output_norms',avg(norm(yd))>avg(norm(yc)),True)
                COUNTS['fixture_D_scalar_reference_expressions']+=2
            if tag=='F08':check(tag+'/zero_Q',p['Q_VECTOR'],0.);exact(tag+'/positive_T',p['T_TRIANGLE']>0,True)
            if tag=='F09':
                exact(tag+'/positive_individual_difference',Tn>0,True)
                yc=yc.copy();yc[0,0]+=7
                p2,z2=evaluate_pair(vc,ac,wc,vd,ad,wd);COUNTS['fixture_pair_calls']+=1
                exact(tag+'/outcome_canary_pair',p,p2)
                for key in z:check(tag+'/outcome_canary_'+key,z[key],z2[key])
        COUNTS['fixture_groups']+=1
        records.append({'id':tag,'name':f['name'],'review_checks':len(LOG)-before,'status':'PASS' if not ISSUES else 'CHECK_ISSUES'})
    return records

def typed_csv(path):
    def cast(s):
        if s=='':return None
        if s=='True':return True
        if s=='False':return False
        if s.lstrip('-').isdigit():return int(s)
        try:return float(s)
        except ValueError:return s
    with Path(path).open(encoding='utf-8',newline='') as f:return [{k:cast(v) for k,v in r.items()} for r in csv.DictReader(f)]

def compare_rows(name,got,want,variance=False):
    exact(name+'/rows',len(got),len(want))
    exact(name+'/columns',set(got[0]),set(want[0]))
    if len(got)!=len(want):return
    for k in got[0]:
        if k not in want[0]:continue
        a=[x[k] for x in got];b=[x[k] for x in want]
        if isinstance(b[0],str) or b[0] is None:
            exact(name+'/'+k,a,b);continue
        if ('factor' in k or 'utilization' in k or k.endswith('_over_Q')) and not k.endswith('_valid'):
            # Algebraic ratio consistency is checked against the submitted primitives below.
            # Cross-environment raw discrepancy remains visible, but do not give large ratios a speed-unit tolerance.
            arr=np.asarray(a,float)-np.asarray(b,float)
            LOG[name+'/'+k]={'status':'DEFERRED_TO_RATIO_PRODUCT','max_abs_difference':float(np.max(np.abs(arr)))}
        else:check(name+'/'+k,a,b,tol=1e-14 if variance and ('variance' in k or 'margin' in k) else 1e-12)

def bound_ratios(rows,where,disp=False):
    for fam in FAMILIES:
        kinds=('SD','variance') if disp else ('pair',)
        for kind in kinds:
            bound=fam if not disp else fam+'_'+kind+'_upper'
            target='observed_S' if not disp else 'post_'+kind
            factor=fam+'_factor_over_outcome' if not disp else fam+'_'+kind+'_factor'
            util=fam+'_utilization' if not disp else fam+'_'+kind+'_utilization'
            fv=fam+'_factor_valid' if not disp else factor+'_valid'
            uv=util+'_valid';floor=1e-24 if kind=='variance' else 1e-12
            B=np.array([r[bound] for r in rows]);S=np.array([r[target] for r in rows])
            FF=np.array([r[fv] for r in rows]);UU=np.array([r[uv] for r in rows])
            exact(where+'/'+fv,FF.tolist(),(S>=floor).tolist());exact(where+'/'+uv,UU.tolist(),(B>=floor).tolist())
            check(where+'/'+factor+'_product',np.array([r[factor] for r in rows if r[fv]])*S[FF],B[FF],tol=1e-14 if kind=='variance' else 1e-12)
            check(where+'/'+util+'_product',np.array([r[util] for r in rows if r[uv]])*B[UU],S[UU],tol=1e-14 if kind=='variance' else 1e-12)
    if not disp:
        for fam in ['K_COMPONENT','P_PROFILE','BEST_PRE']:
            check(where+'/'+fam+'_over_Q_product',np.array([r[fam+'_over_Q'] for r in rows])*np.array([r['Q_VECTOR'] for r in rows]),[r[fam] for r in rows])

def archive_audit(args,root):
    with zipfile.ZipFile(args.archive) as z:
        names=z.namelist();exact('archive/CRC',z.testzip(),None)
        exact('archive/unique',len(names),len(set(names)));exact('archive/case_unique',len(names),len({n.casefold() for n in names}))
        for n in names:
            p=PurePosixPath(n); assert not p.is_absolute() and '..' not in p.parts and '\\' not in n
            assert not stat.S_ISLNK(z.getinfo(n).external_attr>>16)
        man=json.loads(z.read('MANIFEST.json'));exact('archive/coverage',set(names),set(man['files'])|{'MANIFEST.json'})
        for n,e in man['files'].items():
            raw=z.read(n);exact('archive/hash/'+n,ident(raw),e);exact('archive/extracted/'+n,raw,(root/n).read_bytes())
        seal=readj(args.seal);exact('archive/seal',ident(Path(args.archive).read_bytes()),seal['archive'])
        exact('archive/manifest_identity',ident(z.read('MANIFEST.json')),seal['manifest'])
        for name in ['SIM04_REPORT.md','SIM04_EXECUTION_RECEIPT.md']:
            outside=Path(args.archive).parent/name
            if outside.exists():exact('archive/separate/'+name,outside.read_bytes(),z.read(name))
    inp=readj(root/'received/SIM04_INPUT_IDENTITIES_AND_SCHEMAS.json')
    exact('input/map_unchanged',inp,readj(root/'evidence/INPUT_MAP.json'))
    with zipfile.ZipFile(args.upstream_candidate) as old:
        for rel,e in inp['files'].items():
            raw=(root/'inputs'/rel).read_bytes();exact('input/hash/'+rel,ident(raw),{k:e[k] for k in ['bytes','sha256']})
            exact('input/git_blob/'+rel,oid(raw),e['git_blob_sha1'])
            exact('input/earlier_approved_bytes/'+rel,raw,old.read(e['repository_path']))
    with zipfile.ZipFile(args.handoff) as hand:
        hn=hand.namelist();exact('handoff/CRC',hand.testzip(),None)
        for n in hn:
            if not n.endswith('/'):exact('handoff/'+n,hand.read(n),(root/'received'/n).read_bytes())
    baseline=readj(root/'evidence/BASELINE_BEFORE.json')
    exact('preservation/submitted_after',baseline,readj(root/'evidence/PRESERVATION_AFTER.json')['baseline_after'])
    exact('preservation/seal_after',baseline,seal['baseline_after'])
    gate=readj(root/'evidence/IMPLEMENTATION_GATE.json')
    for rel,e in gate['frozen_files'].items():exact('frozen/'+rel,ident((root/rel).read_bytes()),e)
    bs=readj(root/'analysis/PRE_OUTPUT_BOUNDS_SEAL.json')
    exact('source_bound_seal/hash',ident((root/'analysis/PRE_OUTPUT_BOUNDS.npz').read_bytes()),bs['identity'])
    access=readj(root/'evidence/DATA_ACCESS_LOG.json')['access']
    exact('source_bound_seal/chronology',access[-1]['utc']>bs['utc'],True)
    tree=ast.parse((root/'analyst/bounds.py').read_text());names={n.id for n in ast.walk(tree) if isinstance(n,ast.Name)}
    attrs={n.attr for n in ast.walk(tree) if isinstance(n,ast.Attribute)}
    forbidden={'open','load','saved_successor_velocity','retention','post_norm','random','eval','exec','__import__'}
    exact('analytic_source/no_forbidden_names',sorted(forbidden&(names|attrs)),[])
    return {'archive':ident(Path(args.archive).read_bytes()),'members':len(man['files'])+1,
            'manifest_payloads':len(man['files']),'selected_upstream_files':len(inp['files']),
            'upstream_comparison':'byte equality with previously approved SIM03 candidate ZIP; no fresh remote assertion',
            'preservation_boundary':'supplied records, not live Windows filesystem access'}

def primary(root,out):
    source=np.load(root/'inputs/analysis/center_decomposition.npz',allow_pickle=False)
    metadata={k:source[k] for k in ['dataset_id','update_index','center','record_id','update_row','phase','block','source_frame','source_time','complete']}
    lookup={(int(ds),int(n),int(i)):r for r,(ds,n,i) in enumerate(zip(metadata['dataset_id'],metadata['update_index'],metadata['center']))}
    exact('source/unique_keys',len(lookup),len(metadata['center']))
    indices=[];mapping=[]
    for c in range(5):
        for j in range(200):
            n=200*c+j;ds=0 if c==0 else 2
            for i in range(8):
                rr=lookup[(ds,n,i)];indices.append(rr)
                mapping.append(dict(selected_row=len(indices)-1,source_row=rr,record_id=int(metadata['record_id'][rr]),
                                    update_row=int(metadata['update_row'][rr]),dataset_id=ds,update_index=n,cycle=c,phase=j,center=i,
                                    source_frame=int(metadata['source_frame'][rr])))
    ix=np.array(indices).reshape(5,200,8)
    exact('source/selection_completeness',set(indices),set(np.where(np.isin(metadata['dataset_id'],[0,2]))[0]))
    exact('source/selection_count',len(set(indices)),8000)
    COUNTS['selected_updates']=1000;COUNTS['selected_center_records']=8000
    v,a,w,d,H,G,bits=[source[k][ix] for k in ['incoming_velocity','impulse','w','d','H','G','bit_plus']]
    inc=np.array([[avg(norm(v[c,j])) for j in range(200)] for c in range(5)])
    pre=np.array([[avg(norm(w[c,j])) for j in range(200)] for c in range(5)])
    gg=geom(d.reshape(-1,3),bits.reshape(-1)).reshape(5,200,8,3)
    native('input_w_minus_v_plus_a',w-v-a) # independently grouped comparison
    native('input_impulse_factorization',a-(.1*H*G)[...,None]*gg)
    native('input_G_from_incoming',G-1/(1+inc[...,None]))
    native('input_H_common_centers',H-H[...,:1]);native('input_H_common_cycles',H-H[:1,:,:])
    native('input_G_common_centers',G-G[...,:1]);native('input_geometry_norm_minus_one',norm(gg)-1,ineq=True)
    exact('source/bits_binary',bool(np.isin(bits,[0,1]).all()),True)
    check('source/phase',metadata['phase'][ix],np.broadcast_to(np.arange(200)[None,:,None],(5,200,8)))
    check('source/schedule',metadata['source_frame'][ix],np.broadcast_to(np.arange(200)[None,:,None],(5,200,8)))
    check('source/source_time',metadata['source_time'][ix],np.broadcast_to(.1*np.arange(200)[None,:,None],(5,200,8)))
    exact('source/complete',bool(metadata['complete'][ix].all()),True)
    prows=[];cc={}
    for pi,(c,dd) in enumerate(PAIRS):
        for j in range(200):
            p,z=evaluate_pair(v[c,j],a[c,j],w[c,j],v[dd,j],a[dd,j],w[dd,j],
                (d[c,j],bits[c,j],float(H[c,j,0]),float(G[c,j,0]),d[dd,j],bits[dd,j],float(H[dd,j,0]),float(G[dd,j,0])))
            prows.append(dict(pair_id=pi,cycle_c=c,cycle_d=dd,phase=j,update_c=200*c+j,update_d=200*dd+j,**p))
            for key,val in z.items():cc.setdefault(key,[]).append(val)
            COUNTS['primary_pair_phase']+=1;COUNTS['labeled_center_pairs']+=8
    cc={k:np.concatenate(vv,axis=0) for k,vv in cc.items()}
    pa={k:np.array([p[k] for p in prows]) for k in prows[0]}
    packed={'pair__'+k:x for k,x in pa.items()}|{'center__'+k:x for k,x in cc.items()}
    packed['center__pair_phase_row']=np.repeat(np.arange(2000,dtype=np.int32),8)
    packed['center__center']=np.tile(np.arange(8,dtype=np.int8),2000)
    writej(out/'REVIEW_BOUND_FINGERPRINTS.json',{'utc':now(),'stage':'review analytic fields complete before numerical outcome join',
        'note':'report was read beforehand; this is function/dataflow separation, not reviewer blinding',
        'fields':{k:{'shape':list(x.shape),'sha256':hashlib.sha256(x.tobytes()).hexdigest()} for k,x in packed.items()}})
    with np.load(root/'analysis/PRE_OUTPUT_BOUNDS.npz',allow_pickle=False) as original:
        exact('pre_output/fields',set(original.files),set(packed))
        for k,x in packed.items():check('pre_output/'+k,x,original[k])
    for lo,hi in [('Q_VECTOR','T_TRIANGLE'),('T_TRIANGLE','GAMMA_SOURCE'),('GAMMA_SOURCE','OMEGA_COARSE'),
                  ('BEST_PRE','K_COMPONENT'),('BEST_PRE','P_PROFILE'),('K_COMPONENT','Q_VECTOR'),('P_PROFILE','Q_VECTOR')]:
        native('pair_'+lo+'_minus_'+hi,pa[lo]-pa[hi],ineq=True)
    native('difference_alignment_identity',cc['alignment_residual'])
    for lo,hi in [('K_center','Q_center'),('P_center','Q_center'),('Q_center','T_center')]:native('center_'+lo+'_minus_'+hi,cc[lo]-cc[hi],ineq=True)
    for key in ['kappa','lambda']:
        native(key+'_minus_one',cc[key]-1,ineq=True);native('negative_'+key,-cc[key],ineq=True)
    # Only now join saved outcomes. No D evaluation on any actual record.
    y=source['saved_successor_velocity'][ix];source.close()
    yn=norm(y);post=np.array([[avg(yn[c,j]) for j in range(200)] for c in range(5)])
    outcomes={}
    for p in prows:
        c,dd,j=p['cycle_c'],p['cycle_d'],p['phase']
        dy=y[c,j]-y[dd,j];dp=prof(y[c,j])-prof(y[dd,j]);signed=yn[c,j]-yn[dd,j]
        zs,zp=norm(dy),norm(dp);ts=np.abs(signed)
        S=abs(post[c,j]-post[dd,j]);Zs,Zp,Tn=avg(zs),avg(zp),avg(ts);Z=Zs if p['best_is_K'] else Zp
        p.update(observed_S=float(S),signed_collective_difference=float(post[c,j]-post[dd,j]),Zsigned=Zs,Zprofile=Zp,Tnorm=Tn,Zstar=Z,
          gap_Q_to_BEST=p['Q_VECTOR']-p['BEST_PRE'],gap_BEST_to_Zstar=p['BEST_PRE']-Z,gap_Zstar_to_Tnorm=Z-Tn,
          gap_Tnorm_to_S=Tn-S,gap_Q_to_S=p['Q_VECTOR']-S)
        p['gap_telescope_residual']=p['gap_Q_to_S']-sum(p[k] for k in ['gap_Q_to_BEST','gap_BEST_to_Zstar','gap_Zstar_to_Tnorm','gap_Tnorm_to_S'])
        for f in FAMILIES:
            p[f+'_gap']=p[f]-S;p[f+'_utilization_valid']=bool(p[f]>=1e-12);p[f+'_factor_valid']=bool(S>=1e-12)
            p[f+'_utilization']=float(S/p[f]) if p[f+'_utilization_valid'] else None
            p[f+'_factor_over_outcome']=float(p[f]/S) if p[f+'_factor_valid'] else None
        for f in ['K_COMPONENT','P_PROFILE','BEST_PRE']:
            p[f+'_improvement']=p['Q_VECTOR']-p[f];p[f+'_over_Q_valid']=bool(p['Q_VECTOR']>=1e-12)
            p[f+'_over_Q']=p[f]/p['Q_VECTOR'] if p[f+'_over_Q_valid'] else None
        for key,x in dict(post_delta_velocity=dy,post_profile_delta=dp,post_signed_distance=zs,post_profile_distance=zp,
                          signed_speed_difference=signed,individual_abs_speed_difference=ts).items():outcomes.setdefault(key,[]).append(x)
        COUNTS['outcome_pair_phase']+=1
    outcomes={k:np.concatenate(vals) for k,vals in outcomes.items()}
    get=lambda k:np.array([p[k] for p in prows])
    for fam in FAMILIES:native('outcome_S_minus_'+fam,get('observed_S')-get(fam),ineq=True)
    for lo,hi in [('Tnorm','Zsigned'),('Zsigned','K_COMPONENT'),('Tnorm','Zprofile'),('Zprofile','P_PROFILE'),('observed_S','Tnorm')]:native('diagnostic_'+lo+'_minus_'+hi,get(lo)-get(hi),ineq=True)
    native('gap_telescope',get('gap_telescope_residual'))
    for k in ['gap_Q_to_BEST','gap_BEST_to_Zstar','gap_Zstar_to_Tnorm','gap_Tnorm_to_S']:native('negative_'+k,-get(k),ineq=True)
    native('center_post_signed_minus_K',outcomes['post_signed_distance']-cc['K_center'],ineq=True)
    native('center_post_profile_minus_P',outcomes['post_profile_distance']-cc['P_center'],ineq=True)
    for k in ['post_signed_distance','post_profile_distance']:native('center_abs_speed_minus_'+k,outcomes['individual_abs_speed_difference']-outcomes[k],ineq=True)
    packed.update({'outcome__'+k:x for k,x in outcomes.items()})
    with np.load(root/'analysis/center_pair_bounds.npz',allow_pickle=False) as original:
        exact('center_output/fields',set(original.files),set(packed))
        for k,x in packed.items():check('center_output/'+k,x,original[k])
    reference=typed_csv(root/'inputs/analysis/repeated_phase_curves.csv');rmap={(r['cycle'],r['phase']):r for r in reference}
    srows=[]
    for c in range(5):
        for j in range(200):srows.append(dict(cycle=c,phase=j,update_index=200*c+j,incoming=float(inc[c,j]),pre_damping=float(pre[c,j]),post=float(post[c,j])))
    for key,field in [('incoming','incoming_mean_speed'),('pre_damping','pre_damping_mean_speed'),('post','post_mean_speed')]:
        native('reference_speed_'+key,[r[key]-rmap[r['cycle'],r['phase']][field] for r in srows])
    spread={(r['view'],r['phase']):r for r in typed_csv(root/'inputs/analysis/phase_spread.csv')}
    disp=[];vres={k:[] for k in ['incoming','pre_damping','post']};refres={k:[] for k in vres}
    pm={(r['cycle_c'],r['cycle_d'],r['phase']):r for r in prows}
    cls=lambda x: 'PASS' if x>1e-14 else ('NOT_ESTABLISHED' if x< -1e-14 else 'UNRESOLVED')
    for view,cycles in [('all_five',list(range(5))),('new_four',list(range(1,5)))]:
        m=len(cycles);pairs=[(c,d) for c,d in PAIRS if c in cycles and d in cycles]
        for j in range(200):
            r=dict(view=view,phase=j,cycles=m,pairs=len(pairs))
            for key,arr in [('incoming',inc),('pre_damping',pre),('post',post)]:
                vv=var(arr[cycles,j]);pv=math.fsum((float(arr[c,j])-float(arr[d,j]))**2 for c,d in pairs)/(m*m)
                r[key+'_variance']=vv;r[key+'_SD']=math.sqrt(vv);r[key+'_pair_variance']=pv;vres[key].append(pv-vv)
                refcol={'incoming':'incoming_mean_speed_population_std','pre_damping':'pre_damping_mean_speed_population_std','post':'post_mean_speed_population_std'}[key]
                refres[key].append(vv-spread[view,j][refcol]**2)
            for fam in FAMILIES:
                W=math.fsum(pm[c,d,j][fam]**2 for c,d in pairs)/(m*m);E=math.sqrt(W)
                r[fam+'_variance_upper']=W;r[fam+'_SD_upper']=E
                r[fam+'_variance_gap']=W-r['post_variance'];r[fam+'_SD_gap']=E-r['post_SD']
                for unit,bound,obs,floor in [('variance',W,r['post_variance'],1e-24),('SD',E,r['post_SD'],1e-12)]:
                    r[fam+'_'+unit+'_utilization_valid']=bound>=floor;r[fam+'_'+unit+'_factor_valid']=obs>=floor
                    r[fam+'_'+unit+'_utilization']=obs/bound if bound>=floor else None
                    r[fam+'_'+unit+'_factor']=bound/obs if obs>=floor else None
            for ref in ['incoming','pre_damping']:
                margin=r[ref+'_variance']-r['BEST_PRE_variance_upper'];actual=r[ref+'_variance']-r['post_variance']
                r[ref+'_condition_margin']=margin;r[ref+'_condition_class']=cls(margin)
                r[ref+'_actual_margin']=actual;r[ref+'_actual_class']=cls(actual)
            disp.append(r);COUNTS['view_phase']+=1
    for k in vres:
        native('pair_population_identity_'+k,vres[k],tol=1e-14);native('reference_variance_'+k,refres[k],tol=1e-14)
    for fam in FAMILIES:native('post_variance_minus_'+fam,[r['post_variance']-r[fam+'_variance_upper'] for r in disp],tol=1e-14,ineq=True)
    nqa=readj(root/'evidence/NUMERICAL_QA.json')['checks']
    with np.load(root/'analysis/NUMERICAL_RESIDUALS.npz',allow_pickle=False) as nr:
        exact('residuals/coverage',set(nr.files),set(RES));exact('residuals/count',len(nr.files),59)
        for k,x in RES.items():
            tol=nqa[k]['tolerance'];check('residuals/independent_'+k,x,nr[k],tol=tol)
            xx=nr[k];check('residual_receipt/'+k+'_max',float(xx.max()),nqa[k]['max_signed'],tol=0)
            check('residual_receipt/'+k+'_min',float(xx.min()),nqa[k]['min_signed'],tol=0)
            check('residual_receipt/'+k+'_max_abs',float(np.max(np.abs(xx))),nqa[k]['max_abs'],tol=0)
    compare_rows('csv/selected_record_map',typed_csv(root/'analysis/selected_record_map.csv'),mapping)
    compare_rows('csv/cycle_phase_speeds',typed_csv(root/'analysis/cycle_phase_speeds.csv'),srows)
    reported=typed_csv(root/'analysis/pair_phase_bounds.csv');rd=typed_csv(root/'analysis/phase_dispersion_bounds.csv')
    compare_rows('csv/pair_phase_bounds',reported,prows);compare_rows('csv/phase_dispersion_bounds',rd,disp,variance=True)
    bound_ratios(reported,'csv/pair_ratios');bound_ratios(rd,'csv/variance_ratios',disp=True)
    return prows,disp,cc,outcomes,reported,rd

def smallloc(r):return {k:r[k] for k in ['pair_id','cycle_c','cycle_d','view','phase'] if k in r}
def stats(values,locs):
    keep=[(float(x),l) for x,l in zip(values,locs) if x is not None and math.isfinite(float(x))]
    arr=np.array([x for x,l in keep]);result=dict(count=len(keep),masked=len(values)-len(keep),exact_zero=int(np.sum(arr==0)))
    if not keep:return result|{k:None for k in ['min','p05','median','p95','max','mean','min_locator','p05_locator','median_locator','p95_locator','max_locator']}
    order=np.argsort(arr,kind='stable')
    for key,q in [('min',0.),('p05',.05),('median',.5),('p95',.95),('max',1.)]:
        pos=(len(arr)-1)*q;lo,hi=math.floor(pos),math.ceil(pos)
        result[key]=float(np.quantile(arr,q,method='linear'))
        result[key+'_locator']=dict(lower=keep[int(order[lo])][1],upper=keep[int(order[hi])][1],upper_weight=pos-lo)
    result['mean']=avg(arr);return result

def summary_audit(root,pairs,disp,center):
    # After independent primitive checks, summary/ratio verification uses validated stored tables.
    # This avoids confusing conditioning of a large quotient with native-unit bound accuracy.
    groups={'all_pairs':pairs,'new_four_pairs':[r for r in pairs if r['cycle_d']>0]}
    groups.update({f'pair_{c}_{d}':[r for r in pairs if (r['cycle_c'],r['cycle_d'])==(c,d)] for c,d in PAIRS})
    groups.update({view:[r for r in disp if r['view']==view] for view in ['all_five','new_four']})
    result=readj(root/'analysis/RESULTS.json');summary_count=0
    for row in typed_csv(root/'analysis/bound_summary.csv'):
        scope,fam,metric=row['scope'],row['family'],row['metric'];rs=groups[scope]
        if scope in ['all_five','new_four']:
            unit,met=metric.split('_',1)
            col={'bound':fam+'_'+unit+'_upper','outcome':'post_'+unit,'gap':fam+'_'+unit+'_gap',
                 'utilization':fam+'_'+unit+'_utilization','factor':fam+'_'+unit+'_factor'}[met]
        else:col={'bound':fam,'outcome':'observed_S','gap':fam+'_gap','utilization':fam+'_utilization','factor':fam+'_factor_over_outcome'}[metric]
        st=stats([r[col] for r in rs],[smallloc(r) for r in rs]);key=f'{scope}/{fam}/{metric}'
        for k,expected in st.items():
            got=row[k]
            if k.endswith('_locator'):got=json.loads(got) if isinstance(got,str) else got
            if isinstance(expected,(dict,list)) or expected is None:exact('summary/csv/'+key+'/'+k,got,expected)
            else:check('summary/csv/'+key+'/'+k,got,expected)
            eg=result['summary'][scope][fam][metric][k]
            if isinstance(expected,dict) or expected is None:exact('summary/json/'+key+'/'+k,eg,expected)
            else:check('summary/json/'+key+'/'+k,eg,expected)
        summary_count+=1
    slack_rows=typed_csv(root/'analysis/proof_slack_summary.csv')
    for row in slack_rows:
        scope,metric=row['scope'],row['metric']
        if scope=='all_center_pairs':
            arr=center[metric];locs=[dict(**smallloc(pairs[i//8]),center=i%8) for i in range(16000)]
            expected_json=result['proof_slack']['center_'+metric]
        else:
            rs=groups[scope];arr=[r[metric] for r in rs];locs=[smallloc(r) for r in rs]
            expected_json=result['proof_slack'][scope][metric]
        st=stats(arr,locs)
        for k,val in st.items():
            got=row[k]
            if k.endswith('_locator'):got=json.loads(got) if isinstance(got,str) else got
            name='slack_summary/'+scope+'/'+metric+'/'+k
            if isinstance(val,dict) or val is None:exact(name,got,val);exact(name+'/json',expected_json[k],val)
            else:check(name,got,val);check(name+'/json',expected_json[k],val)
    curve=typed_csv(root/'analysis/phase_bound_means.csv')
    for row in curve:
        rs=[r for r in pairs if r['phase']==row['phase']]
        for key,val in row.items():
            if key.endswith('_mean'):check('phase_mean/'+str(row['phase'])+'/'+key,val,avg([r[key[:-5]] for r in rs]))
    # Counts, categories, complete-pair variance aggregates and margin summaries.
    aggregates={};conditions={}
    for scope,rs in groups.items():
        for fam in FAMILIES:
            units=['variance','SD'] if scope in ['all_five','new_four'] else ['pair']
            for unit in units:
                factor=fam+'_factor_over_outcome' if unit=='pair' else fam+'_'+unit+'_factor'
                fs=[r[factor] for r in rs if r[factor] is not None]
                reported=result['factor_categories'][scope][fam]
                if unit!='pair':reported=reported[unit]
                for n in [2,5,10]:exact(f'categories/{scope}/{fam}/{unit}/{n}',reported['within_factor_'+str(n)],sum(x<=n for x in fs))
                exact(f'categories/{scope}/{fam}/{unit}/resolved',reported['resolved'],len(fs))
    for view in ['all_five','new_four']:
        rs=groups[view];actual={k:math.sqrt(avg([r[k+'_variance'] for r in rs])) for k in ['incoming','pre_damping','post']}
        aggregates[view]={'RMS_phase_SD':actual,'bounds':{}};conditions[view]={}
        for k,val in actual.items():check('aggregate/'+view+'/'+k,val,result['aggregate'][view]['RMS_phase_SD'][k])
        for fam in FAMILIES:
            W=avg([r[fam+'_variance_upper'] for r in rs]);E=math.sqrt(W)
            aa=dict(mean_variance_upper=W,RMS_phase_SD_upper=E,SD_factor_over_observed=E/actual['post'],SD_utilization=actual['post']/E)
            aggregates[view]['bounds'][fam]=aa
            for k,val in aa.items():check('aggregate/'+view+'/'+fam+'/'+k,val,result['aggregate'][view]['bounds'][fam][k])
        for ref in ['incoming','pre_damping']:
            obj={typ:{label:sum(r[ref+'_'+('condition' if typ=='sufficient' else 'actual')+'_class']==label for r in rs)
                 for label in ['PASS','NOT_ESTABLISHED','UNRESOLVED']} for typ in ['sufficient','actual']}
            obj['closest_sufficient_margin']=max(r[ref+'_condition_margin'] for r in rs)
            conditions[view][ref]=obj
            for typ in ['sufficient','actual']:exact('conditions/'+view+'/'+ref+'/'+typ,obj[typ],result['conditions'][view][ref][typ])
            for typ in ['condition','actual']:
                st=stats([r[ref+'_'+typ+'_margin'] for r in rs],[smallloc(r) for r in rs])
                for k,val in st.items():
                    e=result['conditions'][view][ref][typ+'_margin'][k]
                    if isinstance(val,dict):exact('conditions_stats/'+view+'/'+ref+'/'+typ+'/'+k,e,val)
                    else:check('conditions_stats/'+view+'/'+ref+'/'+typ+'/'+k,e,val)
    align={k:int(np.count_nonzero(op(center['difference_alignment'],0))) for k,op in [('negative',np.less),('zero',np.equal),('positive',np.greater)]}
    align['cosine_unresolved']=int(np.count_nonzero(~center['difference_cosine_valid']))
    exact('summary/alignment_counts',align,result['alignment_counts'])
    zc=int(center['contains_zero'].sum());exact('summary/zero_intervals',{'count':zc,'total':48000},result['signed_interval_contains_zero'])
    winners={'K_including_ties':sum(r['best_is_K'] for r in pairs),'P_strict':sum(not r['best_is_K'] for r in pairs),
             'exact_ties':sum(r['K_COMPONENT']==r['P_PROFILE'] for r in pairs)}
    exact('summary/refinement_winners',winners,result['refinement_winners'])
    for metric,stored in result['fixed_extreme_locators'].items():
        top=sorted(pairs,key=lambda r:r[metric],reverse=True)[:5]
        for rank,(r,ss) in enumerate(zip(top,stored)):
            for k in ['pair_id','cycle_c','cycle_d','phase']:exact(f'extreme/{metric}/{rank}/{k}',r[k],ss[k])
            check(f'extreme/{metric}/{rank}/value',r[metric],ss['value'])
    slacks={k:avg([r[k] for r in pairs]) for k in ['T_minus_Q','gap_Q_to_BEST','gap_BEST_to_Zstar','gap_Zstar_to_Tnorm','gap_Tnorm_to_S','gap_Q_to_S']}
    return dict(aggregate=aggregates,conditions=conditions,alignment_counts=align,interval_zero_count=zc,
                refinement_winners=winners,mean_slacks=slacks,summary_rows=summary_count,slack_summary_rows=len(slack_rows))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--submission',required=True,type=Path);ap.add_argument('--archive',required=True,type=Path)
    ap.add_argument('--seal',required=True,type=Path);ap.add_argument('--upstream-candidate',required=True,type=Path);ap.add_argument('--handoff',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path);args=ap.parse_args();root=args.submission.resolve();out=args.output.resolve()
    if out==root or root in out.parents:raise ValueError('Reviewer output must be separate from the submission.')
    out.mkdir(exist_ok=True,parents=True)
    if (out/'INDEPENDENT_REVIEW_RESULTS.json').exists() or (out/'REVIEW_STARTED.json').exists():raise FileExistsError('No overwrite or hidden retry of review output.')
    started=time.monotonic();writej(out/'REVIEW_STARTED.json',{'utc':now(),'status':'RUNNING','script':ident(Path(__file__).read_bytes())})
    try:
        arc=archive_audit(args,root);writej(out/'ARCHIVE_REVIEW.json',arc)
        if ISSUES: raise AssertionError('Archive/input gate issues: '+repr(ISSUES))
        fixed=fixtures(root)
        if ISSUES: raise AssertionError('Fixture gate issues: '+repr(ISSUES))
        prows,disp,cc,oo,reported,rd=primary(root,out)
        summary=summary_audit(root,reported,rd,cc)
        # One primary selected-population pass. This final check reuses computed arrays.
        check('additional_theorem/observed_center_P<=K',cc['P_center'],cc['K_center'],inequality=True)
        result=dict(status='PASS' if not ISSUES else 'REVIEW_ISSUES',utc=now(),environment={'python':sys.version,'numpy':np.__version__,'platform':platform.platform()},
            execution_counts=COUNTS,zero_activity=dict(engine_calls=0,new_rollout_updates=0,raw_state_reconstructions=0,centroid_evaluations=0,RNG_samples=0,RNG_restorations=0,
                submitted_scientific_script_invocations=0,D_on_actual_records=0,Git_writes=0),
            archive=arc,fixture_review=fixed,findings=summary,comparison_checks=LOG,issues=ISSUES,elapsed_seconds=time.monotonic()-started,
            methods={'native_tolerance':1e-12,'variance_tolerance':1e-14,'relative_tolerance':0.,
                'ratio_comparisons':'ratio products checked in native units; large raw dimensionless differences recorded, not misclassified using a speed-unit threshold',
                'summary_check':'full quantiles, interpolation locators, categories and aggregates recomputed from independently validated stored primitive tables',
                'existing_review_scripts':'read, never imported or executed'})
        writej(out/'INDEPENDENT_REVIEW_RESULTS.json',result)
        print(json.dumps({'status':result['status'],'counts':COUNTS,'checks':len(LOG),'issues':ISSUES[:30],'seconds':result['elapsed_seconds']},indent=2))
    except Exception as exc:
        writej(out/'REVIEW_EXCEPTION.json',dict(utc=now(),error=repr(exc),execution_counts=COUNTS,issues=ISSUES,elapsed_seconds=time.monotonic()-started))
        raise
if __name__=='__main__':main()
