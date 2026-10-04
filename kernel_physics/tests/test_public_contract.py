"""P12 value ownership and thin delegation; not the P1-P11 parity program."""
from dataclasses import FrozenInstanceError, fields, replace
import inspect
import unittest
from unittest.mock import patch

import numpy as np

from kernel_physics import api as a, dynamics, z_manifold, z_diagnostics
from kernel_physics._response_numeric import ResponsePrecisionError


def provenance():
    return a.Provenance(kind="user_supplied", source_id="P12", source_revision=None,
                        locator="test", literal_values={}, notes="Explicit contract test input.")


def parameters():
    return a.Parameters(eps=.05, g=.2, phase_strength=.001, k=(1, 1.2, .8))


def state():
    return a.State(omega=(.2+.3j, -.4+.1j, .1-.2j), update_index=0)


class PublicContractTests(unittest.TestCase):
    def test_constructors_and_selection_have_no_defaults(self):
        for cls in (a.Parameters, a.State, a.Seed, a.Clock, a.StagedConfig, a.EMAConfig,
                    a.EMAState, a.ObserverRequest, a.Provenance):
            with self.subTest(cls=cls.__name__):
                for argument in inspect.signature(cls).parameters.values():
                    self.assertEqual(argument.default, inspect.Parameter.empty)
                    self.assertEqual(argument.kind, inspect.Parameter.KEYWORD_ONLY)
                with self.assertRaises(TypeError):
                    cls()
        for function in (a.run, a.resume, a.step, a.get_geometry, a.direct_history_coordinates,
                         a.cylinder_point, a.cylinder_history_coordinates, a.history_torus_coordinates):
            for argument in inspect.signature(function).parameters.values():
                self.assertEqual(argument.default, inspect.Parameter.empty)

    def test_parameter_state_arrays_are_detached_immutable_values(self):
        omega = np.array(state().omega)
        k = np.array([1., 2., 3.])
        snapshot = a.State(omega=omega, update_index=5)
        config = a.Parameters(eps=.1, g=.2, phase_strength=-.3, k=k)
        omega[:] = 99
        k[:] = 99
        self.assertEqual(snapshot.omega, state().omega)
        self.assertEqual(config.k, (1., 2., 3.))
        self.assertEqual([f.name for f in fields(a.State)], ["omega", "update_index"])
        with self.assertRaises(FrozenInstanceError):
            snapshot.update_index = 0
        with self.assertRaises(TypeError):
            snapshot.omega[0] = 0
        with self.assertRaises(FrozenInstanceError):
            config.eps = 1

    def test_provenance_detaches_literal_map(self):
        literals = {"eps": ".05"}
        p = replace(provenance(), literal_values=literals)
        literals["eps"] = "999"
        self.assertEqual(p.literal_values["eps"], ".05")
        with self.assertRaises(TypeError):
            p.literal_values["eps"] = "1"

    def test_real_inputs_reject_bool_string_complex_and_nonfinite(self):
        for value in (True, np.bool_(False), "1", 1+0j, np.nan, np.inf):
            for constructor in (lambda: replace(parameters(), eps=value),
                                lambda: a.Clock(q=0, N=12, t=value, q_step=1),
                                lambda: a.EMAState(m=value),
                                lambda: replace(a.historical_observer("paper_e_staged_v1").config, gamma=value)):
                with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                    constructor()

    def test_complex_inputs_and_shapes_are_strict(self):
        for omega in ((True, 0, 0), ("1", 0, 0), (np.inf, 0, 0), [[1, 2, 3]], [1, 2], [1]*4):
            with self.subTest(omega=omega), self.assertRaises((TypeError, ValueError)):
                a.State(omega=omega, update_index=0)
        for k in ([[1, 2, 3]], (1, 2), (1, False, 3), (1, "2", 3)):
            with self.subTest(k=k), self.assertRaises((TypeError, ValueError)):
                replace(parameters(), k=k)
        with self.assertRaises(ValueError):
            a.z_chiral([1]*6)

    def test_counters_and_memory_domains(self):
        for value in (True, np.bool_(False), 1.0, "1", -1):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                a.State(omega=state().omega, update_index=value)
        for value in (0, -1, True, 2.0):
            with self.assertRaises((TypeError, ValueError)):
                a.Clock(q=0, N=value, t=0, q_step=1)
        for value in (-1.01, 1.01):
            with self.assertRaises(ValueError):
                a.EMAState(m=value)
        self.assertEqual(a.Clock(q=-9, N=7, t=-1, q_step=-3).q, -9)

    def test_step_calls_triad_owner_once_without_mutation(self):
        original, config = state(), parameters()
        with patch.object(dynamics, "step3", wraps=dynamics.step3) as triad, patch.object(dynamics, "step_ring") as ring:
            result = a.step(original, config, topology="triad")
        triad.assert_called_once()
        ring.assert_not_called()
        self.assertEqual(result.update_index, 1)
        self.assertEqual(original, state())
        self.assertEqual(triad.call_args.args[1].phase_strength, config.phase_strength)
        self.assertEqual(triad.call_args.args[0], original.omega)

    def test_step_calls_ring_owner_once(self):
        original = a.State(omega=state().omega * 2, update_index=42)
        with patch.object(dynamics, "step_ring", wraps=dynamics.step_ring) as ring, patch.object(dynamics, "step3") as triad:
            result = a.step(original, parameters(), topology="ring")
        ring.assert_called_once()
        triad.assert_not_called()
        self.assertEqual(result.update_index, 43)
        self.assertEqual(len(result.omega), 6)

    def test_invalid_step_is_rejected_before_owner(self):
        with patch.object(dynamics, "step3") as owner:
            for topology in ("unknown", "boundary_response", None):
                with self.assertRaises((TypeError, ValueError)):
                    a.step(state(), parameters(), topology=topology)
            with self.assertRaises(ValueError):
                a.step(a.State(omega=[0]*6, update_index=0), parameters(), topology="triad")
            with self.assertRaises(TypeError):
                a.step(state(), parameters(), topology="triad", dt=.1)
        owner.assert_not_called()

    def test_named_presets_are_exact_and_detached(self):
        seed = a.historical_seed("gate_torus_seed_v1")
        self.assertEqual(seed.omega, state().omega)
        self.assertEqual(seed.provenance.kind, "historical_preset")
        for name, cls in (("paper_e_staged_v1", a.StagedConfig), ("paper_e_ema_v1", a.EMAConfig)):
            request = a.historical_observer(name)
            self.assertIsInstance(request.config, cls)
            self.assertEqual(request.observer_id, name)
            self.assertEqual(request.dt, .1)
            self.assertEqual(request.clock, a.Clock(q=0, N=12, t=0, q_step=1))
            self.assertEqual(request.initialization, "recomputed")
            self.assertEqual((request.config.lambda_vp, request.config.theta_lock), (.618, .244))
        for function in (a.historical_seed, a.historical_observer):
            with self.assertRaises(ValueError):
                function("unknown")

    def test_observer_request_variants_and_modes(self):
        staged = a.historical_observer("paper_e_staged_v1")
        ema = a.historical_observer("paper_e_ema_v1")
        for request, changes in ((staged, {"memory": a.EMAState(m=0)}), (ema, {"memory": None}),
                                 (ema, {"initialization": "historical_constructor_zero", "memory": a.EMAState(m=.1)}),
                                 (ema, {"initialization": "unknown"}), (ema, {"dt": True})):
            with self.assertRaises((TypeError, ValueError)):
                replace(request, **changes)

    def test_observation_is_repeatable_without_advancement(self):
        for name in ("paper_e_staged_v1", "paper_e_ema_v1"):
            request = a.historical_observer(name)
            with patch.object(z_manifold, "advance_clock", side_effect=AssertionError), patch.object(z_manifold, "advance_ema", side_effect=AssertionError):
                if request.variant == "staged":
                    results = [a.observe_staged(state().omega, request.clock, request.config) for _ in range(2)]
                else:
                    results = [a.observe_ema(state().omega, request.clock, request.config, request.memory) for _ in range(2)]
            np.testing.assert_array_equal(results[0].Z_total, results[1].Z_total)
            self.assertEqual(request.clock.q, 0)
            self.assertEqual(request.clock.t, 0)
            results[0].Z_total.setflags(write=True)
            results[0].Z_total[:] = 100
            self.assertFalse(np.all(results[1].Z_total == 100))

    def test_explicit_advancers_delegate_and_keep_signed_dt(self):
        request = a.historical_observer("paper_e_ema_v1")
        with patch.object(z_manifold, "advance_clock", wraps=z_manifold.advance_clock) as clock:
            result = a.advance_clock(request.clock, -.1)
        clock.assert_called_once()
        self.assertEqual((result.q, result.t), (1, -.1))
        with patch.object(z_manifold, "advance_ema", wraps=z_manifold.advance_ema) as ema:
            memory = a.advance_ema(state().omega, request.memory)
        ema.assert_called_once()
        self.assertNotEqual(memory, request.memory)

    def test_passive_facade_calls_diagnostic_owner(self):
        request = a.historical_observer("paper_e_staged_v1")
        readout = a.observe_staged(state().omega, request.clock, request.config)
        cases = [("quadratic_form", ([1, 2, 3],), {}), ("readout_accounting", (readout,), {"alpha": 1, "beta": .5}),
                 ("chiral_area_accounting", (state().omega,), {}), ("intensity_budget", (state().omega, parameters()), {}),
                 ("potential", (state().omega, parameters()), {}),
                 ("historical_alignment", (readout.Z_macro, readout.Z_chiral, readout.Z_total), {})]
        for name, args, kwargs in cases:
            with self.subTest(name=name), patch.object(z_diagnostics, name, wraps=getattr(z_diagnostics, name)) as owner:
                getattr(a, name)(*args, **kwargs)
                owner.assert_called_once()

    def test_displays_delegate_with_explicit_dimensions(self):
        history = {"kappa": [1, 2], "z": [0, .1], "phi_index": [0, 1], "Z_total": [[1, 2, 3], [4, 5, 6]]}
        for name, args, kwargs in (("direct_history_coordinates", (history,), {"key": "Z_total"}),
                                   ("cylinder_point", (1, 2, .1), {"N": 7}),
                                   ("cylinder_history_coordinates", (history,), {"N": 7}),
                                   ("history_torus_coordinates", (history,), {"R": 2, "r_max": 1, "N": 7})):
            with self.subTest(name=name), patch.object(z_diagnostics, name, wraps=getattr(z_diagnostics, name)) as owner:
                getattr(a, name)(*args, **kwargs)
                owner.assert_called_once()

    def test_precision_exception_is_the_original_type(self):
        self.assertIs(a.ResponsePrecisionError, ResponsePrecisionError)
        with self.assertRaises(ResponsePrecisionError):
            a.z_chiral([1e-200, 1e-200j, 0])

    def test_exact_public_export_set(self):
        expected = "Parameters State Seed Provenance historical_seed step z_chiral Clock StagedConfig EMAConfig EMAState advance_clock advance_ema observe_staged observe_ema historical_observer ObserverRequest ZReadout ResponsePrecisionError run resume RunRecord GeometryRecord get_geometry quadratic_form readout_accounting chiral_area_accounting intensity_budget potential historical_alignment direct_history_coordinates cylinder_point cylinder_history_coordinates history_torus_coordinates".split()
        expected += "AXIAL_OBSERVATION_API_VERSION AXIAL_OBSERVER_REVISION AxialSnapshot AxialSourceBudget axial_snapshot axial_source_budget".split()
        self.assertEqual(set(a.__all__), set(expected))
        self.assertEqual({key for key in vars(a) if not key.startswith("_")}, set(expected))
