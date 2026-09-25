"""Render the verified stored coordinates; no model runs or refitting."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from verify_crystal_geometry import HERE

plt.rcParams.update({"font.size":10,"axes.titlesize":12,"figure.facecolor":"white",
                     "axes.spines.top":False,"axes.spines.right":False,"savefig.dpi":180})
host=json.loads((HERE/"HOST_GEOMETRY.json").read_text(encoding="utf8"))
cand=json.loads((HERE/"CANONICAL_CRYSTAL_CANDIDATE.json").read_text(encoding="utf8"))
hist=json.loads((HERE/"HISTORICAL_CRYSTAL.json").read_text(encoding="utf8"))
arr=lambda pts:np.array([[float(sp.sympify(x)) for x in p] for p in pts])
panels=[arr(p["vertices"]) for p in host["panels"]]
O=arr([host["center"]])[0]
U=np.array(host["upper_targets_numeric"]);L=np.array(host["lower_targets_numeric"])
plus=np.array(cand["variants"][0]["physical_host_vertices_numeric"])
minus=np.array(cand["variants"][1]["physical_host_vertices_numeric"])
faces=cand["variants"][0]["faces"]
blue="#1565a7"; red="#ba4b23"; gray="#768696"; teal="#17847c"

def ax3(fig,pos,title,limits=None):
    ax=fig.add_subplot(pos,projection="3d")
    ax.set_title(title,pad=12);ax.set_xlabel("x");ax.set_ylabel("y");ax.set_zlabel("z")
    ax.view_init(elev=22,azim=-65)
    ax.set_box_aspect((1,1,1.1))
    for axis in (ax.xaxis,ax.yaxis,ax.zaxis):axis.set_major_locator(MaxNLocator(5))
    if limits:
        ax.set_xlim(*limits[0]);ax.set_ylim(*limits[1]);ax.set_zlim(*limits[2])
    return ax

hostlimits=[(-.56,.56),(-.1,.94),(-.56,.56)]
def draw_host(ax):
    ax.add_collection3d(Poly3DCollection(panels,facecolors=gray,edgecolors=gray,alpha=.09,linewidths=.7))
    for pts in panels:
        pp=np.vstack([pts,pts[0]])
        ax.plot(*pp.T,color=gray,linewidth=.8,alpha=.65)
    ax.plot([O[0]]*2,[O[1]]*2,[-.55,.55],":",color=gray,linewidth=.8)

def mesh(ax,v,f,alpha=.16):
    ax.add_collection3d(Poly3DCollection([v[x] for x in f[:12]],facecolor=teal,edgecolor=teal,alpha=alpha,linewidth=.6))
    ax.add_collection3d(Poly3DCollection([v[x] for x in f[12:]],facecolor=blue,edgecolor=blue,alpha=alpha,linewidth=.7))
    ax.scatter(*v[12:15].T,c=blue,s=28,depthshade=False)
    ax.scatter(*v[15:18].T,c=red,s=28,depthshade=False)

def planar(ax,title):
    ax.set_title(title);ax.set_aspect("equal");ax.set_xlabel("x");ax.set_ylabel("y");ax.grid(alpha=.15)
    for p in panels:
        ax.plot(p[[1,2],0],p[[1,2],1],color=gray,lw=2)
    ax.scatter([O[0]],[O[1]],color="black",marker="+",s=50)
def triangle(ax,p,color,style="-",label=None):
    q=np.vstack([p,p[0]])
    ax.plot(q[:,0],q[:,1],style,color=color,lw=1.2,label=label)
    ax.scatter(p[:,0],p[:,1],c=color,s=35,zorder=4)

def save(fig,name,caption):
    fig.text(.5,.025,caption,ha="center",va="bottom",fontsize=9,color="#344451")
    fig.savefig(HERE/name,bbox_inches="tight");plt.close(fig)

fig=plt.figure(figsize=(11,5.7))
ax=ax3(fig,121,"Accepted Paper C host and confirmed contacts",hostlimits);draw_host(ax)
ax.scatter(*U.T,c=blue,s=45,label="Upper edge centers")
ax.scatter(*L.T,c=red,s=45,label="Lower edge centers")
for k in range(3):
    ax.text(*(U[k]+[.015,0,.025]),f"U{k}",color=blue)
    ax.text(*(L[k]+[.015,0,-.055]),f"L{k}",color=red)
ax.legend(fontsize=8,loc="upper left")
ax=fig.add_subplot(122);planar(ax,"Axial projection: upper/lower centers coincide")
triangle(ax,U,blue,label="Both triples")
for k in range(3):ax.text(U[k,0]+.012,U[k,1]+.015,f"U{k} / L{k}")
ax.set_xlim(-.57,.57);ax.set_ylim(-.08,.92)
save(fig,"01_host_targets.png","Width = 1. Target planes z = +/-1/2; triangle side = 1/2; no upper/lower angular stagger.")

fig=plt.figure(figsize=(11,6))
v=np.array(hist["vertices"]);v=np.column_stack([v[:,0],-v[:,2],v[:,1]])
ax=ax3(fig,121,"HISTORICAL_AS_CODED\n(rigid reorientation only)",[(-.65,.65),(-.65,.65),(-1,1)])
ax.add_collection3d(Poly3DCollection([v[x] for x in hist["faces"]],facecolor=teal,edgecolor="#626262",alpha=.15,linewidth=.6))
ax.scatter(*v[12:18].T,c=red,s=25);ax.set_zlabel("historical Y")
ax.text2D(.02,.91,"18 V / 60 E / 30 F\n12 crossing pairs; not a surface",transform=ax.transAxes,fontsize=9,bbox={"facecolor":"white","edgecolor":"none","alpha":.9})
ax=ax3(fig,122,"NEW CANDIDATE\n(canonical half-height H = 1)",[(-1,1),(-1,1),(-1,1)])
cv=np.array(cand["variants"][0]["canonical_vertices_numeric"]);mesh(ax,cv,faces)
ax.text2D(.02,.91,"18 V / 42 E / 24 F\nEmbedded open annulus; C3",transform=ax.transAxes,fontsize=9,bbox={"facecolor":"white","edgecolor":"none","alpha":.9})
save(fig,"02_historical_vs_canonical.png","Different constructions, not a uniform rescale. Candidate uses t = (sqrt(2)-1)/4 solely as an illustration.")

fig=plt.figure(figsize=(10,5.5))
ax=fig.add_subplot(121);planar(ax,"Upper tips coincide with edge centers")
triangle(ax,U,blue,label="U = fitted upper tips")
ax.legend(loc="upper left",fontsize=9)
ax.set_xlim(-.45,.45);ax.set_ylim(-.08,.62)
ax=fig.add_subplot(122);ax.axis("off")
ax.text(.02,.9,
        "EXACT UPPER REGISTRATION\n\nCanonical apex height: +1\nHost target height: +1/2\nPhysical scale: 1/2\n\nCanonical upper radius: 1/sqrt(3)\nPhysical upper radius: sqrt(3)/6\n\nAll three residuals: exactly 0\n\nThis leaves contraction/offset freedom.\nNeither 22.5 degrees nor a unique alpha\nis selected by these contacts.",
        va="top",linespacing=1.6)
save(fig,"03_upper_registration.png","The registration follows from the exact host coordinates, not from screen measurements or fitting.")

fig=plt.figure(figsize=(11,5.5))
ax=fig.add_subplot(121);planar(ax,"Predicted lower tips remain on lower edges")
triangle(ax,L,gray,"--",label="Lower edge centers")
triangle(ax,plus[15:18],red,label="Predicted lower tips")
for k in range(3):
    ax.annotate("",xy=plus[15+k,:2],xytext=L[k,:2],arrowprops={"arrowstyle":"->","color":red})
ax.legend(fontsize=8,loc="upper left");ax.set_xlim(-.46,.46);ax.set_ylim(-.09,.66)
ax=fig.add_subplot(122);ax.axis("off")
w=cand["illustrative_witness"]
ax.text(.02,.9,
        "LOWER PREDICTION: NO SECOND FIT\n\nB_k = L_k - t J n_k\n0 < t <= (sqrt(2)-1)/2\n\nDistance from corresponding center = t\nDistance from the lower edge = 0\n\nILLUSTRATED WITNESS ONLY\n"
        f"t = {w['lower_residual_numeric']:.9f}\nalpha = {w['alpha_numeric']:.9f}\ndelta = {w['delta_degrees_numeric']:.6f} degrees\n\nExact lower-center alignment requires t = 0,\nwhich removes the strict contraction/offset.",
        va="top",linespacing=1.55)
save(fig,"04_lower_prediction.png","Exact edge membership and exact center alignment are different claims. Lower-center alignment is RESIDUAL.")

fig=plt.figure(figsize=(11,5.7))
for pos,v,name in [(121,plus,"TWIST_PLUS"),(122,minus,"TWIST_MINUS")]:
    ax=ax3(fig,pos,name,hostlimits);draw_host(ax);mesh(ax,v,faces)
    for i in range(6):
        ax.plot(*v[[i,6+(i+1)%6]].T,color=teal,lw=1.8)
save(fig,"05_twist_plus_minus.png","Exact mirror pair under x -> -x. Same host contacts and clearance; no preferred handedness.")

fig=plt.figure(figsize=(11,6))
ax=ax3(fig,121,"Full host embedding: one exact witness",hostlimits);draw_host(ax);mesh(ax,plus,faces,.23)
ax=fig.add_subplot(122);planar(ax,"Axial view: upper footprint contracts and rotates")
for start,color,label in [(0,blue,"Upper ring"),(6,red,"Lower ring")]:
    pp=plus[start:start+6];pp=np.vstack([pp,pp[0]])
    ax.plot(pp[:,0],pp[:,1],color=color,lw=1.5,label=label)
triangle(ax,plus[12:15],blue,":",label="Upper apex triangle")
triangle(ax,plus[15:18],red,":",label="Lower apex triangle")
for i in range(6):
    ax.plot(plus[[i,6+(i+1)%6],0],plus[[i,6+(i+1)%6],1],color=teal,alpha=.5,lw=.8)
ax.set_xlim(-.49,.49);ax.set_ylim(-.09,.68);ax.legend(fontsize=8,loc="upper left")
save(fig,"06_full_host_embedding.png","All candidate faces stay in the host's inward panel halfspaces. The Paper C shell itself is open, not a closed container.")
print("Rendered six research figures from stored verified coordinates.")
