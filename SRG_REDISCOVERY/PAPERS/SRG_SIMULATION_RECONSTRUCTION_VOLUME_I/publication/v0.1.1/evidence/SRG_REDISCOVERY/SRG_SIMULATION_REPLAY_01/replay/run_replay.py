"""NEW REPLAY: one seed-0 instrumented run plus one identical-seed fidelity run.
Run in CMD after conda activate torment. Refuses to repeat in an existing output.
Authoritative originals are never imported. The sandbox source bytes are unchanged.
"""
from pathlib import Path
import os
import sys
import json
import csv
import platform
import hashlib
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
# Keep any renderer cache writes within the new task directory.
os.environ["MPLCONFIGDIR"] = str(BASE / "mplconfig")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SOURCE = BASE / "source" / "recursive_attractor.py"
EXPECTED = "847819ec381e200d9008395175342ec138e52ab3180a4f599b4db1cb91ae42d3"

def write_json(name, value):
    (BASE/name).write_text(json.dumps(value, indent=2, allow_nan=False)+"\n", encoding="utf-8")

def H(t):
    a1, b1 = 2.0, 0.5
    alpha2, b2 = 1.0, 0.3
    lambda1, omega1 = 1.5, 0.7
    lambda2, omega2 = 1.0, 0.4
    return (
        a1 * np.exp(-b1 * t) * np.cos(t)
        + alpha2 * np.exp(-b2 * t) * np.sin(t)
        + lambda1 * np.exp(-omega1 * t)
        + lambda2 * np.exp(-omega2 * t)
    )

def RPCO(v):
    return v / (1 + np.log1p(np.abs(v)))

def TGMO(pos):
    return np.mod(pos + 1.0, 2.0) - 1.0

def bits_equal(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return (a.shape == b.shape and a.dtype == b.dtype
            and np.array_equal(a.view(np.uint64), b.view(np.uint64)))

def first_divergence(a, b):
    mismatch = np.argwhere(a.view(np.uint64) != b.view(np.uint64))
    if not len(mismatch):
        return None
    loc = tuple(int(x) for x in mismatch[0])
    return {"index":list(loc),"instrumented":float(a[loc]),"reference":float(b[loc]),
            "instrumented_hex":float(a[loc]).hex(),"reference_hex":float(b[loc]).hex()}

def main():
    source_bytes = SOURCE.read_bytes()
    assert hashlib.sha256(source_bytes).hexdigest() == EXPECTED
    if (BASE/"trajectory.npz").exists():
        raise RuntimeError("Existing trajectory: no repeat execution authorized here.")
    # Exclusive marker also prevents a silent rerun after an interrupted execution.
    with (BASE/"execution_receipt.json").open("x", encoding="utf-8") as f:
        json.dump({"status":"started","label":"NEW REPLAY","seed":0}, f)
    receipt = {"label":"NEW REPLAY","seed":0,"started_utc":datetime.now(timezone.utc).isoformat(),
               "instrumented_sweeps_completed":0,"reference_sweeps_completed":0}
    write_json("environment.json",{
        "label":"NEW REPLAY","interpreter":sys.executable,"python":sys.version,
        "numpy":np.__version__,"matplotlib":matplotlib.__version__,
        "platform":platform.platform(),"float_dtype":"float64",
        "rng":"legacy MT19937 / RandomState(0)","matplotlib_backend":matplotlib.get_backend(),
        "source_sha256":EXPECTED,"source_lines":len(source_bytes.decode("utf-8").splitlines()),
        "show_handling":"Agg backend and temporary plt.show no-op for reference source; figure closed without saving.",
        "original_source_imported_or_executed":False,
        "sandbox_source_executed_for_reference":True
    })

    timesteps = 500
    dt = 0.05
    num_attractors = 3
    positions = np.random.RandomState(0).rand(num_attractors, 2) * 2 - 1
    velocities = np.zeros((num_attractors, 2))
    write_json("initial_state.json",{
        "label":"NEW REPLAY","seed":0,"investigator_selected_seed":True,
        "positions":positions.tolist(),"velocities":velocities.tolist(),
        "position_float_hex":[[float(x).hex() for x in row] for row in positions],
        "state_index":0,"last_update_step":None,"last_update_t":None,"last_update_H":None
    })
    states_p = [positions.copy()]
    states_v = [velocities.copy()]
    position_log = []
    clock_t, clock_h, events = [], [], []

    # Same operation order, scalar constants, NumPy types and helper expressions
    # as the historical source. Observations are copies and never feed back.
    for step in range(timesteps):
        t = step * dt
        h_val = H(t)
        clock_t.append(t)
        clock_h.append(h_val)
        new_positions = []
        for i in range(num_attractors):
            obs = {"label":"NEW REPLAY","event_id":len(events)+1,"step":step,
                   "sweep_number":step+1,"point":i,"t":float(t),"H":float(h_val),
                   "input_positions":positions.copy().tolist(),
                   "input_velocities":velocities.copy().tolist(),"interactions":[]}
            net_force = np.zeros(2)
            for j in range(num_attractors):
                if i == j:
                    continue
                diff = positions[j] - positions[i]
                raw_diff = diff.copy()
                diff = TGMO(diff)
                contribution = diff / (np.linalg.norm(diff) + 1e-3)
                net_force += contribution
                obs["interactions"].append({
                    "other_point":j,"raw_diff":raw_diff.tolist(),"wrapped_diff":diff.copy().tolist(),
                    "contribution":contribution.copy().tolist(),
                    "force_wrap_lattice":np.floor((raw_diff+1.0)/2.0).astype(int).tolist()
                })
            obs["net_force"] = net_force.copy().tolist()
            obs["velocity_before"] = velocities[i].copy().tolist()
            velocities[i] += dt * h_val * net_force
            obs["velocity_pre_damping"] = velocities[i].copy().tolist()
            velocities[i] = RPCO(velocities[i])
            obs["velocity_post_damping"] = velocities[i].copy().tolist()
            # These duplicate arithmetic observations are not dynamical inputs.
            obs["native_displacement"] = (dt*velocities[i]).tolist()
            raw_position = positions[i] + dt*velocities[i]
            obs["raw_updated_position"] = raw_position.tolist()
            obs["position_wrap_lattice"] = np.floor((raw_position+1.0)/2.0).astype(int).tolist()
            positions[i] = TGMO(positions[i] + dt * velocities[i])
            new_positions.append(positions[i].copy())
            obs["post_wrap_position"] = positions[i].copy().tolist()
            obs["positions_after_event"] = positions.copy().tolist()
            obs["screen_displacement"] = (
                positions[i]-np.array(obs["input_positions"][i])).tolist()
            events.append(obs)
        position_log.append(np.array(new_positions))
        states_p.append(positions.copy())
        states_v.append(velocities.copy())

    position_log = np.array(position_log)
    states_p, states_v = np.array(states_p), np.array(states_v)
    clock_t, clock_h = np.array(clock_t), np.array(clock_h)
    np.savez_compressed(BASE/"trajectory.npz",
        label=np.array("NEW REPLAY"),positions=states_p,velocities=states_v,
        state_index=np.arange(501),step=np.arange(500),t=clock_t,H=clock_h,
        event_id=np.arange(1,1501),
        event_positions=np.array([e["positions_after_event"] for e in events]),
        event_native_displacement=np.array([e["native_displacement"] for e in events]),
        event_position_wrap_lattice=np.array([e["position_wrap_lattice"] for e in events]))
    with (BASE/"within_sweep.jsonl").open("w",encoding="utf-8",newline="\n") as f:
        for e in events:
            f.write(json.dumps(e, separators=(",",":"), allow_nan=False)+"\n")
    with (BASE/"states.csv").open("w",encoding="utf-8",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["label","state_index","last_update_step","t_used","H_used",
                         "point","x","y","vx","vy"])
        for n in range(501):
            for i in range(3):
                timing = ["","",""] if n == 0 else [
                    n-1,format(clock_t[n-1],".17g"),format(clock_h[n-1],".17g")]
                writer.writerow(["NEW REPLAY",n,*timing,i,
                    *(format(x,".17g") for x in (*states_p[n,i],*states_v[n,i]))])
    receipt["instrumented_sweeps_completed"] = 500
    receipt["instrumented_events"] = 1500
    receipt["status"] = "instrumented data saved; reference next"
    write_json("execution_receipt.json",receipt)

    # Sole permitted fidelity execution: byte-identical sandbox source, same seed.
    np.random.seed(0)
    namespace = {"__name__":"__sandbox_reference__","__file__":str(SOURCE)}
    saved_show = plt.show
    plt.show = lambda *args, **kwargs: None
    try:
        exec(compile(source_bytes, str(SOURCE), "exec"), namespace)
    finally:
        plt.show = saved_show
        plt.close("all")
    ref_p = namespace["position_log"]
    ref_v = namespace["velocities"]
    np.savez_compressed(BASE/"reference_comparison.npz",
                        label=np.array("NEW REPLAY / IDENTICAL-SEED FIDELITY CHECK"),
                        position_log=ref_p,final_velocities=ref_v)
    match_p, match_v = bits_equal(position_log,ref_p), bits_equal(velocities,ref_v)
    validation = {"label":"NEW REPLAY","source_sha256":EXPECTED,
        "position_snapshots_compared":500,"position_float64_values_compared":3000,
        "position_snapshots_bitwise_equal":match_p,"final_velocity_float64_values_compared":6,
        "final_velocities_bitwise_equal":match_v,
        "first_position_divergence":first_divergence(position_log,ref_p),
        "first_final_velocity_divergence":first_divergence(velocities,ref_v),
        "instrumentation_observations_feed_back":False,
        "reference_method":"exec unchanged sandbox source bytes after np.random.seed(0); Agg and plt.show no-op only.",
        "faithful_in_this_environment":match_p and match_v}
    write_json("equivalence.json",validation)
    receipt.update(reference_sweeps_completed=500,reference_seed=0,
                   sampled_initial_configurations=1,status="complete",
                   fidelity_passed=match_p and match_v)
    write_json("execution_receipt.json",receipt)
    if not (match_p and match_v):
        raise RuntimeError("Fidelity mismatch: stop, inspect first divergence; no faithful replay claim.")
    print(json.dumps({"initial_positions":states_p[0].tolist(),"final_positions":states_p[-1].tolist(),
          "snapshots_bitwise_equal":match_p,"final_velocities_bitwise_equal":match_v,
          "instrumented_sweeps":500,"reference_sweeps":500,"point_events":len(events)},indent=2))

if __name__ == "__main__":
    main()

