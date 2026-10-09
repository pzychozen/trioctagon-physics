"""PUB-LT-02: coordinate illustrations only; no project imports.
Owner run: cmd.exe, call conda activate torment, python -B.
Portable: Python 3 with numpy/matplotlib; no conda impersonation needed.
"""
from pathlib import Path
import os, json, sys, platform, hashlib
os.environ.setdefault("MPLCONFIGDIR",str(Path(__file__).resolve().parents[1]/"build/mpl-cache"))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"figures"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,
 "axes.spines.top":False,"axes.spines.right":False,
 "axes.labelsize":10,"axes.titlesize":11,"legend.fontsize":9,
 "pdf.fonttype":42,"svg.fonttype":"none","savefig.dpi":180})
BLUE="#24628c";ORANGE="#b65327";TEAL="#247e70";GRAY="#67747e"
records={}
def keep(name,fig,params,arrays):
    fig.savefig(OUT/(name+".pdf"),bbox_inches="tight",metadata={"CreationDate":None,"ModDate":None,"Creator":"PUB-LT-02 isolated coordinate generator"})
    fig.savefig(OUT/(name+".svg"),bbox_inches="tight")
    fig.savefig(OUT/(name+".png"),bbox_inches="tight")
    plt.close(fig)
    data={k:np.asarray(v).tolist() for k,v in arrays.items()}
    p=OUT/(name+".json");p.write_text(json.dumps({"parameters":params,"data":data},indent=2)+"\n",encoding="utf-8")
    records[name]={"parameters":params,"data_sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def axes_plane(ax,x="signed radius u"):
    ax.axvline(0,c=GRAY,lw=.7);ax.axhline(0,c=GRAY,lw=.5)
    ax.set_aspect("equal");ax.set_xlabel(x);ax.set_ylabel("height z")

t=np.linspace(0,2*np.pi,721)
fig,axs=plt.subplots(1,3,figsize=(9.2,3),layout="constrained")
data={"theta":t}
for ax,a,title in zip(axs,[1.6,1,.5],["Ring: a = 1.6","Horn: a = 1","Spindle: a = 0.5"]):
    u=a+np.cos(t);z=np.sin(t);ax.plot(u,z,c=BLUE,lw=2);axes_plane(ax)
    if a<=1:
        zz=np.sqrt(1-a*a);ax.scatter([0,0],[zz,-zz],c=ORANGE,s=28,zorder=3)
    ax.set_title(title);ax.set_ylim(-1.2,1.2);data[str(a)+"_u"]=u
keep("carriers",fig,{"r":1,"aspects":[1.6,1,.5],"points":721},data)

fig,axs=plt.subplots(1,2,figsize=(8.8,3.8),layout="constrained")
dat={"theta":t}
for ax,a,sgn,title in zip(axs,[2,.5],[1,-1],["Same side: a = 2","Reflected: a = 1/2"]):
    u1=a+np.cos(t);z1=np.sin(t);u2=sgn*(2*a+2*np.cos(t));z2=2*np.sin(t)
    ax.plot(u1,z1,c=BLUE,label="minor radius 1");ax.plot(u2,z2,c=ORANGE,label="minor radius 2")
    axes_plane(ax);ax.set_title(title)
    dat[str(a)+"_small"]=np.c_[u1,z1];dat[str(a)+"_large"]=np.c_[u2,z2]
fig.legend(*axs[0].get_legend_handles_labels(),loc="lower center",bbox_to_anchor=(.5,-.09),ncol=2,frameon=False)
keep("intersections",fig,{"r":1,"h":2,"aspects":[2,.5],"reflected_second":[False,True]},dat)

fig,ax=plt.subplots(figsize=(6.2,4),layout="constrained")
for r,c in [(2,ORANGE),(1,BLUE)]:
    z=np.linspace(-r,r,801)
    dx=np.sqrt(np.maximum(0,r*r-z*z))
    lower=np.maximum(0,.5*r-dx);upper=.5*r+dx
    ax.fill_betweenx(z,lower,upper,color=c,alpha=.15)
    th=np.linspace(-np.arccos(-.5),np.arccos(-.5),601)
    ax.plot(.5*r+r*np.cos(th),r*np.sin(th),c=c,label=f"boundary of K, r = {r}")
th=np.linspace(np.arccos(-.5),2*np.pi-np.arccos(-.5),401)
inner=np.c_[-(1+2*np.cos(th)),2*np.sin(th)]
ax.plot(*inner.T,c=ORANGE,ls="--",label="inner sheet, r = 2")
p=np.array([.75,np.sqrt(15)/4])
ax.scatter(*p,c="black",s=30,zorder=5)
ax.annotate("shared point",p,xytext=(1.65,.35),arrowprops={"arrowstyle":"-","color":GRAY},fontsize=9)
axes_plane(ax,r"cylindrical radius $\rho$");ax.set_xlim(-.08,3.2)
fig.legend(*ax.get_legend_handles_labels(),loc="lower center",bbox_to_anchor=(.5,-.17),ncol=1,frameon=False)
keep("bodies",fig,{"a":.5,"radii":[1,2],"witness":["3/4","sqrt(15)/4"]},{"inner_sheet":inner,"witness":p})

N=3;s=1.5;a=2;r0=1;C=1;alpha=.08;theta=.7;phi=1.1
A=np.array([1,.7*np.exp(.6j),.4*np.exp(-.4j)]);b=np.array([0,.8,1.7])
r=r0*s**np.arange(N);R=a*r
D=R*R+r*r+C*C+2*R*r*np.cos(theta)-2*C*(R+r*np.cos(theta))*np.cos(phi)
w=A*np.exp(-alpha*D)
phases=np.linspace(0,np.pi,601)
direct=np.abs(np.sum(w[:,None]*np.cos(phases[None,:]+b[:,None]),axis=0))**2
sample=np.array([0,np.pi/4,np.pi/2])
values=np.abs(np.sum(w[:,None]*np.cos(sample[None,:]+b[:,None]),axis=0))**2
c0=(values[0]+values[2])/2;c1=(values[0]-values[2])/2;c2=values[1]-c0
rec=c0+c1*np.cos(2*phases)+c2*np.sin(2*phases)
fig,ax=plt.subplots(figsize=(7.2,3.4),layout="constrained")
ax.plot(phases/np.pi,direct,c=BLUE,lw=2,label="direct common-angle sum")
ax.plot(phases[::15]/np.pi,rec[::15],".",c=ORANGE,ms=4,label="three-sample reconstruction")
ax.scatter(sample/np.pi,values,c=TEAL,s=45,zorder=4,label="samples")
ax.set(xlabel=r"prescribed phase $\Phi/\pi$",ylabel=r"intensity $P$",xlim=(-.015,1.015))
ax.legend(loc="upper center")
keep("phase",fig,{"N":N,"s":s,"r0":r0,"a":a,"R0":a*r0*s**(N/2),"C":C,"alpha":alpha,
 "A_real":A.real.tolist(),"A_imag":A.imag.tolist(),"b":b.tolist(),"theta":theta,"phi":phi},
 {"phases":phases,"direct":direct,"reconstructed":rec,"sample_phases":sample,"sample_values":values,"c":[c0,c1,c2]})

k=np.array([0,.4,1,3]);q=np.array([0,1,4,7]);z=np.array([.6,-1,0,.5]);eps=1e-9
h1=max(abs(z))+eps;h2=2+eps;rr=k/(1+k)
old=np.c_[rr*np.cos(np.pi*z/(2*h1)),rr*np.sin(np.pi*z/(2*h1))]
new=np.c_[rr*np.cos(np.pi*z/(2*h2)),rr*np.sin(np.pi*z/(2*h2))]
fig,axs=plt.subplots(1,2,figsize=(8.9,3.5),layout="constrained")
ax=axs[0];ax.scatter(*old.T,c=BLUE,label="original normalization");ax.scatter(*new.T,c=ORANGE,marker="x",label="after append")
for i,(p0,p1) in enumerate(zip(old,new)):
    ax.annotate("",p1,xytext=p0,arrowprops={"arrowstyle":"->","color":GRAY})
    ax.annotate(str(i),p0,xytext=(5,4),textcoords="offset points")
axes_plane(ax,r"$\rho-R$");ax.set_ylabel("display height Z")
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.22),frameon=False)
zg=np.linspace(-1,1,101);axs[1].plot(zg,np.pi*zg/(2*h1),c=BLUE,label="H = 1 + epsilon");axs[1].plot(zg,np.pi*zg/(2*h2),c=ORANGE,label="H = 2 + epsilon")
axs[1].set(xlabel="stored scalar z",ylabel=r"tube angle $\chi$ (radians)");axs[1].legend()
keep("history",fig,{"R":2,"rmax":1,"M":12,"epsilon":eps,"append":[1,2,2],"H_before":h1,"H_after":h2},
 {"kappa":k,"q":q,"z":z,"before_tube_plane":old,"after_tube_plane":new})

fig,axs=plt.subplots(1,2,figsize=(8.8,3.8),layout="constrained")
ax=axs[0];Rc=2;r0c=.6;cc=.4;rc=3.4
ax.plot(Rc+r0c*np.cos(t),r0c*np.sin(t),c=BLUE,label="background meridians")
ax.plot(-Rc+r0c*np.cos(t),r0c*np.sin(t),c=BLUE)
ax.plot(Rc+rc*np.cos(t),rc*np.sin(t),c=ORANGE,ls="--",label="channel radius 3.4")
ax.scatter([-1.4],[0],c="black",zorder=5)
ax.annotate("nonzero witness",(-1.4,0),xytext=(.7,-1.2),arrowprops={"arrowstyle":"-"},fontsize=9)
axes_plane(ax,"signed anchor projection u")
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=8)
rhos=np.linspace(3.4,4.6,601)
cosine=(r0c*r0c-4*Rc*Rc-rhos*rhos)/(4*Rc*rhos)
ang=np.arccos(np.clip(cosine,-1,1))
axs[1].plot(rhos,ang/np.pi,c=TEAL,label=r"$\theta/\pi$")
axs[1].plot(rhos,2-ang/np.pi,c=TEAL,ls="--",label=r"$2-\theta/\pi$")
axs[1].set(xlabel=r"channel tube radius $\rho_c$",ylabel=r"re-entry phase / $\pi$")
axs[1].legend()
keep("channel",fig,{"R":Rc,"r0":r0c,"c":cc,"anchor":0,"witness_Omega":"-(exp(35/3)-1)"},
 {"rho":rhos,"reentry_phase":ang,"witness":[-1.4,0,0]})

(OUT/"FIGURE_RECORD.json").write_text(json.dumps({"python":sys.version,"platform":platform.platform(),
 "numpy":np.__version__,"matplotlib":matplotlib.__version__,"figures":records},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figures":len(records),"names":list(records),"max_phase_reconstruction_error":float(np.max(abs(direct-rec)))}))
