"""Windows scientific worker resource guard; no production imports."""
from common import *
import ctypes as ct
from ctypes import wintypes as wt
import runpy,time
class BASIC(ct.Structure):
    _fields_=[('PerProcessUserTimeLimit',ct.c_longlong),('PerJobUserTimeLimit',ct.c_longlong),('LimitFlags',wt.DWORD),('MinimumWorkingSetSize',ct.c_size_t),('MaximumWorkingSetSize',ct.c_size_t),('ActiveProcessLimit',wt.DWORD),('Affinity',ct.c_size_t),('PriorityClass',wt.DWORD),('SchedulingClass',wt.DWORD)]
class IO(ct.Structure):_fields_=[(x,ct.c_ulonglong) for x in ['ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount']]
class EXT(ct.Structure):_fields_=[('BasicLimitInformation',BASIC),('IoInfo',IO),('ProcessMemoryLimit',ct.c_size_t),('JobMemoryLimit',ct.c_size_t),('PeakProcessMemoryUsed',ct.c_size_t),('PeakJobMemoryUsed',ct.c_size_t)]
k=ct.WinDLL('kernel32',use_last_error=True);k.CreateJobObjectW.restype=wt.HANDLE;k.GetCurrentProcess.restype=wt.HANDLE
k.SetInformationJobObject.argtypes=[wt.HANDLE,ct.c_int,ct.c_void_p,wt.DWORD];k.AssignProcessToJobObject.argtypes=[wt.HANDLE,wt.HANDLE]
k.QueryInformationJobObject.argtypes=[wt.HANDLE,ct.c_int,ct.c_void_p,wt.DWORD,ct.c_void_p]
job=k.CreateJobObjectW(None,None);assert job
limits=EXT();limits.BasicLimitInformation.LimitFlags=0x100|0x2000;limits.ProcessMemoryLimit=2*1024**3
assert k.SetInformationJobObject(job,9,ct.byref(limits),ct.sizeof(limits)),ct.get_last_error()
assert k.AssignProcessToJobObject(job,k.GetCurrentProcess()),ct.get_last_error()
target=Path(sys.argv[1]).resolve();tag=sys.argv[2];sys.argv=[str(target),*sys.argv[3:]];started=now();t=time.monotonic();outcome='FAILED'
try:
    runpy.run_path(str(target),run_name='__main__');outcome='COMPLETED'
finally:
    measured=EXT();assert k.QueryInformationJobObject(job,9,ct.byref(measured),ct.sizeof(measured),None)
    write(L/('RESOURCE_'+tag+'.json'),{'worker':str(target),'started_utc':started,'finished_utc':now(),'elapsed_seconds':time.monotonic()-t,'status':outcome,'wall_limit_seconds':900,'memory_limit_bytes':limits.ProcessMemoryLimit,'peak_process_committed_bytes':measured.PeakProcessMemoryUsed,'mechanism':'Windows Job Object PROCESS_MEMORY and KILL_ON_JOB_CLOSE; supervisor subprocess timeout','historical_science_executed':False})
