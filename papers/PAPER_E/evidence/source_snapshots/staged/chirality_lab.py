"""
chirality_lab.py

Small analysis + visualization lab for:
  - J_eff(t) (chirality)
  - Z_vec(t) 3D geometry (if present in history)
  - torsion-like pulses from sign flips / large |dJ/dt|
  - Jeff–Δ(κ,Z) coupling using existing diagnostics.analyze_Jeff_coupling
  - linear mapping J_eff ≈ w · Z_vec (Z → chirality bridge)

This is designed to sit alongside the v3.3 toy model code and reuse
its history/obs structures.
"""

import numpy as np
import matplotlib.pyplot as plt

# Optional imports from your toy model
try:
    from geometry_3d import history_Zvec_to_xyz
except ImportError:
    history_Zvec_to_xyz = None

try:
    from diagnostics import analyze_Jeff_coupling
except ImportError:
    analyze_Jeff_coupling = None


# ---------------------------------------------------------------------
# 1. Helpers: finite differences, torsion pulses, big-step mask
# ---------------------------------------------------------------------

def finite_diff(x, t):
    """
    Simple finite difference dx/dt given arrays x, t.
    Returns mid-point times and derivatives.
    """
    x = np.asarray(x)
    t = np.asarray(t)
    if len(x) < 2:
        return np.array([]), np.array([])
    dt = np.diff(t)
    dx = np.diff(x)
    # Guard against degenerate dt
    dt_safe = dt + 1e-12
    return t[:-1] + 0.5 * dt, dx / dt_safe


def detect_torsion_pulses(J, t, use_sign_flip=True, dJ_thresh=None):
    """
    Detect "torsion pulses" in J_eff(t).

    Two mechanisms:
      (1) sign flips of J_eff (topological orientation flips),
      (2) optionally, large |dJ/dt| spikes above dJ_thresh.

    Returns:
      dict with keys:
        - "t_sign_flips": np.array of times where sign(J) changes
        - "t_dJ_spikes" : np.array of times where |dJ/dt| > threshold
        - "dJ_dt"       : full derivative array
        - "t_mid"       : mid-point times for dJ/dt
    """
    J = np.asarray(J)
    t = np.asarray(t)

    # --- (1) sign flips ---
    t_sign_flips = []
    if use_sign_flip:
        signs = np.sign(J)
        # treat exact zeros as previous sign to avoid spurious flips
        for i in range(1, len(signs)):
            if signs[i] == 0:
                signs[i] = signs[i-1]
        for i in range(1, len(signs)):
            if signs[i] != signs[i-1]:
                t_sign_flips.append(t[i])

    # --- (2) |dJ/dt| spikes ---
    t_mid, dJ_dt = finite_diff(J, t)
    abs_dJ_dt = np.abs(dJ_dt)

    if dJ_thresh is None and len(abs_dJ_dt) > 0:
        # e.g. pick spikes above the 99th percentile
        dJ_thresh = np.quantile(abs_dJ_dt, 0.99)

    t_dJ_spikes = t_mid[abs_dJ_dt > dJ_thresh] if len(abs_dJ_dt) > 0 else np.array([])

    return {
        "t_sign_flips": np.array(t_sign_flips),
        "t_dJ_spikes": np.array(t_dJ_spikes),
        "t_mid": t_mid,
        "dJ_dt": dJ_dt,
        "dJ_thresh": dJ_thresh,
    }


def build_big_steps_mask_from_kappa_z(history, frac_of_max=0.5):
    """
    Approximate big Δ(κ,Z) mask directly from history, without using
    the full clustering machinery. This is a fallback so we can call
    analyze_Jeff_coupling even in a lightweight lab setting.

    We define a step magnitude:
        Δ_step = sqrt( (Δκ/κ_scale)^2 + (Δz/z_scale)^2 ),
    and mark as "big" those with Δ_step >= frac_of_max * Δ_step_max.

    Returns:
      big_steps_mask: boolean array of length N-1 (for steps).
    """
    kappa = np.asarray(history.get("kappa"))
    z = np.asarray(history.get("z"))

    if len(kappa) < 2 or len(z) < 2:
        print("[chirality_lab] Not enough kappa/z points for Δ(κ,Z) mask.")
        return None

    dk = np.diff(kappa)
    dz = np.diff(z)

    k_scale = np.max(np.abs(kappa)) + 1e-12
    z_scale = np.max(np.abs(z)) + 1e-12

    step_mag = np.sqrt((dk / k_scale) ** 2 + (dz / z_scale) ** 2)
    max_step = np.max(step_mag) + 1e-18
    thresh = frac_of_max * max_step

    big_steps_mask = step_mag >= thresh
    return big_steps_mask


def lagged_corr(x, y, max_lag_steps=10, name_x="X", name_y="Y"):
    """
    Compute corr(x(t), y(t+lag)) for lag = 0..max_lag_steps (in steps).

    Returns:
      {
        "lags": np.array of lags (in steps),
        "corr": np.array of Pearson correlations (same length),
      }
    """
    x = np.asarray(x)
    y = np.asarray(y)
    N = len(x)
    max_lag_steps = min(max_lag_steps, N - 2)  # keep it safe

    lags = []
    corrs = []

    def safe_corr(a, b):
        a = np.asarray(a)
        b = np.asarray(b)
        if a.std() < 1e-14 or b.std() < 1e-14:
            return np.nan
        return np.corrcoef(a, b)[0, 1]

    for lag in range(0, max_lag_steps + 1):
        # x(t) vs y(t+lag)
        if lag == 0:
            x_seg = x
            y_seg = y
        else:
            x_seg = x[:-lag]
            y_seg = y[lag:]

        if len(x_seg) < 5:  # avoid silly small samples
            break

        c = safe_corr(x_seg, y_seg)
        lags.append(lag)
        corrs.append(c)

    lags = np.array(lags, dtype=int)
    corrs = np.array(corrs, dtype=float)

    print(f"\n=== Lagged corr({name_x}(t), {name_y}(t+lag)) ===")
    for L, C in zip(lags, corrs):
        print(f"lag = {L:2d} steps → corr ≈ {C: .4f}")

    return {"lags": lags, "corr": corrs}

# ---------------------------------------------------------------------
# 2. Z_vec → J_eff mapping
# ---------------------------------------------------------------------

def fit_jeff_from_z(history, obs, key="Z_vec"):
    """
    Fit a linear map J_eff ≈ w · Z (Z in R^3) via least squares.

    key: which history key to use ("Z_vec" or "Z_chiral").
    """
    if key not in history:
        print(f"[chirality_lab] history has no '{key}'; cannot fit mapping.")
        return None

    Z = np.asarray(history[key])
    J = np.asarray(obs.get("J_eff"))

    if Z.ndim != 2 or Z.shape[1] != 3:
        print(f"[chirality_lab] {key} has unexpected shape:", Z.shape)
        return None

    if len(J) != len(Z):
        L = min(len(J), len(Z))
        print(f"[chirality_lab] Trimming {key} and J_eff to common length:", L)
        Z = Z[:L]
        J = J[:L]

    ZT_Z = Z.T @ Z
    ZT_J = Z.T @ J

    try:
        w = np.linalg.solve(ZT_Z, ZT_J)
    except np.linalg.LinAlgError:
        w = np.linalg.pinv(ZT_Z) @ ZT_J

    J_pred = Z @ w
    corr = np.corrcoef(J, J_pred)[0, 1]

    print(f"\n=== {key} → J_eff linear fit ===")
    print(f"w_{key} ≈ {w}")
    print(f"corr(J, {key}·w) ≈ {corr:.4f}")
    return w


def fit_jeff_nonlinear_from_z(history, obs, key="Z_vec"):
    """
    Nonlinear (quadratic) fit:
        J_eff ≈ a0
                + a1*Zx + a2*Zy + a3*Zz
                + a4*Zx^2 + a5*Zy^2 + a6*Zz^2
                + a7*Zx*Zy + a8*Zy*Zz + a9*Zz*Zx

    This checks whether quadratic structure in the 3D embedding
    captures more of J_eff than a pure linear map.
    """
    if key not in history:
        print(f"[chirality_lab] history has no '{key}'; cannot do nonlinear fit.")
        return None

    Z = np.asarray(history[key])
    J = np.asarray(obs.get("J_eff"))

    if Z.ndim != 2 or Z.shape[1] != 3:
        print(f"[chirality_lab] {key} has unexpected shape:", Z.shape)
        return None

    if len(J) != len(Z):
        L = min(len(J), len(Z))
        print(f"[chirality_lab] Trimming {key} and J_eff to common length for nonlinear fit:", L)
        Z = Z[:L]
        J = J[:L]

    Zx = Z[:, 0]
    Zy = Z[:, 1]
    Zz = Z[:, 2]

    # Design matrix with linear + quadratic terms
    X = np.column_stack([
        np.ones_like(Zx),      # a0 (bias)
        Zx, Zy, Zz,            # linear terms
        Zx**2, Zy**2, Zz**2,   # pure quadratic terms
        Zx*Zy, Zy*Zz, Zz*Zx,   # cross terms
    ])

    # Least squares fit: minimize ||X a - J||^2
    a, *_ = np.linalg.lstsq(X, J, rcond=None)
    J_pred = X @ a

    # Correlation & simple R^2
    corr = np.corrcoef(J, J_pred)[0, 1]
    ss_res = np.sum((J - J_pred)**2)
    ss_tot = np.sum((J - J.mean())**2) + 1e-18
    r2 = 1.0 - ss_res / ss_tot

    print(f"\n=== {key} → J_eff nonlinear (quadratic) fit ===")
    print(f"corr(J, J_pred) ≈ {corr:.4f},   R^2 ≈ {r2:.4f}")
    # You can print 'a' if you want to inspect coefficients:
    # print(f"a (coeffs) = {a}")
    return {
        "a": a,
        "corr": corr,
        "r2": r2,
    }


def compute_frenet_invariants(history, key="Z_vec"):
    """
    Compute discrete Frenet-Serret invariants (curvature, torsion)
    for a 3D trajectory Z(t) stored in history[key].

    Returns:
      {
        "t_center": t_center,   # time indices corresponding to v/a/j triple
        "kappa": kappa_g,       # curvature array
        "tau": tau,             # torsion array
      }
    """
    if key not in history:
        print(f"[chirality_lab] history has no '{key}'; cannot compute Frenet invariants.")
        return None

    Z = np.asarray(history[key])   # shape (N, 3)
    t = np.asarray(history["t"])

    if Z.ndim != 2 or Z.shape[1] != 3:
        print(f"[chirality_lab] {key} has unexpected shape:", Z.shape)
        return None

    N = len(Z)
    if N < 4:
        print("[chirality_lab] Not enough points for Frenet invariants (need N >= 4).")
        return None

    # Assume roughly uniform dt; we can still use it for scaling
    dt_arr = np.diff(t)
    dt = float(np.mean(dt_arr)) if len(dt_arr) > 0 else 1.0

    # First derivative: velocity v ≈ dZ/dt
    v = np.diff(Z, axis=0) / dt          # shape (N-1, 3)

    # Second derivative: acceleration a ≈ dv/dt
    a = np.diff(v, axis=0) / dt          # shape (N-2, 3)

    # Third derivative: jerk j ≈ da/dt
    j = np.diff(a, axis=0) / dt          # shape (N-3, 3)

    # Align v, a, j to same length L = N-3
    L = min(len(v), len(a), len(j))
    v0 = v[:L]
    a0 = a[:L]
    j0 = j[:L]

    # Cross product v × a
    cross_va = np.cross(v0, a0, axis=1)
    norm_v = np.linalg.norm(v0, axis=1)
    norm_cross = np.linalg.norm(cross_va, axis=1)

    eps = 1e-12

    # Curvature κ_g = ||v × a|| / ||v||^3
    kappa_g = norm_cross / (norm_v**3 + eps)

    # Torsion τ = ((v × a) · j) / ||v × a||^2
    dot_cross_j = np.einsum("ij,ij->i", cross_va, j0)
    tau = dot_cross_j / (norm_cross**2 + eps)

    # Time index for these invariants: roughly t[1:1+L]
    t_center = t[1:1+L]

    return {
        "t_center": t_center,
        "kappa": kappa_g,
        "tau": tau,
    }


def fit_chirality_curvature_index(history, obs, key="Z_vec"):
    """
    Fit a 'chirality curvature index' chi_geom(t) from geometric curvature
    and torsion, attempting to reconstruct |J_eff(t)|.

    Uses Frenet invariants (kappa, tau) of history[key] and builds a small
    nonlinear feature set:

        F = [kappa, |tau|, kappa^2, tau^2, kappa*|tau|]

    Then fits:
        |J| ≈ c0 + F @ c

    Prints:
        - corr(|J|, chi_geom)
        - R^2 for the regression

    Returns:
      {
        "coeffs": coeffs,  # (c0, c1..c5)
        "corr": corr,
        "r2": r2,
      }
    """
    inv = compute_frenet_invariants(history, key=key)
    if inv is None:
        return None

    t_center = inv["t_center"]
    kappa = inv["kappa"]
    tau = inv["tau"]

    t = np.asarray(history["t"])
    J = np.asarray(obs["J_eff"])

    # Align J to invariants (same logic as before)
    L = len(t_center)
    if len(J) < 1 + L:
        L = max(0, len(J) - 1)
        t_center = t_center[:L]
        kappa = kappa[:L]
        tau = tau[:L]
    J_center = J[1:1+L]
    abs_J = np.abs(J_center)

    if L < 10:
        print("[chirality_lab] Not enough points for curvature-index fit.")
        return None

    # Features: [kappa, |tau|, kappa^2, tau^2, kappa*|tau|]
    abs_tau = np.abs(tau)
    F = np.column_stack([
        kappa,
        abs_tau,
        kappa**2,
        tau**2,
        kappa * abs_tau,
    ])

    # Add bias column
    X = np.column_stack([np.ones(L), F])

    # Least squares fit: minimize ||X c - |J||^2
    coeffs, *_ = np.linalg.lstsq(X, abs_J, rcond=None)
    abs_J_pred = X @ coeffs

    # Correlation & R^2
    num = np.sum((abs_J - abs_J.mean()) * (abs_J_pred - abs_J_pred.mean()))
    den = np.sqrt(np.sum((abs_J - abs_J.mean())**2) *
                  np.sum((abs_J_pred - abs_J_pred.mean())**2)) + 1e-18
    corr = num / den

    ss_res = np.sum((abs_J - abs_J_pred)**2)
    ss_tot = np.sum((abs_J - abs_J.mean())**2) + 1e-18
    r2 = 1.0 - ss_res / ss_tot

    print("\n=== Chirality curvature index fit (|J| from kappa, tau) ===")
    print(f"corr(|J|, chi_geom) ≈ {corr:.4f},   R^2 ≈ {r2:.4f}")
    print("coeffs (c0, c_kappa, c_|tau|, c_k2, c_t2, c_k|t|) ≈")
    print(coeffs)

    return {
        "coeffs": coeffs,
        "corr": corr,
        "r2": r2,
    }

def scatter_J_vs_chi_geom(history, obs, coeffs, key="Z_vec", title_suffix=""):
    """
    Visualize the two-sheet structure by plotting J_eff(t) vs chi_geom(t)
    for a single run.

    Uses:
      - Frenet invariants (kappa, tau) from history[key]
      - coefficients from the curvature-index fit:
         (c0, c_kappa, c_|tau|, c_k2, c_t2, c_k|t|)
    Produces:
      - A scatter plot: J_eff vs chi_geom
      - Overlay lines J = chi_geom and J = -chi_geom
    """
    inv = compute_frenet_invariants(history, key=key)
    if inv is None:
        print("[scatter] No Frenet invariants; cannot plot.")
        return

    t_center = inv["t_center"]
    kappa = inv["kappa"]
    tau = inv["tau"]

    t = np.asarray(history["t"])
    J = np.asarray(obs["J_eff"])

    # Align J to invariants
    L = len(t_center)
    if len(J) < 1 + L:
        L = max(0, len(J) - 1)
        t_center = t_center[:L]
        kappa = kappa[:L]
        tau = tau[:L]
    J_center = J[1:1+L]

    if L < 10:
        print("[scatter] Not enough points for meaningful scatter.")
        return

    c0, c_kappa, c_abs_tau, c_k2, c_t2, c_kabs = coeffs
    abs_tau = np.abs(tau)

    chi_geom = (
        c0
        + c_kappa * kappa
        + c_abs_tau * abs_tau
        + c_k2 * (kappa**2)
        + c_t2 * (tau**2)
        + c_kabs * (kappa * abs_tau)
    )

    # Build plot
    plt.figure(figsize=(6, 5))
    plt.scatter(chi_geom, J_center, s=10, alpha=0.6, label=r"$J_{\rm eff}(t)$")

    # Ideal sheets J = ± chi_geom
    x_min = float(np.min(chi_geom))
    x_max = float(np.max(chi_geom))
    xs = np.linspace(x_min, x_max, 200)
    plt.plot(xs,  xs,  linestyle="--", linewidth=1.0, label=r"$J=+\chi_{\rm geom}$")
    plt.plot(xs, -xs, linestyle="--", linewidth=1.0, label=r"$J=-\chi_{\rm geom}$")

    plt.xlabel(r"$\chi_{\rm geom}(\kappa,\tau)$")
    plt.ylabel(r"$J_{\rm eff}$")
    plt.title(r"Two-sheet chirality structure" + title_suffix)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

def analyze_sign_branches_over_chi(history, obs, coeffs, key="Z_vec"):
    """
    Analyze how chirality sign branches (sign(J_eff)) behave over the
    geometric chirality index chi_geom(kappa, tau).

    Inputs:
      - history: dict with "t" and trajectory key (e.g. "Z_vec")
      - obs: dict with "J_eff"
      - coeffs: array of length 6:
          (c0, c_kappa, c_|tau|, c_k2, c_t2, c_k|t|)
      - key: which trajectory to use for Frenet invariants (default "Z_vec")

    Prints:
      - number of sign branches
      - stats for each branch (length, mean|J|, mean chi_geom)
      - average chi_geom/U around sign flips
    """
    inv = compute_frenet_invariants(history, key=key)
    if inv is None:
        return None

    t_center = inv["t_center"]
    kappa = inv["kappa"]
    tau = inv["tau"]

    t = np.asarray(history["t"])
    J = np.asarray(obs["J_eff"])

    # Align J to invariants (same convention as before)
    L = len(t_center)
    if len(J) < 1 + L:
        L = max(0, len(J) - 1)
        t_center = t_center[:L]
        kappa = kappa[:L]
        tau = tau[:L]
    J_center = J[1:1+L]

    if L < 5:
        print("[sign-branches] Not enough points for analysis.")
        return None

    # Unpack coefficients
    c0, c_kappa, c_abs_tau, c_k2, c_t2, c_kabs = coeffs

    abs_tau = np.abs(tau)

    # chi_geom(t) from kappa, tau
    chi_geom = (
        c0
        + c_kappa * kappa
        + c_abs_tau * abs_tau
        + c_k2 * (kappa**2)
        + c_t2 * (tau**2)
        + c_kabs * (kappa * abs_tau)
    )
    U_geom = chi_geom**2
    abs_J = np.abs(J_center)

    # Sign branches
    sign_J = np.sign(J_center)
    # Treat zeros as +1 for branch purposes
    sign_J[sign_J == 0] = 1

    branches = []
    start_idx = 0
    current_sign = sign_J[0]

    for i in range(1, L):
        if sign_J[i] != current_sign:
            # Close current branch at i-1
            branches.append((current_sign, start_idx, i - 1))
            start_idx = i
            current_sign = sign_J[i]
    # Close final branch
    branches.append((current_sign, start_idx, L - 1))

    print("\n=== Sign-branch structure over chi_geom ===")
    print(f"Total branches: {len(branches)}")

    branch_stats = []

    for b_idx, (s, i0, i1) in enumerate(branches):
        length = i1 - i0 + 1
        if length <= 0:
            continue
        mean_absJ = abs_J[i0:i1+1].mean()
        mean_chi = chi_geom[i0:i1+1].mean()
        mean_U = U_geom[i0:i1+1].mean()

        print(f"Branch {b_idx:2d}: sign = {int(s):+d}, "
              f"len = {length:3d}, "
              f"<|J|> ≈ {mean_absJ:.4e}, "
              f"<chi_geom> ≈ {mean_chi:.4e}, "
              f"<U> ≈ {mean_U:.4e}")

        branch_stats.append({
            "sign": s,
            "i0": i0,
            "i1": i1,
            "length": length,
            "mean_absJ": mean_absJ,
            "mean_chi": mean_chi,
            "mean_U": mean_U,
        })

    # Analyze chi_geom around branch flips
    flip_chi_before = []
    flip_chi_after = []
    flip_U_before = []
    flip_U_after = []

    for s, i0, i1 in branches[:-1]:
        # Flip occurs at boundary between this branch and the next one:
        flip_idx = i1
        if 0 < flip_idx < L - 1:
            flip_chi_before.append(chi_geom[flip_idx])
            flip_chi_after.append(chi_geom[flip_idx + 1])
            flip_U_before.append(U_geom[flip_idx])
            flip_U_after.append(U_geom[flip_idx + 1])

    if flip_chi_before:
        print("\n--- Sign-flip neighborhood stats ---")
        print(f"Number of flips: {len(flip_chi_before)}")
        print(f"<chi_geom> just before flip ≈ {np.mean(flip_chi_before):.4e}")
        print(f"<chi_geom> just after  flip ≈ {np.mean(flip_chi_after):.4e}")
        print(f"<U>        just before flip ≈ {np.mean(flip_U_before):.4e}")
        print(f"<U>        just after  flip ≈ {np.mean(flip_U_after):.4e}")
    else:
        print("\n--- No sign flips detected (single sheet) ---")

    return {
        "branches": branch_stats,
        "flip_chi_before": flip_chi_before,
        "flip_chi_after": flip_chi_after,
        "flip_U_before": flip_U_before,
        "flip_U_after": flip_U_after,
    }


def analyze_geometric_torsion_coupling(history, obs, key="Z_vec"):
    """
    Compare Frenet torsion of Z(t) to chirality J_eff(t).

    Prints:
      - corr(J, tau)
      - corr(sign(J), sign(tau))
      - corr(|J|, |tau|)
    """
    inv = compute_frenet_invariants(history, key=key)
    if inv is None:
        return None

    t_center = inv["t_center"]
    tau = inv["tau"]

    t = np.asarray(history["t"])
    J = np.asarray(obs["J_eff"])

    # Align J to same length: use J[1:1+L]
    L = len(t_center)
    if len(J) < 1 + L:
        L = max(0, len(J) - 1)
        t_center = t_center[:L]
        tau = tau[:L]
    J_center = J[1:1+L]

    if L < 2:
        print("[chirality_lab] Not enough aligned points for torsion–Jeff analysis.")
        return None

    # Correlations
    def safe_corr(x, y, name):
        x = np.asarray(x)
        y = np.asarray(y)
        if x.std() < 1e-14 or y.std() < 1e-14:
            print(f"[torsion] {name}: one of the arrays is nearly constant; corr undefined.")
            return np.nan
        return np.corrcoef(x, y)[0, 1]

    corr_J_tau = safe_corr(J_center, tau, "J vs tau")

    sign_J = np.sign(J_center)
    sign_tau = np.sign(tau)
    # Treat zeros as +1 for simplicity
    sign_J[sign_J == 0] = 1
    sign_tau[sign_tau == 0] = 1
    corr_sign = safe_corr(sign_J, sign_tau, "sign(J) vs sign(tau)")

    abs_J = np.abs(J_center)
    abs_tau = np.abs(tau)
    corr_abs = safe_corr(abs_J, abs_tau, "|J| vs |tau|")

    print("\n=== Geometric torsion–chirality coupling (Frenet analysis) ===")
    print(f"corr(J, tau)           ≈ {corr_J_tau:.4f}")
    print(f"corr(sign(J), sign(tau)) ≈ {corr_sign:.4f}")
    print(f"corr(|J|, |tau|)       ≈ {corr_abs:.4f}")

    return {
        "corr_J_tau": corr_J_tau,
        "corr_sign": corr_sign,
        "corr_abs": corr_abs,
        "t_center": t_center,
        "tau": tau,
    }


def analyze_lagged_geometry_to_chirality(history, obs, key="Z_vec", max_lag_steps=10):
    """
    Time-lag analysis:
      - Does curvature κ(t) or torsion τ(t) predict future J_eff(t+Δt)?

    Uses the Frenet invariants of history[key] and compares them to:
      - J_eff(t)
      - |J_eff(t)|
    at various lags (0..max_lag_steps steps).
    """
    inv = compute_frenet_invariants(history, key=key)
    if inv is None:
        return None

    t_center = inv["t_center"]
    kappa = inv["kappa"]
    tau = inv["tau"]

    t = np.asarray(history["t"])
    J = np.asarray(obs["J_eff"])

    # Align J to same length as invariants (we already used J[1:1+L] earlier)
    L = len(t_center)
    if len(J) < 1 + L:
        L = max(0, len(J) - 1)
        t_center = t_center[:L]
        kappa = kappa[:L]
        tau = tau[:L]
    J_center = J[1:1+L]
    abs_J_center = np.abs(J_center)

    if L < 10:
        print("[chirality_lab] Not enough points for lagged geometry→chirality analysis.")
        return None

    print("\n=== Lagged geometry → future chirality analysis ===")
    print(f"(Using {L} aligned points from Frenet invariants)")

    # κ(t) → J(t+lag)
    res_kappa_J = lagged_corr(kappa, J_center,
                              max_lag_steps=max_lag_steps,
                              name_x="kappa", name_y="J")

    # κ(t) → |J|(t+lag)
    res_kappa_absJ = lagged_corr(kappa, abs_J_center,
                                 max_lag_steps=max_lag_steps,
                                 name_x="kappa", name_y="|J|")

    # τ(t) → J(t+lag)
    res_tau_J = lagged_corr(tau, J_center,
                            max_lag_steps=max_lag_steps,
                            name_x="tau", name_y="J")

    # τ(t) → |J|(t+lag)
    res_tau_absJ = lagged_corr(tau, abs_J_center,
                               max_lag_steps=max_lag_steps,
                               name_x="tau", name_y="|J|")

    return {
        "kappa_to_J": res_kappa_J,
        "kappa_to_absJ": res_kappa_absJ,
        "tau_to_J": res_tau_J,
        "tau_to_absJ": res_tau_absJ,
        "t_center": t_center,
    }

# ---------------------------------------------------------------------
# 3. Main analysis entry point
# ---------------------------------------------------------------------
def run_chirality_lab(history, obs, big_steps_mask=None):
    """
    Core analysis function.

    Expects:
      - history: dict-like with at least 't', 'kappa', 'z', optionally 'Z_vec'
      - obs:     dict-like with 'J_eff'
      - big_steps_mask: optional precomputed Δ(κ,Z) boolean mask for steps

    Performs:
      - Z_vec → J_eff mapping fit (if Z_vec present)
      - torsion pulse detection
      - Jeff–Δ(κ,Z) coupling via diagnostics.analyze_Jeff_coupling (if available)
      - time-series plots and (optional) 3D Z_vec visualization
    """
    t = np.asarray(history["t"])
    J = np.asarray(obs["J_eff"])

    # 1) Fit Z_vec → J_eff and, if available, Z_chiral → J_eff
    w_vec = fit_jeff_from_z(history, obs, key="Z_vec")
    w_chiral = fit_jeff_from_z(history, obs, key="Z_chiral")
    # we return both; you can inspect whichever you care about

    # 1b) Nonlinear (quadratic) fits for both embeddings
    nl_vec = fit_jeff_nonlinear_from_z(history, obs, key="Z_vec")
    nl_chiral = fit_jeff_nonlinear_from_z(history, obs, key="Z_chiral")

    # 2) Torsion pulses (sign flips + |dJ/dt| spikes)
    torsion_info = detect_torsion_pulses(J, t)
    t_flips = torsion_info["t_sign_flips"]
    t_spikes = torsion_info["t_dJ_spikes"]

    # 3) Jeff–Δ(κ,Z) coupling (optional)
    if big_steps_mask is None:
        big_steps_mask = build_big_steps_mask_from_kappa_z(history)
    if analyze_Jeff_coupling is not None and big_steps_mask is not None:
        analyze_Jeff_coupling(history, obs, big_steps_mask)
    else:
        print("[chirality_lab] Skipping Jeff–Δ coupling: "
              "no big_steps_mask or analyze_Jeff_coupling not available.")

    # 4) Geometric torsion–chirality coupling for Z_vec
    torsion_geom = analyze_geometric_torsion_coupling(history, obs, key="Z_vec")
    # 4b) Time-lag geometry → chirality analysis (curvature/torsion predicting future J)
    lag_geom = analyze_lagged_geometry_to_chirality(history, obs, key="Z_vec", max_lag_steps=10)

    # 4c) Chirality curvature index: static nonlinear mapping |J| ≈ f(kappa, tau)
    chi_index = fit_chirality_curvature_index(history, obs, key="Z_vec")

    # 7) Sign-branch structure over geometric chirality potential
    if chi_index is not None:
        branch_geom = analyze_sign_branches_over_chi(
            history, obs, chi_index["coeffs"], key="Z_vec"
        )
    else:
        branch_geom = None

    # 5) Plot J_eff(t) with torsion markers
    plt.figure(figsize=(10, 4))
    plt.plot(t, J, label="J_eff(t)")
    plt.axhline(0.0, color="k", lw=0.8)

    if len(t_flips) > 0:
        plt.scatter(t_flips, np.zeros_like(t_flips),
                    marker="x", s=35, c="red", label="sign flips")
    if len(t_spikes) > 0:
        plt.scatter(t_spikes, np.zeros_like(t_spikes),
                    marker="o", s=20, facecolors="none", edgecolors="orange",
                    label="|dJ/dt| spikes")

    plt.xlabel("t")
    plt.ylabel("J_eff")
    plt.title("Chirality dynamics and torsion-like events")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 5) 3D Z_vec trajectory (if available)
    if history_Zvec_to_xyz is not None and "Z_vec" in history:
        from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

        x, y, z = history_Zvec_to_xyz(history)
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection="3d")
        ax.plot(x, y, z, lw=0.8)
        ax.set_xlabel("Zx")
        ax.set_ylabel("Zy")
        ax.set_zlabel("Zz")
        ax.set_title("Z_vec 3D trajectory")
        plt.tight_layout()
        plt.show()
    else:
        print("[chirality_lab] No Z_vec / geometry_3d available for 3D plot.")

    return {
        "w_vec": w_vec,
        "w_chiral": w_chiral,
        "nl_vec": nl_vec,
        "nl_chiral": nl_chiral,
        "torsion_info": torsion_info,
        "torsion_geom": torsion_geom,
        "lag_geom": lag_geom,
        "chi_index": chi_index,
        "branch_geom": branch_geom,
        "big_steps_mask": big_steps_mask,
    }

if __name__ == "__main__":
    """
    Simple entry point:
      1) run the standard toy_model v3.3 simulation via run_sim.main()
      2) feed (history, obs, big_steps_mask) into run_chirality_lab
    """
    import run_sim

    # run_sim.main() now returns (hist, obs, big_steps_mask)
    hist, obs, big_steps_mask = run_sim.main()

    # run our analysis/visualization lab on that data
    results = run_chirality_lab(hist, obs, big_steps_mask)

    # If you want to see the fitted w printed again here:
    print("\n[chirality_lab] Finished.")
    print("  w_vec     =", results["w_vec"])
    print("  w_chiral  =", results["w_chiral"])
    print("  nl_vec    =", results["nl_vec"])
    print("  nl_chiral =", results["nl_chiral"])
