"""Publication diagrams from the proved formulas; no production imports."""
from pathlib import Path
import json, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'mathtext.fontset':'dejavusans','pdf.fonttype':42,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
teal='#176c70';orange='#b65b2b';ink='#243543';muted='#576775';pale='#f0f5f5'
def canvas(h=3.4):
    fig,ax=plt.subplots(figsize=(7.2,h));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off');fig.subplots_adjust(left=.015,right=.985,bottom=.025,top=.98);return fig,ax
def box(ax,x,y,w,h,lines,color=teal,fs=11):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.012,rounding_size=0.018',facecolor=pale,edgecolor=color,lw=1.3))
    ax.text(x,y,lines,ha='center',va='center',color=ink,fontsize=fs,linespacing=1.65)
def arrow(ax,start,end,label='',offset=(0,.025),color=muted):
    ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color=color,lw=1.4))
    mid=np.array(start)*.5+np.array(end)*.5+np.array(offset)
    if label:ax.text(*mid,label,ha='center',va='center',fontsize=10,color=color)
def save(fig,name):
    for ext in ['pdf','svg','png']:
        fig.savefig(OUT/(name+'.'+ext),dpi=220,facecolor='white')
    plt.close(fig)

fig,ax=canvas(3.45)
for x,n,group,deg,g,other in [(.17,2,'C_2',2,0,'One rational partner'),(.50,3,'S_3',6,1,'Quadratic correspondence'),(.83,4,'S_4',24,13,'Cubic correspondence')]:
    box(ax,x,.62,.285,.51,rf'$n={n}$'+'\n'+rf'$\mathrm{{Mon}}= {group}$'+'\n'+f'Closure degree {deg}\nGenus {g}',fs=11)
    ax.text(x,.23,other,ha='center',va='center',fontsize=9.7,color=muted)
ax.text(.5,.97,'GENERIC COVERS OVER THEIR UNCHANGED TARGETS',ha='center',va='top',fontsize=10,color=teal,weight='bold')
ax.text(.5,.07,r'Paper I: the larger quadratic quotient/lift tower is a separate extension.',ha='center',fontsize=9.1,color=ink)
save(fig,'01_hierarchy')

fig,ax=canvas(3.2)
for x,j in [(.18,0),(.5,1),(.82,2)]:
    for y,eps in [(.79,1),(.54,-1)]:
        box(ax,x,y,.22,.15,f'({j}, {(j+eps)%3})',teal if eps==1 else orange,fs=14)
    arrow(ax,(x-.065,.43),(x,.26))
    arrow(ax,(x+.065,.43),(x,.26))
    ax.text(x,.18,str(j),ha='center',va='center',fontsize=17,color=ink)
ax.text(.5,.99,'SIX ORDERED PAIRS OF DISTINCT SHEETS',ha='center',va='top',fontsize=10,color=teal,weight='bold')
ax.text(.5,.035,'Projection to first entry: three sheets, each with a two-point fiber',ha='center',fontsize=10,color=muted)
save(fig,'02_incidence')

fig,ax=canvas(4.1)
box(ax,.22,.85,.26,.14,r'$E$',fs=16);box(ax,.76,.85,.29,.14,r"$E'=E/C_3$",fs=15)
box(ax,.22,.47,.26,.14,r'$\mathbb{P}^1_z$',fs=15);box(ax,.76,.47,.29,.14,r'$\mathbb{P}^1_w$',fs=15)
arrow(ax,(.36,.85),(.60,.85),'3-isogeny',offset=(0,.055))
arrow(ax,(.36,.47),(.60,.47),'degree 3',offset=(0,-.067))
arrow(ax,(.22,.765),(.22,.555),'2',offset=(-.04,0))
arrow(ax,(.76,.765),(.76,.555),'2',offset=(.04,0))
ax.text(.5,.22,'FORGETTING MARKINGS',ha='center',fontsize=9.5,color=teal,weight='bold')
for x,label in [(.17,r'$t\in X_0(6)$'),(.50,r'$h\in X_0(3)$'),(.83,r'$j(E)\in X(1)$')]:ax.text(x,.095,label,ha='center',va='center',fontsize=12,color=ink)
arrow(ax,(.29,.095),(.37,.095),'3',offset=(0,.05));arrow(ax,(.63,.095),(.70,.095),'4',offset=(0,.05))
save(fig,'03_moduli_tower')

fig,ax=canvas(4.0)
rows=[(.86,r'$qr\ne0,9ps$','Smooth closure',r'$S_3$; genus 1',teal),(.65,'Exactly one of q, r = 0','Nodal correspondence',r'$S_3$; normalization genus 0',orange),(.44,r'$q=r=0$ or $qr=9ps$','Split correspondence',r'$C_3$ specialized cover',orange),(.23,r'$ps(ps-qr)=0$','Cancellation','Reduced degree at most 2',muted)]
for y,a,b,c,col in rows:
    ax.plot([.02,.98],[y-.084,y-.084],color='#d4dddd',lw=.7)
    ax.text(.03,y,a,ha='left',va='center',fontsize=10,color=col)
    ax.text(.38,y,b,ha='left',va='center',fontsize=9.8,color=ink)
    ax.text(.71,y,c,ha='left',va='center',fontsize=8.8,color=ink)
ax.text(.5,.99,'CUBIC STRATA IN THE COEFFICIENT CHART',ha='center',va='top',fontsize=10,color=teal,weight='bold')
ax.text(.5,.925,r'First three rows assume $ps(ps-qr)\ne0$.',ha='center',fontsize=8.7,color=muted)
ax.text(.5,.055,r'Normalized cusps:  $t=0,1,9,\infty$     |     $j(E)$ pole orders:  $1,6,2,3$',ha='center',fontsize=10,color=muted)
save(fig,'04_boundaries')

fig=plt.figure(figsize=(7.2,3.6));left=fig.add_axes([.01,.12,.45,.8],projection='3d');right=fig.add_axes([.48,.04,.5,.92]);right.set(xlim=(0,1),ylim=(0,1));right.axis('off')
d=1-np.sqrt(2)/2;h0=(np.sqrt(2)-1)/2;r0=1/np.sqrt(3)
for j in range(3):
    angle=2*np.pi*j/3;u=np.array([-np.sin(angle),np.cos(angle),0.]);v=np.array([-np.cos(angle),-np.sin(angle),0.])
    for eps in [1,-1]:
        pts=np.array([r0*u+np.array([0,0,eps*h0]),(r0-np.sqrt(3)*d/2)*u+d*v/2+np.array([0,0,eps*(h0+d)]),(r0-np.sqrt(3)*d/2)*u-d*v/2+np.array([0,0,eps*(h0+d)])])
        col=teal if eps==1 else orange
        left.add_collection3d(Poly3DCollection([pts],facecolors=col,edgecolors=col,alpha=.6,linewidths=1))
        center=pts.mean(axis=0);left.text(*(center+.10*u+np.array([0,0,.10*eps])),f'{j}{"+" if eps==1 else "-"}',fontsize=9,ha='center',color=col)
    left.plot([r0*u[0]]*2,[r0*u[1]]*2,[-h0,h0],color='#b6c1c4',lw=.8,ls=':')
left.set(xlim=(-.65,.65),ylim=(-.65,.65),zlim=(-.65,.65));left.set_box_aspect((1,1,1));left.view_init(24,22);left.set_axis_off();left.set_title('Existing finite patches',fontsize=10,color=ink,pad=0)
right.text(.5,.91,r'$\mathcal{P}_j^\epsilon\ \longleftrightarrow\ (j,j+\epsilon)$',ha='center',fontsize=15,color=teal)
right.text(.5,.73,r'$R: (j,\epsilon)\mapsto(j+1,\epsilon)$'+'\n'+r'$S: (j,\epsilon)\mapsto(-j,-\epsilon)$',ha='center',va='center',fontsize=11,linespacing=1.8,color=ink)
box(right,.5,.46,.88,.17,'Exact regular $S_3$-set\nwith its three-pair quotient',fs=10)
right.text(.5,.23,'The same finite incidence occurs\nfor every smooth cubic modulus.',ha='center',fontsize=10,color=muted,linespacing=1.5)
right.text(.5,.075,'No branch divisor is selected.',ha='center',fontsize=10,color=orange)
save(fig,'05_finite_bridge')

record={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.glob('*'))}
(ROOT/'records/figure_manifest.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print('Generated 5 figures, each in PDF/SVG/PNG.')
