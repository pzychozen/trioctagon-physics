"""P12 static graph plus fresh-process and forbidden-side-effect checks."""
import ast
from contextlib import ExitStack
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from kernel_physics import api as a, dynamics, z_manifold, z_diagnostics
from kernel_physics.tests.test_public_contract import parameters, state
from kernel_physics.tests.test_runner_records import run_record

_PACKAGE = Path(__file__).resolve().parents[1]
_FORBIDDEN_PUBLIC = {"boundary_response", "srg", "operating_region", "face_state"}


def graph():
    """Resolve every runtime import, including `from . import name`."""
    result, external, trees = {}, {}, {}
    modules = {path.stem for path in _PACKAGE.glob("*.py")}
    for path in _PACKAGE.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
        trees[path.stem] = tree
        result[path.stem], external[path.stem] = set(), set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [item.name for item in node.names]
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    if node.level != 1:
                        raise AssertionError(f"runtime relative import escapes package: {path}:{node.lineno}")
                    names = ["kernel_physics." + node.module] if node.module else ["kernel_physics." + item.name for item in node.names]
                elif node.module == "kernel_physics":
                    names = ["kernel_physics." + item.name for item in node.names]
                else:
                    names = [node.module or ""]
            else:
                continue
            for name in names:
                if name.startswith("kernel_physics."):
                    root = name.split(".")[1]
                    if root == "__version__":
                        root = "__init__"
                    if root not in modules:
                        raise AssertionError(f"unknown runtime dependency: {name}")
                    result[path.stem].add(root)
                else:
                    external[path.stem].add(name)
    return result, external, trees


def reachable(graph_data, source):
    seen, pending = set(), [source]
    while pending:
        node = pending.pop()
        for dependency in graph_data[node] - seen:
            seen.add(dependency)
            pending.append(dependency)
    return seen


class ImportBoundaryTests(unittest.TestCase):
    def test_all_runtime_asts_resolve_and_exclude_research_imports(self):
        imports, external, _ = graph()
        self.assertEqual(set(imports), {p.stem for p in _PACKAGE.glob("*.py")})
        for name, dependencies in external.items():
            for dependency in dependencies:
                with self.subTest(module=name, dependency=dependency):
                    self.assertNotIn(dependency.split(".")[0], {"research", "papers", "tools", "ui", "source_snapshots"})
        for module in ("api", "_runner"):
            self.assertFalse(reachable(imports, module) & _FORBIDDEN_PUBLIC)

    def test_scientific_layers_have_no_forbidden_direct_or_transitive_edges(self):
        imports, _, _ = graph()
        for module in ("dynamics", "covering"):
            self.assertFalse(reachable(imports, module) & {"geometry", "reference_scaffold", "z_manifold", "z_diagnostics", "_runner"})
        for module in ("geometry", "reference_scaffold"):
            self.assertFalse(reachable(imports, module) & {"dynamics", "z_manifold", "z_diagnostics", "_runner"})
        self.assertFalse(reachable(imports, "z_manifold") & {"dynamics", "geometry", "reference_scaffold", "_runner"})
        self.assertFalse(reachable(imports, "z_diagnostics") & {"geometry", "reference_scaffold", "_runner"})
        self.assertFalse(reachable(imports, "axial_observables") & {
            "api", "_contract_types", "_records", "_geometry_records", "_runner", "geometry",
            "reference_scaffold", "face_state", "boundary_response", "srg", "operating_region"})
        for name in ("dynamics", "_runner", "_records", "z_manifold", "geometry"):
            self.assertNotIn("axial_observables", reachable(imports, name))
        self.assertNotIn("_geometry_records", reachable(imports, "_runner"))
        # K0 explicitly permits FaceState as a mixed legacy leaf, outside API.
        self.assertTrue({"geometry", "dynamics", "operating_region"} <= reachable(imports, "face_state"))

    def test_dynamic_loading_has_no_runtime_allowlist_entries(self):
        _, external, trees = graph()
        for module, tree in trees.items():
            self.assertFalse(any(name.split(".")[0] in {"importlib", "runpy", "pkgutil"} for name in external[module]))
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr if isinstance(node.func, ast.Attribute) else ""
                    with self.subTest(module=module, line=node.lineno):
                        self.assertNotIn(name, {"__import__", "import_module", "exec_module", "load_module", "run_module", "eval", "exec"})

    def test_new_layer_contains_only_the_delegated_recurrence_call(self):
        _, _, trees = graph()
        for module in ("api", "_contract_types", "_records", "_geometry_records", "_presets", "_runner"):
            tree = trees[module]
            calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
            self.assertFalse(any(isinstance(node.func, ast.Attribute) and node.func.attr in
                                 {"phase_sync", "sin", "arctan2", "roll", "exp", "angle"} for node in calls))
        function = next(node for node in trees["_runner"].body if isinstance(node, ast.FunctionDef) and node.name == "_step")
        advances = [node for node in ast.walk(function) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "advance"]
        self.assertEqual(len(advances), 1)
        references = {node.attr for node in ast.walk(function) if isinstance(node, ast.Attribute)}
        self.assertTrue({"step3", "step_ring"} <= references)

    def test_clean_api_import_and_execution_do_not_load_option_b(self):
        code = '''
import json, sys
from kernel_physics import api as a
before = sorted(name for name in sys.modules if name.startswith('kernel_physics.'))
p = a.Provenance(kind='user_supplied',source_id='P12',source_revision=None,locator='test',literal_values={},notes='')
r = a.run(a.State(omega=(.2+.3j,-.4+.1j,.1-.2j),update_index=0),a.Parameters(eps=.05,g=.2,phase_strength=.001,k=(1,1,1)),topology='triad',updates=1,parameter_provenance=p,initialization_provenance=p,observers=(a.historical_observer('paper_e_ema_v1'),),readouts=('z_chiral',),diagnostics=('potential',))
a.get_geometry('D03',options={'construction':'regular','s':1})
print(json.dumps({'before':before,'after':sorted(name for name in sys.modules if name.startswith('kernel_physics.'))}))
'''
        output = subprocess.check_output([sys.executable, "-B", "-c", code], cwd=_PACKAGE.parent, text=True,
                                         env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        data = json.loads(output)
        for phase in ("before", "after"):
            self.assertFalse(set(data[phase]) & {"kernel_physics." + name for name in _FORBIDDEN_PUBLIC})
            self.assertIn("kernel_physics._response_numeric", data[phase])

    def test_clean_explicit_legacy_imports_remain_available(self):
        for module in sorted(_FORBIDDEN_PUBLIC):
            code = f"import kernel_physics.{module}; import sys, json; print(json.dumps(sorted(n for n in sys.modules if n.startswith('kernel_physics.'))))"
            output = subprocess.check_output([sys.executable, "-B", "-c", code], cwd=_PACKAGE.parent, text=True)
            loaded = set(json.loads(output))
            self.assertIn("kernel_physics." + module, loaded)
            self.assertNotIn("kernel_physics.api", loaded)

    def test_runner_cannot_select_optional_modules_or_geometry(self):
        for name in (*_FORBIDDEN_PUBLIC, "C01", "D03", "history_torus_coordinates"):
            for selection in ("readouts", "diagnostics"):
                with self.subTest(name=name, selection=selection), self.assertRaises(ValueError):
                    run_record(**{selection: (name,)})
        self.assertFalse(any(name in a.__all__ for name in (*_FORBIDDEN_PUBLIC, "FaceState", "chirality")))

    def test_observers_and_all_passive_readers_never_advance(self):
        request = a.historical_observer("paper_e_staged_v1")
        ema = a.historical_observer("paper_e_ema_v1")
        with ExitStack() as stack:
            for module, name in ((dynamics, "step3"), (dynamics, "step_ring"), (z_manifold, "advance_clock"), (z_manifold, "advance_ema")):
                stack.enter_context(patch.object(module, name, side_effect=AssertionError("forbidden advancement")))
            readout = a.observe_staged(state().omega, request.clock, request.config)
            a.observe_ema(state().omega, ema.clock, ema.config, ema.memory)
            a.z_chiral(state().omega)
            a.axial_snapshot(state().omega)
            a.axial_source_budget(state(), parameters())
            a.quadratic_form([1, 2, 3])
            a.readout_accounting(readout, alpha=1, beta=.5)
            a.chiral_area_accounting(state().omega)
            a.intensity_budget(state().omega, parameters())
            a.potential(state().omega, parameters())
            a.historical_alignment(readout.Z_macro, readout.Z_chiral, readout.Z_total)
            history = {"kappa": [1], "z": [.1], "phi_index": [0], "Z_total": [[1, 2, 3]]}
            a.direct_history_coordinates(history, key="Z_total")
            a.cylinder_point(1, 0, .1, N=12)
            a.cylinder_history_coordinates(history, N=12)
            a.history_torus_coordinates(history, R=2, r_max=1, N=12)
        imports, _, trees = graph()
        for name in ("z_manifold", "z_diagnostics"):
            for node in ast.walk(trees[name]):
                if isinstance(node, ast.ImportFrom) and node.module == "dynamics":
                    self.assertTrue({alias.name for alias in node.names} <= {"DynamicsConfig", "L3"})
