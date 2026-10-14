import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
import os
import csv
import time

# --- Simulation Parameters ---
TORUS_SIZE = 10.0
NUM_TETRAHEDRONS = 8
STEP_COUNT = 200
DT = 0.1  # Time step
VELOCITY_SCALE = 0.2

# Initialize positions and velocities
positions = np.random.rand(NUM_TETRAHEDRONS, 3) * TORUS_SIZE
velocities = (np.random.rand(NUM_TETRAHEDRONS, 3) - 0.5) * VELOCITY_SCALE

# Tetrahedron geometry
tetrahedron_template = np.array([
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
]) * 0.5

faces = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]

# Helper functions
def wrap_position(pos):
    """Wrap positions toroidally within [0, TORUS_SIZE] with teleport detection."""
    wrapped = np.mod(pos, TORUS_SIZE)
    return wrapped

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
    """Glyph Retention Factor based on velocity stability."""
    vel_mags = np.linalg.norm(velocities, axis=1)
    return 1.0 / (1.0 + np.mean(vel_mags))

# Energy tracking
def compute_energy(positions, velocities):
    """Compute total kinetic energy of the system."""
    kinetic_energy = 0.5 * np.sum(np.linalg.norm(velocities, axis=1) ** 2)
    potential_energy = 0.0  # Placeholder: Add pairwise potential if needed
    return kinetic_energy + potential_energy

# Teleport detection
def detect_teleport(prev_positions, new_positions, threshold=1.0):
    """Detect if a tetrahedron teleports by checking large position jumps."""
    teleports = []
    for i in range(NUM_TETRAHEDRONS):
        distance = np.linalg.norm(wrap_position(new_positions[i] - prev_positions[i]))
        if distance > threshold:
            teleports.append((i, distance, new_positions[i], prev_positions[i]))
    return teleports

# CSV export setup
timestamp = time.strftime("%Y%m%d_%H%M%S")
csv_path = f"tetrahedral_states_{timestamp}.csv"
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Step", "Tetrahedron", "X", "Y", "Z", "VX", "VY", "VZ", "Energy", "GRF", "Rule_State"])

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, TORUS_SIZE)
ax.set_ylim(0, TORUS_SIZE)
ax.set_zlim(0, TORUS_SIZE)
ax.set_title("Tetrahedral Attractors with Energy and Teleport Tracking")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

collections = []
for i in range(NUM_TETRAHEDRONS):
    verts = [positions[i] + tetrahedron_template[face] for face in faces]
    poly = Poly3DCollection(verts, alpha=0.6)
    poly.set_facecolor(plt.cm.viridis(i / NUM_TETRAHEDRONS))
    ax.add_collection3d(poly)
    collections.append(poly)

# Animation function
def update(frame):
    global positions, velocities, rule_state
    t = frame * DT
    grf_val = GRF(positions, t)
    h_val = H(t)

    # Store previous positions for teleport detection
    prev_positions = positions.copy()

    for i in range(NUM_TETRAHEDRONS):
        centroid = np.mean(positions, axis=0)
        diff = centroid - positions[i]
        diff = wrap_position(diff + TORUS_SIZE / 2) - TORUS_SIZE / 2
        norm = np.linalg.norm(diff) + 1e-2

        # Recursive logic rule switch
        if grf_val > 0.5 and np.random.rand() < 0.01:
            rule_state[i] = 1 - rule_state[i]

        # Apply force based on rule state
        force = diff / norm * h_val * (-1 if rule_state[i] else 1)

        # Update velocity and position
        velocities[i] += DT * force * grf_val
        velocities[i] = RPCO(velocities[i])
        positions[i] += DT * velocities[i]
        positions[i] = wrap_position(positions[i])

    # Energy tracking
    energy = compute_energy(positions, velocities)

    # Teleport detection
    teleports = detect_teleport(prev_positions, positions)
    if teleports:
        print(f"Step {frame}: Teleport detected - {teleports}")

    # Update collections
    for i, poly in enumerate(collections):
        verts = [positions[i] + tetrahedron_template[face] for face in faces]
        poly.set_verts(verts)
        color_idx = (i + frame) % NUM_TETRAHEDRONS / NUM_TETRAHEDRONS
        poly.set_facecolor(plt.cm.viridis(color_idx) if rule_state[i] == 0 else plt.cm.Reds(color_idx))

    # CSV export
    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(NUM_TETRAHEDRONS):
            writer.writerow([frame, i, *positions[i], *velocities[i], energy, grf_val, rule_state[i]])

    return collections

# Initialize rule state
rule_state = np.zeros(NUM_TETRAHEDRONS, dtype=int)

# Run animation
ani = FuncAnimation(fig, update, frames=STEP_COUNT, interval=50, blit=False)

# Save animation (optional, requires ffmpeg)
output_path = "tetrahedral_attractors_logic.mp4"
try:
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    ani.save(output_path, writer="ffmpeg", fps=20)
    print(f"Animation saved to {output_path}")
except Exception as e:
    print(f"Failed to save animation: {e}. Displaying instead. Ensure ffmpeg is installed.")
    plt.show()
else:
    plt.show()