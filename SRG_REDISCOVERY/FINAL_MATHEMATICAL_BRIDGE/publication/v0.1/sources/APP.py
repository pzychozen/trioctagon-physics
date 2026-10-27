# -*- coding: utf-8 -*-
"""SRG Operators Lab (TGMO / RPCO / REFU)

This Streamlit app is an exploratory interface for the *implemented* numerical operators:
- TGMO: Toroidal Gradient Memory Operator (toroidal Laplacian diffusion)
- RPCO: Recursive Phase-Compression Operator (bounded nonlinear compression)
- REFU: Recursive Field Update (TGMO + nonlinear injection + memory modulation + optional RPCO)

Design intent:
- Reproducible runs (seeded init + explicit parameters)
- Operator-first behavior exploration
- Practical performance defaults (streaming rollout; optional full history for small runs)
"""

from __future__ import annotations

import io
import json
from dataclasses import asdict, dataclass

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from tgmo import make_tgmo_fn
from refu import refu_step, run_refu, compute_Hmax, H


# --------------------------
# Page
# --------------------------
st.set_page_config(page_title="SRG Operators Lab", layout="wide")

st.title("Recursive Operators Lab (TGMO / RPCO / REFU)")
st.caption("Tune parameters, run rollouts, visualize structure, export metrics & config.")


# --------------------------
# Sidebar: parameters
# --------------------------
st.sidebar.header("Run Settings")
seed = st.sidebar.number_input("Seed", value=0, step=1)
n_theta = st.sidebar.selectbox("n_theta", [64, 128, 256], index=1)
n_phi = st.sidebar.selectbox("n_phi", [64, 128, 256], index=1)
steps = st.sidebar.slider("steps", 100, 10000, 2000, 100)
dt = st.sidebar.number_input("dt", value=0.05, step=0.01, format="%.4f")

st.sidebar.header("TGMO")
a = st.sidebar.number_input("a (major radius scale)", value=1.0, step=0.1, format="%.3f")
b = st.sidebar.number_input("b (minor radius scale)", value=0.6, step=0.1, format="%.3f")
periodic_r = st.sidebar.checkbox("periodic_r (3D only)", value=False)

st.sidebar.header("RPCO")
L = st.sidebar.slider("L (clip bound)", 1.0, 20.0, 10.0, 0.5)
eps = st.sidebar.number_input("eps", value=1e-6, format="%.1e")
rpco_mode = st.sidebar.selectbox("rpco_mode", ["paper", "signed"], index=0)

st.sidebar.header("REFU / Memory")
lam = st.sidebar.slider("lambda (H sensitivity)", 0.0, 5.0, 0.5, 0.05)
use_H = st.sidebar.checkbox("use H(t)", value=True)

st.sidebar.header("D(t) + Nonlinear")
use_D = st.sidebar.checkbox("use D(t)=Theta with tanh", value=True)
kappa = st.sidebar.slider("kappa (nonlinear strength)", 0.0, 2.0, 0.1, 0.01)
scale = st.sidebar.slider("scale (tanh divisor)", 0.1, 10.0, 1.0, 0.1)

st.sidebar.header("Ablations")
use_tgmo = st.sidebar.checkbox("use TGMO", value=True)
use_rpco = st.sidebar.checkbox("use RPCO", value=True)

st.sidebar.header("Performance")
diagnostic_samples = st.sidebar.slider("diagnostic samples (≈ rows in CSV)", 50, 400, 200, 10)
store_full_history = st.sidebar.checkbox("store full history (RAM heavy)", value=False)


# --------------------------
# Helpers: metrics
# --------------------------
def spectral_entropy(field2d: np.ndarray) -> float:
    """Basic spectral entropy on rfft2 power spectrum."""
    F = np.fft.rfft2(field2d)
    P = np.abs(F) ** 2
    p = P.ravel()
    s = float(p.sum())
    if s <= 0:
        return 0.0
    p = p / s
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


def grad_energy(field2d: np.ndarray) -> float:
    gx = np.roll(field2d, -1, axis=0) - field2d
    gy = np.roll(field2d, -1, axis=1) - field2d
    return float(np.mean(gx * gx + gy * gy))


def basic_stats(field: np.ndarray) -> dict:
    return {
        "mean": float(np.mean(field)),
        "std": float(np.std(field)),
        "min": float(np.min(field)),
        "max": float(np.max(field)),
    }


def autocorr_lag1_theta(field2d: np.ndarray) -> float:
    f = field2d - np.mean(field2d)
    denom = float(np.mean(f * f) + 1e-12)
    f1 = np.roll(f, 1, axis=0)
    return float(np.mean(f * f1) / denom)


def step_change(prev2d: np.ndarray, cur2d: np.ndarray) -> float:
    d = cur2d - prev2d
    return float(np.sqrt(np.mean(d * d)))


def est_history_bytes(nsteps: int, n0: int, n1: int) -> int:
    return int((nsteps + 1) * n0 * n1 * 8)  # float64


@st.cache_data(show_spinner=False)
def cached_Hmax(t1: float, n: int) -> float:
    return compute_Hmax(0.0, float(t1), n=int(n))


def make_run_id() -> str:
    return (
        f"N{int(n_theta)}x{int(n_phi)}_steps{int(steps)}_dt{float(dt):.4g}"
        f"_a{float(a):.3g}_b{float(b):.3g}_L{float(L):.3g}_eps{float(eps):.2e}"
        f"_lam{float(lam):.3g}_H{int(bool(use_H))}_D{int(bool(use_D))}"
        f"_tgmo{int(bool(use_tgmo))}_rpco{int(bool(use_rpco))}"
        f"_mode{rpco_mode}_seed{int(seed)}"
    )


@dataclass
class RunConfig:
    seed: int
    n_theta: int
    n_phi: int
    steps: int
    dt: float
    a: float
    b: float
    periodic_r: bool
    L: float
    rpco_eps: float
    rpco_mode: str
    lam: float
    use_H: bool
    use_D: bool
    kappa: float
    scale: float
    use_tgmo: bool
    use_rpco: bool
    diagnostic_samples: int
    store_full_history: bool


def compute_row(
    i_step: int,
    Theta: np.ndarray,
    prev_sample: np.ndarray | None,
    Hmax_val: float | None,
) -> tuple[dict, np.ndarray]:
    fp = float(np.mean(np.sin(Theta) + 0.37 * np.cos(3.0 * Theta)))
    delta = 0.0 if prev_sample is None else step_change(prev_sample, Theta)

    ht = float(H(i_step * float(dt))) if use_H else 0.0
    if use_H and Hmax_val is not None:
        Hnorm = ht / float(Hmax_val)
        factor = 1.0 + float(lam) * Hnorm
    else:
        Hnorm = 0.0
        factor = 1.0

    row = {
        "step": int(i_step),
        "t": float(i_step) * float(dt),
        "fingerprint": fp,
        "delta_rms": float(delta),
        **basic_stats(Theta),
        "grad_energy": grad_energy(Theta),
        "spec_entropy": spectral_entropy(Theta),
        "autocorr_lag1": autocorr_lag1_theta(Theta),
        "Hmax": float(Hmax_val) if (use_H and Hmax_val is not None) else 1.0,
        "Hnorm": float(Hnorm),
        "factor": float(factor),
        "H(t)": float(ht),
    }
    return row, Theta.copy()


# --------------------------
# Operator definitions (quick, as-implemented)
# --------------------------
with st.expander("Operator definitions (as implemented)", expanded=False):
    st.markdown(
        r"""
**TGMO (toroidal Laplacian):**  
\[
\nabla_T^2 \Theta = \frac{1}{a^2}\nabla_\theta^2 \Theta + \frac{1}{b^2}\nabla_\phi^2 \Theta \;(+\; \nabla_r^2 \Theta\ \text{in 3D})
\]

**RPCO (bounded compression, elementwise):**  
- `mode=\"paper\"`: \(\exp(\mathrm{clip}(\log(|x|+\varepsilon)\,\mathrm{sign}(x),-L,L))\) (strictly positive output)  
- `mode=\"signed\"`: \(\mathrm{sign}(x)\exp(\mathrm{clip}(\log(|x|+\varepsilon),-L,L))\)

**REFU (composite update):**  
Pre-update: \(\tilde\Theta \leftarrow \Theta + \Delta t\,\nabla_T^2\Theta + \mathrm{Nonlinear}(D(\Theta,t))\) (optional TGMO / nonlinear)  
Global modulation: \(\Theta^\* \leftarrow (1+\lambda\,H(t)/H_{\max})\,\tilde\Theta\) (optional \(H\))  
Compression: \(\Theta \leftarrow \mathrm{RPCO}(\Theta^\*)\) (optional RPCO)
        """
    )


# --------------------------
# Run
# --------------------------
colA, colB = st.columns([1, 1])

bytes_est = est_history_bytes(int(steps), int(n_theta), int(n_phi))
st.sidebar.caption(f"Est. full-history RAM: ~{bytes_est/1024/1024:.1f} MiB (float64)")
if store_full_history and bytes_est > 1200 * 1024 * 1024:
    st.sidebar.warning("This run will likely exceed RAM if you store full history. Consider turning it off.")

if st.button("Run rollout"):
    np.random.seed(int(seed))
    Theta0 = np.random.randn(int(n_theta), int(n_phi)).astype(float)

    tgmo_fn = make_tgmo_fn(a=float(a), b=float(b), periodic_r=bool(periodic_r))

    # D(t)=Theta, Nonlinear=tanh (optional)
    D_fn = (lambda Theta, t: Theta) if use_D else None
    nonlinear_fn = (lambda D: float(kappa) * np.tanh(D / float(scale))) if use_D else None

    # Precompute Hmax once (and cache across reruns)
    if use_H:
        t1 = float(steps) * float(dt)
        n_grid = max(20000, 10 * int(steps))
        Hmax_val = cached_Hmax(t1, n_grid)
    else:
        Hmax_val = None

    stride = max(1, int(steps // int(diagnostic_samples)))
    use_history = bool(store_full_history) and (bytes_est <= 1200 * 1024 * 1024)

    cfg = RunConfig(
        seed=int(seed),
        n_theta=int(n_theta),
        n_phi=int(n_phi),
        steps=int(steps),
        dt=float(dt),
        a=float(a),
        b=float(b),
        periodic_r=bool(periodic_r),
        L=float(L),
        rpco_eps=float(eps),
        rpco_mode=str(rpco_mode),
        lam=float(lam),
        use_H=bool(use_H),
        use_D=bool(use_D),
        kappa=float(kappa),
        scale=float(scale),
        use_tgmo=bool(use_tgmo),
        use_rpco=bool(use_rpco),
        diagnostic_samples=int(diagnostic_samples),
        store_full_history=bool(store_full_history),
    )
    run_id = make_run_id()

    st.write(f"**run_id:** `{run_id}`")
    if use_H:
        st.write(f"**Hmax (cached):** {Hmax_val:.6g}")

    rows: list[dict] = []
    progress = st.progress(0.0, text="running rollout...")

    if use_history:
        hist = run_refu(
            Theta0=Theta0,
            steps=int(steps),
            dt=float(dt),
            lam=float(lam),
            tgmo_fn=tgmo_fn,
            use_tgmo=bool(use_tgmo),
            use_H=bool(use_H),
            compute_global_Hmax=False,
            Hmax=Hmax_val,
            D_fn=D_fn,
            nonlinear_fn=nonlinear_fn,
            use_rpco=bool(use_rpco),
            rpco_L=float(L),
            rpco_eps=float(eps),
            rpco_mode=str(rpco_mode),
            return_history=True,
            detect_saturation=False,
        )

        prev_sample = None
        for i in range(0, len(hist), stride):
            row, prev_sample = compute_row(i_step=i, Theta=hist[i], prev_sample=prev_sample, Hmax_val=Hmax_val)
            rows.append(row)

        if rows[-1]["step"] != len(hist) - 1:
            row, _ = compute_row(i_step=len(hist) - 1, Theta=hist[-1], prev_sample=prev_sample, Hmax_val=Hmax_val)
            rows.append(row)

        final = hist[-1]
        snap0 = hist[0]
        snapm = hist[len(hist) // 2]
        snapf = hist[-1]
        progress.progress(1.0, text="done")

    else:
        Theta = Theta0.copy()
        prev_sample = None

        row0, prev_sample = compute_row(i_step=0, Theta=Theta, prev_sample=None, Hmax_val=Hmax_val)
        rows.append(row0)

        mid_step = int(steps) // 2
        snap0 = Theta0
        snapm = None

        update_every = max(1, int(steps // 200))

        for n in range(int(steps)):
            t = float(n) * float(dt)
            Theta, _ = refu_step(
                Theta=Theta,
                t=t,
                dt=float(dt),
                lam=float(lam),
                tgmo_fn=tgmo_fn,
                use_tgmo=bool(use_tgmo),
                use_H=bool(use_H),
                H_func=H,
                Hmax=Hmax_val,
                D_fn=D_fn,
                nonlinear_fn=nonlinear_fn,
                use_rpco=bool(use_rpco),
                rpco_L=float(L),
                rpco_eps=float(eps),
                rpco_mode=str(rpco_mode),
                detect_saturation=False,
            )

            i_step = n + 1

            if i_step == mid_step:
                snapm = Theta.copy()

            if (i_step % stride == 0) or (i_step == int(steps)):
                row, prev_sample = compute_row(i_step=i_step, Theta=Theta, prev_sample=prev_sample, Hmax_val=Hmax_val)
                rows.append(row)

            if (n % update_every) == 0:
                progress.progress(min(0.999, float(n + 1) / float(steps)), text="running rollout...")

        final = Theta
        snapf = final
        if snapm is None:
            snapm = final.copy()

        progress.progress(1.0, text="done")

    df = pd.DataFrame(rows)

    st.write(f"stride={stride} | rows={len(df)} | mode={'history' if use_history else 'streaming'}")
    st.write("final stats:", basic_stats(final))
    st.dataframe(df.tail(5), use_container_width=True)

    # --------------------------
    # Plots
    # --------------------------
    with colA:
        st.subheader("Field snapshots")
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        ims = []
        for ax, title, snap in zip(axes, ["initial Θ", "mid Θ", "final Θ"], [snap0, snapm, snapf]):
            im = ax.imshow(snap, aspect="auto")
            ax.set_title(title)
            ax.set_xticks([])
            ax.set_yticks([])
            ims.append(im)
        fig.colorbar(ims[-1], ax=axes.ravel().tolist(), shrink=0.75)
        st.pyplot(fig)

    with colB:
        st.subheader("Diagnostics")
        st.dataframe(df, use_container_width=True)

        fig1 = plt.figure()
        plt.plot(df["t"], df["std"])
        plt.title("std(Θ) over time")
        plt.xlabel("t")
        plt.ylabel("std")
        st.pyplot(fig1)

        fig2 = plt.figure()
        plt.plot(df["t"], df["grad_energy"])
        plt.title("gradient energy over time")
        plt.xlabel("t")
        plt.ylabel("E_grad")
        st.pyplot(fig2)

        fig3 = plt.figure()
        plt.plot(df["t"], df["spec_entropy"])
        plt.title("spectral entropy over time")
        plt.xlabel("t")
        plt.ylabel("H_spec")
        st.pyplot(fig3)

        fig4 = plt.figure()
        plt.plot(df["t"], df["delta_rms"])
        plt.title("sample-to-sample RMS change")
        plt.xlabel("t")
        plt.ylabel("delta_rms")
        st.pyplot(fig4)

        if use_H:
            fig5 = plt.figure()
            plt.plot(df["t"], df["H(t)"])
            plt.title("H(t) (memory curve)")
            plt.xlabel("t")
            plt.ylabel("H")
            st.pyplot(fig5)

            fig6 = plt.figure()
            plt.plot(df["t"], df["factor"])
            plt.title("global factor(t) = 1 + λ H(t)/Hmax")
            plt.xlabel("t")
            plt.ylabel("factor")
            st.pyplot(fig6)

    # --------------------------
    # Exports
    # --------------------------
    st.subheader("Export")

    st.download_button(
        "Download metrics CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"{run_id}__metrics.csv",
        mime="text/csv",
    )

    cfg_json = json.dumps(asdict(cfg), indent=2).encode("utf-8")
    st.download_button(
        "Download run config JSON",
        data=cfg_json,
        file_name=f"{run_id}__config.json",
        mime="application/json",
    )

    buf = io.BytesIO()
    np.save(buf, final)
    st.download_button(
        "Download final Θ as .npy",
        data=buf.getvalue(),
        file_name=f"{run_id}__final_theta.npy",
        mime="application/octet-stream",
    )

    st.json(asdict(cfg))
