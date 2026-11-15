from pathlib import Path
import sys, json, datetime, subprocess, hashlib, time, ctypes
from ctypes import wintypes
ROOT=Path(__file__).resolve().parent
def write(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')
class MemoryCounters(ctypes.Structure):
    _fields_=[('cb',wintypes.DWORD),('PageFaultCount',wintypes.DWORD),
    ('PeakWorkingSetSize',ctypes.c_size_t),('WorkingSetSize',ctypes.c_size_t),
    ('QuotaPeakPagedPoolUsage',ctypes.c_size_t),('QuotaPagedPoolUsage',ctypes.c_size_t),
    ('QuotaPeakNonPagedPoolUsage',ctypes.c_size_t),('QuotaNonPagedPoolUsage',ctypes.c_size_t),
    ('PagefileUsage',ctypes.c_size_t),('PeakPagefileUsage',ctypes.c_size_t)]
getmem=ctypes.WinDLL('psapi',use_last_error=True).GetProcessMemoryInfo
getmem.argtypes=[wintypes.HANDLE,ctypes.POINTER(MemoryCounters),wintypes.DWORD]
getmem.restype=wintypes.BOOL
log=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'recheck'
log.mkdir(parents=True,exist_ok=True)
cmd=[sys.executable,'-B',str(ROOT/'exact_check.py'),str(log)]
start=datetime.datetime.now(datetime.timezone.utc).isoformat(); tick=__import__('time').monotonic();peak=0
with (log/'EXACT.stdout').open('wb') as stdout,(log/'EXACT.stderr').open('wb') as stderr:
    proc=subprocess.Popen(cmd,stdout=stdout,stderr=stderr,cwd=ROOT)
    reason=None
    while proc.poll() is None:
        m=MemoryCounters();m.cb=ctypes.sizeof(m)
        if not getmem(int(proc._handle),ctypes.byref(m),m.cb):
            if proc.poll() is not None: break
            reason='Windows memory monitor failed';proc.kill();break
        rss=m.WorkingSetSize;peak=max(peak,rss)
        if time.monotonic()-tick>300:reason='300 second wall limit'
        if rss>768*1024**2:reason='768 MiB RSS limit'
        if reason:proc.kill();break
        time.sleep(0.25)
    code=proc.wait()
write(log/'RUN_RECORD.json',{'argv':cmd,'entry_command':sys.argv,'start_utc':start,'elapsed_seconds':time.monotonic()-tick,'returncode':code,'termination_reason':reason,'peak_observed_rss_bytes':peak,'wall_limit_seconds':300,'rss_limit_bytes':768*1024**2,'worker_sha256':hashlib.sha256((ROOT/'exact_check.py').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
print((log/'EXACT.stdout').read_text());print((log/'EXACT.stderr').read_text());assert code==0 and reason is None
