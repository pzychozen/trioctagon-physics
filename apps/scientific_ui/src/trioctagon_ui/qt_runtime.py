"""Select Qt's Windows ICU dependency before Conda DLL search can shadow it."""
import os
import sys

_icu = None


def prepare_qt():
    """Qt's unversioned ICU symbols belong to the Windows system library.

    Conda also ships icuuc.dll, with version-suffixed symbols. Its DLL directory
    can shadow System32 even inside a fresh venv. Keep the explicit OS library
    handle alive; do not copy DLLs, change PATH or modify the Conda installation.
    This is GUI startup only, never called by the scientific worker.
    """
    global _icu
    if sys.platform == "win32" and _icu is None:
        import ctypes
        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        directory = ctypes.create_unicode_buffer(32768)
        if not kernel.GetSystemDirectoryW(directory, len(directory)):
            raise ctypes.WinError(ctypes.get_last_error())
        _icu = ctypes.WinDLL(os.path.join(directory.value, "icuuc.dll"), winmode=0x800)
