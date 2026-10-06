"""Read-only Three-Way A=B=L scaling analysis. Writes only beside this script.
Run: C:/TORMENT/app-g-dev/env/Scripts/python.exe -B verify_and_plot.py
Dependencies: sympy, mpmath, numpy, matplotlib. No production imports.
The additional turning-point scale is recorded as a STOP, not investigated.
"""
from pathlib import Path
import csv
import hashlib
import json
import platform
import subprocess
import sys

import sympy as sp
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
REPO = Path("C:/TORMENT/TRIOCTAGON_new/trioctagon-physics").resolve()
assert not ROOT.is_relative_to(REPO), "Outputs must be external to repository."
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)
sys.stdout.reconfigure(encoding="utf-8")

def git(*args):
    return subprocess.check_output(["git", "-C", str(REPO), *args], text=True)

before = {"head": git("rev-parse", "HEAD").strip(),
          "status": git("status", "--porcelain=v1")}
x, y, L, s, xi, t = sp.symbols("x y L s xi t")
N, D = L*x**4-L*x**2+1, x**4-L*x**2+L
f = N/D
H = (1+s+s*s/L)/(1-s+2*s/L+s*s/L**2)
O = (xi**4-xi**2/L+L**-3)/(xi**4-xi**2+1/L)
I = (1-xi**2+xi**4/L)/(1-xi**2/L+xi**4/L**3)
fy = (L*y*y-L*y+1)/(y*y-L*y+L)
checks = {
    "division_by_L": f-(x**4-x*x+1/L)/(x**4/L-x*x+1),
    "fixed_error": f+x*x-(x**6+1)/D,
    "reciprocal_error": 1/f+1/x**2-(x**6+1)/(x*x*N),
    "reciprocity": f*f.subs(x,1/x)-1,
    "evenness": f-f.subs(x,-x),
    "plus_lock": f.subs(x,1)-1,
    "lock_slope": sp.diff(f,x).subs(x,1)-4*(L-1),
    "boundary_substitution": fy.subs(y,1+s/L)-H,
    "boundary_s_1": H.subs(s,1)-L,
    "outer_substitution": fy.subs(y,L*xi**2)/L-O,
    "inner_substitution": L*fy.subs(y,xi**2/L)-I,
    "inner_outer_reciprocity": I*O.subs(xi,1/xi)-1,
    "outer_xi_1": O.subs(xi,1)-(L-1+L**-2),
    "constant_L_1": f.subs(L,1)-1,
    "derivative": sp.diff(f,x)-2*x*(L-1)*(2*(L+1)*x*x-L*(x**4+1))/D**2,
    "resultant": sp.resultant(N,D,x)-(L-1)**4*(2*L+1)**2,
}
for name, expression in checks.items():
    assert sp.cancel(expression)==0, name

q = sp.sqrt((1+sp.sqrt(1-4*t))/2)
a_coeff = [1,sp.Rational(1,2),sp.Rational(7,8),sp.Rational(33,16)]
b_coeff = [1,-sp.Rational(1,2),-sp.Rational(5,8),-sp.Rational(21,16)]
assert sp.series(1/q,t,0,4).removeO()==sum(c*t**k for k,c in enumerate(a_coeff))
assert sp.series(q,t,0,4).removeO()==sum(c*t**k for k,c in enumerate(b_coeff))
checks["near_pole_and_inner_zero_series"] = 0
checks["outer_pole_and_near_zero_series"] = 0
for yy in [(L+sp.sqrt(L*L-4*L))/2,(L-sp.sqrt(L*L-4*L))/2]:
    assert sp.simplify(yy*yy-L*yy+L)==0
for yy in [(1+sp.sqrt(1-4/L))/2,(1-sp.sqrt(1-4/L))/2]:
    assert sp.simplify(L*yy*yy-L*yy+1)==0
checks["denominator_roots"] = 0
checks["numerator_roots"] = 0

# STOP-condition evidence only: locate the additional real stationary-point scale.
critical_y = [1+1/L+sp.sqrt(2/L+1/L**2),
              1+1/L-sp.sqrt(2/L+1/L**2)]
for yy in critical_y:
    assert sp.simplify(L*yy**2-2*(L+1)*yy+L)==0
stop = {"triggered": True,
        "reason": "Additional real turning-point scale |x-1|=O(L^-1/2).",
        "exact_positive_locations":
        "sqrt(1+1/L +/- sqrt(2/L+1/L^2))",
        "leading_locations": "1 +/- 1/sqrt(2L) + O(1/L)",
        "action": "Recorded; no shoulder-profile, dynamics, or off-diagonal extension."}

def ND(ell,z):
    return ell*z**4-ell*z*z+1, z**4-ell*z*z+ell
def F(ell,z):
    n,d = ND(ell,z)
    return n/d
def boundary(ell,v):
    return (1+v+v*v/ell)/(1-v+2*v/ell+v*v/ell**2)
def outer(ell,v):
    return (v**4-v*v/ell+ell**-3)/(v**4-v*v+1/ell)
def inner(ell,v):
    return (1-v*v+v**4/ell)/(1-v*v/ell+v**4/ell**3)
def roots(ell):
    qq = mp.sqrt((1+mp.sqrt(1-4/ell))/2)
    return {"near_pole": 1/qq, "outer_pole": mp.sqrt(ell)*qq,
            "near_zero": qq, "inner_zero": 1/(mp.sqrt(ell)*qq)}
def astr(ell):
    return 1+1/(2*ell)+mp.mpf(7)/(8*ell**2)+mp.mpf(33)/(16*ell**3)
def bstr(ell):
    return 1-1/(2*ell)-mp.mpf(5)/(8*ell**2)-mp.mpf(21)/(16*ell**3)
def fmt(v):
    return mp.nstr(v,38)
values = [10,100,1000,10000,1000000,10**12]
fixed = [mp.mpf(0),mp.mpf(1)/2,mp.mpf(2)/3,mp.mpf(3)/4,
         mp.mpf(4)/3,mp.mpf(3)/2,mp.mpf(2)]
# Rebuild rational sample points at each precision, avoiding float64 seeds.
def sample_vectors():
    return ([mp.mpf(a)/b for a,b in [(0,1),(1,2),(2,3),(3,4),(4,3),(3,2),(2,1)]],
            [mp.mpf(a)/b for a,b in [(-3,1),(-2,1),(-1,1),(0,1),(1,2),(3,2),(2,1),(3,1)]],
            [mp.mpf(a)/b for a,b in [(1,2),(3,4),(5,4),(3,2),(2,1)]],
            [mp.mpf(a)/b for a,b in [(0,1),(1,4),(1,2),(3,4),(1,1),(5,4),(3,2),(2,1)]])
def evaluate(dps):
    rows, vectors = [], []
    max_identity = mp.mpf(0)
    with mp.workdps(dps):
        X,S,U,V = sample_vectors()
        for ell0 in values:
            ell = mp.mpf(ell0)
            rr = roots(ell)
            identity = []
            for p in [rr["near_pole"],rr["outer_pole"]]:
                n,d = ND(ell,p)
                identity += [abs(d)/(abs(p)**4+ell*abs(p)**2+ell)]
            for z in [rr["near_zero"],rr["inner_zero"]]:
                n,d = ND(ell,z)
                identity += [abs(n)/(ell*abs(z)**4+ell*abs(z)**2+1)]
            identity += [abs(rr["near_pole"]*rr["near_zero"]-1),
                         abs(rr["outer_pole"]*rr["inner_zero"]-1)]
            for z in X[1:]:
                identity += [abs(F(ell,z)*F(ell,1/z)-1)]
            for v in S:
                direct = F(ell,mp.sqrt(1+v/ell))
                identity += [abs(direct-boundary(ell,v))/max(1,abs(direct))]
            for v in U:
                direct = F(ell,mp.sqrt(ell)*v)/ell
                identity += [abs(direct-outer(ell,v))/max(1,abs(direct)),
                             abs(inner(ell,v)*outer(ell,1/v)-1)]
            for v in V:
                direct = ell*F(ell,v/mp.sqrt(ell))
                identity += [abs(direct-inner(ell,v))/max(1,abs(direct))]
            rooterr_a = rr["near_pole"]-astr(ell)
            rooterr_b = rr["near_zero"]-bstr(ell)
            row = {"L":ell0,"dps":dps, **{k:fmt(v) for k,v in rr.items()},
                   "max_normalized_identity_residual":fmt(max(identity)),
                   "fixed_f_max_sample_error":fmt(max(abs(F(ell,z)+z*z) for z in X)),
                   "fixed_g_max_sample_error":fmt(max(abs(1/F(ell,z)+1/z**2) for z in X[1:])),
                   "boundary_max_sample_error":fmt(max(abs(boundary(ell,v)-(1+v)/(1-v)) for v in S)),
                   "outer_max_sample_error":fmt(max(abs(outer(ell,v)-v*v/(v*v-1)) for v in U)),
                   "inner_Lf_max_sample_error":fmt(max(abs(inner(ell,v)-(1-v*v)) for v in V)),
                   "inner_g_over_L_max_sample_error":fmt(max(abs(1/inner(ell,v)-1/(1-v*v)) for v in V if v!=1)),
                   "normalized_root_A3_error":fmt(abs(rooterr_a)),
                   "normalized_root_B3_error":fmt(abs(rooterr_b)),
                   "L4_signed_A3_error":fmt(ell**4*rooterr_a),
                   "L4_signed_B3_error":fmt(ell**4*rooterr_b)}
            rows.append(row)
            vectors.append([*rr.values(), *[F(ell,z) for z in X],
                            *[boundary(ell,v) for v in S],
                            *[outer(ell,v) for v in U],
                            *[inner(ell,v) for v in V]])
            max_identity = max(max_identity,max(identity))
    return rows,vectors,max_identity

low, lv, lr = evaluate(120)
high,hv,hr = evaluate(200)
with mp.workdps(210):
    precision_change = max(abs(a-b)/max(1,abs(b))
                           for aa,bb in zip(lv,hv) for a,b in zip(aa,bb))
assert lr < mp.mpf("1e-100")
assert hr < mp.mpf("1e-180")
assert precision_change < mp.mpf("1e-100")
mp.mp.dps=120
output = {"scope":"A=B=L>0 only","symbolic_checks_passed":list(checks),
          "precision_dps":[120,200],
          "largest_120_digit_identity_residual":fmt(lr),
          "largest_200_digit_identity_residual":fmt(hr),
          "max_120_vs_200_normalized_change":fmt(precision_change),
          "sample_points": {"fixed_x":"0,1/2,2/3,3/4,4/3,3/2,2",
                            "boundary_s":"-3,-2,-1,0,1/2,3/2,2,3",
                            "outer_xi":"1/2,3/4,5/4,3/2,2",
                            "inner_xi":"0,1/4,1/2,3/4,1,5/4,3/2,2",
                            "inner_reciprocal":"same inner set except 1"},
          "rows_120":low,"rows_200":high,"stop_condition":stop,
          "versions":{"python":platform.python_version(),"sympy":sp.__version__,
                      "mpmath":mp.__version__,"numpy":np.__version__,
                      "matplotlib":matplotlib.__version__}}
(ROOT/"numerical_results.json").write_text(json.dumps(output,indent=2),encoding="utf-8")
with (ROOT/"numerical_results.csv").open("w",newline="",encoding="utf-8") as stream:
    writer=csv.DictWriter(stream,fieldnames=list(low[0]))
    writer.writeheader();writer.writerows(low)
print(json.dumps({k:output[k] for k in ["largest_120_digit_identity_residual",
      "largest_200_digit_identity_residual","max_120_vs_200_normalized_change"]}),flush=True)

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,
                     "axes.titlesize":13,"axes.labelsize":11,
                     "axes.spines.top":False,"axes.spines.right":False,
                     "figure.facecolor":"white","axes.facecolor":"#fafbfc",
                     "savefig.facecolor":"white","svg.fonttype":"none"})
colors=["#cf6a18","#2478a4","#2c9665","#8259a5","#cc4470"]
plotLs=[10,100,1000,10000,1000000]
def label(ell):
    return r"$L=10$" if ell==10 else rf"$L=10^{{{int(np.log10(ell))}}}$"
def curve(ax, xx, fun, color, label_text=None, ylim=None, poles=(), ls="-", lw=1.55):
    yy=[]
    for a in xx:
        try:
            value=float(fun(mp.mpf(str(a))))
        except (ZeroDivisionError,ValueError):
            value=np.nan
        if ylim and not(ylim[0]*1.15-1<=value<=ylim[1]*1.15+1):
            value=np.nan
        yy.append(value)
    yy=np.array(yy)
    for pole in poles:
        j=np.searchsorted(xx,float(pole))
        yy[max(0,j-1):min(len(yy),j+1)]=np.nan
    ax.plot(xx,yy,color=color,label=label_text,ls=ls,lw=lw)
def base(ax,xlabel,ylabel,xlim,ylim):
    ax.set(xlabel=xlabel,ylabel=ylabel,xlim=xlim,ylim=ylim)
    ax.grid(alpha=.2);ax.axhline(0,color="#9ca5af",lw=.65,zorder=0)
def save(fig,name):
    fig.savefig(FIG/(name+".png"),dpi=180,bbox_inches="tight")
    fig.savefig(FIG/(name+".svg"),bbox_inches="tight")
    plt.close(fig)
    print("FIGURE",name,flush=True)

fig,ax=plt.subplots(figsize=(10,5.6),layout="constrained")
for ell0,col in zip(plotLs,colors):
    ell=mp.mpf(ell0);rr=roots(ell)
    refine=np.array([float(mp.sqrt(1+mp.mpf(str(v))/ell)) for v in np.linspace(-6,6,321)])
    xx=np.unique(np.r_[np.linspace(-2,2,2001),refine,-refine])
    curve(ax,xx,lambda v,e=ell:F(e,v),col,label(ell0),(-6,4),
          [-rr["near_pole"],rr["near_pole"]])
xx=np.linspace(-2,2,1201)
curve(ax,xx,lambda v:-v*v,"#171c24",r"Bulk profile $-x^2$ (excludes $\pm1$)",(-6,4),[-1,1],"--",2)
ax.scatter([-1,1],[1,1],s=34,color="#171c24",zorder=7,label="Exact locks, every L")
ax.scatter([-1,1],[-1,-1],s=50,facecolors="white",edgecolors="#171c24",zorder=7)
base(ax,"x",r"$f_L(x)$",(-2,2),(-6,4))
ax.set_title("A  |  Fixed central window: the bulk limit and the surviving locks",loc="left",fontweight="bold")
ax.legend(ncol=3,fontsize=8.5,loc="lower center")
save(fig,"A_fixed_central_window")

fig,ax=plt.subplots(figsize=(10,5.6),layout="constrained")
ss=np.linspace(-4,4,2401)
for ell0,col in zip(plotLs,colors):
    ell=mp.mpf(ell0);rr=roots(ell);spole=ell*(rr["near_pole"]**2-1)
    curve(ax,ss,lambda v,e=ell:boundary(e,v),col,label(ell0),(-8,8),[spole])
curve(ax,ss,lambda v:(1+v)/(1-v),"#171c24",r"Limit $(1+s)/(1-s)$",(-8,8),[1],"--",2)
ax.axvline(1,color="#171c24",ls=":",lw=1,label="Limiting pole s=1")
ax.scatter([0],[1],color="#171c24",s=30,zorder=7,label="Exact lock s=0")
ax.scatter([-1],[0],facecolors="white",edgecolors="#171c24",s=48,zorder=7)
base(ax,r"$s=L(x^2-1)$",r"$f_L(\sqrt{1+s/L})$",(-4,4),(-8,8))
ax.set_title("B  |  Lock boundary layer: an O(1/L) transition",loc="left",fontweight="bold")
ax.legend(ncol=3,fontsize=8.5,loc="lower left")
save(fig,"B_lock_boundary_layer")

fig,ax=plt.subplots(figsize=(10,5.6),layout="constrained")
xx=np.linspace(.4,2,2001)
for ell0,col in zip(plotLs,colors):
    ell=mp.mpf(ell0);pole=roots(ell)["outer_pole"]/mp.sqrt(ell)
    curve(ax,xx,lambda v,e=ell:outer(e,v),col,label(ell0),(-6,6),[pole])
curve(ax,xx,lambda v:v*v/(v*v-1),"#171c24",r"Limit $\xi^2/(\xi^2-1)$",(-6,6),[1],"--",2)
ax.axvline(1,color="#171c24",lw=1,ls=":")
base(ax,r"$\xi=x/\sqrt{L}$",r"$f_L(\sqrt{L}\xi)/L$",(.4,2),(-6,6))
ax.set_title("C  |  Outer scale: values are O(L), away from the pole",loc="left",fontweight="bold")
ax.legend(ncol=2,fontsize=9,loc="lower right")
save(fig,"C_outer_scale")

fig,axes=plt.subplots(1,2,figsize=(12,5.5),layout="constrained")
xx=np.linspace(-2,2,2001)
for ell0,col in zip(plotLs,colors):
    ell=mp.mpf(ell0);zero=roots(ell)["inner_zero"]*mp.sqrt(ell)
    curve(axes[0],xx,lambda v,e=ell:inner(e,v),col,label(ell0),(-4,2))
    curve(axes[1],xx,lambda v,e=ell:1/inner(e,v),col,None,(-6,6),[-zero,zero])
curve(axes[0],xx,lambda v:1-v*v,"#171c24",r"Limit $1-\xi^2$",(-4,2),(),"--",2)
curve(axes[1],xx,lambda v:1/(1-v*v),"#171c24",r"Limit $1/(1-\xi^2)$",(-6,6),[-1,1],"--",2)
base(axes[0],r"$\xi=x\sqrt{L}$",r"$L f_L(\xi/\sqrt{L})$",(-2,2),(-4,2))
base(axes[1],r"$\xi=x\sqrt{L}$",r"$g_L(\xi/\sqrt{L})/L$",(-2,2),(-6,6))
axes[0].legend(ncol=2,fontsize=8.5,loc="lower center")
axes[1].legend(fontsize=9,loc="lower center")
axes[0].set_title("Small forward profile",loc="left")
axes[1].set_title("Large reciprocal profile",loc="left")
fig.suptitle("D  |  Inner scale: exactly paired with the outer scale by inversion",fontweight="bold")
save(fig,"D_reciprocal_inner_scale")

fig,axes=plt.subplots(1,2,figsize=(12,5.5),layout="constrained")
ells=np.unique(np.r_[4.,np.geomspace(4.00001,1e6,500)])
data={k:[] for k in ["near_pole","outer_pole","near_zero","inner_zero"]}
for e0 in ells:
    rr=roots(mp.mpf(str(e0)))
    for k in data:data[k].append(float(rr[k]))
cc={"outer_pole":"#cf6a18","near_pole":"#2478a4","near_zero":"#2c9665","inner_zero":"#8259a5"}
names={"outer_pole":"Outer pole","near_pole":"Near-lock pole","near_zero":"Near-lock zero","inner_zero":"Inner zero"}
for k in ["outer_pole","near_pole","near_zero","inner_zero"]:
    axes[0].loglog(ells,data[k],color=cc[k],lw=1.9,label=names[k]+" (exact)")
large=np.geomspace(10,1e6,450)
axes[0].loglog(large,np.sqrt(large),"#171c24",ls="--",lw=1.15,label=r"Leading scales $\sqrt{L},1,L^{-1/2}$")
axes[0].loglog(large,np.ones_like(large),"#171c24",ls="--",lw=1.15)
axes[0].loglog(large,1/np.sqrt(large),"#171c24",ls="--",lw=1.15)
axes[0].set(xlabel="L",ylabel="Positive root location",xlim=(4,1e6),ylim=(5e-4,2e3))
axes[0].set_title("Reciprocal pole/zero migration",loc="left")
axes[0].legend(fontsize=8)
p_gap=[];z_gap=[]
for e0 in ells:
    e=mp.mpf(str(e0));rr=roots(e)
    p_gap.append(float(e*(rr["near_pole"]-1)))
    z_gap.append(float(e*(1-rr["near_zero"])))
axes[1].semilogx(ells,p_gap,color=cc["near_pole"],label=r"Exact $L(p_{\rm n}-1)$")
axes[1].semilogx(ells,z_gap,color=cc["near_zero"],label=r"Exact $L(1-z_{\rm n})$")
axes[1].semilogx(large,.5+7/(8*large)+33/(16*large**2),color=cc["near_pole"],ls=":",lw=2,label="Pole expansion through L^-3")
axes[1].semilogx(large,.5+5/(8*large)+21/(16*large**2),color=cc["near_zero"],ls=":",lw=2,label="Zero expansion through L^-3")
axes[1].axhline(.5,color="#171c24",ls="--",label="Limiting scaled offset 1/2")
axes[1].set(xlabel="L",ylabel="Scaled distance from x=1",xlim=(4,1e6),ylim=(.45,1.8))
axes[1].set_title("The lock gap remains O(1/L)",loc="left")
axes[1].legend(fontsize=8.5)
for ax in axes:ax.grid(which="major",alpha=.2)
fig.suptitle("E  |  Positive roots; negative roots follow by evenness. Real threshold: L=4.",fontweight="bold")
save(fig,"E_pole_zero_migration")

after={"head":git("rev-parse","HEAD").strip(),"status":git("status","--porcelain=v1")}
assert before==after,"Repository status changed during the run; inspect independently."
manifest={"repository_before":before,"repository_after":after,
          "repository_status_unchanged":True,"output_directory":str(ROOT),
          "work_order_sha256":hashlib.sha256(Path(
              "C:/Users/Notandi/.codex/attachments/0fae0d40-50ae-4352-bae3-84ea14c5bdee/Pasted text.txt"
          ).read_bytes()).hexdigest(),
          "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "files":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted(FIG.iterdir()) if p.is_file()}}
(ROOT/"run_manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
print("PASS: symbolic, 120/200-digit numerics, five figures, repository-status preservation.",flush=True)
