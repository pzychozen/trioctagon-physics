"""GM05 review controls for Section 4. Run with Python and SymPy."""
import sympy as sp

L, beta0, beta, alpha, x, y = sp.symbols("L beta0 beta alpha x y", real=True)
e = sp.ones(3, 1)
T = sp.Matrix([[-sp.S.Half, 1, -sp.S.Half],
               [-sp.sqrt(3)/2, 0, sp.sqrt(3)/2],
               [0, 0, 0]])
D = sp.Rational(2, 3)*T.T
W = sp.Matrix([x, y, 0])
j = alpha*D*W + beta0*e

def energy(j):
    return L*j.dot(j)/2

def is_zero(value):
    return value.applyfunc(sp.simplify).is_zero_matrix if isinstance(value, sp.MatrixBase) else sp.simplify(value) == 0

reversed_j = j + alpha*D*(-2*W)
zero_endpoint = j - alpha*D*W
assert is_zero(reversed_j + j - 2*beta0*e)
assert is_zero(energy(reversed_j) - energy(j))
assert is_zero(zero_endpoint - beta0*e)
assert is_zero(energy(zero_endpoint) - 3*L*beta0**2/2)
assert is_zero(energy(j + beta*e) - energy(j) - (3*L*beta0*beta + 3*L*beta**2/2))
assert is_zero((energy(j + beta*e) - energy(j)).subs({beta0:1, beta:-1}) + 3*L/2)
print("All six additional common-offset controls passed.")

