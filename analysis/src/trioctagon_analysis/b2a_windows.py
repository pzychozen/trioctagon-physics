"""WINDOWS_ATTESTATION_PROTOTYPE: B2A-only Windows proof primitives.

Not a production attestor. No normal analysis issuance or provider shell.
WINDOWS_EXECUTION_BINDING remains NOT_PROVEN; B2B is not enabled.
"""
import ctypes as c
from ctypes import wintypes as w
from pathlib import Path
import os
import subprocess
import uuid


def dll(name):
    if os.name != 'nt':
        raise OSError('B2A requires Windows')
    return c.WinDLL(name, use_last_error=True)


def function(lib, name, result, *args):
    fn = getattr(lib, name)
    fn.restype, fn.argtypes = result, list(args)
    return fn


def checked(ok):
    if not ok:
        raise c.WinError(c.get_last_error())
    return ok


def close(handle):
    if handle:
        checked(function(dll('kernel32'), 'CloseHandle', w.BOOL, w.HANDLE)(handle))


class ReadLease:
    """Keep read access; deny all subsequent write/delete opens until close.

    A lease does not protect a directory member set: use a frozen directory DACL
    as well. Reparse/alias checking belongs to the snapshot admission layer.
    """
    def __init__(self, path, directory=False):
        fn = function(dll('kernel32'), 'CreateFileW', w.HANDLE,
                      w.LPCWSTR, w.DWORD, w.DWORD, c.c_void_p, w.DWORD, w.DWORD, w.HANDLE)
        self.handle = fn(str(path), 0x80 if directory else 0x80000000, 1, None, 3,
                         0x02200000 if directory else 0x00200000, None)
        if self.handle == c.c_void_p(-1).value:
            self.handle = None
            raise c.WinError(c.get_last_error())

    def close(self):
        if self.handle:
            handle, self.handle = self.handle, None
            close(handle)

    def __enter__(self):
        return self

    def __exit__(self, *unused):
        self.close()


def current_user_sid():
    adv, kernel = dll('advapi32'), dll('kernel32')
    token = w.HANDLE()
    process = function(kernel, 'GetCurrentProcess', w.HANDLE)()
    checked(function(adv, 'OpenProcessToken', w.BOOL, w.HANDLE, w.DWORD,
                     c.POINTER(w.HANDLE))(process, 8, c.byref(token)))
    try:
        size = w.DWORD()
        query = function(adv, 'GetTokenInformation', w.BOOL, w.HANDLE, w.DWORD,
                         c.c_void_p, w.DWORD, c.POINTER(w.DWORD))
        query(token, 1, None, 0, c.byref(size))
        storage = c.create_string_buffer(size.value)
        checked(query(token, 1, storage, size, c.byref(size)))
        sid = c.cast(storage, c.POINTER(c.c_void_p))[0]
        result = w.LPWSTR()
        checked(function(adv, 'ConvertSidToStringSidW', w.BOOL,
                         c.c_void_p, c.POINTER(w.LPWSTR))(sid, c.byref(result)))
        text = result.value
        function(kernel, 'LocalFree', c.c_void_p, c.c_void_p)(result)
        return text
    finally:
        close(token)


def set_dacl(path, app_sid=None, writable=False):
    """Change only a caller-owned staging object; never an original input/checkout."""
    rights = 'FA' if writable else 'FRFX'
    # Owner retains WRITE_DAC through Windows ownership, not a worker capability.
    descriptor = 'D:P(A;OICI;FA;;;SY)(A;OICI;' + rights + ';;;' + current_user_sid() + ')'
    if app_sid:
        descriptor += '(A;OICI;' + rights + ';;;' + app_sid + ')'
    pointer = c.c_void_p()
    adv = dll('advapi32')
    checked(function(adv, 'ConvertStringSecurityDescriptorToSecurityDescriptorW', w.BOOL,
                     w.LPCWSTR, w.DWORD, c.POINTER(c.c_void_p), c.c_void_p)(descriptor, 1, c.byref(pointer), None))
    try:
        checked(function(adv, 'SetFileSecurityW', w.BOOL, w.LPCWSTR, w.DWORD, c.c_void_p)(
            str(path), 0x80000004, pointer))
    finally:
        function(dll('kernel32'), 'LocalFree', c.c_void_p, c.c_void_p)(pointer)


class STARTUPINFO(c.Structure):
    _fields_ = [('cb', w.DWORD), ('lpReserved', w.LPWSTR), ('lpDesktop', w.LPWSTR),
        ('lpTitle', w.LPWSTR), ('dwX', w.DWORD), ('dwY', w.DWORD),
        ('dwXSize', w.DWORD), ('dwYSize', w.DWORD), ('dwXCountChars', w.DWORD),
        ('dwYCountChars', w.DWORD), ('dwFillAttribute', w.DWORD), ('dwFlags', w.DWORD),
        ('wShowWindow', w.WORD), ('cbReserved2', w.WORD), ('lpReserved2', c.c_void_p),
        ('hStdInput', w.HANDLE), ('hStdOutput', w.HANDLE), ('hStdError', w.HANDLE)]


class STARTUPINFOEX(c.Structure):
    _fields_ = [('StartupInfo', STARTUPINFO), ('lpAttributeList', c.c_void_p)]


class PROCESS_INFORMATION(c.Structure):
    _fields_ = [('hProcess', w.HANDLE), ('hThread', w.HANDLE),
                ('dwProcessId', w.DWORD), ('dwThreadId', w.DWORD)]


class SECURITY_CAPABILITIES(c.Structure):
    _fields_ = [('AppContainerSid', c.c_void_p), ('Capabilities', c.c_void_p),
                ('CapabilityCount', w.DWORD), ('Reserved', w.DWORD)]


class MEMORY_COUNTERS(c.Structure):
    _fields_ = [('cb', w.DWORD), ('PageFaultCount', w.DWORD)] + [
        (name, c.c_size_t) for name in ('PeakWorkingSetSize', 'WorkingSetSize',
        'QuotaPeakPagedPoolUsage', 'QuotaPagedPoolUsage', 'QuotaPeakNonPagedPoolUsage',
        'QuotaNonPagedPoolUsage', 'PagefileUsage', 'PeakPagefileUsage', 'PrivateUsage')]


class LOAD_DLL(c.Structure):
    _fields_ = [('hFile', w.HANDLE), ('base', c.c_void_p), ('offset', w.DWORD),
                ('size', w.DWORD), ('image_name', c.c_void_p), ('unicode', w.WORD)]


class CREATE_PROCESS(c.Structure):
    _fields_ = [('hFile', w.HANDLE), ('hProcess', w.HANDLE), ('hThread', w.HANDLE),
                ('base', c.c_void_p), ('offset', w.DWORD), ('size', w.DWORD),
                ('tls', c.c_void_p), ('start', c.c_void_p),
                ('image_name', c.c_void_p), ('unicode', w.WORD)]


class EVENT_DATA(c.Union):
    _fields_ = [('dll', LOAD_DLL), ('process', CREATE_PROCESS),
                ('raw', c.c_ubyte * 160), ('code', w.DWORD)]


class DEBUG_EVENT(c.Structure):
    _fields_ = [('event', w.DWORD), ('pid', w.DWORD), ('tid', w.DWORD), ('data', EVENT_DATA)]


def final_path(handle):
    buffer = c.create_unicode_buffer(32768)
    size = function(dll('kernel32'), 'GetFinalPathNameByHandleW', w.DWORD,
                    w.HANDLE, w.LPWSTR, w.DWORD, w.DWORD)(handle, buffer, len(buffer), 0)
    checked(size and size < len(buffer))
    path = buffer.value
    return Path(path[4:] if path.startswith('\\\\?\\') else path)


def next_debug_event(milliseconds=100):
    event = DEBUG_EVENT()
    ok = function(dll('kernel32'), 'WaitForDebugEvent', w.BOOL,
                  c.POINTER(DEBUG_EVENT), w.DWORD)(c.byref(event), milliseconds)
    if not ok and c.get_last_error() == 121:
        return None
    checked(ok)
    return event


def continue_debug_event(event, handled=True):
    checked(function(dll('kernel32'), 'ContinueDebugEvent', w.BOOL,
        w.DWORD, w.DWORD, w.DWORD)(event.pid, event.tid, 0x10002 if handled else 0x80010001))


class AppContainer:
    """Fresh profile, zero capabilities, no inherited handles, no child processes.

    Only the attestation coordinator launches this fixed proof worker. This is
    not a generic scientific-provider process API or a native malware sandbox.
    """
    def __init__(self):
        if os.name != 'nt' or c.sizeof(c.c_void_p) != 8:
            raise OSError('B2A proof requires Windows x86-64')
        self.name = 'Trioctagon.B2A.' + uuid.uuid4().hex
        self.sid = c.c_void_p()
        self.profile_created = False
        self.process = None
        self.userenv = dll('userenv')
        hr = function(self.userenv, 'CreateAppContainerProfile', c.c_long,
            w.LPCWSTR, w.LPCWSTR, w.LPCWSTR, c.c_void_p, w.DWORD, c.POINTER(c.c_void_p))(
                self.name, self.name, 'Temporary B2A validation evidence', None, 0, c.byref(self.sid))
        if hr < 0:
            raise OSError('CreateAppContainerProfile HRESULT ' + hex(hr & 0xffffffff))
        self.profile_created = True
        text = w.LPWSTR()
        try:
            checked(function(dll('advapi32'), 'ConvertSidToStringSidW', w.BOOL,
                             c.c_void_p, c.POINTER(w.LPWSTR))(self.sid, c.byref(text)))
            self.sid_string = text.value
        except BaseException:
            self.close()
            raise
        finally:
            if text:
                function(dll('kernel32'), 'LocalFree', c.c_void_p, c.c_void_p)(text)

    @property
    def folder(self):
        pointer = w.LPWSTR()
        hr = function(self.userenv, 'GetAppContainerFolderPath', c.c_long,
                      w.LPCWSTR, c.POINTER(w.LPWSTR))(self.sid_string, c.byref(pointer))
        if hr < 0:
            raise OSError('AppContainer folder query failed')
        result = Path(pointer.value)
        function(dll('ole32'), 'CoTaskMemFree', None, c.c_void_p)(pointer)
        return result

    def launch(self, interpreter, worker, arguments, cwd, *, environment, debug=False):
        if self.process is not None:
            raise ValueError('single launch per fresh AppContainer')
        interpreter, worker, cwd = (Path(p).absolute() for p in (interpreter, worker, cwd))
        kernel = dll('kernel32')
        size = c.c_size_t()
        init = function(kernel, 'InitializeProcThreadAttributeList', w.BOOL,
                        c.c_void_p, w.DWORD, w.DWORD, c.POINTER(c.c_size_t))
        init(None, 2, 0, c.byref(size))
        storage = c.create_string_buffer(size.value)
        checked(init(storage, 2, 0, c.byref(size)))
        update = function(kernel, 'UpdateProcThreadAttribute', w.BOOL, c.c_void_p,
                          w.DWORD, c.c_size_t, c.c_void_p, c.c_size_t, c.c_void_p, c.c_void_p)
        caps = SECURITY_CAPABILITIES(self.sid, None, 0, 0)
        no_children = w.DWORD(1)
        info = STARTUPINFOEX()
        info.StartupInfo.cb = c.sizeof(info)
        info.lpAttributeList = c.cast(storage, c.c_void_p)
        proc = PROCESS_INFORMATION()
        command = c.create_unicode_buffer(subprocess.list2cmdline([
            str(interpreter), '-I', '-S', '-B', str(worker), *map(str, arguments)]))
        block = c.create_unicode_buffer('\0'.join(k + '=' + v for k, v in sorted(environment.items())) + '\0\0')
        try:
            checked(update(storage, 0, 0x20009, c.byref(caps), c.sizeof(caps), None, None))
            checked(update(storage, 0, 0x2000e, c.byref(no_children), c.sizeof(no_children), None, None))
            checked(function(kernel, 'CreateProcessW', w.BOOL, w.LPCWSTR, w.LPWSTR,
                c.c_void_p, c.c_void_p, w.BOOL, w.DWORD, c.c_void_p, w.LPCWSTR,
                c.POINTER(STARTUPINFOEX), c.POINTER(PROCESS_INFORMATION))(
                    str(interpreter), command, None, None, False,
                    0x00080000 | 0x00000400 | 0x08000000 | (2 if debug else 0), block, str(cwd), c.byref(info), c.byref(proc)))
            self.process = proc.hProcess
            self.pid = proc.dwProcessId
            close(proc.hThread)
        finally:
            function(kernel, 'DeleteProcThreadAttributeList', None, c.c_void_p)(storage)

    def memory(self):
        counters = MEMORY_COUNTERS()
        counters.cb = c.sizeof(counters)
        checked(function(dll('psapi'), 'GetProcessMemoryInfo', w.BOOL,
                         w.HANDLE, c.c_void_p, w.DWORD)(self.process, c.byref(counters), c.sizeof(counters)))
        return {name: getattr(counters, name) for name in
                ('WorkingSetSize', 'PeakWorkingSetSize', 'PrivateUsage', 'PeakPagefileUsage')}

    def wait(self, milliseconds):
        state = function(dll('kernel32'), 'WaitForSingleObject', w.DWORD,
                         w.HANDLE, w.DWORD)(self.process, milliseconds)
        if state == 258:
            return None
        checked(state == 0)
        result = w.DWORD()
        checked(function(dll('kernel32'), 'GetExitCodeProcess', w.BOOL,
                         w.HANDLE, c.POINTER(w.DWORD))(self.process, c.byref(result)))
        return result.value

    def close(self):
        if self.process:
            if self.wait(100) is None:
                terminated = function(dll('kernel32'), 'TerminateProcess', w.BOOL, w.HANDLE, w.UINT)(self.process, 1)
                error = c.get_last_error()
                if not terminated and error != 5:
                    raise c.WinError(error)
                if self.wait(10000) is None:
                    raise OSError('worker did not finish during cleanup')
            close(self.process)
            self.process = None
        if self.profile_created:
            hr = function(self.userenv, 'DeleteAppContainerProfile', c.c_long, w.LPCWSTR)(self.name)
            if hr < 0:
                raise OSError('AppContainer cleanup failed: ' + hex(hr & 0xffffffff))
            self.profile_created = False
        if self.sid:
            function(dll('advapi32'), 'FreeSid', c.c_void_p, c.c_void_p)(self.sid)
            self.sid = None

    def __enter__(self):
        return self

    def __exit__(self, *unused):
        self.close()
