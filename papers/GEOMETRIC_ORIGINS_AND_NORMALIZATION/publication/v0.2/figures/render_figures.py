"""Deterministic manuscript schematics only; consumes retained coordinates.
No geometry solver, sampling experiment, project module or kernel is used.
Run in the torment conda environment with python -B.
"""
from pathlib import Path
import os,json,hashlib
os.environ.setdefault('SOURCE_DATE_EPOCH','1792195200')
os.environ['MPLCONFIGDIR']=str(Path(__file__).resolve().parents[2]/'build/mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
P=Path(__file__).resolve().parent
data=P/'geometry_inventory.json'
g=json.loads(data.read_text(encoding='utf-8'))
assert hashlib.sha256(data.read_bytes()).hexdigest()=='694a9ab0cab1e9335be913ef876483e9fedd59a22cb93cec6b9dda3a33a1afb2'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'svg.fonttype':'none','svg.hashsalt':'GEO-ORIGINS01-v0.1','axes.spines.top':False,'axes.spines.right':False})
ink='#243e55';teal='#187d86';orange='#bb5f24'
def outputs(fig,name):
 for ext in ('pdf','svg','png'):
  fig.savefig(P/(name+'.'+ext),dpi=220,bbox_inches='tight',facecolor='white',metadata={'Creator':'GEO-ORIGINS-01 deterministic schematic'} if ext!='png' else None)
 plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(8.6,2.85))
r=.5
for ax,d,title in zip(axs,[r,2*r*np.cos(np.pi/4)],['Half-radius offsets; total separation r',r'Overlap perimeter $4r\theta=\pi/2$']) :
 for c in (-d/2,d/2):ax.add_patch(Circle((c,0),r,fill=False,lw=1.1,edgecolor='#a2adb4'))
 theta=np.arccos(d/(2*r));v=np.linspace(-theta,theta,240)
 left=np.c_[-d/2+r*np.cos(v),r*np.sin(v)]
 right=np.c_[d/2-r*np.cos(v),r*np.sin(v)]
 ax.add_patch(Polygon(np.vstack((left,right[::-1])),color=teal,alpha=.13,lw=0))
 ax.plot(left[:,0],left[:,1],color=teal,lw=2);ax.plot(right[:,0],right[:,1],color=teal,lw=2)
 ax.scatter([-d/2,d/2],[0,0],color=ink,s=14,zorder=4)
 ax.axhline(0,color='#b5bdc2',ls=':',lw=.8)
 ax.set_aspect('equal');ax.set_xlim(-.92,.92);ax.set_ylim(-.78,.64);ax.axis('off');ax.set_title(title,color=ink,fontsize=10,pad=10)
 ax.annotate('',xy=(-d/2,-.59),xytext=(d/2,-.59),arrowprops={'arrowstyle':'<->','color':ink,'lw':1})
 ax.text(0,-.73,'$d=r$' if d==r else r'$d=2r\cos(\pi/4)$',ha='center',color=ink)
 if d==r:
  ax.text(-d/2-.03,-.12,'$-r/2$',ha='right');ax.text(d/2+.03,-.12,'$r/2$',ha='left')
  ax.text(0,.53,'$r=1/2$',ha='center',color=ink)
 else:
  ax.text(0,.53,r'$r=1/2,\quad\theta=\pi/4$',ha='center',color=ink)
fig.subplots_adjust(wspace=.17)
outputs(fig,'circle_conventions')

fig=plt.figure(figsize=(9,3.6));ax=fig.add_subplot(121,projection='3d')
v=np.array([x['centered'] for x in g['vertices']]);a=1/np.sqrt(3);rho=g['rho'];ra=np.sqrt(7/12);rb=np.sqrt(13/12+np.sqrt(2)/2);h=(np.sqrt(2)-1)/2
ax.add_collection3d(Poly3DCollection([v[f] for f in g['faces']],facecolors=['#6091ad','#499b9e','#b1c3cd'],alpha=.23,edgecolor='none'))
for e in g['edges']:
 seg=v[e['vertices']];ax.plot(*seg.T,color=ink,lw=1.3)
ang=np.linspace(0,2*np.pi,160)
for z in (-.5,.5):ax.plot(a*np.cos(ang),a*np.sin(ang),np.full_like(ang,z),color='#89969e',lw=.9,ls='--')
corners=np.array([[a*np.cos(t),a*np.sin(t),z] for z in (-.5,.5) for t in [np.pi/2,np.pi/2+2*np.pi/3,np.pi/2+4*np.pi/3]])
ax.scatter(*corners.T,color=orange,s=18,depthshade=False)
for i in range(3):ax.plot(*np.array([corners[i],corners[i+3]]).T,color='#89969e',ls='--',lw=.7)
for z in (-.5,.5):
 cs=corners[:3] if z<0 else corners[3:];cs=np.vstack((cs,cs[0]));ax.plot(*cs.T,color='#89969e',ls=':',lw=.7)
for lat in [-np.pi/3,-np.pi/6,0,np.pi/6,np.pi/3]:ax.plot(ra*np.cos(lat)*np.cos(ang),ra*np.cos(lat)*np.sin(ang),np.full_like(ang,ra*np.sin(lat)),color=teal,lw=.35,alpha=.42)
for az in [0,np.pi/3,2*np.pi/3]:ax.plot(ra*np.cos(ang)*np.cos(az),ra*np.cos(ang)*np.sin(az),ra*np.sin(ang),color=teal,lw=.35,alpha=.42)
ax.set(xlim=(-.8,.8),ylim=(-.8,.8),zlim=(-.8,.8));ax.set_box_aspect((1,1,1),zoom=1.23);ax.set_proj_type('ortho');ax.view_init(elev=20,azim=-51);ax.set_axis_off()
ax.set_title('Native panels and measurement enclosure',fontsize=10,color=ink,pad=-5)
ax.text2D(.02,.02,'Orange: six A seam exits / prism corners\nDashed: cylinder; teal: A sphere ($w=1$)',transform=ax.transAxes,fontsize=8.5,color=ink)
ax2=fig.add_subplot(122);ts=np.linspace(0,np.pi/2,200)
for radius,col,label in [(rho,ink,'Original'),(ra,teal,'A'),(rb,orange,'B')]:
 ax2.plot(radius*np.cos(ts),radius*np.sin(ts),color=col,lw=1.2)
ax2.plot([0,1.42],[a,a],color=ink,lw=1)
ax2.plot([0,0],[0,a],color=ink,ls=':',lw=1)
for t,col in [(h,ink),(.5,teal),((1+np.sqrt(2))/2,orange)]:ax2.scatter([t],[a],color=col,s=24,zorder=4)
ax2.annotate('Original',xy=(h,a),xytext=(.08,.91),fontsize=9,color=ink,arrowprops={'arrowstyle':'-','color':ink,'lw':.7})
ax2.annotate('A',xy=(.5,a),xytext=(.65,.87),fontsize=10,color=teal,arrowprops={'arrowstyle':'-','color':teal,'lw':.7})
ax2.annotate('B',xy=((1+np.sqrt(2))/2,a),xytext=(1.28,.83),fontsize=10,color=orange,arrowprops={'arrowstyle':'-','color':orange,'lw':.7})
ax2.annotate('',xy=(h,a-.12),xytext=((1+np.sqrt(2))/2,a-.12),arrowprops={'arrowstyle':'<->','color':orange,'lw':1})
ax2.text(.72,a-.23,'Added at B = $w$',ha='center',color=orange,fontsize=9)
ax2.text(.02,.26,r'$a=w/\sqrt{3}$',rotation=90,fontsize=9,color=ink)
ax2.text(.51,1.23,'A: $t=w/2$, hence $C_A=2t=w$',ha='center',fontsize=9,color=teal)
ax2.set_aspect('equal');ax2.set(xlim=(-.035,1.5),ylim=(0,1.43),xlabel='Along-line distance $t/w$',ylabel='Perpendicular distance / $w$')
ax2.set_title('Centre-edge plane: one outward ray',fontsize=10,color=ink,pad=10);ax2.set_xticks([0,.5,1,1.5]);ax2.set_yticks([0,.5,1]);ax2.tick_params(labelsize=8)
fig.subplots_adjust(wspace=.24,left=.01,right=.99,bottom=.14,top=.89)
outputs(fig,'shell_and_lengths')
