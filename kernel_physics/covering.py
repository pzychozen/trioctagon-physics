"""Exact Paper A §§2–3 cycle matrices; no physical interpretation."""

from operator import index

import sympy as sp


def _positive_size(value: int) -> int:
    if isinstance(value, bool):
        raise ValueError("cycle sizes must be positive integers")
    try:
        size = index(value)
    except TypeError as exc:
        raise ValueError("cycle sizes must be positive integers") from exc
    if size < 1:
        raise ValueError("cycle sizes must be positive integers")
    return size


def cycle_laplacian(size: int) -> sp.ImmutableMatrix:
    """Delta f(n)=f(n+1)+f(n-1)-2f(n), retaining incidence multiplicity."""
    size = _positive_size(size)
    matrix = sp.zeros(size)
    for n in range(size):
        matrix[n, n] -= 2
        matrix[n, (n + 1) % size] += 1
        matrix[n, (n - 1) % size] += 1
    return sp.ImmutableMatrix(matrix)


def pullback_matrix(total_size: int, base_size: int) -> sp.ImmutableMatrix:
    """P[n,n mod d]=1, defined for all positive M,d (including non-divisors)."""
    total_size, base_size = map(_positive_size, (total_size, base_size))
    matrix = sp.zeros(total_size, base_size)
    for n in range(total_size):
        matrix[n, n % base_size] = 1
    return sp.ImmutableMatrix(matrix)


def isometric_pullback(total_size: int, base_size: int) -> sp.ImmutableMatrix:
    """Q=P/sqrt(M/d), an isometry only on the supported divisor domain."""
    total_size, base_size = map(_positive_size, (total_size, base_size))
    if total_size % base_size:
        raise ValueError("Q requires base_size to divide total_size")
    return sp.ImmutableMatrix(
        pullback_matrix(total_size, base_size) / sp.sqrt(total_size // base_size)
    )
