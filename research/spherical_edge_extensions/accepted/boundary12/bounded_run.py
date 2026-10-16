"""Run one new research script with a Windows 2 GiB process-memory job and 900 s wall limit."""
from pathlib import Path
import ctypes,ctypes.wintypes as W,json,os,subprocess,sys,time,datetime,shutil
O=Path(__file__).resolve().parent
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
class Basic(ctypes.Structure):
 _fields_=[('PerProcessUserTimeLimit',ctypes.c_longlong),('PerJobUserTimeLimit',ctypes.c_longlong),('LimitFlags',W.DWORD),('MinimumWorkingSetSize',ctypes.c_size_t),('MaximumWorkingSetSize',ctypes.c_size_t),('ActiveProcessLimit',W.DWORD),('Affinity',ctypes.c_size_t),('PriorityClass',W.DWORD),('SchedulingClass',W.DWORD)]
class IO(ctypes.Structure):_fields_=[(x,ctypes.c_ulonglong) for x in ['ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount']]
class Ext(ctypes.Structure):_fields_=[('BasicLimitInformation',Basic),('IoInfo',IO),('ProcessMemoryLimit',ctypes.c_size_t),('JobMemoryLimit',ctypes.c_size_t),('PeakProcessMemoryUsed',ctypes.c_size_t),('PeakJobMemoryUsed',ctypes.c_size_t)]
k=ctypes.WinDLL('kernel32',use_last_error=True)
k.CreateJobObjectW.restype=W.HANDLE;k.CreateJobObjectW.argtypes=[ctypes.c_void_p,W.LPCWSTR]
k.SetInformationJobObject.argtypes=[W.HANDLE,ctypes.c_int,ctypes.c_void_p,W.DWORD]
k.AssignProcessToJobObject.argtypes=[W.HANDLE,W.HANDLE]
k.QueryInformationJobObject.argtypes=[W.HANDLE,ctypes.c_int,ctypes.c_void_p,W.DWORD,ctypes.c_void_p]
k.CloseHandle.argtypes=[W.HANDLE]
job=k.CreateJobObjectW(None,None);limits=Ext();limits.BasicLimitInformation.LimitFlags=0x100|0x2000;limits.ProcessMemoryLimit=2147483648
assert job and k.SetInformationJobObject(job,9,ctypes.byref(limits),ctypes.sizeof(limits))
script=Path(sys.argv[1]);assert (O/script).resolve().is_relative_to(O)
start=time.monotonic();beg=datetime.datetime.now(datetime.timezone.utc).isoformat()
logs=O/'evidence/runs';logs.mkdir(parents=True,exist_ok=True)
run_name=script.stem+'_'+str(1+len(list(logs.glob(script.stem+'*.execution.json')))).zfill(2)
with (logs/(run_name+'.stdout.txt')).open('w',encoding='utf-8') as out,(logs/(run_name+'.stderr.txt')).open('w',encoding='utf-8') as err:
 command=[shutil.which('node'),str(script)] if script.suffix=='.cjs' else [sys.executable,'-B',str(script)]
 p=subprocess.Popen([*command,*sys.argv[2:]],cwd=O,stdout=out,stderr=err,env={**os.environ,'PYTHONIOENCODING':'utf-8','PYTHONDONTWRITEBYTECODE':'1'})
 if not k.AssignProcessToJobObject(job,W.HANDLE(int(p._handle))):
  p.terminate();p.wait();raise ctypes.WinError(ctypes.get_last_error())
 timeout=False
 try:code=p.wait(timeout=900)
 except subprocess.TimeoutExpired:timeout=True;p.terminate();code=p.wait()
 stats=Ext();assert k.QueryInformationJobObject(job,9,ctypes.byref(stats),ctypes.sizeof(stats),None)
 k.CloseHandle(job)
record={'script':str(script),'started_utc':beg,'wall_seconds':time.monotonic()-start,'exit_code':code,'timeout':timeout,'wall_limit_seconds':900,'memory_limit_bytes':2147483648,'peak_committed_process_bytes':stats.PeakProcessMemoryUsed,'limit_mechanism':'Windows job object process memory cap; parent wall timeout','python':sys.executable,'conda_environment':os.environ['CONDA_DEFAULT_ENV']}
(logs/(run_name+'.execution.json')).write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2));sys.exit(code)
