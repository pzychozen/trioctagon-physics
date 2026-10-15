"""Exactly the supplied 14 synthetic groups; reference D is confined to this file."""
from common import *
import numpy as np,ast,inspect
from radial import evaluate,aggregate,hull,theta,variance_bounds,margin_class,ratio
np.seterr(all='raise')
records=[];counts={'fixture_groups':0,'fixture_cases':0,'pure_pair_calls':0,'D_array_calls':0,'D_scalar_components':0,'primary_calls':0}
def check(name,value,tol=1e-12,kind='equality'):
 a=np.asarray(value,dtype=float);need(np.all(np.isfinite(a)),'fixture nonfinite '+name)
 passed=bool(np.all(np.abs(a)<=tol)) if kind=='equality' else bool(np.all(a<=tol))
 records.append({'name':name,'kind':kind,'tolerance':tol,'min_signed':float(np.min(a)),'max_signed':float(np.max(a)),'max_abs':float(np.max(np.abs(a))),'PASS':passed})
 need(passed,'fixture failed '+name)
def truth(name,test):check(name,0. if test else 1.,0.)
def D(x):
 counts['D_array_calls']+=1;counts['D_scalar_components']+=x.size
 return x/(1+np.log1p(np.abs(x)))
def call(p,q,P):
 counts['pure_pair_calls']+=1
 return evaluate(p,q,P)
def profiles(v,w):
 p=np.sort(np.abs(v),axis=1);q=np.sort(np.abs(w),axis=1);s=np.minimum(p,q);b=1+np.log1p(s)
 P=np.linalg.norm(((b-s/(1+s))/(b*b))*(p-q),axis=1)
 return p,q,P
def fixed_case(g,case):
 tag=g+'/'+case['name'];counts['fixture_cases']+=1
 v=np.asarray(case['history_c_vectors'],dtype=float);w=np.asarray(case['history_d_vectors'],dtype=float)
 p,q,P=profiles(v,w);c,r=call(p,q,P);cr,rr=call(q,p,P)
 dp=D(p);dq=D(q);dv=D(v);dw=D(w)
 fp=np.linalg.norm(dp,axis=1);fq=np.linalg.norm(dq,axis=1);delta=fp-fq;S=abs(math.fsum(delta)/8)
 check(tag+'/symmetry_c',fp-np.linalg.norm(dv,axis=1));check(tag+'/symmetry_d',fq-np.linalg.norm(dw,axis=1))
 for lbl,lo,out,hi in [('p',c['L_p'],fp,c['U_p']),('q',c['L_q'],fq,c['U_q'])]:
  check(tag+'/norm_lower_'+lbl,lo-out,kind='inequality');check(tag+'/norm_upper_'+lbl,out-hi,kind='inequality')
 check(tag+'/theta_decreasing',np.diff(c['theta_nodes'],axis=-1),kind='inequality')
 truth(tag+'/five_node_shape',c['theta_nodes'].shape==(8,3,5))
 for J in (1,4):
  pref=f'J{J}_';exact=dp*dp-dq*dq
  check(tag+pref+'numerator_lower',c[pref+'component_num_lo']-exact,kind='inequality')
  check(tag+pref+'numerator_upper',exact-c[pref+'component_num_hi'],kind='inequality')
  for variant in ('raw_',''):
   check(tag+pref+variant+'center_lower',c[pref+variant+'lo']-delta,kind='inequality')
   check(tag+pref+variant+'center_upper',delta-c[pref+variant+'hi'],kind='inequality')
   check(tag+pref+variant+'reversal_lo',c[pref+variant+'lo']+cr[pref+variant+'hi'])
   check(tag+pref+variant+'reversal_hi',c[pref+variant+'hi']+cr[pref+variant+'lo'])
  check(tag+pref+'prior_lower',-P-c[pref+'lo'],kind='inequality');check(tag+pref+'prior_upper',c[pref+'hi']-P,kind='inequality')
  check(tag+pref+'pair_lower',r[pref+'signed_lower']-S,kind='inequality');check(tag+pref+'pair_upper',S-r[pref+'signed_upper'],kind='inequality')
  check(tag+pref+'signed_unsigned',r[pref+'signed_upper']-r[pref+'unsigned_upper'],kind='inequality')
  check(tag+pref+'unsigned_P',r[pref+'unsigned_upper']-r['P_PROFILE'],kind='inequality')
  for k in ('midpoint_identity_residual','unsigned_identity_residual','cancellation_identity_residual'):check(tag+pref+k,r[pref+k])
  z=c['h']==0
  if np.any(z):truth(tag+pref+'zero_component',np.all(c[pref+'component_num_lo'][z]==0)&np.all(c[pref+'component_num_hi'][z]==0))
 for variant in ('raw_',''):
  check(tag+variant+'nest_lower',c['J1_'+variant+'lo']-c['J4_'+variant+'lo'],kind='inequality')
  check(tag+variant+'nest_upper',c['J4_'+variant+'hi']-c['J1_'+variant+'hi'],kind='inequality')
 if g in ('F01','F02','F03'):
  for J in (1,4):truth(tag+f'/J{J}_exact_zero',np.all(c[f'J{J}_lo']==0)&np.all(c[f'J{J}_hi']==0))
 if g=='F04':truth(tag+'/one_zero_sign',np.all(c['J4_lo']>=0) if case['name']=='positive' else np.all(c['J4_hi']<=0))
 if g=='F05':truth(tag+'/resolved_sign',np.all(c['J4_lo']>1e-12) if case['name']=='larger components' else np.all(c['J4_hi']< -1e-12))
 if g=='F06':
  check(tag+'/equal_undamped_norm',np.linalg.norm(p,axis=1)-np.linalg.norm(q,axis=1));truth(tag+'/different_damped_norms',np.all(np.abs(delta)>1e-12))
 if g=='F07':truth(tag+'/signed_components_retained',np.any(c['h']>0)&np.any(c['h']<0))
 if g=='F08':
  check(tag+'/exact_cancellation',math.fsum(delta)/8);truth(tag+'/strict_unsigned_gain',r['J4_unsigned_upper']>r['J4_signed_upper'] and r['J4_unsigned_upper']>0)
 if g=='F09':truth(tag+'/partial_sign',math.fsum(delta)/8>1e-12 and r['J4_signed_lower']>1e-12)
 if g=='F11':truth(tag+'/theta_zero',float(theta(np.array(0.)))==1.)
 if g=='F14':
  witness={'external_outcome':delta.tolist()};finger=lambda d:hashlib.sha256(b''.join(np.asarray(d[k]).tobytes() for k in sorted(d))).hexdigest()
  h1=finger(c);witness['external_outcome']=[999.]*8;c2,r2=call(p,q,P);h2=finger(c2)
  truth(tag+'/outcome_isolation',h1==h2 and r==r2)
  save(ROOT/'evidence/OUTCOME_ISOLATION.json',{'status':'PASS','before':h1,'after':h2,'external_witness_replaced':True,'false_witness_containment_check':False})

def main():
 started=time.monotonic();preserved();need(load(ROOT/'evidence/INPUT_GATE.json')['status']=='PASS','input gate')
 groups=load(ROOT/'received/SIM05_FIXED_FIXTURES_v0.1.json')['groups'];need(len(groups)==14,'group count')
 save(ROOT/'evidence/MATHEMATICAL_GATE.json',{'status':'PASS','utc':utc(),'proof':ident(ROOT/'MATHEMATICAL_RESULTS.md'),
 'method':'Independent analytic differentiation, concavity/Jensen, signed interval and pair-variance proofs before fixed fixtures.','changed_formulas':0})
 for group in groups:
  g=group['id']
  for case in group.get('cases',[]):fixed_case(g,case)
  if g=='F12':
   for case in group['interval_cases']:
    x=np.asarray(case['centers'],dtype=float);r=aggregate(x[:,0],x[:,1])
    for key in ('midpoint_identity_residual','unsigned_identity_residual','cancellation_identity_residual'):check(g+'/'+case['name']+key,r[key])
    truth(g+'/zero_lower_equivalence/'+case['name'],(r['signed_lower']==0)==(r['lo']<=0<=r['hi']))
    check(g+'/signed_unsigned/'+case['name'],r['signed_upper']-r['unsigned_upper'],kind='inequality')
   l,h,f=hull(np.array([5e-13]),np.array([0.]));truth(g+'/small_inversion_outward',l[0]==0 and h[0]==5e-13 and f[0])
   try:hull(np.array([2e-12]),np.array([0.]));rejected=False
   except ArithmeticError:rejected=True
   truth(g+'/large_inversion_stop',rejected);truth(g+'/undefined_ratio',ratio(0.,0.,1e-12)==(None,False))
  if g=='F13':
   ps={};values={}
   for row in group['cycles']:
    v=np.asarray(row['vectors'],dtype=float);ps[row['cycle']]=np.sort(np.abs(v),axis=1)
    values[row['cycle']]=math.fsum(np.linalg.norm(D(v),axis=1))/8
   pairs={}
   for c in range(1,5):
    for d in range(c):
     p,q,P=profiles(ps[c],ps[d]);_,r=call(p,q,P);pairs[(c,d)]=r
   truth(g+'/ten_unique_pairs',len(pairs)==10)
   for view,cycles in group['views'].items():
    keys=[k for k in pairs if k[0] in cycles and k[1] in cycles];m=len(cycles)
    b=variance_bounds([pairs[k] for k in keys],m);u=np.array([values[c] for c in cycles]);var=float(np.mean((u-np.mean(u))**2))
    check(g+'/'+view+'/pair_variance',math.fsum((values[c]-values[d])**2 for c,d in keys)/(m*m)-var,1e-14)
    truth(g+'/'+view+'/pair_count',len(keys)==(10 if m==5 else 6))
    for J in (1,4):
     check(g+view+str(J)+'/var_lower',b[f'J{J}_variance_lower']-var,1e-14,'inequality')
     check(g+view+str(J)+'/var_upper',var-b[f'RADIAL_{J}_SIGNED_variance_upper'],1e-14,'inequality')
   truth(g+'/positive_margin',margin_class(2e-14)=='PASS');truth(g+'/negative_margin',margin_class(-2e-14)=='NOT_ESTABLISHED');truth(g+'/zero_margin',margin_class(0)=='UNRESOLVED')
  counts['fixture_groups']+=1
  update(ROOT/'evidence/FIXTURES_PROGRESS.json',{'utc':utc(),'counts':counts,'assertions':len(records),'last_group':g})
 # Inspect the pure module dependency boundary without importing historical code.
 tree=ast.parse(read(ROOT/'analyst/radial.py'))
 imports=[n.names[0].name for n in ast.walk(tree) if isinstance(n,ast.Import)]
 truth('pure_imports',imports==['math','numpy'])
 forbidden={'open','load','read','D','F','random','saved_successor_velocity','retention','post_norm','__import__','eval','exec'}
 truth('no_forbidden_pure_names',not any(isinstance(n,ast.Name) and n.id in forbidden for n in ast.walk(tree)))
 save(ROOT/'evidence/ALGEBRA_FIXTURES.json',{'status':'PASS','utc':utc(),'counts':counts,'assertions':len(records),'checks':records,'seconds':time.monotonic()-started,'D_on_source_records':0})
 names=['MATHEMATICAL_RESULTS.md']+[f'analyst/{n}.py' for n in ('common','radial','fixtures','analyze','summarize','supervise')]+[
  'received/'+n for n in ('SRG_SIM05_CODEX_WORK_ORDER_v0.1_20261014.md','SIM05_MATHEMATICAL_SPEC_v0.1.md','SIM05_EXPERIMENT_SPEC_v0.1.json','SIM05_FIXED_FIXTURES_v0.1.json','SIM05_INPUT_IDENTITIES_AND_SCHEMAS.json')]
 save(ROOT/'evidence/IMPLEMENTATION_GATE.json',{'status':'PASS','utc':utc(),'frozen_files':{n:ident(ROOT/n) for n in names},
 'pure_signature':str(inspect.signature(evaluate)),'allowed_pure_imports':imports,'forbidden_names_checked':sorted(forbidden),
 'fixture_groups':14,'fixture_assertions':len(records),'input_gate':ident(ROOT/'evidence/INPUT_GATE.json')})
 print(json.dumps({'status':'PASS','counts':counts,'assertions':len(records),'seconds':time.monotonic()-started}))
if __name__=='__main__':main()
