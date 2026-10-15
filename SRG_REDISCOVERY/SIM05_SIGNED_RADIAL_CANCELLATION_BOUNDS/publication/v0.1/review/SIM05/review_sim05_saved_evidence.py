"""Independent SIM05 review. Does not import submitted code or evaluate D/F on real records.

Usage: python -B review_sim05_saved_evidence.py --submission /path/to/extracted_SIM05 \
  --seal /path/to/SIM05_TRANSPORT_SEAL.json --output /path/to/new_review_output
The numerical pass is one-shot. Synthetic reference damping is counted separately.
The original data are never modified. Prior scientific scripts are inspected, not executed.
"""
from __future__ import annotations
import argparse, ast, csv, hashlib, json, math, platform, sys, time, traceback
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

PAIRS = [(1,0),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)]
FAMILIES = ['P_PROFILE','RADIAL_1_UNSIGNED','RADIAL_1_SIGNED','RADIAL_4_UNSIGNED','RADIAL_4_SIGNED']
RAW = [f'J{j}_raw_{k}_upper' for j in (1,4) for k in ('unsigned','signed')]
ALL = FAMILIES + RAW
TOL, VTOL = 1e-12, 1e-14
CHECKS, COMPARES = [], {}
COUNTS = {'fixture_groups':0,'fixture_vector_cases':0,'fixture_pair_evaluations':0,
          'synthetic_reference_D_array_calls':0,'synthetic_reference_D_components':0,
          'primary_pair_phase_evaluations':0,'primary_center_pairs':0,
          'primary_component_pairs':0,'primary_derivative_node_slots':0,
          'outcome_pair_phase_joins':0,'view_phase_summaries':0,
          'engine_calls':0,'new_trajectories':0,'source_state_reconstructions':0,
          'RNG_operations':0,'D_or_F_calls_on_saved_records':0}

def now(): return datetime.now(timezone.utc).isoformat()
def jload(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def dump(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False, ensure_ascii=False)+'\n',encoding='utf-8')
def identity(path):
    b=Path(path).read_bytes(); return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def require(ok, name):
    if not bool(ok): raise AssertionError(name)
def mean(x):
    a=np.asarray(x); return math.fsum(a.ravel())/a.size

def row_sum(x):
    a=np.asarray(x,dtype=float)
    return np.asarray([math.fsum(row) for row in a.reshape(-1,a.shape[-1])]).reshape(a.shape[:-1])
def block_mean(x): return row_sum(np.asarray(x).reshape(-1,8))/8

def check(name, residual, tol=TOL, inequality=False):
    a=np.asarray(residual,dtype=float)
    require(a.size and np.isfinite(a).all(),name+' finite')
    maximum=float(a.max()); maximum_abs=float(np.max(np.abs(a)))
    rec={'name':name,'shape':list(a.shape),'kind':'inequality' if inequality else 'equality',
         'tolerance':tol,'min_signed':float(a.min()),'max_signed':maximum,'max_abs':maximum_abs,
         'max_abs_index':[int(i) for i in np.unravel_index(int(np.argmax(np.abs(a))),a.shape)] if a.shape else []}
    CHECKS.append(rec)
    require((maximum if inequality else maximum_abs)<=tol,name)

def compare(name, actual, reference, tol=TOL):
    a=np.asarray(actual); b=np.asarray(reference)
    require(a.shape==b.shape,name+' shape')
    if a.dtype.kind in 'buiUS' or b.dtype.kind in 'buiUS':
        require(np.array_equal(a,b),name+' exact values')
        COMPARES[name]={'shape':list(a.shape),'exact':True}; return
    require(np.array_equal(np.isnan(a),np.isnan(b)),name+' NaN mask')
    good=np.isfinite(a)&np.isfinite(b)
    require(np.array_equal(np.isfinite(a),np.isfinite(b)),name+' finiteness mask')
    diff=float(np.max(np.abs(a[good]-b[good]))) if good.any() else 0.
    COMPARES[name]={'shape':list(a.shape),'max_abs_discrepancy':diff,'tolerance':tol}
    require(diff<=tol,name+' numerical discrepancy '+str(diff))

def angle_free_enclosure(p,q,P):
    """Batched pure formula; rows group consecutive labeled centers in groups of eight.
    Only profiles and inherited P are inputs. This function has no data or outcome I/O.
    """
    p=np.asarray(p,dtype=float); q=np.asarray(q,dtype=float); P=np.asarray(P,dtype=float)
    require(p.shape==q.shape and p.ndim==2 and p.shape[1]==3 and len(p)%8==0,'profile shapes')
    require(P.shape==(len(p),),'P shape')
    require(all(np.isfinite(a).all() for a in (p,q,P)),'finite profiles')
    require(all((a>=0).all() for a in (p,q,P)),'nonnegative profiles')
    require((np.diff(p,axis=1)>=0).all() and (np.diff(q,axis=1)>=0).all(),'ascending profiles')
    x,y=p*p,q*q; signed_h=(p-q)*(p+q)
    lo_z,hi_z=np.minimum(x,y),np.maximum(x,y)
    fractions=np.arange(5,dtype=float)/4
    nodes=lo_z[...,None]+(hi_z-lo_z)[...,None]*fractions
    s=np.sqrt(nodes); log_b=1+np.log1p(s)
    # k(s)/b(s), a deliberately separate arithmetic route to theta.
    theta=(1-s/((1+s)*log_b))/(log_b*log_b)
    def envelope(v):
        m=np.sqrt(np.sum(v*v,axis=1)); vmax=v[:,-1]
        require(not np.any((m==0)&np.any(v!=0,axis=1)),'norm underflow')
        return m/(1+np.log1p(vmax)),m/(1+np.log1p(m/math.sqrt(3)))
    lp,up=envelope(p); lq,uq=envelope(q)
    dl,du=lp+lq,up+uq; nl0,nu0=lp-uq,up-lq
    zero=np.all(p==0,axis=1)&np.all(q==0,axis=1)
    require(np.all(dl[~zero]>0),'positive denominator')
    require(np.all(dl<=du+TOL),'denominator ordering')
    c={'profile_c':p,'profile_d':q,'P_center':P,'x':x,'y':y,'h':signed_h,
       'h_residual':signed_h-(x-y),'nodes_z':nodes,'theta_nodes':theta,
       'L_p':lp,'U_p':up,'L_q':lq,'U_q':uq,'denominator_lo':dl,'denominator_hi':du,
       'norm_difference_lo':nl0,'norm_difference_hi':nu0,'both_zero':zero}
    pair={'P_PROFILE':block_mean(P)}
    for J in (1,4):
        pre=f'J{J}_'
        lowtheta=theta[...,-1] if J==1 else np.sum(theta[...,1:],axis=-1)/4
        hightheta=theta[...,0] if J==1 else np.sum(theta[...,:-1],axis=-1)/4
        terms=np.stack((signed_h*lowtheta,signed_h*hightheta),axis=-1)
        cnlo,cnhi=np.min(terms,axis=-1),np.max(terms,axis=-1)
        nlo,nhi=row_sum(cnlo),row_sum(cnhi)
        quot=np.zeros((len(p),4))
        for col,(a,b) in enumerate(((nlo,dl),(nlo,du),(nhi,dl),(nhi,du))):
            quot[~zero,col]=a[~zero]/b[~zero]
        qlo,qhi=quot.min(axis=1),quot.max(axis=1)
        rlo_original=np.maximum(qlo,nl0); rhi_original=np.minimum(qhi,nu0)
        rlo,rhi,rf=outward_hull(rlo_original,rhi_original)
        elo_original=np.maximum(rlo,-P); ehi_original=np.minimum(rhi,P)
        lo,hi,ef=outward_hull(elo_original,ehi_original); flags=rf|ef
        v={'theta_lo':lowtheta,'theta_hi':hightheta,'component_num_lo':cnlo,'component_num_hi':cnhi,
           'numerator_lo':nlo,'numerator_hi':nhi,'four_quotients':quot,'quotient_lo':qlo,'quotient_hi':qhi,
           'raw_lo_original':rlo_original,'raw_hi_original':rhi_original,'raw_lo':rlo,'raw_hi':rhi,
           'raw_hull_flag':rf,'raw_lo_from_quotient':qlo>=nl0,'raw_hi_from_quotient':qhi<=nu0,
           'effective_lo_original':elo_original,'effective_hi_original':ehi_original,'lo':lo,'hi':hi,
           'effective_hull_flag':ef,'roundoff_flag':flags,'P_active_lo':-P>rlo,'P_active_hi':P<rhi,
           'P_tie_lo':-P==rlo,'P_tie_hi':P==rhi,'midpoint':(lo+hi)/2,'radius':(hi-lo)/2,
           'raw_midpoint':(rlo+rhi)/2,'raw_radius':(rhi-rlo)/2,
           'sign':class_sign(lo,hi,flags),'raw_sign':class_sign(rlo,rhi,rf)}
        c.update({pre+k:a for k,a in v.items()})
        for vpre,a,b in [('',lo,hi),('raw_',rlo,rhi)]:
            pair.update({pre+vpre+k:a for k,a in group_intervals(a,b).items()})
        sign=v['sign'].reshape(-1,8)
        pair[pre+'positive_centers']=np.sum(sign==1,axis=1)
        pair[pre+'negative_centers']=np.sum(sign==-1,axis=1)
        pair[pre+'unresolved_centers']=np.sum(sign==0,axis=1)
        pair[pre+'mixed_resolved_signs']=np.any(sign==1,axis=1)&np.any(sign==-1,axis=1)
        pair[pre+'collective_sign']=class_sign(pair[pre+'lo'],pair[pre+'hi'],np.any(flags.reshape(-1,8),axis=1))
        pair[pre+'roundoff_centers']=np.sum(flags.reshape(-1,8),axis=1)
        pair[pre+'prior_active_centers']=np.sum((v['P_active_lo']|v['P_active_hi']).reshape(-1,8),axis=1)
        for kind in ('unsigned','signed'):
            pair[pre+'raw_to_effective_'+kind]=pair[pre+'raw_'+kind+'_upper']-pair[pre+kind+'_upper']
            pair[f'RADIAL_{J}_{kind.upper()}']=pair[pre+kind+'_upper']
    return c,pair

def outward_hull(lo,hi):
    require(np.all(lo-hi<=TOL),'substantive interval inversion')
    return np.minimum(lo,hi),np.maximum(lo,hi),lo>hi

def class_sign(lo,hi,flag):
    return np.where(flag,0,np.where(lo>TOL,1,np.where(hi< -TOL,-1,0)))

def group_intervals(lo,hi):
    mu=(lo+hi)/2; rad=(hi-lo)/2
    L,H=block_mean(lo),block_mean(hi); M,R,AM=block_mean(mu),block_mean(rad),block_mean(np.abs(mu))
    upper=np.maximum(abs(L),abs(H)); unsigned=block_mean(np.maximum(abs(lo),abs(hi)))
    lower=np.where((L<=0)&(H>=0),0.,np.minimum(abs(L),abs(H)))
    return dict(lo=L,hi=H,midpoint=M,mean_radius=R,mean_abs_midpoint=AM,
                signed_upper=upper,unsigned_upper=unsigned,signed_lower=lower,cancellation=unsigned-upper,
                midpoint_identity_residual=upper-(abs(M)+R),unsigned_identity_residual=unsigned-(AM+R),
                cancellation_identity_residual=unsigned-upper-(AM-abs(M)))

def synthetic_D(v):
    COUNTS['synthetic_reference_D_array_calls']+=1
    COUNTS['synthetic_reference_D_components']+=np.asarray(v).size
    return v/(1+np.log1p(abs(v)))

def synthetic_profiles(v,w):
    p,q=np.sort(abs(v),axis=1),np.sort(abs(w),axis=1)
    a=np.minimum(p,q); b=1+np.log1p(a)
    prior=np.sqrt(np.sum(((b-a/(1+a))/b**2*(p-q))**2,axis=1))
    return p,q,prior

def fixture_call(p,q,P):
    COUNTS['fixture_pair_evaluations']+=len(p)//8
    return angle_free_enclosure(p,q,P)

def fixtures(root):
    groups=jload(root/'received/SIM05_FIXED_FIXTURES_v0.1.json')['groups']
    require([g['id'] for g in groups]==[f'F{i:02d}' for i in range(1,15)],'fixed groups')
    for g in groups:
        gid=g['id']
        for case in g.get('cases',[]):
            tag=gid+'/'+case['name']; COUNTS['fixture_vector_cases']+=1
            v,w=map(lambda k:np.array(case[k],dtype=float),('history_c_vectors','history_d_vectors'))
            p,q,P=synthetic_profiles(v,w); c,a=fixture_call(p,q,P); cr,ar=fixture_call(q,p,P)
            dp,dq,dv,dw=synthetic_D(p),synthetic_D(q),synthetic_D(v),synthetic_D(w)
            f=np.linalg.norm(dp,axis=1); h=np.linalg.norm(dq,axis=1); delta=f-h; S=abs(mean(delta))
            check(tag+'/profile symmetry c',f-np.linalg.norm(dv,axis=1));check(tag+'/profile symmetry d',h-np.linalg.norm(dw,axis=1))
            for key,target in [('p',f),('q',h)]:
                check(tag+'/lower envelope '+key,c['L_'+key]-target,inequality=True)
                check(tag+'/upper envelope '+key,target-c['U_'+key],inequality=True)
            check(tag+'/theta monotone',np.diff(c['theta_nodes'],axis=-1),inequality=True)
            for J in (1,4):
                pre=f'J{J}_'; exact=dp**2-dq**2
                check(tag+pre+'component lower',c[pre+'component_num_lo']-exact,inequality=True)
                check(tag+pre+'component upper',exact-c[pre+'component_num_hi'],inequality=True)
                for raw in ('','raw_'):
                    check(tag+pre+raw+'lower',c[pre+raw+'lo']-delta,inequality=True)
                    check(tag+pre+raw+'upper',delta-c[pre+raw+'hi'],inequality=True)
                    check(tag+pre+raw+'swap lower',c[pre+raw+'lo']+cr[pre+raw+'hi'])
                    check(tag+pre+raw+'swap upper',c[pre+raw+'hi']+cr[pre+raw+'lo'])
                check(tag+pre+'prior lower',-P-c[pre+'lo'],inequality=True)
                check(tag+pre+'prior upper',c[pre+'hi']-P,inequality=True)
                check(tag+pre+'collective lower',a[pre+'signed_lower']-S,inequality=True)
                check(tag+pre+'collective upper',S-a[pre+'signed_upper'],inequality=True)
                check(tag+pre+'signed versus unsigned',a[pre+'signed_upper']-a[pre+'unsigned_upper'],inequality=True)
                check(tag+pre+'unsigned versus P',a[pre+'unsigned_upper']-a['P_PROFILE'],inequality=True)
                for r in ['midpoint_identity_residual','unsigned_identity_residual','cancellation_identity_residual']:check(tag+pre+r,a[pre+r])
                zero=c['h']==0
                require(np.all(c[pre+'component_num_lo'][zero]==0) and np.all(c[pre+'component_num_hi'][zero]==0),tag+' exact zero components')
                if gid in ['F01','F02','F03']:require(np.all(c[pre+'lo']==0)&np.all(c[pre+'hi']==0),tag+' equal profiles zero')
            for raw in ('','raw_'):
                check(tag+raw+'refine lower',c['J1_'+raw+'lo']-c['J4_'+raw+'lo'],inequality=True)
                check(tag+raw+'refine upper',c['J4_'+raw+'hi']-c['J1_'+raw+'hi'],inequality=True)
            if gid=='F04': require(np.all(c['J4_lo']>=0) if case['name']=='positive' else np.all(c['J4_hi']<=0),tag+' zero endpoint sign')
            if gid=='F05': require(np.all(c['J4_lo']>TOL) if case['name']=='larger components' else np.all(c['J4_hi']< -TOL),tag+' resolved sign')
            if gid=='F06':
                check(tag+' equal incoming norm',np.linalg.norm(p,axis=1)-np.linalg.norm(q,axis=1))
                require(np.all(abs(delta)>TOL),tag+' unequal outgoing norms')
            if gid=='F07':require(np.any(c['h']>0)&np.any(c['h']<0),tag+' signed components')
            if gid=='F08':check(tag+' cancellation',mean(delta));require(a['J4_unsigned_upper'][0]>a['J4_signed_upper'][0],tag+' cancellation gain')
            if gid=='F09':require(mean(delta)>TOL and a['J4_signed_lower'][0]>TOL,tag+' partial cancellation')
            if gid=='F11': require(np.all(c['theta_nodes'][c['nodes_z']==0]==1),tag+' theta at zero')
            if gid=='F14':
                witness=delta.copy(); fp=fingerprint(c); witness[:]=999.
                c2,a2=fixture_call(p,q,P); require(fp==fingerprint(c2) and fingerprint(a)==fingerprint(a2),'fixture external outcome canary')
        if gid=='F12':
            for case in g['interval_cases']:
                x=np.array(case['centers'],float); a=group_intervals(x[:,0],x[:,1])
                for k in ['midpoint_identity_residual','unsigned_identity_residual','cancellation_identity_residual']:check(gid+case['name']+k,a[k])
                check(gid+case['name']+' triangle',a['signed_upper']-a['unsigned_upper'],inequality=True)
                require((a['signed_lower'][0]==0)==(a['lo'][0]<=0<=a['hi'][0]),'interval lower')
            l,h,f=outward_hull(np.array([5e-13]),np.array([0.]));require(l[0]==0 and h[0]==5e-13 and f[0],'small hull')
            try: outward_hull(np.array([2e-12]),np.array([0.]))
            except AssertionError: pass
            else: raise AssertionError('large inversion not rejected')
            require(ratio_scalar(0,0,1e-12) is None,'undefined ratio mask')
        if gid=='F13':
            prof={}; values={}
            for row in g['cycles']:
                v=np.array(row['vectors'],float); prof[row['cycle']]=np.sort(abs(v),axis=1)
                values[row['cycle']]=mean(np.linalg.norm(synthetic_D(v),axis=1))
            pb={}
            for c,d in PAIRS:
                p,q,P=synthetic_profiles(prof[c],prof[d]); _,a=fixture_call(p,q,P)
                pb[c,d]=a
            for view,cycles in g['views'].items():
                m=len(cycles); vals=[values[c] for c in cycles]; mu=mean(vals)
                var=math.fsum((v-mu)**2 for v in vals)/m
                keys=[(c,d) for c,d in PAIRS if c in cycles and d in cycles]
                check('F13 '+view+' variance',math.fsum((values[c]-values[d])**2 for c,d in keys)/m**2-var,VTOL)
                require(len(keys)==(10 if m==5 else 6),'fixture complete pairs')
                for J in (1,4):
                    low=math.fsum(pb[k][f'J{J}_signed_lower'][0]**2 for k in keys)/m**2
                    high=math.fsum(pb[k][f'J{J}_signed_upper'][0]**2 for k in keys)/m**2
                    check('F13 '+view+str(J)+' lower',low-var,VTOL,True);check('F13 '+view+str(J)+' upper',var-high,VTOL,True)
            require([margin_label(x) for x in [2e-14,-2e-14,0]]==['PASS','NOT_ESTABLISHED','UNRESOLVED'],'margin thresholds')
        COUNTS['fixture_groups']+=1
    stored=jload(root/'evidence/ALGEBRA_FIXTURES.json')
    require(stored['assertions']==816==len(stored['checks']) and all(x['PASS'] for x in stored['checks']),'submitted 816 fixture assertion records')
    for x in stored['checks']:
        require((x['max_abs'] if x['kind']=='equality' else x['max_signed'])<=x['tolerance'],'stored fixture tolerance')
    return {'all_14_fixed_groups_pass':True,'stored_816_assertions_consistent':True,
            'independent_numeric_comparisons':len(CHECKS),'counts':dict(COUNTS)}

def fingerprint(arrays):
    return {k:{'shape':list(np.asarray(v).shape),'dtype':str(np.asarray(v).dtype),
               'sha256':hashlib.sha256(np.ascontiguousarray(v).tobytes()).hexdigest()} for k,v in arrays.items()}
def csvrows(path):
    with Path(path).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def pair_key(row):return tuple(int(row[k]) for k in ('cycle_c','cycle_d','phase'))
def ratio_scalar(a,b,floor):return a/b if b>=floor else None
def margin_label(x):return 'PASS' if x>VTOL else 'NOT_ESTABLISHED' if x< -VTOL else 'UNRESOLVED'
def actual_label(x):return 'DECREASE' if x>VTOL else 'INCREASE' if x< -VTOL else 'UNRESOLVED'

def input_maps(z):
    pk={}; ck={}; require(len(z['pair__pair_id'])==2000,'upstream pair count')
    for r in range(2000):
        c,d,j=[int(z['pair__'+k][r]) for k in ('cycle_c','cycle_d','phase')]
        require((c,d) in PAIRS and 0<=j<200 and (c,d,j) not in pk,'upstream keys')
        require(int(z['pair__pair_id'][r])==PAIRS.index((c,d)),'upstream pair id')
        require(int(z['pair__update_c'][r])==200*c+j and int(z['pair__update_d'][r])==200*d+j,'upstream updates')
        pk[c,d,j]=r
    reverse={r:k for k,r in pk.items()}
    for r,(pr,i) in enumerate(zip(z['center__pair_phase_row'],z['center__center'])):
        require(int(pr) in reverse and 0<=int(i)<8,'center ids')
        k=(*reverse[int(pr)],int(i)); require(k not in ck,'center unique');ck[k]=r
    require(len(ck)==16000 and len(pk)==2000,'key counts')
    return pk,ck

def build_views(pair):
    v={'view':[],'phase':[],'cycles':[],'pairs':[]}
    for view,cycles in [('all_five',range(5)),('new_four',range(1,5))]:
        m=len(cycles)
        for j in range(200):
            ix=np.where((pair['phase']==j)&np.isin(pair['cycle_c'],list(cycles))&np.isin(pair['cycle_d'],list(cycles)))[0]
            require(len(ix)==m*(m-1)//2,'complete view pairs')
            vals={'view':view,'phase':j,'cycles':m,'pairs':len(ix)}
            for f in ALL: vals[f+'_variance_upper']=math.fsum(pair[f][ix]**2)/m**2
            for J in (1,4): vals[f'J{J}_variance_lower']=math.fsum(pair[f'J{J}_signed_lower'][ix]**2)/m**2
            for k,x in vals.items():v.setdefault(k,[]).append(x)
    return {k:np.array(x) for k,x in v.items()}

def compare_mapping(prefix,a,b,tol=TOL):
    require(set(a)==set(b),prefix+' field set: '+str(set(a)^set(b)))
    for k in a:compare(prefix+'/'+k,a[k],b[k], VTOL if 'variance' in k else tol)

# Table parsing is explicit; classification/booleans/JSON locators are not coerced into numeric zeros.
def cell(value):
    if value=='':return None
    if value in ('True','False'):return value=='True'
    if value[:1] in ('{','['):
        try:return json.loads(value)
        except json.JSONDecodeError:pass
    try:return float(value)
    except ValueError:return value

def table_columns(rows):return {k:[cell(r[k]) for r in rows] for k in rows[0]}

def compare_table(name, expected, rows):
    got=table_columns(rows)
    require(set(expected)==set(got),name+' columns '+str(set(expected)^set(got)))
    for k in expected:
        a=np.asarray(expected[k]); b=got[k]
        if k.endswith('_factor') or k.endswith('_utilization'):
            # Preserve discrepancy, but test each quotient via its unamplified product.
            kind='factor' if k.endswith('_factor') else 'utilization'
            base=k[:-(len(kind)+1)]
            if name.startswith('pair'):
                numerator=expected[base] if kind=='factor' else expected['observed_S']
                denominator=expected['observed_S'] if kind=='factor' else expected[base]
            else:
                stage_kind='variance' if base.endswith('_variance') else 'SD'
                numerator=expected[base+'_upper'] if kind=='factor' else expected['post_'+stage_kind]
                denominator=expected['post_'+stage_kind] if kind=='factor' else expected[base+'_upper']
            valid=np.array([x is not None for x in b]); require(np.array_equal(valid,np.array([x is not None for x in expected[k]])),name+k+' quotient mask')
            residual=np.array([b[i]*denominator[i]-numerator[i] for i in np.where(valid)[0]])
            tol=VTOL if 'variance' in base else TOL
            check(name+'/'+k+' product',residual,tol)
            COMPARES[name+'/'+k]={'ratio_compared_through_native_product':True,'max_raw_quotient_discrepancy':float(max([abs(b[i]-expected[k][i]) for i in np.where(valid)[0]] or [0.]))}
        elif a.dtype.kind in 'buiUS': compare(name+'/'+k,a,np.asarray(b,dtype=a.dtype))
        else: compare(name+'/'+k,np.asarray(a,float),np.asarray(b,float),VTOL if 'variance' in k or k.endswith('_margin') else TOL)


def add_ratios(d,base,bound,outcome,floor):
    d[base+'_gap']=bound-outcome
    for k,nu,de in [('factor',bound,outcome),('utilization',outcome,bound)]:
        valid=de>=floor; arr=np.empty(len(de),dtype=object);arr[:]=None
        arr[valid]=nu[valid]/de[valid]
        d[base+'_'+k]=arr.tolist();d[base+'_'+k+'_valid']=valid


def join_outcomes(root,c,pair,view,keys):
    fields=['pair__'+k for k in ('pair_id','cycle_c','cycle_d','phase','update_c','update_d')]+['center__pair_phase_row','center__center',
      'outcome__signed_speed_difference','outcome__individual_abs_speed_difference']
    with np.load(root/'inputs/analysis/center_pair_bounds.npz',allow_pickle=False) as z:od={k:z[k] for k in fields}
    _,oc=input_maps(od)
    ids=np.array([oc[(*k,i)] for k in keys for i in range(8)])
    delta=od['outcome__signed_speed_difference'][ids]; adelta=od['outcome__individual_abs_speed_difference'][ids]
    require(np.isfinite(delta).all()&np.isfinite(adelta).all(),'outcome finite')
    compare('outcome individual abs',adelta,abs(delta),0.)
    signed=block_mean(delta); S=abs(signed)
    priorrows=csvrows(root/'inputs/analysis/pair_phase_bounds.csv'); old={pair_key(r):r for r in priorrows}
    require(set(keys)==set(old) and len(priorrows)==2000,'prior CSV keys')
    accepted=np.array([float(old[k]['signed_collective_difference']) for k in keys]); prior=np.array([float(old[k]['P_PROFILE']) for k in keys])
    pair.update(signed_collective_difference=signed,observed_S=S,accepted_signed_collective_difference=accepted,
                collective_reduction_residual=signed-accepted,prior_reference_residual=pair['P_PROFILE']-prior,
                observed_Tnorm=block_mean(adelta))
    for f in ALL:add_ratios(pair,f,pair[f],S,TOL)
    for J in (1,4):pair[f'J{J}_radius_minus_remaining_slack']=pair[f'J{J}_mean_radius']-(pair[f'RADIAL_{J}_SIGNED']-S)
    pair.update(gap_P_to_unsigned4=pair['P_PROFILE']-pair['RADIAL_4_UNSIGNED'],gap_unsigned4_to_signed4=pair['RADIAL_4_UNSIGNED']-pair['RADIAL_4_SIGNED'],
                gap_signed4_to_S=pair['RADIAL_4_SIGNED']-S,gap_P_to_S=pair['P_PROFILE']-S,
                refinement_signed_J1_to_J4=pair['RADIAL_1_SIGNED']-pair['RADIAL_4_SIGNED'],
                refinement_unsigned_J1_to_J4=pair['RADIAL_1_UNSIGNED']-pair['RADIAL_4_UNSIGNED'])
    pair['gap_telescope_residual']=pair['gap_P_to_S']-pair['gap_P_to_unsigned4']-pair['gap_unsigned4_to_signed4']-pair['gap_signed4_to_S']
    sr=csvrows(root/'inputs/analysis/cycle_phase_speeds.csv'); sm={(int(r['cycle']),int(r['phase'])):r for r in sr}
    require(len(sr)==len(sm)==1000 and set(sm)=={(c,j) for c in range(5) for j in range(200)},'speed keys')
    vr=csvrows(root/'inputs/analysis/phase_dispersion_bounds.csv'); vm={(r['view'],int(r['phase'])):r for r in vr}
    require(len(vr)==len(vm)==400,'old view keys')
    for stage in ['incoming','pre_damping','post']:
        var=[]; pv=[]; ref=[]
        for v,j in zip(view['view'],view['phase']):
            cs=list(range(5)) if v=='all_five' else list(range(1,5)); u={k:float(sm[k,int(j)][stage]) for k in cs};mu=mean(list(u.values()))
            var.append(math.fsum((x-mu)**2 for x in u.values())/len(cs))
            pv.append(math.fsum((u[a]-u[b])**2 for a,b in PAIRS if a in cs and b in cs)/len(cs)**2)
            ref.append(float(vm[v,int(j)][stage+'_variance']))
        var,pv,ref=map(np.array,(var,pv,ref))
        view[stage+'_variance']=var;view[stage+'_SD']=np.sqrt(var);view[stage+'_pair_variance']=pv
        view[stage+'_pair_identity_residual']=pv-var;view[stage+'_reference_residual']=var-ref
    view['P_variance_reference_residual']=view['P_PROFILE_variance_upper']-np.array([float(vm[v,int(j)]['P_PROFILE_variance_upper']) for v,j in zip(view['view'],view['phase'])])
    for f in ALL:
        view[f+'_SD_upper']=np.sqrt(view[f+'_variance_upper'])
        for kind,floor in [('variance',1e-24),('SD',TOL)]:add_ratios(view,f+'_'+kind,view[f+'_'+kind+'_upper'],view['post_'+kind],floor)
    for J in (1,4):view[f'J{J}_SD_lower']=np.sqrt(view[f'J{J}_variance_lower'])
    for ref in ('incoming','pre_damping'):
        margin=view[ref+'_variance']-view['post_variance'];view[ref+'_actual_margin']=margin
        view[ref+'_actual_class']=np.array([actual_label(x) for x in margin])
        for J in (1,4):
            for direction,margin in [('decrease',view[ref+'_variance']-view[f'RADIAL_{J}_SIGNED_variance_upper']),('increase',view[f'J{J}_variance_lower']-view[ref+'_variance'])]:
                k=f'J{J}_{ref}_{direction}';view[k+'_margin']=margin;view[k+'_class']=np.array([margin_label(x) for x in margin])
                contradiction=(view[k+'_class']=='PASS')&(view[ref+'_actual_class']==('INCREASE' if direction=='decrease' else 'DECREASE'))
                require(not contradiction.any(),'no opposite certificates')
    COUNTS['outcome_pair_phase_joins']=len(keys)
    return delta,adelta,ids


def residual_map(c,p,v,prior_res,delta,adelta):
    res={'prior_center_mean_minus_pair':prior_res,'stable_h_minus_direct_squares':c['h_residual'],
         'theta_node_monotonicity':np.diff(c['theta_nodes'],axis=-1)}
    for J in (1,4):
        s=f'J{J}_'
        for a,b in [('numerator_lo','numerator_hi'),('raw_lo_original','raw_hi_original'),('effective_lo_original','effective_hi_original'),('lo','hi')]:res[s+a+'_minus_'+b]=c[s+a]-c[s+b]
        res[s+'effective_hi_minus_prior']=c[s+'hi']-c['P_center'];res[s+'minus_prior_minus_effective_lo']=-c['P_center']-c[s+'lo']
        for raw in ('','raw_'):
            res[s+raw+'signed_minus_unsigned']=p[s+raw+'signed_upper']-p[s+raw+'unsigned_upper']
            for k in ['midpoint_identity_residual','unsigned_identity_residual','cancellation_identity_residual']:res[s+raw+k]=p[s+raw+k]
        res[s+'unsigned_minus_P']=p[s+'unsigned_upper']-p['P_PROFILE'];res[s+'signed_lower_minus_upper']=p[s+'signed_lower']-p[s+'signed_upper']
    for raw in ('','raw_'):
        res[raw+'nesting_lower']=c['J1_'+raw+'lo']-c['J4_'+raw+'lo'];res[raw+'nesting_upper']=c['J4_'+raw+'hi']-c['J1_'+raw+'hi']
    for kind in ('signed','unsigned'):res[kind+'_J4_minus_J1']=p['J4_'+kind+'_upper']-p['J1_'+kind+'_upper']
    res['lower_J1_minus_J4']=p['J1_signed_lower']-p['J4_signed_lower'];res['saved_absolute_difference']=adelta-abs(delta)
    res['collective_reduction_order']=p['collective_reduction_residual'];res['prior_reference_identity']=p['prior_reference_residual']
    for J in (1,4):
        s=f'J{J}_'
        for raw in ('','raw_'):
            res[s+raw+'center_lower_minus_outcome']=c[s+raw+'lo']-delta
            res[s+raw+'outcome_minus_center_upper']=delta-c[s+raw+'hi']
            res[s+raw+'collective_lower_minus_outcome']=p[s+raw+'lo']-p['signed_collective_difference']
            res[s+raw+'outcome_minus_collective_upper']=p['signed_collective_difference']-p[s+raw+'hi']
        res[s+'absolute_lower_minus_S']=p[s+'signed_lower']-p['observed_S']
    for f in ALL:res['S_minus_'+f]=p['observed_S']-p[f]
    for k in ['gap_P_to_unsigned4','gap_unsigned4_to_signed4','gap_signed4_to_S']:res['negative_'+k]=-p[k]
    res['gap_telescope']=p['gap_telescope_residual']
    for stage in ('incoming','pre_damping','post'):
        for suffix in ('pair_identity_residual','reference_residual'):res[stage+'_'+suffix]=v[stage+'_'+suffix]
    res['P_variance_reference']=v['P_variance_reference_residual']
    for f in ALL:res['post_variance_minus_'+f]=v['post_variance']-v[f+'_variance_upper']
    for J in (1,4):res[f'J{J}_lower_variance_minus_post']=v[f'J{J}_variance_lower']-v['post_variance']
    res['variance_upper_refinement']=v['RADIAL_4_SIGNED_variance_upper']-v['RADIAL_1_SIGNED_variance_upper']
    res['variance_lower_refinement']=v['J1_variance_lower']-v['J4_variance_lower']
    return res

def locator(row):
    return {k:row[k] for k in ('pair_id','cycle_c','cycle_d','phase','view','center') if k in row}

def stat(values,locs):
    vals=[(float(a),b) for a,b in zip(values,locs) if a is not None and math.isfinite(float(a))]
    result={'count':len(vals),'masked':len(values)-len(vals),'exact_zero':sum(a==0 for a,b in vals)}
    if not vals:
        return {**result,**{k:None for k in ['min','p05','median','p95','max','mean','min_locator','p05_locator','median_locator','p95_locator','max_locator']}}
    xs=np.array([a for a,b in vals]); order=np.argsort(xs,kind='stable')
    for name,prob in [('min',0.),('p05',.05),('median',.5),('p95',.95),('max',1.)]:
        position=(len(xs)-1)*prob; low=math.floor(position); high=math.ceil(position)
        result[name]=float(np.quantile(xs,prob,method='linear'))
        result[name+'_locator']={'lower':vals[int(order[low])][1],'upper':vals[int(order[high])][1],'upper_weight':position-low}
    result['mean']=math.fsum(xs)/len(xs)
    return result

def recursive_compare(a,b,name,tol=TOL):
    if isinstance(a,dict):
        require(isinstance(b,dict) and set(a)==set(b),name+' dict keys')
        for k in a:recursive_compare(a[k],b[k],name+'/'+k,tol)
    elif isinstance(a,(list,tuple)):
        require(isinstance(b,list) and len(a)==len(b),name+' list count')
        for i,(x,y) in enumerate(zip(a,b)):recursive_compare(x,y,name+'/'+str(i),tol)
    elif a is None or isinstance(a,(str,bool,int,np.integer)):
        require(a==b,name+' exact '+str(a)+' != '+str(b))
    else:
        require(b is not None and math.isfinite(float(a)) and abs(float(a)-float(b))<=tol,name+' difference '+str((a,b)))

def parsed_rows(rows):return [{k:cell(v) for k,v in r.items()} for r in rows]

def category(rows,bound,outcome,floor):
    good=[r for r in rows if r[outcome]>=floor]
    return dict(resolved=len(good),unresolved=len(rows)-len(good),outcome_exact_zero=sum(r[outcome]==0 for r in rows),
      bound_exact_zero=sum(r[bound]==0 for r in rows),utilization_unresolved=sum(r[bound]<floor for r in rows),
      **{f'within_factor_{n}':sum(r[bound]<=n*r[outcome] for r in good) for n in [2,5,10]})

def summaries(root,pcsv,vcsv,c):
    # Summaries are recomputed from primitive submission rows that were independently verified.
    # This avoids treating amplified quotient rounding as an unnormalized-speed error.
    p=parsed_rows(pcsv);v=parsed_rows(vcsv);result=jload(root/'analysis/RESULTS.json')
    groups={'all_pairs':p,'new_four_pairs':[r for r in p if r['cycle_d']>0]}
    groups.update({f'pair_{a}_{b}':[r for r in p if r['cycle_c']==a and r['cycle_d']==b] for a,b in PAIRS})
    bs={(r['scope'],r['family'],r['metric']):r for r in parsed_rows(csvrows(root/'analysis/bound_summary.csv'))}
    gs={(r['scope'],r['family'],r['metric']):r for r in parsed_rows(csvrows(root/'analysis/gap_summary.csv'))}
    metric_names=['gap_P_to_unsigned4','gap_unsigned4_to_signed4','gap_signed4_to_S','gap_P_to_S',
                  'refinement_signed_J1_to_J4','refinement_unsigned_J1_to_J4']
    for J in (1,4):metric_names.extend(f'J{J}_'+s for s in ['mean_radius','raw_mean_radius','cancellation','midpoint','mean_abs_midpoint','signed_lower','raw_to_effective_unsigned','raw_to_effective_signed','radius_minus_remaining_slack'])
    seen_bound=set(); seen_gap=set()
    def verify_stat(scope,family,metric,unit,computed,target,json_target):
        record=target[(scope,family,metric)]
        recursive_compare(computed,{k:record[k] for k in computed},'summary CSV '+str((scope,family,metric)))
        require(record['units']==unit,'summary units')
        recursive_compare(computed,json_target,'summary JSON '+str((scope,family,metric)))
    for scope,rs in groups.items():
        locs=[locator(r) for r in rs]
        for f in ALL:
            for metric,col,unit in [('bound',f,'speed'),('gap',f+'_gap','speed'),('factor',f+'_factor','dimensionless'),('utilization',f+'_utilization','dimensionless')]:
                s=stat([r[col] for r in rs],locs)
                verify_stat(scope,f,metric,unit,s,bs,result['summary'][scope][f][metric]);seen_bound.add((scope,f,metric))
            recursive_compare(category(rs,f,'observed_S',TOL),result['factor_categories'][scope][f],'pair categories '+scope+f)
        for k in metric_names:
            s=stat([r[k] for r in rs],locs)
            verify_stat(scope,'interval_diagnostics',k,'speed',s,gs,result['gaps'][scope][k]);seen_gap.add((scope,'interval_diagnostics',k))
        for J in (1,4):
            s=f'J{J}_';counts={
              'mixed_resolved_center_signs':sum(r[s+'mixed_resolved_signs'] for r in rs),
              'collective_positive':sum(r[s+'collective_sign']==1 for r in rs),'collective_negative':sum(r[s+'collective_sign']==-1 for r in rs),
              'collective_unresolved':sum(r[s+'collective_sign']==0 for r in rs),
              'cancellation_positive_over_tolerance':sum(r[s+'cancellation']>TOL for r in rs),
              'cancellation_exact_zero':sum(r[s+'cancellation']==0 for r in rs),
              'unsigned_equals_P_exact':sum(r[f'RADIAL_{J}_UNSIGNED']==r['P_PROFILE'] for r in rs),
              'unsigned_equals_P_within_tolerance':sum(abs(r[f'RADIAL_{J}_UNSIGNED']-r['P_PROFILE'])<=TOL for r in rs),
              'signed_equals_P_exact':sum(r[f'RADIAL_{J}_SIGNED']==r['P_PROFILE'] for r in rs),
              'signed_equals_P_within_tolerance':sum(abs(r[f'RADIAL_{J}_SIGNED']-r['P_PROFILE'])<=TOL for r in rs),
              'prior_intersection_active_pairs':sum(r[s+'prior_active_centers']>0 for r in rs),
              'roundoff_affected_pairs':sum(r[s+'roundoff_centers']>0 for r in rs)}
            recursive_compare(counts,result['counts'][scope][s],'counts '+scope+s)
        ref={k:{'strict_over_tolerance':sum(r[k]>TOL for r in rs),'exact_zero':sum(r[k]==0 for r in rs)} for k in metric_names[4:6]}
        recursive_compare(ref,result['counts'][scope]['refinement'],'refinement '+scope)
    aggregates={};conditions={}
    for view in ['all_five','new_four']:
        rs=[r for r in v if r['view']==view];locs=[locator(r) for r in rs]
        agg={'actual_RMS_phase_SD':{s:math.sqrt(mean([r[s+'_variance'] for r in rs])) for s in ['incoming','pre_damping','post']},'bounds':{}}
        cond={}
        for f in ALL:
            W=mean([r[f+'_variance_upper'] for r in rs]);SD=math.sqrt(W);obs=agg['actual_RMS_phase_SD']['post']
            agg['bounds'][f]={'mean_variance_upper':W,'RMS_phase_SD_upper':SD,'SD_factor':SD/obs if obs>=TOL else None}
            for kind,floor,unit in [('variance',1e-24,'speed_squared'),('SD',TOL,'speed')]:
                for metric,col,unt in [('bound',f+'_'+kind+'_upper',unit),('gap',f+'_'+kind+'_gap',unit),('factor',f+'_'+kind+'_factor','dimensionless'),('utilization',f+'_'+kind+'_utilization','dimensionless')]:
                    m=kind+'_'+metric;s=stat([r[col] for r in rs],locs)
                    verify_stat(view,f,m,unt,s,bs,result['summary'][view][f][m]);seen_bound.add((view,f,m))
                recursive_compare(category(rs,f+'_'+kind+'_upper','post_'+kind,floor),result['factor_categories'][view][f][kind],'view categories '+view+f+kind)
        for J in (1,4):
            s=f'J{J}_';W=mean([r[s+'variance_lower'] for r in rs])
            agg[s+'lower']={'mean_variance_lower':W,'RMS_phase_SD_lower':math.sqrt(W)};cond[s]={}
            for ref in ['incoming','pre_damping']:
                con={}
                for test in ['decrease','increase']:
                    k=s+ref+'_'+test
                    con[test]={'counts':{label:sum(r[k+'_class']==label for r in rs) for label in ['PASS','NOT_ESTABLISHED','UNRESOLVED']},
                     'exact_zero':sum(r[k+'_margin']==0 for r in rs),'margin':stat([r[k+'_margin'] for r in rs],locs),
                     'PASS_phases':[int(r['phase']) for r in rs if r[k+'_class']=='PASS']}
                con['actual']={label:sum(r[ref+'_actual_class']==label for r in rs) for label in ['DECREASE','INCREASE','UNRESOLVED']}
                cond[s][ref]=con
        recursive_compare(agg,result['aggregate'][view],'aggregates '+view)
        recursive_compare(cond,result['conditions'][view],'conditions '+view)
        aggregates[view]=agg;conditions[view]=cond
    require(set(bs)==seen_bound and len(bs)==576,'all 576 bound summary rows')
    require(set(gs)==seen_gap and len(gs)==288,'all 288 gap summary rows')
    center_counts={}
    for J in (1,4):
        s=f'J{J}_';sign=c[s+'sign']
        center_counts[s]={
         'positive':int(np.sum(sign==1)),'negative':int(np.sum(sign==-1)),'unresolved':int(np.sum(sign==0)),
         'raw_hulls':int(np.sum(c[s+'raw_hull_flag'])),'effective_hulls':int(np.sum(c[s+'effective_hull_flag'])),
         'prior_active_lower':int(np.sum(c[s+'P_active_lo'])),'prior_active_upper':int(np.sum(c[s+'P_active_hi'])),
         'prior_active_either':int(np.sum(c[s+'P_active_lo']|c[s+'P_active_hi'])),
         'effective_unchanged_from_raw':int(np.sum((c[s+'lo']==c[s+'raw_lo'])&(c[s+'hi']==c[s+'raw_hi'])))}
    recursive_compare(center_counts,result['center_counts'],'center counts')
    pm=parsed_rows(csvrows(root/'analysis/phase_interval_means.csv'));require(len(pm)==200,'phase means count')
    for j,r in enumerate(pm):
        rs=[r for r in p if r['phase']==j];want={'phase':j,'pairs':10}
        want.update({k+'_mean':mean([row[k] for row in rs]) for k in ALL+['observed_S']+metric_names})
        recursive_compare(want,r,'phase interval means '+str(j))
    ex={}
    for k in ['gap_P_to_unsigned4','gap_unsigned4_to_signed4','gap_signed4_to_S','RADIAL_4_SIGNED_factor']:
        chosen=sorted([r for r in p if r[k] is not None],key=lambda x:x[k],reverse=True)[:5]
        ex[k]=[{**locator(r),'value':r[k],'S':r['observed_S'],'P':r['P_PROFILE'],'U4':r['RADIAL_4_UNSIGNED'],'B4':r['RADIAL_4_SIGNED']} for r in chosen]
    recursive_compare(ex,result['fixed_extreme_locators'],'top five extreme locators')
    return {'all_six_CSV_tables_verified':True,'table_rows':{'pair_phase_intervals':2000,'phase_dispersion_intervals':400,
     'join_map':16000,'bound_summary':576,'gap_summary':288,'phase_interval_means':200},
     'aggregate':aggregates,'conditions':conditions,'center_counts':center_counts,'extremes':ex}


def preservation(root,seal):
    baseline=jload(root/'evidence/BASELINE_BEFORE.json')
    require(baseline==jload(root/'evidence/PRESERVATION_AFTER.json')['baseline_after']==seal['baseline_after'],'preservation records agree')
    require(baseline['staged']=='' and len(baseline['modified_tracked'])==10,'baseline dirty and staging counts')
    frozen=jload(root/'evidence/IMPLEMENTATION_GATE.json')['frozen_files']
    for n,ident in frozen.items():require(identity(root/n)==ident,'frozen identity '+n)
    before=jload(root/'analysis/PRE_OUTPUT_INTERVALS_SEAL.json')
    require(before['identity']==identity(root/'analysis/PRE_OUTPUT_INTERVALS.npz'),'pre-output seal identity')
    require(before['counts']['outcome_pair_phase_joins']==0 and before['outcome_fields_loaded']==[],'production pre-output status')
    log=jload(root/'evidence/DATA_ACCESS_LOG.json')['access']
    require(log[0]['utc']<before['utc']<log[1]['utc']<=log[2]['utc'],'logged dataflow ordering')
    require(log[0]['fields']==before['allowed_fields'],'allowed inputs')
    require(jload(root/'evidence/MATHEMATICAL_GATE.json')['utc']<=jload(root/'evidence/ALGEBRA_FIXTURES.json')['utc']<before['utc'],'proof fixture ordering')
    for name in ['FIXTURES','PRIMARY','FIGURES']:
        rec=jload(root/f'evidence/{name}_COMPLETE.json')
        require(rec['status']=='PASS' and rec['attempts']==1 and rec['seconds']<=rec['limit_seconds'],'stage receipt '+name)
    tree=ast.parse((root/'analyst/radial.py').read_text())
    forbidden={'D','F','open','load','read','random','saved_successor_velocity','retention','post_norm','__import__','eval','exec'}
    require(not any(isinstance(n,ast.Name) and n.id in forbidden for n in ast.walk(tree)),'pure module static names')
    require([n.names[0].name for n in ast.walk(tree) if isinstance(n,ast.Import)]==['math','numpy'],'pure imports')
    require(seal['aggregate_bytes_including_this_seal']<=seal['aggregate_cap_bytes'],'submission size cap')
    return {'before_after_and_transport_baselines_agree':True,'dirty_tracked_count':10,'staging_empty_in_receipt':True,
       'frozen_files':len(frozen),'production_pre_output_order_consistent':True,'static_pure_function_boundary':'PASS',
       'local_filesystem_independently_accessed':False,'remote_main_queried':False}


def main(args):
    root=Path(args.submission);out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    startpath=out/'REVIEW_STARTED.json'
    with startpath.open('x',encoding='utf-8') as f:json.dump({'started':now(),'method':'new independent reviewer; one pass; fixed source population'},f)
    start=time.monotonic();np.seterr(all='raise')
    try:
        seal=jload(args.seal)
        proofmeta=preservation(root,seal)
        fix=fixtures(root);dump(out/'FIXTURE_REVIEW.json',fix)
        fields=['pair__'+k for k in ['pair_id','cycle_c','cycle_d','phase','update_c','update_d','P_PROFILE']]+[
          'center__pair_phase_row','center__center','center__profile_c','center__profile_d','center__P_center']
        with np.load(root/'inputs/analysis/PRE_OUTPUT_BOUNDS.npz',allow_pickle=False) as z:data={k:z[k] for k in fields}
        pk,ck=input_maps(data);keys=[(a,b,j) for a,b in PAIRS for j in range(200)]
        prows=np.array([pk[k] for k in keys]);crows=np.array([ck[(*k,i)] for k in keys for i in range(8)])
        # The only actual analytic data here are the 12 permitted upstream fields.
        c,p=angle_free_enclosure(data['center__profile_c'][crows],data['center__profile_d'][crows],data['center__P_center'][crows])
        prior_res=p['P_PROFILE']-data['pair__P_PROFILE'][prows];p['P_PROFILE']=data['pair__P_PROFILE'][prows]
        p={**{k:data['pair__'+k][prows] for k in ['pair_id','cycle_c','cycle_d','phase','update_c','update_d']},**p}
        c['pair_phase_row']=np.repeat(np.arange(2000),8);c['center']=np.tile(np.arange(8),2000)
        v=build_views(p)
        COUNTS.update(primary_pair_phase_evaluations=2000,primary_center_pairs=16000,primary_component_pairs=48000,
                      primary_derivative_node_slots=240000,view_phase_summaries=400)
        analytic={**{'center__'+k:x for k,x in c.items()},**{'pair__'+k:x for k,x in p.items()},**{'view__'+k:x for k,x in v.items()}}
        dump(out/'REVIEW_PREOUTPUT_FINGERPRINTS.json',{'sealed':now(),'outcome_fields_loaded':False,'counts':dict(COUNTS),
                                                    'arrays':fingerprint(analytic)})
        with np.load(root/'analysis/PRE_OUTPUT_INTERVALS.npz',allow_pickle=False) as z:
            compare_mapping('pre_output',analytic,{k:z[k] for k in z.files})
        delta,adelta,orows=join_outcomes(root,c,p,v,keys)
        with np.load(root/'analysis/center_intervals_and_outcomes.npz',allow_pickle=False) as z:
            cm={**{'center__'+k:x for k,x in c.items()},'outcome__signed_speed_difference':delta,'outcome__individual_abs_speed_difference':adelta}
            compare_mapping('center_outcome',cm,{k:z[k] for k in z.files})
        pcsv=csvrows(root/'analysis/pair_phase_intervals.csv');vcsv=csvrows(root/'analysis/phase_dispersion_intervals.csv')
        compare_table('pair',p,pcsv);compare_table('view',v,vcsv)
        jrows=parsed_rows(csvrows(root/'analysis/join_map.csv'));require(len(jrows)==16000,'join-map count')
        for k,(row,srow,orow) in enumerate(zip(jrows,crows,orows)):
            a,b,j=keys[k//8];expected=dict(pair_phase_row=k//8,center=k%8,cycle_c=a,cycle_d=b,phase=j,
                input_pair_source_row=int(prows[k//8]),input_center_source_row=int(srow),outcome_center_source_row=int(orow))
            recursive_compare(expected,row,'join '+str(k))
        source_rows=csvrows(root/'inputs/analysis/selected_record_map.csv')
        require(len(source_rows)==8000 and {(int(r['dataset_id']),int(r['update_index']),int(r['center'])) for r in source_rows}==
          {(0 if a==0 else 2,200*a+j,i) for a in range(5) for j in range(200) for i in range(8)},'represented source population')
        residual=residual_map(c,p,v,prior_res,delta,adelta)
        qa=jload(root/'evidence/NUMERICAL_QA.json')['checks']
        with np.load(root/'analysis/NUMERICAL_RESIDUALS.npz',allow_pickle=False) as z:
            require(len(z.files)==len(residual)==len(qa)==96 and set(z.files)==set(residual)==set(qa),'96 residual names')
            for name,a in residual.items():
                meta=qa[name]; tolerance=float(meta['tolerance']);inequality=meta['kind']=='inequality'
                check('numerical/'+name,a,tolerance,inequality)
                b=z[name];compare('residual/'+name,a,b,tolerance)
                require(list(b.shape)==meta['shape'],'QA shape '+name)
                for field,value in [('min_signed',float(b.min())),('max_signed',float(b.max())),('max_abs',float(np.max(abs(b))))]:
                    require(value==meta[field],'stored QA extremum '+name+field)
                for field,ind in [('min_index',np.argmin(b)),('max_index',np.argmax(b)),('max_abs_index',np.argmax(abs(b)))]:
                    want=list(np.unravel_index(int(ind),b.shape)) if b.shape else []
                    require(want==meta[field],'QA locator '+name+field)
        sums=summaries(root,pcsv,vcsv,c)
        # Preserve direct independently calculated tightness and nonpassing phase rows.
        direct={}
        for view in ['all_five','new_four']:
            ix=v['view']==view;obs=math.sqrt(mean(v['post_variance'][ix]))
            direct[view]={'observed_aggregate_SD':obs,'J4_lower_aggregate_SD':math.sqrt(mean(v['J4_variance_lower'][ix])),
             'J4_upper_aggregate_SD':math.sqrt(mean(v['RADIAL_4_SIGNED_variance_upper'][ix])),
             'J4_upper_SD_factor':math.sqrt(mean(v['RADIAL_4_SIGNED_variance_upper'][ix]))/obs,
             'nonpassing_J4_pre_damping_decrease_phases':[int(j) for j in v['phase'][ix&(v['J4_pre_damping_decrease_class']!='PASS')]]}
        result={'status':'PASS','started':jload(startpath)['started'],'completed':now(),'elapsed_seconds':time.monotonic()-start,
                'environment':{'python':sys.version,'numpy':np.__version__,'platform':platform.platform()},
                'counts':COUNTS,'represented_distinct_saved_updates':1000,'represented_distinct_center_records':8000,
                'source_and_preservation':proofmeta,'fixture_review':fix,'analytic_field_count':len(analytic),
                'independent_direct_results':direct,'summary_verification':sums,
                'comparisons':COMPARES,'numerical_checks':CHECKS,
                'bound_information_boundary':'No saved outcomes loaded into analytic functions; fingerprints written before outcome join. Not blinded to report.',
                'summary_method':'Recomputed summary tables/JSON from independently checked primitive submission rows. Ratios checked through native-unit products.',
                'scope':'Internal saved-profile mathematical/numerical review; no engine or actual-record D/F evaluation, RNG, raw states, source reconstruction, or repository writes.'}
        dump(out/'INDEPENDENT_REVIEW_RESULTS.json',result)
        print(json.dumps({'status':'PASS','counts':COUNTS,'direct':direct,'elapsed_seconds':result['elapsed_seconds']},indent=2))
    except Exception:
        dump(out/'REVIEW_FAILURE.json',{'status':'FAILED','utc':now(),'counts':COUNTS,'traceback':traceback.format_exc(),
                                       'checks_completed':len(CHECKS),'compares_completed':len(COMPARES)})
        raise

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--submission',required=True);ap.add_argument('--seal',required=True);ap.add_argument('--output',required=True)
    main(ap.parse_args())
