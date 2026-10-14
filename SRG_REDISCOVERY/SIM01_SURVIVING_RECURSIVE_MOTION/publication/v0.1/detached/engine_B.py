# Generated from reviewed original; see EXTRACTION_MAP.json.
import numpy as np
TORUS_SIZE = 10.0
NUM_TETRAHEDRONS = 8
STEP_COUNT = 2000
DT = 0.1
VELOCITY_SCALE = 0.2

def wrap_position(pos):
    """Wrap positions toroidally within [0, TORUS_SIZE]."""
    return np.mod(pos, TORUS_SIZE)

def H(t):
    """REFU memory curve function."""
    a1, b1 = (2.0, 0.5)
    alpha2, b2 = (1.0, 0.3)
    lambda1, omega1 = (1.5, 0.7)
    lambda2, omega2 = (1.0, 0.4)
    return a1 * np.exp(-b1 * t) * np.cos(t) + alpha2 * np.exp(-b2 * t) * np.sin(t) + lambda1 * np.exp(-omega1 * t) + lambda2 * np.exp(-omega2 * t)

def RPCO(v):
    """RPCO damping function."""
    return v / (1 + np.log1p(np.abs(v)))

def GRF(positions, t):
    """Glyph Retention Factor (simplified, based on position stability)."""
    vel_mags = np.linalg.norm(velocities, axis=1)
    return 1.0 / (1.0 + np.mean(vel_mags))

def initialize():
    global positions, velocities
    positions = np.random.rand(NUM_TETRAHEDRONS, 3) * TORUS_SIZE
    velocities = (np.random.rand(NUM_TETRAHEDRONS, 3) - 0.5) * VELOCITY_SCALE

def numerical_step(frame, _trace=None):
    global positions, velocities
    t = frame * DT
    grf_val = GRF(positions, t)
    h_val = H(t)
    for i in range(NUM_TETRAHEDRONS):
        if _trace is not None:
            _trace('before', i, positions, velocities)
        centroid = np.mean(positions, axis=0)
        diff = centroid - positions[i]
        diff = wrap_position(diff + TORUS_SIZE / 2) - TORUS_SIZE / 2
        force = diff / (np.linalg.norm(diff) + 0.01) * h_val
        velocities[i] += DT * force * grf_val
        velocities[i] = RPCO(velocities[i])
        positions[i] += DT * velocities[i]
        positions[i] = wrap_position(positions[i])
        if _trace is not None:
            _trace('after', i, positions, velocities)
    return {'t': t, 'H': h_val, 'G': grf_val}
