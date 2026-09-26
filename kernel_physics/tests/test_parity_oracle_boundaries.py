"""K2a-only assertion receipts and a small, auditable oracle import check."""

import ast
from collections import Counter
from pathlib import Path
import unittest

import mpmath as mp
import sympy as sp


# In-memory bounded aggregates, exported by the validation invocation after PASS.
EVIDENCE = {}


def gate_record(gate):
    return EVIDENCE.setdefault(gate, {"checks": Counter(), "fixtures": set(),
                                    "falsifiers": {}, "worst": None})


class ParityCase(unittest.TestCase):
    """Only common assertions/receipts; no mathematical reference implementation."""

    def exact(self, gate, fixture, actual, expected=0):
        a, b = sp.Matrix(actual), sp.Matrix(expected) if isinstance(expected, (list, tuple, sp.MatrixBase)) else None
        if b is None:
            b = sp.zeros(*a.shape) + expected * sp.ones(*a.shape)
        self.assertEqual(a.shape, b.shape, fixture)
        self.assertTrue(all(sp.simplify(x-y) == 0 for x, y in zip(a, b)), fixture)
        r = gate_record(gate)
        r["checks"]["EXACT_SYMBOLIC"] += len(a)
        r["fixtures"].add(fixture)

    def discrete(self, gate, fixture, actual, expected):
        self.assertEqual(actual, expected, fixture)
        r = gate_record(gate)
        r["checks"]["EXACT_DISCRETE"] += 1
        r["fixtures"].add(fixture)

    @mp.workdps(80)
    def bounded(self, gate, fixture, actual, expected, scales, factor,
                kind="HIGH_PRECISION_REFERENCE"):
        def scalar(v):
            if isinstance(v, (mp.mpf, mp.mpc)):
                return v
            z = complex(v)
            return mp.mpc(mp.mpf(z.real), mp.mpf(z.imag))
        r = gate_record(gate)
        for j, (a, b, scale) in enumerate(zip(actual, expected, scales, strict=True)):
            # Bound is frozen independently; no absolute floor or result-based scale.
            scale = mp.mpf(scale)
            bound = factor * mp.mpf(2)**-52 * scale
            self.assertGreaterEqual(scale, 0)
            error = abs(scalar(a)-scalar(b))
            fraction = error/bound if bound else (mp.mpf(0) if error == 0 else mp.inf)
            receipt = dict(quantity=f"component[{j}]", fixture=fixture,
                           runtime=str(a), oracle=mp.nstr(scalar(b), 35),
                           absolute_error=mp.nstr(error, 35), scale=mp.nstr(scale, 35),
                           allowed_bound=mp.nstr(bound, 35),
                           normalized_bound_fraction=mp.nstr(fraction, 35),
                           factor_u=factor, tolerance_class=kind)
            self.assertLessEqual(error, bound, f"K2A_STATUS=HOLD: {receipt}")
            if r["worst"] is None or fraction > mp.mpf(r["worst"]["normalized_bound_fraction"]):
                r["worst"] = receipt
            r["checks"][kind] += 1
            r["fixtures"].add(fixture)

    def falsifier(self, gate, name, condition):
        self.assertTrue(condition, name)
        gate_record(gate)["falsifiers"][name] = "PASS"


class OracleImportBoundaryTests(ParityCase):
    """PASS SUPPORTS: explicit independent imports and absence of simple escapes.
    PASS DOES NOT SUPPORT: a general Python sandbox or proof of oracle equations.
    """

    def test_every_oracle_has_only_explicit_allowed_imports(self):
        allowed = {"math", "cmath", "fractions", "itertools", "csv", "json",
                   "hashlib", "numpy", "sympy", "mpmath", "collections"}
        files = sorted((Path(__file__).parent / "parity_oracles").glob("*.py"))
        self.assertGreaterEqual(len(files), 2)
        for path in files:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for name in node.names:
                        self.assertIn(name.name.split(".")[0], allowed, str(path))
                elif isinstance(node, ast.ImportFrom):
                    self.assertEqual(node.level, 0, str(path))
                    self.assertIn((node.module or "").split(".")[0], allowed, str(path))
                elif isinstance(node, ast.Name):
                    self.assertNotIn(node.id, {"__import__", "importlib", "exec", "eval", "compile"}, str(path))
                elif isinstance(node, ast.Attribute):
                    self.assertNotIn(node.attr, {"__import__", "import_module", "exec_module",
                                                 "load_module", "run_path", "run_module"}, str(path))
        self.discrete("ORACLE_IMPORT_BOUNDARY", "all independent module ASTs", True, True)
