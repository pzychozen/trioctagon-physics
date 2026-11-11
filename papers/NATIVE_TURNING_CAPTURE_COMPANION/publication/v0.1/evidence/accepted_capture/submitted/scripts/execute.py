"""Measure actual execution, independent of scientific correctness."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys
R=Path(__file__).resolve().parents[1]
assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'
target=R/sys.argv[1]; assert target.is_relative_to(R/'scripts')
tag=target.stem+('_'+sys.argv[2] if len(sys.argv)>2 else '')
cmd=[sys.executable,'-B',str(target),*sys.argv[2:]];start=datetime.now(timezone.utc).isoformat()
with (R/'logs'/f'{tag}.stdout.txt').open('wb') as out,(R/'logs'/f'{tag}.stderr.txt').open('wb') as err:result=subprocess.run(cmd,cwd=R,stdout=out,stderr=err)
record={'command':cmd,'cwd':str(R),'started_utc':start,'finished_utc':datetime.now(timezone.utc).isoformat(),'exit_status':result.returncode,'conda_environment':os.environ.get('CONDA_DEFAULT_ENV'),'script_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'stdout':f'logs/{tag}.stdout.txt','stderr':f'logs/{tag}.stderr.txt'}
with (R/'logs/EXECUTION_RECORDS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(record)+'\n')
print(json.dumps(record,indent=2));raise SystemExit(result.returncode)
