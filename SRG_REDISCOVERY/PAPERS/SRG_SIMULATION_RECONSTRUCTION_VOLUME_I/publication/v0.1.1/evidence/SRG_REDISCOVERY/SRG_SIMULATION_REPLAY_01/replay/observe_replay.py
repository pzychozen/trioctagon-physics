"""NEW REPLAY observation/rendering only. Loads saved records; never advances dynamics."""
from pathlib import Path
import os, json, csv
BASE=Path(__file__).resolve().parent
os.environ["MPLCONFIGDIR"]=str(BASE/"mplconfig")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

VIS=BASE.parent/"visuals"
VIS.mkdir(exist_ok=True)
data=np.load(BASE/"trajectory.npz",allow_pickle=False)
events=[json.loads(s) for s in (BASE/"within_sweep.jsonl").read_text().splitlines()]
assert json.loads((BASE/"equivalence.json").read_text())["faithful_in_this_environment"]
P,V=data["positions"],data["velocities"]
E=data["event_positions"]
h,t=data["H"],data["t"]
COLORS=["#1875b9","#e87816","#269650"]
PAIRS=[(0,1),(0,2),(1,2)]
wrap=lambda z: np.mod(z+1.0,2.0)-1.0
pair_dist=np.stack([np.linalg.norm(wrap(P[1:,b]-P[1:,a]),axis=1) for a,b in PAIRS],axis=1)
loc=np.unravel_index(np.argmin(pair_dist),pair_dist.shape)
closest_step,closest_pair=int(loc[0]),PAIRS[int(loc[1])]
crossings=[e for e in events if any(e["position_wrap_lattice"])]
native=np.linalg.norm(data["event_native_displacement"],axis=1)
screen=np.array([np.linalg.norm(e["screen_displacement"]) for e in events])
largest=int(np.argmax(native))
def brief(e):
    return {k:e[k] for k in ("event_id","step","sweep_number","point","t","H",
            "native_displacement","raw_updated_position","post_wrap_position",
            "screen_displacement","position_wrap_lattice")}
def bounds(center):
    return list(range(max(0,center-1),min(499,center+1)+1))
windows=[{"name":"opening","steps":[0,1,2],"rule":"First three complete sweeps."}]
if crossings:
    windows.append({"name":"first_wrap","steps":bounds(crossings[0]["step"]),
                    "rule":"First actual position-wrap event, with adjacent sweeps."})
windows.append({"name":"closest_pair","steps":bounds(closest_step),
                "rule":"Minimum simultaneous torus pair distance over saved end states; earliest state/pair tie break."})
summary={
 "label":"NEW REPLAY","sampled_initial_configurations":1,
 "position_wrap_event_count":len(crossings),
 "position_wrap_events_by_point":[sum(e["point"]==i for e in crossings) for i in range(3)],
 "first_position_wrap":brief(crossings[0]) if crossings else None,
 "force_comparisons_with_nonzero_wrap":sum(any(c["force_wrap_lattice"]) for e in events for c in e["interactions"]),
 "largest_native_step":{**brief(events[largest]),"norm":float(native[largest])},
 "largest_screen_step":{"event_id":int(np.argmax(screen))+1,"norm":float(screen.max())},
 "closest_simultaneous_pair":{"step":closest_step,"state_index":closest_step+1,
        "t_used":float(t[closest_step]),"pair":list(closest_pair),"distance":float(pair_dist[loc]),
        "positions":P[closest_step+1].tolist(),"velocities":V[closest_step+1].tolist()},
 "initial_pair_distances":[{"pair":list(pair),"distance":float(np.linalg.norm(wrap(P[0,b]-P[0,a])))} for pair in PAIRS for a,b in [pair]],
 "final_pair_distances":[{"pair":list(pair),"distance":float(pair_dist[-1,k])} for k,pair in enumerate(PAIRS)],
 "initial_positions":P[0].tolist(),"final_positions":P[-1].tolist(),"final_velocities":V[-1].tolist(),
 "first_three_end_states":[{"state_index":n,"step":n-1,"t":float(t[n-1]),"H":float(h[n-1]),"positions":P[n].tolist(),"velocities":V[n].tolist()} for n in range(1,4)],
 "H_min":float(h.min()),"H_max":float(h.max()),
 "H_sign_changes":[{"step_before":int(k),"step_after":int(k+1),"t_after":float(t[k+1]),"H_before":float(h[k]),"H_after":float(h[k+1])} for k in np.flatnonzero(np.signbit(h[1:])!=np.signbit(h[:-1]))],
 "windows":windows,
 "window_center_events":{w["name"]:[events[3*(crossings[0]["step"] if w["name"]=="first_wrap" else closest_step if w["name"]=="closest_pair" else 0)+i] for i in range(3)] for w in windows},
 "all_position_wrap_events":[brief(e) for e in crossings],
 "position_bounds":{"min":P.min(axis=(0,1)).tolist(),"max":P.max(axis=(0,1)).tolist()},
 "native_increment_total_by_point":[float(native[i::3].sum()) for i in range(3)],
 "finite_arrays":bool(np.isfinite(P).all() and np.isfinite(V).all()),
 "screen_native_lattice_identity_max_residual":float(max(np.max(np.abs(np.array(e["screen_displacement"])-np.array(e["native_displacement"])+2*np.array(e["position_wrap_lattice"]))) for e in events))
}
(BASE/"observation_summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
selected=[e for e in events if any(e["step"] in w["steps"] for w in windows)]
(BASE/"selected_events.jsonl").write_text("\n".join(json.dumps(e,separators=(",",":")) for e in selected)+"\n",encoding="utf-8")
with (BASE/"selected_events.csv").open("w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["label","event_id","step","point","t","H",
        "input_P0_x","input_P0_y","input_P1_x","input_P1_y","input_P2_x","input_P2_y",
        "net_force_x","net_force_y","velocity_before_x","velocity_before_y",
        "velocity_pre_damping_x","velocity_pre_damping_y","velocity_after_x","velocity_after_y",
        "native_dx","native_dy","raw_x","raw_y","wrapped_x","wrapped_y","wrap_kx","wrap_ky"])
    for e in selected:
        vals=[e["t"],e["H"],*np.array(e["input_positions"]).ravel(),*e["net_force"],
              *e["velocity_before"],*e["velocity_pre_damping"],*e["velocity_post_damping"],
              *e["native_displacement"],*e["raw_updated_position"],*e["post_wrap_position"]]
        writer.writerow(["NEW REPLAY",e["event_id"],e["step"],e["point"],
                         *(format(float(x),".17g") for x in vals),*e["position_wrap_lattice"]])

def setup(ax,world=True):
    ax.set_aspect("equal",adjustable="box")
    ax.grid(alpha=.2)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    if world:
        ax.set_xlim(-1.06,1.06);ax.set_ylim(-1.06,1.06)
        ax.add_patch(Rectangle((-1,-1),2,2,fill=False,ls="--",lw=.9,color="#777777"))
def path(ax,i,seam=False,up_to=500,include_initial=False,alpha=1):
    begin=0 if include_initial else 1
    xs=[];ys=[]
    for n in range(begin,up_to+1):
        if n>begin and seam and any(events[(n-1)*3+i]["position_wrap_lattice"]):
            xs.append(np.nan);ys.append(np.nan)
        xs.append(P[n,i,0]);ys.append(P[n,i,1])
    ax.plot(xs,ys,color=COLORS[i],lw=1.3,alpha=alpha,label=f"Point {i} (Attractor {i+1})")
def save(fig,name):
    fig.savefig(VIS/name,dpi=150,facecolor="white",metadata={"Description":"NEW REPLAY; legacy seed 0; recorded data only"})
    plt.close(fig)

for seam,name in [(False,"wrapped_paths.png"),(True,"seam_aware_paths.png")]:
    fig,ax=plt.subplots(figsize=(8,8))
    for i in range(3):path(ax,i,seam)
    ax.set_title("NEW REPLAY · legacy seed 0\n"+("Seam-aware paths: omit observed wrap connectors" if seam else "Source convention: join wrapped recorded positions"))
    ax.set_xlabel("X");ax.set_ylabel("Y");ax.grid(True);ax.axis("equal");ax.legend(fontsize=9)
    fig.text(.5,.015,"500 post-sweep samples per point. Lines join samples; no intermediate states are inferred.",
             ha="center",fontsize=8)
    fig.tight_layout(rect=(0,.035,1,1))
    save(fig,name)

# Ordered contacts: each row is one whole sweep, each column is before/after a point.
for window in windows:
    steps=window["steps"]
    seen=np.concatenate([P[steps[0]][None],E[3*steps[0]:3*(steps[-1]+1)]],axis=0)
    has_wrap=any(any(events[k]["position_wrap_lattice"]) for k in range(3*steps[0],3*(steps[-1]+1)))
    mn,mx=seen.min(axis=(0,1)),seen.max(axis=(0,1))
    center=(mn+mx)/2;span=max(float(np.max(mx-mn))*1.35,.002)
    fig,axes=plt.subplots(len(steps),4,figsize=(16,4*len(steps)),squeeze=False)
    for row,step in enumerate(steps):
        frames=[P[step],E[3*step],E[3*step+1],E[3*step+2]]
        for col,positions in enumerate(frames):
            ax=axes[row,col]
            setup(ax,has_wrap)
            if not has_wrap:
                ax.set_xlim(center[0]-span/2,center[0]+span/2)
                ax.set_ylim(center[1]-span/2,center[1]+span/2)
            ax.tick_params(labelsize=7)
            # Window-local trails, using actual event endpoints only; seams omitted.
            event_end=3*step+col
            for i in range(3):
                hist=[P[steps[0],i]]
                for k in range(3*steps[0],event_end):
                    if events[k]["point"]==i:
                        if any(events[k]["position_wrap_lattice"]):hist.append([np.nan,np.nan])
                        hist.append(events[k]["post_wrap_position"])
                hist=np.array(hist)
                ax.plot(hist[:,0],hist[:,1],color=COLORS[i],lw=1,alpha=.55)
                ax.scatter(*positions[i],color=COLORS[i],s=42,zorder=4)
                ax.annotate(f"P{i}",positions[i],xytext=(5,6+8*i),textcoords="offset points",fontsize=8,color=COLORS[i])
            if col:
                e=events[3*step+col-1];i=e["point"]
                ax.scatter(*positions[i],s=150,facecolors="none",edgecolors="black",lw=1,zorder=5)
                before=np.array(e["input_positions"][i])
                ax.plot(*before,marker="x",color="black",ms=5)
                if not any(e["position_wrap_lattice"]):
                    ax.annotate("",xy=positions[i],xytext=before,arrowprops={"arrowstyle":"->","color":"black","lw":.8})
                title=f"step {step} · after P{i} · event {e['event_id']}"
            else:title=f"step {step} · before P0 · event {3*step}"
            ax.set_title(title+f"\nt={t[step]:.2f}, H={h[step]:.5g}",fontsize=9)
    fig.suptitle(f"NEW REPLAY · {window['name'].replace('_',' ')} · read rows left to right\n"
                 "Circles: recorded positions. Black ring: point just updated. ×: its previous position.",fontsize=13)
    fig.tight_layout(rect=(0,.02,1,.94))
    fig.text(.5,.006,"Fixed axes within this sheet. Arrows connect recorded endpoints; no interpolated states. "+("Full wrapped square." if has_wrap else "Local coordinate zoom."),
             ha="center",fontsize=9)
    save(fig,window["name"]+"_sequence.png")

fig,axes=plt.subplots(2,1,figsize=(11,7),sharex=True)
for k,(a,b) in enumerate(PAIRS):
    axes[0].plot(np.arange(1,501),pair_dist[:,k],label=f"P{a}–P{b}")
axes[0].scatter([closest_step+1],[float(pair_dist[loc])],color="black",s=25,zorder=5)
axes[0].set_ylabel("Simultaneous torus distance");axes[0].legend();axes[0].grid(alpha=.2)
for i in range(3):axes[1].plot(np.arange(1,501),native[i::3],color=COLORS[i],label=f"P{i}")
axes[1].set_xlabel("Completed sweeps / state index n");axes[1].set_ylabel("Native increment length |dt · v_new|");axes[1].legend();axes[1].grid(alpha=.2)
fig.suptitle("NEW REPLAY · timing separates occupied positions from accumulated trails")
fig.tight_layout()
save(fig,"movement_over_time.png")

if crossings:
    e=crossings[0];i=e["point"];before=np.array(e["input_positions"][i]);raw=np.array(e["raw_updated_position"]);after=np.array(e["post_wrap_position"])
    fig,axes=plt.subplots(1,2,figsize=(12,5))
    ax=axes[0];setup(ax)
    ax.plot([before[0],after[0]],[before[1],after[1]],":",color="#9b2f2f",label="Screen connector, not a native long step")
    ax.scatter(*before,color=COLORS[i],marker="o",label="Before");ax.scatter(*after,color=COLORS[i],marker="s",label="After wrapping")
    ax.legend(fontsize=8);ax.set_title(f"event {e['event_id']} · step {e['step']} · P{i}")
    ax=axes[1];setup(ax,False)
    ax.scatter(*before,color=COLORS[i],label="Recorded input");ax.scatter(*raw,color=COLORS[i],marker="s",label="Recorded raw endpoint")
    ax.annotate("",xy=raw,xytext=before,arrowprops={"arrowstyle":"->","color":"black"})
    span=max(np.max(np.abs(raw-before))*3,.003);mid=(before+raw)/2
    ax.set_xlim(mid[0]-span,mid[0]+span);ax.set_ylim(mid[1]-span,mid[1]+span)
    for d in range(2):
        for edge in [-1,1]:
            if d==0:ax.axvline(edge,color="#777",ls="--",lw=1)
            else:ax.axhline(edge,color="#777",ls="--",lw=1)
    ax.legend(fontsize=8);ax.set_title("Local view before coordinate wrapping")
    fig.suptitle("NEW REPLAY · first observed wrap\n"
                 f"native increment {np.linalg.norm(e['native_displacement']):.8g}; screen change {np.linalg.norm(e['screen_displacement']):.8g}")
    fig.tight_layout()
    save(fig,"first_wrap_detail.png")
else:
    (VIS/"NO_POSITION_WRAP.txt").write_text("NEW REPLAY: no raw updated coordinate left [-1,1) in any of the 1500 point updates. No artificial jump example was generated.\n")

# Self-contained recorded-state viewer, not a model or integrator.
template=(BASE/"viewer_template.html").read_text(encoding="utf-8")
payload={"label":"NEW REPLAY","initial":P[0].tolist(),"events":events,
         "closest_event_id":3*(closest_step+1),
         "first_wrap_event_id":crossings[0]["event_id"] if crossings else None}
(VIS/"replay_viewer.html").write_text(template.replace("__RECORDED_DATA__",json.dumps(payload,separators=(",",":"))),encoding="utf-8")
print(json.dumps({k:summary[k] for k in ["position_wrap_event_count","position_wrap_events_by_point",
      "first_position_wrap","force_comparisons_with_nonzero_wrap","largest_native_step",
      "closest_simultaneous_pair","final_pair_distances","H_sign_changes","windows"]},indent=2))

