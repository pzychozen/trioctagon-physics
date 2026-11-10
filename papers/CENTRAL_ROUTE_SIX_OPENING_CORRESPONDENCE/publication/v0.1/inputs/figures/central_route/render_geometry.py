"""Exact inherited geometry, plotted without an invented source width or flow."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

out = Path(__file__).resolve().parent
K = math.sqrt(3) / 12 + math.sqrt(6) / 4
a = K / (1 + math.sqrt(3) / 2)
R = math.sqrt(7) * a / 2
R0 = math.sqrt(13 / 12 - math.sqrt(2) / 2)
theta = np.linspace(0, 2 * math.pi, 1601)
x = K + R * np.cos(theta)
z = R * np.sin(theta)
dist = np.hypot(x, z)

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(10.8, 7.3), facecolor="#ffffff")
fig.subplots_adjust(left=.085, right=.96, top=.84, bottom=.18)
fig.text(.085, .94, "The inherited carrier curve and original sphere", fontsize=18, weight="bold", color="#172d3d")
fig.text(.085, .895, "Median-plane section · unit host width · geometric positions only", fontsize=11.5, color="#4a5d68")

ax.fill(R0 * np.cos(theta), R0 * np.sin(theta), color="#eef3f5", zorder=0)
ax.plot(R0 * np.cos(theta), R0 * np.sin(theta), color="#8d9da7", lw=1.7, ls=(0, (5, 4)), zorder=1)
ax.axhline(0, color="#c9d2d8", lw=1.0, zorder=0)
ax.axvline(0, color="#dbe1e5", lw=1.0, zorder=0)
ax.plot(x, z, color="#3164a8", lw=3.2, zorder=3)
inside = dist <= R0
ax.plot(np.where(inside, x, np.nan), np.where(inside, z, np.nan), color="#087e7c", lw=4.0, zorder=4)
ax.scatter([a, a], [a, -a], s=65, color="#c77528", edgecolor="white", linewidth=1.2, zorder=6)
ax.scatter([0], [0], s=38, color="#152b3a", zorder=6)
ax.scatter([K - R], [0], s=36, color="#087e7c", zorder=6)
ax.scatter([K + R], [0], s=26, color="#3164a8", zorder=6)
ax.annotate("Center O", (0, 0), xytext=(-.20, -.095), fontsize=11, color="#172d3d",
            arrowprops={"arrowstyle": "-", "color": "#6f808a", "lw": .8})
ax.annotate("Closest carrier point\n0.220258 from O", (K - R, 0), xytext=(.65, -.18), fontsize=10.5, color="#075f5d",
            arrowprops={"arrowstyle": "-", "color": "#087e7c", "lw": .9})
ax.annotate("Upper contact P+\nsource-profile center", (a, a), xytext=(.63, .55), fontsize=10.5, color="#92501b",
            arrowprops={"arrowstyle": "-", "color": "#b7793e", "lw": .9})
ax.annotate("Lower contact P−\nsource-profile center", (a, -a), xytext=(-.35, -.44), fontsize=10.5, color="#92501b",
            arrowprops={"arrowstyle": "-", "color": "#b7793e", "lw": .9})
ax.annotate("Farthest point\n1.293162 from O", (K + R, 0), xytext=(.79, .19), fontsize=10.5, color="#244e86",
            arrowprops={"arrowstyle": "-", "color": "#3164a8", "lw": .9})
ax.text(-.54, .37, "Original close sphere\nradius 0.613373", fontsize=10.5, color="#566a76")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-.68, 1.53)
ax.set_ylim(-.69, .70)
ax.set_xlabel("Radial coordinate along the fixed support direction u", labelpad=8, color="#4b5d69")
ax.set_ylabel("Height z", labelpad=8, color="#4b5d69")
ax.tick_params(colors="#5f717c", labelsize=9)
for side in ("left", "bottom"):
    ax.spines[side].set_color("#b4c1c9")

handles = [Line2D([0], [0], color="#3164a8", lw=3, label="Inherited C1 curve"),
           Line2D([0], [0], color="#087e7c", lw=3, label="Portion inside the sphere"),
           Line2D([0], [0], color="#8d9da7", ls="--", lw=1.7, label="Reference sphere section")]
fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(.08, .074), ncol=3, frameon=False, fontsize=10)
fig.text(.085, .040, "The sphere is a geometric reference. Contact centers are shown; source widths and flow directions are not selected.", fontsize=9.5, color="#556b77")
fig.text(.085, .016, "Source: paired-gap geometry v0.1.1 and conditional carrier crossings v0.1. New radial comparison: GPT assessment, 9 November 2026.", fontsize=8.4, color="#6c7d87")
fig.savefig(out / "CENTRAL_ROUTE_GEOMETRY.png", dpi=180, facecolor=fig.get_facecolor())
fig.savefig(out / "CENTRAL_ROUTE_GEOMETRY.svg", facecolor=fig.get_facecolor())
plt.close(fig)
