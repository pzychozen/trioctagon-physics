#!/usr/bin/env python3
"""
z_spike_diagnostic.py

Diagnose "spike / branch" behavior in Z trajectories by time-localizing rare
high-turning events (v_rec spikes) and exporting local windows for inspection.

This script is DISPLAY/DIAGNOSTIC only:
- does not change the model
- uses the same compute_recursive_velocity_geom() you already trust
"""

from __future__ import annotations

import argparse
import os
from dataclasses import asdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from provenance import make_run_meta
from model_core import ModelParams, ModelState, TriOctaPhaseLockModel
from constants_selector import default_k_triplet
from definitions import compute_recursive_velocity_geom, compute_jeff_series
from geometry_3d import history_Zvec_to_xyz


def run_triocta_once(
    seed: int,
    eps: float,
    g: float,
    k3_scale: float,
    dt: float,
    steps: int,
) -> dict:
    rng = np.random.default_rng(int(seed))

    # parameters
    k_vals = default_k_triplet(float(k3_scale))
    params = ModelParams(eps=float(eps), g=float(g), k_vals=k_vals)

    # provenance (stable hash)
    params_dict = {"seed": int(seed), "eps": float(eps), "g": float(g), "k3_scale": float(k3_scale), "dt": float(dt), "steps": int(steps)}
    meta = make_run_meta("3.7", int(seed), params_dict)

    # initial state in channel space
    Omega0 = rng.standard_normal(3) + 1j * rng.standard_normal(3)
    Omega0 /= np.linalg.norm(Omega0) + 1e-12

    state0 = ModelState(Omega0)
    model = TriOctaPhaseLockModel(params)
    hist = model.run(state0, n_steps=int(steps), dt=float(dt))

    # add canonical J_eff series for correlation plots
    hist = dict(hist)
    hist["J_eff"] = compute_jeff_series(hist)

    # attach meta
    hist["_meta"] = {"run_id": meta.run_id, "version": "3.7", **params_dict}
    return hist


def safe_xyz(hist: dict, z_key: str):
    try:
        return history_Zvec_to_xyz(hist, key=z_key)
    except Exception:
        # legacy fallback
        return history_Zvec_to_xyz(hist, key="Z_vec")


def pick_spikes(v: np.ndarray, mode: str, value: float) -> tuple[np.ndarray, float]:
    """
    Returns (spike_indices_in_v, threshold_used)
    v is length (steps-1) typically.
    """
    v = np.asarray(v, dtype=float)
    v = v[np.isfinite(v)]
    if v.size == 0:
        return np.array([], dtype=int), np.nan

    if mode == "pctl":
        thr = np.quantile(v, value)
    elif mode == "abs":
        thr = float(value)
    else:
        raise ValueError("mode must be pctl or abs")

    # use original series for indices
    # (keep spikes where v_rec >= thr and finite)
    return np.where(np.isfinite(v_rec_series) & (v_rec_series >= thr))[0], float(thr)


def write_outputs(
    hist: dict,
    z_key: str,
    include_dkappa: bool,
    outdir: str,
    spike_mode: str,
    spike_value: float,
    window: int,
    last_n_3d: int,
):
    os.makedirs(outdir, exist_ok=True)
    meta = hist.get("_meta", {})
    run_id = meta.get("run_id", "run_unknown")

    # time base
    steps = int(meta.get("steps", len(np.asarray(hist.get("kappa", [])))))
    dt = float(meta.get("dt", 1.0))
    t = np.arange(steps, dtype=float) * dt

    # Z trajectory
    xz, yz, zz = safe_xyz(hist, z_key=z_key)

    # v_rec (directional geometric velocity)
    v_rec = compute_recursive_velocity_geom(
        hist,
        z_key=z_key,
        w_kappa=(1.0 if include_dkappa else 0.0),
    )
    v_rec = np.asarray(v_rec, dtype=float)  # length ~ steps-1
    t_v = t[1:] if t.size >= 2 else np.arange(len(v_rec), dtype=float) * dt

    # store for spike picker scope
    global v_rec_series
    v_rec_series = v_rec

    # pick spikes
    if spike_mode == "pctl":
        spike_idx, thr = pick_spikes(v_rec, "pctl", spike_value)
        spike_tag = f"pctl{int(spike_value*100)}"
    else:
        spike_idx, thr = pick_spikes(v_rec, "abs", spike_value)
        spike_tag = f"abs{spike_value:g}"

    # ---- CSV: per-step core series (for later plotting) ----
    df_series = pd.DataFrame({
        "i": np.arange(len(t), dtype=int),
        "t": t,
        "Zx": np.asarray(xz, float),
        "Zy": np.asarray(yz, float),
        "Zz": np.asarray(zz, float),
    })
    # align v_rec (t[1:])
    v_full = np.full(len(t), np.nan, dtype=float)
    v_full[1:1+len(v_rec)] = v_rec[:len(t)-1]
    df_series["v_rec"] = v_full

    # J_eff if present
    if "J_eff" in hist:
        J = np.asarray(hist["J_eff"], dtype=float)
        if J.size == len(t):
            df_series["J_eff"] = J
        elif J.size == len(t) - 1:
            tmp = np.full(len(t), np.nan, dtype=float)
            tmp[1:] = J
            df_series["J_eff"] = tmp

    series_path = os.path.join(outdir, f"{run_id}_{z_key}_series.csv")
    df_series.to_csv(series_path, index=False)

    # ---- CSV: spike windows ----
    rows = []
    for j, idx in enumerate(spike_idx):
        # idx indexes v_rec (t_v), corresponds to step i = idx+1 in t
        center_i = int(idx + 1)
        lo = max(0, center_i - window)
        hi = min(len(t) - 1, center_i + window)
        for i in range(lo, hi + 1):
            rows.append({
                "spike_id": int(j),
                "center_i": int(center_i),
                "i": int(i),
                "t": float(t[i]),
                "v_rec": float(v_full[i]) if np.isfinite(v_full[i]) else np.nan,
                "Zx": float(xz[i]),
                "Zy": float(yz[i]),
                "Zz": float(zz[i]),
            })
    df_spikes = pd.DataFrame(rows)
    spikes_path = os.path.join(outdir, f"{run_id}_{z_key}_spikes_{spike_tag}_win{window}.csv")
    df_spikes.to_csv(spikes_path, index=False)

    # ---- Plot 1: v_rec with spike markers ----
    plt.figure()
    plt.plot(t_v, v_rec, lw=1.2)
    if spike_idx.size:
        plt.scatter(t_v[spike_idx], v_rec[spike_idx], s=18)
    plt.axhline(thr, linestyle="--", linewidth=1.0)
    plt.xlabel("time")
    plt.ylabel("v_rec (geom, dir)")
    plt.title(f"v_rec spikes ({z_key}) | thr={thr:.6g} | n={len(spike_idx)}")
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, f"{run_id}_{z_key}_vrec_spikes.png"), dpi=200)
    plt.close()

    # ---- Plot 2: 3D scatter colored by time, spikes highlighted ----
    from mpl_toolkits.mplot3d import Axes3D  # noqa

    N = int(last_n_3d) if last_n_3d > 0 else len(t)
    lo3 = max(0, len(t) - N)

    xs = np.asarray(xz[lo3:], float)
    ys = np.asarray(yz[lo3:], float)
    zs = np.asarray(zz[lo3:], float)
    ts = np.asarray(t[lo3:], float)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(xs, ys, zs, c=ts, s=6)
    fig.colorbar(sc, ax=ax, shrink=0.6, pad=0.08)

    # highlight spike points (convert spike center indices to global i)
    if spike_idx.size:
        spike_i = spike_idx + 1  # align to t
        spike_i = spike_i[(spike_i >= lo3) & (spike_i < len(t))]
        ax.scatter(np.asarray(xz[spike_i]), np.asarray(yz[spike_i]), np.asarray(zz[spike_i]), s=40)

    ax.set_xlabel("Z1")
    ax.set_ylabel("Z2")
    ax.set_zlabel("Z3")
    ax.set_title(f"Z trajectory ({z_key}) | last {N} steps | spikes highlighted")
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, f"{run_id}_{z_key}_Z3_time_scatter.png"), dpi=200)
    plt.close()

    # ---- Text summary ----
    with open(os.path.join(outdir, f"{run_id}_{z_key}_summary.txt"), "w", encoding="utf-8") as f:
        f.write(f"run_id: {run_id}\n")
        for k, v in meta.items():
            f.write(f"{k}: {v}\n")
        f.write(f"\nZ key: {z_key}\n")
        f.write(f"include_dkappa: {include_dkappa}\n")
        f.write(f"spike_mode: {spike_mode}\n")
        f.write(f"threshold: {thr}\n")
        f.write(f"n_spikes: {len(spike_idx)}\n")
        if len(spike_idx):
            f.write(f"first_spike_t: {t_v[spike_idx[0]]}\n")
            f.write(f"last_spike_t: {t_v[spike_idx[-1]]}\n")

    print(f"[ok] wrote:\n  {series_path}\n  {spikes_path}\n  {outdir}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--eps", type=float, required=True)
    ap.add_argument("--g", type=float, required=True)
    ap.add_argument("--k3", type=float, required=True, help="k3_scale")
    ap.add_argument("--dt", type=float, required=True)
    ap.add_argument("--steps", type=int, default=2000)

    ap.add_argument("--z_key", type=str, default="Z_total", choices=["Z_total", "Z_macro", "Z_chiral"])
    ap.add_argument("--include_dkappa", action="store_true")

    ap.add_argument("--spike_mode", choices=["pctl", "abs"], default="pctl")
    ap.add_argument("--spike_value", type=float, default=0.99, help="percentile (0..1) if pctl, else absolute threshold")
    ap.add_argument("--window", type=int, default=25, help="+/- window (steps) around spike center")
    ap.add_argument("--last_n_3d", type=int, default=500, help="plot last N points in 3D (0 = all)")

    ap.add_argument("--outdir", type=str, default="z_spike_out")
    args = ap.parse_args()

    hist = run_triocta_once(
        seed=args.seed,
        eps=args.eps,
        g=args.g,
        k3_scale=args.k3,
        dt=args.dt,
        steps=args.steps,
    )

    write_outputs(
        hist=hist,
        z_key=args.z_key,
        include_dkappa=args.include_dkappa,
        outdir=args.outdir,
        spike_mode=args.spike_mode,
        spike_value=args.spike_value,
        window=args.window,
        last_n_3d=args.last_n_3d,
    )


if __name__ == "__main__":
    main()
