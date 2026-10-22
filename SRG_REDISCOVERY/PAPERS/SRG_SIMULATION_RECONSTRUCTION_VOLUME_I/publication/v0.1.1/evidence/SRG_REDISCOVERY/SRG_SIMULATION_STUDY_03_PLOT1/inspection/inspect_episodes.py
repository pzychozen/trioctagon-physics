"""Local windows of original numerical records; no state evolution."""
from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
def read(fn):
    with (ROOT/"originals"/fn).open(newline="") as f:
        r=csv.reader(f);next(r);return np.array(list(r),float).reshape(-1,8,11)
def H(t):
    return 2*np.exp(-.5*t)*np.cos(t)+np.exp(-.3*t)*np.sin(t)+1.5*np.exp(-.7*t)+np.exp(-.4*t)
logs={"A":read("PLOT_1_tetrahedral_states_20250712_015421.csv"),
      "B":read("tetrahedral_states_20250712_015647.csv")}
records=[]
for label,i,start,end,reason in [
    ("A",4,10,19,"first mode flip"),
    ("B",5,5,15,"first mode flip"),
    ("B",7,400,420,"three coordinate seam crossings"),
    ("A",4,1003,1007,"strong turn when frame clock restarts"),
]:
    a=logs[label];x=a[:,:,2:5];v=a[:,:,5:8]
    for q in range(start,end+1):
        mixed=np.concatenate((x[q,:i],x[q-1,i:]),axis=0)
        c=mixed.mean(axis=0);d=(c-x[q-1,i]+5)%10-5
        radial=np.dot(v[q,i],d)/np.linalg.norm(d)
        cos=np.dot(v[q,i],v[q-1,i])/(np.linalg.norm(v[q,i])*np.linalg.norm(v[q-1,i]))
        records.append({"log":label,"episode":reason,"callback":q,"body":i,
            "csv_line":8*q+2+i,"label":int(a[q,0,0]),"mode":int(a[q,i,10]),
            "H":float(H(.1*a[q,0,0])),"GRF":float(a[q,0,9]),
            "position":x[q,i].tolist(),"velocity":v[q,i].tolist(),
            "mixed_centroid":c.tolist(),"wrapped_centroid_displacement":d.tolist(),
            "speed":float(np.linalg.norm(v[q,i])),"radial_outgoing_velocity":float(radial),
            "consecutive_velocity_cosine":float(cos)})
(ROOT/"analysis/episode_records.json").write_text(json.dumps(records,indent=2),encoding="utf-8")
a=logs["B"];q=np.arange(400,421)
fig,axs=plt.subplots(3,1,figsize=(11,8),sharex=True,layout="constrained")
axs[0].plot(q,a[q,7,2],".-",color="#be185d");axs[0].set_ylabel("Recorded X in [0,10)")
axs[1].plot(q,a[q,7,5],".-",color="#0369a1");axs[1].axhline(0,color="gray",lw=.7);axs[1].set_ylabel("Recorded VX")
axs[2].step(q,a[q,7,10],where="mid",label="Rule_State");axs[2].set_yticks([0,1]);axs[2].set_ylabel("Binary mode")
for ax in axs:
    for event in (409,414,418):ax.axvline(event,ls=":",color="#999999")
    ax.grid(alpha=.2)
axs[2].set_xlabel("Original log B callback index, not the repeated Step label")
fig.suptitle("Original log B, body 7: repeated seam crossings with an unchanged mode")
fig.savefig(ROOT/"visuals/B_body7_seam_window.png",dpi=140);plt.close(fig)
# Compare chronology to the historical chart's folded Step axis using source
# records only. This diagnoses a chart construction, never changes raw records.
q=np.arange(len(a))
fig,axs=plt.subplots(3,1,figsize=(11,9),sharex=True,layout="constrained")
for dim,ax in enumerate(axs):
    ax.plot(a[:,0,0],a[:,7,2+dim],color="orange")
    for ev in (409,414,418):ax.axvline(ev,color="red",ls="--",lw=1)
    ax.set_ylabel("XYZ"[dim]);ax.grid(alpha=.2)
axs[-1].set_xlabel("Stored Step for curves; callback indices for red markers (mixed clocks)")
fig.suptitle("DERIVED diagnostic from original log B: reproducing the folded-axis construction")
fig.savefig(ROOT/"visuals/B_historical_axis_diagnostic.png",dpi=140);plt.close(fig)
for label,body in [("A",4),("B",5)]:
    print(label,"first switch window",json.dumps([{k:r[k] for k in
        ["callback","csv_line","label","mode","H","speed","radial_outgoing_velocity","consecutive_velocity_cosine"]}
        for r in records if r["log"]==label and r["body"]==body and r["episode"]=="first mode flip"],indent=2))
print("B body 7 mode in 400..420:",np.unique(a[400:421,7,10]).tolist())
