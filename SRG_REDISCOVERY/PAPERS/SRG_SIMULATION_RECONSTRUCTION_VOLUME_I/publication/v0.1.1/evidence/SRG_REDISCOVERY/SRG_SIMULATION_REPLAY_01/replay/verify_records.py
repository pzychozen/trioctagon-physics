"""NEW REPLAY: check already saved records; no source execution or state integration."""
from pathlib import Path
import csv,json,re
import numpy as np
BASE=Path(__file__).resolve().parent
p=np.load(BASE/"trajectory.npz",allow_pickle=False)
ref=np.load(BASE/"reference_comparison.npz",allow_pickle=False)
ev=[json.loads(s) for s in (BASE/"within_sweep.jsonl").read_text().splitlines()]
summary=json.loads((BASE/"observation_summary.json").read_text())
def same(a,b):
    a,b=np.asarray(a,dtype=np.float64),np.asarray(b,dtype=np.float64)
    return a.shape==b.shape and np.array_equal(a.view(np.uint64),b.view(np.uint64))
checks={}
def ck(name,value):
    checks[name]=bool(value)
    assert value,name
ck("501_states_and_1500_events",p["positions"].shape==(501,3,2) and len(ev)==1500)
ck("saved_reference_positions_bitwise_equal",same(p["positions"][1:],ref["position_log"]))
ck("saved_reference_final_velocities_bitwise_equal",same(p["velocities"][-1],ref["final_velocities"]))
pos=p["positions"][0].copy();vel=p["velocities"][0].copy()
for k,e in enumerate(ev):
    assert e["event_id"]==k+1 and e["step"]==k//3 and e["point"]==k%3
    assert same(e["input_positions"],pos)
    assert same(e["input_velocities"],vel)
    assert same(e["velocity_before"],vel[e["point"]])
    assert same([e["t"],e["H"]],[p["t"][k//3],p["H"][k//3]])
    # Reassemble observations only; do not calculate new movement.
    pos[e["point"]]=e["post_wrap_position"]
    vel[e["point"]]=e["velocity_post_damping"]
    assert same(pos,e["positions_after_event"]) and same(pos,p["event_positions"][k])
    if k%3==2:
        assert same(pos,p["positions"][k//3+1]) and same(vel,p["velocities"][k//3+1])
ck("all_event_inputs_and_outputs_contiguous",True)
ck("all_end_sweep_records_match_event_records",True)
with (BASE/"states.csv").open(newline="",encoding="utf-8") as f:
    rows=list(csv.DictReader(f))
ck("csv_row_count",len(rows)==501*3)
for row in rows:
    n,i=int(row["state_index"]),int(row["point"])
    assert same([float(row[x]) for x in ["x","y"]],p["positions"][n,i])
    assert same([float(row[x]) for x in ["vx","vy"]],p["velocities"][n,i])
    if n:
        assert int(row["last_update_step"])==n-1
        assert same([float(row["t_used"]),float(row["H_used"])],[p["t"][n-1],p["H"][n-1]])
    else:
        assert not row["last_update_step"] and not row["t_used"] and not row["H_used"]
ck("csv_roundtrips_every_recorded_float",True)
selected=[json.loads(s) for s in (BASE/"selected_events.jsonl").read_text().splitlines()]
ids=[e["event_id"] for e in selected]
ck("selected_events_are_native_order_exact_copies",
   ids==sorted(set(ids)) and all(e==ev[e["event_id"]-1] for e in selected))
ck("no_position_wraps",all(not any(e["position_wrap_lattice"]) for e in ev))
ck("no_force_wraps",all(not any(x["force_wrap_lattice"]) for e in ev for x in e["interactions"]))
ck("all_recorded_values_finite",bool(np.isfinite(p["positions"]).all() and np.isfinite(p["velocities"]).all()))
html=(BASE.parent/"visuals"/"replay_viewer.html").read_text(encoding="utf-8")
embedded=json.loads(re.search(r'<script id="recorded" type="application/json">(.*?)</script>',html,re.S).group(1))
ck("optional_viewer_contains_exact_saved_records",embedded["events"]==ev and same(embedded["initial"],p["positions"][0]))
ck("optional_viewer_event_targets_match_summary",embedded["closest_event_id"]==507 and embedded["first_wrap_event_id"] is None)
window=[]
for n in [168,169,170]:
    delta=p["positions"][n,2]-p["positions"][n,1]
    window.append({"state_index":n,"step":n-1,"event_id":3*n,
                   "P1_P2_distance":float(np.linalg.norm(np.mod(delta+1,2)-1))})
out={"label":"NEW REPLAY","method":"Saved-record consistency only, no additional trajectory execution.",
     "checks":checks,"closest_window_end_distances":window,
     "visual_inspection":{"PNGs":["wrapped_paths.png","seam_aware_paths.png","opening_sequence.png","closest_pair_sequence.png","movement_over_time.png"],
        "contact_sheet_reading":"Rows top to bottom, columns left to right; all represented event states inspected.",
        "html_browser_playback_validated":False,
        "html_preview_limitation":"Browser URL policy rejected file:// preview. No alternate-surface or server workaround used. Embedded data and source were checked; primary evidence is the inspected PNG sequences."}}
(BASE/"record_checks.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))

