"""SIM05 file operations and bounded preservation; no historical entry-point imports."""
from pathlib import Path,PurePosixPath
import os,sys,json,hashlib,zipfile,subprocess,datetime,csv,io,time,math
ROOT=Path(__file__).resolve().parent.parent
REPO=ROOT.parent.parent
SOURCE=ROOT.parent/'SIM04_FINITE_STEP_COLLECTIVE_SPEED_BOUNDS'
CAP=268435456
os.environ.update(PYTHONDONTWRITEBYTECODE='1',GIT_OPTIONAL_LOCKS='0',MPLBACKEND='Agg',
 MPLCONFIGDIR=str(ROOT/'cache'),TEMP=str(ROOT/'tmp'),TMP=str(ROOT/'tmp'),
 OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
def lp(p):
 s=str(p);return Path(s) if s.startswith('\\\\?\\') else Path('\\\\?\\'+str(Path(p).resolve()))
def read(p):return lp(p).read_bytes()
def identbytes(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def ident(p):return identbytes(read(p))
def need(x,m):
 if not x:raise AssertionError(m)
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(p):return json.loads(read(p))
def put(p,b):
 p=lp(p);p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('xb') as f:f.write(b.encode('utf-8') if isinstance(b,str) else b)
def save(p,x):put(p,json.dumps(x,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def update(p,x):lp(p).write_text(json.dumps(x,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8',newline='\n')
def size():return sum(p.stat().st_size for p in lp(ROOT).rglob('*') if p.is_file())
def cap():
 n=size();need(n<CAP,'aggregate cap exceeded');return n
def git(*args):return subprocess.check_output(['git','--no-optional-locks',*args],cwd=REPO,stderr=subprocess.PIPE)
def baseline():
 changes=sorted(x.decode() for x in git('diff','--name-only','-z','HEAD').split(b'\0') if x)
 idx=Path(git('rev-parse','--git-path','index').decode().strip())
 if not idx.is_absolute():idx=REPO/idx
 attrs=[x.decode() for x in git('ls-files','-z','--','**/.gitattributes','.gitattributes').split(b'\0') if x]
 return {'HEAD':git('rev-parse','HEAD').decode().strip(),'branch':git('branch','--show-current').decode().strip(),
 'tracked_status':git('status','--porcelain=v1','--untracked-files=no').decode(),'staged':git('diff','--cached','--name-status').decode(),
 'git_index':ident(idx),'index_entries':identbytes(git('ls-files','--stage','-z')),
 'modified_tracked':{n:ident(REPO/n) for n in changes},'research_index':ident(REPO/'SRG_REDISCOVERY/README.md'),
 'license_scope':ident(REPO/'LICENSE_SCOPE.md'),'gitattributes':identbytes(git('ls-files','--stage','--','**/.gitattributes','.gitattributes')),
 'attribute_file_bytes':{n:ident(REPO/n) for n in attrs}}
def safe(z):
 names=z.namelist();need(len(names)==len(set(names))==len(set(n.casefold() for n in names)),'ZIP duplicate/case collision')
 need(all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and ':' not in n and '\\' not in n for n in names),'ZIP unsafe path')
 need(all(((i.external_attr>>16)&0o170000)!=0o120000 for i in z.infolist()),'ZIP symlink');need(z.testzip() is None,'ZIP CRC')
 return names
def preserved():
 need(baseline()==load(ROOT/'evidence/BASELINE_BEFORE.json'),'protected baseline changed')
 p=load(ROOT/'evidence/PRESERVATION_INPUTS.json')
 for n,v in p['SIM04_files'].items():need(ident(SOURCE/n)==v,'accepted SIM04 changed '+n)
 for n,v in p['local_copies'].items():need(ident(ROOT/n)==v,'immutable input/review changed '+n)
 return {'status':'UNCHANGED','SIM04_files':len(p['SIM04_files']),'input_review_copies':len(p['local_copies']),'repository_baseline':'UNCHANGED'}
def write_csv(path,rows):
 need(rows,'empty CSV');p=lp(path);p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def npzsave(path,arrays):
 import numpy as np
 with lp(path).open('xb') as f:np.savez_compressed(f,**arrays)

