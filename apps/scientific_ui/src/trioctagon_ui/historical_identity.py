"""Observed installed loader identity, independent of saved producer claims."""
from dataclasses import dataclass
import hashlib
from importlib import metadata
from importlib.util import find_spec
import json
from pathlib import Path
import sys
import zipfile


def historical_lock():
    dist = metadata.distribution("trioctagon-scientific-ui")
    files = [p for p in dist.files or () if str(p).replace("\\", "/").endswith(
        "share/trioctagon-scientific-ui/historical-protocol-artifact.lock.json")]
    if len(files) != 1:
        raise ValueError("Exactly one installed Historical protocol lock is required")
    return json.loads(dist.locate_file(files[0]).read_bytes())


def verify_historical_wheel(path, lock):
    path = Path(path)
    if path.name != lock["wheel_filename"] or hashlib.sha256(path.read_bytes()).hexdigest() != lock["wheel_sha256"]:
        raise ValueError("Approved Historical protocol archive identity mismatch")
    with zipfile.ZipFile(path) as archive:
        expected = {row["path"]: row for row in lock["member_manifest"]}
        if len(archive.namelist()) != len(expected) or set(archive.namelist()) != set(expected):
            raise ValueError("Historical protocol archive member closure mismatch")
        for name, row in expected.items():
            data = archive.read(name)
            if len(data) != row["size"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
                raise ValueError("Historical protocol archive member mismatch: " + name)
    return lock["wheel_sha256"]


@dataclass(frozen=True)
class HistoricalLoaderIdentity:
    distribution: str
    version: str
    approved_archive_sha256: str
    source_commit: str
    installed_members: str = "MATCH_APPROVED_MANIFEST"
    producer_execution_verification: str = "UNAVAILABLE"
    windows_execution_binding: str = "NOT_PROVEN"


def verify_installed_historical():
    """Check files before importing Historical protocol; this is not B2 execution attestation.

    pip rewrites RECORD and adds its own installation metadata. All original
    members except RECORD are checked; the runtime package closure is exact.
    Certification installs this package with --no-compile.
    """
    lock = historical_lock()
    dist = metadata.distribution(lock["distribution"])
    if dist.version != lock["version"]:
        raise ValueError("Installed Historical protocol version differs from approved pin")
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
                raise ValueError("Missing/ambiguous installed Historical protocol resource: " + suffix)
            path = Path(dist.locate_file(matches[0]))
        else:
            path = Path(dist.locate_file(name))
        data = path.read_bytes()
        if len(data) != row["size"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
            raise ValueError("Installed Historical protocol content mismatch: " + name)
        if name.startswith("trioctagon_historical_protocol/"):
            expected_code.add(path.resolve())
    root = Path(dist.locate_file("trioctagon_historical_protocol")).resolve()
    spec = find_spec("trioctagon_historical_protocol")
    if spec is None or Path(spec.origin or "").resolve() != root / "__init__.py" or tuple(
            Path(p).resolve() for p in spec.submodule_search_locations or ()) != (root,):
        raise ValueError("Historical protocol import path differs from installed pin")
    if {p.resolve() for p in root.rglob("*") if p.is_file()} != expected_code:
        raise ValueError("Installed Historical protocol runtime closure mismatch (including bytecode)")
    for name, module in tuple(sys.modules.items()):
        if name == "trioctagon_historical_protocol" or name.startswith("trioctagon_historical_protocol."):
            if Path(getattr(module, "__file__", "")).resolve() not in expected_code:
                raise ValueError("Historical protocol module origin differs from installed pin")
    return HistoricalLoaderIdentity(lock["distribution"], lock["version"],
        lock["wheel_sha256"], lock["source_commit"])
