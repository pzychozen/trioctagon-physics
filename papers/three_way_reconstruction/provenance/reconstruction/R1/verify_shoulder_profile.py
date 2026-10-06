"""Verify the authorized shoulder-profile follow-up. All writes are external."""
from pathlib import Path
import hashlib, json, subprocess
import sympy as sp
import mpmath as mp

ROOT=Path(__file__).resolve().parent
REPO=Path("C:/TORMENT/TRIOCTAGON_new/trioctagon-physics").resolve()
assert not ROOT.is_relative_to(REPO)
def status():
    return {k:subprocess.check_output(["git","-C",str(REPO),*args],text=True).strip()
            for k,args in [("head",["rev-parse","HEAD"]),("status",["status","--porcelain=v1"])]}
before=status()
h,s,y,t,L,d=sp.symbols("h s y t L d", nonzero=True)
fy=(L*y*y-L*y+1)/(y*y-L*y+L)
Q=-s+h+2*h*h*s+h**3*s*s
P=(s*s+2+2*h*s+h*h*s*s)/Q
W=-s-2/s
E=h*((3*s*s+2)+h*(3*s**3+4*s)+h*h*(s**4+2*s*s))/(s*Q)
H=(1+t)/(1-t)
R=(1-t)/(1-t+2*t/L+t*t/L**2)*(1+(t*t+2*t)/(2*L)+t*t/(2*L**2))
A=d+2/(L*d)
b=(d+2)/L
q=(1+d)**2/(L*d)
checks={
"exact_shoulder_substitution":(fy.subs({y:1+h*s,L:h**-2})+1)/h-P,
"exact_profile_error":P-W-E,
"first_correction":sp.limit((P-W)/h,h,0)+3+2/s**2,
"fixed_s_limit":sp.limit(P,h,0)-W,
"exact_bridge":fy.subs(y,1+d)+1+(A+b)/(1-q),
"exact_bulk_error":fy+y-(y**3+1)/(y*y-L*y+L),
"exact_lock_matching_ratio":(fy.subs(y,1+t/L)+1)/(H+1)-R,
"exact_stationary_derivative":sp.diff(P,s)-(1-h*h)*(2+2*h*s-s*s)/Q**2,
"limit_profile_derivative":sp.diff(W,s)-(-1+2/s**2),
}
for name,expression in checks.items():
    assert sp.cancel(expression)==0,name

def F(ell,x):
    return (ell*x**4-ell*x*x+1)/(x**4-ell*x*x+ell)
def PP(hh,ss):
    return (ss*ss+2+2*hh*ss+hh*hh*ss*ss)/(-ss+hh+2*hh*hh*ss+hh**3*ss*ss)
def WW(ss):
    return -ss-2/ss
def evaluate(dps):
    with mp.workdps(dps):
        points=[-mp.mpf(2),-mp.sqrt(2),-mp.mpf(1),-mp.mpf(1)/2,
                 mp.mpf(1)/2,mp.mpf(1),mp.sqrt(2),mp.mpf(2)]
        rows=[]; values=[]; max_identity=mp.mpf(0)
        for n in [10,100,1000,10000,10**6,10**12]:
            ell=mp.mpf(n); hh=1/mp.sqrt(ell)
            errors=[]; identities=[]
            for ss in points:
                direct=(F(ell,mp.sqrt(1+hh*ss))+1)/hh
                scaled=PP(hh,ss)
                identities.append(abs(direct-scaled)/max(1,abs(scaled)))
                errors.append(abs(scaled-WW(ss)))
                values.append(scaled)
            ratios={}
            for sign,label in [(1,"positive"),(-1,"negative")]:
                delta=sign*ell**(-mp.mpf(1)/4)
                fx=F(ell,mp.sqrt(1+delta))
                ratios["bulk_"+label+"_ratio"]=(fx+1)/(-delta)
                delta=sign*ell**(-mp.mpf(3)/4)
                tt=ell*delta
                fx=F(ell,mp.sqrt(1+delta))
                lock=(1+tt)/(1-tt)
                ratios["lock_"+label+"_ratio"]=(fx+1)/(lock+1)
            critical_ss=[hh-mp.sqrt(2+hh*hh),hh+mp.sqrt(2+hh*hh)]
            for ss in critical_ss:
                identities.append(abs(ss*ss-2*hh*ss-2))
            row={"L":n,"dps":dps,
                 "max_profile_sample_error":max(errors),
                 "sqrtL_max_profile_sample_error":max(errors)/hh,
                 "max_normalized_identity_residual":max(identities),**ratios}
            values.extend(ratios.values())
            rows.append({k:(mp.nstr(v,40) if isinstance(v,mp.mpf) else v) for k,v in row.items()})
            max_identity=max(max_identity,max(identities))
        return rows,values,max_identity
low,lv,lr=evaluate(120); high,hv,hr=evaluate(200)
with mp.workdps(210):
    change=max(abs(a-b)/max(1,abs(b)) for a,b in zip(lv,hv))
assert lr<mp.mpf("1e-95") and hr<mp.mpf("1e-175")
assert change<mp.mpf("1e-100")
after=status()
assert before==after
mp.mp.dps=120
result={"symbolic_checks_passed":list(checks),"precision_dps":[120,200],
        "sample_s":"-2,-sqrt(2),-1,-1/2,1/2,1,sqrt(2),2",
        "bulk_overlap_sequence":"delta=+/-L^(-1/4); ratio=(f+1)/(-delta)",
        "lock_overlap_sequence":"delta=+/-L^(-3/4); t=L*delta; ratio=(f+1)/(H(t)+1)",
        "largest_120_digit_identity_residual":mp.nstr(lr,40),
        "largest_200_digit_identity_residual":mp.nstr(hr,40),
        "max_120_vs_200_normalized_change":mp.nstr(change,40),
        "rows_120":low,"rows_200":high,"repository_before":before,
        "repository_after":after,"repository_unchanged":True,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions":{"sympy":sp.__version__,"mpmath":mp.__version__}}
(ROOT/"shoulder_verification_results.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({k:result[k] for k in ["symbolic_checks_passed","largest_120_digit_identity_residual",
"largest_200_digit_identity_residual","max_120_vs_200_normalized_change","rows_120","repository_unchanged"]},indent=2))
