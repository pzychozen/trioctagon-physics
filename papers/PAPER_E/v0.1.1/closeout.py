"""Paper E v0.1.1 local preservation/inventory; never stages or changes Git."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;REPO=ROOT.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def git(*a):return subprocess.check_output(['git','-C',str(REPO),*a]).decode().strip()
def public():return sorted(p for p in PARENT.rglob('*') if p.is_file() and '.build' not in p.parts)
def inventory():
    names=sorted({p.relative_to(REPO).as_posix() for p in public()}|{(ROOT/leaf).relative_to(REPO).as_posix() for leaf in ['PROPOSED_PUBLICATION_ALLOWLIST.txt','SHA256SUMS.txt','PRESERVATION_RECEIPT.json','WHITESPACE_REPORT.json']})
    # Before the final receipt exists, provisional inventory includes only actual files.
    return names
def proposal():
    names=sorted({p.relative_to(REPO).as_posix() for p in public()}|{(ROOT/'PROPOSED_PUBLICATION_ALLOWLIST.txt').relative_to(REPO).as_posix()})
    (ROOT/'PROPOSED_PUBLICATION_ALLOWLIST.txt').write_text('\n'.join(names)+'\n')
    print('Provisional actual-file allowlist:',len(names))
def whitespace():
    empty=ROOT/'.build/empty';empty.write_bytes(b'');findings=[]
    text_ext={'.md','.py','.json','.txt','.tex','.bib','.svg','.log'}
    for p in public():
        if p.suffix not in text_ext:continue
        args=['git','-c','core.autocrlf=false','-c','core.whitespace=cr-at-eol','diff','--no-index','--check','--',str(empty),str(p)]
        r=subprocess.run(args,capture_output=True)
        assert not r.stderr,(p,r.stderr.decode(errors='replace'))
        output=r.stdout.decode(errors='replace')
        if output:
            preserved=not p.is_relative_to(ROOT) or 'gpt_review' in p.parts
            rawlog=p.suffix=='.log'
            item={'path':p.relative_to(REPO).as_posix(),'returncode':r.returncode,'classification':'preserved evidence' if preserved else 'raw generated build log' if rawlog else 'new authored administrative content','diagnostics':output}
            findings.append(item)
            assert preserved or rawlog,('New authored whitespace must be corrected',item)
        else:assert r.returncode in [0,1],(p,r.returncode)
    write(ROOT/'WHITESPACE_REPORT.json',{'attribution':'Read-only CRLF-aware Git no-index whitespace inspection; no index writes',
      'findings':findings,'paths_with_findings':len(findings),'new_authored_administrative_files':'PASS',
      'exception_authorized':False,'disposition':'Preserved historical/review/figure/log bytes retain these findings. No blanket or publication exception is assumed.'})
    return len(findings)
def finalize():
    b=json.loads((ROOT/'.build/preservation_before.json').read_text())
    allowed=set(b['append_only_records']);changed=[];unchanged=[]
    for path,h in b['files'].items():
        p=Path(path);now=sha(p)
        if path in allowed:
            old=(ROOT/'.build'/p.name).read_bytes();new=p.read_bytes()
            assert hashlib.sha256(old).hexdigest()==h and new.startswith(old) and len(new)>len(old),path
            changed.append({'path':path,'before_sha256':h,'after_sha256':now,'original_prefix_bytes':len(old),'appended_bytes':len(new)-len(old),'prefix_preserved':True})
        else:
            assert now==h,path;unchanged.append(path)
    head=git('rev-parse','HEAD');index=git('ls-files','--stage')
    outside='\n'.join(x for x in git('status','--porcelain=v1','-uall').splitlines() if not x[3:].startswith('papers/PAPER_E/v0.1.1/'))
    assert head==b['head'] and index==b['index'] and outside==b['outside_status']
    ws=whitespace()
    write(ROOT/'PRESERVATION_RECEIPT.json',{'baseline_count':len(b['files']),'byte_unchanged_count':len(unchanged),'authorized_append_only_count':len(changed),
      'append_only_records':changed,'before_sha256':b['files'],'reviewed_predecessor_paths':90,'all_predecessor_bytes_preserved':True,
      'head_before':b['head'],'head_after':head,'index_unchanged':True,'outside_revision_status_unchanged':True,
      'tracked_status':git('status','--porcelain=v1','-uno') or 'clean','staged_paths':git('diff','--cached','--name-only').splitlines(),
      'whitespace_paths_with_findings':ws,'publication_exception_assumed':False,'git_mutations':'none; no staging, commit, push, fetch, tag or release'})
    names=inventory();(ROOT/'PROPOSED_PUBLICATION_ALLOWLIST.txt').write_text('\n'.join(names)+'\n')
    manifest=ROOT/'SHA256SUMS.txt'
    manifest.write_text(''.join(sha(REPO/n)+'  '+n+'\n' for n in names if REPO/n!=manifest))
    print('Preservation PASS:',len(unchanged),'unchanged;',len(changed),'prefix-preserving appends;',len(names),'proposed paths')
def verify():
    names=(ROOT/'PROPOSED_PUBLICATION_ALLOWLIST.txt').read_text().splitlines()
    assert len(names)==len(set(names)) and set(names)=={p.relative_to(REPO).as_posix() for p in public()}
    rows=(ROOT/'SHA256SUMS.txt').read_text().splitlines()
    assert len(rows)==len(names)-1
    for row in rows:
        h,n=row.split('  ',1);assert sha(REPO/n)==h,n
    print('Combined package PASS:',len(rows),'hashes;',len(names),'explicit paths')

def verify_copy():
    verify()
    target=ROOT/'.build/minimal_copy/repo'
    assert target.is_dir(),'The bounded build copy must already exist'
    names=(ROOT/'PROPOSED_PUBLICATION_ALLOWLIST.txt').read_text().splitlines()
    for name in names:
        source=REPO/name;destination=target/name
        assert source.resolve().is_relative_to(PARENT.resolve())
        assert destination.resolve().is_relative_to(target.resolve())
        destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,destination)
        assert sha(source)==sha(destination),name
    manifest=ROOT/'SHA256SUMS.txt'
    rows=manifest.read_text().splitlines()
    for row in rows:
        digest,name=row.split('  ',1)
        assert sha(target/name)==digest,name
    write(ROOT/'.build/minimal_copy_final_receipt.json',{
      'attribution':'Codex final inventory reconciliation after the recorded minimal-copy build',
      'copied_paths':len(names),'verified_manifest_entries':len(rows),
      'manifest_sha256':sha(manifest),'allowlist_sha256':sha(ROOT/'PROPOSED_PUBLICATION_ALLOWLIST.txt'),
      'all_copied_bytes_equal_canonical':True,
      'scope':'Copy final metadata and restore canonical preserved assets within the existing disposable build tree; no additional build, science execution or source edit'})
    print('Final minimal-copy inventory PASS:',len(names),'paths;',len(rows),'manifest hashes')

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('mode',choices=['proposal','finalize','verify','verify_copy']);globals()[a.parse_args().mode]()
