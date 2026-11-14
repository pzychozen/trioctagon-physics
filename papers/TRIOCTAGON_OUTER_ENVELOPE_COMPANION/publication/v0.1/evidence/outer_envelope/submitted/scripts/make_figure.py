"""Explanatory rendering from certified cycles, never a geometry decision."""
from common import *
from geometry import *
import importlib.metadata
os.environ['MPLCONFIGDIR']=str(R/'scratch/matplotlib_config')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
cert=read(D/'exact_certificate.json');checked=read(D/'CHECKER_RESULT.json');changes=read(D/'TRANSITION_READOUT.json');points=inventory_family()
patch=next(r for r in changes['six_local_changes'] if r['transition_face']==checked['candidate']['transition_facet_id']);labels=patch['transition_cycle']
settings=[('C1',Q(F(3,5)),'Before: two triangles + one quadrilateral'),('T',T,'At x*: one maximal hexagon'),('C2',Q(F(2,3)),'After: two quadrilaterals')]
fig=plt.figure(figsize=(15,5.4),facecolor='white');colors=['#75b8d1','#edb969','#9cc6a3'];all_xyz=[]
for kind,t,_ in settings:
    all_xyz.extend([[float(v[0]),float(v[1])*3**.5,float(v[2])] for label in labels for v in [veval(points[label],t)]])
all_xyz=np.array(all_xyz);center=(all_xyz.min(axis=0)+all_xyz.max(axis=0))/2;span=max(np.ptp(all_xyz,axis=0))*1.32
for i,(kind,t,title) in enumerate(settings,1):
    ax=fig.add_subplot(1,3,i,projection='3d');xyz={label:np.array([float(v[0]),float(v[1])*3**.5,float(v[2])]) for label in labels for v in [veval(points[label],t)]}
    faces=[{'cycle':labels}] if kind=='T' else patch[kind]
    for j,f in enumerate(faces):
        ax.add_collection3d(Poly3DCollection([[xyz[k] for k in f['cycle']]],facecolors=colors[j%3],edgecolors='#233748',linewidths=1.8,alpha=.86))
    for label in labels:
        p=xyz[label];left=p[0]<center[0];shift=np.array([-.025 if left else .025,0,.028 if p[2]>center[2] else -.025]);ax.scatter(*p,color='#182d3d',s=18,depthshade=False);ax.text(*(p+shift),label,fontsize=8,color='#102535',ha='right' if left else 'left',va='bottom' if p[2]>center[2] else 'top')
    for axis,c in zip([ax.set_xlim,ax.set_ylim,ax.set_zlim],center):axis(c-span/2,c+span/2)
    ax.set_box_aspect((1,1,1));ax.view_init(elev=22,azim=-90);ax.set_axis_off()
    ax.set_title(title+'\n'+('x = 3(√2 − 1)/2' if kind=='T' else ('x = 3/5' if kind=='C1' else 'x = 2/3')),fontsize=11,pad=1)
fig.suptitle('One of six symmetry-related outer-envelope facet changes',fontsize=16,y=.99)
fig.text(.5,.045,'Actual 3D facet patches at width w = 1; fixed camera and common scale. Black lines are convex-envelope edges.\nThe six branch positions remain distinct. Convexification is an observation convention, not an adopted material wall.',ha='center',fontsize=10,color='#374654')
fig.subplots_adjust(left=.01,right=.99,top=.86,bottom=.15,wspace=.01)
out=R/'figures';out.mkdir(exist_ok=True)
for ext in ['png','svg']:fig.savefig(out/('local_facet_transition.'+ext),dpi=170,facecolor='white')
plt.close(fig)
write(out/'FIGURE_RECORD.json',{'created_utc':now(),'purpose':'Optional explanatory numerical rendering of certified exact face cycles; no proof supplied by the image.','certificate_sha256':sha((D/'exact_certificate.json').read_bytes()),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'parameters':[t.dump() for _,t,_ in settings],'same_three_nomination_parameters_reused':True,'additional_hull_nominations':0,'normalization':'Physical coordinates divided by common width w=1; common plotting scale and camera.','triangulation':'Matplotlib renders filled planar maximal polygons internally; only true polygon boundary edges are displayed.','viewpoint':'azimuth -90 degrees, elevation 22 degrees; illustration only, no new geometric/physical adoption.','files':[{'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sorted(out.glob('local_facet_transition.*'))]})
print('Created explanatory PNG/SVG; matplotlib',matplotlib.__version__)
