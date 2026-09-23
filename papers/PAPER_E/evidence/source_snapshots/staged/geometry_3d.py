# geometry_3d.py
import numpy as np

def history_to_xyz(history):
    """
    Map history dict -> 3D trajectory using (kappa, phi_index, z).

    x = kappa * cos(phi)
    y = kappa * sin(phi)
    z = emergent Z (already in history["z"])

    phi is the D24 phase: 2π * phi_index / 12.
    """
    kappa = history["kappa"]
    z = history["z"]
    phi_index = history["phi_index"]

    phi = 2.0 * np.pi * phi_index / 12.0

    x = kappa * np.cos(phi)
    y = kappa * np.sin(phi)

    return x, y, z

def history_to_torus_xyz(history, R: float = 2.0, r_max: float = 1.0):
    """
    Map history -> torus coordinates (X, Y, Z_torus).

    - phi (D24 angle) selects position around the big ring
    - kappa controls minor radius r via a soft normalization
    - Z controls tilt around the tube (chi angle)

    Torus parameterization:
        X = (R + r cos chi) cos phi
        Y = (R + r cos chi) sin phi
        Z = r sin chi
    """
    kappa = history["kappa"]          # (T,)
    z = history["z"]                  # (T,)
    phi_index = history["phi_index"]  # (T,)

    # D24 angle
    phi = 2.0 * np.pi * phi_index / 12.0

    # normalized radius 0..1 from kappa
    rho = kappa / (1.0 + kappa)
    r = r_max * rho

    # use Z to define chi along the tube
    z_abs_max = np.max(np.abs(z)) + 1e-9  # avoid divide by zero
    z_norm = z / z_abs_max                # roughly in [-1, 1]
    chi = 0.5 * np.pi * z_norm            # roughly in [-π/2, π/2]

    X = (R + r * np.cos(chi)) * np.cos(phi)
    Y = (R + r * np.cos(chi)) * np.sin(phi)
    Z = r * np.sin(chi)

    return X, Y, Z

def history_Zvec_to_xyz(history, key: str = "Z_total"):
    """
    Use a stored 3D Z-trajectory directly.

    key defaults to "Z_total" (the blended orientation manifold).
    Backwards compatible: falls back to "Z_vec" if needed.
    """
    if key not in history:
        if key == "Z_total" and "Z_vec" in history:
            key = "Z_vec"
        else:
            raise KeyError(f"history does not contain '{key}'")
    Z = history[key]  # shape (T, 3)
    x = Z[:, 0]
    y = Z[:, 1]
    z = Z[:, 2]
    return x, y, z


