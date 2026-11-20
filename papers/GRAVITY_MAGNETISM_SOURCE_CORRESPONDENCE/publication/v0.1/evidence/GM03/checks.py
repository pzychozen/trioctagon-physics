"""GM03 exact consequences and measurement identifiability, not physical data."""
from pathlib import Path
import hashlib,json,platform,sys
import sympy as sp
ROOT=Path(__file__).resolve().parent
R=sp.Rational
checks=[]
def zero(name,value,scope):
    vals=list(value) if isinstance(value,sp.MatrixBase) else [value]
    vals=[sp.simplify(sp.expand(v)) for v in vals]
    assert all(v==0 for v in vals),(name,vals)
    checks.append(dict(id=name,kind="exact_identity",pass_check=True,scope=scope))
def yes(name,value,scope):
    assert bool(value),name
    checks.append(dict(id=name,kind="exact_predicate",pass_check=True,scope=scope))
def imul(a,b):
    c=[x*y for x in a for y in b];return min(c),max(c)
def iadd(a,b):return a[0]+b[0],a[1]+b[1]
def ineg(a):return -a[1],-a[0]
def isub(a,b):return iadd(a,ineg(b))
def idiv(a,b):
    assert not b[0]<=0<=b[1]
    return imul(a,(1/b[1],1/b[0]))
def interval(poly,var,bounds):
    result=(R(0),R(0))
    for c in sp.Poly(poly,var).all_coeffs():
        assert c.is_Rational
        result=iadd(imul(result,bounds),(c,c))
    return result
def fmt_bounds(v):
    return dict(lo=str(v[0]),hi=str(v[1]),decimal_lo=str(sp.N(v[0],22)),decimal_hi=str(sp.N(v[1],22)))
def bisect(poly,s,lo=R(1,2),hi=R(3,2)):
    p=sp.Poly(poly,s)
    assert p.eval(lo)<0<p.eval(hi)
    for _ in range(100):
        mid=(lo+hi)/2
        if p.eval(mid)<0:lo=mid
        else:hi=mid
    return lo,hi

def main():
    old=json.loads((ROOT/"inputs/CHECK_RESULTS.json").read_text())
    oldcases={x["case"]:x for x in old["certified_examples"]}
    source_brackets={}
    for label,row in oldcases.items():
        p=sp.sympify(row["polynomial"])
        var=next(iter(p.free_symbols))
        lo,hi=R(row["lo"]),R(row["hi"])
        yes("T01_"+label,p.subs(var,lo)<0<p.subs(var,hi) and hi-lo==R(1,2**100),
            "Recheck stored rational signs and widths, without replaying the accepted GM02 suite.")
        source_brackets[label]=(lo,hi)
    s,t1,t2,z=sp.symbols("s t1 t2 z",real=True)
    a=R(1,10000);t=R(1,20)
    I=3*(1-t*s)**2+2*a*a*s*s
    W=sp.Matrix([sp.sqrt(3)*a*a*s*s/2,3*a*s*(1-t*s)/2,0])
    w=W.subs(s,1);w2=sp.simplify(w.dot(w))
    Cg=sp.expand(9-I**2)
    CgF=Cg.subs(s,1)
    a0,b0=R(1,100),R(10**6)
    xi=sp.cancel(a0*CgF/(b0*w2))
    cstar=sp.cancel((1+xi)/3)
    rstar=sp.sqrt(2/xi)
    angle=sp.acos(sp.sqrt(cstar))*180/sp.pi
    yes("T02_neutral_interior",0<xi<2 and R(1,3)<cstar<1,"Interior benchmark neutral angle.")
    zero("T03_neutral_angle",a0*CgF+b0*w2*(1-3*cstar),"Unloaded endpoint criterion only.")
    zero("T04_neutral_distance",a0*CgF/rstar-2*b0*w2/rstar**3,"Fixed parameters: loads scale as inverse distance and inverse distance cubed.")
    yes("T05_distance_certification",rstar>1 and 4*xi>2,"Critical distance and held-out 2r0 remain at or above r0; all angles slow at 2r0.")
    yes("T06_reported_rounding",abs(sp.N(angle,50)-R("38.79941498"))<R(1,200000000)
        and abs(sp.N(rstar,50)-R("1.55971045"))<R(1,200000000),
        "High precision decimal corroboration; exact formulas define the locus.")

    n=sp.Matrix(sp.symbols("n0:3",real=True));norm2=n.dot(n)
    Q=sp.eye(3)-3*n*n.T/norm2
    zero("T07_direction_uniformity",Q*n+2*n,"Axial eigenvalue -2 for every nonzero center direction; orthogonal subspace eigenvalue +1.")
    zero("T08_tensor_square",Q*Q-sp.eye(3)-3*n*n.T/norm2,"Spectral norm 2, hence the GM02 bound covers all directions.")
    Qpar=sp.eye(3)-3*w*w.T/w2
    Qperp=sp.diag(1,1,-2)
    # Scan plane span(w,e_z). Only cos^2(theta) enters this polynomial.
    Qneutral=sp.eye(3)-3*cstar*w*w.T/w2
    def magnetic(polyQ):
        return sp.expand((W.subs(s,t1).T*polyQ*W.subs(s,t2))[0])
    def pair(polyQ,aa,bb):
        return sp.expand(-aa*I.subs(s,t1)*I.subs(s,t2)+bb*magnetic(polyQ))
    def residual(P):
        Pdiag=P.subs({t1:s,t2:s})
        delta=sp.expand(Pdiag-P.subs({t1:0,t2:0}))
        return sp.cancel(s-1+delta/(4*s)),delta,Pdiag
    Pneutral=pair(Qneutral,a0,b0)
    rn,dn,_=residual(Pneutral)
    zero("T09_neutral_loaded_root",rn.subs(s,1),"Unique certified root is exactly s=1; Qneutral is its restriction to the W plane.")
    # The discarded e_z cross terms vanish for these planar W vectors.
    ct=sp.symbols("c",real=True)
    nscan=sp.sqrt(ct)*w/sp.sqrt(w2)+sp.sqrt(1-ct)*sp.Matrix([0,0,1])
    zero("T10_scan_plane_restriction",magnetic(sp.eye(3)-3*nscan*nscan.T)-
         magnetic(sp.eye(3)-3*ct*w*w.T/w2),"All path W lie in the body plane; a full physical n is specified for the scan.")

    loaded={}
    for label,qmat in [("parallel",Qpar),("transverse",Qperp)]:
        P=pair(qmat,a0,b0);r,delta,Pdiag=residual(P)
        bracket=source_brackets["magnetic_"+label]
        yes("T11_"+label+"_same_polynomial",r.subs(s,bracket[0])<0<r.subs(s,bracket[1]),"Independently construct the residual and enclose its root in the GM02 bracket.")
        hm=(2*bracket[0]-1,2*bracket[1]-1)
        hmid=sum(hm)/2
        loaded[label]=dict(s_bracket=fmt_bounds(bracket),next_off_bracket=fmt_bounds(hm),
            s_mid=str(sp.N(sum(bracket)/2,24)),next_off_mid=str(sp.N(hmid,24)),
            switching_work_over_S=fmt_bounds(ineg(interval(Pdiag,s,bracket))))
        desired=R("1.012072433686") if label=="parallel" else R("0.981577610351")
        yes("T12_"+label+"_next_rounding",abs(sp.N(hmid,40)-desired)<R(1,2*10**12),"Published 12-decimal next-step multiplier.")
        # eta=1, U measured in S for this dimensionless benchmark.
        sest=idiv(ineg(interval(delta,s,bracket)),interval(4*s*(s-1),s,bracket))
        yes("T13_"+label+"_store_scale",sest[0]<=1<=sest[1],"In-model consistency only; does not replace independently measured work.")
        loaded[label]["in_model_S_over_eta_fit"]=fmt_bounds(sest)
        ph=pair(qmat,a0/2,b0/8);rh,dh,_=residual(ph)
        hb=bisect(rh,s)
        loaded[label]["heldout_2r0"]=dict(s_bracket=fmt_bounds(hb),
            s_mid=str(sp.N(sum(hb)/2,24)),polynomial=str(rh))
        yes("T14_"+label+"_heldout_slows",hb[1]<1,"Held-out geometry prediction using unchanged source/storage scales.")
    zero("T15_switch_off_doubling",(2*s-1)-1-2*(s-1),"Exact multiplier relation.")
    zero("T16_neutral_off_control",(2*s-1).subs(s,1)-1,"No induced store difference at the neutral preparation.")
    h=sp.symbols("h",real=True)
    zero("T17_fixed_state_control",h*sp.zeros(6,1),"d=0 prevents a displacement-based identification of h.")

    # Nonzero second native direction, without assuming phase kicks remain zero.
    min_a=1-(t+a)*R(3,2)
    yes("T18_modulus_annulus",min_a>R(9,10),"For all s in [1/2,3/2], each input modulus is between 0.9 and 1.")
    low_rho=R(19,20)+R(1,10)*(R(999,1000)-1)
    high_rho=R(19,20)+R(1,10)*(R(1001,1000)-R(9,10)**2)
    coupling_bound=R(1,60)*3*a
    gap=(1-high_rho)*R(9,10)-coupling_bound
    prelower=low_rho*R(9,10)-coupling_bound
    zero("T19_native_gap_constant",gap-R(5561,200000),"Every second prestage modulus is at least this much below its input modulus.")
    yes("T20_regular_second_prestage",prelower>0 and gap>0,"Second prestages are nonzero; synchronization preserves their strict modulus deficit.")
    omega=-R(1,2)-sp.I*sp.sqrt(3)/2
    q=sp.Matrix([1,omega,omega**2])
    qpath=sp.diag(1-(t+a)*s,1-t*s,1-(t-a)*s)*q
    zero("T21_sum_bound_identity",sum(qpath)-a*s*(omega**2-1),"Magnitude is sqrt(3) a s < 3a on the certified box.")

    # Observational projection and direction check.
    d=sp.Matrix(sp.symbols("d0:6",real=True))
    obs=sp.Matrix(sp.symbols("y0:6",real=True))
    projected=obs.dot(d)/d.dot(d)
    residual_vec=obs-projected*d
    zero("T22_projection_orthogonality",residual_vec.dot(d),"d nonzero; perpendicular residual tests response direction.")
    zero("T23_projection_recovery",(s*d).dot(d)/d.dot(d)-s,"Exact registered state displacement.")
    dv=sp.Matrix([1,2,0,0,0,0]);ev=sp.Matrix([-2,1,0,0,0,0])
    yes("T24_direction_negative_control",dv.dot(ev)==0 and ev.dot(ev)>0,"A transverse displacement cannot be hidden by fitting s.")
    E,S,eta,U,eta2=sp.symbols("E S eta U eta2",real=True)
    zero("T25_switching_work",(eta2*U+E)-(eta*U+E)-(eta2-eta)*U,"q,h fixed across external switching.")
    zero("T26_work_scale_inference",(-(-4*S*s*(s-1)/eta)/(4*s*(s-1)))-S/eta,"s not zero or one; unscaled pair work U.")
    zero("T27_sensitivity",sp.diff(sp.log(s*(s-1)),s)-(2*s-1)/(s*(s-1)),"Diverging relative sensitivity near neutral advance.")

    # Two trial state measurements identify two ratios, not all dimensional scales.
    rows=[];rhs=[]
    for label,qmat in [("parallel",Qpar),("transverse",Qperp)]:
        bracket=source_brackets["magnetic_"+label]
        rows.append((interval(Cg,s,bracket),interval(magnetic(qmat).subs({t1:s,t2:s}),s,bracket)))
        rhs.append(interval(-4*s*(s-1),s,bracket))
    det=isub(imul(rows[0][0],rows[1][1]),imul(rows[1][0],rows[0][1]))
    yes("T28_identifiability_rank",det[0]>0 and rows[0][0][0]>0 and rows[1][0][0]>0
        and rows[0][1][1]<0<rows[1][1][0],
        "Independent source-work columns: positive gravity, negative parallel magnetic and positive transverse magnetic coefficients.")
    num_a=isub(imul(rhs[0],rows[1][1]),imul(rhs[1],rows[0][1]))
    num_b=isub(imul(rows[0][0],rhs[1]),imul(rows[1][0],rhs[0]))
    fit_a,fit_b=idiv(num_a,det),idiv(num_b,det)
    yes("T29_two_ratio_fit",fit_a[0]<=a0<=fit_a[1] and fit_b[0]<=b0<=fit_b[1],"Interval recovery from model-generated state data, not independent validation.")
    scale,alpha,kappa=sp.symbols("scale alpha kappa",nonzero=True)
    zero("T30_scale_degeneracy",(scale*alpha)**2/(scale**2*S)-alpha**2/S,"Common source scaling and squared store scaling preserve state response.")
    zero("T31_sign_degeneracy",(-kappa)**2-kappa**2,"Identical-body pair experiments do not recover the sign of kappa.")
    zero("T32_zero_state_hidden_store",(2*s-1)*d-d-2*(s-1)*d,"Matched copies have different next displacements whenever s!=1 and d!=0.")

    result=dict(status="PASS",count=len(checks),checks=checks,
        benchmark=dict(I_F=str(I.subs(s,1)),W_squared=str(w2),gravity_work_coefficient=str(CgF),
            neutral_ratio_xi=str(xi),neutral_cos_squared=str(cstar),
            neutral_angle_degrees_approx=str(sp.N(angle,30)),
            neutral_distance_ratio_approx=str(sp.N(rstar,30)),
            neutral_distance_squared_exact=str(2/xi)),
        matched_trials=loaded,
        second_native_step=dict(modulus_deficit_lower_bound=str(gap),prestage_modulus_lower_bound=str(prelower),
                               native_direction_norm_lower_bound=str(sp.sqrt(3)*gap)),
        identifiability=dict(design_determinant=fmt_bounds(det),a_load=fmt_bounds(fit_a),b_load=fmt_bounds(fit_b)),
        environment=dict(python=sys.version,executable=sys.executable,sympy=sp.__version__,platform=platform.platform()),
        empirical_status="No independent physical measurements; all examples are consequences of the stated mathematical candidate.",
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    assert "envs\\torment\\" in sys.executable.lower()
    (ROOT/"CHECK_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(status="PASS",checks=len(checks),benchmark=result["benchmark"],
        next_off={k:v["next_off_mid"] for k,v in loaded.items()},
        heldout_2r0={k:v["heldout_2r0"]["s_mid"] for k,v in loaded.items()}),indent=2))
if __name__=="__main__":main()
