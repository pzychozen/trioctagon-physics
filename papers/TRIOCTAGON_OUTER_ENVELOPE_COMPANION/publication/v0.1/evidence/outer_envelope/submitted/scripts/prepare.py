from common import *
import zipfile,platform,importlib.metadata
from pathlib import PurePosixPath
src=Path(r'C:\Users\Notandi\Downloads\TRIOCTAGON_OUTER_ENVELOPE_01_CODEX_PACKET.zip')
assert not P.exists()
with zipfile.ZipFile(src) as z:
    names=z.namelist();assert len(names)==len(set(names))==len({n.casefold() for n in names}) and z.testzip() is None
    for n in names:
        p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts and ':' not in n and '\\' not in n
    z.extractall(P)
run([sys.executable,'-B',P/'tools/verify_packet.py'],'packet_integrity')
snap={}
for key,args in [('head',['rev-parse','HEAD']),('branch',['symbolic-ref','--short','HEAD']),('origin',['remote','get-url','origin']),('status',['status','--porcelain=v1','-uno']),('staged',['diff','--cached','--binary']),('unstaged',['diff','--binary'])]:
    b=git(args,'private_before_'+key).stdout;snap[key]={'bytes':len(b),'sha256':sha(b)}
    if key in ['head','branch','origin']:snap[key]['value']=b.decode().strip()
index=Path(git(['rev-parse','--git-path','index'],'private_index_path').stdout.decode().strip());index=index if index.is_absolute() else REPO/index
snap['index_path']=str(index);snap['index_sha256']=sha(index.read_bytes())
tracked=git(['ls-files','-z'],'private_tracked_paths').stdout.decode().split('\0')
snap['tracked_files']={p:sha((REPO/p).read_bytes()) for p in tracked if p and (REPO/p).is_file()}
write(R/'private_operator_before.json',snap)
write(D/'INPUT_VERIFICATION.json',{'status':'PASS','checked_utc':now(),'packet_bytes':src.stat().st_size,'packet_sha256':sha(src.read_bytes()),'packet_members':len(names),'manifest_entries':len(read(P/'PACKET_MANIFEST.json')['files']),'repository_head':snap['head']['value'],'reading_checkpoint':CHECKPOINT,'repository_read_only':True})
versions={}
for name in ['sympy','numpy','scipy','mpmath','psutil']:
    try:versions[name]=importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:versions[name]=None
write(D/'ENVIRONMENT.json',{'observed_utc':now(),'platform':platform.platform(),'python':sys.version,'executable':sys.executable,'conda':'torment','libraries':versions,'new_dependencies_installed':False})
run([sys.executable,'-B',P/'tools/collect_sources.py','--repo',REPO,'--out',S,'--include-optional'],'source_collection')
print('PASS packet and sources; environment',versions)
