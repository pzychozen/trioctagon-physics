"""Five deterministic, vector-PDF scientific figures; no model evolution."""
from pathlib import Path
import sys, os, datetime, json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR",str(ROOT/".build/matplotlib"))
deps=ROOT/".build/plotdeps"
if deps.exists(): sys.path.insert(0,str(deps))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from accepted_coordinates import centres,normals,tangents,ez,polygons,local,compare_source
OUT=ROOT/"figures"
OUT.mkdir(exist_ok=True)
INK="#233241"; BLUE="#205e92"; TEAL="#137a75"; GOLD="#ae7016"; GRAY="#79838d"
COL=[BLUE,TEAL,GOLD]
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.titlesize":11,
 "axes.labelsize":10,"pdf.fonttype":42,"ps.fonttype":42,"svg.fonttype":"none",
 "svg.hashsalt":"paper-b-v0.1","text.color":INK,"axes.labelcolor":INK,
 "axes.edgecolor":"#c4cbd1","savefig.facecolor":"white"})
date=datetime.datetime(2026,9,23,tzinfo=datetime.timezone.utc)
meta={"Title":"Triadic Chirality and Orientation Geometry",
      "Author":"Hilmir Frímann Halldórsson","Creator":"Paper B reproducible figure source",
      "CreationDate":date,"ModDate":date}
C=np.array([list(x) for x in centres],float)
N=np.array([list(x) for x in normals],float)
T=np.array([list(x) for x in tangents],float)
Z=np.array(list(ez),float)
POL=[np.array([list(v) for v in poly],float) for poly in polygons]
UV=np.array(local,float)
def save(fig,name):
    fig.savefig(OUT/(name+".pdf"),bbox_inches="tight",pad_inches=.12,metadata=meta)
    fig.savefig(OUT/(name+".png"),dpi=220,bbox_inches="tight",pad_inches=.12)
    plt.close(fig)
def arrow(ax,start,end,color=INK,style="-|>",lw=1.7,rad=0):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle=style,mutation_scale=12,
                  linewidth=lw,color=color,connectionstyle=f"arc3,rad={rad}"))
def shell(ax,faces=(0,1,2),frames=False):
    for i in faces:
        ax.add_collection3d(Poly3DCollection([POL[i]],facecolors=COL[i],alpha=.14,
                            edgecolors=COL[i],linewidths=1.1))
        ax.scatter(*C[i],color=COL[i],s=15)
        pos=C[i]+.10*N[i]+.25*Z
        ax.text(*pos,"ABC"[i],color=COL[i],weight="bold",fontsize=12)
        if frames:
            for vec,color,label in [(N[i],INK,"n"),(T[i],COL[i],"t"),(Z,GRAY,"e_z")]:
                ax.quiver(*C[i],*(.23*vec),color=color,linewidth=1.3,arrow_length_ratio=.2)
                if label=="e_z" and i!=1: continue
                end=C[i]+.29*vec
                txt="$"+label+"_"+"ABC"[i]+"$" if label!="e_z" else "$e_z$"
                ax.text(*end,txt,color=color,fontsize=9)
    ax.set(xlim=(-.8,.8),ylim=(-.3,1.1),zlim=(-.6,.6))
    ax.set_box_aspect((1.5,1.3,1.15));ax.view_init(elev=26,azim=-90)
    ax.set_proj_type("ortho");ax.set_axis_off()
def section(ax,frame=False):
    corners=np.array([[-.5,0],[.5,0],[0,np.sqrt(3)/2],[-.5,0]])
    ax.plot(*corners.T,color=GRAY,lw=1.0)
    for i,c in enumerate(C):
        ax.scatter(*c[:2],color=COL[i],s=30,zorder=4)
        off=.075*N[i,:2] if not frame else -.07*N[i,:2]
        ax.text(*(c[:2]+off),"ABC"[i],ha="center",va="center",color=COL[i],weight="bold")
        if frame:
            for d,label,color in [(N[i,:2],"n",INK),(T[i,:2],"t",COL[i])]:
                arrow(ax,c[:2],c[:2]+.25*d,color)
                ax.text(*(c[:2]+.33*d),"$"+label+"_"+"ABC"[i]+"$",ha="center",va="center",color=color)
    ax.set_aspect("equal");ax.set_xlim(-.84,.84);ax.set_ylim(-.45,1.05);ax.set_axis_off()
def plane(ax,limits=(-.61,.61),outline=True):
    if outline: ax.add_patch(Polygon(UV,closed=True,facecolor="#f3f6f8",edgecolor="#aebac3",lw=1))
    arrow(ax,(limits[0],0),(limits[1],0),GRAY,lw=.9)
    arrow(ax,(0,limits[0]),(0,limits[1]),GRAY,lw=.9)
    ax.text(limits[1]-.02,-.045,"$q$  ($t_B$)",ha="right",fontsize=10)
    ax.text(.018,limits[1]-.02,"$p$  ($e_z$)",va="top",fontsize=10)
    ax.set_aspect("equal");ax.set_xlim(*limits);ax.set_ylim(*limits);ax.set_axis_off()
evidence=compare_source()
fig=plt.figure(figsize=(8.0,3.8),layout="constrained")
ax=fig.add_subplot(121,projection="3d");shell(ax,frames=True)
ax.set_title("(a) Folded octagons and frames",pad=0)
ax=fig.add_subplot(122);section(ax,True)
ax.text(-.75,-.40,"$e_z$ points out of this section",fontsize=9)
ax.set_title("(b) Exact central section, $z=0$")
save(fig,"figure_1_folded_frames")
fig,ax=plt.subplots(figsize=(5.25,4.2),layout="constrained");plane(ax)
v=np.array([.30,.12]);jv=np.array([-v[1],v[0]])
d=np.pi/4;rot=np.array([[np.cos(d),-np.sin(d)],[np.sin(d),np.cos(d)]])@v
for w,c,l,off in [(v,BLUE,"$v$",(.025,-.018)),(jv,TEAL,"$Jv$",(-.07,.02)),
                  (rot,GOLD,r"$e^{i\delta}v$",(.025,.01))]:
    arrow(ax,(0,0),w,c,lw=2);ax.text(*(w+off),l,color=c,fontsize=12)
ax.plot([v[0],v[0]],[0,v[1]],ls=":",color=BLUE)
ax.plot([0,v[0]],[v[1],v[1]],ls=":",color=BLUE)
ang=np.arctan2(v[1],v[0]);pts=np.linspace(ang,ang+d,40)
ax.plot(.20*np.cos(pts),.20*np.sin(pts),color=GOLD,lw=1.1)
ax.text(.13,.19,r"$\delta$",color=GOLD)
ax.text(-.49,-.44,r"$J(q,p)=(-p,q)$",fontsize=11)
ax.text(-.49,.43,r"$t_B\times e_z=n_B$",fontsize=10)
save(fig,"figure_2_complex_plane")
fig=plt.figure(figsize=(8.0,3.6),layout="constrained")
ax=fig.add_subplot(121,projection="3d");shell(ax,(0,1))
for i in (0,1):
    w=.28*T[i]+.20*Z
    ax.quiver(*C[i],*w,color=COL[i],linewidth=2.5,arrow_length_ratio=.17)
    ax.text(*(C[i]+w+.025*Z),r"$T_{AB}v_B$" if i==0 else "$v_B$",color=COL[i],fontsize=10)
ax.set_title("(a) Free vectors at their face centres")
ax=fig.add_subplot(122);plane(ax,(-.12,.48),outline=False)
arrow(ax,(0,0),(.28,.20),BLUE,lw=3)
ax.plot([.28,.28],[0,.20],ls=":",color=GRAY);ax.plot([0,.28],[.20,.20],ls=":",color=GRAY)
ax.text(.19,.245,r"$(0.28,0.20)$",fontsize=10)
ax.text(.23,.36,r"$E_A(T_{AB}v_B)$"+"\n"+r"$=E_B(v_B)$",fontsize=11,ha="center")
ax.text(-.10,-.10,"Same pair in both oriented frames",fontsize=9)
ax.set_title("(b) Component preservation")
save(fig,"figure_3_transport")
fig,ax=plt.subplots(figsize=(5.25,4.2),layout="constrained");plane(ax)
u=np.array([.30,.08]);w=np.array([.10,.28])
ax.add_patch(Polygon([(0,0),u,u+w,w],facecolor="#bcded5",edgecolor=TEAL,alpha=.65,lw=1))
arrow(ax,(0,0),u,BLUE,lw=2);arrow(ax,(0,0),w,TEAL,lw=2)
ax.text(.305,.055,"$v_B$",color=BLUE,fontsize=12)
ax.text(.035,.315,r"$T_{BC}v_C$",color=TEAL,fontsize=12)
ax.text(.22,.225,r"$+\mathcal{A}_{BC}$",ha="center",fontsize=12,color=TEAL)
ax.text(-.48,-.43,r"$0.30(0.28)-0.08(0.10)=0.076$",fontsize=10,bbox=dict(facecolor="white",edgecolor="none",alpha=.92))
ax.text(-.48,.43,r"$n_B$ toward reader; positive $(q,p)$ orientation",fontsize=9,bbox=dict(facecolor="white",edgecolor="none",alpha=.92))
save(fig,"figure_4_signed_area")
fig,axes=plt.subplots(1,3,figsize=(8.4,4.25),layout="constrained")
titles=[r"$C_3$: cyclic rotation",r"$H$: horizontal mirror",r"$V$: vertical mirror"]
states=[r"$\Omega'=P\Omega$",r"$\Omega'=\overline{\Omega}$",r"$\Omega'=-S\overline{\Omega}$"]
zforms=[r"$Z'=PZ$",r"$Z'=-Z$",r"$Z'=SZ$"]
slots=["(AB, BC, CA)","-(BC, CA, AB)","(AB, CA, BC)"]
for k,ax in enumerate(axes):
    section(ax);ax.set_title(titles[k],fontsize=11);ax.set_ylim(-.88,1.08)
    if k==0:
        for i in range(3): arrow(ax,C[i,:2],C[(i+1)%3,:2],GRAY,lw=1,rad=.22)
    elif k==1: ax.text(0,.29,r"$z\mapsto-z$",ha="center",fontsize=12)
    else:
        ax.plot([0,0],[-.08,.93],ls="--",color=GRAY,lw=.8)
        arrow(ax,C[0,:2],C[2,:2],GRAY,style="<->",lw=1,rad=-.3)
    ax.text(0,-.38,states[k],ha="center",fontsize=12)
    ax.text(0,-.58,zforms[k],ha="center",fontsize=12,color=TEAL)
    ax.text(0,-.78,slots[k],ha="center",fontsize=9)
fig.supxlabel("Bottom row lists signed old pair slots in the new (BC, CA, AB) order.",fontsize=9)
save(fig,"figure_5_symmetry")
evidence.update({"matplotlib":matplotlib.__version__,"numpy":np.__version__,
 "figure_count":5,"formats":["vector PDF","220 dpi PNG"],
 "arbitrary_state_vectors":"explicit diagram fixtures only; no dynamics executed"})
(ROOT/"evidence/figure_generation.json").write_text(json.dumps(evidence,indent=2)+"\n",encoding="utf8")
print(json.dumps(evidence))
