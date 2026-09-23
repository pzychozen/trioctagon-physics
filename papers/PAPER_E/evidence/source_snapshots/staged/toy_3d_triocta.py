# toy_3d.py
# ============================================================
# 3D geometry viewer for the TriOcta phase-locking model
# (Toy_Model v3.3)
#
# Sliders:
#   - eps, g, k3_scale, noise_sigma
#   - trail_len (how many steps of the trajectory to display)
#
# Plots:
#   - 3D torus with the 3-node Ω(t) trajectory
#   - J_eff(t) vs time
#   - Corridor occupancy wheel (same logic as toy_lab)
#
# This is TriOcta-focused, complementary to:
#   - toy_lab.py  (2D + wheel)
#   - toy_ui.py   (RSB recursion + coupling)
# ============================================================

import csv
import datetime
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# ------------------------------------------------------------
# Launch-boundary shim (PEP 366)
# ------------------------------------------------------------
# This viewer has historically been launched two ways:
#     python -m kernel.toy_3d_triocta      (from the repository root)
#     python toy_3d_triocta.py             (from inside kernel/)
#
# The second form leaves __package__ empty, so the package-relative imports
# below would raise "attempted relative import with no known parent package".
# Setting __package__ and putting the repository root on sys.path makes both
# forms resolve to the same kernel.* module objects, which also prevents a
# sibling being imported twice under two different names.
#
# This changes import resolution only. No model equation, parameter, output
# path or plotting behaviour is affected.
if __package__ in (None, ""):
    import sys as _sys

    _repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _repo_root not in _sys.path:
        _sys.path.insert(0, _repo_root)
    __package__ = "kernel"
    import kernel  # noqa: F401  (initialise the package so relative imports resolve)

from .provenance import make_run_meta

VERSION = "3.5"


from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from mpl_toolkits.mplot3d.art3d import Line3DCollection

from .model_core import ModelParams, ModelState, TriOctaPhaseLockModel
from .constants_selector import default_k_triplet
from .physics_sampler import sample_physics_observables
from .rsb_model import RSBParams, RSBModel
from .definitions import (
    analyze_rsb_history,
    estimate_z_stabilization_time,
    compute_jeff_series,
    count_sign_flips,
    estimate_chirality_commit_time,
    vrec_geom_direction,
)
from .geometry_3d import history_Zvec_to_xyz


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------


# --- Compatibility / canonical metric helpers ---
def _vrec_geom(history: dict, z_key: str = "Z_total") -> np.ndarray:
    """Preferred geometric v_rec (direction drift on selected Z component)."""
    try:
        return vrec_geom_direction(history, z_key=z_key)
    except Exception:
        # Fallback to older name if present in definitions.py (pre-contract)
        try:
            from .definitions import compute_recursive_velocity_geom  # type: ignore
            return _vrec_geom(history, z_key=z_key)
        except Exception:
            return np.asarray([], dtype=float)

def _jeff_series(history: dict, obs: dict | None = None) -> np.ndarray:
    """Preferred Jeff series: use obs['J_eff'] if provided; else derive from history."""
    try:
        if obs is not None and "J_eff" in obs and obs["J_eff"] is not None:
            return np.asarray(obs["J_eff"], dtype=float)
    except Exception:
        pass
    return compute_jeff_series(history)


def tri_to_rsb_params(tri_obs, base_alpha: float = 0.6):
    """
    Map the TriOcta physics (mainly J_eff) into effective RSB parameters.

    tri_obs: dict returned by sample_physics_observables(history)
    base_alpha: baseline collapse strength for the RSB engine

    Returns (alpha_eff, mu_eff, gamma_eff).
    """
    if tri_obs is None or "J_eff" not in tri_obs:
        return base_alpha, 0.6, 0.2

    J = np.asarray(tri_obs["J_eff"])
    if J.size == 0:
        return base_alpha, 0.6, 0.2

    # overall chirality strength
    J_abs = np.abs(J)
    J_mean = float(J_abs.mean())
    J_max = float(J_abs.max()) if J_abs.max() > 0 else 1.0
    J_norm = np.clip(J_mean / J_max, 0.0, 1.0)

    # plateau sign → chirality tilt
    if J.size > 20:
        J_plateau = float(J[-20:].mean())
    else:
        J_plateau = float(J.mean())
    J_sign = float(np.sign(J_plateau)) if J_plateau != 0 else 0.0

    alpha_eff = base_alpha * (0.3 + 0.7 * J_norm)
    mu_eff    = 0.6 + 0.2 * J_sign
    gamma_eff = 0.2 * (0.5 + 0.5 * J_norm)

    return alpha_eff, mu_eff, gamma_eff


def run_triocta(
    eps: float,
    g: float,
    k3_scale: float,
    noise_sigma: float,
    n_steps: int = 300,
    dt: float = 0.05,
    seed: int = 42,
    do_rsb: bool = True,
    rsb_steps: int = 300,
):
    """
    Run a single TriOcta trajectory and (optionally) one coupled RSB run.

    Returns:
        history      : dict with TriOcta time series
        obs          : dict with TriOcta observables (J_eff, etc.)
        params       : ModelParams used for TriOcta
        rsb_results  : dict with RSB info, or None if do_rsb=False

    Expects model_core.TriOctaPhaseLockModel.run(...) to produce a history
    dict that includes:
        - "t"
        - "kappa"
        - "z"
        - "Omega"     (complex 3-vector per step)
        - "phi_index" (corridor index per step)
    If your key for Ω(t) differs, just change the 'Omega' usage elsewhere.
    """
    rng = np.random.default_rng(seed)

    # --- k wells (same style as toy_lab.py) ---
    k_vals = default_k_triplet(mode="theta_soft", alpha=1.0).copy()
    k_vals[2] *= k3_scale

    params = ModelParams(
        eps=eps,
        g=g,
        k_vals=k_vals,
    )

    params_dict = {
        "eps": float(eps),
        "g": float(g),
        "k3_scale": float(k3_scale),
        "noise_sigma": float(noise_sigma),
        "n_steps": int(n_steps),
        "dt": float(dt),
        "do_rsb": bool(do_rsb),
        "rsb_steps": int(rsb_steps),
        "k_vals": [float(x) for x in np.asarray(k_vals).ravel().tolist()],
    }
    meta = make_run_meta(VERSION, int(seed), params_dict)

    # --- initial Ω₀ (small random complex vector on unit sphere) ---
    Omega0 = 0.1 * (rng.standard_normal(3) + 1j * rng.standard_normal(3))
    Omega0 /= np.linalg.norm(Omega0) + 1e-12

    state0 = ModelState(Omega=Omega0)
    model = TriOctaPhaseLockModel(params)

    # --- main TriOcta evolution ---
    history = model.run(state0, n_steps=n_steps, dt=dt)
    obs = sample_physics_observables(history)

    # --- optional measurement-level noise on kappa, z, J_eff ---
    if noise_sigma > 0.0:
        kappa = np.asarray(history["kappa"])
        z = np.asarray(history["z"])
        J = np.asarray(obs["J_eff"])

        kappa_noisy = kappa + noise_sigma * rng.standard_normal(kappa.shape)
        z_noisy = z + noise_sigma * rng.standard_normal(z.shape)
        J_noisy = J + noise_sigma * rng.standard_normal(J.shape)

        history = dict(history)
        history["kappa"] = kappa_noisy
        history["z"] = z_noisy

        obs = dict(obs)
        obs["J_eff"] = J_noisy

    # --- optional coupled RSB run (for band overlay, etc.) ---
    rsb_results = None
    if do_rsb:
        base_alpha = 0.6  # can later become a slider
        alpha_eff, mu_eff, gamma_eff = tri_to_rsb_params(obs, base_alpha)

        rsb_params = RSBParams(
            kappa_L=0.02,
            kappa_S=0.30,
            mu=mu_eff,
            gamma=gamma_eff,
            eta=0.005,
            alpha=alpha_eff,
        )

        rsb_model = RSBModel(rsb_params)
        rsb_rng = np.random.default_rng(int(seed) + 1)
        psi_hist = rsb_model.run(n_steps=rsb_steps, rng=rsb_rng, seed=None)

        rsb_stats = analyze_rsb_history(
            psi_hist,
            chan_axis=1,
            phase_axis=2,
            hel_axis=3,
            dark_channels=(1, 2),
            verbose=False,
            seed=seed + 1,
        )

        band_series = rsb_stats.get("band_energy_series", None)
        if band_series is not None:
            band_series = np.asarray(band_series)
            if band_series.ndim == 2 and band_series.size > 0:
                E_final = band_series[-1]   # shape (M,)
            else:
                E_final = None
        else:
            E_final = None

        rsb_results = {
            "params": rsb_params,
            "psi_hist": psi_hist,
            "stats": rsb_stats,
            "E_final": E_final,
        }

    history = dict(history)
    history["_meta"] = {
        "run_id": meta.run_id,
        "seed": meta.seed,
        "version": meta.version,
        "timestamp_utc": meta.timestamp_utc,
    }
    if rsb_results is not None and isinstance(rsb_results, dict):
        rsb_results = dict(rsb_results)
        rsb_results["_meta"] = {
            "parent_run_id": meta.run_id,
            "seed": int(seed) + 1,
            "version": meta.version,
        }
    return history, obs, params, rsb_results


def embed_on_torus(omega_hist: np.ndarray,
                   R: float = 2.0,
                   r0: float = 0.6,
                   mag_scale: float = 0.4):
    """
    Embed Ω_j(t) (shape: n_steps × 3 complex) onto a 3D torus.

    Node index j = 0,1,2:
      → fixed azimuthal anchors φ_j = 0, 2π/3, 4π/3

    For each node j and timestep t:
      θ_j(t)  = arg(Ω_j(t))
      ρ_j(t)  = r0 * (1 + mag_scale * log1p(|Ω_j(t)|))

      x = (R + ρ cos θ) cos φ_j
      y = (R + ρ cos θ) sin φ_j
      z =  ρ sin θ

    Returns:
      x, y, z arrays of shape (3, n_steps)
    """
    n_steps, n_nodes = omega_hist.shape
    assert n_nodes == 3, "TriOcta viewer assumes 3-node system."

    phi_nodes = np.linspace(0, 2 * np.pi, 4, endpoint=True)[:3]  # 0, 2π/3, 4π/3

    x = np.zeros((n_nodes, n_steps))
    y = np.zeros((n_nodes, n_steps))
    z = np.zeros((n_nodes, n_steps))

    for j in range(n_nodes):
        omega_j = omega_hist[:, j]
        theta = np.angle(omega_j)
        mag = np.abs(omega_j)
        rho = r0 * (1.0 + mag_scale * np.log1p(mag))

        phi = phi_nodes[j]

        x[j, :] = (R + rho * np.cos(theta)) * np.cos(phi)
        y[j, :] = (R + rho * np.cos(theta)) * np.sin(phi)
        z[j, :] = rho * np.sin(theta)

    return x, y, z

def compute_phi_index(Omega, n_corridors: int = 12) -> int:
    """
    Reconstruct SRG corridor index from complex 3-node state Omega.
    Uses the mean phase, same as toy_lab.
    """
    ang = np.angle(np.mean(Omega)) % (2 * np.pi)
    corridor_width = 2 * np.pi / n_corridors
    return int(ang // corridor_width)

def detect_meta_shell_time(t, Z, window_frac=0.1, z_min=0.05):
    n = len(Z)
    w = max(5, int(window_frac * n))
    for i in range(n - w):
        seg = Z[i:i+w]
        if np.mean(seg) > z_min:
            return t[i]
        if np.mean(seg) < -z_min:
            return t[i]
    return np.nan

def dump_timeseries_csv(history, obs, tag="auto"):
    """
    Dump time series needed for meta-shell diagnostics:
    t, Z(t), J_eff(t), phi_index
    """
    t = np.asarray(history["t"])
    z = np.asarray(history["z"])
    phi = np.asarray(history["phi_index"], dtype=int)
    J = np.asarray(obs["J_eff"])

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"timeseries_{tag}_{ts}.csv"

    outdir = "outputs"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, fname)

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["t", "Z", "J_eff", "phi_index"])
        for i in range(len(t)):
            writer.writerow([t[i], z[i], J[i], phi[i]])

    print(f"[auto-dump] saved time series → {path}")


# ------------------------------------------------------------
# Main UI
# ------------------------------------------------------------

def launch_3d_lab():
    # initial slider values
    eps0 = 0.05
    g0 = 0.20
    k3_scale0 = 1.0
    noise0 = 0.0
    seed0 = 42

    n_steps0 = 300
    dt0 = 0.05

    # first run
    hist, obs, params, rsb_results = run_triocta(
        eps=eps0,
        g=g0,
        k3_scale=k3_scale0,
        noise_sigma=noise0,
        n_steps=n_steps0,
        dt=dt0,
        seed=42,
        do_rsb=True,
        rsb_steps=300,
    )
    rsb_alpha = rsb_results["params"].alpha if rsb_results is not None else 0.0

    dump_timeseries_csv(hist, obs, tag="startup")

    # will hold Line3D objects for the spectral halo rings
    rsb_band_lines = []

    E_final = rsb_results["E_final"] if rsb_results is not None else None
    t = np.asarray(hist["t"])
    kappa = np.asarray(hist["kappa"])
    z = np.asarray(hist["z"])
    J = np.asarray(obs["J_eff"])
    omega_hist = np.asarray(hist["Omega"])  # adapt key if needed
    phi_idx = np.asarray(hist["phi_index"], dtype=int)
    Omega_final = omega_hist[-1]
    phi_idx_final = compute_phi_index(Omega_final, n_corridors=12)

    x, y, z3d = embed_on_torus(omega_hist)

    # normalize J_eff for color mapping along the trail
    J_min, J_max = J.min(), J.max()
    if J_max > J_min:
        J_norm = (J - J_min) / (J_max - J_min)
    else:
        J_norm = np.zeros_like(J)

    # colormap for J_eff-coded trails
    cmap_J = plt.get_cmap("coolwarm")
    trail_collections = []

    # corridor wheel setup (same N=12 as toy_lab)
    N_corridors = 12
    theta_bins = np.linspace(0, 2 * np.pi, N_corridors + 1)
    phi_hist = np.zeros(N_corridors, dtype=float)
    for p in phi_idx:
        phi_hist[p % N_corridors] += 1
    phi_hist_plot = phi_hist / phi_hist.max() if phi_hist.max() > 0 else phi_hist

    # --------------------------------------------------------
    # Figure layout
    # --------------------------------------------------------
    # Bigger canvas, torus gets full left side (both rows)
    fig = plt.figure(figsize=(11, 8))

    # provenance stamp (updates every run)
    meta_text = fig.text(0.02, 0.98, "", ha="left", va="top", fontsize=9, alpha=0.9, family="monospace")
    vrec_text = fig.text(0.02, 0.94, "", ha="left", va="top", fontsize=9, alpha=0.9, family="monospace")
    tz_text   = fig.text(0.02, 0.91, "", ha="left", va="top", fontsize=9, alpha=0.85, family="monospace")

    def _update_tz_text(history, tri_obs, z_key: str):
        """Update the small t_Z / t_J timing readout (meta-shell sanity check)."""
        try:
            t = np.asarray(history.get("t", []), dtype=float)
            J = _jeff_series(history, tri_obs)
            tZ = estimate_z_stabilization_time(history, z_key=z_key)

            # commit time from canonical rule (index → time)
            tJ = None
            if t.size > 0 and J.size == t.size:
                idx, sgn = estimate_chirality_commit_time(J, frac=0.90)
                if idx is not None:
                    tJ = float(t[int(idx)])

            if tZ is None and tJ is None:
                tz_text.set_text("t_Z / t_J: -")
            else:
                sZ = "-" if tZ is None else f"{tZ:.3g}"
                sJ = "-" if tJ is None else f"{tJ:.3g}"
                tz_text.set_text(f"t_Z / t_J: {sZ} / {sJ}")
        except Exception:
            tz_text.set_text("t_Z / t_J: -")

    if isinstance(hist, dict) and "_meta" in hist:
        m = hist["_meta"]
        meta_text.set_text(f"{m.get('run_id','')} | {m.get('timestamp_utc','')}")
    # v_rec (geom) summary for current Z (defaults to Z_total here)
    try:
        v_geom0 = _vrec_geom(hist, z_key="Z_total") if isinstance(hist, dict) else np.asarray([])
        if v_geom0.size:
            vrec_text.set_text(f"v_rec(mean/max): {v_geom0.mean():.4g} / {v_geom0.max():.4g}")
        else:
            vrec_text.set_text("v_rec(mean/max): -")
    except Exception:
        vrec_text.set_text("v_rec(mean/max): -")

    # Meta-shell style timing sanity: does Z settle before chirality commits?
    _update_tz_text(hist, obs, z_key="Z_total")


    # 2 rows, 2 columns: left column is wide (torus), right column narrow (plots)
    gs = fig.add_gridspec(
        2, 2,
        width_ratios=[2.2, 1.0],
        height_ratios=[2.0, 1.3],
    )

    # 3D torus spans both rows on the left
    ax3d = fig.add_subplot(gs[:, 0], projection="3d")

    # J_eff(t) on top-right
    axJ = fig.add_subplot(gs[0, 1])

    # Corridor wheel on bottom-right
    axPHI = fig.add_subplot(gs[1, 1], projection="polar")

    plt.subplots_adjust(
        left=0.07,
        bottom=0.22,
        right=0.97,
        top=0.98,
        hspace=0.45,
        wspace=0.30,
    )


    def make_segments3d(xline, yline, zline):
        """Return segments array of shape (L-1, 2, 3) for Line3DCollection."""
        pts = np.stack([xline, yline, zline], axis=1)
        return np.stack([pts[:-1], pts[1:]], axis=1)

    def draw_rsb_halo():
        """
        Draw (or refresh) the RSB spectral halo around the torus, using
        the final band energies E_final and effective alpha rsb_alpha.
        """
        nonlocal rsb_band_lines

        # clear previous rings
        for ln in rsb_band_lines:
            ln.remove()
        rsb_band_lines = []

        # no halo if there's no RSB info or effectively α≈0
        if E_final is None or rsb_alpha <= 0.0:
            return

        E = np.asarray(E_final, dtype=float)
        E = np.clip(E, 1e-12, None)
        logE = np.log10(E)
        lo, hi = logE.min(), logE.max()
        if hi > lo:
            norm_E = (logE - lo) / (hi - lo)
        else:
            norm_E = np.zeros_like(logE)

        n_bands = E.shape[0]

        # brightness factor: how "collapsed" the halo looks
        # base_alpha in run_triocta is 0.6, so this roughly spans [0,1]
        bright = np.clip(rsb_alpha / 0.6, 0.15, 1.0)

        # geometry for rings slightly outside the wireframe torus
        phi_ring = np.linspace(0, 2 * np.pi, 200)
        cmap_rsb = plt.get_cmap("plasma")

        def torus_ring(theta_fixed):
            Xr = (R_frame * 1.01 + r_frame * 1.05 * np.cos(theta_fixed)) * np.cos(phi_ring)
            Yr = (R_frame * 1.01 + r_frame * 1.05 * np.cos(theta_fixed)) * np.sin(phi_ring)
            Zr = (r_frame * 1.05) * np.sin(theta_fixed) * np.ones_like(phi_ring)
            return Xr, Yr, Zr

        for m in range(n_bands):
            theta_m = 2 * np.pi * (m + 0.5) / n_bands
            Xr, Yr, Zr = torus_ring(theta_m)
            color_m = cmap_rsb(norm_E[m])
            ln, = ax3d.plot(
                Xr, Yr, Zr,
                lw=2.0,
                color=color_m,
                alpha=0.25 + 0.55 * bright,
            )
            rsb_band_lines.append(ln)

    # --- 3D torus frame + corridor rings ---
    phi_frame = np.linspace(0, 2 * np.pi, 80)
    theta_frame = np.linspace(0, 2 * np.pi, 40)
    PhiF, ThetaF = np.meshgrid(phi_frame, theta_frame)
    R_frame, r_frame = 2.0, 0.6
    XF = (R_frame + r_frame * np.cos(ThetaF)) * np.cos(PhiF)
    YF = (R_frame + r_frame * np.cos(ThetaF)) * np.sin(PhiF)
    ZF = r_frame * np.sin(ThetaF)
    ax3d.plot_wireframe(
        XF, YF, ZF,
        rstride=4, cstride=6,
        linewidth=0.3,
        alpha=0.15,
        color="gray",
    )

    # draw initial RSB spectral halo (if any)
    draw_rsb_halo()

    ax3d.set_title("TriOcta trajectory on torus (Ω₁, Ω₂, Ω₃)")
    ax3d.set_xlabel("X")
    ax3d.set_ylabel("Y")
    ax3d.set_zlabel("Z")
    ax3d.view_init(elev=30, azim=40)

    # optional: tighten limits so torus fills the frame nicely
    ax3d.set_box_aspect((1, 1, 0.6))  # X:Y:Z aspect

    # ----- color-coded trail based on J_eff(t) -----
    init_trail = max(30, n_steps0 // 4)
    colors_nodes = ["tab:cyan", "tab:orange", "tab:purple"]
    labels = [r"$\Omega_1$", r"$\Omega_2$", r"$\Omega_3$"]

    for j in range(3):
        L = init_trail
        segs = make_segments3d(x[j, :L], y[j, :L], z3d[j, :L])
        seg_colors = cmap_J(J_norm[1:L])
        coll = Line3DCollection(segs, colors=seg_colors, linewidth=1.8)
        ax3d.add_collection3d(coll)
        trail_collections.append(coll)

    # endpoint markers (solid node colors)
    pts = []
    for j in range(3):
        p = ax3d.scatter(
            x[j, init_trail - 1],
            y[j, init_trail - 1],
            z3d[j, init_trail - 1],
            s=30,
            color=colors_nodes[j],
        )
        pts.append(p)

    # dummy lines for legend
    for j in range(3):
        ax3d.plot([], [], [], color=colors_nodes[j], label=labels[j])
    ax3d.legend(loc="upper left")

    # --------------------------------------------------------
    # Z trajectory overlay (Patch #2: Z_total / Z_macro / Z_chiral)
    # --------------------------------------------------------
    current_Z_key = "Z_total"

    def _zvec_to_scalar(history, key):
        """Project a 3D Z-vector time series to a 1D scalar used for 'strong-Δ' gating.
        Default projection is elevation angle (tilt), which is scale-invariant.
        Falls back to legacy history['z'] if Z vectors are missing.
        """
        try:
            zx, zy, zz = history_Zvec_to_xyz(history, key=key)
            r = np.sqrt(zx*zx + zy*zy) + 1e-12
            return np.arctan2(zz, r)
        except Exception:
            # legacy scalar channel (older runs)
            return np.asarray(history.get("z", []), dtype=float)

    def _get_Z_scaled(history, key):
        xz, yz, zz = history_Zvec_to_xyz(history, key=key)
        Z = np.vstack([xz, yz, zz]).T
        norms = np.linalg.norm(Z, axis=1)

        # robust denom from finite, non-trivial points
        m = np.isfinite(norms) & (norms > 1e-12)
        if np.any(m):
            denom = np.percentile(norms[m], 99)   # 99 or 99.5 recommended
        else:
            denom = 1.0

        denom = float(denom) if np.isfinite(denom) and denom > 1e-12 else 1.0
        scale = 0.85 * r_frame / denom
        return scale * xz, scale * yz, scale * zz

    Zx, Zy, Zz = _get_Z_scaled(hist, current_Z_key)
    z_line, = ax3d.plot(Zx, Zy, Zz, lw=2.0, alpha=0.85)
    z_line.set_label(current_Z_key)

    # Place Z overlay controls relative to the J_eff axis so it never overlaps it
    posJ = axJ.get_position()   # Bbox in figure coords
    posP = axPHI.get_position() # polar axis below (also figure coords)

    # Put the toggle in the vertical gap between axJ (top-right) and axPHI (bottom-right)
    gap_bottom = posP.y1
    gap_top    = posJ.y0
    gap_h = max(0.05, gap_top - gap_bottom)

    toggle_h = min(0.12, 0.85 * gap_h)
    toggle_w = posJ.width
    toggle_x = posJ.x0
    toggle_y = gap_bottom + 0.5 * (gap_h - toggle_h)

    ax_z_toggle = fig.add_axes([toggle_x, toggle_y, toggle_w, toggle_h])

    z_radio = RadioButtons(ax_z_toggle, ("Z_total", "Z_macro", "Z_chiral", "off"), active=0)
    ax_z_toggle.set_title("Z overlay", fontsize=9)
    ax_z_toggle.set_facecolor("none")
    for spine in ax_z_toggle.spines.values():
        spine.set_alpha(0)

    def on_z_toggle(label):
        nonlocal current_Z_key
        lab = str(label)
        if lab == "off":
            z_line.set_visible(False)
            fig.canvas.draw_idle()
            return
        current_Z_key = lab
        Zx2, Zy2, Zz2 = _get_Z_scaled(hist, current_Z_key)
        z_line.set_data(Zx2, Zy2)
        z_line.set_3d_properties(Zz2)
        z_line.set_visible(True)
        z_line.set_label(current_Z_key)

        # update v_rec + strong-Δ gating to match the selected Z component
        try:
            v_geom = _vrec_geom(hist, z_key=current_Z_key)
            if v_geom.size:
                vrec_text.set_text(f"v_rec(mean/max): {v_geom.mean():.4g} / {v_geom.max():.4g}")
            else:
                vrec_text.set_text("v_rec(mean/max): -")
        except Exception:
            vrec_text.set_text("v_rec(mean/max): -")

        # update t_Z/t_J readout to match selected Z component
        _update_tz_text(hist, obs, z_key=current_Z_key)

        # (optional) recompute strong-Δ sectors using the same Z projection
        try:
            kappa_series = np.asarray(hist["kappa"])
            z_series = _zvec_to_scalar(hist, current_Z_key)
            dk = np.diff(kappa_series)
            dz = np.diff(z_series)
            mags = np.sqrt(dk**2 + dz**2)
            thr = 0.5 * mags.max() if mags.size and mags.max() > 0 else np.inf
            big_mask = mags > thr

            strong_counts = np.zeros(N_corridors, dtype=int)
            for i, is_big in enumerate(big_mask):
                if is_big:
                    sector = int(phi_idx[i + 1]) % N_corridors
                    strong_counts[sector] += 1

            for i, bar in enumerate(bars):
                if strong_counts[i] > 0:
                    bar.set_facecolor("orange")
                    bar.set_alpha(0.85)
                else:
                    bar.set_facecolor("lightgray")
                    bar.set_alpha(0.6)
        except Exception:
            pass

        fig.canvas.draw_idle()

    z_radio.on_clicked(on_z_toggle)

    # --- J_eff(t) ---
    line_J, = axJ.plot(t, J, lw=1.5)
    axJ.set_xlabel("time")
    axJ.set_ylabel(r"$J_{\mathrm{eff}}$")
    axJ.set_title(r"$J_{\mathrm{eff}}(t)$")

    if len(J) > 20:
        J_plateau = J[-20:].mean()
    else:
        J_plateau = J.mean()
    J_sign = int(np.sign(J_plateau)) if J_plateau != 0 else 0
    plateau_text = axJ.text(
        0.02, 0.95,
        f"plateau ≈ {J_plateau:.3f}, sign={J_sign:+d}, flips={count_sign_flips(J):d}",
        transform=axJ.transAxes,
        va="top",
        ha="left",
        fontsize=9,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.7),
    )

    # --- corridor wheel ---
    bars = axPHI.bar(
        theta_bins[:-1],
        phi_hist_plot,
        width=(2 * np.pi / N_corridors),
        bottom=0.0,
        color="lightgray",
        edgecolor="k",
        alpha=0.6,
    )
    axPHI.set_ylim(0, 1.0)
    axPHI.set_title("Corridor occupancy / strong-Δ sectors", fontsize=10)

    # pointer for current corridor
    final_phi = phi_idx[-1]
    pointer_angle = (final_phi + 0.5) * (2 * np.pi / N_corridors)
    axPHI._pointer = axPHI.plot(
        [pointer_angle, pointer_angle],
        [0, 1.1],
        color="red",
        lw=2.0,
    )[0]

    # --------------------------------------------------------
    # Sliders & buttons
    # --------------------------------------------------------
    ax_eps = plt.axes([0.12, 0.17, 0.50, 0.03])
    ax_g   = plt.axes([0.12, 0.13, 0.50, 0.03])
    ax_k3  = plt.axes([0.12, 0.09, 0.50, 0.03])
    ax_n   = plt.axes([0.12, 0.05, 0.50, 0.03])
    ax_trail = plt.axes([0.12, 0.01, 0.50, 0.03])
    ax_seed = plt.axes([0.70, 0.13, 0.20, 0.03])


    s_eps = Slider(ax_eps, r"$\varepsilon$", 0.01, 0.10, valinit=eps0, valstep=0.005)
    s_g   = Slider(ax_g,   r"$g$",           0.10, 0.30, valinit=g0,   valstep=0.01)
    s_k3  = Slider(ax_k3,  r"$k_3$ scale",   0.5,  3.0,  valinit=k3_scale0)
    s_n   = Slider(ax_n,   r"noise $\sigma$",0.0,  0.10, valinit=noise0)
    s_seed = Slider(ax_seed, "seed", 0, 1_000_000, valinit=seed0, valstep=1)


    s_trail = Slider(
        ax_trail,
        "trail length",
        10,
        n_steps0,
        valinit=init_trail,
        valstep=1,
    )

    ax_button = plt.axes([0.70, 0.06, 0.20, 0.06])
    btn_run = Button(ax_button, "Run", hovercolor="0.9")

    # --------------------------------------------------------
    # Callbacks
    # --------------------------------------------------------

    def update_trail(val=None):
        L = int(s_trail.val)
        L = max(2, min(L, x.shape[1]))  # need at least 2 points for segments

        # update color-coded trail
        for j in range(3):
            segs = make_segments3d(x[j, :L], y[j, :L], z3d[j, :L])
            seg_colors = cmap_J(J_norm[1:L])
            trail_collections[j].set_segments(segs)
            trail_collections[j].set_colors(seg_colors)

            # move endpoint marker
            pts[j]._offsets3d = (
                np.array([x[j, L - 1]]),
                np.array([y[j, L - 1]]),
                np.array([z3d[j, L - 1]]),
            )

        fig.canvas.draw_idle()

    s_trail.on_changed(update_trail)

    def rerun_model(event=None):
        nonlocal x, y, z3d, hist, obs, params, t, phi_idx, J_norm
        nonlocal E_final, rsb_alpha, rsb_results

        eps = s_eps.val
        g = s_g.val
        k3_scale = s_k3.val
        noise_sigma = s_n.val

        seed = int(s_seed.val)

        history_new, obs_new, params_new, rsb_results_new = run_triocta(
            eps=eps,
            g=g,
            k3_scale=k3_scale,
            noise_sigma=noise_sigma,
            n_steps=n_steps0,
            dt=dt0,
            seed=seed,
            do_rsb=True,
            rsb_steps=300,
        )

        hist, obs, params, rsb_results = history_new, obs_new, params_new, rsb_results_new
        # Update provenance + v_rec summaries
        if isinstance(hist, dict) and "_meta" in hist:
            m = hist["_meta"]
            meta_text.set_text(f"{m.get('run_id','')} | {m.get('timestamp_utc','')}")
        try:
            key_for_v = current_Z_key if current_Z_key != "off" else "Z_total"
            v_geom = _vrec_geom(hist, z_key=key_for_v)
            if v_geom.size:
                vrec_text.set_text(f"v_rec(mean/max): {v_geom.mean():.4g} / {v_geom.max():.4g}")
            else:
                vrec_text.set_text("v_rec(mean/max): -")
        except Exception:
            vrec_text.set_text("v_rec(mean/max): -")

        E_final = rsb_results["E_final"] if rsb_results is not None else None
        rsb_alpha = rsb_results["params"].alpha if rsb_results is not None else 0.0

        t_new = np.asarray(history_new["t"])
        kappa_new = np.asarray(history_new["kappa"])
        z_new = np.asarray(history_new.get("z", []))  # legacy scalar (kept for CSV/back-compat)
        J_new = np.asarray(obs_new["J_eff"])
        # recompute normalized J_eff for color mapping
        J_min, J_max = J_new.min(), J_new.max()
        if J_max > J_min:
            J_norm = (J_new - J_min) / (J_max - J_min)
        else:
            J_norm = np.zeros_like(J_new)

        omega_new = np.asarray(history_new["Omega"])  # adapt key if needed
        phi_idx = np.asarray(history_new["phi_index"], dtype=int)

        # recompute torus embedding
        x_new, y_new, z_new3d = embed_on_torus(omega_new)

        # resize arrays
        x[:] = x_new
        y[:] = y_new
        z3d[:] = z_new3d

        # update Z overlay (if enabled)
        if z_line.get_visible() and current_Z_key != "off":
            try:
                Zx2, Zy2, Zz2 = _get_Z_scaled(hist, current_Z_key)
                z_line.set_data(Zx2, Zy2)
                z_line.set_3d_properties(Zz2)
            except Exception:
                # If Z keys missing for some reason, hide overlay
                z_line.set_visible(False)

        # update J(t)
        line_J.set_xdata(t_new)
        line_J.set_ydata(J_new)
        axJ.relim()
        axJ.autoscale_view()

        if len(J_new) > 20:
            J_plateau_new = J_new[-20:].mean()
        else:
            J_plateau_new = J_new.mean()
        J_sign_new = int(np.sign(J_plateau_new)) if J_plateau_new != 0 else 0
        plateau_text.set_text(
            f"plateau ≈ {J_plateau_new:.3f}, sign={J_sign_new:+d}, flips={count_sign_flips(J_new):d}"
        )

        # corridor occupancy / strong-Δ
        N = N_corridors
        phi_hist[:] = 0.0
        for p in phi_idx:
            phi_hist[p % N] += 1

        if phi_hist.max() > 0:
            phi_hist_plot = phi_hist / phi_hist.max()
        else:
            phi_hist_plot = phi_hist

        kappa_series = np.asarray(history_new["kappa"])
        z_series = _zvec_to_scalar(history_new, current_Z_key if current_Z_key != "off" else "Z_total")
        dk = np.diff(kappa_series)
        dz = np.diff(z_series)
        mags = np.sqrt(dk**2 + dz**2)
        if mags.size > 0 and mags.max() > 0:
            thr = 0.5 * mags.max()
        else:
            thr = np.inf
        big_mask = mags > thr

        strong_counts = np.zeros(N, dtype=int)
        for i, is_big in enumerate(big_mask):
            if is_big:
                sector = phi_idx[i + 1] % N
                strong_counts[sector] += 1

        for i, bar in enumerate(bars):
            bar.set_height(phi_hist_plot[i])
            if strong_counts[i] > 0:
                bar.set_color("red")
                bar.set_alpha(0.8)
            else:
                bar.set_color("lightgray")
                bar.set_alpha(0.6)

        # refresh color-coded trail with new data, using current trail length
        L = int(s_trail.val)
        L = max(2, min(L, x.shape[1]))

        for j in range(3):
            segs = make_segments3d(x[j, :L], y[j, :L], z3d[j, :L])
            seg_colors = cmap_J(J_norm[1:L])
            trail_collections[j].set_segments(segs)
            trail_collections[j].set_colors(seg_colors)

            pts[j]._offsets3d = (
                np.array([x[j, L - 1]]),
                np.array([y[j, L - 1]]),
                np.array([z3d[j, L - 1]]),
            )

        # update pointer
        if hasattr(axPHI, "_pointer"):
            axPHI._pointer.remove()

        final_phi = phi_idx[-1]
        pointer_angle = (final_phi + 0.5) * (2 * np.pi / N)
        axPHI._pointer = axPHI.plot(
            [pointer_angle, pointer_angle],
            [0, 1.1],
            color="red",
            lw=2.0,
        )[0]

        # reset / clamp trail slider to valid range
        s_trail.valmax = x.shape[1]
        s_trail.ax.set_xlim(s_trail.valmin, s_trail.valmax)
        s_trail.set_val(min(int(s_trail.val), x.shape[1]))

        print("\n===== toy_3d run =====")
        print(f"eps={eps:.3f}, g={g:.3f}, k3_scale={k3_scale:.3f}, noise_sigma={noise_sigma:.3f}")
        print("k_vals used:", params_new.k_vals)
        print(f"J_eff plateau ≈ {J_plateau_new:.4f}, sign={J_sign_new:+d}")
        # refresh RSB spectral halo with new band energies / alpha
        draw_rsb_halo()
        dump_timeseries_csv(hist, obs, tag="rerun")
        fig.canvas.draw_idle()
    btn_run.on_clicked(rerun_model)

    plt.show()

    # auto-dump on close
    def on_close(event):
        try:
            dump_timeseries_csv(hist, obs, tag="onclose")
        except Exception as e:
          print("[auto-dump] close save failed:", e)
    fig.canvas.mpl_connect("close_event", on_close)


if __name__ == "__main__":
    launch_3d_lab()