from pathlib import Path
import json,hashlib,os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
O=Path(__file__).resolve().parent
read=lambda p:json.loads((O/p).read_text())
G=read('incoming/reference/BOUNDARY11/data/geometry_inventory.json')
data={'geometry':G,'events':{n:ev for n,ev in zip(['original','A','B'],G['coincidence_events'])},
 'graphs':{n:read(f'data/graph_{n}.json') for n in ['original','A','B']},
 'hulls':{n:read(f'data/hull_{n}.json') for n in ['original','A','B']},
 'presets':read('data/fixed_presets.json'),'source_identities':read('evidence/HANDOFF_VALIDATION.json')}
(O/'data/viewer_data.json').write_text(json.dumps(data,indent=2)+'\n')
lib=(O/'assets/plotly-3.1.0.min.js').read_text(encoding='utf-8')
upstream=O.parents[1]/'research/BOUNDARY11_20261016/assets/plotly-3.1.0.min.js'
assert hashlib.sha256(upstream.read_bytes()).hexdigest()==hashlib.sha256((O/'assets/plotly-3.1.0.min.js').read_bytes()).hexdigest()
template=(O/'viewer_template.html').read_text(encoding='utf-8')
html=template.replace('__PLOTLY__',lib).replace('__DATA__',json.dumps(data,separators=(',',':'))).replace('__MATH__',(O/'viewer_math.js').read_text())
(O/'BOUNDARY12_VIEWER.html').write_text(html,encoding='utf-8')
F=O/'figures';F.mkdir(exist_ok=True)
V=np.array([v['centered'] for v in G['vertices']]);colors={'seam':'#b94747','horizontal':'#087f8c','chamfer':'#7652aa'}
plt.rcParams.update({'font.size':10,'axes.titlesize':12,'axes.labelsize':9,'svg.fonttype':'none'})
def scene(ax,name,az=-60,elev=23,hull=True,graph=True):
 H=data['hulls'][name];N=data['graphs'][name];P=np.array([v['xyz'] for v in H['vertices']]);Q=np.array([v['xyz'] for v in N['vertices']]);R=data['events'][name]['R_over_w']
 if hull:
  ax.add_collection3d(Poly3DCollection([P[f['vertices']] for f in H['faces']],facecolor='#70aeb2',edgecolor='none',alpha=.10))
  for e in H['edges']:ax.plot(*P[e['vertices']].T,color='#b57a18',lw=.9,alpha=.85)
 ax.add_collection3d(Poly3DCollection([V[f] for f in G['faces']],facecolor='#77a6c4',edgecolor='none',alpha=.20))
 for e in G['edges']:ax.plot(*V[e['vertices']].T,color='#173247',lw=1.5)
 if graph:
  for e in N['edges']:
   if e['segment_kind']=='added':ax.plot(*Q[e['vertices']].T,color=colors[e['source_class']],lw=.8)
  ax.scatter(*Q.T,s=8,color='#264e5c',depthshade=False)
 ax.scatter(*P.T,s=17,color='#b57a18',depthshade=False)
 lim=R*1.08;ax.set(xlim=(-lim,lim),ylim=(-lim,lim),zlim=(-lim,lim),xlabel='x / w',ylabel='y centred / w',zlabel='z / w');ax.set_box_aspect((1,1,1));ax.set_proj_type('ortho');ax.view_init(elev,az)
 ticks=np.linspace(-R,R,3);ax.set_xticks(ticks);ax.set_yticks(ticks);ax.set_zticks(ticks);ax.tick_params(labelsize=8,pad=0)
 for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.set_major_formatter(plt.FormatStrFormatter('%.2f'));axis.set_pane_color((1,1,1,0));axis._axinfo['grid']['color']=(.85,.89,.92,.35)
 if elev==90:ax.set_zticks([]);ax.set_zlabel('')
 if elev==0:ax.set_yticks([]);ax.set_ylabel('')
fig=plt.figure(figsize=(13,5))
for i,name in enumerate(['original','A','B'],1):
 ax=fig.add_subplot(1,3,i,projection='3d');scene(ax,name);N=data['graphs'][name];H=data['hulls'][name]
 ax.set_title(f'{name}: graph {N["V"]}V / {N["E"]}E\nhull {H["V"]}V / {H["E"]}E / {H["F"]}F',pad=9)
fig.suptitle('Exact event networks and their separate convex envelopes',fontsize=16)
fig.subplots_adjust(left=.01,right=.99,bottom=.1,top=.77,wspace=.03)
fig.savefig(F/'event_networks_and_hulls.png',dpi=170);fig.savefig(F/'event_networks_and_hulls.svg');plt.close(fig)
fig=plt.figure(figsize=(12,8))
for i,(elev,az,label) in enumerate([(23,-60,'Oblique'),(90,-90,'Axial projection'),(0,-90,'Side projection'),(20,30,'Opposite oblique')],1):
 ax=fig.add_subplot(2,2,i,projection='3d');scene(ax,'B',az,elev);ax.set_title(label)
fig.suptitle('Crossing B: all 105 open graph segments are interior to the hull',fontsize=14)
fig.subplots_adjust(left=.01,right=.99,bottom=.06,top=.89,wspace=.02,hspace=.24)
fig.savefig(F/'B_four_views.png',dpi=170);fig.savefig(F/'B_four_views.svg');plt.close(fig)
print(json.dumps({'viewer_bytes':(O/'BOUNDARY12_VIEWER.html').stat().st_size,'library_unchanged':True,'figures':sorted(p.name for p in F.iterdir())},indent=2))
