"""K2a independent parity for Paper A and channel symmetries, one step only."""

from itertools import permutations
from unittest.mock import patch

import mpmath as mp
import numpy as np
import sympy as sp

from kernel_physics import covering, dynamics as d
from kernel_physics.readouts import z_chiral
from kernel_physics.tests.parity_oracles import paper_a_oracle as a
from kernel_physics.tests.test_parity_oracle_boundaries import ParityCase


W = (complex(3/8, 7/8), complex(-1/2, 1/4), complex(1/8, -3/4))
K = (1/2, 5/4, 3/2)


def symbols():
    x = sp.symbols("x0:3", real=True)
    y = sp.symbols("y0:3", real=True)
    return sp.Matrix([x[j]+sp.I*y[j] for j in range(3)])


class P1Tests(ParityCase):
    """PASS SUPPORTS: accepted one-step polynomial, simultaneous phase and Arg0.
    PASS DOES NOT SUPPORT: multi-step, global, stability or physical behavior.
    """

    def test_polynomial_and_phase_off(self):
        w = symbols()
        eps, g = sp.symbols("eps g", real=True)
        k = sp.symbols("k0:3", real=True)
        defining = w + eps*sp.Matrix([w[j]*(k[j]-sp.expand_complex(w[j]*sp.conjugate(w[j]))) for j in range(3)]) + g*(sp.ones(3)-3*sp.eye(3))*w
        self.exact("P1", "symbolic expanded Paper A polynomial", a.polynomial(w, eps, g, k), defining)
        for name, v, e, coupling in (("dyadic spread", W, 1/16, 3/16),
                                     ("negative parameters", W, -1/32, -1/8),
                                     ("common zero", (0j,)*3, 1/16, 3/16)):
            ref, scales = a.step(v, e, coupling, K, 0)
            out = d.step3(v, d.DynamicsConfig(e, coupling, 0, K))
            self.bounded("P1", name, out, ref, scales, 32)

    def test_full_composition_and_direct_phase(self):
        for strength in (1/4, -1/5):
            ref, scales = a.step(W, 1/16, 3/16, K, strength)
            self.bounded("P1", f"full phase {strength}", d.step3(W, d.DynamicsConfig(1/16, 3/16, strength, K)), ref, scales, 64)
            ref, scales = a.synchronize(W, strength)
            out = d.phase_sync(W, strength)
            self.bounded("P1", f"direct phase {strength}", out, ref, scales, 64)
            self.bounded("P1", f"retained modulus {strength}", abs(out), [abs(v) for v in ref], scales, 64)

    def test_signed_zero_through_full_step(self):
        v = (complex(-0.0, 0.0), -1+1j, -2+.5j)
        strength = .25
        ref, scales = a.step(v, 0.0, 0.0, K, strength)
        captured = []
        original = d.phase_sync
        def observe_pre(values, lam):
            captured.append(values.copy())
            return original(values, lam)
        with patch.object(d, "phase_sync", side_effect=observe_pre):
            out = d.step3(v, d.DynamicsConfig(0, 0, strength, K))
        pre = captured[0]
        self.discrete("P1", "full-step negative-real signed zero exists", bool(pre[0] == 0 and np.signbit(pre[0].real)), True)
        self.discrete("P1", "Arg0 zero is positive zero", (float(d.arg0(pre)[0]), bool(np.signbit(d.arg0(pre)[0]))), (0.0, False))
        self.bounded("P1", "signed-zero full composition", out, ref, scales, 64)
        # Deliberately wrong alternatives, using the actual signed input but no
        # runtime target as an oracle. Both must alter BOTH nonzero neighbours.
        with mp.workdps(80):
            values = [a.number(z) for z in pre]
            p = [mp.arg(z) if z else mp.mpf(0) for z in values]
            ordinary = [mp.pi, p[1], p[2]]
            wrong_angle, omitted = [], []
            for j in (1, 2):
                other = [l for l in range(3) if l != j]
                wrong_angle.append(abs(values[j])*mp.exp(mp.j*(ordinary[j]+strength*sum(mp.sin(3*(ordinary[l]-ordinary[j])) for l in other))))
                omitted.append(abs(values[j])*mp.exp(mp.j*(p[j]+strength*sum(mp.sin(3*(p[l]-p[j])) for l in other if values[l]))))
            for label, mutant in (("ordinary-angle signed-zero falsifier", wrong_angle), ("omitted zero-neighbour falsifier", omitted)):
                self.falsifier("P1", label, all(abs(mutant[j-1]-ref[j]) > 1000*64*mp.mpf(2)**-52*scales[j] for j in (1, 2)))
        self.discrete("P1", "zero output branch", complex(out[0]), 0j)

    def test_sequential_falsifier(self):
        ref, scales = a.synchronize(W, .25)
        with mp.workdps(80):
            phase = [mp.arg(a.number(z)) for z in W]
            for j in range(3):
                phase[j] += mp.mpf(.25)*sum(mp.sin(3*(phase[l]-phase[j])) for l in range(3) if l != j)
            mutant = [abs(a.number(z))*mp.exp(mp.j*p) for z, p in zip(W, phase)]
            self.falsifier("P1", "sequential phase update", any(abs(x-y) > 1000*64*mp.mpf(2)**-52*s for x, y, s in zip(mutant, ref, scales)))
        self.bounded("P1", "simultaneous spread phases", d.phase_sync(W, .25), ref, scales, 64)


class P2Tests(ParityCase):
    """PASS SUPPORTS: equal-k synchronized scalar reduction including zeros/signs.
    PASS DOES NOT SUPPORT: unequal-k invariance or attraction/stability.
    """

    def test_exact_scalar_reduction_and_binary_cases(self):
        x, y, eps, g, kappa = sp.symbols("x y eps g kappa", real=True)
        w = x+sp.I*y
        self.exact("P2", "L3 annihilates e", (sp.ones(3)-3*sp.eye(3))*sp.ones(3, 1))
        self.exact("P2", "symbolic scalar reduction", a.polynomial([w]*3, eps, g, [kappa]*3), [w*(1+eps*(kappa-x*x-y*y))]*3)
        for name, w, e in (("complex", .5+.25j, .125), ("positive", .5, .125), ("common zero", 0j, .125), ("negative multiplier", 2+0j, 1.0)):
            ref, scales = a.step([w]*3, e, .25, (1,)*3, 0)
            for lam in (0,.25):
                out = d.step3([w]*3, d.DynamicsConfig(e, .25, lam, (1,)*3))
                self.bounded("P2", name+f" lambda={lam}", out, ref, scales, 32)
                self.discrete("P2", name+f" lambda={lam} span(e)", bool(out[0] == out[1] == out[2]), True)

    def test_unequal_k_falsifier(self):
        ref, scales = a.step([.5+.25j]*3, .125, .25, K, 0)
        out = d.step3([.5+.25j]*3, d.DynamicsConfig(.125, .25, 0, K))
        self.bounded("P2", "unequal ordered k", out, ref, scales, 32)
        self.falsifier("P2", "unequal k leaves span(e)", len(set(out)) == 3)


class P3Tests(ParityCase):
    """PASS SUPPORTS: triad S3 with permuted k, conjugation, qualified common U(1).
    PASS DOES NOT SUPPORT: ring S3, global phase-on U(1), spatial chirality.
    """

    def test_symbolic_polynomial_symmetries_and_chirality(self):
        w = symbols()
        eps, g = sp.symbols("eps g", real=True)
        k = sp.symbols("k0:3", real=True)
        f = a.polynomial(w, eps, g, k)
        c = a.chirality(w)
        for p in permutations(range(3)):
            P = sp.eye(3)[list(p), :]
            self.exact("P3", f"symbolic S3 {p}", a.polynomial(P*w, eps, g, P*sp.Matrix(k)), P*f)
            self.exact("P3", f"oriented chirality {p}", a.chirality(P*w), P.det()*P*c)
        self.exact("P3", "symbolic conjugation", a.polynomial(sp.conjugate(w), eps, g, k), sp.conjugate(f))
        self.exact("P3", "chirality conjugation sign", a.chirality(sp.conjugate(w)), -c)
        # Exact unit-circle parametrization; the omitted point (-1,0) is
        # separately polynomial and is included as rotation -1.
        t = sp.symbols("t", real=True)
        rotation = (1-t*t+2*sp.I*t)/(1+t*t)
        for r in (rotation, -1):
            self.exact("P3", "symbolic global U1", a.polynomial(r*w, eps, g, k), r*f)
            self.exact("P3", "chirality U1", a.chirality(r*w), c)

    def test_all_six_permutations_and_fixed_k_negative(self):
        for lam in (0, .25):
            _, base_scale = a.step(W, .0625, .1875, K, lam)
            base = d.step3(W, d.DynamicsConfig(.0625, .1875, lam, K))
            for p in permutations(range(3)):
                w, k = tuple(W[i] for i in p), tuple(K[i] for i in p)
                _, scale = a.step(w, .0625, .1875, k, lam)
                out = d.step3(w, d.DynamicsConfig(.0625, .1875, lam, k))
                self.bounded("P3", f"S3 lambda={lam} p={p}", out, base[list(p)], [scale[j]+base_scale[p[j]] for j in range(3)], 128, "BINARY64_TERM_SCALE")
        p = [1, 0, 2]
        _, scale = a.step(tuple(W[i] for i in p), .0625, .1875, K, 0)
        wrong = d.step3(np.array(W)[p], d.DynamicsConfig(.0625, .1875, 0, K))
        base = d.step3(W, d.DynamicsConfig(.0625, .1875, 0, K))
        self.falsifier("P3", "fixed unequal k permutation", np.max(abs(wrong-base[p])) > 1e-3)

    def test_conjugation_u1_and_zero_counterexample(self):
        rotation = complex(.6, .8)
        for lam in (0, .25):
            ref, base_scale = a.step(W, .0625, .1875, K, lam)
            base = d.step3(W, d.DynamicsConfig(.0625, .1875, lam, K))
            for name, transform in (("conjugation", np.conjugate), ("common U1 nonzero stratum", lambda v: rotation*np.asarray(v))):
                w = transform(W)
                pre, _ = a.presync(w, .0625, .1875, K)
                self.assertTrue(all(pre))
                _, scale = a.step(w, .0625, .1875, K, lam)
                out = d.step3(w, d.DynamicsConfig(.0625, .1875, lam, K))
                self.bounded("P3", f"{name} lambda={lam}", out, transform(base), [x+y for x,y in zip(scale,base_scale)], 128, "BINARY64_TERM_SCALE")
        zero = (0j, W[1], W[2])
        for lam in (0, .25):
            _, s1 = a.step(zero, 0, 0, K, lam)
            _, s2 = a.step(rotation*np.asarray(zero), 0, 0, K, lam)
            base = d.step3(zero, d.DynamicsConfig(0, 0, lam, K))
            out = d.step3(rotation*np.asarray(zero), d.DynamicsConfig(0, 0, lam, K))
            if lam == 0:
                self.bounded("P3", "global phase-off includes zero", out, rotation*base, [x+y for x,y in zip(s1,s2)], 128, "BINARY64_TERM_SCALE")
            else:
                self.falsifier("P3", "phase-on global U1 false at pre-sync zero", np.max(abs(out-rotation*base)) > .01)
        for p in permutations(range(3)):
            w = np.array(W)[list(p)]
            ref, scale = a.chiral_reference(w)
            self.bounded("P3", f"raw chirality {p}", z_chiral(w), ref, scale, 128)
        for name, w in (("chirality conjugate", np.conjugate(W)), ("chirality rotation", rotation*np.array(W))):
            ref, scale = a.chiral_reference(w)
            self.bounded("P3", name, z_chiral(w), ref, scale, 128)


class P4Tests(ParityCase):
    """PASS SUPPORTS: exact P/Q divisor domains, multiplicities, one-step P lifts.
    PASS DOES NOT SUPPORT: sector attraction or long-time ring/triad closeness;
    M=3 is a self-path sanity check, with different paths only at M=6,12,24.
    """

    def test_exact_matrices_and_domain(self):
        for n in (1, 2, 3, 4, 5, 6, 12, 24):
            self.exact("P4", f"cycle multiplicity n={n}", covering.cycle_laplacian(n), a.cycle(n))
        self.exact("P4", "size two doubled incidence", a.cycle(2), [[-2,2],[2,-2]])
        for m,d0 in ((1,1),(2,1),(2,2),(3,3),(6,3),(12,3),(24,3),(6,2),(3,2),(5,3),(2,3),(1,4)):
            P = a.pullback(m,d0)
            self.exact("P4", f"P definition {m,d0}", covering.pullback_matrix(m,d0), P)
            residual = a.cycle(m)*P-P*a.cycle(d0)
            self.discrete("P4", f"intertwining iff divisor {m,d0}", residual == sp.zeros(m,d0), m%d0 == 0)
            if m%d0 == 0:
                Q = P/sp.sqrt(sp.Rational(m,d0))
                self.exact("P4", f"Q definition {m,d0}", covering.isometric_pullback(m,d0), Q)
                self.exact("P4", f"Q isometry {m,d0}", Q.T*Q, sp.eye(d0))
                self.exact("P4", f"Q compression {m,d0}", Q.T*a.cycle(m)*Q, a.cycle(d0))
            else:
                with self.assertRaises(ValueError):
                    covering.isometric_pullback(m,d0)
        P = a.pullback(3,2)
        projector = P*(P.T*P).inv()*P.T
        self.exact("P4", "exception (3,2) image invariant", (sp.eye(3)-projector)*a.cycle(3)*P)
        self.falsifier("P4", "(3,2) invariant image is not intertwining", a.cycle(3)*P != P*a.cycle(2))

    def test_nonlinear_p_lifts_and_off_sector_wrap(self):
        for m in (3,6,12,24):
            for name,w in (("spread", W), ("zero component", (0j,W[1],W[2])), ("all zero", (0j,)*3)):
                for lam in (0,.25):
                    lifted = tuple(w[j%3] for j in range(m))
                    ref, scales = a.step(lifted,.0625,.1875,K,lam)
                    pre_ref, pre_scales = a.presync(lifted,.0625,.1875,K)
                    _, tri_scales = a.step(w,.0625,.1875,K,lam)
                    config = d.DynamicsConfig(.0625,.1875,lam,K)
                    captured = []
                    original = d.phase_sync
                    def observe_pre(values,strength):
                        captured.append(values.copy())
                        return original(values,strength)
                    with patch.object(d,"phase_sync",side_effect=observe_pre):
                        ring = d.step_ring(lifted,config)
                    tri = d.step3(w,config)
                    fixture = f"P lift m={m} {name} lambda={lam}"
                    self.bounded("P4",fixture+" pre-sync including coupling",captured[0],pre_ref,pre_scales,128)
                    self.bounded("P4",fixture+" independent map",ring,ref,scales,128)
                    self.bounded("P4",fixture+" paths",ring,[tri[j%3] for j in range(m)],[scales[j]+tri_scales[j%3] for j in range(m)],128,"BINARY64_TERM_SCALE")
            w = tuple(complex((j%5-2)/8,(j%7-3)/8) for j in range(m))
            ref, scales = a.step(w,.0625,.1875,K,.25)
            self.bounded("P4",f"off-sector periodic wrap m={m}",d.step_ring(w,d.DynamicsConfig(.0625,.1875,.25,K)),ref,scales,128)

    def test_q_substitution_and_ring_rejections(self):
        # M/d=4 gives exact binary scaling 1/2; no sqrt rounding explains failure.
        tri = d.step3(W,d.DynamicsConfig(.125,.25,0,K))
        q_w = tuple(W[j%3]/2 for j in range(12))
        ref, scales = a.step(q_w,.125,.25,K,0)
        ring = d.step_ring(q_w,d.DynamicsConfig(.125,.25,0,K))
        self.bounded("P4","Q substituted input actual recurrence",ring,ref,scales,128)
        self.falsifier("P4","Q is not nonlinear lifting operator",np.max(abs(ring-np.tile(tri/2,4))) > .01)
        for m in (4,5):
            with self.assertRaises(ValueError):
                d.step_ring([1j]*m,d.DynamicsConfig(.125,.25,0,K))
        self.discrete("P4","ring sizes 4,5 rejected",True,True)
