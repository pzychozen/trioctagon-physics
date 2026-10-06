"""Independent fresh-eyes checks of the TriOctagon native map (no repo code imported).

Native update (GR1 eq. 1):
  z~_i = z_i + eps z_i (k_i - |z_i|^2) + g (Delta z)_i
  theta_i^+ = theta~_i + lam * sum_{j~i} sin 3(theta~_j - theta~_i),  |z^+| = |z~|
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 60
rng = np.random.default_rng(0)


def lap(N):
    D = -2 * np.eye(N)
    for i in range(N):
        D[i, (i + 1) % N] += 1
        D[i, (i - 1) % N] += 1
    return D


def native_step(z, eps, g, lam, k):
    N = len(z)
    zt = z + eps * z * (k - np.abs(z) ** 2) + g * (lap(N) @ z)
    th = np.angle(zt)
    inc = lam * (np.sin(3 * (np.roll(th, 1) - th)) + np.sin(3 * (np.roll(th, -1) - th)))
    return np.abs(zt) * np.exp(1j * (th + inc))


def k_for_branch(r, eps, g):
    """Coefficients making the positive in-phase r an exact fixed point (GR1 eq. 24)."""
    return r ** 2 - (g / eps) * (lap(len(r)) @ r) / r


print("=" * 72)
print("A. Fixed point + phase Jacobian = S P  (independent re-derivation)")
eps, g, lam = 0.05, 0.2, 0.01
ell = 3 * lam
r3 = np.array([0.8, 1.0, 1.3])
N = 12
r = np.tile(r3, N // 3)
k = k_for_branch(r, eps, g)
print("fixed-point residual:", np.max(np.abs(native_step(r + 0j, eps, g, lam, k) - r)))
D = lap(N)
R = np.diag(r)
H = np.eye(N) + g * (D - np.diag((D @ r) / r))     # Doob / ground-state form
print("H r = r  (ground-state transform) :", np.allclose(H @ r, r))
P = np.linalg.inv(R) @ H @ R
S = np.eye(N) + ell * D
J = S @ P
# finite-difference phase Jacobian of the native map
h = 1e-6
Jfd = np.zeros((N, N))
for j in range(N):
    dp = np.zeros(N); dp[j] = h
    zp = native_step(r * np.exp(1j * dp), eps, g, lam, k)
    zm = native_step(r * np.exp(-1j * dp), eps, g, lam, k)
    Jfd[:, j] = (np.angle(zp) - np.angle(zm)) / (2 * h)
print("max |J_fd - S P| :", np.max(np.abs(Jfd - J)))
off = [P[i, (i + 1) % N] - g * r[(i + 1) % N] / r[i] for i in range(N)]
print("P_{i,i+1} = g r_{i+1}/r_i :", np.allclose(off, 0))
print("pre-sync phase block in Cartesian b=R phi is H (uniform conductance g, symmetric):",
      np.allclose(R @ P @ np.linalg.inv(R), H), np.allclose(H, H.T))


print("=" * 72)
print("B. Bloch-block imaginary obstruction: native vs generator vs weighted-sync diagnostic")


def Dz(z):
    return np.array([[-2, 1, 1 / z], [1, -2, 1], [z, 1, -2]], dtype=complex)


def blocks(a, b, c, g, ell, z):
    r = np.array([a, b, c])
    Rm = np.diag(r)
    sig = r.sum()
    Hz = np.eye(3) - g * np.diag((sig - 3 * r) / r) + g * Dz(z)
    Pz = np.linalg.inv(Rm) @ Hz @ Rm
    Jnat = (np.eye(3) + ell * Dz(z)) @ Pz                    # native composite
    Jgen = Pz + ell * Dz(z)                                  # generator (sum) = P + S - I
    Jw = (np.eye(3) + ell * np.linalg.inv(Rm) ** 2 @ Dz(z)) @ Pz  # counterfactual: R^-2 weighted sync
    return Jnat, Jgen, Jw


def Bcoef(M):
    return (np.trace(M) ** 2 - np.trace(M @ M)) / 2


a, b, c = 0.8, 1.0, 1.3
V = (a - b) * (a - c) * (b - c)
for (gg, ll) in [(0.2, 0.03), (0.2, 0.3), (0.1, 0.1)]:
    Jn, Jg, Jw = blocks(a, b, c, gg, ll, 1j)
    E = ll * (1 + 3 * gg) - gg
    print(f" g={gg}, ell={ll}:  -Im B_native={-Bcoef(Jn).imag:+.6e}  "
          f"GR2 Gamma=ell g E V/abc={ll*gg*E*V/(a*b*c):+.6e}")
    print(f"           -Im B_gen   ={-Bcoef(Jg).imag:+.6e}  ell g (ell-g) V/abc={ll*gg*(ll-gg)*V/(a*b*c):+.6e}"
          f"   | weighted-sync diagnostic: {-Bcoef(Jw).imag:+.3e}")

print("\n step-size scaling g=h*0.4, ell=h*0.9 (so ell_hat-g_hat=0.5):")
for hh in [1e-1, 1e-2, 1e-3]:
    gg, ll = 0.4 * hh, 0.9 * hh
    Jn, Jg, Jw = blocks(a, b, c, gg, ll, 1j)
    En = ll * (1 + 3 * gg) - gg
    print(f"  h={hh:.0e}: E/h={En/hh:.6f} (=(ell^-g^)+3 h g^ell^ = {0.5+3*hh*0.36:.6f});"
          f" GammaNat/h^3={-Bcoef(Jn).imag/hh**3:+.5e}, GammaGen/h^3={-Bcoef(Jg).imag/hh**3:+.5e},"
          f" weighted/h^3={-Bcoef(Jw).imag/hh**3:+.3e}")
    ev = np.linalg.eigvals(Jn)
    rates = 1 - ev                       # per-step decrement
    slow = rates[np.argmin(np.abs(rates))]
    print(f"           eigen-rates/h (native, z=i): {np.round(rates/hh, 5)}")

print("\n same with ell = g (no metric mismatch at generator level), h=1e-3:")
gg = ll = 0.5e-3
Jn, Jg, Jw = blocks(a, b, c, gg, ll, 1j)
print(f"  GammaNat={-Bcoef(Jn).imag:+.3e} (order h^4, pure splitting), GammaGen={-Bcoef(Jg).imag:+.3e}")


print("=" * 72)
print("C. Triad Kolmogorov cycle factor: native vs generator")


def cyc(M):
    return M[0, 1] * M[1, 2] * M[2, 0] - M[1, 0] * M[2, 1] * M[0, 2]


def triadJ(a, b, c, g, ell, gen=False):
    r = np.array([a, b, c]); Rm = np.diag(r); L3 = np.ones((3, 3)) - 3 * np.eye(3)
    sig = r.sum()
    H3 = np.eye(3) - g * np.diag((sig - 3 * r) / r) + g * L3
    P3 = np.linalg.inv(Rm) @ H3 @ Rm
    return (P3 + ell * L3) if gen else (np.eye(3) + ell * L3) @ P3


for hh in [1e-1, 1e-2, 1e-3]:
    gg, ll = 0.4 * hh, 0.9 * hh
    cn, cg = cyc(triadJ(a, b, c, gg, ll)), cyc(triadJ(a, b, c, gg, ll, True))
    pred = gg * ll * (gg - ll) * ((c/a + a/b + b/c) - (a/c + b/a + c/b))
    print(f"  h={hh:.0e}: C_native/h^3={cn/hh**3:+.6e}  C_gen/h^3={cg/hh**3:+.6e}  "
          f"g ell (g-ell)[cyclic ratio diff]/h^3={pred/hh**3:+.6e}")


print("=" * 72)
print("D. Channel area = planar-spin vector chirality = U(1) Noether bond current; local Z3 of sync")
Om = rng.normal(size=3) + 1j * rng.normal(size=3)
x, y = Om.real, Om.imag
C = np.cross(x, y)
s = [np.array([x[i], y[i]]) for i in range(3)]
cr = lambda u, v: u[0] * v[1] - u[1] * v[0]
chir = np.array([cr(s[1], s[2]), cr(s[2], s[0]), cr(s[0], s[1])])
bond = np.array([np.imag(np.conj(Om[1]) * Om[2]), np.imag(np.conj(Om[2]) * Om[0]), np.imag(np.conj(Om[0]) * Om[1])])
print(" C = (s_B x s_C, s_C x s_A, s_A x s_B):", np.allclose(C, chir), "| C = Im(conj(Om_i) Om_j):", np.allclose(C, bond))
I = np.sum(np.abs(Om) ** 2)
print(" I^2 = |Om.Om|^2 + 4|C|^2 (3D polarization / oscillator identity):",
      np.isclose(I ** 2, abs(np.sum(Om * Om)) ** 2 + 4 * C @ C))
w = np.exp(2j * np.pi / 3)
f1 = np.array([1, w ** -1, w ** -2]) / np.sqrt(3)
print(" f1 . f1 = 0 (circular / maximal chirality):", np.isclose(np.sum(f1 * f1), 0))


def sync_only(z, lam):
    th = np.angle(z)
    inc = lam * (np.sin(3 * (np.roll(th, 1) - th)) + np.sin(3 * (np.roll(th, -1) - th)))
    return np.abs(z) * np.exp(1j * (th + inc))


n = rng.integers(0, 3, size=9)
z9 = rng.normal(size=9) + 1j * rng.normal(size=9)
G = w ** n
print(" sync stage commutes with LOCAL Z3 phase rotations:",
      np.allclose(sync_only(G * z9, 0.3), G * sync_only(z9, 0.3)))
Lz = lap(9) @ (G * z9) - G * (lap(9) @ z9)
print(" graph-coupling stage does NOT (max defect):", np.max(np.abs(Lz)).round(3))


print("=" * 72)
print("E. Paper G M2 flip location vs explicit-step stability of the synchronizer")
m1 = 0.4334093508963767
lam_c = (1 + 1 / m1) / 9
print(f" lambda_c = {lam_c:.12f};  sync-alone triad transverse multiplier 1-9*lambda_c = {1-9*lam_c:.6f}"
      f"  (|.|>1 for lambda>2/9={2/9:.6f})")
print(" SIMS boundary g*=2/3  <->  1-3g = -1 (explicit diffusion step limit on the triad)")

print("=" * 72)
print("F. Generator (small-step) limit of the complex Bloch rates; Hatano-Nelson net flux")
def Dz2(z): return np.array([[-2,1,1/z],[1,-2,1],[z,1,-2]],dtype=complex)
def parts2(a,b,c,g,ell,z):
    r=np.array([a,b,c]);Rm=np.diag(r);sig=r.sum()
    Hz=np.eye(3)-g*np.diag((sig-3*r)/r)+g*Dz2(z); Pz=np.linalg.inv(Rm)@Hz@Rm
    return Pz,(np.eye(3)+ell*Dz2(z))@Pz, Pz+ell*Dz2(z), (np.eye(3)+ell*np.linalg.inv(Rm)**2@Dz2(z))@Pz
a,b,c=0.8,1.0,1.3
print("generator-level rates (P+S-I), per unit h, z=i, ghat=0.4, ellhat=0.9:")
for h in [1e-1,1e-2,1e-3,1e-4]:
    P,Jn,Jg,Jw=parts2(a,b,c,0.4*h,0.9*h,1j)
    rn=np.sort_complex((1-np.linalg.eigvals(Jn))/h); rg=np.sort_complex((1-np.linalg.eigvals(Jg))/h); rw=np.sort_complex((1-np.linalg.eigvals(Jw))/h)
    print(f" h={h:.0e} native {np.round(rn,6)}\n        gen    {np.round(rg,6)}\n        R2-wtd {np.round(rw,6)}")
print("\nell_hat = g_hat (=0.5) generator:", np.round(np.sort_complex((1-np.linalg.eigvals(parts2(a,b,c,0.5e-3,0.5e-3,1j)[2]))/1e-3),8))
# Hatano-Nelson style net imaginary flux per cell of the generator (nearest-neighbour ring)
def lap2(N):
    D=-2*np.eye(N)
    for i in range(N): D[i,(i+1)%N]+=1; D[i,(i-1)%N]+=1
    return D
N=12; r=np.tile([a,b,c],N//3); g,ell=0.04,0.09
D=lap2(N); R=np.diag(r); H=np.eye(N)+g*(D-np.diag((D@r)/r)); P=np.linalg.inv(R)@H@R
Jg=P+ell*D
fwd=np.prod([Jg[i,(i+1)%N] for i in range(N)]); bwd=np.prod([Jg[(i+1)%N,i] for i in range(N)])
print("\ngenerator ring N=12: log(prod fwd/prod bwd) =",np.log(fwd/bwd), " per cell:",np.log(fwd/bwd)/(N//3))
ev=np.linalg.eigvals(Jg); print(" max |Im eig| (generator, N=12):",np.max(np.abs(ev.imag)))
Jn=(np.eye(N)+ell*D)@P; print(" max |Im eig| (native,    N=12):",np.max(np.abs(np.linalg.eigvals(Jn).imag)))
