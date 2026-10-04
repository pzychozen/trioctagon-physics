"""PEP 517 wrapper: clean source / provenance-bearing sdist -> external stage.

No runtime imports, science execution, dependency downloads or source writes.
Setuptools creates the archives. Every archive member is checked before return.
"""
import ast
from contextlib import contextmanager
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tarfile
import tempfile
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parent
MODULES = tuple(sorted("kernel_physics/" + n + ".py" for n in (
    "__init__", "api", "_contract_types", "_runner", "_records", "_geometry_records",
    "_presets", "dynamics", "readouts", "z_manifold", "z_diagnostics",
    "_response_numeric", "geometry", "reference_scaffold")))
PYTHON_FILES = tuple(sorted((*MODULES, *("kernel_physics/" + n + ".py" for n in
    ("covering", "face_state", "boundary_response", "srg", "operating_region", "axial_observables")))))
INPUTS = tuple(sorted((*PYTHON_FILES, "pyproject.toml", "_build_backend.py", "LICENSE",
                       "LICENSE_SCOPE.md", "kernel_physics/README.md")))
MANIFEST = "kernel_physics/_distribution_provenance.json"
APACHE_SHA256 = "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30"
BUILD_VERSIONS = {"setuptools": "81.0.0", "wheel": "0.47.0"}
DEPENDENCIES = ["numpy==2.4.4", "sympy==1.14.0", "mpmath==1.3.0"]
SCOPE_PHRASES = ("top-level kernel_physics", "pyproject.toml", "_build_backend.py",
    "tools/verify_distribution.py", "kernel_physics/tests/test_distribution_provenance.py",
    "kernel_physics/requirements.txt", "kernel_physics/README.md", "distribution metadata",
    "provenance metadata", "papers/", "research/", "research datasets", "figures",
    "publication manuscripts", "Twisted Hex Crystal", "fixtures/evidence", "golden_388",
    "Paper-F support", "historical scientific/publication", "separate explicit license")


def canonical(value):
    """Canonical UTF-8: sorted keys, compact separators, no nonfinite numbers."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def input_digest(manifest):
    return digest(canonical({k: v for k, v in manifest.items() if k != "build_input_sha256"}))


def parse(raw):
    def pairs(items):
        result = {}
        for k, v in items:
            if k in result:
                raise ValueError("duplicate manifest key")
            result[k] = v
        return result
    def invalid(value):
        raise ValueError("nonfinite manifest constant: " + value)
    return json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid)


def keys(value, expected):
    if not isinstance(value, dict) or set(value) != set(expected):
        raise ValueError("unexpected or missing provenance fields")


def read_inputs(root):
    result = {}
    for path in INPUTS:
        target = root / path
        if target.is_symlink() or not target.is_file() or not target.resolve().is_relative_to(root.resolve()):
            raise ValueError("missing/nonregular build input: " + path)
        result[path] = target.read_bytes()
    return result


def definitions(inputs):
    """Read frozen definitions statically; builds do not need NumPy/SymPy."""
    def assignment(path, name):
        tree = ast.parse(inputs[path].decode("utf-8-sig"))
        return next(n.value for n in tree.body if isinstance(n, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == name for t in n.targets))
    package_version = ast.literal_eval(assignment("kernel_physics/__init__.py", "__version__"))
    api_version = ast.literal_eval(assignment("kernel_physics/_records.py", "_VERSION"))
    papers = ast.literal_eval(assignment("kernel_physics/_records.py", "_PAPERS"))
    # _MODULES is a sorted generator over a literal tuple of module stems.
    expr = assignment("kernel_physics/_records.py", "_MODULES")
    stems = ast.literal_eval(expr.args[0].args[0].generators[0].iter)
    if tuple(sorted("kernel_physics/" + n + ".py" for n in stems)) != MODULES:
        raise ValueError("frozen 14-path identity changed")
    for path in ("kernel_physics/_runner.py", "kernel_physics/_geometry_records.py"):
        found = {}
        for node in ast.walk(ast.parse(inputs[path].decode("utf-8-sig"))):
            if isinstance(node, ast.Dict):
                for k, v in zip(node.keys, node.values):
                    if isinstance(k, ast.Constant) and k.value in ("schema_version", "api_version", "ledger_version"):
                        found.setdefault(k.value, set()).add(ast.literal_eval(v))
        if found != {"schema_version": {api_version}, "api_version": {api_version}, "ledger_version": {"0.1"}}:
            raise ValueError("source schema/version definitions changed")
    if api_version != "1.0.0" or set(papers) != set("ABCDEF"):
        raise ValueError("unsupported source definitions")
    return {"package_version": package_version, "api_version": api_version,
            "run_record_schema_version": api_version, "geometry_record_schema_version": api_version,
            "ledger_version": "0.1"}, papers


def validate_project(inputs):
    data = tomllib.loads(inputs["pyproject.toml"].decode("utf-8"))
    project = data["project"]
    expected = {"name": "trioctagon-physics", "dynamic": ["version"],
        "readme": "kernel_physics/README.md", "requires-python": ">=3.11,<3.12",
        "license": "Apache-2.0", "license-files": ["LICENSE", "LICENSE_SCOPE.md"],
        "authors": [{"name": "Hilmir Frímann Halldórsson"}], "dependencies": DEPENDENCIES,
        "urls": {"Source": "https://github.com/pzychozen/trioctagon-physics"}}
    keys(project, (*expected, "description"))
    if any(project[k] != v for k, v in expected.items()):
        raise ValueError("project metadata differs from K3 authority")
    if data["build-system"] != {"requires": ["setuptools==81.0.0", "wheel==0.47.0"],
                                "build-backend": "_build_backend", "backend-path": ["."]}:
        raise ValueError("unapproved build system")
    if data["tool"] != {"setuptools": {"packages": ["kernel_physics"], "include-package-data": False,
        "dynamic": {"version": {"attr": "kernel_physics.__version__"}},
        "package-data": {"kernel_physics": ["_distribution_provenance.json"]}}}:
        raise ValueError("unapproved package enumeration/data")
    keys(data, ("build-system", "project", "tool"))
    if digest(inputs["LICENSE"]) != APACHE_SHA256:
        raise ValueError("LICENSE must match the unmodified Apache-2.0 standard text")
    scope = " ".join(inputs["LICENSE_SCOPE.md"].decode("utf-8").split())
    if any(s not in scope for s in SCOPE_PHRASES) or "Not automatically covered" not in scope:
        raise ValueError("incomplete software license scope notice")


def validate_manifest(data, inputs):
    """Strict build-side validation, including all 20 files and build inputs.

    Runtime's smaller validator in _records checks the same schema and the 14
    identity files; it cannot require build tools or paper files in a wheel.
    """
    keys(data, ("manifest_type", "manifest_version", "source", "software", "modules", "papers", "build", "build_input_sha256"))
    if data["manifest_type"] != "TRIOCTAGON_DISTRIBUTION_PROVENANCE" or data["manifest_version"] != "1":
        raise ValueError("unsupported manifest type/version")
    source = data["source"]
    keys(source, ("repository", "commit", "tracked_dirty"))
    if not isinstance(source["repository"], str) or not source["repository"]:
        raise ValueError("missing repository identity")
    if not isinstance(source["commit"], str) or re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", source["commit"]) is None:
        raise ValueError("invalid commit identity")
    if source["tracked_dirty"] is not False:
        raise ValueError("dirty source attestation")
    software, papers = definitions(inputs)
    if data["software"] != software:
        raise ValueError("software identity mismatch")
    def hashes(entries, paths):
        if not isinstance(entries, list) or len(entries) != len(paths):
            raise ValueError("file set mismatch")
        for row, path in zip(entries, paths):
            keys(row, ("path", "sha256"))
            if row["path"] != path or row["sha256"] != digest(inputs[path]):
                raise ValueError("source byte identity/set/order mismatch: " + path)
    hashes(data["modules"], MODULES)
    refs = data["papers"]
    if not isinstance(refs, list) or len(refs) != 6:
        raise ValueError("paper set mismatch")
    for row, k in zip(refs, sorted(papers)):
        keys(row, ("source_id", "edition", "path", "sha256"))
        if (row["source_id"], row["edition"], row["path"]) != ("P" + k, *papers[k]):
            raise ValueError("paper identity/set/order mismatch")
        if not isinstance(row["sha256"], str) or re.fullmatch(r"[0-9a-f]{64}", row["sha256"]) is None:
            raise ValueError("malformed paper SHA-256")
    keys(data["build"], ("backend", "setuptools", "wheel", "files"))
    if {k: v for k, v in data["build"].items() if k != "files"} != {"backend": "_build_backend", **BUILD_VERSIONS}:
        raise ValueError("unapproved build facts")
    hashes(data["build"]["files"], INPUTS)
    if data["build_input_sha256"] != input_digest(data):
        raise ValueError("manifest canonical digest mismatch")
    return data


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.PIPE)


def exact_source(root):
    try:
        return Path(git(root, "rev-parse", "--show-toplevel").decode().strip()).resolve() == root.resolve()
    except (OSError, subprocess.CalledProcessError):
        if (root / ".git").exists():
            raise ValueError("broken source checkout; manifest fallback forbidden")
        return False


def capture(root=ROOT):
    root = Path(root).resolve()
    inputs = read_inputs(root)
    validate_project(inputs)
    software, papers = definitions(inputs)
    if exact_source(root):
        commit = git(root, "rev-parse", "HEAD^{commit}").decode().strip()
        repository = git(root, "remote", "get-url", "origin").decode().strip()
        tracked = set(git(root, "ls-files", "-z").decode().split("\0"))
        required = {*INPUTS, *(v[1] for v in papers.values())}
        if not required <= tracked or git(root, "status", "--porcelain", "--untracked-files=no").strip():
            raise ValueError("build requires a clean complete tracked source checkout")
        for path in INPUTS:
            if git(root, "cat-file", "blob", commit + ":" + path) != inputs[path]:
                raise ValueError("Git blob differs from checked-out input: " + path)
        refs = []
        for k, (edition, path) in sorted(papers.items()):
            raw = (root / path).read_bytes()
            if git(root, "cat-file", "blob", commit + ":" + path) != raw:
                raise ValueError("paper source differs from captured commit")
            refs.append({"source_id": "P" + k, "edition": edition, "path": path, "sha256": digest(raw)})
        data = {"manifest_type": "TRIOCTAGON_DISTRIBUTION_PROVENANCE", "manifest_version": "1",
            "source": {"repository": repository, "commit": commit, "tracked_dirty": False},
            "software": software, "modules": [{"path": p, "sha256": digest(inputs[p])} for p in MODULES],
            "papers": refs, "build": {"backend": "_build_backend", **BUILD_VERSIONS,
            "files": [{"path": p, "sha256": digest(inputs[p])} for p in INPUTS]}}
        data["build_input_sha256"] = input_digest(data)
        if git(root, "rev-parse", "HEAD").decode().strip() != commit or git(root, "status", "--porcelain", "--untracked-files=no").strip():
            raise ValueError("source changed during provenance capture")
    else:
        data = parse((root / MANIFEST).read_bytes())
    validate_manifest(data, inputs)
    return inputs, data


def metadata_names(package_version):
    stem = "trioctagon_physics-" + package_version
    return stem + ".dist-info", "trioctagon_physics.egg-info", stem


def archive_contents(path, inputs, manifest):
    """Verify exact archive allowlists and raw source bytes; never extract."""
    path = Path(path)
    info, egg, stem = metadata_names(manifest["software"]["package_version"])
    if path.suffix == ".whl":
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)):
                raise ValueError("duplicate wheel members")
            if any(n.endswith("/") for n in names) or any(
                    stat.S_ISLNK(m.external_attr >> 16) for m in archive.infolist()):
                raise ValueError("unexpected wheel directory/link member")
            contents = {n: archive.read(n) for n in names if not n.endswith("/")}
        expected = {*PYTHON_FILES, MANIFEST, *(info + "/" + p for p in
            ("METADATA", "WHEEL", "RECORD", "top_level.txt", "licenses/LICENSE", "licenses/LICENSE_SCOPE.md"))}
        # PEP 517 permits private prepared metadata, which must be preserved.
        optional = {info + "/build_input.sha256"}
    else:
        with tarfile.open(path, "r:gz") as archive:
            members = archive.getmembers()
            names = [m.name for m in members]
            if len(names) != len(set(names)) or any(not (m.isfile() or m.isdir()) for m in members):
                raise ValueError("unsafe/duplicate sdist members")
            if any(n != stem and not n.startswith(stem + "/") for n in names):
                raise ValueError("unexpected sdist root")
            if any(m.isdir() and m.name not in (stem, stem + "/kernel_physics", stem + "/" + egg)
                   for m in members):
                raise ValueError("unexpected sdist directory")
            contents = {m.name[len(stem)+1:]: archive.extractfile(m).read() for m in members if m.isfile()}
        expected = {*INPUTS, MANIFEST, "PKG-INFO", "setup.cfg", *(egg + "/" + p for p in
            ("PKG-INFO", "SOURCES.txt", "dependency_links.txt", "requires.txt", "top_level.txt"))}
        optional = set()
    if not expected <= contents.keys() or contents.keys() - expected - optional:
        raise ValueError(f"artifact content mismatch: missing={sorted(expected-contents.keys())}, extra={sorted(contents.keys()-expected-optional)}")
    for name in PYTHON_FILES:
        if contents[name] != inputs[name]:
            raise ValueError("artifact changed Python bytes: " + name)
    if path.suffix != ".whl":
        for name in INPUTS:
            if contents[name] != inputs[name]:
                raise ValueError("sdist changed input bytes: " + name)
    if contents[MANIFEST] != canonical(manifest):
        raise ValueError("artifact changed manifest")
    return contents


def destination(path):
    result = Path(path).resolve()
    if result.is_relative_to(ROOT):
        raise ValueError("build output/metadata must be outside the source tree")
    result.mkdir(parents=True, exist_ok=True)
    return result


@contextmanager
def staged():
    inputs, manifest = capture()
    for name, required in BUILD_VERSIONS.items():
        if version(name) != required:
            raise ValueError("unapproved build dependency: " + name)
    with tempfile.TemporaryDirectory(prefix="trioctagon-build-") as temp:
        stage = Path(temp)
        if stage.is_relative_to(ROOT):
            raise ValueError("temporary stage must be external")
        for name, raw in {**inputs, MANIFEST: canonical(manifest)}.items():
            target = stage / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        if read_inputs(stage) != inputs:
            raise ValueError("staging changed source bytes")
        # A staging-only manifest tells Setuptools to include the in-tree backend
        # in sdist. It is excluded from the archive and never touches source.
        (stage / "MANIFEST.in").write_text("include _build_backend.py\nexclude MANIFEST.in\n", encoding="utf-8")
        cwd, argv = Path.cwd(), sys.argv[:]
        try:
            os.chdir(stage)
            from setuptools import build_meta
            yield build_meta, inputs, manifest
        finally:
            os.chdir(cwd)
            sys.argv[:] = argv


def _settings(config_settings):
    if config_settings:
        raise ValueError("custom Setuptools build arguments are outside the frozen build contract")


def get_requires_for_build_wheel(config_settings=None):
    _settings(config_settings)
    with staged() as (backend, _, _):
        return backend.get_requires_for_build_wheel(config_settings)


def get_requires_for_build_sdist(config_settings=None):
    _settings(config_settings)
    with staged() as (backend, _, _):
        return backend.get_requires_for_build_sdist(config_settings)


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    _settings(config_settings)
    target = destination(metadata_directory)
    with staged() as (backend, _, manifest):
        name = backend.prepare_metadata_for_build_wheel(str(target), config_settings)
        (target / name / "build_input.sha256").write_bytes(manifest["build_input_sha256"].encode("ascii"))
        return name


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _settings(config_settings)
    target = destination(wheel_directory)
    metadata = None if metadata_directory is None else Path(metadata_directory).resolve()
    with staged() as (backend, inputs, manifest):
        prepared = {}
        if metadata is not None:
            if metadata.is_relative_to(ROOT):
                raise ValueError("prepared metadata must be external")
            if metadata.suffix != ".dist-info":
                metadata = metadata / metadata_names(manifest["software"]["package_version"])[0]
            if (metadata / "build_input.sha256").read_bytes() != manifest["build_input_sha256"].encode("ascii"):
                raise ValueError("source identity changed since metadata preparation")
            prepared = {p.relative_to(metadata).as_posix(): p.read_bytes() for p in metadata.rglob("*") if p.is_file()}
        name = backend.build_wheel(str(target), config_settings, None if metadata is None else str(metadata))
        contents = archive_contents(target / name, inputs, manifest)
        info = metadata_names(manifest["software"]["package_version"])[0]
        if any(contents.get(info + "/" + p) != raw for p, raw in prepared.items()):
            raise ValueError("wheel changed prepared metadata")
        return name


def build_sdist(sdist_directory, config_settings=None):
    _settings(config_settings)
    target = destination(sdist_directory)
    with staged() as (backend, inputs, manifest):
        name = backend.build_sdist(str(target), config_settings)
        archive_contents(target / name, inputs, manifest)
        return name
