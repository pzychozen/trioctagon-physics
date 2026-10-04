"""Independent nominal cross-check (no interval AD, no shared code): 130-digit complex iteration of the accepted map from
sqrt3 f_1, own host (Newton), own basis, gauge via arg(u.Psi). Compares quotient points at N=300, 301 with the
v0.2 interval boxes. Numerical consistency only, not proof."""
import mpmath as mp, json, hashlib, sys
mp.mp.dps = 130
eps = mp.mpf(1)/20; g = mp.mpf(1)/5; k = [mp.mpf(1), mp.mpf('1.2208964704604097'), mp.mpf('6.35310346037241')]
def L3(v): s = sum(v); return [s - 3*x for x in v]
u = [mp.mpf('1.554467816928818'), mp.mpf('1.573421131869043'), mp.mpf('2.085939972794636')]
for _ in range(12):
    Jm = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3): Jm[i, j] = (eps*(k[i] - 3*u[i]**2) if i == j else 0) + g*(1 - 3*(i == j))
    r = mp.matrix([eps*u[i]*(k[i] - u[i]**2) + L3(u)[i]*g for i in range(3)]); du = mp.lu_solve(Jm, r); u = [u[i] - du[i] for i in range(3)]
a = mp.sqrt(u[0]**2 + u[1]**2); n = mp.sqrt(sum(x**2 for x in u))
v1 = [u[1]/a, -u[0]/a, 0]; v2 = [u[0]*u[2]/(a*n), u[1]*u[2]/(a*n), -a/n]
M = [[(1 + eps*(k[i] - u[i]**2) if i == j else 0) + g*(1 - 3*(i == j)) for j in range(3)] for i in range(3)]
K = [[sum(V1[i]*sum(M[i][j]*V2[j] for j in range(3)) for i in range(3)) for V2 in (v1, v2)] for V1 in (v1, v2)]
m1 = (K[0][0] + K[1][1] + mp.sqrt((K[0][0] - K[1][1])**2 + 4*K[0][1]**2))/2
lam = (1 + 1/m1)/9 + mp.mpf('0.005')
def F(O):
    P = [O[i] + eps*O[i]*(k[i] - abs(O[i])**2) + g*L3(O)[i] for i in range(3)]
    ph = [mp.arg(z) for z in P]
    return [abs(P[i])*mp.expj(ph[i] + lam*sum(mp.sin(3*(ph[j] - ph[i])) for j in range(3) if j != i)) for i in range(3)]
def q(O):
    th = mp.arg(sum(u[i]*O[i] for i in range(3))); G = [z*mp.expj(-th) for z in O]
    return [mp.re(G[i]) - u[i] for i in range(3)] + [sum(mp.im(G[i])*v1[i] for i in range(3)), sum(mp.im(G[i])*v2[i] for i in range(3))]
O = [mp.mpc(1), mp.expj(-2*mp.pi/3), mp.expj(-4*mp.pi/3)]
O = [mp.sqrt(3)*z/mp.sqrt(3) for z in O]   # sqrt3 * f_1 with f_1 = (1, w, w^2)/sqrt3
qs = {}
for nstep in range(1, 302):
    O = F(O)
    if nstep in (21, 300, 301): qs[nstep] = q(O)
R = json.load(open(sys.argv[1]))['values']
from fractions import Fraction
def frac(x): s_, man, exp, bc = x._mpf_; return Fraction((-1)**s_*man)*Fraction(2)**exp
def inbox(pt, bx): return all(Fraction(lo) <= frac(x) <= Fraction(hi) for x, (lo, hi) in zip(pt, bx))
out = {"lambda": mp.nstr(lam, 60),
       "q300_nominal": [mp.nstr(x, 30) for x in qs[300]], "q301_nominal": [mp.nstr(x, 30) for x in qs[301]],
       "q300_inside_interval_box": inbox(qs[300], R["EXACT: N=300 box endpoints (rationals)"]),
       "q301_inside_interval_box": inbox(qs[301], R["EXACT: N=301 box endpoints (rationals)"]),
       "script_sha256": hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}
print(json.dumps(out, indent=1)); json.dump(out, open(__file__.replace('.py', '_results.json'), 'w'), indent=1)
