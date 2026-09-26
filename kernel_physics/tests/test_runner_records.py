"""P12 scheduling, restart and record wire contract checks."""
from dataclasses import replace
import json
import unittest
from unittest.mock import patch

import numpy as np

from kernel_physics import api as a, dynamics, z_manifold, z_diagnostics
from kernel_physics import _records as codec, _runner
from kernel_physics.tests.test_public_contract import parameters, provenance, state


def run_record(*, updates=2, initial=None, observers=(), readouts=(), diagnostics=(), topology="triad", initial_provenance=None):
    return a.run(state() if initial is None else initial, parameters(), topology=topology, updates=updates,
                 parameter_provenance=provenance(), initialization_provenance=provenance() if initial_provenance is None else initial_provenance,
                 observers=observers, readouts=readouts, diagnostics=diagnostics)


def observers():
    return (a.historical_observer("paper_e_staged_v1"), a.historical_observer("paper_e_ema_v1"))


def unpack(record):
    return json.loads(record.to_json())


class RunnerRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = run_record(observers=observers(), readouts=("z_chiral",), diagnostics=codec._DIAGNOSTICS)

    def test_zero_updates_has_one_row_and_no_advancement(self):
        with patch.object(dynamics, "step3", side_effect=AssertionError), patch.object(z_manifold, "advance_clock", side_effect=AssertionError), patch.object(z_manifold, "advance_ema", side_effect=AssertionError):
            record = run_record(updates=0, observers=observers(), readouts=("z_chiral",), diagnostics=codec._DIAGNOSTICS)
        data = unpack(record)
        self.assertEqual(len(data["samples"]), 1)
        self.assertEqual(data["samples"][0]["omega"], codec._encode(state().omega))
        for snapshot in data["samples"][0]["observer_states"].values():
            self.assertEqual(snapshot["observer_update_count"], "0")
            self.assertEqual(snapshot["q"], "0")
        for result in data["samples"][0]["observer_results"].values():
            self.assertEqual(result["initialization"], "recomputed")

    def test_constructor_zero_calls_owner_and_keeps_raw_chirality(self):
        requests = tuple(replace(o, initialization="historical_constructor_zero") for o in observers())
        with patch.object(z_manifold, "historical_constructor_zero", wraps=z_manifold.historical_constructor_zero) as zero, patch.object(z_manifold, "observe_staged", side_effect=AssertionError), patch.object(z_manifold, "observe_ema", side_effect=AssertionError):
            record = run_record(updates=0, observers=requests, readouts=("z_chiral",))
        self.assertEqual(zero.call_count, 2)
        sample = unpack(record)["samples"][0]
        self.assertNotEqual(sample["raw_readouts"]["z_chiral"], codec._encode([0., 0., 0.]))
        for result in sample["observer_results"].values():
            self.assertEqual(result["Z_chiral"], codec._encode([0., 0., 0.]))
            self.assertEqual(result["initialization"], "historical_constructor_zero")

    def test_constructor_zero_requires_index_zero(self):
        request = replace(observers()[0], initialization="historical_constructor_zero")
        with patch.object(dynamics, "step3") as step, self.assertRaises(ValueError):
            run_record(initial=replace(state(), update_index=1), observers=(request,))
        step.assert_not_called()

    def test_exact_schedule_new_omega_then_clock_then_ema_then_observe(self):
        request = observers()[1]
        events = []
        original = {name: getattr(z_manifold, name) for name in ("advance_clock", "advance_ema", "observe_ema")}
        native_step = dynamics.step3
        new_states = []

        def step(*args):
            events.append("step")
            result = native_step(*args)
            new_states.append(tuple(result))
            return result

        def clock(*args):
            events.append("clock")
            return original["advance_clock"](*args)

        def memory(omega, m):
            events.append("ema")
            self.assertEqual(tuple(omega), new_states[-1])
            return original["advance_ema"](omega, m)

        def observe(*args):
            events.append("observe")
            return original["observe_ema"](*args)

        with patch.object(dynamics, "step3", side_effect=step), patch.object(z_manifold, "advance_clock", side_effect=clock), patch.object(z_manifold, "advance_ema", side_effect=memory), patch.object(z_manifold, "observe_ema", side_effect=observe):
            run_record(observers=(request,), updates=2)
        self.assertEqual(events, ["observe", "step", "clock", "ema", "observe", "step", "clock", "ema", "observe"])

    def test_multiple_observers_have_independent_memory_and_clocks(self):
        first = replace(observers()[1], observer_id="first", clock=a.Clock(q=-8, N=7, t=.2, q_step=-2), dt=0)
        second = replace(observers()[1], observer_id="second", memory=a.EMAState(m=.3),
                         clock=a.Clock(q=4, N=9, t=-.3, q_step=3), dt=-.05)
        with patch.object(dynamics, "step3", wraps=dynamics.step3) as step, patch.object(z_manifold, "advance_ema", wraps=z_manifold.advance_ema) as ema:
            both = unpack(run_record(updates=3, observers=(first, second)))
        self.assertEqual((step.call_count, ema.call_count), (3, 6))
        self.assertEqual(both["selection"]["observer_ids"], ["first", "second"])
        for request in (first, second):
            solo = unpack(run_record(updates=3, observers=(request,)))
            for together, alone in zip(both["samples"], solo["samples"]):
                self.assertEqual(together["observer_states"][request.observer_id], alone["observer_states"][request.observer_id])
                self.assertEqual(together["observer_results"][request.observer_id], alone["observer_results"][request.observer_id])
        self.assertEqual(both["samples"][-1]["observer_states"]["first"]["t"], codec._encode(.2))

    def test_multiple_observers_advance_and_observe_in_request_order(self):
        requests = (replace(observers()[1], observer_id="one"), replace(observers()[1], observer_id="two"))
        events = []
        originals = {name: getattr(z_manifold, name) for name in ("advance_clock", "advance_ema", "observe_ema")}

        def wrapper(name):
            def call(*args):
                events.append(name)
                return originals[name](*args)
            return call

        with patch.object(z_manifold, "advance_clock", side_effect=wrapper("advance_clock")), patch.object(z_manifold, "advance_ema", side_effect=wrapper("advance_ema")), patch.object(z_manifold, "observe_ema", side_effect=wrapper("observe_ema")):
            run_record(updates=2, observers=requests)
        self.assertEqual(events, ["observe_ema"]*2 + ["advance_clock", "advance_ema", "observe_ema"]*4)

    def test_clock_t_uses_delegated_repeated_addition(self):
        record = unpack(run_record(updates=10, observers=(observers()[0],)))
        clock = observers()[0].clock
        for sample in record["samples"]:
            self.assertEqual(sample["observer_states"][observers()[0].observer_id]["t"], codec._encode(clock.t))
            clock = a.advance_clock(clock, .1)
        self.assertNotEqual(record["samples"][-1]["observer_states"][observers()[0].observer_id]["t"], codec._encode(1.0))

    def test_observer_and_diagnostic_selection_cannot_change_trajectory(self):
        plain = unpack(run_record())
        observed = unpack(self.record)
        self.assertEqual([s["omega"] for s in plain["samples"]], [s["omega"] for s in observed["samples"]])
        self.assertTrue(all(not s["raw_readouts"] and not s["observer_results"] and not s["diagnostics"] for s in plain["samples"]))

    def test_intensity_budget_is_from_each_stored_state(self):
        for sample in unpack(self.record)["samples"]:
            omega = [codec._complex(v) for v in sample["omega"]]
            expected = z_diagnostics.intensity_budget(omega, parameters()._native())
            self.assertEqual(sample["diagnostics"]["intensity_budget"], codec._encode(expected))

    def test_abort_on_numeric_failure_preserves_inputs(self):
        initial, request = state(), observers()[1]
        with patch.object(z_manifold, "advance_ema", side_effect=a.ResponsePrecisionError("intentional domain failure")), patch.object(_runner, "RunRecord", wraps=a.RunRecord) as record:
            with self.assertRaises(a.ResponsePrecisionError):
                run_record(initial=initial, observers=(request,))
        record.assert_not_called()
        self.assertEqual(initial, state())
        self.assertEqual(request.memory.m, 0)
        self.assertEqual(request.clock.q, 0)

    def test_real_precision_failure_aborts_requested_readout_only(self):
        tiny = a.State(omega=(1e-200, 1e-200j, 0), update_index=0)
        self.assertEqual(len(run_record(initial=tiny, updates=0).data["samples"]), 1)
        with self.assertRaises(a.ResponsePrecisionError):
            run_record(initial=tiny, updates=0, readouts=("z_chiral",))

    def test_bad_requests_are_rejected_before_execution(self):
        cases = [dict(updates=True), dict(updates=-1), dict(readouts=["z_chiral"]), dict(readouts=("unknown",)),
                 dict(readouts=("z_chiral", "z_chiral")), dict(diagnostics=("unknown",)),
                 dict(diagnostics=("readout_accounting",)), dict(observers=[observers()[0]]),
                 dict(observers=(observers()[0], observers()[0])), dict(observers=(object(),)),
                 dict(topology="ring", readouts=("z_chiral",)), dict(topology="ring", observers=observers()),
                 dict(topology="ring", diagnostics=("potential",))]
        with patch.object(dynamics, "step3") as step, patch.object(z_manifold, "observe_staged") as observe:
            for case in cases:
                with self.subTest(case=case), self.assertRaises((ValueError, TypeError)):
                    run_record(**case)
        step.assert_not_called()
        observe.assert_not_called()

    def test_ring_record_and_large_counters(self):
        index = 2**90
        record = run_record(initial=a.State(omega=state().omega*2, update_index=index), topology="ring")
        data = unpack(a.RunRecord.from_json(record.to_json()))
        self.assertEqual(data["state_size"], "6")
        self.assertEqual(data["samples"][-1]["update_index"], str(index + 2))
        self.assertIn("A06", data["definition_ids"])
        self.assertNotIn("A05", data["definition_ids"])

    def test_nonzero_checkpoint_and_large_initial_q(self):
        request = replace(observers()[0], clock=a.Clock(q=2**90, N=13, t=0, q_step=-1))
        p = replace(provenance(), kind="checkpoint", source_id="checkpoint-input")
        data = unpack(run_record(initial=replace(state(), update_index=2**80), initial_provenance=p, observers=(request,), updates=1))
        self.assertEqual(data["initialization"]["kind"], "checkpoint")
        self.assertEqual(data["observers"][0]["q"], str(2**90))
        self.assertEqual(data["samples"][-1]["observer_states"][request.observer_id]["q"], str((2**90-1) % 13))

    def test_historical_seed_provenance_requires_literal_match(self):
        seed = a.historical_seed("gate_torus_seed_v1")
        data = unpack(run_record(initial_provenance=seed.provenance, updates=0))
        self.assertEqual(data["initialization"]["preset_id"], seed.name)
        self.assertIn("L02", data["definition_ids"])
        with self.assertRaises(ValueError):
            run_record(initial=a.State(omega=[0, 0, 0], update_index=0), initial_provenance=seed.provenance)

    def test_resume_preserves_full_prefix_and_matches_continuous_run(self):
        resumed = unpack(a.resume(self.record, updates=3))
        full = unpack(run_record(updates=5, observers=observers(), readouts=("z_chiral",), diagnostics=codec._DIAGNOSTICS))
        parent = unpack(self.record)
        self.assertEqual(resumed["samples"][:3], parent["samples"])
        self.assertEqual(resumed["samples"], full["samples"])
        self.assertEqual(resumed["continuation"], {"parent_digest": self.record.deterministic_sha256, "junction_index": "2"})
        for field in ("parameters", "selection", "observers", "initialization"):
            self.assertEqual(resumed[field], parent[field])

    def test_resume_does_not_reobserve_or_readvance_junction(self):
        requests = tuple(replace(o, initialization="historical_constructor_zero") for o in observers())
        parent = run_record(updates=0, observers=requests)
        with patch.object(z_manifold, "historical_constructor_zero", side_effect=AssertionError), patch.object(z_manifold, "advance_ema", wraps=z_manifold.advance_ema) as ema, patch.object(z_manifold, "observe_ema", wraps=z_manifold.observe_ema) as observe:
            resumed = a.resume(parent, updates=2)
        self.assertEqual((ema.call_count, observe.call_count), (2, 2))
        self.assertEqual(unpack(resumed)["samples"][0], unpack(parent)["samples"][0])

    def test_zero_resume_preserves_samples_and_adds_segment(self):
        with patch.object(dynamics, "step3", side_effect=AssertionError), patch.object(z_manifold, "observe_staged", side_effect=AssertionError):
            resumed = unpack(a.resume(self.record, updates=0))
        self.assertEqual(resumed["samples"], unpack(self.record)["samples"])
        self.assertEqual(len(resumed["execution_metadata"]), 2)

    def test_continuation_junction_must_match_the_last_execution_segment(self):
        resumed = unpack(a.resume(self.record, updates=1))
        resumed["continuation"]["junction_index"] = "1"
        with self.assertRaisesRegex(ValueError, "last execution junction"):
            a.RunRecord(codec._signed(resumed))
        resumed["continuation"] = None
        with self.assertRaisesRegex(ValueError, "exactly one execution segment"):
            a.RunRecord(codec._signed(resumed))

    def test_resume_requires_source_and_hash_match(self):
        for field in ("commit", "modules"):
            data = unpack(self.record)
            if field == "commit":
                data["implementation"][field] = "a"*40
            else:
                data["implementation"][field][0]["sha256"] = "a"*64
            record = a.RunRecord(codec._signed(data))
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "matching source revision"):
                a.resume(record, updates=1)

    def test_resume_allows_environment_change_and_reports_segments(self):
        data = unpack(self.record)
        data["execution_metadata"][0]["numpy"] = "different-producer"
        modified = a.RunRecord(data)
        resumed = unpack(a.resume(modified, updates=1))
        self.assertEqual(resumed["execution_metadata"][0]["numpy"], "different-producer")
        self.assertEqual(resumed["execution_metadata"][1]["numpy"], np.__version__)
        self.assertEqual(resumed["samples"][:3], data["samples"])

    def test_record_and_resume_have_no_mutation_or_parameter_override(self):
        with self.assertRaises(AttributeError):
            self.record._json = "{}"
        with self.assertRaises(AttributeError):
            del self.record._json
        with self.assertRaises(TypeError):
            self.record.data["parameters"]["eps"]["f64"] = "0x0.0p+0"
        with self.assertRaises(TypeError):
            a.resume(self.record, updates=1, parameters=parameters())
        with self.assertRaises(TypeError):
            a.resume(self.record, updates=1, observers=observers())

    def test_exact_roundtrip_without_any_scientific_evaluation(self):
        text = self.record.to_json()
        with patch.object(dynamics, "step3", side_effect=AssertionError), patch.object(z_manifold, "observe_staged", side_effect=AssertionError), patch.object(z_manifold, "observe_ema", side_effect=AssertionError), patch.object(z_diagnostics, "potential", side_effect=AssertionError):
            decoded = a.RunRecord.from_json(text)
            self.assertEqual(decoded.to_json(), text)
            self.assertEqual(decoded.deterministic_sha256, self.record.deterministic_sha256)

    def test_signed_zero_roundtrip_for_real_and_complex_values(self):
        initial = a.State(omega=(complex(-0., 0.), complex(0., -0.), complex(-0., -0.)), update_index=0)
        p = replace(parameters(), eps=-0., phase_strength=-0., k=(-0., 0., 1.))
        record = a.run(initial, p, topology="triad", updates=0, parameter_provenance=provenance(), initialization_provenance=provenance(), observers=(), readouts=(), diagnostics=())
        data = unpack(a.RunRecord.from_json(record.to_json()))
        self.assertEqual(data["samples"][0]["omega"], codec._encode(initial.omega))
        self.assertEqual(data["parameters"]["eps"], {"f64": "-0x0.0p+0"})
        self.assertEqual(codec._complex(data["samples"][0]["omega"][2]).imag.hex(), "-0x0.0p+0")

    def test_deterministic_digest_excludes_environment_only(self):
        first = run_record(updates=0)
        second = run_record(updates=0)
        self.assertEqual(first.deterministic_sha256, second.deterministic_sha256)
        data = unpack(first)
        data["execution_metadata"][0]["platform"] = "another platform"
        self.assertEqual(a.RunRecord(data).deterministic_sha256, first.deterministic_sha256)
        data["parameter_provenance"]["notes"] = "changed deterministic content"
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            a.RunRecord(data)
        self.assertNotEqual(a.RunRecord(codec._signed(data)).deterministic_sha256, first.deterministic_sha256)

    def test_unknown_fields_versions_and_ids_are_rejected_even_with_valid_digest(self):
        mutations = [lambda d: d.update(geometry={}), lambda d: d.update(schema_version="1.1.0"),
                     lambda d: d.update(api_version="2.0.0"), lambda d: d.update(ledger_version="9"),
                     lambda d: d["parameters"].update(dt=codec._encode(.1)),
                     lambda d: d["selection"]["readouts"].append("srg"),
                     lambda d: d["definition_ids"].append("Z99"),
                     lambda d: d["observers"][0]["config"].update(other=codec._encode(1.)),
                     lambda d: d["samples"][0]["observer_results"][observers()[0].observer_id].update(Z_vec=[]),
                     lambda d: d["execution_metadata"][0].update(unknown="field")]
        for mutate in mutations:
            data = unpack(self.record)
            mutate(data)
            with self.subTest(mutation=mutate), self.assertRaises((TypeError, ValueError)):
                a.RunRecord(codec._signed(data))

    def test_structural_inconsistencies_and_numeric_codec_are_rejected(self):
        oid = observers()[1].observer_id
        mutations = [lambda d: d["samples"][0]["omega"].pop(),
                     lambda d: d["samples"][1].update(update_index="9"),
                     lambda d: d["samples"][0]["omega"][0].update(re=codec._encode(99.)),
                     lambda d: d["samples"][0]["observer_states"][oid].update(observer_update_count="1"),
                     lambda d: d["samples"][1]["observer_states"][oid].update(m=codec._encode(2.)),
                     lambda d: d["samples"][1]["observer_states"][oid].update(t={"f64": "nan"}),
                     lambda d: d["samples"][1]["observer_states"][oid].update(q=True),
                     lambda d: d["samples"][1]["observer_states"][oid].update(q="01"),
                     lambda d: d["samples"][1]["observer_states"][oid].update(q="-0"),
                     lambda d: d["parameters"].update(eps={"f64": ".05"}),
                     lambda d: d["samples"][0]["diagnostics"]["intensity_budget"]["increment"].pop(),
                     lambda d: d["samples"][0]["diagnostics"]["historical_alignment"][oid].update(TM_resolved="false"),
                     lambda d: d["selection"]["observer_ids"].reverse(),
                     lambda d: d.update(samples=[]), lambda d: d.update(state_size="4")]
        for mutate in mutations:
            data = unpack(self.record)
            mutate(data)
            with self.subTest(mutation=mutate), self.assertRaises((ValueError, TypeError)):
                a.RunRecord(codec._signed(data))

    def test_diagnostic_numbers_are_not_recomputed_or_repaired_on_load(self):
        data = unpack(self.record)
        data["samples"][1]["diagnostics"]["potential"] = codec._encode(12345.)
        with patch.object(z_diagnostics, "potential", side_effect=AssertionError):
            record = a.RunRecord.from_json(codec._canonical(codec._signed(data)))
        self.assertEqual(record.data["samples"][1]["diagnostics"]["potential"]["f64"], float(12345).hex())

    def test_duplicate_keys_and_nonfinite_json_are_rejected(self):
        for text in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}', '{"x":-Infinity}', '{"x":{"y":0,"y":1}}'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                a.RunRecord.from_json(text)

    def test_definition_and_source_metadata_cover_selected_operations(self):
        data = unpack(self.record)
        self.assertEqual(data["definition_ids"], sorted(set(data["definition_ids"])))
        self.assertTrue({"A05", "B01", "E01", "E02", "E03", "E04", "E06", "E07", "E08", "E09", "E10", "L03", "L04", "L06", "S03"} <= set(data["definition_ids"]))
        self.assertEqual([p["source_id"] for p in data["paper_references"]], ["PA", "PB", "PE"])
        self.assertEqual(len(data["implementation"]["commit"]), 40)
        self.assertEqual([m["path"] for m in data["implementation"]["modules"]], list(codec._MODULES))
