"""Installed tests and external-only, fail-closed Windows certification tooling.

Acquisition is the only network-enabled phase. Certification uses offline pip.
This file needs only stdlib until the installed application tests are executed.
"""
import argparse
from email.parser import BytesParser
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import tomllib
import unittest
import zipfile


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def command(args, cwd, log, env=None):
    result = subprocess.run(list(map(str, args)), cwd=cwd, env=env, capture_output=True,
                            text=True, encoding="utf-8", errors="replace", timeout=900)
    Path(log).write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}); see {log}\n{result.stdout[-2000:]}\n{result.stderr[-6000:]}")
    return result.stdout + result.stderr


def require_lane():
    if sys.platform != "win32" or sys.version_info[:2] != (3, 11) or struct.calcsize("P") != 8:
        raise RuntimeError("Certification requires Windows x86-64 CPython 3.11")


def paths(source, workspace):
    source, workspace = source.resolve(), workspace.resolve()
    if workspace == source or source in workspace.parents:
        raise ValueError("Use a disposable workspace outside the checkout")
    workspace.mkdir(parents=True, exist_ok=True)
    return source, source / "apps/scientific_ui", workspace


def verify_kernel(app, workspace):
    lock = json.loads((app / "kernel-artifact.lock.json").read_text(encoding="utf-8"))
    assert lock["REGISTRY_RESOLUTION_ALLOWED"] is False
    evidence = workspace / "kernel-evidence"
    wheel = evidence / lock["temporary_retrieval"]["wheel_path"]
    assert wheel.name == lock["artifact_filename"] and sha(wheel) == lock["artifact_sha256"]
    for name, key in (("certification.json", "certification_json_sha256"), ("direct-archive.json", "direct_archive_json_sha256")):
        assert sha(evidence / name) == lock["k3c_evidence_identity"][key]
    certification = json.loads((evidence / "certification.json").read_text(encoding="utf-8"))
    assert certification["status"] == "PASS" and certification["source_commit"] == lock["source_commit"]
    # Archive inspection is installer verification, never an application runtime identity query.
    with zipfile.ZipFile(wheel) as archive:
        manifest = json.loads(archive.read("kernel_physics/_distribution_provenance.json"))
    assert manifest["source"]["commit"] == lock["source_commit"]
    assert manifest["source"]["repository"] == lock["source_repository"]
    assert manifest["manifest_version"] == lock["provenance_manifest_version"]
    assert manifest["build_input_sha256"] == lock["manifest_build_input_sha256"]
    assert manifest["software"]["package_version"] == lock["version"]
    direct = json.loads((evidence / "direct-archive.json").read_text(encoding="utf-8"))
    assert direct["manifest"] == manifest
    return wheel, lock


def build_requirements(app, workspace):
    config = tomllib.loads((app / "pyproject.toml").read_text(encoding="utf-8"))
    entries = config["tool"]["trioctagon-ui"]["build-wheels"]
    file = workspace / "build-requirements.txt"
    file.write_text("".join(f"{v['name']}=={v['version']} --hash=sha256:{v['sha256']}\n" for v in entries), encoding="utf-8")
    return file, entries


def inventory(app, workspace):
    locked = {}
    for line in (app / "requirements-win-py311.lock").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"): continue
        match = re.fullmatch(r"([a-z0-9-]+)==(\S+) --hash=sha256:([a-f0-9]{64})", line)
        assert match, line
        locked[match[1]] = (match[2], match[3])
    rows = []; names = set()
    for wheel in sorted((workspace / "wheelhouse").glob("*.whl")):
        with zipfile.ZipFile(wheel) as archive:
            meta = BytesParser().parsebytes(archive.read(next(n for n in archive.namelist() if n.endswith(".dist-info/METADATA"))))
            name = re.sub(r"[-_.]+", "-", meta["Name"]).lower()
            assert name not in names; names.add(name)
            assert (meta["Version"], sha(wheel)) == locked[name]
            notices = [n for n in archive.namelist() if ("/licenses/" in n.lower() or any(t in Path(n).name.lower() for t in ("license", "copying", "notice"))) and not n.endswith(("/", ".py", ".pyi"))]
            rows.append({"name": name, "version": meta["Version"], "filename": wheel.name,
                "sha256": sha(wheel), "requires_python": meta["Requires-Python"],
                "requires_dist": meta.get_all("Requires-Dist", []),
                "license": str(meta["License-Expression"] or meta["License"] or "See packaged notices"),
                "notices": [{"path": n, "sha256": hashlib.sha256(archive.read(n)).hexdigest()} for n in notices]})
    assert names == set(locked) and len(rows) == 15
    assert {n: locked[n][0] for n in ("numpy", "sympy", "mpmath")} == {"numpy": "2.4.4", "sympy": "1.14.0", "mpmath": "1.3.0"}
    notices_text = (app / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    assert all(v["sha256"] in notices_text for v in rows)
    _, builds = build_requirements(app, workspace)
    for v in builds:
        assert sha(workspace / "build-wheelhouse" / v["filename"]) == v["sha256"]
    write_json(workspace / "dependency-inventory-certification.json", rows)
    return rows


def acquire(source, workspace):
    require_lane(); source, app, workspace = paths(source, workspace)
    lock = json.loads((app / "kernel-artifact.lock.json").read_text(encoding="utf-8"))
    repo = lock["temporary_retrieval"]["repository"]
    raw = command(["gh", "run", "view", lock["k3c_run_id"], "--repo", repo, "--json", "conclusion,headSha,status,url"], workspace, workspace / "kernel-run.log")
    run = json.loads(raw)
    assert run["conclusion"] == "success" and run["headSha"] == lock["source_commit"]
    evidence = workspace / "kernel-evidence"
    if not evidence.exists():
        command(["gh", "run", "download", lock["k3c_run_id"], "--repo", repo, "--name",
            lock["k3c_evidence_identity"]["artifact_name"], "--dir", evidence], workspace, workspace / "kernel-acquire.log")
    verify_kernel(app, workspace)
    for name, requirements in (("wheelhouse", app / "requirements-win-py311.lock"), ("build-wheelhouse", build_requirements(app, workspace)[0])):
        command([sys.executable, "-I", "-B", "-m", "pip", "--isolated", "download", "--only-binary=:all:",
            "--no-deps", "--require-hashes", "--dest", workspace / name, "-r", requirements], workspace, workspace / (name + "-acquire.log"))
    rows = inventory(app, workspace)
    write_json(workspace / "acquisition.json", {"status": "PASS", "kernel": lock, "dependencies": rows, "k3c_run": run})
    print("ACQUISITION=PASS; exact kernel and 15 runtime wheels verified", flush=True)


def certify(source, workspace):
    require_lane(); source, app, workspace = paths(source, workspace)
    kernel, lock = verify_kernel(app, workspace); dependencies = inventory(app, workspace)
    git = lambda *args: subprocess.check_output(["git", "-C", str(source), *args])
    tracked = git("ls-files", "-z").decode().split("\0")[:-1]
    starting = {p: sha(source / p) for p in tracked}
    status = git("status", "--porcelain", "--untracked-files=all")
    head = git("rev-parse", "HEAD").decode().strip()
    # Each attempt gets a fresh, external installation; failed evidence is retained.
    # Short environment paths also support Windows hosts without long-path opt-in.
    attempt = Path(tempfile.mkdtemp(prefix="c-", dir=workspace))
    evidence = attempt / "evidence"; evidence.mkdir()
    empty = attempt / "outside-checkout"; empty.mkdir()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1", QT_QPA_PLATFORM="offscreen",
               QT_OPENGL="software", MPLCONFIGDIR=str(attempt / "mplconfig"),
               TRIOCTAGON_UI_EVIDENCE=str(evidence), TRIOCTAGON_UI_SOURCE=str(source))
    env.pop("PYTHONPATH", None)
    def run(label, args, cwd=empty):
        return command(args, cwd, evidence / (label + ".log"), env)
    def venv(name):
        directory = attempt / name
        run(name + "-create", [sys.executable, "-I", "-B", "-m", "venv", directory])
        return directory / "Scripts/python.exe"
    def locked_install(python, requirements, wheels, label):
        run(label, [python, "-I", "-B", "-m", "pip", "--isolated", "install", "--no-index",
            "--only-binary=:all:", "--find-links", wheels, "--require-hashes", "-r", requirements])
    build = venv("b")
    locked_install(build, app / "requirements-win-py311.lock", workspace / "wheelhouse", "build-runtime-deps")
    locked_install(build, build_requirements(app, workspace)[0], workspace / "build-wheelhouse", "build-tools")
    build_src = attempt / "build-source"
    shutil.copytree(app, build_src, ignore=shutil.ignore_patterns("__pycache__", "*.egg-info", "build", "dist"))
    dist = attempt / "dist"; dist.mkdir()
    run("wheel-build", [build, "-I", "-B", "-m", "pip", "--isolated", "wheel", "--no-index",
        "--no-deps", "--no-build-isolation", "--wheel-dir", dist, build_src])
    wheels = list(dist.glob("*.whl")); assert len(wheels) == 1
    wheel = wheels[0]
    with zipfile.ZipFile(wheel) as archive:
        members = archive.namelist()
        package = {"trioctagon_ui/" + p.name for p in (app / "src/trioctagon_ui").iterdir() if p.is_file()}
        assert {n for n in members if n.startswith("trioctagon_ui/")} == package
        assert all(n in package or ".dist-info/" in n or ".data/data/share/trioctagon-scientific-ui/" in n for n in members)
        for n in members:
            if ".data/" in n:
                assert Path(n).name in ("kernel-artifact.lock.json", "requirements-win-py311.lock")
                assert archive.read(n) == (app / Path(n).name).read_bytes()
        assert not any(n.endswith((".whl", ".dll", ".pyd")) or n.startswith(("tests/", "kernel_physics/")) for n in members)
        write_json(evidence / "app-wheel.json", {"filename": wheel.name, "sha256": sha(wheel), "members": members})
    runtime = venv("r")
    locked_install(runtime, app / "requirements-win-py311.lock", workspace / "wheelhouse", "runtime-deps")
    run("kernel-app-install", [runtime, "-I", "-B", "-m", "pip", "--isolated", "install", "--no-index", "--no-deps", kernel, wheel])
    run("pip-check", [runtime, "-I", "-B", "-m", "pip", "check"])
    tests = attempt / "test-suite"; tests.mkdir()
    for file in (app / "tests").glob("test_*.py"): shutil.copyfile(file, tests / file.name)
    env["TRIOCTAGON_UI_APP_WHEEL"] = str(wheel)
    result = run("app-tests", [runtime, "-I", "-B", "-m", "unittest", "discover", "-s", tests, "-p", "test_*.py", "-v"])
    match = re.search(r"Ran (\d+) tests in ([\d.]+)s\s+OK\s*$", result)
    assert match
    assert {p: sha(source / p) for p in tracked} == starting
    assert git("status", "--porcelain", "--untracked-files=all") == status
    assert git("rev-parse", "HEAD").decode().strip() == head
    run("diff-check", ["git", "-C", source, "diff", "--check"])
    assert sha(kernel) == lock["artifact_sha256"]
    report = {"status": "PASS", "source_commit": head, "github_sha": os.environ.get("GITHUB_SHA"),
        "python": platform.python_version(), "platform": platform.platform(), "kernel": lock,
        "dependencies": dependencies, "app_wheel": str(wheel), "app_wheel_sha256": sha(wheel),
        "app_tests": int(match[1]), "seconds": float(match[2]), "installed_runtime": str(runtime),
        "offline_installs": True, "runtime_network_attempts": 0, "model_required": False, "gpu_required": False,
        "all_tracked_bytes_unchanged": True, "source_status_unchanged": True, "evidence": str(evidence)}
    write_json(evidence / "certification.json", report)
    write_json(workspace / "latest-certification.json", report)
    print(json.dumps({k: report[k] for k in ("status", "app_tests", "app_wheel_sha256", "evidence", "installed_runtime")}), flush=True)


class InstallTests(unittest.TestCase):
    def evidence(self, name, data):
        if os.environ.get("TRIOCTAGON_UI_EVIDENCE"):
            write_json(Path(os.environ["TRIOCTAGON_UI_EVIDENCE"]) / name, data)

    def test_installed_isolated_launch_and_entry_point(self):
        with tempfile.TemporaryDirectory(prefix="ui-launch-") as directory:
            for args in ([sys.executable, "-I", "-B", "-m", "trioctagon_ui", "--smoke-test"],
                         [str(Path(sys.executable).parent / "trioctagon-scientific-ui.exe"), "--smoke-test"]):
                result = subprocess.run(args, cwd=directory, capture_output=True, text=True, encoding="utf-8", timeout=90)
                self.assertEqual(result.returncode, 0, result.stderr)
                report = json.loads(result.stdout.strip().splitlines()[-1])
                self.assertEqual(report["status"], "PASS")
                self.assertEqual(report["scientific_jobs_submitted"], 0)
                self.assertEqual(report["runtime_network_attempts"], [])
                self.evidence("installed-launch" + ("-isolated" if report["isolated"] else "-entry-point") + ".json", report)

    def test_installed_resources_and_module_origins(self):
        import trioctagon_ui
        from trioctagon_ui.requests import help_data
        from trioctagon_ui.record_views import kernel_lock
        from kernel_physics import api
        site = Path(sys.prefix).resolve()
        origins = {"app": str(Path(trioctagon_ui.__file__).resolve()), "kernel_api": str(Path(api.__file__).resolve())}
        self.assertTrue(all(Path(p).is_relative_to(site) for p in origins.values()))
        self.assertEqual(importlib.metadata.version("trioctagon-scientific-ui"), "0.1.0")
        self.assertTrue(help_data()["items"])
        self.assertFalse(kernel_lock()["REGISTRY_RESOLUTION_ALLOWED"])
        self.evidence("installed-origins.json", {"prefix": str(site), "origins": origins, "kernel_lock": kernel_lock()})

    def test_installed_worker_science_evidence(self):
        from trioctagon_ui import requests as r
        from trioctagon_ui.record_views import kernel_lock
        from test_requests import example
        from test_worker_contract import run_child
        child, report = run_child(r.run_request(example("1")))
        self.assertEqual(child.returncode, 0, child.stderr)
        self.assertEqual(report["result"]["source_commit"], kernel_lock()["source_commit"])
        self.assertTrue(report["isolated"])
        self.assertEqual(report["runtime_network_attempts"], [])
        self.assertEqual(report["imports"], {"gui": [], "models": []})
        self.evidence("installed-worker.json", report)

    def test_installed_k4c_science_smokes(self):
        from trioctagon_ui import requests as r
        from test_requests import example, custom
        from test_worker_contract import run_child, ring_example
        draft = example("1"); draft["observers"] = [custom("staged", "s"), custom("ema", "e")]
        cases = {"ring": r.run_request(ring_example()), "custom_observers": r.run_request(draft),
            "passive": r.analysis_request("quadratic_form", {"vector": ["1", "2", "3"]}),
            "C01_section": r.geometry_request("C01", {"section_heights": ["1/10"]}),
            "D03_aligned": r.geometry_request("D03", {"construction": "aligned", "s": "1", "g_gap": "1"})}
        reports = {}
        for name, envelope in cases.items():
            child, response = run_child(envelope)
            self.assertEqual(child.returncode, 0, child.stderr)
            self.assertEqual(response["ui_response_version"], 2)
            self.assertEqual(response["imports"], {"gui": [], "models": []})
            self.assertEqual(response["runtime_network_attempts"], [])
            self.assertTrue(response["isolated"]); reports[name] = response
        parent = reports["custom_observers"]["result"]["canonical_json"]
        child, response = run_child(r.analysis_request("direct_history_coordinates", {"observer_id": "s", "key": "Z_total"}, source={"mode": "record", "record_json": parent, "sample_index": "0"}))
        self.assertEqual(child.returncode, 0, child.stderr)
        self.assertEqual(response["result"]["result_kind"], "analysis")
        reports["history"] = response
        self.evidence("installed-k4c-smokes.json", reports)


if __name__ == "__main__":
    if "--acquire" in sys.argv or "--certify" in sys.argv:
        parser = argparse.ArgumentParser(description=__doc__)
        action = parser.add_mutually_exclusive_group(required=True)
        action.add_argument("--acquire", action="store_true"); action.add_argument("--certify", action="store_true")
        parser.add_argument("--source", type=Path, required=True); parser.add_argument("--workspace", type=Path, required=True)
        args = parser.parse_args()
        (acquire if args.acquire else certify)(args.source, args.workspace)
    else:
        unittest.main()
