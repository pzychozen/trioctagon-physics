# refu.py
import numpy as np


# --------------------------
# Memory curve H(t)
# --------------------------
def H(t):
    """
    REFU memory curve H(t), vectorized for numpy arrays.
    """
    t = np.asarray(t, dtype=float)
    a1, b1 = 2.0, 0.5
    a2, b2 = 1.0, 0.3
    lam1, om1 = 1.5, 0.7
    lam2, om2 = 1.0, 0.4
    return (
        a1 * np.exp(-b1 * t) * np.cos(t)
        + a2 * np.exp(-b2 * t) * np.sin(t)
        + lam1 * np.exp(-om1 * t)
        + lam2 * np.exp(-om2 * t)
    )


def compute_Hmax(t0, t1, n=20000, eps=1e-12):
    """
    Robust max |H(t)| on [t0,t1] via dense sampling.
    """
    t_grid = np.linspace(float(t0), float(t1), int(n), endpoint=True)
    vals = np.abs(H(t_grid))
    return float(np.max(vals) + eps)


# --------------------------
# RPCO
# --------------------------
def rpco(x, L=9.0, eps=1e-9, mode="paper"):
    """
    Recursive Phase-Compression Operator (RPCO)

    mode="paper":
        exp( clip( log(|x|+eps) * sign(x), -L, L ) )
        (strictly positive output)

    mode="signed":
        sign(x) * exp( clip( log(|x|+eps), -L, L ) )
        (sign-preserving output)

    Notes:
      - eps must be > 0.
      - L controls the hard bound via exp(±L).
    """
    if eps <= 0:
        raise ValueError("rpco eps must be > 0")

    x = np.asarray(x, dtype=float)
    mag = np.abs(x) + float(eps)
    log_mag = np.log(mag)

    if mode == "paper":
        z = log_mag * np.sign(x)
        z = np.clip(z, -float(L), float(L))
        return np.exp(z)

    if mode == "signed":
        z = np.clip(log_mag, -float(L), float(L))
        return np.sign(x) * np.exp(z)

    raise ValueError("rpco mode must be 'paper' or 'signed'")


# --------------------------
# REFU step + rollout
# --------------------------
def refu_step(
    Theta,
    t,
    dt,
    lam,
    tgmo_fn=None,
    use_tgmo=True,
    use_H=True,
    H_func=H,
    Hmax=None,
    D_fn=None,
    nonlinear_fn=None,
    use_rpco=True,
    rpco_L=9.0,
    rpco_eps=1e-9,
    rpco_mode="paper",
    detect_saturation=False,
):
    """
    One REFU update step.

    Order:
      pre = Theta
      if TGMO: pre += dt * tgmo_fn(Theta)
      if nonlinear: pre += nonlinear_fn(D_fn(Theta,t))
      if H: factor = 1 + lam * H(t)/Hmax; pre *= factor
      if RPCO: pre = rpco(pre)
      return pre, saturated_flag
    """
    Theta = np.asarray(Theta, dtype=float)
    dt = float(dt)
    lam = float(lam)
    t = float(t)

    pre = Theta

    # TGMO contribution (discrete toroidal Laplacian or similar)
    if use_tgmo:
        if tgmo_fn is None:
            raise ValueError("use_tgmo=True but tgmo_fn is None")
        pre = pre + dt * np.asarray(tgmo_fn(Theta), dtype=float)

    # Optional nonlinear injection
    if (D_fn is not None) and (nonlinear_fn is not None):
        Dval = D_fn(Theta, t)
        pre = pre + np.asarray(nonlinear_fn(Dval), dtype=float)

    # Global memory modulation
    if use_H:
        if Hmax is None:
            raise ValueError("use_H=True requires a valid Hmax (computed in run_refu).")
        ht = float(H_func(t))
        factor = 1.0 + lam * (ht / float(Hmax))
        pre = factor * pre

    # Optional compression
    saturated = False
    if use_rpco:
        pre = rpco(pre, L=rpco_L, eps=rpco_eps, mode=rpco_mode)
        if detect_saturation:
            # Detect collapse to a constant field (common when saturating at exp(L))
            saturated = bool(np.allclose(pre, pre.flat[0]))

    return pre, saturated


def run_refu(
    Theta0,
    steps=2000,
    dt=0.05,
    lam=0.05,
    tgmo_fn=None,
    use_tgmo=True,
    use_H=True,
    H_func=H,
    compute_global_Hmax=True,
    Hmax=None,
    D_fn=None,
    nonlinear_fn=None,
    use_rpco=True,
    rpco_L=9.0,
    rpco_eps=1e-9,
    rpco_mode="paper",
    return_history=True,
    detect_saturation=False,
):
    """
    Rollout REFU for `steps` updates.

    Returns:
      - hist: array of shape (steps+1, ...) if return_history=True
        else final Theta
      - (optional) saturation_steps list if detect_saturation=True
    """
    Theta = np.asarray(Theta0, dtype=float)
    steps = int(steps)
    dt = float(dt)

    # Compute Hmax over the full horizon (recommended)
    if use_H:
        if compute_global_Hmax:
            t0 = 0.0
            t1 = steps * dt
            Hmax = compute_Hmax(t0, t1, n=max(20000, 10 * steps))
        else:
            if Hmax is None:
                raise ValueError("use_H=True but compute_global_Hmax=False and Hmax=None")
    else:
        Hmax = None  # unused

    saturation_steps = []

    if return_history:
        hist = [Theta.copy()]

    for n in range(steps):
        t = n * dt
        Theta, saturated = refu_step(
            Theta=Theta,
            t=t,
            dt=dt,
            lam=lam,
            tgmo_fn=tgmo_fn,
            use_tgmo=use_tgmo,
            use_H=use_H,
            H_func=H_func,
            Hmax=Hmax,
            D_fn=D_fn,
            nonlinear_fn=nonlinear_fn,
            use_rpco=use_rpco,
            rpco_L=rpco_L,
            rpco_eps=rpco_eps,
            rpco_mode=rpco_mode,
            detect_saturation=detect_saturation,
        )

        if detect_saturation and saturated:
            saturation_steps.append(n)

        if return_history:
            hist.append(Theta.copy())

    if return_history:
        hist = np.asarray(hist, dtype=float)
        if detect_saturation:
            return hist, saturation_steps
        return hist

    if detect_saturation:
        return Theta, saturation_steps
    return Theta


# --------------------------
# Quick self-test
# --------------------------
if __name__ == "__main__":
    # Minimal sanity test without TGMO (pure modulation + rpc)
    np.random.seed(0)
    Theta0 = np.random.randn(64, 64)

    # D(t)=Theta with tanh injection
    D_fn = lambda Th, t: Th
    nonlinear_fn = lambda D: 0.1 * np.tanh(D / 7.2)

    hist, sat = run_refu(
        Theta0,
        steps=200,
        dt=0.05,
        lam=0.05,
        tgmo_fn=None,
        use_tgmo=False,
        use_H=True,
        D_fn=D_fn,
        nonlinear_fn=nonlinear_fn,
        use_rpco=True,
        rpco_L=9,
        rpco_eps=2e-9,
        rpco_mode="paper",
        return_history=True,
        detect_saturation=True,
    )

    final = hist[-1]
    print("final mean/std/min/max:", float(final.mean()), float(final.std()), float(final.min()), float(final.max()))
    print("saturation steps:", sat[:10], ("..." if len(sat) > 10 else ""))
