# geometry_embeddings.py
import math
import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class TorusConfig:
    R: float       # major radius
    r_max: float   # max tube thickness
    n_sectors: int = 12  # D24 gives 12 sectors

def history_to_xyz(history):
    κ = history["kappa"]
    z = history["z"]
    phi_idx = history["phi_index"]
    phi = 2 * math.pi * phi_idx / 12
    return κ * np.cos(phi), κ * np.sin(phi), z

def history_to_torus_xyz(history, config: TorusConfig):
    κ = history["kappa"]
    z = history["z"]
    phi_idx = history["phi_index"]

    phi = 2 * math.pi * phi_idx / config.n_sectors
    rho = κ / (1 + κ)
    r = config.r_max * rho

    # chi angle from normalized Z
    z_scale = np.max(np.abs(z)) + 1e-9
    chi = 0.5 * math.pi * (z / z_scale)

    X = (config.R + r * np.cos(chi)) * np.cos(phi)
    Y = (config.R + r * np.cos(chi)) * np.sin(phi)
    Z = r * np.sin(chi)
    return X, Y, Z
