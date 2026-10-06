"""Present established formulas only; no simulation or new evidence count."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'pdf.fonttype':42,'svg.fonttype':'none'})
meta={'CreationDate':None,'ModDate':None,'Creator':'Tri-Octagon candidate figure source'}
s=np.sqrt(2)-1;p=1/(2*np.sqrt(3))
verts=np.array([[-.5,-s/2],[-s/2,-.5],[s/2,-.5],[.5,-s/2],[.5,s/2],[s/2,.5],[-s/2,.5],[-.5,s/2]])
fig=plt.figure(figsize=(7.3,5.6),layout='constrained');ax=fig.add_subplot(projection='3d')
for phi in np.deg2rad([30,150,270]):
    n=np.array([np.cos(phi),np.sin(phi),0]);t=np.array([-np.sin(phi),np.cos(phi),0])
    xyz=p*n+verts[:,0,None]*t+verts[:,1,None]*[0,0,1]
    ax.add_collection3d(Poly3DCollection([xyz],facecolors='#83bccd',edgecolors='#16495b',linewidths=1.4,alpha=.65))
theta=np.linspace(0,2*np.pi,241);R=1/np.sqrt(3)
for z in [-.5,.5]:ax.plot(R*np.cos(theta),R*np.sin(theta),z*np.ones_like(theta),c='#b78425',lw=1.6)
for th in np.linspace(0,2*np.pi,9)[:-1]:ax.plot([R*np.cos(th)]*2,[R*np.sin(th)]*2,[-.5,.5],c='#b78425',ls=':',lw=.8)
ax.scatter([0],[0],[0],s=16,c='#182e3b');ax.text(0,0,.04,'o')
ax.set(xlabel=r'$X-o_x$',ylabel=r'$Y-o_y$',zlabel=r'$z$',xlim=(-.7,.7),ylim=(-.7,.7),zlim=(-.6,.6))
ax.set_box_aspect([1.4,1.4,1.2]);ax.view_init(23,-57)
ax.set_title('Static folded module and measurement cylinder',pad=14)
for fmt in ['pdf','svg']:fig.savefig(ROOT/'measurement/figures'/f'scaffold.{fmt}',metadata=meta if fmt=='pdf' else None)
plt.close(fig)
h=np.linspace(0,.25,401)
coef=lambda x:np.sqrt(3)*(33*x*x-240*x+688)/(6*(1-3*x)**3)
fig,ax=plt.subplots(figsize=(7,4.1),layout='constrained')
ax.plot(h,coef(h),color='#17596f',lw=2.2)
steps=np.array([0,.001,.01,.1]);ax.scatter(steps,coef(steps),c='#b78425',s=34,zorder=4)
ax.set(xlabel=r'Mathematical step scale $h$',ylabel=r'Analytic coefficient $c_+(h)$',xlim=(-.004,.255),ylim=(0,13000))
ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
ax.set_title('Cubic coefficient on the admitted reference interval')
ax.text(.025,.91,r'$\nu_+=2c_+(h)\eta^3+O(\eta^5)$',transform=ax.transAxes)
for fmt in ['pdf','svg']:fig.savefig(ROOT/'drift/figures'/f'coefficient.{fmt}',metadata=meta if fmt=='pdf' else None)
np.savetxt(ROOT/'drift/figures/coefficient_formula.csv',np.c_[h,coef(h)],delimiter=',',header='h,c_plus_formula',comments='')
(ROOT/'provenance/figure_sources.json').write_text(json.dumps({'scaffold':{'source':'M1-M11; centered panel coordinates','evidence':'formula presentation; no new validation'},'TL4_MEASUREMENT_VIEWS':{'source':'TL4 retained PNG; hash in source inventory','evidence':'unchanged historical diagram'},'coefficient':{'source':'D3 exact coefficient','domain':'0 <= h <= 1/4','dots':'h=0,1/1000,1/100,1/10; coefficient evaluations, not finite-eta rates','evidence':'formula presentation; no experiment'}},indent=2)+'\n')
print('Two formula figures generated as PDF/SVG; retained TL4 PNG unchanged.')
