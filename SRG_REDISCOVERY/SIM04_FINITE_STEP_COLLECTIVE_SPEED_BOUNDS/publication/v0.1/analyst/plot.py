"""Six figures from completed SIM04 output tables only; no analytic bound reevaluation."""
from common import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def rows(name):
    return list(csv.DictReader(io.StringIO(read(ROOT/'analysis'/name).decode())))
def arr(rs,key):return np.array([float(r[key]) if r[key]!='' else np.nan for r in rs],dtype=float)
def main():
    start=time.monotonic();need(load(ROOT/'evidence/PRIMARY_COMPLETE.json')['status']=='PASS','primary completion')
    inputs=['phase_dispersion_bounds.csv','phase_bound_means.csv','center_pair_bounds.npz','RESULTS.json']
    before={n:ident(ROOT/'analysis'/n) for n in inputs}
    spread=rows('phase_dispersion_bounds.csv');curves=rows('phase_bound_means.csv')
    byview={view:[r for r in spread if r['view']==view] for view in ('all_five','new_four')}
    results=load(ROOT/'analysis/RESULTS.json')
    plt.rcParams.update({'font.size':11,'axes.titlesize':12,'axes.labelsize':11,'figure.titlesize':16,
        'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white','axes.grid':True,'grid.alpha':.2})
    paths=[];labels={'all_five':'All five cycles (10 pairs)','new_four':'Four new cycles (6 reused pairs)'}
    colors={'Q_VECTOR':'#2166ac','K_COMPONENT':'#ef8a62','P_PROFILE':'#238b45','BEST_PRE':'#762a83'}
    def axes2(title):
        fig,axs=plt.subplots(2,1,figsize=(12,8),sharex=True,layout='constrained')
        fig.suptitle(title)
        for ax,view in zip(axs,byview):
            ax.set_title(labels[view],loc='left');ax.set_xlim(0,199);ax.set_xlabel('Common source phase j (0–199)')
        return fig,axs
    def finish(fig,name):
        dest=ROOT/'plots'/name;need(not dest.exists(),'figure exists')
        fig.savefig(dest,dpi=150);plt.close(fig);paths.append(name);cap()
    fig,axs=axes2('The baseline bound is valid but loose')
    for ax,(view,rs) in zip(axs,byview.items()):
        x=arr(rs,'phase');ax.plot(x,arr(rs,'Q_VECTOR_SD_upper'),label='Q vector SD upper bound',color=colors['Q_VECTOR'],lw=2)
        ax.plot(x,arr(rs,'post_SD'),label='Observed successor SD',color='#111111',lw=2)
        ax.set_ylabel('Native speed units');ax.legend()
    finish(fig,'01_baseline_and_observed_SD.png')
    fig,axs=axes2('Component profiles give the substantial fixed refinement')
    for ax,(view,rs) in zip(axs,byview.items()):
        x=arr(rs,'phase')
        for fam,label,ls in [('Q_VECTOR','Q vector','-'),('K_COMPONENT','K signed intervals','--'),
                             ('P_PROFILE','P absolute profiles','-'),('BEST_PRE','BEST = min(K,P)',':')]:
            ax.plot(x,arr(rs,fam+'_SD_upper'),label=label,color=colors[fam],ls=ls,lw=2)
        ax.plot(x,arr(rs,'post_SD'),label='Observed SD',color='black',lw=1.7)
        ax.set_yscale('log');ax.set_ylabel('Native speed units (log scale)');ax.legend(ncol=3,fontsize=9)
    finish(fig,'02_fixed_refinements.png')
    fig,axs=plt.subplots(2,1,figsize=(12,8),sharex=True,layout='constrained')
    fig.suptitle('Difference alignment and triangle-inequality slack')
    x=arr(curves,'phase')
    axs[0].plot(x,arr(curves,'T_TRIANGLE_mean'),label='Mean T over ten pair families',color='#a6611a')
    axs[0].plot(x,arr(curves,'Q_VECTOR_mean'),label='Mean Q over ten pair families',color=colors['Q_VECTOR'])
    axs[0].plot(x,arr(curves,'T_minus_Q_mean'),label='Mean T − Q',color='#018571',lw=2)
    axs[0].set_ylabel('Native speed units');axs[0].legend()
    with np.load(lp(ROOT/'analysis/center_pair_bounds.npz'),allow_pickle=False) as z:
        cross=z['center__difference_alignment'];j=z['pair__phase'][z['center__pair_phase_row']]
    axs[1].scatter(j,cross,s=3,alpha=.2,color='#555555',rasterized=True)
    axs[1].axhline(0,color='black',lw=.8);axs[1].set_ylabel('2 Δv · Δa (squared speed)')
    axs[1].set_title('Each dot is one labeled-center pair; cross-history alignment, not single-history v · a',fontsize=11)
    for ax in axs:ax.set_xlim(0,199);ax.set_xlabel('Common source phase j (0–199)')
    finish(fig,'03_difference_alignment.png')
    fig,axs=plt.subplots(2,1,figsize=(12,8),sharex=True,layout='constrained')
    fig.suptitle('Where the baseline inequality loses information')
    axs[0].plot(x,arr(curves,'gap_Q_to_S_mean'),label='Total Q − S',color=colors['Q_VECTOR'],lw=2)
    axs[0].plot(x,arr(curves,'gap_Q_to_BEST_mean'),label='Q − BEST: fixed refinement',color=colors['P_PROFILE'],lw=2)
    for key,label,color in [('gap_BEST_to_Zstar','BEST − Z*: derivative interval slack','#d95f02'),
                            ('gap_Zstar_to_Tnorm','Z* − Tnorm: norm projection','#7570b3'),
                            ('gap_Tnorm_to_S','Tnorm − S: signed center cancellation','#1b9e77')]:
        axs[1].plot(x,arr(curves,key+'_mean'),label=label,color=color,lw=1.8)
    for ax in axs:
        ax.set_xlim(0,199);ax.set_xlabel('Common source phase j (0–199)');ax.set_ylabel('Mean gap, native speed units');ax.legend(fontsize=10)
    axs[1].set_title('Means over the same ten pair families; inequality slack is not causal attribution',fontsize=11)
    finish(fig,'04_proof_slack_ladder.png')
    fig,axs=plt.subplots(2,2,figsize=(13,8),sharex=True,layout='constrained')
    fig.suptitle('Sufficient conditions versus actual variance changes')
    for vi,(view,rs) in enumerate(byview.items()):
        for ri,reference in enumerate(('incoming','pre_damping')):
            ax=axs[vi,ri];x=arr(rs,'phase')
            ax.plot(x,arr(rs,reference+'_condition_margin'),label='Reference variance − BEST upper bound',color='#b2182b')
            ax.plot(x,arr(rs,reference+'_actual_margin'),label='Reference variance − observed variance',color='#2166ac')
            ax.axhline(0,color='black',lw=.8);ax.set_xlim(0,199)
            ax.set_title(labels[view]+'\nReference: '+reference.replace('_',' '),fontsize=11)
            ax.set_ylabel('Variance margin (squared speed)');ax.set_xlabel('Common phase j (0–199)')
            ax.legend(fontsize=8,loc='lower right')
    finish(fig,'05_sufficient_condition_margins.png')
    fig,axs=axes2('Phasewise bound / observed SD: all phases retained')
    for ax,(view,rs) in zip(axs,byview.items()):
        x=arr(rs,'phase')
        for fam,label,ls in [('Q_VECTOR','Q vector','-'),('K_COMPONENT','K signed intervals','--'),('BEST_PRE','BEST (P for every recorded pair)','-')]:
            ax.plot(x,arr(rs,fam+'_SD_factor'),label=label,color=colors[fam],ls=ls,lw=1.8)
        for value in (2,5,10):ax.axhline(value,color='#aaaaaa',ls=':',lw=.8)
        ax.set_yscale('log');ax.set_ylabel('Dimensionless factor (log scale)');ax.legend(fontsize=9)
    finish(fig,'06_phasewise_tightness.png')
    need(len(paths)==6,'figure count')
    for n,x in before.items():need(ident(ROOT/'analysis'/n)==x,'plot changed numerical output')
    save(ROOT/'evidence/FIGURE_RESULT.json',{'status':'PASS','utc':utc(),'seconds':time.monotonic()-start,
        'count':6,'matplotlib':matplotlib.__version__,'sources':before,'files':{n:ident(ROOT/'plots'/n) for n in paths},
        'complete_phase_axes':[0,199],'presentation_corrections':0,'new_bound_evaluations':0,
        'native_units':True,'log_scale_figures':[2,6],'no_fit_or_independent_trial_errorbars':True})
    print(json.dumps({'status':'PASS','figures':paths,'seconds':time.monotonic()-start}))
if __name__=='__main__':main()

