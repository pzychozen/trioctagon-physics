"""Bounded baseline-plus-proposal replay; no kernel/science programs or downloads.

Run from a Git checkout with existing Python/pypdf and explicitly declared
PAPER_B/C_PANDOC, PAPER_B/C_TECTONIC and PAPER_B/C_TEX_CACHE prerequisites.
All new files go to this packet's ignored .build or attributed evidence folder.
"""
from pathlib import Path
import datetime,hashlib,json,os,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent;REPO=ROOT.parents[2]
BASE='08c2a79739d540ffe1cab4743284052e2aa7214b'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(s)
record=json.loads((ROOT/'evidence/five_approved_additions.json').read_text())
expected=json.loads((ROOT/'evidence/bounded_verification.json').read_text())
allow=(ROOT/'COMBINED_PUBLICATION_ALLOWLIST.txt').read_text().splitlines()
assert len(allow)==len(set(allow))
deps=[record['baseline_B_source']['path'],record['baseline_C_source']['path']]
deps+=expected['papers']['B']['relative_links_resolve']+expected['papers']['C']['relative_links_resolve']
deps=sorted(set(deps)-set(allow))
assert len(deps)==8, deps
iso=ROOT/'.build'/('isolated_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
iso.mkdir(parents=True,exist_ok=False)
baseline=[]
for name in deps:
    data=subprocess.run(['git','show',BASE+':'+name],cwd=REPO,check=True,capture_output=True).stdout
    write(iso/name,data);baseline.append({'path':name,'sha256':sha(iso/name),'source':'git show '+BASE+':'+name})
proposal=[]
for name in allow:
    p=(REPO/name).resolve();assert p.is_relative_to(REPO) and p.is_file(),name
    write(iso/name,p.read_bytes());proposal.append({'path':name,'sha256':sha(p)})
assert sorted(p.relative_to(iso).as_posix() for p in iso.rglob('*') if p.is_file())==sorted(deps+allow)
env=os.environ.copy()
for key in ['PYTHONPATH','PYTHONHOME','PAPER_B_PYTHON_PATH','PAPER_C_PYTHON_PATH','TEXINPUTS','TEXMFHOME','TEXMFLOCAL']:
    env.pop(key,None)
env['PYTHONNOUSERSITE']='1';env['PYTHONDONTWRITEBYTECODE']='1'
prereqs={}
for name in ['B','C']:
    for suffix in ['PANDOC','TECTONIC','TEX_CACHE']:
        key=f'PAPER_{name}_{suffix}';value=env.get(key)
        assert value and Path(value).exists(),'Provide explicit existing prerequisite '+key
        prereqs[key]={'path':str(Path(value).resolve()),'sha256':sha(Path(value)) if Path(value).is_file() else None}
specs={'B':'papers/PAPER_B/publication/v0.1.2','C':'papers/PAPER_C/publication/v1.0.1'}
results={}
for name,folder in specs.items():
    original=REPO/folder;dest=iso/folder;pdf=next(original.glob('*.pdf')).name
    command=[sys.executable,'-B','-X','utf8',str(dest/'build_publication.py')]
    run=subprocess.run(command,cwd=dest,env=env,capture_output=True)
    write(ROOT/'evidence'/f'isolated_{name}_stdout.txt',run.stdout+run.stderr)
    assert run.returncode==0,(name,run.stdout[-5000:],run.stderr[-5000:])
    assert sha(dest/pdf)==expected['papers'][name]['pdf_sha256'],(name,'PDF bytes differ')
    assert sha(dest/f'paper_{name}_final.tex')==sha(original/f'paper_{name}_final.tex'),(name,'TeX differs')
    results[name]={'PASS':True,'command':command,'cwd':str(dest),'pdf_sha256':sha(dest/pdf),'pages':expected['papers'][name]['pages'],'PDF_byte_identical':True,'TeX_byte_identical':True,'no_science_or_figure_program_run':True}
verify=iso/ROOT.relative_to(REPO)/'verify_revisions.py'
run=subprocess.run([sys.executable,'-B','-X','utf8',str(verify)],cwd=iso,env=env,capture_output=True)
write(ROOT/'evidence/isolated_bounded_stdout.txt',run.stdout+run.stderr)
assert run.returncode==0,run.stderr
local_results=json.loads((verify.parent/'evidence/bounded_verification.json').read_text())
assert local_results==expected
dp=iso/'papers/PAPER_D/v0.1.1/publication/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.pdf'
assert sha(dp)==record['D_approved_sha256']
receipt={'attribution':'New Codex isolated B/C replay; not part of GPT review','status':'PASS','baseline_commit':BASE,'isolated_root':str(iso),
 'baseline_dependency_paths':baseline,'proposed_input_paths_at_build_start':proposal,'proposed_input_count_at_build_start':len(proposal),
 'external_prerequisites':prereqs,'python':sys.version,'python_executable':sys.executable,'system_fonts':'C:/Windows/Fonts; external, unchanged',
 'only_explicit_baseline_and_proposal_files_copied':True,'wider_source_workspace_fallback':False,'only_cached_TeX_resources':True,
 'results':results,'bounded_verifier_results_identical':True,'cross_paper_references_resolve_in_isolated_copy':True,
 'D_approved_sha256':sha(dp),'D_build_executed':False,
 'receipt_timing':'Input identities describe the build-start snapshot. Later final administrative receipts/manifests are synchronized and read-only checked separately; no build input changes are permitted.'}
write(ROOT/'evidence/isolated_reproduction.json',(json.dumps(receipt,indent=2)+'\n').encode())
print(json.dumps({k:v for k,v in receipt.items() if k not in ['proposed_input_paths_at_build_start','external_prerequisites']},indent=2))
