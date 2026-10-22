"""Read original CSVs in physical row order. Never simulate or call old code.

Equation residuals substitute consecutive OBSERVED states, including observed
post-update position prefixes. No calculated state is fed into a later step.
"""
from pathlib import Path
import csv, hashlib, json, platform
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "A": "PLOT_1_tetrahedral_states_20250712_015421.csv",
    "B": "tetrahedral_states_20250712_015647.csv",
}
DT, L = 0.1, 10.0
SCHEMA = ["Step","Tetrahedron","X","Y","Z","VX","VY","VZ","Energy","GRF","Rule_State"]
def H(t):
    return 2*np.exp(-.5*t)*np.cos(t)+np.exp(-.3*t)*np.sin(t)+1.5*np.exp(-.7*t)+np.exp(-.4*t)
def D(x):
    return (x+5)%10-5
def save_json(name, obj):
    (ROOT/"analysis"/name).write_text(json.dumps(obj,indent=2,allow_nan=False),encoding="utf-8")
def write_csv(name, rows):
    if not rows:
        return
    with (ROOT/"analysis"/name).open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def anchor(q,i=None):
    q=int(q)
    return {"callback":q,"csv_first_line":8*q+2,"csv_last_line":8*q+9,
            **({"body":int(i),"csv_line":8*q+2+int(i)} if i is not None else {})}
def longest_true(mask):
    best=(0,0,0)
    start=None
    for q, flag in enumerate(np.r_[mask,False]):
        if flag and start is None:start=q
        if not flag and start is not None:
            if q-start>best[0]:best=(q-start,start,q-1)
            start=None
    return best

summary={}
for label, filename in FILES.items():
    path=ROOT/"originals"/filename
    with path.open(newline="",encoding="utf-8-sig") as f:
        reader=csv.reader(f); header=next(reader); rows=list(reader)
    assert header==SCHEMA
    assert all(len(r)==11 for r in rows)
    a=np.array(rows,dtype=float)
    assert np.isfinite(a).all()
    assert len(a)%8==0
    a=a.reshape(-1,8,11)
    n=len(a)
    assert np.all(a[:,:,1]==np.arange(8))
    assert np.all(a[:,:,0]==a[:,0,0,None])
    assert all(np.all(a[:,:,col]==a[:,0,col,None]) for col in (8,9))
    assert np.all(np.isin(a[:,:,10],[0,1]))
    f=a[:,0,0].astype(int); x=a[:,:,2:5]; v=a[:,:,5:8]
    E=a[:,0,8]; g=a[:,0,9]; b=a[:,:,10].astype(int)
    assert np.all((x>=0)&(x<10))
    assert np.all(a[:,:,0]==a[:,:,0].astype(int))
    speed=np.linalg.norm(v,axis=2)
    native=.1*v[1:]
    raw=np.diff(x,axis=0)
    shift=np.rint((raw-native)/10).astype(int)
    seam=np.any(shift!=0,axis=2)
    native_len=np.linalg.norm(native,axis=2)
    raw_len=np.linalg.norm(raw,axis=2)
    detector=np.linalg.norm(raw%10,axis=2)
    alarm=detector>1
    flipped=b[1:]!=b[:-1]
    turn_cos=np.sum(v[1:]*v[:-1],axis=2)/(speed[1:]*speed[:-1])
    # No deduplication: rows and callback indices remain ordered.
    discontinuities=np.flatnonzero(np.diff(f)!=1)+1
    starts=np.r_[0,discontinuities];ends=np.r_[discontinuities-1,n-1]
    segments=[{**anchor(s),"end_callback":int(e),"end_csv_line":8*int(e)+9,
               "first_label":int(f[s]),"last_label":int(f[e]),
               "callback_count":int(e-s+1)}
              for s,e in zip(starts,ends)]
    resets=[{**anchor(q),"previous_label":int(f[q-1]),"label":int(f[q]),
             "previous_energy":float(E[q-1]),"energy":float(E[q]),
             "previous_GRF":float(g[q-1]),"GRF":float(g[q]),
             "previous_H":float(H(.1*f[q-1])),"H":float(H(.1*f[q])),
             "max_native_increment":float(native_len[q-1].max())}
            for q in discontinuities]
    wrap_events=[]
    for qi,i in np.argwhere(seam):
        q=int(qi+1);i=int(i)
        wrap_events.append({**anchor(q,i),"previous_label":int(f[q-1]),"label":int(f[q]),
            "coordinate_shift":shift[qi,i].tolist(),"before":x[q-1,i].tolist(),
            "after":x[q,i].tolist(),"velocity":v[q,i].tolist(),
            "native_increment":float(native_len[qi,i]),
            "stored_coordinate_jump":float(raw_len[qi,i]),
            "source_detector_distance":float(detector[qi,i]),
            "source_detector_would_flag":bool(alarm[qi,i])})
    switches=[]
    for qi,i in np.argwhere(flipped):
        q=int(qi+1);i=int(i)
        switches.append({**anchor(q,i),"label":int(f[q]),"old_mode":int(b[q-1,i]),
                         "new_mode":int(b[q,i]),"GRF":float(g[q]),
                         "H":float(H(.1*f[q])),"incoming_speed":float(speed[q-1,i]),
                         "outgoing_speed":float(speed[q,i]),
                         "velocity_direction_cosine":float(turn_cos[qi,i]),
                         "native_increment":float(native_len[qi,i])})
    pair_records=[];best_streak=(0,None)
    for i in range(8):
        for j in range(i+1,8):
            dist=np.linalg.norm(D(x[:,j]-x[:,i]),axis=1)
            cosine=np.sum(v[:,i]*v[:,j],axis=1)/(speed[:,i]*speed[:,j])
            q=int(np.argmin(dist))
            record={**anchor(q),"body_i":i,"body_j":j,"line_i":8*q+2+i,"line_j":8*q+2+j,
                    "label":int(f[q]),"periodic_distance":float(dist[q]),
                    "velocity_cosine":float(cosine[q]),
                    "speed_i":float(speed[q,i]),"speed_j":float(speed[q,j]),
                    "relative_speed":float(np.linalg.norm(v[q,i]-v[q,j]))}
            pair_records.append(record)
            # Declared descriptive screen, not a path-inheritance criterion.
            mask=(dist<.1)&(cosine>.9)&(speed[:,i]>1e-6)&(speed[:,j]>1e-6)
            count,s,e=longest_true(mask)
            if count>best_streak[0]:
                best_streak=(count,{"body_i":i,"body_j":j,"start":anchor(s),
                    "end":anchor(e),"callbacks":count,"labels":[int(f[s]),int(f[e])],
                    "distance_range":[float(dist[s:e+1].min()),float(dist[s:e+1].max())],
                    "cosine_min":float(cosine[s:e+1].min()),
                    "speed_range":[float(min(speed[s:e+1,i].min(),speed[s:e+1,j].min())),
                                   float(max(speed[s:e+1,i].max(),speed[s:e+1,j].max()))]})
    closest=min(pair_records,key=lambda z:z["periodic_distance"])
    qmax,imax=np.unravel_index(np.argmax(native_len),native_len.shape);qmax+=1
    qraw,iraw=np.unravel_index(np.argmax(raw_len),raw_len.shape);qraw+=1
    qturn,iturn=np.unravel_index(np.argmin(turn_cos),turn_cos.shape);qturn+=1
    qfp,ifp=np.argwhere(alarm&~seam)[0]
    qfp+=1
    samples=sorted(set(list(range(1,6))+list(range(n-5,n))+
        [int(qmax),int(qturn),max(1,closest["callback"]),int(discontinuities[0]),
         int(np.flatnonzero(np.diff(f)<0)[0]+1)]+
        ([switches[0]["callback"]] if switches else [])+
        ([wrap_events[0]["callback"]] if wrap_events else [])))
    # Residuals: plug OBSERVED old and new values into equations, independently
    # for each sample. Never feed calculated velocity/position into another body.
    checks=[]
    for q in samples:
        gs=1/(1+speed[q-1].mean());hs=H(.1*f[q])
        residuals=[];work=0.;loss=0.
        for i in range(8):
            mixed=np.concatenate((x[q,:i],x[q-1,i:]),axis=0)
            c=mixed.mean(axis=0)
            d=D(c-x[q-1,i])
            kick=.1*gs*hs*(1-2*b[q,i])*d/(np.linalg.norm(d)+.01)
            candidate=v[q-1,i]+kick
            rhs=candidate/(1+np.log1p(np.abs(candidate)))
            residuals.append(float(np.max(np.abs(v[q,i]-rhs))))
            work+=float(np.dot(v[q-1,i],kick)+.5*np.dot(kick,kick))
            loss+=float(.5*(np.dot(candidate,candidate)-np.dot(v[q,i],v[q,i])))
        checks.append({**anchor(q),"label":int(f[q]),
                       "maximum_velocity_equation_residual":max(residuals),
                       "GRF_residual":float(abs(g[q]-gs)),
                       "kinetic_change":float(E[q]-E[q-1]),
                       "drive_work_plus_quadratic":work,"damping_loss":loss,
                       "energy_balance_residual":float(abs(E[q]-E[q-1]-work+loss))})
    totalK=.5*np.sum(speed**2,axis=1)
    block_rows=[]
    for q in range(n):
        block_rows.append({**anchor(q),"label":int(f[q]),"H_argument":.1*int(f[q]),
          "H":float(H(.1*f[q])),"energy":float(E[q]),"GRF":float(g[q]),
          "mean_speed":float(speed[q].mean()),"max_speed":float(speed[q].max()),
          "mode_1_count":int(b[q].sum()),
          "flips_from_previous":int(flipped[q-1].sum()) if q else "",
          "seam_bodies_from_previous":int(seam[q-1].sum()) if q else "",
          "source_detector_flags_from_previous":int(alarm[q-1].sum()) if q else "",
          "max_native_increment_from_previous":float(native_len[q-1].max()) if q else "",
          "max_stored_jump_from_previous":float(raw_len[q-1].max()) if q else ""})
    s={
      "file":filename,"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
      "schema":header,"data_rows":len(rows),"callbacks":n,"partial_or_corrupt_blocks":0,
      "labels":{"min":int(f.min()),"max":int(f.max()),"unique":len(set(f)),
                "duplicate_step_body_rows":len(rows)-len(set(zip(a[:,:,0].ravel(),a[:,:,1].ravel()))),
                "counts":{str(int(k)):int(vv) for k,vv in zip(*np.unique(f,return_counts=True))}},
      "segments":segments,"nonconsecutive_label_transitions":resets,
      "first_modes":b[0].tolist(),"last_modes":b[-1].tolist(),
      "GRF_range":[float(g.min()),float(g.max())],
      "gate_eligible_callbacks":int(np.sum(g>.5)),
      "observed_between_block_mode_flips":int(flipped.sum()),
      "flips_per_body":flipped.sum(axis=0).astype(int).tolist(),
      "flips_at_closed_gate":int(np.sum(flipped&~(g[1:,None]>.5))),
      "flips_with_immediate_obtuse_velocity_turn":int(np.sum(flipped&(turn_cos<0))),
      "total_obtuse_velocity_turns":int(np.sum(turn_cos<0)),
      "seam_body_events":int(seam.sum()),"seam_coordinate_events":int(np.sum(shift!=0)),
      "source_detector_flags":int(alarm.sum()),
      "source_detector_flag_no_seam":int(np.sum(alarm&~seam)),
      "source_detector_flag_with_seam":int(np.sum(alarm&seam)),
      "source_detector_unflagged_seams":int(np.sum(~alarm&seam)),
      "max_native":{"value":float(native_len[qmax-1,imax]),**anchor(qmax,imax),"label":int(f[qmax])},
      "max_stored_jump":{"value":float(raw_len[qraw-1,iraw]),**anchor(qraw,iraw),"label":int(f[qraw]),
                         "native_increment":float(native_len[qraw-1,iraw])},
      "most_obtuse_turn":{"cosine":float(turn_cos[qturn-1,iturn]),**anchor(qturn,iturn),
                           "label":int(f[qturn]),"speed_before":float(speed[qturn-1,iturn]),
                           "speed_after":float(speed[qturn,iturn]),"mode_before":int(b[qturn-1,iturn]),
                           "mode_after":int(b[qturn,iturn])},
      "first_detector_flag_without_seam":{**anchor(qfp,ifp),"label":int(f[qfp]),
           "raw_delta":raw[qfp-1,ifp].tolist(),"native_increment":float(native_len[qfp-1,ifp]),
           "detector_distance":float(detector[qfp-1,ifp])},
      "energy":{"initial_recorded":float(E[0]),"last":float(E[-1]),
                "min":float(E.min()),"min_callback":int(np.argmin(E)),
                "max":float(E.max()),"max_callback":int(np.argmax(E)),
                "all_block_residual_max":float(np.max(np.abs(E-totalK)))},
      "position_velocity_identity_max_residual":float(np.max(np.abs(D(raw-native)))),
      "GRF_previous_velocity_all_transition_max_residual":float(np.max(np.abs(g[1:]-1/(1+speed[:-1].mean(axis=1))))),
      "sampled_velocity_checks":checks,"closest_pair":closest,
      "descriptive_pair_screen":{"condition":"periodic distance < 0.1; velocity cosine > 0.9; each speed > 1e-6; consecutive physical callback blocks",
                                 "longest":best_streak[1]},
      "body7_first_position":x[0,7].tolist(),
      "body7_first_last_position_each_segment":[{"start":int(st),"end":int(en),
          "start_position":x[st,7].tolist(),"end_position":x[en,7].tolist()} for st,en in zip(starts,ends)],
      "first_switch":switches[0] if switches else None,
      "first_seam":wrap_events[0] if wrap_events else None,
      "checked_transitions":n-1,
    }
    summary[label]=s
    save_json(f"{label}_wrap_events.json",wrap_events)
    save_json(f"{label}_switch_events.json",switches)
    save_json(f"{label}_pair_minima.json",pair_records)
    write_csv(f"{label}_callbacks.csv",block_rows)
    write_csv(f"{label}_equation_residuals.csv",checks)
    # Fresh figures depict original records only, using callback order.
    fig,axs=plt.subplots(4,1,figsize=(12,10),sharex=True,layout="constrained")
    q=np.arange(n)
    axs[0].plot(q,f,lw=1,color="#334155");axs[0].set_ylabel("Stored Step label")
    axs[1].plot(q,E,color="#be185d",lw=1);axs[1].set_ylabel("System Energy\n(sum once)")
    axs[2].plot(q,g,color="#0369a1",lw=1);axs[2].axhline(.5,color="gray",ls="--");axs[2].set_ylabel("Incoming GRF")
    axs[3].imshow(b.T,aspect="auto",origin="lower",interpolation="nearest",
        extent=[-.5,n-.5,-.5,7.5],cmap="Greys",vmin=0,vmax=1)
    axs[3].set_yticks(range(8));axs[3].set_ylabel("Body / binary mode\nwhite 0, black 1")
    axs[3].set_xlabel("Callback index in original CSV row order (zero based)")
    for ax in axs[:3]:
        for reset in discontinuities:ax.axvline(reset,color="#999999",ls=":",lw=.6)
        ax.grid(alpha=.2)
    fig.suptitle(f"Original log {label}: labels restart while recorded state continues")
    fig.savefig(ROOT/"visuals"/f"{label}_chronology.png",dpi=140);plt.close(fig)
    fig,axs=plt.subplots(3,1,figsize=(12,8),sharex=True,layout="constrained")
    axs[0].plot(q[1:],native_len.max(axis=1),label="max 0.1 |recorded velocity|",color="#0369a1")
    axs[0].set_ylabel("Native increment");axs[0].legend(loc="upper right")
    axs[1].plot(q[1:],raw_len.max(axis=1),color="#be185d");axs[1].set_ylabel("Largest stored\ncoordinate jump")
    axs[2].plot(q[1:],alarm.sum(axis=1),label="source detector would flag",lw=.7)
    axs[2].step(q[1:],seam.sum(axis=1),label="actual coordinate seam",lw=1)
    axs[2].set_ylabel("Bodies per callback");axs[2].legend(loc="upper right")
    axs[2].set_xlabel("Callback index in original CSV row order (zero based)")
    for ax in axs:ax.grid(alpha=.2)
    fig.suptitle(f"Original log {label}: native movement, wrapped coordinates and detector")
    fig.savefig(ROOT/"visuals"/f"{label}_movement.png",dpi=140);plt.close(fig)
save_json("log_summary.json",summary)
save_json("analysis_environment.json",{"python":platform.python_version(),"numpy":np.__version__,
    "matplotlib":matplotlib.__version__,"scope":"Original-data analysis only; no old module imports, RNG draws, new initial states or simulated transitions."})
for label,s in summary.items():
    short={k:v for k,v in s.items() if k not in ["labels","schema","sampled_velocity_checks","body7_first_last_position_each_segment"]}
    print(label,json.dumps(short,indent=2))
