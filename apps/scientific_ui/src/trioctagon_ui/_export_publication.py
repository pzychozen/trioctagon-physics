"""Windows destination-parent publication, with ownership retained by file handle.

No ACL edits, hard links or private staging directories. Each rename refuses an
existing name. A pair is two renames, NOT a two-name atomic transaction: consumers
must validate its provenance/hash. A process crash can leave a scratch file or
one pair member. On a handled failure we delete only our open file objects.
"""
import ctypes
from ctypes import wintypes as w
from contextlib import contextmanager
import io
import os
from pathlib import Path
import secrets


class _RenameInfo(ctypes.Structure):
    _fields_ = [("ReplaceIfExists", w.BOOL), ("RootDirectory", w.HANDLE),
                ("FileNameLength", w.DWORD), ("FileName", w.WCHAR * 1)]


def _api():
    if os.name != "nt":
        raise OSError("Export publication requires the certified Windows filesystem lane")
    api = ctypes.WinDLL("kernel32", use_last_error=True)
    api.CreateFileW.argtypes = [w.LPCWSTR, w.DWORD, w.DWORD, ctypes.c_void_p, w.DWORD, w.DWORD, w.HANDLE]
    api.CreateFileW.restype = w.HANDLE
    api.SetFileInformationByHandle.argtypes = [w.HANDLE, ctypes.c_int, ctypes.c_void_p, w.DWORD]
    api.SetFileInformationByHandle.restype = w.BOOL
    api.CloseHandle.argtypes = [w.HANDLE]
    return api


class _OwnedFile:
    def __init__(self, destination):
        import msvcrt
        self.destination = Path(destination).resolve()
        self.api = _api()
        # NULL security attributes: inherit the actual destination parent's ACL.
        # CREATE_NEW is exclusive. The handle denies other writers/deleters until
        # completion, including the interval between primary and sidecar rename.
        for _ in range(16):
            self.path = self.destination.parent / (".trioctagon-" + secrets.token_hex(16) + ".tmp")
            handle = self.api.CreateFileW(str(self.path), 0xC0010000, 1, None, 1, 0x80, None)
            if handle != ctypes.c_void_p(-1).value:
                break
            error = ctypes.get_last_error()
            if error not in (80, 183): raise ctypes.WinError(error)
        else:
            raise FileExistsError("Could not reserve an exclusive export temporary file")
        try:
            fd = msvcrt.open_osfhandle(handle, os.O_RDWR | os.O_BINARY)
        except BaseException as failure:
            try: self._discard_handle(handle)
            except OSError as error:
                raise OSError(f"Export cleanup incomplete; owned scratch {self.path}: {error}") from failure
            finally: self.api.CloseHandle(handle)
            raise
        try:
            self.stream = os.fdopen(fd, "w+b")
        except BaseException as failure:
            try: self._discard_handle(handle)
            except OSError as error:
                raise OSError(f"Export cleanup incomplete; owned scratch {self.path}: {error}") from failure
            finally: os.close(fd)
            raise
        self.handle = handle  # owned by stream; never close it a second time

    def flush(self):
        self.stream.flush()
        os.fsync(self.stream.fileno())

    def read(self):
        self.flush()
        self.stream.seek(0)
        return self.stream.read()

    def publish(self):
        self.flush()
        encoded = str(self.destination).encode("utf-16-le")
        size = max(ctypes.sizeof(_RenameInfo), _RenameInfo.FileName.offset + len(encoded) + 2)
        buffer = ctypes.create_string_buffer(size)
        info = _RenameInfo.from_buffer(buffer)
        info.ReplaceIfExists = False
        info.RootDirectory = None
        info.FileNameLength = len(encoded)
        ctypes.memmove(ctypes.addressof(buffer) + _RenameInfo.FileName.offset, encoded, len(encoded))
        if not self.api.SetFileInformationByHandle(self.handle, 3, buffer, size):  # FileRenameInfo
            raise ctypes.WinError(ctypes.get_last_error())
        self.path = self.destination

    def _discard_handle(self, handle):
        delete = ctypes.c_ubyte(1)
        if not self.api.SetFileInformationByHandle(handle, 4, ctypes.byref(delete), 1):  # FileDispositionInfo
            raise ctypes.WinError(ctypes.get_last_error())

    def discard(self):
        # No pathname unlink: even a colliding independently created sidecar is
        # outside our ownership. Windows deletes this object at final close.
        self._discard_handle(self.handle)

    def close(self):
        self.stream.close()


@contextmanager
def publication(*destinations):
    owned = []
    failure = None
    try:
        for destination in destinations:
            owned.append(_OwnedFile(destination))
        yield owned
    except BaseException as error:
        failure = error
        raise
    finally:
        errors = []
        if failure is not None:
            for item in reversed(owned):
                try: item.discard()
                except OSError as error: errors.append(f"delete owned {item.path}: {error}")
        for item in reversed(owned):
            try: item.close()
            except OSError as error: errors.append(f"close owned {item.path}: {error}")
        if errors:
            raise OSError("Export cleanup incomplete; inspect the named owned files. " + "; ".join(errors)) from failure


@contextmanager
def text_writer(stream, *, newline=""):
    """Text formatting on the owned binary stream without transferring ownership."""
    text = io.TextIOWrapper(stream, encoding="utf-8", newline=newline)
    try:
        yield text
        text.flush()
    finally:
        text.detach()
