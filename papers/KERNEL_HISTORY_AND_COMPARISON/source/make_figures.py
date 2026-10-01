"""Render only saved, checked inert data; no simulations or scientific imports."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'evidence/figure_table_data.json').read_bytes())
identity=hashlib.sha256((ROOT/'evidence/figure_table_data.json').read_bytes()).hexdigest()
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'svg.fonttype':'none'})
figures=[]
def save(fig,name):
 for ext in ['pdf','png','svg']:fig.savefig(ROOT/'figures'/(name+'.'+ext),dpi=180,bbox_inches='tight')
 plt.close(fig);figures.append({'name':name,'data_sha256':identity,'data_source':'evidence/figure_table_data.json' if name!='01_lineage' else 'evidence/SOURCE_MAP.md: lineage rows; H0-H6B documentary sources'})
fig,ax=plt.subplots(figsize=(9.4,4.3));ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off')
def box(x,y,w,h,text,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',facecolor=color,edgecolor='#677581',linewidth=.8))
 ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=9,linespacing=1.45)
def arrow(a,b,label=None,color='#406b85',dashed=False):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,color=color,linewidth=1.2,linestyle='--' if dashed else '-'))
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.1,label,ha='center',va='bottom',fontsize=8,color=color,bbox=dict(facecolor='white',edgecolor='none',pad=1.5))
box(.15,3.65,3.05,1.05,'Historical sources / kernel_TO\n2025 papers; archived model family\nEvidence, not the whole service','#f1ede3')
box(6.55,3.65,3.05,1.05,'Production TORMENT\nAudited service snapshot, 2026\nMemory interfaces and wrappers','#f1ede3')
box(.15,1.35,3.05,1.15,'Historical reference v0.1.0\nH4/H5 freeze -> H6B, 1 Oct 2026\nIndependent implementation','#e6f1ef')
box(6.55,1.35,3.05,1.15,'Current physics kernel v0.1.0\nPapers A-F; explicit scientific API\nIndependent implementation','#e8eff7')
arrow((3.25,4.15),(6.47,4.15),'related/copied core; H2')
arrow((1.65,3.55),(1.65,2.59),'reconstruction / H4-H6B')
arrow((3.25,3.65),(6.5,2.5),'re-expression / Papers A-F')
arrow((3.3,1.9),(6.42,1.9),'P3 comparison',dashed=True)
ax.text(5,.5,'Solid arrows: documented lineage, not runtime imports.\nDashed arrow: comparison of inert independent outputs. No production replacement is implied.',ha='center',va='center',fontsize=9)
save(fig,'01_lineage')
profiles=list(data['profiles']);names=['Historical scaled','Historical soft','Historical simple','Current L01'];colors=['#14648d','#ca702e','#25866c'];palette=['#913b53','#287fac','#75619c','#404040']
fig,axes=plt.subplots(2,2,figsize=(9,6.0))
for ax,p,label in zip(axes.flat,profiles,names):
 points=data['profiles'][p]['points'];a=np.array([r['magnitudes'] for r in points[:129]])
 for j in range(3):ax.plot(np.arange(129),a[:,j],color=colors[j],label=f'channel {j+1}',linewidth=1.5)
 ax.set(title=label,xlabel='update n',ylabel=r'$|\Omega_j|$',ylim=(0,2.2));ax.grid(alpha=.17);ax.legend(fontsize=7,loc='upper left')
fig.tight_layout();save(fig,'02_amplitudes')
fig,axes=plt.subplots(1,2,figsize=(9,3.4))
for p,label,color in zip(profiles,names,palette):
 rows=data['profiles'][p]['points'];n=np.arange(len(rows))
 axes[1].plot(n,[float.fromhex(r['m']) for r in rows],color=color,label=label,linewidth=1.6)
 if p!='CURRENT_L01':
  axes[0].plot(n[1:],[r['raw'] for r in rows[1:]],color=color,label=label.replace('Historical ','')+' raw')
  axes[0].plot(n[1:],[r['aligned'] for r in rows[1:]],color=color,linestyle='--',label=label.replace('Historical ','')+' aligned')
axes[0].set(xscale='log',xlabel='update n (log scale)',ylabel='L2 distance from L01');axes[1].set(xlabel='update n',ylabel='EMA memory m')
for ax in axes:ax.grid(alpha=.17);ax.legend(fontsize=7)
fig.tight_layout();save(fig,'03_distance_memory')
(ROOT/'evidence/figure_manifest.json').write_text(json.dumps({'status':'LOCAL_REVIEW_ONLY','seed_id':data['seed_id'],'eps':.05,'g':.2,'phase_strength':.001,'horizon':1024,'numpy':np.__version__,'matplotlib':matplotlib.__version__,'figures':figures,'note':'No exact-zero error is placed on a log y axis. Figure 3 uses log x only. Figure 2 displays n<=128; tables give n=1024. Figure 1 depicts source lineage, not computation dependencies.'},indent=2)+'\n',encoding='utf-8')
