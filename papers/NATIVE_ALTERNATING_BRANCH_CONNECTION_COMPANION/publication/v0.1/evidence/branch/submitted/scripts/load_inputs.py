from common import *
import importlib.util,importlib.metadata,shutil,platform
manifest=read(P/'PACKET_MANIFEST.json')
print('manifest type/keys',type(manifest).__name__,list(manifest) if isinstance(manifest,dict) else len(manifest))
for row in manifest['files']:
    b=(P/row['path']).read_bytes();assert sha(b)==row['sha256']
    if 'bytes' in row:assert len(b)==row['bytes']
rows=[];required=read(P/'REQUIRED_LOCAL_INPUTS.json')
for row in required['files']:
    origin=REPO/row['path'];b=origin.read_bytes();h=sha(b)
    if 'sha256' in row:assert h==row['sha256'],str(origin)
    if 'bytes' in row:assert len(b)==row['bytes']
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if 'git_blob' in row:assert blob==row['git_blob']
    commitbytes=git(['show',required['reading_checkpoint']+':'+row['path']],'source_'+origin.stem).stdout
    assert commitbytes==b
    target=S/origin.name;target.write_bytes(b)
    rows.append(dict(row,actual_origin=str(origin),copied_path=target.relative_to(R).as_posix(),bytes=len(b),sha256=h,git_blob=blob,checkpoint_bytes_equal=True))
for relative in ['papers/PAPER_G/v0.1.1/CLAIM_SOURCE_MAP.md','papers/PAPER_G/v0.1.1/reproducibility/README.md','papers/PAPER_G/README.md']:
    b=(REPO/relative).read_bytes();name={'papers/PAPER_G/README.md':'PAPER_G_README.md','papers/PAPER_G/v0.1.1/reproducibility/README.md':'SUPPLEMENT_README.md'}.get(relative,Path(relative).name)
    (S/name).write_bytes(b);rows.append({'path':relative,'actual_origin':str(REPO/relative),'copied_path':(S/name).relative_to(R).as_posix(),'bytes':len(b),'sha256':sha(b)})
deps={}
for name in ['numpy','scipy','mpmath','sympy','flint','gmpy2']:
    spec=importlib.util.find_spec(name)
    if spec:
        module=__import__(name);deps[name]={'available':True,'version':getattr(module,'__version__','unknown'),'origin':spec.origin}
    else:deps[name]={'available':False}
write(L/'ENVIRONMENT.json',{'observed_utc':now(),'conda':os.environ['CONDA_DEFAULT_ENV'],'python':sys.version,'executable':sys.executable,'platform':platform.platform(),'dependencies':deps,'installed_new_dependencies':False})
snap={}
for key,args in [('head',['rev-parse','HEAD']),('branch',['symbolic-ref','--short','HEAD']),('status',['status','--porcelain=v1','-uall']),('staged',['diff','--cached','--binary']),('unstaged',['diff','--binary'])]:snap[key]=git(args,'operator_before_'+key,USER).stdout.decode(errors='replace')
index=Path(git(['rev-parse','--git-path','index'],'operator_index',USER).stdout.decode().strip())
if not index.is_absolute():index=USER/index
snap['index_path']=str(index);snap['index_sha256']=sha(index.read_bytes())
write(L/'OPERATOR_BEFORE.json',snap)
write(L/'INPUT_IDENTITIES.json',{'status':'PASS','checked_utc':now(),'packet_sha256':sha((R/'received/NATIVE_ALTERNATING_BRANCH_CONNECTION_01_CODEX_PACKET.zip').read_bytes()),'packet_manifest_entries':len(manifest['files']),'required_files_authenticated':5,'reading_checkpoint':required['reading_checkpoint'],'files':rows})
print(json.dumps({'status':'PASS','inputs':[(x['copied_path'],x['sha256']) for x in rows],'dependencies':deps},indent=2))
