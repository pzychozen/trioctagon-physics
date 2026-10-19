"""Paper-local static presentation. No evolution, quadrature or project imports."""
from pathlib import Path
import os,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
for k in ['MPLCONFIGDIR','TEMP','TMP','XDG_CACHE_HOME']:os.environ[k]=str(ROOT/'cache')
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':11,'pdf.fonttype':42,'svg.fonttype':'none','figure.facecolor':'white'})
BLUE='#256f9e';RED='#b2314d';GOLD='#b07b16';INK='#253a49';GREY='#8b9aa5'
def read(n):return json.loads((ROOT/'data'/n).read_text(encoding='utf8'))
ledger={'kind':'static presentation of retained coordinates and data','new_quadratures':0,'evolution_steps':0,'figures':{}}
def save(fig,n,source,detail):
 fig.savefig(ROOT/'figures'/f'{n}.pdf',bbox_inches='tight');fig.savefig(ROOT/'figures'/f'{n}.png',dpi=160,bbox_inches='tight');fig.savefig(ROOT/'figures'/f'{n}.svg',bbox_inches='tight');plt.close(fig)
 ledger['figures'][n]={'source':source,'presentation':detail}
g=read('coordinates.json');sp=read('spatial.json');p=read('pulse_plot.json');t=read('timing_plot.json')
O=np.array(g['origin']['numeric']);verts=np.array([x['numeric'] for x in g['vertices']]);a=float(g['constants']['a']['decimal']);K=float(g['constants']['K']['decimal']);R=float(g['constants']['R']['decimal'])
ang=np.linspace(0,2*np.pi,361);curve=O+np.c_[np.zeros_like(ang),K+R*np.cos(ang),R*np.sin(ang)]
az,el=np.deg2rad([-24,22]);cam=np.array([[-np.sin(az),np.cos(az),0],[-np.sin(el)*np.cos(az),-np.sin(el)*np.sin(az),np.cos(el)]])
def xy(x):return (np.asarray(x)-O)@cam.T
def shell(ax,pts,col=INK,lw=.4):
 pts=xy(pts)
 for f in g['faces']:ax.add_patch(Polygon(pts[f],facecolor='#dfe7eb',alpha=.5,edgecolor='none'))
 for i,j in g['edges']:ax.plot(*pts[[i,j]].T,c=col,lw=lw)
fig,axs=plt.subplots(1,3,figsize=(10,4),gridspec_kw={'width_ratios':[1,1.25,1.25]})
ax=axs[0];ax.plot(K+R*np.cos(ang),R*np.sin(ang),c=RED,lw=1.7)
theta=np.arctan(2/np.sqrt(3))
for sg in [1,-1]:
 ax.scatter([a],[sg*a],c=RED,s=25);ax.annotate(r'$P_+$' if sg==1 else r'$P_-$',(a,sg*a),(-25,8*sg),textcoords='offset points')
 ax.annotate('',(a+.2*2/np.sqrt(7),sg*a+sg*.2*np.sqrt(3/7)),(a,sg*a),arrowprops={'arrowstyle':'->','color':BLUE,'lw':1.4})
ax.scatter([K],[0],c=INK,s=15);ax.text(K+.03,.03,r'$B_0$');ax.text(.03,0,'short\narc',ha='center',fontsize=9);ax.text(1.13,0,'long\narc',ha='center',fontsize=9)
ax.axhline(0,c=GREY,lw=.5);ax.set(xlim=(-.1,1.4),ylim=(-.75,.75),xlabel=r'$u\cdot(X-O)$',ylabel='Height',title='(a) Selected contact plane');ax.set_aspect('equal')
for ax,fam in zip(axs[1:],['H','R']):
 shell(ax,verts);ax.plot(*xy(curve).T,c=RED,lw=1.2)
 for ring in sp['fixtures'][fam]:
  col=BLUE if ring['id'] in ['H0','R2'] else GREY
  rr=ring['R_numeric'];hh=ring['h_numeric'];cc=O+np.c_[rr*np.cos(ang),rr*np.sin(ang),np.full_like(ang,hh)];ax.plot(*xy(cc).T,c=col,lw=.5)
  for pr in ring['probes']:shell(ax,np.array(pr['center']['numeric'])+(verts-O)@np.array(pr['frame_numeric']).T/4,col)
 ax.set_aspect('equal');ax.autoscale_view();ax.axis('off');ax.set_title('(b) H: five heights' if fam=='H' else '(c) R: three radii')
fig.tight_layout(w_pad=1);save(fig,'geometry',['coordinates.json','spatial.json'],'Orthographic full-module views; exact median circle. Normals are blue; no flow arrow or new site.')

fig,ax=plt.subplots(figsize=(9.8,3.5));ax.set(xlim=(0,10),ylim=(0,3.6));ax.axis('off')
boxes=[(.1,2.15,2.2,.9,'Native state +\nreadout clock\nInherited definitions'),(2.8,2.15,2,.9,'Fixed registration\npaired projections\nMissing azimuth'),(5.35,2.15,1.9,.9,'C1 adoption\nOne driven field\nSigned work'),(7.8,2.15,2,.9,'C6 adoption\nExterior history map\nFixed H/R frames'),(2.8,.35,2,.9,'Prescribed pulses /\nsymbolic common hold'),(5.35,.35,1.9,.9,'Residual modes\nMean retained'),(7.8,.35,2,.9,'Scalar / directional\nrecords and limits')]
for x,y,w,h,txt in boxes:
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',edgecolor=BLUE if 'adoption' in txt else GREY,facecolor='#f2f6f8',lw=1));ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=9.5)
for start,end in [((2.35,2.6),(2.7,2.6)),((4.9,2.6),(5.25,2.6)),((7.35,2.6),(7.7,2.6)),((3.8,1.35),(3.8,2.05)),((6.3,2.05),(6.3,1.35)),((7.35,.8),(7.7,.8)),((8.8,2.05),(8.8,1.35))]:ax.annotate('',end,start,arrowprops={'arrowstyle':'->','lw':1.1,'color':INK})
save(fig,'dependencies',[],'Typed dependency graph of manuscript definitions; no new coupling.')

fig,axs=plt.subplots(1,2,figsize=(9.7,3.9));sc=np.array(t['scalar_contrast']);fu=np.array(t['full_contrast']);mx=max(sc.max(),fu.max())
for ax,values,title in zip(axs,[sc,fu],['Scalar record: swapped quarter timing','Full record: swapped quarter timing']):
 im=ax.imshow(values,aspect='auto',vmin=0,vmax=mx,cmap='viridis',origin='upper');ax.set(yticks=range(len(t['array_rows'])),yticklabels=t['array_rows'],xticks=range(0,12,2),xlabel='Fixed site index k',title=title)
fig.subplots_adjust(wspace=.35,right=.88);cb=fig.colorbar(im,ax=axs,cax=fig.add_axes([.9,.16,.018,.64]));cb.set_label('Phasor contrast / (gₒF₀/c)')
save(fig,'exterior',['timing_plot.json'],'Exact inherited swapped-input contrast at nu=1; shared color scale; equatorial zeros by proof, no threshold.')

fig,axs=plt.subplots(1,2,figsize=(9.7,3.6));axs[0].plot(p['prescribed_pulse_t_over_T'],p['prescribed_envelope'],c=BLUE,lw=1.8);axs[0].set(xlabel='Prescribed analysis time t/T',ylabel='h(t)',title='(a) Common one-circuit input',ylim=(-.05,1.1));axs[0].grid(alpha=.2)
x=np.arange(len(p['storage_controls']));axs[1].bar(x,p['storage_mean'],color=GREY,label='Static mean');axs[1].bar(x,p['storage_harmonic'],bottom=p['storage_mean'],color=GOLD,label='Standing harmonic');axs[1].set(xticks=x,xticklabels=p['storage_controls'],ylabel='Storage / (F₀²L/c²)',title='(b) Generated work and storage',ylim=(0,.72));axs[1].legend(fontsize=9)
fig.tight_layout(w_pad=2);save(fig,'pulse',['pulse_plot.json'],'Retained prescribed envelope and storage bars; no generated trajectories.')

fig,axs=plt.subplots(2,1,figsize=(9.6,6.6),gridspec_kw={'height_ratios':[1,1.15]});tt=np.array(t['time_over_T']);controls=t['control_order'];pulse=t['pulse_values_over_F0']
# The schedules are prescribed analytic inputs already sampled in the retained plot data.
for control,col,ls in [('CO',GREY,'-'),('LOWER_LATE_Q',RED,'--'),('LOWER_LATE_H',BLUE,':')]:
 val=pulse[control]
 if isinstance(val,dict):
  vals=list(val.values());line=vals[1]
 else:line=np.array(val)[:,1] if np.array(val).shape[0]==len(tt) else np.array(val)[1]
 axs[0].plot(tt,line,c=col,ls=ls,lw=1.7,label={'CO':'Lower port: co-timed','LOWER_LATE_Q':'Lower port: T/4 late','LOWER_LATE_H':'Lower port: T/2 late'}[control])
axs[0].set(xlabel='Prescribed analysis time t/T',ylabel='Lower-port input / F₀',title='(a) Fixed input timings',ylim=(-.05,1.3));axs[0].legend(ncol=3,fontsize=9,loc='upper center');axs[0].grid(alpha=.18)
st=np.array(t['storage_rows']);xx=np.arange(len(controls));bottom=np.zeros(len(xx))
for j,(lab,col) in enumerate(zip(['Static mean','Positive direction','Negative direction'],[GREY,RED,BLUE])):
 axs[1].bar(xx,st[:,j],bottom=bottom,color=col,label=lab);bottom+=st[:,j]
axs[1].set(xticks=xx,xticklabels=['CO','Lower Q','Upper Q','Lower H','One upper','ZERO'],ylabel='Storage / (F₀²L/c²)',ylim=(0,.79),title='(b) Generated residual at common reference 3T/2');axs[1].legend(ncol=3,fontsize=9);axs[1].grid(axis='y',alpha=.15)
fig.tight_layout(h_pad=2);save(fig,'timing',['timing_plot.json'],'Retained schedules and full mean/directional bars, common phase and scale.')
(ROOT/'figures/FIGURE_DATA_LEDGER.json').write_text(json.dumps(ledger,indent=2),encoding='utf8')
print('Five paper-local vector figures rendered from retained data and stated geometry.')
