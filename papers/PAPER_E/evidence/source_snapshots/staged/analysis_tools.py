# analysis_tools.py
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D)
from geometry_embeddings import history_to_xyz, history_to_torus_xyz, TorusConfig
from geometry_3d import history_to_xyz, history_to_torus_xyz, history_Zvec_to_xyz
from cp_windows import cp_mask_from_phi_indices, default_cp_config
from dual_tetra_mapper import DualTetraConfig, map_history_to_dual_tetra


def plot_history(history):
    """Simple diagnostic plots for kappa, Z, and identity_state."""
    t = history["t"]
    kappa = history["kappa"]
    z = history["z"]
    identity = history["identity_state"]

    # --- κ(t) ---
    plt.figure()
    plt.plot(t, kappa)
    plt.xlabel("time")
    plt.ylabel(r"$\kappa$")
    plt.title(r"$\kappa(t)$ (global amplitude)")
    plt.grid(True)

    # --- Z(t) ---
    plt.figure()
    plt.plot(t, z)
    plt.xlabel("time")
    plt.ylabel("Z")
    plt.title("Emergent Z(t)")
    plt.grid(True)

    # --- identity_state(t) ---
    plt.figure()
    plt.step(t, identity, where="post")
    plt.xlabel("time")
    plt.ylabel("identity_state")
    plt.title("Identity state over time")
    plt.yticks(range(9))  # s0..s8
    plt.grid(True)

    plt.show()

def plot_trajectory_3d(history):
    """
    3D trajectory plot: (x,y,Z) with x,y from (kappa, phi_index),
    Z from history["z"].
    """
    x, y, z = history_to_xyz(history)
    t = history["t"]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # plot the trajectory
    ax.plot(x, y, z)

    ax.set_xlabel("x (kappa cos phi)")
    ax.set_ylabel("y (kappa sin phi)")
    ax.set_zlabel("Z")
    ax.set_title("3D trajectory in (x,y,Z) space")

    # optional: mark start and end
    ax.scatter([x[0]], [y[0]], [z[0]], marker="o")
    ax.scatter([x[-1]], [y[-1]], [z[-1]], marker="^")

    plt.show()

def plot_torus_trajectory_3d(history, R: float = 2.0, r_max: float = 1.0):
    """
    3D trajectory on a torus cell using history_to_torus_xyz.
    """
    X, Y, Z = history_to_torus_xyz(history, R=R, r_max=r_max)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(X, Y, Z)

    # mark start/end
    ax.scatter([X[0]], [Y[0]], [Z[0]], marker="o")
    ax.scatter([X[-1]], [Y[-1]], [Z[-1]], marker="^")

    ax.set_xlabel("X (torus)")
    ax.set_ylabel("Y (torus)")
    ax.set_zlabel("Z (torus)")
    ax.set_title("Torus-embedded trajectory")

    plt.show()

def plot_Zvec_trajectory_3d(history, key: str = "Z_total"):
    """
    3D plot of a stored Z-trajectory over time.

    key:
      - "Z_total" (default): blended alpha*macro + beta*chiral
      - "Z_macro": macro corridor geometry contribution
      - "Z_chiral": pure chiral embedding
      - "Z_vec": legacy alias for total
    """
    x, y, z = history_Zvec_to_xyz(history, key=key)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(x, y, z)
    ax.scatter([x[0]], [y[0]], [z[0]], marker="o")
    ax.scatter([x[-1]], [y[-1]], [z[-1]], marker="^")

    ax.set_xlabel("Zx")
    ax.set_ylabel("Zy")
    ax.set_zlabel("Zz")
    ax.set_title("Z_vec trajectory")

    plt.show()

def plot_Z_components_trajectory_3d(history):
    """
    Convenience view: overlay Z_macro, Z_chiral, and Z_total in separate figures.
    Uses default matplotlib colors (no explicit color choices).
    """
    for key, title in [
        ("Z_macro", "Z_macro trajectory"),
        ("Z_chiral", "Z_chiral trajectory"),
        ("Z_total", "Z_total trajectory"),
    ]:
        if key not in history and key == "Z_total" and "Z_vec" in history:
            key_use = "Z_vec"
        else:
            key_use = key
        if key_use not in history:
            print(f"[analysis_tools] Missing {key}, skipping.")
            continue
        x, y, z = history_Zvec_to_xyz(history, key=key_use)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot(x, y, z)
        ax.scatter([x[0]], [y[0]], [z[0]], marker="o")
        ax.scatter([x[-1]], [y[-1]], [z[-1]], marker="^")
        ax.set_xlabel("Zx")
        ax.set_ylabel("Zy")
        ax.set_zlabel("Zz")
        ax.set_title(title)
        plt.show()

def plot_kappa_z_scatter(history):
    """
    Scatter plot of (kappa, Z) over time.
    Shows how the trajectory fills the amplitude–height plane.
    """
    kappa = history["kappa"]
    z = history["z"]
    t = history["t"]

    plt.figure()
    plt.scatter(kappa, z, s=10)  # default colors, no explicit color choice
    plt.xlabel(r"$\kappa$")
    plt.ylabel("Z")
    plt.title(r"Scatter of $(\kappa, Z)$ over time")

    # optional: mark final point
    plt.scatter([kappa[-1]], [z[-1]], s=40, marker="x")

    plt.grid(True)
    plt.show()

def plot_kappa_z_cp_scatter(history):
    """
    Scatter of (kappa, Z) with CP-window points highlighted.

    - All points: small scatter
    - CP-window points (based on phi_index in CP windows): over-plotted with larger markers
    """
    kappa = history["kappa"]
    z = history["z"]
    phi_idx = history["phi_index"]

    cfg = default_cp_config()
    mask_cp = cp_mask_from_phi_indices(phi_idx, cfg)

    # base scatter: all points
    plt.figure()
    plt.scatter(kappa, z, s=10)  # default color

    # overlay CP-window points (matplotlib will auto-pick another color)
    plt.scatter(kappa[mask_cp], z[mask_cp], s=40, marker="x")

    plt.xlabel(r"$\kappa$")
    plt.ylabel("Z")
    plt.title(r"$(\kappa, Z)$ scatter with CP-window highlights")
    plt.grid(True)
    plt.show()

def plot_dual_tetra_trajectory(history):
    """
    Dual-tetra throat:
    - edges of the two tetrahedra
    - SRG trajectory segmented by cycle_stage
    - CP-window hits marked along the path
    """
    cfg = DualTetraConfig(scale=1.5, throat_radius=1.0)
    path, tetra_A, tetra_B = map_history_to_dual_tetra(history, cfg)

    stages = history["cycle_stage"]
    phi_idx = history["phi_index"]

    # CP mask in sector space
    cp_cfg = default_cp_config()
    mask_cp = cp_mask_from_phi_indices(phi_idx, cp_cfg)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # --- draw tetra edges ---

    edges = [(0, 1), (0, 2), (0, 3),
             (1, 2), (1, 3), (2, 3)]

    def draw_tetra(vertices):
        for i, j in edges:
            xs = [vertices[i, 0], vertices[j, 0]]
            ys = [vertices[i, 1], vertices[j, 1]]
            zs = [vertices[i, 2], vertices[j, 2]]
            ax.plot(xs, ys, zs)  # default color cycling

    draw_tetra(tetra_A)
    draw_tetra(tetra_B)

    # --- draw trajectory segmented by cycle_stage ---

    current_stage = int(stages[0])
    segment = [path[0]]

    for i in range(1, len(path)):
        s = int(stages[i])
        if s == current_stage:
            segment.append(path[i])
        else:
            # flush previous segment
            seg_arr = np.array(segment)
            ax.plot(seg_arr[:, 0], seg_arr[:, 1], seg_arr[:, 2])  # default color
            # start new segment
            segment = [path[i]]
            current_stage = s

    # flush last segment
    if segment:
        seg_arr = np.array(segment)
        ax.plot(seg_arr[:, 0], seg_arr[:, 1], seg_arr[:, 2])

    # --- CP hits as markers along the path ---

    cp_points = path[mask_cp]
    if cp_points.size > 0:
        ax.scatter(cp_points[:, 0], cp_points[:, 1], cp_points[:, 2],
                   marker="x", s=40)  # color left to default cycle

    # mark start and end of the whole trajectory
    ax.scatter([path[0, 0]], [path[0, 1]], [path[0, 2]], marker="o", s=40)
    ax.scatter([path[-1, 0]], [path[-1, 1]], [path[-1, 2]], marker="^", s=40)

    ax.set_xlabel("X (x-basis)")
    ax.set_ylabel("Y (y-basis)")
    ax.set_zlabel("Z (u-basis)")
    ax.set_title("Dual-tetra throat segmented by cycle_stage with CP hits")

    plt.show()

