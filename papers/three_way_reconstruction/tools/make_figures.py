"""Deterministic mathematical figures; vector PDF/SVG and 300-dpi PNG."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

OUT=Path(__file__).resolve().parents[1]/'figures'; OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':9,'mathtext.fontset':'dejavuserif','axes.spines.top':False,'axes.spines.right':False,'axes.labelsize':9,'axes.titlesize':10,'pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'none','axes.prop_cycle':matplotlib.cycler(color=['#126775','#bb5d28','#69559b','#467b42'])})
teal,orange,purple,gray='#126775','#bb5d28','#69559b','#697580'
def save(fig,name):
    for ext in ['pdf','svg','png']:fig.savefig(OUT/f'{name}.{ext}',dpi=300,bbox_inches='tight',pad_inches=.10)
    plt.close(fig)
def box(ax,xy,text,w=2.35,h=.8,color=teal,fs=10):
    ax.add_patch(FancyBboxPatch((xy[0]-w/2,xy[1]-h/2),w,h,boxstyle='round,pad=0.07',facecolor='white',edgecolor=color,lw=1.3))
    ax.text(*xy,text,ha='center',va='center',fontsize=fs,color=color)
def arr(ax,start,end,text='',color=gray,offset=(0,.17)):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=10,lw=1,color=color))
    ax.text((start[0]+end[0])/2+offset[0],(start[1]+end[1])/2+offset[1],text,ha='center',va='center',fontsize=8,color=color)
def diagram(size=(7,3)):
    f,ax=plt.subplots(figsize=size);ax.set_xlim(0,10);ax.set_ylim(0,5);ax.axis('off');return f,ax
def F(A,B,x):return (A*x**4-B*x*x+1)/(x**4-B*x*x+A)
def realroots(co):
    rr=np.roots(co);return sorted([float(r.real) for r in rr if abs(r.imag)<1e-9])
fig,axs=plt.subplots(2,2,figsize=(7,5.4),sharex=True,sharey=True,layout='constrained')
phi=(1+np.sqrt(5))/2
for ax,(A,B,label) in zip(axs.flat,[(9,9,'(9,9)'),(9,1,'(9,1)'),(np.pi,np.e,r'$(\pi,e)$'),(phi,1-phi,r'$(\phi,1-\phi)$')]):
    for inv,col,ls,lab in [(False,teal,'-',r'$f$'),(True,orange,'--',r'$1/f$')]:
        roots=realroots([A,0,-B,0,1] if inv else [1,0,-B,0,A]);cuts=[-3.3]+[r for r in roots if -3.3<r<3.3]+[3.3]
        for i,(lo,hi) in enumerate(zip(cuts[:-1],cuts[1:])):
            xx=np.linspace(lo+1e-5,hi-1e-5,1200);vv=F(A,B,xx);vv=1/vv if inv else vv
            ax.plot(xx,vv,color=col,ls=ls,lw=1.25,label=lab if i==0 else None)
        for r in roots:ax.axvline(r,color=col,lw=.45,alpha=.35)
    ax.axhline(1,color=gray,lw=.65,ls=':');ax.axhline(-1,color=gray,lw=.65,ls=':');ax.axhline(0,color=gray,lw=.45)
    ax.scatter([-1,1],[1,1],s=16,color='black',zorder=4);ax.set_title(label);ax.set_xlim(-3.3,3.3);ax.set_ylim(-4,5);ax.grid(alpha=.13)
axs[0,0].legend(loc='lower center',ncol=2,frameon=True,facecolor='white',framealpha=.95);fig.supxlabel('$x$');fig.supylabel('function value');save(fig,'01_historical_graphs')

fig,ax=plt.subplots(figsize=(6.4,3.8),layout='constrained');v=1.65+.7j;pts=[v,-v,1/v,-1/v];labels=[r'$u$',r'$-u$',r'$u^{-1}$',r'$-u^{-1}$']
th=np.linspace(0,2*np.pi,500);ax.plot(np.cos(th),np.sin(th),color=gray,ls=':',lw=.8)
for zz,lab in zip(pts,labels):ax.scatter(zz.real,zz.imag,s=38,color=teal);ax.annotate(lab,(zz.real,zz.imag),xytext=(-24,-14) if lab==r'$-u$' else (8,8),textcoords='offset points')
for i,j,col,rad in [(0,1,orange,.12),(0,2,purple,-.22),(1,3,purple,-.22),(2,3,orange,.1)]:
    ax.add_patch(FancyArrowPatch((pts[i].real,pts[i].imag),(pts[j].real,pts[j].imag),connectionstyle=f'arc3,rad={rad}',arrowstyle='<->',mutation_scale=9,lw=.8,color=col,shrinkA=6,shrinkB=6))
ax.text(-2.1,1.35,r'$R:u\mapsto-u$',color=orange);ax.text(.2,1.35,r'$T:u\mapsto u^{-1}$',color=purple)
ax.axhline(0,lw=.5,color=gray);ax.axvline(0,lw=.5,color=gray);ax.set_aspect('equal');ax.set_xlim(-2.2,2.2);ax.set_ylim(-1.35,1.65);ax.set_xlabel(r'$\operatorname{Re}u$');ax.set_ylabel(r'$\operatorname{Im}u$');save(fig,'02_v4_orbit')

fig,ax=diagram((7,3.2));box(ax,(1.5,3.5),r'$\mathbb{P}^{1}_{u}$'+'\nsource sphere');box(ax,(5,3.5),r'$r=u+u^{-1}$'+'\nJoukowski map');box(ax,(8.5,3.5),r'$\beta=r^2/4$'+'\nquotient sphere')
arr(ax,(2.8,3.5),(3.7,3.5),'degree 2',offset=(0,.5));arr(ax,(6.3,3.5),(7.2,3.5),'degree 2',offset=(0,.5))
for xx,tx in [(1.5,r'$u=\pm i$'+'\n'+r'$\beta=0$'),(5,r'$u=\pm1$'+'\n'+r'$\beta=1$'),(8.5,r'$u=0,\infty$'+'\n'+r'$\beta=\infty$')]:box(ax,(xx,1.25),tx,w=2.3,h=1,color=gray)
ax.text(5,2.35,r'Each exceptional orbit: two points, each of local degree 2',ha='center',fontsize=9);save(fig,'03_belyi_quotient')

fig,ax=plt.subplots(figsize=(7,4.5),layout='constrained');av=np.linspace(-3,11,600);bv=np.linspace(-13,13,600);AA,BB=np.meshgrid(av,bv);dd=(AA+1)**2-BB*BB
ax.contourf(AA,BB,np.sign(dd),levels=[-2,0,2],colors=['#f5e8df','#e7f0f2'],alpha=.75)
ax.plot(av,av+1,color=teal,label=r'$B=\pm(A+1)$');ax.plot(av,-av-1,color=teal)
ap=np.linspace(0,11,400);ax.plot(ap,2*np.sqrt(ap),color=orange,label=r'$B^2=4A$');ax.plot(ap,-2*np.sqrt(ap),color=orange)
ax.axvline(1,color=purple,ls='--',lw=1,label=r'$A=1$');ax.axvline(-1,color=gray,ls=':',lw=.8);ax.axhline(0,color=gray,ls=':',lw=.8)
for aa,bb,lab,off in [(9,9,'(9,9)',(6,6)),(9,1,'(9,1)',(6,6)),(np.pi,np.e,r'$(\pi,e)$',(8,-18)),(phi,1-phi,r'$(\phi,1-\phi)$',(10,-18))]:ax.scatter(aa,bb,s=22,color='black',zorder=5);ax.annotate(lab,(aa,bb),xytext=off,textcoords='offset points',fontsize=8)
ax.text(6,3,r'$\Delta>0$',color=teal);ax.text(0,9,r'$\Delta<0$',color=orange);ax.set_xlabel('$A$');ax.set_ylabel('$B$');ax.set_xlim(-3,11);ax.set_ylim(-13,13);ax.legend(loc='lower right',fontsize=8,frameon=True);save(fig,'04_parameter_strata')

fig,axs=plt.subplots(1,2,figsize=(7,3.4),layout='constrained');ls=np.logspace(1,5,400)
axs[0].loglog(ls,ls**-.5,label=r'intermediate $|y-1|\sim L^{-1/2}$',color=teal);axs[0].loglog(ls,ls**-1,label=r'lock $|y-1|\sim L^{-1}$',color=orange);axs[0].fill_between(ls,ls**-1,ls**-.5,color=orange,alpha=.07);axs[0].set_xlabel('$L$');axs[0].set_ylabel(r'distance $|y-1|$');axs[0].legend(fontsize=7,frameon=False,loc='upper right');axs[0].grid(alpha=.2,which='major')
for ll,col in [(100,orange),(10000,teal)]:
    for lo,hi in [(-4,-.3),(.3,4)]:
        ss=np.linspace(lo,hi,600);yy=1+ss/np.sqrt(ll);pp=((ll*yy*yy-ll*yy+1)/(yy*yy-ll*yy+ll)+1)*np.sqrt(ll)
        axs[1].plot(ss,pp,color=col,lw=1,label=f'$L={ll}$' if lo<0 else None)
for lo,hi in [(-4,-.3),(.3,4)]:
    ss=np.linspace(lo,hi,600);axs[1].plot(ss,-ss-2/ss,color='black',ls='--',lw=1,label='$W(s)$' if lo<0 else None)
axs[1].scatter([-np.sqrt(2),np.sqrt(2)],[2*np.sqrt(2),-2*np.sqrt(2)],color=purple,s=25,zorder=5);axs[1].set_xlim(-4,4);axs[1].set_ylim(-8,8);axs[1].set_xlabel('$s$');axs[1].set_ylabel(r'$\sqrt{L}(f_L+1)$');axs[1].legend(fontsize=7,frameon=False);axs[1].grid(alpha=.15);save(fig,'05_scaling_hierarchy')

fig,ax=diagram((7,4));box(ax,(1.6,4),r'$E_t$'+'\ngenus 1',w=2.6);box(ax,(1.6,1),r'$\mathbb{P}^{1}_{x}$'+'\ngenus 0',w=2.6);box(ax,(5,1),r'$\mathbb{P}^{1}_{y}$'+'\ngenus 0',w=2.6);box(ax,(8.5,1),r'$\mathbb{P}^{1}_{\beta}$'+'\ngenus 0',w=2.6)
arr(ax,(1.6,3.45),(1.6,1.55),'degree 2',offset=(-.75,0));arr(ax,(3,1),(3.6,1),'2',offset=(0,.35));arr(ax,(6.4,1),(7.1,1),'4',offset=(0,.35));arr(ax,(3,3.95),(8.5,1.55),'Galois degree 16',offset=(.4,.38));ax.text(5.4,4.3,r'$\operatorname{Gal}(E_t/\beta)=D_4\times C_2$',ha='center',color=teal);ax.text(3.3,1.95,r'$y=x^2$',ha='center',color=gray);save(fig,'06_cover_tower')

fig,ax=diagram((7,3.4));ax.add_patch(Circle((3.1,2.6),1.7,edgecolor=teal,facecolor='#f2f8f8',lw=1.2))
for p,lab,col in [((2,2),'0',gray),((4.2,2.1),'1',gray),((3.1,4.1),r'$\infty$',gray),((2.6,3.1),r'$\lambda$',orange),((4,3.25),r'$\nu$',purple)]:ax.scatter(*p,s=30,color=col);ax.text(p[0]+.15,p[1]+.15,lab,color=col,fontsize=12)
ax.text(7.6,3.9,'Five labeled target points',ha='center',fontsize=11);ax.text(7.6,2.6,r'$(0,1,\infty,\lambda,\nu)$'+'\n\n'+r'$\lambda,\nu\notin\{0,1,\infty\}$'+'\n'+r'$\lambda\ne\nu$',ha='center',va='center',fontsize=11)
ax.text(7.6,.85,'Cover type must also be specified.\nPositions are schematic, not a real ordering.',ha='center',fontsize=8,color=gray);ax.set_aspect('equal');save(fig,'07_five_marked_target')

fig,ax=diagram((7,3.8));ax.set_xlim(-.2,10.2)
for yy in [1.25,3.5]:
    ax.plot([.8,9.2],[yy,yy],color=gray,lw=.65)
    for lo,hi in [(2,4),(6,8)]:ax.plot([lo,hi],[yy,yy],color=teal,lw=3)
    for xx,lab in [(2,r'$-a^{-1}$'),(4,r'$-a$'),(6,r'$a$'),(8,r'$a^{-1}$')]:ax.scatter(xx,yy,s=24,color=orange,zorder=4);ax.text(xx,yy+.3,lab,ha='center')
for lo,hi in [(2,4),(6,8)]:
    arr(ax,(lo+.5,3.32),(lo+.5,1.43),'',color=purple);arr(ax,(hi-.5,1.43),(hi-.5,3.32),'',color=purple)
    ax.text((lo+hi)/2,2.37,'opposite\nbanks',ha='center',va='center',fontsize=8,color=purple)
ax.text(.6,4.35,r'Two sheets of $z^2=(x^2-t)/(tx^2-1)$',fontsize=11);ax.text(5,.3,r'Glue pointwise along the cuts: $2g-2=-4+4=0$',ha='center');save(fig,'08_elliptic_double_cover')

fig,axs=plt.subplots(1,2,figsize=(7,3.7),layout='constrained');vv=np.linspace(-4.5,4.5,1000);UU,VV=np.meshgrid(vv,vv);axs[0].contour(UU,VV,UU*UU+VV*VV-1-.25*UU*UU*VV*VV,levels=[0],colors=[teal],linewidths=1.3);axs[0].set_aspect('equal');axs[0].set_xlabel('$U$');axs[0].set_ylabel('$V$');axs[0].set_title(r'Edwards, $t=1/2$');axs[0].scatter([0,1],[1,0],color=orange,s=25);axs[0].annotate('$O$',(0,1),xytext=(8,8),textcoords='offset points');axs[0].annotate('$P$',(1,0),xytext=(8,8),textcoords='offset points')
mm=1/9
for lo,hi in [(0,mm),(1,1.65)]:
    ell=np.linspace(lo,hi,800);eta=np.sqrt(np.maximum(0,ell*(ell-1)*(ell-mm)));axs[1].plot(ell,eta,color=teal);axs[1].plot(ell,-eta,color=teal)
axs[1].scatter([0,mm,1],[0,0,0],s=20,color=orange);axs[1].set_xlabel(r'$\ell$');axs[1].set_ylabel(r'$\eta$');axs[1].set_title(r'Legendre, $m=1/9$');axs[1].set_xlim(-.1,1.7);axs[1].axhline(0,color=gray,lw=.5)
for ax in axs:ax.grid(alpha=.15)
save(fig,'09_edwards_legendre')

fig,ax=diagram((7,3.6));box(ax,(2.2,3.6),'Original source\n'+r'$\mathbb{P}^{1}_x$, genus 0',w=3.4,h=1,color=teal);box(ax,(7.8,3.6),'Galois closure\n'+r'$E_t$, genus 1',w=3.4,h=1,color=purple)
arr(ax,(6,3.6),(4,3.6),'degree 2',offset=(0,.45));box(ax,(2.2,1.3),'Real graph\nchosen affine coordinates',w=3.4,h=1,color=gray);box(ax,(7.8,1.3),'Complex analytic surface\n'+r'$\mathbb{C}/\Lambda$',w=3.4,h=1,color=gray)
arr(ax,(2.2,3),(2.2,1.9),'restrict / plot',offset=(.85,0));arr(ax,(7.8,3),(7.8,1.9),'uniformize',offset=(.8,0));ax.text(5,.3,'A surface of revolution would require a separate profile, axis, and gluing rule.',ha='center',fontsize=8);save(fig,'10_sphere_torus_distinction')
print('Generated 10 figures in PDF, SVG, and PNG.')
