"""Shared Historical readout mathematics. Strict H5 response arithmetic only."""
import math
from .constants import LAMBDA_VP, THETA_LOCK, HARMONIC, BETA
from .numerics import stable_norm, checked, multiply, add
from .clock import angle
from .chirality import raw_chirality
from .types import Observation


def harmonic(omega, clock):
    norm = stable_norm(omega)
    denominator = add((1.0, norm), "norm saturation denominator")
    rho = checked(norm / denominator, "rho", nonzero=norm != 0)
    theta = angle(clock)
    locked = multiply(float(HARMONIC), add((theta, -THETA_LOCK), "lock subtraction"), "harmonic angle")
    cosine = checked(math.cos(locked), "harmonic cosine")
    amplitude = multiply(LAMBDA_VP, rho, "harmonic amplitude")
    return multiply(amplitude, cosine, "harmonic scalar")


def observe(omega, clock, z):
    theta = angle(clock)
    macro = (multiply(z, math.cos(theta), "macro cosine"), multiply(z, math.sin(theta), "macro sine"), z)
    chiral = raw_chirality(omega)
    total = tuple(add((m, multiply(BETA, c, "chirality blend coefficient")), "macro-chiral blend")
                  for m, c in zip(macro, chiral))
    return Observation(z, macro, chiral, total)
