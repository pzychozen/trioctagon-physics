"""Inert, bounded import and no-replacement copy. No scientific jobs here."""
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import stat
import sys
import tempfile

from .analysis_identity import AnalysisLoaderIdentity, verify_installed_analysis
from .historical_loading import LoadedHistoricalResult, LoadedHistoricalReceipt, parse_historical

MAX_INPUT_FILE_BYTES = 16 * 1024 * 1024
MAX_JSON_DEPTH = 32
MAX_LOADED_ANALYSIS_ARTIFACTS = 64
MAX_RETAINED_ANALYSIS_BYTES = 128 * 1024 * 1024
MAX_DISPLAY_DIAGNOSTIC_BYTES = 8 * 1024
MAX_RAW_TEXT_PREVIEW_BYTES = 1024 * 1024


def bounded_text(text, limit=MAX_DISPLAY_DIAGNOSTIC_BYTES):
    raw = str(text).encode("utf-8")
    marker = b"\n[UI preview truncated]"
    return (raw if len(raw) <= limit else raw[:limit-len(marker)].decode(
        "utf-8", errors="ignore").encode("utf-8") + marker).decode("utf-8")


def local_path(value, *, missing_leaf=False):
    path = Path(os.path.abspath(value))
    # Reject network paths, device namespace, ADS and remote mapped drives.
    if str(path).startswith(("\\\\", "//")) or ":" in str(path)[2:]:
        raise ValueError("Only local filesystem paths are supported")
    if os.name == "nt":
        import ctypes
        if ctypes.windll.kernel32.GetDriveTypeW(str(path.anchor)) != 3:
            raise ValueError("A local fixed drive is required")
    for part in (*reversed(path.parents), path):
        try:
            info = part.lstat()
        except FileNotFoundError:
            if missing_leaf and part == path:
                continue
            raise
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise ValueError("Reparse-point artifact paths are not supported")
    return path


def snapshot_file(value):
    path = local_path(value)
    before = path.stat()
    if not stat.S_ISREG(before.st_mode) or before.st_size > MAX_INPUT_FILE_BYTES:
        raise ValueError("Artifact must be a regular file of at most 16 MiB")
    signature = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
    with path.open("rb") as stream:
        opened = os.fstat(stream.fileno())
        if signature(before) != signature(opened):
            raise ValueError("Artifact changed while opening")
        raw = stream.read(MAX_INPUT_FILE_BYTES + 1)
        after = os.fstat(stream.fileno())
    local_path(path)
    if len(raw) > MAX_INPUT_FILE_BYTES or len(raw) != before.st_size or any(
        signature(s) != signature(before) for s in (after, path.stat())):
        raise ValueError("Artifact changed during bounded capture")
    return path, raw


@dataclass(frozen=True, slots=True)
class LoadedDerivedArtifact:
    document: object
    source: Path
    sha256: str
    loader: AnalysisLoaderIdentity
    external_expected_sha256: str | None = None
    external_identity_source: str | None = None

    @property
    def raw(self):
        return self.document.to_bytes()


@dataclass(frozen=True, slots=True)
class LoadedAttemptArtifact(LoadedDerivedArtifact):
    pass


@dataclass(frozen=True, slots=True)
class CoreArtifactCandidate:
    """A hint only: the existing Core loader must still validate these bytes."""
    family: str
    raw: bytes


class ArtifactLibrary:
    def __init__(self):
        self._items = []
        self.retained_bytes = 0

    @property
    def items(self):
        return tuple(self._items)

    def load(self, path, *, expected_sha256=None, identity_source=None):
        loader = verify_installed_analysis()
        # Avoid introducing bytecode outside the approved runtime member closure.
        previous = sys.dont_write_bytecode
        try:
            sys.dont_write_bytecode = True
            from trioctagon_analysis import probe_artifact_envelope
            from trioctagon_analysis.codec import ParseLimits
            from trioctagon_analysis.records import DerivedAnalysisRecord, AttemptReceipt
        finally:
            sys.dont_write_bytecode = previous
        verify_installed_analysis()  # imported origins must also match
        source, raw = snapshot_file(path)
        limits = ParseLimits(MAX_INPUT_FILE_BYTES, MAX_JSON_DEPTH)
        hint = probe_artifact_envelope(raw, limits)
        family = hint.family_hint.value
        if family in ("KERNEL_RUN_RECORD", "GEOMETRY_RECORD"):
            return CoreArtifactCandidate(family, raw)
        owners = {
            "TRIOCTAGON_DERIVED_ANALYSIS_RECORD": (DerivedAnalysisRecord, LoadedDerivedArtifact),
            "TRIOCTAGON_ANALYSIS_ATTEMPT_RECEIPT": (AttemptReceipt, LoadedAttemptArtifact),
        }
        # The public inert probe has already bounded nesting and rejected duplicate
        # keys, ambiguous envelopes and noncanonical number syntax. It intentionally
        # classifies Historical families as UNKNOWN; inspect only their literal
        # routing fields, then require the Historical owning parser. No fallback.
        envelope = json.loads(raw) if family == "UNKNOWN" else {}
        historical_family = envelope.get("family", "")
        if historical_family.startswith("TRIOCTAGON_HISTORICAL_"):
            document, handle, loader = parse_historical(raw, historical_family, envelope.get("schema"), limits)
        elif family not in owners:
            raise ValueError("UNKNOWN / UNSUPPORTED: no artifact loader for " + family)
        else:
            owner, handle = owners[family]
            document = owner.from_bytes(raw, limits)
        if raw != document.to_bytes():
            raise ValueError("NONCANONICAL_INPUT: accepted analysis bytes must already be canonical")
        digest = hashlib.sha256(raw).hexdigest()
        if expected_sha256 is not None:
            if not identity_source or expected_sha256 != digest:
                raise ValueError("EXTERNAL_IDENTITY_MISMATCH: independently supplied identity required")
        item = handle(document, source, digest, loader, expected_sha256, identity_source)
        for prior in self._items:
            if (type(prior), prior.sha256, prior.source, prior.external_expected_sha256, prior.external_identity_source) == (
                handle, digest, source, expected_sha256, identity_source):
                return prior
        if len(self._items) >= MAX_LOADED_ANALYSIS_ARTIFACTS or self.retained_bytes + len(raw) > MAX_RETAINED_ANALYSIS_BYTES:
            raise ValueError("VIEWER_RESOURCE_LIMIT: artifact session cache is full")
        self._items.append(item)
        self.retained_bytes += len(raw)
        return item


@dataclass(frozen=True, slots=True)
class CopyObservation:
    destination: str
    sha256: str
    bytes_written: int
    status: str = "LOCAL_UI_BYTE_COPY_VERIFIED"


def copy_artifact(item, destination):
    if type(item) not in (LoadedDerivedArtifact, LoadedAttemptArtifact, LoadedHistoricalResult, LoadedHistoricalReceipt):
        raise TypeError("Canonical copying requires an accepted analysis handle")
    path = local_path(destination, missing_leaf=True)
    if os.path.normcase(str(path)) == os.path.normcase(str(item.source)) or os.path.lexists(path):
        raise FileExistsError("Copy refuses source overwrite or any existing destination")
    raw = item.raw
    fd, staging = tempfile.mkstemp(prefix=".trioctagon-ui-copy-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        if hashlib.sha256(Path(staging).read_bytes()).hexdigest() != item.sha256:
            raise OSError("Staged copy SHA-256 mismatch")
        local_path(path, missing_leaf=True)
        # Same-filesystem hard-link publication fails atomically if the name exists.
        os.link(staging, path)
        if hashlib.sha256(path.read_bytes()).hexdigest() != item.sha256:
            raise OSError("Published copy SHA-256 mismatch")
        return CopyObservation(str(path), item.sha256, len(raw))
    finally:
        # Never remove someone else's destination, even after a publication error.
        Path(staging).unlink(missing_ok=True)
