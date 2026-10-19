"""Static paper-local views of accepted data; no research program import."""
from pathlib import Path
import os,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
for key in ['MPLCONFIGDIR','XDG_CACHE_HOME','TEMP','TMP']:os.environ[key]=str(ROOT/'cache')
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':12,'axes.labelsize':11,'pdf.fonttype':42,'svg.fonttype':'none','figure.facecolor':'white','axes.facecolor':'white'})
def read(rel):return json.loads((ROOT/'input'/rel).read_text(encoding='utf8'))
geo=read('retained_srg02/figures/coordinates.json');obs=read('retained_srg03/OBSERVER_MAP.json');spa=read('retained_srg04/SPATIAL_MAP.json')
O=np.array(geo['origin']['numeric']); verts=np.array([x['numeric'] for x in geo['vertices']]);faces=geo['faces'];edges=geo['edges']
a=float(geo['constants']['a']['decimal']);K=float(geo['constants']['K']['decimal']);r=float(geo['constants']['R']['decimal']);h0=float(geo['constants']['h0']['decimal']);d=float(geo['constants']['d']['decimal'])
RED='#af2446';GOLD='#a86a00';BLUE='#236f9e';INK='#263744';GREY='#75828b'
data={'source_files':{},'presentation_only':True,'new_positions':False,'evolution':False,'figures':{}}
for rel in ['retained_srg02/figures/coordinates.json','retained_srg03/OBSERVER_MAP.json','retained_srg04/SPATIAL_MAP.json']:
    data['source_files'][rel]=hashlib.sha256((ROOT/'input'/rel).read_bytes()).hexdigest()
ang=np.linspace(0,2*np.pi,481)
loop=geo['loops'][0]; u=np.array(loop['u']['numeric']);v=np.array(loop['v']['numeric']);ez=np.array([0,0,1]);B=np.array(loop['center']['numeric'])
curve=B+r*(np.cos(ang)[:,None]*u+np.sin(ang)[:,None]*ez)
def camera(az=-35,el=20):
    az,el=np.deg2rad([az,el]);return np.array([[-np.sin(az),np.cos(az),0],[-np.sin(el)*np.cos(az),-np.sin(el)*np.sin(az),np.cos(el)]])
def project(x,cam):return (np.asarray(x)-O)@cam.T
def shell(ax,points,cam,color=INK,fill='#d9e3e9',lw=.6):
    pts=project(points,cam)
    for f in faces:ax.add_patch(Polygon(pts[f],closed=True,facecolor=fill,alpha=.65,edgecolor='none'))
    for i,j in edges:ax.plot(*pts[[i,j]].T,color=color,lw=lw)
def finish(ax):ax.set_aspect('equal');ax.autoscale_view();ax.axis('off')
def save(fig,name,record):
    fig.savefig(ROOT/'figures'/f'{name}.pdf',bbox_inches='tight',facecolor='white')
    fig.savefig(ROOT/'figures'/f'{name}.png',dpi=180,bbox_inches='tight',facecolor='white')
    fig.savefig(ROOT/'figures'/f'{name}.svg',bbox_inches='tight',facecolor='white')
    plt.close(fig);data['figures'][name]=record

# Focused finite-region view and analytic median section.
fig,axs=plt.subplots(1,2,figsize=(9,4.5),gridspec_kw={'width_ratios':[1,1.15]})
cam=camera(-27,17);ax=axs[0];shell(ax,verts,cam,lw=1)
for reg in geo['regions']:
    pts=project(verts[reg['ids']],cam);ax.add_patch(Polygon(pts,facecolor='#ecc568',alpha=.38,edgecolor='none'))
    ax.plot(*pts[[1,2]].T,color=GOLD,ls='--',lw=1.3)
    if reg['sign']==1:
        xy=pts[0];ax.annotate(reg['pair'],xy,xytext=(0,13),textcoords='offset points',ha='center',color=GOLD,weight='bold')
ax.plot(*project(curve,cam).T,color=RED,lw=2);finish(ax);ax.set_title('(a) Paired finite regions')
ax=axs[1];ax.plot(K+r*np.cos(ang),r*np.sin(ang),color=RED,lw=2,label=r'Conditional $\Gamma_0$')
r0=1/np.sqrt(3);c=np.sqrt(3)/2
for sign in [1,-1]:
    rr=np.array([r0,r0-c*d]);zz=sign*np.array([h0,.5]);ax.plot(rr,zz,color=GOLD,lw=3)
    rline=np.array([.05,1.30]);ax.plot(rline,sign*(K-rline)/c,color=GOLD,ls=':',lw=.9)
    ax.scatter([a],[sign*a],color=RED,s=24,zorder=5)
    ax.annotate(r'$P_0^+$' if sign==1 else r'$P_0^-$',(a,sign*a),xytext=(-28,10 if sign==1 else -18),textcoords='offset points')
    nr=2/np.sqrt(7);nz=sign*np.sqrt(3/7);ax.annotate('',(a+.22*nr,sign*a+.22*nz),(a,sign*a),arrowprops={'arrowstyle':'->','color':BLUE,'lw':1.6})
ax.plot([r0,r0],[-h0,h0],color=INK,lw=3,label='Material seam')
ax.scatter([K],[0],color=INK,s=17);ax.text(K+.025,.035,r'$B_0$')
ax.axhline(0,color='#bec7cc',lw=.7);ax.axvline(0,color='#bec7cc',lw=.7)
ax.set(xlim=(-.05,1.38),ylim=(-.78,.78),xlabel=r'$r=u_0\cdot(X-O)$',ylabel=r'$z$',title='(b) Median section');ax.set_aspect('equal');ax.grid(alpha=.12)
fig.tight_layout(w_pad=2)
save(fig,'paired_geometry',{'geometry':geo,'circle_samples':curve.tolist(),'camera':cam.tolist(),'changes':'Orthographic camera, separate median section, labels and line styles; exact geometry unchanged.'})

# Full ring and enlarged same physical module in local view.
fig,axs=plt.subplots(1,2,figsize=(9,4.8),gridspec_kw={'width_ratios':[1.6,1]})
cam=camera(-35,50);ax=axs[0]
shell(ax,verts,cam,lw=.7);ax.plot(*project(curve,cam).T,color=RED,lw=1.5)
circle=O+3*np.c_[np.cos(ang),np.sin(ang),np.zeros_like(ang)]
ax.plot(*project(circle,cam).T,color=GREY,lw=.7)
for probe in obs['geometry']['probes']:
    points=np.array([z['numeric'] for z in probe['vertices']]);shell(ax,points,cam,color=INK,lw=.55)
    xy=project(np.array(probe['center']['numeric']),cam);out=xy*1.10
    ax.text(*out,str(probe['index']),fontsize=9,ha='center',va='center')
finish(ax);ax.set_title('(a) Twelve complete modules')
ax=axs[1];cam2=camera(-40,25);probe=obs['geometry']['probes'][0]
pts=np.array([z['numeric'] for z in probe['vertices']]);centre=np.array(probe['center']['numeric'])
shell(ax,pts-centre+O,cam2,lw=1.1)
frame=np.array(probe['frame_numeric']);labels=[r'$e_r$',r'$e_z$',r'$-e_\phi$']
for j,label in enumerate(labels):
    end=cam2@(frame[:,j]*.24);ax.annotate('',end,(0,0),arrowprops={'arrowstyle':'->','color':BLUE});ax.text(*(end*1.15),label,color=BLUE,ha='center')
finish(ax);ax.set_xlim(-.30,.30);ax.set_ylim(-.28,.30);ax.set_title('(b) Frame at site 0')
fig.tight_layout(w_pad=2)
save(fig,'full_modules',{'source_probes':obs['geometry']['probes'],'camera':cam.tolist(),'inset_camera':cam2.tolist(),'changes':'Enlarged view of existing site 0, no resized physical fixture; annotations are frame vectors.'})

# Fixed H and R layouts, using stored centres and frames, complete polygons.
fig,axs=plt.subplots(1,2,figsize=(9,5.0));cam=camera(-22,20)
reconstructed={}
for ax,fam in zip(axs,['H','R']):
    shell(ax,verts,cam,lw=.65);ax.plot(*project(curve,cam).T,color=RED,lw=1)
    reconstructed[fam]=[]
    for ring in spa['fixtures'][fam]:
        common=(ring['id'] in ['H0','R2']);col=BLUE if common else GREY
        rad=ring['R_numeric'];height=ring['h_numeric'];circle=O+np.c_[rad*np.cos(ang),rad*np.sin(ang),np.full_like(ang,height)]
        ax.plot(*project(circle,cam).T,color=col,lw=.8,alpha=.7)
        ringpts=[]
        for probe in ring['probes']:
            centre=np.array(probe['center']['numeric']);frame=np.array(probe['frame_numeric'])
            pts=centre+(verts-O)@frame.T/4
            shell(ax,pts,cam,color=col,lw=.5);ringpts.append(pts.tolist())
        reconstructed[fam].append({'id':ring['id'],'vertices':ringpts})
    finish(ax);ax.set_title('(a) H: five heights' if fam=='H' else '(b) R: three radii')
axs[0].text(.5,-.03,r'$R=3;\ h/a=2,1,0,-1,-2$',transform=axs[0].transAxes,ha='center',fontsize=10)
axs[1].text(.5,-.03,r'$h=0;\ R=2,3,4$',transform=axs[1].transAxes,ha='center',fontsize=10)
fig.tight_layout(w_pad=2)
save(fig,'hr_controls',{'retained_fixtures':spa['fixtures'],'reconstructed_vertices':reconstructed,'camera':cam.tolist(),'changes':'Two separate orthographic panels, common middle ring in blue. Complete 18-vertex modules, no HxR product.'})

fig,ax=plt.subplots(figsize=(8.6,3.4));values=np.array([z['numeric'] for z in obs['figure_fixture']['probe_C_differences']]);x=np.arange(12)
for j,(label,col,marker) in enumerate(zip(['Radial','Vertical','Negative azimuthal'],[BLUE,GOLD,RED],['o','s','^'])):
    ax.plot(x,values[:,j],marker=marker,lw=1.4,color=col,label=label,ms=5)
ax.axhline(0,color=GREY,lw=.6);ax.set(xlabel='Fixed observer index k (not time)',ylabel=r'$\Delta y_k^{\mathcal{C}}$',xticks=x,ylim=(-.27,.29));ax.grid(alpha=.18);ax.legend(ncol=3,loc='upper center',fontsize=10)
fig.tight_layout()
save(fig,'state_contrast',{'fixture':obs['figure_fixture'],'changes':'Only retained chirality-component differences plotted; line segments guide the fixed-site pattern.'})

fig,axs=plt.subplots(1,2,figsize=(9,3.7));heights=np.array([-2,-1,0,1,2]);near=np.sqrt((3-a)**2+(np.abs(heights)*a-a)**2)
axs[0].plot(heights,near,'o-',color=BLUE,lw=1.4)
for h,x in zip(heights,near):axs[0].annotate(f'{x:.6f}',(h,x),xytext=(0,10),textcoords='offset points',ha=('left' if h==-2 else 'right' if h==2 else 'center'),fontsize=9)
axs[0].set(xlabel=r'Height $h/a$ at $R=3$',ylabel=r'$c_*\tau_{\min}$',xticks=heights,ylim=(2.585,2.65),title='(a) Possible onset distance');axs[0].grid(alpha=.15)
phase=np.linspace(0,2*np.pi,401);aligned=(5+4*np.cos(phase))/9;axis=np.cos(phase/2)**2
axs[1].plot(phase,aligned,color=BLUE,label='Aligned vertical');axs[1].plot(phase,axis,color=RED,ls='--',label='Off-ring axial');axs[1].axhline(1,color=GOLD,ls=':',label='Aligned tangential')
axs[1].set(xlabel=r'Differential phase $\vartheta$',ylabel='Squared gain',xticks=[0,np.pi,2*np.pi],xticklabels=['0',r'$\pi$',r'$2\pi$'],ylim=(-.06,1.16),title='(b) Exact phase identities');axs[1].grid(alpha=.15);axs[1].legend(fontsize=9,loc='lower left')
fig.tight_layout(w_pad=2)
save(fig,'delay_comparison',{'heights_in_a':heights.tolist(),'earliest_distance':near.tolist(),'phase_drawing_samples':phase.tolist(),'aligned_vertical_gain_sq':aligned.tolist(),'axial_gain_sq':axis.tolist(),'changes':'Analytic curves as functions of differential phase only; fixed onset values. No evolved history.'})
(ROOT/'figures/figure_data.json').write_text(json.dumps(data,indent=2),encoding='utf8')
print('Rendered five static figures; retained author sketch is sixth manuscript figure.')
