"""Regenerate explanatory vector figures from the retained exact formulas.

Adapted from the two input renderers; plotting samples are not proof evidence.
No dynamics, profile width, physical wall, tube or energetic flow is selected.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATE = datetime(2026, 11, 10, tzinfo=timezone.utc)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9,
    'axes.labelsize': 10, 'axes.titlesize': 10, 'legend.fontsize': 8,
    'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none',
    'svg.hashsalt': 'central-route-six-opening-v0.1', 'axes.spines.top': False,
    'axes.spines.right': False, 'grid.alpha': .22, 'axes.axisbelow': True})
K = np.sqrt(3)/12 + np.sqrt(6)/4
ac = K/(1+np.sqrt(3)/2)
R = np.sqrt(7)*ac/2
R0 = np.sqrt(13/12-np.sqrt(2)/2)
rg, dg, hg = np.sqrt(3)/6, 1-np.sqrt(2)/2, (np.sqrt(2)-1)/2
ag, H0 = dg/2, .5
D = np.sqrt(10-6*np.sqrt(2))
blue, orange, gray = '#205580', '#b46a27', '#53616d'
made = []

def save(fig, name):
    for suffix in ['pdf', 'svg', 'png']:
        p = ROOT/f'{name}.{suffix}'
        meta = {'Creator': 'render_figures.py; accepted source geometry'}
        if suffix == 'pdf': meta.update(CreationDate=DATE, ModDate=DATE)
        if suffix == 'svg': meta.update(Date=DATE.isoformat())
        fig.savefig(p, dpi=180, bbox_inches='tight', metadata=meta)
        made.append(p)
    plt.close(fig)

theta = np.linspace(0, 2*np.pi, 1001)
fig, ax = plt.subplots(figsize=(5.9, 4.35), layout='constrained')
ax.plot(K+R*np.cos(theta), R*np.sin(theta), color=blue, lw=1.7,
        label=r'Selected carrier $\Gamma_0$')
ax.plot(R0*np.cos(theta), R0*np.sin(theta), color=gray, ls='--', lw=1.1,
        label=r'Original sphere section $R_0$')
ax.axhline(0, color='#bbc2c8', lw=.65)
ax.axvline(0, color='#bbc2c8', lw=.65)
ax.scatter([0], [0], color='black', s=17, zorder=5)
ax.annotate(r'$O$', (0,0), xytext=(-15,-14), textcoords='offset points')
ax.scatter([ac,ac],[ac,-ac], color=orange, s=29, zorder=5)
ax.annotate(r'$P_+\in N_1^+$', (ac,ac), xytext=(-72,9), textcoords='offset points', color=orange)
ax.annotate(r'$P_-\in N_1^-$', (ac,-ac), xytext=(-72,-15), textcoords='offset points', color=orange)
ax.scatter([K-R],[0], color=blue, s=24, zorder=5)
ax.annotate('Nearest carrier point', (K-R,0), xytext=(15,22), textcoords='offset points',
            arrowprops={'arrowstyle':'-', 'color':blue, 'lw':.7}, color=blue, fontsize=8)
ax.set(xlim=(-.72,1.38), ylim=(-.72,.73), xlabel=r'Median coordinate $(P-O)\cdot u_0$',
       ylabel=r'Centered height $\zeta$')
ax.set_aspect('equal'); ax.grid(); ax.legend(loc='upper right', frameon=False)
save(fig, 'central_route')

fig, axes = plt.subplots(1,2,figsize=(7.1,3.8), layout='constrained')
t = np.linspace(0,1,151)
zz = (1-t)*hg+t*H0
envelope = D*((1-t)*ag+t*rg)
th = np.linspace(0,np.pi,1001)
for ax in axes:
    ax.fill_betweenx(zz, 0, envelope, color='#ead7bf', alpha=.9,
                     label='Individual-hull envelope')
    zline = np.linspace(0,.62,301)
    ax.plot(.6*zline+.06,zline, '--', color=orange,lw=1.3,
            label=r'$r_\perp=3|\zeta|/5+3/50$')
    ax.plot(K+R*np.cos(th), R*np.sin(th), color=blue,lw=1.7,
            label='Inherited circle projection')
    ax.set(xlabel=r'Cylindrical radius $r_\perp$', ylabel=r'Absolute height $|\zeta|$', ylim=(0,.59))
    ax.grid()
axes[0].set(xlim=(0,1.35),title='Full radial comparison')
axes[1].set(xlim=(0,.61),title='Near-axis detail')
axes[0].legend(loc='lower right', frameon=False, fontsize=8)
save(fig, 'six_opening')

record = {'python':sys.executable, 'python_version':sys.version, 'matplotlib':matplotlib.__version__,
          'numpy':np.__version__, 'generated_utc':datetime.now(timezone.utc).isoformat(),
          'method':'Regenerated from exact accepted geometry; editorial notation adapted; no simulation.',
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in made}}
(ROOT/'FIGURE_RECEIPT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
