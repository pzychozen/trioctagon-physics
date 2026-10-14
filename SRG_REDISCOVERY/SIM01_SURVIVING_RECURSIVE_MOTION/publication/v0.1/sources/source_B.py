import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
import os

# --- Simulation Parameters ---
TORUS_SIZE = 10.0
NUM_TETRAHEDRONS = 8
STEP_COUNT = 2000
DT = 0.1  # Time step
VELOCITY_SCALE = 0.2

# Initialize positions and velocities
positions = np.random.rand(NUM_TETRAHEDRONS, 3) * TORUS_SIZE
velocities = (np.random.rand(NUM_TETRAHEDRONS, 3) - 0.5) * VELOCITY_SCALE

# Tetrahedron geometry (relative vertices, normalized)
tetrahedron_template = np.array([
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
]) * 0.5  # Scale to fit within a reasonable size

faces = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]

# Helper functions
def wrap_position(pos):
    """Wrap positions toroidally within [0, TORUS_SIZE]."""
    return np.mod(pos, TORUS_SIZE)

def H(t):
    """REFU memory curve function."""
    a1, b1 = 2.0, 0.5
    alpha2, b2 = 1.0, 0.3
    lambda1, omega1 = 1.5, 0.7
    lambda2, omega2 = 1.0, 0.4
    return (a1 * np.exp(-b1 * t) * np.cos(t) +
            alpha2 * np.exp(-b2 * t) * np.sin(t) +
            lambda1 * np.exp(-omega1 * t) +
            lambda2 * np.exp(-omega2 * t))

def RPCO(v):
    """RPCO damping function."""
    return v / (1 + np.log1p(np.abs(v)))

def GRF(positions, t):
    """Glyph Retention Factor (simplified, based on position stability)."""
    vel_mags = np.linalg.norm(velocities, axis=1)
    return 1.0 / (1.0 + np.mean(vel_mags))  # Higher stability = higher GRF

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, TORUS_SIZE)
ax.set_ylim(0, TORUS_SIZE)
ax.set_zlim(0, TORUS_SIZE)
ax.set_title("Tetrahedral Attractors in Toroidal Space")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Initialize collections
collections = []
for i in range(NUM_TETRAHEDRONS):
    verts = [positions[i] + tetrahedron_template[face] for face in faces]
    poly = Poly3DCollection(verts, alpha=0.6)
    poly.set_facecolor(plt.cm.viridis(i / NUM_TETRAHEDRONS))
    ax.add_collection3d(poly)
    collections.append(poly)

# Animation function
def update(frame):
    global positions, velocities
    t = frame * DT

    # Compute GRF
    grf_val = GRF(positions, t)

    # Update dynamics with REFU and RPCO
    h_val = H(t)
    for i in range(NUM_TETRAHEDRONS):
        # Simple inter-tetrahedron interaction (attraction to centroid)
        centroid = np.mean(positions, axis=0)
        diff = centroid - positions[i]
        diff = wrap_position(diff + TORUS_SIZE / 2) - TORUS_SIZE / 2
        force = diff / (np.linalg.norm(diff) + 1e-2) * h_val

        # Update velocity with REFU * force and RPCO damping
        velocities[i] += DT * force * grf_val
        velocities[i] = RPCO(velocities[i])

        # Update position
        positions[i] += DT * velocities[i]
        positions[i] = wrap_position(positions[i])

    # Update collections (replace instead of clear)
    for i, poly in enumerate(collections):
        verts = [positions[i] + tetrahedron_template[face] for face in faces]
        poly.set_verts(verts)
        poly.set_facecolor(plt.cm.viridis((i + frame) % NUM_TETRAHEDRONS / NUM_TETRAHEDRONS))

    return collections

# Run animation
ani = FuncAnimation(fig, update, frames=STEP_COUNT, interval=50, blit=True)

# Save animation (optional, requires ffmpeg)
output_path = "tetrahedral_attractors_animation.mp4"
try:
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    ani.save(output_path, writer="ffmpeg", fps=60)
    print(f"Animation saved to {output_path}")
except Exception as e:
    print(f"Failed to save animation: {e}. Displaying instead. Ensure ffmpeg is installed.")
    plt.show()  # Fall back to displaying if save fails
else:
    plt.show()  # Show after successful save if desired