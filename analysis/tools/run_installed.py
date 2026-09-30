"""External installed-wheel test runner; not included in the distribution."""
import hashlib
import importlib.metadata as metadata
import json
import os
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile

expected = json.loads(Path(sys.argv[1]).read_bytes())
source = Path(expected["source"]).resolve()
copied = Path(expected["analysis_source"]).resolve()
prefix = Path(sys.prefix).resolve()
evidence = Path(expected["evidence"])
assert sys.flags.isolated and sys.flags.dont_write_bytecode
assert sys.prefix != sys.base_prefix and not os.environ.get("PYTHONPATH")
assert "include-system-site-packages = false" in (prefix / "pyvenv.cfg").read_text().lower()
assert not list(Path.cwd().iterdir())
sys.path.insert(0, expected["tests"])
assert not any(Path(p).resolve().is_relative_to(root) for p in sys.path if p for root in (source, copied))
network = []
def audit(event, args):
    # Local hostname retrieval (used by JUnit) performs no network I/O.
    if (event.startswith("socket.") and event != "socket.gethostname") or event == "urllib.Request":
        network.append(event)
        raise RuntimeError("network prohibited in installed analysis tests")
sys.addaudithook(audit)

import trioctagon_analysis
assert trioctagon_analysis.__version__ == metadata.version("trioctagon-analysis") == "0.1.1"
assert not any(n.startswith(("kernel_physics", "trioctagon_ui", "PySide6")) for n in sys.modules)
site = Path(trioctagon_analysis.__file__).resolve().parent.parent
assert site.is_relative_to(prefix)
with zipfile.ZipFile(expected["wheel"]) as archive:
    for row in expected["members"]:
        name = row["path"]
        if ".data/data/" in name:
            path = prefix / name.split(".data/data/", 1)[1]
        else:
            path = site / name
        # pip legitimately rewrites RECORD and generates its own installer metadata.
        if not name.endswith(".dist-info/RECORD"):
            assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"], name
package = site / "trioctagon_analysis"
assert {p.name for p in package.iterdir()} == {Path(row["path"]).name for row in expected["members"] if row["path"].startswith("trioctagon_analysis/")}
with zipfile.ZipFile(expected["kernel"]) as archive:
    for name in archive.namelist():
        if name.startswith("kernel_physics/"):
            assert (site / name).read_bytes() == archive.read(name), name

import pytest
code = pytest.main([expected["tests"], "-q", "-p", "no:cacheprovider",
    "--rootdir=" + expected["tests"], "--confcutdir=" + expected["tests"],
    "--basetemp=" + str(evidence / "pytest-temp"), "--junitxml=" + str(evidence / "installed-tests.xml")])
origins = {name: str(Path(module.__file__).resolve()) for name, module in sys.modules.items()
    if name.startswith(("trioctagon_analysis", "kernel_physics")) and getattr(module, "__file__", None)}
assert all(Path(path).is_relative_to(site) for path in origins.values())
assert not any(n.startswith(("trioctagon_ui", "PySide6", "research", "kernel_TO")) for n in sys.modules)
assert not network
assert not any(Path(p).resolve().is_relative_to(root) for p in sys.path if p for root in (source, copied))
suite = ET.parse(evidence / "installed-tests.xml").getroot()
counts = {key: sum(int(node.attrib.get(key, 0)) for node in suite.findall("testsuite")) for key in ("tests", "failures", "errors", "skipped")}
result = {"status": "PASS" if code == 0 else "FAIL", "exit_code": code, "counts": counts,
    "isolated": True, "prefix": str(prefix), "origins": origins, "sys_path": sys.path,
    "no_checkout_imports": True, "network_attempts": network, "analysis_version": metadata.version("trioctagon-analysis"),
    "kernel_version": metadata.version("trioctagon-physics"), "wheel_members_verified": True,
    "qualification": "TEST_FIXTURES_AND_DISABLED_PROTOTYPE_TESTS_ARE_NOT_PRODUCTION_ATTESTATION"}
(evidence / "installed-result.json").write_text(json.dumps(result, indent=2) + "\n")
raise SystemExit(code)
