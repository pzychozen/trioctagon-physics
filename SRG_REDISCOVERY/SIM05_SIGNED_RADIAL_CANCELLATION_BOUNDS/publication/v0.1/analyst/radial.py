"""Pure SIM05 enclosures. Explicit profile/P inputs; no I/O, RNG, D/F or outcome dependency."""
import math
import numpy as np
FAMILIES=('P_PROFILE','RADIAL_1_UNSIGNED','RADIAL_1_SIGNED','RADIAL_4_UNSIGNED','RADIAL_4_SIGNED')
def avg(x):return math.fsum(float(v) for v in x)/len(x)
def theta(s):
 b=1+np.log1p(s)
 return (b-s/(1+s))/(b*b*b)
def hull(lo,hi):
 inv=lo-hi
 if np.any(inv>1e-12):raise ArithmeticError('substantive interval inversion')
 return np.minimum(lo,hi),np.maximum(lo,hi),inv>0
def norm_envelope(p):
 m=np.linalg.norm(p,axis=-1);M=np.max(p,axis=-1)
 if np.any((m==0)&np.any(p!=0,axis=-1)):raise ArithmeticError('norm underflow')
 return m/(1+np.log1p(M)),m/(1+np.log1p(m/np.sqrt(3.)))
def sign_class(lo,hi,flag):
 return np.where(flag,0,np.where(lo>1e-12,1,np.where(hi< -1e-12,-1,0)))
def aggregate(lo,hi):
 mid=(lo+hi)/2;radius=(hi-lo)/2
 l=avg(lo);r=avg(hi);mu=avg(mid);eps=avg(radius)
 signed=max(abs(l),abs(r));unsigned=avg(np.maximum(np.abs(lo),np.abs(hi)))
 lower=0. if l<=0<=r else min(abs(l),abs(r))
 return {'lo':l,'hi':r,'midpoint':mu,'mean_radius':eps,'mean_abs_midpoint':avg(np.abs(mid)),
 'signed_upper':signed,'unsigned_upper':unsigned,'signed_lower':lower,'cancellation':unsigned-signed,
 'midpoint_identity_residual':signed-(abs(mu)+eps),
 'unsigned_identity_residual':unsigned-(avg(np.abs(mid))+eps),
 'cancellation_identity_residual':unsigned-signed-(avg(np.abs(mid))-abs(mu))}
def evaluate(p,q,prior):
 if p.shape!=(8,3) or q.shape!=(8,3) or prior.shape!=(8,):raise ValueError('profile/P shapes')
 if not all(np.all(np.isfinite(x)) for x in (p,q,prior)):raise ValueError('nonfinite input')
 if np.any(p<0) or np.any(q<0) or np.any(prior<0):raise ValueError('negative profile/P')
 if np.any(np.diff(p,axis=1)<0) or np.any(np.diff(q,axis=1)<0):raise ValueError('unsorted profile')
 x=p*p;y=q*q;h=(p-q)*(p+q)
 zlo=np.minimum(x,y);zhi=np.maximum(x,y)
 nodes=zlo[...,None]+(zhi-zlo)[...,None]*np.array([0.,.25,.5,.75,1.])
 weights=theta(np.sqrt(nodes))
 Lp,Up=norm_envelope(p);Lq,Uq=norm_envelope(q)
 dlo=Lp+Lq;dhi=Up+Uq;bothzero=np.all(p==0,axis=1)&np.all(q==0,axis=1)
 if np.any((~bothzero)&(dlo<=0)):raise ArithmeticError('nonpositive denominator')
 if np.any(dlo>dhi+1e-12):raise ArithmeticError('denominator inversion')
 c={'profile_c':p,'profile_d':q,'P_center':prior,'x':x,'y':y,'h':h,'h_residual':h-(x-y),
 'nodes_z':nodes,'theta_nodes':weights,'L_p':Lp,'U_p':Up,'L_q':Lq,'U_q':Uq,
 'denominator_lo':dlo,'denominator_hi':dhi,'norm_difference_lo':Lp-Uq,'norm_difference_hi':Up-Lq,
 'both_zero':bothzero}
 pair={'P_PROFILE':avg(prior)}
 for J in (1,4):
  pref=f'J{J}_'
  tl=weights[...,4] if J==1 else np.mean(weights[...,1:],axis=-1)
  th=weights[...,0] if J==1 else np.mean(weights[...,:4],axis=-1)
  a=h*tl;b=h*th;cl=np.minimum(a,b);ch=np.maximum(a,b)
  nl=np.array([math.fsum(row) for row in cl]);nh=np.array([math.fsum(row) for row in ch])
  qs=np.zeros((8,4))
  for j,(nn,dd) in enumerate(((nl,dlo),(nl,dhi),(nh,dlo),(nh,dhi))):np.divide(nn,dd,out=qs[:,j],where=~bothzero)
  ql=np.min(qs,axis=1);qh=np.max(qs,axis=1)
  rawl0=np.maximum(ql,Lp-Uq);rawh0=np.minimum(qh,Up-Lq)
  rawl,rawh,rawflag=hull(rawl0,rawh0)
  l0=np.maximum(rawl,-prior);r0=np.minimum(rawh,prior)
  l,r,effflag=hull(l0,r0);flag=rawflag|effflag
  vals={'theta_lo':tl,'theta_hi':th,'component_num_lo':cl,'component_num_hi':ch,
    'numerator_lo':nl,'numerator_hi':nh,'four_quotients':qs,'quotient_lo':ql,'quotient_hi':qh,
    'raw_lo_original':rawl0,'raw_hi_original':rawh0,'raw_lo':rawl,'raw_hi':rawh,'raw_hull_flag':rawflag,
    'raw_lo_from_quotient':ql>=Lp-Uq,'raw_hi_from_quotient':qh<=Up-Lq,
    'effective_lo_original':l0,'effective_hi_original':r0,'lo':l,'hi':r,'effective_hull_flag':effflag,
    'roundoff_flag':flag,'P_active_lo':-prior>rawl,'P_active_hi':prior<rawh,
    'P_tie_lo':-prior==rawl,'P_tie_hi':prior==rawh,
    'midpoint':(l+r)/2,'radius':(r-l)/2,'sign':sign_class(l,r,flag),
    'raw_midpoint':(rawl+rawh)/2,'raw_radius':(rawh-rawl)/2,
    'raw_sign':sign_class(rawl,rawh,rawflag)}
  c.update({pref+k:v for k,v in vals.items()})
  ag=aggregate(l,r);rawag=aggregate(rawl,rawh)
  pair.update({pref+k:v for k,v in ag.items()});pair.update({pref+'raw_'+k:v for k,v in rawag.items()})
  signs=vals['sign'];pair.update({pref+'positive_centers':int(np.sum(signs==1)),pref+'negative_centers':int(np.sum(signs==-1)),
   pref+'unresolved_centers':int(np.sum(signs==0)),pref+'mixed_resolved_signs':bool(np.any(signs==1)&np.any(signs==-1)),
   pref+'collective_sign':int(sign_class(np.array(ag['lo']),np.array(ag['hi']),np.array(np.any(flag)))),
   pref+'roundoff_centers':int(np.sum(flag)),pref+'prior_active_centers':int(np.sum(vals['P_active_lo']|vals['P_active_hi'])),
   pref+'raw_to_effective_unsigned':rawag['unsigned_upper']-ag['unsigned_upper'],
   pref+'raw_to_effective_signed':rawag['signed_upper']-ag['signed_upper'],
   f'RADIAL_{J}_UNSIGNED':ag['unsigned_upper'],f'RADIAL_{J}_SIGNED':ag['signed_upper']})
 if not all(np.all(np.isfinite(v)) for v in c.values()):raise ArithmeticError('nonfinite analytic output')
 return c,pair
def variance_bounds(rows,m):
 r={f+'_variance_upper':math.fsum(x[f]**2 for x in rows)/(m*m) for f in FAMILIES}
 for J in (1,4):
  r[f'J{J}_variance_lower']=math.fsum(x[f'J{J}_signed_lower']**2 for x in rows)/(m*m)
  for kind in ('signed','unsigned'):
   r[f'J{J}_raw_{kind}_variance_upper']=math.fsum(x[f'J{J}_raw_{kind}_upper']**2 for x in rows)/(m*m)
 return r
def margin_class(x):return 'PASS' if x>1e-14 else 'NOT_ESTABLISHED' if x< -1e-14 else 'UNRESOLVED'
def ratio(a,b,floor):return (a/b,True) if b>=floor else (None,False)
