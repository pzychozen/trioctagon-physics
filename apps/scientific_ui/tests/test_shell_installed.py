"""Same assertions for isolated source and installed UI; no omitted source tests."""
import hashlib
from importlib import resources
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from trioctagon_ui import shell_reference as ref


class ShellInstalledTests(unittest.TestCase):
    def test_packaged_resource_and_actual_module_identities(self):
        root=resources.files('trioctagon_ui'); identity=ref.implementation_identity()
        self.assertEqual(hashlib.sha256(root.joinpath(ref.RESOURCE).read_bytes()).hexdigest(),ref.RESOURCE_SHA)
        self.assertEqual(hashlib.sha256(root.joinpath(ref.MANIFEST).read_bytes()).hexdigest(),ref.MANIFEST_SHA)
        self.assertIn('Hilmir',root.joinpath('shell_reference_notice_v0_1.txt').read_text(encoding='utf-8'))
        for name,digest in identity['module_sha256'].items(): self.assertEqual(hashlib.sha256(root.joinpath(name).read_bytes()).hexdigest(),digest)
        forbidden=('.html','.pdf','.js','.whl','.pyd')
        self.assertFalse(any(p.name.endswith(forbidden) for p in root.iterdir() if p.name.startswith('shell_')))
        if os.environ.get('TRIOCTAGON_UI_EVIDENCE'):
            (Path(os.environ['TRIOCTAGON_UI_EVIDENCE'])/'shell-origins.json').write_text(json.dumps({'status':'PASS','module':str(ref.__file__),'identity':identity,'source_ui_route':os.environ.get('TRIOCTAGON_UI_SOURCE_TESTS'),'python':sys.executable},indent=2),encoding='utf-8')

    def test_pure_evaluator_no_scientific_gui_network_or_rng_imports(self):
        script='''import sys,importlib.abc,json
sys.path.insert(0,sys.argv[1])
class Block(importlib.abc.MetaPathFinder):
 def find_spec(self,fullname,*args):
  if fullname.split('.')[0] in {'PySide6','matplotlib','numpy','sympy','kernel_physics','trioctagon_analysis','trioctagon_historical_protocol','trioctagon_historical_kernel','random','socket','subprocess'}: raise AssertionError('Forbidden import '+fullname)
sys.meta_path.insert(0,Block())
from trioctagon_ui.shell_reference import load_reference
from trioctagon_ui.shell_observer import evaluate,Request
ref=load_reference()
for key in ('original','A','B','R_equals_w','t_equals_w','assigned_R10','assigned_RT'): assert len(evaluate(ref,Request(preset=key)).data['branches'])==42
print('PURE_PASS')
'''
        # importlib.abc may preload random: remove it before installing the guard.
        script=script.replace('sys.meta_path.insert(0,Block())',"sys.modules.pop('random',None)\nsys.meta_path.insert(0,Block())")
        with tempfile.TemporaryDirectory(prefix='shell-pure-') as temporary:
            path=Path(temporary)/'pure.py'; path.write_text(script,encoding='utf-8')
            result=subprocess.run([sys.executable,'-I','-B',str(path),str(Path(ref.__file__).parent.parent)],cwd=temporary,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr); self.assertIn('PURE_PASS',result.stdout)
