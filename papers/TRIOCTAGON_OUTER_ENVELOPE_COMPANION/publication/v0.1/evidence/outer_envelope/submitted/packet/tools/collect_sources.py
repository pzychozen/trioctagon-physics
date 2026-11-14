r"""Read-only local collection of the listed pinned geometry sources.
Usage: python tools\collect_sources.py --repo C:\...\trioctagon-physics --out C:\...\new_inputs
No network, installations, line-ending normalization, or repository writes.
"""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess
from pathlib import Path

def blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',required=True,type=Path)
    parser.add_argument('--out',required=True,type=Path)
    parser.add_argument('--include-optional',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    spec=json.loads((root/'REQUIRED_SOURCES.json').read_text(encoding='utf-8'))
    repo=args.repo.resolve();out=args.out.resolve()
    if not repo.is_dir(): raise SystemExit('Repository directory not found.')
    if out==repo or repo in out.parents: raise SystemExit('Output must be outside the repository.')
    if out.exists(): raise SystemExit('Output must be a new directory; refusing overwrite.')
    out.mkdir(parents=True)
    env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
    records=[];bad=[]
    for item in spec['sources']:
        if not item['mandatory'] and not args.include_optional: continue
        rel=Path(item['path']);source=repo/rel;data=None;mode=None
        if source.is_file():
            raw=source.read_bytes()
            if blob_id(raw)==item['git_blob_sha1']: data=raw;mode='matching_working_file_raw_bytes'
        if data is None:
            try:
                p=subprocess.run(['git','--no-optional-locks','-C',str(repo),'show',spec['reading_commit']+':'+item['path']],capture_output=True,check=False,timeout=45,env=env)
            except (OSError,subprocess.TimeoutExpired) as exc:
                bad.append({'id':item['id'],'path':item['path'],'error':str(exc)});continue
            if p.returncode!=0:
                bad.append({'id':item['id'],'path':item['path'],'error':p.stderr.decode('utf-8',errors='replace')});continue
            data=p.stdout;mode='read_only_git_show'
        actual=blob_id(data)
        if actual!=item['git_blob_sha1']:
            bad.append({'id':item['id'],'path':item['path'],'error':'Git blob identity mismatch','actual':actual});continue
        target=out/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        records.append({'id':item['id'],'path':item['path'],'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob_sha1':actual,'mode':mode})
    receipt={'status':'PASS' if not bad else 'SOURCE_BLOCKED','reading_commit':spec['reading_commit'],'copied':records,'failures':bad,'science_executed':False}
    (out/'SOURCE_COPY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':receipt['status'],'copied':len(records),'failures':len(bad)},indent=2))
    if bad: raise SystemExit(1)
if __name__=='__main__': main()
