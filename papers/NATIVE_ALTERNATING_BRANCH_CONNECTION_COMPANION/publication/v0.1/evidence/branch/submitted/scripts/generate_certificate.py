from common import *
from validation import *
import time
nom=read(D/'NOMINAL_PLAN_128.json');N=nom['patch_count'];c=constants(True)
radii=['0.0005','0.0005','0.0006','0.001','0.0001']
started=now();tic=time.time();patches=[];joins=[]
for i in range(N):
    node=nom['nodes'][i+1]
    p=validate_box(node['x'],radii,node['inverse'],[str(F(i,200*N)),str(F(i+1,200*N))],c)
    p['id']=i;patches.append(p)
    if not p['passed']:
        write(D/'FAILED_FULL_VALIDATION_01.json',{'patches':patches,'failed_patch':i});raise AssertionError('Patch failed')
    if i%32==0:print('validated patch',i,'q',p['q_display'],flush=True)
for i in range(N-1):
    left,right=patches[i:i+2]
    hull=[[min(F(left['state_box'][j][0]),F(right['state_box'][j][0])),max(F(left['state_box'][j][1]),F(right['state_box'][j][1]))] for j in range(5)]
    center=[str((a+b)/2) for a,b in hull];rad=[str((b-a)/2) for a,b in hull]
    join=validate_box(center,rad,left['A'],[left['mu'][1],left['mu'][1]],c)
    join['left']=i;join['right']=i+1
    # Shared uniqueness needs contraction on a convex box containing both roots;
    # it does not rely on overlapping boxes or this connector's self-inclusion.
    join['shared_uniqueness_pass']=join['q_display']<1 and join['regularity_positive']
    joins.append(join)
    if not join['shared_uniqueness_pass']:
        write(D/'FAILED_FULL_VALIDATION_01.json',{'patches':patches,'joins':joins,'failed_join':i});raise AssertionError('Join failed')
    if i%32==0:print('validated shared uniqueness',i,'q',join['q_display'],flush=True)
special={}
for key,node,parent in [('onset',nom['nodes'][0],patches[0]),('endpoint',nom['nodes'][-1],patches[-1])]:
    result=validate_box(node['x'],['0.0000000001']*5,node['inverse'],[node['mu'],node['mu']],c)
    assert result['passed']
    result['parent_patch']=parent['id']
    result['box_inside_parent']=all(F(parent['state_box'][i][0])<F(result['state_box'][i][0]) and F(result['state_box'][i][1])<F(parent['state_box'][i][1]) for i in range(5))
    assert result['box_inside_parent']
    special[key]=result
endpoint_box=[IV.bounds(*map(F,row)) for row in special['endpoint']['root_enclosure']]
z=reconstruct(endpoint_box,IV.make(F(1,200)),c)
up=read(S/'m3_accepted_support.json')['values']['exact_receipts']['Up']
inclusion=all(F(a)<F(v.lo,SCALE) and F(v.hi,SCALE)<F(b) for v,(a,b) in zip(z,up))
assert inclusion,'Continued endpoint not certified in exact Up'
special['endpoint']['quotient_enclosure']=serial(z)
special['endpoint']['Up']=up
special['endpoint']['parity']='positive e^T eta; direct Up, no H swap'
special['endpoint']['strict_inside_exact_Up']=inclusion
result={'task':'NATIVE_ALTERNATING_BRANCH_CONNECTION_01','status':'CERTIFIED_CONNECTION_CANDIDATE_FOR_REVIEW','started_utc':started,'finished_utc':now(),'elapsed_seconds':time.time()-tic,'interval_bits':BITS,'mu_coverage':['0','1/200'],'zero_is_anchor_only':True,'chart':'t=mu/nu; xi=t X; eta=sqrt(t)(e+t y e_perp)','root_nontriviality':'For mu>0, nu>0 and e^T eta=sqrt(mu/nu)>0','inputs':read(L/'INPUT_IDENTITIES.json'),'constants':serial(c),'patches':patches,'joins':joins,**special,'stability':'Separate assessment; root contraction is not dynamical stability','implementation_identities':{p.name:sha(p.read_bytes()) for p in (R/'scripts').glob('*.py')}}
write(D/'CONNECTION_CERTIFICATE.json',result)
print(json.dumps({'status':result['status'],'patches':len(patches),'joins':len(joins),'max_patch_q':max(p['q_display'] for p in patches),'max_join_q':max(p['q_display'] for p in joins),'endpoint_in_Up':inclusion,'elapsed_seconds':time.time()-tic},indent=2))
