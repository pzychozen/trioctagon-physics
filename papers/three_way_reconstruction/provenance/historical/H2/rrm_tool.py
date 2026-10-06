
import argparse
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Tuple, List, Dict

# ----------------------------- Core math -----------------------------

def rrm_func(A: float, B: float, C: float = 1.0):
    """
    Build f(x) = (A x^4 - B x^2 + C) / (x^4 - B x^2 + A)
    and its reciprocal g(x) = 1/f(x).
    """
    def f(x):
        return (A*x**4 - B*x**2 + C) / (x**4 - B*x**2 + A)
    def g(x):
        return (x**4 - B*x**2 + A) / (A*x**4 - B*x**2 + C)
    return f, g

def asymptotes_den_x4(a: float, b: float) -> List[float]:
    """
    Real x where denominator x^4 + a x^2 + b = 0.
    Substitute y = x^2 -> y^2 + a y + b = 0.
    Return sorted list of real x asymptotes (±sqrt(y) for y>=0).
    """
    A = 1.0; B = a; C = b
    disc = B*B - 4*A*C
    roots = []
    if disc >= 0:
        y1 = (-B + math.sqrt(disc))/(2*A)
        y2 = (-B - math.sqrt(disc))/(2*A)
        for y in (y1, y2):
            if y >= 0:
                roots.extend([math.sqrt(y), -math.sqrt(y)])
    return sorted(roots)

def stats_in_regions(func, xs: np.ndarray) -> Dict[str, float]:
    regions = {
        "inside": (np.abs(xs) <= 1),
        "outside_left": (xs < -1),
        "outside_right": (xs > 1),
    }
    out = {}
    y_all = func(xs)
    for name, mask in regions.items():
        y = y_all[mask]
        y = y[np.isfinite(y)]
        if y.size == 0:
            out[f"{name}_min"] = float('nan')
            out[f"{name}_max"] = float('nan')
            out[f"{name}_p05"] = float('nan')
            out[f"{name}_p95"] = float('nan')
        else:
            out[f"{name}_min"] = float(np.min(y))
            out[f"{name}_max"] = float(np.max(y))
            out[f"{name}_p05"] = float(np.percentile(y, 5))
            out[f"{name}_p95"] = float(np.percentile(y, 95))
    return out

# ----------------------------- Arc length -----------------------------

def arc_length_from_xy(x: np.ndarray, y: np.ndarray) -> float:
    """
    Numerical arc length of a polyline defined by (x, y). Non-finite points are dropped.
    """
    m = np.isfinite(x) & np.isfinite(y)
    x = x[m]; y = y[m]
    if x.size < 2:
        return float('nan')
    dx = np.diff(x)
    dy = np.diff(y)
    seg = np.sqrt(dx*dx + dy*dy)
    return float(np.sum(seg))

def arc_lengths_by_region(func, xs: np.ndarray, exclude_eps: float = 1e-4) -> Dict[str, float]:
    """
    Compute arc length for three regions:
      - inside: |x| <= 1 - eps
      - outside_left: [min(xs), -1 - eps]
      - outside_right: [1 + eps, max(xs)]
    exclude_eps trims a tiny margin around x = ±1 to avoid asymptote spikes.
    """
    x_min, x_max = xs.min(), xs.max()
    inside_mask = (np.abs(xs) <= (1.0 - exclude_eps))
    left_mask   = (xs < (-1.0 - exclude_eps))
    right_mask  = (xs > ( 1.0 + exclude_eps))

    out = {}
    for name, m in [("inside", inside_mask), ("outside_left", left_mask), ("outside_right", right_mask)]:
        x_reg = xs[m]
        if x_reg.size < 2:
            out[f"{name}_length"] = float('nan')
        else:
            y_reg = func(x_reg)
            out[f"{name}_length"] = arc_length_from_xy(x_reg, y_reg)
    return out

# ----------------------------- Plotting -----------------------------

def plot_family(xs, funcs, labels, title, ylim, outpath):
    plt.figure(figsize=(10, 6))
    for fn, style, label in labels:
        y = funcs[fn](xs)
        plt.plot(xs, y, linestyle=style, label=label)
    plt.ylim(*ylim)
    plt.title(title)
    plt.xlabel("x"); plt.ylabel("value")
    plt.axvline(-1, color='k', alpha=0.15); plt.axvline(1, color='k', alpha=0.15)
    plt.grid(True, alpha=0.3)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig(outpath, dpi=160)
    plt.show()
    plt.close()
    return outpath

# ----------------------------- Presets -----------------------------

def preset_params(name: str) -> Tuple[Tuple[float,float,float], Tuple[float,float,float]]:
    n = name.lower()
    if n in ("9_1", "9-1", "nine_one", "classic"):
        return (9.0, 9.0, 1.0), (math.pi, math.e, 1.0)
    if n in ("pi_e", "π_e", "pi-e"):
        return (math.pi, math.e, 1.0), (9.0, 9.0, 1.0)
    raise ValueError(f"Unknown preset '{name}'. Use 'classic' or 'pi_e'.")

# ----------------------------- Main -----------------------------

def main():
    ap = argparse.ArgumentParser(description="Reciprocal Rational Map analyzer (RRM) + arc-lengths")
    ap.add_argument("--preset", default="classic", help="Preset pair: 'classic' (9,1) or 'pi_e' (π,e).")
    ap.add_argument("--xwide", type=float, nargs=2, default=[-5.0, 5.0], help="Wide x-range [min max].")
    ap.add_argument("--xzoom", type=float, nargs=2, default=[-1.2, 1.2], help="Zoom x-range [min max].")
    ap.add_argument("--ylim_wide", type=float, nargs=2, default=[-50, 50], help="Y-limits for wide plot.")
    ap.add_argument("--ylim_zoom", type=float, nargs=2, default=[-6, 6], help="Y-limits for zoom plot.")
    ap.add_argument("--samples", type=int, default=6000, help="Number of x samples per plot.")
    ap.add_argument("--outdir", default=".", help="Output directory.")
    ap.add_argument("--exclude_eps", type=float, default=1e-4, help="Trim around x=±1 for arc-length calc.")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    (A1, B1, C1), (A2, B2, C2) = preset_params(args.preset)

    f1, g1 = rrm_func(A1, B1, C1)
    f2, g2 = rrm_func(A2, B2, C2)

    funcs = {"f1": f1, "g1": g1, "f2": f2, "g2": g2}

    # Wide & Zoom plots
    xs_wide = np.linspace(args.xwide[0], args.xwide[1], args.samples)
    xs_zoom = np.linspace(args.xzoom[0], args.xzoom[1], args.samples)

    wide_path = os.path.join(args.outdir, "rrm_wide.png")
    zoom_path = os.path.join(args.outdir, "rrm_zoom.png")

    plot_family(
        xs_wide, funcs,
        labels=[("f1", "-", f"f1 ({A1:.3g},{B1:.3g})"), ("g1", "--", "1/f1"),
                ("f2", "-", f"f2 ({A2:.3g},{B2:.3g})"), ("g2", "--", "1/f2")],
        title=f"RRM — Wide View (x ∈ [{args.xwide[0]}, {args.xwide[1]}])",
        ylim=tuple(args.ylim_wide),
        outpath=wide_path
    )

    plot_family(
        xs_zoom, funcs,
        labels=[("f1", "-", f"f1 ({A1:.3g},{B1:.3g})"), ("g1", "--", "1/f1"),
                ("f2", "-", f"f2 ({A2:.3g},{B2:.3g})"), ("g2", "--", "1/f2")],
        title=f"RRM — Zoom Near ±1 (x ∈ [{args.xzoom[0]}, {args.xzoom[1]}])",
        ylim=tuple(args.ylim_zoom),
        outpath=zoom_path
    )

    # Stats inside/outside for each function over the wide xs domain
    rows = []
    for key in ["f1", "g1", "f2", "g2"]:
        s = stats_in_regions(funcs[key], xs_wide)
        s = pd.Series(s, name=key)
        rows.append(s)
    summary = pd.DataFrame(rows)
    summary_path = os.path.join(args.outdir, "rrm_stats.csv")
    summary.to_csv(summary_path)

    # Arc lengths per region
    arc_rows = []
    for key in ["f1", "g1", "f2", "g2"]:
        al = arc_lengths_by_region(funcs[key], xs_wide, exclude_eps=args.exclude_eps)
        arc_rows.append(pd.Series(al, name=key))
    arc_df = pd.DataFrame(arc_rows)
    arc_path = os.path.join(args.outdir, "rrm_arclengths.csv")
    arc_df.to_csv(arc_path)

    # Asymptotes
    def asym_recip(A, B, C):
        disc = B*B - 4*A*C
        roots = []
        if disc >= 0 and A != 0:
            y1 = (B + math.sqrt(disc))/(2*A)
            y2 = (B - math.sqrt(disc))/(2*A)
            for y in (y1, y2):
                if y >= 0:
                    roots.extend([math.sqrt(y), -math.sqrt(y)])
        return sorted(roots)

    asym_f1 = asymptotes_den_x4(-B1, A1)
    asym_g1 = asym_recip(A1, B1, C1)
    asym_f2 = asymptotes_den_x4(-B2, A2)
    asym_g2 = asym_recip(A2, B2, C2)

    asym_df = pd.DataFrame({
        "denominator": [f"x^4 - {B1} x^2 + {A1}", f"{A1} x^4 - {B1} x^2 + {C1}",
                        f"x^4 - {B2} x^2 + {A2}", f"{A2} x^4 - {B2} x^2 + {C2}"],
        "asymptote_x_values": [asym_f1, asym_g1, asym_f2, asym_g2],
        "function": ["f1", "1/f1", "f2", "1/f2"]
    })
    asym_path = os.path.join(args.outdir, "rrm_asymptotes.csv")
    asym_df.to_csv(asym_path, index=False)

    print("Saved plots:", wide_path, zoom_path)
    print("Saved stats:", summary_path)
    print("Saved arc lengths:", arc_path)
    print("Saved asymptotes:", asym_path)

if __name__ == "__main__":
    main()
