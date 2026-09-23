"""Paper E preservation and explicit publication inventory; never stages Git."""
from pathlib import Path
import argparse, hashlib, json, subprocess
P=Path(__file__).resolve().parent; REPO=P.parents[1]; WORK=REPO.parent
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return h.hexdigest()
def git(*a):return subprocess.check_output(['git','-C',str(REPO),*a]).decode().strip()
def write(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def outside_status():return '\n'.join(x for x in git('status','--porcelain=v1','-uall').splitlines() if not x[3:].startswith('papers/PAPER_E/'))
def baseline():
    f=P/'.build/preservation_before.json'
    if f.exists():raise SystemExit('Refusing to replace preservation baseline')
    prior=WORK/'research/GPT_proof/historical_z_manifold_v0.1/preservation_before.json'
    paths={Path(x) for x in json.loads(prior.read_text(encoding='utf-8'))['files']}
    paths.add(WORK/'research/GPT_proof/HISTORICAL_Z_MANIFOLD_AND_SIX_GAP_RECONSTRUCTION_v0.1.md')
    paths.update(p for p in (WORK/'research/GPT_proof/historical_z_manifold_v0.1').rglob('*') if p.is_file())
    write(f,{'head':git('rev-parse','HEAD'),'index':git('ls-files','--stage'),'outside_status':outside_status(),
             'files':{str(p):sha(p) for p in sorted(paths)}})
    print('Preservation baseline:',len(paths),'files')
def finalize():
    b=json.loads((P/'.build/preservation_before.json').read_text(encoding='utf-8'))
    bad=[p for p,h in b['files'].items() if not Path(p).is_file() or sha(p)!=h]
    unchanged=git('rev-parse','HEAD')==b['head'] and git('ls-files','--stage')==b['index'] and outside_status()==b['outside_status']
    assert not bad and unchanged,(bad,unchanged)
    write(P/'PRESERVATION_RECEIPT.json',{'protected_count':len(b['files']),'mismatches':bad,'head':b['head'],
          'index_and_outside_status_unchanged':unchanged,'outside_untracked_count':sum(x.startswith('?? ') for x in b['outside_status'].splitlines()),
          'protected_sha256':b['files'],'writes':'Paper E directory only; no staging, commit or push'})
    files=sorted(x for x in P.rglob('*') if x.is_file() and '.build' not in x.parts and x.name!='SHA256SUMS.txt')
    names=sorted({str(x.relative_to(REPO)).replace('\\','/') for x in files}|{'papers/PAPER_E/SHA256SUMS.txt','papers/PAPER_E/PROPOSED_GIT_ALLOWLIST.txt'})
    (P/'PROPOSED_GIT_ALLOWLIST.txt').write_text('\n'.join(names)+'\n',encoding='utf-8')
    files=sorted(x for x in P.rglob('*') if x.is_file() and '.build' not in x.parts and x.name!='SHA256SUMS.txt')
    (P/'SHA256SUMS.txt').write_text(''.join(sha(x)+'  '+x.relative_to(P).as_posix()+'\n' for x in files),encoding='utf-8')
    print('Preservation PASS;',len(names),'explicit proposed publication paths')
def verify():
    rows=(P/'SHA256SUMS.txt').read_text().splitlines()
    assert all(sha(P/r.split('  ',1)[1])==r.split('  ',1)[0] for r in rows)
    actual={p.relative_to(REPO).as_posix() for p in P.rglob('*') if p.is_file() and '.build' not in p.parts}
    proposed=set((P/'PROPOSED_GIT_ALLOWLIST.txt').read_text().splitlines())
    assert actual==proposed,(actual-proposed,proposed-actual)
    print('Package PASS:',len(rows),'hashes;',len(actual),'allowlisted files')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['baseline','finalize','verify']);a=p.parse_args()
    globals()[a.mode]()
