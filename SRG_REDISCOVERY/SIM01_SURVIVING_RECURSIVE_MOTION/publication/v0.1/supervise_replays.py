"""Hard per-run timeout and output budget; no retries or adaptive extension."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time
ROOT=Path(__file__).resolve().parent
ledger=ROOT/'evidence/REPLAY_SUPERVISION.json'
assert not ledger.exists(), 'Replay supervision already began; no automatic retry.'
assert json.loads((ROOT/'evidence/PREFLIGHT_RESULTS.json').read_text())['status']=='PASS'
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
env['MPLCONFIGDIR']=str(ROOT/'cache/matplotlib');env['TMP']=env['TEMP']=str(ROOT/'tmp')
records=[]
def save():ledger.write_text(json.dumps({'limits':{'wall_seconds_per_run':120,'output_bytes_per_run':256*1024*1024},'runs':records},indent=2)+'\n',encoding='utf-8')
save()
for name in 'ABC':
    rec={'source':name,'status':'STARTING','wall_seconds_limit':120,'output_byte_limit':256*1024*1024}
    records.append(rec);save()
    log=ROOT/'evidence'/f'RUN_{name}_CONSOLE.txt'
    start=time.monotonic();reason=None;peak=0
    with log.open('wb') as stdout:
        process=subprocess.Popen([sys.executable,'-B',str(ROOT/'worker_replay.py'),name],cwd=ROOT,
            env=env,stdout=stdout,stderr=subprocess.STDOUT,creationflags=0x08000000 if os.name=='nt' else 0)
        while process.poll() is None:
            elapsed=time.monotonic()-start
            directory=ROOT/'runs'/name
            size=sum(p.stat().st_size for p in directory.rglob('*') if p.is_file())+log.stat().st_size
            peak=max(peak,size)
            if elapsed>=120 or size>256*1024*1024:
                reason='TIMEOUT' if elapsed>=120 else 'OUTPUT_BUDGET_STOP'
                process.kill();process.wait();break
            time.sleep(.05)
    rec.update(status=reason or ('COMPLETE' if process.returncode==0 else 'ERROR_STOP'),
        returncode=process.returncode,elapsed_seconds=time.monotonic()-start,peak_observed_output_bytes=peak)
    result=ROOT/'runs'/name/'RUN_RESULT.json'
    if result.exists():rec['worker']=json.loads(result.read_text())
    save()
    if rec['status']!='COMPLETE':
        print(json.dumps(rec));raise SystemExit('Stopped; no retries or later runs.')
assert sum(r['worker']['completed_updates'] for r in records)==2700
print(json.dumps({'status':'COMPLETE','runs':records,'full_system_updates':2700},indent=2))
