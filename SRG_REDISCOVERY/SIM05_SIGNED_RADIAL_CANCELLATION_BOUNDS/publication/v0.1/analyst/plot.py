"""Six fixed presentation figures from completed new CSV tables only."""
from common import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
start=time.monotonic();preserved()
sources=['phase_dispersion_intervals.csv','phase_interval_means.csv']
before={n:ident(ROOT/'analysis'/n) for n in sources}
def csvread(n):
 with lp(ROOT/'analysis'/n).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
views=csvread(sources[0]);means=csvread(sources[1]);x=np.arange(200)
plt.rcParams.update({'font.size':10,'axes.titlesize':12,'axes.labelsize':10,'figure.dpi':120,'savefig.dpi':160})
colors={'P':'#7b5c9b','unsigned':'#d88919','signed':'#007c83','observed':'#111111','J1':'#c16a36','J4':'#007c83','lower':'#487fb0'}
files=[]
def finish(fig,name,title):
 fig.suptitle(title,fontsize=14)
 for ax in fig.axes:
  ax.set_xlim(0,199);ax.set_xlabel('Recorded phase j (all 200 phases)');ax.grid(alpha=.2)
 fig.tight_layout(rect=(0,0,1,.95));path=ROOT/'plots'/name
 need(not lp(path).exists(),'figure collision');fig.savefig(lp(path));plt.close(fig);files.append(name)
def val(rows,key):return np.array([float(r[key]) for r in rows])
def byview(view):return [r for r in views if r['view']==view]
fig,axs=plt.subplots(1,2,figsize=(13,4.7))
for ax,view in zip(axs,('all_five','new_four')):
 rs=byview(view)
 for col,label,color in [('P_PROFILE_SD_upper','Inherited P upper',colors['P']),('RADIAL_4_UNSIGNED_SD_upper','J=4 unsigned upper',colors['unsigned']),('RADIAL_4_SIGNED_SD_upper','J=4 signed upper',colors['signed']),('post_SD','Observed post SD',colors['observed'])]:
  ax.plot(x,val(rs,col),label=label,color=color,lw=1.5)
 ax.set_yscale('log');ax.set_ylabel('SD (native speed units; log scale)');ax.set_title(view.replace('_',' '));ax.legend(fontsize=8)
finish(fig,'01_profile_unsigned_signed.png','SIM05: same saved population, stronger scalar bounds')
fig,axs=plt.subplots(1,2,figsize=(13,4.7))
for ax,view in zip(axs,('all_five','new_four')):
 rs=byview(view)
 for J,color in [(1,colors['J1']),(4,colors['J4'])]:
  low=val(rs,f'J{J}_SD_lower');upper=val(rs,f'RADIAL_{J}_SIGNED_SD_upper')
  ax.fill_between(x,low,upper,color=color,alpha=.12)
  ax.plot(x,upper,color=color,lw=1.3,label=f'J={J} upper');ax.plot(x,low,color=color,lw=1,ls='--',label=f'J={J} lower')
 ax.plot(x,val(rs,'post_SD'),color='black',lw=1,label='Observed post SD');ax.set_yscale('log');ax.set_ylabel('SD interval (native speed; log scale)');ax.set_title(view.replace('_',' '));ax.legend(fontsize=8,ncol=2)
finish(fig,'02_fixed_resolution_enclosures.png','SIM05: one versus four fixed subintervals')
fig,axs=plt.subplots(2,1,figsize=(12,6.6),sharex=True)
for J,col in [(1,colors['J1']),(4,colors['J4'])]:
 axs[0].plot(x,val(means,f'J{J}_cancellation_mean'),color=col,label=f'J={J}',lw=1.5)
 axs[1].plot(x,val(means,f'J{J}_mean_radius_mean'),color=col,label=f'J={J}',lw=1.5)
axs[0].set_title('Unsigned minus signed upper bound: retained midpoint cancellation');axs[1].set_title('Mean interval radius: uncertainty remains in the signed bound')
for ax in axs:ax.set_ylabel('Ten-pair mean (native speed)');ax.legend()
finish(fig,'03_cancellation_and_uncertainty.png','SIM05: cancellation and uncertainty are separate quantities')
fig,ax=plt.subplots(figsize=(12,4.8))
for key,label,col in [('gap_P_to_unsigned4','P − unsigned J=4: center enclosure',colors['P']),('gap_unsigned4_to_signed4','Unsigned − signed J=4: averaging',colors['unsigned']),('gap_signed4_to_S','Signed J=4 − observed: remaining slack',colors['signed'])]:
 ax.plot(x,val(means,key+'_mean'),label=label,color=col,lw=1.6)
ax.set_ylabel('Ten-pair mean gap (native speed)');ax.legend(fontsize=9)
finish(fig,'04_fixed_gap_ladder.png','SIM05: three information losses in the fixed gap identity')
fig,axs=plt.subplots(2,2,figsize=(14,8.5))
for row,view in enumerate(('all_five','new_four')):
 rs=byview(view)
 for col,ref in enumerate(('incoming','pre_damping')):
  ax=axs[row,col]
  for J,style,width in [(1,':',1),(4,'-',1.5)]:
   ax.plot(x,val(rs,f'J{J}_{ref}_decrease_margin'),color=colors['signed'],ls=style,lw=width,label=f'J={J} decrease margin')
   ax.plot(x,val(rs,f'J{J}_{ref}_increase_margin'),color=colors['J1'],ls=style,lw=width,label=f'J={J} increase margin')
  ax.plot(x,val(rs,ref+'_actual_margin'),color='black',lw=.9,label='Actual reference − post')
  ax.axhline(0,color='#777777',lw=.6);ax.set_yscale('symlog',linthresh=1e-8)
  ax.set_title(view.replace('_',' ')+' / '+ref.replace('_',' '));ax.set_ylabel('Variance margin (native speed²; symlog)');ax.legend(fontsize=7,ncol=2)
finish(fig,'05_two_sided_conditions.png','SIM05: positive sufficient margins can establish either direction (threshold 1e−14)')
fig,axs=plt.subplots(1,2,figsize=(13,4.7))
for ax,view in zip(axs,('all_five','new_four')):
 rs=byview(view)
 for f,label,col in [('P_PROFILE','Inherited P',colors['P']),('RADIAL_1_SIGNED','Signed J=1',colors['J1']),('RADIAL_4_SIGNED','Signed J=4',colors['J4'])]:
  ax.plot(x,val(rs,f+'_SD_factor'),color=col,label=label,lw=1.5)
 for level in (1,2,5,10):ax.axhline(level,color='#999999',ls=':',lw=.65)
 ax.set_yscale('log');ax.set_ylabel('SD upper / observed SD (log scale)');ax.set_title(view.replace('_',' '));ax.legend(fontsize=8)
finish(fig,'06_full_phase_tightness.png','SIM05: all-phase relative tightness; horizontal guides are descriptive')
for n,v in before.items():need(ident(ROOT/'analysis'/n)==v,'plot source changed')
save(ROOT/'evidence/FIGURE_RESULT.json',{'status':'PASS','utc':utc(),'seconds':time.monotonic()-start,'count':len(files),
 'sources':before,'files':{n:ident(ROOT/'plots'/n) for n in files},'matplotlib':matplotlib.__version__,
 'phase_range':[0,199],'presentation_corrections':0,'new_bound_evaluations':0,'log_scale_figures':[1,2,6],
 'symlog_figure':{'figure':5,'linear_threshold':1e-8,'reason':'Show both signs across native variance magnitudes; numerical classifications remain at 1e-14.'},
 'no_fits_or_independent_trial_errorbars':True,'preservation':preserved(),'bytes':cap()})
print(json.dumps({'status':'PASS','figures':files,'seconds':time.monotonic()-start,'bytes':size()}))
