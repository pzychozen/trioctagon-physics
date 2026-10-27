import numpy as np


def _d2_periodic(f, axis):
    return np.roll(f, -1, axis=axis) - 2.0 * f + np.roll(f, 1, axis=axis)


def _d2_reflect(f, axis):
    g = np.swapaxes(f, axis, 0)
    if g.shape[0] < 3:
        raise ValueError("Need at least 3 points along reflected axis")
    left = g[1:2]
    right = g[-2:-1]
    g_ext = np.concatenate([left, g, right], axis=0)
    d2 = g_ext[2:] - 2.0 * g_ext[1:-1] + g_ext[:-2]
    return np.swapaxes(d2, 0, axis)


def toroidal_laplacian(field, a=1.0, b=1.0, periodic_theta=True, periodic_phi=True, periodic_r=False):
    """TGMO core: toroidal Laplacian over (theta, phi, r) axes.

    The reference form in your 'Recursive Numerical Operators' note is:
        ∇_T^2 f = (1/a^2) ∇_θ^2 f + (1/b^2) ∇_φ^2 f + ∇_r^2 f

    Implementation details:
    - theta and phi are periodic by default.
    - r is reflecting (Neumann) by default; set periodic_r=True for periodic.

    Accepts:
    - 2D field: axes are (theta, phi)
    - 3D field: axes are (theta, phi, r)
    """
    f = np.asarray(field, dtype=float)
    if f.ndim not in (2, 3):
        raise ValueError("field must be 2D (theta,phi) or 3D (theta,phi,r)")

    d2_theta = _d2_periodic(f, 0) if periodic_theta else _d2_reflect(f, 0)
    d2_phi = _d2_periodic(f, 1) if periodic_phi else _d2_reflect(f, 1)

    lap = (1.0 / (a * a)) * d2_theta + (1.0 / (b * b)) * d2_phi

    if f.ndim == 3:
        d2_r = _d2_periodic(f, 2) if periodic_r else _d2_reflect(f, 2)
        lap = lap + d2_r

    return lap


def tgmo_step(field, dt=0.1, a=1.0, b=1.0, **kwargs):
    """One TGMO update step: field <- field + dt * ∇_T^2(field)."""
    return np.asarray(field, dtype=float) + dt * toroidal_laplacian(field, a=a, b=b, **kwargs)


def constant_field_test(n=64):
    f2 = np.ones((n, n))
    ok2 = np.allclose(toroidal_laplacian(f2), 0.0)
    f3 = np.ones((n, n, n))
    ok3 = np.allclose(toroidal_laplacian(f3), 0.0)
    return bool(ok2 and ok3)


def torus_embedding(theta, phi, a=1.0, b=1.0):
    """Map torus parameters (theta, phi) to Cartesian coordinates.

    Standard torus parameterization:
        x = (a + b cos(phi)) cos(theta)
        y = (a + b cos(phi)) sin(theta)
        z = b sin(phi)

    `theta` and `phi` can be scalars or numpy arrays.
    """
    theta = np.asarray(theta, dtype=float)
    phi = np.asarray(phi, dtype=float)
    x = (a + b * np.cos(phi)) * np.cos(theta)
    y = (a + b * np.cos(phi)) * np.sin(theta)
    z = b * np.sin(phi)
    return x, y, z


def theta_phi_grid(n_theta=256, n_phi=256):
    """Convenience: uniform grid on [0, 2pi) x [0, 2pi)."""
    theta = np.linspace(0.0, 2.0 * np.pi, int(n_theta), endpoint=False)
    phi = np.linspace(0.0, 2.0 * np.pi, int(n_phi), endpoint=False)
    return np.meshgrid(theta, phi, indexing="ij")

def make_tgmo_fn(a=1.0, b=1.0, periodic_theta=True, periodic_phi=True, periodic_r=False):
    """
    Returns a function tgmo_fn(Theta) that REFU can call.
    """
    def tgmo_fn(Theta):
        return toroidal_laplacian(
            Theta,
            a=a,
            b=b,
            periodic_theta=periodic_theta,
            periodic_phi=periodic_phi,
            periodic_r=periodic_r,
        )
    return tgmo_fn
