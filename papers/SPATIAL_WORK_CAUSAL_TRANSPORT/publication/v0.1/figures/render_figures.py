"""Deterministic abstract account/support diagrams; no trajectory simulation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

assert os.environ.get('CONDA_DEFAULT_ENV') == 'torment', 'Activate torment in Command Prompt.'
ROOT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'pdf.fonttype':42,
    'svg.fonttype':'none','svg.hashsalt':'spatial-causal-v01','mathtext.fontset':'dejavusans'})
BLUE='#234f73'; TEAL='#24746a'; INK='#27313d'; GRAY='#65717d'; LIGHT='#eef3f7'
DATE=datetime(2026,11,10,tzinfo=timezone.utc)

def txt(ax,x,y,s,size=10,color=INK,ha='center',**kw):
    return ax.text(x,y,s,fontsize=size,color=color,ha=ha,va='center',**kw)
def arrow(ax,x0,y0,x1,y1,color=BLUE,lw=1.8):
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),arrowprops={'arrowstyle':'-|>','color':color,'lw':lw})
def box(ax,x,y,w,h):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06,rounding_size=0.09',
        fc=LIGHT,ec='#9caebe',lw=1))
def save(fig,name):
    fig.savefig(ROOT/(name+'.pdf'),bbox_inches='tight',pad_inches=.07,
        metadata={'Title':name,'Author':'Hilmir Frímann Halldórsson (pzychozen)',
        'CreationDate':DATE,'ModDate':DATE,'Creator':'Deterministic Matplotlib figure source'})
    fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight',pad_inches=.07,
        metadata={'Date':'2026-11-10','Creator':'Deterministic Matplotlib figure source'})
    fig.savefig(ROOT/(name+'.png'),dpi=170,bbox_inches='tight',pad_inches=.07)
    plt.close(fig)

fig,ax=plt.subplots(figsize=(11.4,4.4)); ax.set(xlim=(0,11.5),ylim=(0,4.55)); ax.axis('off')
txt(ax,5.75,4.3,'Abstract state connection',13)
box(ax,.15,1.3,2.25,2); box(ax,8.95,1.3,2.35,2)
txt(ax,1.27,2.85,'Retained RX',12); txt(ax,1.27,2.32,r'$x,\ Q,\ z$',13)
txt(ax,1.27,1.7,r'$H_{\rm RX}=H_N+H_C+H_R$',9)
txt(ax,10.12,2.85,'New receiving field',11); txt(ax,10.12,2.32,r'$\zeta\in Y$',13)
txt(ax,10.12,1.7,r'$H_G=\beta_G\|\zeta\|_Y^2/2$',10)
txt(ax,3.0,3.55,r'Near: $\xi=0$',10); txt(ax,8.2,3.55,r'Far: $\xi=\theta_X(s)$',10)
arrow(ax,2.65,2.73,8.7,2.73,BLUE); arrow(ax,8.7,1.93,2.65,1.93,TEAL)
txt(ax,2.9,2.99,r'$a$',12,BLUE); txt(ax,8.42,2.99,r'$c$',12,BLUE)
txt(ax,2.9,1.65,r'$b$',12,TEAL); txt(ax,8.42,1.65,r'$d$',12,TEAL)
txt(ax,5.65,3.03,r'$u_+:\ \partial_tu_++\partial_\xi u_+=0$',10,BLUE)
txt(ax,5.65,1.64,r'$u_-:\ \partial_tu_--\partial_\xi u_-=0$',10,TEAL)
txt(ax,5.65,2.33,r'$E_{\rm tr}\geq0$   |   $\xi$ is time / age',11)
txt(ax,1.27,.83,r'$\dot H_{\rm RX}=-P_N$',11)
txt(ax,5.65,.83,r'$\dot E_{\rm tr}=P_N-P_G$',11)
txt(ax,10.12,.83,r'$\dot H_G=P_G$',11)
txt(ax,5.75,.26,'Indexed by (s, X); no ambient path or physical aperture flux is drawn.',10,GRAY)
save(fig,'channel_account')

fig,(ax,lat)=plt.subplots(2,1,figsize=(11.3,6.35),gridspec_kw={'height_ratios':[1,1.05]})
fig.subplots_adjust(hspace=.38)
ax.set(xlim=(-2.1,5),ylim=(0,3.8)); ax.axis('off')
txt(ax,-2.05,3.6,'A  One fixed delay: history and temporal test',12,ha='left')
theta=1.2; T=3.5
for y in (2.7,1.25):
    ax.plot([-1.7,4.65],[y,y],color='#b4bdc5',lw=.9)
ax.plot([0,T],[2.7,2.7],color=BLUE,lw=7,solid_capstyle='butt')
ax.plot([-theta,0],[1.25,1.25],color=TEAL,lw=7,solid_capstyle='butt')
ax.plot([0,T-theta],[1.25,1.25],color=BLUE,lw=7,solid_capstyle='butt')
for x,y,s in [(0,2.32,'0'),(T,2.32,r'$T$'),(-theta,.88,r'$-\theta$'),(0,.88,'0'),(T-theta,.88,r'$T-\theta$')]:
    txt(ax,x,y,s,10)
txt(ax,4.65,2.7,r'$\lambda(t)$',11,ha='right')
txt(ax,4.65,1.25,r'$q(u)$',11,ha='right')
arrow(ax,1.8,2.52,.6,1.44,BLUE,1.4)
txt(ax,2.25,2.02,r'Observation: $u=t-\theta$',10,ha='left')
arrow(ax,-.35,1.44,.85,2.52,TEAL,1.4)
txt(ax,-2.02,1.98,r'Adjoint: $t=u+\theta$',10,TEAL,ha='left')
txt(ax,-.6,.4,'prehistory',9,TEAL)
txt(ax,2.1,.08,r'Full geometry: forward adjoint is zero a.e. when $T\leq\theta_-$.',10)
lat.set(xlim=(-.6,3.4),ylim=(0,4)); lat.axis('off')
txt(lat,-.58,3.85,'B  Empty added states and the carrier-preload witness',12,ha='left')
lat.axvline(1,ymin=.13,ymax=.8,color='#aab5bf',ls=':',lw=1)
lat.axvline(2,ymin=.13,ymax=.8,color='#aab5bf',ls=':',lw=1)
for y in (2.9,1.85,.8): lat.plot([0,3.1],[y,y],color='#b4bdc5',lw=.9)
txt(lat,-.15,2.9,r'$H_G$',11,ha='right'); txt(lat,-.15,1.85,r'$b$',11,ha='right')
txt(lat,-.15,.8,'launch',10,ha='right')
lat.plot([0,1],[2.9,2.9],color=GRAY,lw=4,solid_capstyle='butt')
lat.plot([0,2],[1.85,1.85],color=GRAY,lw=4,solid_capstyle='butt')
lat.plot([1.015,1.35],[2.9,2.9],color=TEAL,lw=6,solid_capstyle='butt')
lat.plot([2.015,2.35],[1.85,1.85],color=TEAL,lw=6,solid_capstyle='butt')
for x,y in [(1,2.9),(1.36,2.9),(2,1.85),(2.36,1.85)]:
    lat.plot(x,y,'o',ms=4,mfc='white',mec=TEAL,zorder=4)
txt(lat,.5,3.22,'zero through '+r'$\theta_-$',9)
txt(lat,1.87,3.22,r'$H_G>0$ on $(\theta_-,\theta_-+\varepsilon)$',10,TEAL)
txt(lat,.9,2.17,r'zero a.e. before $2\theta_-$',9)
txt(lat,2.48,1.44,r'$\|b\|_V>0$ a.e.',10,TEAL)
txt(lat,2.48,1.15,r'on $(2\theta_-,2\theta_-+\varepsilon)$',9,TEAL)
arrow(lat,.02,.8,3,.8,BLUE)
txt(lat,1.5,.49,r'$-\kappa^2Q$ acts immediately',10,BLUE)
for x,s in [(0,'0'),(1,r'$\theta_-$'),(2,r'$2\theta_-$')]: txt(lat,x,.12,s,10)
txt(lat,3.1,.12,'t',11)
save(fig,'time_support')
record={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.iterdir()) if p.suffix in {'.pdf','.svg','.png','.py'}}
(ROOT/'FIGURE_IDENTITIES.json').write_text(json.dumps({'scope':'Deterministic explanatory vector figures; no scientific-suite execution.','files':record},indent=2)+'\n',encoding='utf-8')
print('Created both PDF/SVG figures and PNG previews.')
