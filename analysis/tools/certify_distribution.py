"""Windows distribution certification tooling; never a runtime attestor.

Acquisition may use the network. Certification builds and tests offline outside
the checkout. --precommit records a candidate, never a certified source commit.
"""
import argparse
import base64
import csv
from email.parser import BytesParser
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import tomllib
import zipfile

MODULES = frozenset(("__init__ approval attestation b2a_proof b2a_snapshot b2a_windows b2a_worker "
    "catalogue codec common constants coordinator digests envelope errors persistence provider records requests schema").split())
DOCUMENTS = ("SPECIFICATION.md", "RESOURCE_LIMIT_PROPOSAL.md", "CONFORMANCE.md",
             "B2A_WINDOWS_PROOF.md", "B2A_CONFORMANCE.md", "tests/fixtures/golden_vectors.json")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def git(source, *args):
    return subprocess.check_output(["git", "--no-optional-locks", "-C", str(source), *args])


def run(log, args, cwd, env):
    result = subprocess.run([str(a) for a in args], cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    log.write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(f"{log.name} failed ({result.returncode}):\n" + (result.stdout + result.stderr)[-6000:])


def verify_kernel(path, lock):
    if path.name != lock["filename"] or sha(path.read_bytes()) != lock["sha256"]:
        raise ValueError("Core test artifact does not match the independent exact pin")
    with zipfile.ZipFile(path) as archive:
        manifest = json.loads(archive.read("kernel_physics/_distribution_provenance.json"))
    assert manifest["source"]["commit"] == lock["source_commit"]
    assert manifest["software"]["package_version"] == lock["version"]


def acquire(source, workspace, kernel_path):
    lock_path = source / "analysis/requirements-certification-win-py311.lock"
    wheels = workspace / "dependencies"
    wheels.mkdir()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PIP_DISABLE_PIP_VERSION_CHECK="1")
    env.pop("PYTHONPATH", None)
    run(workspace / "acquisition.log", [sys.executable, "-I", "-B", "-m", "pip", "download",
        "--only-binary=:all:", "--no-deps", "--require-hashes", "-r", lock_path, "--dest", wheels], workspace, env)
    kernel_lock = json.loads((source / "analysis/tools/kernel-test-artifact.lock.json").read_bytes())
    target = workspace / kernel_lock["filename"]
    if kernel_path:
        verify_kernel(kernel_path, kernel_lock)
        shutil.copyfile(kernel_path, target)
        origin = "EXPLICIT_LOCAL_EXACT_ARCHIVE"
    else:
        result = subprocess.run(["gh", "api", f"repos/{kernel_lock['repository']}/actions/artifacts/{kernel_lock['artifact_id']}/zip"],
                                capture_output=True, check=True)
        assert sha(result.stdout) == kernel_lock["artifact_zip_sha256"], "Core certification ZIP identity mismatch"
        with zipfile.ZipFile(io.BytesIO(result.stdout)) as archive:
            target.write_bytes(archive.read(kernel_lock["wheel_path"]))
        origin = "PINNED_CERTIFICATION_ARCHIVE"
    verify_kernel(target, kernel_lock)
    write_json(workspace / "acquisition.json", {"status": "PASS", "origin": origin,
        "requirements_sha256": sha(lock_path.read_bytes()), "kernel": kernel_lock,
        "dependencies": [{"filename": p.name, "sha256": sha(p.read_bytes())} for p in sorted(wheels.glob("*.whl"))]})


def verify_wheel(wheel, copied):
    stem = "trioctagon_analysis-0.1.1"
    metadata = stem + ".dist-info/"
    expected = {"trioctagon_analysis/" + name + ".py": copied / "src/trioctagon_analysis" / (name + ".py") for name in MODULES}
    expected.update({stem + ".data/data/share/trioctagon-analysis/" + Path(name).name: copied / name for name in DOCUMENTS})
    expected.update({metadata + "licenses/" + name: copied / name for name in ("LICENSE", "LICENSE_SCOPE.md")})
    generated = {metadata + name for name in ("METADATA", "WHEEL", "top_level.txt", "RECORD")}
    with zipfile.ZipFile(wheel) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert set(names) == set(expected) | generated, "unexpected wheel package/member closure"
        for name, path in expected.items():
            assert archive.read(name) == path.read_bytes(), name
        meta = BytesParser().parsebytes(archive.read(metadata + "METADATA"))
        assert (meta["Name"], meta["Version"]) == ("trioctagon-analysis", "0.1.1")
        assert not meta.get_all("Requires-Dist")
        assert set(meta["Requires-Python"].split(",")) == {">=3.11", "<3.12"}
        assert archive.read(metadata + "top_level.txt") == b"trioctagon_analysis\n"
        rows = list(csv.reader(io.StringIO(archive.read(metadata + "RECORD").decode())))
        assert len(rows) == len(names) and {r[0] for r in rows} == set(names)
        for name, digest, size in rows:
            if name == metadata + "RECORD":
                assert digest == size == ""
            else:
                data = archive.read(name)
                assert int(size) == len(data)
                assert digest == "sha256=" + base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode()
        return [{"path": name, "size": len(archive.read(name)), "sha256": sha(archive.read(name))} for name in sorted(names)]


def certify(source, workspace, precommit):
    if os.environ.get("GITHUB_ACTIONS") and precommit:
        raise ValueError("CI cannot certify a precommit candidate")
    before = git(source, "status", "--porcelain", "--untracked-files=all")
    tracked_status = git(source, "status", "--porcelain", "--untracked-files=no")
    if not precommit and tracked_status.strip():
        raise ValueError("Certification requires a clean tracked checkout")
    if os.environ.get("GITHUB_ACTIONS") and before.strip():
        raise ValueError("CI requires a completely clean checkout")
    tracked = git(source, "ls-files", "-z").decode().split("\0")[:-1]
    before_hashes = {name: sha((source / name).read_bytes()) for name in tracked}
    head = git(source, "rev-parse", "HEAD").decode().strip()
    tree = git(source, "rev-parse", "HEAD^{tree}").decode().strip()
    analysis_tree = git(source, "rev-parse", "HEAD:analysis").decode().strip()
    work = workspace / ("candidate" if precommit else "certified")
    work.mkdir()
    evidence = work / "evidence"
    evidence.mkdir()
    copied = work / "analysis-source"
    for name in tracked:
        if name.startswith("analysis/"):
            path = copied / name.removeprefix("analysis/")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((source / name).read_bytes() if precommit else git(source, "show", head + ":" + name))
    inputs = {p.relative_to(copied).as_posix(): sha(p.read_bytes()) for p in sorted(copied.rglob("*")) if p.is_file()}
    source_content = sha(json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode())
    metadata = tomllib.loads((copied / "pyproject.toml").read_text())
    assert metadata["project"]["version"] == "0.1.1"
    assert set(p.stem for p in (copied / "src/trioctagon_analysis").glob("*.py")) == MODULES
    kernel_lock = json.loads((copied / "tools/kernel-test-artifact.lock.json").read_bytes())
    kernel = workspace / kernel_lock["filename"]
    verify_kernel(kernel, kernel_lock)
    acquisition = json.loads((workspace / "acquisition.json").read_bytes())
    lock = copied / "requirements-certification-win-py311.lock"
    assert acquisition["requirements_sha256"] == sha(lock.read_bytes())
    dependencies = workspace / "dependencies"
    assert {p.name for p in dependencies.iterdir()} == {row["filename"] for row in acquisition["dependencies"]}
    for row in acquisition["dependencies"]:
        assert sha((dependencies / row["filename"]).read_bytes()) == row["sha256"]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1", PIP_NO_INDEX="1",
        PIP_DISABLE_PIP_VERSION_CHECK="1", PYTEST_DISABLE_PLUGIN_AUTOLOAD="1",
        SOURCE_DATE_EPOCH=git(source, "show", "-s", "--format=%ct", head).decode().strip())
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)
    interpreters = {}
    for lane in ("build", "runtime"):
        prefix = work / lane
        run(evidence / (lane + "-venv.log"), [sys.executable, "-I", "-B", "-m", "venv", prefix], work, env)
        python = prefix / "Scripts/python.exe"
        interpreters[lane] = python
        run(evidence / (lane + "-dependencies.log"), [python, "-I", "-B", "-m", "pip", "install",
            "--no-index", "--no-compile", "--require-hashes", "--find-links", dependencies, "-r", lock], work, env)
    wheel_dir = evidence / "wheel"
    wheel_dir.mkdir()
    run(evidence / "build.log", [interpreters["build"], "-I", "-B", "-m", "pip", "wheel",
        "--no-index", "--no-deps", "--no-build-isolation", "--wheel-dir", wheel_dir, copied], work, env)
    wheels = list(wheel_dir.glob("*.whl"))
    assert len(wheels) == 1 and wheels[0].name == "trioctagon_analysis-0.1.1-py3-none-any.whl"
    wheel = wheels[0]
    members = verify_wheel(wheel, copied)
    write_json(evidence / "member-manifest.json", members)
    run(evidence / "install.log", [interpreters["runtime"], "-I", "-B", "-m", "pip", "install",
        "--no-index", "--no-deps", "--no-compile", wheel, kernel], work, env)
    run(evidence / "pip-check.log", [interpreters["runtime"], "-I", "-B", "-m", "pip", "check"], work, env)
    tests = work / "installed-tests"
    shutil.copytree(copied / "tests", tests)
    runtime_check = work / "run_installed.py"
    shutil.copyfile(copied / "tools/run_installed.py", runtime_check)
    expected = {"source": str(source), "analysis_source": str(copied), "wheel": str(wheel),
        "members": members, "kernel": str(kernel), "tests": str(tests), "evidence": str(evidence)}
    write_json(work / "expected.json", expected)
    empty = work / "empty"
    empty.mkdir()
    run(evidence / "installed-tests.log", [interpreters["runtime"], "-I", "-B", runtime_check, work / "expected.json"], empty, env)
    assert git(source, "status", "--porcelain", "--untracked-files=all") == before
    assert {name: sha((source / name).read_bytes()) for name in tracked} == before_hashes
    run(evidence / "diff-check.log", ["git", "--no-optional-locks", "-C", source, "diff", "--check"], work, env)
    installed = json.loads((evidence / "installed-result.json").read_bytes())
    result = {"status": "PRECOMMIT_PASS" if precommit else "PASS", "distribution": "trioctagon-analysis", "version": "0.1.1",
        "wheel_filename": wheel.name, "wheel_sha256": sha(wheel.read_bytes()),
        "source_commit": None if precommit else head, "baseline_head": head, "git_tree": tree,
        "analysis_git_tree": analysis_tree, "source_content_sha256": source_content, "source_files": inputs,
        "build_inputs": {"python": sys.version, "requirements_sha256": sha(lock.read_bytes()),
            "wheels": acquisition["dependencies"], "build_system": metadata["build-system"], "source_date_epoch": env["SOURCE_DATE_EPOCH"]},
        "member_manifest_sha256": sha((evidence / "member-manifest.json").read_bytes()), "installed_test_result": installed,
        "kernel_test_artifact": kernel_lock, "ci_run": ("https://github.com/" + os.environ["GITHUB_REPOSITORY"] + "/actions/runs/" + os.environ["GITHUB_RUN_ID"]) if os.environ.get("GITHUB_RUN_ID") else None,
        "checkout_unchanged": True, "windows_execution_binding": "NOT_PROVEN", "production_attestation_enabled": False,
        "ready_for_b2b": False, "qualification": "DISTRIBUTION_CERTIFICATION_ONLY_NOT_PRODUCER_EXECUTION_ATTESTATION"}
    write_json(evidence / "certification.json", result)
    print(json.dumps({key: result[key] for key in ("status", "wheel_filename", "wheel_sha256", "source_commit", "ci_run")}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--acquire", action="store_true")
    mode.add_argument("--certify", action="store_true")
    parser.add_argument("--kernel-wheel", type=Path)
    parser.add_argument("--precommit", action="store_true")
    args = parser.parse_args()
    assert sys.platform == "win32" and sys.version_info[:2] == (3, 11) and struct.calcsize("P") == 8
    source, workspace = args.source.resolve(), args.workspace.resolve()
    if workspace == source or workspace.is_relative_to(source):
        raise ValueError("Certification workspace must be outside the checkout")
    workspace.mkdir(parents=True, exist_ok=True)
    if args.acquire:
        acquire(source, workspace, args.kernel_wheel)
    else:
        certify(source, workspace, args.precommit)


if __name__ == "__main__":
    main()
