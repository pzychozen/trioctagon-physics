"""New source-derived budget arithmetic, not an engine or trajectory operator."""
from common import *
import numpy as np

def budget(v,a):
    """Nine-fixture-tested center ledger. No geometry, position or RNG update."""
    w=v.copy();w+=a
    ell=np.log1p(np.abs(w));z=w/(1+ell)
    r=float(np.linalg.norm(v));m=float(np.linalg.norm(w));t=float(np.linalg.norm(z))
    v2=float(np.dot(v,v));w2=float(np.dot(w,w));z2=float(np.dot(z,z))
    an=float(np.linalg.norm(a));I=float(np.dot(a,a));A=float(2*np.dot(v,a))
    Ldirect=w2-z2
    L=float(np.sum(w*w*(ell*(2+ell)/(1+ell)**2)))
    den=m+r
    if den>0:B=I/den;C=A/den
    else:
        need(np.all(v==0) and np.all(a==0) and I==A==0,'zero m+r inconsistent with vectors/numerators')
        B=C=0.
    R=m-t
    if m+t>0:Rstable=L/(m+t)
    else:
        need(np.all(w==0) and np.all(z==0) and L==0,'zero m+t inconsistent with vectors/loss')
        Rstable=0.
    cv=r>0 and an>0
    if cv:
        need(r*an>0,'alignment denominator underflow')
        cosine=float(np.dot(v,a)/(r*an))
    else:cosine=np.nan
    rv=m>0
    if rv:
        need(w2*w2>0,'concentration denominator underflow')
        retention=t/m;chi=float(np.sum(w**4)/(w2*w2))
    else:retention=chi=np.nan
    return dict(w=w,z=z,r=r,m=m,t=t,v2=v2,w2=w2,z2=z2,impulse_norm=an,
        I=I,A=A,L=L,L_direct=Ldirect,L_stable_minus_direct=L-Ldirect,
        B=B,C=C,R=R,R_stable=Rstable,R_stable_minus_direct=Rstable-R,
        cosine=cosine,cosine_valid=cv,retention=retention,retention_valid=rv,
        chi=chi,chi_valid=rv,budget_zero_denominator=den==0,damping_zero_denominator=m+t==0,
        square_internal_residual=(z2-v2)-(I+A-L),
        square_direct_internal_residual=(z2-v2)-(I+A-Ldirect),
        speed_internal_residual=(t-r)-(B+C-R),
        speed_stable_internal_residual=(t-r)-(B+C-Rstable))

def run_tests():
    need(not (ROOT/'evidence/ALGEBRA_GATE.json').exists(),'algebra gate already recorded')
    cases=spec()['algebra_fixtures'];need(len(cases)==9,'nine fixtures')
    results=[]
    for case in cases:
        v=np.asarray(case['v'],dtype=np.float64);a=np.asarray(case['impulse'],dtype=np.float64)
        b=budget(v,a)
        for k in ['square_internal_residual','square_direct_internal_residual','speed_internal_residual',
                  'speed_stable_internal_residual','L_stable_minus_direct','R_stable_minus_direct']:
            need(abs(b[k])<=1e-12,case['name']+' '+k)
        need(b['I']>=0 and b['L']>=0 and b['L_direct']>=-1e-12 and b['R']>=-1e-12,'fixture nonnegativity')
        # An independent norm subtraction checks the net forcing terms.
        need(abs((b['m']-b['r'])-(b['B']+b['C']))<=1e-12,'fixture forcing speed')
        if b['cosine_valid']:need(abs(b['cosine'])<=1+1e-12,'fixture angle')
        if b['chi_valid']:need(1/3-1e-12<=b['chi']<=1+1e-12,'fixture concentration')
        results.append({'fixture':case,'results':{k:(x.tolist() if isinstance(x,np.ndarray) else (None if isinstance(x,float) and not math.isfinite(x) else x)) for k,x in b.items()}})
    need(results[0]['results']['I']==results[0]['results']['B']==results[0]['results']['C']==results[0]['results']['R']==0,'zero fixture')
    need(results[5]['results']['m']==0 and results[5]['results']['C']==-2,'exact cancellation fixture')
    need(results[4]['results']['A']<0 and results[3]['results']['A']>0,'signed alignment fixtures')
    s=np.array([0.,1e-12,.1,1.,10.]);ell=np.log1p(s)
    derivative=(1+ell-s/(1+s))/(1+ell)**2
    need(np.all((derivative>0)&(derivative<=1)) and derivative[0]==1,'damping derivative check')
    axis=np.array([1.,0.,0.]);equal=np.ones(3)/np.sqrt(3.)
    da=axis/(1+np.log1p(abs(axis)));de=equal/(1+np.log1p(abs(equal)))
    need(abs(np.linalg.norm(axis)-np.linalg.norm(equal))<=1e-12 and np.linalg.norm(de)>np.linalg.norm(da),'orientation example')
    need(np.linalg.norm(da-de)<=np.linalg.norm(axis-equal)+1e-12,'damping fixed-vector bound')
    gain=[]
    for u,v in [(0.,0.),(0.,1.),(.01,.4),(1.,10.)]:
        lhs=abs(1/(1+u)-1/(1+v));rhs=abs(u-v)/((1+u)*(1+v))
        need(abs(lhs-rhs)<=1e-12 and lhs<=abs(u-v)+1e-12,'gain identity')
        gain.append({'u':u,'other_u':v,'lhs':lhs,'rhs':rhs})
    # Deterministic schema and mixed-position assembly check (not a trajectory).
    p=np.arange(24,dtype=np.float64).reshape(8,3);q=p+100;p.setflags(write=False);q.setflags(write=False)
    mixed=p.copy();mixed[:3]=q[:3]
    need(np.array_equal(mixed[:3],q[:3]) and np.array_equal(mixed[3:],p[3:]) and not p.flags.writeable,'mixed saved geometry fixture')
    payload={'status':'PASS','utc':utc(),'nine_algebra_fixtures':results,'derivative_samples':derivative.tolist(),
        'orientation_example_r':1.,'axis_post_norm':float(np.linalg.norm(da)),'equal_components_post_norm':float(np.linalg.norm(de)),
        'gain_checks':gain,'deterministic_schema_fixture':True,'saved_trajectory_records_used':0,'engine_calls':0,'RNG_samples':0,
        'note':'Fixed mathematical/schema fixtures; not observations from C or scientific rollout calls.'}
    save(ROOT/'evidence/ALGEBRA_GATE.json',payload,True)
    print(json.dumps({'algebra_gate':'PASS','fixed_budget_fixtures':9,'saved_records_used':0}),flush=True)

if __name__=='__main__':run_tests()
