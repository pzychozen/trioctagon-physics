"""Illustrate a proved radial enclosure. Plot samples are not the proof.

Requires matplotlib and numpy only for rendering; verification is independent.
Outputs PNG and SVG beside this script without touching retained source files.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "svg.fonttype": "none",
})

r = np.sqrt(3) / 6
a = (1 - np.sqrt(2) / 2) / 2
h = (np.sqrt(2) - 1) / 2
H = 0.5
D = np.sqrt(10 - 6 * np.sqrt(2))
K = np.sqrt(3) / 12 + np.sqrt(6) / 4
ac = K / (1 + np.sqrt(3) / 2)
R = np.sqrt(7) * ac / 2

fig = plt.figure(figsize=(12.6, 7.8), facecolor="white")
grid = fig.add_gridspec(1, 2, left=0.07, right=0.97, bottom=0.27,
                       top=0.79, width_ratios=(1.0, 1.0), wspace=0.25)
axes = [fig.add_subplot(grid[0, i]) for i in range(2)]
z_band = np.linspace(h, H, 400)
enclosure = D * ((1 - (z_band - h) / (H - h)) * a
                 + (z_band - h) / (H - h) * r)
theta = np.linspace(0, np.pi, 1600)
rho_circle = K + R * np.cos(theta)
z_circle = R * np.sin(theta)
green, blue, gray = "#168C78", "#244B93", "#5E6873"

for ax in axes:
    ax.fill_betweenx(z_band, 0, enclosure, color=green, alpha=0.16,
                     label="Enclosure of all individual G hulls")
    ax.plot(enclosure, z_band, color=green, lw=2)
    heights = np.linspace(0, 0.55, 500)
    ax.plot(0.6 * heights + 0.06, heights, "--", color=gray, lw=1.5,
            label=r"Separating bound: $\rho=0.6|\zeta|+0.06$")
    ax.plot(rho_circle, z_circle, color=blue, lw=2.6,
            label=r"Retained carrier $\Gamma_j$ (radial projection)")
    ax.set_ylim(0, 0.56)
    ax.set_xlabel(r"Cylindrical radius $\rho$ about the axis through $O$")
    ax.set_ylabel(r"Absolute height $|\zeta|$ from $O$")
    ax.grid(alpha=0.17)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(colors="#334155")

axes[0].set_xlim(0, 1.34)
axes[0].set_title("Entire inherited carrier", loc="left", pad=12)
axes[1].set_xlim(0.12, 0.64)
axes[1].set_title("Closest branch and the central enclosure", loc="left", pad=12)
axes[1].annotate("No intersection", xy=(0.295, 0.30), xytext=(0.395, 0.16),
                 fontsize=11, color=blue,
                 arrowprops={"arrowstyle": "-", "color": blue, "lw": 1.1})

fig.suptitle("Six-opening correspondence: a geometric separation",
             x=0.07, y=0.965, ha="left", fontsize=20, weight="bold",
             color="#18283D")
fig.text(0.07, 0.902,
         "Proposed result for independent review • Width one • Both hands • Entire admitted static family",
         fontsize=11, color="#52616F")
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower left", bbox_to_anchor=(0.063, 0.08),
           frameon=False, fontsize=10, ncol=1, handlelength=3)
fig.text(0.07, 0.025,
         "Shading is a mathematical bounding region, not an adopted aperture. "
         "The exact proof gives distance > 0.0594 × common host width.",
         fontsize=10, color="#52616F")
fig.savefig(HERE / "SIX_OPENING_SEPARATION.png", dpi=180, facecolor="white")
fig.savefig(HERE / "SIX_OPENING_SEPARATION.svg", facecolor="white")
print("Rendered SIX_OPENING_SEPARATION.png and SIX_OPENING_SEPARATION.svg")
