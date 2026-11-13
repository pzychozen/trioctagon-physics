from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,os,subprocess,sys
R=Path(__file__).resolve().parents[1]; P=R/'packet'; S=R/'sources'; D=R/'data'; L=R/'logs'
REPO=Path(r'C:\TORMENT\TRIOCTAGON_new\wt-ntc-pub01')
USER=Path(r'C:\TORMENT\TRIOCTAGON_new\trioctagon-physics')
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
assert not sys.flags.optimize
def now():return datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,o):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def run(cmd,tag,cwd=R,check=True):
    env=os.environ.copy();env['GIT_OPTIONAL_LOCKS']='0'
    start=now();r=subprocess.run(list(map(str,cmd)),cwd=cwd,env=env,capture_output=True)
    (L/(tag+'.stdout')).write_bytes(r.stdout);(L/(tag+'.stderr')).write_bytes(r.stderr)
    with (L/'EXECUTIONS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'command':list(map(str,cmd)),'cwd':str(cwd),'started_utc':start,'finished_utc':now(),'exit_status':r.returncode,'stdout':tag+'.stdout','stderr':tag+'.stderr'})+'\n')
    if check and r.returncode:raise RuntimeError(r.stderr.decode(errors='replace')[:2000])
    return r
def git(args,tag,cwd=REPO):return run(['git','-C',str(cwd),*args],tag,cwd)
