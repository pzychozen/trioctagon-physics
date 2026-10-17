"""Explicit cross-token acceptance command, not a same-token unittest substitute.

Run --matrix CONFIG with the installed certified runtime. A normal operator gets
the ordinary Windows UAC prompt for an external test coordinator. CI starts high.
No file/directory ACL, machine policy or existing user data is changed. Fresh
medium children use the normal operator token locally, and a native
restricted token in elevated CI (recorded explicitly). The negative witness must
deny access.
"""
import ctypes as c
from ctypes import wintypes as w
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import traceback

K = c.WinDLL("kernel32", use_last_error=True) if os.name == "nt" else None
A = c.WinDLL("advapi32", use_last_error=True) if os.name == "nt" else None
if K:
    K.GetCurrentProcess.restype = w.HANDLE
    K.CloseHandle.argtypes = [w.HANDLE]
    K.LocalFree.argtypes = [c.c_void_p]
    K.WaitForSingleObject.argtypes = [w.HANDLE, w.DWORD]
    K.GetExitCodeProcess.argtypes = [w.HANDLE, c.POINTER(w.DWORD)]
    K.CreateFileW.argtypes = [w.LPCWSTR, w.DWORD, w.DWORD, c.c_void_p, w.DWORD, w.DWORD, w.HANDLE]
    K.CreateFileW.restype = w.HANDLE
    K.CopyFileW.argtypes = [w.LPCWSTR, w.LPCWSTR, w.BOOL]
    A.OpenProcessToken.argtypes = [w.HANDLE, w.DWORD, c.POINTER(w.HANDLE)]
    A.GetTokenInformation.argtypes = [w.HANDLE, c.c_int, c.c_void_p, w.DWORD, c.POINTER(w.DWORD)]
    A.SetTokenInformation.argtypes = [w.HANDLE, c.c_int, c.c_void_p, w.DWORD]
    A.ConvertSidToStringSidW.argtypes = [c.c_void_p, c.POINTER(w.LPWSTR)]
    A.ConvertStringSidToSidW.argtypes = [w.LPCWSTR, c.POINTER(c.c_void_p)]
    A.GetNamedSecurityInfoW.argtypes = [w.LPWSTR, c.c_int, w.DWORD, c.c_void_p, c.c_void_p, c.c_void_p, c.c_void_p, c.POINTER(c.c_void_p)]
    A.ConvertSecurityDescriptorToStringSecurityDescriptorW.argtypes = [c.c_void_p, w.DWORD, w.DWORD, c.POINTER(w.LPWSTR), c.c_void_p]
    A.CreateRestrictedToken.argtypes = [w.HANDLE, w.DWORD, w.DWORD, c.c_void_p, w.DWORD, c.c_void_p, w.DWORD, c.c_void_p, c.POINTER(w.HANDLE)]


class SidAttributes(c.Structure):
    _fields_ = [("sid", c.c_void_p), ("attributes", w.DWORD)]


class Startup(c.Structure):
    _fields_ = [("cb", w.DWORD), ("reserved", w.LPWSTR), ("desktop", w.LPWSTR), ("title", w.LPWSTR),
                ("x", w.DWORD), ("y", w.DWORD), ("sx", w.DWORD), ("sy", w.DWORD),
                ("charsx", w.DWORD), ("charsy", w.DWORD), ("fill", w.DWORD), ("flags", w.DWORD),
                ("show", w.WORD), ("reserved_size", w.WORD), ("reserved_ptr", c.c_void_p),
                ("stdin", w.HANDLE), ("stdout", w.HANDLE), ("stderr", w.HANDLE)]


class Process(c.Structure):
    _fields_ = [("process", w.HANDLE), ("thread", w.HANDLE), ("pid", w.DWORD), ("tid", w.DWORD)]


def checked(ok):
    if not ok: raise c.WinError(c.get_last_error())


def token_info(handle, kind):
    size = w.DWORD(); A.GetTokenInformation(handle, kind, None, 0, c.byref(size))
    if not size.value: raise c.WinError(c.get_last_error())
    buf = c.create_string_buffer(size.value)
    checked(A.GetTokenInformation(handle, kind, buf, len(buf), c.byref(size)))
    return buf


def sid_text(ptr):
    out = w.LPWSTR(); checked(A.ConvertSidToStringSidW(ptr, c.byref(out)))
    try: return out.value
    finally: K.LocalFree(out)


def token_identity():
    handle = w.HANDLE(); checked(A.OpenProcessToken(K.GetCurrentProcess(), 8, c.byref(handle)))
    try:
        groups = token_info(handle, 2)
        class Groups(c.Structure):
            _fields_ = [("count", w.DWORD), ("groups", SidAttributes * c.cast(groups, c.POINTER(w.DWORD))[0])]
        rows = [{"sid": sid_text(g.sid), "attributes": g.attributes} for g in Groups.from_buffer(groups).groups]
        return {"user_sid": sid_text(c.cast(token_info(handle, 1), c.POINTER(c.c_void_p))[0]),
                "owner_sid": sid_text(c.cast(token_info(handle, 4), c.POINTER(c.c_void_p))[0]),
                "integrity_sid": sid_text(c.cast(token_info(handle, 25), c.POINTER(c.c_void_p))[0]),
                "elevation_type": c.cast(token_info(handle, 18), c.POINTER(w.DWORD))[0],
                "is_elevated": bool(c.cast(token_info(handle, 20), c.POINTER(w.DWORD))[0]),
                "administrator_groups": [r for r in rows if r["sid"] == "S-1-5-32-544"]}
    finally: K.CloseHandle(handle)


def security(path):
    ptr = c.c_void_p(); out = w.LPWSTR(); flags = 0x17
    error = A.GetNamedSecurityInfoW(str(path), 1, flags, None, None, None, None, c.byref(ptr))
    if error: raise c.WinError(error)
    try:
        checked(A.ConvertSecurityDescriptorToStringSecurityDescriptorW(ptr, 1, flags, c.byref(out), None))
        return out.value
    finally:
        if out: K.LocalFree(out)
        K.LocalFree(ptr)


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def require_medium(identity):
    assert not identity["is_elevated"] and identity["integrity_sid"] == "S-1-16-8192", identity
    assert all(g["attributes"] & 16 and not g["attributes"] & 4 for g in identity["administrator_groups"]), identity


def medium_token():
    original = w.HANDLE(); checked(A.OpenProcessToken(K.GetCurrentProcess(), 0xF01FF, c.byref(original)))
    try:
        restricted = w.HANDLE()
        # Remove the Administrators grant and privileges, preserving the logon
        # session's normal desktop access; do not merely lower integrity.
        admin = c.c_void_p()
        checked(A.ConvertStringSidToSidW("S-1-5-32-544", c.byref(admin)))
        try:
            disabled = SidAttributes(admin, 0)
            checked(A.CreateRestrictedToken(original, 1 | 4, 1, c.byref(disabled), 0, None, 0, None, c.byref(restricted)))
        finally: K.LocalFree(admin)
        sid = c.c_void_p()
        try:
            checked(A.ConvertStringSidToSidW("S-1-16-8192", c.byref(sid)))
            label = SidAttributes(sid, 0x20)
            checked(A.SetTokenInformation(restricted, 25, c.byref(label), c.sizeof(label)))
            user = token_info(restricted, 1)
            owner = c.c_void_p(c.cast(user, c.POINTER(c.c_void_p))[0])
            checked(A.SetTokenInformation(restricted, 4, c.byref(owner), c.sizeof(owner)))
            # A venv launcher creates a second process. Its reduced token's
            # default DACL must permit that same user to initialize the child.
            # This is test-token construction, never an exported-file ACL edit.
            A.ConvertStringSecurityDescriptorToSecurityDescriptorW.argtypes = [w.LPCWSTR, w.DWORD, c.POINTER(c.c_void_p), c.c_void_p]
            A.GetSecurityDescriptorDacl.argtypes = [c.c_void_p, c.POINTER(w.BOOL), c.POINTER(c.c_void_p), c.POINTER(w.BOOL)]
            descriptor = c.c_void_p(); acl = c.c_void_p(); present = w.BOOL(); defaulted = w.BOOL()
            checked(A.ConvertStringSecurityDescriptorToSecurityDescriptorW(
                "D:(A;;GA;;;SY)(A;;GA;;;" + sid_text(owner.value) + ")", 1, c.byref(descriptor), None))
            try:
                checked(A.GetSecurityDescriptorDacl(descriptor, c.byref(present), c.byref(acl), c.byref(defaulted)))
                checked(A.SetTokenInformation(restricted, 6, c.byref(acl), c.sizeof(acl)))
            finally: K.LocalFree(descriptor)
            return restricted, "NATIVE_LUA_RESTRICTED_MEDIUM_TOKEN_ADMIN_DENY_ONLY"
        except BaseException:
            K.CloseHandle(restricted); raise
        finally:
            if sid: K.LocalFree(sid)
    finally: K.CloseHandle(original)


def child(mode, config, output, token=None):
    args = [sys.executable, "-I", "-B", "-X", "utf8", str(Path(__file__).resolve()), mode, str(config), str(output)]
    if token is None:
        subprocess.run(args, check=True, cwd=Path(config).parent, timeout=180)
    else:
        A.CreateProcessAsUserW.argtypes = [w.HANDLE, w.LPCWSTR, w.LPWSTR, c.c_void_p,
                                          c.c_void_p, w.BOOL, w.DWORD, c.c_void_p,
                                          w.LPCWSTR, c.POINTER(Startup), c.POINTER(Process)]
        startup = Startup(); startup.cb = c.sizeof(startup); startup.flags = 1; startup.show = 0
        # CreateProcessAsUser otherwise selects a noninteractive window station;
        # its default ACL can deny DLL initialization to the reduced token.
        # Reuse the coordinator's existing station/desktop; change no object ACL.
        user = c.WinDLL("user32", use_last_error=True)
        user.GetProcessWindowStation.restype = w.HANDLE
        user.GetThreadDesktop.argtypes = [w.DWORD]; user.GetThreadDesktop.restype = w.HANDLE
        user.GetUserObjectInformationW.argtypes = [w.HANDLE, c.c_int, c.c_void_p, w.DWORD, c.POINTER(w.DWORD)]
        def object_name(handle):
            buf = c.create_unicode_buffer(256); needed = w.DWORD()
            checked(user.GetUserObjectInformationW(handle, 2, buf, c.sizeof(buf), c.byref(needed)))
            return buf.value
        startup.desktop = object_name(user.GetProcessWindowStation()) + "\\" + object_name(user.GetThreadDesktop(K.GetCurrentThreadId()))
        K.SetErrorMode(1 | 2)  # child failures are recorded; no modal crash dialog
        process = Process(); line = c.create_unicode_buffer(subprocess.list2cmdline(args))
        checked(A.CreateProcessAsUserW(token, sys.executable, line, None, None,
                                      False, 0x08000000, None, str(Path(config).parent), c.byref(startup), c.byref(process)))
        try:
            assert K.WaitForSingleObject(process.process, 180000) == 0, "Cross-token child timed out"
            code = w.DWORD(); checked(K.GetExitCodeProcess(process.process, c.byref(code)))
            assert code.value == 0, f"Cross-token child failed: {code.value}; {output}"
        finally: K.CloseHandle(process.thread); K.CloseHandle(process.process)
    result = json.loads(Path(output).read_text(encoding="utf-8"))
    assert result["status"] == "PASS", result
    return result


def writer(config):
    sys.path.insert(0, str(Path(__file__).parent))
    from test_export_publication import cached_view, no_science
    from trioctagon_ui import axial_exports
    from unittest.mock import patch
    view = cached_view(); identity = token_identity(); elevated = identity["is_elevated"]
    if not elevated: require_medium(identity)
    else: assert identity["integrity_sid"] == "S-1-16-12288"
    rows = []
    for destination in config["destinations"]:
        folder = Path(destination) / ("elevated" if elevated else "normal"); folder.mkdir()
        with no_science(), patch.object(os, "link", side_effect=AssertionError("os.link forbidden")):
            axial_exports.export_json(view, folder / "cache.json")
            axial_exports.export_csv(view, folder / "cache.csv")
        assert (folder / "cache.json").read_bytes() == view.canonical_json.encode("utf-8")
        assert json.loads((folder / "cache.csv.provenance.json").read_bytes())["sha256"] == hashlib.sha256((folder / "cache.csv").read_bytes()).hexdigest()
        published = sorted(folder.iterdir())
        assert len(published) == 3 and all(p.stat().st_nlink == 1 for p in published)
        for path in published:
            sibling = folder / ("direct-" + path.name); sibling.write_bytes(path.read_bytes())
            assert security(path) == security(sibling), (path, security(path), security(sibling))
        # Actual CPython TemporaryDirectory, without any fixture ACL adjustment.
        with tempfile.TemporaryDirectory(prefix="private-control-", dir=folder) as temporary:
            scratch = Path(temporary) / "payload.json"; scratch.write_bytes(b'{"negative":"private directory plus rename"}\n')
            private_security = security(scratch)
            os.rename(scratch, folder / "negative-private-rename.json")
        assert not list(folder.glob(".trioctagon-*")) and not list(folder.glob("private-control-*"))
        for path in sorted(folder.iterdir()):
            rows.append({"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                         "security": security(path), "links": path.stat().st_nlink,
                         "negative": path.name.startswith("negative-"), "writer_elevated": elevated})
        assert all(r["links"] == 1 for r in rows)
    return {"status": "PASS", "pid": os.getpid(), "python": sys.version, "token": identity,
            "files": rows, "negative_staged_security": private_security, "json_exact": True,
            "csv_hash": True, "direct_sibling_security_equal": True, "no_scratch": True,
            "os_link_forbidden": True, "scientific_calls_forbidden": True}


def reader(config):
    identity = token_identity(); require_medium(identity)
    rows = []
    copyroot = Path(config["copy_destination"]); copyroot.mkdir()
    for source in config["files"]:
        path = Path(source["path"]); row = {"path": str(path)}
        expected_denied = source["negative"] and source["writer_elevated"]
        try:
            with path.open("rb") as stream: raw = stream.read()
            row["python_read"] = "PASS"; row["sha256"] = hashlib.sha256(raw).hexdigest()
        except OSError as error: row.update(python_read="DENIED", python_error=error.winerror, python_errno=error.errno)
        handle = K.CreateFileW(str(path), 0x80000000, 7, None, 3, 0x80, None)
        row["read_only_error"] = c.get_last_error() if handle == c.c_void_p(-1).value else 0
        if row["read_only_error"] == 0: K.CloseHandle(handle)
        target = copyroot / (str(len(rows)) + "-" + path.name)
        row["copy_error"] = 0 if K.CopyFileW(str(path), str(target), True) else c.get_last_error()
        if expected_denied:
            assert row["python_read"] == "DENIED" and row["python_errno"] == 13 and row["read_only_error"] == row["copy_error"] == 5, row
            assert not target.exists()
        else:
            assert row["python_read"] == "PASS" and row["read_only_error"] == row["copy_error"] == 0, row
            assert row["sha256"] == source["sha256"] == hashlib.sha256(target.read_bytes()).hexdigest()
        row["expected_denied"] = expected_denied; rows.append(row)
    assert sum(r["expected_denied"] for r in rows) == len(config["destinations"])
    return {"status": "PASS", "pid": os.getpid(), "token": identity, "python": sys.version, "files": rows}


def elevated(config_path):
    config = json.loads(Path(config_path).read_text(encoding="utf-8"))
    identity = token_identity(); assert identity["is_elevated"]
    assert sys.version_info[:3] >= (3, 11, 10), "Negative witness requires affected CPython Windows mkdir semantics"
    token, mechanism = medium_token()
    root = Path(config_path).parent
    try:
        normal = child("--writer", config_path, root / "normal-writer.json", token)
        high = child("--writer", config_path, root / "elevated-writer.json")
        reader_config = {**config, "files": normal["files"] + high["files"]}
        read_path = root / "reader-config.json"; write_json(read_path, reader_config)
        read = child("--reader", read_path, root / "normal-reader.json", token)
        assert len({normal["pid"], high["pid"], read["pid"]}) == 3
        assert normal["token"]["user_sid"] == high["token"]["user_sid"] == read["token"]["user_sid"]
        return {"status": "PASS", "python": sys.version, "platform": platform.platform(), "coordinator_token": identity,
                "medium_token_mechanism": mechanism, "normal_writer": normal, "elevated_writer": high, "normal_reader": read,
                "ui_version": importlib.metadata.version("trioctagon-scientific-ui"),
                "source_commit": config["source_commit"], "negative_private_directory_rename_denied": True}
    finally: K.CloseHandle(token)


def matrix(config_path):
    path = Path(config_path); output = path.parent / "cross-token-access.json"
    if token_identity()["is_elevated"]:
        result = elevated(path); write_json(output, result)
    else:
        assert sys.version_info[:3] >= (3, 11, 10), "Negative witness requires affected CPython"
        config = json.loads(path.read_text(encoding="utf-8"))
        normal = child("--writer", path, path.parent / "normal-writer.json")
        # ShellExecute/UAC is the normal Windows elevation path; no service or
        # scheduled-task workaround. All arguments identify this external test.
        quote = lambda s: "'" + str(s).replace("'", "''") + "'"
        high_output = path.parent / "elevated-writer.json"
        arguments = subprocess.list2cmdline(["-I", "-B", "-X", "utf8", str(Path(__file__).resolve()), "--writer", str(path), str(high_output)])
        command = "$p=Start-Process -FilePath " + quote(sys.executable) + " -ArgumentList " + quote(arguments) + " -Verb RunAs -WindowStyle Hidden -PassThru -Wait; exit $p.ExitCode"
        subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", command], check=True, timeout=600)
        high = json.loads(high_output.read_text(encoding="utf-8")); assert high["status"] == "PASS"
        assert high["token"]["is_elevated"]
        read_path = path.parent / "reader-config.json"
        write_json(read_path, {**config, "files": normal["files"] + high["files"]})
        read = child("--reader", read_path, path.parent / "normal-reader.json")
        assert len({normal["pid"], high["pid"], read["pid"]}) == 3
        assert normal["token"]["user_sid"] == high["token"]["user_sid"] == read["token"]["user_sid"]
        result = {"status": "PASS", "python": sys.version, "platform": platform.platform(),
                  "coordinator_token": token_identity(), "medium_token_mechanism": "ORDINARY_OPERATOR_FRESH_PROCESSES",
                  "normal_writer": normal, "elevated_writer": high, "normal_reader": read,
                  "ui_version": importlib.metadata.version("trioctagon-scientific-ui"),
                  "source_commit": config["source_commit"], "negative_private_directory_rename_denied": True}
        write_json(output, result)
    assert result["status"] == "PASS", result
    print(json.dumps({"status": result["status"], "medium_token_mechanism": result["medium_token_mechanism"], "evidence": str(output)}))


if __name__ == "__main__":
    try:
        mode, config_path = sys.argv[1:3]
        if mode == "--matrix": matrix(config_path)
        else:
            config = json.loads(Path(config_path).read_text(encoding="utf-8"))
            result = elevated(config_path) if mode == "--elevated" else (writer(config) if mode == "--writer" else reader(config))
            write_json(sys.argv[3], result)
    except BaseException:
        if len(sys.argv) > 3: write_json(sys.argv[3], {"status": "FAIL", "traceback": traceback.format_exc()})
        raise
