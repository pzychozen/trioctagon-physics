"""Installed tests and external-only, fail-closed Windows certification tooling.

Acquisition is the only network-enabled phase. Certification uses offline pip.
This file needs only stdlib until the installed application tests are executed.
"""
import argparse
import base64
import csv
from email.parser import BytesParser
import hashlib
import importlib.metadata
import io
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
    selection_path = workspace / "kernel-selection.json"
    if selection_path.exists():
        selection = json.loads(selection_path.read_text(encoding="utf-8"))
        wheel = (workspace / selection["relative_path"]).resolve()
        if not wheel.is_relative_to(workspace.resolve()): raise ValueError("Kernel path must remain in acquisition workspace")
        verify_wheel_equivalence(wheel, lock)
        if selection["classification"] == "CERTIFIED_RECONSTRUCTION": return wheel, lock
        if selection["classification"] != "PREFERRED_EXACT_ARCHIVE": raise ValueError("Unknown kernel acquisition classification")
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
    verify_wheel_equivalence(wheel, lock)
    return wheel, lock


def verify_wheel_equivalence(wheel, lock):
    """Observe certified bytes; never normalize or rewrite an accepted archive."""
    rule = lock["wheel_equivalence"]
    if lock["lock_version"] != 2 or rule["version"] != 1: raise ValueError("Unsupported kernel lock/equivalence version")
    raw = wheel.getvalue() if isinstance(wheel, io.BytesIO) else Path(wheel).read_bytes()
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = archive.namelist()
        if len(set(names)) != len(names): raise ValueError("Duplicate wheel members")
        contents = {name: archive.read(name) for name in names}
    optional = rule["optional_prepared_metadata"]; record_path = rule["record"]["path"]
    stable = {v["path"]: v for v in rule["stable_members"]}
    if len(stable) != 25 or rule["stable_member_count"] != 25: raise ValueError("Frozen stable inventory must have 25 members")
    if set(contents) - {optional["path"], record_path} != set(stable) or record_path not in contents:
        raise ValueError("Stable member set mismatch or unknown extra member")
    for name, expected in stable.items():
        value = contents[name]
        if len(value) != expected["size"] or hashlib.sha256(value).hexdigest() != expected["sha256"]:
            raise ValueError("Stable member bytes mismatch: " + name)
    manifest = json.loads(contents["kernel_physics/_distribution_provenance.json"])
    if (manifest["source"]["commit"] != lock["source_commit"] or manifest["source"]["repository"] != lock["source_repository"]
        or manifest["build_input_sha256"] != lock["manifest_build_input_sha256"]
        or manifest["manifest_version"] != lock["provenance_manifest_version"]
        or manifest["software"]["package_version"] != lock["version"]): raise ValueError("Frozen manifest/source identity mismatch")
    if optional["size"] != 64 or optional["content"] != manifest["build_input_sha256"]: raise ValueError("Invalid optional witness contract")
    present = optional["path"] in contents
    if present and contents[optional["path"]] != optional["content"].encode("ascii"):
        raise ValueError("Optional witness must contain exactly 64 ASCII manifest-digest bytes")
    rows = list(csv.reader(io.StringIO(contents[record_path].decode("utf-8")), strict=True))
    if any(len(row) != 3 for row in rows): raise ValueError("RECORD requires triples")
    paths = [row[0] for row in rows]
    if len(set(paths)) != len(paths) or set(paths) != set(contents): raise ValueError("RECORD must contain exactly one row per actual member")
    for name, recorded_hash, recorded_size in rows:
        if name == record_path:
            if recorded_hash or recorded_size: raise ValueError("RECORD self row requires empty hash and size")
        else:
            expected = "sha256=" + base64.urlsafe_b64encode(hashlib.sha256(contents[name]).digest()).decode("ascii").rstrip("=")
            if recorded_hash != expected or recorded_size != str(len(contents[name])): raise ValueError("RECORD hash/size mismatch: " + name)
    projected = sorted((row for row in rows if row[0] != optional["path"]), key=lambda row: row[0])
    core = hashlib.sha256(json.dumps(projected, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest()
    if core != rule["record"]["core_sha256"]: raise ValueError("RECORD core identity mismatch")
    return {"status": "PASS", "archive_sha256": hashlib.sha256(raw).hexdigest(), "member_count": len(contents),
        "stable_member_count": 25, "prepared_metadata_witness": present, "record_internal_validation": "PASS",
        "record_core_sha256": core, "manifest_identity": "PASS", "source_commit": manifest["source"]["commit"]}


def acquire_preferred(app, workspace, lock):
    """Only definite absence/expiry enables fallback; downloaded corruption is fatal."""
    evidence = workspace / "kernel-evidence"
    if evidence.exists():
        return verify_preferred(app, workspace, lock)
    repo = lock["temporary_retrieval"]["repository"]
    result = subprocess.run(["gh", "api", f"repos/{repo}/actions/artifacts/{lock['k3c_evidence_identity']['artifact_id']}"],
        cwd=workspace, capture_output=True, text=True, encoding="utf-8", timeout=120)
    (workspace / "kernel-availability.log").write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode:
        if "HTTP 404" in result.stderr or "HTTP 410" in result.stderr: return None
        raise RuntimeError("Preferred artifact availability could not be established; see kernel-availability.log")
    metadata = json.loads(result.stdout)
    if metadata["expired"]: return None
    if metadata["id"] != lock["k3c_evidence_identity"]["artifact_id"] or metadata["name"] != lock["k3c_evidence_identity"]["artifact_name"]:
        raise ValueError("Preferred artifact metadata identity mismatch")
    command(["gh", "run", "download", lock["k3c_run_id"], "--repo", repo, "--name", metadata["name"], "--dir", evidence], workspace, workspace / "kernel-acquire.log")
    return verify_preferred(app, workspace, lock)


def verify_preferred(app, workspace, lock):
    evidence = workspace / "kernel-evidence"
    wheel = evidence / lock["temporary_retrieval"]["wheel_path"]
    if sha(wheel) != lock["artifact_sha256"]: raise ValueError("Downloaded preferred archive SHA mismatch; reconstruction fallback forbidden")
    for name, key in (("certification.json", "certification_json_sha256"), ("direct-archive.json", "direct_archive_json_sha256")):
        if sha(evidence / name) != lock["k3c_evidence_identity"][key]: raise ValueError("Preferred K3 evidence identity mismatch")
    certification = json.loads((evidence / "certification.json").read_text(encoding="utf-8"))
    if certification["status"] != "PASS" or certification["source_commit"] != lock["source_commit"]: raise ValueError("Preferred K3 certification mismatch")
    direct = verify_wheel_equivalence(wheel, lock)
    rebuilt = evidence / "rebuilt-wheel" / lock["artifact_filename"]
    if sha(rebuilt) != lock["wheel_equivalence"]["certified_variants"]["rebuilt"]["archive_sha256"]: raise ValueError("Original rebuilt archive identity mismatch")
    other = verify_wheel_equivalence(rebuilt, lock)
    write_json(workspace / "preferred-equivalence.json", {"direct": direct, "rebuilt": other})
    return wheel


def reconstruct_kernel(app, workspace, lock):
    """Network-enabled acquisition only; exact detached source and offline build."""
    directory = Path(tempfile.mkdtemp(prefix="k-", dir=workspace)); source = directory / "s"
    env = dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1"); env.pop("PYTHONPATH", None)
    def run(label, args): return command(args, directory, directory / (label + ".log"), env).strip()
    run("init", ["git", "init", source]); run("crlf", ["git", "-C", source, "config", "core.autocrlf", "false"])
    run("origin", ["git", "-C", source, "remote", "add", "origin", lock["source_repository"]])
    run("fetch", ["git", "-C", source, "fetch", "--depth", "1", "origin", lock["source_commit"]])
    run("checkout", ["git", "-C", source, "checkout", "--detach", lock["source_commit"]])
    if run("head", ["git", "-C", source, "rev-parse", "HEAD"]) != lock["source_commit"]: raise ValueError("Reconstruction HEAD mismatch")
    if run("origin-read", ["git", "-C", source, "remote", "get-url", "origin"]) != lock["source_repository"]: raise ValueError("Reconstruction origin mismatch")
    if run("clean-before", ["git", "-C", source, "status", "--porcelain", "--untracked-files=no"]): raise ValueError("Dirty reconstruction source")
    build = directory / "b"; run("venv", [sys.executable, "-I", "-B", "-m", "venv", build]); python = build / "Scripts/python.exe"
    tools = lock["reconstruction"]["build_tools"]
    if tools != build_requirements(app, workspace)[1]: raise ValueError("Reconstruction tool lock differs from approved build tools")
    wheels = []
    for entry in tools:
        path = workspace / "build-wheelhouse" / entry["filename"]
        if sha(path) != entry["sha256"]: raise ValueError("Reconstruction tool hash mismatch")
        wheels.append(path)
    # The kernel backend imports its frozen numeric dependencies to capture identity.
    wheels.extend(next((workspace / "wheelhouse").glob(name + "-*.whl")) for name in ("numpy", "sympy", "mpmath"))
    run("install", [python, "-I", "-B", "-m", "pip", "--isolated", "install", "--no-index", "--no-deps", *wheels])
    dist = directory / "dist"; dist.mkdir()
    run("build", [python, "-I", "-B", "-m", "pip", "--isolated", "wheel", "--no-index", "--no-deps", "--no-build-isolation", "--wheel-dir", dist, source])
    wheel = dist / lock["artifact_filename"]; equivalence = verify_wheel_equivalence(wheel, lock)
    run("k3-verifier", [python, "-B", source / "tools/verify_distribution.py", "--source", source, "--wheel", wheel, "--report", directory / "k3-verifier.json"])
    if run("clean-after", ["git", "-C", source, "status", "--porcelain", "--untracked-files=no"]): raise ValueError("Reconstruction changed tracked source")
    report = {"classification": "CERTIFIED_RECONSTRUCTION", "relative_path": wheel.relative_to(workspace).as_posix(),
        "equivalence": equivalence, "source_commit": lock["source_commit"], "build_tools": tools, "existing_k3_verifier": "PASS", "wheel_postprocessing": False}
    write_json(workspace / "reconstructed-kernel.json", report)
    return wheel


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
    for name, requirements in (("wheelhouse", app / "requirements-win-py311.lock"), ("build-wheelhouse", build_requirements(app, workspace)[0])):
        command([sys.executable, "-I", "-B", "-m", "pip", "--isolated", "download", "--only-binary=:all:",
            "--no-deps", "--require-hashes", "--dest", workspace / name, "-r", requirements], workspace, workspace / (name + "-acquire.log"))
    rows = inventory(app, workspace)
    preferred = acquire_preferred(app, workspace, lock)
    reconstructed = reconstruct_kernel(app, workspace, lock)
    selected = preferred or reconstructed
    write_json(workspace / "kernel-selection.json", {"classification": "PREFERRED_EXACT_ARCHIVE" if preferred else "CERTIFIED_RECONSTRUCTION", "relative_path": selected.relative_to(workspace).as_posix()})
    verify_kernel(app, workspace)
    write_json(workspace / "acquisition.json", {"status": "PASS", "kernel": lock, "dependencies": rows,
        "preferred_artifact": "PASS" if preferred else "UNAVAILABLE", "forced_reconstruction": json.loads((workspace / "reconstructed-kernel.json").read_text(encoding="utf-8"))})
    print("ACQUISITION=PASS; exact closure and forced certified reconstruction verified", flush=True)


def certify(source, workspace):
    require_lane(); source, app, workspace = paths(source, workspace)
    kernel, lock = verify_kernel(app, workspace); dependencies = inventory(app, workspace)
    reconstruction = json.loads((workspace / "reconstructed-kernel.json").read_text(encoding="utf-8"))
    reconstructed = (workspace / reconstruction["relative_path"]).resolve()
    if not reconstructed.is_relative_to(workspace): raise ValueError("Reconstruction path escaped acquisition workspace")
    verify_wheel_equivalence(reconstructed, lock)
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
    env["TRIOCTAGON_UI_PREFERRED_KERNEL"] = str(workspace / "kernel-evidence" / lock["temporary_retrieval"]["wheel_path"])
    env["TRIOCTAGON_UI_RECONSTRUCTED_KERNEL"] = str(reconstructed)
    result = run("app-tests", [runtime, "-I", "-B", "-m", "unittest", "discover", "-s", tests, "-p", "test_*.py", "-v"])
    match = re.search(r"Ran (\d+) tests in ([\d.]+)s\s+OK\s*$", result)
    assert match
    # Second kernel installation needs only the frozen numeric closure: the
    # existing scientific worker is GUI-free. The full UI suite ran above.
    alternate = venv("a")
    numeric = [next((workspace / "wheelhouse").glob(n + "-*.whl")) for n in ("numpy", "sympy", "mpmath")]
    run("reconstructed-install", [alternate, "-I", "-B", "-m", "pip", "--isolated", "install", "--no-index", "--no-deps", *numeric, reconstructed, wheel])
    smoke_script = empty / "kernel-smoke.py"
    smoke_script.write_text(KERNEL_WORKER_SMOKE, encoding="utf-8")
    original_smoke = json.loads(run("selected-kernel-worker", [runtime, "-I", "-B", smoke_script]))
    rebuilt_smoke = json.loads(run("reconstructed-kernel-worker", [alternate, "-I", "-B", smoke_script]))
    assert original_smoke["source_commit"] == rebuilt_smoke["source_commit"] == lock["source_commit"]
    write_json(evidence / "both-kernel-installations.json", {"selected": original_smoke, "reconstructed": rebuilt_smoke,
        "equivalence": verify_wheel_equivalence(reconstructed, lock), "reconstruction": reconstruction})
    for filename in ("acquisition.json", "preferred-equivalence.json", "reconstructed-kernel.json", "kernel-selection.json"):
        if (workspace / filename).exists(): shutil.copyfile(workspace / filename, evidence / filename)
    assert {p: sha(source / p) for p in tracked} == starting
    assert git("status", "--porcelain", "--untracked-files=all") == status
    assert git("rev-parse", "HEAD").decode().strip() == head
    run("diff-check", ["git", "-C", source, "diff", "--check"])
    verify_kernel(app, workspace)
    report = {"status": "PASS", "source_commit": head, "github_sha": os.environ.get("GITHUB_SHA"),
        "python": platform.python_version(), "platform": platform.platform(), "kernel": lock,
        "dependencies": dependencies, "app_wheel": str(wheel), "app_wheel_sha256": sha(wheel),
        "app_tests": int(match[1]), "seconds": float(match[2]), "installed_runtime": str(runtime),
        "offline_installs": True, "runtime_network_attempts": 0, "model_required": False, "gpu_required": False,
        "all_tracked_bytes_unchanged": True, "source_status_unchanged": True, "evidence": str(evidence)}
    report["certified_reconstruction"] = reconstruction
    write_json(evidence / "certification.json", report)
    write_json(workspace / "latest-certification.json", report)
    print(json.dumps({k: report[k] for k in ("status", "app_tests", "app_wheel_sha256", "evidence", "installed_runtime")}), flush=True)


KERNEL_WORKER_SMOKE = '''import json,pathlib,subprocess,sys,tempfile
from trioctagon_ui import requests
draft=requests.apply_reference(requests.apply_seed(requests.blank_draft()),'0')
draft.update(update_index='0',updates='1')
with tempfile.TemporaryDirectory(prefix='kernel-worker-smoke-') as directory:
 directory=pathlib.Path(directory); request=directory/'request.json'; response=directory/'response.json'
 request.write_text(json.dumps(requests.run_request(draft)),encoding='utf-8')
 child=subprocess.run([sys.executable,'-I','-B','-m','trioctagon_ui.worker','--request',str(request),'--response',str(response)],cwd=directory,capture_output=True,text=True,encoding='utf-8')
 assert child.returncode==0,child.stderr
 result=json.loads(response.read_text(encoding='utf-8'))
 assert result['status']=='completed' and result['isolated'] and result['imports']=={'gui':[],'models':[]} and result['runtime_network_attempts']==[]
 print(json.dumps({'status':'PASS','source_commit':result['result']['source_commit'],'digest':result['result']['deterministic_sha256'],'isolated_worker':True,'runtime_network_attempts':0}))
'''


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

    def test_installed_k4d_dataset_comparison_and_exports(self):
        from PySide6.QtWidgets import QApplication
        from matplotlib.figure import Figure
        from trioctagon_ui import sweeps, exports
        from trioctagon_ui.comparison import ComparisonView
        from trioctagon_ui.jobs import JobManager
        from trioctagon_ui.record_views import RecordView, kernel_lock
        from test_requests import example
        from test_sweeps import spin
        qt = QApplication.instance() or QApplication([])
        self.__class__.qt = qt
        with tempfile.TemporaryDirectory(prefix="installed-k4d-") as directory:
            directory = Path(directory); jobs = JobManager(); controller = sweeps.SweepController(jobs)
            plan = sweeps.make_plan(example("1"), {"g": {"values": [".1", ".2"]}}, kernel_lock())
            controller.create(plan, directory / "dataset"); controller.start(); spin(lambda: not controller.active)
            self.assertEqual([c["status"] for c in controller.manifest["cases"]], ["completed", "completed"])
            records = [RecordView((directory / "dataset" / c["record_path"]).read_text(encoding="utf-8")) for c in controller.manifest["cases"]]
            comparison = ComparisonView(*records, (0, 1, 2)); self.assertTrue(comparison.rows())
            figure = Figure(); ax = figure.subplots()
            values = comparison.series()["omega[0].re"]
            ax.plot([v[0] for v in values], [v[1] for v in values], label="A", marker="o")
            ax.plot([v[0] for v in values], [v[2] for v in values], label="B", linestyle="--", marker="s")
            context = {"view_type": "comparison", "parents": [exports.parent_identity(v) for v in records],
                "display_precision": 17, "visible_series": ["omega[0].re"], "selection": {"exact_common_update_indices": [0, 1]}}
            exports.export_csv(records[0], directory / "samples.csv", ["omega"], {"mode": "all"}, kernel_identity=kernel_lock())
            for extension in ("png", "svg"): exports.export_image(figure, directory / ("comparison." + extension), context)
            self.evidence("installed-k4d-smoke.json", {"status": "PASS", "cases": 2, "manifest_version": 1,
                "comparison": "exact stored update-index intersection", "exports": ["CSV", "PNG", "SVG"], "sidecars": 3,
                "parent_digests": [v.digest for v in records], "scientific_worker_operations": "existing run only"})
            if os.environ.get("TRIOCTAGON_UI_EVIDENCE"):
                shutil.copytree(directory, Path(os.environ["TRIOCTAGON_UI_EVIDENCE"]) / "k4d-examples")


class KernelEquivalenceTests(unittest.TestCase):
    def inputs(self):
        from trioctagon_ui.record_views import kernel_lock
        lock = kernel_lock()
        preferred = Path(os.environ.get("TRIOCTAGON_UI_PREFERRED_KERNEL", "missing"))
        candidate = Path(os.environ.get("TRIOCTAGON_UI_RECONSTRUCTED_KERNEL", "missing"))
        if not candidate.is_file(): self.skipTest("Run external certification to supply immutable reconstruction evidence")
        return lock, preferred, candidate

    def test_original_certified_variants_and_reconstruction(self):
        lock, preferred, candidate = self.inputs()
        observed = {"reconstructed": verify_wheel_equivalence(candidate, lock)}
        if preferred.exists():
            rebuilt = preferred.parent.parent / "rebuilt-wheel" / preferred.name
            observed.update(direct=verify_wheel_equivalence(preferred, lock), rebuilt=verify_wheel_equivalence(rebuilt, lock))
            self.assertTrue(observed["direct"]["prepared_metadata_witness"])
            self.assertFalse(observed["rebuilt"]["prepared_metadata_witness"])
        self.assertTrue(all(v["stable_member_count"] == 25 for v in observed.values()))
        self.assertEqual({v["record_core_sha256"] for v in observed.values()}, {lock["wheel_equivalence"]["record"]["core_sha256"]})
        if os.environ.get("TRIOCTAGON_UI_EVIDENCE"): write_json(Path(os.environ["TRIOCTAGON_UI_EVIDENCE"]) / "kernel-equivalence.json", observed)

    def test_reject_all_unauthorized_equivalence_variance(self):
        from copy import deepcopy
        lock, preferred, candidate = self.inputs()
        reference = preferred if preferred.exists() else candidate
        original_hash = sha(reference)
        with zipfile.ZipFile(reference) as archive: original = {n: archive.read(n) for n in archive.namelist()}
        optional = lock["wheel_equivalence"]["optional_prepared_metadata"]["path"]
        record = lock["wheel_equivalence"]["record"]["path"]
        # Deliberately invalid in-memory test fixtures, never candidate artifacts.
        def with_rows(data, mutate):
            rows = list(csv.reader(io.StringIO(data[record].decode("utf-8"))))
            mutate(rows)
            text = io.StringIO(newline=""); csv.writer(text, lineterminator="\n").writerows(rows)
            data[record] = text.getvalue().encode("utf-8")
        stable = lock["wheel_equivalence"]["stable_members"][0]["path"]
        def witness_present(data):
            data[optional] = lock["manifest_build_input_sha256"].encode("ascii")
            with_rows(data, lambda rows: rows.append([optional, "sha256=" + base64.urlsafe_b64encode(hashlib.sha256(data[optional]).digest()).decode().rstrip("="), "64"]) if not any(v[0] == optional for v in rows) else None)
        base = deepcopy(original); witness_present(base)
        cases = {
            "changed stable bytes": lambda d: d.__setitem__(stable, d[stable] + b"x"),
            "missing stable member": lambda d: d.pop(stable),
            "extra unknown member": lambda d: d.__setitem__("unexpected.txt", b"extra"),
            "wrong witness value": lambda d: d.__setitem__(optional, b"0" * 64),
            "wrong witness size": lambda d: d.__setitem__(optional, d[optional] + b"\n"),
            "witness row without file": lambda d: d.pop(optional),
            "witness file without row": lambda d: with_rows(d, lambda rows: rows.__setitem__(slice(None), [v for v in rows if v[0] != optional])),
            "wrong RECORD hash": lambda d: with_rows(d, lambda rows: rows[0].__setitem__(1, "sha256=incorrect")),
            "wrong RECORD size": lambda d: with_rows(d, lambda rows: rows[0].__setitem__(2, "99999")),
            "duplicate RECORD row": lambda d: with_rows(d, lambda rows: rows.append(rows[0][:])),
            "nonexistent RECORD path": lambda d: with_rows(d, lambda rows: rows.append(["ghost", "sha256=absent", "0"])),
        }
        rejected = []
        for name, change in cases.items():
            with self.subTest(name=name):
                data = deepcopy(base); change(data); fixture = io.BytesIO()
                with zipfile.ZipFile(fixture, "w") as archive:
                    for path, value in data.items(): archive.writestr(path, value)
                with self.assertRaises(ValueError): verify_wheel_equivalence(fixture, lock)
                rejected.append(name)
        changed_lock = deepcopy(lock); changed_lock["wheel_equivalence"]["record"]["core_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "core identity"): verify_wheel_equivalence(reference, changed_lock)
        rejected.append("different RECORD core identity")
        self.assertEqual(sha(reference), original_hash)
        if os.environ.get("TRIOCTAGON_UI_EVIDENCE"): write_json(Path(os.environ["TRIOCTAGON_UI_EVIDENCE"]) / "kernel-equivalence-negative-tests.json", {"rejected": rejected, "accepted_archive_unchanged": True})


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
