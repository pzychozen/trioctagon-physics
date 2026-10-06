"""Five mathematical schematics; no fitted data, parameter scan or physical imagery."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','pdf.fonttype':42,'svg.fonttype':'none'})
NAVY='#16324f'; TEAL='#147d83'; LIGHT='#edf4f7'; GREY='#5a6976'; GOLD='#a66b12'
def start(title,size=(11,4)):
 fig,ax=plt.subplots(figsize=size);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
 ax.text(.015,.98,title,fontsize=19,fontweight='bold',color=NAVY,va='top')
 return fig,ax
def box(ax,x,y,w,h,title,body='',color=TEAL):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.01,rounding_size=0.015',facecolor=LIGHT,edgecolor=color,lw=1.5))
 ax.text(x+w/2,y+h*.73,title,ha='center',va='center',fontsize=14,fontweight='bold',color=NAVY)
 if body:ax.text(x+w/2,y+h*.32,body,ha='center',va='center',fontsize=12,color=GREY,linespacing=1.4)
def arrow(ax,x,y,X,Y,dashed=False):
 ax.annotate('',xy=(X,Y),xytext=(x,y),arrowprops=dict(arrowstyle='->',color=GREY,lw=1.4,linestyle='--' if dashed else '-'))
def save(fig,name,note):
 fig.text(.03,.025,note,fontsize=10,color=GREY)
 fig.subplots_adjust(left=.015,right=.985,top=.985,bottom=.08)
 for ext in ('pdf','svg','png'):fig.savefig(OUT/f'{name}.{ext}',dpi=180,facecolor='white')
 plt.close(fig)
fig,ax=start('Native map, response, and representation')
box(ax,.02,.51,.23,.28,'Native map F','amplitude/coupling\nthen phase synchronization')
box(ax,.385,.51,.23,.28,'Derivative DF','fixed positive background\nfinite-ring response')
box(ax,.75,.51,.23,.28,'Spectral test','diagonal balance\nversus general SPD')
arrow(ax,.25,.65,.38,.65);arrow(ax,.62,.65,.745,.65)
box(ax,.09,.08,.33,.24,'Adopted decoder D','three labelled tangent fibres')
box(ax,.58,.08,.33,.24,'Passive observables','spatial equivariants / coherence')
arrow(ax,.13,.50,.25,.33);arrow(ax,.50,.50,.74,.33)
ax.text(.67,.435,'linear response of',ha='center',fontsize=10,color=GREY)
save(fig,'01_architecture','Derivation: GR0-GR2, CM0, SA0. No arrow denotes a physical interaction.')
fig,ax=start('Weighted response before and after synchronization')
box(ax,.02,.33,.26,.41,'Equal background','constant weights\ncommuting Fourier factors')
box(ax,.365,.33,.27,.41,'Unequal pre-stage P',r'weights $r_i^2$'+'\n'+r'edge weights $g r_i r_j$')
box(ax,.72,.33,.26,.41,'Complete response SP','native stage order\ncycle balance may fail',GOLD)
arrow(ax,.28,.53,.36,.53);arrow(ax,.64,.53,.715,.53)
ax.text(.5,.13,r'$R^2P=P^T R^2$ does not imply a positive diagonal balance for $SP$.',ha='center',fontsize=14,color=NAVY)
save(fig,'02_weighted_response','Derivation: GR1 §§3-6. Conductance language assumes g > 0; no spacetime identification.')
fig,ax=start('Finite-ring spectral alternatives',(11,5))
box(ax,.02,.57,.27,.27,'Triad, N = 3','positive radii: real quotient\nnear stable equality: SPD')
box(ax,.365,.57,.27,.27,'Six-ring, N = 6','generic weak domain: real\nexceptional native defect')
box(ax,.71,.57,.27,.27,'N = 3q, q ≥ 3','distinct radii + ΓB ≠ 0:\nnon-real Bloch modes',GOLD)
box(ax,.20,.11,.19,.25,'δ < 0','complex pair',GOLD)
box(ax,.425,.11,.19,.25,'δ = 0','rank 1, square zero',GOLD)
box(ax,.65,.11,.19,.25,'δ > 0','three simple real roots')
arrow(ax,.50,.56,.52,.38);arrow(ax,.39,.23,.42,.23);arrow(ax,.615,.23,.645,.23)
save(fig,'03_spectral_hierarchy','Derivation: GR2 §§3-6. Bottom row: fixed nonzero small τ, sufficiently small δ; stability can persist.')
fig,ax=start('Spatial covariance and independent chiral projections',(11,4.8))
box(ax,.345,.58,.31,.23,r'Channel area $C=q\times p$','not an ambient Cartesian vector')
box(ax,.04,.19,.40,.24,r'Horizontal axial $W=T_fC$','transverse channel-area component')
box(ax,.56,.19,.40,.24,r'Vertical polar $\Gamma_{\rm ch}e_z$','common channel-area component')
arrow(ax,.40,.57,.25,.44);arrow(ax,.60,.57,.75,.44)
ax.text(.25,.055,'Polar spaces: 2 linear, 5 quadratic',ha='center',fontsize=13,color=NAVY)
ax.text(.75,.055,'Axial spaces: 2 linear, 3 quadratic',ha='center',fontsize=13,color=NAVY)
save(fig,'04_observables','Derivation: CM0 §§3-4. Dimensions count maps; parity does not supply a physical position or axis.')
fig,ax=start('Typed state-to-shell attachment',(11,5))
box(ax,.015,.55,.22,.27,'Preparation','lens + incident pair\nsix complex coordinates')
box(ax,.385,.55,.22,.27,r'Canonical $\Omega_0$','named extraction\nthree complex channels')
box(ax,.755,.55,.23,.27,r'$D\Omega_0$','three tangent vectors\nsix real coordinates')
arrow(ax,.24,.68,.38,.68);arrow(ax,.61,.68,.75,.68)
box(ax,.07,.12,.36,.24,'Fixed shell / scaffold','geometry and incidence only')
box(ax,.57,.12,.36,.24,'Continuous field / boundary law','no native definition',GOLD)
arrow(ax,.88,.54,.78,.37,True)
ax.text(.51,.22,'≠',ha='center',va='center',fontsize=28,color=GOLD)
save(fig,'05_typed_attachment','Derivation: SA0 §§2-3,7. Dashed arrow is absent, not a proposed model extension.')
(OUT/'FIGURE_SOURCES.json').write_text(json.dumps({'generator':'generate_figures.py','figures':[
 {'file':f'{i:02d}_{n}.pdf','type':'schematic; no numerical dataset','authority':s} for i,n,s in [
 (1,'architecture','GR0–GR2; SA0'),(2,'weighted_response','GR1 §§3–6'),(3,'spectral_hierarchy','GR2 §§3–6'),
 (4,'observables','CM0 §§3–4'),(5,'typed_attachment','SA0 §§2–3,7')]]},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Generated five PDF/SVG/PNG mathematical schematics.')
