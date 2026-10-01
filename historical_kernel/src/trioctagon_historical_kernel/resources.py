"""Windows process resource limits only. No B2 snapshot, protection or attestation."""
import ctypes
from ctypes import wintypes
import os


class MemoryCounters(ctypes.Structure):
    _fields_ = [("cb",wintypes.DWORD),("PageFaultCount",wintypes.DWORD),
        ("PeakWorkingSetSize",ctypes.c_size_t),("WorkingSetSize",ctypes.c_size_t),
        ("QuotaPeakPagedPoolUsage",ctypes.c_size_t),("QuotaPagedPoolUsage",ctypes.c_size_t),
        ("QuotaPeakNonPagedPoolUsage",ctypes.c_size_t),("QuotaNonPagedPoolUsage",ctypes.c_size_t),
        ("PagefileUsage",ctypes.c_size_t),("PeakPagefileUsage",ctypes.c_size_t),
        ("PrivateUsage",ctypes.c_size_t)]


class BasicLimits(ctypes.Structure):
    _fields_ = [("PerProcessUserTimeLimit",ctypes.c_int64),("PerJobUserTimeLimit",ctypes.c_int64),
        ("LimitFlags",wintypes.DWORD),("MinimumWorkingSetSize",ctypes.c_size_t),
        ("MaximumWorkingSetSize",ctypes.c_size_t),("ActiveProcessLimit",wintypes.DWORD),
        ("Affinity",ctypes.c_size_t),("PriorityClass",wintypes.DWORD),("SchedulingClass",wintypes.DWORD)]


class IOCount(ctypes.Structure):
    _fields_ = [(name,ctypes.c_uint64) for name in ("ReadOperationCount","WriteOperationCount","OtherOperationCount",
                                                  "ReadTransferCount","WriteTransferCount","OtherTransferCount")]


class ExtendedLimits(ctypes.Structure):
    _fields_ = [("BasicLimitInformation",BasicLimits),("IoInfo",IOCount),("ProcessMemoryLimit",ctypes.c_size_t),
        ("JobMemoryLimit",ctypes.c_size_t),("PeakProcessMemoryUsed",ctypes.c_size_t),("PeakJobMemoryUsed",ctypes.c_size_t)]


class CompletionPort(ctypes.Structure):
    _fields_ = [("CompletionKey",ctypes.c_void_p),("CompletionPort",wintypes.HANDLE)]


def _apis():
    if os.name != "nt":
        raise RuntimeError("local issuer currently requires certified Windows")
    kernel = ctypes.WinDLL("kernel32",use_last_error=True)
    kernel.GetCurrentProcess.restype = wintypes.HANDLE
    kernel.CreateJobObjectW.argtypes = (ctypes.c_void_p,wintypes.LPCWSTR)
    kernel.CreateJobObjectW.restype = wintypes.HANDLE
    kernel.SetInformationJobObject.argtypes = (wintypes.HANDLE,ctypes.c_int,ctypes.c_void_p,wintypes.DWORD)
    kernel.SetInformationJobObject.restype = wintypes.BOOL
    kernel.AssignProcessToJobObject.argtypes = (wintypes.HANDLE,wintypes.HANDLE)
    kernel.AssignProcessToJobObject.restype = wintypes.BOOL
    kernel.OpenProcess.argtypes = (wintypes.DWORD,wintypes.BOOL,wintypes.DWORD)
    kernel.OpenProcess.restype = wintypes.HANDLE
    kernel.IsProcessInJob.argtypes = (wintypes.HANDLE,wintypes.HANDLE,ctypes.POINTER(wintypes.BOOL))
    kernel.IsProcessInJob.restype = wintypes.BOOL
    kernel.CreateIoCompletionPort.argtypes = (wintypes.HANDLE,wintypes.HANDLE,ctypes.c_size_t,wintypes.DWORD)
    kernel.CreateIoCompletionPort.restype = wintypes.HANDLE
    kernel.GetQueuedCompletionStatus.argtypes = (wintypes.HANDLE,ctypes.POINTER(wintypes.DWORD),ctypes.POINTER(ctypes.c_size_t),ctypes.POINTER(ctypes.c_void_p),wintypes.DWORD)
    kernel.GetQueuedCompletionStatus.restype = wintypes.BOOL
    kernel.CloseHandle.argtypes = (wintypes.HANDLE,)
    kernel.CloseHandle.restype = wintypes.BOOL
    psapi = ctypes.WinDLL("psapi",use_last_error=True)
    psapi.GetProcessMemoryInfo.argtypes = (wintypes.HANDLE,ctypes.c_void_p,wintypes.DWORD)
    psapi.GetProcessMemoryInfo.restype = wintypes.BOOL
    return kernel,psapi


def peak_memory(handle=None):
    kernel,psapi = _apis()
    info = MemoryCounters();info.cb=ctypes.sizeof(info)
    if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess() if handle is None else handle,ctypes.byref(info),info.cb):
        raise ctypes.WinError(ctypes.get_last_error())
    # Conservative whole-worker accounting: peak resident + peak private commit.
    # This can double count private resident pages; measurement/policy use the
    # same definition. Shared mapped image pages are included by resident usage.
    return int(info.PeakWorkingSetSize+info.PeakPagefileUsage)


class ProcessBudget:
    def __init__(self, process_handle, memory_bytes):
        self.kernel,_ = _apis()
        self.worker = None
        self.launcher = process_handle
        self.port = None
        self.resource_exhausted = False
        self.peak = 0
        self.handle = self.kernel.CreateJobObjectW(None,None)
        if not self.handle:
            raise ctypes.WinError(ctypes.get_last_error())
        limits = ExtendedLimits()
        # Windows venv python.exe is a launcher plus the actual interpreter.
        # Both are constrained together; the actual worker is also explicitly
        # assigned at its ready gate to cover child creation before assignment.
        limits.BasicLimitInformation.LimitFlags = 0x00000200 | 0x00002000 | 0x00000008
        limits.BasicLimitInformation.ActiveProcessLimit = 2
        limits.JobMemoryLimit = memory_bytes
        self.port = self.kernel.CreateIoCompletionPort(wintypes.HANDLE(-1),None,0,1)
        association = CompletionPort(1,self.port)
        if not self.port or not self.kernel.SetInformationJobObject(self.handle,7,ctypes.byref(association),ctypes.sizeof(association)):
            error=ctypes.get_last_error();self.close();raise ctypes.WinError(error)
        if not self.kernel.SetInformationJobObject(self.handle,9,ctypes.byref(limits),ctypes.sizeof(limits)) or not self.kernel.AssignProcessToJobObject(self.handle,process_handle):
            error=ctypes.get_last_error();self.close();raise ctypes.WinError(error)

    def attach_worker(self, pid):
        if type(pid) is not int or pid <= 0 or self.worker is not None:
            raise ValueError("invalid worker resource handshake")
        self.worker=self.kernel.OpenProcess(0x0100|0x0400|0x0010|0x0001,False,pid)
        if not self.worker:raise ctypes.WinError(ctypes.get_last_error())
        inside=wintypes.BOOL()
        if not self.kernel.IsProcessInJob(self.worker,self.handle,ctypes.byref(inside)):
            raise ctypes.WinError(ctypes.get_last_error())
        if not inside.value and not self.kernel.AssignProcessToJobObject(self.handle,self.worker):
            raise ctypes.WinError(ctypes.get_last_error())

    def exceeded(self, memory_bytes):
        # Notifications corroborate hard allocation denials; absence of a
        # notification is never treated as proof that an unknown exit succeeded.
        code=wintypes.DWORD();key=ctypes.c_size_t();overlapped=ctypes.c_void_p()
        while self.kernel.GetQueuedCompletionStatus(self.port,ctypes.byref(code),ctypes.byref(key),ctypes.byref(overlapped),0):
            if code.value in (3,9,10):self.resource_exhausted=True
        observed=peak_memory(self.launcher)
        if self.worker:observed+=peak_memory(self.worker)
        self.peak=max(self.peak,observed)
        return self.resource_exhausted or self.peak>memory_bytes

    def close(self):
        if self.handle:
            self.kernel.CloseHandle(self.handle)
            self.handle = None
        if self.worker:
            self.kernel.CloseHandle(self.worker);self.worker=None
        if self.port:
            self.kernel.CloseHandle(self.port);self.port=None
