"""Paper E exact analytic figures and rendering of frozen, attributed replay data."""
import runtime
from runtime import ROOT
import numpy as np,matplotlib,json,hashlib,datetime
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
F=ROOT/'figures';F.mkdir(exist_ok=True)
D=np.load(ROOT/'evidence/plot_data.npz',allow_pickle=False)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':11,'axes.labelsize':10,
                     'svg.fonttype':'none','svg.hashsalt':'paper-e-v01','pdf.fonttype':42,'savefig.facecolor':'white'})
BLUE='#176b91';ORANGE='#bc562b';GREEN='#397650';INK='#223444';GRAY='#adb9c0';registry=[]
def save(fig,name,description):
    for ext in ('pdf','svg','png'):
        meta={'Creator':'Paper E generate_figures.py'} if ext=='pdf' else {}
        if ext=='pdf':meta.update(CreationDate=datetime.datetime(2026,9,23,tzinfo=datetime.timezone.utc),ModDate=datetime.datetime(2026,9,23,tzinfo=datetime.timezone.utc))
        fig.savefig(F/(name+'.'+ext),dpi=220,bbox_inches='tight',pad_inches=.16,metadata=meta)
    registry.append({'name':name,'description':description,'formats':['pdf','svg','png']});plt.close(fig)
def h(name,key):return D[name+'__'+key]
def norm(a):return np.linalg.norm(a,axis=-1)
def M(th,l=.244,A=1):
    z=A*np.cos(3*(th-l));return z[:,None]*np.column_stack((np.cos(th),np.sin(th),np.ones(len(th))))
def spatial(ax,points,title,lim=None,labels=('X','Y','Z')):
    ax.plot(*points.T,color=BLUE,lw=.8);ax.set_title(title,pad=12);ax.set_box_aspect((1,1,1))
    center=(points.max(axis=0)+points.min(axis=0))/2;r=max(np.ptp(points,axis=0).max()/2,1e-10)*1.12
    if lim is not None:center=np.zeros(3);r=lim
    ax.set(xlim=(center[0]-r,center[0]+r),ylim=(center[1]-r,center[1]+r),zlim=(center[2]-r,center[2]+r))
    ax.set_xlabel(labels[0],labelpad=2);ax.set_ylabel(labels[1],labelpad=2);ax.set_zlabel('');ax.tick_params(labelsize=8,pad=0)
    # Keep the third-coordinate label within the panel: Axes3D's ordinary
    # external label can be clipped by a neighbouring panel's background.
    ax.text2D(.90,.90,labels[2],transform=ax.transAxes,ha='center',va='center',fontsize=9)
def box(ax,xy,w,h,text,face='#edf3f6'):
    ax.add_patch(FancyBboxPatch(xy,w,h,boxstyle='round,pad=0.018',facecolor=face,edgecolor=BLUE,lw=1))
    ax.text(xy[0]+w/2,xy[1]+h/2,text,ha='center',va='center',fontsize=10)
def arrow(ax,a,b,**kw):ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color=INK,lw=1.5,**kw))
fig,ax=plt.subplots(figsize=(9,4.2));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
box(ax,(.20,.82),.6,.13,'Record current state (including stored Z) before the step')
nodes=[(.02,.52),(.36,.52),(.70,.52),(.70,.18),(.36,.18),(.02,.18)]
texts=['Pre-sync amplitude / coupling\n'+r'$V=\Omega+\epsilon\Omega(k-|\Omega|^2)+gL_3\Omega+\delta$',
       'Phase synchronization\nthen optional complex noise','Commit new '+r'$\Omega$'+'\nadvance q, then t by dt',
       'Compute scalar z\nthen macro M','Compute channel C\nthen T = alpha M + beta C','Cycle / identity diagnostics\nreturn to next pre-step record']
for xy,t in zip(nodes,texts):box(ax,xy,.28,.20,t)
arrow(ax,(.23,.82),(.16,.72));arrow(ax,(.30,.62),(.36,.62));arrow(ax,(.64,.62),(.70,.62));arrow(ax,(.84,.52),(.84,.38));arrow(ax,(.70,.28),(.64,.28));arrow(ax,(.36,.28),(.30,.28))
ax.text(.5,.055,'Z is a downstream readout in this core; the next Omega update does not read it.',ha='center',color=INK)
save(fig,'01_update_order','Exact dependency order; grouping does not change sequential order.')
th=np.linspace(0,2*np.pi,1601);q=np.arange(12)*np.pi/6;ex=.244+np.arange(6)*np.pi/3
fig,ax=plt.subplots(figsize=(7.4,3.4));ax.plot(th*180/np.pi,np.cos(3*(th-.244)),color=BLUE,label='Frozen A = 1')
ax.scatter(q*180/np.pi,np.cos(3*(q-.244)),color=ORANGE,s=28,label='Default 12-clock samples',zorder=3)
ax.scatter(ex*180/np.pi,(-1.)**np.arange(6),color=GREEN,marker='x',s=45,label='Continuous extrema',zorder=4)
ax.axhline(0,color=GRAY,lw=.7);ax.set(xlabel='Clock angle (degrees)',ylabel='z / A',xlim=(0,360));ax.legend(loc='lower left',fontsize=8,ncol=1)
save(fig,'02_scalar_harmonic','Frozen scalar harmonic; default samples miss all continuous extrema.')
fig=plt.figure(figsize=(7,4.8));ax=fig.add_subplot(111,projection='3d');pts=M(th);spatial(ax,pts,'Macro curve on its direct-coordinate double cone',1.12,('M1','M2','M3'))
theta=np.linspace(0,2*np.pi,25);rr=np.linspace(0,1,6);TT,RR=np.meshgrid(theta,rr)
for sign in [-1,1]:ax.plot_wireframe(RR*np.cos(TT),RR*np.sin(TT),sign*RR,color=GRAY,alpha=.22,lw=.5)
ee=M(ex);ax.scatter(*ee.T,color=ORANGE,s=26)
for pt,name in zip(ee,['U0','L2','U1','L0','U2','L1']):ax.text(*(pt*1.08),name,fontsize=9)
save(fig,'03_macro_cone','Double cone and proven signed-extremum visiting order; no gap locations implied.')
fig,axs=plt.subplots(1,2,figsize=(9,3.8));xy=pts[:,:2];axs[0].plot(*xy.T,color=BLUE,label='Continuous projection')
ss=M(q);axs[0].plot(*np.vstack([ss[:,:2],ss[:1,:2]]).T,color=ORANGE,ls='--',marker='o',ms=3,label='12-sample polyline')
axs[0].set_aspect('equal');axs[0].set(xlabel='M1',ylabel='M2',title='Three-petal rose, frozen amplitude');axs[0].legend(fontsize=8,loc='lower left')
axs[1].plot(th,pts[:,0],color=INK,label='Mx');axs[1].plot(th,.5*np.cos(4*th-3*.244),color=BLUE,label='frequency 4 term');axs[1].plot(th,.5*np.cos(2*th-3*.244),color=ORANGE,label='frequency 2 term');axs[1].set(xlabel='theta (radians)',ylabel='Coordinate value',title='Exact product-to-sum decomposition');axs[1].legend(fontsize=8)
fig.subplots_adjust(wspace=.35);save(fig,'04_rose_decomposition','Planar projection, sampling, and Mx harmonic summands; My companion derived in text.')
fig=plt.figure(figsize=(10,3.6));lim=max(norm(h('baseline',k)).max() for k in ['Z_macro','Z_chiral','Z_total'])*1.1
for j,k in enumerate(['Z_macro','Z_chiral','Z_total']):spatial(fig.add_subplot(1,3,j+1,projection='3d'),h('baseline',k),k,lim,('Z1','Z2','Z3'))
fig.subplots_adjust(wspace=.14);save(fig,'05_components','Baseline direct components, common scale, no percentile normalization.')
fig,axs=plt.subplots(1,3,figsize=(9.4,3.2))
for ax,c,title in zip(axs,[np.array([.75,.50]),np.array([-.65,.25]),np.array([-1.,.07])],['Constructive','Destructive','Near cancellation']):
    m=np.array([1.,0]);t=m+c
    for a,b,col in [(np.zeros(2),m,BLUE),(m,t,ORANGE),(np.zeros(2),t,GREEN)]:ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color=col,lw=2))
    ax.set(xlim=(-.2,1.9),ylim=(-.35,.85),title=title);ax.set_aspect('equal');ax.axhline(0,color=GRAY,lw=.6);ax.axis('off')
    ax.text(.5,-.20,'alpha M',color=BLUE,ha='center');ax.text(1.0,.68,'beta C',color=ORANGE,ha='center');ax.text(t[0]-.03,t[1]+.10,'T',color=GREEN)
fig.text(.5,.04,'Illustrative weighted vectors in a chosen plane; not a historical trajectory or scaffold map.',ha='center',fontsize=9)
save(fig,'06_blend_alignment','Vector-addition geometry and cancellation; coefficients absorbed into arrows.')
kap=h('baseline','kappa');z=h('baseline','z');angle=2*np.pi*h('baseline','phi_index')/12
cylinder=np.column_stack([kap*np.cos(angle),kap*np.sin(angle),z]);r=kap/(1+kap);chi=np.pi*z/(2*(np.max(abs(z))+1e-9))
torus=np.column_stack([(2+r*np.cos(chi))*np.cos(angle),(2+r*np.cos(chi))*np.sin(angle),r*np.sin(chi)])
fig=plt.figure(figsize=(8,7.3))
for j,(a,title) in enumerate([(cylinder,'Scalar cylinder'),(torus,'History-normalized torus'),(h('baseline','Z_total'),'Direct total')]):spatial(fig.add_subplot(2,2,j+1,projection='3d'),a,title)
ax=fig.add_subplot(224,projection='3d');o=h('baseline','Omega');curves=[]
for j in range(3):
    rad=.6*(1+.4*np.log1p(abs(o[:,j])));ph=np.angle(o[:,j]);aj=2*np.pi*j/3
    curves.append(np.column_stack([(2+rad*np.cos(ph))*np.cos(aj),(2+rad*np.cos(ph))*np.sin(aj),rad*np.sin(ph)]))
spatial(ax,np.concatenate(curves),'Three channel torus curves',3.)
ax.lines[0].remove()
for j,a in enumerate(curves):ax.plot(*a.T,lw=1,label='channel '+str(j+1))
ax.legend(fontsize=8,loc='upper left');fig.subplots_adjust(wspace=.14,hspace=.32)
save(fig,'07_four_displays','Four distinct maps of the same stored baseline; equal axis units within each panel.')
vv=h('subcritical','v');j=int(np.nanargmax(vv[1:64])+1);center=j+1;start=max(0,center-8);stop=center+9
fig=plt.figure(figsize=(9,4));ax=fig.add_subplot(121);rows=np.arange(start+1,stop)
for key,label,color in [('v','full v',INK),('dZ','displacement',BLUE),('dphi','phase',ORANGE)]:ax.plot(rows,h('subcritical',key)[start:stop-1],label=label,color=color,lw=1.4)
ax.plot(rows,.5*h('subcritical','dcorr')[start:stop-1],color=GREEN,label='clock term');ax.axhline(.8,color=GRAY,ls='--');ax.axvline(center,color=GRAY,ls=':');ax.set(xlabel='Endpoint history row',ylabel='Weighted diagnostic',title='Recovered phase-off event');ax.legend(fontsize=8)
ax=fig.add_subplot(122,projection='3d');points=h('subcritical','Z_total')[start:stop];spatial(ax,points,'Local direct-T window',labels=('T1','T2','T3'));ax.scatter(*h('subcritical','Z_total')[center],color=ORANGE,s=45)
fig.subplots_adjust(wspace=.25);save(fig,'08_spike_window','Finite full-v maximum among transitions 1..63; local endpoint/window alignment. Centre row '+str(center)+'.')
fig,axs=plt.subplots(2,2,figsize=(8.8,6))
for row,name in enumerate(['subcritical','critical']):
    a=h(name,'Z_total');valid=np.isfinite(a).all(axis=1)&(np.max(abs(a),axis=1)>0);scale=np.max(abs(a[valid]),axis=1);lognorm=np.log10(scale)+.5*np.log10(np.sum((a[valid]/scale[:,None])**2,axis=1))
    axs[row,0].plot(np.flatnonzero(valid),lognorm,color=BLUE,label='Source replay');axs[row,0].scatter(np.flatnonzero(valid)[::65],lognorm[::65],s=14,marker='x',color=ORANGE,label='Saved data (equal)')
    axs[row,0].set(title=name+': direct total magnitude',ylabel='log10 norm(T)',xlabel='History row');axs[row,0].legend(fontsize=8)
    v=h(name,'v');rows=np.arange(1,len(v)+1);good=np.isfinite(v);axs[row,1].plot(rows[good],v[good],color=BLUE);axs[row,1].axhline(.8,color=ORANGE,ls='--');axs[row,1].set(ylim=(0,4),xlabel='Endpoint history row',ylabel='v (display clipped at 4)',title=str(int(np.sum(good&(v>=.8))))+' finite threshold events')
    if name=='critical':
        for col in range(2):axs[row,col].axvspan(1279,1999,color=GRAY,alpha=.3);axs[row,col].text(1650,axs[row,col].get_ylim()[1]*.72,'nonfinite\nZ tail',ha='center',fontsize=8)
fig.subplots_adjust(hspace=.45,wspace=.33);save(fig,'09_preserved_reproduction','Phase-off saved-run reproduction; no numerical clipping in stored arrays. Shading begins at first nonfinite Z row 1279.')
fig=plt.figure(figsize=(8.5,4.2));ax=fig.add_subplot(121)
for name,col in [('baseline',BLUE),('ema',ORANGE)]:ax.plot(h(name,'t'),h(name,'z'),color=col,lw=.8,label=name)
ax.set(xlabel='Historical time t',ylabel='Scalar z',title='Same Omega; different historical Z');ax.legend(fontsize=8)
ax=fig.add_subplot(122,projection='3d');spatial(ax,h('ema','Z_total'),'Direct totals on one scale',1.4,('T1','T2','T3'));ax.lines[0].set_color(ORANGE);ax.lines[0].set_label('EMA');ax.plot(*h('baseline','Z_total').T,color=BLUE,lw=.8,label='staged');ax.legend(fontsize=8)
fig.subplots_adjust(wspace=.28);save(fig,'10_staged_ema','The staged envelope and committed EMA are distinct formulas; no merged long-time law.')
fig,ax=plt.subplots(figsize=(7.5,4));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
box(ax,(.12,.70),.76,.20,'Recovered Z state and readout geometry\nz, M, C, T; clock and diagnostic definitions')
arrow(ax,(.5,.70),(.5,.32));ax.text(.53,.51,'?  Spatial attachment map is unspecified',fontsize=10,va='center',bbox=dict(facecolor='white',edgecolor='none',pad=4))
box(ax,(.12,.10),.76,.21,'Author-recalled scaffold openings\n3 upper + 3 lower; no coordinates assigned here',face='#fbf1e9')
save(fig,'11_open_interface','Explicit open interface; diagram boxes are not spatial gap positions.')
(ROOT/'evidence/figure_manifest.json').write_text(json.dumps({'figures':registry,'raw_scaling':True,
 'data_sha256':hashlib.sha256((ROOT/'evidence/plot_data.npz').read_bytes()).hexdigest()},indent=2)+'\n')
print('Generated',len(registry),'figures in PDF, SVG and PNG')
