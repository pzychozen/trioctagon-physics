"""Bounded static import audit for the single new K2b oracle."""
import ast
from pathlib import Path
import unittest


class K2bOracleBoundaryTests(unittest.TestCase):
    def test_transverse_oracle_import_boundary(self):
        path = Path(__file__).parent/'parity_oracles'/'transverse_axis_oracle.py'
        tree = ast.parse(path.read_text(encoding='utf-8'))
        for node in ast.walk(tree):
            if isinstance(node,ast.Import):
                self.assertTrue(all(v.name in {'mpmath','sympy'} for v in node.names))
            elif isinstance(node,ast.ImportFrom):
                self.fail('No from/relative import is needed in this bounded oracle')
            elif isinstance(node,ast.Name):
                self.assertNotIn(node.id,{'__import__','__builtins__','importlib','exec','eval','compile'})
            elif isinstance(node,ast.Attribute):
                self.assertNotIn(node.attr,{'__import__','import_module','exec_module','load_module','run_path','run_module'})
