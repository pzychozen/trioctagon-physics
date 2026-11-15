from pathlib import Path
import sys, os, json, hashlib, zipfile, subprocess, platform, concurrent.futures, datetime
ROOT=Path(__file__).resolve().parent
REPO=Path(r'C:\TORMENT\TRIOCTAGON_new\trioctagon-physics')
OUT=ROOT/'review'; OUT.mkdir(exist_ok=True)
(OUT/'records').mkdir(exist_ok=True)
(ROOT/'private').mkdir(exist_ok=True)
def sha(b): return hashlib.sha256(b).hexdigest()
def write(p,obj): p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def git(*args):
    p=subprocess.run(['git','-c','core.longpaths=true','-C',str(REPO),*args],capture_output=True,env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'},check=True)
    if p.stderr: raise RuntimeError(p.stderr.decode(errors='replace'))
    return p.stdout
def record_file(path):
    p=Path(path); b=p.read_bytes(); return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def snapshot(name):
    paths=sorted(set(x.decode('utf-8') for x in git('ls-files','-z','--modified','--others','--exclude-standard').split(b'\0') if x))
    def one(rel):
        p=REPO/rel
        if not p.exists(): return {'path':rel,'missing':True}
        row=record_file(p); row['path']=rel; return row
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: rows=list(pool.map(one,paths))
    state={x:sha(git(*args)) for x,args in {
      'status':('status','--porcelain=v1','-z','--untracked-files=all'),
      'unstaged_diff':('diff','--binary','--no-ext-diff'),
      'staged_diff':('diff','--cached','--binary','--no-ext-diff'),
      'refs':('show-ref',), 'local_config':('config','--local','--list')}.items()}
    state['head']=git('rev-parse','HEAD').decode().strip()
    state['branch']=git('symbolic-ref','--short','HEAD').decode().strip()
    idx=Path(git('rev-parse','--path-format=absolute','--git-path','index').decode().strip())
    state['index_sha256']=sha(idx.read_bytes())
    state['files']=rows
    write(ROOT/'private'/f'{name}.json',state)
    public={k:v for k,v in state.items() if k!='files'}
    public['modified_or_untracked_count']=len(rows)
    public['file_inventory_sha256']=sha(json.dumps(rows,sort_keys=True).encode())
    write(OUT/'records'/f'REPOSITORY_{name.upper()}.json',public)
    print(name,public)
def prepare():
    zpath=Path(r'C:\Users\Notandi\Downloads\NATIVE_RESPONSE_DRIFT_CORRESPONDENCE_01_CODEX_PACKET.zip')
    with zipfile.ZipFile(zpath) as z:
        names=z.namelist(); assert len(names)==len(set(n.casefold() for n in names))
        manifest=json.loads(z.read('PACKET_MANIFEST.json'))
        assert set(names)=={x['path'] for x in manifest['files']}|{'PACKET_MANIFEST.json'}
        for x in manifest['files']:
            b=z.read(x['path']); assert len(b)==x['bytes'] and sha(b)==x['sha256']
            assert (ROOT/'packet'/x['path']).read_bytes()==b
        assert z.testzip() is None
    identities=json.loads((ROOT/'packet/SOURCE_IDENTITIES.json').read_text())
    checked=[]
    for r in identities['records']:
        b=(ROOT/'packet'/r['path']).read_bytes()
        assert len(b)==r['bytes'] and sha(b)==r['sha256']
        assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['git_blob_sha1_of_preserved_bytes']
        row={'packet_path':r['path'],'sha256':sha(b),'bytes':len(b),'packet_identity_match':True}
        if r['repository_path']:
            obj=git('show',f"ae2c02c80c49dfcf266d3b27ebd21be76a938de1:{r['repository_path']}")
            row['checkpoint_blob_match']=obj==b; assert obj==b
        checked.append(row)
    (OUT/'incoming').mkdir(exist_ok=True)
    (OUT/'incoming'/zpath.name).write_bytes(zpath.read_bytes())
    side=zpath.with_name(zpath.name+'.sha256')
    if side.exists():
        assert sha(zpath.read_bytes()) in side.read_text().lower()
        (OUT/'incoming'/side.name).write_bytes(side.read_bytes())
    import sympy
    write(OUT/'records/ENVIRONMENT.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'executable':sys.executable,'platform':platform.platform(),'sympy':sympy.__version__,'conda_prefix':os.environ.get('CONDA_PREFIX'),'command':'run_python.cmd audit.py prepare','no_install':True})
    write(OUT/'records/INPUT_VERIFICATION.json',{'status':'PASS','archive':record_file(zpath),'members':len(names),'manifest_entries':len(manifest['files']),'sources':checked,'remote_requests':0,'identity_scope':'Packet member bytes and local Git object at specified checkpoint; not fresh remote verification.'})
    print('Input verified:',len(names),'members;',len(checked),'sources')
if __name__=='__main__':
    if sys.argv[1]=='prepare': prepare()
    else: snapshot(sys.argv[1])
