from common import *
import time
target,tag=sys.argv[1:3];cmd=[sys.executable,'-B',R/'scripts/worker_bootstrap.py',R/'scripts'/target,tag,*sys.argv[3:]]
try:
    q=run(cmd,tag,timeout=900,check=False);print(q.stdout.decode(errors='replace'));print(q.stderr.decode(errors='replace'),file=sys.stderr);sys.exit(q.returncode)
except subprocess.TimeoutExpired as e:
    (L/(tag+'.stdout')).write_bytes(e.stdout or b'');(L/(tag+'.stderr')).write_bytes(e.stderr or b'')
    write(L/('TIMEOUT_'+tag+'.json'),{'status':'TIMEOUT','command':list(map(str,cmd)),'recorded_utc':now(),'wall_limit_seconds':900});raise
