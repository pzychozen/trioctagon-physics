"""Actual quotient derivative for a separate stability assessment.
Direct original cubic prestage; harmonic identity and real positive gauge.
No divided-system derivative is used as a dynamical multiplier.
"""
from common import *
from model import *
from validation import serial,intervals
import numpy as np,time
def direct_quotient(z,mu,c):
    zz=[AD(v,[v*0+int(i==j) for j in range(5)]) for i,v in enumerate(z)]
    x=[c['u'][i]+zz[i] for i in range(3)];y=mv(c['V'],zz[3:])
    pr=[];pi=[]
    for i in range(3):
        factor=1+c['ep']*(c['k'][i]-x[i]**2-y[i]**2)
        pr.append(factor*x[i]+c['g']*(sum(x)-3*x[i]))
        pi.append(factor*y[i]+c['g']*(sum(y)-3*y[i]))
    rad=[sqrt(pr[i]**2+pi[i]**2) for i in range(3)]
    outR=[];outI=[]
    for i in range(3):
        terms=[]
        for j in range(3):
            if i==j:continue
            a=pr[j]*pr[i]+pi[j]*pi[i];b=pi[j]*pr[i]-pr[j]*pi[i]
            terms.append((3*a*a*b-b**3)/(rad[i]**3*rad[j]**3))
        delta=(c['lc']+mu)*sum(terms);w=delta**2
        co=1+w*entire_tail(w,'C');si=delta*(1+w*entire_tail(w,'S'))
        outR.append(pr[i]*co-pi[i]*si);outI.append(pr[i]*si+pi[i]*co)
    hr=dot(c['u'],outR);hi=dot(c['u'],outI);den=sqrt(hr**2+hi**2)
    real=[(outR[i]*hr+outI[i]*hi)/den for i in range(3)]
    imag=[(outI[i]*hr-outR[i]*hi)/den for i in range(3)]
    result=[real[i]-c['u'][i] for i in range(3)]+mv(tr(c['V']),imag)
    return result,{'prestage_radii':[r.v for r in rad],'gauge_modulus':den.v,'slice':dot(c['u'],[v.v for v in x])}
def infnorm(M):return max(sum(F(v.absup(),SCALE) for v in row) for row in M)
def assess(p,node,c,cn):
    mu=IV.bounds(*map(F,p['mu']));xs=[IV.bounds(*map(F,row)) for row in p['state_box']]
    zs=reconstruct(xs,mu,c)
    image,margin=direct_quotient(zs,mu,c);J=[v.d for v in image]
    M=[[v*(1 if i<3 else -1) for v in row] for i,row in enumerate(J)];P2=mm(M,M)
    zn=[float(v) for v in node['state']];mn=float(F(node['mu']))
    nom,_=direct_quotient(zn,mn,cn)
    Jn=np.array([v.d for v in nom]);Mn=np.diag([1,1,1,-1,-1])@Jn;Pn=Mn@Mn
    eigen,Q=np.linalg.eig(Pn)
    if np.max(abs(np.imag(Q)))>1e-10:raise RuntimeError('Complex nominal eigenbasis: no planned certificate')
    Q=np.real(Q);Rinv=np.linalg.inv(Q)
    qs=[[format(v,'.17g') for v in row] for row in Q];rs=[[format(v,'.17g') for v in row] for row in Rinv]
    Qiv=[intervals(row) for row in qs];Riv=[intervals(row) for row in rs]
    E=[[int(i==j)-v for j,v in enumerate(row)] for i,row in enumerate(mm(Riv,Qiv))]
    defect=infnorm(E);assert defect<1
    sim=mm(mm(Riv,P2),Qiv);bound=infnorm(sim)/(1-defect)
    regular=all(v.lo>0 for v in [*margin['prestage_radii'],margin['gauge_modulus'],margin['slice']])
    return {'patch':p['id'],'mu':p['mu'],'quotient_box':serial(zs),'D_Fhat':serial(J),'P_two_step':serial(P2),'Q':qs,'approximate_Q_inverse':rs,'inverse_defect':str(defect),'transformed_matrix':serial(sim),'norm_upper':str(bound),'norm_display':float(bound),'certified_attracting':bool(bound<1 and regular),'direct_map_regularity':serial(margin),'nominal_eigenvalues':list(map(float,np.real(eigen))),'nominal_is_not_proof':True}
if __name__=='__main__':
    cert=read(D/'CONNECTION_CERTIFICATE.json');nom=read(D/'NOMINAL_PLAN_128.json');c=constants(True);cn=constants(False);results=[];tic=time.time()
    for p,node in zip(cert['patches'],nom['nodes'][1:-1]):
        row=assess(p,node,c,cn);results.append(row)
        if p['id']%32==0:print('two-step stability patch',p['id'],'bound',row['norm_display'],'proved',row['certified_attracting'],flush=True)
    passed=[r['patch'] for r in results if r['certified_attracting']]
    result={'status':'SEPARATE_STABILITY_ASSESSMENT','checked_utc':now(),'elapsed_seconds':time.time()-tic,'theorem':'At a symmetric root P=D_Fhat(Hz)D_Fhat(z)=(H D_Fhat(z))^2. A fixed rational Q is nonsingular by ||I-RQ||<1. The bound ||R P Q||/(1-||I-RQ||)<1 certifies local quotient attraction.','shared_engine':'New direct quotient AD uses the same dyadic interval and entire-trigonometric helpers as the continuation; not an independent interval engine','inherited_near_onset':'M2 local attraction for sufficiently small mu; no explicit range imported','inherited_endpoint':'M3 exact endpoint trapping and two-step contraction unchanged','certified_patch_ids':passed,'inconclusive_patch_ids':[r['patch'] for r in results if not r['certified_attracting']],'rows':results}
    write(D/'STABILITY_CERTIFICATE.json',result)
    print('certified',len(passed),'of',len(results),'first',passed[0] if passed else None,'last',passed[-1] if passed else None,'seconds',time.time()-tic)
