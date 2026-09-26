"""K2c static independence and scoped runtime file-access checks."""
import ast
import builtins
import io
import os
from pathlib import Path
import unittest
from unittest.mock import patch


def guarded_open(original):
    def checked(file,*args,**kwargs):
        if isinstance(file,(str,bytes,os.PathLike)):
            name=os.fsdecode(file).replace('\\','/').lower()
            if '/papers/' in '/'+name or '/research/' in '/'+name or 'verifier' in name or 'paper_f_exact_checks' in name:
                raise AssertionError('K2C_STATUS=HOLD: forbidden support/verifier file access: '+name)
        return original(file,*args,**kwargs)
    return checked


class GuardedOracleCase(unittest.TestCase):
    """All P7/P8 oracle and runtime tests execute under the same read guard."""
    def setUp(self):
        for module,name in ((builtins,'open'),(io,'open'),(os,'open')):
            context=patch.object(module,name,guarded_open(getattr(module,name)))
            context.start()
            self.addCleanup(context.stop)


class K2cOracleBoundaryTests(GuardedOracleCase):
    """PASS SUPPORTS explicit imports and no direct/dynamic source/file loading.
    PASS DOES NOT SUPPORT a general-purpose sandbox or mathematical proof.
    """
    def test_oracle_imports_and_file_boundary(self):
        path=Path(__file__).parent/'parity_oracles'/'paper_f_oracle.py'
        tree=ast.parse(path.read_text(encoding='utf-8'))
        imports=[]
        banned={'__import__','__builtins__','importlib','exec','eval','compile',
                'open','getattr','globals','locals','vars','breakpoint'}
        attributes={'import_module','exec_module','load_module','run_path','run_module',
                    'read_text','read_bytes','read','write','open','__dict__','__builtins__',
                    '__import__','lambdify','sympify','parse_expr'}
        for node in ast.walk(tree):
            if isinstance(node,ast.Import):
                for alias in node.names:
                    self.assertIn(alias.name,{'sympy','mpmath'})
                    imports.append(alias.name)
            elif isinstance(node,ast.ImportFrom):
                self.fail('No project-local or from import is used by K2c oracle')
            elif isinstance(node,ast.Name):
                self.assertNotIn(node.id,banned)
            elif isinstance(node,ast.Attribute):
                self.assertNotIn(node.attr,attributes)
        self.assertEqual(sorted(imports),['mpmath','sympy'])

    def test_file_guard_rejects_support_reads_without_opening_them(self):
        forbidden=['papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md',
                   'research/paper_F_transverse_normal_form/paper_f_exact_checks_v0_2.py']
        for file in forbidden:
            for opener in (builtins.open,io.open,os.open):
                with self.assertRaisesRegex(AssertionError,'forbidden support/verifier'):
                    opener(file,'r')
