import ast
from pathlib import Path
import subprocess
import sys

import trioctagon_analysis

PACKAGE = Path(trioctagon_analysis.__file__).parent

def test_only_public_loader_import_and_no_other_kernel_calls():
    imports = []
    for path in PACKAGE.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                assert not any(n.name.startswith(("kernel_physics", "trioctagon_ui", "PySide6",
                                                  "research", "kernel_TO")) for n in node.names)
            if isinstance(node, ast.ImportFrom) and node.module and node.module.startswith("kernel_physics"):
                assert node.module == "kernel_physics" and [n.name for n in node.names] == ["api"]
                imports.append((path.name, node.lineno))
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                text = ast.unparse(node.func)
                if text.startswith("api."):
                    assert text == "api.RunRecord.from_json"
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                assert node.func.id not in ("eval", "exec", "__import__")
    assert len(imports) == 1 and imports[0][0] == "provider.py"

def test_test_only_mock_never_in_distributed_runtime():
    for path in PACKAGE.glob("*.py"):
        text = path.read_text(encoding="utf-8")
        assert "TEST_ONLY_MockAttestor" not in text
        assert "trust_parent_commit" not in text
        assert "skip_attestation" not in text
        assert "development_accept_anything" not in text

def test_headless_package_import_does_not_import_kernel_or_ui():
    code = """
import sys
sys.path.insert(0, sys.argv[1])
import trioctagon_analysis.catalogue
import trioctagon_analysis.records
import trioctagon_analysis.coordinator
import trioctagon_analysis.persistence
assert not any(n.startswith(('kernel_physics', 'trioctagon_ui', 'PySide6')) for n in sys.modules)
print('HEADLESS_IMPORT_PASS')
"""
    result = subprocess.run([sys.executable, "-I", "-B", "-c", code, str(PACKAGE.parent)],
                            capture_output=True, text=True, check=True)
    assert result.stdout.strip() == "HEADLESS_IMPORT_PASS"
