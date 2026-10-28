"""Render retained data and a labelled schematic. No recurrence is evaluated."""
from pathlib import Path
from fractions import Fraction
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
DATA=ROOT/'evidence'
tw=json.loads((DATA/'turning_witness_20261028.json').read_text())
dg=json.loads((DATA/'delayed_graph_response_20261028.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'savefig.bbox':'tight'})
blue='#245b85';orange='#b75a29';green='#327965'
def midpoint(x): return sum(map(float,x['decimal_enclosure']))/2
def complex_record(z): return complex(float(Fraction(z['real']['exact'])),float(Fraction(z['imag']['exact'])))
means=[complex(*[midpoint(x) for x in row]) for row in tw['means']]
means[0]=1+0j
fig,ax=plt.subplots(figsize=(6.5,3.6))
for j,(a,b) in enumerate(zip(means,means[1:])):
 ax.annotate('',(b.real,b.imag),(a.real,a.imag),arrowprops={'arrowstyle':'->','lw':2,'color':blue})
 mid=(a+b)/2
 ax.annotate(r'$m_%d-m_%d$'%(j+1,j),(mid.real,mid.imag),xytext=((8,0) if j==0 else (-22,27)),textcoords='offset points',color=blue)
ax.scatter([z.real for z in means],[z.imag for z in means],s=35,color=blue,zorder=3)
for j,z in enumerate(means): ax.annotate(r'$m_%d$'%j,(z.real,z.imag),xytext=((-24,-16) if j==2 else ((10,-4) if j==1 else (6,5))),textcoords='offset points')
ax.set(xlabel=r'$\operatorname{Re}m$ (complex-state coordinate)',ylabel=r'$\operatorname{Im}m$',xlim=(.72,1.05),ylim=(-.035,.255))
ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.18)
fig.savefig(OUT/'mean_two_steps.pdf');plt.close(fig)
t0=complex_record(dg['t0']);ts=complex_record(dg['t_star'])
fig,ax=plt.subplots(figsize=(6.5,3.4))
for z,col,lab in [(t0,blue,r'$t(0)$'),(ts,orange,r'$t(1/60)$')]:
 ax.annotate('',(z.real,z.imag),(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':col})
 ax.annotate(lab,(z.real,z.imag),xytext=(-9,9 if col==blue else -19),textcoords='offset points',color=col)
ax.scatter([0],[0],color='black',s=16)
ax.set(xlabel='Real part of second mean increment',ylabel='Imaginary part',xlim=(-.062,.006),ylim=(-.019,.011))
ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.18)
fig.savefig(OUT/'matched_second_steps.pdf');plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(7,3.4))
ax=axes[0];ax.add_patch(Wedge((0,0),1.1,-7.5,7.5,width=.2,color=blue,alpha=.22))
for ang in [-7.5,7.5]:
 a=math.radians(ang);ax.plot([0,1.15*math.cos(a)],[0,1.15*math.sin(a)],color=blue,lw=1)
ax.annotate(r'$\Delta\leq\pi/12$',(.64,.075),xytext=(.27,.29),arrowprops={'arrowstyle':'-','color':blue})
ax.text(.85,-.28,r'$0.9\leq r\leq1.1$',ha='center')
ax.set_title('Invariant sector (schematic)')
ax.set(xlim=(-.05,1.25),ylim=(-.45,.45),xlabel='Real state coordinate',ylabel='Imaginary state coordinate')
ax=axes[1];ang=.12
ax.plot([0,1.18*math.cos(ang)],[0,1.18*math.sin(ang)],color=green,lw=1)
for j,r in enumerate([.93,1,1.07]):
 ax.scatter([r*math.cos(ang)],[r*math.sin(ang)],color=green,s=24)
 ax.annotate('ABC'[j],(r*math.cos(ang),r*math.sin(ang)),xytext=(0,12+13*(j%2)),textcoords='offset points',ha='center')
ax.text(.65,-.23,r'Common $\theta_\infty$; unequal $r_{*,i}$',ha='center')
ax.set_title('Aligned limit (schematic)')
ax.set(xlim=(-.05,1.25),ylim=(-.45,.45),xlabel='Real state coordinate')
for ax in axes: ax.set_aspect('equal');ax.grid(alpha=.12)
fig.tight_layout();fig.savefig(OUT/'sector_and_limit.pdf');plt.close(fig)
def interval(x):
 lo,hi=x['decimal_enclosure']
 return '$'+(lo if lo==hi else '['+lo+', '+hi+']')+'$'
tables=ROOT/'tables';tables.mkdir(exist_ok=True)
def table(name,header,rows):
 n=len(header)
 text='\\begin{tabular}{@{}'+'l'*n+'@{}}\n\\toprule\n'+' & '.join(header)+' \\\\\n\\midrule\n'
 text+='\n'.join(' & '.join(row)+' \\\\' for row in rows)+'\n\\bottomrule\n\\end{tabular}\n'
 (tables/name).write_text(text,encoding='utf-8')
table('increments.tex',['Step','$\\Re\\Delta m$','$\\Im\\Delta m$'],[[str(i)+' to '+str(i+1),interval(row[0]),interval(row[1])] for i,row in enumerate(tw['increments'])])
table('areas.tex',['$n$','$W_x$','$W_y$'],[[str(i),interval(row[0]),interval(row[1])] for i,row in enumerate(tw['W'])])
table('budgets.tex',['$n$','Contribution','Real part','Imaginary part'],[[str(i),term,interval(b[key][0]),interval(b[key][1])] for i,b in enumerate(tw['stage_budgets']) for term,key in [('$B_n$','onsite_mean_increment'),('$S_n$','synchronizer_mean_increment')]])
(OUT/'FIGURE_DATA.json').write_text(json.dumps({'sources':['../evidence/turning_witness_20261028.json','../evidence/delayed_graph_response_20261028.json'],'mean_plot':'Midpoints of retained enclosures, initial mean exactly 1; discrete points only.','comparison_plot':'Float rendering of exact retained rational second increments.','schematic':'Illustrative radii .93,1,1.07 are not computed r_star and are not a trajectory.','state_updates_performed':0},indent=2)+'\n',encoding='utf-8')
print('Three vector figures and three tables rendered from retained records/schematic; zero state updates.')
