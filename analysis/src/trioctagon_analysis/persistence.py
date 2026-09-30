"""One-file content addressing on local Windows NTFS; no replacement fallback."""
from dataclasses import dataclass
import ctypes
from ctypes import wintypes
import os
from pathlib import Path
import stat
import tempfile

from .digests import FullArtifactDigest, byte_digest, require_digest
from .errors import ProtocolError, require
from .records import DerivedAnalysisRecord

@dataclass(frozen=True, slots=True)
class StoredArtifact:
    path: Path
    digest: FullArtifactDigest
    reused: bool

def _ntfs_directory(directory):
    require(os.name == "nt", "PERSISTENCE_FAILURE", "B1 publication is qualified only on Windows NTFS")
    directory = Path(directory).absolute()
    require(directory.is_dir(), "PERSISTENCE_FAILURE", "existing application-owned directory required")
    for path in (directory, *directory.parents):
        info = path.lstat()
        require(not (getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT),
                "PERSISTENCE_FAILURE", "reparse-point publication directory prohibited")
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    get_path = kernel.GetVolumePathNameW
    get_path.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD]
    get_path.restype = wintypes.BOOL
    volume = ctypes.create_unicode_buffer(32768)
    if not get_path(str(directory), volume, len(volume)):
        raise ctypes.WinError(ctypes.get_last_error())
    get_type = kernel.GetDriveTypeW
    get_type.argtypes = [wintypes.LPCWSTR]
    get_type.restype = wintypes.UINT
    require(get_type(volume.value) == 3, "PERSISTENCE_FAILURE", "local fixed volume required")
    get_info = kernel.GetVolumeInformationW
    get_info.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD,
                        ctypes.POINTER(wintypes.DWORD), ctypes.POINTER(wintypes.DWORD),
                        ctypes.POINTER(wintypes.DWORD), wintypes.LPWSTR, wintypes.DWORD]
    get_info.restype = wintypes.BOOL
    filesystem = ctypes.create_unicode_buffer(256)
    if not get_info(volume.value, None, 0, None, None, None, filesystem, len(filesystem)):
        raise ctypes.WinError(ctypes.get_last_error())
    require(filesystem.value == "NTFS", "PERSISTENCE_FAILURE", "unqualified filesystem; no weaker fallback")
    return directory

def _rename_noreplace(source, destination):
    move = ctypes.WinDLL("kernel32", use_last_error=True).MoveFileExW
    move.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.DWORD]
    move.restype = wintypes.BOOL
    # WRITE_THROUGH only: never REPLACE_EXISTING, COPY_ALLOWED, or delayed reboot.
    if not move(str(source), str(destination), 0x8):
        raise ctypes.WinError(ctypes.get_last_error())

def _existing_matches(path, raw, expected):
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and not
            (getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT),
            "PERSISTENCE_FAILURE", "existing artifact is not a regular non-reparse file")
    require(info.st_size == len(raw), "PERSISTENCE_FAILURE", "existing artifact size differs")
    existing = path.read_bytes()
    require(byte_digest(FullArtifactDigest, existing) == expected and existing == raw,
            "PERSISTENCE_FAILURE", "content-address collision/corruption; existing bytes preserved")

def persist_record(record, directory):
    """Persist an inert record claim; this does not verify its producer evidence."""
    require(type(record) is DerivedAnalysisRecord, "INVALID_SCHEMA", "DerivedAnalysisRecord required")
    directory = _ntfs_directory(directory)
    raw = record.to_bytes()
    require(len(raw) <= record.data["catalogue"]["descriptors"][0]["resource_policy"]["limits"]["output_bytes"],
            "RESOURCE_LIMIT", "complete artifact exceeds its declared output limit")
    identity = byte_digest(FullArtifactDigest, raw)
    destination = directory / ("sha256-" + identity.sha256 + ".json")
    fd, temporary = tempfile.mkstemp(prefix=".analysis-", suffix=".tmp", dir=directory)
    temporary = Path(temporary)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            _rename_noreplace(temporary, destination)
        except FileExistsError:
            _existing_matches(destination, raw, identity)
            return StoredArtifact(destination, identity, True)
        _existing_matches(destination, raw, identity)
        return StoredArtifact(destination, identity, False)
    except OSError as exc:
        raise ProtocolError("PERSISTENCE_FAILURE", "publication failed; no replacement attempted") from exc
    finally:
        # Only our exact staging path is removed. Never remove an existing destination.
        temporary.unlink(missing_ok=True)

def load_record(path, expected_digest, limits):
    require_digest(expected_digest, FullArtifactDigest)
    path = Path(path)
    require(path.name == "sha256-" + expected_digest.sha256 + ".json",
            "PERSISTENCE_FAILURE", "content-addressed filename mismatch")
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and not
            (getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)),
            "PERSISTENCE_FAILURE", "regular artifact required")
    require(info.st_size <= limits.max_bytes, "RESOURCE_LIMIT", "artifact byte limit")
    with path.open("rb") as stream:
        raw = stream.read(limits.max_bytes + 1)
    require(len(raw) <= limits.max_bytes, "RESOURCE_LIMIT", "artifact grew beyond byte limit")
    require(byte_digest(FullArtifactDigest, raw) == expected_digest,
            "PERSISTENCE_FAILURE", "artifact bytes do not match external full digest")
    record = DerivedAnalysisRecord.from_bytes(raw, limits)
    require(record.to_bytes() == raw, "INVALID_CODEC", "stored artifact must be canonical bytes")
    return record
