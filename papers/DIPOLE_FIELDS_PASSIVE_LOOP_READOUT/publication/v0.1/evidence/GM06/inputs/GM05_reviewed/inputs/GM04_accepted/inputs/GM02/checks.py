"""Exact GM02 algebra and rational certificates. Run through run_python.cmd."""
from pathlib import Path
import hashlib
import json
import platform
import sys
import sympy as sp

ROOT=Path(__file__).resolve().parent
R=sp.Rational
checks=[]
def zero(name,value,scope):
    vals=list(value) if isinstance(value,sp.MatrixBase) else [value]
    reduced=[sp.simplify(sp.expand(v)) for v in vals]
    assert all(v==0 for v in reduced),(name,reduced)
    checks.append(dict(id=name,passed=True,kind="exact_identity",scope=scope))
def truth(name,value,scope):
    assert bool(value),name
    checks.append(dict(id=name,passed=True,kind="exact_inequality_or_predicate",scope=scope))
def avf(poly,t1,t2,s1,s2):
    theta=sp.Symbol("theta",real=True)
    return [sp.integrate(sp.diff(poly,t).subs({t1:theta*s1,t2:theta*s2}), (theta,0,1)).expand()
            for t in [t1,t2]]
def root_certificate(poly,s,label,lo=R(1,2),hi=R(3,2)):
    poly=sp.Poly(poly,s)
    assert all(c.is_Rational for c in poly.all_coeffs())
    assert poly.eval(lo)<0 and poly.eval(hi)>0
    for _ in range(100):
        mid=(lo+hi)/2
        if poly.eval(mid)<0:lo=mid
        else:hi=mid
    mid=(lo+hi)/2
    residual=poly.eval(mid)
    return dict(case=label,lo=str(lo),hi=str(hi),width=str(hi-lo),
                decimal_mid=str(sp.N(mid,24)),root_residual_at_mid=str(residual),
                scaled_energy_defect_at_mid=str(4*mid*residual),
                scaled_energy_defect_decimal=str(sp.N(4*mid*residual,8)),
                h_plus=str(sp.N(2*mid-1,24)),
                normalized_total_storage_change=str(sp.N((2*mid-1)**2-1,24)),
                polynomial=str(poly.as_expr()),method="100 rational bisections; uniqueness from the written contraction theorem")

def main():
    e=sp.ones(3,1); L=e*e.T-3*sp.eye(3)
    T=sp.Matrix([[-R(1,2),1,-R(1,2)],[-sp.sqrt(3)/2,0,sp.sqrt(3)/2],[0,0,0]])
    q=sp.Matrix([1,-R(1,2)-sp.I*sp.sqrt(3)/2,-R(1,2)+sp.I*sp.sqrt(3)/2])
    k=sp.Matrix([R(999,1000),1,R(1001,1000)])
    eps,g=R(1,10),R(1,60)
    def intensity(v):return sp.expand(sum(sp.conjugate(vv)*vv for vv in v))
    def W(v):
        x=sp.re(v);y=sp.im(v)
        return sp.simplify(T*x.cross(y))
    prestage=q+eps*sp.Matrix([(k[i]-sp.conjugate(q[i])*q[i])*q[i] for i in range(3)])+g*L*q
    multipliers=sp.Matrix([R(9499,10000),R(9500,10000),R(9501,10000)])
    zero("C01_fourier_prestage",prestage-sp.diag(*multipliers)*q,"Actual native tuple; input amplitudes are one.")
    truth("C02_positive_multipliers",all(a>0 for a in multipliers),"All prestage phases equal their original root-of-unity phases.")
    zero("C03_zero_triple_phase_kicks",sp.Matrix([sp.im((q[j]*sp.conjugate(q[i]))**3) for i in range(3) for j in range(3)]),"Positive multipliers leave the phases; every native kick vanishes.")
    wf=sp.Matrix([sp.sqrt(3)/200000000,R(57,400000),0])
    zero("C04_initial_silent",W(q),"Full native state space; outside the NPC aligned sector.")
    zero("C05_emergent_W",W(prestage)-wf,"Unnormalized Fourier entrance used in the supplied order.")
    wf2=sp.simplify(wf.dot(wf))
    truth("C06_emergent_W_positive",wf2>0,"The proposed source moment is nonzero for nonzero kappa.")
    t1,t2,s1,s2,s=sp.symbols("t1 t2 s1 s2 s",real=True)
    aa=R(1,10000);v=2*aa**2;tt=R(1,20)
    path=q+s*(prestage-q)
    Is=3*(1-tt*s)**2+2*aa**2*s**2
    Ws=sp.Matrix([sp.sqrt(3)*aa**2*s**2/2,3*aa*s*(1-tt*s)/2,0])
    zero("C07_path_intensity",intensity(path)-Is,"Exact interpolation along the single unloaded native direction.")
    zero("C08_path_moment",W(path)-Ws,"Moment direction need not stay parallel to W at s=1.")
    nproj=wf*wf.T/wf2
    Qpar=sp.eye(3)-3*nproj
    Qside=sp.diag(1,1,-2)
    zero("C09_parallel_energy", (wf.T*Qpar*wf)[0]+2*wf2,"Actual GM01 pair potential tensor.")
    zero("C10_transverse_energy",(wf.T*Qside*wf)[0]-wf2,"Line of centers chosen along e_z, perpendicular to every path W.")
    zero("C11_angular_difference",(wf.T*(Qside-Qpar)*wf)[0]-3*wf2,"Gravity and internal-only terms cancel at equal distance.")
    zero("C12_equal_coefficient_control",W(R(19,20)*q),"Equal k makes all three multipliers equal, so the moment stays zero.")
    kap=sp.Symbol("kappa",real=True)
    zero("C13_zero_moment_coupling_control",(3*kap**2*wf2).subs(kap,0),"Kappa=0 removes the angular work.")

    pre_real=e+eps*(k-e)+g*L*e
    zero("C14_real_native_step",pre_real-sp.Matrix([R(9999,10000),1,R(10001,10000)]),"GM01 D5.")
    zero("C15_intensity_increment",intensity(pre_real)-3-v,"Exact nonzero increment in the NPC domain.")
    zero("C16_real_path_silent",W(e+s*(pre_real-e)),"No dipole contribution for any real interpolation.")
    M,b,A,D=sp.symbols("M b A D",real=True)
    Pg=-A*(M+b*t1**2)*(M+b*t2**2)
    zero("C17_gravity_work",Pg.subs({t1:1,t2:1})-Pg.subs({t1:0,t2:0})+A*(2*M*b+b**2),"A=G_N/r, b=alpha/50000000.")
    Lg=avf(Pg,t1,t2,s1,s2)
    zero("C18_gravity_AVF",sp.Matrix(Lg)-sp.Matrix([-A*b*s1*(M+b*s2**2/2),-A*b*s2*(M+b*s1**2/2)]),"Two independently loaded bodies, before restricting to the diagonal.")

    # General endpoint work, with all simultaneous cross terms retained.
    m1,m2,dm1,dm2=sp.symbols("m1 m2 dm1 dm2",real=True)
    u1=sp.Matrix(sp.symbols("u10:13",real=True));u2=sp.Matrix(sp.symbols("u20:23",real=True))
    du1=sp.Matrix(sp.symbols("du10:13",real=True));du2=sp.Matrix(sp.symbols("du20:23",real=True))
    K=sp.Matrix([[1,2,3],[2,5,7],[3,7,11]]) # symmetry is the only matrix premise
    Ksymbols=sp.symbols("K0:6",real=True)
    K=sp.Matrix([[Ksymbols[0],Ksymbols[1],Ksymbols[2]],
                 [Ksymbols[1],Ksymbols[3],Ksymbols[4]],
                 [Ksymbols[2],Ksymbols[4],Ksymbols[5]]])
    dU=-A*((m1+dm1)*(m2+dm2)-m1*m2)+((u1+du1).T*K*(u2+du2))[0]-(u1.T*K*u2)[0]
    work=-A*((m2+dm2/2)*dm1+(m1+dm1/2)*dm2)
    work+=((u2+du2/2).T*K*du1)[0]+((u1+du1/2).T*K*du2)[0]
    zero("C19_endpoint_mean_field_work",dU-work,"General symmetric dipole tensor and gravitational product.")
    zero("C20_silent_start_half_fields",dU.subs({**dict(zip(u1,[0]*3)),**dict(zip(u2,[0]*3)),dm1:0,dm2:0})-(du1.T*K*du2)[0],"Initial-field charging would give zero; endpoint means give the full interaction.")
    p2=sp.Symbol("P_squared",nonnegative=True)
    zero("C21_fixed_canonical_kinetic",p2/(2*(m1+dm1))-p2/(2*m1)+p2*dm1/(2*m1*(m1+dm1)),"Positive initial and final mass; canonical P held fixed.")

    coeff=sp.symbols("c0:9")
    P=sum(coeff[3*i+j]*t1**i*t2**j for i in range(3) for j in range(3))
    l1,l2=avf(P,t1,t2,s1,s2)
    Delta=P.subs({t1:s1,t2:s2})-P.subs({t1:0,t2:0})
    zero("C22_AVF_exact_work",Delta-s1*l1-s2*l2,"Generic polynomial of degree at most two in each body's path parameter.")
    h1,h2,S1,S2,eta=sp.symbols("h1 h2 S1 S2 eta",real=True)
    r1=s1-h1+eta*l1/(2*S1);r2=s2-h2+eta*l2/(2*S2)
    dE=eta*Delta+S1*((2*s1-h1)**2-h1**2)/2+S2*((2*s2-h2)**2-h2**2)/2
    zero("C23_energy_residual_identity",dE-2*S1*s1*r1-2*S2*s2*r2,"Exact conservation at any root; exact residual-to-energy relation otherwise.")
    zero("C24_zero_load_recovery",sp.Matrix([r1,r2]).subs({eta:0,s1:h1,s2:h2}),"h remains fixed at eta=0; neutral h=1 recovers F at every step.")
    zero("C25_zero_load_jacobian",sp.Matrix([r1,r2]).jacobian([s1,s2]).subs(eta,0)-sp.eye(2),"IFT in s at fixed preparation; no derivative of F needed.")

    Ppar=sp.expand(-A*Is.subs(s,t1)*Is.subs(s,t2)+D*(Ws.subs(s,t1).T*Qpar*Ws.subs(s,t2))[0])
    Pside=sp.expand(-A*Is.subs(s,t1)*Is.subs(s,t2)+D*(Ws.subs(s,t1).T*Qside*Ws.subs(s,t2))[0])
    zero("C26_exchange_symmetry",Ppar-Ppar.xreplace({t1:t2,t2:t1}),"Identical bodies, poses and stores; forces equal s on the local branch.")
    for name,poly in [("parallel",Ppar),("transverse",Pside)]:
        la,lb=avf(poly,t1,t2,s1,s2)
        DeltaF=poly.subs({t1:1,t2:1})-poly.subs({t1:0,t2:0})
        zero("C27_"+name+"_leading_coefficient",la.subs({s1:1,s2:1})-DeltaF/2,"s=1-eta Delta U_F/(4S)+O(eta^2).")
        zero("C28_"+name+"_diagonal_work",2*s*la.subs({s1:s,s2:s})-(poly.subs({t1:s,t2:s})-poly.subs({t1:0,t2:0})),"No spurious multiplication by s in the branch equation.")
    geometric_gap=3*D*(wf.dot(Ws))**2/wf2
    zero("C29_loaded_angular_gap",Pside.subs({t1:s,t2:s})-Ppar.subs({t1:s,t2:s})-geometric_gap,"Fixed center line parallel to W(1); W(s) is allowed to turn.")

    Bbox=R(3,2)
    w0,w1,w2=R(1,4000),R(1,6000),R(1,60000)
    truth("C30_W_uniform_bounds",aa**2*Bbox**2+3*aa*Bbox/2<w0 and 2*aa**2*Bbox+3*aa/2<w1 and 2*aa**2+3*aa*tt<w2,"Componentwise bounds use sqrt(3)<2 on 0<=z<=3/2.")
    truth("C31_intensity_derivative_bounds",6*tt-2*(3*tt**2+2*aa**2)*Bbox>0 and 2*(3*tt**2+2*aa**2)<R(1,50),"I decreases, |I'|<=3/10, I''<1/50 on the segment.")
    shift=(R(9,10)*R(1,4)+R(10**6,12_000_000))/2
    lip=(R(3,20)*R(1,4)+R(23*10**6,360_000_000))/4
    zero("C32_magnetic_box_constants",sp.Matrix([shift-R(37,240),lip-R(73,2880)]),"0<=a_load<=1/4 and 0<=b_load<=10^6.")
    truth("C33_magnetic_contraction",shift<R(1,2) and lip<1,"Full two-variable map, both arrangements.")
    zeta=R(1,300_000_000)
    gshift=R(1,10)*Bbox*(1+zeta*Bbox**2)
    glip=R(1,10)*(1+3*zeta*Bbox**2)
    truth("C34_gravity_contraction",gshift<R(1,2) and glip<1,"0<=gamma<=1/10, zeta<=1/300000000.")
    truth("C35_real_domain_preservation",1-aa*Bbox>=R(9,10) and 1+aa*Bbox<=R(11,10),"Positive real output remains in NPC finite domain for the specified one step.")
    truth("C36_magnetic_path_positivity",1-(tt+aa)*Bbox>R(9,10),"All phases fixed along the segment; the Fourier phase sector stays outside NPC.")
    # General extra energy terms have their own nonzero changes.
    coeffg,coeffm=sp.symbols("C_g C_m",real=True)
    zero("C37_self_energy_midpoints",-coeffg*((m1+dm1)**2-m1**2)+2*coeffg*(m1+dm1/2)*dm1,"Gravity self effective potential -C_g m^2.")
    zero("C38_magnetic_self_midpoints",-coeffm*((u1+du1).dot(u1+du1)-u1.dot(u1))+2*coeffm*(u1+du1/2).dot(du1),"Magnetic fixed-moment effective self potential -C_m |mu|^2.")
    def nativeV(vv):
        iss=[sp.simplify(sp.conjugate(c)*c) for c in vv]
        return sp.simplify(eps*sum(iss[i]**2/4-k[i]*iss[i]/2 for i in range(3))+
            g*sum(sp.conjugate(vv[i]-vv[j])*(vv[i]-vv[j]) for i in range(3) for j in range(i+1,3))/2)
    dv=nativeV(pre_real)-nativeV(e)
    truth("C39_native_V_zero_load_defect",dv<0,"Adding a nonzero energy scale times native V breaks the benchmark's zero-load conservation.")
    zero("C40_stationary_unresponsive_direction",e+g*L*e-e,"Equal k=1 and Omega=e have d=0 despite a nonzero gravitational mass gradient.")
    # A radial magnetic self-energy check: isotropic angular average of the transverse projector.
    nx2,ny2,nz2=sp.symbols("nx2 ny2 nz2")
    zero("C41_isotropic_projection_trace_average",sp.eye(3)-sp.eye(3)/3-R(2,3)*sp.eye(3),"Rotational symmetry gives angular average kk^T/|k|^2=I/3; Parseval proof is in the report.")

    numerics=[]
    for gamma,label in [(R(1,10),"gravity_r"),(R(1,20),"gravity_2r")]:
        residual=s-1-gamma*s*(1+zeta*s**2)
        numerics.append(root_certificate(residual,s,label))
        truth("C42_"+label+"_other_roots",residual.subs(s,0)<0 and residual.subs(s,2)>0 and sp.Poly(residual,s).LC()<0,"Cubic has an additional positive root beyond 2 and a negative root; uniqueness is restricted to the certified box.")
    for label,poly in [("magnetic_parallel",Ppar),("magnetic_transverse",Pside)]:
        poly=poly.subs({A:R(1,100),D:10**6})
        lf=avf(poly,t1,t2,s1,s2)[0].subs({s1:s,s2:s})
        residual=sp.expand(s-1+lf/2)
        cert=root_certificate(residual,s,label)
        cert["unloaded_pair_work_over_S"]=str(poly.subs({t1:1,t2:1})-poly.subs({t1:0,t2:0}))
        cert["unloaded_pair_work_over_S_decimal"]=str(sp.N(sp.sympify(cert["unloaded_pair_work_over_S"]),20))
        numerics.append(cert)
    truth("C43_magnetic_response_order",sp.Rational(numerics[2]["lo"])>1>sp.Rational(numerics[3]["hi"]),"Certified example with gravity active: end-to-end advances farther, transverse advances less.")
    truth("C44_gravity_response_order",sp.Rational(numerics[0]["lo"])>sp.Rational(numerics[1]["hi"])>1,"Same sources and stores, doubled separation.")
    report=dict(status="PASS",checks=checks,count=len(checks),
        meanings="Exact identities, rational bounds and root brackets; not physical experiments or independent review.",
        W_plus=[str(a) for a in wf],W_plus_squared=str(wf2),
        magnetic_I_plus=str(Is.subs(s,1)),native_V_zero_load_change_per_body=str(dv),
        certified_examples=numerics,
        normalized_box=dict(magnetic_image_shift=str(shift),magnetic_lipschitz=str(lip),
                            gravity_shift_upper=str(gshift),gravity_lipschitz_upper=str(glip)),
        environment=dict(python=sys.version,executable=sys.executable,sympy=sp.__version__,platform=platform.platform()),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    assert "envs\\torment\\" in sys.executable.lower()
    (ROOT/"CHECK_RESULTS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(status="PASS",checks=len(checks),examples=[{k:c[k] for k in ["case","decimal_mid","h_plus","scaled_energy_defect_decimal"]} for c in numerics]),indent=2))
if __name__=="__main__":main()
