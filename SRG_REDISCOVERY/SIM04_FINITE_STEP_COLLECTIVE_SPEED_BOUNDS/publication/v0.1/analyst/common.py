"""File-only SIM04 input preparation and protected-state accounting."""
from pathlib import Path,PurePosixPath
import os,sys,json,hashlib,zipfile,subprocess,datetime,csv,io,time
ROOT=Path(__file__).resolve().parent.parent
REPO=ROOT.parent.parent
SOURCE_REL='SRG_REDISCOVERY/SIM03_DRIVING_GEOMETRY_AND_RESPONSE_ALIGNMENT/publication/v0.1'
SOURCE=REPO/SOURCE_REL
CHECKPOINT='e1f5115402a05965834493c1254b03118a531c92'
CAP=268435456
os.environ.update(PYTHONDONTWRITEBYTECODE='1',GIT_OPTIONAL_LOCKS='0',MPLBACKEND='Agg',
    MPLCONFIGDIR=str(ROOT/'cache/matplotlib'),TEMP=str(ROOT/'tmp'),TMP=str(ROOT/'tmp'),
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
def size():
    return sum(p.stat().st_size for p in lp(ROOT).rglob('*') if p.is_file())
def cap():
    n=size();need(n<CAP,'aggregate file cap exceeded');return n
def git(*args):return subprocess.check_output(['git','--no-optional-locks',*args],cwd=REPO,stderr=subprocess.PIPE)
def baseline():
    changes=sorted(x.decode() for x in git('diff','--name-only','-z','HEAD').split(b'\0') if x)
    idx=Path(git('rev-parse','--git-path','index').decode().strip())
    if not idx.is_absolute():idx=REPO/idx
    attrs=[x.decode() for x in git('ls-files','-z','--','**/.gitattributes','.gitattributes').split(b'\0') if x]
    return {'HEAD':git('rev-parse','HEAD').decode().strip(),'branch':git('branch','--show-current').decode().strip(),
        'tracked_status':git('status','--porcelain=v1','--untracked-files=no').decode(),
        'staged':git('diff','--cached','--name-status').decode(),'git_index':ident(idx),
        'index_entries':identbytes(git('ls-files','--stage','-z')),
        'modified_tracked':{n:ident(REPO/n) for n in changes},
        'research_index':ident(REPO/'SRG_REDISCOVERY/README.md'),'license_scope':ident(REPO/'LICENSE_SCOPE.md'),
        'gitattributes':identbytes(git('ls-files','--stage','--','**/.gitattributes','.gitattributes')),
        'attribute_file_bytes':{n:ident(REPO/n) for n in attrs}}
def safe(z):
    names=z.namelist()
    need(len(names)==len(set(names))==len(set(n.casefold() for n in names)),'ZIP duplicate/case paths')
    need(all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and ':' not in n and '\\' not in n for n in names),'ZIP path safety')
    need(all(((i.external_attr>>16)&0o170000)!=0o120000 for i in z.infolist()),'ZIP symlink')
    need(z.testzip() is None,'ZIP CRC')
    return names
def preserved():
    need(baseline()==load(ROOT/'evidence/BASELINE_BEFORE.json'),'protected repository baseline changed')
    mp=load(ROOT/'evidence/INPUT_MAP.json')['files']
    for n,x in mp.items():
        expected={k:x[k] for k in ('bytes','sha256')}
        need(ident(SOURCE/n)==expected,'original selected source changed '+n)
        need(ident(ROOT/'inputs'/n)==expected,'copied input changed '+n)
    return {'selected_originals':len(mp),'input_copies':len(mp),'protected_baseline':'UNCHANGED'}
def write_csv(path,rows):
    need(rows,'empty CSV');p=lp(path);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def prepare():
    need(not any(lp(ROOT).glob('*STARTED*')) and not lp(ROOT/'analysis').exists(),'prior scientific start/output exists')
    need(not lp(ROOT/'evidence/INPUT_GATE.json').exists(),'inputs already prepared')
    b=baseline();need(b['HEAD']==CHECKPOINT and b['branch']=='main' and not b['staged'],'unexpected checkout baseline')
    previous=REPO/'SRG_REDISCOVERY/SIM03_DRIVING_GEOMETRY_AND_RESPONSE_ALIGNMENT/PAPER_PUBLICATION_PREPARATION_v0.1/R01_R02_REVISION/PUBLICATION_CLOSEOUT/FINAL_PRESERVATION.json'
    prev=load(previous)['baseline_after']
    need(all(b[k]==v for k,v in prev.items()),'baseline differs from closed SIM03')
    handoff=Path(r'C:\Users\Notandi\Downloads\SRG_SIM04_CODEX_HANDOFF_v0.1_20261014.zip')
    with zipfile.ZipFile(handoff) as z:
        names=safe(z);m=json.loads(z.read('HANDOFF_MANIFEST.json'))
        need(set(names)==set(m['files'])|{'HANDOFF_MANIFEST.json'},'handoff coverage')
        for n,x in m['files'].items():need(identbytes(z.read(n))==x,'handoff hash '+n)
        for n in names:put(ROOT/'received'/n,z.read(n))
    put(ROOT/'received'/handoff.name,read(handoff))
    ids=load(ROOT/'received/SIM04_INPUT_IDENTITIES_AND_SCHEMAS.json')
    pub=load(SOURCE/'PUBLICATION_MANIFEST.json');need(len(ids['files'])==13,'input count')
    for n,x in ids['files'].items():
        source=SOURCE/n;raw=read(source)
        need(identbytes(raw)=={k:x[k] for k in ('bytes','sha256')},'selected source identity '+n)
        oid=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        need(oid==x['git_blob_sha1'],'raw Git identity '+n)
        need(git('rev-parse',CHECKPOINT+':'+x['repository_path']).decode().strip()==oid,'committed input identity '+n)
        if n!='PUBLICATION_MANIFEST.json':
            need({k:pub['files'][n][k] for k in ('bytes','sha256')}==identbytes(raw),'published inventory '+n)
        put(ROOT/'inputs'/n,raw)
    import numpy as np
    headers={}
    with zipfile.ZipFile(lp(ROOT/'inputs/analysis/center_decomposition.npz')) as z:
        for n in z.namelist():
            with z.open(n) as f:
                ver=np.lib.format.read_magic(f)
                need(ver in ((1,0),(2,0)),'unsupported NPY header version')
                reader=np.lib.format.read_array_header_1_0 if ver==(1,0) else np.lib.format.read_array_header_2_0
                shape,fortran,dtype=reader(f)
                need(not dtype.hasobject,'pickle/object field')
                headers[n[:-4]]={'shape':list(shape),'dtype':str(dtype)}
    need(headers==ids['npz_field_schema'],'NPZ header schema mismatch')
    for n,header in ids['reference_csv_headers'].items():
        actual=next(csv.reader(io.StringIO(read(ROOT/'inputs'/n).decode())))
        need(actual==header,'CSV header schema mismatch '+n)
    for n in ('tmp','cache/matplotlib','evidence','analysis','plots'):(ROOT/n).mkdir(parents=True,exist_ok=True)
    save(ROOT/'evidence/BASELINE_BEFORE.json',b)
    save(ROOT/'evidence/INPUT_MAP.json',ids)
    save(ROOT/'evidence/INPUT_GATE.json',{'status':'PASS','utc':utc(),'handoff':ident(handoff),
        'handoff_members':len(names),'selected_files':13,'committed_input_blobs':'MATCH',
        'NPZ_fields_header_only':len(headers),'outcome_array_values_loaded':False,
        'numpy_version':np.__version__,'python':sys.version,'protected_modified_files':len(b['modified_tracked']),
        'file_bytes':cap()})
    print(json.dumps({'status':'PASS','input_files':13,'NPZ_headers':len(headers),'protected_modified_files':len(b['modified_tracked']),'bytes':size()}))
if __name__=='__main__':prepare()
