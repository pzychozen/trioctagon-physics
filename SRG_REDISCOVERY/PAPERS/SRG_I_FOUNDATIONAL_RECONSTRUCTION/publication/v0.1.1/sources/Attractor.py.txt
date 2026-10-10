import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
timesteps = 500
dt = 0.05
num_attractors = 3

# Initialize position and velocity for attractors
positions = np.random.rand(num_attractors, 2) * 2 - 1  # in [-1, 1]
velocities = np.zeros((num_attractors, 2))

# Log for position over time
position_log = []

# REFU memory curve function
def H(t):
    a1, b1 = 2.0, 0.5
    alpha2, b2 = 1.0, 0.3
    lambda1, omega1 = 1.5, 0.7
    lambda2, omega2 = 1.0, 0.4
    return (
        a1 * np.exp(-b1 * t) * np.cos(t)
        + alpha2 * np.exp(-b2 * t) * np.sin(t)
        + lambda1 * np.exp(-omega1 * t)
        + lambda2 * np.exp(-omega2 * t)
    )

# RPCO damping
def RPCO(v):
    return v / (1 + np.log1p(np.abs(v)))

# TGMO toroidal field wrapping
def TGMO(pos):
    return np.mod(pos + 1.0, 2.0) - 1.0  # keep in [-1, 1]

# Simulation loop
for step in range(timesteps):
    t = step * dt
    h_val = H(t)

    new_positions = []
    for i in range(num_attractors):
        # Compute influence from other attractors
        net_force = np.zeros(2)
        for j in range(num_attractors):
            if i == j:
                continue
            diff = positions[j] - positions[i]
            diff = TGMO(diff)
            net_force += diff / (np.linalg.norm(diff) + 1e-3)

        # Update with REFU * TGMO * RPCO
        velocities[i] += dt * h_val * net_force
        velocities[i] = RPCO(velocities[i])
        positions[i] = TGMO(positions[i] + dt * velocities[i])
        new_positions.append(positions[i].copy())

    position_log.append(np.array(new_positions))

# Convert log to array for plotting
position_log = np.array(position_log)

# Plot attractor trajectories
plt.figure(figsize=(8, 8))
for i in range(num_attractors):
    plt.plot(position_log[:, i, 0], position_log[:, i, 1], label=f'Attractor {i+1}')
plt.title("Recursive Attractor Trajectories under REFU/TGMO/RPCO")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
