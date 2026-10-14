# Generated from reviewed original; see EXTRACTION_MAP.json.
import numpy as np
timesteps = 500
dt = 0.05
num_attractors = 3

def H(t):
    a1, b1 = (2.0, 0.5)
    alpha2, b2 = (1.0, 0.3)
    lambda1, omega1 = (1.5, 0.7)
    lambda2, omega2 = (1.0, 0.4)
    return a1 * np.exp(-b1 * t) * np.cos(t) + alpha2 * np.exp(-b2 * t) * np.sin(t) + lambda1 * np.exp(-omega1 * t) + lambda2 * np.exp(-omega2 * t)

def RPCO(v):
    return v / (1 + np.log1p(np.abs(v)))

def TGMO(pos):
    return np.mod(pos + 1.0, 2.0) - 1.0

def initialize():
    global positions, velocities
    positions = np.random.rand(num_attractors, 2) * 2 - 1
    velocities = np.zeros((num_attractors, 2))

def numerical_step(step, _trace=None):
    global positions, velocities
    t = step * dt
    h_val = H(t)
    for i in range(num_attractors):
        if _trace is not None:
            _trace('before', i, positions, velocities)
        net_force = np.zeros(2)
        for j in range(num_attractors):
            if i == j:
                continue
            diff = positions[j] - positions[i]
            diff = TGMO(diff)
            net_force += diff / (np.linalg.norm(diff) + 0.001)
        velocities[i] += dt * h_val * net_force
        velocities[i] = RPCO(velocities[i])
        positions[i] = TGMO(positions[i] + dt * velocities[i])
        if _trace is not None:
            _trace('after', i, positions, velocities)
    return {'t': t, 'H': h_val, 'G': None}
