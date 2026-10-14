# Generated from reviewed original; see EXTRACTION_MAP.json.
import numpy as np
TORUS_SIZE = 10.0
NUM_TETRAHEDRONS = 8
STEP_COUNT = 200
DT = 0.1
VELOCITY_SCALE = 0.2

def wrap_position(pos):
    """Wrap positions toroidally within [0, TORUS_SIZE] with teleport detection."""
    wrapped = np.mod(pos, TORUS_SIZE)
    return wrapped

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
    """Glyph Retention Factor based on velocity stability."""
    vel_mags = np.linalg.norm(velocities, axis=1)
    return 1.0 / (1.0 + np.mean(vel_mags))

def compute_energy(positions, velocities):
    """Compute total kinetic energy of the system."""
    kinetic_energy = 0.5 * np.sum(np.linalg.norm(velocities, axis=1) ** 2)
    potential_energy = 0.0
    return kinetic_energy + potential_energy

def detect_teleport(prev_positions, new_positions, threshold=1.0):
    """Detect if a tetrahedron teleports by checking large position jumps."""
    teleports = []
    for i in range(NUM_TETRAHEDRONS):
        distance = np.linalg.norm(wrap_position(new_positions[i] - prev_positions[i]))
        if distance > threshold:
            teleports.append((i, distance, new_positions[i], prev_positions[i]))
    return teleports

def initialize():
    global positions, velocities, rule_state
    positions = np.random.rand(NUM_TETRAHEDRONS, 3) * TORUS_SIZE
    velocities = (np.random.rand(NUM_TETRAHEDRONS, 3) - 0.5) * VELOCITY_SCALE
    rule_state = np.zeros(NUM_TETRAHEDRONS, dtype=int)

def numerical_step(frame, _trace=None):
    global positions, velocities, rule_state
    t = frame * DT
    grf_val = GRF(positions, t)
    h_val = H(t)
    for i in range(NUM_TETRAHEDRONS):
        if _trace is not None:
            _trace('before', i, positions, velocities)
        centroid = np.mean(positions, axis=0)
        diff = centroid - positions[i]
        diff = wrap_position(diff + TORUS_SIZE / 2) - TORUS_SIZE / 2
        norm = np.linalg.norm(diff) + 0.01
        if grf_val > 0.5 and np.random.rand() < 0.01:
            rule_state[i] = 1 - rule_state[i]
        force = diff / norm * h_val * (-1 if rule_state[i] else 1)
        velocities[i] += DT * force * grf_val
        velocities[i] = RPCO(velocities[i])
        positions[i] += DT * velocities[i]
        positions[i] = wrap_position(positions[i])
        if _trace is not None:
            _trace('after', i, positions, velocities)
    return {'t': t, 'H': h_val, 'G': grf_val}
