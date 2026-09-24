"""Self-contained K2 checks; no papers, repository metadata or historical imports."""
from dataclasses import FrozenInstanceError
import json
import math
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import mpmath as mp
import numpy as np
import sympy as sp

from kernel_physics import readouts
from kernel_physics.dynamics import DynamicsConfig, step3
from kernel_physics import z_manifold as z


class ClockTests(unittest.TestCase):
    def test_defaults_wrap_and_integer_q(self):
        c = z.Clock(q=11)
        nxt = z.advance_clock(c, .1)
        self.assertEqual((c.q, c.t, c.N, c.q_step), (11, 0., 12, 1))
        self.assertEqual((nxt.q, nxt.t), (0, .1))
        self.assertIs(type(nxt.q), int)
        self.assertEqual(z.clock_angle(nxt), 0.)

    def test_non_twelve_sectors_and_signed_multistep(self):
        c = z.Clock(q=6, N=7, t=2, q_step=3)
        nxt = z.advance_clock(c, -.25)
        self.assertEqual((nxt.q, nxt.t), (2, 1.75))
        self.assertAlmostEqual(z.clock_angle(nxt), 4*math.pi/7)
        self.assertEqual(z.advance_clock(z.Clock(q=0, N=7, q_step=-2), 0).q, 5)

    def test_zero_and_selected_dt(self):
        c = z.Clock(q=2, t=1.25)
        self.assertEqual(z.advance_clock(c, 0), z.Clock(q=3, t=1.25))
        self.assertEqual(z.advance_clock(c, .75), z.Clock(q=3, t=2.))
        self.assertEqual(z.advance_clock(z.Clock(t=1), -1).t, 0.)

    def test_huge_integer_periodicity(self):
        c = z.Clock(q=12*10**400+3)
        self.assertEqual(z.clock_angle(c), math.pi/2)
        self.assertEqual(c.q, 12*10**400+3)
        self.assertEqual(z.clock_angle(z.Clock(q=-1)), z.clock_angle(z.Clock(q=11)))

    def test_invalid_clock_fields_and_dt(self):
        for name in ('q', 'N', 'q_step'):
            for bad in (True, np.bool_(False), 1.0, '1', 1j, np.array(1)):
                with self.subTest(name=name, bad=repr(bad)), self.assertRaises(TypeError):
                    z.Clock(**{name: bad})
        for bad in (0, -2):
            with self.assertRaises(ValueError):
                z.Clock(N=bad)
        for bad in (True, '1', 1j, np.nan, np.inf, np.array([1.])):
            with self.subTest(bad=repr(bad)), self.assertRaises((TypeError, ValueError)):
                z.Clock(t=bad)
            with self.assertRaises((TypeError, ValueError)):
                z.advance_clock(z.Clock(), bad)
        with self.assertRaises(TypeError):
            z.clock_angle(0)

    def test_clock_range_and_stagnation_failures(self):
        c = z.Clock(t=1e300)
        for dt in (1., -1.):
            with self.assertRaises(z.ResponsePrecisionError):
                z.advance_clock(c, dt)
        with self.assertRaises(z.ResponsePrecisionError):
            z.advance_clock(z.Clock(t=sys.float_info.max), sys.float_info.max)
        with self.assertRaises(z.ResponsePrecisionError):
            z.clock_angle(z.Clock(q=1, N=10**400))
        self.assertEqual(c.t, 1e300)


class StagedTests(unittest.TestCase):
    def test_literal_defaults(self):
        cfg = z.StagedConfig()
        self.assertEqual((cfg.lambda_vp, cfg.gamma, cfg.theta_lock, cfg.alpha, cfg.beta),
                         (.618, .577, .244, 1., .5))
        self.assertNotEqual(cfg.lambda_vp, (math.sqrt(5)-1)/2)
        self.assertFalse(hasattr(z.EMAConfig(), 'gamma'))

    def test_hand_state_and_direct_chirality_delegation(self):
        omega = np.array([1+4j, 2+5j, 3+6j])
        original = omega.copy()
        c = z.Clock(t=1)
        with patch.object(readouts, 'z_chiral', wraps=readouts.z_chiral) as called:
            out = z.observe_staged(omega, c, z.StagedConfig())
            called.assert_called_once()
        expected = .618*math.sqrt(91)/(1+math.sqrt(91))*math.cos(.732)*math.exp(-.577)
        self.assertAlmostEqual(out.z, expected, places=15)
        np.testing.assert_array_equal(out.Z_chiral, [-3, 6, -3])
        np.testing.assert_array_equal(out.Z_chiral, readouts.z_chiral(omega))
        np.testing.assert_allclose(out.Z_macro, [expected, 0, expected], rtol=2e-15, atol=0)
        np.testing.assert_allclose(out.Z_total, [expected-1.5, 3, expected-1.5],
                                   rtol=2e-15, atol=0)
        np.testing.assert_array_equal(omega, original)

    def test_signed_coefficients_gamma_zero_and_envelope(self):
        w = [1+4j, 2+5j, 3+6j]
        c = z.Clock(q=3, N=10, t=2.)
        cfg = z.StagedConfig(lambda_vp=-2., gamma=0., theta_lock=-.25, alpha=-3., beta=-2.)
        theta = 3*math.pi/5
        scalar = -2*math.sqrt(91)/(1+math.sqrt(91))*math.cos(3*(theta+.25))
        out = z.observe_staged(w, c, cfg)
        m = scalar*np.array([math.cos(theta), math.sin(theta), 1])
        np.testing.assert_allclose(out.Z_total, -3*m-2*np.array([-3, 6, -3]),
                                   rtol=3e-15, atol=3e-15)
        damped = z.observe_staged(w, c, z.StagedConfig(gamma=.5))
        plain = z.observe_staged(w, c, z.StagedConfig(gamma=0))
        self.assertAlmostEqual(damped.z/plain.z, math.exp(-1), places=15)
        np.testing.assert_array_equal(damped.Z_chiral, plain.Z_chiral)

    def test_fixed_high_precision_scalar_oracle(self):
        fixtures = [
            ([.3+.7j, -.4+.2j, .1-.8j], z.Clock(q=5, N=17, t=.7), z.StagedConfig()),
            ([2-.5j, -.3-1j, .7+.4j], z.Clock(q=-2, N=9, t=-.3),
             z.StagedConfig(lambda_vp=-.8, gamma=-.4, theta_lock=-.2)),
        ]
        with mp.workdps(70):
            for omega, c, cfg in fixtures:
                norm = mp.sqrt(sum(mp.mpf(v.real)**2+mp.mpf(v.imag)**2 for v in omega))
                theta = 2*mp.pi*(c.q % c.N)/c.N
                expected = (mp.mpf(cfg.lambda_vp)*norm/(1+norm)
                            *mp.cos(3*(theta-mp.mpf(cfg.theta_lock)))
                            *mp.exp(-mp.mpf(cfg.gamma)*mp.mpf(c.t)))
                self.assertTrue(math.isclose(z.staged_scalar(omega,c,cfg),float(expected),
                                             rel_tol=2e-14,abs_tol=2e-15))

    def test_alpha_beta_selection_and_alias(self):
        w = [1+4j, 2+5j, 3+6j]
        out = z.observe_staged(w, z.Clock(), z.StagedConfig(alpha=0, beta=2))
        np.testing.assert_array_equal(out.Z_total, [-6, 12, -6])
        self.assertIs(out.Z_vec, out.Z_total)
        with self.assertRaises((FrozenInstanceError, AttributeError, TypeError)):
            out.Z_vec = np.ones(3)

    def test_fresh_readonly_values_and_repeat_observation(self):
        omega = np.array([1+4j,2+5j,3+6j])
        c = z.Clock(q=2,t=.4)
        cfg = z.StagedConfig()
        a = z.observe_staged(omega,c,cfg)
        b = z.observe_staged(omega,c,cfg)
        for name in ('Z_macro','Z_chiral','Z_total'):
            x, y = getattr(a,name), getattr(b,name)
            np.testing.assert_array_equal(x,y)
            self.assertFalse(np.shares_memory(x,y))
            self.assertFalse(np.shares_memory(x,omega))
            with self.assertRaises(ValueError):
                x[0] = 100
        self.assertEqual(c, z.Clock(q=2,t=.4))
        with self.assertRaises(FrozenInstanceError):
            cfg.gamma = 0

    def test_explicit_config_variant_and_validation(self):
        with self.assertRaises(TypeError):
            z.observe_staged([0,0,0],z.Clock(),z.EMAConfig())
        with self.assertRaises(TypeError):
            z.observe_staged([0,0,0],z.Clock())
        for cls, fields in ((z.StagedConfig, ('lambda_vp','gamma','theta_lock','alpha','beta')),
                            (z.EMAConfig, ('lambda_vp','theta_lock','alpha','beta'))):
            for field in fields:
                for bad in (True,'1',1j,np.inf,np.nan,np.array([1.])):
                    with self.subTest(cls=cls.__name__,field=field,bad=repr(bad)):
                        with self.assertRaises((TypeError,ValueError)):
                            cls(**{field:bad})


class EMATests(unittest.TestCase):
    def test_common_phase_counterexample_and_first_update(self):
        real = [1,1,1]; imaginary = [1j,1j,1j]
        np.testing.assert_array_equal(readouts.z_chiral(real), [0,0,0])
        np.testing.assert_array_equal(readouts.z_chiral(imaginary), [0,0,0])
        self.assertEqual(z.cubic_j(real), 0)
        self.assertEqual(z.cubic_j(imaginary), 1)
        self.assertEqual(z.normalized_cubic(imaginary), .5)
        self.assertEqual(z.advance_ema(imaginary,z.EMAState()).m, .005)

    def test_mixed_signed_cubic_hand_values(self):
        # (1+4i)*(2-5i)*(3+6i) = 48+141i.
        self.assertEqual(z.cubic_j([1+4j,2+5j,3+6j]),141)
        self.assertEqual(z.cubic_j([1-4j,2-5j,3-6j]),-141)
        self.assertEqual(z.normalized_cubic([1+4j,2+5j,3+6j]),141/142)
        self.assertEqual(z.normalized_cubic([1-4j,2-5j,3-6j]),-141/142)

    def test_one_two_updates_against_exact_rationals(self):
        m0 = z.EMAState(.25)
        m1 = z.advance_ema([1j,1j,1j],m0)
        m2 = z.advance_ema([-1j,-1j,-1j],m1)
        exact1 = sp.Rational(99,100)*sp.Rational(1,4)+sp.Rational(1,100)*sp.Rational(1,2)
        exact2 = sp.Rational(99,100)*exact1-sp.Rational(1,100)*sp.Rational(1,2)
        self.assertAlmostEqual(m1.m,float(exact1),places=16)
        self.assertAlmostEqual(m2.m,float(exact2),places=16)
        self.assertEqual(m0.m,.25)

    def test_endpoint_memories_and_invalid_domain(self):
        for initial in (-1.,1.):
            m = z.advance_ema([1j,1j,1j],z.EMAState(initial))
            self.assertAlmostEqual(m.m, .99*initial+.005,places=16)
            self.assertLessEqual(abs(m.m),1)
        for bad in (-1.00001,1.00001,np.nan,np.inf,True,'0',1j,np.array([0])):
            with self.subTest(bad=repr(bad)), self.assertRaises((TypeError,ValueError)):
                z.EMAState(bad)

    def test_zero_omega_retains_memory(self):
        before = z.EMAState(.5)
        after = z.advance_ema([0,0,0],before)
        out = z.observe_ema([0,0,0],z.Clock(),z.EMAConfig(),after)
        self.assertEqual(after.m,.495)
        self.assertEqual(out.z,.495)
        np.testing.assert_array_equal(out.Z_macro,[.495,0,.495])
        np.testing.assert_array_equal(out.Z_chiral,[0,0,0])

    def test_pure_observation_does_not_consume_memory(self):
        w = [1j,1j,1j]
        memory = z.advance_ema(w,z.EMAState())
        cfg = z.EMAConfig(lambda_vp=0)
        c = z.Clock(q=3,t=.1)
        with patch.object(z,'advance_ema',side_effect=AssertionError('implicit update')):
            a = z.observe_ema(w,c,cfg,memory)
            b = z.observe_ema(w,c,cfg,memory)
        self.assertEqual(a.z,.005)
        self.assertEqual(b.z,.005)
        self.assertEqual(memory.m,.005)
        self.assertNotEqual(a.z,.00995)
        np.testing.assert_array_equal(a.Z_total,b.Z_total)

    def test_ema_has_no_clock_time_envelope_and_requires_memory(self):
        w = [1+4j,2+5j,3+6j]
        cfg = z.EMAConfig()
        a = z.observe_ema(w,z.Clock(q=2,t=0),cfg,z.EMAState(.2))
        b = z.observe_ema(w,z.Clock(q=2,t=1000),cfg,z.EMAState(.2))
        self.assertEqual(a.z,b.z)
        with self.assertRaises(TypeError):
            z.observe_ema(w,z.Clock(),z.StagedConfig(),z.EMAState())
        with self.assertRaises(TypeError):
            z.observe_ema(w,z.Clock(),cfg,0.)
        with self.assertRaises(TypeError):
            z.advance_ema(w,0.)

    def test_common_state_exact_total_cancellation(self):
        # x=(1,0,-1), y=(0,1,0) => C=(1,0,1); m=1, lambda=0 => M=C.
        w = [1,1j,-1]
        out = z.observe_ema(w,z.Clock(),z.EMAConfig(lambda_vp=0,alpha=1,beta=-1),
                            z.EMAState(1))
        np.testing.assert_array_equal(out.Z_macro,[1,0,1])
        np.testing.assert_array_equal(out.Z_chiral,[1,0,1])
        np.testing.assert_array_equal(out.Z_total,[0,0,0])
        self.assertEqual(out.z,1)
        self.assertTrue(np.any(np.asarray(w)!=0))

    def test_saturation_rounding_to_endpoints_is_allowed(self):
        self.assertEqual(z.normalized_cubic([1j*1e100,1,1e100]),1.)
        self.assertEqual(z.normalized_cubic([-1j*1e100,1,1e100]),-1.)
        self.assertEqual(z.saturated_norm([1e200,0,0]),1.)
        self.assertEqual(z.advance_ema([1j*1e100,1,1e100],z.EMAState(1)).m,1.)


class InitializationTests(unittest.TestCase):
    def test_constructor_zero_is_not_recomputed(self):
        w = np.array([1+4j,2+5j,3+6j])
        cfg = z.EMAConfig()
        with patch.object(z,'advance_ema',side_effect=AssertionError('update at construction')):
            record = z.historical_constructor_zero(w,z.Clock(),cfg)
        self.assertEqual(record.memory.m,0)
        self.assertEqual(record.readout.initialization,'historical_constructor_zero')
        self.assertEqual(record.readout.variant,'ema')
        for name in ('Z_macro','Z_chiral','Z_total'):
            np.testing.assert_array_equal(getattr(record.readout,name),[0,0,0])
        recomputed = z.observe_ema(w,record.clock,cfg,record.memory)
        np.testing.assert_array_equal(recomputed.Z_chiral,[-3,6,-3])
        self.assertEqual(recomputed.initialization,'recomputed')
        self.assertFalse(np.shares_memory(record.omega,w))
        with self.assertRaises(ValueError):
            record.omega[0] = 0

    def test_constructor_validates_metadata_and_omega(self):
        for cfg in (None,'staged',0):
            with self.assertRaises(TypeError):
                z.historical_constructor_zero([0,0,0],z.Clock(),cfg)
        with self.assertRaises(TypeError):
            z.historical_constructor_zero([0,0,0],0,z.StagedConfig())
        for w in ([True,0,0],[np.inf,0,0],[1,2]):
            with self.assertRaises((TypeError,ValueError)):
                z.historical_constructor_zero(w,z.Clock(),z.StagedConfig())
        row = z.historical_constructor_zero([1,1,1],z.Clock(),z.StagedConfig())
        self.assertEqual(row.readout.variant,'staged')
        self.assertEqual(row.readout.z,0)

    def test_pre_step_recording_and_final_state_index(self):
        cfg = z.EMAConfig(lambda_vp=0)
        dyn = DynamicsConfig(eps=0,g=0,phase_strength=0,k=(1,1,1))
        row = z.historical_constructor_zero([1j,1j,1j],z.Clock(),cfg)
        omega, clock, memory, out = row.omega,row.clock,row.memory,row.readout
        rows = []
        for _ in range(3):
            rows.append((clock.q,clock.t,memory.m,out.z))
            omega = step3(omega,dyn)
            clock = z.advance_clock(clock,.1)
            memory = z.advance_ema(omega,memory)
            out = z.observe_ema(omega,clock,cfg,memory)
        self.assertEqual([r[0] for r in rows],[0,1,2])
        self.assertEqual([r[3] for r in rows],[0,.005,.00995])
        self.assertEqual(clock.q,3)
        self.assertAlmostEqual(out.z,.0148505,places=16)
        self.assertNotEqual(out.z,rows[-1][3])
        np.testing.assert_array_equal(omega,[1j,1j,1j])


class PrecisionTests(unittest.TestCase):
    def test_stable_small_large_norm_and_raw_scale(self):
        for scale in (1e-200,1e200):
            self.assertEqual(z.state_norm([scale,0,0]),scale)
            self.assertGreater(z.staged_scalar([scale,0,0],z.Clock(),z.StagedConfig()),0)
        # The supplied decimal floats are rounded; use their actual values.
        with mp.workdps(70):
            expected = float(mp.sqrt(mp.mpf(3e200)**2+mp.mpf(4e200)**2))
        self.assertEqual(z.state_norm([3e200,4e200,0]),expected)
        with self.assertRaises(z.ResponsePrecisionError):
            z.state_norm([complex(sys.float_info.max,sys.float_info.max)]*3)
        with self.assertRaises(z.ResponsePrecisionError):
            z.state_norm([1e-320,0,0])

    def test_invalid_state_shapes_components_and_zero_shortcut(self):
        for bad in ([1,2],[[1,2,3]], [True,0,0],['1',0,0],[np.inf,0,0],[np.nan,0,0]):
            for fn in (z.state_norm,z.cubic_j,z.normalized_cubic):
                with self.subTest(fn=fn.__name__,bad=repr(bad)):
                    with self.assertRaises((TypeError,ValueError)):
                        fn(bad)
            with self.assertRaises((TypeError,ValueError)):
                z.observe_staged(bad,z.Clock(),z.StagedConfig(lambda_vp=0,alpha=0,beta=0))
        with self.assertRaises((TypeError,ValueError)):
            z.macro_vector(True,z.Clock())
        with self.assertRaises(ValueError):
            z.blend_vectors([0,0],[0,0,0],alpha=0,beta=0)

    def test_exponential_and_scalar_failures(self):
        for t in (1000.,710.,-1000.):
            with self.subTest(t=t), self.assertRaises(z.ResponsePrecisionError):
                z.staged_scalar([1,0,0],z.Clock(t=t),z.StagedConfig(gamma=1))
        with self.assertRaises(z.ResponsePrecisionError):
            z.staged_scalar([1,0,0],z.Clock(t=1e308),z.StagedConfig(gamma=1e308))
        with self.assertRaises(z.ResponsePrecisionError):
            z.staged_scalar([1,0,0],z.Clock(t=-3),z.StagedConfig(lambda_vp=1e308,gamma=1))
        with self.assertRaises(z.ResponsePrecisionError):
            z.staged_scalar([1e-20,0,0],z.Clock(),z.StagedConfig(lambda_vp=1e-300))
        with self.assertRaises(z.ResponsePrecisionError):
            z.staged_scalar([0,0,0],z.Clock(t=1000),z.StagedConfig(gamma=1))

    def test_cubic_stage_limits(self):
        for omega in ([1e-110,1e-110,1j*1e-110],[1e200,1e200,1j],
                      [.1,1e-310,0]):
            with self.subTest(omega=omega), self.assertRaises(z.ResponsePrecisionError):
                z.cubic_j(omega)
        # No cubic is evaluated by the pure current-memory readout.
        out = z.observe_ema([1e110,1e110,1e110],z.Clock(),z.EMAConfig(),z.EMAState())
        self.assertTrue(math.isfinite(out.z))
        with self.assertRaises(z.ResponsePrecisionError):
            z.advance_ema([1e110,1e110,1e110],z.EMAState())

    def test_complete_decomposition_keeps_chirality_failures_at_beta_zero(self):
        for w in ([1e-200,1j*1e-200,0],[1e200,1j*1e200,0]):
            self.assertTrue(math.isfinite(z.staged_scalar(w,z.Clock(),z.StagedConfig(beta=0))))
            with self.assertRaises(z.ResponsePrecisionError):
                z.observe_staged(w,z.Clock(),z.StagedConfig(beta=0))
        with patch.object(readouts,'z_chiral',side_effect=z.ResponsePrecisionError('delegated')):
            with self.assertRaises(z.ResponsePrecisionError):
                z.observe_ema([1,1,1],z.Clock(),z.EMAConfig(beta=0),z.EMAState())

    def test_blend_failures_and_failure_atomicity(self):
        c = z.Clock(t=1)
        cfg = z.StagedConfig()
        memory = z.EMAState(.5)
        w = np.array([1e200,1e200,1j])
        saved = w.copy()
        with self.assertRaises(z.ResponsePrecisionError):
            z.advance_ema(w,memory)
        np.testing.assert_array_equal(w,saved)
        self.assertEqual(memory.m,.5)
        self.assertEqual(c.t,1.)
        self.assertEqual(cfg.gamma,.577)
        for m,cvec,a,b in (([2,0,0],[0,0,0],1e308,0),
                          ([2,0,0],[2,0,0],1e308,-1e308),
                          ([1e-200,0,0],[0,0,0],1e-200,0)):
            with self.assertRaises(z.ResponsePrecisionError):
                z.blend_vectors(m,cvec,alpha=a,beta=b)


class MathematicalTests(unittest.TestCase):
    def test_exact_macro_cone_and_norm(self):
        scalar,theta = sp.symbols('z theta',real=True)
        m = sp.Matrix([scalar*sp.cos(theta),scalar*sp.sin(theta),scalar])
        self.assertEqual(sp.trigsimp(m[0]**2+m[1]**2-m[2]**2),0)
        self.assertEqual(sp.trigsimp(m.dot(m)-2*scalar**2),0)
        for c in (z.Clock(q=1,N=7),z.Clock(q=5,N=13)):
            v = z.macro_vector(-.75,c)
            self.assertLessEqual(abs(v[0]**2+v[1]**2-v[2]**2),8*np.finfo(float).eps*.75**2)

    def test_exact_frozen_extrema_and_sample_distinction(self):
        a,t,lock = sp.symbols('A t ell',real=True)
        f = a*sp.cos(3*(t-lock))
        self.assertEqual(sp.diff(f,t),-3*a*sp.sin(3*(t-lock)))
        for k in range(6):
            point = lock+sp.pi*k/3
            self.assertEqual(sp.simplify(sp.diff(f,t).subs(t,point)),0)
            self.assertEqual(sp.simplify(f.subs(t,point)),a*(-1)**k)
            self.assertEqual(sp.simplify(sp.diff(f,t,2).subs(t,point)),-9*a*(-1)**k)
        self.assertEqual(f.subs(a,0),0)
        default_samples = [math.cos(3*(math.pi*q/6-.244)) for q in range(12)]
        self.assertLess(max(abs(v) for v in default_samples),.75)
        for q in range(0,12,2):
            self.assertEqual(sp.cos(3*(sp.pi*q/6)),(-1)**(q//2))

    def test_exact_cross_product_order(self):
        x = sp.symbols('x1:4',real=True); y = sp.symbols('y1:4',real=True)
        omega = [a+sp.I*b for a,b in zip(x,y)]
        pairs = sp.Matrix([sp.expand(sp.im(sp.conjugate(omega[j])*omega[k]))
                           for j,k in ((1,2),(2,0),(0,1))])
        self.assertEqual(pairs,sp.Matrix(x).cross(sp.Matrix(y)))

    def test_exact_ema_unrolling_weights_and_persistent_input(self):
        a = sp.Rational(99,100)
        m0,j1,j2,j3 = sp.symbols('m0 j1 j2 j3',real=True)
        value = m0
        for current in (j1,j2,j3):
            value = a*value+(1-a)*current
        self.assertEqual(sp.expand(value-(a**3*m0+(1-a)*(a**2*j1+a*j2+j3))),0)
        n = sp.symbols('n',integer=True,positive=True)
        self.assertEqual(sp.simplify(a**n+(1-a)*(1-a**n)/(1-a)),1)
        self.assertTrue(a>0 and (1-a)>0)
        exact = sp.Rational(1,2)*(1-a**3)
        current = z.EMAState()
        for _ in range(3):
            current = z.advance_ema([1j,1j,1j],current)
        self.assertAlmostEqual(current.m,float(exact),places=16)
        self.assertGreater(current.m,0)


class BoundaryTests(unittest.TestCase):
    def test_observers_leave_same_recurrence_trajectory_exactly_unchanged(self):
        initial = np.array([.2+.3j,-.4+.1j,.1-.2j])
        for strength in (0.,.001):
            dyn = DynamicsConfig(.05,.2,strength,(1.,1.2,1.4))
            baseline=[initial.copy()]
            for _ in range(5):
                baseline.append(step3(baseline[-1],dyn))
            for variant, dt in (('staged',.1),('staged',.7),('ema',.2)):
                omega=initial.copy();clock=z.Clock(N=7,q_step=2);memory=z.EMAState(-.4)
                for i in range(5):
                    omega=step3(omega,dyn)
                    clock=z.advance_clock(clock,dt)
                    if variant=='ema':
                        memory=z.advance_ema(omega,memory)
                        z.observe_ema(omega,clock,z.EMAConfig(alpha=-2,beta=3),memory)
                    else:
                        z.observe_staged(omega,clock,z.StagedConfig(gamma=-.2,alpha=2,beta=-1))
                    np.testing.assert_array_equal(omega,baseline[i+1])

    def test_clean_process_import_boundary(self):
        root=Path(__file__).resolve().parents[2]
        code = (
            "import sys,json; import kernel_physics; "
            "assert 'kernel_physics.z_manifold' not in sys.modules; "
            "import kernel_physics.z_manifold as z; "
            "print(json.dumps({'loaded':list(sys.modules),'path':z.__file__}))"
        )
        proc=subprocess.run([sys.executable,'-B','-c',code],cwd=root,
                            capture_output=True,text=True,check=True)
        data=json.loads(proc.stdout)
        self.assertTrue(Path(data['path']).resolve().is_relative_to(root/'kernel_physics'))
        for name in ('kernel_physics.dynamics','kernel_physics.geometry',
                     'kernel_physics.reference_scaffold','kernel_physics.face_state'):
            self.assertNotIn(name,data['loaded'])
        self.assertFalse(any(name.startswith(('kernel_TO','torment','openai','anthropic'))
                             for name in data['loaded']))


if __name__ == '__main__':
    unittest.main()
