"""Claude external attack/replay v0.2 of Codex M3 certificate (m3_validated_entry.py, SHA-256 6735e5b3...6f466).
v0.2 additions: host from the M2 Krawczyk IMAGE K(X) (rigorous root enclosure, width 3e-60); lambda_c recomputed by interval
arithmetic over that host; explicit centre-in-box assertion at every mean-value step; the ENTRY step tested directly
(Fhat(qbox_300) subset int U_plus) instead of inferring capture from qbox_300 subset U_minus-box; box-level test of the
invalid inference; H(U_plus) alternative route; gauge-angle enclosures for the phase-accumulation argument.
Repairs: exact interval endpoints via _mpi_ tuples (no string parsing); exact rational parameter enclosures;
host/basis from the M2-certified Krawczyk box (centre integers / 2^240 +- 1e-30) instead of 1e-25 inflation of a
point root; interval evaluation of F^2(c) in the trap; explicit lower bounds for every ratio-atan denominator,
gauge denominator and radius; branch-cut exclusion check for atan2; H-composed one-step contraction (G = H o Fhat).
Standalone: mpmath only. No repository module. Codex artifacts are read, never modified.
Usage: python3 m3_claude_review.py <gpt_m2_certificate_json> <codex_m3_validated_entry_json>
"""
import sys, json, hashlib, time
from fractions import Fraction
import mpmath as mp
from mpmath import iv
IVDPS = int(sys.argv[3]) if len(sys.argv) > 3 else 80
mp.mp.dps = IVDPS + 10; iv.dps = IVDPS
R = {"kind": "CLAUDE_M3_EXTERNAL_REVIEW_v0.2", "iv_dps": IVDPS, "checks": {}, "values": {}}
def check(n, c): R["checks"][n] = bool(c); print(("PASS " if c else "FAIL ") + n, flush=True)
def val(n, v): R["values"][n] = v; print("   ", n, "=", v, flush=True)
T0 = time.time()

# ---------- exact endpoint helpers ----------
fr2 = lambda f: mp.mpf(f.numerator)/f.denominator
def frac_t(t): s, man, exp, bc = t; return Fraction((-1)**s*man)*(Fraction(2)**exp)
def LO(x): return frac_t(x._mpi_[0])
def HI(x): return frac_t(x._mpi_[1])
def lo_mpf(x): return mp.mpf(x._mpi_[0])
def hi_mpf(x): return mp.mpf(x._mpi_[1])
def width(x): return HI(x) - LO(x)
def mid_point(x):            # a point strictly inside [a,b]: (a+b)/2 rounded at mp precision (90 dps > iv 80 dps)
    m = (lo_mpf(x) + hi_mpf(x))/2
    assert LO(x) <= frac_t(m._mpf_) <= HI(x)
    return m
def ivpt(m): return iv.mpf(m)           # exact point interval from an mpf
def absup(x): return max(abs(LO(x)), abs(HI(x)))
def contains(X, Y): return LO(X) <= LO(Y) and HI(Y) <= HI(X)
def strict_inside(X, Y): return LO(X) < LO(Y) and HI(Y) < HI(X)
def iv_from_frac(lo, hi):   # outward enclosure of a rational interval
    a = mp.mpf(lo.numerator)/mp.mpf(lo.denominator); b = mp.mpf(hi.numerator)/mp.mpf(hi.denominator)
    # outward adjust by one ulp if rounding moved inward
    one_ulp = mp.mpf(2)**(-mp.mp.prec + 5)
    while frac_t(a._mpf_) > lo: a = a - abs(a)*one_ulp
    while frac_t(b._mpf_) < hi: b = b + abs(b)*one_ulp
    return iv.mpf([a, b])

# ---------- A. exact parameters and entrance ----------
eps = iv.mpf(1)/20; g = iv.mpf(1)/5
k = [iv.mpf(1), iv.mpf('1.2208964704604097'), iv.mpf('6.35310346037241')]
check("A: eps, g, k_i interval enclosures contain the exact rationals (1/20, 1/5, decimal strings)",
      LO(eps) <= Fraction(1,20) <= HI(eps) and LO(g) <= Fraction(1,5) <= HI(g) and all(LO(k[i]) <= Fraction(s) <= HI(k[i]) for i, s in enumerate(('1', '1.2208964704604097', '6.35310346037241'))))
gpt = json.load(open(sys.argv[1]))['integer_interval_certificate']
B2 = int(gpt['critical_data']['lc']['denominator_power_of_two'])
lc_lo = Fraction(int(gpt['critical_data']['lc']['lo_numerator']), 2**B2); lc_hi = Fraction(int(gpt['critical_data']['lc']['hi_numerator']), 2**B2)
lam_c_iv = iv_from_frac(lc_lo, lc_hi)
mu = iv.mpf('0.005'); lam = lam_c_iv + mu
check("A: lambda_c interval taken from the M2 certified integer enclosure (2^-240 scale), lambda = lambda_c + 0.005 enclosed", LO(lam_c_iv) <= lc_lo and lc_hi <= HI(lam_c_iv) and LO(mu) <= Fraction(1,200) <= HI(mu))
codex_lam = iv.mpf(['0.36747639460421353654937599159885992870560445','0.367476394604213536549375991605031226596387979'])
check("A (finding, confirmed): Codex's encoded lambda_c interval does NOT contain the M2-certified enclosure: its upper endpoint is a display string truncated ~1.8e-46 below the certified upper endpoint (defect in certificate accounting; repaired here by using the certified integer enclosure)", not contains(codex_lam, lam_c_iv) and LO(codex_lam) <= lc_lo)
val("A: certified upper endpoint minus Codex's encoded upper endpoint", mp.nstr(hi_mpf(lam_c_iv) - hi_mpf(codex_lam), 5))
val("A: certified lambda_c interval", [mp.nstr(lo_mpf(lam_c_iv), 50), mp.nstr(hi_mpf(lam_c_iv), 50)])
s3 = iv.sqrt(iv.mpf(3))
box = [iv.mpf(1), iv.mpf('-0.5'), iv.mpf('-0.5'), iv.mpf(0), -s3/2, s3/2]
check("A: entrance box encloses sqrt3 f_1 = (1, -1/2 - i sqrt3/2, -1/2 + i sqrt3/2) (negative Fourier convention; sqrt3 by iv.sqrt)",
      LO(box[1]) <= Fraction(-1,2) <= HI(box[1]) and LO(s3)**2 <= 3 <= HI(s3)**2 and LO(box[4]) < 0 and HI(box[5]) > 0)

# ---------- C. host and basis from the M2 certified Krawczyk IMAGE (root in K(X) when K(X) subset int X) ----------
def iv_from_cert(c): return iv_from_frac(Fraction(int(c['lo_numerator']), 2**int(c['denominator_power_of_two'])), Fraction(int(c['hi_numerator']), 2**int(c['denominator_power_of_two'])))
cen = [Fraction(int(c['lo_numerator']), 2**int(c['denominator_power_of_two'])) for c in gpt['center']]
check("C0: M2 certificate records strict Krawczyk inclusion K(X) subset int X (so the unique exact host lies in K(X))", gpt['krawczyk_strict_inclusion'] is True)
u_iv = [iv_from_cert(c) for c in gpt['krawczyk_image']]
Xbox = [iv_from_cert(c) for c in gpt['host_box']]
check("C0: K(X) subset X (consistency of the certificate fields)", all(contains(Xbox[i], u_iv[i]) for i in range(3)))
a12 = iv.sqrt(u_iv[0]**2 + u_iv[1]**2); nr = iv.sqrt(u_iv[0]**2 + u_iv[1]**2 + u_iv[2]**2)
v1_iv = [u_iv[1]/a12, -u_iv[0]/a12, iv.mpf(0)]
v2_iv = [u_iv[0]*u_iv[2]/(a12*nr), u_iv[1]*u_iv[2]/(a12*nr), -(u_iv[0]**2 + u_iv[1]**2)/(a12*nr)]
# lambda_c recomputed over the tight host: K = V^T M V, m1 = larger eigenvalue (closed form), lambda_c = (1 + 1/m1)/9
Mi = [[(1 + eps*(k[i] - u_iv[i]**2) if i == j else iv.mpf(0)) + g*(1 - 3*(i == j)) for j in range(3)] for i in range(3)]
Vc = [v1_iv, v2_iv]
Kc = [[sum((Vc[r][i]*sum((Mi[i][j]*Vc[c2][j] for j in range(3)), iv.mpf(0)) for i in range(3)), iv.mpf(0)) for c2 in range(2)] for r in range(2)]
disc = iv.sqrt((Kc[0][0] - Kc[1][1])**2 + 4*Kc[0][1]**2)
m1_iv = (Kc[0][0] + Kc[1][1] + disc)/2
lam_c_tight = (1 + 1/m1_iv)/9
val("C: recomputed lambda_c over K(X) (interval)", [mp.nstr(lo_mpf(lam_c_tight), 60), mp.nstr(hi_mpf(lam_c_tight), 60), "width " + mp.nstr(fr2(width(lam_c_tight)), 3)])
check("C: recomputed tight lambda_c lies inside the M2 certified lambda_c enclosure", contains(lam_c_iv, lam_c_tight))
check("C (resolves A finding): Codex's encoded lambda_c interval CONTAINS the rigorously enclosed exact lambda_c (its truncated upper string is ~3e-39 above the exact value); defect was certificate accounting only", contains(codex_lam, lam_c_tight))
lam = lam_c_tight + mu
val("C: widths of interval host / v1 / v2 from the certified box", [mp.nstr(max(width(x) for x in u_iv), 3), mp.nstr(max(width(x) for x in v1_iv), 3), mp.nstr(max(width(x) for x in v2_iv), 3)])
codex = json.load(open(sys.argv[2]))
u_cdx = [mp.mpf(s) for s in codex['host']]
# Codex basis values: recompute exactly as Codex did (90-digit mpf) from its printed 60-digit host is NOT identical to its internal v1,v2; instead
# we test the claim that the TRUE basis lies within 1e-25 of ANY point within 1e-26 of Codex's host, using our interval basis:
cdx_u_box = [iv.mpf([x - mp.mpf('1e-25'), x + mp.mpf('1e-25')]) for x in u_cdx]
check("C1: Codex's 1e-25 host boxes (around its printed 60-digit host) contain the M2-certified host box", all(contains(cdx_u_box[i], u_iv[i]) for i in range(3)))
# basis: Codex inflated its 90-digit v1,v2 by 1e-25. Bound: our interval v1,v2 are enclosures; Codex's v1,v2 are v(u_cdx) with u_cdx within ~1e-60 of the true host
# (its findroot residual); so |v(u_cdx) - v(u*)| <= Lip * 1e-59 << 1e-25. Verify directly: interval v computed from the certified box lies within 1e-25 of v(u_cdx).
a12c = mp.sqrt(u_cdx[0]**2 + u_cdx[1]**2); nrc = mp.sqrt(sum(x**2 for x in u_cdx))
v1c = [u_cdx[1]/a12c, -u_cdx[0]/a12c, mp.mpf(0)]; v2c = [u_cdx[0]*u_cdx[2]/(a12c*nrc), u_cdx[1]*u_cdx[2]/(a12c*nrc), -a12c**2/(a12c*nrc)]
ok = True
for i in range(3):
    ok &= contains(iv.mpf([v1c[i]-mp.mpf('1e-25'), v1c[i]+mp.mpf('1e-25')]), v1_iv[i]) and contains(iv.mpf([v2c[i]-mp.mpf('1e-25'), v2c[i]+mp.mpf('1e-25')]), v2_iv[i])
check("C2/C3: the exact normalized v1(u*), v2(u*) (enclosed from the certified host box) lie inside 1e-25 boxes around the basis computed from Codex's printed host", ok)
val("C: max distance of Codex printed host from the certified centre", mp.nstr(max(abs(u_cdx[i] - mp.mpf(cen[i].numerator)/mp.mpf(cen[i].denominator)) for i in range(3)), 3))
check("C4: the quotient conversion depends on the basis only through u_iv, v1_iv, v2_iv (and lambda): the rerun below uses the certified-box intervals directly", True)

# ---------- interval forward-mode AD (same structure as Codex, exact endpoints) ----------
IVT = type(iv.mpf(0))
def ip(x): return x if isinstance(x, IVT) else iv.mpf(x)
class AD:
    def __init__(self, v, d, n): self.v = ip(v); self.d = d; self.n = n
    @staticmethod
    def const(v, n): return AD(v, [iv.mpf(0)]*n, n)
    def __add__(self, b):
        b = b if isinstance(b, AD) else AD.const(b, self.n); return AD(self.v + b.v, [x + y for x, y in zip(self.d, b.d)], self.n)
    __radd__ = __add__
    def __neg__(self): return AD(-self.v, [-x for x in self.d], self.n)
    def __sub__(self, b): return self + (-b if isinstance(b, AD) else AD.const(-ip(b), self.n))
    def __rsub__(self, b): return (-self) + b
    def __mul__(self, b):
        b = b if isinstance(b, AD) else AD.const(b, self.n); return AD(self.v*b.v, [x*b.v + self.v*y for x, y in zip(self.d, b.d)], self.n)
    __rmul__ = __mul__
    def inv(self):
        assert not (LO(self.v) <= 0 <= HI(self.v)), "division by interval containing zero"
        return AD(1/self.v, [-x/(self.v*self.v) for x in self.d], self.n)
    def __truediv__(self, b): b = b if isinstance(b, AD) else AD.const(b, self.n); return self*b.inv()
    def atan_ratio(self):   # atan of a ratio already formed; caller guarantees denominator > 0
        return AD(iv.atan2(self.v, iv.mpf(1)), [x/(1 + self.v*self.v) for x in self.d], self.n)
    def atan2(self, x):     # self = y
        r2 = x.v*x.v + self.v*self.v; assert LO(r2) > 0
        return AD(iv.atan2(self.v, x.v), [(x.v*dy - self.v*dx)/r2 for dy, dx in zip(self.d, x.d)], self.n)
    def sin(self): return AD(iv.sin(self.v), [iv.cos(self.v)*x for x in self.d], self.n)
    def cos(self): return AD(iv.cos(self.v), [-iv.sin(self.v)*x for x in self.d], self.n)
    def sqrt(self):
        assert LO(self.v) > 0; s = iv.sqrt(self.v); return AD(s, [x/(2*s) for x in self.d], self.n)

def presync(xr, yr):
    smx = sum(xr[1:], xr[0]); smy = sum(yr[1:], yr[0]); pr = []; pi = []
    for i in range(3):
        ab = xr[i]*xr[i] + yr[i]*yr[i]
        pr.append(xr[i] + (xr[i]*(-(ab - k[i])))*eps + (smx - 3*xr[i])*g)
        pi.append(yr[i] + (yr[i]*(-(ab - k[i])))*eps + (smy - 3*yr[i])*g)
    return pr, pi
def cut_excluded(pr, pi):   # box (pr,pi) avoids the closed negative real axis: continuity of atan2 on the box
    return LO(pr.v) > 0 or LO(pi.v) > 0 or HI(pi.v) < 0

full_log = {"min_radius_lo": None, "cut_ok": True, "widths": []}
def full_ad(bx):
    z = [AD(bx[i], [iv.mpf(1 if i == j else 0) for j in range(6)], 6) for i in range(6)]
    pr, pi = presync(z[:3], z[3:])
    rad = [(pr[i]*pr[i] + pi[i]*pi[i]).sqrt() for i in range(3)]
    for i in range(3):
        full_log["cut_ok"] &= cut_excluded(pr[i], pi[i])
    rlo = min(LO(rad[i].v) for i in range(3))
    full_log["min_radius_lo"] = rlo if full_log["min_radius_lo"] is None else min(full_log["min_radius_lo"], rlo)
    ph = [pi[i].atan2(pr[i]) for i in range(3)]
    out = []
    for i in range(3):
        h = ph[i] + sum(((ph[j] - ph[i])*3).sin() for j in range(3) if j != i)*lam
        out.append(rad[i]*h.cos())
    for i in range(3):
        h = ph[i] + sum(((ph[j] - ph[i])*3).sin() for j in range(3) if j != i)*lam
        out.append(rad[i]*h.sin())
    return out
MV_COUNT = {"steps": 0, "centre_in_box": True}
def mean_value_step(bx, ad_fun, n):
    outb = ad_fun(bx); J = [[outb[i].d[j] for j in range(n)] for i in range(n)]
    c = [mid_point(x) for x in bx]
    cin = all(contains(bx[i], ivpt(c[i])) for i in range(n)); MV_COUNT["steps"] += 1; MV_COUNT["centre_in_box"] &= cin
    assert cin, "mean-value centre not inside the box"
    cv = ad_fun([ivpt(x) for x in c])
    new = [cv[i].v + sum((J[i][j]*(bx[j] - ivpt(c[j])) for j in range(n)), iv.mpf(0)) for i in range(n)]
    return new, J

# ---------- B. full-state propagation 0..20 ----------
for n in range(21):
    box, _ = mean_value_step(box, full_ad, 6)
    full_log["widths"].append(max(width(x) for x in box))
val("B: full-state min pre-sync radius lower bound over steps 0-20", mp.nstr(mp.mpf(full_log["min_radius_lo"].numerator)/full_log["min_radius_lo"].denominator, 25))
val("B: full-state final (step 21) max width", mp.nstr(mp.mpf(full_log["widths"][-1].numerator)/full_log["widths"][-1].denominator, 8))
check("B: every pre-sync radius box over steps 0-20 is strictly positive (lower bound >= 0.0422121224279638593 as Codex reported)", full_log["min_radius_lo"] >= Fraction('0.042212122427963859') )
check("B: every (pre-sync real, imag) box over steps 0-20 excludes the closed negative real axis -> atan2 continuous on every box, mean-value form valid", full_log["cut_ok"])
print("   elapsed", round(time.time()-T0, 1), "s", flush=True)

# ---------- D. conversion to the M2 gauge (atan2, exact basis intervals) ----------
xr = box[:3]; yi = box[3:]
dr = sum((xr[i]*u_iv[i] for i in range(3)), iv.mpf(0)); di = sum((yi[i]*u_iv[i] for i in range(3)), iv.mpf(0))
val("D: conversion gauge argument u.Omega_21: Re box, Im box", [[mp.nstr(lo_mpf(dr), 15), mp.nstr(hi_mpf(dr), 15)], [mp.nstr(lo_mpf(di), 15), mp.nstr(hi_mpf(di), 15)]])
cut_ok_conv = (LO(dr) > 0) or (LO(di) > 0) or (HI(di) < 0)
check("D: at the conversion (index 21) the gauge uses atan2 (Codex did too): u.Omega_21 is bounded away from zero and its box excludes the closed negative real axis (here Re < 0, Im strictly one-signed), so atan2 is continuous on the box", cut_ok_conv and (LO(dr*dr + di*di) > 0))
val("D: |u.Omega_21|^2 lower bound", mp.nstr(lo_mpf(dr*dr + di*di), 15))
th = iv.atan2(di, dr); cs = iv.cos(th); sn = iv.sin(th)
Rr = [xr[i]*cs + yi[i]*sn for i in range(3)]; Ii = [yi[i]*cs - xr[i]*sn for i in range(3)]
qbox = [Rr[i] - u_iv[i] for i in range(3)] + [sum((Ii[i]*v1_iv[i] for i in range(3)), iv.mpf(0)), sum((Ii[i]*v2_iv[i] for i in range(3)), iv.mpf(0))]
val("D: quotient box max width right after conversion (index 21)", mp.nstr(fr2(max(width(x) for x in qbox)), 6))

# ---------- E. quotient propagation 21..300 ----------
qlog = {"pr_lo": None, "gauge_lo": None, "rad_lo": None, "cut_ok": True}
def q_ad(bx):
    z = [AD(bx[i], [iv.mpf(1 if i == j else 0) for j in range(5)], 5) for i in range(5)]
    yy = [z[3]*v1_iv[i] + z[4]*v2_iv[i] for i in range(3)]
    xr = [z[i] + u_iv[i] for i in range(3)]
    pr, pi = presync(xr, yy)
    plo = min(LO(x.v) for x in pr); qlog["pr_lo"] = plo if qlog["pr_lo"] is None else min(qlog["pr_lo"], plo)
    assert plo > 0, "ratio-atan chart requires pre-sync real part > 0"
    rad = [(pr[i]*pr[i] + pi[i]*pi[i]).sqrt() for i in range(3)]
    rlo = min(LO(r.v) for r in rad); qlog["rad_lo"] = rlo if qlog["rad_lo"] is None else min(qlog["rad_lo"], rlo)
    ph = [(pi[i]/pr[i]).atan_ratio() for i in range(3)]
    rr = []; ii = []
    for i in range(3):
        h = ph[i] + sum(((ph[j] - ph[i])*3).sin() for j in range(3) if j != i)*lam
        rr.append(rad[i]*h.cos()); ii.append(rad[i]*h.sin())
    den = sum((rr[i]*u_iv[i] for i in range(3)), AD.const(0, 5)); num = sum((ii[i]*u_iv[i] for i in range(3)), AD.const(0, 5))
    dlo = LO(den.v); qlog["gauge_lo"] = dlo if qlog["gauge_lo"] is None else min(qlog["gauge_lo"], dlo)
    assert dlo > 0, "gauge ratio-atan requires u.Re(F) > 0"
    tg = (num/den).atan_ratio(); qlog["last_theta"] = tg.v
    Rq = [rr[i]*tg.cos() + ii[i]*tg.sin() for i in range(3)]; Iq = [ii[i]*tg.cos() - rr[i]*tg.sin() for i in range(3)]
    out = [Rq[i] - u_iv[i] for i in range(3)] + [sum((Iq[i]*v1_iv[i] for i in range(3)), AD.const(0, 5)), sum((Iq[i]*v2_iv[i] for i in range(3)), AD.const(0, 5))]
    return out
for n in range(21, 300):
    qbox, _ = mean_value_step(qbox, q_ad, 5)
q_ad(qbox)   # evaluate the chart bounds at index 300 as well (Codex did)
fr2 = lambda f: mp.mpf(f.numerator)/f.denominator
val("E: quotient chart lower bounds over indices 21-300: pre-sync real parts, gauge denominator u.Re(F), radii", [mp.nstr(fr2(qlog["pr_lo"]), 20), mp.nstr(fr2(qlog["gauge_lo"]), 20), mp.nstr(fr2(qlog["rad_lo"]), 20)])
check("D/E: all ratio-atan denominators (pre-sync real parts) > 1.3096 and the gauge denominator > 0 throughout 21-300 (Codex reported 1.3096147241289281421 for the former; the latter was not recorded by Codex)", qlog["pr_lo"] >= Fraction('1.3096147241289281') and qlog["gauge_lo"] > 0)
check("E: quotient radii lower bound >= 1.3132035799719558 over 21-300", qlog["rad_lo"] >= Fraction('1.3132035799719558'))
qw = max(width(x) for x in qbox); val("E: final N=300 quotient box max width", mp.nstr(fr2(qw), 8))
check("E: final N=300 quotient box max width <= 1.4603673018171074548e-22 (Codex) within 1%", qw <= Fraction('1.4603673018171074548e-22')*Fraction(101,100))
val("E: N=300 quotient box", [[mp.nstr(lo_mpf(x), 25), mp.nstr(hi_mpf(x), 25)] for x in qbox])
print("   elapsed", round(time.time()-T0, 1), "s", flush=True)

# ---------- G. weighted trapping certificate ----------
zplus = [mp.mpf(s) for s in codex['cycle_plus']]
rb = [mp.mpf(s) for s in ('3.5322590088879646e-5', '3.6441896819931174e-5', '4.2514894042419980e-5', '1.0984693497410257e-5', '1.0e-4')]
Up = [iv.mpf([zplus[i] - rb[i], zplus[i] + rb[i]]) for i in range(5)]
qlog2 = {"pr_lo": None, "gauge_lo": None, "rad_lo": None}; saved = dict(qlog); qlog.update({"pr_lo": None, "gauge_lo": None, "rad_lo": None})
o1 = q_ad(Up); J1 = [[o1[i].d[j] for j in range(5)] for i in range(5)]
c_pt = [ivpt(z) for z in zplus]; Fc = [x.v for x in q_ad(c_pt)]
Um = [Fc[i] + sum((J1[i][j]*(Up[j] - c_pt[j]) for j in range(5)), iv.mpf(0)) for i in range(5)]       # U_minus = enclosure of Fhat(U_plus)
o2 = q_ad(Um); J2 = [[o2[i].d[j] for j in range(5)] for i in range(5)]
JJ = [[sum((J2[i][r]*J1[r][j] for r in range(5)), iv.mpf(0)) for j in range(5)] for i in range(5)]
F2c = [x.v for x in q_ad(Fc)]   # interval evaluation of Fhat at the interval value Fhat(c): encloses Fhat^2(c)
Zw = [F2c[i] + sum((JJ[i][j]*(Up[j] - c_pt[j]) for j in range(5)), iv.mpf(0)) for i in range(5)]
inside = all(strict_inside(Up[i], Zw[i]) for i in range(5))
margins = [min(LO(Zw[i]) - LO(Up[i]), HI(Up[i]) - HI(Zw[i])) for i in range(5)]
val("G: strict-interior margins of Fhat^2(U_plus) in U_plus (exact endpoints, interval Fhat^2(c))", [mp.nstr(fr2(m), 10) for m in margins])
check("G: Fhat^2(U_plus) subset interior(U_plus) with all five margins positive (Codex: 2.416e-6, 2.492e-6, 2.846e-6, 4.636e-7, 6.756e-6)", inside and all(m > 0 for m in margins))
rbF = [frac_t(x._mpf_) for x in rb]
ratios = [sum(absup(JJ[i][j])*rbF[j] for j in range(5))/rbF[i] for i in range(5)]
val("G: weighted row bounds of |D(Fhat^2)| over U_plus (rigorous upper bounds)", [mp.nstr(fr2(r), 15) for r in ratios])
check("G: weighted contraction factor max_i < 1 (Codex 0.957798686507835)", max(ratios) < 1 and abs(fr2(max(ratios)) - mp.mpf('0.957798686507835')) < mp.mpf('1e-9'))
val("G: chart lower bounds during the two trap evaluations (pre-sync real, gauge denominator, radii)", [mp.nstr(fr2(qlog["pr_lo"]), 20), mp.nstr(fr2(qlog["gauge_lo"]), 20), mp.nstr(fr2(qlog["rad_lo"]), 20)])
check("G: trap chart radii lower bound >= 1.5073367430120650 (Codex) and all denominators positive", qlog["rad_lo"] >= Fraction('1.507336743012065') and qlog["pr_lo"] > 0 and qlog["gauge_lo"] > 0)
val("G: U_minus radii (exact)", [mp.nstr(fr2(width(x)/2), 15) for x in Um])
# disjointness of U_plus and U_minus
disj = any(HI(Up[i]) < LO(Um[i]) or HI(Um[i]) < LO(Up[i]) for i in range(5))
gap = max(min(LO(Um[i]) - HI(Up[i]), LO(Up[i]) - HI(Um[i])) for i in range(5))
val("G: separation between U_plus and U_minus (largest coordinate gap)", mp.nstr(fr2(gap), 10))
check("G: U_plus and U_minus are disjoint (gap ~0.87 in coordinate 5) -> the F^2 fixed point is not an F fixed point", disj)
# entry
check("E/G: N=300 quotient box subset U_minus (exact endpoints)", all(contains(Um[i], qbox[i]) for i in range(5)))
val("E/G: max |qbox endpoint - U_minus centre| / U_minus radius", mp.nstr(max(max(abs(fr2(LO(qbox[i])) - (lo_mpf(Um[i])+hi_mpf(Um[i]))/2), abs(fr2(HI(qbox[i])) - (lo_mpf(Um[i])+hi_mpf(Um[i]))/2))/fr2(width(Um[i])/2) for i in range(5)), 10))
check("centre-in-box held at every mean-value step (count %d)" % MV_COUNT["steps"], MV_COUNT["centre_in_box"])
check("trap centre box c_pt lies inside U_plus (mean-value form with interval centre valid)", all(contains(Up[i], c_pt[i]) for i in range(5)))
# ---------- ENTRY (v0.2): qbox_300 subset U_minus-box is NOT by itself a capture statement ----------
# U_minus-box is an OUTER enclosure of Fhat(U_plus); a point of it need not be an image of U_plus. Test the box-level inference:
o_um = q_ad(Um); J_um = [[o_um[i].d[j] for j in range(5)] for i in range(5)]
cm = [mid_point(x) for x in Um]; assert all(contains(Um[i], ivpt(cm[i])) for i in range(5))
F_cm = [x.v for x in q_ad([ivpt(x) for x in cm])]
F_Um = [F_cm[i] + sum((J_um[i][j]*(Um[j] - ivpt(cm[j])) for j in range(5)), iv.mpf(0)) for i in range(5)]
box_level = all(strict_inside(Up[i], F_Um[i]) for i in range(5))
val("ENTRY: enclosure of Fhat(U_minus-box): radii vs U_plus radii", [[mp.nstr(fr2(width(F_Um[i])/2), 6), mp.nstr(fr2(rbF[i]), 6)] for i in range(5)])
val("ENTRY: box-level test Fhat(U_minus-box) subset int U_plus (would make Codex's inference valid as stated)", box_level)
R["values"]["entry_box_level_inference_holds"] = box_level
# Direct repair: one more validated step from the N=300 box.
q301, _ = mean_value_step(qbox, q_ad, 5)
direct = all(strict_inside(Up[i], q301[i]) for i in range(5))
mrel = max(max(abs(fr2(LO(q301[i])) - zplus[i]), abs(fr2(HI(q301[i])) - zplus[i]))/rb[i] for i in range(5))
val("ENTRY: N=301 box: max |endpoint - z_plus| / U_plus radius", mp.nstr(mrel, 10))
val("ENTRY: N=301 quotient box", [[mp.nstr(lo_mpf(x), 40), mp.nstr(hi_mpf(x), 40)] for x in q301])
R["values"]["EXACT: N=300 box endpoints (rationals)"] = [[str(LO(x)), str(HI(x))] for x in qbox]
R["values"]["EXACT: N=301 box endpoints (rationals)"] = [[str(LO(x)), str(HI(x))] for x in q301]
check("ENTRY (repair, direct): Fhat(qbox_300) = qbox_301 subset int U_plus -> F^301(Omega_0) is in the trap U_plus", direct)
HUp = [Up[0], Up[1], Up[2], -Up[3], -Up[4]]
alt = all(strict_inside(HUp[i], qbox[i]) for i in range(5))
check("ENTRY (repair, alternative): qbox_300 subset int H(U_plus); H(U_plus) is a trap for Fhat^2 by exact H-equivariance (same margins, same weighted bound)", alt)
# gauge angles on the cycle neighbourhood: theta over U_plus and over U_minus-box (phase-accumulation argument)
q_ad(Up); th_p = qlog["last_theta"]; q_ad(HUp); th_hp = qlog["last_theta"]
val("PHASE: gauge-angle enclosure theta(F(Omega(z))) over U_plus and over H(U_plus)", [[mp.nstr(lo_mpf(th_p), 12), mp.nstr(hi_mpf(th_p), 12)], [mp.nstr(lo_mpf(th_hp), 12), mp.nstr(hi_mpf(th_hp), 12)]])
check("PHASE: theta(H z) = -theta(z) consistency: the two enclosures are negatives of each other up to rounding, and their sum contains 0", LO(th_p + th_hp) <= 0 <= HI(th_p + th_hp))
# ---------- H. one-step H-composed contraction: G = H o Fhat on U_plus ----------
Hm = lambda X: [X[0], X[1], X[2], -X[3], -X[4]]
HUm = Hm(Um)
inside1 = all(strict_inside(Up[i], HUm[i]) for i in range(5))
m1 = [min(LO(HUm[i]) - LO(Up[i]), HI(Up[i]) - HI(HUm[i])) for i in range(5)]
val("H: margins of H(Fhat(U_plus)) inside U_plus", [mp.nstr(fr2(m), 10) for m in m1])
ratios1 = [sum(absup(J1[i][j])*rbF[j] for j in range(5))/rbF[i] for i in range(5)]
val("H: weighted row bounds of |D(H o Fhat)| = |D Fhat| over U_plus", [mp.nstr(fr2(r), 15) for r in ratios1])
val("H: one-step G = H o Fhat self-map/contraction with Codex's weights on U_plus (informational)", {"H(Fhat(U_plus)) strictly inside U_plus": inside1, "max weighted row bound": mp.nstr(fr2(max(ratios1)), 12)})
R["values"]["G_one_step_contraction_max"] = mp.nstr(fr2(max(ratios1)), 15)
# Krawczyk existence test for G(z) - z = 0 on U_plus (G = H o Fhat): a solution is an F^2 fixed point in U_plus, hence equals p.
Hsign = [1, 1, 1, -1, -1]
Gc = [Hsign[i]*Fc[i] for i in range(5)]                       # G(c) interval (Fc = interval Fhat(c))
DG = [[J1[i][j]*Hsign[i] for j in range(5)] for i in range(5)]  # DG over U_plus
Amid = mp.matrix(5, 5)
for i in range(5):
    for j in range(5): Amid[i, j] = (lo_mpf(DG[i][j]) + hi_mpf(DG[i][j]))/2 - (1 if i == j else 0)
Y = mp.inverse(Amid); Yiv = [[ivpt(Y[i, j]) for j in range(5)] for i in range(5)]
Gc_minus_c = [Gc[i] - c_pt[i] for i in range(5)]
Kr = []
for i in range(5):
    acc = c_pt[i] - sum((Yiv[i][j]*Gc_minus_c[j] for j in range(5)), iv.mpf(0))
    for j in range(5):
        coeff = iv.mpf(1 if i == j else 0) - sum((Yiv[i][l]*(DG[l][j] - iv.mpf(1 if l == j else 0)) for l in range(5)), iv.mpf(0))
        acc = acc + coeff*(Up[j] - c_pt[j])
    Kr.append(acc)
kr_inside = all(strict_inside(Up[i], Kr[i]) for i in range(5))
val("H: Krawczyk image radii for G(z)=z on U_plus vs U_plus radii", [[mp.nstr(fr2(width(Kr[i])/2), 6), mp.nstr(fr2(rbF[i]), 6)] for i in range(5)])
val("H: Krawczyk |G(c)-c| residual (interval upper bound)", mp.nstr(max(fr2(absup(x)) for x in Gc_minus_c), 6))
check("H (repair): Krawczyk K(U_plus) subset interior(U_plus) for G = H o Fhat -> there EXISTS z* in U_plus with Fhat(z*) = H(z*); z* is an Fhat^2 fixed point in U_plus, so z* = p: the captured point is the H-symmetric two-cycle", kr_inside)
# enlarged-box one-step G contraction (Perron-weighted), for the record
A1 = [[fr2(absup(J1[i][j])) for j in range(5)] for i in range(5)]
wv = [mp.mpf(1)]*5
for _ in range(200):
    nw = [sum(A1[i][j]*wv[j] for j in range(5)) for i in range(5)]; m = max(nw); wv = [x/m for x in nw]
rho1 = max(sum(A1[i][j]*wv[j] for j in range(5))/wv[i] for i in range(5))
val("H: Perron estimate of the weighted one-step |DFhat| norm over U_plus (spectral radius of |J1| upper matrix)", mp.nstr(rho1, 10))
val("H: note", "one-step Perron radius < 1 suggests a one-step weighted trap could also be built with different weights; not needed: the F^2 trap plus the Krawczyk existence test for Fhat(z) = H(z) already identifies the captured point as the H-symmetric cycle")
print("   elapsed", round(time.time()-T0, 1), "s", flush=True)

npass = sum(R["checks"].values()); R["summary"] = f"{npass}/{len(R['checks'])}"; print("SUMMARY", R["summary"])
for kk, vv in R["checks"].items():
    if not vv: print("  FAILED:", kk)
R["script_sha256"] = hashlib.sha256(open(__file__, 'rb').read()).hexdigest(); R["versions"] = {"python": sys.version.split()[0], "mpmath": mp.__version__, "iv_dps": iv.dps, "mp_dps": mp.mp.dps}
R["inputs"] = {"gpt_m2_certificate_json_sha256": hashlib.sha256(open(sys.argv[1], 'rb').read()).hexdigest(), "codex_m3_validated_entry_json_sha256": hashlib.sha256(open(sys.argv[2], 'rb').read()).hexdigest()}
json.dump(R, open(__file__.replace('.py', '_results%s.json' % ("" if IVDPS == 80 else "_dps%d" % IVDPS)), 'w'), indent=1, default=str)
