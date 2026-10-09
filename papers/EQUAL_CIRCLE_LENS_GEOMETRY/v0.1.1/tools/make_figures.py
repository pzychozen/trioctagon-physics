"""Reproduce six mathematical figures from declared formulas; no runtime imports."""
from pathlib import Path
from datetime import datetime,timezone
import os,sys,json,hashlib,argparse
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon,Arc
mp.mp.dps=80
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.titlesize":11,
    "axes.spines.top":False,"axes.spines.right":False,"axes.labelsize":10,
    "legend.fontsize":9,"pdf.fonttype":42,"svg.fonttype":"none","svg.hashsalt":"PUB-LT-01-v0.1"})
navy="#193c58";blue="#237eaa";orange="#c77928";green="#237c62"
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--only-figure3",action="store_true",help="Revise Figure 3 only; preserve all other delivered assets and data.")
ONLY_FIGURE3=parser.parse_args().only_figure3
data=json.loads((OUT/"FIGURE_DATA.json").read_text(encoding="utf-8")) if ONLY_FIGURE3 else {}
identities=[]
def save(fig,name,values):
    if ONLY_FIGURE3 and name!="03_shape_invariant":
        plt.close(fig)
        return
    data[name]=values
    for ext in ["pdf","svg","png"]:
        path=OUT/(name+"."+ext)
        meta={"CreationDate":datetime(2026,10,9,tzinfo=timezone.utc),"ModDate":datetime(2026,10,9,tzinfo=timezone.utc)} if ext=="pdf" else ({"Date":"2026-10-09"} if ext=="svg" else {})
        fig.savefig(path,bbox_inches="tight",dpi=180,metadata=meta)
        identities.append({"file":path.name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"bytes":path.stat().st_size})
    plt.close(fig)
def lens(ax,r,t,parents=True):
    d=2*r*np.cos(t)
    ang=np.linspace(-t,t,300)
    right=np.column_stack((-d/2+r*np.cos(ang),r*np.sin(ang)))
    left=np.column_stack((d/2-r*np.cos(ang),-r*np.sin(ang)))
    ax.add_patch(Polygon(np.vstack([right,left]),closed=True,facecolor=blue,alpha=.18,edgecolor="none"))
    if parents:
        for x in [-d/2,d/2]:ax.add_patch(Circle((x,0),r,fill=False,ls="--",lw=1,color="#9aa9b4"))
    ax.plot(right[:,0],right[:,1],color=blue,lw=2.2)
    ax.plot(left[:,0],left[:,1],color=blue,lw=2.2)
    ax.set_aspect("equal");return d
fig,ax=plt.subplots(figsize=(6.2,3.6))
t=np.pi/3;r=1.;d=lens(ax,r,t)
ax.scatter([-d/2,d/2],[0,0],s=15,color=navy,zorder=4)
ax.plot([-d/2,0],[0,np.sin(t)],color=orange,lw=1.5)
ax.plot([-d/2,d/2],[0,0],color=navy,lw=.9)
ax.add_patch(Arc((-d/2,0),.48,.48,theta1=0,theta2=60,color=orange,lw=1.2))
ax.text(-.23,.09,r"$\theta$",color=orange)
ax.text(-.43,.5,r"$r$",color=orange)
ax.annotate("",xy=(-d/2,-.16),xytext=(d/2,-.16),arrowprops={"arrowstyle":"<->","color":navy})
ax.text(0,-.28,r"$d$",ha="center",color=navy)
ax.text(0,.48,r"$A$",ha="center",color=blue)
ax.annotate(r"boundary arcs: $P$",xy=(.45,.23),xytext=(.82,.73),
            color=blue,arrowprops={"arrowstyle":"-","color":blue})
ax.text(-d/2,-.43,r"$c_-$",ha="center");ax.text(d/2,-.43,r"$c_+$",ha="center")
ax.set(xlim=(-1.7,1.85),ylim=(-1.12,1.12));ax.axis("off")
save(fig,"01_geometry",{"r":1,"theta":"pi/3","d":1,"arc_samples":300,"description":"Exact circles sampled for vector paths; filled lens shown once."})

uv=np.linspace(0,1,501)
fv=np.array([float(mp.mpf(str(x))-mp.sin(mp.pi*mp.mpf(str(x)))/mp.pi) for x in uv])
fig,ax=plt.subplots(figsize=(6.2,3.25))
ax.plot(uv,uv,label=r"$u$",color=navy)
ax.plot(uv,fv,label=r"$f$",color=blue,lw=2)
ax.plot(uv,np.sqrt(fv),label=r"$G=\sqrt{f}$",color=orange)
ax.set(xlabel=r"normalized perimeter $u=2\theta/\pi$",ylabel="dimensionless value",xlim=(0,1),ylim=(0,1.02))
ax.legend(loc="upper left");ax.grid(alpha=.17)
save(fig,"02_normalized",{"u":uv.tolist(),"f":fv.tolist(),"G":np.sqrt(fv).tolist(),"evaluation":"mpmath 80 digits, converted to binary64 for drawing"})

def vals(x):
    x=mp.mpf(str(x));j=(2*x-mp.sin(2*x))/(16*x*x)
    jp=mp.cos(x)*(mp.sin(x)-x*mp.cos(x))/(4*x**3)
    return j,jp
theta=np.linspace(0,np.pi/2,501)
j=np.array([0. if x==0 else float(vals(x)[0]) for x in theta])
eps=np.geomspace(1e-5,.2,160)
gap=np.array([float(1/(4*mp.pi)-vals(mp.pi/2-mp.mpf(str(x)))[0]) for x in eps])
fig,(ax,bx)=plt.subplots(1,2,figsize=(6.9,3.0),layout="constrained")
ax.plot(theta[1:],j[1:],color=blue,lw=2);ax.plot(theta[:161],theta[:161]/12,color=orange,ls="--",label=r"$\theta/12$")
ax.scatter([0],[0],facecolors="white",edgecolors=blue,s=38,linewidths=1.4,zorder=5)
ax.annotate(r"$J(0^+)=0$ (limit)",xy=(0,0),xytext=(.34,.008),fontsize=9,
            arrowprops={"arrowstyle":"-","color":blue},color=navy)
ax.scatter([np.pi/2],[1/(4*np.pi)],color=blue,s=18)
ax.set(xlabel=r"half-angle $\theta$",ylabel=r"$J=A/P^2$",xticks=[0,np.pi/4,np.pi/2],xticklabels=["0",r"$\pi/4$",r"$\pi/2$"])
ax.legend();ax.grid(alpha=.17)
bx.loglog(eps,gap,color=blue,lw=2,label="exact gap")
bx.loglog(eps,eps**2/np.pi**3,color=orange,ls="--",label=r"$\epsilon^2/\pi^3$")
bx.set(xlabel=r"$\epsilon=\pi/2-\theta$",ylabel=r"$1/(4\pi)-J$");bx.legend();bx.grid(alpha=.17)
save(fig,"03_shape_invariant",{"theta":theta.tolist(),"J":j.tolist(),"epsilon":eps.tolist(),"gap":gap.tolist(),"evaluation":"80 digits; endpoint curve evaluated by high-precision subtraction",
    "scientific_domain":"0 < theta <= pi/2; J=A/P^2 requires P>0.",
    "curve_data_indices":{"start_inclusive":1,"stop_exclusive":len(theta)},
    "plot_limit_metadata":{"index":0,"theta":0,"J_limit":0,
        "admissible_ratio_evaluation":False,"marker":"open",
        "meaning":"J(0+)=0 is a one-sided limit only. A/P^2 is undefined at (P,A)=(0,0)."},
    "coincident_endpoint_marker":"filled"})

fig,axes=plt.subplots(1,2,figsize=(6.8,3),layout="constrained")
for ax,rv,tv,label,area in [(axes[0],.5,np.pi/3,r"$r=1/2,\ \theta=\pi/3$",np.pi/6-np.sqrt(3)/8),
                           (axes[1],1/3,np.pi/2,r"$r=1/3,\ \theta=\pi/2$",np.pi/9)]:
    lens(ax,rv,tv,parents=False)
    ax.set(xlim=(-.6,.6),ylim=(-.57,.57),xlabel="length",ylabel="length")
    ax.set_title(label+"\n"+r"$A="+f"{area:.6f}"+r"$")
    ax.grid(alpha=.15)
fig.suptitle(r"Both boundary lengths: $P=2\pi/3$",fontsize=11)
save(fig,"04_equal_perimeter",{"cases":[{"r":.5,"theta":"pi/3","A":"pi/6-sqrt(3)/8"},{"r":"1/3","theta":"pi/2","A":"pi/9"}],"P":"2pi/3","plot_limits_identical":True})

tv=np.geomspace(1e-4,.4,220);ja=[];jp=[];ta=[];tp=[]
for x in tv:
    z=mp.mpf(str(x));j0,j1=vals(z);p=4*z;a=2*z-mp.sin(2*z)
    ja.append(float(1/p**2));jp.append(float(2*a/p**3))
    ta.append(float(1/(p**2*j1)));tp.append(float(2*a/(p**3*j1)))
fig,(ax,bx)=plt.subplots(1,2,figsize=(6.9,3.15),layout="constrained")
for axis,ys1,ys2,lab1,lab2,const in [(ax,ja,jp,r"$|\partial J/\partial A|$",r"$|\partial J/\partial P|$",1/24),
                                   (bx,ta,tp,r"$|\partial\theta/\partial A|$",r"$|\partial\theta/\partial P|$",.5)]:
    axis.loglog(tv,ys1,color=blue,label=lab1);axis.loglog(tv,ys2,color=orange,label=lab2)
    axis.axhline(const,color=orange,ls=":",lw=1)
    axis.set(xlabel=r"half-angle $\theta$",ylabel="coefficient magnitude")
    axis.legend(loc="upper right");axis.grid(alpha=.16)
save(fig,"05_absolute_sensitivity",{"theta":tv.tolist(),"abs_J_A":ja,"abs_J_P":jp,"abs_theta_A":ta,"abs_theta_P":tp,
    "r":1,"error_model":"Local absolute errors in A and P, in a fixed chosen length unit; coefficient magnitudes have different dimensions. Not finite perturbations.",
    "excluded_endpoint":"theta=0; divergent coefficients are not plotted there."})

us=np.concatenate([np.linspace(.001,.85,240),1-np.geomspace(.15,.0001,180)])
ks=[float(vals(mp.pi*mp.mpf(str(x))/2)[0]/(mp.pi*mp.mpf(str(x))/2*vals(mp.pi*mp.mpf(str(x))/2)[1])) for x in us]
fig,ax=plt.subplots(figsize=(6.2,3.2))
ax.semilogy(us,ks,color=blue,lw=2,label=r"$K=J/(\theta J')$")
ax.axhline(1,color=navy,ls=":",label="tangency limit: 1")
sel=us>=.85;ax.semilogy(us[sel],1/(2*(1-us[sel])),color=orange,ls="--",label=r"$1/[2(1-u)]$ near coincidence")
ax.set(xlabel=r"$u=2\theta/\pi$",ylabel="relative half-angle coefficient",xlim=(0,1));ax.grid(alpha=.17);ax.legend(loc="upper left")
save(fig,"06_relative_sensitivity",{"u":us.tolist(),"K":ks,"relative_error_model":"dtheta/theta=K(dA/A-2dP/P), first order",
    "excluded_endpoints":"u=0 and u=1; endpoint limits are analytic, not finite plotted values."})
(OUT/"FIGURE_DATA.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
(ROOT/"evidence/FIGURE_BUILD.json").write_text(json.dumps({"python":sys.version,"matplotlib":matplotlib.__version__,
    "numpy":np.__version__,"mpmath":mp.__version__,"mp_dps":mp.mp.dps,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "mode":"Figure 3 only; other assets retained unchanged" if ONLY_FIGURE3 else "All six figures",
    "figures":identities},indent=2)+"\n",encoding="utf-8")
print("Generated Figure 3 only; other figure assets and data retained." if ONLY_FIGURE3 else "Generated 6 figures, each PDF/SVG/PNG, with retained quantitative data.")
