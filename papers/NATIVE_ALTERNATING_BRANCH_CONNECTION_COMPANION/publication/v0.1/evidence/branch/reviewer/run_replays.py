import subprocess, sys, json, time
from pathlib import Path
r=Path(__file__).resolve().parent
w=r.parent/'replay_work'
records=[]
for name in ['check_certificate','algebra_checks']:
    start=time.time()
    with (r/(name+'.stdout.txt')).open('w') as out, (r/(name+'.stderr.txt')).open('w') as err:
        p=subprocess.run([sys.executable,'-B','scripts/'+name+'.py'],cwd=w,stdout=out,stderr=err)
    records.append({'command':[sys.executable,'-B','scripts/'+name+'.py'],'cwd':str(w),'exit_code':p.returncode,'elapsed_seconds':time.time()-start})
    (r/'REPLAY_EXECUTION.json').write_text(json.dumps(records,indent=2))
    if p.returncode:break
(r/'REPLAY_DONE.json').write_text(json.dumps({'records':records,'all_passed':len(records)==2 and all(x['exit_code']==0 for x in records)},indent=2))
