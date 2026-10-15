"""Pure pre-output analytic functions. No I/O, saved outcomes, RNG or evolution operator."""
import math
import numpy as np
FAMILIES=('OMEGA_COARSE','GAMMA_SOURCE','T_TRIANGLE','Q_VECTOR','K_COMPONENT','P_PROFILE','BEST_PRE')
def mean(x):return math.fsum(float(t) for t in x)/len(x)
def norm(x):return np.linalg.norm(x,axis=-1)
def profile(x):return np.sort(np.abs(x),axis=-1)
def k(s):
    b=1.0+np.log1p(s)
    return (b-s/(1.0+s))/(b*b)
def geometry(d,bit_plus):
    return (1.0-2.0*bit_plus[:,None])*d/(norm(d)[:,None]+0.01)
def vector_pair(v_c,a_c,w_c,v_d,a_d,w_d):
    dv=v_c-v_d;da=a_c-a_d;dw=w_c-w_d
    vn=norm(dv);an=norm(da);qn=norm(dw)
    contains=(np.minimum(w_c,w_d)<=0)&(np.maximum(w_c,w_d)>=0)
    ell=np.where(contains,0.0,np.minimum(np.abs(w_c),np.abs(w_d)))
    kap=k(ell);kn=norm(kap*dw)
    pc=profile(w_c);pd=profile(w_d);lam=k(np.minimum(pc,pd));pn=norm(lam*(pc-pd))
    cross=2*np.sum(dv*da,axis=-1)
    valid=(vn>0)&(an>0)
    cosine=np.full(8,np.nan,dtype=np.float64)
    np.divide(cross,2*vn*an,out=cosine,where=valid)
    Q=mean(qn);K=mean(kn);P=mean(pn);V=mean(vn);J=mean(an)
    pair={'T_TRIANGLE':V+J,'Q_VECTOR':Q,'K_COMPONENT':K,'P_PROFILE':P,'BEST_PRE':min(K,P),
        'V':V,'J':J,'best_is_K':K<=P,'T_minus_Q':V+J-Q}
    center={'delta_v':dv,'delta_a':da,'delta_w':dw,'v_distance':vn,'a_distance':an,
        'Q_center':qn,'K_center':kn,'P_center':pn,'T_center':vn+an,
        'difference_alignment':cross,'difference_cosine':cosine,'difference_cosine_valid':valid,
        'alignment_residual':qn*qn-vn*vn-an*an-cross,
        'triangle_slack':vn+an-qn,'contains_zero':contains,'ell':ell,'kappa':kap,'lambda':lam,
        'profile_c':pc,'profile_d':pd,'profile_distance':norm(pc-pd)}
    return pair,center
def source_pair(v_c,a_c,w_c,d_c,H_c,G_c,bit_plus_c,v_d,a_d,w_d,d_d,H_d,G_d,bit_plus_d):
    pair,center=vector_pair(v_c,a_c,w_c,v_d,a_d,w_d)
    gc=geometry(d_c,bit_plus_c);gd=geometry(d_d,bit_plus_d)
    Rg=mean(norm(gc-gd));q_c=mean(norm(gc));q_d=mean(norm(gd))
    h=abs(0.1*H_c);deltaG=abs(G_c-G_d);V=pair['V']
    gc_bound=V+h*(deltaG*q_c+G_d*Rg)
    gd_bound=V+h*(deltaG*q_d+G_c*Rg)
    pair.update(GAMMA_SOURCE=min(gc_bound,gd_bound),OMEGA_COARSE=(1+h)*V+h*min(G_c,G_d)*Rg,
        Gamma_c_given_d=gc_bound,Gamma_d_given_c=gd_bound,Rg=Rg,qbar_c=q_c,qbar_d=q_d,
        G_c=G_c,G_d=G_d,abs_delta_G=deltaG,H_c=H_c,H_d=H_d,h=h)
    center.update(g_c=gc,g_d=gd)
    return pair,center

