"""Reproducible static geometry figures and standalone viewer assembly."""
from pathlib import Path
import hashlib,json,os,urllib.request
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
O=Path(__file__).resolve().parent
D=json.loads((O/'data/geometry_inventory.json').read_text())
V=np.array([v['centered'] for v in D['vertices']]); edges=D['edges'];rho=D['rho']; a=D['inner_radius']
F=O/'figures';F.mkdir(exist_ok=True);A=O/'assets';A.mkdir(exist_ok=True)
library=A/'plotly-3.1.0.min.js'
if not library.exists():
    with urllib.request.urlopen('https://cdn.plot.ly/plotly-3.1.0.min.js',timeout=45) as r: library.write_bytes(r.read())
libtext=library.read_text(encoding='utf-8')
assert 'plotly.js v3.1.0' in libtext[:500]
template=(O/'viewer_template.html').read_text(encoding='utf-8')
html=template.replace('__PLOTLY_LIBRARY__',libtext).replace('__GEOMETRY_DATA__',json.dumps(D,separators=(',',':'))).replace('__GEOMETRY_MATH__',(O/'viewer_math.js').read_text())
(O/'BOUNDARY11_VIEWER.html').write_text(html,encoding='utf-8')
(O/'evidence/viewer_library.json').write_text(json.dumps({'source':'https://cdn.plot.ly/plotly-3.1.0.min.js','version':'3.1.0','license':'MIT; header retained','sha256':hashlib.sha256(library.read_bytes()).hexdigest(),'standalone_no_network_required':True},indent=2)+'\n')
plt.rcParams.update({'font.size':9,'axes.titlesize':11,'axes.labelsize':8,'svg.fonttype':'none'})
colors={'seam':'#b94747','horizontal':'#087f8c','chamfer':'#7652aa'}

def qpoints(R):
    t=np.sqrt(R*R-1/3)
    return np.array([[np.array(e['midpoint'])+sg*t*np.array(e['unit_direction']) for sg in [-1,1]] for e in edges])
def wire(ax,r,col,alpha=.18):
    u=np.linspace(0,2*np.pi,60); vv=np.linspace(-np.pi/2,np.pi/2,13)
    xx=r*np.outer(np.cos(u),np.cos(vv)); yy=r*np.outer(np.sin(u),np.cos(vv)); zz=r*np.outer(np.ones_like(u),np.sin(vv))
    ax.plot_wireframe(xx,yy,zz,rcount=9,ccount=7,color=col,lw=.35,alpha=alpha)
def scene(ax,R,elev=24,azim=-62,spheres=True,radial=False,labels=False):
    points=qpoints(R)
    if spheres:
        wire(ax,R,'#8d9aa3',.2);wire(ax,a,'#2e9463',.22);wire(ax,rho,'#3785bf',.23)
    pc=Poly3DCollection([V[f] for f in D['faces']],facecolor='#87b4d0',edgecolor='none',alpha=.24)
    ax.add_collection3d(pc)
    for e,p in zip(edges,points):
        ax.plot(*p.T,color=colors[e['class']],lw=.8,alpha=.8)
        ax.scatter(*p.T,color=colors[e['class']],s=10,depthshade=False)
        ax.plot(*V[e['vertices']].T,color='#173247',lw=1.5)
    if radial:
        proj=V*R/rho;ax.scatter(*proj.T,color='#d67720',marker='x',s=22,depthshade=False)
    lim=1.05*R;ax.set(xlim=(-lim,lim),ylim=(-lim,lim),zlim=(-lim,lim),xlabel='x / w',ylabel='y centred / w',zlabel='z / w')
    ticks=np.linspace(-R,R,5)
    ax.set_xticks(ticks);ax.set_yticks(ticks);ax.set_zticks(ticks)
    for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
    if elev==90:ax.set_zticks([]);ax.set_zlabel('')
    if elev==0 and azim==-90:ax.set_yticks([]);ax.set_ylabel('')
    ax.set_box_aspect((1,1,1));ax.view_init(elev,azim);ax.set_proj_type('ortho');ax.tick_params(labelsize=7,pad=0)
    for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.set_pane_color((1,1,1,0));axis._axinfo['grid']['color']=(.85,.88,.90,.55)

fig=plt.figure(figsize=(11,8));
for k,(elev,azim,title) in enumerate([(24,-62,'Oblique: 3D panels and straight lines'),(90,-90,'Axial view: projection only'),(0,-90,'Side view: latitude structure'),(18,30,'Opposite oblique: radial crosses added')],1):
    ax=fig.add_subplot(2,2,k,projection='3d');scene(ax,1,elev,azim,radial=k==4);ax.set_title(title,pad=4)
fig.suptitle('R / w = 1 (illustrative): 42 edge-line exits; radial projection has 18 points',fontsize=12)
fig.subplots_adjust(left=.02,right=.98,bottom=.045,top=.91,wspace=.04,hspace=.22)
fig.savefig(F/'01_static_views.png',dpi=190);fig.savefig(F/'01_static_views.svg');plt.close(fig)

fig=plt.figure(figsize=(11,4))
for k,event in enumerate(D['coincidence_events'],1):
    ax=fig.add_subplot(1,3,k,projection='3d');scene(ax,event['R_over_w'],24,-62,spheres=False)
    ax.set_title(['Vertex sphere','Crossing A','Crossing B'][k-1]+f"\nR/w = {event['R_over_w']:.9f}; 18 points",pad=4)
fig.suptitle('Exactly the three coincidence radii; 42 labelled incidences remain at each',fontsize=12)
fig.subplots_adjust(left=.02,right=.98,bottom=.06,top=.78,wspace=.02)
fig.savefig(F/'02_coincidence_spheres.png',dpi=190);fig.savefig(F/'02_coincidence_spheres.svg');plt.close(fig)

R=np.linspace(rho,2.05,1100);t=np.sqrt(R*R-1/3);fplus=(.5+t)/np.sqrt(2);fminus=(.5-t)/np.sqrt(2)
fig,ax=plt.subplots(figsize=(10.5,3.6))
for z,col,label,style in [(t,colors['seam'],'Seam: ±t (3 per signed level)','-'),(np.ones_like(t)*.5,colors['horizontal'],'Horizontal: ±1/2 (6 per signed level)','-'),(fplus,colors['chamfer'],'Chamfer: ±(1/2+t)/√2 (6 per level)','-'),(fminus,colors['chamfer'],'Chamfer: ±(1/2−t)/√2 (6 per level)','--')]:
    ax.plot(R,np.degrees(np.arcsin(np.clip(z/R,-1,1))),color=col,label=label,ls=style,lw=1.4)
    ax.plot(R,-np.degrees(np.arcsin(np.clip(z/R,-1,1))),color=col,ls=style,lw=1.4)
for e in D['coincidence_events']:ax.axvline(e['R_over_w'],color='#8996a1',lw=.8,alpha=.7)
ax.set(xlabel='Enclosing radius R / w',ylabel='Latitude (degrees)',xlim=(rho,2.05),ylim=(-90,90));ax.grid(alpha=.2);ax.legend(loc='upper left',bbox_to_anchor=(1.01,1),frameon=False,fontsize=8)
fig.tight_layout();fig.savefig(F/'03_latitude_families.png',dpi=190);fig.savefig(F/'03_latitude_families.svg');plt.close(fig)

# Numerical drawing data are derived from the exact inventory and do not select a radius by point count.
examples=[]
for R0 in [rho,0.7,np.sqrt(7/12),1,D['coincidence_events'][2]['R_over_w'],2]:
    p=qpoints(R0);err=max(abs(np.linalg.norm(x)-R0) for x in p.reshape(-1,3))
    assert err<3e-15
    examples.append({'R_over_w':float(R0),'maximum_sphere_residual':float(err),'points':p.tolist()})
(O/'data/numerical_display_examples.json').write_text(json.dumps(examples,indent=2)+'\n')
print(json.dumps({'viewer_bytes':(O/'BOUNDARY11_VIEWER.html').stat().st_size,'static_figures':sorted(p.name for p in F.iterdir()),'sample_sphere_residual_max':max(e['maximum_sphere_residual'] for e in examples)},indent=2))
