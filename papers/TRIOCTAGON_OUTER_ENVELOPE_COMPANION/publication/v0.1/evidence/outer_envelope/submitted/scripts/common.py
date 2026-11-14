from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,sys,subprocess
R=Path(__file__).resolve().parents[1];P=R/'packet';S=R/'sources';D=R/'data';L=R/'logs'
REPO=Path(r'C:\TORMENT\TRIOCTAGON_new\trioctagon-physics')
CHECKPOINT='46bf10808b8694476b61b359be305a66a46d4614'
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment' and not sys.flags.optimize
for p in [D,L]:p.mkdir(exist_ok=True)
def now():return datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,obj):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def run(cmd,tag,cwd=R,timeout=900,check=True):
    start=now();q=subprocess.run(list(map(str,cmd)),cwd=cwd,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'},capture_output=True,timeout=timeout)
    (L/(tag+'.stdout')).write_bytes(q.stdout);(L/(tag+'.stderr')).write_bytes(q.stderr)
    with (L/'EXECUTIONS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'command':list(map(str,cmd)),'cwd':str(cwd),'started_utc':start,'finished_utc':now(),'exit_status':q.returncode,'stdout':tag+'.stdout','stderr':tag+'.stderr'})+'\n')
    if check and q.returncode:raise RuntimeError(tag+': '+q.stderr.decode(errors='replace')[:3000])
    return q
def git(args,tag):return run(['git','--no-optional-locks','-C',REPO,*args],tag,timeout=120)
