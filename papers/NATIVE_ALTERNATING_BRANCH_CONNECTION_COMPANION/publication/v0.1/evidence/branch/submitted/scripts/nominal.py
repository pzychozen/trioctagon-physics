"""Bounded root planning only. No trajectory or proof from residuals."""
from common import *
from model import *
import numpy as np,time
N=128;c=constants(False);accepted=read(S/'m2_accepted_certificate.json')['analytic_taylor_numerical_values']
x=np.array([float(v)/2 for v in accepted['w']]+[0.,float(accepted['c'])/float(accepted['sigma'])])
nodes=[F(0)]+[F(2*i+1,400*N) for i in range(N)]+[F(1,200)]
assert len(nodes)<=read(R/'FROZEN_PLAN.json')['nominal_budget']['maximum_root_solves']
results=[];started=now();tic=time.time()
def direct(z,mu):
    u=np.array(c['u']);V=np.array(c['V']);omega=u+z[:3]+1j*(V@z[3:])
    v=omega+c['ep']*omega*(np.array(c['k'])-abs(omega)**2)+c['g']*(sum(omega)-3*omega)
    phase=np.angle(v);delta=np.array([(c['lc']+mu)*sum(np.sin(3*(phase[j]-phase[i])) for j in range(3) if j!=i) for i in range(3)])
    out=v*np.exp(1j*delta);h=u@out;out*=np.conj(h)/abs(h)
    return np.r_[out.real-u,V.T@out.imag]
for n,mu in enumerate(nodes):
    history=[]
    for iteration in range(30):
        rr,m=regularized(list(x),float(mu),c)
        f=np.array([v.v for v in rr]);J=np.array([v.d for v in rr]);step=np.linalg.solve(J,-f)
        history.append({'iteration':iteration,'residual_infinity':float(max(abs(f))),'step_infinity':float(max(abs(step)))})
        x=x+step
        assert x[4]>0
        if max(abs(step))<2e-13:break
    else:raise RuntimeError('Nominal Newton budget exhausted')
    rr,m=regularized(list(x),float(mu),c);f=np.array([v.v for v in rr]);J=np.array([v.d for v in rr])
    z=np.array(reconstruct(list(x),float(mu),c));G=direct(z,float(mu))-z*np.array([1,1,1,-1,-1])
    results.append({'mu':str(mu),'x':[format(v,'.17g') for v in x],'inverse':[[format(v,'.17g') for v in row] for row in np.linalg.inv(J)],'regularized_residual_infinity':float(max(abs(f))),'original_G_residual_infinity':float(max(abs(G))),'state':[format(v,'.17g') for v in z],'iterations':history,'determinant':float(np.linalg.det(J))})
    if n%32==0 or n==len(nodes)-1:print(n,str(mu),'x',x.tolist(),'residual',max(abs(f)),flush=True)
result={'kind':'NOMINAL_PLANNING_NOT_A_CERTIFICATE','started_utc':started,'finished_utc':now(),'seconds':time.time()-tic,'patch_count':N,'root_solves':len(results),'newton_iterations':sum(len(r['iterations']) for r in results),'nodes':results,'critical_basis':c,'no_native_trajectory':True}
write(D/'NOMINAL_PLAN_128.json',result)
print('onset nu versus inherited c/sigma',results[0]['x'][4],float(accepted['c'])/float(accepted['sigma']))
print('endpoint state',results[-1]['state'],'seconds',time.time()-tic)
