"""Nine deterministic construction figures from exact symbolic coordinates."""
import runtime
from runtime import ROOT
from geometry_coordinates import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import json,hashlib
OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':11,'svg.fonttype':'none','svg.hashsalt':'PaperD-v0.1-20260923','pdf.fonttype':42,'savefig.facecolor':'white'})
EDGE='#176b91';GAP='#bb592b';INK='#253541';PALE='#e7eff3';GOLD='#efd298'
def xy(points):return np.array([[float(S.N(v)) for v in p] for p in points])
def line(ax,points,**kw):
    a=xy(points);ax.plot(a[:,0],a[:,1],**kw)
def base(ax):ax.set_aspect('equal');ax.axis('off');ax.margins(.16)
def shell(ax,d,labels=False):
    h=d['H'];ax.add_patch(Polygon(xy(h),color=PALE,zorder=0))
    for k in range(6):
        line(ax,[h[k],h[(k+1)%6]],color=EDGE if k%2==0 else GAP,lw=2.6,ls='-' if k%2==0 else '--')
        if labels:
            q=xy([(h[k]+h[(k+1)%6])/2])[0]*1.18
            ax.text(*q,('$E_'+str(k//2)+'$' if k%2==0 else '$G_'+str(k//2)+'$'),ha='center',va='center',color=EDGE if k%2==0 else GAP)
def corners(ax,d):
    for i in range(3):ax.add_patch(Polygon(xy([d['B'][i],d['V'][i],d['A'][(i+1)%3]]),facecolor=GOLD,edgecolor=GAP,lw=1,alpha=.8))
    line(ax,d['V']+[d['V'][0]],color=INK,lw=.9)
registry=[]
def save(fig,name,description):
    fig.savefig(OUT/(name+'.pdf'),bbox_inches='tight',metadata={'CreationDate':None,'ModDate':None})
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
    fig.savefig(OUT/(name+'.png'),dpi=210,bbox_inches='tight')
    plt.close(fig);registry.append({'id':name,'description':description,'construction_only':True})

fig,ax=plt.subplots(figsize=(6.8,4.4));base(ax)
o=octagon(1);a,w,R=metrics(1)
ax.add_patch(Polygon(xy(o),facecolor=PALE,edgecolor=INK,lw=1.5))
line(ax,[o[4],o[5]],color=EDGE,lw=3)
line(ax,[S.zeros(2,1),S.Matrix([-a,0])],color=GAP,lw=1.4)
line(ax,[S.zeros(2,1),o[1]],color=GAP,lw=1.4,ls='--')
ax.text(-float(a)/2,.09,'$a$',ha='center');ax.text(.65,.35,'$R_{oct}$')
ax.text(-float(a)-.12,0,'$s$',ha='right');ax.text(0,-float(a)-.22,'width $w=2a$',ha='center')
ax.annotate('',xy=(float(a)+.4,0),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'gray'})
ax.annotate('',xy=(0,float(a)+.4),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'gray'})
ax.text(float(a)+.48,0,'$x$',ha='left',va='center');ax.text(0,float(a)+.45,'$y$',ha='center',va='bottom')
ax.set_xlim(-1.8,1.9);ax.set_ylim(-1.7,1.8)
save(fig,'01_octagon_metrics','Local octagon, inward selected edge, apothem, circumradius and width.')

fig,ax=plt.subplots(figsize=(6.8,4.6));base(ax);d=scaffold(1,S.Rational(3,5))
for i in range(3):
    line(ax,[S.zeros(2,1),d['p']*U[i]],color='gray',ls=':',lw=1)
    line(ax,[d['A'][i],d['B'][i]],color=EDGE,lw=3)
    for name,q in [('A',d['A'][i]),('B',d['B'][i])]:
        q=xy([q])[0];ax.scatter(*q,color=EDGE,s=18);ax.text(q[0]*1.1,q[1]*1.1,f'${name}_{i}$',ha='center',va='center')
    c=xy([d['p']*U[i]])[0];t=xy([T[i]])[0]
    ax.annotate('',xy=c+.38*t,xytext=c,arrowprops={'arrowstyle':'->','color':GAP})
ax.scatter(0,0,s=16,color=INK);ax.text(.06,-.06,'O');ax.set_title('Three oriented selected edges; connectors not yet drawn')
save(fig,'02_three_frames','Tangent selected edges and endpoint convention before connector construction.')

for num,g,title in [(3,S.Rational(3,5),'Generic positive member: $g_{gap}/s=3/5$'),(4,S.Integer(1),'Regular member: $g_{gap}=s$')]:
    fig,ax=plt.subplots(figsize=(6.8,4.5));base(ax);d=scaffold(1,g);shell(ax,d,True)
    ax.scatter(*xy([S.zeros(2,1)])[0],color=INK,s=12);ax.set_title(title)
    ax.text(.5,-.08,'Solid blue: selected octagon edges   |   Dashed orange: connectors',transform=ax.transAxes,ha='center',fontsize=9)
    save(fig,f'{num:02d}_'+('alternating' if num==3 else 'regular_roles'),'Exact six-segment chain; colors mark source roles, not dynamic quantities.')

for num,g,title in [(5,S.Rational(3,5),'Support triangle: $W=s+2g_{gap}$'),(6,S.Integer(1),'Regular case: $W=3s$, three corner cells of side $s$')]:
    fig,ax=plt.subplots(figsize=(6.8,5));base(ax);d=scaffold(1,g);corners(ax,d);shell(ax,d)
    for i in range(3):
        c=xy([(d['B'][i]+d['V'][i]+d['A'][(i+1)%3])/3])[0];ax.text(*c,'$g_{gap}$' if num==5 else '$s$',ha='center',va='center',fontsize=9)
        q=xy([d['V'][i]])[0]*1.08;ax.text(*q,f'$V_{i}$',ha='center',va='center')
    ax.text(0,0,'central\nhexagon',ha='center',va='center',color=INK);ax.set_title(title)
    save(fig,f'{num:02d}_'+('support_triangle' if num==5 else 'regular_truncation'),'Support-triangle truncation with equilateral reference corner cells.')

fig,ax=plt.subplots(figsize=(7.2,5.9));base(ax);d=scaffold(1,1)
for i,o in enumerate(planar_frames(1,1)):
    ax.add_patch(Polygon(xy(o),facecolor=PALE,edgecolor='#778892',lw=1))
    c=xy([(d['p']+d['a'])*U[i]])[0];ax.text(*c,f'$C_{i}$',ha='center',va='center')
corners(ax,d);shell(ax,d)
ax.set_title('Complete planar reference frames; $L=a+p_*$')
save(fig,'07_complete_frames','Three full covariant regular octagons, reference corner cells and the regular central chain.')

fig,axs=plt.subplots(1,2,figsize=(8,4.1))
for ax,g,title in zip(axs,[1/r2,1],['Paper-C top measurement','$p=p_*$, same octagon side']):
    base(ax);d=scaffold(1,g);shell(ax,d,True);ax.set_title(title);ax.set_xlim(-1.5,1.5);ax.set_ylim(-1.45,1.45)
    ax.text(.5,-.04,('$g_{gap}/s=1/\\sqrt{2}$' if g!=1 else '$g_{gap}/s=1$'),transform=ax.transAxes,ha='center')
save(fig,'08_paper_c_measurement','Same-scale comparison of Paper-C unequal measurement chain and regular reference chain.')

fig=plt.figure(figsize=(10.1,5.2));s0=r2-1;a0=S.Rational(1,2);p0=a0/r3;lam=(1+r2)/3
cases=[(s0,p0,'Original width-one Paper C'),(s0,r3*s0/2,'Fixed size: move centres'),(S.Rational(1,3),p0,'Fixed centres: shrink faces')]
for j,(ss,pp,title) in enumerate(cases):
    ax=fig.add_subplot(1,3,j+1,projection='3d');aa=metrics(ss)[0];faces=vertical_frames(ss,pp)
    for pts in faces:
        arr=xy(pts);ax.add_collection3d(Poly3DCollection([arr],facecolors=PALE,edgecolors='#677983',alpha=.62,linewidth=.8))
    d=scaffold(ss,r3*pp-ss/2)
    for k in range(6):
        pair=xy([d['H'][k],d['H'][(k+1)%6]]);ax.plot(pair[:,0],pair[:,1],[float(aa)]*2,color=EDGE if k%2==0 else GAP,lw=2,ls='-' if k%2==0 else '--')
    for i in range(3):
        c=xy([pp*U[i]])[0];ax.scatter(c[0],c[1],0,color=INK,s=12)
    # Fixed reference height explicitly survives as a dashed construction line.
    ax.plot([-.65,.65],[.62,.62],[.5,.5],color='gray',ls=':',lw=1)
    ax.text2D(.5,-.01,('$z_{top}=1/2$' if j<2 else '$z_{top}=(1+\\sqrt{2})/6$\n$<1/2$'),transform=ax.transAxes,ha='center',fontsize=13)
    ax.set_title(title,fontsize=13,pad=8);ax.set_xlim(-.75,.75);ax.set_ylim(-.75,.75);ax.set_zlim(-.56,.59);ax.set_box_aspect((1,1,.86));ax.view_init(24,-52);ax.set_axis_off()
fig.subplots_adjust(left=.01,right=.99,bottom=.14,top=.9,wspace=.02)
save(fig,'09_translation_and_shrink','Actual vertical octagons: original, outward translation and fixed-centre shrink, with changed top height at equal plotted scale.')
(OUT/'figure_manifest.json').write_text(json.dumps({'figures':registry,'generator':'generate_figures.py','source':'geometry_coordinates.py','historical_simulations':False,'numeric_conversion':'Exact SymPy coordinates converted only at drawing boundary.'},indent=2)+'\n')
print('Generated nine analytic construction figures, each PDF/SVG/PNG.')
