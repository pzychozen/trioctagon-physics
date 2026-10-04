"""Four Paper G illustrations; outputs only to --output (external build scratch).
Nominal map/basis copied in substance from accepted m3_nominal_crosscheck_v0_2.py.
Fresh 321-step, 130-digit nominal replay; not a new certificate or parameter scan.
M2 points reuse the accepted original finite-run table without rerunning it.
"""
from pathlib import Path
from fractions import Fraction
import argparse, csv, hashlib, json
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
mp.mp.dps=130
eps=mp.mpf(1)/20;g=mp.mpf(1)/5
k=list(map(mp.mpf,['1','1.2208964704604097','6.35310346037241']))
def L(v):return [sum(v)-3*x for x in v]
u=list(map(mp.mpf,['1.55','1.57','2.09']))
for _ in range(14):
 J=mp.matrix([[(eps*(k[i]-3*u[i]**2) if i==j else 0)+g*(1-3*(i==j)) for j in range(3)] for i in range(3)])
 d=mp.lu_solve(J,mp.matrix([eps*u[i]*(k[i]-u[i]**2)+g*L(u)[i] for i in range(3)]));u=[u[i]-d[i] for i in range(3)]
a=mp.sqrt(u[0]**2+u[1]**2);un=mp.sqrt(sum(v*v for v in u))
v1=[u[1]/a,-u[0]/a,0];v2=[u[0]*u[2]/(a*un),u[1]*u[2]/(a*un),-a/un]
M=[[(1+eps*(k[i]-u[i]**2) if i==j else 0)+g*(1-3*(i==j)) for j in range(3)] for i in range(3)]
K=[[sum(v[i]*M[i][j]*w[j] for i in range(3) for j in range(3)) for w in (v1,v2)] for v in (v1,v2)]
m1=(K[0][0]+K[1][1]+mp.sqrt((K[0][0]-K[1][1])**2+4*K[0][1]**2))/2
lam=(1+1/m1)/9+mp.mpf(1)/200
def F(O):
 P=[O[i]+eps*O[i]*(k[i]-abs(O[i])**2)+g*L(O)[i] for i in range(3)]
 ph=[mp.arg(z) if z else mp.mpf(0) for z in P]
 return [abs(P[i])*mp.expj(ph[i]+lam*sum(mp.sin(3*(ph[j]-ph[i])) for j in range(3) if j!=i)) for i in range(3)]
def quotient(O):
 t=mp.arg(sum(u[i]*O[i] for i in range(3)));s=[z*mp.expj(-t) for z in O]
 return [s[i].real-u[i] for i in range(3)]+[sum(s[i].imag*v[i] for i in range(3)) for v in (v1,v2)]
def cross(x,y):return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
def obs(O):
 C=cross([z.real for z in O],[z.imag for z in O])
 return C,[-C[0]/2+C[1]-C[2]/2,mp.sqrt(3)*(C[2]-C[0])/2],sum(C)
def mpfrac(x):
 s,m,e,_=x._mpf_;return Fraction((-1)**s*m)*Fraction(2)**e

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);o=ap.parse_args().output.resolve()
 protected=next((p for p in ROOT.parents if (p/'.git').exists()),ROOT)
 if o==protected or protected in o.parents:raise ValueError('Use external figure scratch')
 o.mkdir(parents=True,exist_ok=False)
 receipt=json.loads((ROOT/'reproducibility/inputs/m3_accepted_support.json').read_text())['values']['exact_receipts']
 center=[mp.mpf(Fraction(x).numerator)/Fraction(x).denominator for x in receipt['centers']]
 radii=[mp.mpf(Fraction(x).numerator)/Fraction(x).denominator for x in receipt['positive_weights']]
 O=[mp.mpc(1),mp.mpc(-mp.mpf(1)/2,-mp.sqrt(3)/2),mp.mpc(-mp.mpf(1)/2,mp.sqrt(3)/2)]
 assert abs(sum(abs(x)**2 for x in O)-3)<mp.mpf('1e-125')
 rows=[];states=[];checks={}
 for n in range(322):
  C,W,G=obs(O);z=quotient(O);zh=z if n%2 else z[:3]+[-x for x in z[3:]]
  dist=max(abs(zh[i]-center[i])/radii[i] for i in range(5))
  rows.append([str(n),*map(lambda x:mp.nstr(x,65),[*C,*W,G,*z,dist])]);states.append(O[:])
  if n in (300,301):checks[f'q{n}_inside_accepted_box']=all(Fraction(lo)<=mpfrac(x)<=Fraction(hi) for x,(lo,hi) in zip(z,receipt['qbox' if n==300 else 'q301']))
  if n<321:O=F(O)
 assert all(checks.values())
 with (o/'nominal_trajectory.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(['n','C_A','C_B','C_C','W_x','W_y','Gamma','z1','z2','z3','z4','z5','parity_aligned_weighted_distance']);w.writerows(rows)
 d=np.asarray(rows,dtype=float)
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'svg.hashsalt':'paper-g-v0.1','axes.labelcolor':'#253246','text.color':'#253246'})
 colors=['#176b91','#bd5b2a','#7060a6']
 def save(fig,name):
  fig.savefig(o/(name+'.pdf'),bbox_inches='tight',metadata={'CreationDate':None,'ModDate':None,'Title':'Paper G local review '+name})
  fig.savefig(o/(name+'.png'),dpi=160,bbox_inches='tight');plt.close(fig)
 # Paper B centers and exact frame directions; no artificial surface field.
 T=np.array([[-.5,1,-.5],[-np.sqrt(3)/2,0,np.sqrt(3)/2]])
 N=np.array([[-np.sqrt(3)/2,0,np.sqrt(3)/2],[.5,-1,.5]])
 centres=np.array([[-.25,0,.25],[np.sqrt(3)/4,0,np.sqrt(3)/4]])
 fig,axs=plt.subplots(1,3,figsize=(10.3,3.25),gridspec_kw={'width_ratios':[1.1,1,1]})
 for i,label in enumerate('ABC'):
  cc=centres[:,i];tt=T[:,i];nn=N[:,i]
  axs[0].plot([cc[0]-.5*tt[0],cc[0]+.5*tt[0]],[cc[1]-.5*tt[1],cc[1]+.5*tt[1]],c=colors[i],lw=2)
  for vec,style in [(tt,'-'),(nn,'--')]:axs[0].annotate('',xy=cc+.18*vec,xytext=cc,arrowprops={'arrowstyle':'->','color':colors[i],'linestyle':style})
  axs[0].text(*(cc+.23*nn),label,ha='center',va='center',color=colors[i])
 axs[0].set(xlim=(-.7,.7),ylim=(-.37,.97),aspect='equal',xlabel='Paper B horizontal x',ylabel='Paper B horizontal y',title='(a) Actual central section')
 axs[0].text(-.67,.87,'solid: tangent tᵢ\ndashed: outward normal nᵢ',fontsize=8)
 C=np.array([float(x) for x in obs(states[1])[0]]);cp=np.repeat(C.mean(),3);ct=C-cp
 xx=np.arange(3);axs[1].bar(xx-.22,C,.22,label='C',color='#253246');axs[1].bar(xx,cp,.22,label='C parallel',color='#aeb6c2');axs[1].bar(xx+.22,ct,.22,label='C perpendicular',color='#176b91')
 axs[1].set(xticks=xx,xticklabels=list('ABC'),ylabel='Channel signed area',title='(b) Entrance after one update');axs[1].legend(fontsize=7,loc='lower right');axs[1].axhline(0,c='.7',lw=.6)
 for i in range(3):
  v=T[:,i]*C[i];axs[2].annotate('',xy=v,xytext=(0,0),arrowprops={'arrowstyle':'->','color':colors[i]});axs[2].text(*(v*1.1),f'C{list("ABC")[i]} t{list("ABC")[i]}',fontsize=7,color=colors[i])
 W=T@C;axs[2].annotate('',xy=W,xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#17222e','lw':2});axs[2].text(*(W*1.2),'W',fontweight='bold')
 axs[2].set(xlim=(-.30,.22),ylim=(-.23,.30),aspect='equal',xlabel='Ambient axial x',ylabel='Ambient axial y',title='(c) Tangent-weighted sum')
 axs[2].axhline(0,c='.8',lw=.5);axs[2].axvline(0,c='.8',lw=.5)
 fig.tight_layout(w_pad=2);save(fig,'01_geometry_observable')
 fig,axs=plt.subplots(3,2,figsize=(9.4,6.0),sharex='col',gridspec_kw={'width_ratios':[2.2,1]})
 for row,(col,name) in enumerate([(4,'Wₓ'),(5,'Wᵧ'),(6,'Γ')]):
  for parity,mark,colr in [(0,'o',colors[0]),(1,'s',colors[1])]:
   ix=(d[:,0]%2==parity)
   for j in range(2):axs[row,j].plot(d[ix,0],d[ix,col],marker=mark,ms=2.0,lw=.65,color=colr,label=['even n','odd n'][parity])
  axs[row,0].set_ylabel(name+' (signed)');axs[row,1].set_xlim(299.5,311.5)
  late=d[(d[:,0]>=300)&(d[:,0]<=312),col];lim=1.23*max(abs(late));axs[row,1].set_ylim(-lim,lim)
  for ax in axs[row]:ax.axhline(0,c='.7',lw=.5);ax.grid(alpha=.13)
 axs[0,0].legend(ncol=2,fontsize=8);axs[0,0].set_title('(a) Correctly normalized entrance, 321 updates');axs[0,1].set_title('(b) Late signed branches')
 axs[-1,0].set_xlabel('Update index n');axs[-1,1].set_xlabel('Update index n');fig.tight_layout();save(fig,'02_signed_trajectory')
 tab=json.loads((ROOT/'reproducibility/inputs/m2_nominal_onset.json').read_text())['values']['amplitude_law_table']
 keys=['0.0001','0.0004','0.0016'];mu=np.array(list(map(float,keys)));wm=np.array([float(tab[x]['|W| measured']) for x in keys]);wp=np.array([float(tab[x]['|W| predicted |W_q| a_pred']) for x in keys])
 fig,ax=plt.subplots(1,2,figsize=(9.4,3.3));grid=np.geomspace(mu.min(),mu.max(),100)
 ax[0].plot(np.sqrt(grid),25.000075367*np.sqrt(grid),'--',c=colors[0],label='Local leading term');ax[0].scatter(np.sqrt(mu),wm,c=colors[1],label='Stored numerical observations',zorder=3)
 ax[0].set(xlabel='√μ',ylabel='|W|',title='(a) M2 numerical onset versus asymptotic');ax[0].legend(fontsize=8)
 ax[1].semilogx(mu,wm/wp,'o',c=colors[1]);ax[1].axhline(1,c=colors[0],ls='--');ax[1].set(xlabel='μ = λ − λc',ylabel='Observed |W| / leading term',title='(b) Finite observations only',ylim=(.94,1.004));fig.tight_layout();save(fig,'03_local_onset')
 qrows=np.array([float(Fraction(x)) for x in receipt['weighted_row_bounds']]);bound=[];entry=[]
 for i in range(5):
  cc=Fraction(receipt['centers'][i]);rr=Fraction(receipt['positive_weights'][i])
  bound.append(float(max(abs(Fraction(x)-cc) for x in receipt['Zw'][i])/rr))
  entry.append(float(max(abs(Fraction(x)-cc) for x in receipt['q301'][i])/rr))
 fig,ax=plt.subplots(1,2,figsize=(9.4,3.6));ax[0].semilogy(d[21:,0],d[21:,-1],c=colors[0],lw=1.2);ax[0].axhline(1,c=colors[1],ls='--',label='Box boundary');ax[0].axvline(301,c='#555',ls=':',label='Certified sufficient N=301');ax[0].set(xlabel='Update index n',ylabel='Parity-aligned max |zᵢ − cᵢ| / rᵢ',title='(a) Nominal approach to the trap');ax[0].legend(fontsize=7)
 xx=np.arange(5);ax[1].bar(xx-.23,entry,.22,label='X301 offsets',color='#4c96ad');ax[1].bar(xx,bound,.22,label='F̂² box offsets',color='#bd5b2a');ax[1].bar(xx+.23,qrows,.22,label='Derivative row bounds',color='#9293a6');ax[1].axhline(1,c='#555',ls='--');ax[1].set(xticks=xx,xticklabels=['1','2','3','4','5'],xlabel='Quotient coordinate',ylabel='Scaled bound (decimal display)',ylim=(0,1.4),title='(b) Five-coordinate certificate summary');ax[1].legend(fontsize=7,loc='upper center');fig.tight_layout();save(fig,'04_capture')
 (o/'figure_record.json').write_text(json.dumps({'evidence_class':'NOMINAL_ILLUSTRATION plus rounded displays of existing interval bounds','precision_digits':130,'updates':321,'normalization':'Omega0=(1,-1/2-i*sqrt(3)/2,-1/2+i*sqrt(3)/2); norm squared 3','checks':checks,'M2_onset_subset':keys,'M2_table_replayed':False,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(o.iterdir()) if p.is_file()}},indent=2)+'\n')
 print('Four figures generated; accepted q300/q301 membership passed.')
if __name__=='__main__':main()
