"""Eight figures from completed SIM03 tables only. No accepted state reads."""
from common import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import time

def table(name):
    with (ROOT/'analysis'/name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def col(rows,key):return np.array([float(r[key]) if r[key]!='' else np.nan for r in rows])
def style(ax,title,xlabel,ylabel):
    ax.set_title(title,fontsize=11);ax.set_xlabel(xlabel);ax.set_ylabel(ylabel);ax.grid(alpha=.2)
def savefig(fig,name,title):
    fig.suptitle(title,fontsize=15)
    fig.savefig(ROOT/'plots'/name,dpi=160,bbox_inches='tight',facecolor='white');plt.close(fig)
def phase_lines(ax,rows,key):
    for c in range(5):
        part=[r for r in rows if int(r['cycle'])==c]
        ax.plot(col(part,'phase'),col(part,key),label='c0 inherited' if c==0 else 'c'+str(c),
            color='0.4' if c==0 else COLORS[c-1],ls='--' if c==0 else '-',lw=1.25)
COLORS=['#0072B2','#E69F00','#009E73','#CC79A7']

def main():
    start=time.monotonic()
    need(load(ROOT/'evidence/QA.json')['status']=='PASS','completed QA required')
    need(not list((ROOT/'plots').glob('*.png')),'plot collision')
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'legend.fontsize':8})
    updates=table('update_budgets.csv');phase=table('repeated_phase_curves.csv')
    pairs=table('same_phase_comparisons.csv');spread=table('phase_spread.csv');cross=table('cross_arm_comparisons.csv')
    with np.load(ROOT/'analysis/center_decomposition.npz',allow_pickle=False) as z:
        centers={k:z[k] for k in ['dataset_id','update_index','center','q','cosine','cosine_valid','impulse_norm','retention','chi','m']}
    figures=[]
    fig,axes=plt.subplots(3,2,figsize=(14,11),layout='constrained')
    prefix=[r for r in updates if r['dataset']=='PREFIX']
    for j,arm in enumerate(['CONTINUOUS','REPEATED']):
        rows=prefix+[r for r in updates if r['dataset']==arm];x=col(rows,'update_index')
        for key,label in [('incoming_mean_speed','incoming'),('pre_damping_mean_speed','pre-damping'),('post_mean_speed','saved post')]:
            axes[0,j].plot(x,col(rows,key),lw=1.2,label=label)
        for k,color in zip(['B','C','R'],['#0072B2','#009E73','#D55E00']):
            axes[1,j].plot(x,col(rows,'mean_'+k)*(-1 if k=='R' else 1),color=color,label='−R' if k=='R' else k,lw=1.)
        axes[1,j].plot(x,col(rows,'observed_delta_speed'),color='black',lw=.8,label='observed Δu')
        for k,color in zip(['I','A','L'],['#0072B2','#009E73','#D55E00']):
            axes[2,j].plot(x,col(rows,'mean_'+k)*(-1 if k=='L' else 1),color=color,label='−L' if k=='L' else k,lw=1.)
        axes[2,j].plot(x,col(rows,'observed_delta_squared_speed'),color='black',lw=.8,label='observed Δ mean |v|²')
        for i,ylabel in enumerate(['Mean speed (native units)','Speed budget per update','Squared-speed budget per update']):
            style(axes[i,j],arm+(' · speed' if i==0 else ' · center means'),'Actual update n',ylabel)
            axes[i,j].axvspan(0,199,color='0.75',alpha=.25)
            for b in [200,400,600,800]:axes[i,j].axvline(b,color='0.65',ls=':',lw=.7)
            axes[i,j].legend(ncol=2)
    savefig(fig,'01_actual_speed_budgets.png','Saved motion: incoming → pre-damping → post-damping\nShaded prefix is inherited once, displayed in both views');figures.append('01_actual_speed_budgets.png')

    fig,axes=plt.subplots(2,3,figsize=(14,8),layout='constrained')
    for ax,k in zip(axes.flat,['I','A','L','B','C','R']):
        phase_lines(ax,phase,'mean_'+k);style(ax,k+' · center mean','Driving phase j','Squared-speed units' if k in 'IAL' else 'Speed units')
        ax.axhline(0,color='0.5',lw=.5)
    axes[0,0].legend(ncol=2)
    savefig(fig,'02_phase_budget_terms.png','Repeated drive: six distinct budget terms at equal phase\nI + A − L and B + C − R; five correlated cycles');figures.append('02_phase_budget_terms.png')

    fig,axes=plt.subplots(2,2,figsize=(13,9),layout='constrained')
    for ds,label,color in [(0,'prefix','#777777'),(1,'CONTINUOUS','#0072B2'),(2,'REPEATED','#D55E00')]:
        q=np.sort(centers['q'][centers['dataset_id']==ds]);axes[0,0].plot(q,np.arange(1,len(q)+1)/len(q),label=label,color=color)
    for q in [.9,.99,.999]:axes[0,0].axvline(q,color='0.6',ls=':',lw=.8)
    style(axes[0,0],'Observed normalization q','q = |d| / (|d| + 0.01)','Empirical cumulative fraction');axes[0,0].legend()
    phase_lines(axes[0,1],phase,'q_min');style(axes[0,1],'Smallest q among centers at each phase','Driving phase j','Minimum q');axes[0,1].legend(ncol=2)
    new=[r for r in spread if r['view']=='new_four'];x=col(new,'phase')
    for k,label in [('h','h = 0.1 |H|'),('G_squared','G²'),('mean_q2','mean(q²)')]:
        axes[1,0].plot(x,col(new,k+'_mean'),label=label,lw=1.4)
    axes[1,0].set_yscale('log');style(axes[1,0],'Factors; average across new cycles','Driving phase j','Magnitude / dimensionless factors (log)')
    axes[1,0].legend()
    for ds,label,color in [(0,'prefix','#777777'),(1,'CONTINUOUS','#0072B2'),(2,'REPEATED','#D55E00')]:
        rows=[r for r in updates if r['dataset']==label or (ds==0 and r['dataset']=='PREFIX')]
        axes[1,1].scatter(col(rows,'incoming_mean_speed'),col(rows,'G'),s=6,alpha=.4,color=color,label=label)
    style(axes[1,1],'G = 1 / (1 + incoming mean speed)','Incoming mean speed','Saved incoming G')
    axes[1,1].legend()
    savefig(fig,'03_normalization_and_gain.png','Impulse magnitude = h G q; geometry is usually, but not always, near saturation\nGain is a defined function of incoming speed, not independent evidence');figures.append('03_normalization_and_gain.png')

    fig,axes=plt.subplots(2,2,figsize=(13,9),layout='constrained')
    for c in range(5):
        rows=[r for r in phase if int(r['cycle'])==c];x=col(rows,'phase');color='0.4' if c==0 else COLORS[c-1]
        axes[0,0].plot(x,col(rows,'mean_A'),color=color,lw=1.1,label='c'+str(c)+' signed')
        axes[0,0].plot(x,col(rows,'mean_abs_A'),color=color,lw=.8,ls=':')
        axes[0,1].plot(x,col(rows,'mean_C'),color=color,lw=1.1,label='c'+str(c)+' signed')
        axes[0,1].plot(x,col(rows,'mean_abs_C'),color=color,lw=.8,ls=':')
        axes[1,1].plot(x,col(rows,'C_cancellation'),color=color,lw=1.,label='c0 inherited' if c==0 else 'c'+str(c))
    style(axes[0,0],'A: solid signed mean; dotted mean |A|','Driving phase j','Squared-speed units')
    style(axes[0,1],'C: solid signed mean; dotted mean |C|','Driving phase j','Speed units')
    valid=centers['cosine_valid']
    for ds,label,color in [(0,'prefix','#777777'),(1,'CONTINUOUS','#0072B2'),(2,'REPEATED','#D55E00')]:
        s=valid&(centers['dataset_id']==ds)
        axes[1,0].scatter(centers['impulse_norm'][s],centers['cosine'][s],s=3,alpha=.3,label=label,color=color)
    axes[1,0].set_xscale('log');style(axes[1,0],'Angle shown with impulse magnitude','|impulse| (native units, log)','cos(v, impulse)');axes[1,0].legend()
    style(axes[1,1],'Within-update cancellation of C','Driving phase j','1 − |sum C| / sum |C|');axes[1,1].legend(ncol=2)
    savefig(fig,'04_alignment_and_cancellation.png','Alignment is signed and magnitude-dependent\nDotted activity must not be mistaken for the signed contribution');figures.append('04_alignment_and_cancellation.png')

    fig,axes=plt.subplots(1,2,figsize=(13,5.5),layout='constrained')
    a=axes[0].scatter(centers['m'],centers['retention'],c=centers['chi'],s=4,alpha=.5,cmap='viridis',vmin=1/3,vmax=1)
    axes[0].set_xscale('log');style(axes[0],'Retention with magnitude and concentration','Pre-damping norm m (native units, log)','t / m')
    fig.colorbar(a,ax=axes[0],label='Component concentration χ')
    a=axes[1].scatter(centers['chi'],centers['retention'],c=centers['m'],norm=LogNorm(),s=4,alpha=.5,cmap='plasma')
    style(axes[1],'Orientation and magnitude vary together','Component concentration χ','t / m');fig.colorbar(a,ax=axes[1],label='Pre-damping norm m (log color)')
    savefig(fig,'05_damping_retention_orientation.png','Componentwise damping in all 14,400 center records\nDescriptive association; magnitude and orientation were not independently controlled');figures.append('05_damping_retention_orientation.png')

    fig,axes=plt.subplots(3,1,figsize=(12,11),layout='constrained')
    choices=spec()['same_phase_unique_pairs']
    for stage,color in [('incoming','#0072B2'),('pre_damping','#E69F00'),('post_damping','#009E73')]:
        curves=np.array([col([r for r in pairs if int(r['cycle'])==c and int(r['reference_cycle'])==d],stage+'_distance_mean') for c,d in choices])
        axes[0].plot(np.arange(200),np.mean(curves,axis=0),color=color,label=stage.replace('_','-'))
        axes[0].fill_between(np.arange(200),curves.min(axis=0),curves.max(axis=0),color=color,alpha=.12)
    style(axes[0],'Mean over seven pair curves; bands show pair range','Driving phase j','Mean labeled-center velocity distance');axes[0].legend(ncol=3)
    for c,d in choices:
        rows=[r for r in pairs if int(r['cycle'])==c and int(r['reference_cycle'])==d]
        axes[1].plot(col(rows,'phase'),col(rows,'damping_distance_ratio_mean'),label=f'({c},{d})',lw=1.)
        axes[2].scatter(col(rows,'post_damping_distance_mean'),abs(col(rows,'post_mean_speed_difference')),s=6,alpha=.5,label=f'({c},{d})')
    style(axes[1],'Damping-stage ratio; all denominators resolved','Driving phase j','Post / pre mean vector distance')
    axes[1].axhline(1,color='black',ls=':');axes[1].legend(ncol=7)
    style(axes[2],'Scalar similarity can coexist with vector difference','Post-damping labeled velocity distance','|Difference of mean speeds|')
    savefig(fig,'06_phase_velocity_differences.png','Incoming, pre-damping and post-damping differences\n1,400 fixed pair/phase comparisons; reused cycles are not independent trials');figures.append('06_phase_velocity_differences.png')

    fig,axes=plt.subplots(2,2,figsize=(13,9),layout='constrained')
    for j,view in enumerate(['all_five','new_four']):
        rows=[r for r in spread if r['view']==view];x=col(rows,'phase')
        for key,label in [('pre_damping_mean_speed','pre-damping'),('post_mean_speed','saved post'),('mean_R','damping loss')]:
            axes[0,j].plot(x,col(rows,key+'_population_std'),label=label)
        style(axes[0,j],view.replace('_',' ')+' · scalar dispersion','Driving phase j','Population SD of mean speed / loss');axes[0,j].legend()
        for key,label,factor in [('pre_damping_variance','Var(pre)',1),('loss_variance','Var(loss)',1),
                    ('covariance_pre_damping_loss','−2 Cov(pre, loss)',-2),('post_damping_variance','Var(post)',1)]:
            axes[1,j].plot(x,col(rows,key)*factor,label=label,lw=1.2)
        style(axes[1,j],view.replace('_',' ')+' · variance balance','Driving phase j','Squared speed units');axes[1,j].legend()
    savefig(fig,'07_scalar_dispersion_balance.png','Damping lowers scalar phase dispersion here; the vector theorem alone does not require it\nPopulation moments of correlated cycles; covariance is descriptive');figures.append('07_scalar_dispersion_balance.png')

    fig,axes=plt.subplots(2,2,figsize=(13,9),layout='constrained');x=col(cross,'update_index')
    for key,label in [('mean_B_difference','ΔB'),('mean_C_difference','ΔC'),('mean_R_difference','ΔR')]:axes[0,0].plot(x,col(cross,key),label=label,lw=1.)
    for key,label in [('mean_I_difference','ΔI'),('mean_A_difference','ΔA'),('mean_L_difference','ΔL')]:axes[0,1].plot(x,col(cross,key),label=label,lw=1.)
    for key,label in [('incoming_distance_mean','incoming'),('pre_damping_distance_mean','pre-damping'),('post_damping_distance_mean','saved post')]:axes[1,0].plot(x,col(cross,key),label=label,lw=1.)
    axes[1,1].plot(x,col(cross,'post_mean_speed_difference'),color='#0072B2',label='Δ saved post mean speed')
    axes[1,1].plot(x,col(cross,'pre_damping_mean_speed_difference'),color='#E69F00',label='Δ pre-damping mean speed')
    for ax,title,ylabel in [(axes[0,0],'Actual speed-budget differences','Speed units'),(axes[0,1],'Squared-speed-budget differences','Squared-speed units'),
        (axes[1,0],'Equal-update labeled velocity distances','Native velocity units'),(axes[1,1],'Different schedules, different magnitudes','Speed units')]:
        style(ax,title,'Actual update n',ylabel);ax.legend()
        for b in [400,600,800]:ax.axvline(b,color='0.6',ls=':',lw=.7)
    savefig(fig,'08_cross_arm_context.png','REPEATED minus CONTINUOUS across the 800 new saved updates\nMatched draw / bit histories are inherited accepted facts, not replayed here');figures.append('08_cross_arm_context.png')
    need(len(figures)==8,'figure count')
    elapsed=time.monotonic()-start;need(elapsed<120,'plot time cap')
    save(ROOT/'evidence/PLOT_RECEIPT.json',{'status':'PASS','utc':utc(),'elapsed_seconds':elapsed,'matplotlib':matplotlib.__version__,
        'backend':matplotlib.get_backend(),'figures':{n:ident(ROOT/'plots'/n) for n in figures},
        'inputs':'Completed SIM03 CSV/NPZ only','source_trajectory_reads':0,'primary_reconstructions':0,
        'display_aggregations':'Sorting for ECDF and means/ranges across already saved pair curves only; no new source decomposition.'},True)
    output_cap();print(json.dumps({'status':'PASS','figures':8,'elapsed_seconds':elapsed}),flush=True)

if __name__=='__main__':main()
