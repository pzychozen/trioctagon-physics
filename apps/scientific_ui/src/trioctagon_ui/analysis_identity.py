"""Observed installed loader identity, independent of saved producer claims."""
from dataclasses import dataclass
import hashlib
from importlib import metadata
from importlib.util import find_spec
import json
from pathlib import Path
import sys
import zipfile


def analysis_lock():
    dist = metadata.distribution("trioctagon-scientific-ui")
    files = [p for p in dist.files or () if str(p).replace("\\", "/").endswith(
        "share/trioctagon-scientific-ui/analysis-artifact.lock.json")]
    if len(files) != 1:
        raise ValueError("Exactly one installed analysis lock is required")
    return json.loads(dist.locate_file(files[0]).read_bytes())


def verify_analysis_wheel(path, lock):
    path = Path(path)
    if path.name != lock["wheel_filename"] or hashlib.sha256(path.read_bytes()).hexdigest() != lock["wheel_sha256"]:
        raise ValueError("Approved analysis archive identity mismatch")
    with zipfile.ZipFile(path) as archive:
        expected = {row["path"]: row for row in lock["member_manifest"]}
        if len(archive.namelist()) != len(expected) or set(archive.namelist()) != set(expected):
            raise ValueError("Analysis archive member closure mismatch")
        for name, row in expected.items():
            data = archive.read(name)
            if len(data) != row["size"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
                raise ValueError("Analysis archive member mismatch: " + name)
    return lock["wheel_sha256"]


@dataclass(frozen=True)
class AnalysisLoaderIdentity:
    distribution: str
    version: str
    approved_archive_sha256: str
    source_commit: str
    installed_members: str = "MATCH_APPROVED_MANIFEST"
    producer_execution_verification: str = "UNAVAILABLE"
    windows_execution_binding: str = "NOT_PROVEN"


def verify_installed_analysis():
    """Check files before importing analysis; this is not B2 execution attestation.

    pip rewrites RECORD and adds its own installation metadata. All original
    members except RECORD are checked; the runtime package closure is exact.
    Certification installs this package with --no-compile.
    """
    lock = analysis_lock()
    dist = metadata.distribution(lock["distribution"])
    if dist.version != lock["version"]:
        raise ValueError("Installed analysis version differs from approved pin")
    files = tuple(dist.files or ())
    expected_code = set()
    for row in lock["member_manifest"]:
        name = row["path"]
        if name.endswith(".dist-info/RECORD"):
            continue
        if ".data/data/" in name:
            suffix = name.split(".data/data/", 1)[1]
            matches = [p for p in files if str(p).replace("\\", "/").endswith(suffix)]
            if len(matches) != 1:
                raise ValueError("Missing/ambiguous installed analysis resource: " + suffix)
            path = Path(dist.locate_file(matches[0]))
        else:
            path = Path(dist.locate_file(name))
        data = path.read_bytes()
        if len(data) != row["size"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
            raise ValueError("Installed analysis content mismatch: " + name)
        if name.startswith("trioctagon_analysis/"):
            expected_code.add(path.resolve())
    root = Path(dist.locate_file("trioctagon_analysis")).resolve()
    spec = find_spec("trioctagon_analysis")
    if spec is None or Path(spec.origin or "").resolve() != root / "__init__.py" or tuple(
            Path(p).resolve() for p in spec.submodule_search_locations or ()) != (root,):
        raise ValueError("Analysis import path differs from installed pin")
    if {p.resolve() for p in root.rglob("*") if p.is_file()} != expected_code:
        raise ValueError("Installed analysis runtime closure mismatch (including bytecode)")
    for name, module in tuple(sys.modules.items()):
        if name == "trioctagon_analysis" or name.startswith("trioctagon_analysis."):
            if Path(getattr(module, "__file__", "")).resolve() not in expected_code:
                raise ValueError("Analysis module origin differs from installed pin")
    return AnalysisLoaderIdentity(lock["distribution"], lock["version"],
        lock["wheel_sha256"], lock["source_commit"])
