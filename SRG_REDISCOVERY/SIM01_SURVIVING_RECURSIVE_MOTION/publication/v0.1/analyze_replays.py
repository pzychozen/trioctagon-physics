"""Read saved replay arrays only. Does not import or call a numerical engine."""
import csv
import json
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR']=str(ROOT/'cache/matplotlib')
os.environ['TMP']=os.environ['TEMP']=str(ROOT/'tmp')
os.environ['MPLBACKEND']='Agg'
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':10,'axes.titlesize':12,'axes.labelsize':10,'figure.dpi':130,
    'savefig.dpi':150,'axes.spines.top':False,'axes.spines.right':False})
colors=plt.get_cmap('tab10').colors
all_data={};results={}


def savefig(fig,name):
    fig.savefig(ROOT/'plots'/name,bbox_inches='tight',facecolor='white')
    plt.close(fig)


for name,steps,L,dt in [('A',500,2.,.05),('B',2000,10.,.1),('C',200,10.,.1)]:
    directory=ROOT/'runs'/name
    with np.load(directory/'states.npz',allow_pickle=False) as f:d={k:f[k] for k in f.files}
    p=d['positions'];v=d['velocities'];raw=d['raw_displacements'];minimal=d['minimal_image_displacements']
    assert len(p)==steps+1 and np.isfinite(p).all() and np.isfinite(v).all()
    assert np.array_equal(d['source_frame'],np.arange(steps))
    assert np.array_equal(d['source_time'],np.arange(steps)*dt)
    low=-1 if name=='A' else 0
    assert np.all((p>=low)&(p<low+L))
    assert np.array_equal(raw,np.diff(p,axis=0))
    assert np.array_equal(minimal,np.mod(raw+L/2,L)-L/2)
    assert np.max(np.abs(dt*v[1:]))<L/2
    residual=float(np.max(np.abs(minimal-dt*v[1:])))
    assert residual<1e-13
    speed=np.linalg.norm(v,axis=2)
    diff=np.mod(p[:,:,None,:]-p[:,None,:,:]+L/2,L)-L/2
    pairs=np.linalg.norm(diff,axis=3)[:,np.triu_indices(p.shape[1],1)[0],np.triu_indices(p.shape[1],1)[1]]
    mean_pair=pairs.mean(axis=1);diameter=pairs.max(axis=1)
    body_crossings=np.any(np.abs(raw)>L/2,axis=2)
    row={'source':name,'updates':steps,'stored_states':len(p),'finite_states':True,
        'source_time_range':[float(d['source_time'][0]),float(d['source_time'][-1])],
        'initial_mean_speed':float(speed[0].mean()),'final_mean_speed':float(speed[-1].mean()),
        'final_max_speed':float(speed[-1].max()),'peak_mean_speed':float(speed.mean(axis=1).max()),
        'initial_mean_pair_distance':float(mean_pair[0]),'final_mean_pair_distance':float(mean_pair[-1]),
        'minimum_mean_pair_distance':float(mean_pair.min()),'minimum_mean_pair_state_index':int(mean_pair.argmin()),
        'initial_toroidal_diameter':float(diameter[0]),'final_toroidal_diameter':float(diameter[-1]),
        'coordinate_wrap_crossing_body_updates':int(body_crossings.sum()),
        'maximum_minimal_image_step':float(np.linalg.norm(minimal,axis=2).max()),
        'unwrapping_position_velocity_residual':residual,
        'path_length_by_body':np.linalg.norm(minimal,axis=2).sum(axis=0).tolist(),
        'net_unwrapped_displacement_by_body':np.linalg.norm(d['unwrapped_positions'][-1]-p[0],axis=1).tolist(),
        'final_tenth_path_length_by_body':np.linalg.norm(minimal[-steps//10:],axis=2).sum(axis=0).tolist(),
        'H_range':[float(d['H'].min()),float(d['H'].max())],
        'H_negative_update_count':int(np.sum(d['H']<0)),'H_final':float(d['H'][-1]),
        'G_range':None if name=='A' else [float(d['G'].min()),float(d['G'].max())],
        'source_energy_initial_passive':float(.5*np.sum(speed[0]**2)) if name=='C' else None,
        'source_energy_final':float(d['energy'][-1]) if name=='C' else None}
    if name=='C':
        changes=d['bits'][1:]!=d['bits'][:-1]
        gate=d['G']>.5
        assert np.array_equal(d['draw_count'],8*gate.astype(int))
        assert np.array_equal(np.isfinite(d['draws']),np.repeat(gate[:,None],8,axis=1))
        assert np.array_equal(changes,np.where(gate[:,None],d['draws']<.01,False))
        assert np.array_equal(d['energy'],.5*np.sum(speed[1:]**2,axis=1))
        assert np.array_equal(d['detector_flags'],d['detector_distance']>1)
        switches=[{'update_index':int(k),'successor_state':int(k+1),'body':int(i),'draw':float(d['draws'][k,i]),
            'new_bit':int(d['bits'][k+1,i])} for k,i in zip(*np.where(changes))]
        row.update(actual_random_draws=int(d['draw_count'].sum()),gate_open_updates=int(gate.sum()),
            switches=switches,switch_count=len(switches),final_bits=d['bits'][-1].tolist(),
            historical_detector_events=int(d['detector_flags'].sum()),
            minimal_image_events_above_same_threshold=int(np.sum(np.linalg.norm(minimal,axis=2)>1)))
        with (directory/'switch_events.csv').open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=['update_index','successor_state','body','draw','new_bit']);w.writeheader();w.writerows(switches)
    with (directory/'observations.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['state_index','source_update_index','source_time_used','H_used','G_incoming',
            'mean_speed','max_speed','mean_minimal_image_pair_distance','toroidal_diameter',
            'wrap_crossing_bodies','source_detector_events','actual_draws','switches','source_energy_after_step'])
        for k in range(steps+1):
            j=k-1
            w.writerow([k,j if k else '',d['source_time'][j] if k else '',d['H'][j] if k else '',
                d['G'][j] if k and name!='A' else '',speed[k].mean(),speed[k].max(),mean_pair[k],diameter[k],
                int(body_crossings[j].sum()) if k else '',int(d['detector_flags'][j].sum()) if k and name=='C' else '',
                int(d['draw_count'][j]) if k and name=='C' else '',int(changes[j].sum()) if k and name=='C' else '',
                d['energy'][j] if k and name=='C' else ''])
    (directory/'OBSERVATIONS.json').write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8')
    results[name]=row;all_data[name]=(d,speed,mean_pair)

    fig=plt.figure(figsize=(12,5.5),layout='constrained')
    axes=[fig.add_subplot(1,2,i+1,projection='3d' if name!='A' else None) for i in range(2)]
    for which,ax in enumerate(axes):
        data=p.copy() if which==0 else d['unwrapped_positions']
        for i in range(p.shape[1]):
            line=data[:,i].copy()
            if which==0:line[1:][body_crossings[:,i]]=np.nan
            coords=[line[:,j] for j in range(p.shape[2])]
            ax.plot(*coords,color=colors[i],lw=1.2,label=f'Center {i}')
            ax.scatter(*[data[0,i,j] for j in range(p.shape[2])],color=colors[i],marker='o',s=20)
            ax.scatter(*[data[-1,i,j] for j in range(p.shape[2])],color=colors[i],marker='x',s=30)
        ax.set_xlabel('x');ax.set_ylabel('y')
        if name!='A':ax.set_zlabel('z');ax.view_init(elev=24,azim=-58)
        else:ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.2)
        if which==0:
            ax.set_xlim(low,low+L);ax.set_ylim(low,low+L)
            if name!='A':ax.set_zlim(low,low+L)
        ax.set_title('Stored wrapped coordinates; lines break at crossings' if which==0 else 'Displacement-accumulated unwrapped view')
    handles,labels=axes[0].get_legend_handles_labels()
    fig.legend(handles,labels,loc='outside lower center',ncol=4 if name!='A' else 3,frameon=False)
    fig.suptitle(f'{name}: {steps:,} updates, seed 2038 | circles = initial, crosses = final\nUnwrapped view is passive accounting, not extra dynamical state',fontsize=13)
    savefig(fig,f'{name}_trajectories.png')

fig,axs=plt.subplots(3,2,figsize=(12,10),layout='constrained')
for r,name in enumerate('ABC'):
    d,speed,pair=all_data[name];x=np.arange(len(speed))
    for i in range(speed.shape[1]):axs[r,0].semilogy(x,np.maximum(speed[:,i],1e-18),color=colors[i],alpha=.5,lw=.7)
    axs[r,0].semilogy(x,np.maximum(speed.mean(axis=1),1e-18),color='black',lw=1.8,label='Mean speed')
    axs[r,0].set_title(f'{name}: carried velocity magnitude');axs[r,0].set_ylabel('Speed (source coordinates / source time)')
    axs[r,0].legend(frameon=False)
    axs[r,1].semilogy(x,np.maximum(pair,1e-18),color='#006d77',lw=1.6)
    axs[r,1].set_title(f'{name}: mean pair distance on the periodic box');axs[r,1].set_ylabel('Minimal-image distance')
    for ax in axs[r]:ax.set_xlabel('Completed numerical updates');ax.grid(alpha=.2)
fig.suptitle('Finite replay observations | log display floor 1e-18; raw zeros retained\nDifferent models and durations are independent baselines, not matched interventions',fontsize=13)
savefig(fig,'motion_metrics.png')

fig,axs=plt.subplots(3,2,figsize=(12,10),layout='constrained')
for r,name in enumerate('ABC'):
    d=all_data[name][0]
    axs[r,0].plot(d['update_index'],d['H'],color='#8b4b31')
    axs[r,0].axhline(0,color='gray',lw=.6)
    axs[r,0].set_title(f'{name}: prescribed H evaluated at {"0.05" if name=="A" else "0.1"} x source index')
    axs[r,0].set_xlabel('Source update/frame index');axs[r,0].set_ylabel('H used for this update');axs[r,0].grid(alpha=.2)
for r,name in enumerate('BC'):
    d=all_data[name][0]
    axs[r,1].plot(d['update_index'],d['G'],color='#5c4d7d')
    axs[r,1].set_title(f'{name}: G from incoming mean speed (frozen per call)')
    axs[r,1].set_xlabel('Source frame index');axs[r,1].set_ylabel('G');axs[r,1].grid(alpha=.2)
d=all_data['C'][0]
axs[2,1].imshow(d['bits'].T,aspect='auto',origin='lower',interpolation='nearest',cmap='coolwarm',vmin=0,vmax=1,
    extent=(-.5,len(d['bits'])-.5,-.5,7.5))
axs[2,1].set_title(f'C: binary sign history ({results["C"]["switch_count"]} actual toggles)\nBlue = bit 0; red = bit 1 (force-sign multiplier)')
axs[2,1].set_xlabel('Completed numerical updates');axs[2,1].set_ylabel('Center index');axs[2,1].set_yticks(range(8))
fig.suptitle('Assigned clock forcing, state feedback and recorded binary choices\nH is externally scheduled; G and rule bits are distinct quantities',fontsize=13)
savefig(fig,'forcing_and_feedback.png')

final={'method':'Passive readout of completed saved replays; zero numerical engine calls.',
    'numerical_updates_added':0,'A':results['A'],'B':results['B'],'C':results['C'],
    'state_schema':'positions/velocities/bits: state 0 is initial; state k+1 follows update k. H/G/time/draw/detector/energy arrays are per update. Unwrapped coordinates sum minimal-image increments.',
    'rendering':'Matplotlib Agg; no GUI. Wrapped trajectory segments crossing box edges are broken, not connected across the box.'}
(ROOT/'evidence/REPLAY_OBSERVATIONS.json').write_text(json.dumps(final,indent=2)+'\n',encoding='utf-8')
print(json.dumps(final,indent=2))
