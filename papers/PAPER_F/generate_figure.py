"""Figure 1: accepted equations (6), (7), (17), (25); no model evolution."""
from pathlib import Path
import json,datetime
import numpy as np
import sympy as s
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
ROOT=Path(__file__).resolve().parent
OUT=ROOT/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Serif","font.size":10,"svg.hashsalt":"paper-f-v02","pdf.fonttype":42,"ps.fonttype":42,"axes.titleweight":"bold"})
u=s.Matrix([1,-1,0])/s.sqrt(2);v=s.Matrix([1,1,-2])/s.sqrt(6)
def orbit(seed,projective=False,conjugation=False):
 mod=6 if projective else 12
 found={seed};todo=[seed]
 while todo:
  k=todo.pop()
  for j in [(k+4)%mod,(6-k)%mod]+([(k+6)%mod] if conjugation else []):
   if j not in found:found.add(j);todo.append(j)
 return sorted(found)
orbits=[orbit(0),orbit(3),orbit(1)]
assert orbits==[[0,2,4,6,8,10],[3,7,11],[1,5,9]]
inputs={"source_equations":[6,7,17,25],"basis_u":[str(x) for x in u],"basis_v":[str(x) for x in v],
 "circle":"q(phi)=u*cos(phi)+v*sin(phi)","P":"k -> k+4 (mod 12)","T":"k -> 6-k (mod 12)","conjugation":"k -> k+6 (mod 12)",
 "D3_oriented_orbits":orbits,"D6_oriented_orbits":[orbit(0,conjugation=True),orbit(1,conjugation=True)],
 "D3_projective_orbits":[orbit(0,True),orbit(1,True)],"roots":[],"new_model_runs":0}
for k in range(12):
 phi=s.pi*k/6
 inputs["roots"].append({"k":k,"phi":str(phi),"uv":[str(s.cos(phi)),str(s.sin(phi))],"channel_q":[str(s.simplify(x)) for x in u*s.cos(phi)+v*s.sin(phi)]})
(OUT/"figure_1_exact_inputs.json").write_text(json.dumps(inputs,indent=2)+"\n")
colors=["#21618c","#b35314","#704390"];markers=["o","s","^"]
fig,axs=plt.subplots(1,2,figsize=(7.4,4.35))
theta=np.linspace(0,2*np.pi,721)
for ax in axs:
 ax.set_aspect("equal");ax.set_xlim(-1.4,1.4);ax.set_ylim(-1.4,1.4)
 ax.plot(np.cos(theta),np.sin(theta),color="#808080",lw=.9)
 for dx,dy in [(1.31,0),(0,1.31)]:
  ax.annotate("",xy=(dx,dy),xytext=(-dx/1.2,-dy/1.2),arrowprops={"arrowstyle":"->","color":"#777777","lw":.6})
 ax.text(1.32,-.14,r"$u$",fontsize=11);ax.text(.08,1.27,r"$v$",fontsize=11)
 ax.axis("off")
axs[0].set_title(r"(a) Oriented circle: $D_3$",fontsize=12,pad=12)
for inds,col,mark in zip(orbits,colors,markers):
 ang=np.array(inds)*np.pi/6
 axs[0].scatter(np.cos(ang),np.sin(ang),s=47,c=col,marker=mark,zorder=4)
 for k,ph in zip(inds,ang):
  axs[0].text(1.15*np.cos(ph),1.15*np.sin(ph),str(k),ha="center",va="center",fontsize=9,color=col)
axs[0].text(0,.13,r"$q(\phi)=u\cos\phi+v\sin\phi$",ha="center",fontsize=10)
axs[0].text(0,-.14,r"$\phi=k\pi/6$",ha="center",fontsize=10)
axs[0].legend([Line2D([0],[0],color=c,marker=m,lw=0,markersize=6) for c,m in zip(colors,markers)],
 [r"$u$-type: 6",r"$v$-type: 3",r"opposite $v$: 3"],loc="upper center",bbox_to_anchor=(.5,-.03),frameon=False,ncol=1,fontsize=9,handletextpad=.3,labelspacing=.35)
axs[1].set_title(r"(b) Projective axes: $q\sim-q$",fontsize=12,pad=12)
for k in range(6):
 ph=k*np.pi/6;x,y=np.cos(ph),np.sin(ph)
 col=colors[0] if k%2==0 else colors[1]
 axs[1].plot([-x,x],[-y,y],color=col,lw=1.5,ls="-" if k%2==0 else "--")
 axs[1].text(1.15*x,1.15*y,str(k),ha="center",va="center",color=col,fontsize=9)
axs[1].legend([Line2D([0],[0],color=colors[0],lw=1.5),Line2D([0],[0],color=colors[1],lw=1.5,ls="--")],
 [r"$\{0,2,4\}$: 3 axes",r"$\{1,3,5\}$: 3 axes"],loc="upper center",bbox_to_anchor=(.5,-.03),frameon=False,fontsize=9,labelspacing=.35)
fig.subplots_adjust(left=.015,right=.985,top=.90,bottom=.25,wspace=.07)
fig.text(.5,.025,r"Conjugation: $k\mapsto k+6$       $D_3\longrightarrow D_6$: oriented sizes $6+6$",ha="center",fontsize=10)
epoch=datetime.datetime(2026,9,25,tzinfo=datetime.timezone.utc)
fig.savefig(OUT/"figure_1_transverse_symmetry.pdf",metadata={"Title":"Intrinsic transverse symmetry","Author":"Hilmir Frímann Halldórsson","CreationDate":epoch,"ModDate":epoch})
fig.savefig(OUT/"figure_1_transverse_symmetry.svg",metadata={"Date":"2026-09-25","Creator":"Equation-generated Paper F publication figure"})
fig.savefig(OUT/"figure_1_transverse_symmetry.png",dpi=300)
plt.close(fig)
print(json.dumps({"D3":orbits,"D6":inputs["D6_oriented_orbits"],"projective":inputs["D3_projective_orbits"]}))
